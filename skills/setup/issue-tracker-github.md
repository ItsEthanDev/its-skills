# Issue tracker: GitHub

Issues for this repo live in **<owner/repo>** on GitHub. Use the `gh` CLI for all operations.

## Conventions

Run inside this project's clone so `gh` infers the repo from its remote. If issues live elsewhere or remotes are ambiguous, pass `--repo <owner/repo>` explicitly.

- **Create an issue**: `gh issue create --title "..." --body "..."`. Use `--body-file <path>` for a multi-line body stored in a file.
- **Read an issue**: `gh issue view <number> --json number,title,body,labels,comments`.
- **List issues**: `gh issue list --state open --json number,title,body,labels`. Use label and state filters as needed; fetch comments separately with `gh issue view`.
- **Comment on an issue**: `gh issue comment <number> --body "..."`.
- **Apply / remove labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`. Use `docs/agents/triage-labels.md` to map implementation triage roles to this repo's label strings.
- **Close**: `gh issue close <number> --comment "..."`.

## Parent tickets and blocking relationships

Use native sub-issues and blocking relationships when available. Check the installed CLI's help for supported operations. Native API relationships use database issue IDs, not the displayed issue numbers.

If native relationships are unavailable, put `Part of #<parent>` and `Blocked by: #<number>, #<number>` in each child body, and add children to a task list in the parent. A ticket is unblocked when every blocker is closed.

## When a skill says "publish to the issue tracker"

Create a GitHub issue in the configured repository.

## When a skill says "fetch the relevant ticket"

Read the issue body and comments with `gh issue view`.

## Wayfinding operations

Used by `wayfinder`. The map is a single issue with child issues as decision tickets. Check the installed CLI's help before using version-dependent relationship flags.

- **Map**: create an issue labelled `wayfinder:map`, holding the Destination, Notes, Decisions so far, Not yet specified, and Out of scope sections.
- **Child ticket**: create an issue labelled `wayfinder:<type>`, where the type is `research`, `prototype`, `alignment`, or `task`. Link it to the map with `gh issue create --parent <map> ...` or `gh issue edit <map> --add-sub-issue <child>`. If these flags are unavailable, use the native sub-issue API; if native sub-issues are unavailable, use the parent-body fallback above. Decision tickets never carry implementation triage labels.
- **Blocking**: use native issue dependencies, such as `gh issue edit <child> --add-blocked-by <blocker>` when supported. API alternative: `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`. Obtain the database ID with `gh api repos/<owner>/<repo>/issues/<blocker> --jq .id`; it is not the displayed issue number or `node_id`. Use the `Blocked by` body fallback only when native dependencies are unavailable.
- **Frontier**: enumerate all of the map's children through its native sub-issues or fallback task list, preserving map order. Keep only open children with no assignee and no open blocker. Read native dependencies or resolve each issue named in `Blocked by`; a closed blocker no longer gates the ticket. Paginate API results rather than relying on the default issue-list limit. First in map order wins.
- **Claim**: re-read the ticket to check it is still open and unassigned, then `gh issue edit <number> --add-assignee @me` before any work. Use the driving dev's login instead if the authenticated account is not that dev.
- **Resolve**: `gh issue comment <number> --body "<answer>"`, then `gh issue close <number>`, then append a context pointer (gist + issue link) to the map's Decisions so far section.
