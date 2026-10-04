---
name: understanding-code
description: Explain how code behaves, trace execution and data flow, and investigate design rationale when answering codebase questions or preparing specifications, plans, reviews, or changes.
---

# Understanding Code

Bound the investigation to the behavior, module, or design decision needed for the current task. Establish the reader's existing knowledge and desired depth from context; ask only when ambiguity would materially change the investigation. Avoid a repository-wide tour unless that is the assignment.

## Investigate

1. Read applicable project instructions and use existing documentation for orientation. Locate actual entry points, callers, implementations, relevant configuration, and tests. Verify documentation claims against current sources rather than treating a directory name or comment as proof of behavior.
2. Follow a concrete input or operation from entry to result. Trace the control flow, data transformations, state ownership, and externally meaningful effects needed to explain it. Include relevant failure paths and conditions; distinguish a possible path from one actually exercised.
3. Resolve indirect behavior through framework registration, dependency injection, configuration, generated code, or dynamic dispatch. Identify what selects the implementation and which conditions change that selection. If resolution depends on unavailable runtime configuration, explain the alternatives and uncertainty instead of choosing one silently.
4. When rationale matters, consult relevant decision records and targeted local Git history. Separate documented reasons from plausible tradeoffs inferred from code. A commit showing when a structure appeared does not establish why it was chosen. Report missing rationale rather than fabricate intent.
5. When runtime observation would resolve a material uncertainty, use [Verifying Work](../verifying-work/SKILL.md) within the assignment's authority. Prefer inspection otherwise. Inspect execution prerequisites and effects before running code; understanding a system does not authorize contacting services, altering data, or changing maintained code.

## Explain

6. Lead with the answer, then give the smallest useful model of the mechanism. Use the traced example to connect important steps, rather than paraphrase every line or list unrelated files. Cite relevant paths and symbols, with line references when useful. Separate source-established behavior, runtime observations, and hypotheses; disclose configuration or execution assumptions.
7. When structure, interactions, or transitions would be clearer visually, use [Diagramming](../diagramming/SKILL.md). Keep diagrams grounded in the same evidence as the explanation.
8. State unresolved questions and evidence limits that affect the answer. Report discovered defect candidates or improvement opportunities separately, without starting unsolicited review, repairs, or redesign. Return the explanation to the caller; write durable documentation only when that is within the assignment.

Stop when the bounded question has a source-backed answer or a specific unresolved dependency, and further exploration would not materially improve it.
