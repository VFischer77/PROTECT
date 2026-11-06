# GOV-001-04 — Risk-Based Verification & Validation Procedure
**v0.1 DRAFT — approval pending**

## Assessment
For each requirement/change, evaluate patient/product/compliance/operational impact as applicable, likelihood of erroneous result, detectability and human review effectiveness. Record rationale and planned controls; avoid pretending a numeric risk score is validated before criteria are approved.

## Verification evidence
Test ID, requirement ID, test purpose, source SHA/build, environment, synthetic or authorized data, preconditions, steps, expected results, observed results, status, anomaly link, executor, independent reviewer and timestamp.

## Validation evidence
Representative user workflow, intended-use claims, actual user decision point, data provenance, expected behavior, observed result, limitation, user acceptance and residual-risk disposition. Verify error paths and misleading-output risks.

## Independence and deviations
Separate implementation from acceptance review where practical; document compensating controls. Failed tests trigger defect triage and targeted retest; regression breadth determined by impact, not automatic full repetition.

## P04.1 baseline
Workflow run 42150810078: 48 tests and synthetic E2E PASS on pilot source. This is **technical verification evidence**, not approved commercial product validation.
