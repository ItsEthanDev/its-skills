# Authoring ItsSkills Bundled Scripts

Use this guidance when adding or changing a script distributed with ItsSkills. Follow the [Nix-backed script specification](spec.md) and the portable [script-writing guidance](../../skills/playbooks/authoring-skills/references/scripts.md).

## Supply the execution environment

Declare required tools in repository-owned Nix resources. Follow the selected packaging convention rather than assume a separate flake per skill or a shared environment. Locate bundled resources relative to the script, not the caller's working directory. Keep the entry point usable after either supported installation path.

State the Nix prerequisite in the affected skill's execution instructions. Declare required Nix features and supported platforms. Require NixOS only when the operation actually depends on it.

Pin runtime dependencies through the selected declarations and applicable application locks and hashes. Pinning a runtime does not pin packages it downloads. Package the application with its dependency graph rather than resolving undeclared packages at execution time.

Allow Nix to acquire declared dependencies without installing them into a user profile. If Nix is unavailable, report that prerequisite and fail without trying to install it or change host configuration.

## Check the dependency boundary

Exercise a representative successful invocation with Nix available and additional required tools absent from the host. Check invalid inputs, missing Nix, and unavailable runtime prerequisites.

Run from another working directory and from a relocated bundle to check resource resolution. When installation tooling is available, check that both Nix consumption and skills CLI installation preserve scripts and dependency resources. Report an unavailable installation path as unverified rather than infer preservation from the source tree.

Credentials, input files, ports, permissions, and service access remain runtime prerequisites. Dependency provisioning neither supplies them nor authorizes external effects.
