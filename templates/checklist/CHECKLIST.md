# {{TITLE}} Checklist

> A reusable quality gate. Checklists are the **release gates** referenced by
> `standards/checklists/` and embedded in PR templates (ARCHITECTURE §11/§16).
> Every item must be **objectively verifiable** — prefer items a script can check.

**Applies to:** {{APPLIES_TO}} (e.g. every skill PR)
**Version:** {{VERSION}} · **Min standard:** {{MIN_STANDARD}}

## How to use

- [ ] Copy these items into the relevant PR / review.
- [ ] Every box must be checked (or explicitly N/A with a reason) before merge.

## Structure & naming

- [ ] Folder name matches the artifact `name` and the frontmatter `name`.
- [ ] Lives in the correct location (e.g. `skills/<category>/<name>/`).
- [ ] Naming follows `standards/naming.md`.
- [ ] No leftover `{{PLACEHOLDERS}}`.

## Required files

- [ ] Spec file present (`SKILL.md` / `AGENT.md` / `WORKFLOW.md` / `TEAM.md`).
- [ ] `README.md` present and complete.
- [ ] `metadata.yaml` present and agrees with the spec frontmatter.
- [ ] `CHANGELOG.md` present with this version's entry.
- [ ] `tests/` present and meaningful.

## Quality

- [ ] `description` is a single action-oriented sentence ("Use this to…").
- [ ] Documentation meets `standards/documentation.md`.
- [ ] Tests cover happy path, an edge case, and a failure/refusal case.
- [ ] Security rules followed (`standards/security.md`); dual-use disclosed.
- [ ] Version + `min_standard` are correct (`standards/versioning.md`).

## Composition (agents / workflows / teams)

- [ ] References use name + min version; point only *down* the ladder.
- [ ] All referenced artifacts exist at the declared versions.

## Automation

- [ ] `scripts/validate` passes locally.
- [ ] CI checks pass.
