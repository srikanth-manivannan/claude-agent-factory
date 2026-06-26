# Implementation Guidance — System Design Reviewer

> How to apply this skill. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Build order

1. **Restate** the design + goals; if ambiguous, list clarifying questions and pause.
2. **Map the critical path** (the request/data flow that matters most) and its dependencies.
3. **Review per quality attribute** — scalability, reliability, security, cost/operability, data.
4. **Severity-tag** each finding 🔴/🟠/🟡 with a concrete recommendation.
5. **Note strengths**, then give a verdict derived from the highest open severity.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Depth | Quick triage vs deep audit — scope to the critical path |
| Security | Flag at design level; defer depth to `security-audit` |
| Verdict | 🔴 → needs-rework; 🟠 only → approve-with-changes; 🟡 only → approve |

## Pitfalls

- ❌ Vague criticism → ✅ every finding cites a component + a fix.
- ❌ Silently redesigning → ✅ recommend, don't rewrite.
- ❌ Verdict inconsistent with findings → ✅ derive it from severity.

## Hand-off

Findings feed `architecture/adr-author`, `architecture/tradeoff-analyzer` (option choice),
and the `architecture-review` workflow; rework items feed `architecture/migration-planner`.
