import unittest
from protect_q01_p01.recommendation_decisions import CHOICES,CAPA_INTEGRATION,create_review_entry
class RecommendationDecisionTests(unittest.TestCase):
    def test_choices_unique(self):
        self.assertEqual(len(CHOICES),len(set(code for code,_ in CHOICES)))
    def test_comment_and_actor_required(self):
        with self.assertRaises(ValueError):create_review_entry("REC-1","","MONITOR","rationale")
        with self.assertRaises(ValueError):create_review_entry("REC-1","Reviewer","MONITOR","")
    def test_action_detail_required(self):
        for choice in ("IMPROVEMENT","REFER_CAPA","OTHER"):
            with self.assertRaises(ValueError):create_review_entry("REC-1","Reviewer",choice,"rationale")
    def test_referral_is_not_capa_creation(self):
        r=create_review_entry("REC-1","Reviewer","REFER_CAPA","Rationale","Review external CAPA need")
        self.assertEqual(r.decision,"REFER_CAPA")
        self.assertFalse(CAPA_INTEGRATION["writes_external_records"])
        self.assertFalse(CAPA_INTEGRATION["stores_capa_lifecycle"])
    def test_external_reference_only_for_referral(self):
        with self.assertRaises(ValueError):create_review_entry("REC-1","Reviewer","MONITOR","Rationale",external_reference="CAPA-1")
    def test_future_button_disabled(self):
        self.assertEqual(CAPA_INTEGRATION["status"],"FUTURE_DISABLED")
    def test_comment_retains_rationale(self):
        r=create_review_entry("REC-1","Reviewer","MONITOR","  Review next month  ")
        self.assertEqual(r.comment,"Review next month")
if __name__=="__main__":unittest.main()
