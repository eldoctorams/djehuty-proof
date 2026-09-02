from djehuty_proof import audit_report

def test_links_claim_to_exact_evidence():
    result=audit_report("The detector processed 500 events successfully.",{"run.txt":"The detector processed 500 events successfully."})
    assert result["coverage"]==1
    assert result["claims"][0]["evidence"]["sha256"]

def test_marks_unsupported_claim():
    result=audit_report("The system achieved perfect accuracy.",{"notes.txt":"The system was evaluated on a small sample."})
    assert result["claims"][0]["verdict"]=="insufficient"

def test_requires_human_review():
    assert audit_report("Three controls were tested.",{})["policy"]["human_review_required"] is True
