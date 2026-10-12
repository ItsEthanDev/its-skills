---
name: principles
description: Apply engineering principles when making consequential implementation, debugging, refactoring, architecture, migration, verification, or review decisions.
---

# Principles

Select the smallest relevant set of principles, read each selected reference in full, and let its guidance affect a concrete decision. Do not load every principle by default or cite one that did not affect the work.

Resolve reference paths relative to the directory containing this file. If a selected reference is missing, report the incomplete `principles` bundle rather than search for an individual principle skill.

Preserve applicable project rules and the caller's authorized boundary.

## Selection

### Core

- **Laziness Protocol:** Refactoring, diff size, abstractions, or signal threading. Read [Laziness Protocol](references/laziness-protocol.md).
- **Foundational Thinking:** Core types, data structures, shared state, or foundational investments. Read [Foundational Thinking](references/foundational-thinking.md).
- **Redesign from First Principles:** Integrating a requirement into an existing design. Read [Redesign from First Principles](references/redesign-from-first-principles.md).
- **Subtract Before You Add:** Removing obsolete structure during additions or refactors. Read [Subtract Before You Add](references/subtract-before-you-add.md).
- **Minimize Reader Load:** Indirection or hidden state makes code hard to understand. Read [Minimize Reader Load](references/minimize-reader-load.md).
- **Outcome-Oriented Execution:** Planned rewrites or migrations with authorized isolation boundaries. Read [Outcome-Oriented Execution](references/outcome-oriented-execution.md).
- **Experience First:** Product, user experience, or feature-scope tradeoffs. Read [Experience First](references/experience-first.md).
- **Exhaust the Design Space:** Novel interactions or architectural choices with multiple plausible answers. Read [Exhaust the Design Space](references/exhaust-the-design-space.md).
- **Build the Lever:** Non-trivial edits, migrations, analyses, or checks that a tool could execute or prove. Read [Build the Lever](references/build-the-lever.md).

### Architecture

- **Design Deep Modules:** Interface depth, seam placement, locality, or testability. Read [Design Deep Modules](references/design-deep-modules.md).
- **Model the Domain:** Stateful logic or repeated shape assumptions. Read [Model the Domain](references/model-the-domain.md).
- **Boundary Discipline:** Validation, error handling, external data, or framework adapters. Read [Boundary Discipline](references/boundary-discipline.md).
- **Type System Discipline:** Types or signatures in a typed language. Read [Type System Discipline](references/type-system-discipline.md).
- **Make Operations Idempotent:** Operations exposed to retries or partial failure. Read [Make Operations Idempotent](references/make-operations-idempotent.md).
- **Migrate Callers Then Delete Legacy APIs:** An internal API replacement without external compatibility obligations. Read [Migrate Callers Then Delete Legacy APIs](references/migrate-callers-then-delete-legacy-apis.md).
- **Separate Before Serializing Shared State:** Concurrent actors may write the same mutable object. Read [Separate Before Serializing Shared State](references/separate-before-serializing-shared-state.md).

### Verification

- **Prove It Works:** Evidence for a result or completion claim. Read [Prove It Works](references/prove-it-works.md).
- **Fix Root Causes:** Causal explanations or proposed defect repairs. Read [Fix Root Causes](references/fix-root-causes.md).
- **Sequence Work into Verifiable Units:** Work granularity affects failure localization or delivery evidence. Read [Sequence Work into Verifiable Units](references/sequence-verifiable-units.md).

### Context and authority

- **Guard the Context Window:** Large payloads or repeated reads threaten useful context. Read [Guard the Context Window](references/guard-the-context-window.md).
- **Never Block on the Human:** Routine work tempts unnecessary confirmation, or a consequential choice needs direction. Read [Never Block on the Human](references/never-block-on-the-human.md).

### Structural learning

- **Encode Lessons in Structure:** Recurring corrections or failure-prevention instructions. Read [Encode Lessons in Structure](references/encode-lessons-in-structure.md).

## Application

Resolve tension according to the actual decision, project constraints, and available evidence. Prefer the smallest sufficient change unless evidence warrants a different design, experiment, or tool.

Use only available and authorized capabilities. If a selected principle reveals broader work or unresolved authority, return that finding to the caller rather than initiate another workflow. When making a completion claim, select the evidence guidance relevant to that claim; do not turn selection into a mandatory verification sequence.
