---
name: show-me
description: Show work for feedback in chat, a live Hunk diff, a browser-based Markdown viewer, or UI screenshots. Use when asked to present work, walk through it, or capture a UI for visual feedback.
---

# Show Me

Use the surface the user requests. If none is specified, show the work in chat, or ask when chat would not be useful. Confirm that the chosen surface displays the requested work and give the user its location.

- **Chat:** Summarize the work with relevant paths or links.
- **Hunk:** For an interactive diff, read [Hunk](references/hunk.md) and guide the live session.
- **Browser:** For a directory of Markdown files, read [mdts](references/mdts.md) and serve the requested files.
- **UI capture:** For screenshots of a requested screen or state, read [UI capture](references/ui-capture.md) and deliver inspected images.

If the requested surface is not covered here, ask rather than substitute another one. Browser script execution requires Nix; chat and the guidance-only Hunk and UI-capture branches do not. Report missing tools or access rather than install dependencies, escalate permissions, or change configuration implicitly.
