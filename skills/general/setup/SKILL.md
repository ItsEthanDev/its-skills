---
name: setup
description: "Configure this repo's documentation baseline, issue tracker, triage labels, and domain doc layout. Run once when bringing a project into the skills workflow."
disable-model-invocation: true
---

# Setup

Scaffold the per-repo documentation and configuration that developers and agents need:

- **Project docs**: `README.md`, `AGENTS.md`, `docs/quickstart.md`, and `docs/deployment.md`
- **Issue tracker**: where issues live (GitHub by default; local markdown is also supported out of the box)
- **Triage labels**: how canonical implementation triage roles map to this repo's labels or local ticket statuses
- **Domain docs**: `GLOSSARY.md`, where ADRs belong, and the consumer rules for reading them

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config`: where is this repo hosted? Which remote tracks the project?
- `README.md` and `AGENTS.md` at the repo root: what do they already cover? Is there an `## Agent skills` section?
- `docs/quickstart.md`, `docs/deployment.md`, and equivalent documentation elsewhere: are there working instructions worth preserving or linking to?
- Manifests, lockfiles, development environment configuration, scripts, environment examples, and CI: what prerequisites, local commands, and checks does the repo actually use?
- Release workflows and infrastructure configuration: what is deployed or distributed, where, and what triggers a release? What evidence exists for verification and rollback?
- `GLOSSARY.md` and `GLOSSARY-MAP.md` at the repo root, plus any mapped glossaries
- `docs/adr/` and any context-specific ADR directories
- `docs/agents/`: does this skill's prior output already exist?
- `.scratch/`: a sign that a local-markdown issue tracker convention is already in use
- Monorepo signals: workspace configuration or multiple packages with their own source trees. Multiple packages alone do not imply separate domain contexts.

Identify a small set of domain terms from existing docs and code. Distinguish candidate definitions from definitions already agreed in a glossary; flag contradictions rather than silently resolving them.

Finish exploration with an inventory of existing docs, evidence for the workflows, and gaps requiring user decisions. Find facts in the repo before asking the user.

### 2. Present findings and ask

Summarise what's present and what's missing. Then take the sections in order. One section, one answer, then the next.

Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip questions already settled by existing configuration.

**Section A: Issue tracker.**

The issue tracker is where issues live for this repo. Skills need to know whether to call a CLI, write a markdown file under `.scratch/`, or follow some other workflow you describe. Pick the place you actually track work for this repo.

If a project remote points at GitHub, propose GitHub. If it points at GitLab (including a self-hosted instance), propose GitLab. Otherwise, or if the user prefers, offer:

- **GitHub**: issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab**: issues live in the repo's GitLab Issues (uses the `glab` CLI)
- **Local markdown**: issues live as files under `.scratch/<feature>/` in this repo
- **Other** (Jira, Linear, etc.): ask the user to describe the workflow in one paragraph

Record the choice in `docs/agents/issue-tracker.md`. Resolve ambiguous remotes or a tracker in a different repository with the user. Include the template's "Wayfinding operations" section, adapted to the configured tracker. For another tracker, establish its project identifier and how to create, read, list, comment on, and close tickets; also record how to store a Wayfinder map, identify and type its children, record blocking, select the frontier, claim a ticket, and resolve it.

**Triage label vocabulary.** Recommend the default roles from [triage-labels.md](triage-labels.md): `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`. Ask whether to keep those strings; preserve any existing mapping or collect the user's overrides. Record the agreed mapping in `docs/agents/triage-labels.md`. Local implementation tickets use those strings in `Status:`; Wayfinder decision tickets instead use the tracker-specific lifecycle convention. Record required remote labels without creating them: setup writes documentation only.

**Section B: Project docs.**

Recommend the four-file baseline below. Preserve useful existing content; use the baseline files as short entry points when equivalent docs already own the procedures.

| File | Purpose |
| --- | --- |
| `README.md` | What the project is, who it is for, and where to go next |
| `docs/quickstart.md` | From a fresh checkout to running locally and verifying a change |
| `docs/deployment.md` | How a change reaches a deployed environment or a distributed release, how to verify it, and how to roll it back |
| `AGENTS.md` | Project-specific agent rules and conditional pointers to the docs |

