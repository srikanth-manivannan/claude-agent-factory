# Claude Runtime Adapter

> The runtime adapter for **Claude / Claude Code** — the only runtime today
> (`runtime: claude`). Part of the pluggable [runtime seam](../README.md).

## What "runtime: claude" means

An artifact targeting this runtime is authored for Claude Code's skill model: a
`SKILL.md` with YAML frontmatter (name/description/…) plus instructions Claude follows,
optionally with helper `scripts/` and `resources/`. Skills are fork-and-run: copy the
folder into a project's skills directory and invoke via Claude Code.

## Mapping (portable format → Claude)

| Portable artifact | Claude runtime |
|-------------------|----------------|
| `SKILL.md` frontmatter `name` + `description` | Skill discovery/invocation metadata |
| `SKILL.md` instructions | The prompt/behavior Claude executes |
| `scripts/` (advanced skills) | Helper scripts the skill invokes |
| `resources/` | On-demand reference loaded progressively |

## Model guidance

Prefer the **latest Claude models** for authored prompts (see
[standards/prompt-engineering.md](../../../standards/prompt-engineering.md) and the
`claude-api` reference). The artifact format does not hardcode a model — model choice is
a runtime concern.

> This adapter is intentionally thin: most of the contract lives in the portable format
> and the [standards](../../../standards/). It exists so future runtimes have a sibling
> to mirror.
