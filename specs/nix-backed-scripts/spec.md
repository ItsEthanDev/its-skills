# Nix-Backed Script Execution

## Outcome

Bundled skill scripts use Nix to obtain their required tools instead of relying on those tools being installed on the host. Nix is an explicit execution prerequisite, not a dependency on a particular consumer repository or machine configuration.

This specification defines intended behavior for bundled skill scripts. The [constitution](../../CONSTITUTION.md) governs the collection.

## Requirements

### NS-001: Nix is the script execution prerequisite

Bundled scripts MUST require Nix for execution. Skills that use scripts MUST make this prerequisite clear.

Guidance-only skills MUST remain usable without Nix. Installing skill files through Vercel's skills CLI MUST NOT itself imply that Nix or script dependencies have been installed.

### NS-002: Tools come from Nix

Bundled scripts MUST obtain required tool dependencies through Nix rather than assume host-installed versions are available. A script MUST be usable when Nix is available but its additional required tools are not installed on the host.

For example, a script that needs a JSON processor must obtain it through Nix rather than rely on a host installation.

### NS-003: Dependencies belong to the collection

The repository MUST own the declarations needed to supply script tool dependencies. Execution MUST NOT depend on an undeclared package set, a maintainer-specific configuration, or a particular consumer repository.

Non-tool prerequisites, such as required credentials, input files, or access to an external service, MUST be explicit where applicable. Supplying tools through Nix does not supply those prerequisites or authorize external actions.

### NS-004: Missing Nix fails clearly

When Nix is unavailable, the supported script execution path MUST report that prerequisite clearly and MUST NOT attempt to install Nix automatically.

The failure MUST NOT be presented as a missing script-specific tool when Nix itself is the missing prerequisite.

### NS-005: Installation paths preserve execution resources

Both Nix-based skill consumption and Vercel skills CLI installation MUST preserve the resources needed to execute bundled scripts. Neither installation path may require a separately maintained copy of a script or its dependency declarations.

## Acceptance conditions

- A bundled script can run with Nix available and its additional required tools absent from the host.
- Script dependencies are supplied by repository-owned Nix declarations, without reliance on a particular consumer configuration.
- Missing Nix produces a clear failure without an automatic installation attempt.
- A guidance-only skill can be used without Nix.
- Both installation paths retain the resources required for script execution.
- Required non-tool inputs and access are identified rather than treated as supplied by Nix.

## Outside this feature

This feature does not add scripts, select a Nix packaging mechanism, prescribe per-skill versus shared dependency environments, configure a consumer, or implement either installation path. It does not promise non-Nix script execution or supply credentials and external-service access.
