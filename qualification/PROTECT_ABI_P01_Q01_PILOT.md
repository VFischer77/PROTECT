# PROTECT–ABI–P01 — Q01 controlled offline development pilot

**Status:** Implementation staged for founder review; Q01 v0.8 remains conditionally approved architecture only.

## Source reconciliation
Based on `modules/Q01-Deviations/Q01-v0.8-conditional-baseline.md`, `requirements/classification-criteria-master-v0.1.md`, and `architecture/GC-001-global-configuration.md`.

## Implemented
- Read-only exploratory monthly deviation counts by event occurrence date.
- Candidate recurrence grouping by normalized, supplied failure-mechanism text; results explicitly labeled hypotheses requiring review.
- Deterministic ordering, duplicate/missing identifier rejection, ISO date validation.
- Synthetic data only in tests. No automatic classification, CAPA effectiveness assessment, or predictive risk assignment.

## Qualification
Seven focused unittest scenarios supplied; run locally from repository root:
`python -m unittest discover -s tests -p 'test_protect_q01_p01.py' -v`

GitHub repository CI not executed. Focused test outcome must be independently recorded after execution; no PASS is claimed by this document.

## Open design controls
- Q01-OPEN-01 industry-specific classification criteria and module-to-criteria mapping: REVIEW REQUIRED, not implemented.
- Q01-OPEN-02 KPI population, denominator, exclusions and extension rules: OPEN. Monthly counts are descriptive only, not approved KPIs.
- Q01-OPEN-03 predictive model acceptance thresholds: OPEN. No predictions.
- F-06 historical source integrity/provenance: ON HOLD outside Q01.
- IP-13 CAPA effectiveness remains authoritative in Q02 and is not calculated here.
- GC-001 one-time Industry and Service Domain configuration is a separate design requirement, not implemented in this pilot.
- No regulatory determination, client data ingestion, deployment, or production authorization.

## Human acceptance
Pending. No merge to main.
