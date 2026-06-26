# FAQ

## General

**What is the Claude Agent Factory?**
A framework + collection for building production-ready agentic building blocks. The
framework (standards, schemas, templates, generators, a validation gate) produces the
collection (skills, workflows, agents, teams, playbooks). See the [README](../README.md).

**Is this an official Anthropic project?**
No. It's an independent, community, MIT-licensed project. "Claude" is Anthropic's
trademark, used here only to describe compatibility (nominative fair use).

**What's the difference between a skill, agent, workflow, team, and playbook?**
- **Skill** — a reusable capability.
- **Agent** — an AI specialist that applies skills.
- **Team** — a coordinated collection of agents.
- **Workflow** — a repeatable sequence of activities (composes ≥2 skills).
- **Playbook** — an operating guide composing teams + workflows for a full outcome.

See [standards/architecture.md](../standards/architecture.md) and the
[diagram](architecture-diagram.md).

## Using it

**How do I use a skill in my project?**
Copy the skill folder into your project's skills directory and invoke it via Claude
Code. Each skill's `README.md` has a Quickstart.

**Do I have to adopt the whole framework?**
No — it's fork-first. Take a single skill and run; there's no lock-in (MIT).

**Do I need Python?**
Only for *full* validation (schema + links) and the catalog index. The basic checks
(structure, naming, placeholders) and all generators are pure shell. See
[Validation & CI](guides/validation-and-ci.md).

## Contributing

**How do I add a skill?**
`sh generators/bin/new-skill <category> <name> "..."`, fill in the scaffold, run
`sh scripts/validate`, add a row to [TAXONOMY.md](../TAXONOMY.md), open a PR. Full
tutorial: [Create Your First Skill](guides/create-your-first-skill.md).

**What are "pending references" and why are they warnings, not errors?**
A workflow may reference a skill that isn't built yet (the "declared-pending" pattern).
That's intentional — the workflow defines the contract the skill must meet. The warning
auto-resolves when the skill is built. Cycles and missing *required files*, by contrast,
are hard errors.

**My PR's CI failed on a date — why?**
Bare YAML dates parse as date objects and fail the schema. Quote them:
`created: "2026-06-26"`.

**Who reviews contributions?**
Maintainers via [CODEOWNERS](../.github/CODEOWNERS), against the public
[checklists](../standards/checklists/). Acceptance is based on standards compliance, not
author identity — the bar is identical for everyone.

## Project

**Why is the framework "frozen"?**
v0.1.0 froze the architecture, standards, schemas, and validation model so that
mass-generated skills inherit a stable contract. Adding skills is *additive* (MINOR) and
doesn't unfreeze it; breaking the contract requires a MAJOR bump + migration note. See
[ADR 0001](adr/0001-framework-v0.1.0-freeze.md).

**Can this support models other than Claude?**
It's Claude-first but architected to be expandable. The artifact format is portable; the
runtime is pluggable (`shared/runtime/`). Adding a model is additive. See [VISION §15](../VISION.md).

**How do I report a security issue?**
Privately — see [SECURITY.md](../SECURITY.md). Do not open a public issue.

**Where do I ask a question not covered here?**
Open a GitHub Discussion (link in the issue template), or read the
[guides](guides/) and foundational docs.
