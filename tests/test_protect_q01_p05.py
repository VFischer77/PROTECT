import unittest
from protect_q01_p01.integration import Workspace
from protect_q01_p01.capa_analytics import CapaRecord
from protect_q01_p01.operational_intelligence import management_snapshot

class P05Tests(unittest.TestCase):
    def setUp(self):
        self.w=Workspace("Pharmaceuticals","GMP/Quality")
        self.d=[{"id":"D1","occurred_on":"2026-01-02","failure_mechanism":"Seal"},
                {"id":"D2","occurred_on":"2026-03-02","failure_mechanism":"seal"}]
        self.c=[CapaRecord("C1","2026-01-03","2026-02-01","2026-02-15","Effective",("D1","D2"))]
    def test_descriptive_snapshot(self):
        r=management_snapshot(self.w,self.d,self.c)
        self.assertEqual(r["deviation_monthly_counts"],{"2026-01":1,"2026-03":1})
        self.assertEqual(r["client_capa_outcome_counts"]["Effective"],1)
    def test_review_queue(self):
        r=management_snapshot(self.w,self.d,self.c)
        self.assertEqual({i["type"] for i in r["review_queue"]},{"RECURRENCE_HYPOTHESIS","POST_VERIFICATION_EVENT"})
        self.assertTrue(all(i["status"]=="HUMAN_REVIEW_REQUIRED" for i in r["review_queue"]))
    def test_no_prediction(self):
        r=management_snapshot(self.w,self.d,self.c)
        self.assertEqual(r["risk_score"],"NOT_CALCULATED")
        self.assertEqual(r["predictive_thresholds"],"NOT_APPROVED")
        self.assertEqual(r["classification"],"NOT_ASSIGNED")
    def test_empty(self):
        r=management_snapshot(self.w,[],[])
        self.assertEqual(r["review_queue"],())
        self.assertEqual(r["deviation_record_count"],0)
    def test_invalid_references_rejected(self):
        with self.assertRaises(ValueError):
            management_snapshot(self.w,self.d,[CapaRecord("C1","2026-01-03",linked_deviation_ids=("UNKNOWN",))])
if __name__=="__main__": unittest.main()
