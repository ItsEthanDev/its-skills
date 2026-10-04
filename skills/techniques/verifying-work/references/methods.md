# Selecting Verification Methods

Follow the user's requested tools and suitable project conventions before these defaults. Prefer the smallest check that establishes the claim, supplemented by checks at other boundaries when the claim crosses them.

| Claim | Suitable observation |
| --- | --- |
| Application or library behavior | Existing automated runner through the affected public interface; consider Vitest for a suitable JavaScript or TypeScript project without a convention |
| Browser behavior or appearance | Existing browser harness; consider Playwright when suitable, with interaction assertions and visual inspection as needed |
| CLI or TUI behavior | Invoke the actual entry point with fixtures; inspect exit status, output, and required effects; use a PTY harness when terminal interaction matters |
| Service or integration behavior | Local contract fixtures, test adapters, and boundary checks; live operations only with the required permission |
| Packaging or installation | Build the intended artifact and exercise its actual consumption path, not only the source checkout |
| Documentation or configuration | Compare authoritative sources, check references and schema constraints, and exercise commands or examples where practical and authorized |
| Performance | A relevant baseline and comparable repeated measurements with controlled conditions and an explanation of what limits the result |

Treat this as method selection, not a requirement to run every row. For a numerical performance claim, account for warmup, caches, workload, noise, and changes in environment before attributing an improvement to the code.

An existing runner may require only a focused command. Retain a new script or harness only when repeatability justifies it and the assignment permits creating it. Do not introduce dependencies merely to follow a suggested technology.
