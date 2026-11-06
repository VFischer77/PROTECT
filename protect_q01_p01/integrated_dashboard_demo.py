"""Generate a synthetic P05.5 integrated dashboard contract from actual pilot logic."""
import json
from pathlib import Path
from .dashboard_demo import synthetic_dashboard
from .module_registry import registry

def synthetic_integrated_dashboard():
    source = synthetic_dashboard()
    modules = []
    for m in registry():
        if m.code == "Q01":
            metrics = {"deviation_records":source["summary"]["deviation_records"],"monthly_counts":source["deviation_trend"]}
        elif m.code == "Q02":
            metrics = {"capa_records":source["summary"]["capa_records"],"client_outcomes":source["capa_outcome_distribution"]}
        else:
            metrics = None
        modules.append({"code":m.code,"name":m.name,"status":m.status,"metrics":metrics})
    return {
        "schema_version":"P05.5-PILOT-1",
        "data_origin":"SYNTHETIC",
        "modules":modules,
        "active_module_codes":["Q01","Q02"],
        "cross_module_scope":"Q01_Q02_ONLY",
        "source_dashboard":source,
        "kpi_status":"NOT_APPROVED",
        "risk_prediction":"NOT_PERFORMED",
        "human_decision":"REQUIRED",
        "limitations":"Design-only modules contain no operational data. No approved KPIs or predictive conclusions.",
    }

def export(path):
    p=Path(path)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(synthetic_integrated_dashboard(),indent=2,sort_keys=True),encoding="utf-8")
    return p

if __name__=="__main__":
    import sys
    if len(sys.argv)!=2: raise SystemExit("Usage: python -m protect_q01_p01.integrated_dashboard_demo OUTPUT.json")
    print(export(sys.argv[1]))
