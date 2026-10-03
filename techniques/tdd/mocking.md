# When to Mock

Choose substitutes according to the approved seam and the behavior the test must establish, not merely whether a dependency is owned by the project.

Prefer real behavior inside the module under test. Do not mock its internal collaborators just to assert implementation choices such as call counts or ordering.

A dependency beyond the selected seam may need a substitute:

- External APIs, such as payment or email services.
- Owned remote services accessed through a defined port.
- Time and randomness when controlled values establish the behavior under test.
- Databases or filesystems when a test instance or substitute preserves the relevant behavior. Prefer a real test instance when its semantics matter to the claim.

An owned remote service can have an in-memory test adapter without turning the test into an assertion about internal implementation. Ownership alone does not determine whether substitution is valid.

## Limits of evidence

A substitute supports only the behavior it models. A mock response does not prove network behavior, serialization, authentication, or compatibility with the actual service. Use the project's required verification for claims at those boundaries, within authorized scope.

If the substitute would erase the behavior being tested, use a different test setup or report the limitation. Do not broaden the selected seam or access external services without the necessary approval.

## Designing for Mockability

### Inject dependencies at the seam

Pass dependencies in rather than creating them inside the behavior under test:

```typescript
// Easy to substitute at the selected seam
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Couples behavior to construction and external configuration
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

### Expose meaningful operations

An operation-specific interface can make the contract and test setup clearer than a generic fetcher with conditional behavior:

```typescript
// Each operation exposes its own input and result contract
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// Tests may need to reconstruct routing logic inside the substitute
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

Choose the interface that fits actual callers and the approved seam. Test convenience alone does not justify a new abstraction or interface redesign.
