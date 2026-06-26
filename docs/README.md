# Documentation

> Human documentation for the Claude Agent Factory. Foundational specs live at the repo
> root ([VISION](../VISION.md), [ARCHITECTURE](../ARCHITECTURE.md), [FACTORY](../FACTORY.md),
> [TAXONOMY](../TAXONOMY.md), [WORKFLOWS](../WORKFLOWS.md)); the enforceable rules live in
> [/standards/](../standards/). This folder holds release notes, decision records, and guides.

## Release & decisions
- [Release Notes — v0.1.0](RELEASE-NOTES-v0.1.0.md) — the Framework Freeze.
- [ADR 0001 — Framework v0.1.0 Freeze](adr/0001-framework-v0.1.0-freeze.md).

## Start here
- [Getting Started](guides/getting-started.md) — clone to first use.
- [Create Your First Skill](guides/create-your-first-skill.md) — hands-on tutorial.
- [Validation & CI](guides/validation-and-ci.md) — the gate, errors vs. warnings, CI.
- [FAQ](FAQ.md) · [Architecture Diagrams](architecture-diagram.md) · [Release Checklist](release-checklist.md)

## Author & contributor guides
- [Contributor Guide](guides/contributor-guide.md) — the workflow.
- [Skill Author Guide](guides/skill-author-guide.md)
- [Agent Author Guide](guides/agent-author-guide.md)
- [Workflow Author Guide](guides/workflow-author-guide.md)
- [Playbook Author Guide](guides/playbook-author-guide.md)

## The model in one line

> **The framework is the product; skills are products the framework generates.**
> Author with the [generators](../generators/), conform to the [standards](../standards/),
> prove it with [`scripts/validate`](../scripts/validate).
