---
name: authoring-project-verification
description: Create or maintain a project-specific verification skill when requested. Turn project conventions and behavior requirements into executable verification instructions and reusable helpers where needed.
---

# Authoring Project Verification

Confirm the requested project, creation or maintenance task, and permitted edit boundary. A missing verification skill is a finding, not permission to create one. Read [Authoring Skills](../authoring-skills/SKILL.md) for general skill construction and [Verifying Work](../../techniques/verifying-work/SKILL.md) for verification methods and shared test guidance.

## Discover the project protocol

Inspect repository instructions, behavior requirements, contracts, documented run commands, existing tests, dependencies, and skill locations. For maintenance, read the current verification skill and inspect the implementation and requirements affected by the requested change.

Identify the user-facing surfaces, how to launch and drive them, observable expected results, required fixtures or credentials, and how to isolate and clean up execution. Prefer existing project tools. Ask only for consequential missing decisions or facts that cannot be established from project sources. Follow target-project dependency conventions rather than introducing a provisioning system from another repository.

If the application cannot build or start, establish the specific blocker. Repair it only when the assignment permits product changes; otherwise deliver the blocked protocol or partial draft with the missing prerequisite explicit.

## Write or update the skill

Read [Project protocol construction](references/project-protocol.md) before authoring the project-specific instructions. Use the target project's skill location and supported metadata. Select a technique for a bounded verification operation unless the actual work requires another role.

Keep concrete project commands, fixtures, interaction recipes, special hazards, and expected observations in the project skill. Link authoritative behavior sources rather than copy requirements or silently redefine them from current output. Keep shared verification and test-writing rules with their existing owners. Do not add an instruction that invokes Verifying Work back from the generated skill.

Add a feature map only when distinct repeated interaction recipes justify it. State which branches it covers and the observations that establish their claims. Add a helper only when it improves repeatability; use the portable script-writing guidance selected by Authoring Skills and the target project's approved tools.

For maintenance, classify each discrepancy before editing: a stale command, selector, or documented prerequisite is protocol drift; inability to drive otherwise correct behavior is a harness gap; behavior contrary to accepted intent is a product regression. Fix protocol or harness drift within the assignment. Report product regressions without changing expected behavior or repairing product code unless separately authorized.

## Prove the instructions

Follow the authored instructions using only the documented prerequisites and commands. For creation, exercise at least one representative feature through setup, readiness, interaction, evidence capture, and cleanup. For maintenance, re-exercise each changed executable branch and affected helper. Check that required evidence remains accessible for its stated lifetime after cleanup.

Clean up resources from failed iterations before retrying, including scratch state and owned processes. Diagnose an invalid recipe or health check within the edit boundary; do not keep driving an unhealthy instance. Report inaccessible environments or unsafe prerequisites instead of improvising broader access.

Mark unexecuted branches as unverified. A partially exercised skill is a draft with explicit gaps, not proof that every mapped feature works. Report the delivered paths, exercised branches and observations, remaining coverage, blockers, and anything left active or retained. Return the result and control to the caller.
