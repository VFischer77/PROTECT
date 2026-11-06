# P05.4 — Integrated PROTECT Dashboard Architecture
**Status: Pilot technical qualification PASS; founder design review pending**

## Decision
Create one registry-driven dashboard architecture spanning the planned PROTECT domains. Reuse P05.2 Q01/Q02 descriptive data and P05.3 pilot without changing approved analytics. Nonimplemented modules are **design-only placeholders with null metrics**, never zero-valued operational results. Q05 remains scope-pending; do not infer a finalized module definition.

## Module registry
Q01 Deviations, Q02 CAPA, Q03 Internal Audits, Q04 External Audits & Inspections, Q04-G01 Audit Governance, Q05 (scope pending), O01 Maintenance, Q09 Training, O06 Change Control, Q10 Management Review, Q11 Opportunities for Improvement, RI01 Regulatory Intelligence. Registry naming and module-to-classification mapping remain subject to founder approval.

## Interfaces
Each module exposes code, name, lifecycle status, source and optional metrics. The integrated dashboard exposes only Q01/Q02 cross-module signals and explicitly labels their limited scope. Future connectors must be independently specified, verified and qualified before data is shown. No common severity mapping is adopted until explicit founder approval.

## Exclusions
No customer data ingestion, graphical integration of all modules, new module calculations, approved KPIs, predictive thresholds, regulatory conclusions, risk scoring, automatic CAPA decisions, SaaS deployment or commercial release.

## Qualification
Seven focused synthetic architecture tests, full prior regression and synthetic integration smoke. Technical PASS does not constitute product validation or founder acceptance.

## Verified actual-source qualification
GitHub Actions run https://github.com/VFischer77/PROTECT/actions/runs/42153673732 completed SUCCESS: **73/73 Python tests PASS**, integrated synthetic registry smoke PASS, and existing prototype JavaScript syntax PASS. No integrated all-module graphical UI or browser acceptance test has been performed. This is technical pilot evidence, not commercial product validation.
