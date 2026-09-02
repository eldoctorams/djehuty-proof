from __future__ import annotations

import hashlib
import re
from pathlib import Path

STOP = {"the","a","an","and","or","of","to","in","on","for","with","is","are","was","were","be","this","that"}
NEGATIONS = {"not","never","no","none","without","false","failed"}

def _tokens(text: str) -> set[str]:
    return {word.lower() for word in re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]+", text) if word.lower() not in STOP and len(word)>2}

def _claims(markdown: str) -> list[str]:
    cleaned = re.sub(r"```.*?```", "", markdown, flags=re.S)
    cleaned = re.sub(r"[#>*_`\[\]()]", " ", cleaned)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+|\n+", cleaned) if len(_tokens(part)) >= 3]

def audit_report(report: str, sources: dict[str, str]) -> dict:
    if not report.strip(): raise ValueError("report cannot be empty")
    evidence_spans=[]
    for source_name,text in sources.items():
        for index,span in enumerate(filter(None,re.split(r"(?<=[.!?])\s+|\n+",text))):
            evidence_spans.append((source_name,index,span.strip(),_tokens(span)))
    rows=[]
    for index,claim in enumerate(_claims(report),1):
        claim_tokens=_tokens(claim)
        ranked=[]
        for source_name,span_index,span,span_tokens in evidence_spans:
            union=claim_tokens|span_tokens
            similarity=len(claim_tokens&span_tokens)/len(union) if union else 0
            ranked.append((similarity,source_name,span_index,span))
        best=max(ranked,default=(0,"",0,""))
        claim_neg=bool(claim_tokens&NEGATIONS); evidence_neg=bool(_tokens(best[3])&NEGATIONS)
        contradiction=best[0]>=.28 and claim_neg!=evidence_neg
        verdict="contradicted" if contradiction else "supported" if best[0]>=.42 else "partial" if best[0]>=.22 else "insufficient"
        claim_id=f"CLM-{index:04d}-{hashlib.sha256(claim.encode()).hexdigest()[:8]}"
        rows.append({"claim_id":claim_id,"claim":claim,"verdict":verdict,"support_score":round(best[0],3),"evidence":{"source":best[1],"span_index":best[2],"text":best[3],"sha256":hashlib.sha256(best[3].encode()).hexdigest() if best[3] else None}})
    supported=sum(row["verdict"]=="supported" for row in rows)
    return {"engine":"DJEHUTY PROOF","version":"0.1.0","report_sha256":hashlib.sha256(report.encode()).hexdigest(),"coverage":round(supported/len(rows),3) if rows else 0,"claims":rows,"policy":{"automatic_truth_verdict":False,"human_review_required":True}}

def audit_files(report_path: Path,sources_dir: Path) -> dict:
    sources={p.name:p.read_text(encoding="utf-8") for p in sorted(sources_dir.glob("*")) if p.is_file()}
    return audit_report(report_path.read_text(encoding="utf-8"),sources)
