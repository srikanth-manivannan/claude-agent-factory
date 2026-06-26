# Contributor Guide

> How to contribute to the Claude Agent Factory. The canonical rules are
> [/standards/contributing.md](../../standards/contributing.md); this guide is the
> practical walkthrough. Be excellent and kind (VISION §10).

## TL;DR

```sh
# 1. Scaffold (inherit the standards by construction)
sh generators/bin/new-skill <category> <name> "Use this to ..."
# 2. Fill in the scaffold, conform to /standards/
# 3. Register it: add a row to /TAXONOMY.md (skills) or /WORKFLOWS.md (workflows)
# 4. Prove it
sh scripts/validate
# 5. Self-review with /standards/checklists/, then open a PR
```

## Prerequisites

- A POSIX shell (Git Bash on Windows). **Optional:** Python 3 + `pip install pyyaml
  jsonschema referencing` for full schema/link validation (CI runs this).

## The contribution flow

1. **Fork & branch** — never work on the default branch.
2. **Scaffold** with a [generator](../../generators/) — don't hand-roll structure.
3. **Build to the standards** — every doc in [/standards/](../../standards/). Cross-
   reference; never duplicate guidance.
4. **Validate** — `sh scripts/validate` until green (== CI).
5. **Self-review** — run the [universal core](../../standards/checklists/_universal.md)
   + the relevant domain checklist(s).
6. **Register** — skills → [/TAXONOMY.md](../../TAXONOMY.md); workflows →
   [/WORKFLOWS.md](../../WORKFLOWS.md); new category → [`new-category`](../../generators/bin/new-category) + TAXONOMY.
7. **PR** — fill the template (embeds the checklist) and attach `scripts/validate` output.

## What gets your PR merged

- `scripts/validate` is **green** (errors fail; pending-reference and recommended-file
  **warnings** are acceptable).
- Standards compliance — judged against the [checklists](../../standards/checklists/),
  not the author. The bar is identical for everyone (VISION §6).

## Artifact-specific guides

- [Skill Author Guide](skill-author-guide.md) · [Agent](agent-author-guide.md) ·
  [Workflow](workflow-author-guide.md) · [Playbook](playbook-author-guide.md)

## Licensing

All contributions are **MIT**, inbound = outbound. Third-party content must be
license-compatible (record provenance in `RESOURCES.md`).
