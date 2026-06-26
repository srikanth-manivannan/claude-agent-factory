---
name: team-security
description: A coordinated team of agents that drives secure design, review, and hardening.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [team, security, appsec]
---

# Team Security

> A coordinated team of agents that drives secure design, review, and hardening.

A coordinated collection of agents ([/standards/architecture.md](../../standards/architecture.md)).
Defensive/authorized use only.

## Charter
Own the security domain across the lifecycle: threat-aware design, secret hygiene,
secure review, and release gating.

## Agents
- `security-engineer` (≥ 0.1.0) — security posture + hardening.
- `api-architect` (≥ 0.1.0) — secure-by-design API/system review.
- `qa-engineer` (≥ 0.1.0) — verification gate.

## Coordination
api-architect designs with security in mind → security-engineer reviews + hardens →
qa-engineer gates. Composed by `play-secure-software-delivery`.
