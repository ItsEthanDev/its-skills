# Deepening

Use these criteria when judging whether related shallow modules would benefit from a deeper interface. The vocabulary in [SKILL.md](SKILL.md) defines module, interface, seam, and adapter.

## Dependency categories

A dependency's behavior and available substitutes affect which interface and test strategy are credible. The category is evidence for a design decision, not an instruction to merge modules automatically.

### In-process

Pure computation or in-memory state can often sit behind one interface without an adapter. Favor that shape when it gathers coherent knowledge and reduces caller complexity; locality and ownership still matter.

### Local-substitutable

A dependency may have a useful local substitute, such as an in-memory filesystem or a database test implementation. Judge whether it preserves the behavior relevant to the claim. Its existence does not prove that production semantics are covered.

### Remote but owned

For an owned service across a network, a port can separate domain behavior from transport. An injected adapter may let tests exercise domain behavior locally. Network, serialization, and remote failure claims still require evidence at those boundaries.

### External service

An injected adapter can make behavior involving a third-party service testable without calling the service for every test. A mock supports claims about the modeled contract, not proof of actual service compatibility or authenticated access.

## Seam discipline

- Prefer a seam that corresponds to real variation, not hypothetical flexibility. Production and test adapters may justify it when their distinction matters.
- Internal seams may remain private to the implementation. Testing is not by itself a reason to expand the public interface.
- Favor the interface that concentrates meaningful behavior without erasing separate ownership or coupling unrelated responsibilities.

## Coverage after deepening

Interface-level tests can replace redundant implementation-coupled tests when they preserve the required coverage. Retain tests that establish distinct claims; do not delete tests merely because the design changed.

Judge tests by the observable behavior they establish. A test that breaks only because internal structure changed may be crossing the wrong seam.

Before restructuring, deleting code or tests, or executing checks, confirm that the action is within the assignment and project rules.
