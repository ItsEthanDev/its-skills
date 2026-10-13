---
name: verifying-work
description: "Prove changed behavior or artifacts before claiming completion. Use when finishing work, checking a delivered result, establishing a feedback loop, or creating or maintaining project-specific verification guidance."
---

# Verifying Work

Before claiming work is complete, prove that it meets the request. A claim is only as strong as the observation that distinguishes it from a plausible mistake. Inspect the actual artifact or behavior, including delegated work; a task list or an agent's summary is not evidence.

Follow the branch requested by the caller:

- **Verify a result:** follow the procedure below.
- **Establish a feedback loop:** follow steps 1–4 and [Feedback loops](FEEDBACK-LOOPS.md), then return the demonstrated signal and its limits. Establishing a loop does not authorize repairing the product.
- **Create or maintain project verification guidance:** read [Project verification](PROJECT-VERIFICATION.md). A missing project skill does not block verification when existing commands suffice.

## 1. Establish the claims

Read the request, applicable requirements, affected artifacts, and project instructions. Identify the material behaviors or facts to establish, relevant failure cases, and the expected observation for each. Ground expectations in requirements, contracts, or independently worked examples rather than derive them solely from the implementation being checked.

Match evidence to the claim. Compilation establishes a build result, not working behavior. UI claims require inspecting the rendered result and relevant interactions. Integration claims require evidence across the actual communication seam. Documentation claims may need source, link, and example checks rather than software execution. Performance claims need a relevant baseline and comparable measurements. Verify distributed artifacts through their consumption path when the claim concerns packaging or installation.

## 2. Find the verification path

Use explicit user direction, suitable project verification skills, documented commands, and existing harnesses before inventing tools. Call the project's verification skill when its applicable procedure is needed. Load only the relevant branches.

When selecting software test surfaces or adapters, call the Skill tool with "codebase-design" and read its `DEEPENING.md` resource for dependency categories and testing strategy. The module's interface is the test surface: assert observable outcomes, not internal call structure. Test adapters can establish the module's logic but do not prove the real transport or external integration works. In a deepening refactor, replace shallow tests only after the new interface tests preserve their distinct behavior coverage; a rewrite is not permission to discard coverage.

For new or changed maintained tests, call the Skill tool with "tdd" for test quality, agreed seams, and dependency substitution. Consult that guidance without starting test-first development unless the assignment requires it. Reuse existing seam approval; running existing checks or temporary observations needs no new seam-approval pause.

Select checks that can catch plausible mistakes in the affected result. For a fix, include the original reported scenario; for a refactor, establish a baseline for preserved behavior before editing and compare afterward. State what narrower checks cannot establish.

## 3. Establish a tight feedback loop

Read [Feedback loops](FEEDBACK-LOOPS.md) when a trustworthy signal is missing, weak, flaky, or expensive. Prefer repeatable, agent-runnable checks that give specific feedback quickly. Existing trustworthy checks need not be replaced or deliberately broken on every task.

Before execution, inspect commands and lifecycle hooks for remote calls and consequential effects. Use authorized environments, isolated fixtures, and known initial state. Establish readiness and the intended build or version. Missing tools, credentials, or permissions are blockers, not permission to install dependencies, drive shared sessions, or widen access.

## 4. Run and interpret

Run the selected checks and capture the invocation or action, observed result, and relevant side effects. Redact secrets and unnecessary private data; use bounded waits. After a surprising failure, check the instance and harness before attributing it to product behavior.

Distinguish a product failure, invalid check, unavailable prerequisite, and ambiguous expected behavior. Correct an invalid check only within the authorized edit scope and with expectations still grounded in their source. Preserve expected results: never weaken assertions, refresh baselines, or redefine requirements merely to obtain a pass.

For authorized implementation, correct in-scope findings and repeat affected checks and relevant regression checks. Otherwise return the finding to the caller. Stop retries that yield no new evidence. Clean up resources created by successful and failed runs, while preserving unrelated processes and evidence still needed to interpret the result.

## 5. Report evidence and limits

Mark material claims **passed**, **failed**, **blocked**, or **unverified**. Include the relevant command or action, observed result or evidence location, coverage limits, and cleanup status. A stale observation, inconclusive result, or check on the wrong surface is not a pass. Limit completion claims to what the evidence establishes; an unavailable check remains unverified.

Use project conventions for temporary evidence. A permanent harness or committed report is not required for every task. When recurring project-specific procedures justify a reusable skill, use [Project verification](PROJECT-VERIFICATION.md) within the authorized edit scope; otherwise report the proposed addition. Return findings and control to the caller rather than initiating diagnosis, independent review, deployment, or a broader workflow.
