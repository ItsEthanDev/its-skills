# Feedback Loops

Build a **tight** signal: specific enough to detect the relevant mistake, repeatable enough to trust, and fast enough to guide the next change. Spend disproportionate effort on the signal when it is weak. Reading more code cannot substitute for observing the result.

## Choose the surface

Prefer existing project tools and the smallest check that establishes the claim. Supplement it when the claim crosses another seam.

| Surface | Signal |
| --- | --- |
| Automated test | Exercise the affected public interface with fixtures and assertions on observable outcomes. |
| HTTP interaction | Drive the intended running instance and assert response content and required effects, not just status. |
| CLI or TUI | Invoke the real entry point with fixture input; check exit status, output, and effects. Use a terminal harness when interaction matters. |
| Browser | Drive the relevant interaction and assert DOM, console, or network outcomes; inspect screenshots for visual claims. |
| Captured trace | Replay a redacted request, payload, or event sequence through the relevant code path. |
| Temporary harness | Run the smallest representative subset that still exercises the behavior; disclose substitutions and what they omit. |
| Property or fuzz check | Generate bounded inputs against an independent property; retain seeds and inputs for failures. |
| Bisection | Automate the verdict across known states so `git bisect run` can consume it. |
| Differential check | Compare old/new versions or configurations on identical inputs against the preserved contract. |
| Documentation or configuration | Inspect authoritative sources, resolve references, validate schemas, and exercise relevant examples where safe. |
| Performance | Compare controlled repeated measurements with a relevant baseline; account for warmup, caches, workload, and noise. |
| Human-assisted check | Give precise actions and expected observations; capture the actual answer and its limits. |

When human interaction cannot be automated, adapt [the human-assisted template](scripts/hitl-loop.template.sh) if useful. Run it in a terminal the human can actually interact with, or have them run it and return the captured observations. A prompt printed into an unattended tool session is not human assistance. Capture observations, never credentials.

## Make the check red-capable

Ask: what plausible wrong result would make this check fail? A successful process exit or an assertion that restates the implementation is not enough for a behavior claim.

Demonstrate sensitivity when establishing a new or doubtful check: use a known-bad fixture, a safe isolated mutation, a failing version, or the reported bug. Confirm the failure comes from the relevant assertion, not an unrelated setup error. If mutating a disposable copy, inspect the diff to confirm the mutation landed and restore it afterward. Respect the assignment's edit permissions; report sensitivity as unverified when it cannot safely be demonstrated.

A new feature can use a failing behavioral test; a refactor can use baseline and old/new checks; documentation can use independent source inspection. A diagnosis caller additionally requires an observed failure of the actual reported symptom. Red-capability alone does not establish that the bug was reproduced.

## Tighten the loop

- **Sharper:** assert the exact outcome, including relevant failure states and effects, rather than "didn't crash."
- **More repeatable:** isolate state, pin time and random seeds, control dependencies, and reset between runs.
- **Faster:** narrow inputs and scope, cache safe setup, and skip unrelated initialization without excluding the behavior under test.
- **Agent-runnable:** prefer unattended execution; record any unavoidable human action and the resulting observation.

For intermittent behavior, record attempts and failures under controlled conditions. Use bounded repetition, stress, or scheduling controls in an authorized environment to increase reproduction rate. Compare like-for-like workloads before and after a change; one green run is not proof that a flaky defect disappeared. Report uncertainty rather than promise determinism.

## Completion criterion

Return a command or explicit human-assisted procedure that you have actually exercised, with its expected result, observed output, relevant state, and coverage limits. Explain how it detects the mistake, its repeatability, and whether its speed supports iteration. A signal must measure the target claim; there is no universal seconds-only requirement for expensive integration or performance checks.

If a trustworthy signal cannot be established, report what you tried and the minimum missing prerequisite: environment access, a redacted artifact, a human observation, or permission for instrumentation. Return the blocker to the caller without inventing observations or changing the expected outcome.
