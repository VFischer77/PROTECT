"""P04 controlled Q01/Q02 analytical integration; synthetic/offline, read-only.

Chronology and shared links support review hypotheses, never causal/effectiveness claims.
"""
from .integration import Workspace, CapaReference, analyze_workspace
from .capa_analytics import CapaRecord, summarize_capa_records

def analyze_q01_q02(workspace, deviations, capas, audit_events=()):
    if not isinstance(workspace, Workspace):
        raise ValueError("workspace required")
    if not isinstance(capas, (list, tuple)):
        raise ValueError("CAPA records must be a collection")
    # Both analyses validate the same input; do not silently ignore invalid records.
    q02 = summarize_capa_records(capas, deviations)
    references = tuple(
        CapaReference(c.capa_id, c.linked_deviation_ids, c.client_effectiveness)
        for c in capas
    )
    shared = analyze_workspace(workspace, deviations, references, audit_events)
    recurrence_groups = shared["q01"]["recurrence_candidates"]
    by_deviation = {}
    for link in shared["capa_deviation_links"]:
        by_deviation.setdefault(link["deviation_id"], set()).add(link["capa_id"])
    hypotheses = []
    for group in recurrence_groups:
        ids = group["deviation_ids"]
        capa_ids = sorted(set().union(*(by_deviation.get(i, set()) for i in ids)))
        hypotheses.append({
            "failure_mechanism": group["failure_mechanism"],
            "deviation_ids": tuple(ids),
            "linked_capa_ids": tuple(capa_ids),
            "status": "CONTEXTUAL_REVIEW_REQUIRED",
            "causality": "NOT_ESTABLISHED",
        })
    return {
        "workspace_profile": shared["workspace_profile"],
        "q01": shared["q01"],
        "q02": q02,
        "capa_deviation_links": shared["capa_deviation_links"],
        "recurrence_capa_review": tuple(hypotheses),
        "post_verification_review_flags": tuple(q02["review_flags"]),
        "audit_event_count": shared["audit_event_count"],
        "classification_mapping": "DRAFT_REVIEW_REQUIRED",
        "kpi_rules": "NOT_APPROVED",
        "predictive_thresholds": "NOT_APPROVED",
        "capa_effectiveness_authority": "CLIENT_SOURCE_ONLY",
        "limitations": "Shared mechanism labels and event chronology do not prove recurrence, causality, or CAPA failure."
    }
