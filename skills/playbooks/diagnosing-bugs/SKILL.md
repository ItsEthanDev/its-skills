---
name: diagnosing-bugs
description: Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.
---

# Diagnosing Bugs

A discipline for hard bugs. Skip phases only when explicitly justified.

## Authority and scope

Establish whether the assignment authorizes diagnosis only or also repair. Keep investigation, instrumentation, tests, and changes within that scope and applicable project rules. A debugging request does not by itself authorize new infrastructure, production instrumentation, external access, or broader fixes.

For diagnosis-only work, return the evidenced cause and proposed repair without applying it. Report broader needs to an authorized caller or requester rather than initiate another workflow. Any investigation changes require authorization too; diagnosis-only does not imply permission to modify maintained content.

When exploring the codebase, read `CONTEXT.md` (if it exists) to get a clear mental model of the relevant modules, and check ADRs in the area you're touching.

## Redact

Before showing commands, outputs, or captured artifacts, **redact every secret**: write `<REDACTED>` in its place. Build loops against env vars, so the credential stays in the environment rather than in what you show. Captured artifacts carry auth headers: quote only the lines that carry the signal.

If the redacted output is not enough to diagnose the bug, say so and ask the user.

## Phase 1: Build a feedback loop

If you have a **tight** pass/fail signal for the bug (one that goes red on _this_ bug), you will find the cause; bisection, hypothesis-testing, and instrumentation all just consume it. If you don't have one, no amount of staring at code will save you.

Spend disproportionate effort here. **Be aggressive. Be creative. Refuse to give up.**

### Ways to construct one, in roughly this order

These are possible methods, not guaranteed facilities. Use available, authorized project tools. Report missing prerequisites rather than installing tools or services implicitly.

Use `verifying-work` to execute checks and interpret their evidence. Before writing an initial failing test or a regression test, read its `references/automated-tests.md` resource. When test-first repair applies, use `tdd` for the red-green cadence.

1. **Failing test** at an approved seam that reaches the bug: unit, integration, e2e.
2. **Curl / HTTP script** against a running dev server.
3. **CLI invocation** with a fixture input, diffing stdout against a known-good snapshot.
4. **Headless browser script** (Playwright / Puppeteer) that drives the UI and asserts on DOM/console/network.
5. **Replay a captured trace.** Save a real network request / payload / event log to disk; replay it through the code path in isolation.
6. **Throwaway harness.** Spin up a minimal subset of the system (one service, mocked deps) that exercises the bug code path with a single function call.
7. **Property / fuzz loop.** If the bug is "sometimes wrong output", run 1000 random inputs and look for the failure mode.
8. **Bisection harness.** If the bug appeared between two known states (commit, dataset, version), automate "boot at state X, check, repeat" so you can `git bisect run` it.
9. **Differential loop.** Run the same input through old-version vs new-version (or two configs) and diff outputs.

Build the right feedback loop, and the bug is 90% fixed.

### Tighten the loop

Treat the loop as a product. Once you have _a_ loop, **tighten** it:

- Can I make it faster? (Cache setup, skip unrelated init, narrow the test scope.)
- Can I make the signal sharper? (Assert on the specific symptom, not "didn't crash".)
- Can I make it more deterministic? (Pin time, seed RNG, isolate filesystem, freeze network.)

A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight, a debugging superpower.

### Non-deterministic bugs

The goal is not a clean repro but a **higher reproduction rate**. Loop the trigger 100×, parallelise, add stress, narrow timing windows, inject sleeps. A 50%-flake bug is debuggable; 1% is not, so keep raising the rate until it's debuggable.

### When you genuinely cannot build a loop

Stop and say so explicitly. List what you tried. Ask for the minimum needed to establish the signal: (a) access to the relevant environment, (b) a redacted captured artifact (HAR file, log dump, core dump, screen recording with timestamps), (c) an explicitly described human-assisted check, or (d) permission for temporary production instrumentation. Do not assume that access or instrumentation is authorized. Do **not** proceed to hypothesise without a loop.

### Completion criterion: a tight loop that goes red

Phase 1 is done when the loop is **tight** and **red-capable**: you can name **one command** (a script path, a test invocation, a curl) that you have **already run at least once** (show the invocation and its output, redacted), and that is:

- [ ] **Red-capable**: it drives the actual bug code path and asserts the **user's exact symptom**, so it can go red on this bug and green once fixed. Not "runs without erroring"; it must be able to _catch this specific bug_.
- [ ] **Deterministic**: same verdict every run (flaky bugs: a pinned, high reproduction rate, per above).
- [ ] **Fast**: seconds, not minutes.
- [ ] **Agent-runnable where possible**: prefer unattended execution. If human assistance is necessary, state the exact action, expected observation, and why automation is unavailable. Record the actual observation and its limitations; do not imply that a missing helper script exists.

