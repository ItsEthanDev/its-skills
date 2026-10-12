# Issue tracker: GitLab

Issues for this repo live in **<namespace/project>** on **<GitLab host>**. Use the `glab` CLI for all operations.

## Conventions

Run inside this project's clone so `glab` infers the project from its remote. If issues live elsewhere or remotes are ambiguous, record the explicit project selection here. For a self-hosted instance, authenticate to the configured host.

- **Create an issue**: `glab issue create --title "..." --description "..."`.
- **Read an issue**: `glab issue view <number> --comments`.
- **List issues**: `glab issue list`. Use label and state filters as needed.
- **Comment on an issue**: `glab issue note <number> --message "..."`. GitLab calls comments "notes".
- **Close**: post the explanation with `glab issue note`, then run `glab issue close <number>`.

Check the installed CLI's help before using version-dependent flags or API operations.

## Parent tickets and blocking relationships

Record `Part of #<parent>` in each child description and list the children in the parent. Use native blocking links when the project's GitLab tier supports them; otherwise record `Blocked by: #<number>, #<number>` in the description. A ticket is unblocked when every blocker is closed.

## When a skill says "publish to the issue tracker"

Create a GitLab issue in the configured project.

## When a skill says "fetch the relevant ticket"

Read the issue body and comments with `glab issue view <number> --comments`.
