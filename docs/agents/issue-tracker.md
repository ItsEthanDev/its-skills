# Issue tracker: GitHub

Issues live in `ItsEthanDev/its-skills`. Use `gh` with an explicit repository
argument, or the repository-qualified API paths below.

Authentication must be configured before remote operations. Documentation of
an operation is not authorization to execute it.

## Common operations

```sh
gh issue create --repo ItsEthanDev/its-skills --title "..." --body-file body.md
gh issue view NUMBER --repo ItsEthanDev/its-skills \
  --json number,title,body,labels,comments,assignees,state
gh issue list --repo ItsEthanDev/its-skills --state open \
  --json number,title,labels,assignees
gh issue comment NUMBER --repo ItsEthanDev/its-skills --body-file answer.md
gh issue edit NUMBER --repo ItsEthanDev/its-skills --add-label "LABEL"
gh issue edit NUMBER --repo ItsEthanDev/its-skills --remove-label "LABEL"
gh issue close NUMBER --repo ItsEthanDev/its-skills
```

Replace uppercase arguments with actual values. Use
[triage labels](triage-labels.md) for implementation tickets.

When instructed to publish a spec or fetch a ticket, use this repository's issues.
Read comments as well as the body when loading a ticket.

## Native relationships

Use native sub-issues and blocking dependencies. Inspect installed CLI help
before using relationship flags; otherwise use the native API.

API relationship writes use database issue IDs, not displayed issue numbers.
Obtain an ID with:

```sh
gh api repos/ItsEthanDev/its-skills/issues/NUMBER --jq .id
```

Attach an existing child to its parent:

```sh
gh api --method POST repos/ItsEthanDev/its-skills/issues/PARENT/sub_issues \
  -F sub_issue_id=CHILD_DATABASE_ID
```

Record that a child is blocked by another issue:

```sh
gh api --method POST \
  repos/ItsEthanDev/its-skills/issues/CHILD/dependencies/blocked_by \
  -F issue_id=BLOCKER_DATABASE_ID
```

If GitHub lacks the relevant native capability, record `Part of #NUMBER`
and `Blocked by: #NUMBER` in child bodies, and maintain an ordered child task
list in the parent. Missing CLI flags alone do not justify this fallback.
Authentication, permission, and transient failures are blockers, not evidence
that native relationships are unavailable.

## Wayfinding operations

Refer to maps and tickets by linked titles in human-facing prose.

- **Map:** one issue labelled `wayfinder:map`, containing Destination, Notes,
  Decisions so far, Not yet specified, and Out of scope.
- **Children:** decision issues with one type label: `wayfinder:research`,
  `wayfinder:prototype`, `wayfinder:alignment`, or `wayfinder:task`.
  Create issues first, then attach them and wire blocking relationships.
  Maps and children carry only `wayfinder:` labels.
- **Frontier:** enumerate the map's native children in their returned order.
  Keep open, unassigned children whose blockers are all closed.
  Fetch all pages of children and dependencies. Use the fallback parent task
  list order only when native sub-issues are unavailable.
- **Claim:** re-read the selected ticket and skip it if closed or assigned.
  Assign it to the developer driving the map before starting work.
  Use `--add-assignee @me` only when the authenticated account is that developer.
  Re-read after assignment; assignment is not an atomic lock, so stop and
  coordinate if concurrent claims conflict.
- **Resolve:** post the answer as a comment, close the ticket, then append a
  linked-title gist to the map's Decisions so far. Preserve concurrent map
  changes by re-reading before editing its body.

List native children and blockers using paginated API reads:

```sh
gh api --paginate \
  'repos/ItsEthanDev/its-skills/issues/MAP/sub_issues?per_page=100'
gh api --paginate \
  'repos/ItsEthanDev/its-skills/issues/CHILD/dependencies/blocked_by?per_page=100'
```

Claim example:

```sh
gh issue edit NUMBER --repo ItsEthanDev/its-skills --add-assignee DEVELOPER_LOGIN
```

Required remote labels are the five implementation labels and the five
`wayfinder:` labels documented here. Setup does not create them.

## Verification limits

The local repository check passes. Authenticated tracker operations, label
existence, and native relationship operations have not been exercised during
setup.
