# Setup acceptance check: issue 13

Review of [Generalize project setup with domain-specific configuration](https://github.com/ItsEthanDev/its-skills/issues/13), starting from `experimental` at `281e095`.

## Scope and result

The bounded setup implementation is ready for review with two small corrections:

1. Explicitly defer a selected integration whose conventions are still being designed, without blocking independent setup. This supplies the extension boundary requested by the issue without defining learning-suite behavior or restoring a learning-specific warning.
2. Move the README seed's instruction to select a glossary map into its removable seed comment. It is an instruction to the generator, not content for the human-facing project index.

No broader skill retirement, project-standards feature generalization, or learning-suite implementation is included. Those remain separate work.

## Acceptance review

| Requirement | Evidence | Result and limit |
| --- | --- | --- |
| Review the full bundle and invocation | Read `SKILL.md`, all 12 references, all 16 assets, provenance, and both license files. Every instruction/seed file has provenance coverage; every reference is reachable from the selected-feature table. | Passed document review. Setup remains explicitly user-invoked. |
| Domain-independent setup | Exploration does not require Git, build tooling, or deployment. Features are selected from intent; engineering standards, tooling, implementation triage, and tracker use are conditional. | Passed review and manually specified output fixtures. No claim about autonomous feature selection. |
| Preserve explore, propose, confirm, write | The process requires findings, intent, feature selection, draft approval, scoped edits, and verification. Existing approval procedures and external-effect authorization remain binding. | Passed instruction review. The live approval exchange was not independently tested. |
| Preserve existing work and policy | Writing, engineering, and scoped fixtures retained existing content. The engineering fixture preserved source, tests, Black/Ruff configuration, CI, and request-only commit policy. | Passed fixture assertions. Full-project migration and arbitrary rerun behavior remain untested. |
| Leave unsettled learning contracts open | The added generic extension boundary defers dependent integrations rather than inventing conventions. A mixed writing/learning fixture left pending preferences and activity-format notes unchanged while establishing only a draft constitution. | Passed instruction review and bounded fixture assertions, not autonomous deferral behavior. |
| Exercise engineering/non-engineering examples and links | Three disposable output fixtures exercised ten seed templates. All 32 checked project-local Markdown links/anchors resolved. The engineering quickstart commands ran; the prose fixture needed no build tools. | Passed the checks described below. The fixtures use preset decisions, not independent model runs. |
| Catalog, provenance, notices | The existing catalog describes project documentation, conventions, and selected tooling. Provenance covers the bundle and records these corrections. Both license files are unchanged from the baseline. | Passed static checks; no attribution reclassification or catalog change is needed for these corrections. |

## Fixture observations

These were manually specified adaptations of the current seeds, created and checked with a one-off Python helper. They test whether representative outputs can be made consistent with the documented method; they do not prove that an independently invoked agent will generate those outputs or stop for approval.

### Non-engineering writing project

Preset decisions: essays, a text editor, no Git or build tooling, no tracker or constitution, custom `handbook/` guidance locations, and an existing `CLAUDE.md` entry point.

- Generated overview, quickstart, single-context glossary, domain guidance, and selected harness pointers.
- Kept author voice instructions and the existing essay unchanged.
- Confirmed that no repository, automatic-commit section, tracker, constitution, or coding-standards document was created.
- Confirmed the quickstart's stated opening sentence exists in the essay; no automated prose checker was invented.
- Checked 13 local links/anchors, including glossary-to-guidance and README-to-guide navigation. Retained the applicable MIT notice for adapted domain guidance inside the fixture.
- A negative assertion exposed the README seed's generator instruction in human-facing output. It failed before the seed correction and passed afterward.

### Engineering project

Preset decisions: an existing standard-library Python calculation and test, Black/Ruff configuration and CI to preserve, request-only commits, and local implementation tracking with a custom `work-ready` role mapping. Tool installation and migration were not selected.

- Generated overview, quickstart, coding standards, local tracker/triage guidance, and selected agent pointers.
- Confirmed existing source, tests, tool configuration, and CI remained byte-identical; retained the request-only commit instruction rather than adding automatic commits.
- Executed `python3 app.py`; observed output `15` and exit status 0.
- Executed `python3 -B -m unittest discover -s tests`; observed one passing test and `OK`.
- Temporarily changed the calculation to return the wrong value; the same test command failed with `AssertionError`. Restored the source and verified its original hash.
- Created a local fixture ticket using the selected role string, without remote tracker access.
- Checked 13 local links/anchors. Black, Ruff, and remote CI were not installed or executed.

### Scoped constitution in a mixed writing/learning project

Preset decisions: a constitution-only request, one agreed privacy constraint, explicit owner ratification, and custom `rules/` locations. Existing tracker, commit policy, and unresolved learning notes were outside scope.

- Generated a draft constitution and agent guide with the appropriate discovery links.
- Confirmed the constitution remains unratified; no agent proposal became accepted governance.
- Confirmed tracker and unresolved learning notes remained byte-identical and existing commit/tracker instructions remained present.
- Confirmed no glossary, coding standards, or replacement tracker was created.
- Checked six local links/anchors. This was not a learning-suite design or migration test.

## Checks and limits

- `python3 scripts/check_repo.py`: repository consistency checks passed.
- `git diff --check`: passed.
- One-off fixture helper: three scenarios passed; selected source links, reference reachability, provenance coverage, and invocation metadata passed.
- Byte comparison against `281e095`: both setup license files unchanged; seed files other than `assets/readme.md` unchanged.
- All temporary project directories were removed, including after the negative assertion. The one-off helper is session-local, not a maintained repository test.
- No tools or dependencies were installed. No source was published, remote tracker mutated, release performed, system activated, or live agent configuration changed by these checks.

Independent agent execution, live confirmation behavior, toolchain installation/migration, remote tracker operations, deployment/recovery, multi-context glossary generation, and installed-source consumption were not exercised. Static assertions about the added extension instruction establish its presence, not model compliance. The cross-domain audit and installation verification remain separate work; this report does not close the organization gate.
