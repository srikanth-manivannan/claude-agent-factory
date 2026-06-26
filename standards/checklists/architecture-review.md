# Architecture Review Checklist

> Reviews a system/software design for soundness. Run **after** the
> [Universal Core](_universal.md). Backs the `architecture-review` workflow.
> Legend: [README.md](README.md).

**Applies to:** designs, ADRs, services, teams · **Min standard:** 0.1.0

## Decision quality
- [ ] 🟠 `[manual]` The decision is recorded as an ADR (what, why, alternatives).
- [ ] 🟡 `[manual]` Trade-offs are documented against weighted criteria.
- [ ] 🟡 `[manual]` Risky/irreversible decisions have a reversibility or migration path.

## Structure & boundaries
- [ ] 🟠 `[manual]` Component boundaries and responsibilities are clear.
- [ ] 🟠 `[manual]` Dependency direction is acyclic and points the right way.
- [ ] 🟡 `[manual]` A diagram (C4 / mermaid) communicates the design.

## Quality attributes
- [ ] 🔴 `[manual]` No single point of failure in the critical path.
- [ ] 🟠 `[manual]` Scalability path identified (stateless where possible).
- [ ] 🟠 `[manual]` Failure modes + graceful degradation considered.
- [ ] 🟠 `[manual]` Data model is intentional; consistency model is stated.
- [ ] 🟡 `[manual]` Cost and operational impact considered.

## Cross-cutting
- [ ] 🟠 `[manual]` Security implications reviewed (→ `security-review`).
- [ ] 🟡 `[manual]` Observability/operability designed in, not bolted on.
