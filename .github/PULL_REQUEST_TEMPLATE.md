<!-- Thanks for contributing to the Claude Agent Factory! -->

## What does this PR do?

<!-- One or two sentences. Link any related issue: Closes #__ -->

## Type of change
- [ ] New skill
- [ ] New workflow / agent / team / playbook
- [ ] New category
- [ ] Framework / tooling / docs
- [ ] Fix

## Checklist (see [standards/checklists/](../standards/checklists/))

**Universal core**
- [ ] Scaffolded from a generator (or matches the canonical structure)
- [ ] Folder name == artifact `name` == frontmatter `name`
- [ ] All required files present; **no leftover `{{placeholders}}`**
- [ ] `metadata.yaml` agrees with the spec frontmatter and validates against its schema
- [ ] Version + `min_standard` set; `CHANGELOG.md` updated
- [ ] No secrets committed

**Quality**
- [ ] `description` is one action-oriented sentence
- [ ] Docs complete per [standards/documentation.md](../standards/documentation.md)
- [ ] Tests cover happy / edge / failure ([standards/testing.md](../standards/testing.md))
- [ ] Security rules followed ([standards/security.md](../standards/security.md)); dual-use disclosed

**Registration & proof**
- [ ] Registered: skill → `TAXONOMY.md`; workflow → `WORKFLOWS.md`
- [ ] `sh scripts/validate` passes locally (paste the summary below)
- [ ] Self-reviewed with the relevant domain checklist(s)

## `scripts/validate` output

```
<!-- paste the summary line, e.g. "validate: ALL CHECKS PASSED" -->
```
