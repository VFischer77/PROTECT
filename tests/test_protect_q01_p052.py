import copy
import unittest
from protect_q01_p01.integration import Workspace
from protect_q01_p01.capa_analytics import CapaRecord
from protect_q01_p01.dashboard import build_management_dashboard

class P052Tests(unittest.TestCase):
    def setUp(self):
        self.w=Workspace("Pharmaceuticals","GMP/Quality")
        self.d=[{"id":"D1","occurred_on":"2026-01-05","failure_mechanism":"Seal"},
                {"id":"D2","occurred_on":"2026-03-05","failure_mechanism":"seal"}]
        self.c=[CapaRecord("C1","2026-01-10","2026-02-01","2026-02-20","Effective",("D1","D2"))]
    def test_sorted_trend_without_imputation(self):
        r=build_management_dashboard(self.w,self.d,self.c)
        self.assertEqual(r["deviation_trend"],({"period":"2026-01","count":1},{"period":"2026-03","count":1}))
        self.assertEqual(r["missing_periods"],"NOT_IMPUTED")
    def test_capa_outcomes(self):
        r=build_management_dashboard(self.w,self.d,self.c)
        self.assertEqual(r["capa_outcome_distribution"],({"outcome":"Effective","count":1},))
    def test_signal_distribution(self):
        r=build_management_dashboard(self.w,self.d,self.c)
        self.assertEqual(sum(x["count"] for x in r["review_signal_distribution"]),2)
        self.assertEqual(r["summary"]["human_review_items"],2)
    def test_no_unapproved_analytics(self):
        r=build_management_dashboard(self.w,self.d,self.c)
        self.assertEqual(r["kpi_status"],"NOT_APPROVED")
        self.assertEqual(r["risk_prediction"],"NOT_PERFORMED")
        self.assertEqual(r["human_decision"],"REQUIRED")
    def test_empty(self):
        r=build_management_dashboard(self.w,[],[])
        self.assertEqual(r["deviation_trend"],())
        self.assertEqual(r["review_signal_distribution"],())
    def test_no_mutation(self):
        before=copy.deepcopy(self.d)
        build_management_dashboard(self.w,self.d,self.c)
        self.assertEqual(before,self.d)
        self.assertEqual(self.c[0].client_effectiveness,"Effective")
    def test_invalid_links_rejected(self):
        with self.assertRaises(ValueError):
            build_management_dashboard(self.w,self.d,[CapaRecord("C1","2026-01-01",linked_deviation_ids=("UNKNOWN",))])
if __name__=="__main__": unittest.main()
