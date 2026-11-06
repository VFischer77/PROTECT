import json
import tempfile
import unittest
from pathlib import Path
from protect_q01_p01.integrated_dashboard_demo import synthetic_integrated_dashboard,export

class P055Tests(unittest.TestCase):
    def test_active_modules_only(self):
        d=synthetic_integrated_dashboard()
        self.assertEqual([m["code"] for m in d["modules"] if m["metrics"] is not None],["Q01","Q02"])
    def test_design_only_null_metrics(self):
        d=synthetic_integrated_dashboard()
        self.assertTrue(all(m["metrics"] is None for m in d["modules"] if m["status"]!="PILOT_DATA_AVAILABLE"))
    def test_synthetic_only(self):
        d=synthetic_integrated_dashboard()
        self.assertEqual(d["data_origin"],"SYNTHETIC")
        self.assertEqual(d["cross_module_scope"],"Q01_Q02_ONLY")
    def test_human_decision(self):
        d=synthetic_integrated_dashboard()
        self.assertEqual(d["human_decision"],"REQUIRED")
        self.assertEqual(d["risk_prediction"],"NOT_PERFORMED")
    def test_json_export(self):
        with tempfile.TemporaryDirectory() as temp:
            p=export(Path(temp)/"sample.json")
            self.assertEqual(json.loads(p.read_text())["schema_version"],"P05.5-PILOT-1")
    def test_ui_navigation_and_safe_rendering(self):
        js=Path("prototype/p055/integrated.js").read_text()
        html=Path("prototype/p055/index.html").read_text()
        self.assertIn('id="modules"',html)
        self.assertIn('aria-pressed',js)
        self.assertIn("textContent",js)
        self.assertNotIn("innerHTML",js)
    def test_unresolved_module_scope(self):
        d=synthetic_integrated_dashboard()
        self.assertEqual(next(m["status"] for m in d["modules"] if m["code"]=="Q05"),"SCOPE_PENDING")
if __name__=="__main__":unittest.main()
