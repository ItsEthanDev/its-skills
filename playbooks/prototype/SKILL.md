---
name: prototype
description: Build a lightweight prototype or experiment to answer a question before production implementation. Use when the user wants to experience an interaction, explore a design, check feasibility, measure behavior, or try an approach in isolation.
---

# Prototype

A prototype is a throwaway instrument for learning, not production code. Optimize for answering the question cheaply, not for producing a shippable implementation.

## Process

1. **Define the question.** State what the experiment should reveal and what observation would answer it. Ask when materially different questions remain plausible. Keep preparation brief; do not start a production implementation plan.
2. **Choose the smallest useful form.** Use a script, benchmark, interactive demo, isolated component, or small app. Prefer a self-contained file or the lightest setup that works. Use the project's framework or dependencies when their behavior matters to the question. Gather references only when they help explore an open design space.
3. **Isolate the work.** Follow the repository's established experiment-location convention; otherwise use `experiment/<question-slug>/` relative to the applicable repository root. Create it only when needed. Keep it outside production imports, routes, and builds. Add a short `README.md` with the question, run command, and known shortcuts. Mark the artifact as experimental.
4. **Build enough to learn.** Skip production polish, abstractions, defensive infrastructure, test suites, and coverage targets. Keep relevant state and output visible. For interactive demos, use domain-language controls and make awkward scenarios easy to exercise and reset. Preserve enough realistic layout, data density, or runtime context to avoid misleading results. When comparison helps, build meaningfully different, labeled alternatives behind one simple switcher or run command; do not manufacture variants for a question that needs only one experiment.
5. **Observe on the matching surface.** Run the artifact. Drive UI interactions and capture screenshots when useful. Inspect output for behavioral questions and measure timing for performance questions. Use a small assertion or repeatable measurement when it is the cheapest reliable evidence for the question, without introducing a production test harness. Complete this step when the observation supports an answer or exposes a specific remaining uncertainty.
6. **Report and stop.** Give the question, artifact path, run command, observations, limitations, alternatives explored, and recommendation. Distinguish demonstrated results from assumptions; an inconclusive result is valid. For experiential questions, present the artifact for user feedback rather than treating successful execution as design acceptance. Say plainly that the code is throwaway. Leave production implementation to separately authorized work.

## Boundaries

- Keep experiments outside routine linting, formatting, type checking, test discovery, coverage, and other project-wide checks. Inspect existing exclusions and recommend narrow exclusions for the experiment directory where needed. Change shared check configuration only within the authorized scope; never weaken checks for production code. Run focused checks only when they help answer the experiment's question.
- Use synthetic data and in-memory state by default. When persistence is the question, use disposable storage isolated from production. Follow applicable permissions for external access or mutations; experimental work does not authorize them.
- Preserve the useful artifact and its findings in the isolated directory, with a pointer from the relevant project record when one exists. No archival branch is required. Do not automatically delete experiments or deploy them.
- Carry accepted learning into the normal development workflow. Do not automatically promote prototype code into production or treat a runnable experiment as a verified production solution.
