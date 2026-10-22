---
name: pause-work
description: Pause work safely and save a resume checkpoint for another agent or after compaction.
disable-model-invocation: true
---

1. **Stop at a safe boundary** Finish the current atomic action or leave it explicitly incomplete. Start no new task work. Stop all child agents background work belonging to the paused task. Report anything still active and why. If a stop fails, report the failure rather than claiming all work has stopped. Do not schedule or launch a continuation. Do not push, deploy, or take other irreversible action merely to make the pause tidy.

2. **Write a handoff document** Write a document summarizing the current conversation so a fresh agent can continue the work. Generally, save to the temporary directory of the user's OS - not the current workspace - unless the user has stated they are pausing for a shutdown/reboot, then save it to a location that survives reboots.

- Include a "suggested skills" section in the document, naming which skills the next agent should call the skill tool for.
- Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.
- Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

3. **Provide a resume prompt** End your chat response with a fenced text block the user can copy into a new agent session. Include the handoff document's absolute path and instruct the agent to read it before resuming. Keep task details in the handoff document rather than repeating them in the prompt.
