# ItsSkills

ItsSkills is an experimental collection of agent skills for human-directed, agent-executed software engineering, governed by its [constitution](CONSTITUTION.md).

Developers retain authority over intent, constraints, and consequential tradeoffs while agents handle implementation and supporting work within delegated boundaries. Specification-driven development connects explicit intent to verifiable results, with documentation proportional to the task. The goal is greater problem-solving capacity without sacrificing artifact quality or accountability.

## Installation

The repository follows Vercel's skills CLI source layout. End-to-end installation verification is pending publication. The Nix distribution interface remains planned.

### Recommended

The Recommended profile is a curated starting point for improving agent reasoning, output quality, and verification without requiring adoption of the collection's development lifecycle. It contains 38 skills: the Principles router and all 22 leaves, 12 techniques, and the Refactoring, Integrating Web APIs, and Development Review playbooks.

```sh
npx skills add ItsEthanDev/its-skills --skill \
  alignment \
  calling-web-apis \
  commit \
  development-review \
  diagramming \
  dry-run \
  integrating-web-apis \
  pause-work \
  principle-boundary-discipline \
  principle-build-the-lever \
  principle-design-deep-modules \
  principle-encode-lessons-in-structure \
  principle-exhaust-the-design-space \
  principle-experience-first \
  principle-fix-root-causes \
  principle-foundational-thinking \
  principle-guard-the-context-window \
  principle-laziness-protocol \
  principle-make-operations-idempotent \
  principle-migrate-callers-then-delete-legacy-apis \
  principle-minimize-reader-load \
  principle-model-the-domain \
  principle-never-block-on-the-human \
  principle-outcome-oriented-execution \
  principle-prove-it-works \
  principle-redesign-from-first-principles \
  principle-separate-before-serializing-shared-state \
  principle-sequence-verifiable-units \
  principle-subtract-before-you-add \
  principle-type-system-discipline \
  principles \
  propose-first \
  refactoring \
  repitch \
  show-me \
  understanding-code \
  verifying-work \
  writing
```

### Maximal

Install every skill, including optional development workflows. Making a skill available does not require using it or override its activation conditions.

```sh
npx skills add ItsEthanDev/its-skills --skill '*'
```

### Individual skills

Choose any skill or combination by identifier:

```sh
npx skills add ItsEthanDev/its-skills --skill writing understanding-code
```

### Installation notes

- The commands leave target-agent selection to the CLI prompts and use project-local installation by default. Add `--global` for user-wide installation or `--agent <agent>` to select a target explicitly. Profiles do not force installation to every agent.
- Guidance-only skills do not require Nix. Bundled scripts require Nix and keep their pinned environments with the owning skill.
- Profile commands select skills; they do not automatically install referenced skills outside that selection. If a task requires an unavailable reference, install that skill separately or use Maximal. The [dependency graph](DEPENDENCIES.md) shows the references.
- Invocation metadata support depends on the consuming agent.

The Recommended command above is the authoritative profile list. When adding, renaming, or removing skills, review Recommended membership and update that command as needed. New skills are not automatically Recommended. Maximal selects all available skills without a separately maintained inventory.

## Skills

Runtime sources live under `skills/<role>/<skill-name>/`. Specifications, generated graph outputs, and maintenance tools remain at the repository level.

Guidance-only skills remain usable without Nix. Bundled script execution requires Nix; the Show Me browser helper supplies mdts through its own pinned environment. Explicit-invocation settings depend on harness support.

### Stages

- [Development Stages](skills/stages/stages/SKILL.md): Coordinate applicable Constitute, Specify, Plan, and Implement work without requiring every stage or a fixed sequence.

### Playbooks

- [Authoring Skills](skills/playbooks/authoring-skills/SKILL.md): Create or revise a skill using target-project conventions; explicitly invoked.
- [Authoring Project Verification](skills/playbooks/authoring-project-verification/SKILL.md): Create or maintain project-specific verification instructions and prove the affected procedures.
- [Ingest Document](skills/playbooks/ingest-document/SKILL.md): Identify proposals in a document and ask which to adopt; explicitly invoked.
- [Refactoring](skills/playbooks/refactoring/SKILL.md): Improve structure while preserving accepted behavior, with direct checks and separate reporting of discovered defects.
- [Prototype](skills/playbooks/prototype/SKILL.md): Build an isolated, throwaway experiment to answer a question before production implementation.
- [Development Review](skills/playbooks/development-review/SKILL.md): Conduct an authorized, bounded review without changing maintained project content.
- [Diagnosing Bugs](skills/playbooks/diagnosing-bugs/SKILL.md): Establish a red-capable feedback loop, investigate causes, and repair only within authorized scope.
- [Integrating Web APIs](skills/playbooks/integrating-web-apis/SKILL.md): Build or change remote integrations, with conditional inbound-webhook guidance.

