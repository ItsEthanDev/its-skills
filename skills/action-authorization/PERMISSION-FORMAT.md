# Permission file format

The project permission file contains active project-specific denials and standing permissions. Leave defaults in the skill and temporary grants in the conversation.

## Record format

Start with `# Action permissions`. Give each decision a stable, unique heading and these fields:

- **Decision:** `Deny` or `Standing permission`.
- **Action:** the operation or bounded class of operations.
- **Target:** exact repositories, remotes, branches, services, accounts, hosts, or environments, or an explicitly approved target set. Avoid targets that silently change with local configuration.
- **Constraints:** limits on methods, effects, data, resources, cost, and prerequisites, including relevant exclusions. Use `None` only for explicitly approved unconstrained scope.
- **User decision:** date and concise account of the explicit decision; include a conversation/decision reference if available. Omit credentials and sensitive payloads; invent no references.

Use separate records for different scopes. Clarify underspecified or conflicting records with the user rather than infer permission.

## Example

Illustrative only; record only scopes the user actually approved.

```markdown
# Action permissions

## AP-001 — Push feature branches

- **Decision:** Standing permission
- **Action:** Push completed, verified commits.
- **Target:** Remote `origin` in this repository; branches under `feature/`.
- **Constraints:** Normal pushes only. Excludes default-branch changes, force-pushes, and pushes that trigger deployments.
- **User decision:** YYYY-MM-DD — User explicitly granted standing permission for these pushes.
```

## Update active records

Preserve unrelated decisions. For an explicitly revised or revoked decision, update or remove its record; keep proposals and superseded text outside active records. Version control preserves history.

Recording a decision does not authorize pushing the file. If persistence fails, report it; the decision still applies in the current session, but do not claim it will survive that session.
