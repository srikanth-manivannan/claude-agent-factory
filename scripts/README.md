# Scripts

> Repo maintenance & the validation gate. POSIX-shell entrypoints (the canonical
> interface, ARCHITECTURE §9). The basic path (structure, naming, placeholders) needs
> **no runtime**; schema + link validation and index building use an optional **Python
> adapter** ([lib/factory.py](lib/factory.py)) and degrade gracefully if Python is absent.

## Commands

| Script | Does | Runtime |
|--------|------|---------|
| [`validate`](validate) | The full gate: placeholders → lint → schema + links. **`scripts/validate == CI`.** | shell (+ Python for schema/links) |
| [`lint`](lint) | Structure, required files, folder/name match, kebab-case | pure shell |
| [`check-placeholders`](check-placeholders) | Fail on any leftover `{{PLACEHOLDER}}` | pure shell |
| [`check-links`](check-links) | Reference resolution + cycle detection | Python adapter |
| [`build-index`](build-index) | Emit `index.json` catalog from every `metadata.yaml` | Python adapter |

## Usage

```sh
sh scripts/validate          # run the whole gate (what CI runs)
sh scripts/lint              # structure only (no runtime)
sh scripts/check-placeholders
sh scripts/check-links       # needs Python
sh scripts/build-index       # writes ./index.json
```

## Exit codes & severity

- **Errors fail** (exit 1): missing required files, bad naming, leftover placeholders,
  schema violations, metadata↔frontmatter mismatch, **dependency cycles**.
- **Warnings pass** (exit 0): missing *recommended* files, and **pending references**
  — a type-valid composition target that isn't built yet (the "declared-pending"
  pattern; see [/standards/architecture.md](../standards/architecture.md)).

## The Python adapter

[lib/factory.py](lib/factory.py) implements `validate`, `links`, and `index`. It needs
`pyyaml` (+ `jsonschema referencing` for the schema step):

```sh
pip install pyyaml jsonschema referencing
```

If Python is missing, `validate` still runs the pure-shell checks and clearly warns
that schema + link validation were skipped. CI installs the adapter so the full gate
always runs there.