Keep the docs short, but concrete. The quickstart needs prerequisites, configuration, exact commands, and expected results. Deployment needs the platform, environments, release trigger, required access, verification, and rollback. Ask about missing operational facts; do not invent infrastructure or release procedures. If the project is not deployed, document its release/distribution workflow, or a brief "This project is not deployed or distributed" statement when neither applies.

Document secret names and how to obtain access, never secret values. Mark any unresolved facts explicitly rather than presenting guesses as working instructions.

**Section C: Domain docs.**

Default to **single-context** (one root `GLOSSARY.md` + `docs/adr/`). Preserve an existing `GLOSSARY-MAP.md` layout. Offer **multi-context** only when exploration found genuinely distinct domain contexts; then confirm the layout and paths with the user.

Propose the candidate terms and definitions, following [glossary.md](./glossary.md). Confirm them with the user before writing. Seed the glossary with agreed terms, not generic programming vocabulary or implementation details. If no terms can be established yet, use only the context heading, its description, and an empty `## Language` section. In a multi-context repo, establish the mapped glossaries rather than duplicating their terms in a root glossary.

Record layout and consumer rules in `docs/agents/domain.md`. Establish the ADR location without creating placeholder ADRs or empty directories. Decisions get records only when there is a consequential, agreed trade-off to capture.

### 3. Confirm and edit

Show the user a draft of all proposed additions and changes:

- `README.md`, `docs/quickstart.md`, and `docs/deployment.md`
- The `AGENTS.md` changes, including the `## Agent skills` block
- `GLOSSARY.md`, or the map and relevant context glossaries
- `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and `docs/agents/domain.md`

Use the seed templates below as starting points, adapting paths and commands to the repo. Show unresolved facts and any instructions you could not verify. Let the user edit before writing. Proceed only after they approve the draft.

### 4. Write and verify

Edit root `AGENTS.md` if it exists; create it if it does not. If an `## Agent skills` block already exists, update its contents in-place rather than appending a duplicate. Preserve user edits and unrelated sections in every existing file. On reruns, propose only needed changes; switching trackers must not move or delete existing issues.

Use conditional pointers so agents load the procedures when needed. Adapt this block to the agreed layout:

```markdown
## Agent skills

### Getting started

When setting up the checkout, running locally, or verifying a change, read `docs/quickstart.md`.

### Deployment

Before planning a deployment or release, read `docs/deployment.md`.

### Issue tracker

Before reading, creating, or updating tickets, read `docs/agents/issue-tracker.md`.

### Triage labels

Before applying implementation triage roles or writing local implementation ticket statuses, read `docs/agents/triage-labels.md`.

### Domain docs

Before exploring a domain area or proposing a change, read `docs/agents/domain.md` and follow its glossary and ADR pointers.
```

Keep procedures in their owning docs. Link to them from the README instead of duplicating them in `AGENTS.md`.

Seed templates:

- [readme.md](./readme.md): project overview and documentation links
- [quickstart.md](./quickstart.md): local setup and verification
- [deployment.md](./deployment.md): deployment or release workflow
- [glossary.md](./glossary.md): confirmed domain terms
- [issue-tracker-github.md](./issue-tracker-github.md): GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md): GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md): local-markdown issue tracker
- [triage-labels.md](./triage-labels.md): implementation triage role mapping
- [domain.md](./domain.md): domain doc consumer rules and layout

For other issue trackers, write `docs/agents/issue-tracker.md` from the confirmed workflow.

Check that all required docs exist in the agreed locations, local links resolve, template placeholders are replaced, and commands match the repo's scripts and configuration. Run safe local checks when feasible; record what was actually verified. Setup writes documentation only: do not deploy, provision infrastructure, publish releases, or mutate the external tracker to test the instructions.

### 5. Done

Tell the user which files were created or updated, what was verified, and any remaining gaps. Agents can now follow the pointers in `AGENTS.md`; do not claim every installed skill reads these files automatically.

Mention they can edit the docs directly later. Re-running this skill is useful when workflows change or the baseline needs refreshing.
