# Project docs

Recommend the four-file baseline below. Preserve useful existing content; use the baseline files as short entry points when equivalent docs already own the procedures.

| File | Purpose |
| --- | --- |
| `README.md` | What the project is, who it is for, and where to go next |
| `docs/quickstart.md` | From a fresh checkout to running locally and verifying a change |
| `docs/deployment.md` | How a change reaches a deployed environment or a distributed release, how to verify it, and how to roll it back |
| `AGENTS.md` | Project-specific agent rules and conditional pointers to the docs |

Keep the docs short, but concrete. The quickstart needs prerequisites, configuration, exact commands, and expected results. Deployment needs the platform, environments, release trigger, required access, verification, and rollback. Ask about missing operational facts; do not invent infrastructure or release procedures. If the project is not deployed, document its release/distribution workflow, or a brief "This project is not deployed or distributed" statement when neither applies.

Document secret names and how to obtain access, never secret values. Mark any unresolved facts explicitly rather than presenting guesses as working instructions.
