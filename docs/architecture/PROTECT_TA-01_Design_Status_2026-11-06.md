# PROTECT — TA-01 Technical Architecture Handoff
**Date:** 2026-11-06  
**Status:** DRAFT — conditional design acceptance recommended; not approved for implementation.

## Scope and architectural direction
PROTECT is a modular Quality, Compliance, Operational Performance, and Operational Resilience intelligence platform. Initial architecture recommendation: **modular monolith**, with clear internal interfaces and independently configurable external connectors. This recommendation remains subject to founder acceptance.

## Functional baseline
- Functional mapping v2.2 is the consolidated draft review baseline.
- Preserve the original 105 cross-module relationships and 11 CAPA predictive factors (PF-01 through PF-11).
- Q01–Q11 and RI01 remain the functional design reference; Q05 remains reserved.
- The additional OR-X01–OR-X12 resilience relationships are **proposed**, not approved.
- R01–R06 are conceptual Operational Resilience capabilities, not six mandatory separate applications.

## Operational Resilience (approved direction)
PROTECT provides **resilience intelligence and monitoring**, integrating with a client's existing BCMS; it is not intended initially to replace that BCMS or deliver a full BCMS.
PROTECT maintains a critical-operations and dependency registry synchronized with client systems. The client's BCMS remains authoritative for approved BIA, continuity plans, recovery objectives and associated records.
Detailed integration, synchronization, thresholds and vendor decisions remain open.

## Technical components proposed in TA-01
1. Client source connectors: eQMS, ERP, CMMS, LMS, BCMS, and external regulatory sources.
2. Integration and data integrity: validation, provenance, synchronization and source ownership.
3. Domain functions: Quality, Compliance, Operational Performance, and Resilience.
4. Shared rules, risk signals, audit history and workflow authorization.
5. Management dashboards, early warnings, and improvement recommendations.

## Record-creation governance
Detection and record initiation may be configurable, including automatic or human-approved initiation, according to client authorization, risk classification and regulatory requirements. Formal regulated approvals, dispositions, product release, and execution remain separately governed. This is a design direction, not permission for autonomous regulated decisions.

## Open material decisions
- TA-D01: founder acceptance of modular-monolith starting architecture.
- TA-D03: tenant isolation, source ownership, traceability, and data integrity controls.
- TA-D04: detailed workflow authorization and record initiation/approval separation.
Nonessential vendor choices, deployment topology, scoring, technical contracts and other details are deferred under progressive risk-based acceptance.

## Scope restrictions
**No coding, deployment, production authorization, or predictive model development.** Predictive work is ON HOLD; preserve all 11 CAPA factors unchanged.

## Source artifact inventory (prepared outside this GitHub handoff)
- PROTECT_Consolidated_Architecture_DRAFT_v2.2.xlsx
- PROTECT_OR-01_Operational_Resilience_Integration_Assessment.md
- PROTECT_DR_v2.1_Consolidated_Design_Review.md
- PROTECT_TA-01_Consolidated_Technical_Architecture_DRAFT_v1.0.md

**Note:** This GitHub file is a controlled design-status handoff, not a claim that the four source artifacts themselves have been uploaded or reconciled in the repository. Preserve the originals for a later source-artifact import.

## Next milestone
Founder review of the three material TA-01 decisions, followed by a limited synthetic proof-of-concept plan only if explicitly authorized. Resume Aster ABI-001 separately; no PROTECT implementation begins.
