---
name: decision-records
description: Record consequential decisions. Use when offering to create an ADR or recording or editing an ADR.
---

# Decision Records

## File structure

Most repos have a single context:

```
/
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `GLOSSARY-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── GLOSSARY-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
└── src/
    ├── ordering/
    │   └── docs/adr/                 ← context-specific decisions
    └── billing/
        └── docs/adr/
```

Create files lazily: only when you have something to write. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).
