# ItsSkills

ItsSkills is an experimental collection of agent skills for human-directed, agent-executed software engineering.

## Skill catalog

Use these identifiers with `--skill` when installing individual skills. Each link opens the skill's instructions. Invocation metadata support depends on the consuming agent.

### Model invoked

The model can load these skills when their invocation conditions match the task. You can also invoke them explicitly.

| Skill | Purpose |
| --- | --- |
| [action-authorization](skills/action-authorization/SKILL.md) | Resolve permission for consequential actions and record scoped grants or denials. |
| [alignment](skills/alignment/SKILL.md) | Stress-test a plan, decision, or idea with the user. |
| [code-review](skills/code-review/SKILL.md) | Review changes against repository standards and the originating spec in parallel. |
| [codebase-design](skills/codebase-design/SKILL.md) | Design deeper modules, clearer interfaces, and testable boundaries. |
| [commit](skills/commit/SKILL.md) | Stage and commit scoped changes using Conventional Commits. |
| [constitute](skills/constitute/SKILL.md) | Establish or amend durable project constraints. |
| [decision-records](skills/decision-records/SKILL.md) | Record consequential decisions in architecture decision records (ADRs). |
| [diagnosing-bugs](skills/diagnosing-bugs/SKILL.md) | Diagnose bugs and performance regressions. |
| [domain-language](skills/domain-language/SKILL.md) | Sharpen project terminology and maintain a glossary. |
| [frontend-design](skills/frontend-design/SKILL.md) | Design or reshape frontend pages, components, and interactive prototypes. |
| [pr](skills/pr/SKILL.md) | Write a pull request body. |
| [propose-first](skills/propose-first/SKILL.md) | Propose a solution and wait for approval before implementing. |
| [prototype](skills/prototype/SKILL.md) | Build a throwaway prototype to answer a design question. |
| [repitch](skills/repitch/SKILL.md) | Re-explain a message or part of one. |
| [research](skills/research/SKILL.md) | Investigate primary sources and save findings as Markdown in the repo. |
| [tdd](skills/tdd/SKILL.md) | Build features or fix bugs with test-driven development. |
| [verifying-work](skills/verifying-work/SKILL.md) | Prove results, establish feedback loops, and maintain verification guidance. |
| [wizard](skills/wizard/SKILL.md) | Generate an interactive Bash wizard for steps only a human can perform. |
| [writing](skills/writing/SKILL.md) | Write and revise technical prose for humans and coding agents. |

### Manually invoked

Invoke these skills explicitly. Their metadata sets `disable-model-invocation: true`.

| Skill | Purpose |
| --- | --- |
| [dry-run](skills/dry-run/SKILL.md) | Preview a small edit as a diff and wait for approval before changing files. |
| [implement](skills/implement/SKILL.md) | Implement work from a spec or set of tickets. |
| [improve-codebase-architecture](skills/improve-codebase-architecture/SKILL.md) | Find module-deepening opportunities, present an HTML report, and align on a choice. |
| [ingest-document](skills/ingest-document/SKILL.md) | Extract project-relevant proposals from a document and ask which to adopt. |
| [pause-work](skills/pause-work/SKILL.md) | Pause safely and save a resume checkpoint. |
| [retro](skills/retro/SKILL.md) | Conduct a retrospective on a coding session. |
| [setup](skills/setup/SKILL.md) | Configure project documentation, issue tracking, triage labels, and domain docs. |
| [to-spec](skills/to-spec/SKILL.md) | Synthesize the conversation into a spec and publish it to the issue tracker. |
| [teach](skills/teach/SKILL.md) | Teach a skill or concept through lessons in a persistent learning workspace. |
| [to-implementation-tickets](skills/to-implementation-tickets/SKILL.md) | Break a plan, spec, or conversation into tracer-bullet implementation tickets with explicit blocking dependencies. |
| [to-questionnaire](skills/to-questionnaire/SKILL.md) | Turn unresolved decisions into a questionnaire for someone with the missing knowledge. |
| [wayfinder](skills/wayfinder/SKILL.md) | Map work spanning multiple agent sessions into decision tickets and resolve them in sequence. |

## Installation

The repository follows Vercel's skills CLI source layout and can be consumed as a source-only Nix flake input. Both methods use the same skill directories. End-to-end installation verification against the published repository is pending publication.

### Individual skills

Choose any skill or combination by identifier:

```sh
npx skills add ItsEthanDev/its-skills --skill writing codebase-design
```

### Project setup

Install `setup` to establish a project's documentation baseline, issue-tracker configuration, and domain-doc layout:

```sh
npx skills add ItsEthanDev/its-skills --skill setup
```

Invoke `setup` explicitly in your agent. It explores the repo and asks you to approve the proposed documentation before writing.

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

The directory contains every skill. To select individual skills, use their complete directory paths instead, such as `"${inputs.its-skills}/skills/writing"`. Keep each selected skill's references, templates, scripts, `PROVENANCE.md`, `LICENSE`, and any `licenses/` directory with it; selecting a `SKILL.md` alone does not preserve its bundle or notices.

### Installation notes

- The CLI commands leave target-agent selection to the CLI prompts and use project-local installation by default. Add `--global` for user-wide installation or `--agent <agent>` to select a target explicitly.
- Invocation metadata support depends on the consuming agent.

## Verification

Run the repository consistency check with Python 3 (no additional packages):

```sh
python3 scripts/check_repo.py
```

The check requires every skill in the README catalog and a `LICENSE` and `PROVENANCE.md` in each skill directory. It validates existing third-party inventory entries, classifications, and provenance links without requiring an inventory entry for every skill. It reports all errors and exits nonzero on failure. Provenance accuracy and license adequacy still require human review.

The same check runs in GitHub Actions on pushes and pull requests.

## Contributor docs

- [Quickstart](docs/quickstart.md): checkout prerequisites and local verification.
- [Distribution](docs/deployment.md): consumption paths and release-verification gaps.
- [Issue tracker](docs/agents/issue-tracker.md): GitHub operations and wayfinding conventions.
- [Triage labels](docs/agents/triage-labels.md): implementation triage vocabulary.
- [Domain docs](docs/agents/domain.md): glossary conventions.
- [Glossary](GLOSSARY.md): agreed project terms.

## Project principles

The [project constitution](CONSTITUTION.md) governs skill composition, context use, and attribution. [Agent instructions](AGENTS.md) point contributors using agents to the applicable guidance.

## Acknowledgments

ItsSkills draws on ideas and adapted guidance from:

- [Matt Pocock's skills](https://github.com/mattpocock/skills), published under the [MIT license](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/LICENSE). Copyright (c) 2026 Matt Pocock.
- [Lauren Tan (Poteto)'s Pstack](https://github.com/cursor/plugins/tree/main/pstack), published under the [MIT license](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/LICENSE). Copyright (c) 2026 Lauren Tan.
- [Anthropic's frontend design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design), published under the [Apache License 2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt).

## License

ItsSkills' original material uses [MIT](LICENSE). Copied and adapted material retains its applicable upstream notices. The [skill inventory](THIRD-PARTY-NOTICES.md#skill-inventory) classifies audited skills and links to file-level evidence. Each skill directory includes `PROVENANCE.md`, `LICENSE`, and any additional upstream licenses under `licenses/`; retain them with individual skill distributions. Inspiration credits do not change the license of original local text.
