# Skill Dependency Graph

## Outcome

GitHub visitors can inspect a committed Mermaid view of skill dependencies without cloning or building the repository. Consumers can use committed machine-readable graph data to determine the dependencies of a selected subset and the potential impact of changing a skill.

The [constitution](../../CONSTITUTION.md), [Skill Roles](../skill-roles/spec.md), [Progressive Disclosure](../progressive-disclosure/spec.md), and [Contextual Defaults](../contextual-defaults/spec.md) govern this feature.

## Requirements

### DG-001: Exact name-based references

Runtime skill instructions and supporting Markdown MUST reference other skills by their exact frontmatter `name` in inline code, rather than links to other skills' files. Existing cross-skill links MUST be migrated without losing their loading conditions, intended instruction, or authority limits. Links to resources within the same skill remain supported. Repository navigation and specifications MAY link to skill files.

An inline-code span whose complete content matches a registered skill identifier MUST create a dependency from its owning skill to that identifier. All such references count, whether explanatory, conditional, or an explicit invocation. Ordinary prose, YAML frontmatter, fenced code examples, and Markdown comments MUST NOT create dependencies. Duplicate references MUST produce one edge; self-references MUST NOT produce edges. Unmatched code spans MUST be ignored, since they can name commands, paths, and symbols. No conditional markers or edge types are required.

Name-based references do not guarantee that a consumer has installed or can discover the referenced skill. Reference syntax MUST NOT grant execution authority or replace activation conditions.

### DG-002: Source-derived graph and provenance

Each skill under `skills/` MUST have one graph node identified by its frontmatter name, with its role and repository-relative source location. Source discovery MUST follow SR-002; it MUST NOT scan repository documentation or maintenance tooling as skill sources. References in supporting Markdown MUST contribute to their owning skill's dependencies. The generator MUST retain source locations for dependency evidence and include skills without dependencies.

The graph MUST be generated from the same source instructions used by consumers, not a second hand-maintained dependency inventory. Ordering and serialization MUST be deterministic, with no timestamps or machine-specific paths. Resource-only links MUST NOT create separate skill nodes.

### DG-003: Committed visual and machine-readable outputs

The repository MUST commit `DEPENDENCIES.md` with a GitHub-compatible fenced Mermaid graph grouped by role, a direction legend, and a dependency table with source links. An arrow from A to B means that A references B. README MUST link to this view.

The repository MUST also commit machine-readable JSON graph data derived from the same graph. Its documented structure MUST expose identifiers, roles, source locations, and direct dependency relationships so consumers can calculate transitive dependency and reverse-dependency sets. Schema particulars belong to the generator and its tool documentation rather than a second declaration in this spec.

Focused visual views MAY be added when they make a dense graph easier to read; a separate view for every skill is not required.

### DG-004: Conservative dependency and impact semantics

A conservative installation set is the selected skills plus every transitively referenced skill, without removing dependencies merely because a particular invocation may not use them. Supporting resources remain part of their owning skill, not independently installable graph nodes.

Reverse dependencies identify direct and transitive users that may be affected by a changed skill. A changed supporting resource maps first to its owning skill. These relationships indicate potential impact, not proven breakage or a requirement to modify every caller.

This feature MUST NOT provide dependency-aware installation tools, package resolution, or installer integration. The committed graph data enables consumers to calculate these sets using their own tooling; query commands are not required for this feature.

### DG-005: Validation and freshness

Generation MUST validate unique valid identifiers, source-directory identity, dependency role directions, and absence of cycles. The conservative dependency graph MUST obey the existing role-direction matrix, without introducing permission to invoke otherwise forbidden roles. Existing cross-skill links in runtime Markdown MUST be rejected after migration, including links into another skill's resources.

The repository MUST provide an explicit regeneration command and a non-mutating check that fails on missing, invalid, or stale committed outputs. CI MUST run that check and the generator's tests. Diagnostics MUST identify offending sources or stale outputs; invalid input MUST NOT silently produce a partial successful graph.

Shared authoring and repository guidance MUST establish the reference convention and output regeneration expectations. Script execution MUST follow the applicable repository dependency policy without installing prerequisites into the user's profile.

## Acceptance cases

- A known identifier in inline code creates one dependency; repeated references do not duplicate edges, and a self-reference creates none.
- A plain-text skill name, an unknown inline-code identifier, a comment, frontmatter, or a fenced example creates no dependency.
- A supporting resource references a skill: the dependency and evidence belong to the resource's owning skill.
- A migrated reference retains its conditional loading instruction and permission boundary; same-skill resource links and repository navigation remain valid.
- An isolated skill appears as a node with no outgoing dependencies.
- A chain A to B to C supports the conservative set A, B, C and identifies A and B as potential users of C from the exported direct relationships.
- Duplicate identifiers, invalid source identity, forbidden role directions, cycles, or residual cross-skill links fail with source diagnostics.
- Repeated generation from unchanged sources produces identical Markdown and JSON; changing an identifier reference makes check mode fail without rewriting files until regeneration.
- The committed Markdown contains the complete Mermaid graph, grouping, legend, and source-linked table; JSON describes the same nodes and edges.
- Consumers receive data and documentation, not an installation command or a claim that missing dependencies are automatically resolved.

## Boundaries

This feature does not change skill activation or runtime permission rules, implement Nix or skills CLI installation, or infer dependencies from arbitrary prose. GitHub rendering, consumer discovery, and resource preservation must be reported as unverified when those interfaces cannot be exercised. General permission and loading guidance remains applicable even when a dependency is not used during a particular invocation.
