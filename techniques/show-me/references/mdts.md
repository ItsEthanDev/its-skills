# Browser Markdown Viewer

When mdts is selected, use the bundled helper to browse Markdown in a specified directory.

1. Select the directory the user intends to view. Before remote access, establish which files may be exposed and how the other device will reach the server. An explicit request and known authorized route may settle these inputs; do not ask again merely for ceremony. Do not start or configure Tailscale implicitly.
2. Run `sh <skill-directory>/scripts/browser.sh --help`, then invoke the helper with the selected inputs. Defer to its help for arguments, supported systems, and prerequisites. Report blockers rather than install Nix, change host configuration, or broaden the network bind as automatic recovery.
3. Preserve process ownership. The helper serves in the foreground; use an available, authorized process-management facility to keep that owned process accessible while the user inspects it. Retain its process or session handle. Do not claim it will survive the agent's exit unless the chosen facility establishes that behavior.
4. Confirm the page and a requested file load, then give the user a reachable URL. A start message is not readiness evidence. Use a different available port if needed; do not terminate an existing listener or infer that its page is the requested directory.
5. Keep the server running while the user inspects it. Task completion or a pause is not a closure request. An explicit keep-open instruction remains in force until the user explicitly authorizes closure. Otherwise stop only the owned process when the user indicates they are finished. Report the result; do not stop unrelated viewers.

Keep the helper, adjacent flake and lockfile, and npm package resources together. Dependency license notices remain part of their packages; the collection's license does not replace them.
