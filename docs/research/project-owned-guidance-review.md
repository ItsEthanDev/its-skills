# Upstream review: project-owned guidance

## Status and conclusion

This is a source comparison and design review, not a ratified project decision or evidence that one prompting architecture performs better. No implementation changes are made by this review.

Project-owned methods are a coherent extension of upstream's existing project-owned configuration. The domain-language and decision-record migration substantially preserves the upstream method. Its largest unverified risk is activation: whether agents actually load and apply the local guidance at the right time after the skill descriptions and explicit skill calls disappear.

Recommend a bounded trial of the two migrated methods, with behavioral comparison before further retirement. Commit and constitute need separate completeness checks; they are local original skills, not two additional upstream Matt Pocock skills being copied.

## Sources and comparison scope

Upstream snapshot: `mattpocock/skills` at `5beb35b040e3de97e54fa9e386d7e42d15c295c2`, obtained from the repository's HEAD during this review. Local attribution pin: `49dd158d1076134a641b33efb035946536778336`.

Primary source files:

- [Current domain-modeling skill](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/SKILL.md).
- [Pinned domain-modeling skill](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md).
- [Glossary format and rules](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/GLOSSARY-FORMAT.md).
- [ADR format, criteria, examples, and numbering](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling/ADR-FORMAT.md).
- [Current setup skill](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/SKILL.md).
- [Current generated domain-guide seed](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/setup-matt-pocock-skills/domain.md).
- [Upstream domain-modeling explanation](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/docs/engineering/domain-modeling.md).
- [Upstream setup explanation](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/docs/engineering/setup-matt-pocock-skills.md).
- [Hard versus soft setup dependency ADR](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/.agents/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md).

The three domain-modeling source files were fetched at both revisions and compared byte-for-byte. All are unchanged between the pinned and current revisions:

| File | SHA-256 at both revisions |
| --- | --- |
| `SKILL.md` | `7b925d7b1e341a2eeae33ad68a8a8c0ab889a38ddd22a7598e4c240e5a7556a3` |
| `GLOSSARY-FORMAT.md` | `21dcc40cdec8e151a829b98ab1517c1867bc444e3665134a98c6983411996801` |
| `ADR-FORMAT.md` | `944c92aa790e8fbdc9199640b170979abb8a34ba8d0fe18c2a01a63bce140ca0` |

Local material reviewed: the setup skill, references and generated-document seeds; the migrated wayfinder/architecture-review callers; and the still-present commit/constitute skills and their provenance. The working branch is based on `63c4dfe`; an existing uncommitted discovery-reference edit was inspected but not changed. References in this report are relative to the report's location where applicable.

Upstream's explanatory docs are useful first-party accounts of intended behavior and reported problems. They are not controlled benchmarks. Where prose and the executable instruction file differ, do not infer tool behavior from the prose alone: for example, the current setup skill instructs label creation while its explanation says it does not create labels.

## What upstream actually owns

Matt's upstream `domain-modeling` combines glossary maintenance and ADR behavior in one model-invoked skill. Our former domain-language and decision-records bundles were local splits, not two distinct upstream skills.

Upstream setup already writes per-project tracker, label, and domain-layout configuration. The upstream explanation explicitly describes these as repository-specific Markdown consumed by otherwise identical skills. The new proposal moves further: the active methods themselves, not only their configuration, become project-owned.

Upstream's domain-modeling explanation reports two relevant limitations:

1. Automatic invocation is weak; other workflows can load the interviewing skill and skip domain modeling. It recommends invoking domain modeling explicitly when necessary.
2. The bundled ADR conventions can conflict with an established project format; project agent docs or a local copy are described as workarounds.

The explanation also recommends project-specific domain guidance as a workaround for another gap: checking prior terminology decisions recorded in the issue tracker. These observations support project-level customization but do not constitute an endorsement or a performance demonstration of retiring the skill.

## Method-preservation comparison

