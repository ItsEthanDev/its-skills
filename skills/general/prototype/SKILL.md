---
name: prototype
description: Build a throwaway prototype to answer a design question. Use when the user needs something concrete to react to, such as an outline, sample lesson, paper mockup, or UI/logic demo.
---

# Prototype

A prototype is **a throwaway artifact or set of artifacts that answers a question**. The question decides the shape.

## Prerequisite: version control

Version control is required for code and non-code prototypes alike. Before creating prototype artifacts, identify the version-controlled location where they will be preserved. If none is available, stop and ask where to preserve the work; do not initialize a repository merely to proceed.

## Pick a branch

Identify and state which question is being answered, using the user's prompt, the surrounding work, or by asking if the user is around:

- **"Does this logic / state model feel right?" (software logic)** → Read [ENGINEERING.md](ENGINEERING.md) and [LOGIC.md](LOGIC.md). Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the state machine through cases that are hard to reason about on paper, and that a non-developer can drive.
- **"What should this look like?" (software UI)** → Read [ENGINEERING.md](ENGINEERING.md) and [UI.md](UI.md). Generate several radically different UI variations on a single route, switchable via a URL search param and a floating bottom bar.
- **A non-code question about content, structure, or a workflow** → Make the smallest concrete example the user can judge: an outline, a sample lesson, a draft ticket, or a paper mockup. Include enough detail to expose the choice, not a finished deliverable or a learner activity by default. No code or runnable demo is required. A workflow or state model does not require the engineering branch merely because it has states or transitions; choose the artifact that exposes the question.

These branches produce very different artifacts, so getting this wrong wastes the whole prototype. If the question is genuinely ambiguous and the user isn't reachable, default to whichever branch better matches the surrounding work and state the assumption at the top of the prototype.

## Rules that apply to all branches

1. **Throwaway from day one, and clearly marked as such.** Locate the prototype close to where it will actually be used so context is obvious, but name it so a casual reader can see it's a prototype, not a finished deliverable.
2. **Trivial to inspect.** Whether it's one file or several, no thinking required to open it.
3. **Skip the polish.** Include only what the user needs to judge the question. The point is to learn something fast.
4. **Surface the state.** When the question involves behavior or a workflow, make the relevant state and changes visible so the user can see what each action does.
5. **State the question.** Before handing it over, record the question, necessary assumptions, and a context pointer to the prototype in the relevant issue. Follow the caller's recording convention, including wayfinder's asset link when working a prototype decision ticket. Without an issue tracker, use a project record or put the context alongside the prototype. A few lines are enough; add instructions for inspecting it only when they aren't obvious.
6. **Hand it over.** Show the prototype and ask the user to react to the stated question. Adjust it when their feedback exposes a missing case or alternative. If the answer is obvious from the question and available evidence, the agent can choose it and record why without waiting for feedback. Otherwise, seek the user's judgment. Follow any caller requirement for human confirmation, including wayfinder's HITL tickets; an agent decision is not user approval. If work pauses with the decision still open, preserve the prototype and mark that status in the same record.
7. **Capture it when done.** Once the prototype has answered its question, capture the prototype itself as a **primary source**: commit it to a throwaway branch, out of main, and leave a context pointer to that branch and revision in the same record. This applies to code and non-code prototypes alike. Follow an explicit project convention instead when it provides equivalent isolation and a durable revision pointer. Capture the answer too (the verdict, why, and the question it settled) in the same record. Preservation does not require ongoing upkeep or keeping the prototype in sync with finished work. Applying the decision to finished work requires that work to be in scope. A local commit satisfies capture; publishing or pushing the prototype requires authorization.
