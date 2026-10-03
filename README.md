# ItsSkills

ItsSkills is an experimental collection of agent skills, governed by its [constitution](CONSTITUTION.md).

Nix and Vercel's skills CLI are intended installation paths. Installation tooling is not yet implemented or verified.

## Skills

All current skills are guidance-only and need no Nix installation to use their instructions. Explicit-invocation settings depend on harness support.

### Stages

- [Development Stages](stages/stages/SKILL.md): Coordinate applicable Constitute, Specify, Plan, and Implement work without requiring every stage or a fixed sequence.

### Playbooks

- [Authoring Skills](playbooks/authoring-skills/SKILL.md): Create or revise a skill. Adapted to the collection's governance and specifications; explicitly invoked.
- [Ingest Document](playbooks/ingest-document/SKILL.md): Identify proposals in a document and ask which to adopt; explicitly invoked.
- [Prototype](playbooks/prototype/SKILL.md): Build an isolated, throwaway experiment to answer a question before production implementation.
- [Development Review](playbooks/development-review/SKILL.md): Conduct an authorized, bounded review without changing maintained project content.
- [Diagnosing Bugs](playbooks/diagnosing-bugs/SKILL.md): Establish a red-capable feedback loop, investigate causes, and repair only within authorized scope.

### Techniques

- [Alignment](techniques/alignment/SKILL.md): Settle the questions needed for shared understanding.
- [Propose First](techniques/propose-first/SKILL.md): Propose an approach and pause before implementation when requested.
- [Repitch](techniques/repitch/SKILL.md): Replace an explanation with a clearer one when requested.
- [Dry Run](techniques/dry-run/SKILL.md): Preview a bounded edit and wait for approval; explicitly invoked.
- [Project Documentation](techniques/project-documentation/SKILL.md): Choose authoritative artifact owners and maintain or reconcile project documentation.
- [Writing](techniques/writing/SKILL.md): Plan, draft, revise, or review technical prose for humans or coding agents.
- [Commit](techniques/commit/SKILL.md): Stage and commit completed work; push only when explicitly requested.
- [Pause Work](techniques/pause-work/SKILL.md): Pause a task safely and save a resume checkpoint; explicitly invoked.
- [TDD](techniques/tdd/SKILL.md): Develop tested behavior through a red-green loop at approved seams; refactoring remains separate work.

### Principles

The [Principles router](principles/principles/SKILL.md) selects among 22 engineering principles. Each leaf is also a separate skill under `principles/`, with its source-authored explicit-invocation setting. Router and leaf discovery depend on the consuming harness.

## Features

- [Skill roles](specs/skill-roles/spec.md) defines responsibilities and source organization.
- [Progressive disclosure](specs/progressive-disclosure/spec.md) defines on-demand loading of specialized guidance.
- [Nix-backed script execution](specs/nix-backed-scripts/spec.md) defines execution prerequisites and tool dependencies.

## License

[MIT](LICENSE).
