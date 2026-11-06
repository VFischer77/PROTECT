"""P05.4 integrated module architecture; no invented metrics for unimplemented modules."""
from .dashboard import build_management_dashboard
from .module_registry import registry

def build_integrated_dashboard(workspace, deviations, capas, audit_events=()):
    existing = build_management_dashboard(workspace, deviations, capas, audit_events)
    modules=[]
    for module in registry():
        modules.append({
            "code": module.code,
            "name": module.name,
            "status": module.status,
            "source": module.source,
            "metrics": None if module.status != "PILOT_DATA_AVAILABLE" else
                ({"deviation_records":existing["summary"]["deviation_records"],
                  "monthly_counts":existing["deviation_trend"]} if module.code=="Q01" else
                 {"capa_records":existing["summary"]["capa_records"],
                  "client_outcomes":existing["capa_outcome_distribution"]}),
        })
    return {
        "schema_version":"P05.4-PILOT-1",
        "workspace_profile":existing.get("workspace_profile"),
        "modules":tuple(modules),
        "cross_module_signals":tuple(existing["review_worklist"]),
        "cross_module_scope":"Q01_Q02_ONLY",
        "available_module_count":sum(m["status"]=="PILOT_DATA_AVAILABLE" for m in modules),
        "unavailable_modules_have_no_metrics":True,
        "source_dashboard":existing,
        "status":"DESCRIPTIVE_PILOT_NOT_VALIDATED",
        "kpi_status":"NOT_APPROVED",
        "predictive_thresholds":"NOT_APPROVED",
        "human_decision":"REQUIRED",
        "limitations":"Other modules are architectural placeholders, not ingested records or validated cross-module predictors.",
    }
