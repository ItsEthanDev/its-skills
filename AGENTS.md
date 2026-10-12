# Repository Guidance

Read [README.md](README.md) and [CONSTITUTION.md](CONSTITUTION.md) before changing skills or their resources.

## Collection conventions

Place each skill at `skills/<role-directory>/<skill-name>/SKILL.md`, using `stages`, `playbooks`, `techniques`, or `principles`.

Scripts distributed by ItsSkills require Nix-backed execution with repository-owned, pinned dependencies; scripts authored in other projects follow those projects' conventions. Missing Nix must fail clearly without an automatic installation attempt. Check resource preservation through both supported installation paths when tooling is available and report unavailable paths as unverified.

When changing verification guidance, keep reusable instruction owners distinct from project-specific recipes and expected behavior sources.

## Installation profiles

When adding, renaming, or removing skills, review Recommended membership and update the authoritative command and counts in [README.md](README.md). Apply these membership rules:

- Exclude stages.
- Include playbooks selectively when they provide useful problem-solving strategies without requiring adoption of the collection's development lifecycle.
- Include techniques by default, with exceptions for those unsuitable for the curated starting point.
- Include `principles` with all its bundled references.

Maximal selects all available skills; do not maintain a separate inventory for it.

## Skill references

In runtime skills and supporting Markdown, reference another skill by its exact frontmatter identifier in inline code, not by a link into another skill's directory. Preserve conditional loading instructions and authority limits. Keep links to same-skill resources; repository navigation may still link to skills.

## Skill writing

Write statements that change an agent's decisions or actions. Omit prose that merely describes the skill's purpose or role, or redundantly restates metadata. Declarative statements establishing agent responsibilities or decision authority are operational guidance, not scope metacommentary.

Use the role model to classify and compose skills while authoring, not as commentary to insert into their runtime instructions. Keep role definitions in the authoring guidance.

Preserve concrete activation conditions, handoffs, approval requirements, and safety rules. State them as operational instructions when needed. For example, permission to implement a mutation is not permission to execute it. Do not remove such a rule merely because it limits an action.
