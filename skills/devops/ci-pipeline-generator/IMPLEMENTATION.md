# Implementation Guidance — CI Pipeline Generator

> How to apply this skill. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Build order

1. **Detect stack + CI platform** (or use the stated one); match conventions.
2. **Define fast-fail stages** — install → lint → test → build → validate.
3. **Wire the test stage** to the project's tests; **fail the build on any test failure**.
4. **Add caching** for deps/build artifacts; **pin tool versions** (reproducible).
5. **Add a security step** + **gate merges** (required status check).

## Key decisions

| Decision | Guidance |
|----------|----------|
| Ordering | Fast-fail: cheap checks (lint) before expensive (test/build) |
| Secrets | Platform secret store — never inline |
| Reproducibility | Pin versions; local commands match CI (`scripts/validate == CI`) |

## Pitfalls

- ❌ `continue-on-error` on tests → ✅ tests must fail the build.
- ❌ No caching → ✅ cache deps/artifacts (CI speed).
- ❌ Red CI still mergeable → ✅ set as a required status check.

## Hand-off

Feeds the `release-pipeline` workflow and `cd-deployment-builder` (planned); consumed by
`developer-experience/project-scaffolder`; pair with `dockerfile-author` (planned).
