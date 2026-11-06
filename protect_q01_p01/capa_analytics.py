"""P03 Q02 descriptive CAPA analytics; no effectiveness determination or KPI approval."""
from collections import Counter
from dataclasses import dataclass
from datetime import date

_ALLOWED = frozenset({"Effective", "Not Effective", "Pending"})

@dataclass(frozen=True)
class CapaRecord:
    capa_id: str
    initiated_on: str
    implemented_on: str | None = None
    verified_on: str | None = None
    client_effectiveness: str = "Pending"
    linked_deviation_ids: tuple[str, ...] = ()

def _day(value):
    if not isinstance(value, str):
        raise ValueError("date required")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("invalid date") from exc
    if parsed.isoformat() != value:
        raise ValueError("date must be YYYY-MM-DD")
    return parsed

def summarize_capa_records(capas, deviations):
    """Return descriptive populations and contextual review flags only.

    Same linked deviation occurring after verification is a *review flag*, not
    evidence that a client-approved effectiveness result should be changed.
    """
    if not isinstance(capas, (list, tuple)) or not isinstance(deviations, (list, tuple)):
        raise ValueError("collections required")
    dev_dates = {}
    for dev in deviations:
        if not isinstance(dev, dict) or not isinstance(dev.get("id"), str) or not dev["id"] or dev["id"] in dev_dates:
            raise ValueError("invalid or duplicate deviation")
        dev_dates[dev["id"]] = _day(dev.get("occurred_on"))
    seen = set()
    counts = Counter()
    flags = []
    links = set()
    for capa in capas:
        if not isinstance(capa, CapaRecord) or not capa.capa_id or capa.capa_id in seen:
            raise ValueError("invalid or duplicate CAPA")
        seen.add(capa.capa_id)
        start = _day(capa.initiated_on)
        implemented = _day(capa.implemented_on) if capa.implemented_on is not None else None
        verified = _day(capa.verified_on) if capa.verified_on is not None else None
        if implemented is not None and implemented < start:
            raise ValueError("implementation precedes initiation")
        if verified is not None and (implemented is None or verified < implemented):
            raise ValueError("verification chronology invalid")
        if capa.client_effectiveness not in _ALLOWED:
            raise ValueError("unsupported client effectiveness")
        if verified is None and capa.client_effectiveness != "Pending":
            raise ValueError("conclusive outcome requires verification date")
        if len(set(capa.linked_deviation_ids)) != len(capa.linked_deviation_ids):
            raise ValueError("duplicate CAPA deviation link")
        counts[capa.client_effectiveness] += 1
        for dev_id in capa.linked_deviation_ids:
            if dev_id not in dev_dates:
                raise ValueError("unknown deviation link")
            links.add((capa.capa_id, dev_id))
            if verified is not None and dev_dates[dev_id] > verified:
                flags.append({"capa_id": capa.capa_id, "deviation_id": dev_id,
                              "flag": "POST_VERIFICATION_EVENT_REVIEW",
                              "client_effectiveness_unchanged": capa.client_effectiveness})
    return {
        "capa_count": len(capas),
        "client_outcome_counts": {k: counts[k] for k in ("Effective", "Not Effective", "Pending")},
        "unique_link_count": len(links),
        "review_flags": sorted(flags, key=lambda f: (f["capa_id"], f["deviation_id"])),
        "kpi_status": "NOT_APPROVED",
        "effectiveness_assessment": "CLIENT_SOURCE_ONLY",
        "causality": "NOT_ASSESSED",
        "limitations": "Descriptive counts only; no denominator, verified adequacy or causal inference."
    }
