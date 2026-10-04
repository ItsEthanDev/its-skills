---
name: principle-build-the-lever
description: "Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Default to building the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The tool is the artifact a reviewer can rerun."
disable-model-invocation: true
---
# Build the Lever

When the work isn't trivial, default to building the tool that does it instead of doing it by hand.

**Why:** Two payoffs. Throughput: a codemod, generator, or script does the work the same way every time and can be rerun. Confidence: the tool is one artifact a reviewer can read and rerun to check the work. Existing checks can verify hand-done changes, but do not necessarily make their execution repeatable. A deterministic script turns "trust me" into "run this".

**Pattern:** Default to building the lever, including for non-trivial one-off work. Reuse or adapt an existing suitable lever rather than duplicate it. Follow explicit user direction or an intentional project workflow that selects another approach; do not infer such an override from incidental practice. Otherwise skip construction only when the task is genuinely trivial, a couple of obvious edits you can see at a glance. Existing verification alone does not automatically replace automation of execution.

- A useful lever reproduces the expected result on a representative unit and is safe to rerun. Compare its output against an independent baseline; no fixed manual-first development sequence is required.
- Codemod or script for edits, generator for repetitive files, a dump-to-sqlite query for analysis, a rerunnable check for verification.
- A deterministic lever beats fan-out. If the tool can process every unit in one pass, run it yourself; don't fan out delegates to hand-apply what a script can do.
- When authorized delegation is available, a shared, read-only execution contract can prevent instructions from drifting across delegates. Its value comes from consistent inputs, verification expectations, and scope limits, not a mandatory new skill for every delegation.
- Make the lever available as a runnable artifact, not merely a promise to automate.
- Preserve a useful lever in the appropriate owner when the work outlives the session. Follow project rules and authorized scope for creating and committing it.


**Balance:** The bar is triviality, not repetition. A one-off still earns a lever when the lever is what makes the work checkable. Per the `principle-laziness-protocol`, build the smallest script that does or proves the job, never a framework.

When deciding how to enforce a recurring correction, read `principle-encode-lessons-in-structure`. When scripting a verification check, read `principle-prove-it-works`.
