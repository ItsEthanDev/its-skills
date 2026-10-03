# Writing Skill Scripts

Use scripts for repeatable mechanics with explicit inputs and observable results. Leave ambiguous choices and authorization decisions to the agent or user.

## Keep one source of truth

Let the script own its arguments, defaults, validation, execution steps, and implemented verification. Provide usage through its help interface.

In the skill, state when to invoke the script, what authorization or context it needs, and what remains outside its responsibility. Point to the script and its help instead of reproducing their contents. Do not instruct the agent to repeat checks the script already performs.

## Supply tools through Nix

Require Nix for bundled script execution and make that prerequisite explicit. Obtain required tools through repository-owned Nix declarations rather than relying on host-installed versions. Locate required bundled resources relative to the script, not the caller's working directory.

Keep the script runnable after installation through either supported path. Preserve any required shared resources as well as resources inside the skill. Do not depend on a personal configuration or a particular consumer repository. Follow the repository's selected packaging design rather than assume a separate flake per skill or a shared environment.

Declare required Nix features and supported platforms. Do not require NixOS unless the operation actually depends on it. Installing skill files does not install Nix or supply execution dependencies by itself.

Pin runtime dependencies through the selected Nix declarations and applicable application dependency locks and hashes. Pinning a runtime does not pin packages it downloads. Prefer packaging the application with its dependency graph over resolving packages at execution time.

Allow Nix to acquire declared dependencies without installing them into a user profile. If Nix is unavailable, report that prerequisite clearly and fail without trying to install it. Do not change host configuration as automatic recovery.

## Separate dependencies from runtime state

Treat credentials, input files, ports, permissions, network connectivity, and authenticated services as runtime conditions. Supplying an executable does not supply those prerequisites or authorize external actions.

Check only prerequisites needed for the requested operation. Local browser viewing does not require Tailscale. Remote viewing requires an explicitly selected access method.

Do not broaden network exposure, authenticate services, or change system configuration as automatic recovery. Require authorization for those actions.

## Make execution predictable

Validate inputs before side effects. Quote paths and arguments, preserve argument boundaries, and avoid evaluating caller-provided shell text.

Use safe defaults and explicit inputs for consequential behavior. For a viewer, default to loopback access and serve only the requested directory.

Define success through observable postconditions. Use bounded waits and actionable failures when checking readiness. Return a nonzero exit status on failure, and do not report success merely because a process started.

Make process ownership explicit. Either run in the foreground or return a handle for stopping the process. Clean up resources the script owns on failure; do not stop unrelated processes.

Keep output useful to the caller. Report results clearly and send diagnostics to standard error. Use structured output when a caller needs to parse results reliably.

## Verify the boundary

Check syntax and exercise a representative successful invocation. Test relevant failures, including invalid inputs, missing Nix, and unavailable runtime prerequisites.

Verify execution with Nix available and additional required tools absent from the host. Run from another working directory and check bundled path resolution. When installation paths are available, verify that both preserve required scripts and dependency declarations.

Distinguish reproducible dependencies from stateful execution. A declared environment does not guarantee available ports, connectivity, credentials, or permissions. Report checks that could not be performed.
