# Issue tracker: GitHub

Issues for this repo live in **<owner/repo>** on GitHub. Use the `gh` CLI for all operations.

## Conventions

Run inside this project's clone so `gh` infers the repo from its remote. If issues live elsewhere or remotes are ambiguous, pass `--repo <owner/repo>` explicitly.

- **Create an issue**: `gh issue create --title "..." --body "..."`. Use `--body-file <path>` for a multi-line body stored in a file.
- **Read an issue**: `gh issue view <number> --json number,title,body,labels,comments`.
- **List issues**: `gh issue list --state open --json number,title,body,labels`. Use label and state filters as needed; fetch comments separately with `gh issue view`.
- **Comment on an issue**: `gh issue comment <number> --body "..."`.
- **Close**: `gh issue close <number> --comment "..."`.

## Parent tickets and blocking relationships

Use native sub-issues and blocking relationships when available. Check the installed CLI's help for supported operations. Native API relationships use database issue IDs, not the displayed issue numbers.

If native relationships are unavailable, put `Part of #<parent>` and `Blocked by: #<number>, #<number>` in each child body, and add children to a task list in the parent. A ticket is unblocked when every blocker is closed.

## When a skill says "publish to the issue tracker"

Create a GitHub issue in the configured repository.

## When a skill says "fetch the relevant ticket"

Read the issue body and comments with `gh issue view`.
