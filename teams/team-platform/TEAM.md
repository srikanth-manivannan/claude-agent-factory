---
name: team-platform
description: A coordinated team of agents that builds and secures the delivery platform.
version: 0.1.0
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [team, platform, devops, cloud]
---

# Team Platform

> A coordinated team of agents that builds and secures the delivery platform.

A coordinated collection of agents ([/standards/architecture.md](../../standards/architecture.md)).

## Charter
Own the platform domain: infrastructure, CI/CD, project foundations, and platform security.

## Agents
- `platform-engineer` (≥ 0.1.0) — infra + CI/CD + scaffolding.
- `security-engineer` (≥ 0.1.0) — secure the platform.
- `qa-engineer` (≥ 0.1.0) — quality gate.

## Coordination
platform-engineer provisions + wires CI → security-engineer hardens → qa-engineer
verifies. Composed by `play-aws-serverless-delivery`.