For a human-assisted loop, replace the command requirement with the explicit check and its observed result, and justify that exception. Preserve a signal that distinguishes this bug from unrelated failure.

If you catch yourself building a theory before this feedback signal exists, **stop and establish a red-capable signal before proceeding.** No red-capable feedback signal, no Phase 2.

## Phase 2: Reproduce + minimise

Run the loop. Watch it go red as the bug appears.

Confirm:

- [ ] The loop produces the failure mode the **user** described, not a different failure that happens to be nearby. Wrong bug = wrong fix.
- [ ] The failure is reproducible across multiple runs (or, for non-deterministic bugs, reproducible at a high enough rate to debug against).
- [ ] You have captured the exact symptom (error message, wrong output, slow timing) so later phases can verify the fix actually addresses it.

### Minimise

Once it's red, shrink the repro to the **smallest scenario that still goes red**. Cut inputs, callers, config, data, and steps **one at a time**, re-running the loop after each cut, and keep only what's load-bearing for the failure.

Why bother: a minimal repro shrinks the hypothesis space in Phase 3 (fewer moving parts left to suspect) and becomes the clean regression test in Phase 5.

Done when **every remaining element is load-bearing**: removing any one of them makes the loop go green.

Do not proceed until you have reproduced **and** minimised.

## Phase 3: Hypothesise

Generate **3–5 ranked hypotheses** before testing any of them. Single-hypothesis generation anchors on the first plausible idea.

Each hypothesis must be **falsifiable**: state the prediction it makes.

> Format: "If <X> is the cause, then <changing Y> will make the bug disappear / <changing Z> will make it worse."

If you cannot state the prediction, the hypothesis is a vibe: discard or sharpen it.

**Show the ranked list to the user before testing.** They often have domain knowledge that re-ranks instantly ("we just deployed a change to #3"), or know hypotheses they've already ruled out. Cheap checkpoint, big time saver. Don't block on it; proceed with your ranking if the user is AFK.

## Phase 4: Instrument

Each probe must map to a specific prediction from Phase 3. **Change one variable at a time.**

Tool preference:

1. **Debugger / REPL inspection** if the env supports it. One breakpoint beats ten logs.
2. **Targeted logs** at the boundaries that distinguish hypotheses.
3. Never "log everything and grep".

**Tag investigation-owned debug logs** with a unique prefix, e.g. `[DEBUG-a4f2]`, when instrumentation is authorized. Track what this investigation introduced so cleanup can distinguish it from existing work. A matching prefix is not permission to remove someone else's instrumentation.

**Perf branch.** For performance regressions, logs are usually wrong. Instead: establish a baseline measurement (timing harness, `performance.now()`, profiler, query plan), then bisect. Measure first, fix second.

## Phase 5: Fix + regression test

Apply a repair only when the assignment authorizes it. Otherwise report the evidenced cause, proposed fix, and test coverage needs, then perform only authorized cleanup.

For an authorized test-first repair, use the `tdd` at an approved seam that reproduces the real bug pattern.

A correct seam is one where the test exercises the **real bug pattern** as it occurs at the call site. If the only available seam is too shallow (single-caller test when the bug needs multiple callers, unit test that can't replicate the chain that triggered the bug), a regression test there gives false confidence.

**If no correct seam exists, that itself is a finding.** Report the limitation and any proposed architectural change. Obtain authorization before redesigning the interface.

When a correct, approved seam exists, use the minimised reproduction as the regression case under the TDD rules. Verify an authorized repair against the original, un-minimised feedback loop as well; passing a narrower test does not prove that the user's scenario is fixed.

## Phase 6: Cleanup

Before reporting completion:

- [ ] For an authorized repair, the original reproduction no longer exhibits the defect and the regression test passes, or the coverage limitation is explicit.
- [ ] For diagnosis-only work, the causal finding, evidence, proposed repair, and remaining uncertainty are explicit. Do not claim that an unapplied repair is verified.
- [ ] Investigation-owned instrumentation is accounted for and removed where cleanup is authorized. Report anything left active or in place and why.
- [ ] Useful reproductions and findings are retained according to project conventions. Remove only authorized temporary artifacts; do not automatically delete experiments or unrelated files.
- [ ] The supported causal explanation and verification limits appear in the result. Include them in a commit or PR message if that artifact is already part of the authorized workflow; neither is required merely to finish diagnosis.

Return the result and control to the caller.
