# Skill Roles

## Outcome

Each skill has a clear responsibility within a composable four-role model. The role defines which decisions the skill owns; the source directory makes that role visible to authors and readers.

This specification defines the intended organization. It does not imply that skills or installation tooling already exist. The [constitution](../../CONSTITUTION.md) governs the collection.

## Requirements

### SR-001: One primary role

Every skill MUST have exactly one primary role: stage, playbook, technique, or principle. Imported and adapted skills MUST follow the same rule.

Choose the role by the decision the skill owns, not its topic, tool, or position in a task sequence.

| Role | Owns | Does not own |
| --- | --- | --- |
| Stage | Work state, prerequisites, transition gates, and transition authority | The strategy for solving a particular problem |
| Playbook | A reusable strategy for a problem or outcome | Work-stage transition gates |
| Technique | A bounded, reusable operation and its result | The purpose or strategy of the larger task |
| Principle | Constraints on judgment that can change or reject a decision | A prescribed task sequence |

### SR-002: Source organization

Skills MUST reside under the root directory corresponding to their primary role:

```text
stages/<skill-name>/SKILL.md
playbooks/<skill-name>/SKILL.md
techniques/<skill-name>/SKILL.md
principles/<skill-name>/SKILL.md
```

Supporting resources belong with the skill they support. They do not become separate skills merely because they contain specialized guidance.

### SR-003: Composition without duplicated authority

Skills MAY compose across roles. Instructions that appear to overlap MUST be assigned to the role that owns the relevant decision. Other skills may refer to that guidance rather than duplicate its rules.

For example, readiness to leave an implementation stage belongs to a stage skill; choosing an investigation strategy belongs to a diagnosis playbook; tracing a code path belongs to a technique; a constraint on accepting a proposed fix belongs to a principle.

### SR-004: Role does not dictate packaging

Stage skills MAY represent individual stages or route to guidance for multiple stages. The same role boundaries apply in either design.

Role directories MUST NOT imply required category routers, invocation order, or hidden discovery. Routers and progressive disclosure are design choices based on selection needs and context cost. Directory nesting alone is not a promise that skill descriptions are hidden from an agent.

## Acceptance conditions

- Each skill has one primary role and resides in its corresponding directory.
- Imported or adapted skills receive the same classification as locally authored skills.
- A skill's responsibilities match its role, and composition does not copy another role's rules.
- Both an individual-stage skill and a stage router are permitted without changing the role model.
- The layout can be used without introducing a router for every category or prescribing invocation order.

## Outside this feature

This feature does not select or add skills, define installation interfaces, require a role metadata field, or implement automated classification checks. Installation discovery must be verified when the installation paths are designed, rather than inferred from this source layout.
