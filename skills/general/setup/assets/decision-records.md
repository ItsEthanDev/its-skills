# Decision records

This guide explains when and how to record consequential project decisions. Read records relevant to the area being changed; surface conflicts with accepted decisions rather than silently overriding them. The [decision-record index](../adr/README.md) links to the records themselves.

## Conventions

- **Location:** <Agreed record location or context-specific locations.>
- **Naming:** <Agreed naming and numbering convention. For sequential numbering, scan the relevant directory for the highest existing number and increment by one.>
- **Acceptance:** <Who approves a decision and how acceptance is recorded.>
- **Status and supersession:** <How later decisions revisit or replace accepted records.>

## During the session

### Offer records sparingly

Only offer to create a decision record when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the record. If a decision is easy to reverse, you'll just reverse it. If it's not surprising, nobody will wonder why. If there was no real alternative, there's nothing to record beyond "we did the obvious thing."

### What qualifies

- **Architectural shape.** "We're using a monorepo." "The write model is event-sourced, the read model is projected into Postgres."
- **Integration patterns between contexts.** "Ordering and Billing communicate via domain events, not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment target. Not every library: just the ones that would take a quarter to swap out.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; other contexts reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We're using manual SQL instead of an ORM because X." Anything where a reasonable reader would assume the opposite. These stop the next engineer from "fixing" something that was deliberate.
- **Constraints not visible in the code.** "We can't use AWS because of compliance requirements." "Response times must be under 200ms because of the partner API contract."
- **Rejected alternatives when the rejection is non-obvious.** If you considered GraphQL and picked REST for subtle reasons, record it; otherwise someone will suggest GraphQL again in six months.

These are engineering examples. For other work, apply the same criteria to its consequential choices; do not invent an architectural decision to use this guide.

## Record format

```markdown
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

That's it. A record can be a single paragraph. The value is in recording _that_ a decision was made and _why_, not in filling out sections.

### Optional sections

Only include these when they add genuine value. Most records won't need them.

- **Status** (`proposed | accepted | deprecated | superseded by <record identifier>`): useful when decisions are revisited
- **Considered Options**: only when the rejected alternatives are worth remembering
- **Consequences**: only when non-obvious downstream effects need to be called out

## Maintenance

Add an index link when a record is accepted. A proposal is not an accepted decision; follow the acceptance process above before presenting it as one. Preserve the history and rationale when a decision is superseded, and reconcile guidance affected by the new decision. Changes to these conventions require <the project's agreed approval process>.

If guidance or a record moves, reconcile its index links and other pointers. Create an individual record only when there is a decision to record; this index can exist before the first one.

Adapted guidance and applicable notices: [Third-party notices](relative-path-to-retained-notices).

<!-- Seed instructions: these criteria and the short format are proposed defaults, not mandatory conventions for every project. Confirm or adapt them to the user's intent and existing practices. Keep only examples relevant to the project, replacing them with concrete domain examples when useful. Resolve location, naming, acceptance, status/supersession, and maintenance placeholders; format examples are intentional instructional syntax. Adapt the link to the actual human-facing record index. The generated project must contain the actual chosen criteria and format, not delegate them to a skill. Remove this comment before writing. -->
