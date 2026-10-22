---
name: retro
description: "Conduct a retrospective on an agent session."
disable-model-invocation: true
---

The user has asked for a **retrospective**. You are suggesting improvements to the agent's **environment** to improve future runs.

## Steps

1. Call the Skill tool with `writing` for the writing style guide.

2. Read the primary sources for the session the user specifies. This may mean searching through session logs on this machine. If the user doesn't specify a session, default to the current one.

3. Look for candidates for improvement in these categories. When reviewing software engineering work, also read [ENGINEERING.md](ENGINEERING.md) for automated checks, coding standards, and implementation-versus-review guidance.

- **Navigation**: how easy was it for the agent to find the right files? Are there hidden dependencies between files? Would a **navigation pointer** make it easier? _Use when_ the session took a long time to find a piece of information.
- **Automated checks**: could a repeatable check catch errors the agent made? Read the project's existing checks first, so a check that already exists but sits unwired or silently broken is the finding, not a reinvention. _Use when_ the agent made a mistake a check could have caught.
- **Global AGENTS.md**: are there any steering instructions that should be moved to conditional references or applicable automated checks instead? _Use when_ the AGENTS.md file is particularly large - in the project OR the user's global scope.
- **Tool economy**: did the agent make expensive tool calls that could be streamlined? Is there any custom tooling (CLI's, MCP's) that is particularly token-inefficient? _Use when_ the agent made an expensive tool call.
- **No-ops**: look for instructions in steering files that don't modify the agent's behavior. _Use when_ the steering files are large and unwieldy.
- **Information access**: look for opportunities to increase the agent's access to information. _Use when_ a crucial piece of information was not available to the agent.

4. Present these candidates to the user, in order of severity. Suggesting an improvement does not authorize implementing it.

## Reference

### Files

You may have access to these files in the project:

- `CLAUDE.md`/`AGENTS.md`: these files are pushed to the context window of any agent working in this project. They should be used incredibly sparingly, usually only for **navigation pointers** to other files.
- Docs: use docs as references files, pointed to by other files. Look for existing docs before writing new ones.
- Skills: use skills for docs (since their description goes into the agent's context window), or for user-invoked commands. Use the `writing` skill and read its `agent-writing.md` reference.
