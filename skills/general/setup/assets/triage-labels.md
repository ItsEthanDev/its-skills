# Triage Labels

Skills use canonical triage roles. This file maps each role to the label string used by this repo's issue tracker, or the `Status:` value used by local implementation tickets.

| Skill role        | Label in our tracker | Meaning                                          |
| ----------------- | -------------------- | ------------------------------------------------ |
| `needs-triage`    | `needs-triage`       | Maintainer needs to evaluate this issue          |
| `needs-info`      | `needs-info`         | Waiting on the reporter for more information     |
| `ready-for-agent` | `ready-for-agent`    | Fully specified, ready for an agent to implement |
| `ready-for-human` | `ready-for-human`    | Requires human implementation                    |
| `wontfix`         | `wontfix`            | Will not be actioned                             |

When a skill mentions a role, use its configured string from the "Label in our tracker" column. Edit that column to match existing tracker vocabulary rather than introducing duplicate labels.

These roles apply to implementation triage, not Wayfinder decision tickets. Decision ticket types and claiming/resolution conventions belong to the issue tracker doc's "Wayfinding operations" section.
