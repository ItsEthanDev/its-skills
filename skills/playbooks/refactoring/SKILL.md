---
name: refactoring
description: Refactor, simplify, or reorganize code while preserving accepted behavior. Use for authorized structural changes and internal interface reshaping.
---

# Refactoring

## Establish the change

Identify the observed structural problem, the intended improvement, affected consumers, and the permitted edit boundary. Use concrete friction such as duplicated knowledge, scattered invariants, unnecessary indirection, or a change that repeatedly touches unrelated places. Decline cosmetic reshaping with no useful benefit.

Read applicable requirements, contracts, project decisions, and the relevant code before choosing a target shape. Separate accepted behavior from observed quirks and known defects. Report a discovered bug or missing feature as a separate finding; repair or implement it only when the assignment includes that authority. Continue unaffected structural work only while adequate evidence remains.

When interface depth or seam placement matters, read `principle-design-deep-modules`. When the shape duplicates domain knowledge, read `principle-model-the-domain`. When evaluating removal or an added abstraction, read `principle-subtract-before-you-add` and `principle-minimize-reader-load`. Use the criteria relevant to the observed problem, not every principle for every refactor.

## Establish behavior evidence

Use `verifying-work` to select and execute checks against the preserved contract. Run suitable existing checks before changing structure so their actual coverage and initial result are known.

When coverage is insufficient or an old/new comparison is needed, read [Behavior preservation](references/behavior-preservation.md). Before writing maintained tests, read `verifying-work` and its `references/automated-tests.md` resource for quality and seam approval. Do not start a test-first development workflow merely because a refactor needs a check.

If a defect, missing prerequisite, or ambiguous requirement prevents establishing the relevant preserved behavior, report the gap and seek the necessary decision rather than manufacture a passing baseline. Record known failures separately from the checks expected to stay satisfied.

## Change structure and recheck

Name the smallest sufficient target shape and why it addresses the observed problem. Make bounded changes, rechecking affected behavior after each meaningful unit. Preserve unrelated work. Follow project rules for any explicitly authorized isolated intermediate breakage; the delivered artifact must meet the preserved contract.

For an internal API replacement, use `principle-migrate-callers-then-delete-legacy-apis` when its conditions apply. Inventory actual callers and references, including serialized names, configuration, documentation, and tests where relevant. Do not infer that external consumers can absorb the same coordinated change.

When a check fails, use its finding to revise the structural change within the assignment and recheck. Separate a behavior change from a faulty check or an existing defect before editing further. Do not weaken expected results, discard distinct test coverage, or refresh a baseline simply to obtain a pass.

## Judge and report the result

Verify the final artifact through `verifying-work`, including the affected user or caller path and relevant regression checks. Compare the delivered structure with the stated benefit: which duplicated decisions, indirection, invalid states, or change friction were actually removed?

If the change does not earn its complexity, revise or abandon only this assignment's changes. Follow the project's normal commit and delivery rules; refactoring alone does not authorize publication or an independent review.

Return the structural change and observed benefit, preserved behavior and supporting checks, known defects kept separate, and remaining verification limits. Return broader needs and control to the caller.
