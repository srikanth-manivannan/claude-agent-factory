---
name: {{NAME}}
description: {{DESCRIPTION}}
version: {{VERSION}}
runtime: {{RUNTIME}}
license: MIT
tags: {{TAGS}}
---

# {{TITLE}} (Prompt)

> A reusable prompt building block. Lives in `shared/prompts/` and is composed
> into skills/agents/workflows so wording is single-sourced (ARCHITECTURE §10).

## Purpose

What this prompt fragment is for and where it's meant to be inserted.

## Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `{{VAR}}` | yes/no | What the caller substitutes |

## Prompt

```
<the reusable prompt text, with {{VAR}} placeholders for caller substitution>
```

## Usage

How to compose this into an artifact (which section, with what variables).

## Notes & guidance

- Tone/format guidance, known pitfalls, and what NOT to put here.

## Examples

**Variables:** `{{VAR}}` = …
**Rendered:** …
