<div align="center">

# 🏭 Claude Agent Factory

**The open-source standard library for agentic engineering — fork, customize, extend.**

Build enterprise-grade Claude Code Skills, agentic AI workflows, and reusable AI engineering teams.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/framework-v0.1.0%20(frozen)-blue.svg)](docs/RELEASE-NOTES-v0.1.0.md)
[![Standard](https://img.shields.io/badge/standard-0.1.0-blue.svg)](standards/README.md)
[![CI](https://github.com/srikanth-manivannan/claude-agent-factory/actions/workflows/validate.yml/badge.svg)](https://github.com/srikanth-manivannan/claude-agent-factory/actions/workflows/validate.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

> ⚠️ **Community project.** Not affiliated with or endorsed by Anthropic. "Claude" is a
> trademark of Anthropic; this project uses it under nominative fair use to describe
> compatibility.

---

## What is this?

The Claude Agent Factory is a **framework for producing production-ready, reusable
agentic building blocks** — and a growing **collection** of them. Instead of starting
every agentic project from a blank file, you fork a proven, validated foundation.

Two things live here:

1. **The framework** *(the product)* — standards, schemas, templates, a validation
   gate, and generators that turn an idea into a standards-compliant artifact in minutes.
2. **The collection** *(products the framework generates)* — skills, workflows, agents,
   teams, and playbooks, each documented, tested, versioned, and review-gated.

## Why?

- **Fork-first, not framework-first** — take one piece and run; no lock-in (MIT).
- **Quality is enforced, not hoped for** — every artifact passes a real gate
  (`scripts/validate`, the same check CI runs).
- **Consistent by construction** — generators bake the standards in, so the easy path
  is the correct path.
- **Composable** — skills → agents → teams / workflows → playbooks.

## Quickstart

### Use a skill (fork-and-run)
```sh
# Copy a skill into your project's skills directory, then invoke it via Claude Code.
cp -r skills/architecture/tradeoff-analyzer /path/to/your/project/skills/
```
Browse the collection in [`skills/`](skills/) or the backlog in [TAXONOMY.md](TAXONOMY.md).

### Create a skill (author-and-validate)
```sh
sh generators/bin/new-skill data schema-designer "Use this to design a database schema."
# fill in the scaffold, then:
sh scripts/validate
```
Full walkthrough: **[Create Your First Skill](docs/guides/create-your-first-skill.md)**.

> **Requirements:** a POSIX shell (Git Bash on Windows). *Optional* for full schema/link
> validation: `pip install pyyaml jsonschema referencing` (the pure-shell path needs no runtime).

## The artifact hierarchy

```
Skill     → a reusable capability
  └─ Agent      → an AI specialist that applies skills
       └─ Team       → a coordinated collection of agents
Workflow  → a repeatable sequence of activities (composes ≥2 skills)
  └─ Playbook   → an operating guide composing teams + workflows for a full outcome
```

Defined in [standards/architecture.md](standards/architecture.md); diagram in
[docs/architecture-diagram.md](docs/architecture-diagram.md).

## Repository map

| Path | What |
|------|------|
| [`skills/`](skills/) | The collection, grouped by category |
| [`workflows/`](workflows/) | Multi-skill orchestrations |
| [`standards/`](standards/) | The rules every artifact must satisfy (+ [checklists](standards/checklists/)) |
| [`shared/schemas/`](shared/schemas/) | JSON-Schema for each artifact type |
| [`templates/`](templates/) | Scaffolds + a technology-agnostic block library |
| [`generators/`](generators/) | The Factory's scaffolders (`new-skill`, …) |
| [`scripts/`](scripts/) | The validation gate (`validate`, `lint`, …) |
| [`docs/`](docs/) | Guides, release notes, decision records |
| [VISION](VISION.md) · [ARCHITECTURE](ARCHITECTURE.md) · [FACTORY](FACTORY.md) | Foundational specs |
| [TAXONOMY](TAXONOMY.md) · [WORKFLOWS](WORKFLOWS.md) | The backlog + workflow library |

## Status

**Framework v0.1.0 — frozen and stable.** The framework (standards, schemas, templates,
generators, validation gate) is production-grade and the engineering graph is fully
connected (zero unresolved dependencies).

**Catalog (65 artifacts, all validating):** 38 skills · 6 agents · 4 teams · 12 workflows
· 5 playbooks, across 15 categories, plus 3 end-to-end [showcases](examples/showcases/).

> **Skill maturity:** **15** skills are **reference-grade** (fully documented gold
> standard) — start with [`skills/architecture/`](skills/architecture/). The other **23**
> are **baseline** skills generated to complete the dependency graph; they have valid
> contracts and structure with **expanded guidance in progress**. Each skill's
> `README.md` reflects its depth. Contributions to deepen baseline skills are very
> welcome — see [Contributing](CONTRIBUTING.md).

See the [Release Notes](docs/RELEASE-NOTES-v0.1.0.md) and [CHANGELOG](CHANGELOG.md).

## Maturity model

This is an **honest preview release**. Every skill declares its depth via a `maturity`
field in `metadata.yaml`, so you always know what you're getting:

| Maturity | Meaning | Status |
|----------|---------|--------|
| 🥇 **gold** | Production reference implementation — fully documented, exemplary depth | `active` |
| 🔹 **baseline** | Complete but intentionally concise — valid contract, structure, and standards conformance; minimal examples | `draft` |
| ⏳ **draft** | Planned future enhancement (placeholder for a not-yet-built artifact) | `draft` |

**Today:** 15 skills are 🥇 gold (start with [`skills/architecture/`](skills/architecture/));
23 are 🔹 baseline. All 65 artifacts validate; the engineering graph is fully connected.
Deepening baseline skills toward gold is the most welcome contribution
([Contributing](CONTRIBUTING.md)).

## Documentation

- 🚀 [Getting Started](docs/guides/getting-started.md)
- 🛠️ [Create Your First Skill](docs/guides/create-your-first-skill.md)
- ✅ [Validation & CI](docs/guides/validation-and-ci.md)
- 🤝 [Contributing](CONTRIBUTING.md) · [Code of Conduct](CODE_OF_CONDUCT.md)
- ❓ [FAQ](docs/FAQ.md) · 🔒 [Security](SECURITY.md)
- 💬 [Discussions](https://github.com/srikanth-manivannan/claude-agent-factory/discussions) — questions, ideas, show & tell

## Contributing

We'd love your help growing the collection. Every contribution is scaffolded by a
generator, validated by the gate, and reviewed against public checklists — the bar is
the same for everyone. Start with the [Contributor Guide](docs/guides/contributor-guide.md).

## License

[MIT](LICENSE) © Srikanth Manivannan. Inbound = outbound.
