import copy
import unittest
from protect_q01_p01.integration import Workspace, CapaReference, LinkedEvent, analyze_workspace

DATA=[{"id":"D1","occurred_on":"2026-01-01","failure_mechanism":"seal"},{"id":"D2","occurred_on":"2026-02-01","failure_mechanism":"Seal"}]
class P02Tests(unittest.TestCase):
    def setUp(self):
        self.w=Workspace("Pharmaceuticals","GMP/Quality")
    def test_one_time_inheritance(self):
        self.assertIs(self.w.module_profile("Q01"),self.w.module_profile("Q02"))
        self.assertEqual(self.w.profile.baseline,"ISO 9001")
    def test_invalid_profile(self):
        with self.assertRaises(ValueError): Workspace("Unknown","GMP/Quality")
    def test_change_control_gate(self):
        with self.assertRaises(PermissionError): self.w.reconfigure("Biotechnology","GMP/Quality")
    def test_q01_integration(self):
        r=analyze_workspace(self.w,DATA)
        self.assertEqual(r["q01"]["monthly_counts"],{"2026-01":1,"2026-02":1})
        self.assertEqual(len(r["q01"]["recurrence_candidates"]),1)
    def test_many_to_many_links(self):
        capas=(CapaReference("C1",("D1","D2"),"Effective"),CapaReference("C2",("D1",),"Pending"))
        r=analyze_workspace(self.w,DATA,capas)
        self.assertEqual(len(r["capa_deviation_links"]),3)
        self.assertEqual(r["q01"]["record_count"],2)
        self.assertEqual(r["q02_capa_references"][1]["client_effectiveness"],"Pending")
    def test_dangling_link_rejected(self):
        with self.assertRaises(ValueError): analyze_workspace(self.w,DATA,(CapaReference("C1",("D9",)),))
    def test_duplicate_link_rejected(self):
        with self.assertRaises(ValueError): analyze_workspace(self.w,DATA,(CapaReference("C1",("D1","D1")),))
    def test_invalid_effectiveness_rejected(self):
        with self.assertRaises(ValueError): analyze_workspace(self.w,DATA,(CapaReference("C1",("D1",),"Closed"),))
    def test_audit_types(self):
        r=analyze_workspace(self.w,DATA,audit_events=(LinkedEvent("A1","Internal Audit","2026-01-02"),LinkedEvent("A2","Authority Inspection","2026-02-03")))
        self.assertEqual(r["audit_event_count"],2)
        self.assertEqual(r["cross_module_causality"],"NOT_ASSESSED")
    def test_unchanged_sources(self):
        data=copy.deepcopy(DATA)
        capas=(CapaReference("C1",("D1",)),)
        analyze_workspace(self.w,DATA,capas)
        self.assertEqual(DATA,data)
    def test_mapping_not_approved(self):
        r=analyze_workspace(self.w,DATA)
        self.assertEqual(r["classification_mapping"],"DRAFT_REVIEW_REQUIRED")
        self.assertEqual(r["iso9001_conformity"],"NOT_ASSESSED")
    def test_unsupported_module(self):
        with self.assertRaises(ValueError): self.w.module_profile("Q99")
if __name__=="__main__": unittest.main()
