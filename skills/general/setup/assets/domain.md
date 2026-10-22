# Domain Language

Actively build and sharpen the project's domain language as you design. This is the _active_ discipline: challenging terms, inventing edge-case scenarios, and writing the glossary down the moment terms crystallise. Merely reading the glossary for vocabulary is not the whole practice: use this guidance when changing the language, not just consuming it.

## Before exploring, read these

<Links to the project's glossary, or its glossary map and relevant context glossaries. Use actual project-relative links.>

When your output names a domain concept (in an issue title, a proposal, a hypothesis, or a work product), use the term as defined in the relevant glossary. Don't drift to synonyms the glossary explicitly avoids.

## File structure

<The agreed glossary locations and context relationships. For a single context, one glossary is usually enough. For multiple contexts, link a glossary map that lists each context, its glossary, and how the contexts relate.>

When multiple contexts exist, infer which one the current topic relates to. If unclear, ask.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in the glossary, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with project work

When the user states how something works, check whether the project work agrees. In engineering work, check the code. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?" For other work, compare the claim with the relevant source material or artifacts rather than requiring code.

### Update the glossary inline

When a term is resolved, update its owning glossary right there, following the approval process below. Don't batch these up: capture them as they happen. Distinguish a proposed definition from an accepted one; proposing a term does not settle it.

The glossary should be totally devoid of implementation details. Do not treat it as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

## Definition format

```markdown
**<Confirmed term>**:
<One or two sentences defining what the concept is.>
_Avoid_: <Synonyms the project has agreed not to use; omit if none>
```

- **Be opinionated.** When multiple words exist for the same concept, pick the best one and list the others under `_Avoid_`.
- **Keep definitions tight.** One or two sentences max. Define what it IS, not what it does.
- **Only include terms specific to this project's context.** General programming concepts (timeouts, error types, utility patterns) don't belong even if the project uses them extensively. Before adding a term, ask: is this a concept specific to this context, or a general concept? Only the former belongs.
- **Group terms under subheadings** when natural clusters emerge. If all terms belong to a single cohesive area, a flat list is fine.

## Maintenance and approval

Record a definition when the user agrees to it; do not ask for the same approval again. <Any explicit project-specific additional approval requirement, or: No separate approval is required to record an agreed definition.>

Preserve established definitions unless the change is agreed, and reconcile affected guidance when terminology changes. Changes to this guide follow <the project's agreed approval process for this guidance>.

Keep each accepted term in its owning context glossary. Keep this guide and the documentation index linked when owners move. If decision records are used, follow their separate guidance for consequential decisions rather than recording them as definitions.

Adapted guidance and applicable notices: [Third-party notices](relative-path-to-retained-notices).

<!-- Seed instructions: confirm the active practice, definition format, context layout, and approval process with the user. Replace prose placeholders and supply real project-relative links; the term-format example is intentional instructional syntax. Retain the engineering example only when useful to the project. Remove this comment before writing. -->
