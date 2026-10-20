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

Instruction generalization, dependency auditing, and nested-layout consumption
checks are complete under [task-domain organization](https://github.com/ItsEthanDev/its-skills/issues/2).
That prerequisite is satisfied; separate learning-suite design and implementation
criteria still apply. Maintained workflow-dependency presentation remains deferred.

Each distributed bundle must retain its supporting resources and notices.
Follow the [license guidance](../README.md#license) and
[third-party notices](../THIRD-PARTY-NOTICES.md).

## Release workflow

No automated release or deployment workflow is present.
Repository CI checks consistency on pushes and pull requests; it does not publish
a package or activate a consumer configuration.

The repository contains a `v0.1` tag, but a tag-creation policy and release
approval procedure are not documented. Do not infer them from the tag.

A Nix consumer's lockfile selects its source revision. Unpinned consumers may
receive later source changes when reinstalling or updating.

## Verify distribution

Run the [local checks](quickstart.md#verify-a-change) before publication.

Published experimental revision `1ff4cc988f4e2d98469126ea047ac4abec46d9e7`
passed skills CLI discovery of all 27 identifiers, representative installations,
full-bundle comparisons of all 148 files, source-only Nix fetching, and actual Pi
resource discovery. [Installation verification](https://github.com/ItsEthanDev/its-skills/issues/16)
records tool versions, selections, and limits. These checks did not exercise
model behavior, Home Manager activation, or full configuration builds.

The unpinned README examples target main, which did not contain the nested layout
at verification time. Recheck those paths after the merge before claiming they
consume the new layout. Later source changes are not covered by the recorded
revision's results: exercise each affected consumption path and inspect the bundle
for instructions, supporting resources, provenance, and applicable license files.

## Recovery

A Nix consumer can select a previously known-good source revision in its
configuration and lockfile; the exact update and activation procedure belongs
to that consumer project.

A skills CLI recovery procedure has not been established here.
Neither consumption path's recovery procedure has been exercised during setup.

Publishing, changing tags, or activating consumer configurations requires
separate authorization.
