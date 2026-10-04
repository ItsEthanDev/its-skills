# Inbound Webhooks

Use this reference when implementing or changing an endpoint that receives provider events. Establish the provider's documented delivery contract for the behavior being handled.

## Authenticate before processing

Verify the documented signature or authentication mechanism before trusted business processing. Where signature verification uses raw request bytes, preserve them before parsing or framework transformations. Follow the provider's algorithm and verification rules rather than invent a compatible-looking scheme.

Payload schema validation is separate from sender authentication. Do not trust claimed sender identity or event type merely because its shape is valid. If sender identity cannot be verified, surface the limitation and resolve the intended trust model before treating deliveries as trusted.

After authenticity is established, validate the event fields the handler relies on. Keep untrusted transport data out of trusted application logic.

## Handle delivery semantics

Determine which replay, duplicate, ordering, and retry conditions the provider can produce and which the application must tolerate.

- Apply documented timestamp or replay checks where supported. A valid signature alone does not prove that a delivery is new.
- Make repeated delivery safe when the same event can arrive more than once. Identify the appropriate event identity and durable effect boundary rather than assume one HTTP request equals one event.
- Establish what acknowledgement means: received, queued, or successfully processed. Use documented response and timeout behavior; do not acknowledge completed processing before the required work is secured.
- Treat out-of-order events or delivery gaps according to the relevant contract rather than invent guarantees the provider does not make.

Implement only the semantics needed by the accepted behavior. Resolve consequential persistence or processing choices with the authorized caller or requester.

## Test locally

Use local fixtures or a fake sender to exercise valid, forged, malformed, repeated, and stale deliveries where relevant. Confirm that rejected authentication cannot reach trusted processing and that repeated delivery does not duplicate the intended effect.

Test raw-body handling and acknowledgement failures when they matter to the provider's contract. A local signature fixture does not prove real provider compatibility; report that limit.

Real webhook registration, job triggering, or other provider calls require the Calling Web APIs technique's authorization. Local fixtures do not authorize exposure of an endpoint, authentication changes, external access, or live business effects.
