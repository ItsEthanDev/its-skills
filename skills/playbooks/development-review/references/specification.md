# Specification review

Review desired behavior for product clarity, completeness, and readiness without choosing its implementation. Load `project-documentation` and its feature-specification guidance before applying this lens.

## Inspect

- **Problem and value:** The target identifies the affected actors, the problem, the desired outcome, and why the change is worth making.
- **Scope:** In-scope behavior, non-goals, assumptions, priorities, and dependencies prevent materially different readings.
- **Flows and states:** Normal, empty, boundary, failure, recovery, and success behavior are defined where users or external consumers can observe them.
- **Obligations:** Each requirement expresses one unambiguous, independently verifiable behavior with observable acceptance.
- **Outcomes:** Success criteria are measurable and technology-independent when the outcome genuinely needs a metric.
- **Consistency:** Behavior agrees with project governance, canonical domain language, related capabilities, and other accepted requirements.
- **Separation:** The specification does not settle libraries, schemas, file layouts, architecture, or other technical design that belongs in planning.
- **Readiness:** No unresolved product choice could materially change scope, security, privacy, data handling, or user experience downstream.

Stay within behavior and product intent. When a gap can be resolved responsibly, recommend concrete specification wording or behavior. Route technical questions to the project's technical-design owner rather than using them to reject a behaviorally complete specification.

## Complete the lens

Account for every normative obligation and acceptance scenario in the requested target. Identify missing behavior through concrete actor scenarios rather than generic checklist prompts. Route behavioral changes to the project's intended-behavior owner and terminology conflicts to its canonical-language owner. Identify their actual artifacts or locations.
