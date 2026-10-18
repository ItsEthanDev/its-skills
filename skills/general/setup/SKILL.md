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

Read each reference when you reach its section, in this order:

- **Section A: Issue tracker.** Read [references/issue-tracker.md](references/issue-tracker.md) to configure the tracker and triage vocabulary.
- **Section B: Project docs.** Read [references/project-docs.md](references/project-docs.md) to agree on the documentation baseline.
- **Section C: Domain docs.** Read [references/domain-docs.md](references/domain-docs.md) to agree on glossary layout, terms, and decision-record locations.

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

- [assets/readme.md](assets/readme.md): project overview and documentation links
- [assets/quickstart.md](assets/quickstart.md): local setup and verification
- [assets/deployment.md](assets/deployment.md): deployment or release workflow
- [assets/glossary.md](assets/glossary.md): confirmed domain terms
- [assets/issue-tracker-github.md](assets/issue-tracker-github.md): GitHub issue tracker
- [assets/issue-tracker-gitlab.md](assets/issue-tracker-gitlab.md): GitLab issue tracker
- [assets/issue-tracker-local.md](assets/issue-tracker-local.md): local-markdown issue tracker
- [assets/triage-labels.md](assets/triage-labels.md): implementation triage role mapping
- [assets/domain.md](assets/domain.md): domain doc consumer rules and layout

For other issue trackers, write `docs/agents/issue-tracker.md` from the confirmed workflow.

Check that all required docs exist in the agreed locations, local links resolve, template placeholders are replaced, and commands match the repo's scripts and configuration. Run safe local checks when feasible; record what was actually verified. Setup writes documentation only: do not deploy, provision infrastructure, publish releases, or mutate the external tracker to test the instructions.

### 5. Done

Tell the user which files were created or updated, what was verified, and any remaining gaps. Agents can now follow the pointers in `AGENTS.md`; do not claim every installed skill reads these files automatically.

Mention they can edit the docs directly later. Re-running this skill is useful when workflows change or the baseline needs refreshing.
