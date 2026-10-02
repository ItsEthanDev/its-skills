# ItsSkills Constitution

This constitution defines the durable constraints for ItsSkills. Project changes must conform to these rules. A change that conflicts with them requires an explicit amendment rather than an exception hidden in implementation.

## Purpose

The collection prioritizes its maintainer's agent workflows. General-purpose usefulness is welcome but is not a requirement. Public availability does not create a support commitment.

## Distribution

Skills must be easy to include through Nix configuration and easy to install through Vercel's skills CLI. Both installation paths must consume the same skill sources, without separately maintained copies.

Changes to packaging or discovery must be verified against both installation paths. Neither path may become an incidental or unsupported alternative.

## Independence

Skills must not depend on a particular consumer repository or machine configuration. Required tools and environment assumptions must be explicit rather than inherited from the maintainer's setup.

## Scope

The repository owns skills and only the documentation and tooling needed to maintain and distribute them. It is not a general collection of agent configurations, prompts, or unrelated utilities.

## Evolution

The collection favors experimentation. Skills, names, behavior, and installation interfaces may change without backward compatibility guarantees.

Change does not remove the requirement that both installation paths remain functional and easy to use.

## License

The collection uses the MIT license. Contributions must be distributable under that license.
