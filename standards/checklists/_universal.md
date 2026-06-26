# Universal Core Checklist

> The items **every** artifact (skill, agent, workflow, team) must pass, regardless
> of domain. **Run this first**, then the relevant domain checklist. Shared by all
> review checklists (the DRY "universal core"). Legend: see
> [README.md](README.md).

**Applies to:** every artifact · **Min standard:** 0.1.0

## Structure & location
- [ ] 🔴 `[auto]` Folder name == artifact `name` == frontmatter `name`.
- [ ] 🔴 `[auto]` Lives in the correct path (e.g. `skills/<category>/<name>/`).
- [ ] 🟠 `[auto]` Naming follows `standards/naming.md` (kebab-case, correct form).

## Required files
- [ ] 🔴 `[auto]` Spec file present (`SKILL.md`/`AGENT.md`/`WORKFLOW.md`/`TEAM.md`).
- [ ] 🔴 `[auto]` `README.md` present.
- [ ] 🔴 `[auto]` `metadata.yaml` present.
- [ ] 🔴 `[auto]` `CHANGELOG.md` present with an entry for this version.
- [ ] 🔴 `[auto]` `tests/` present and non-empty.

## Metadata & schema
- [ ] 🟠 `[auto]` `metadata.yaml` + frontmatter validate against `shared/schemas/`.
- [ ] 🟠 `[auto]` `metadata.yaml` agrees with the spec frontmatter.
- [ ] 🔴 `[auto]` No leftover `{{placeholders}}` (tech-profile fields may be `n/a`).

## Versioning
- [ ] 🟠 `[auto]` `version` is valid SemVer; `min_standard` set (`standards/versioning.md`).
- [ ] 🟡 `[manual]` Version bump matches the change type (MAJOR/MINOR/PATCH).

## Composition & links
- [ ] 🟠 `[auto]` All references resolve at their declared min versions (`tests/links/`).
- [ ] 🟠 `[auto]` Composition points only *down* the ladder; graph is acyclic.

## Documentation baseline
- [ ] 🟠 `[manual]` `description` is one action-oriented sentence ("Use this to…").

## Safety baseline
- [ ] 🔴 `[auto]` No secrets committed.
- [ ] 🟠 `[manual]` Dual-use behavior disclosed; authorized use only (→ `security-review`).

## Validation
- [ ] 🔴 `[auto]` `scripts/validate` passes locally.
- [ ] 🔴 `[auto]` CI is green.
