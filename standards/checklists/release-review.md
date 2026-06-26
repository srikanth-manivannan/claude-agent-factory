# Release Review Checklist

> Reviews readiness to cut a release. Run **after** the
> [Universal Core](_universal.md). Backs the `release-pipeline` workflow.
> Legend: [README.md](README.md).

**Applies to:** any release (repo-level or per-artifact) · **Min standard:** 0.1.0

## Versioning & notes
- [ ] 🔴 `[auto]` Version bumped per SemVer (`standards/versioning.md`).
- [ ] 🔴 `[auto]` `CHANGELOG.md` has an entry for this release.
- [ ] 🟡 `[manual]` Release notes drafted and accurate.
- [ ] 🟡 `[auto]` Release tag created.

## Compatibility
- [ ] 🟠 `[manual]` Breaking changes flagged with a migration note.
- [ ] 🟠 `[manual]` Deprecations marked (`status: deprecated` + `deprecated_by`).
- [ ] 🟠 `[manual]` Downstream dependents of MAJOR changes notified.

## Quality gate
- [ ] 🔴 `[auto]` All CI checks green (`scripts/validate == CI`).
- [ ] 🟡 `[manual]` Docs updated to match the release.
- [ ] 🟡 `[manual]` A rollback plan exists for this release.
