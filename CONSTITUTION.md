# ItsSkills Constitution

This constitution defines the durable constraints for ItsSkills. Project changes must conform to these rules. A change that conflicts with them requires an explicit amendment rather than an exception hidden in implementation.

## Purpose

ItsSkills helps software developers and engineers solve problems through human-directed, agent-executed software engineering. The goal is to increase a developer's problem-solving capacity by reducing implementation effort and cognitive load while preserving engineering judgment, artifact quality, and accountability.

The collection prioritizes its maintainer's agent workflows. General-purpose usefulness is welcome but is not a requirement. Public availability does not create a support commitment.

## Engineering model

Humans retain authority over problem definition, intended behavior, constraints, and consequential tradeoffs. Agents contribute analysis and proposed solutions, and perform implementation, investigation, testing, and documentation within delegated boundaries. Delegation may include bounded engineering judgment, not only execution. Decisions outside that authority or discoveries that materially change the agreed outcome must be surfaced rather than silently adopted.

Specification-driven development makes intent, constraints, and acceptance criteria explicit enough to guide implementation and evaluate results. Documentation must be proportional to the task; a separate specification or fixed sequence of development stages is not required for every change.

Implementation and verification provide feedback into problem definition and solution design. Specifications may evolve as understanding improves, but agents must not silently redefine accepted requirements to fit their implementation.

Delegating implementation does not remove responsibility for artifact quality. Code and documentation must satisfy the agreed behavior and constraints, remain understandable and maintainable for their intended use, and be supported by proportionate verification evidence. A convincing demonstration alone is not sufficient evidence of engineering quality.

Agents must make consequential choices, unresolved uncertainties, and verification limits visible so developers can assess and maintain the result without having to author every line.

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
