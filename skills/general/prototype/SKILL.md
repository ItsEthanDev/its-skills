---
name: prototype
description: Build a throwaway artifact to answer a design question. Use when the user needs something concrete to react to, such as an outline, sample lesson, paper mockup, or UI/logic demo.
---

# Prototype

A prototype is a **throwaway artifact that answers a question**. The question decides the shape.

## Pick a branch

Identify which question is being answered, using the user's prompt, the surrounding work, or by asking if the user is around:

- **"Does this logic / state model feel right?"** → Read [ENGINEERING.md](ENGINEERING.md) and [LOGIC.md](LOGIC.md). Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the state machine through cases that are hard to reason about on paper, and that a non-developer can drive.
- **"What should this software UI look like?"** → Read [ENGINEERING.md](ENGINEERING.md) and [UI.md](UI.md). Generate several radically different UI variations on a single route, switchable via a URL search param and a floating bottom bar.
- **A non-code question about content, structure, or a workflow** → Make the smallest concrete example the user can judge: an outline, a sample lesson, a draft ticket, or a paper mockup. Include enough detail to expose the choice, not a finished deliverable. No code or runnable demo is required.

These branches produce very different artifacts, so getting this wrong wastes the whole prototype. If the question is genuinely ambiguous and the user isn't reachable, default to whichever branch better matches the surrounding work and state the assumption at the top of the prototype.

## Rules that apply to all branches

1. **State the question.** Write down the decision the prototype should help make, at the top of the artifact or alongside it. A sample lesson used to decide its structure is a decision aid, not a learner activity by default.
2. **Throwaway from day one, and clearly marked as such.** Keep the artifact near the relevant work and name it so a casual reader can see it's a prototype, not a finished deliverable.
3. **Skip the polish.** Include only what the user needs to judge the question. The point is to learn something fast.
4. **Hand it over.** Show the artifact and ask the user to react to the stated question. Adjust it when their feedback exposes a missing case or alternative. If feedback is pending, the decision is still open; the agent does not supply the user's verdict.
5. **Capture it when done.** Record the question, the verdict and why, and a context pointer to the prototype as a **primary source** in the relevant ticket or project record. Preserve it in a form appropriate to the artifact; a local document is enough when no Git branch is needed. Follow the caller's recording convention, including wayfinder's asset link when working a prototype decision ticket. Applying the decision to finished work is separate from resolving it and requires that work to be in scope. Publishing or pushing the artifact requires authorization.
