# PROTECT–GOV–001–SEC–001 — Security & Deployment Qualification Strategy
**v0.1 — PROPOSED CONTROLLED BASELINE; founder approval pending**

## Decision and scope
Initial commercial deployment target: **customer-hosted licensed software**, subject to founder approval and product architecture assessment. Development/verification may use controlled local and cloud environments with synthetic or authorized test data. Fischer-Carballo-operated production SaaS is **deferred**, not authorized. This strategy does not assert that customer-hosted deployment eliminates supplier cybersecurity duties.

## Supplier software security minimum
1. Restricted repository and build permissions, MFA, least privilege, protected release process and documented approvals.
2. Dependency and third-party component inventory, vulnerability review and proportionate remediation.
3. Secure coding and review for authentication, authorization, input handling, secrets, logging, data boundaries and update mechanisms.
4. Versioned, integrity-verifiable release artifacts; documented supported runtime and configuration.
5. Threat/risk assessment tied to intended use, data categories, interfaces, misuse and human decision controls.
6. Security defect intake, customer notification criteria, patch/rollback and supported-version policy.
7. Risk-based security verification of high-impact misuse cases before release; retain evidence and disposition.

## Customer-hosted deployment qualification
Supplier provides installation prerequisites, supported topology, configuration baseline, integration/data-flow specification, secure configuration guide, installation verification protocol, upgrade/rollback instructions and supplier verification/validation summary. Customer is responsible for infrastructure selection/qualification, identity administration, backup/recovery, network operations, site-specific configuration, user procedures and intended-use validation unless contracted otherwise. A shared responsibility matrix must be signed or incorporated into agreement.

## Cloud development versus cloud production
Use of GitHub or cloud-hosted development/testing tools does not automatically create a production SaaS validation obligation. Qualify or assess those tools proportionate to their impact on software quality records, code integrity, build/release evidence and regulated use. Avoid unapproved customer production data in development environments.

## SaaS future gate (not part of initial release)
Require separately approved architecture, hosting-provider assessment, tenant isolation, security/privacy model, data residency/retention, backup and recovery, monitoring, incident response, service levels, cloud infrastructure qualification and operational validation before SaaS commercial launch.

## Constraints and open decisions
Final product architecture, licensing method, deployment package, supported platforms, data types, applicable GxP/Part 11/Annex 11 obligations, contractual allocations and security acceptance criteria remain open. No security certification, cloud validation, production qualification or commercial release is claimed by this document.

## Approval
Founder product/technical owner: PENDING
Independent quality/security review: PENDING
Effective date: NOT ASSIGNED
