# Domain review

Review canonical project language and context ownership. Load `project-documentation` and its domain-context guidance before applying this lens.

## Inspect

- **Canonical language:** Each project-specific concept has one preferred term and a distinguishable meaning; competing or overloaded language is explicit.
- **Identity:** Scenarios make clear when two references represent the same concept and what, if anything, changes that identity.
- **Lifecycle and invariants:** Relevant states, transitions, and truths that must remain valid are understandable without implementation detail.
- **Relationships and ownership:** Relationships between concepts identify direction, responsibility, and ownership where ambiguity would change behavior.
- **Context boundaries:** Each context has a coherent responsibility, and cross-context language or relationships identify both roles.
- **Concrete scenarios:** Ordinary, boundary, and failure scenarios expose ambiguity that glossary definitions alone can hide.
- **Reality:** Specifications, interfaces, and relevant code use the canonical terms consistently or reveal a conflict that needs an owner.
- **Separation:** Definitions do not absorb feature requirements, storage design, technical architecture, or session notes.

Review the project's chosen domain model. Do not require aggregates, entities, value objects, foreign keys, repositories, persistence, or other tactical DDD structures unless the target claims to model them and the project needs them.

## Complete the lens

Exercise each affected concept through enough concrete scenarios to expose material ambiguity in identity, lifecycle, relationships, and context ownership. Route canonical terminology and context changes to the project's domain-language owner, behavior changes to its intended-behavior owner, and technical representation to its technical-design owner. Identify their actual artifacts or locations.
