---
name: diagramming
description: Select and create clear diagrams for structure, relationships, interactions, decisions, and state transitions while specifying, planning, documenting, or explaining information.
---

# Diagramming

Consider a diagram when information depends on relationships, boundaries, order, or transitions, including while deriving a specification from accepted conversation context. Do not wait for an explicit request for a diagram. Prefer prose, a table, or a concrete example when that communicates the information more clearly.

## Select the representation

1. Identify the reader, the point to communicate, and the authoritative information. Establish whether the result describes observed behavior, an accepted target, or a proposal. Keep unresolved choices visible rather than inventing connections or requirements.
2. Choose a representation that makes the important relationships easy to follow:
   - Boundaries, dependencies, and ownership: a context or component diagram.
   - Interactions and ordering between participants: a sequence diagram.
   - States and permitted transitions: a state diagram.
   - Decisions and branching paths: a flowchart.
   - Data relationships and cardinality: an entity relationship diagram.
   Use a table for independent attributes or comparisons and prose for a simple linear explanation. Do not add a diagram merely to inventory components.
3. Follow the user's requested format, then established project and destination conventions. Use Mermaid as the fallback when neither selects a format and the destination supports it. If the destination cannot display the chosen format, provide a compatible representation. If rendering support is unknown, keep readable source and explanatory prose and report rendering as unverified.

## Construct and check

4. Include only the elements needed to communicate the point. Keep one abstraction level per diagram; separate a system overview from detailed internals. Split distinct concerns instead of shrinking a crowded diagram into unreadable text.
5. Use the same names as the surrounding artifact and its sources. Label meaningful connections and make their direction and meaning explicit. Show branches, conditions, loops, cardinality, or asynchronous behavior when omitting them would change the interpretation. Distinguish known relationships from hypotheses; explain nonstandard notation and do not rely on color alone.
6. Compare the diagram with its sources. Check each node, relationship, transition, and ordering claim. Distinguish permitted transitions from required or automatic actions, and label optional paths. For specifications, draw intended behavior from accepted requirements, not current implementation by default. Describe unresolved behavior in notes instead of drawing unsupported participants or events. Do not silently settle an unresolved product question through a diagram.
7. Check syntax and render when existing, authorized tooling is available. Inspect label legibility, clipping, crossing connections, and consistency with the accompanying text; successful parsing alone is not enough. Do not install tooling, send content to an external renderer, or start a viewer without the required authorization. Report unrendered or unchecked aspects directly.
8. Present the diagram with a short explanation of its main point and important constraints it cannot express. In text-only destinations, retain enough prose to understand the result without a rendered image. Persist files only within the assignment and follow the artifact's established location and format; link separate assets from the owning document. When both source and rendered output are maintained, identify the editable source and update the derived output rather than let them disagree.

Finish when the representation communicates the intended point, its claims match their sources, and presentation checks or limits are stated. If a diagram adds no clarity, return the simpler representation instead.
