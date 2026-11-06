"""Export a synthetic, read-only P05.3 demo from the P05.2 dashboard contract."""
import json
from pathlib import Path
from .integration import Workspace
from .capa_analytics import CapaRecord
from .dashboard import build_management_dashboard

def synthetic_dashboard():
    deviations = [
        {"id":"SYN-D1","occurred_on":"2026-01-05","failure_mechanism":"Seal issue"},
        {"id":"SYN-D2","occurred_on":"2026-03-05","failure_mechanism":"seal issue"},
    ]
    capas = [CapaRecord("SYN-C1","2026-01-10","2026-02-01","2026-02-20","Effective",("SYN-D1","SYN-D2"))]
    return build_management_dashboard(Workspace("Pharmaceuticals","GMP/Quality"), deviations, capas)

def export_synthetic(path):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(synthetic_dashboard(), indent=2, sort_keys=True), encoding="utf-8")
    return target

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m protect_q01_p01.dashboard_demo OUTPUT.json")
    print(export_synthetic(sys.argv[1]))
