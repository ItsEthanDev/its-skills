# Quantitative evaluation

1. **Define the measurement.** Name the metric, improvement direction, workload, units, environment, and minimum meaningful gain. Use requested thresholds; otherwise justify them from observed variation and practical value. Reject misleading proxies, such as lower latency from skipping required work.
2. **Validate the harness.** Prefer an existing suitable harness. Inspect its execution and permissions. Use representative input sizes, state, and failure cases. Confirm contrasting workloads or a controlled perturbation produce distinguishable results.
3. **Measure repeatably.** Sample enough to estimate variation and use a suitable summary, such as median timing. Keep workload and environment comparable; interleave baseline and candidate runs when order could bias results. Record completed work, errors, and relevant resource costs alongside the metric. Preserve commands, inputs, versions, samples, and summary method for reproduction.
4. **Interpret the gain.** Require improvement beyond both noise and practical-value thresholds. Treat unstable, under-sampled, or contradictory results as inconclusive. Extend sampling only when useful within budget. Use agreed priorities for competing metrics, not weights invented after seeing results. Evaluate unmeasured qualities separately.

Report baseline, final value, variation, and relevant costs. Name the baseline and direction for percentage claims. For example, higher throughput counts only when the same workload completes correctly.
