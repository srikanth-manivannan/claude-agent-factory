# Templates

> Blank, **standards-compliant** scaffolds for every artifact type. Copy a template, replace the `{{PLACEHOLDERS}}`, and you have a compliant artifact. The Factory (`generators/`) automates this copy. Implements ARCHITECTURE.md §8.

**Rule:** templates must always satisfy the current `standards/`. A standards change that breaks a template is incomplete until the templates are updated (CI enforces this).

---

## Which template do I use?

| I want to build… | Use | Lands in |
|---|---|---|
| A single-capability skill (the common case) | [`skill/`](skill/) | `skills/<category>/<name>/` |
| A complex skill (scripts, resources, progressive disclosure) | [`skill-advanced/`](skill-advanced/) | `skills/<category>/<name>/` |
| A reusable agent role | [`agent/`](agent/) | `agents/<name>/` |
| A multi-step orchestration | [`workflow/`](workflow/) | `workflows/<name>/` |
| A reusable quality gate / checklist | [`checklist/`](checklist/) | `standards/checklists/` |
| A structured review / critique | [`review/`](review/) | (review output, e.g. PRs, `docs/`) |
| A design / architecture doc | [`architecture/`](architecture/) | repo root or `docs/` |
| A reusable prompt building block | [`prompt/`](prompt/) | `shared/prompts/` |
| A worked, runnable demonstration | [`example/`](example/) | `examples/<name>/` |
| The canonical machine metadata file | [`_meta/metadata.yaml`](_meta/metadata.yaml) | every artifact folder |
| A reusable, technology-agnostic document block | [`blocks/`](blocks/) | composed into any artifact |

> Teams (`teams/team-<domain>/`) are assembled from existing agents/workflows/skills; use the `workflow/` + `agent/` templates for the parts, then write the `TEAM.md` charter. A dedicated `team/` template arrives in a later phase.

---

## Placeholder convention

All templates use **`{{DOUBLE_BRACE}}`** placeholders. `generators/` find-and-replace these. The canonical set:

| Placeholder | Meaning | Example |
|---|---|---|
| `{{NAME}}` | kebab-case artifact name (== folder name) | `api-mock` |
| `{{TITLE}}` | Human-readable title | `API Mock` |
| `{{DESCRIPTION}}` | One action-oriented sentence ("Use this to…") | `Use this to generate mock API responses…` |
| `{{CATEGORY}}` | Parent category (skills only) | `testing` |
| `{{VERSION}}` | Per-artifact SemVer | `0.1.0` |
| `{{MIN_STANDARD}}` | Minimum `standards/` version targeted | `0.1.0` |
| `{{RUNTIME}}` | Runtime seam value | `claude` |
| `{{TAGS}}` | Discovery tags | `[testing, http]` |
| `{{AUTHOR}}` | Contributor / handle | `@example` |
| `{{DATE}}` | ISO date | `2026-06-25` |

**Anything in `{{...}}` must be replaced before an artifact passes validation.** A leftover placeholder is a lint failure.

## Standard vs Advanced skill

Both have the **same folder shape**. The difference is **depth**: `skill/` is a lean scaffold for one capability; `skill-advanced/` carries the same files with deeper guidance plus scaffolded optional `scripts/` and `resources/` for complex skills. Use Advanced only when a skill genuinely needs helper scripts, bundled resources, or progressive disclosure.
