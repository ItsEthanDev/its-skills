---
name: principle-encode-lessons-in-structure
description: "Apply to recurring corrections or failure-prevention rules. Prefer feasible, proportionate structural enforcement over repeated instructions."
disable-model-invocation: true
---

# Encode Lessons in Structure

A recurring rule is more dependable when a mechanism enforces it than when every reader must notice, remember, and comply. Prefer structural enforcement where it is feasible and proportionate.

- Consider an unrepresentable state, metadata flag, lint rule, canonical helper, runtime check, or script according to the failure being prevented.
- Favor the strongest appropriate mechanism, not the strongest mechanism regardless of cost. Enforcement must fit the project's tools, constraints, and actual recurring problem.
- Retain guidance that requires judgment or explains limits the mechanism cannot enforce. Make that guidance concrete with an example of the failure mode.
- Delete redundant instructions only after the replacement mechanism is established and its coverage is understood.
- Distinguish a recurring pattern from a one-off correction before generalizing it. A correction alone does not justify new automation or a durable personal record.

A structural diagnosis does not authorize its implementation. Apply an accepted fix within scope, or report the proposed follow-up for an authorized decision. Record information only in an appropriate owner when recording is permitted; do not persist every correction automatically.
