# Maintenance Review Checklist

> Reviews long-term health of a change (refactors, upgrades, debt paydown). Run
> **after** the [Universal Core](_universal.md). Backs the `refactor-module` and
> `tech-debt-paydown` workflows. Legend: [README.md](README.md).

**Applies to:** maintenance/refactor changes · **Min standard:** 0.1.0

## Scope discipline
- [ ] 🟠 `[manual]` Change is correctly scoped (refactor ≠ behavior change).
- [ ] 🟡 `[manual]` Backwards compatibility preserved (or a MAJOR bump + migration).

## Code health
- [ ] 🟠 `[auto]` Dependencies up to date; no abandoned/unused deps.
- [ ] 🟡 `[manual]` Dead code removed.
- [ ] 🟠 `[manual]` Deprecated APIs migrated, or migration scheduled.
- [ ] 🟡 `[auto]` Lint/format clean.

## Debt & standards
- [ ] 🟠 `[manual]` New tech debt is tracked, not silently added.
- [ ] 🟡 `[manual]` Tests remain meaningful after the change.
- [ ] 🟡 `[manual]` Artifact targets the latest standard (→ `skill-upgrader`).
- [ ] 🟡 `[manual]` Docs updated to reflect the change.
