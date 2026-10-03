---
name: calling-web-apis
description: Make real remote web API requests under explicit permission and environment constraints. Use before live HTTP, SDK, CLI, GraphQL, RPC, or integration-test calls, including unauthenticated reads.
---

# Calling Web APIs

Make only the real API operations the user authorizes. This technique owns live-access checks, not integration implementation, diagnosis strategy, or workflow transitions.

Retrieving public documentation and using local mocks or fake servers do not require API-access permission. The rules below apply equally to raw HTTP, SDKs, CLIs, GraphQL, RPC, and integration tests that contact a real service.

## Establish permission and effect

Identify the service, intended account, target environment, operation, and documented effect before calling it. Check the relevant contract and local configuration without exposing credentials.

Ask once per service and environment before real read requests, including unauthenticated or read-only requests. Explicit permission covers related read-only requests during the current session, not other services, environments, unrelated work, or future sessions. Use permission already clearly granted for that scope rather than ask again for each request.

A scoped request may be:

> May I use `$SERVICE_API_KEY` for documented read-only requests to Service X's production API during this session? I will limit requests to this work, minimize returned data, and avoid printing or persisting credentials.

An HTTP verb, SDK method name, or "dry run" label does not prove that an endpoint is non-mutating. Use a read endpoint only when its documentation establishes that effect. If the effect is unclear, stop and resolve it rather than assume a safe read.

Execute a mutation only when the user explicitly authorizes its operation, specific effect, and target environment. Read permission is not mutation permission, and permission to implement mutation code is not permission to run it. Message delivery, job triggers, uploads, token or webhook creation, acknowledgements, and state-changing reads count as mutations regardless of transport syntax.

## Bound the request

Check cost, quota, rate-limit, audit, and sensitive-data implications before execution. Stay within the approved service, account, environment, and purpose. Ask again when the service or environment changes; resolve an unexpected account rather than treat it as interchangeable.

Request the fewest fields, records, pages, and shortest date range that answer the question. Prefer a bounded observation over a broad export. Do not install a client, broaden access, or change authentication configuration as automatic recovery.

Reference credentials through environment variables or the project's approved secret mechanism without printing their values. Do not write credentials or raw sensitive responses into the repository. Redact sensitive values before sharing logs, commands, or results.

## Execute and inspect

Run only the approved operation. Inspect the actual response or execution result, including service errors and any reported account or environment. Stop if it identifies an unexpected account or environment; do not continue related calls until the mismatch is resolved.

If a request fails or times out, do not infer that a mutation had no effect or retry it blindly. Use the documented operation semantics and authorized observation to establish what is known. A failed response does not grant permission for new calls or effects.

## Return the result

Report the operation and environment, useful redacted evidence, and any uncertainty about the result or effect. Distinguish a performed call from a proposed call or a result that could not be verified.

Return results and control to the caller. Permission for this operation does not authorize broader work, an integration workflow, or a stage transition.
