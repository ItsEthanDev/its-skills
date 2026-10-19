---
name: prototype
description: Build a throwaway prototype to answer a design question. Use when the user needs something concrete to react to, such as an outline, sample lesson, paper mockup, or UI/logic demo.
---

# Prototype

A prototype is **a throwaway artifact or set of artifacts built to answer a question**. The question decides the shape.

## Pick a branch

Identify and state which question is being answered, using the user's prompt, the surrounding work, or by asking if the user is around:

- **"Does this logic / state model feel right?"** → Read [ENGINEERING.md](ENGINEERING.md) and [LOGIC.md](LOGIC.md). Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the state machine through cases that are hard to reason about on paper, and that a non-developer can drive.
- **"What should this software UI look like?"** → Read [ENGINEERING.md](ENGINEERING.md) and [UI.md](UI.md). Generate several radically different UI variations on a single route, switchable via a URL search param and a floating bottom bar.
- **A non-code question about content, structure, or a workflow** → Make the smallest concrete example the user can judge: an outline, a sample lesson, a draft ticket, or a paper mockup. Include enough detail to expose the choice, not a finished deliverable or a learner activity by default. No code or runnable demo is required.

These branches produce very different artifacts, so getting this wrong wastes the whole prototype. If the question is genuinely ambiguous and the user isn't reachable, default to whichever branch better matches the surrounding work and state the assumption at the top of the prototype.

## Rules that apply to all branches

1. **Throwaway from day one, and clearly marked as such.** Locate the prototype close to where it will actually be used so context is obvious, but name it so a casual reader can see it's a prototype, not a finished deliverable.
2. **Trivial to inspect.** Whether it's one file or several, no thinking required to open it.
3. **Skip the polish.** Include only what the user needs to judge the question. The point is to learn something fast.
4. **Hand it over.** Show the prototype and ask the user to react to the stated question. Adjust it when their feedback exposes a missing case or alternative. If feedback is pending, the decision is still open; the agent does not supply the user's verdict.
5. **Capture it when done.** Once the user has confirmed the answer, capture the prototype itself as a **primary source**: in a Git project, commit it to a throwaway branch, out of main, and leave a context pointer to that branch on the relevant ticket or project record. This applies to non-code prototypes too. Without Git, preserve the artifacts and link to their location. Capture the answer too (the question, the verdict and why) in the relevant ticket or project record. Follow the caller's recording convention, including wayfinder's asset link when working a prototype decision ticket. Applying the decision to finished work requires that work to be in scope. Publishing or pushing the prototype requires authorization.
