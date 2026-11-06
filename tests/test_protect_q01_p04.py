import copy
import unittest
from protect_q01_p01.integration import Workspace, LinkedEvent
from protect_q01_p01.capa_analytics import CapaRecord
from protect_q01_p01.q01_q02_integrated import analyze_q01_q02

DEVIATIONS = [
    {"id":"D2","occurred_on":"2026-03-05","failure_mechanism":"Seal issue","source_classification":"Major"},
    {"id":"D1","occurred_on":"2026-01-05","failure_mechanism":"seal issue","source_classification":"Minor"},
    {"id":"D3","occurred_on":"2026-01-20","failure_mechanism":"Label issue"}
]
CAPAS = [
    CapaRecord("C1","2026-01-10","2026-02-01","2026-02-20","Effective",("D1","D2")),
    CapaRecord("C2","2026-01-21",None,None,"Pending",("D3",))
]
class P04Tests(unittest.TestCase):
    def setUp(self): self.w=Workspace("Pharmaceuticals","GMP/Quality")
    def test_integrated_hypothesis(self):
        r=analyze_q01_q02(self.w,DEVIATIONS,CAPAS)
        h=r["recurrence_capa_review"][0]
        self.assertEqual(h["deviation_ids"],("D1","D2"))
        self.assertEqual(h["linked_capa_ids"],("C1",))
        self.assertEqual(h["causality"],"NOT_ESTABLISHED")
    def test_post_verification_flag_only(self):
        r=analyze_q01_q02(self.w,DEVIATIONS,CAPAS)
        self.assertEqual(r["post_verification_review_flags"][0]["deviation_id"],"D2")
        self.assertEqual(r["q02"]["client_outcome_counts"]["Effective"],1)
    def test_many_to_many_unique(self):
        more=CAPAS+[CapaRecord("C3","2026-01-12",None,None,"Pending",("D1","D2"))]
        r=analyze_q01_q02(self.w,DEVIATIONS,more)
        self.assertEqual(len(r["capa_deviation_links"]),5)
        self.assertEqual(r["q01"]["record_count"],3)
        self.assertEqual(r["recurrence_capa_review"][0]["linked_capa_ids"],("C1","C3"))
    def test_unlinked_recurrence(self):
        r=analyze_q01_q02(self.w,DEVIATIONS,[])
        self.assertEqual(r["recurrence_capa_review"][0]["linked_capa_ids"],())
    def test_source_unchanged(self):
        before=copy.deepcopy(DEVIATIONS)
        analyze_q01_q02(self.w,DEVIATIONS,CAPAS)
        self.assertEqual(DEVIATIONS,before)
        self.assertEqual(CAPAS[0].client_effectiveness,"Effective")
    def test_unapproved_rules_blocked(self):
        r=analyze_q01_q02(self.w,DEVIATIONS,CAPAS)
        self.assertEqual(r["classification_mapping"],"DRAFT_REVIEW_REQUIRED")
        self.assertEqual(r["predictive_thresholds"],"NOT_APPROVED")
        self.assertEqual(r["kpi_rules"],"NOT_APPROVED")
    def test_profile_inherited(self):
        r=analyze_q01_q02(self.w,DEVIATIONS,CAPAS)
        self.assertIs(r["workspace_profile"],self.w.module_profile("Q02"))
    def test_invalid_link_rejected(self):
        with self.assertRaises(ValueError):
            analyze_q01_q02(self.w,DEVIATIONS,[CapaRecord("C4","2026-01-01",linked_deviation_ids=("missing",))])
    def test_invalid_chronology_rejected(self):
        with self.assertRaises(ValueError):
            analyze_q01_q02(self.w,DEVIATIONS,[CapaRecord("C4","2026-03-01","2026-02-01")])
    def test_audit_reference(self):
        r=analyze_q01_q02(self.w,DEVIATIONS,CAPAS,[LinkedEvent("A1","Internal Audit","2026-01-01")])
        self.assertEqual(r["audit_event_count"],1)
    def test_empty(self):
        r=analyze_q01_q02(self.w,[],[])
        self.assertEqual(r["q01"]["record_count"],0)
        self.assertEqual(r["q02"]["capa_count"],0)
    def test_duplicate_capa_rejected(self):
        with self.assertRaises(ValueError): analyze_q01_q02(self.w,DEVIATIONS,CAPAS+CAPAS)
if __name__=="__main__": unittest.main()
