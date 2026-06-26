# Release Checklist

> A repeatable checklist for publishing the repository and cutting releases. Covers the
> **first public release** and **subsequent versioned releases**. Aligns with the
> [release-review checklist](../standards/checklists/release-review.md).

## A. First public release (one-time)

### Legal & identity
- [ ] [LICENSE](../LICENSE) present (MIT) and copyright line correct.
- [ ] README states this is an **unofficial community project** (Claude trademark note).
- [ ] All third-party content is license-compatible; provenance recorded.

### Required community health files
- [ ] [README.md](../README.md) — hero, quickstart, repo map, status.
- [ ] [CONTRIBUTING.md](../CONTRIBUTING.md), [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md),
      [SECURITY.md](../SECURITY.md).
- [ ] [.github/](../.github/) — issue templates, PR template, CODEOWNERS, CI workflow.
- [ ] [.gitignore](../.gitignore) present.

### Substitutions (no placeholders shipped)
- [ ] Repo slug `srikanth-manivannan/claude-agent-factory` correct in README badges,
      SECURITY, issue config, CI badge.
- [ ] Contact email correct in SECURITY.md / CODE_OF_CONDUCT.md.
- [ ] No leftover `OWNER`, `INSERT`, or `{{ }}` placeholders anywhere.

### Quality gate
- [ ] `sh scripts/validate` → **ALL CHECKS PASSED** (warnings OK).
- [ ] `sh scripts/build-index` succeeds.
- [ ] All internal doc links resolve.
- [ ] CI workflow runs green on a test PR.

### Repository settings (on GitHub, after push)
- [ ] Description + topics set; Discussions enabled (issue config links to it).
- [ ] Branch protection on `main`: require the `validate` check + ≥1 review.
- [ ] Private vulnerability reporting enabled (Security tab).
- [ ] License detected by GitHub (shows "MIT" in the sidebar).

### Announce
- [ ] Tag `v0.1.0`; publish the [release notes](RELEASE-NOTES-v0.1.0.md).

## B. Every versioned release

- [ ] Version bumped per SemVer ([versioning](../standards/versioning.md));
      root [CHANGELOG.md](../CHANGELOG.md) + affected per-artifact changelogs updated.
- [ ] Breaking changes flagged with a migration note; deprecations marked.
- [ ] `sh scripts/validate` green; CI green.
- [ ] `sh scripts/build-index` regenerated.
- [ ] Release notes drafted; tag created; release published.
- [ ] A rollback plan exists (revert the tag/commit).

## C. Per-wave (skill generation)

- [ ] Each new skill: scaffolded, validated, self-reviewed, registered in
      [TAXONOMY.md](../TAXONOMY.md).
- [ ] New workflows registered in [WORKFLOWS.md](../WORKFLOWS.md).
- [ ] `scripts/validate` green across the whole repo after the wave.
- [ ] Wave summarized in the CHANGELOG (MINOR bump — additive, does not unfreeze v0.1.0).
