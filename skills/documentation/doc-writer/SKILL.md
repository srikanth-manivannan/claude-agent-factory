---
name: doc-writer
description: Use this to write or refresh a README and docs from code and intent, following the documentation standard.
version: 0.1.0
category: documentation
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [documentation, readme, writing, docs]
---

# Doc Writer

> Use this to write or refresh a README and docs from code and intent, following the documentation standard.

> **Tech profile** — Technology: any · Language: any · Stack: any · Toolchain: any · Domain: documentation
> *(Documents any artifact or codebase; structure comes from the documentation standard.)*

## When to use this skill

- Writing a README for new code, a skill, or a project.
- Refreshing stale docs to match current behavior.
- Standardizing docs across a repo to a consistent shape.

## When NOT to use this skill

- Generating API reference from a spec — use `documentation/api-reference-generator`.
- Linting existing docs only — use `documentation/doc-linter`.
- Writing inline docstrings — use `documentation/docstring-writer`.

## Prerequisites

- The subject (code, artifact, or feature) and its intent/audience.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subject` | yes | What is being documented |
| `audience` | no | Who reads it (defaults to developers) |
| `existing_docs` | no | Current docs to refresh, if any |

## Instructions

1. **Identify subject, audience, and purpose.** What problem does it solve; who reads
   this and why.
2. **Apply the required structure** from [/standards/documentation.md](../../../standards/documentation.md):
   title + one-sentence description, What it does, Quickstart, Inputs & outputs,
   Customization, Limitations, Changelog link.
3. **Write a runnable Quickstart.** Copy-pasteable; the fastest path to first value.
4. **Be accurate, not aspirational.** Document actual behavior; mark known limitations
   honestly. Never describe features that don't exist.
5. **Cross-reference, don't duplicate.** Link to standards/related artifacts instead of
   restating them.
6. **Keep it GitHub-readable.** Headings, tables, short paragraphs, working relative links.
7. **Verify no leftover placeholders** and that links resolve.

## Output

A complete `README.md` (and any requested companion docs) matching the documentation
standard's required sections, accurate to current behavior, with working links.

## Constraints & safety

- **One-sentence `description`** ([/standards/naming.md](../../../standards/naming.md)).
- **No invented behavior**; no stale claims.
- **No secrets** in examples ([/standards/security.md](../../../standards/security.md)).

## Examples

Minimal below; full examples in [EXAMPLES.md](EXAMPLES.md).

**Given:** an undocumented utility library.
**Produces:** a README with a one-line description, a 3-step quickstart, inputs/outputs,
customization, and honest limitations.
