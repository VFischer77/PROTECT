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
