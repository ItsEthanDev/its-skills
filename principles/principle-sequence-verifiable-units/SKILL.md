---
name: principle-sequence-verifiable-units
description: "Apply when judging multi-step work and delivery granularity. Favor coherent units that localize failure and make verification evidence understandable."
disable-model-invocation: true
---

# Sequence Work into Verifiable Units

A failure is easier to explain when the unit that caused it is identifiable. Favor units that produce a coherent, observable change instead of batches whose effects cannot be distinguished.

- Choose granularity that gives useful evidence without repeating expensive checks unnecessarily. A unit can be several related edits when together they establish one meaningful result.
- Prefer checks that distinguish the affected behavior from its prior state. Broader verification adds value when narrower evidence cannot establish the claim.
- Preserve the validity of evidence: later changes may invalidate a passing check, while unchanged relevant behavior need not be checked again merely for ceremony.
- Make delivery understandable through coherent changes and clear evidence. Baseline comparisons, tests, or a subtraction before a reshape can help explain the result without prescribing a commit or PR structure.

Follow project rules for delivery order and acceptance checks. Run an independent review only when explicitly requested or scheduled by an authoritative project artifact.

When judging whether a check establishes its claim, read [Prove It Works](../principle-prove-it-works/SKILL.md). When deciding whether a repeatable tool would improve a check, read [Build the Lever](../principle-build-the-lever/SKILL.md). Keep resulting work within the authorized assignment.
