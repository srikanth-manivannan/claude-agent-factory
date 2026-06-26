# Examples — CI Pipeline Generator

> Worked examples. Platform-agnostic; emits config for the target CI. See [SKILL.md](SKILL.md).

## Example 1 — Standard pipeline (happy path)

**Input:** a project with a unit-test suite; CI platform = the project's default.

**Produces (stages):**
1. install (with dependency cache)
2. lint / format check
3. **test** — runs the suite; **build fails on any failure**
4. build
5. validate (structural checks)

Plus: required status check on the default branch; pinned tool versions; a note on
running the same steps locally.

## Example 2 — Edge: extra stages

**Input:** `stages: [type-check, security-scan]`.

**Behavior:** inserts type-check before test and a dependency/secret scan after build;
keeps fast-fail ordering.

## Example 3 — Edge: platform inference

**Input:** no `ci_platform`.

**Behavior:** detects the platform from the repo and emits its native config format,
matching existing conventions.

## Anti-example

- ❌ `continue-on-error: true` on the test stage. Tests must gate the build — green CI
  over failing tests is forbidden.
- ❌ Hardcoding a token in the config. Use the platform's secret store.

## Try it yourself

- Add `stages: [coverage]` — note the coverage step + threshold gate.
- Remove caching and compare CI duration on a re-run.
