# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`.
- The spec is `.scratch/<feature-slug>/spec.md`.
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file.
- Record a parent ticket or source spec as a path near the top of each ticket.
- Record blocking edges as `Blocked by: <ticket numbers or paths>`, or `None`.
- Record status near the top of each ticket, preserving an established repo convention. If none exists, use `open`, `claimed`, and `resolved`.
- Comments and conversation history append to the bottom of the file under a `## Comments` heading.
- Close a ticket by recording the outcome and setting its status to `resolved`. A ticket is unblocked when every blocker is resolved.

## When a skill says "publish to the issue tracker"

Create one new file per ticket in `.scratch/<feature-slug>/issues/`, in dependency order so blockers have identifiers first. Preserve existing numbering and files.

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path, including its comments. Resolve a bare ticket number within its feature directory; ask if the feature is ambiguous.
