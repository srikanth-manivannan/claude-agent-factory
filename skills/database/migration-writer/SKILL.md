---
name: migration-writer
description: Use this to write safe, reversible database migrations from a schema change.
version: 0.1.0
category: database
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [database]
---

# Migration Writer

> Use this to write safe, reversible database migrations from a schema change.

> **Maturity: baseline** — complete but intentionally concise. See the
> [maturity model](../../../README.md#maturity-model). The 15 gold-standard skills are the
> deep reference implementations.

## When to use this skill
- When you need to: use this to write safe, reversible database migrations from a schema change.
- As part of a database workflow that requires this capability.

## When NOT to use this skill
- For needs outside this single capability — see related skills in the [database category](../).

## Inputs
| Input | Required | Description |
|-------|----------|-------------|
| subject | yes | What the skill operates on (the thing to act upon). |
| context | no | Constraints, goals, or standards that shape the result. |

## Instructions
1. Confirm the goal — _Use this to write safe, reversible database migrations from a schema change._ — and gather the inputs above.
2. Apply the method and conform to the relevant [standards](../../../standards/).
3. Produce the output and validate it (see Output and `tests/`).

## Output
A clear, reviewable result that fulfils the skill's purpose: _Use this to write safe, reversible database migrations from a schema change._

## Constraints & safety
- Conforms to [/standards/security.md](../../../standards/security.md) and
  [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md).

## Examples
See [EXAMPLES.md](EXAMPLES.md). This is a baseline skill — concise by design.
