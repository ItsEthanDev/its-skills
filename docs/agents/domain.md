# Domain language

Actively build and sharpen the project's domain language as you design. This is the _active_ discipline: challenging terms, inventing edge-case scenarios, and writing the glossary down the moment terms crystallise. Merely reading the glossary for vocabulary is not the whole practice: use this guidance when changing the language, not just consuming it.

## Layout and reading rules

This repository has one domain context. Before exploring a domain area, discussing or changing domain concepts, or proposing a change, read the [root glossary](../../GLOSSARY.md).

Use the glossary's terms consistently in proposals, documentation, and tickets. Don't drift to synonyms the glossary explicitly avoids. If the glossary cannot be found, explain the gap and ask how to proceed rather than inventing terminology.

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

Confirm new or changed definitions with the user before recording them. Preserve established definitions unless the change is agreed, and reconcile affected guidance when terminology changes. Changes to this procedure require explicit user approval; constitutional changes follow the constitution's amendment rules.

Keep this guide, the glossary, and the README documentation index linked when owners move. Follow [decision-record guidance](decision-records.md) for consequential decisions rather than recording them as definitions.

Adapted guidance and applicable notices are recorded in [Third-party notices](../../THIRD-PARTY-NOTICES.md#project-guidance).
