# Permission file format

Use `docs/agent/action-permissions.md`, or the location explicitly designated by project instructions. This file contains active project-specific denials and standing permissions, not a copy of skill defaults or a transcript of temporary approvals.

## Structure

Start with `# Action permissions`. Give each decision a stable, unique heading and these fields:

- **Decision:** `Deny` or `Standing permission`.
- **Action:** the operation or bounded class of operations.
- **Target:** repository, remote, branch, service, account, host, or environment. Name exact targets or an explicitly approved target set; avoid relying on whichever target happens to be configured later.
- **Constraints:** limits on methods, effects, data, resources, cost, and prerequisites. State exclusions that matter. Use `None` only when the user explicitly approves an unconstrained scope.
- **User decision:** a concise account of the explicit approval or denial, including its date and available conversation/decision reference. Do not invent a reference or store credentials or sensitive payloads.

Use separate records when actions, targets, or constraints differ. An underspecified record is not permission to guess. Resolve conflicting records with the user; a specific denial overrides a broader permission until explicitly changed.

## Example

This is illustrative, not an active grant. Substitute only scopes the user actually approved.

```markdown
# Action permissions

## AP-001 — Push feature branches

- **Decision:** Standing permission
- **Action:** Push completed, verified commits.
- **Target:** Remote `origin` in this repository; branches under `feature/`.
- **Constraints:** Normal pushes only. Excludes default-branch changes, force-pushes, and pushes that trigger deployments.
- **User decision:** YYYY-MM-DD — User explicitly granted standing permission for these pushes.

## AP-002 — Production database mutations

- **Decision:** Deny
- **Action:** Change production database data or schema.
- **Target:** Production database for this project.
- **Constraints:** Includes mutations through APIs, SQL, scripts, and migrations. Read-only development inspection remains permitted.
- **User decision:** YYYY-MM-DD — User explicitly denied agent-performed production database mutations.
```

## Maintenance

Record only explicit user decisions. Preserve unrelated records and scope each edit to the decision made. A denial of a proposed operation covers that operation, not every action on its service.

Keep this file limited to active records. When the user explicitly revises or revokes a decision, update or remove the affected record and record the new decision source where applicable. Let version control preserve history; keep proposals and superseded text outside the active records so they cannot be mistaken for current permission.

A durable decision authorizes its documentation, not a remote push of the documentation. If the file cannot be written, report that persistence failed; do not claim the decision will survive the session. Continue to honor an explicit denial in the current session even if recording it fails.
