---
name: principles
description: Apply engineering principles when making consequential implementation, debugging, refactoring, architecture, migration, verification, or review decisions.
---

# Principles

Select the smallest relevant set of principles, read each selected skill in full, and let its guidance affect a concrete decision. Do not load every principle by default or cite one that did not affect the work.

Selection does not authorize implementation, delegation, external actions, or broader scope. Preserve applicable project rules and the caller's authorized boundary. Principles constrain judgment; the caller's workflow owns execution and transitions.

## Selection

### Core

- **Laziness Protocol:** Refactoring, diff size, abstractions, or signal threading. Read [Laziness Protocol](../principle-laziness-protocol/SKILL.md).
- **Foundational Thinking:** Core types, data structures, shared state, or foundational investments. Read [Foundational Thinking](../principle-foundational-thinking/SKILL.md).
- **Redesign from First Principles:** Integrating a requirement into an existing design. Read [Redesign from First Principles](../principle-redesign-from-first-principles/SKILL.md).
- **Subtract Before You Add:** Removing obsolete structure during additions or refactors. Read [Subtract Before You Add](../principle-subtract-before-you-add/SKILL.md).
- **Minimize Reader Load:** Indirection or hidden state makes code hard to understand. Read [Minimize Reader Load](../principle-minimize-reader-load/SKILL.md).
- **Outcome-Oriented Execution:** Planned rewrites or migrations with authorized isolation boundaries. Read [Outcome-Oriented Execution](../principle-outcome-oriented-execution/SKILL.md).
- **Experience First:** Product, user experience, or feature-scope tradeoffs. Read [Experience First](../principle-experience-first/SKILL.md).
- **Exhaust the Design Space:** Novel interactions or architectural choices with multiple plausible answers. Read [Exhaust the Design Space](../principle-exhaust-the-design-space/SKILL.md).
- **Build the Lever:** A repeatable tool could improve throughput or evidence. Read [Build the Lever](../principle-build-the-lever/SKILL.md).

### Architecture

- **Design Deep Modules:** Interface depth, seam placement, locality, or testability. Read [Design Deep Modules](../principle-design-deep-modules/SKILL.md).
- **Model the Domain:** Stateful logic or repeated shape assumptions. Read [Model the Domain](../principle-model-the-domain/SKILL.md).
- **Boundary Discipline:** Validation, error handling, external data, or framework adapters. Read [Boundary Discipline](../principle-boundary-discipline/SKILL.md).
- **Type System Discipline:** Types or signatures in a typed language. Read [Type System Discipline](../principle-type-system-discipline/SKILL.md).
- **Make Operations Idempotent:** Operations exposed to retries or partial failure. Read [Make Operations Idempotent](../principle-make-operations-idempotent/SKILL.md).
- **Migrate Callers Then Delete Legacy APIs:** An internal API replacement without external compatibility obligations. Read [Migrate Callers Then Delete Legacy APIs](../principle-migrate-callers-then-delete-legacy-apis/SKILL.md).
- **Separate Before Serializing Shared State:** Concurrent actors may write the same mutable object. Read [Separate Before Serializing Shared State](../principle-separate-before-serializing-shared-state/SKILL.md).

### Verification

- **Prove It Works:** Evidence for a result or completion claim. Read [Prove It Works](../principle-prove-it-works/SKILL.md).
- **Fix Root Causes:** Causal explanations or proposed defect repairs. Read [Fix Root Causes](../principle-fix-root-causes/SKILL.md).
- **Sequence Work into Verifiable Units:** Work granularity affects failure localization or delivery evidence. Read [Sequence Work into Verifiable Units](../principle-sequence-verifiable-units/SKILL.md).

### Context and authority

- **Guard the Context Window:** Large payloads or repeated reads threaten useful context. Read [Guard the Context Window](../principle-guard-the-context-window/SKILL.md).
- **Never Block on the Human:** Routine work tempts unnecessary confirmation, or a consequential choice needs direction. Read [Never Block on the Human](../principle-never-block-on-the-human/SKILL.md).

### Structural learning

- **Encode Lessons in Structure:** Recurring corrections or failure-prevention instructions. Read [Encode Lessons in Structure](../principle-encode-lessons-in-structure/SKILL.md).

## Application

Resolve tension according to the actual decision, project constraints, and available evidence. Prefer the smallest sufficient change unless evidence warrants a different design, experiment, or tool.

Use only available and authorized capabilities. If a selected principle reveals broader work or unresolved authority, return that finding to the caller rather than initiate another workflow. When making a completion claim, select the evidence guidance relevant to that claim; do not turn selection into a mandatory verification sequence.

The leaves retain their explicit-invocation metadata. Its effect depends on harness support; neither directory nesting nor this router guarantees that leaf descriptions are hidden from initial context.
