# Qualitative evaluation

## Make the comparison explicit

Translate the intended improvement into observable criteria before editing. Identify the reader, user, or maintainer whose work should improve and select representative tasks or cases. Include a difficult case and relevant counterexamples, not only cases that favor the proposed change.

Define what would count as better, worse, or inconclusive for each criterion. Use concrete observations rather than aesthetic preference or invented numeric scores. Keep hard constraints distinct from preferences. Set priorities for competing qualities from the request and accepted decisions; ask when a consequential priority is unresolved.

## Compare artifacts on the same cases

Preserve the baseline and compare the candidate with the current best using the same criteria, tasks, and context. Inspect or exercise the actual artifacts. Cite passages, dependencies, execution paths, task outcomes, or other specific evidence for each judgment.

Use observed user or agent behavior when the claimed improvement depends on that behavior. Static inspection can establish that contradictory statements were removed, but cannot establish that readers now make fewer mistakes. If behavioral evaluation is unavailable, narrow the claim and report the unverified outcome.

Separate facts from judgments. Record what changed, why it helps the selected task, what got worse, and what remains unknown.

When feasible within the run's permissions and resources, launch a fresh evaluator subagent separate from the attempt author. Give it the criteria, cases, preserved constraints, and both artifacts, but not the attempt author's preferred verdict. Use neutral artifact labels and withhold which is the candidate when practical. Keep the evaluator read-only and require specific evidence for advantages, regressions, and uncertainty. It reports a comparison, not an acceptance decision. External evaluation still requires explicit authorization.

If a separate evaluator is not feasible, state the limitation and have the supervisor compare the actual artifacts directly against the fixed criteria. The attempt author's self-assessment alone is insufficient. Keep final acceptance with the supervisor even when an evaluator recommends a winner.

## Decide from evidence

Accept the candidate when it improves the stated criteria without unacceptable regressions or costs. A persuasive explanation of the edit is not evidence that the artifact is better. Retain the current best when the comparison is a tie or remains inconclusive. Ask for a decision when improvements require a consequential tradeoff outside delegated judgment.

Use examples such as these to choose evidence, not to prescribe targets:

| Objective | Representative comparison | Evidence and limits |
| --- | --- | --- |
| Make an operational guide easier to follow | Locate a prerequisite, perform the routine procedure, and recover from a failure using each version | Identify missing steps, ambiguous choices, and information needed at the point of action. Without reader trials, claim improved coverage or wording, not faster task completion. |
| Improve an interface boundary | Trace the same consumer tasks and explore a representative future change against both designs | Identify leaked invariants, duplicated decisions, and unrelated changes required. A hypothetical change reveals design pressure, not measured future maintenance savings. |
| Clarify a product proposal | Answer the same questions about behavior, exclusions, and unresolved choices from each draft | Cite answers made explicit and contradictions removed. Preserve unresolved product decisions instead of silently resolving them for cleaner prose. |

For mixed evidence, report the measured outcome and qualitative comparison separately. Do not collapse unlike criteria into an unsupported overall score.
