"""P05 descriptive management view; no validated KPI or predictive risk score."""
from .q01_q02_integrated import analyze_q01_q02

def management_snapshot(workspace, deviations, capas, audit_events=()):
    integrated = analyze_q01_q02(workspace, deviations, capas, audit_events)
    q01, q02 = integrated["q01"], integrated["q02"]
    review_queue = []
    for item in integrated["recurrence_capa_review"]:
        review_queue.append({
            "type": "RECURRENCE_HYPOTHESIS",
            "deviation_ids": item["deviation_ids"],
            "linked_capa_ids": item["linked_capa_ids"],
            "status": "HUMAN_REVIEW_REQUIRED",
        })
    for item in integrated["post_verification_review_flags"]:
        review_queue.append({
            "type": "POST_VERIFICATION_EVENT",
            "deviation_ids": (item["deviation_id"],),
            "linked_capa_ids": (item["capa_id"],),
            "status": "HUMAN_REVIEW_REQUIRED",
        })
    return {
        "workspace_profile": integrated["workspace_profile"],
        "deviation_monthly_counts": dict(q01["monthly_counts"]),
        "deviation_record_count": q01["record_count"],
        "capa_record_count": q02["capa_count"],
        "client_capa_outcome_counts": dict(q02["client_outcome_counts"]),
        "review_queue": tuple(review_queue),
        "review_queue_is_deduplicated": False,
        "indicator_type": "DESCRIPTIVE_COUNTS_NOT_APPROVED_KPIS",
        "early_warning": "UNVALIDATED_REVIEW_CANDIDATES_ONLY",
        "classification": "NOT_ASSIGNED",
        "risk_score": "NOT_CALCULATED",
        "predictive_thresholds": "NOT_APPROVED",
        "management_decision": "HUMAN_REQUIRED",
    }
