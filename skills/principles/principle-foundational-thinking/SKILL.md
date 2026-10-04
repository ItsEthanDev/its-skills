---
name: principle-foundational-thinking
description: "Apply when choosing core types, data structures, shared state, or foundations that affect later work. Preserve useful options without introducing speculative infrastructure."
disable-model-invocation: true
---

# Foundational Thinking

Structural decisions protect useful options. Code-level decisions protect simplicity. Over-engineering often closes doors through premature commitments; a suitable data structure makes later behavior simpler.

- Favor data shapes that match real access patterns and invariants. Scattered assumptions in downstream logic are evidence that the foundation needs reconsideration.
- Converge types and domain models rather than abstract every repeated line. A few similar statements can be cheaper than a premature abstraction.
- Prefer foundations whose benefit to the accepted work is concrete. CI, test infrastructure, or shared types may provide leverage, but their existence is not a universal prerequisite for feature work.
- Before sharing mutable state, consider interference between actors. Isolation preserves options when sharing is not an actual invariant.
- Prefer increments that establish or deepen a coherent abstraction rather than spread special-case coordination across callers.
- Remove obsolete structure when doing so simplifies the foundation, within the authorized scope.

Evaluate a foundation by the complexity it removes and the options it preserves, not by how much infrastructure it adds.