| Upstream value | Local proposal | Assessment |
| --- | --- | --- |
| Active modeling, not merely reading vocabulary | The generated domain guide opens with the active-discipline distinction. | Preserved. |
| Challenge conflicting terms immediately | The same instruction and cancellation example remain. | Preserved with glossary location made project-specific. |
| Sharpen vague/overloaded terms | The same account/Customer/User paragraph remains. | Preserved. |
| Stress-test concrete scenarios | The same scenario paragraph remains. | Preserved. |
| Cross-reference code with the user's claim | Code remains explicit for engineering; source material/artifacts extend it to other work. | Deliberate broadening, not removal. |
| Record resolved terms inline rather than batch at the end | The instruction remains, with project approval requirements added. | Preserved, but approval wording can weaken immediacy if interpreted as an extra gate. |
| Glossary is definitions only, never a spec or decision diary | The strong prohibition remains. | Preserved and important; retain it verbatim where possible. |
| Tight definitions, rejected synonyms, context-specific terms, natural grouping | All four rules remain; the context-specific question broadens beyond programming. | Substantially preserved. |
| Multi-context map with relationships and scoped owners | Replaced by setup-resolved links/layout, with context relationships requested in the seed. | Intentional personalization, but the upstream concrete map example is no longer available in the output by default. Validate actual multi-context generation, not just backlinks. |
| Offer ADRs sparingly only when all three criteria hold | The same three criteria and rejection rationale remain. | Preserved. |
| A short context/choice/reason record; optional sections only when useful | Short format and optional sections remain. | Preserved. Status encoding and numbering are project choices instead of fixed assumptions. |
| Concrete examples of decisions that qualify | Engineering examples remain, with instructions to retain/adapt relevant examples. | Preserved; review generated adaptations so useful examples are not replaced with vague prose. |
| No prerequisites; create glossary/ADR directory lazily | Setup and project guidance replace automatic lazy bootstrap. | A real behavioral trade-off, accepted in principle by the user, not a wording-only refactor. |
| Model-invoked description and explicit consumer skill calls | Agent-entry-point conditions and project-document discovery replace them. | The largest unverified behavioral change. |

## Risks beyond the initial migration

### 1. Preserved text can still become inactive

An agent must encounter the active guidance before it can apply it. README links alone do not guarantee this. The current agent-navigation seed points through the README rather than directly linking each local owner, adding a discovery step.

Recommendation: keep the README as the human-facing index, but allow a direct, conditional pointer to the relevant guide in the actual harness-loaded entry point. The project owns that path; reusable skills still need not hard-code it. Verify which entry point the harness actually reads. Do not claim that either skills or project documents guarantee invocation.

### 2. Soft guidance can accidentally become a hard prerequisite

Upstream explicitly distinguishes hard dependencies (a tracker is required to publish to the correct place) from soft ones (vocabulary/ADR awareness can sharpen analysis without being required for all work). Its domain seed says to proceed silently when optional files are absent.

The local proposal instead asks when required guidance is missing and distinguishes explicit opt-out. That is sensible for establishing or changing a policy, but "required" needs a narrow meaning. An agent should not refuse ordinary architecture analysis merely because the project has no glossary or ADR practice. Ask when the missing policy is necessary to perform the requested artifact change correctly; let unrelated analysis proceed.

### 3. Approval can become ceremony

The local templates add approval and acceptance placeholders. This prevents invented policy but can accidentally turn "record the term the user just agreed to" into another approval round.

Recommendation: make the chosen project procedure explicit. Agreement on a definition can itself authorize recording it unless the project requires more. Do not conflate an ordinary term update with amending governance. Keep the upstream inline-capture instruction strong.

### 4. Project copies freeze both improvements and defects

Freezing conventions is part of the benefit, but fixes no longer arrive when an installed skill is updated. Projects may preserve a bug or an outdated tool procedure indefinitely.

Recommendation: record template origin/revision lightly enough to aid comparison, and offer explicit scoped review/migration. Preserve project edits and show substantive differences. Avoid automatic regeneration or a custom synchronization system. Even inside this repository, setup templates and the repository's own adopted guidance have different roles: improving a template does not silently amend the project's accepted practice.

### 5. The setup agent can paraphrase away the method

The templates preserve strong language, but setup still adapts them. A generated document could retain the headings and lose the behavioral triggers, examples, or glossary-only boundary.

