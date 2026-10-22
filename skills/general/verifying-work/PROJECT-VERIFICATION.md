# Project Verification

Create or maintain a project-level verification skill when explicitly requested or when recurring project-specific setup, interactions, or hazards justify it within the authorized edit scope. A one-off check does not require a new skill. If creation would expand the assignment, propose it and request approval; continue available checks meanwhile.

## Discover the protocol

Inspect project instructions, requirements and contracts, documented commands, tests, manifests, CI, dependencies, and existing skill locations. For maintenance, read the current skill and the affected implementation and requirements.

Identify the surfaces under test, how to launch and drive them, expected observations, credentials or fixtures, isolation, and cleanup. Find facts in project sources before asking for consequential missing decisions. Follow the target project's tools and skill conventions rather than impose this collection's paths or provisioning choices.

If the application cannot build or start, identify the blocker. Repair product code only when authorized; otherwise deliver the protocol as a draft with the missing prerequisite explicit.

## Write executable guidance

Call the Skill tool with "writing" and read its agent-writing and skill-writing guidance. Give the project skill a trigger-rich description naming its verification surfaces, and add a conditional pointer from an established project instruction owner when authorized. A file's presence alone does not ensure discovery.

Keep concrete project procedures in the project skill, and link authoritative behavior sources rather than duplicate requirements. Include the applicable details:

- **Setup and readiness:** working directory, build/start commands, environment, required data or authentication, and observations proving the intended instance is healthy.
- **Isolation and reset:** disposable accounts, ports, directories, profiles, or sessions; initial state and reset instructions; shared-state constraints.
- **Interaction:** actual routes, CLI entry points, stable accessible selectors, or service operations that drive the relevant behavior.
- **Expected observations:** returned or visible results and required effects, including relevant failures, linked to accepted requirements or contracts.
- **Evidence:** actions and observations to capture, safe output locations, redaction, and useful retention lifetime.
- **Cleanup:** resources created by the procedure, including failed attempts; identify owned processes by handles rather than killing by name.

Inspect scripts and hooks for real service effects. Local commands and `--dry-run` labels do not establish safety. Keep access-dependent branches explicit and document secret names or access instructions, never secret values. Add helpers only when repeatability justifies them, with declared prerequisites, an entry point, and observable failure.

Use a small feature index only when distinct repeated recipes justify it. State what each branch covers and misses. Keep arguments and defaults with their authoritative scripts or configuration unless documenting a necessary operational convention.

The generic `verifying-work` skill calls the project skill. Keep the project skill focused on its concrete procedure; do not invoke `verifying-work` back or copy its generic rules.

## Prove and maintain the instructions

Follow the authored procedure using only its documented prerequisites and commands. For creation, exercise at least one representative branch through setup, readiness, interaction, evidence capture, and cleanup. For maintenance, rerun each changed executable branch and affected helper. Clean up failed attempts before retrying, and confirm needed evidence survives cleanup.

Classify discrepancies before editing:

- **Protocol drift:** stale commands, selectors, or prerequisites. Correct and exercise the replacement within scope.
- **Harness gap:** the observation method cannot drive or measure the behavior. Repair only within the authorized edit boundary.
- **Product regression:** behavior contradicts accepted intent. Preserve the expectation and report the defect; repair product code only when authorized.

Mark unexecuted branches as unverified. A partly exercised skill is a draft with explicit gaps, not proof of every mapped feature. Report delivered paths, actual invocations and observations, coverage, blockers, and anything retained or left running. Return control to the caller.
