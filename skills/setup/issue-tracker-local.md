# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`.
- The spec is `.scratch/<feature-slug>/spec.md`.
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file.
- Record a parent ticket or source spec as a path near the top of each ticket.
- Record blocking edges as `Blocked by: <ticket numbers or paths>`, or `None`.
- For implementation tickets, record triage state as a `Status:` line near the top, using the role strings configured in `docs/agents/triage-labels.md` (for example, `ready-for-agent`). Preserve an established repo convention and adapt templates to the configured strings.
- Comments and conversation history append to the bottom of the file under a `## Comments` heading.
- Close a ticket by recording the outcome and setting its status to `resolved`. A ticket is unblocked when every blocker is resolved. Decision tickets use the lifecycle convention in "Wayfinding operations" below, not implementation triage roles.

## When a skill says "publish to the issue tracker"

Write specs to `.scratch/<feature-slug>/spec.md`. Create one new implementation ticket per file in `.scratch/<feature-slug>/issues/`, in dependency order so blockers have identifiers first. Preserve existing numbering and files. For Wayfinder maps and decision tickets, use "Wayfinding operations" below.

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path, including its comments. Resolve a bare ticket number within its feature directory; ask if the feature is ambiguous.

## Wayfinding operations

Used by `wayfinder`. The map is a file with one child file per decision ticket.

- **Map**: `.scratch/<effort>/map.md`, holding the Destination, Notes, Decisions so far, Not yet specified, and Out of scope sections.
- **Child ticket**: `.scratch/<effort>/issues/<NN>-<slug>.md`, numbered from `01`, with the question in the body and the map path near the top. A `Type:` line records `research`, `prototype`, `alignment`, or `task`; a `Status:` line records `open`, `claimed`, or `resolved`. New decision tickets start as `open`; they never carry implementation triage roles.
- **Blocking**: a `Blocked by: <NN>, <NN>` line near the top, or `None`. A ticket is unblocked when every listed blocker is `resolved`.
- **Frontier**: scan the map's child files for tickets with `Status: open` and no unresolved blockers; first by number wins. Claimed and resolved tickets are excluded.
- **Claim**: set `Status: claimed` and save before any work. Re-read the ticket first; skip it if another session has already claimed or resolved it.
- **Resolve**: append the answer under an `## Answer` heading, set `Status: resolved`, then append a context pointer (gist + relative file link) to the map's Decisions so far section.
