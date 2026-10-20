# Project Constitution

**Status:** Ratified
**Version:** 1.1.0
**Ratified:** 2026-10-12
**Last amended:** 2026-10-19

## Purpose and scope

This constitution establishes durable constraints for ItsSkills' skills,
supporting resources, project guidance, and distributions.

## PR-001 — Composable skills

Each skill MUST have a clear purpose and invocation boundary. Shared guidance MUST have one canonical owner; consuming skills MUST reference that owner rather than duplicate its rules.

**Compliance signal:** New or changed skills identify when they apply. Guidance shared by multiple skills has an authoritative source and references from its consumers.

## PR-002 — Deliberate context use

Skills MUST keep universally needed instructions inline and disclose branch-specific guidance through pointers that state when to read it. Skill descriptions MUST identify invocation conditions; user-invoked descriptions MUST state the task they serve.

**Compliance signal:** New or changed descriptions make invocation clear. Required references have explicit reading conditions, and branch-specific material is loaded only when relevant.

## PR-003 — Attribution

Distributions of copied or adapted material MUST preserve applicable copyright and permission notices. Attribution MUST distinguish known provenance from unresolved lineage and MUST NOT imply upstream authorship of unrelated material.

**Compliance signal:** A distribution of copied or adapted material includes its applicable notices. Provenance claims match the evidence recorded in [Third-party notices](THIRD-PARTY-NOTICES.md).

Each skill directory includes its provenance and applicable license files, as documented in the [README](README.md#license). Individual-directory distributions must retain those files; collection-level notices alone do not cover a distribution that omits them.

## Governance

- Amendments require explicit approval from the project maintainer before
  taking effect. Approval must identify the proposed amendment in a recorded
  review or conversation. An agent's proposal is not ratification.
- Approved amendments MUST update the version and amendment date.
  The ratification date records the constitution's original adoption.
- A changed or removed principle MUST be reconciled with dependent
  specifications, plans, instructions, and checks.
