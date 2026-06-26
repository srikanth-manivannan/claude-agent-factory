# Validation & CI

> How the validation gate works, how to run it, and how it maps to CI. The core
> principle: **`scripts/validate` == CI** — what passes locally passes CI.

## The gate

[`scripts/validate`](../../scripts/validate) runs three layers in order:

| Layer | Script | Runtime | Checks |
|-------|--------|---------|--------|
| Placeholders | [`check-placeholders`](../../scripts/check-placeholders) | pure shell | no leftover `{{...}}` |
| Structure/lint | [`lint`](../../scripts/lint) | pure shell | required files, folder/name match, kebab-case |
| Schema + links | [`factory.py`](../../scripts/lib/factory.py) | Python adapter | JSON-Schema validation, reference resolution, cycle detection |

```sh
sh scripts/validate          # run everything (the gate)
sh scripts/lint              # structure only (no runtime)
sh scripts/check-links       # references only (needs Python)
sh scripts/build-index       # write index.json (needs Python)
```

## Errors vs. warnings

**Errors fail the build (exit 1):**
- missing required files; folder name ≠ `metadata.yaml` name ≠ frontmatter name
- leftover `{{placeholders}}`
- schema violations; `metadata.yaml` disagrees with the spec frontmatter
- **dependency cycles**

**Warnings pass (exit 0):**
- missing *recommended* files (`EXAMPLES.md`, `TROUBLESHOOTING.md`, …)
- **pending references** — a type-valid composition target that isn't built yet. This is
  the intentional "declared-pending" pattern: a workflow may reference a skill before
  that skill exists; the warning becomes resolved automatically once it's built.

## The optional Python adapter

Schema/link/index checks need Python:

```sh
pip install pyyaml jsonschema referencing
```

If Python is **absent**, `scripts/validate` still runs the pure-shell checks and clearly
warns that schema + link validation were skipped — it never silently passes. CI always
installs the adapter, so the full gate runs there.

> **Windows note:** the `python3` command may be a non-functional Microsoft Store stub.
> The scripts probe candidates by actually executing them and will find a working
> `python`. Install Python 3 from python.org if needed.

## Continuous Integration

[`.github/workflows/validate.yml`](../../.github/workflows/validate.yml) runs on every
push and pull request:

1. checkout → set up Python 3.12
2. `pip install pyyaml jsonschema referencing`
3. `sh scripts/validate`
4. `sh scripts/build-index` (sanity check)

A red gate blocks merge (configure it as a required status check). Because the local and
CI commands are identical, you should never be surprised by CI.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `leftover placeholder` | search the artifact for `{{` and fill it (tech-profile may be `n/a`, braces gone) |
| `schema: ... is not of type 'string'` on a date | quote it: `created: "2026-06-26"` |
| `metadata ... != frontmatter` | make `description`/`version`/etc. identical in both |
| `pending reference -> ...` | expected if the target isn't built yet; build it to resolve |
| `dependency cycle` | break the cycle — composition must point down only |
| schema checks skipped | install the Python adapter deps |
