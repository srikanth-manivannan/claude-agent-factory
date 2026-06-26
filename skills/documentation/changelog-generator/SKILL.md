---
name: changelog-generator
description: Use this to generate a Keep a Changelog entry from a set of changes.
version: 0.1.0
category: documentation
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [documentation]
---

# Changelog Generator

> Use this to generate a Keep a Changelog entry from a set of changes.

> **Maturity: baseline** — complete but intentionally concise. See the
> [maturity model](../../../README.md#maturity-model). The 15 gold-standard skills are the
> deep reference implementations.

## When to use this skill
- When you need to: use this to generate a keep a changelog entry from a set of changes.
- As part of a documentation workflow that requires this capability.

## When NOT to use this skill
- For needs outside this single capability — see related skills in the [documentation category](../).

## Inputs
| Input | Required | Description |
|-------|----------|-------------|
| subject | yes | What the skill operates on (the thing to act upon). |
| context | no | Constraints, goals, or standards that shape the result. |

## Instructions
1. Confirm the goal — _Use this to generate a Keep a Changelog entry from a set of changes._ — and gather the inputs above.
2. Apply the method and conform to the relevant [standards](../../../standards/).
3. Produce the output and validate it (see Output and `tests/`).

## Output
A clear, reviewable result that fulfils the skill's purpose: _Use this to generate a Keep a Changelog entry from a set of changes._

## Constraints & safety
- Conforms to [/standards/security.md](../../../standards/security.md) and
  [/standards/prompt-engineering.md](../../../standards/prompt-engineering.md).

## Examples
See [EXAMPLES.md](EXAMPLES.md). This is a baseline skill — concise by design.