### Techniques

- [Alignment](skills/techniques/alignment/SKILL.md): Settle the questions needed for shared understanding.
- [Propose First](skills/techniques/propose-first/SKILL.md): Propose an approach and pause before implementation when requested.
- [Repitch](skills/techniques/repitch/SKILL.md): Replace an explanation with a clearer one when requested.
- [Dry Run](skills/techniques/dry-run/SKILL.md): Preview a bounded edit and wait for approval; explicitly invoked.
- [Project Documentation](skills/techniques/project-documentation/SKILL.md): Choose authoritative artifact owners and maintain or reconcile project documentation.
- [Writing](skills/techniques/writing/SKILL.md): Plan, draft, revise, or review technical prose for humans or coding agents.
- [Understanding Code](skills/techniques/understanding-code/SKILL.md): Explain behavior, trace execution and data flow, and investigate design rationale with source-backed claims.
- [Diagramming](skills/techniques/diagramming/SKILL.md): Choose and construct clear visual representations while specifying, planning, documenting, or explaining information, with Mermaid as a conditional fallback.
- [Commit](skills/techniques/commit/SKILL.md): Stage and commit completed work; push only when explicitly requested.
- [Reflect](skills/techniques/reflect/SKILL.md): Propose evidence-backed improvements from selected work; explicitly invoked, proposal-only by default, with bounded caller-applied updates when requested.
- [Pause Work](skills/techniques/pause-work/SKILL.md): Pause a task safely and save a resume checkpoint; explicitly invoked.
- [Verifying Work](skills/techniques/verifying-work/SKILL.md): Select and execute checks, interpret findings, and return evidence and verification limits.
- [TDD](skills/techniques/tdd/SKILL.md): Develop behavior test-first through a red-green loop using shared automated-test guidance; refactoring remains separate work.
- [Show Me](skills/techniques/show-me/SKILL.md): Present work in chat, Hunk, a Markdown browser viewer, or UI screenshots. Its bundled browser script requires Nix.
- [Calling Web APIs](skills/techniques/calling-web-apis/SKILL.md): Make real API requests within explicit service, environment, and effect authorization.

### Principles

The [Principles router](skills/principles/principles/SKILL.md) selects among 22 engineering principles. Each leaf is also a separate skill under `skills/principles/`, with its source-authored explicit-invocation setting. Router and leaf discovery depend on the consuming harness.

## Dependency graph

Browse the committed [Mermaid dependency graph](DEPENDENCIES.md) on GitHub. [Machine-readable graph data](dependencies.json) records direct dependencies and source evidence for consumer analysis. References are conservative: a dependency may not be used on every invocation. The graph identifies potential change impact and supports computing subset dependency sets; it does not install skills or resolve packages.

[Graph tooling](tools/skill-graph/README.md) documents regeneration, validation, and freshness checks.

## Features

- [Skill roles](specs/skill-roles/spec.md) defines responsibilities and source organization.
- [Skill dependency graph](specs/skill-dependency-graph/spec.md) defines name-based references, committed graph outputs, and freshness validation.
- [Progressive disclosure](specs/progressive-disclosure/spec.md) defines on-demand loading of specialized guidance.
- [Contextual defaults](specs/contextual-defaults/spec.md) defines request and convention precedence, useful fallbacks, and conditional loading of default-specific detail.
- [Nix-backed script execution](specs/nix-backed-scripts/spec.md) defines execution prerequisites for scripts distributed by this collection. Generated project scripts follow their target project's conventions.
- [Self-verifying work](specs/self-verifying-work/spec.md) defines verification behavior, instruction ownership, and project-local protocol authoring.

## Repository guidance

Follow [AGENTS.md](AGENTS.md) when changing the collection. Use the [Authoring Skills playbook](skills/playbooks/authoring-skills/SKILL.md) when creating or revising a skill.

## License

[MIT](LICENSE).
