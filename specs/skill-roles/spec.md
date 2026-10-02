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

Skills MAY compose across roles within the reference restrictions in SR-005. Instructions that appear to overlap MUST be assigned to the role that owns the relevant decision. Other skills may refer to that guidance rather than duplicate its rules when the reference is permitted.

For example, readiness to leave an implementation stage belongs to a stage skill; choosing an investigation strategy belongs to a diagnosis playbook; tracing a code path belongs to a technique; a constraint on accepting a proposed fix belongs to a principle.

### SR-004: Role does not dictate packaging

Stage skills MAY represent individual stages or route to guidance for multiple stages. The same role boundaries apply in either design.

Role directories MUST NOT imply required category routers, invocation order, or hidden discovery. Routers and progressive disclosure are design choices based on selection needs and context cost. Directory nesting alone is not a promise that skill descriptions are hidden from an agent.

### SR-005: Directional operational references

An operational reference instructs an agent to load, invoke, or follow another skill. Operational references MUST follow this matrix:

| From / To | Stages | Playbooks | Techniques | Principles |
| --- | --- | --- | --- | --- |
| Stages | Allowed | Allowed | Allowed | Allowed |
| Playbooks | Forbidden | Allowed | Allowed | Allowed |
| Techniques | Forbidden | Forbidden | Allowed | Allowed |
| Principles | Forbidden | Forbidden | Forbidden | Allowed |

Stages may coordinate useful playbooks, techniques, and principles. Playbooks may compose supporting playbooks, techniques, and principles, but MUST NOT initiate stage transitions. Techniques may use supporting techniques and principles, but MUST NOT initiate playbooks or stage workflows. Principles may reference other principles, but MUST NOT direct execution through another role.

The restriction applies to instructions in both the main skill file and its supporting resources. Moving an instruction into a reference document does not change its role boundary.

Explanatory mentions and examples are not operational references unless they instruct the agent to load, invoke, or follow a skill. Documentation outside runtime skills MAY link across roles freely.

### SR-006: References preserve authority and control

An allowed reference MUST NOT be treated as authorization to execute the referenced skill. Its activation conditions and applicable project rules still govern execution.

Same-role references MUST preserve the caller's scope. Operational references MUST NOT form circular invocation or delegation chains.

A called skill MUST return control and its result to its caller. It MAY report that broader work is needed, but MUST NOT select and initiate a workflow forbidden by SR-005. The caller or requester decides what to do next within its own authority.

For example, a diagnosis playbook may invoke a tracing technique. The technique returns its findings; it does not start a diagnosis playbook in response to those findings.

## Acceptance conditions

- Each skill has one primary role and resides in its corresponding directory.
- Imported or adapted skills receive the same classification as locally authored skills.
- A skill's responsibilities match its role, and composition does not copy another role's rules.
- Both an individual-stage skill and a stage router are permitted without changing the role model.
- The layout can be used without introducing a router for every category or prescribing invocation order.
- Operational references, including those in supporting resources, follow the SR-005 matrix.
- Explanatory examples do not create operational dependencies merely by mentioning another role.
- A permitted reference does not bypass activation conditions or project authority.
- Same-role composition preserves scope and contains no circular invocation or delegation chain.
- A called skill returns control to its caller rather than initiating a forbidden broader workflow.

## Outside this feature

This feature does not select or add skills, define installation interfaces, require a role metadata field, or implement automated classification checks. Installation discovery must be verified when the installation paths are designed, rather than inferred from this source layout.
