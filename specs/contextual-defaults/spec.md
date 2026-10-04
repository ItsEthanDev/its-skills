# Contextual Defaults

## Outcome

Skills provide useful, well-chosen defaults without obstructing user requests or established project practices. An agent resolves discretionary choices from the applicable context before using a fallback, and loads fallback-specific detail only when it needs that branch.

The [constitution](../../CONSTITUTION.md), [skill roles](../skill-roles/spec.md), and [progressive disclosure](../progressive-disclosure/spec.md) govern this feature.

## Requirements

### CD-001: Resolve choices from context first

For a discretionary choice, a skill MUST direct the agent to follow explicit user direction, then applicable project conventions and accepted decisions, then its default when neither supplies the answer. This ordering MUST remain subject to instruction priority, binding requirements, authorization, and actual capabilities.

A skill MUST NOT require changing an otherwise valid project convention merely to match its default. Existing tools, artifact owners, formats, and workflows MUST be considered before introducing alternatives. Defaults MUST NOT be presented as mandatory requirements when other valid choices satisfy the intended outcome.

### CD-002: Distinguish defaults from binding requirements

A default is a choice used in the absence of a controlling request or convention. It does not waive a binding constraint or authorize an action. Skills MUST keep mandatory prerequisites and safety rules distinguishable from preferences.

When direction conflicts with a binding requirement or applicable sources leave consequential intent unresolved, the agent MUST surface the conflict rather than silently choose an override. It MUST NOT install tools, contact services, mutate data, or expand scope merely to make a default usable. The [Nix-backed execution requirements](../nix-backed-scripts/spec.md) for ItsSkills' bundled scripts remain binding collection policy, not an overridable consumer preference.

### CD-003: Supply useful defaults where appropriate

Skills SHOULD provide a concrete default for a recurring discretionary choice when one can be made without guessing product intent or authorization. When no generally useful default exists or the decision needs missing consequential information, the skill SHOULD instead identify the information or decision needed.

Defaults MUST fit the intended task, state their applicability conditions, and make relevant tool or environment prerequisites explicit. They SHOULD use the smallest sufficient approach without unnecessary dependencies, artifacts, or ceremony. If no particular tool or format improves the outcome, the guidance SHOULD prefer an existing suitable option rather than introduce one.

The agent MUST NOT add a routine approval pause merely to use a suitable default within existing authority. If a default is unavailable or unsuitable, it MUST select another supported choice within scope or report the specific blocker; it MUST NOT claim the fallback was executed successfully.

### CD-004: Keep selection guidance available

`SKILL.md` MUST contain enough guidance to identify the choice, apply precedence, recognize the default and its applicability, and know when to load a supporting reference. Conditions affecting permission, safety, feasibility, or conflict handling MUST be available before the agent commits to the choice.

General instructions that apply regardless of the selected option MUST remain available on their applicable branch. They MUST NOT be hidden solely inside a default-specific reference.

### CD-005: Disclose longer default-specific detail conditionally

Longer procedures, examples, or rationale useful only when a particular default is used SHOULD reside in supporting reference material with an explicit loading trigger. When that default is superseded by a request or convention, the agent MUST NOT be instructed to load that material merely to proceed with the selected alternative.

When a selected default requires a reference, the agent MUST read it before relying on its instructions. The main file MUST state both the reference location and the condition that selects it. Moving text to another file without a conditional pointer does not satisfy this requirement.

Short defaults MAY remain inline when that is clearer and cheaper than a separate reference. This feature MUST NOT require a reference per default, a fixed length threshold, or extraction of material merely because it mentions a default. [Progressive Disclosure](../progressive-disclosure/spec.md) owns the general resource-loading and authority rules; these requirements apply them to default selection.

### CD-006: Preserve operational ownership

Concrete defaults and their conditional procedures MUST stay with the skill or resource that governs the operation. Shared authoring guidance MUST establish precedence, default quality, and disclosure expectations without creating a second inventory of concrete defaults.

Runtime instructions MUST state actionable selection rules and loading conditions rather than narrate the shared feature's scope. References MUST preserve the caller's authority and the permitted directions defined by [Skill Roles](../skill-roles/spec.md).

## Acceptance cases

These cases define expected behavior, not evidence that the current collection already conforms.

| Case | Expected result |
| --- | --- |
| The user requests a supported diagram format different from the skill default. | Use the requested format within applicable constraints; skip instructions useful only for the superseded default. |
| A project has an established experiment directory and the user specifies no location. | Use the project directory rather than the skill's fallback; do not introduce a second convention. |
| Neither the request nor project conventions select a format or location, and the skill's default fits. | Use the stated default without a redundant approval pause. |
| The selected default requires a longer reference procedure. | Recognize the default and loading trigger in `SKILL.md`; load the reference before using its procedure. |
| A convention supersedes a default, but general clarity and permission checks still apply. | Retain those checks without loading default-only syntax, examples, or rationale. |
| A default is concise and needs no specialized procedure. | Keep it inline; do not create a reference solely to satisfy a packaging pattern. |
| A preferred tool is unavailable. | Use a suitable authorized alternative or report the blocker; do not install it automatically or claim unperformed checks passed. |
| A request conflicts with a binding execution prerequisite. | Explain the conflict and the prerequisite; do not treat preference ordering as an exemption. |
| The missing choice would establish product behavior or authorize an external mutation. | Obtain the required decision or authority rather than invent a fallback. |

## Boundaries

This feature establishes a collection-wide behavior and authoring contract. It does not select a universal toolchain, require a new runtime skill or router, prescribe every default, relax safety requirements, or mandate automated evaluation infrastructure. Conditional source instructions do not by themselves prove harness discovery behavior or measured context savings.
