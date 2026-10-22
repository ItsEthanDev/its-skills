---
name: setup
description: "Establish, extend, or migrate a project's documentation, conventions, and selected tooling, across the project or for a specific feature."
disable-model-invocation: true
---

# Setup

Scaffold the project documentation and configuration that people and agents need. Set up the whole project, or just the feature the user asks for: a constitution, an issue tracker, a quickstart, or another feature below.

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

The project owns the resulting conventions. Its documentation must explain how to use and maintain them without this skill being installed. Later changes to this skill do not change an existing project's rules.

## Process

### 1. Explore

Look at the current project to understand its starting state. Read whatever exists; don't assume:

- `README.md` and `AGENTS.md` at the project root: what do they already cover? Is there a documentation index? Follow existing links before assuming guidance is missing.
- Existing governance, coding standards, and decision records: where do accepted conventions live, and how are changes approved?
- Quickstart, deployment, and equivalent documentation elsewhere: are there working instructions worth preserving or linking to?
- In a Git repository, `git remote -v` and `.git/config`: where is it hosted? Which remote tracks the project?
- Manifests, lockfiles, environment configuration, scripts, and CI, where present: what prerequisites, local commands, and checks does the project actually use?
- Release workflows and infrastructure configuration, where present: what is deployed or distributed, where, and what triggers a release? What evidence exists for verification and rollback?
- `GLOSSARY.md` and `GLOSSARY-MAP.md`, or the project's linked equivalents, plus any mapped glossaries.
- `docs/agents/` and `.scratch/`: does this skill's prior output or an established tracker convention already exist?
- Monorepo signals, where present: workspace configuration or multiple packages with their own source trees. Multiple packages alone do not imply separate domain contexts. Other projects can also have distinct subject areas.

For scoped setup, inspect the requested feature and its dependencies, not every unrelated workflow. A project need not use Git, have build tooling, or deploy anything.

Finish exploration with an inventory of relevant docs, evidence for the workflows, and gaps requiring user decisions. Find facts in the project before asking the user.

### 2. Establish intent

For a new project, ask an open-ended question:

> What is this project? Tell me a little about what you want to do here.

For an existing project, summarise what's present, then ask what this setup run should accomplish. Establish whether the user wants to preserve and extend current conventions, migrate to current recommendations, or adopt selected changes. A difference from this skill's recommendations is not itself a defect.

Use the user's request when it already establishes intent; don't ask them to repeat it. Don't make them choose a project type from a menu. A project can support writing, learning, and engineering together.

Keep a scoped request scoped. "Set up a constitution" does not mean reconfigure the tracker or replace the project's commit policy. Surface necessary dependencies and conflicts before expanding the work.

### 3. Present findings and ask

Summarise what's present and what's missing. Recommend the features that serve the user's intent, and explain what each would establish. For general setup, start with a project overview and discoverable guidance; recommend the other features from the work the project will support. This is a starting recommendation, not a required document inventory.

The user decides which features to establish and when. Create a document early when they expect to use it, even if only a few rules are agreed. Don't invent content to make it look complete. Skip features they don't want; a project need not have a constitution, decision records, or an issue tracker.

Then take the selected features in an order that respects their dependencies. One section, one answer, then the next. Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip questions already settled by the request or existing configuration.

Read only the references for the selected features, when you reach them:

