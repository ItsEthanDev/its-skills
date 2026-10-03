# Repository Guidance

Read [README.md](README.md), [CONSTITUTION.md](CONSTITUTION.md), and the applicable feature specifications before changing skills or their resources.

## Skill writing

Write direct instructions that change an agent's decisions or actions. Do not include scope metacommentary in skills or supporting references: statements narrating the skill's role, what it owns, or which responsibilities belong elsewhere. Let the name, activation conditions, and procedure establish its scope.

Use the role model to classify and compose skills while authoring, not as commentary to insert into their runtime instructions. Keep role definitions in the authoring guidance and feature specification.

Preserve concrete activation conditions, handoffs, approval requirements, and safety rules. State them as operational instructions when needed. For example, permission to implement a mutation is not permission to execute it. Do not remove such a rule merely because it limits an action.
