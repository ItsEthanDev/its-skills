# Project standards

These standards describe the qualities that guide work on ItsSkills, including
the design and review of its skills and supporting resources. They support
judgment and trade-offs; they are not additional constitutional requirements.

Some standards also guide the artifacts and practices that consuming agents
produce through the skills. Where applicable, embed that behavior in the skill's
instructions rather than repeat the standard by name or require downstream
projects to adopt this document. Each standard's scope is described below.

## Composable skills

Each skill should have a clear purpose and invocation boundary. Shared guidance
should follow the Clear ownership standard: consuming skills reference its
authoritative source rather than duplicate its rules.

This standard governs skill design and relationships between skills, not the
conventions of consuming projects.

**Review question:** Is it clear when this skill applies and which guidance it
owns rather than obtains from another source?

## Deliberate context use

Skills should keep universally needed instructions inline and disclose
branch-specific guidance through pointers that state when to read it.
Descriptions should identify invocation conditions; user-invoked descriptions
should state the task they serve.

This standard governs how skills present and load instructions. Discoverability
addresses how readers find relevant guidance.

**Review question:** Can an agent identify when to invoke the skill and load
the guidance needed for the task without loading unrelated branches?

## Project independence

Projects should remain understandable and maintainable without the skills
that established their conventions.

Generated project documentation preserves both the accepted conventions and
the methods needed to use and maintain them. Updating a skill does not silently
change an existing project's rules; adopting newer guidance is a deliberate
project choice.

Skills that establish or migrate project conventions should direct agents to
leave the necessary usage and maintenance guidance inside the project. This
does not require every skill to generate documentation or make every future
task independent of reusable skills.

**Review question:** Can a contributor use and maintain the resulting
conventions through project documentation alone?

## Skill independence

Skills should be free to evolve without maintaining compatibility with every
project they helped establish.

Existing projects retain their adopted conventions. New skill guidance offers
a starting point for new projects and a deliberate migration option for
existing ones, rather than an obligation to preserve old approaches indefinitely.

This standard governs skill design, not downstream project practices. Its
freedom concerns past project conventions; changes still need to account for
active dependencies between skills and workflows.

**Review question:** Can this skill change without requiring previously
established projects to change with it?

## Current-state clarity

Skills and ongoing documentation should describe the current design directly,
without accumulating explanations of earlier versions.

Write guidance as a coherent current design, not as layers of amendments to
previous designs. Skills that write or update ongoing documentation should
encourage the same clarity in their outputs.

Preserve history in artifacts intended for that purpose, such as decision
records, changelogs, and migration guides. Current-state clarity does not mean
erasing useful historical records.

**Review question:** Does this guidance explain the current design without
requiring knowledge of its predecessors?

## Audience separation

Human-facing artifacts should stand on their own for human readers. Keep
instructions specific to agent behavior in dedicated agent guidance. Keep
shared project procedures and governance in their canonical project documents,
where both humans and agents can use them.

Apply this separation both to artifacts maintained here and to documents that
skills direct consuming agents to produce or edit. Separate content by audience
and purpose, not merely because an agent might follow it.

Link related documents without duplicating their rules. One agent guide can
serve several artifacts; separation does not require a new guide for every file.

**Review question:** Is this passage part of the project's content or shared
procedures, or does it exist specifically to steer an agent?

## Clear ownership

Each convention or method should have one authoritative home. Other documents
should reference that owner rather than maintain competing versions.

Projects own their adopted conventions. Skills own their task boundaries and
prerequisites. For example, a skill determines whether missing tracker details
prevent ticket publication; project guidance determines where those tickets
belong and how the tracker is used.

Apply this ownership boundary when designing skills. Skills that use or maintain
project guidance should also direct agents to find existing owners, make changes
in the appropriate home, and reference guidance rather than create competing
copies.

**Review question:** Is it clear where this guidance belongs and which source
governs when documents disagree?

## Method commitment, convention flexibility

Skills should uphold the methods and safeguards that define their purpose
while accommodating project-owned conventions.

Distinguish essential behavior from supporting arrangements such as document
locations, tracker structure, and naming. Using a skill should not require
adopting unrelated conventions or migrating the project's entire workflow.

This standard governs the skill's own instructions. It is not a principle that
downstream projects must adopt.

**Review question:** Is this requirement essential to the skill's purpose, or
does it unnecessarily impose a particular project arrangement?

## Method preservation

Preserve a skill's established methods, constraints, and deliberate wording
unless changing them is part of the intended outcome.

Renaming, reorganizing, or broadening applicability is not, by itself, a reason
to weaken requirements or paraphrase instructions. Identify substantive
behavior changes and their rationale before treating the revision as equivalent.

This standard governs changes to the skills themselves; it is not a requirement
to pass on to consuming agents.

**Review question:** Which methods, constraints, or wording changed, and what
justifies each departure?

## Discoverability

Important guidance should have a recognizable purpose, a clear home, and a
reliable path for reaching it when needed.

Skills and references need clear invocation or reading conditions. Index project
guidance by purpose, and use conditional pointers to connect relevant work to
its owning guidance rather than require fixed filenames or load every procedure
into every session.

Skills that establish or reorganize project guidance should make their outputs
discoverable to the intended readers. A document's existence provides a
maintenance cue, but does not replace a path to finding it.

**Review question:** Can the intended reader find this guidance when it matters,
without already knowing where it lives?

## Proportionate structure

Structure should serve the work, not complete a prescribed inventory.

Organize skills, references, and workflows around useful needs. Skills should
likewise direct consuming agents to use documents, tickets, and workflow stages
when they support the intended outcome.

Small tasks should have a lightweight path. Early structure is useful when it
gives an anticipated practice a clear home; it need not wait until every detail
is known.

**Review question:** What useful decision, action, or maintenance need does this
structure support?

## Durable context

Accepted decisions, rationale, and unresolved questions should remain usable
beyond the conversation that produced them.

Keep them in the appropriate project records, distinguishing agreed direction
from proposals and open questions. Preserve enough context for a later session
to resume without reconstructing the chat.

Skills supporting work across sessions should guide consuming agents to preserve
that continuity too. This does not require persistent records for every short
interaction.

**Review question:** Could someone continue this work after losing the
conversation, and does the skill support that continuity where relevant?
