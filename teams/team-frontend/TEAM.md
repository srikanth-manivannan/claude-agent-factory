---
name: team-frontend
description: A coordinated team of agents that builds accessible, tested frontend experiences.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [team, frontend, accessibility]
---

# Team Frontend

> A coordinated team of agents that builds accessible, tested frontend experiences.

A coordinated collection of agents ([/standards/architecture.md](../../standards/architecture.md)).

## Charter
Own the frontend delivery domain: accessible UI components/features + the quality gate.

## Agents
- `frontend-engineer` (≥ 0.1.0) — accessible, tested UI.
- `qa-engineer` (≥ 0.1.0) — quality gate (tests, a11y, docs).

## Coordination
frontend-engineer builds → qa-engineer verifies accessibility + coverage. Composed by
`play-react-enterprise-dev` and `play-accessibility-compliance`.
