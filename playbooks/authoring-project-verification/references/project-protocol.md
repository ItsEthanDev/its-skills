# Project Protocol Construction

Write the next agent's executable instructions, grounded in the target project. Use the project's existing documentation and skill format rather than impose a fixed section schema.

## Make the operation discoverable

Name the application and the verification surfaces in the description. State the distinct tasks that should select the skill and its prerequisites. Point to its location from an established project instruction or documentation owner when the assignment permits that update. Do not rely on a private machine path or directory nesting for discovery.

Document the project's concrete evidence standards and special verification decisions that cannot be recovered reliably from a command's help or configuration. For example, identify which test environment is representative or which operation needs a disposable account. Avoid an essay about quality or copied generic test rules.

## Document the actual execution path

Provide enough project-specific detail to run applicable branches:

- **Setup and readiness:** the approved build or launch command, working directory, environment selection, required data or authentication, and the observation that proves this is the intended healthy instance. Include a read-only health check where available.
- **Isolation:** separate ports, data directories, accounts, profiles, or sessions where needed. Identify shared state that must not be driven concurrently. If isolation is unavailable, state the constraint instead of teaching agents to interfere with a user's session.
- **Interaction:** real routes, commands, selectors, or public API operations. Prefer stable accessible handles and project-supported harnesses. State initial conditions and reset steps so an earlier run cannot produce a misleading result.
- **Expected observations:** the visible or returned outcome and required effects, linked to the authoritative requirement or contract. Include relevant failure cases and known prerequisites for inaccessible branches.
- **Evidence:** the action and resulting observation needed to interpret the check, the approved capture location, redaction requirements, and the useful retention period. Use existing project conventions; do not require committed reports for every run.
- **Cleanup:** exact procedures for resources this run creates, including failed attempts. Track process handles instead of killing by name. Respect explicit keep-running instructions and retain evidence for its stated lifetime.

Inspect commands and helpers for real service access and consequential effects. Local execution and names such as `dry-run` do not establish non-mutation. Follow the applicable access rules through [Calling Web APIs](../../../techniques/calling-web-apis/SKILL.md) when a real remote operation is needed. Keep permission-dependent branches explicit; do not embed credentials in instructions.

## Keep executable detail with its owner

Let command help, configuration, and scripts define their arguments, defaults, and implemented checks. Explain when to invoke them and what the agent must decide rather than reproduce their internals in prose. A helper must have a documented entry point, explicit prerequisites, and observable failure. Do not add an invocation of Verifying Work to the generated skill.

## Add feature recipes selectively

For distinct repeated branches, use a small index and one recipe per coherent interaction. Each recipe identifies its user-visible behavior, source of intent, route to the feature, fixture and reset needs, concrete drive instructions, expected observations, and hazards.

Link existing owners of intended behavior instead of maintaining another specification. Do not include every current configuration value or source detail. A map describes the verification paths it covers, not proof that all product behavior has been exercised.

During maintenance, compare the recipe with both accepted intent and live behavior. Correct a drifted selector or command after proving the replacement. When the application violates intent, preserve the expected observation and report the product defect. Never approve a new baseline solely because it matches current output.
