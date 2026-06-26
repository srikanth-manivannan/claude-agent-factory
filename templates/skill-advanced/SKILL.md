---
name: {{NAME}}
description: {{DESCRIPTION}}
version: {{VERSION}}
category: {{CATEGORY}}
runtime: {{RUNTIME}}
min_standard: {{MIN_STANDARD}}
license: MIT
tags: {{TAGS}}
---

# {{TITLE}}

> {{DESCRIPTION}}

<!-- ADVANCED SKILL. Same folder shape as the standard skill, deeper guidance.
     Use this only when the skill genuinely needs helper scripts, bundled
     resources, or progressive disclosure. -->

## When to use this skill

- Use when …
- Use when …

## When NOT to use this skill

- Don't use for … (point to the simpler alternative)

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| {{INPUT_NAME}} | yes/no | What it is | Acceptable values / format |

## Instructions

High-level procedure first; details progressively disclosed below so Claude only
loads what it needs.

1. …
2. … (if helper needed, call `scripts/{{HELPER}}` — see "Helper scripts")
3. …

### Progressive disclosure

Keep the top-level instructions short. Put long reference material in
`resources/` and load it only when the relevant branch is taken.

- For <case A>, read `resources/REFERENCE.md` section X.
- For <case B>, run `scripts/{{HELPER}}`.

## Helper scripts

| Script | Purpose | Inputs | Outputs |
|--------|---------|--------|---------|
| `scripts/{{HELPER}}` | … | … | … |

Scripts must be language-neutral/portable per ARCHITECTURE §9 (prefer POSIX shell;
declare any runtime in `metadata.yaml`).

## Resources

| File | Purpose |
|------|---------|
| `resources/REFERENCE.md` | Detailed reference loaded on demand |

## Output

Exact format, structure, and side effects.

## Constraints & safety

- Preconditions, limits, and safety rules (per `standards/security.md`).
- Dual-use disclosure if applicable.

## Error handling

How the skill behaves on bad input or failure. Should fail gracefully.

## Examples

Minimal examples here; full runnable demos in `examples/`.
