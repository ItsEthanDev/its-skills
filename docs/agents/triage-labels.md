# Triage labels

Use these GitHub labels for implementation triage.

| Skill role        | Label             | Meaning                                   |
| ----------------- | ----------------- | ----------------------------------------- |
| `needs-triage`    | `needs-triage`    | Maintainer evaluation required.           |
| `needs-info`      | `needs-info`      | Waiting for missing information.          |
| `ready-for-agent` | `ready-for-agent` | Fully specified for agent implementation. |
| `ready-for-human` | `ready-for-human` | Requires human implementation.            |
| `wontfix`         | `wontfix`         | Will not be actioned.                     |

Wayfinder maps and decision tickets use only `wayfinder:` labels, not these
implementation labels. Their lifecycle is defined in
[Issue tracker](issue-tracker.md#wayfinding-operations).

These are the agreed label names. Setup does not create remote labels or verify
whether they already exist.

## Maintenance

When a skill names a triage role, use its configured label string.
Changes to mappings require explicit project-maintainer approval. Update this
owner rather than introducing duplicate labels. Remote label changes require
separate authorization.
