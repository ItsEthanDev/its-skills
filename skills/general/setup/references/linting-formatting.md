# Linting and formatting

Configure the actual tools as well as the guidance when this feature is selected. Inspect the project's languages, package manager, lockfiles, current linter and formatter, scripts, ignores, and CI before proposing a toolchain.

## Recommend, don't replace by default

For applicable JavaScript/TypeScript projects, recommend **Oxlint** for linting and **Oxfmt** for formatting. Explain that these are recommendations: the user can keep existing tools or choose others. For other languages, recommend suitable tooling from the project's ecosystem rather than imposing a JavaScript linter.

On a preserve-and-improve run, keep the established toolchain and address agreed gaps. On a migration run, compare rule coverage, plugins, formatting behavior, and current enforcement before proposing replacement. A faster tool is not evidence that every existing check is preserved.

Consult the selected tools' current official documentation before writing version-specific configuration or commands. For Oxlint/Oxfmt, start with the [Oxlint guide](https://oxc.rs/docs/guide/usage/linter.html) and [Oxfmt guide](https://oxc.rs/docs/guide/usage/formatter). Don't turn this skill into a second copy of their configuration reference.

## Propose the concrete change

Show dependencies and versions, configuration and ignores, check/fix commands, and any CI changes. Use the project's package manager, scripts, and existing CI rather than creating a parallel workflow. Check whether existing commands already provide the requested enforcement; prefer wiring an established command over adding a second tool for the same check.

Propose a repository-wide reformat as a separate change. Initial configuration may reveal existing violations; report them and agree how to handle them rather than fixing unrelated files or silently disabling rules. Keep generated files and vendored code out of the proposed scope where appropriate.

Get approval for the concrete plan before installing dependencies or changing configuration. Inspect package lifecycle hooks and command effects before execution; stop if they exceed the authorized scope. Do not activate a remote CI workflow, change branch protection, or push merely to test setup.

## Configure and verify

Apply the approved local dependencies, configuration, task commands, and CI configuration. Run the non-mutating lint and format-check commands on representative project files and inspect their results. Use temporary isolated samples if needed to show that a relevant violation is detected without altering unrelated work.

Distinguish broken configuration from a tool correctly reporting existing violations. Record what passed, what failed, and what was not exercised; local execution does not prove remote CI ran.

Document how to run checks and fixes, when the project requires them, and which configuration files own the rules. Link that guidance from the README and from coding standards or the quickstart when those features exist. The project configuration is authoritative after setup; future contributors need not keep using the tools this skill recommends for new projects.