Recommendation: retain the selected method as the starting text; replace concrete paths and agreed policy slots, and review substantive removals. Use a behavior-to-document checklist, not only Markdown-link checks. A shorter summary is not necessarily an equivalent method.

### 6. Removing helpers is not logically necessary for project authority

A helper skill could discover project guidance and defer to it while remaining available for direct invocation. Project ownership and helper retirement are separate decisions.

Retirement removes a named entry point and the no-setup fallback. Keeping helpers avoids some migration friction but risks a second copy of the method and competing defaults. The proposed retirement is coherent, but should be chosen for reducing duplicate authorities, not presented as the only way to achieve project independence.

### 7. Attribution still needs a completed output path

The templates retain notice-link placeholders. A subsequent local commit removed the automatic copying instruction. This review does not reverse that edit or prescribe a copying mechanism.

However, retained adapted material still needs applicable notices when distributed, as required by the project constitution and upstream MIT terms. Resolve the output notice path or another compliant form rather than leave a broken placeholder. Source relocation does not remove the obligation. This is independent of whether project-owned guidance is the right architecture.

## Commit and constitute: separate completeness gaps

The repository's provenance classifies both as local original material. A comparison to Matt's domain-modeling source cannot establish their completeness.

### Commit

The project seed already preserves scoped staging, the selected message format, reporting, and commit-versus-push separation. Its deliberate policy change is to ask for a project format rather than impose Conventional Commits.

Two existing guardrails are not explicit in the generated procedure:

- Do not repeat checks or initiate another review merely because the commit step was requested, unless the project requires them.
- Do not infer a different commit convention merely from ad hoc commit history.

Preserve the distinction between satisfying project prerequisites and redundantly rerunning already satisfied work before retiring the skill. The existing skill remains installed, so these are future migration gaps, not current deletions.

### Constitute

The seed includes authority, compliance, approval, versioning, and reconciliation. Some of the actual amendment method still lives in the setup reference or constitute skill rather than the generated constitution:

- Distinguish durable constraints from current implementation and feature-specific requirements.
- Do not infer policy from code or promote a one-feature requirement into governance.
- Use existing policy owners rather than create a competing constitution.
- Verify affected paths, links, and commands at their sources after reconciliation.

Transfer relevant ongoing amendment guidance into the constitution's own short instructions before retiring constitute. Initial setup instructions need not all become permanent governance, but instructions needed for later maintenance must survive.

## Suggested behavioral comparison before broader retirement

The existing checks establish links, structural preservation, and sample output completeness. They do not establish equivalent agent behavior. A small evaluation should compare the upstream method and project-owned output under the same model/harness and comparable task conditions, with more than one run if conclusions depend on model behavior.

Cases:

1. An overloaded account term: agent challenges it instead of silently choosing a meaning.
2. A term is agreed mid-conversation: agent records the tight definition inline, without a spec dump or redundant approval round.
3. Code/source material contradicts the user's claim: agent surfaces the conflict before changing either.
4. A reversible routine choice: agent does not offer an unnecessary ADR.
5. A costly, surprising trade-off: agent offers the short record and respects acceptance requirements.
6. Multiple contexts: agent selects the right glossary and follows the map's relationships; it does not duplicate terms arbitrarily.
7. A missing or explicitly declined glossary/ADR practice: unrelated work proceeds; a genuinely blocked artifact update asks for direction.
8. An existing accepted record conflicts with a proposal: agent surfaces and handles the conflict under project rules.

Inspect observable actions and transcript evidence, not just whether the agent says it followed guidance. Do not substitute synthetic rendered templates for autonomous execution in the report. No such behavioral experiment was run during this review.

## Recommendation

Proceed with the project-owned direction as a bounded experiment, not as a demonstrated improvement over upstream. Domain language and decision records are good first candidates because their core methods have survived the text migration. Strengthen the actual loading path, keep soft dependencies soft, and protect inline capture from approval ceremony.

Do not retire commit or constitute merely for symmetry. Complete their method-to-document checks first. Keep retirement, adoption by existing projects, and future setup migration explicit and separately reviewable.

The user accepts the initial migration cost. The remaining decision is whether the loss of centralized activation and automatic method updates is acceptable in exchange for project independence. That trade-off cannot be resolved by a text diff alone.
