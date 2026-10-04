---
name: stages
description: Coordinate constitute, specify, plan, and implement work, or a requested stage. Select stages according to unresolved decisions and project requirements rather than enforce a fixed sequence.
---

# Development Stages

Use the requested stage, or select according to the decision:

- Durable project rules: [Constitute](references/constitute.md).
- Intended behavior: [Specify](references/specify.md).
- Approach and verification: [Plan](references/plan.md).
- Authorized delivery and completion evidence: [Implement](references/implement.md).

Load only references relevant to the work.

## Select applicable stages

A full-workflow request authorizes coordination of the stages needed for that work, not an obligation to perform all four. Existing governance may need no Constitute work. A small change may move directly from Specify to Implement when the target and approach are sufficiently clear and project rules do not require separate planning. Stages may be combined or skipped when their decisions are already resolved; do not manufacture artifacts or approval gates to fill a sequence.

A request for one stage does not authorize the next. At its boundary, return the result and identify remaining decisions. Revisit earlier decisions only within the assignment; report an out-of-scope need to an authorized caller or requester.

Skipping a separate stage does not waive unresolved decisions, verification obligations, or project-specific gates. Apply the project's actual readiness and transition rules.

## Preserve authority

A user request or joint conversation that establishes a target is sufficient direction to record it; do not demand a second approval of the user's own decision. Before adopting an agent-proposed material target change, present it and obtain direction. Ask when conflicting artifacts leave consequential intent unclear. Respect explicit user-requested pauses and stricter project governance.

When maintaining artifacts, use `project-documentation` for owner selection and reconciliation. References do not grant execution authority. Every call inherits the assignment's scope, may receive a narrower scope, and returns results and control to its caller.

## Handoff

After a material change, reconcile affected artifacts through their canonical owners before proceeding within the authorized workflow. Report what target or design changed, what remains unresolved, and what was verified. Do not create a persistent handoff file unless an established owner or explicit request calls for one.

Do not infer authorization for formal review, publication, deployment, or broader implementation from completing a stage.
