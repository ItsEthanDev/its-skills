# Interface Contracts

Define a contract when another component or consumer needs a stable observable agreement without knowing provider internals. Check service APIs, events, plugin and library interfaces, automation-facing CLIs, and exchanged formats. A human-only CLI may need usage and error documentation without a separate contract artifact.

1. Identify the provider, consumers, and agreement owner. The provider normally owns the authoritative contract; consult affected consumers on consequential changes.
2. Record inputs and outputs, validation, observable behavior and side effects, failures, and compatibility guarantees at the level consumers need. A schema can own exact fields while prose explains retries, idempotency, or other behavior the schema cannot express. Reference the feature spec for intended outcomes rather than duplicating it.
3. Draft a new interface in a feature-local `contracts/` when useful. For a lasting interface shared across features, select one established owner, such as repository-level `contracts/`. Reference it from features rather than creating competing editable copies. Cross-repository consumers pin a version or read-only copy with its source and revision.
4. Verify provider and consumer obligations, including failure cases. Mocks alone do not prove the real provider conforms. Agree and version changes before consumers rely on them; coordinate migration and old-version support where necessary.
5. If implementation reveals a mismatch, reconcile the authoritative contract, affected specs, plans, tests, and consumer versions. Do not silently edit a consumer copy or assume that a changed schema authorizes new product behavior.

The repository's own conventions determine exact formats and paths.
