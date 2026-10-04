---
name: verifying-work
description: Check changed behavior and artifacts against requirements, and gather evidence before claiming completion.
---

# Verifying Work

Check the result against the requested behavior and its authoritative sources. Read [Prove It Works](../../principles/principle-prove-it-works/SKILL.md) when deciding whether evidence supports a claim.

## Prepare the checks

1. **Identify the claims.** Read the request, affected artifacts, and applicable requirements. List the material behaviors or facts to establish, including relevant failure cases. Name the expected observation and its source for each claim; do not infer correctness solely from the implementation being checked.
2. **Find the existing verification path.** Follow user direction, then suitable project conventions and existing harnesses. Read the relevant project-local verification technique or concrete recipe when one exists. Use only its applicable branches. Report guidance requiring a broader workflow to the caller. If no suitable recipe exists, use the project's documented commands and available tools; report a recurring protocol gap rather than creating a new skill automatically.
3. **Select proportionate checks.** Choose checks that can reveal plausible mistakes in the affected result. Include the original user interaction when verifying a reported fix, and relevant regression checks. State any consequential coverage limit before relying on narrower evidence. Load only the applicable guidance:
   - Writing or changing automated tests: [Automated tests](references/automated-tests.md).
   - Verifying browser-visible behavior: [Browser checks](references/browser-checks.md).
   - Choosing another surface or a tool when the project has no convention: [Verification methods](references/methods.md).

## Execute and interpret

4. **Prepare safe, known state.** Inspect what each command can execute, including lifecycle hooks and remote calls. Before a real API operation, use [Calling Web APIs](../calling-web-apis/SKILL.md). Prefer isolated fixtures and test instances. Do not drive a user's shared session or modify maintained content without authorization. Identify readiness, expected build or version, and the resources this run will create. Missing prerequisites are a blocker, not permission to install tools or widen access.
5. **Run the selected checks.** Exercise the actual artifact or interaction and capture the action, observed result, and relevant side effects. Record commands or artifact locations sufficient to reproduce the observation. Use bounded waits and redact credentials and unnecessary private data. After a surprising failure, check instance health and return to known state before trying again. Clean up resources created by failed attempts as well as successful ones; preserve evidence still needed by the caller and leave unrelated processes untouched.
6. **Classify each result.** Distinguish failed product behavior, an invalid assertion or harness, unavailable prerequisites, and ambiguous expected behavior. Repair an invalid check only when editing it is authorized and its expected result remains grounded in the authoritative source. Never weaken an assertion, update a baseline, or redefine expected behavior merely to pass. Stop retries when they yield no new evidence and return the precise finding.
7. **Return evidence and limits.** Mark claims as passed, failed, blocked, or unverified. Include the relevant command, observed result or evidence location, coverage limits, and cleanup status. An inconclusive or wrong-surface check is not a pass. Return findings and control to the caller so authorized corrections can be followed by another verification pass.
