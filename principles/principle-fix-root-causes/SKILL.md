---
name: principle-fix-root-causes
description: "Apply when assessing a defect or proposed fix. Prefer evidenced causal explanations over symptom suppression, while preserving the authorized repair scope."
disable-model-invocation: true
---

# Fix Root Causes

A fix should address the mechanism that causes a defect, not merely hide its visible symptom. Workarounds can leave the cause intact and accumulate complexity.

- Reproduction, instrumentation, and causal explanations strengthen confidence in a proposed fix. When reproduction is unavailable, state the resulting uncertainty instead of guessing.
- Judge a guard by its purpose. Validation of genuinely invalid input can be correct; a nil check that conceals a broken invariant is symptom suppression.
- A long workaround explanation is a reason to examine the design, not proof by itself that the code is wrong.
- Look for repeated instances when they help establish the cause or repair scope. Fix only those within the authorized assignment and report broader needs.
- Prefer evidence from actual errors and state over speculative explanations.

## Restart-related failures

Persistent state, caches, configuration, lock files, and serialized data are hypotheses worth examining when behavior changes after restart. Restoration after clearing state is evidence to investigate, not proof that state validation is the only fix.

Do not delete state or broaden repairs merely to test a hypothesis without the required authorization. The investigation strategy and execution sequence belong to the caller's workflow.
