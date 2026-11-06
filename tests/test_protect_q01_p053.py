import json
import tempfile
import unittest
from pathlib import Path
from protect_q01_p01.dashboard_demo import synthetic_dashboard, export_synthetic

class P053Tests(unittest.TestCase):
    def test_contract(self):
        d=synthetic_dashboard()
        self.assertEqual(d["summary"]["human_review_items"],2)
        self.assertEqual(d["risk_prediction"],"NOT_PERFORMED")
        self.assertEqual(d["human_decision"],"REQUIRED")
        self.assertEqual(d["kpi_status"],"NOT_APPROVED")
    def test_export_matches_contract(self):
        with tempfile.TemporaryDirectory() as t:
            path=export_synthetic(Path(t)/"demo.json")
            self.assertEqual(json.loads(path.read_text()),json.loads(json.dumps(synthetic_dashboard())))
    def test_source_is_synthetic(self):
        d=synthetic_dashboard()
        self.assertTrue(all(id.startswith("SYN-") for item in d["review_worklist"] for id in item["deviation_ids"]))
    def test_ui_controls_present(self):
        html=Path("prototype/p053/index.html").read_text()
        js=Path("prototype/p053/dashboard.js").read_text()
        self.assertIn('id="filter"',html)
        self.assertIn("filter.addEventListener",js)
        self.assertIn("textContent",js)
        self.assertNotIn("innerHTML",js)
        self.assertNotIn("localStorage",js)
    def test_empty_analytics_remain_descriptive(self):
        d=synthetic_dashboard()
        self.assertEqual(d["chart_semantics"],"DESCRIPTIVE_COUNTS_ONLY")
        self.assertEqual(d["missing_periods"],"NOT_IMPUTED")
if __name__=="__main__": unittest.main()
