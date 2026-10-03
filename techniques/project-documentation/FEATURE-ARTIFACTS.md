# Feature Artifacts

Use established repository owners first. Otherwise group a coherent feature under `specs/<feature-name>/` and conventionally name its target `spec.md`, approach `plan.md`, and work checklist `tasks.md`. Do not create a file merely to fill out this set. Split features when their outcomes can be accepted, changed, or delivered independently and combining them obscures decisions, not by layer, sprint, or MVP stage. Use the small [spec](templates/spec.md), [plan](templates/plan.md), and [tasks](templates/tasks.md) starters when useful; omit unused sections.

## Specification

Describe the current intended outcome, relevant actors, scope, externally meaningful behavior, constraints, and significant failure cases. Distinguish desired behavior from current implementation. Use `MUST` for required behavior, `SHOULD` with its exception condition for expected behavior, and `MAY` for permitted behavior. Prefer observable examples or acceptance conditions in the format clearest for this feature; user stories and Given/When/Then are options, not required structure. Give separately discussable requirements stable IDs so the user can reference them in chat. Keep technical design and field-by-field schema copies out unless those particulars are themselves the intended constraint.

When the user designates a value operational, specify any durable rule governing it, not each current value. When a schema or configuration owns concrete details, reference it and state intent or constraints that the declaration cannot express. If an agent's discovery calls for a material target change, obtain user direction before treating it as accepted. A user-requested or jointly agreed change needs no duplicate approval. Remove legacy targets rather than accumulating deprecated requirements; preserve needed history in Git or a decision record.

## Plan

Describe the selected approach against the real implementation, affected interfaces, consequential unknowns, and direct verification for the target. Link the specification or its established substitute and any contract. Identify migration and rollback concerns when relevant. Let code or a schema own declarations that it expresses adequately; do not copy them into a plan. A planning discovery that changes intended behavior must be resolved with the user rather than quietly turned into design.

## Tasks

Record actionable remaining work, dependencies, and progress when a checklist helps. Link specific requirements or plan decisions when those links aid execution; use stable IDs for items the user may discuss. No fixed task grammar, phase structure, parallel marker, or exact-path rule is required. A checked task means its result was verified. On a changed target, remove irrelevant tasks even if completed, keep completed tasks whose verified results still apply, and add work for any new gap. Git retains the previous checklist; do not delete unfinished work to imply it was completed.

Research, data models, and validation procedures may have separate owners when they make a substantial question or verification clearer. Tests and CI normally own verification evidence; add a durable results record only when existing evidence cannot be located or interpreted later. See [CONTRACTS.md](CONTRACTS.md) for interface agreements and [ARTIFACT-MODEL.md](ARTIFACT-MODEL.md) for change reconciliation.
