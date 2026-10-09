---
name: hillclimb
description: Improve a selected target through supervised subagent experiments using quantitative or qualitative evidence.
disable-model-invocation: true
---

# Hillclimb

Use fresh subagents for attempts; report a blocker if delegation is unavailable or prohibited. The supervisor owns the objective, evaluation, experiment record, and acceptance decisions. Keep every assignment within the caller's permissions. Do not change accepted requirements or authorize external actions. Follow user direction and intentional project conventions for tools, models, and delivery.

## 1. Frame the run

Read the target and requirements. Define the objective, editable surface, preserved constraints, improvement criteria, representative cases, and regression checks. Resolve missing intent or authority. Use `understanding-code` for execution or architecture investigation and `writing` for prose.

Use quantitative evidence whenever an accessible measurement meaningfully reflects the objective. Before evaluating, read [Quantitative evaluation](references/quantitative.md) for measurements and [Qualitative evaluation](references/qualitative.md) for qualities numbers do not adequately capture. Use both when needed.

Establish a recoverable baseline through `verifying-work`. Confirm the evaluation exposes the weakness and distinguishes improvements from regressions; separate known failures. Fix an inadequate evaluation within authority or report the gap before experimenting.

Follow the requested or project-defined budget; otherwise allow at most five attempts. State the budget and any target before starting. Keep a small experiment record using the project convention or Markdown in the run's scratch location. Record the objective, criteria, cases, baseline, budget, and evidence references without secrets or unrelated private data.

## 2. Delegate one hypothesis

Read the record and choose a specific improvement mechanism by likely benefit, cost, and reversibility. Prefer the smallest coherent experiment. Use `refactoring` for behavior-preserving structural changes. Retry rejected ideas only with new evidence.

Give a fresh attempt subagent the hypothesis, current best artifact, relevant project guidance, edit boundary, constraints, evaluation cases, and execution permissions. Require the candidate or diff, before/after evidence, regression results, costs, and uncertainties. It must not alter evaluation criteria, accept its own work, or commit or publish independently.

Run sequentially by default. For authorized parallel attempts, use the same baseline and isolated worktrees or artifact workspaces within the total attempt budget. Evaluate candidates separately. Test combinations as new hypotheses rather than merging unevaluated changes.

## 3. Compare

Inspect the returned artifact and reproduce acceptance evidence through `verifying-work`, including regression checks. Compare against the current best using fixed criteria and cases, not the attempt's summary. For qualitative work, use a separate evaluator when feasible as described in its reference.

If the evaluation must change, document why and reevaluate both artifacts before deciding. Never weaken criteria to obtain a win.

## 4. Decide and record

Keep supported improvements only when constraints hold and costs are justified. Discard regressions or unsupported changes; retain the current best when inconclusive. Restore only the attempt's changes, preserving unrelated work. Ask for decisions on tradeoffs outside delegated judgment.

Log each hypothesis, change, comparison evidence, regression results, verdict, and reason before continuing. At a plateau, reconsider the mechanism rather than repeat failed attempts.

## 5. Finish

Stop at the target, budget, blocked evidence, or when remaining hypotheses do not justify their cost. Recheck the final artifact, finish or stop this run's subagents, and clean up only its disposable resources while retaining needed evidence.

Report baseline-to-final results, accepted changes, attempt verdict counts, stopping reason, record location, verification limits, and any promising next hypothesis. Report observed improvement, not proof of an optimum.
