"""P05.2 presentation-ready descriptive dashboard data; no rendered UI or validated KPIs."""
from .review_worklist import build_review_worklist

def build_management_dashboard(workspace, deviations, capas, audit_events=()):
    result = build_review_worklist(workspace, deviations, capas, audit_events)
    snap = result["source_snapshot"]
    monthly = snap["deviation_monthly_counts"]
    outcomes = snap["client_capa_outcome_counts"]
    return {
        "title": "PROTECT Operational Intelligence — Descriptive Overview",
        "deviation_trend": tuple({"period": month, "count": count} for month, count in sorted(monthly.items())),
        "capa_outcome_distribution": tuple({"outcome": outcome, "count": count} for outcome, count in sorted(outcomes.items())),
        "review_signal_distribution": tuple({
            "signal_type": kind,
            "count": sum(1 for x in result["worklist"] if x["signal_type"] == kind)
        } for kind in sorted({x["signal_type"] for x in result["worklist"]})),
        "summary": {
            "deviation_records": snap["deviation_record_count"],
            "capa_records": snap["capa_record_count"],
            "human_review_items": result["worklist_count"],
        },
        "review_worklist": result["worklist"],
        "chart_semantics": "DESCRIPTIVE_COUNTS_ONLY",
        "missing_periods": "NOT_IMPUTED",
        "exposure_normalization": "NOT_AVAILABLE",
        "kpi_status": "NOT_APPROVED",
        "risk_prediction": "NOT_PERFORMED",
        "severity_assignment": "NOT_PERFORMED",
        "human_decision": "REQUIRED",
        "limitations": "No denominator, normalization, control limits, approved KPI rules or predictive thresholds. Counts are not risk or compliance conclusions.",
    }
