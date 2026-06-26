# Naming Standard

> Naming rules for every artifact, file, and category. Implements VISION §11.2.
> Enforced by [`/shared/schemas/metadata.schema.yaml`](../shared/schemas/metadata.schema.yaml)
> and the [universal checklist](checklists/_universal.md).

**Min standard:** 0.1.0 · See also: [metadata.md](metadata.md), [architecture.md](architecture.md).

## The one rule

> **Folder name == artifact `name` == frontmatter/`metadata.yaml` `name`.** All three
> are identical, lowercase **kebab-case**: `^[a-z0-9]+(-[a-z0-9]+)*$`.

## Per-artifact naming

| Artifact | Form | Example |
|----------|------|---------|
| **Skill** | noun/verb phrase of the capability | `pdf-extract`, `rest-endpoint-scaffold` |
| **Agent** | role-based name | `code-reviewer`, `release-manager` |
| **Team** | domain, prefixed `team-` | `team-backend`, `team-security` |
| **Workflow** | outcome-based name | `build-feature`, `fix-bug` |
| **Playbook** | objective, prefixed `play-` | `play-zero-to-production`, `play-secure-launch` |
| **Category** | plural-ish domain slug | `testing`, `agentic-ai` |
| **Prompt block** | what it produces | `code-review-rubric` |

## Paths

- Skills live at `skills/<category>/<name>/` — the category folder must match the
  `category` field (see [metadata.md](metadata.md)).
- All other artifacts: `<type-plural>/<name>/` (`agents/`, `teams/`, `workflows/`,
  `playbooks/`).

## Descriptions

Every artifact's `description` is **one action-oriented sentence** ("Use this to…").
It drives discovery and invocation; keep it specific. (Detailed in
[documentation.md](documentation.md).)

## Reserved / conventions

- Files prefixed `_` (e.g. `_universal.md`, `templates/_meta/`) are shared/internal,
  not artifacts.
- Spec files are UPPERCASE: `SKILL.md`, `AGENT.md`, `WORKFLOW.md`, `TEAM.md`,
  `PLAYBOOK.md`. Machine metadata is `metadata.yaml`.
- No spaces, no camelCase, no underscores inside artifact names.
