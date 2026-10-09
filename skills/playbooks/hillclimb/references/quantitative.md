# Quantitative evaluation

## Define a meaningful measurement

Choose measurements tied to the intended outcome and name the direction that counts as better. Define the workload, units, environment, and minimum meaningful improvement. Use the requested thresholds when given. Otherwise, justify a threshold from observed variation and practical value rather than treating every numeric movement as a win.

Check that a proxy still represents the objective. Lower latency obtained by doing less required work is a regression. Fewer lines or dependencies alone do not establish a better design.

## Establish a repeatable comparison

Use an existing suitable harness before introducing another. Inspect what it executes and keep access within the authorized environment. Include representative input sizes, state, and failure cases that can change the result. Confirm that contrasting cases or a controlled perturbation produce distinguishable results before relying on the harness.

Record the actual work completed, errors, and relevant resource costs alongside the primary metric. Run the baseline enough times to estimate variation. Use repeated samples and a suitable summary, such as a median for noisy timings, rather than one favorable run. Keep workload and environment comparable; when order or changing machine conditions may bias the result, interleave baseline and candidate runs.

Record commands, inputs, versions, sample results, and summary method sufficient to reproduce the comparison. Keep these fixed while comparing attempts. If they must change, record the reason and rerun the current best under the revised method.

## Interpret the result

Accept a numeric improvement only when it clears the chosen noise and practical-value thresholds and passes the preserved requirements. Treat unstable, under-sampled, or contradictory measurements as inconclusive. Extend measurement only when it can resolve the uncertainty within the run's budget; otherwise retain the current best.

For several measurements, use the agreed priorities and acceptable regressions rather than inventing a weighted score after seeing results. Evaluate qualities the measurements omit through the qualitative branch.

For example, a batch processor's throughput improvement counts only when it completes the same workload correctly. Report baseline and final throughput, sample variation, errors, and any change in memory use. Do not claim a percentage improvement without naming its baseline and direction.
