# Browser Checks

Use the project's existing browser harness and supported browsers first. If no convention exists, prefer Playwright for browser interaction and assertions when it fits the application and approved tooling. Run unattended or headless when that preserves the behavior being checked; use headed mode when windowing or focus behavior is part of the claim. A recommendation does not authorize installation.

## Exercise the user path

Start the intended build in an authorized local or test environment. Confirm readiness, the expected version, and isolation of accounts, data, ports, and browser profiles. Inspect startup and interaction paths for real service calls before running them.

Drive the affected interaction through stable handles such as accessible roles and names or established test IDs. Avoid coordinates, fixed sleeps, and internal state setters when they bypass the behavior being claimed. Wait for observable readiness or state changes with a timeout.

Assert the relevant visible result and the required effects of the action. A form check may need submission and its resulting state, not merely a screenshot of the initial page. Check relevant navigation, validation, keyboard interaction, or responsive states when they are part of the change. Do not turn every UI task into an exhaustive cross-browser audit.

## Observe and retain useful evidence

Capture enough of the action and resulting state to explain the finding. Inspect relevant console errors and network failures without treating every unrelated warning as a product defect. Screenshots help establish appearance; DOM assertions and interactions establish other behavior. Do not claim visual correctness from DOM assertions alone or interaction correctness from a screenshot alone.

For subjective appearance or an unresolved product choice, provide the concrete observation and return the decision to the caller. Do not silently adopt a new visual target.

Use project-approved evidence locations and redact private data. Close only browser sessions and processes this verification run created and is permitted to stop. Respect explicit keep-open instructions. After an unexpected failure, health-check the instance and reset the page or isolated state before repeating the interaction.
