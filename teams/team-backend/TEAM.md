---
name: team-backend
description: A coordinated team of agents that designs, builds, and quality-gates backend services.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [team, backend]
---

# Team Backend

> A coordinated team of agents that designs, builds, and quality-gates backend services.

A coordinated collection of agents (skill → agent → **team** / workflow → playbook,
[/standards/architecture.md](../../standards/architecture.md)).

## Charter
Own the backend delivery domain: API design, server-side implementation + persistence,
and the quality gate.

## Agents
- `api-architect` (≥ 0.1.0) — API + system design.
- `backend-engineer` (≥ 0.1.0) — implementation + persistence + tests.
- `qa-engineer` (≥ 0.1.0) — quality gate.

## Coordination
api-architect defines the contract → backend-engineer implements → qa-engineer verifies.
Composed by `play-enterprise-api-delivery`.
