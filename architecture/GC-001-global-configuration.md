# GC-001 — One-Time Global Configuration (design requirement)

**Status:** Owner-approved architecture clarification, 2026-11-03. Design only; not implemented or tested.

## Trigger and scope
At creation of each PROTECT client engagement or analytical workspace, the authorized configurator selects **Industry** and **Service Domain** once. They are separate selections but form one workspace profile. The setup is not repeated at Q01, Q02 or any subsequent module. A distinct workspace may have a different profile.

### Industry options (extendable)
Pharmaceuticals; Biotechnology; Medical Devices; General Manufacturing; Professional & Business Services; Other Industries.

### Service Domain options (extendable)
GMP/Quality; Operational Excellence; Enterprise Risk Management; Business Continuity & Resilience; Combined Services.

## Requirements
- **GC-001:** Trigger configuration once at initial workspace setup.
- **GC-002:** All applicable modules inherit the same workspace profile automatically; no module-level Industry or Service Domain dropdowns.
- **GC-003:** The profile determines applicable modules, terminology, regulatory/industry context, and contextual applicability of shared CC-01–CC-30 criteria. Modules evaluate only relevant criteria; the master criteria library remains shared.
- **GC-004:** Preserve client-provided original classifications separately; absence of a classification is not None.
- **GC-005:** Subsequent configuration changes require authorized, traceable workspace-level change control, impact assessment for affected modules and outputs, and consistent reapplication; never silently change historical interpretations.
- **GC-006:** Module-specific event facts and analytical parameters may still be collected; they do not constitute repeated global Industry/Service Domain selection.
- **GC-007:** Multi-industry or multi-domain work requires an explicit, authorized workspace profile design/extension; do not assume one selection is sufficient for materially distinct regulated contexts.

## FR-001 foundation override
Every configured workspace inherits the mandatory ISO 9001 requirements baseline. Industry/Service Domain determine additional applicable overlays and proportional workflows, not removal of the common baseline. See `architecture/FR-001-layered-requirements-foundation.md`. The requirements register must distinguish not assessed, insufficient evidence, justified non-applicability, conforming and nonconforming. A limited-scope module assessment does not establish full organizational conformity.

## Traceability
Applies to PROTECT architecture and all current/future modules, specifically Q01 v0.8 and Q02 v0.2. Does not alter Q01's conditional acceptance or Q02's conditional acceptance status.

## Proposed verification (not executed)
- GC-T01: Initialize once; all active modules receive identical profile.
- GC-T02: Navigate Q01 to Q02 without second selection.
- GC-T03: Inapplicable module/criteria not enabled merely by module defaults.
- GC-T04: Authorized profile change produces impact review and audit trail.
- GC-T05: Historical outputs remain traceable to profile version.