| Feature                    | Read when setting up                                             | Seed templates                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Project overview           | [references/project-docs.md](references/project-docs.md)         | [README](assets/readme.md)                                                                                                          |
| Documentation discovery    | [references/discovery.md](references/discovery.md)               | [Agent navigation](assets/agent-guidance.md)                                                                                        |
| Quickstart                 | [references/quickstart.md](references/quickstart.md)             | [Quickstart](assets/quickstart.md)                                                                                                  |
| Deployment or distribution | [references/deployment.md](references/deployment.md)             | [Deployment](assets/deployment.md)                                                                                                  |
| Issue tracker              | [references/issue-tracker.md](references/issue-tracker.md)       | [GitHub](assets/issue-tracker-github.md), [GitLab](assets/issue-tracker-gitlab.md), [local markdown](assets/issue-tracker-local.md) |
| Implementation triage      | [references/triage-labels.md](references/triage-labels.md)       | [Triage labels](assets/triage-labels.md)                                                                                            |
| Domain language            | [references/domain-docs.md](references/domain-docs.md)           | [Glossary](assets/glossary.md), [consumer guidance](assets/domain.md)                                                               |
| Decision records           | [references/decision-records.md](references/decision-records.md) | [Record index](assets/decision-record-index.md), [agent guidance](assets/decision-records.md)                                       |
| Constitution               | [references/constitution.md](references/constitution.md)         | [Constitution](assets/constitution.md), [agent guidance](assets/constitution-guidance.md)                                           |

Paths in the templates are starting points, not requirements. Preserve existing owners and agree on locations before writing. When adding guidance or changing its location, include documentation discovery in scope so people and agents can find it.

### 4. Confirm and edit

Show the user a draft of all proposed additions and changes for the selected features, including index and agent-pointer changes.

For migration, show what is being replaced, what depends on the old convention, and how those consumers and links will be reconciled. Follow the project's existing amendment and approval procedure; approving setup does not bypass it.

Use the seed templates as starting points, adapting paths and commands to the project. Preserve their strong guidance, conventions, and wording where applicable rather than summarizing away the methods. Show unresolved facts and any instructions you could not verify. Let the user edit before writing. Proceed only after they approve the draft.

### 5. Write and verify

Preserve user edits and unrelated sections in every existing file. On reruns, make only the agreed changes; switching trackers must not move or delete existing issues. Update existing sections in-place rather than appending duplicates.

Keep procedures in their owning docs. Index human-facing artifacts under Project documentation and agent procedures under Agent documentation in the README. Put direct, conditional links to the selected guidance in the harness-loaded instruction file rather than duplicate the procedures there. Write the conventions and their maintenance instructions into the project: future contributors must not need this skill or its templates to understand the rules.

Write standing project documentation as the current design and procedures. Retained historical verification evidence, migration progress, and transitional context belong in the configured issue tracker. Link to the tracker only for general discovery, such as its location in global guidance. Do not link to specific issues or pull requests, or direct readers to search the tracker for topic-specific context, from standing documentation. Keep accepted conventions, required procedures, and decision rationale in their project-owned documents so the tracker is dispensable. These restrictions do not apply to tickets or other active work in the tracker.

Check that all selected docs exist in the agreed locations, local links resolve, template placeholders are replaced, and commands match the project's scripts and configuration. Follow discovery from both README sections and the direct harness pointers through the relevant guidance. Confirm that human-facing artifacts and agent procedures are separated, their links resolve, and a contributor can apply the selected methods, format, and maintenance/approval rules using only project documentation, without consulting tracker history. Check proposed standing documentation for historical or transitional narratives and topic-specific tracker references. No required procedure may exist only in this skill, its references, or removable template comments. Leave unselected features alone.

Run safe local checks when feasible; record what was actually verified. Setup may write documentation and configure approved local tooling. Before executing dependency installation or checks, inspect lifecycle hooks and command effects. Obtain separate authorization for effects outside the approved scope. Do not deploy, provision infrastructure, publish releases, activate systems, or mutate the external tracker to test the instructions. Documenting a push or deployment procedure is not permission to execute it.

### 6. Done

Tell the user which files were created or updated, what was verified, and any remaining gaps. Distinguish documented procedures from exercised ones. Agents can now follow the pointers in `AGENTS.md`; do not claim every installed skill reads these files automatically.

Mention they can edit the docs directly later. Re-running this skill is useful when workflows change, a feature is needed, or the project wants to adopt newer conventions. It can be scoped to that work.
