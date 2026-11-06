import copy
import unittest
from protect_q01_p01.analysis import analyze_deviations

SAMPLE = [
    {"id":"DEV-002","occurred_on":"2026-02-03","failure_mechanism":"Seal defect","source_classification":"Major"},
    {"id":"DEV-001","occurred_on":"2026-01-04","failure_mechanism":"seal defect","source_classification":"Minor"},
    {"id":"DEV-003","occurred_on":"2026-02-08","failure_mechanism":None}
]
class Q01PilotTests(unittest.TestCase):
    def test_monthly_counts_and_candidate(self):
        r=analyze_deviations(SAMPLE)
        self.assertEqual(r["monthly_counts"],{"2026-01":1,"2026-02":2})
        self.assertEqual(r["recurrence_candidates"][0]["deviation_ids"],["DEV-001","DEV-002"])
        self.assertEqual(r["recurrence_candidates"][0]["status"],"HYPOTHESIS_REQUIRES_REVIEW")
    def test_source_unchanged(self):
        original=copy.deepcopy(SAMPLE)
        analyze_deviations(SAMPLE)
        self.assertEqual(SAMPLE,original)
    def test_no_severity_or_prediction(self):
        r=analyze_deviations(SAMPLE)
        self.assertEqual(r["severity_classification"],"NOT_EVALUATED")
        self.assertEqual(r["predictive_risk"],"NOT_EVALUATED")
    def test_missing_or_duplicate_id_rejected(self):
        with self.assertRaises(ValueError): analyze_deviations([SAMPLE[0],SAMPLE[0]])
        with self.assertRaises(ValueError): analyze_deviations([{"occurred_on":"2026-01-01"}])
    def test_invalid_date_rejected(self):
        with self.assertRaises(ValueError): analyze_deviations([{"id":"x","occurred_on":"2026-02-30"}])
    def test_empty_data(self):
        r=analyze_deviations([])
        self.assertEqual(r["record_count"],0)
        self.assertEqual(r["recurrence_candidates"],[])
    def test_nontext_mechanism_rejected(self):
        with self.assertRaises(ValueError): analyze_deviations([{"id":"x","occurred_on":"2026-01-01","failure_mechanism":42}])
if __name__=="__main__": unittest.main()
