# Design It Twice

Use these criteria when comparing alternative interfaces. A second design is useful when it challenges a consequential assumption in the first, not when it merely renames the same shape.

Use the module, interface, seam, adapter, and leverage definitions in [SKILL.md](SKILL.md). [DEEPENING.md](DEEPENING.md) describes dependency tradeoffs when those affect the comparison.

## Meaningful alternatives

Different design priorities can reveal hidden costs:

- A smaller interface may increase leverage while making unusual cases harder.
- A more flexible interface may cover more cases while increasing what every caller must learn.
- An interface optimized for the common caller may simplify default use at the cost of explicit exceptional paths.
- Different seam placements may change ownership, dependency substitution, or where verification can observe behavior.

No fixed number of designs, agents, or prototypes establishes a good comparison. Use enough concrete evidence to expose the tradeoff in question.

## Comparison criteria

- **Depth:** How much behavior does each caller gain for the interface knowledge required?
- **Locality:** Where do changes, defects, and verification concentrate?
- **Seam placement:** Does the seam match real variation and ownership?
- **Contract:** Are invariants, ordering, errors, configuration, and performance assumptions understandable?
- **Use:** Do realistic examples make the common and exceptional cases clear?
- **Dependencies:** Does the design preserve the behavior and access constraints that matter?

Favor a design whose tradeoffs fit the actual constraints. A hybrid is useful only when its combined interface remains coherent and its additional cost earns its place.
