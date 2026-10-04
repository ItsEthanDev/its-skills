---
name: principles
description: Apply engineering principles when making consequential implementation, debugging, refactoring, architecture, migration, verification, or review decisions.
---

# Principles

Select the smallest relevant set of principles, read each selected skill in full, and let its guidance affect a concrete decision. Do not load every principle by default or cite one that did not affect the work.

Preserve applicable project rules and the caller's authorized boundary.

## Selection

### Core

- **Laziness Protocol:** Refactoring, diff size, abstractions, or signal threading. Read `principle-laziness-protocol`.
- **Foundational Thinking:** Core types, data structures, shared state, or foundational investments. Read `principle-foundational-thinking`.
- **Redesign from First Principles:** Integrating a requirement into an existing design. Read `principle-redesign-from-first-principles`.
- **Subtract Before You Add:** Removing obsolete structure during additions or refactors. Read `principle-subtract-before-you-add`.
- **Minimize Reader Load:** Indirection or hidden state makes code hard to understand. Read `principle-minimize-reader-load`.
- **Outcome-Oriented Execution:** Planned rewrites or migrations with authorized isolation boundaries. Read `principle-outcome-oriented-execution`.
- **Experience First:** Product, user experience, or feature-scope tradeoffs. Read `principle-experience-first`.
- **Exhaust the Design Space:** Novel interactions or architectural choices with multiple plausible answers. Read `principle-exhaust-the-design-space`.
- **Build the Lever:** A repeatable tool could improve throughput or evidence. Read `principle-build-the-lever`.

### Architecture

- **Design Deep Modules:** Interface depth, seam placement, locality, or testability. Read `principle-design-deep-modules`.
- **Model the Domain:** Stateful logic or repeated shape assumptions. Read `principle-model-the-domain`.
- **Boundary Discipline:** Validation, error handling, external data, or framework adapters. Read `principle-boundary-discipline`.
- **Type System Discipline:** Types or signatures in a typed language. Read `principle-type-system-discipline`.
- **Make Operations Idempotent:** Operations exposed to retries or partial failure. Read `principle-make-operations-idempotent`.
- **Migrate Callers Then Delete Legacy APIs:** An internal API replacement without external compatibility obligations. Read `principle-migrate-callers-then-delete-legacy-apis`.
- **Separate Before Serializing Shared State:** Concurrent actors may write the same mutable object. Read `principle-separate-before-serializing-shared-state`.

### Verification

- **Prove It Works:** Evidence for a result or completion claim. Read `principle-prove-it-works`.
- **Fix Root Causes:** Causal explanations or proposed defect repairs. Read `principle-fix-root-causes`.
- **Sequence Work into Verifiable Units:** Work granularity affects failure localization or delivery evidence. Read `principle-sequence-verifiable-units`.

### Context and authority

- **Guard the Context Window:** Large payloads or repeated reads threaten useful context. Read `principle-guard-the-context-window`.
- **Never Block on the Human:** Routine work tempts unnecessary confirmation, or a consequential choice needs direction. Read `principle-never-block-on-the-human`.

### Structural learning

- **Encode Lessons in Structure:** Recurring corrections or failure-prevention instructions. Read `principle-encode-lessons-in-structure`.

## Application

Resolve tension according to the actual decision, project constraints, and available evidence. Prefer the smallest sufficient change unless evidence warrants a different design, experiment, or tool.

Use only available and authorized capabilities. If a selected principle reveals broader work or unresolved authority, return that finding to the caller rather than initiate another workflow. When making a completion claim, select the evidence guidance relevant to that claim; do not turn selection into a mandatory verification sequence.
