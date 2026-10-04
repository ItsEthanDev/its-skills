# Behavior Preservation

Use the accepted contract to decide which observations must remain equivalent. Keep known defects labelled as defects rather than treating every current output as intended behavior.

## Choose a suitable comparison

Prefer existing checks that establish the affected claims. Supplement them only where useful evidence is missing:

| Situation | Suitable evidence |
| --- | --- |
| Observable behavior lacks focused coverage | Characterization cases through the public interface, with expectations grounded in accepted behavior |
| An implementation is replaced behind a stable contract | Old/new comparisons on representative inputs, including relevant failures and effects |
| A transformation has many meaningful input shapes | Accepted fixtures or recorded, sanitized inputs replayed through the affected boundary |
| A public interaction spans components | Exercise the same user or caller path against the intended artifact or test instance |

A characterization check records an observation; it does not approve a mismatch with the requirement. State the limitation when old behavior is wrong or the source of intent is uncertain.

Use shared automated-test guidance for assertions, seams, and substitutes. Do not require a new framework, exhaustive test suite, or permanent harness for a small change.

## Compare the required dimensions

Select the dimensions that matter to the contract: returned or visible values, errors and exit status, ordering, persisted state, emitted effects, compatibility, and relevant resource or performance constraints. An equal return value does not prove an equal required side effect.

Control time, randomness, environment, and fixture state when they would otherwise confound the comparison. Normalize only irrelevant variation justified by the contract, such as a noncontractual timestamp; do not normalize away a changed error, effect, or required ordering to make results match.

Preserve the old artifact or baseline only when the comparison needs it and the assignment permits it. Use an isolated build, worktree, fixture, or temporary copy according to project conventions. Record which versions and conditions were compared, and clean up only resources this check created and is permitted to remove.

Use `verifying-work` to execute checks and classify their results. An incomplete or wrong-boundary comparison must remain a coverage limit, not proof of equivalence.
