# P05.7 — Recommendations, Comments & Action Decisions
**Status: Draft implementation; founder review and technical qualification pending**

## Design decision
PROTECT is an intelligence and human decision-support layer, **not** a CAPA repository or full action-management system. Provide a simple, initially fixed decision dropdown with future configurable options; allow comment/rationale and optional proposed action description. Do not treat a proposed action as an execution task. External eQMS remains the authoritative CAPA system.

## Initial dropdown
Further investigation required; Continue monitoring; Recommend improvement; Recommend CAPA initiation; Accept recommendation; Reject recommendation; Other — specify. Labels and classifications remain subject to founder review. These choices are **management dispositions**, not regulatory severity classes.

## Data and governance
Future production persistence must use authenticated actor identity, server-side timestamps, append-only decision/comment history, permissions, and audit trail. The pilot Python contract validates inputs but does **not** implement authenticated persistence. The static browser preview copies an explicitly unsaved draft only; it does not save or send any data.

## Future eQMS initiation
Reserve a future **Initiate CAPA** capability, currently disabled. Requires authorized human confirmation, qualified vendor-specific connector, external acknowledgement before showing success, idempotency/error handling and no CAPA lifecycle replication. A referral recommendation is not a created CAPA.

## Exclusions
No live CAPA creation, external writes, client records, task execution tracking, custom dropdown editor, database persistence, release, or production hosting.

## Founder review
Approve/revise initial dropdown wording, minimal comment fields, whether action-detail text should be mandatory for improvement/CAPA referral, and future customizable options.
