---
name: hillclimb
description: Improve a selected target through supervised subagent experiments using quantitative or qualitative evidence.
disable-model-invocation: true
---

# Hillclimb

Establish what better means, delegate one hypothesis per attempt, and retain only supported improvements. Invoke explicitly. Use subagents for every attempt. If subagent tools are unavailable or applicable instructions prohibit delegation, report the blocker rather than silently run solo. Stay within the authorized edit and execution boundaries; subagents receive no broader authority, and hillclimbing does not authorize external actions or changes to accepted requirements.

Keep the objective, evaluation criteria, baseline, experiment record, and acceptance decision with the supervisor. Follow user direction and intentional project conventions for subagent tooling and model selection; do not require a particular provider or model.

## Establish the run

1. **Bound the objective.** Identify the target, intended improvement, editable surface, preserved behavior and constraints, and consequential tradeoffs. Read the applicable requirements and the target before choosing an evaluation. Use `understanding-code` when execution or architecture needs investigation, and `writing` when improving prose. Resolve missing intent or authority before experimenting.
2. **Choose the evidence.** Use quantitative results whenever an accessible measurement meaningfully reflects the objective. Read [Quantitative evaluation](references/quantitative.md) before using measurements. For qualities not adequately captured by numbers, read [Qualitative evaluation](references/qualitative.md) before making comparisons. Use both when needed. Set the improvement criteria, regression checks, and conditions that make a result inconclusive before editing. Do not substitute a convenient proxy for the actual objective.
3. **Set a stopping budget.** Follow the requested budget or intentional project convention. Otherwise, default to at most five attempts for this run. State the budget and any target before starting; do not invent a numeric target for an unspecified preference. Stop earlier when the objective is met, evidence is blocked, or remaining hypotheses do not justify their cost. Never relax criteria to claim success.
4. **Establish the baseline.** Use `verifying-work` to execute suitable checks against representative cases and preserved requirements. Confirm that the evaluation exposes the relevant weakness and can distinguish a better result from a worse one. Record known failures separately. Preserve a recoverable baseline and identify the current best artifact. If the evaluation is inadequate, repair it within authority or report the gap before changing the target.
5. **Start an experiment record.** Follow the project's experiment-record convention. Otherwise, use a small Markdown record in the run's scratch or evidence location. Record the objective, criteria, cases, baseline, budget, and artifact references. For each attempt, record its hypothesis, change, before/after evidence, regression results, verdict, and reason. Keep enough evidence to resume or reproduce the comparison without recording secrets or unrelated private data.

## Run the experiments

6. **Choose one hypothesis.** Read the record and identify a specific mechanism expected to improve the current best. Prefer the smallest coherent change that tests it. Rank hypotheses by likely benefit, evidence, cost, and reversibility. Use `refactoring` for behavior-preserving structural changes. Do not stack unevaluated changes or retry a rejected idea without new evidence.
7. **Delegate the candidate.** Preserve the current best and launch a fresh attempt subagent with the hypothesis, baseline artifact, relevant project guidance, editable surface, preserved constraints, evaluation cases and criteria, and execution permissions. Give it only the context needed for that attempt. Require the candidate artifact or diff, before/after evidence, regression results, costs, and uncertainties. Keep it from changing the evaluation criteria, accepting its own candidate, or committing or publishing independently.

   Run attempts sequentially by default. When parallel attempts are authorized and useful, start each from the same baseline in an isolated worktree or equivalent isolated artifact workspace. Give them independent edit surfaces and a bounded share of the run's attempt budget. Evaluate each candidate separately; do not merge unevaluated changes. Test any combination as a new hypothesis against the current best.

8. **Verify the returned candidate.** Inspect the actual artifact or diff and verify the evidence through `verifying-work` before deciding. Compare the candidate and current best using the same criteria and cases, and execute the regression checks. Reproduce the observations supporting acceptance rather than relying only on the attempt's summary. For qualitative comparisons, follow the separate-evaluator instructions in [Qualitative evaluation](references/qualitative.md). Keep the evaluation stable across attempts. If a case or method is invalid, document why, correct it within authority, and reevaluate the current best and candidate before accepting either result.
9. **Decide and record.** Keep a candidate only when evidence supports the intended improvement, preserved constraints hold, and its costs are justified. Discard regressions and unsupported changes. Mark unresolved comparisons inconclusive and retain the current best. Restore only this attempt's changes, preserving unrelated work. When a tradeoff exceeds delegated judgment, present the evidence and obtain the necessary decision instead of choosing new priorities. Log the verdict before the next attempt.
10. **Reconsider at a plateau.** Inspect rejected hypotheses and the target again. Try a different mechanism when it has a credible benefit within the remaining budget. Treat combinations of earlier attempts as new hypotheses requiring evaluation. Report exhaustion or blocked evidence rather than spinning or declaring an optimum.

## Finish

Recheck the final artifact against the improvement criteria and preserved requirements. Follow the project's commit and delivery rules; do not impose per-attempt commits or initiate publication. Leave the current best in place, finish or stop this run's subagents, and remove only disposable workspaces and resources created for this run. Preserve the experiment record and evidence needed by the caller.

Return the objective, evaluation method, baseline-to-final result, attempts kept/discarded/inconclusive, accepted changes, stopping reason, record location, and remaining verification limits. State the next promising hypothesis if one remains. Distinguish an observed improvement from proof that no better solution exists.
