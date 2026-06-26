# Examples — Project Scaffolder

> Realistic enterprise scenarios. Stack-agnostic method; layout shown generically. See [SKILL.md](SKILL.md).

## Example 1 — New backend service (happy path)

**Inputs:** project_type = service; name = `billing-svc`; conventions = MIT, CODEOWNERS,
conventional commits.

**Produces:**
```
billing-svc/
├── src/                      # source (golden-path layout)
├── tests/                    # test harness + one passing example test
├── docs/                     # README + docs skeleton (per documentation standard)
├── .github/workflows/ci.yml  # install → lint → test → build (required check)
├── .pre-commit-config        # lint + format on commit
├── Makefile                  # setup | test | lint | build | run
├── LICENSE  .gitignore  .editorconfig  CODEOWNERS  CHANGELOG.md  .env.example
└── README.md
```
**Golden-path proof:** `make setup && make test` is green on a fresh clone.

## Example 2 — Library (different layout, same verbs)

**Inputs:** project_type = library; name = `retry-utils`.

**Behavior:** uses a library layout (public API surface, packaging metadata, docs for
consumers) but exposes the **same task verbs** (`setup/test/lint/build`) so contributors
move between repos without relearning.

## Example 3 — Edge: org conventions

**Inputs:** conventions = "Apache-2.0, require 2 reviewers, trunk-based".

**Behavior:** sets the Apache license, encodes CODEOWNERS + a note for branch protection
(2 reviewers), and configures a trunk-based `.gitignore`/CI — conventions enforced, not
just documented.

## Anti-example

- ❌ A bare repo with a single file and "we'll add CI/tests later." Later never comes;
  bake the golden path in from commit one.
- ❌ Committing a real `.env` with secrets. Ship `.env.example` only.
- ❌ Every repo with different task commands — contributors waste time relearning.

## Try it yourself

- Switch `project_type` to CLI — note the entrypoint + packaging changes.
- Add `conventions: signed commits` — see the pre-commit/CI adjust.
