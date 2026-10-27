# Issue tracker

The issue tracker is where issues live for this project. Skills need to know whether to call a CLI, write a markdown file under `.scratch/`, or follow some other workflow you describe. Pick the place you actually track work for this project. If the user does not want an issue tracker, leave this feature out; do not create one just to complete setup.

If a project remote points at GitHub, propose GitHub. If it points at GitLab (including a self-hosted instance), propose GitLab. Otherwise, or if the user prefers, offer:

- **GitHub**: issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab**: issues live in the repo's GitLab Issues (uses the `glab` CLI)
- **Local markdown**: issues live as files under `.scratch/<feature>/` in this repo
- **Other** (Jira, Linear, etc.): ask the user to describe the workflow in one paragraph

Record the choice in the project's issue-tracker guidance; `docs/agents/issue-tracker.md` is a starting location, not a requirement. Resolve ambiguous remotes or a tracker in a different repository with the user. Use the selected tracker seed, adapting paths and keeping the sections needed by the agreed workflows. Include the template's "Wayfinding operations" section when wayfinding is used. For another tracker, establish its project identifier and how to create, read, list, comment on, and close tickets; when relevant, also record how to store a Wayfinder map, identify and type its children, record blocking, select the frontier, claim a ticket, and resolve it.

Implementation triage is a separate feature. Don't require implementation labels for projects that track only decisions, research, or learning activities. Remove references to unselected triage or implementation workflows from the seed. Record any needed remote labels without creating them; setup does not mutate the external tracker to establish or test the documentation.

Record authorization requirements and verification limits alongside the operations. Published instructions are not permission to execute remote writes. Switching trackers must not move or delete existing issues. Link the agreed guidance from the README's documentation index.
