# ItsSkills

ItsSkills is an experimental collection of reusable agent skills for general work, software engineering, and learning.

## Skill catalog

Use these identifiers with `--skill` when installing individual skills. Each link opens the skill's instructions. Invocation metadata support depends on the consuming agent.

Skills named `to-<artifact>` transform context or source material into the named
[artifact](GLOSSARY.md#work-products). Their completion criterion is producing the
artifact, rather than executing its downstream use. Not every skill that produces
an artifact needs a `to-` name.

Skills live under `skills/<task-domain>/<skill>/`. Classify by purpose, not by
implementation tools or occasional reuse. Each skill has one canonical home;
workflows in other domains can use it without copying it.

The lists below describe current instructions. Cross-domain instruction changes
and an audit remain open under [task-domain organization](https://github.com/ItsEthanDev/its-skills/issues/2).

### General

Cross-domain work, including Git collaboration on code, prose, or other files.

#### Model invoked

The model can load these skills when their invocation conditions match the task.
You can also invoke them explicitly.

| Skill | Purpose |
| --- | --- |
| [action-authorization](skills/general/action-authorization/SKILL.md) | Resolve permission for consequential actions and record scoped grants or denials. |
| [alignment](skills/general/alignment/SKILL.md) | Stress-test a plan, decision, or idea with the user. |
| [pr](skills/general/pr/SKILL.md) | Write a pull request body. |
| [propose-first](skills/general/propose-first/SKILL.md) | Propose a solution and wait for approval before implementing. |
| [prototype](skills/general/prototype/SKILL.md) | Build a throwaway artifact to answer a design question. |
| [repitch](skills/general/repitch/SKILL.md) | Re-explain a message or part of one. |
| [research](skills/general/research/SKILL.md) | Investigate primary sources and save findings as Markdown in the repo. |
| [verifying-work](skills/general/verifying-work/SKILL.md) | Prove results, establish feedback loops, and maintain verification guidance. |
| [wizard](skills/general/wizard/SKILL.md) | Generate an interactive Bash wizard for steps only a human can perform. |
| [writing](skills/general/writing/SKILL.md) | Write and revise technical prose for humans and coding agents. |

#### Manually invoked

Invoke these skills explicitly. Their metadata sets `disable-model-invocation: true`.

| Skill | Purpose |
| --- | --- |
| [dry-run](skills/general/dry-run/SKILL.md) | Preview a small edit as a diff and wait for approval before changing files. |
| [ingest-document](skills/general/ingest-document/SKILL.md) | Extract project-relevant proposals from a document and ask which to adopt. |
| [pause-work](skills/general/pause-work/SKILL.md) | Pause safely and save a resume checkpoint. |
| [retro](skills/general/retro/SKILL.md) | Conduct a retrospective on an agent session. |
| [setup](skills/general/setup/SKILL.md) | Establish, extend, or migrate discoverable project guidance and selected tooling, across the project or for a specific feature. |
| [to-questionnaire](skills/general/to-questionnaire/SKILL.md) | Turn unresolved decisions into a questionnaire for someone with the missing knowledge. |
| [wayfinder](skills/general/wayfinder/SKILL.md) | Map work spanning multiple agent sessions into decision tickets and resolve them in sequence. |

### Engineering

Software design, implementation, review, diagnosis, and testing.

#### Model invoked

| Skill | Purpose |
| --- | --- |
| [code-review](skills/engineering/code-review/SKILL.md) | Review changes against repository standards and the originating spec in parallel. |
| [codebase-design](skills/engineering/codebase-design/SKILL.md) | Design deeper modules, clearer interfaces, and testable boundaries. |
| [diagnosing-bugs](skills/engineering/diagnosing-bugs/SKILL.md) | Diagnose bugs and performance regressions. |
| [frontend-design](skills/engineering/frontend-design/SKILL.md) | Design or reshape frontend pages, components, and interactive prototypes. |
| [tdd](skills/engineering/tdd/SKILL.md) | Build features or fix bugs with test-driven development. |

#### Manually invoked

| Skill | Purpose |
| --- | --- |
| [implement](skills/engineering/implement/SKILL.md) | Implement work from a spec or set of tickets. |
| [improve-codebase-architecture](skills/engineering/improve-codebase-architecture/SKILL.md) | Find module-deepening opportunities, present an HTML report, and align on a choice. |
| [to-spec](skills/engineering/to-spec/SKILL.md) | Synthesize the conversation into a spec and publish it to the issue tracker. |
| [to-implementation-tickets](skills/engineering/to-implementation-tickets/SKILL.md) | Break a plan, spec, or conversation into tracer-bullet implementation tickets with explicit blocking dependencies. |

### Learning

#### Manually invoked

| Skill | Purpose |
| --- | --- |
| [teach](skills/learning/teach/SKILL.md) | Teach a skill or concept through lessons in a persistent learning workspace. |

## Installation

The repository follows Vercel's skills CLI source layout and can be consumed as a source-only Nix flake input. Both methods use the same complete skill bundles. End-to-end installation verification against the published repository is pending publication.

A task-domain directory is an ownership and browsing boundary, not a self-contained
installation. Include the general skills required by selected workflows. Selection
uses existing CLI options or Nix paths; there is no custom installer or dependency
resolver. The dependency audit and verified group-selection commands remain open
under [task-domain organization](https://github.com/ItsEthanDev/its-skills/issues/2).

### Workflow dependencies

These are explicit calls to other shipped skills, not a requirement to install all
of `general`. Include the dependencies of each selected branch recursively. A
conditional dependency is needed only when that branch is used.

| Skill | Required skills | Conditional skills |
| --- | --- | --- |
| `ingest-document` | `alignment` | — |
| `retro` | `writing` | — |
| `wayfinder` | — | `alignment` for charting or alignment tickets; `research` for research tickets; `prototype` for prototype tickets. |
| `verifying-work` | — | `codebase-design` for software test surfaces/adapters; `tdd` for maintained tests; `writing` when authoring project verification guidance; the project's own verification skill when its procedure applies. |
| `diagnosing-bugs` | `verifying-work` | Follow the verification branch's dependencies. |
| `frontend-design` | — | `verifying-work` when executing checks. |
| `implement` | `verifying-work`, `code-review` | `tdd` where applicable; follow those skills' conditional dependencies. |
| `improve-codebase-architecture` | `codebase-design` | `alignment` after choosing a candidate. |
| `tdd` | — | `codebase-design` when the interface or seam is unsettled. |

Skills not listed have no explicit calls to another shipped skill. References to
an independently run workflow, such as TDD's review-stage reference to
`code-review`, do not make that workflow part of the current invocation.
Suggestions to run `setup` establish missing project guidance; setup is not an
installed runtime dependency of those consumers.

Project-owned commit, constitution, domain-language, and decision-record guidance
replaces the retired skills with those names. Preserve that guidance and the
selected skill's own prerequisites: `prototype` requires version control, but
`teach` does not require Git, `pr`, or any other shipped skill. General-purpose
skills may still require a tracker, delegation, a shell, or version control for
the particular method selected; those are not engineering-only assumptions.

This table is a source-level dependency inventory, not evidence that either
installation path resolves dependencies automatically or has been exercised.
Published-source discovery and complete-bundle installation remain tracked in
[installation verification](https://github.com/ItsEthanDev/its-skills/issues/16).

### Individual skills

Choose any skill or combination by identifier:

```sh
npx skills add ItsEthanDev/its-skills --skill writing codebase-design
```

### Project setup

Install `setup` to establish a project's documentation, conventions, and selected tooling:

```sh
npx skills add ItsEthanDev/its-skills --skill setup
```

Invoke `setup` explicitly in your agent. It explores the project, establishes your
intent, and asks you to approve the proposed changes before writing. Run it for
general setup, scope it to a feature such as commit guidance or a constitution,
or use it to extend or migrate existing conventions. Features are selected for
the work the project supports; a tracker, constitution, or toolchain is not
mandatory. Approved lint/format setup can configure tools as well as document them.

The generated guidance belongs to the project and remains usable without the
setup skill. The README indexes selected guidance by purpose; agent instructions
explain when to follow it. Future setup recommendations do not change existing
project policy without an approved change.

### Nix

Add a source-only input to your configuration flake:

```nix
inputs.its-skills = {
  url = "github:ItsEthanDev/its-skills";
  flake = false;
};
```

Your consumer's `flake.lock` pins the source revision. ItsSkills does not require a provider flake, package build, or separate copy of the skills.

For Pi through Home Manager, pass your flake `inputs` through `extraSpecialArgs` and point its skill discovery at the source directory:

```nix
{ inputs, ... }: {
  programs.pi-coding-agent = {
    enable = true;
    settings.skills = [ "${inputs.its-skills}/skills" ];
  };
}
```

The directory contains every skill in nested task-domain directories. To select
engineering plus all general skills, use:

```nix
settings.skills = [
  "${inputs.its-skills}/skills/general"
  "${inputs.its-skills}/skills/engineering"
];
```

For individual skills, use complete directory paths such as
`"${inputs.its-skills}/skills/general/writing"`, and include any skills they require.
Selecting only a domain directory does not add dependencies from other domains.
Keep each selected skill's references, templates, scripts, `PROVENANCE.md`,
`LICENSE`, and any `licenses/` directory with it; selecting a `SKILL.md` alone does
not preserve its bundle or notices.

### Installation notes

- The CLI commands leave target-agent selection to the CLI prompts and use project-local installation by default. Add `--global` for user-wide installation or `--agent <agent>` to select a target explicitly.
- Invocation metadata support depends on the consuming agent.

## Verification

Run the repository consistency check with Python 3 (no additional packages):

```sh
python3 scripts/check_repo.py
```

The check enforces `skills/<general|engineering|learning>/<skill>/SKILL.md`, globally unique skill directory names, catalog coverage, and a `LICENSE` and `PROVENANCE.md` in each skill directory. It validates existing third-party inventory entries, classifications, and provenance links without requiring an inventory entry for every skill. It reports all errors and exits nonzero on failure. Provenance accuracy and license adequacy still require human review.

The same check runs in GitHub Actions on pushes and pull requests.

## Contributor docs

- [Quickstart](docs/quickstart.md): checkout prerequisites and local verification.
- [Distribution](docs/deployment.md): consumption paths and release-verification gaps.
- [Issue tracker](docs/agents/issue-tracker.md): GitHub operations and wayfinding conventions.
- [Triage labels](docs/agents/triage-labels.md): implementation triage vocabulary.
- [Domain guidance](docs/agents/domain.md): active terminology practice, glossary format, and maintenance.
- [Glossary](GLOSSARY.md): agreed project terms.
- [Decision records](docs/agents/decision-records.md): criteria, format, approval, and record index.

## Project principles

The [project constitution](CONSTITUTION.md) governs skill composition, context use, and attribution. [Project standards](STANDARDS.md) describe the guiding qualities used to design and assess skills and their applicable downstream artifacts and practices. [Agent instructions](AGENTS.md) point contributors using agents to the applicable guidance.

## Acknowledgments

ItsSkills draws on ideas and adapted guidance from:

- [Matt Pocock's skills](https://github.com/mattpocock/skills), published under the [MIT license](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/LICENSE). Copyright (c) 2026 Matt Pocock.
- [Lauren Tan (Poteto)'s Pstack](https://github.com/cursor/plugins/tree/main/pstack), published under the [MIT license](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/LICENSE). Copyright (c) 2026 Lauren Tan.
- [Anthropic's frontend design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design), published under the [Apache License 2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt).

## License

ItsSkills' original material uses [MIT](LICENSE). Copied and adapted material retains its applicable upstream notices. The [skill inventory](THIRD-PARTY-NOTICES.md#skill-inventory) classifies audited skills and links to file-level evidence. Each skill directory includes `PROVENANCE.md`, `LICENSE`, and any additional upstream licenses under `licenses/`; retain them with individual skill distributions. Inspiration credits do not change the license of original local text.
