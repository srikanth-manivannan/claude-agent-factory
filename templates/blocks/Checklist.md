# {{TITLE}} Checklist

> A reusable, **technology-agnostic** quality gate. Every item is objectively
> verifiable (prefer items a script can check). Reused by `standards/checklists/`
> and PR templates.

**Applies to:** {{APPLIES_TO}}
**Version:** {{VERSION}} · **Min standard:** {{MIN_STANDARD}}

## How to use

- [ ] Every box checked, or explicitly **N/A** with a reason, before merge.

## Structure & naming
- [ ] Folder name == artifact `name` == frontmatter `name`.
- [ ] Correct location (e.g. `skills/<category>/<name>/`).
- [ ] Naming follows `standards/naming.md`.
- [ ] No leftover `{{PLACEHOLDERS}}` (tech-profile fields may be `n/a`, braces gone).

## Required files
- [ ] Spec file present and complete.
- [ ] `README.md` present and complete.
- [ ] `metadata.yaml` present and agrees with the spec frontmatter.
- [ ] `CHANGELOG.md` has this version's entry.
- [ ] `tests/` present and meaningful.

## Quality
- [ ] `description` is one action-oriented sentence.
- [ ] Docs meet `standards/documentation.md`.
- [ ] Tests cover happy path, an edge case, and a failure/refusal case.
- [ ] Security rules followed (`standards/security.md`); dual-use disclosed.
- [ ] Version + `min_standard` correct (`standards/versioning.md`).

## Technology-agnostic check
- [ ] No concrete technology hardcoded where a Tech-profile placeholder belongs.
- [ ] Artifact reads correctly with the Tech profile set to a *different* stack.

## Composition
- [ ] References use name + min version and point only *down* the ladder.
- [ ] All referenced artifacts exist at the declared versions.

## Automation
- [ ] `scripts/validate` passes locally.
- [ ] CI checks pass.
