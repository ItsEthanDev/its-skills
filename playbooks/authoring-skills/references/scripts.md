# Writing Skill Scripts

Use scripts for repeatable mechanics with explicit inputs and observable results. Leave ambiguous choices and authorization decisions to the agent or user.

## Keep one source of truth

Let the script own its arguments, defaults, validation, execution steps, and implemented verification. Provide usage through its help interface.

In the skill, state when to invoke the script, what authorization or context it needs, and which decisions the agent must resolve before execution. Point to the script and its help instead of reproducing their contents. Do not instruct the agent to repeat checks the script already performs.

## Declare execution prerequisites

Follow the target project's dependency and packaging conventions. State required tools, versions where behavior depends on them, supported platforms, and how to obtain the approved environment. Reuse project dependency declarations and locks rather than add an unrelated provisioning system.

Locate bundled resources relative to the script, not the caller's working directory. Keep the script runnable through the project's supported installation paths and preserve required shared resources. Do not rely on undeclared details of a personal environment.

Report missing tools or unsupported platforms clearly. Installing skill files does not itself supply execution dependencies. Do not install dependencies or change host configuration as automatic recovery; follow the project's authorization rules.

## Separate dependencies from runtime state

Treat credentials, input files, ports, permissions, network connectivity, and authenticated services as runtime conditions. Supplying an executable does not supply those prerequisites or authorize external actions.

Check only prerequisites needed for the requested operation. Require remote-access facilities only when remote access is requested.

Do not broaden network exposure, authenticate services, or change system configuration as automatic recovery. Require authorization for those actions.

## Make execution predictable

Validate inputs before side effects. Quote paths and arguments, preserve argument boundaries, and avoid evaluating caller-provided shell text.

Use safe defaults and explicit inputs for consequential behavior. For a viewer, default to loopback access and serve only the requested directory.

Define success through observable postconditions. Use bounded waits and actionable failures when checking readiness. Return a nonzero exit status on failure, and do not report success merely because a process started.

Make process ownership explicit. Either run in the foreground or return a handle for stopping the process. Clean up resources the script owns on failure; do not stop unrelated processes.

Keep output useful to the caller. Report results clearly and send diagnostics to standard error. Use structured output when a caller needs to parse results reliably.

## Verify the boundary

Check syntax and exercise a representative successful invocation. Test relevant failures, including invalid inputs, missing tools, and unavailable runtime prerequisites.

Verify execution in the declared environment rather than rely on incidental host tools. Run from another working directory and check bundled path resolution. When supported installation paths are available, verify that they preserve required scripts and dependency resources.

Distinguish reproducible dependencies from stateful execution. A declared environment does not guarantee available ports, connectivity, credentials, or permissions. Report checks that could not be performed.
