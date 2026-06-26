# Implementation Guidance — Project Scaffolder

> How to produce a golden-path scaffold a fresh clone can run. See [SKILL.md](SKILL.md)
> and [/standards/documentation.md](../../../standards/documentation.md).

## Build order

1. **Layout** — source/tests/docs/config dirs with predictable names for the stack.
2. **Task runner** — define the standard verbs first; everything else hangs off them.
3. **Test harness** — one passing example (via `testing/unit-test-generator`) so `test` works.
4. **Lint/format/pre-commit** — automatic style.
5. **CI** — via `devops/ci-pipeline-generator` (install → lint → test → build, required).
6. **Conventions** — LICENSE, .gitignore, editorconfig, CODEOWNERS, CHANGELOG, .env.example.
7. **Docs** — README skeleton per the documentation standard.
8. **Verify** — fresh clone → `setup` → `test` green.

## The standard verbs (every project, same interface)

```make
setup:   ## install deps + hooks
test:    ## run the test suite
lint:    ## lint + format check
build:   ## build artifacts
run:     ## run locally
```
Consistent verbs across repos are the single biggest DX win — contributors never relearn.

## Golden-path rule

> A new contributor, on a fresh clone, with **no tribal knowledge**, runs `setup` then
> `test` and sees green. If that's not true, the scaffold isn't done.

## Conventions as enforcement

| Convention | Mechanism |
|------------|-----------|
| Style | lint + format + pre-commit (fails the commit) |
| Quality gate | CI required status check |
| Ownership | CODEOWNERS |
| Licensing | LICENSE + headers if org requires |
| Secrets hygiene | `.env.example` only; `.env` gitignored |

## Secrets

Never ship a real `.env`. Provide `.env.example` with placeholder keys and document
required variables in the README. (See `security/secret-scanner`.)

## Handing off

For a deployable service, chain into the `scaffold-new-service` workflow (adds
containerization/infra). The scaffold is the foundation, not the whole system.
