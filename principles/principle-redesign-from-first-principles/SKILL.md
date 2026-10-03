---
name: principle-redesign-from-first-principles
description: "Apply when integrating a requirement into an existing design. Evaluate the design as though the requirement had been known from the start, without assuming authority for a broad rewrite."
disable-model-invocation: true
---

# Redesign From First Principles

Use a new requirement to reconsider the design, not merely to append a special case. Ask what the system would look like if that requirement had been a foundational assumption.

- Understand the affected design well enough to distinguish essential structure from historical accident.
- Prefer a coherent design that accommodates the accepted requirement over layers added only to preserve an obsolete shape.
- Consider affected types, documentation, examples, and rationale so the proposed change is internally consistent.
- Balance the cleaner design against migration cost, risk, and the smallest change that satisfies the assignment. A from-scratch comparison is a reasoning tool, not an instruction to rewrite everything.

Reconcile affected dependents within authorized scope. Report necessary broader changes for a decision by an authorized caller or requester. This principle does not expand the assignment or determine delivery sequencing.
