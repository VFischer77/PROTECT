import unittest
from protect_q01_p01.capa_analytics import CapaRecord, summarize_capa_records

D=[{"id":"D1","occurred_on":"2026-01-02"},{"id":"D2","occurred_on":"2026-03-02"}]
def c(**kwargs):
    base={"capa_id":"C1","initiated_on":"2026-01-03","implemented_on":"2026-02-01","verified_on":"2026-02-15","client_effectiveness":"Effective","linked_deviation_ids":("D1","D2")}
    base.update(kwargs)
    return CapaRecord(**base)

class P03Tests(unittest.TestCase):
    def test_counts_and_post_verification_review(self):
        r=summarize_capa_records([c()],D)
        self.assertEqual(r["client_outcome_counts"]["Effective"],1)
        self.assertEqual(r["review_flags"][0]["deviation_id"],"D2")
        self.assertEqual(r["review_flags"][0]["client_effectiveness_unchanged"],"Effective")
    def test_no_reclassification_or_kpi(self):
        r=summarize_capa_records([c()],D)
        self.assertEqual(r["kpi_status"],"NOT_APPROVED")
        self.assertEqual(r["causality"],"NOT_ASSESSED")
    def test_pending_without_verification(self):
        r=summarize_capa_records([c(implemented_on=None,verified_on=None,client_effectiveness="Pending")],D)
        self.assertEqual(r["client_outcome_counts"]["Pending"],1)
    def test_conclusive_without_verification_denied(self):
        with self.assertRaises(ValueError): summarize_capa_records([c(verified_on=None)],D)
    def test_invalid_chronology(self):
        with self.assertRaises(ValueError): summarize_capa_records([c(verified_on="2026-01-20")],D)
    def test_duplicate_capa(self):
        with self.assertRaises(ValueError): summarize_capa_records([c(),c()],D)
    def test_duplicate_link(self):
        with self.assertRaises(ValueError): summarize_capa_records([c(linked_deviation_ids=("D1","D1"))],D)
    def test_dangling_link(self):
        with self.assertRaises(ValueError): summarize_capa_records([c(linked_deviation_ids=("D9",))],D)
    def test_unsupported_outcome(self):
        with self.assertRaises(ValueError): summarize_capa_records([c(client_effectiveness="Closed")],D)
    def test_before_verification_not_flagged(self):
        r=summarize_capa_records([c(linked_deviation_ids=("D1",))],D)
        self.assertEqual(r["review_flags"],[])
    def test_empty_collections(self):
        self.assertEqual(summarize_capa_records([],[])["capa_count"],0)
    def test_invalid_date(self):
        with self.assertRaises(ValueError): summarize_capa_records([c(initiated_on="2026-02-30")],D)
if __name__=="__main__": unittest.main()
