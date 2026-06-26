# Documentation Standard

> What every artifact must document. "Undocumented = doesn't exist" (VISION §6.4).
> Enforced by the [documentation-review checklist](checklists/documentation-review.md);
> templates implement it via [`/templates/blocks/`](../templates/blocks/).

**Min standard:** 0.1.0 · See also: [naming.md](naming.md) (descriptions),
[prompt-engineering.md](prompt-engineering.md).

## Required documents

Every artifact folder contains:

- **Spec file** (`SKILL.md` / `AGENT.md` / `WORKFLOW.md` / `TEAM.md` / `PLAYBOOK.md`)
  — the artifact itself.
- **`README.md`** — the human overview (sections below).
- **`CHANGELOG.md`** — per [versioning.md](versioning.md).
- **`IMPLEMENTATION.md`** — **required for skills**: how to apply the skill (build order,
  key decisions, pitfalls, hand-off). Enforced by `scripts/validate`.

## Required & recommended docs by artifact type

Expectations differ per type (enforced by `scripts/validate`). **Required** = error if
missing; **recommended** = warning only.

| Type | Required | Recommended |
|------|----------|-------------|
| **skill** | spec + README + metadata.yaml + CHANGELOG + **IMPLEMENTATION.md** + `tests/` | EXAMPLES, TROUBLESHOOTING, RESOURCES, REVIEW |
| **agent** | spec + README + metadata.yaml + CHANGELOG | RESOURCES, REVIEW |
| **team** | spec + README + metadata.yaml + CHANGELOG | RESOURCES |
| **workflow** | spec + README + metadata.yaml + CHANGELOG | RESOURCES, REVIEW |
| **playbook** | spec + README + metadata.yaml + CHANGELOG | RESOURCES, REVIEW |

Rationale: skills carry the full doc set (they're the implemented unit); roles and
orchestrators (agent/team/workflow/playbook) need cross-links + review notes, but the
skill-oriented EXAMPLES/TROUBLESHOOTING are not expected of them.

## Required README sections

| Section | Must contain |
|---------|--------------|
| Title + description | The one action-oriented sentence ([naming.md](naming.md)) |
| What it does | Plain-language problem it solves + why fork it |
| Quickstart | Copy-paste runnable steps (supports VISION's "minutes to first use") |
| Inputs & outputs | What it consumes and produces |
| Customization | Safe extension points |
| Limitations | Honest constraints |
| Changelog link | → `CHANGELOG.md` |

For technical artifacts, prefer the reusable blocks:
[Troubleshooting](../templates/blocks/Troubleshooting.md),
[Resources](../templates/blocks/Resources.md),
[Examples](../templates/blocks/Examples.md).

## Rules

- **One sentence descriptions.** No paragraphs in `description`.
- **No leftover `{{placeholders}}`** (tech-profile fields may be `n/a`).
- **Docs match behavior.** Stale docs are a defect.
- **Cross-reference, don't duplicate** — link to standards rather than restating them.
- **GitHub-readable** — headings, tables, short paragraphs, working relative links.
