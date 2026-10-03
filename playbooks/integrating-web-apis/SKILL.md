---
name: integrating-web-apis
description: Build or change code that communicates with a remote web API or receives webhooks. Use for integration implementation, not as a replacement for diagnosis or an authorized development review.
---

# Integrating Web APIs

Implement the behavior the application needs against the relevant remote contract. Keep implementation authority separate from permission to contact the service.

For diagnosis, use the [Diagnosing Bugs playbook](../diagnosing-bugs/SKILL.md) within its authorized scope. For an explicitly requested or scheduled review, use [Development Review](../development-review/SKILL.md). This playbook supplies implementation strategy; it does not initiate either workflow merely because integration code exists.

## Establish the relevant contract

Identify the behavior being changed, its service and version, and the request, response, or event contract it depends on. Investigate authentication, scopes, pagination, limits, errors, and retry behavior only where they affect that behavior. A parsing correction need not become a survey of the entire API.

Prefer official versioned schemas for wire shape, supported by official endpoint documentation and SDK types or source. Preserve documented constraints that a schema cannot express. Use repository evidence and permitted live responses as supporting evidence, not silent replacements for the documented contract. State consequential conflicts and inferences rather than guess.

## Choose a proportionate interaction

Inspect project rules, installed dependencies, existing clients, and nearby integrations. An SDK's existence alone does not establish a project convention.

Follow a suitable existing convention. Otherwise choose and report a routine, proportionate option. Ask when alternatives materially affect dependency ownership, maintenance, security, or architecture. Dependency installation still follows project authorization; selecting a client does not grant permission to install it or make a live call.

## Implement the affected boundary

Reuse a suitable interface. Introduce an adapter only when it concentrates meaningful vendor knowledge or supports real variation, not merely to wrap a single call. When validation or representation placement is uncertain, read [Boundary Discipline](../../principles/principle-boundary-discipline/SKILL.md). When interface depth or seam placement is uncertain, read [Design Deep Modules](../../principles/principle-design-deep-modules/SKILL.md).

Treat remote input as unknown. Validate and map the relevant data into application types, deriving wire types from an authoritative schema where available. Keep parsing and mapping pure where practical. Do not silently accept malformed data. Preserve error, timeout, cancellation, pagination, and retry behavior relevant to the application's contract.

When receiving webhooks, read [Inbound Webhooks](references/inbound-webhooks.md) before implementing or changing delivery handling. Payload shape alone does not establish sender authenticity.

## Verify locally and report

Test the affected behavior using documented examples, local fakes, or sanitized fixtures without credentials or network access. Cover request construction, parsing, mapping, and relevant failure behavior. Add pagination, retry, or missing-field cases when those are part of the change, not as a universal checklist. When test-first implementation applies, use [TDD](../../techniques/tdd/SKILL.md) at approved seams.

Keep live contract checks separate and disabled by default. Before any real API operation, use [Calling Web APIs](../../techniques/calling-web-apis/SKILL.md); implementing a mutation does not authorize executing it.

Retain useful, stable documentation links near the boundary when project conventions permit and the link preserves a non-obvious contract fact. Use [Project Documentation](../../techniques/project-documentation/SKILL.md) when a durable contract or decision needs an owner; do not create an artifact merely to record routine work.

Report the relevant contract evidence, consequential interaction choices, assumptions or conflicts, checks performed, and live behavior that remains unverified. Local modeled-contract tests do not prove actual provider compatibility. Return the result and control to the caller without expanding the assignment or initiating a stage transition.
