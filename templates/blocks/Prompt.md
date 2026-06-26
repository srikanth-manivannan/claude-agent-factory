---
name: {{NAME}}
description: {{DESCRIPTION}}
version: {{VERSION}}
runtime: {{RUNTIME}}
license: MIT
tags: {{TAGS}}
---

# {{TITLE}} (Prompt)

> A reusable prompt building block (`shared/prompts/`), composed into
> skills/agents/workflows so wording is single-sourced.

> **Tech profile** — Technology: {{TECHNOLOGY}} · Language: {{LANGUAGE}} ·
> Stack: {{STACK}} · Toolchain: {{TOOLCHAIN}} · Domain: {{DOMAIN}}
> *(Keep the prompt text technology-neutral; pass stack details via variables.)*

## Purpose

What this fragment is for and where it's inserted.

## Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `{{VAR}}` | yes/no | What the caller substitutes |

## Prompt

```
<the reusable prompt text, using {{VAR}} for caller substitution.
 Do NOT hardcode a technology here — accept it as a variable.>
```

## Usage

Which section to insert this into, with what variables.

## Guidance

- Tone/format notes, known pitfalls, what NOT to put here.

## Example

**Variables:** `{{VAR}}` = … **Rendered:** …
