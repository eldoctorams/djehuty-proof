import unittest
from djehuty_proof import audit_report

class EngineTests(unittest.TestCase):
    def test_exact_evidence(self):
        result=audit_report("The detector processed 500 events successfully.",{"run.txt":"The detector processed 500 events successfully."})
        self.assertEqual(result["coverage"],1)
        self.assertTrue(result["claims"][0]["evidence"]["sha256"])
    def test_unsupported(self):
        result=audit_report("The system achieved perfect accuracy.",{"notes.txt":"The system was evaluated on a small sample."})
        self.assertEqual(result["claims"][0]["verdict"],"insufficient")
    def test_human_review(self):
        self.assertTrue(audit_report("Three controls were tested.",{})["policy"]["human_review_required"])

if __name__=="__main__": unittest.main()
