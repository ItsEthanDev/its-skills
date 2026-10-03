---
name: propose-first
description: Propose a solution and pause before implementing when asked to "propose first" or explain a recommended approach before making changes.
---

# Propose First

When asked to propose first, explain a recommended change before implementing it. This is an opt-in pause before implementation, not a pause before investigation or a general approval gate for other requests.

1. Investigate enough to make a useful recommendation. Read, inspect, and run checks as needed under the applicable project and action boundaries. Do not make the proposed change yet.
2. State the problem as understood and recommend a proportionate approach. Explain consequential reasoning, assumptions, and alternatives only when they could change the decision.
3. Make the next step clear: identify what the user needs to tell or decide, what the user needs to do outside the agent's reach, and what the agent can do and verify after approval. Omit categories that do not apply. Do not request secrets in chat. If the result of a user action could change the approach, ask for that observation before settling the proposal.
4. Stop and wait for approval of the bounded approach before implementing. A supplied fact or follow-up question alone is not approval; a clear direction to proceed with the proposed change is. If new information changes the approach, present the revised proposal before implementing it.

Approval of the proposal covers only the described change. Follow existing rules for pushing, deployment, and other external actions. Other skills may supply the investigation method or implementation workflow; this skill owns only the proposal and pause.
