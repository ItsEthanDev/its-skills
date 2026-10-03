# Artifact Model

## Ownership and reconciliation

Identify the semantic claim before choosing its owner. A feature spec owns intended behavior; a plan owns technical approach and intended verification; tasks own current execution state; a contract owns the precise consumer-facing interface; code, schemas, and configuration own concrete declarations where appropriate; tests own executable assertions and CI or a report owns observed results. Governance constrains these owners. Link to a source rather than copying it when possible.

Use flow-back: a discovery or edit may begin in any artifact. Determine whether it changes intent, design, work, or merely the current implementation. Bring affected owners and their direct dependents into agreement. Search references to changed paths, headings, and IDs to find dependents; avoid maintaining reverse-reference lists. Do not choose the newest file as the source of truth. If two plausible interpretations would materially change the target and existing authority does not settle them, present the conflict and ask the user. Fix an obvious stale reference without a new decision.

A living spec describes the current target, even while code has not caught up. Delete obsolete target behavior instead of marking it deprecated. Git preserves earlier text. Keep an ADR or an older contract version when its history or compatibility is still needed. Feature directories represent coherent independently verifiable outcomes, not delivery stages.

A user-requested or jointly agreed target change may be recorded without a second approval. An agent-proposed material target change requires user direction before adoption. The active workflow owns any transition gate; this technique does not add one.

## Operational and declarative owners

When the user calls a choice operational, treat its *current value* as flexible during regular operation. Record where it is maintained and any intended durable limits, not the changing list or setting in a feature spec. If unclear whether the rule or only its instances vary, ask. Operational flexibility does not waive authorization, auditing, or governance.

When a user designates a declarative artifact as owner of a detail, reference the schema, configuration, or definition instead of copying its exact entries. Describe the intended capability, type of information, privacy boundaries, and other obligations in the spec as needed. The declaration can change independently only within those obligations. For an external consumer, follow the contract owner and compatibility process in [CONTRACTS.md](CONTRACTS.md), even if the authoritative schema lives in code.

## Conventions

If the project has no convention, use `specs/<feature-name>/` with `spec.md`, `plan.md`, and `tasks.md` when each adds distinct value. Stable IDs make individually discussable requirements and tasks easy to reference in conversation. Use a small consistent scheme, such as `REQ-001` and `T-001`; add story or outcome IDs only if useful. Preserve identities across wording changes and never reuse an ID for a different claim. Give dependent artifacts source links and IDs when relevant. Start from the templates when useful, and remove empty sections.

A task list is an active checklist. Remove obsolete tasks even if checked; retain completed tasks whose verified results remain useful, and add tasks for new gaps. Mark complete only after direct verification. Keep observed results in existing tests, CI, or delivery reporting where sufficient rather than duplicating a results table.
