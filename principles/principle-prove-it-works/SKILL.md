---
name: principle-prove-it-works
description: "Apply when assessing results or making completion claims. Match evidence to the claim and inspect the real artifact or behavior rather than rely on proxies or self-reports."
disable-model-invocation: true
---

# Prove It Works

A claim is only as strong as the evidence that distinguishes it from a plausible mistake. Inspect the actual artifact or behavior; do not substitute a proxy, a stale observation, or an agent's intention for a result.

Match evidence to the claim:

- Process liveness requires observing the process, not merely a file timestamp.
- A configured value requires inspecting its authoritative value, not a cached representation.
- Compilation supports a build claim, not a claim that the feature works.
- Runtime behavior may require exercising the affected feature path. An integration claim may require evidence across the actual communication boundary.
- A documentation or analysis claim may be supported by source inspection rather than running software.

When a check fails, consider whether the observation method actually measures the claim before concluding that the system is wrong. Delegated work requires evidence from the output artifact or behavior, not only a delegate's summary.

A deterministic check is useful when repeatability increases confidence enough to justify its cost. A new script or retained results artifact is not mandatory for every task. Follow project rules and authorized scope for creating or committing verification resources.

State what was observed, what remains unverified, and what the evidence cannot establish. Missing access or execution authority limits the claim; it does not authorize external actions or a new workflow.
