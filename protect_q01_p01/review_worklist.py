"""P05.1 read-only human review worklist; no automated risk or CAPA decisions."""
from .operational_intelligence import management_snapshot

def build_review_worklist(workspace, deviations, capas, audit_events=()):
    snapshot = management_snapshot(workspace, deviations, capas, audit_events)
    # Deduplicate identical evidence signals only; distinct signal types remain distinct.
    entries = {}
    for item in snapshot["review_queue"]:
        kind = item["type"]
        ids = tuple(sorted(set(item["deviation_ids"])))
        capa_ids = tuple(sorted(set(item["linked_capa_ids"])))
        key = (kind, ids, capa_ids)
        entries[key] = {
            "signal_type": kind,
            "deviation_ids": ids,
            "linked_capa_ids": capa_ids,
            "review_status": "OPEN_FOR_HUMAN_REVIEW",
            "evidence_status": "HYPOTHESIS_NOT_CONFIRMED",
            "recommended_action": "REVIEW_CONTEXT_AND_SOURCE_RECORDS",
            "risk_level": "NOT_ASSIGNED",
            "client_effectiveness_modified": False,
        }
    ordered = tuple(entries[key] for key in sorted(entries))
    return {
        "worklist": ordered,
        "worklist_count": len(ordered),
        "source_signal_count": len(snapshot["review_queue"]),
        "source_snapshot": snapshot,
        "auto_closure": False,
        "auto_escalation": False,
        "data_modification": False,
        "limitations": "Signal grouping is descriptive; does not establish recurrence, CAPA ineffectiveness, causality, or risk.",
    }
