# API Architect (Agent)

> Use this agent to design and review API-centric system architecture before implementation.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does
A reusable role that designs API contracts and reviews the surrounding system design,
composing three architecture/backend skills. Staffs `team-backend` and `team-security`.

## Skills it relies on
- `architecture/system-design-reviewer`, `backend/openapi-designer`, `architecture/tradeoff-analyzer`.

## Customization
Swap `openapi-designer` for a GraphQL/gRPC contract skill as those land.

## Changelog
See [CHANGELOG.md](CHANGELOG.md). Spec: [AGENT.md](AGENT.md).
