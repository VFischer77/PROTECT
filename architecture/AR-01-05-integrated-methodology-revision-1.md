# PROTECT — AR-01–AR-05 Integrated Architecture and Methodology, Revision 1
Status: PROPOSED integrated design; owner authorized consideration/integration of supplied methodology. Not qualified, implemented or deployed.
Source: user-provided 14-page 'FC-Protect Predictive Operational Performance & Risk Management.docx' (2026-11-04). Preserve its proposed methods as candidates; do not treat illustrative values as validated.

## 1. Governing design
FR-001 remains controlling: ISO 9001 mandatory minimum PROTECT requirements/assessment baseline. Additional applicable industry, jurisdictional, contractual and specialized frameworks are additive. GC-001 Industry and Service Domain selected once per workspace; AGP-001 proportional governance proposed, without dropping applicable requirements. No limited-scope module report may claim organization-wide conformity or certification. Existing Q01 v0.8 and Q02 v0.2 remain conditionally accepted, Q03 v0.1 proposed; impact review required, not automatic reapproval.

## 2. Source-derived methodology mapped to PROTECT
Source six-stage sequence: P Performance Baseline; R Risk & Driver Identification; O Operational Data Analytics; T Trend Prediction; E Early Warning & Evaluation; C/T Corrective Action & Tracking. These are engagement/methodology stages, distinct from each module's M1–M6 analytical lifecycle. Do not silently equate them.
Source five disciplines: operational performance management, statistical predictive analytics, operational risk management, early warning, continuous improvement.
Source KPI families: (A) productivity/efficiency, (B) quality, (C) operational reliability, (D) workforce, (E) supply chain/resources, (F) financial/operational impact. Build one shared Performance Intelligence Framework (PIF-001), with client-specific selection of ~10–15 well-defined KPIs and one primary outcome KPI where suitable. KPI formulas are candidate definitions, not approved calculations.
Source statistical levels: (1) descriptive statistics and SPC, (2) correlation/regression, (3) time-series forecasting, (4) predictive risk index. Method selection depends on data, assumptions and independent qualification. Correlation is not causation.
Source early warning: trend alert, performance risk, critical deterioration; workflow Detect > Validate > Investigate > Assess > Act > Verify. Alerts are advisory and require client decision ownership.
Source qualification: time-respecting train/validation separation, simple baseline comparisons, forecast uncertainty, MAE/RMSE/MAPE as applicable, classification precision/recall/F1, false alarm/miss rates and monitoring. No unqualified forecasts.
Source prototype/tool suggestions: Excel, Power BI, Python, Power Automate; options only, not technology commitment or spend authorization.
Source commercial packages: Assessment; Predictive; Enterprise. Make offerings modular: Enterprise need not require prediction. Source 8–10 week schedule illustrative only; prediction conditional on adequate data.
Source example: simulated manufacturing prototype; extend to professional-services case for cross-industry verification.

## 3. AR-01 — Foundation, scope and applicability
Requirements traceability must cover ISO 9001 baseline and applicable overlays, with explicit assessed/not assessed/insufficient evidence/not applicable with justification/conforming/nonconforming states. Introduce process context, leadership, customer requirements, risk/opportunity, resources, operational control, performance evaluation and improvement. Maintain separate client/source and PROTECT analytical conclusions. Validate ISO edition and clause text from controlled normative source before claiming full mapping.

## 4. AR-02 — Shared data and performance intelligence
PIF-001 candidate KPI contract: KPI ID, business question, owner, process, definition, numerator/denominator, units, exposure, segmentation, observation interval, baseline, targets, aggregation, missingness, exclusions, data source, data quality, interpretation and review. Define canonical entity/event identifiers, event occurrence/detection/recording/decision times, relationship provenance and deduplication. Client owns original records; PROTECT assesses fitness of inputs for analytics.
Example KPI issues: labor productivity adjusted for output mix; capacity denominator; cycle-time boundaries; cost-of-poor-quality accounting basis; training pass rate vs workplace effectiveness. No universal positive/negative interpretation of utilization.
Support low-data descriptive/structured expert assessment with prediction disabled.

## 5. AR-03 — Predictive qualification and decision interface
Prediction target, horizon, reference population, decision use, minimum data sufficiency, leakage controls, drift, calibration, cost of false alerts/misses, uncertainty, performance against baseline and shutdown conditions must be specified per use case. Source illustrative weighted 0–100 risk index (downtime 25%, rework 25%, cycle time 20%, material 15%, workforce 15%; bands 0–29/30–49/50–69/70–100) is NOT accepted or approved; do not display as validated probability or severity. Start with transparent independent signals. Human-review/escalation authority and action-effectiveness monitoring belong to client.

## 6. AR-04 — Security, qualification and traceability
Risk-based integrated test gates: requirement coverage, source mapping, KPI calculations, chronology, deduplication, contextual reasoning, profile inheritance, predictive validity, client decision traceability, confidentiality and workspace separation. Simulated data can validate mechanics, not real-world predictive utility. Document independent review and test evidence; no tests have been run.

## 7. AR-05 — Management system and commercial operating model
Complete ISO 9001 management-system requirements mapping in controlled separate artifact. Establish engagement scopes: Assessment (baseline, KPIs, risks, opportunities), Predictive (only after qualification), Enterprise (operational excellence, risk and resilience with or without prediction). 8–10 weeks is not a commitment. Client owns approvals, operational interventions and results; consultants advise and measure. Quantify benefits/ROI with defensible baseline, attribution caveats and cost definitions.

## 8. Impact review and open specifications
Q01: map operational events and process failures alongside GMP deviations; retain Q01-OPEN-01–03.
Q02: map improvement/corrective actions without requiring GMP CAPA form for all; retain Q02-OPEN-01–04.
Q03: proportionate change and improvement management with ISO 9001 baseline; retain Q03-OPEN-01–04.
Open integration items: PIF-OPEN-01 KPI dictionary and formula verification; PIF-OPEN-02 exposure, mix and missing-data rules; PRED-OPEN-01 use-case qualification criteria; RISK-OPEN-01 risk dimensions and index decision; ISO-OPEN-01 verified edition/clauses and complete mapping; COM-OPEN-01 package scope and delivery assumptions.

## 9. Proposed acceptance scenarios (not executed)
INT-01 professional services uses ISO 9001 baseline without GMP-only paperwork.
INT-02 manufacturing uses performance KPI definitions with stable denominators.
INT-03 medical-device overlay adds requirements while retaining baseline.
INT-04 one event linked across Q01/Q02/Q03 counted correctly.
INT-05 low-data client receives assessment without unsupported forecast.
INT-06 illustrative composite index cannot be presented as validated.
INT-07 temporal holdout excludes future information.
INT-08 alert creates advisory review, not autonomous operational approval.
INT-09 Enterprise package works without predictive subscription.
INT-10 simulation results labeled synthetic and not client outcome evidence.

## Disposition
Integrated design draft prepared for owner review. No new modules, production model, software or deployment authorized. AR-01–AR-05 are not closed by this document.
