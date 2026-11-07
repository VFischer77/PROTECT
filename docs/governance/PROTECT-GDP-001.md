# PROTECT-GDP-001 — Recordkeeping, Good Documentation Practice and Data Integrity
Version: 0.1
Decision date: 2026-11-06
Decision: CONDITIONALLY APPROVED FOR DESIGN (founder decision)
Effective operational status: NOT EFFECTIVE; implementation and qualification not authorized by this decision
Approval scope: conceptual documentation and record-control architecture; no claim of GMP/Part 11 validation or production readiness.

## Purpose and scope
Establish ALCOA+ principles (attributable, legible, contemporaneous, original, accurate, complete, consistent, enduring, available) for PROTECT development, operations, and client GxP records, distinguishing ownership and intended use. Applicable requirements include 21 CFR 210/211, Part 11, EU GMP Chapter 4/Annex 11, and device-specific requirements where applicable; applicability is determined by regulated use and predicate rules.

## Controlled record requirements
Classify R1 governance, R2 design/development, R3 verification/qualification, R4 operations, R5 client GxP, R6 supporting records (controlled if used as decision evidence). For controlled records maintain unique identifier, title, class, version, author/system identity, creation timestamp/time zone, owner, status, module, approval decision/authority, authoritative location, evidence links and retention class. Preserve originals, metadata, corrections, previous values and reason where required. No silent overwrites, invented approvals, shared regulated signing identities or retrospective reconstruction presented as contemporaneous evidence.

## Lifecycle and evidence
Draft -> Review -> Approved -> Effective -> Superseded/Retired; conditional, on-hold, rejected states supported. Exact approved version, identity, meaning, date and restrictions must be linked. A Git SHA identifies code but does not itself constitute qualification or a compliant electronic signature. Each milestone records exact repository/branch/SHA, scope, evidence, decision/approver, linked open exceptions and next milestone in its existing issue/PR; no duplicate archive package.

## Electronic controls (where applicable)
Risk-based access control, secure time-stamped audit trails retaining relevant original/changed values, actor, time and reason; controlled audit trail review; validated electronic-signature identity/authentication, meaning and record binding when Part 11 applies; secure retention and retrievability. Distinguish source data, transformations, indicators, model outputs and human decisions with traceable versioned provenance. Do not misrepresent AI-generated recommendations as original observations. Retention schedule must reflect applicable predicate rules and client contracts, not one universal duration. Backups are not a substitute for records retention and retrieval.

## Governance and exceptions
Founders approve foundational architecture and material risk decisions. Designated quality authority reviews GMP applicability and qualification evidence. Client remains authoritative for its approved GxP records unless contractual arrangements state otherwise. Nonconformities use existing deviation/CAPA and change-control processes; do not duplicate CAPAs. Risk-based effectiveness sampling of real records is required before operational adoption.

## Conditional acceptance — only essential outstanding decisions
1. Confirm intended regulated use and record ownership boundaries by deployment/client domain, including where Part 11 and EU Annex 11 apply.
2. Approve controlled-record metadata/classification and identify the authoritative records system plus applicable retention schedule.
3. Assign the designated quality approval authority and establish proportional implementation/qualification criteria before regulated operation.

Detailed interfaces, audit-trail technology, and module-specific implementation are deferred until applicable use cases demand them. No code, deployment, or production authorization is implied.

Decision provenance: founder's explicit conditional approval in ChatGPT conversation on 2026-11-06; this GitHub record preserves that design decision, but is not represented as a Part 11 electronic signature.


## Design-governance integration — 2026-11-06 (within conditional approval)
**Status:** GDP-001 is the reference design standard for future PROTECT module specifications and controlled milestone records. This integration is a design-governance update only, not a new founder approval, effective SOP, validated application control, or deployment.

### Applicability decision matrix (provisional; assess by intended use)
| Context | Record owner / authoritative system | GDP treatment |
|---|---|---|
| PROTECT requirements, architecture, source and qualification evidence | PROTECT controlled GitHub/design evidence | R1–R3, controlled versions and decision traceability; Part 11 not presumed solely because stored electronically |
| PROTECT processing configuration, runs, transformations, AI outputs, monitoring and audit evidence | PROTECT operational record service when implemented | R4; attributable, timestamped, source-linked and protected as required by risk and intended use |
| Client deviations, CAPAs, inspections, training, change control and approved GxP source records | Client's designated regulated QMS/system | R5; PROTECT references or ingests authorized copies, preserving provenance; no replacement of client approvals |
| Client BIA, continuity plans, recovery objectives and approved BCMS records | Client BCMS | Client remains authoritative; PROTECT-owned dependency registry maintains synchronized references, not duplicate approvals |
| Nonregulated client applications | Contractual/client policy plus minimum applicable quality baseline | Proportional GDP controls; do not automatically impose Part 11 |
| Regulated electronic records/signatures within predicate-rule scope | Designated accountable regulated organization/system | Assess 21 CFR Part 11, EU Annex 11 and applicable predicate rules; require qualified technical and procedural controls before use |

### Mandatory design review gates for subsequent modules
At module design review, identify: (a) source vs derived record and authoritative owner; (b) record class and mandatory metadata; (c) exact approval/version and lifecycle semantics; (d) retention and retrieval obligation or explicit TBD; (e) audit trail/signature applicability; (f) upstream/downstream provenance and changes affecting prior outputs; (g) exception/CAPA linkage. Reuse one existing module milestone/decision record; do not create parallel registers or archives.

### Decisions reserved for subsequent founder/quality approval
- Confirm specific regulated intended uses and Part 11/Annex 11 applicability at client/deployment level.
- Approve retention schedule and storage/archival arrangements by record class and client obligations.
- Name designated quality approval authority and authorize implementation/qualification scope.

Until decided, label these items **PROVISIONAL / NOT EFFECTIVE**. Do not infer technical controls exist from this guideline. No implementation, production activation, external action or additional testing is authorized by this design integration.
