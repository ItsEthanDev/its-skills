---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Before claiming completion, call the Skill tool with "verifying-work" to check the delivered behavior and artifacts and report evidence and limits.

Then call the Skill tool with "code-review" to review the work. After review-driven changes, call "verifying-work" again to rerun affected checks and relevant regression checks.

Commit your verified work to the current branch.
