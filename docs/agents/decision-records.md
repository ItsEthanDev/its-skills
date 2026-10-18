# Decision records

This guide is the index for consequential project decisions and explains how to record new ones. Read records relevant to the area being changed; surface conflicts with accepted decisions rather than silently overriding them.

## Conventions

- **Location:** individual records live in `docs/adr/`. Create that directory only when there is an actual record to write.
- **Naming:** use sequential numbering, `0001-slug.md`, `0002-slug.md`, and so on. Scan the directory for the highest existing number and increment by one.
- **Acceptance:** the user confirms the decision before it is recorded as accepted. An agent's proposal is not an accepted decision.
- **Status and supersession:** mark a proposal as proposed if it needs a draft record. Preserve an accepted record's rationale when it is superseded, and link both records so readers can follow the change.

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

These are engineering examples. The same criteria apply to consequential skill-design and workflow choices in this collection.

## Record format

```markdown
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

That's it. A record can be a single paragraph. The value is in recording *that* a decision was made and *why*, not in filling out sections.

### Optional sections

Only include these when they add genuine value. Most records won't need them.

- **Status** (`proposed | accepted | deprecated | superseded by ADR-NNNN`): useful when decisions are revisited
- **Considered Options**: only when the rejected alternatives are worth remembering
- **Consequences**: only when non-obvious downstream effects need to be called out

## Records

No individual records have been written in `docs/adr/` yet. Existing issue discussions remain in the tracker; this change does not turn them into accepted ADRs or duplicate their answers here.

## Maintenance

Add an index link when a record is accepted. Preserve the history and rationale when a decision is superseded, and reconcile guidance affected by the new decision. Changes to these conventions require explicit user approval. Changes affecting the constitution also follow its amendment rules.

If guidance or a record moves, reconcile its index links and other pointers. This guide remains usable without a decision-record skill or an external template.

Adapted guidance and applicable notices are recorded in [Third-party notices](../../THIRD-PARTY-NOTICES.md#project-guidance).
