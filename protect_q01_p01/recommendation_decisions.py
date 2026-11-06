"""P05.7 bounded recommendation discussion and decision contract.

No CAPA repository, no eQMS write integration, no automated execution.
"""
from dataclasses import dataclass
from datetime import datetime, timezone

CHOICES = (
    ("INVESTIGATE", "Further investigation required"),
    ("MONITOR", "Continue monitoring"),
    ("IMPROVEMENT", "Recommend improvement"),
    ("REFER_CAPA", "Recommend CAPA initiation"),
    ("ACCEPT", "Accept recommendation"),
    ("REJECT", "Reject recommendation"),
    ("OTHER", "Other — specify"),
)

@dataclass(frozen=True)
class ReviewEntry:
    recommendation_id: str
    actor: str
    timestamp_utc: str
    decision: str
    comment: str
    action_detail: str = ""
    external_reference: str = ""

def create_review_entry(recommendation_id, actor, decision, comment, action_detail="", external_reference="", timestamp_utc=None):
    if decision not in dict(CHOICES):
        raise ValueError("Unsupported decision")
    if not recommendation_id.strip() or not actor.strip() or not comment.strip():
        raise ValueError("Recommendation, actor and rationale required")
    if decision in ("IMPROVEMENT", "REFER_CAPA", "OTHER") and not action_detail.strip():
        raise ValueError("Action detail required for this choice")
    if external_reference and decision != "REFER_CAPA":
        raise ValueError("External CAPA reference only on CAPA referral")
    return ReviewEntry(
        recommendation_id.strip(), actor.strip(),
        timestamp_utc or datetime.now(timezone.utc).isoformat(),
        decision, comment.strip(), action_detail.strip(), external_reference.strip()
    )

CAPA_INTEGRATION = {
    "capability": "INITIATE_CAPA",
    "status": "FUTURE_DISABLED",
    "requires": ["authorized_human_confirmation", "qualified_eQMS_connector", "external_system_acknowledgement"],
    "writes_external_records": False,
    "stores_capa_lifecycle": False,
}
