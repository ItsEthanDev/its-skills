# Automated Tests

## Choose and approve the seam

A **seam** is the public boundary where the test exercises behavior and observes its result. Read project domain context and decisions relevant to that boundary so names and expectations match the accepted model.

Before writing maintained tests, use an already approved seam or obtain confirmation for a new or changed seam. When an approved implementation plan identifies its selected seams, reuse that approval. Otherwise record the selection in the project's existing work artifact and obtain confirmation before writing the first maintained test. Do not create a standalone seams file by default or ask again for each test at an approved seam.

Running existing tests or making a temporary observation does not require a new seam-approval pause. Temporary checks still require permission for their actions and effects.

If the interface itself is uncertain, read `principle-design-deep-modules` for seam and interface design criteria. Report a necessary redesign rather than adopt it solely to make a test convenient.

## Write a discriminating assertion

Test behavior users or callers care about through the chosen interface. Prefer tests that survive internal refactoring and whose names state the capability rather than implementation steps.

Use an independent expected value: an accepted requirement, known literal, worked example, or authoritative fixture. Do not recompute the expected result using the same logic under test or generate a baseline from the output being verified without an independent review of its meaning.

Keep each test focused on one behavior. Multiple assertions may establish that behavior; assertion count alone does not determine test quality. Check relevant failure cases and boundary values rather than accumulate cases with no relationship to the claim.

For examples of meaningful assertions and implementation-coupled or tautological tests, read [Good and bad tests](tests.md). When selecting dependency substitutes, read [When to mock](mocking.md).

## Check that the test can detect the mistake

Inspect whether the assertion would fail for the plausible defect. Where practical and authorized, demonstrate that sensitivity using a known failing fixture, the original reproduction, or a disposable incorrect implementation. Restore any temporary change and re-run the correct case. Do not introduce live breakage or modify another person's work to manufacture a red result.

A runner exiting successfully is not enough when it skipped the test or exercised the wrong path. Check the selected cases and their observations. Preserve a useful failure signal; do not suppress errors or refresh snapshots simply to obtain green output.
