# PROTECT–ABI–P04 — Integrated Q01/Q02 offline analysis

**Status:** Implementation committed; focused qualification and founder acceptance to be confirmed.

## Baselines and scope
Extends P01 Q01 v0.8 deviation analysis, P02 GC-001 workspace/profile and link validation, and P03 Q02 v0.2 descriptive CAPA analytics. No client records, external action, merge, or production release.

## Integration behavior
- Q01 recurrence *candidate* groups are cross-referenced with Q02 CAPA-to-deviation links.
- P03 post-verification events are surfaced as human-review flags without changing authoritative client CAPA effectiveness.
- Shared workspace profile is inherited. Many-to-many link checks remain in force.
- Source classifications remain untouched; no automatic severity, KPI, causal or predictive decisions.
- Audit references count only; no finding-level association or regulatory conclusion.

## Qualification
12 focused synthetic scenarios in `tests/test_protect_q01_p04.py`.
Run `python -m unittest discover -s tests -p 'test_protect_q01_p04.py' -v` from repository root.
The full P01–P04 suite and GitHub CI require separate evidence.

## Open design items
Q01-OPEN-01/02/03, Q02-OPEN-01/02/03/04 remain OPEN. The module-to-classification-criteria mapping remains DRAFT/REVIEW pending founder approval. F-06 remains ON HOLD outside Q01. ABI-REC-001 contextual recurrence evidence engine, full CAPA verification adequacy, KPI denominator rules, and validated predictive thresholds are not implemented. Human acceptance required; no merge to main.
