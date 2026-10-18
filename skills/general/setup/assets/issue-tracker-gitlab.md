# Issue tracker: GitLab

Issues for this repo live in **<namespace/project>** on **<GitLab host>**. Use the `glab` CLI for all operations.

## Conventions

Run inside this project's clone so `glab` infers the project from its remote. If issues live elsewhere or remotes are ambiguous, record the explicit project selection here. For a self-hosted instance, authenticate to the configured host.

- **Create an issue**: `glab issue create --title "..." --description "..."`.
- **Read an issue**: `glab issue view <number> --comments`.
- **List issues**: `glab issue list`. Use label and state filters as needed.
- **Comment on an issue**: `glab issue note <number> --message "..."`. GitLab calls comments "notes".
- **Apply / remove labels**: `glab issue update <number> --label "..."` / `--unlabel "..."`. Use `docs/agents/triage-labels.md` to map implementation triage roles to this repo's label strings.
- **Close**: post the explanation with `glab issue note`, then run `glab issue close <number>`.

Check the installed CLI's help before using version-dependent flags or API operations.

## Parent tickets and blocking relationships

Record `Part of #<parent>` in each child description and list the children in the parent. Use native blocking links when the project's GitLab tier supports them; otherwise record `Blocked by: #<number>, #<number>` in the description. A ticket is unblocked when every blocker is closed.

## When a skill says "publish to the issue tracker"

Create a GitLab issue in the configured project.

## When a skill says "fetch the relevant ticket"

Read the issue body and comments with `glab issue view <number> --comments`.

## Wayfinding operations

Used by `wayfinder`. The map is a single issue with child issues as decision tickets. Check the installed CLI's help before using version-dependent flags or API operations.

- **Map**: create an issue labelled `wayfinder:map`, holding the Destination, Notes, Decisions so far, Not yet specified, and Out of scope sections.
- **Child ticket**: create an issue with `Part of #<map>` near the top of its description and a `wayfinder:<type>` label, where the type is `research`, `prototype`, `alignment`, or `task`. List it in the map's child task list to establish order. Decision tickets never carry implementation triage labels.
- **Blocking**: use native blocking links on Premium/Ultimate when available, for example `glab issue note <child> --message "/blocked_by #<blocker>"`. Otherwise use the `Blocked by` description fallback above. A ticket is unblocked when every blocker is closed.
- **Frontier**: enumerate all of the map's children from its child task list, preserving map order. Keep only open children with no assignee and no open blocker. Read native blocking links through the issue-links API, or resolve each issue named in `Blocked by`. Paginate API results or list commands so children beyond the default page are included. First in map order wins.
- **Claim**: re-read the ticket to check it is still open and unassigned, then `glab issue update <number> --assignee <driving-dev-login>` before any work.
- **Resolve**: `glab issue note <number> --message "<answer>"`, then `glab issue close <number>`, then append a context pointer (gist + issue link) to the map's Decisions so far section.
