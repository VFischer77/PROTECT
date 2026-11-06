import copy
import unittest
from protect_q01_p01.integration import Workspace
from protect_q01_p01.capa_analytics import CapaRecord
from protect_q01_p01.review_worklist import build_review_worklist

class P051Tests(unittest.TestCase):
    def setUp(self):
        self.w=Workspace("Pharmaceuticals","GMP/Quality")
        self.d=[{"id":"D1","occurred_on":"2026-01-05","failure_mechanism":"Seal issue","source_classification":"Minor"},
                {"id":"D2","occurred_on":"2026-03-05","failure_mechanism":"seal issue","source_classification":"Major"}]
        self.c=[CapaRecord("C1","2026-01-10","2026-02-01","2026-02-20","Effective",("D1","D2"))]
    def test_two_distinct_signals(self):
        r=build_review_worklist(self.w,self.d,self.c)
        self.assertEqual(r["worklist_count"],2)
        self.assertEqual({x["signal_type"] for x in r["worklist"]},{"RECURRENCE_HYPOTHESIS","POST_VERIFICATION_EVENT"})
    def test_preserves_human_gate(self):
        r=build_review_worklist(self.w,self.d,self.c)
        self.assertTrue(all(x["review_status"]=="OPEN_FOR_HUMAN_REVIEW" for x in r["worklist"]))
        self.assertFalse(r["auto_closure"])
        self.assertFalse(r["auto_escalation"])
    def test_no_risk_classification(self):
        r=build_review_worklist(self.w,self.d,self.c)
        self.assertTrue(all(x["risk_level"]=="NOT_ASSIGNED" for x in r["worklist"]))
    def test_source_unchanged(self):
        before=copy.deepcopy(self.d)
        build_review_worklist(self.w,self.d,self.c)
        self.assertEqual(before,self.d)
        self.assertEqual(self.c[0].client_effectiveness,"Effective")
    def test_empty(self):
        r=build_review_worklist(self.w,[],[])
        self.assertEqual(r["worklist"],())
        self.assertEqual(r["worklist_count"],0)
    def test_invalid_link_rejected(self):
        with self.assertRaises(ValueError):
            build_review_worklist(self.w,self.d,[CapaRecord("C1","2026-01-10",linked_deviation_ids=("MISSING",))])
if __name__=="__main__": unittest.main()
