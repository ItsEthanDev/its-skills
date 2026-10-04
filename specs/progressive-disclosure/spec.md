# Progressive Disclosure

## Outcome

An agent can use a skill's essential guidance without loading every specialized procedure or reference. Detail becomes available when the task needs it.

The [constitution](../../CONSTITUTION.md) and [skill-role specification](../skill-roles/spec.md) govern the collection.

## Requirements

### PD-001: Essential guidance in the main skill

Each skill MUST keep the guidance needed on every invocation in `SKILL.md`. The agent MUST be able to identify the skill's purpose, activation conditions, and essential actions without reading all supporting resources.

The main file MUST NOT require unconditional loading of branch-specific material that is irrelevant to the current task.

### PD-002: Explicit on-demand references

Specialized procedures, tool-specific detail, and branch-specific guidance MAY reside in supporting resources. When a resource is needed, the skill MUST identify it and state when to read it.

The agent MUST load resources required for the selected branch before relying on their instructions. Unrelated branches need not be loaded.

For example, a presentation technique may keep surface selection in its main file and browser-specific instructions in a reference loaded only when a browser is the requested surface.

[Contextual Defaults](../contextual-defaults/spec.md) defines precedence and the conditional disclosure of detail useful only when a particular default is selected.

### PD-003: Scope survives disclosure

Moving guidance into a supporting resource MUST NOT change its responsibility or authority. Supporting instructions MUST obey the skill's role, operational-reference restrictions, and inherited scope defined in the skill-role specification.

A supporting resource is not an independently selectable skill merely because it contains specialized guidance. A distinct reason for independent invocation MAY justify a separate skill; its own role and activation conditions must then be defined.

### PD-004: No prescribed router architecture

Progressive disclosure MUST NOT require a router for every role or impose a fixed file size or reference count. Packaging remains a design choice based on the guidance needed for selection and execution.

Directory nesting alone MUST NOT be treated as evidence that a skill's description is hidden from initial agent context. Claims about discovery or context reduction require evidence from the applicable consumer.

## Acceptance conditions

- The main skill provides enough guidance to select and begin the relevant work without loading every resource.
- Each required resource has a clear location and loading condition.
- A task requiring one branch can proceed without loading unrelated branch instructions.
- Selected branches receive their required guidance before execution.
- Supporting resources preserve role and authority boundaries.

## Outside this feature

This feature does not add skills, define harness-specific discovery behavior, require routers, or establish automated context measurements or evaluation tooling.
