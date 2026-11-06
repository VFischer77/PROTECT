import unittest
from protect_q01_p01.module_registry import registry
from protect_q01_p01.integrated_dashboard import build_integrated_dashboard
from protect_q01_p01.integration import Workspace
from protect_q01_p01.capa_analytics import CapaRecord

class P054Tests(unittest.TestCase):
    def setUp(self):
        self.w=Workspace("Pharmaceuticals","GMP/Quality")
        self.d=[{"id":"D1","occurred_on":"2026-01-05","failure_mechanism":"Seal"},
                {"id":"D2","occurred_on":"2026-03-05","failure_mechanism":"seal"}]
        self.c=[CapaRecord("C1","2026-01-10","2026-02-01","2026-02-20","Effective",("D1","D2"))]
    def test_registry_unique(self):
        self.assertEqual(len({m.code for m in registry()}),len(registry()))
    def test_only_two_active_modules(self):
        r=build_integrated_dashboard(self.w,self.d,self.c)
        self.assertEqual(r["available_module_count"],2)
        self.assertEqual({m["code"] for m in r["modules"] if m["metrics"] is not None},{"Q01","Q02"})
    def test_unimplemented_modules_are_not_fabricated(self):
        r=build_integrated_dashboard(self.w,self.d,self.c)
        self.assertTrue(all(m["metrics"] is None for m in r["modules"] if m["status"]!="PILOT_DATA_AVAILABLE"))
    def test_existing_q01_q02_evidence(self):
        r=build_integrated_dashboard(self.w,self.d,self.c)
        self.assertEqual(len(r["cross_module_signals"]),2)
        self.assertEqual(r["cross_module_scope"],"Q01_Q02_ONLY")
    def test_human_controls(self):
        r=build_integrated_dashboard(self.w,self.d,self.c)
        self.assertEqual(r["human_decision"],"REQUIRED")
        self.assertEqual(r["kpi_status"],"NOT_APPROVED")
    def test_empty_data(self):
        r=build_integrated_dashboard(self.w,[],[])
        self.assertEqual(r["source_dashboard"]["summary"]["deviation_records"],0)
        self.assertEqual(r["available_module_count"],2)
    def test_q05_unresolved(self):
        self.assertEqual(next(m.status for m in registry() if m.code=="Q05"),"SCOPE_PENDING")
if __name__=="__main__": unittest.main()
