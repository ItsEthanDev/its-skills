# Distribution

ItsSkills distributes source skill bundles rather than a deployed application.
The supported consumption paths are the skills CLI and a source-only Nix input.
See the [installation instructions](../README.md#installation).

## Source and access

The source repository is `ItsEthanDev/its-skills` on GitHub.
Publishing source changes requires repository write access.
Local consistency checks require no credentials.

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

End-to-end published-source installation verification remains unverified for
both consumption paths. Before claiming a distribution works, exercise each
affected path and inspect the installed bundle for instructions, supporting
resources, provenance, and applicable license files.

## Recovery

A Nix consumer can select a previously known-good source revision in its
configuration and lockfile; the exact update and activation procedure belongs
to that consumer project.

A skills CLI recovery procedure has not been established here.
Neither consumption path's recovery procedure has been exercised during setup.

Publishing, changing tags, or activating consumer configurations requires
separate authorization.
