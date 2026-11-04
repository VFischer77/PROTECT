# FR-001 — Mandatory ISO 9001 Foundation and Additive Requirements
Status: OWNER APPROVED architectural requirement (2026-11-03 conversation); design-only, not implemented or qualified.

## Intent
ISO 9001 requirements form the mandatory minimum PROTECT design and assessment baseline across client industries and service domains. Additional sector, legal, regulatory, contractual and specialized management-system requirements are layered on top. No profile can silently bypass baseline requirements. Use of PROTECT does not certify a client or demonstrate conformity without assessed evidence.

## Layer model
L1 ISO 9001 common QMS requirements baseline; L2 applicable specialized management frameworks (e.g. ISO 22301; ISO 31000 is guidance, not a certification requirements standard); L3 applicable industry, product, jurisdiction and contractual obligations (e.g. GMP, ISO 13485, FDA QMSR). Layers are additive where applicable; do not presume one document automatically supersedes another. Resolve apparent conflicts with explicit legal/technical review and traceable decisions.

## Requirement contract
For each requirement: unique ID, authoritative standard and edition, clause/reference, applicability and rationale, source/obligation type, affected process/module, expected evidence, observed evidence references, assessment result, assessor/reviewer, effective dates, change history and linked corrective action. Allowed states: conforming; nonconforming; not assessed; insufficient evidence; not applicable with documented justification. Not applicable cannot be used to bypass an actually applicable ISO 9001 requirement. Distinguish process-level findings from organization-wide QMS conformity claims.

## GC-001 integration
Select Industry and Service Domain once at workspace setup; derive additional obligation profiles and applicable sector overlays, never a module-level industry selector. ISO 9001 baseline is always present in PROTECT assessment logic. Controlled profile changes preserve historical interpretation and require impact assessment. Multi-jurisdiction/multi-industry work needs explicit scope mapping.

## Proportionality
Risk-based rigor, documentation, monitoring and sampling may vary where permitted by the applicable requirements. Do not impose GMP-only forms on professional services. ISO 9001 baseline coverage is not the same as performing a full ISO 9001 conformity audit in every limited-scope engagement. Explicitly label engagement scope, unassessed requirements and limits of conclusions.

## Edition control
Maintain a verified authoritative ISO 9001 edition and amendment register, including effective dates and transition requirements. Do not assume an edition or its clause wording without controlled source verification. Full clause-by-clause mapping remains OPEN pending authorized access to applicable normative text.

## Verification cases — proposed, not run
FR-T01 professional services retains ISO 9001 baseline without GMP-specific records.
FR-T02 medical device overlay adds applicable ISO 13485/QMSR obligations without removing ISO 9001 baseline.
FR-T03 specialized continuity overlay adds relevant ISO 22301 requirements.
FR-T04 unjustified N/A on applicable baseline is rejected.
FR-T05 missing evidence cannot produce conforming.
FR-T06 limited module assessment cannot produce full organizational conformity claim.
FR-T07 changed jurisdiction/edition triggers impact review with historical traceability.
FR-T08 duplicate equivalent requirements are linked without losing independent obligations.
FR-T09 conflicting requirements trigger documented review, not silent override.
FR-T10 low-data operation preserves deterministic and expert assessment while prediction remains unavailable.
