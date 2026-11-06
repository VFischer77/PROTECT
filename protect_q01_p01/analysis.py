"""PROTECT Q01 P01: exploratory offline deviation recurrence/trend prototype.

No severity assignment, prediction, source-record changes, or regulatory decisions.
"""
from collections import Counter, defaultdict
from datetime import date

def analyze_deviations(records):
    """Analyze synthetic or explicitly authorized records without changing them.

    Candidate recurrence groups are keyed by supplied failure mechanism only;
    they are hypotheses requiring human review, not confirmed recurrence.
    """
    if not isinstance(records, list):
        raise ValueError("records must be a list")
    seen = set()
    by_month = Counter()
    mechanisms = defaultdict(list)
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("record must be a mapping")
        identifier = record.get("id")
        occurred = record.get("occurred_on")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise ValueError("missing or duplicate deviation id")
        seen.add(identifier)
        if not isinstance(occurred, str):
            raise ValueError("occurred_on required")
        try:
            day = date.fromisoformat(occurred)
        except ValueError as exc:
            raise ValueError("invalid occurrence date") from exc
        if day.isoformat() != occurred:
            raise ValueError("date must use YYYY-MM-DD")
        by_month[day.strftime("%Y-%m")] += 1
        mechanism = record.get("failure_mechanism")
        if mechanism is not None:
            if not isinstance(mechanism, str):
                raise ValueError("failure mechanism must be text or null")
            if mechanism.strip():
                mechanisms[mechanism.strip().casefold()].append((day, identifier))
    candidates = []
    for mechanism, events in sorted(mechanisms.items()):
        if len(events) > 1:
            ordered = sorted(events)
            candidates.append({
                "failure_mechanism": mechanism,
                "deviation_ids": [identifier for _, identifier in ordered],
                "status": "HYPOTHESIS_REQUIRES_REVIEW"
            })
    return {
        "record_count": len(records),
        "monthly_counts": dict(sorted(by_month.items())),
        "recurrence_candidates": candidates,
        "severity_classification": "NOT_EVALUATED",
        "predictive_risk": "NOT_EVALUATED",
        "limitations": "Counts have no exposure denominator; matching mechanism is not proof of recurrence."
    }
