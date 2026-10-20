# Distribution

ItsSkills distributes source skill bundles rather than a deployed application.
The supported consumption paths are the skills CLI and a source-only Nix input.
See the [installation instructions](../README.md#installation).

## Source and access

The source repository is `ItsEthanDev/its-skills` on GitHub.
Publishing source changes requires repository write access.
Local consistency checks require no credentials.

Bundles live at `skills/<general|engineering|learning>/<skill>/`. Each skill has
one canonical home. A task-domain directory is not a self-contained installation:
include the general skills required by the selected workflows, using existing CLI
selection options or Nix paths. There is no custom installer or dependency resolver.

Each distributed bundle must retain its supporting resources and notices.
Follow the [license guidance](../README.md#license) and
[third-party notices](../THIRD-PARTY-NOTICES.md).

## Publication

Source changes reaching main become available to later unpinned installations.
Pinned consumers adopt changes by selecting another revision.

There is no automated release workflow. Tags and GitHub releases are optional,
separately authorized publication actions; no versioning scheme is established.

Repository CI checks consistency on pushes and pull requests; it does not publish
a package or activate a consumer configuration.

Before publication:

1. Identify the exact candidate revision, target branch or tag, and remote.
2. Complete the applicable [quickstart checks](quickstart.md#verify-a-change) and review.
3. Verify each consumption path affected by the change.
4. Record the revision, commands, tool versions, results, and verification limits
   in the issue tracker.
5. Obtain explicit authorization for the publication action.

Directory or bundle changes require affected discovery and installation checks.
Nix or Pi discovery changes require corresponding checks. A wording-only change
does not by itself require repeating installation checks.

If a required check cannot run, report the gap before publication. Proceed only
with explicit project-maintainer approval of the documented exception.

Local inspection does not establish current remote contents, branch protection,
or successful remote CI.

## Verify distribution

Run the [local checks](quickstart.md#verify-a-change) before publication.

Exercise each affected consumption path against the candidate revision:

- For skills CLI changes, check discovery and representative installations in an
  isolated location.
- For Nix changes, check source-only fetching of the candidate revision.
- For Pi discovery changes, check actual resource discovery with the candidate
  revision selected in the test configuration.
- Inspect each affected installed or fetched bundle for its instructions,
  supporting resources, provenance, and applicable license files.

Success means the affected skills are discoverable and their bundles are complete.
These checks do not establish model behavior, Home Manager activation, or full
consumer configuration builds.

## Recovery

No project recovery procedure is established.

## Maintenance

Changes to this workflow require explicit project-maintainer approval.
Keep consumption instructions and documentation pointers consistent. Keep
run-specific verification evidence in the issue tracker, not this runbook.
Documentation does not authorize publication, tracker writes, remote configuration
changes, or consumer activation.
