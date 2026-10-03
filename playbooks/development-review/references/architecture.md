# Architecture review

Survey repository structure for evidence-backed opportunities to improve interfaces, locality, leverage, testability, and navigability. Load `principles`, select **Design Deep Modules**, and use its module, interface, depth, seam, adapter, leverage, locality, and deletion-test vocabulary.

## Establish the system view

When the user does not name a narrower scope, treat the whole repository as in scope. Identify composition roots, major modules, dependency direction, public interfaces, state owners, external adapters, tests, domain context, and applicable ADRs or governance. Use history and current work to prioritize investigation, not to narrow the declared scope.

State that a repository-wide structural survey maps and samples consequential architecture; it is not a claim that every line was inspected.

## Inspect

Look for observed friction:

- understanding one concept requires movement across many shallow modules;
- callers must know implementation details, ordering rules, or scattered invariants;
- policy or state ownership is duplicated across seams;
- a logical change repeatedly requires shotgun edits;
- tests bypass the public interface or rely on artificial seams created only for mocking;
- dependency direction conflicts with documented ownership;
- pass-through modules add interface without hiding decisions;
- missing seams make real variation, failure, or replacement difficult to test;
- legacy and replacement paths preserve complexity without an active migration need; or
- module names and interfaces obscure canonical domain concepts.

Apply the deletion test to a suspected shallow module. An opportunity is stronger when deletion would redistribute meaningful complexity to callers and the proposed deepening would concentrate that complexity behind a smaller interface. One adapter does not justify a seam without other demonstrated variation.

## Calibrate opportunities

Support each opportunity with concrete files, call paths, change history, test friction, or leaked knowledge. Explain the likely direction and payoff without designing a detailed replacement interface during review. Distinguish current friction from a speculative future benefit, identify conflicts with existing ADRs, and permit a result with no worthwhile opportunities.

Route a selected opportunity to the project's intended-behavior owner when it changes externally meaningful behavior, its technical-design owner when it preserves behavior, or its durable-rule owner when it requires new governance. Identify actual artifacts or locations; do not initiate their workflows.

## Complete the lens

Describe the repository structure inspected, the important areas sampled, and the limits of the survey. Rank only evidenced opportunities; do not fill a quota or generate a standalone architecture report.
