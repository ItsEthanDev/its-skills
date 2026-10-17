---
name: frontend-design
description: Design frontend pages, components, and interactive prototypes, or reshape an existing UI. Build task-centered layouts with concise copy, familiar icons, and deliberate visual hierarchy.
---

# Frontend Design

Apply this guidance to the frontend work already requested. Preserve the accepted feature scope and interaction behavior; surface consequential product questions rather than inventing answers.

Design around the user's task, not an explanation of the implementation. Use layout, hierarchy, familiar controls, and concise copy to communicate. Add explanation when it helps someone act, decide, or recover.

Follow explicit user direction, then intentional project conventions and accepted decisions, then the defaults here. Look for evidence such as design-system guidance or configured components; incidental styling is not a competing convention. Preserve compatible usability and accessibility guidance when adapting a default.

## Plan the screen

1. Identify the audience, the main task, and the primary action. Read the relevant brief, real content, and existing UI conventions. Ask only when missing information would materially change the product behavior or design.
2. Sort the content into essential information, secondary information needed on demand, and information to omit. Keep what users need to complete the task or understand its outcome. Do not invent sections to fill space.
3. Make a compact design plan before writing UI code. Establish the information order, grouping, primary and secondary actions, spacing, type hierarchy, color roles, and narrow-screen behavior. Sketch a layout when it helps compare alternatives. Reuse suitable project tokens and components. Keep the plan proportional to the change and proceed within existing authority without a routine approval pause.

## Build with restraint

- Make the primary action easy to find. Group related inputs and information through proximity, alignment, and spacing before adding containers or explanatory labels.
- Match typography, palette, density, and imagery to the audience and subject. Extend an existing product's visual language rather than redesigning it for novelty. For a new UI, choose a coherent direction instead of assembling generic cards, badges, gradients, and decorative headings.
- Let important content carry emphasis; keep surrounding elements quiet. Add a border, card, divider, or animation only when it communicates grouping, priority, state, or a useful response to an action.
- Keep useful density. Simplifying a working screen does not mean hiding essential controls or spreading related information across excessive whitespace.
- Cover the interaction's relevant states, including validation, loading, success, failure, and empty results. Show feedback where the user acted. Preserve clear recovery paths and required disclosures.

### Make text earn its place

Use short, specific action labels and the user's vocabulary. Name what an action does, not how the system implements it. Keep the same action name throughout the flow.

Remove introductions that repeat a heading, descriptions of obvious controls, and notices about invisible implementation conveniences. A form that survives refresh usually needs no browser-storage explanation. If persistence affects privacy, retention, or a decision the user must make, explain that consequence rather than the storage mechanism.

Keep secondary guidance near the relevant field or reveal it when needed. Do not hide information users need before acting, replace field labels with placeholders, or remove useful error instructions merely to reduce word count.

### Use icons intentionally

Prefer a familiar icon over text when the surrounding context makes the action clear, such as closing a dialog, returning to the preceding screen, or opening search. Keep a short label when an icon would leave the action or destination ambiguous. Do not decorate every label with an icon.

Use the project's intentional icon set; use Lucide as the fallback when available within the authorized toolchain. Do not introduce a new dependency merely to obtain an icon when a suitable existing option works. Keep icon size, stroke, alignment, and hit areas consistent. Give icon-only controls accessible names, visible keyboard focus, and adequate pointer targets. Hide decorative icons from assistive technology. A tooltip may supplement a control, but must not be its only accessible name or the only way to discover an unfamiliar action.

### Keep prototype commentary out of the UI

Omit preview banners, demo disclaimers, technical notes, and lists of unfinished features unless requested or required by the product's accepted constraints. Describe limitations in the handoff or developer documentation instead.

Do not imply that a simulated action completed a real payment, delivery, or submission. Use interaction-local feedback that matches what actually happened, without adding a global disclaimer by default.

### Prefer these treatments

| Instead of | Prefer |
| --- | --- |
| "Back to company website (opens in a new tab)" | A back arrow when context makes the destination clear, or an arrow with a short destination label. Do not add a new-tab sentence by default. |
| "Form details are stored in browser storage and persist on refresh" | No notice for routine draft persistence; retain an explanation only for a user-relevant consequence. |
| "Preview: This demo does not submit requests yet" | No persistent demo notice. Report the limitation in the handoff and do not claim that a real request was sent. |
| "Please click the button below to save your changes" | "Save changes" on the button. |

## Inspect and simplify

Use `verifying-work` when executing checks. Inspect the rendered UI at desktop and mobile sizes with available, authorized browser tooling. Exercise the primary interaction and relevant failure states. Check hierarchy, spacing, text wrapping, overflow, keyboard navigation, contrast, focus, and reduced-motion behavior when motion is present. Inspect screenshots rather than treating compilation as evidence of visual quality.

Make a subtraction pass after seeing the result:

- Can the user identify the main task and primary action without reading an introductory paragraph?
- Which text, notice, container, or decoration can disappear without losing meaning?
- Would a familiar icon improve scanning without making the action ambiguous?
- Are implementation details or unsolicited prototype commentary still visible?
- Are essential labels, consequences, errors, and recovery instructions still clear?
- Does the narrow layout preserve the task rather than merely shrink the desktop layout?

Correct unnecessary clutter and interaction problems within scope, then inspect the affected result again. Finish when the primary task is clear and usable, every visible explanation serves a user need, and the relevant checks pass or have a specific reported limit. If rendering tools are unavailable, perform supported source checks and report visual and interaction quality as unverified; do not claim the UI was inspected.
