# Nix-Backed Script Execution

## Outcome

Scripts bundled and distributed by ItsSkills use Nix to obtain their required tools instead of relying on those tools being installed on the host. Nix is an explicit execution prerequisite, not a dependency on a particular consumer repository or machine configuration.

Scripts or skills generated in another project follow that project's dependency conventions. They do not acquire a Nix requirement from the use of an ItsSkills authoring skill. The [constitution](../../CONSTITUTION.md) governs the collection.

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

### NS-006: Repository policy stays local

ItsSkills-specific script dependency guidance MUST remain in repository-local contributor guidance, with [AGENTS.md](../../AGENTS.md) directing authors to it. General skill-authoring instructions MUST describe explicit prerequisites and target-project conventions without imposing Nix.

[Authoring bundled scripts](authoring.md) provides the collection's operational authoring guidance.

## Acceptance conditions

- A bundled script can run with Nix available and its additional required tools absent from the host.
- Script dependencies are supplied by repository-owned Nix declarations, without reliance on a particular consumer configuration.
- Missing Nix produces a clear failure without an automatic installation attempt.
- A guidance-only skill can be used without Nix.
- Both installation paths retain the resources required for script execution.
- Required non-tool inputs and access are identified rather than treated as supplied by Nix.
- A script authored in another project follows that project's conventions without inheriting a Nix prerequisite.
- Nix-specific contributor guidance is discoverable from repository instructions without appearing in the portable authoring skill.

## Outside this feature

Packaging may use per-skill or shared dependency environments if both installation paths preserve the required resources. Consumer configuration, credentials, and external-service permissions remain separate from dependency provisioning. Non-Nix execution of scripts distributed by ItsSkills is not a supported requirement.
