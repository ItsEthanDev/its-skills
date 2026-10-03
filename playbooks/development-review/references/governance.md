# Governance review

Review durable project rules for fitness as authority. Load `project-documentation` and its project-governance guidance before applying this lens.

## Inspect

- **Classification:** Each rule belongs in durable governance rather than a feature specification, implementation plan, agent instruction, or description of current behavior.
- **Force:** Normative language identifies a concrete obligation and does not disguise a preference or slogan as policy.
- **Compliance:** Each obligation has an observable signal that later work can provide without subjective interpretation.
- **Authority:** Ownership, precedence, amendment behavior, and conflicts with other instructions are explicit.
- **Composition:** Rules work together without contradiction, circular dependency, or an exception that silently defeats another obligation.
- **Cost and aging:** The rule remains defensible under realistic maintenance, migration, growth, and failure scenarios. Its rigidity is proportional to the invariant it protects.
- **Coverage:** Consequential project-wide obligations involving architecture, security, state, verification, or supported interfaces are not left to accidental convention.
- **Dependents:** Direct specifications, plans, instructions, and checks still agree with amended governance.

Judge the governance actually chosen by the project. Do not impose generic requirements for a particular technology, scale target, performance budget, team structure, or process.

## Complete the lens

Inspect every normative rule in the requested governance target. Report ambiguity with the conflicting plausible interpretations, and support missing-rule findings with a concrete recurring decision that lacks an owner. Route governance changes to the project's durable-rule owner and dependent inconsistencies to the artifact that owns the inconsistent claim. Identify actual project owners rather than prescribe a stage or file layout.
