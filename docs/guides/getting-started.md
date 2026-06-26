# Getting Started

> Go from "just cloned" to "using and creating skills" in a few minutes. New here?
> Read this first, then [Create Your First Skill](create-your-first-skill.md).

## 1. What you're looking at

The Claude Agent Factory is **a framework + a collection**. The framework (standards,
schemas, templates, generators, the validation gate) produces the collection (skills,
workflows, …). See the [README](../../README.md) and
[architecture diagram](../architecture-diagram.md).

## 2. Prerequisites

| Need | For | Required? |
|------|-----|-----------|
| A POSIX shell (Git Bash on Windows, sh/bash on macOS/Linux) | running `scripts/` and `generators/` | ✅ yes |
| Python 3 + `pip install pyyaml jsonschema referencing` | full schema + link validation | ⚪ optional |
| Claude Code | actually *running* a skill | ⚪ to use skills |

> The pure-shell path (structure, naming, placeholders) needs **no runtime**. Schema
> and link validation use an optional Python adapter that degrades gracefully.

## 3. Clone and look around

```sh
git clone https://github.com/srikanth-manivannan/claude-agent-factory.git
cd claude-agent-factory
```

| Want to… | Go to |
|----------|-------|
| Browse skills | [`skills/`](../../skills/) · the backlog [`TAXONOMY.md`](../../TAXONOMY.md) |
| Browse workflows | [`WORKFLOWS.md`](../../WORKFLOWS.md) · [`workflows/`](../../workflows/) |
| Understand the rules | [`standards/`](../../standards/) |
| Understand the design | [`VISION`](../../VISION.md) · [`ARCHITECTURE`](../../ARCHITECTURE.md) · [`FACTORY`](../../FACTORY.md) |

## 4. Use a skill

Skills are fork-first — copy one into your project and invoke it via Claude Code:

```sh
cp -r skills/architecture/tradeoff-analyzer /path/to/your/project/skills/
```

Each skill's `README.md` has a Quickstart; the `SKILL.md` is the instructions Claude
follows. A great first read: [`tradeoff-analyzer`](../../skills/architecture/tradeoff-analyzer/).

## 5. Run the validation gate

This is how you (and CI) prove an artifact is sound:

```sh
sh scripts/validate
```

You should see `validate: ALL CHECKS PASSED` (with some *pending-reference* warnings —
those are expected; see [Validation & CI](validation-and-ci.md)).

## 6. Create something

```sh
sh generators/bin/new-skill <category> <name> "Use this to ..."
```

Then follow [Create Your First Skill](create-your-first-skill.md).

## 7. Next steps

- 🛠️ [Create Your First Skill](create-your-first-skill.md)
- ✅ [Validation & CI](validation-and-ci.md)
- 🤝 [Contributing](../../CONTRIBUTING.md)
- ❓ [FAQ](../FAQ.md)
