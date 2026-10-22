## Project guidance

Use [Project documentation](README.md#project-documentation) and [Agent documentation](README.md#agent-documentation) to locate the project's guidance. Follow these direct pointers when their conditions apply:

- Before using local tools or verifying work, read the [quickstart](docs/quickstart.md).
- Before pushing, releasing, deploying, or changing environment configuration, read [deployment/distribution guidance](docs/deployment.md) for triggers, prerequisites, and required authorization.
- Before reading, creating, or updating tickets, read [issue-tracker guidance](docs/agents/issue-tracker.md). Before assigning implementation triage roles, read the [triage mapping](docs/agents/triage-labels.md).
- Before exploring a domain area, discussing or changing domain concepts, or proposing a change, read [domain-language guidance](docs/agents/domain.md). Follow its active terminology and approval practices, not just its definitions.
- When resolving a consequential trade-off or offering, writing, or revisiting a decision record, read [decision-record guidance](docs/agents/decision-records.md) and relevant records.
- Before changing governed work or proposing an amendment, read the [constitution](CONSTITUTION.md) and [agent constitution guidance](docs/agents/constitution.md). Surface conflicts rather than silently bypassing the constitution; amendments follow its approval procedure.
- Before writing or reviewing code, read [coding standards](CODING_STANDARDS.md) and the applicable lint/format configuration.
- Before committing, read [commit guidance](docs/agents/commits.md).

Follow the selected document's maintenance and approval rules when recording an agreed change.

## Commits

After completing and verifying a coherent unit of work, commit the changes unless explicitly instructed otherwise. Stage only changes belonging to that work; leave unrelated changes untouched. If verification or commit scope is unresolved, report the blocker rather than commit incomplete or ambiguous work. A request to commit does not imply permission to push.

<!-- Seed instructions: retain only pointers for selected features and replace all links with actual paths relative to the harness-loaded instruction file. Link to the actual README section anchors. Include the Commits section only when the project uses Git; omit it otherwise. Present this default for approval, preserving explicit existing policy unless changing it is in scope. Preserve existing instructions; do not imply this block overrides higher-priority instructions. Remove this comment before writing. -->
