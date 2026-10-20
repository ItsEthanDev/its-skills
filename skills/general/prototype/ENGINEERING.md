# Engineering prototypes

Code-specific instructions for the UI and logic branches, in addition to the shared rules in [SKILL.md](SKILL.md).

1. **Trivial to run.** A UI prototype starts from one command in the project's task runner: `pnpm <name>`, `python <path>`, `bun <path>`, etc. A logic demo is a single HTML file the user double-clicks. Either way, no thinking required to start it.
2. **No persistence by default.** State lives in memory. Persistence is the thing the prototype is _checking_, not something it should depend on. If the question explicitly involves a database, hit a scratch DB or a local file with a clear "PROTOTYPE, wipe me" name.
3. **Skip the polish.** No tests, no error handling beyond what makes the prototype _runnable_, no abstractions.
4. **Surface the state.** After every action (logic) or on every variant switch (UI), print or render the full relevant state so the user can see what changed.
