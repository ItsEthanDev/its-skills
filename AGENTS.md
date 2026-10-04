# Repository Guidance

Read [README.md](README.md), [CONSTITUTION.md](CONSTITUTION.md), and the applicable feature specifications before changing skills or their resources.

## Collection conventions

Place each skill at `skills/<role-directory>/<skill-name>/SKILL.md`, using `stages`, `playbooks`, `techniques`, or `principles` as specified in [Skill Roles](specs/skill-roles/spec.md).

When adding or changing a script distributed by ItsSkills, read [Authoring ItsSkills bundled scripts](specs/nix-backed-scripts/authoring.md). This collection requires Nix-backed execution; scripts authored in other projects follow those projects' conventions. Check resource preservation through both supported installation paths when tooling is available and report unavailable paths as unverified.

When changing verification guidance, use the ownership map in [Self-Verifying Work](specs/self-verifying-work/spec.md). Keep reusable instruction owners distinct from project-specific recipes and expected behavior sources.

## Skill references and graph

Follow [Skill Dependency Graph](specs/skill-dependency-graph/spec.md). In runtime skills and supporting Markdown, reference another skill by its exact frontmatter identifier in inline code, not by a link into another skill's directory. Preserve conditional loading instructions and authority limits. Keep links to same-skill resources; repository navigation may still link to skills.

Every matching inline identifier contributes a dependency, including explanatory mentions. Avoid using a registered identifier for an unrelated command or concept; plain prose and fenced examples are not graph inputs. Regenerate the committed graph after changing references or source locations, and run its freshness check. See [graph tooling](tools/skill-graph/README.md) for commands and prerequisites.

## Specification scope

Create feature specifications for objectives that require coordinated behavior across skill or artifact owners and shared acceptance criteria. Keep an individual skill's executable guidance in `SKILL.md`; do not create one spec per skill or restate that guidance in a second owner. A reference to another skill alone does not justify a feature spec.

Update an existing specification when it already owns the shared requirement. Do not combine independent objectives into a feature merely because their skills are implemented together. Use [Feature Artifacts](skills/techniques/project-documentation/FEATURE-ARTIFACTS.md) when choosing the artifact.

## Skill writing

Write direct instructions that change an agent's decisions or actions. Do not include scope metacommentary in skills or supporting references: statements narrating the skill's role, what it owns, or which responsibilities belong elsewhere. Let the name, activation conditions, and procedure establish its scope.

Use the role model to classify and compose skills while authoring, not as commentary to insert into their runtime instructions. Keep role definitions in the authoring guidance and feature specification.

Preserve concrete activation conditions, handoffs, approval requirements, and safety rules. State them as operational instructions when needed. For example, permission to implement a mutation is not permission to execute it. Do not remove such a rule merely because it limits an action.
