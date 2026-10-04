# Plan review

Review whether an accepted behavioral contract has a sufficient, economical, and verifiable technical design. Load `project-documentation` and its planning guidance before applying this lens. When interfaces, seams, or testability materially affect the design, load `principles` and select `principle-design-deep-modules`.

## Inspect

- **Accepted input:** The plan references accepted behavior and applicable governance without weakening, reinterpreting, or adding user-visible obligations.
- **Reality:** Proposed paths, modules, interfaces, commands, dependencies, and constraints match the current codebase.
- **Traceability:** Every accepted requirement maps to a technical change, direct evidence, and executable work; every planned change and task has upstream justification.
- **Design economy:** The approach is the smallest coherent design that satisfies the accepted behavior and known constraints without speculative layers or compatibility paths.
- **Interfaces and seams:** Changed modules provide useful depth, concentrate policy with locality, expose an appropriate test surface, and add adapters only where variation is real.
- **Verification:** Evidence exercises the relevant public behavior, covers meaningful failure paths, and can distinguish success from a proxy or self-report.
- **Delivery:** Dependencies, ordering, vertical slices, and parallel claims reflect actual prerequisites and conflicting state.
- **Operations:** Data transitions, migration, rollback, deployment, compatibility, observability, performance, and security are addressed when the change creates those concerns.
- **Unknowns:** Consequential technical choices are resolved with evidence or explicitly block implementation; behavioral discoveries have been reported to the project's intended-behavior owner.

## Complete the lens

Trace every accepted requirement through design, evidence, and executable work. Inspect the real implementation context for each consequential design claim. Route behavioral gaps, technical changes, domain conflicts, and governance conflicts to the project's corresponding intended-behavior, technical-design, domain-language, and durable-rule owners. Identify actual artifacts or locations rather than invoke stages.
