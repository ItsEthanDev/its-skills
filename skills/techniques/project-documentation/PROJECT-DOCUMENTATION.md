# Human Documentation and Governance

## Help developers get oriented

Use the root `README.md` as the short entry point when human documentation is useful. State what the project does, the common starting path, and where to find deeper material. Keep the core easy to scan. Put details in linked guides only when they help a reader act or look up facts; do not create documentation merely to fill a standard set of files. Follow established locations, otherwise use `docs/` for longer guides. Link to canonical specifications and implementation instead of repeating their declarations.

## Make setup reproducible

Put a short local start path in the README. Use `docs/setup.md` when prerequisites and steps would obscure orientation. From a clean checkout, an authorized developer should be able to identify required tools and access, find the approved way to obtain access, run verified commands, and check an expected result. Separate local setup from production deployment. Do not record credentials or secret values; report steps that could not be verified instead of presenting them as tested.

## Locate operational dependencies

When helpful, link a concise `docs/operations.md` or the repository's existing owner from the README. Describe separately:

- **Existing deployments:** environment, where to inspect the live service, source of the observed state, and when it was verified. Do not infer that an environment is live from deployment configuration alone.
- **Required external integrations and configuration:** what function depends on them, where authorized developers find or request the configuration, and a safe way to check connectivity or setup when known. Do not infer that an integration is configured merely because code calls it.
- **Repository-owned configuration:** a pointer to the declarations, not a second list of their values.

Keep the guide provider-agnostic in form and document only services actually relevant to that project. If the live state cannot be verified, say so. Do not store secrets or sensitive operational details in tracked prose. Documenting these dependencies does not authorize deploying, modifying external services, or accessing credentials. Reconcile the guide when its verified facts change, without duplicating the operational systems' state as another editable authority.

## Record governance in its owner

Governance owns durable constraints on future work, not a description of every current behavior. Use existing policy owners when present; use `specs/constitution.md` only when the project needs a consolidated owner and has none. Record an actionable rule and how to recognize compliance. Do not infer policy from current code or move a one-feature requirement into governance. If a proposed change conflicts with governance, surface the conflict rather than bypassing it.

Agent-specific operating instructions belong in the applicable `AGENTS.md` or harness equivalent; point to canonical human-facing documentation for shared facts. Verify changed paths, links, and commands at their sources. The optional [governance starter](templates/constitution.md) may help when a consolidated constitution is needed.
