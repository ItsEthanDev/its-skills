---
name: dry-run
description: Preview a small, concrete edit as a diff in chat and wait for approval before changing files.
disable-model-invocation: true
---

# Dry Run

1. **Inspect without changing anything** Read the target, project rules, and existing changes. Identify a small, exact edit. If you cannot, ask for missing information or narrow the scope.
2. **Preview the edit** Put each file path above a fenced diff showing complete changed lines. Omit headers and unnecessary context. Separate existing changes from the proposal and note consequential assumptions or planned checks. Do not apply or save the patch.
3. **Wait for explicit approval** Questions and added context are not approval. If the request changes, update the preview and wait again.
4. **Apply and verify** Recheck the target. If it changed or the edit would materially differ, preview again and seek approval. Otherwise apply only the approved edit, verify it, report results, and follow project commit rules. Approval does not authorize pushing, deploying, or unrelated changes.

Apply this workflow only to the current request, including revisions and approval. Do not require dry runs for later requests unless explicitly asked.
