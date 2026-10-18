# Issue tracker

The issue tracker is where issues live for this repo. Skills need to know whether to call a CLI, write a markdown file under `.scratch/`, or follow some other workflow you describe. Pick the place you actually track work for this repo.

If a project remote points at GitHub, propose GitHub. If it points at GitLab (including a self-hosted instance), propose GitLab. Otherwise, or if the user prefers, offer:

- **GitHub**: issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab**: issues live in the repo's GitLab Issues (uses the `glab` CLI)
- **Local markdown**: issues live as files under `.scratch/<feature>/` in this repo
- **Other** (Jira, Linear, etc.): ask the user to describe the workflow in one paragraph

Record the choice in `docs/agents/issue-tracker.md`. Resolve ambiguous remotes or a tracker in a different repository with the user. Include the template's "Wayfinding operations" section, adapted to the configured tracker. For another tracker, establish its project identifier and how to create, read, list, comment on, and close tickets; also record how to store a Wayfinder map, identify and type its children, record blocking, select the frontier, claim a ticket, and resolve it.

**Triage label vocabulary.** Recommend the default roles from [triage-labels.md](../assets/triage-labels.md): `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`. Ask whether to keep those strings; preserve any existing mapping or collect the user's overrides. Record the agreed mapping in `docs/agents/triage-labels.md`. Local implementation tickets use those strings in `Status:`; Wayfinder decision tickets instead use the tracker-specific lifecycle convention. Record required remote labels without creating them: setup writes documentation only.
