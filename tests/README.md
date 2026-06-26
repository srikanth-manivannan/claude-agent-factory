# Tests (collection-wide)

> Global quality gates for the **whole collection** — consistency, schema, links, and
> docs integrity. Per-artifact behavior tests live in each artifact's own `tests/`
> folder. Two tiers, per ARCHITECTURE §14 and [standards/testing.md](../standards/testing.md).

## Two-tier testing model

| Tier | Where | Checks |
|------|-------|--------|
| **Local** | each artifact's `tests/test-cases.md` | behavior: happy / edge / failure |
| **Global** | here + `scripts/` | structure, schema, links, docs, naming |

## How global checks run today

The global tier is implemented by the **validation gate**, not a separate test runner:

```sh
sh scripts/validate      # structural + schema + links + placeholders (== CI)
```

- **structural / naming / placeholders** → [scripts/lint](../scripts/lint),
  [scripts/check-placeholders](../scripts/check-placeholders)
- **schema + reference resolution + cycles** →
  [scripts/check-links](../scripts/check-links) + the Python adapter
  ([scripts/lib/factory.py](../scripts/lib/factory.py))

## Planned subfolders

As the collection grows, dedicated fixtures/harnesses land here:

| Path | Purpose |
|------|---------|
| `structural/` | folder-shape + required-file assertions |
| `schema/` | metadata/frontmatter vs `shared/schemas/` |
| `links/` | cross-reference integrity (down-only, acyclic) |
| `runtime/` | each artifact loads under the active [runtime](../shared/runtime/) |
| `fixtures/` | shared test fixtures |

For now, these checks are covered end-to-end by `scripts/validate`. See
[Validation & CI](../docs/guides/validation-and-ci.md).
