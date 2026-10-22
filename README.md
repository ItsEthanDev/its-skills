# ItsSkills

ItsSkills is an collection of reusable agent skills for general work, software engineering, and learning.

## Skill catalog

Use these identifiers with `--skill` when installing individual skills. Each link opens the skill's instructions. Invocation metadata support depends on the consuming agent.

Skills live under `skills/<task-domain>/<skill>/` classified by purpose, not by implementation tools or occasional reuse. Each skill has one canonical home. Workflows in other domains can use it without copying it.

Skills are divided into model invoked skills and manually invoked skills. The model can load model invoked skills when their invocation conditions match the task, while manually invoked skills must be explicitly invoked by the user.

### General

#### Model invoked

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

The repository follows Vercel's skills CLI source layout and can be consumed as a source-only Nix flake input. Both methods use the same complete skill bundles. The unpinned examples below target main; select a revision containing the skills you need.

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

Invoke `setup` explicitly in your agent harness. It explores the project, establishes your intent, and asks you to approve the proposed changes before writing. Run it for general setup, scope it to a feature such as commit guidance or a constitution, or use it to extend or migrate existing conventions. Features are selected for the work the project supports; a tracker, constitution, or toolchain is not mandatory. Approved lint/format setup can configure tools as well as document them.

The generated guidance belongs to the project and remains usable without the setup skill. The README indexes selected guidance by purpose; agent instructions explain when to follow it.

### Nix

Add a source-only input to your configuration flake:

```nix
inputs.its-skills = {
  url = "github:ItsEthanDev/its-skills";
  flake = false;
};
```

For installation of skills through Home Manager, pass your flake `inputs` through `extraSpecialArgs` and point its skill discovery at the source directory. Replace `my-coding-agent` with your preferred agent harness. Refer to home manager options to determine the exact interface for your setup.

```nix
{ inputs, ... }: {
  programs.my-coding-agent = {
    enable = true;
    settings.skills = [ "${inputs.its-skills}/skills" ];
  };
}
```

The directory contains every skill in nested task-domain directories. To select a specific directory, use the following pattern:

```nix
settings.skills = [
  "${inputs.its-skills}/skills/general"
  "${inputs.its-skills}/skills/engineering"
];
```

For individual skills, use complete directory paths such as `"${inputs.its-skills}/skills/general/writing"`, and include any skills they require. Selecting only a domain directory does not add dependencies from other domains.

### Installation notes

- The CLI commands leave target-agent selection to the CLI prompts and use project-local installation by default. Add `--global` for user-wide installation or `--agent <agent>` to select a target explicitly.
- Invocation metadata support depends on the consuming agent.

## Project documentation

- [Quickstart](docs/quickstart.md): prerequisites and local verification.
- [Distribution](docs/deployment.md): source publication, verification, and limits.
- [Constitution](CONSTITUTION.md): binding project constraints and amendment rules.
- [Project standards](STANDARDS.md): guiding qualities for project work.
- [Glossary](GLOSSARY.md): agreed project terms.
- [Decision records](docs/decisions.md): accepted decisions and their rationale.

## Agent documentation

- [Agent instructions](AGENTS.md): conditional pointers and commit behavior.
- [Commit guidance](docs/agents/commits.md): agent prerequisites, messages, branches, and reporting.
- [Constitution guidance](docs/agents/constitution.md): applying and amending governance.
- [Issue tracker](docs/agents/issue-tracker.md): GitHub operations and wayfinding.
- [Triage labels](docs/agents/triage-labels.md): implementation-role mappings.
- [Domain guidance](docs/agents/domain.md): active terminology practice and maintenance.
- [Decision-record guidance](docs/agents/decision-records.md): selection, format, approval, and maintenance.

## Acknowledgments

ItsSkills draws on ideas and adapted guidance from:

- [Matt Pocock's skills](https://github.com/mattpocock/skills), published under the [MIT license](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/LICENSE). Copyright (c) 2026 Matt Pocock.
- [Lauren Tan (Poteto)'s Pstack](https://github.com/cursor/plugins/tree/main/pstack), published under the [MIT license](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/LICENSE). Copyright (c) 2026 Lauren Tan.
- [Anthropic's frontend design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design), published under the [Apache License 2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt).
