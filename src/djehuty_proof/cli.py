import argparse,json
from pathlib import Path
from .engine import audit_files

def main()->None:
    parser=argparse.ArgumentParser(prog="djehuty",description="Audit claims against local evidence")
    parser.add_argument("report");parser.add_argument("--sources",required=True);parser.add_argument("--output",default="djehuty-audit.json")
    args=parser.parse_args();result=audit_files(Path(args.report),Path(args.sources));Path(args.output).write_text(json.dumps(result,indent=2),encoding="utf-8");print(json.dumps({"claims":len(result["claims"]),"coverage":result["coverage"]},indent=2))
if __name__=="__main__":main()
