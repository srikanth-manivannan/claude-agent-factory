# Create Your First Skill

> A hands-on tutorial: scaffold, author, validate, and review a real skill. ~15 minutes.
> Companion reference: the [Skill Author Guide](skill-author-guide.md).

We'll build `data/schema-designer` — a skill that designs a database schema.

## Step 0 — Prerequisites

A POSIX shell. *(Optional but recommended for the full gate:* `pip install pyyaml
jsonschema referencing`*.)* See [Getting Started](getting-started.md).

## Step 1 — Create the category (if it doesn't exist)

```sh
sh generators/bin/new-category data "Schema, migrations, query tuning, data modeling."
```

This creates `skills/data/README.md`. Then add a row for the category to
[`TAXONOMY.md`](../../TAXONOMY.md).

## Step 2 — Scaffold the skill

```sh
sh generators/bin/new-skill data schema-designer \
  "Use this to design a normalized, intentional database schema from requirements."
```

You now have `skills/data/schema-designer/` with the canonical **10 files**, all
placeholders pre-filled with your name/description/date and scaffold content to complete.

## Step 3 — Author the contract (`SKILL.md`)

Open `skills/data/schema-designer/SKILL.md` and replace the scaffold placeholders. Aim for:

- **When to use / not use** — concrete triggers.
- **Inputs** — e.g. `requirements`, `access_patterns`.
- **Instructions** — imperative, ordered steps (model entities → normalize → keys →
  indexes → review).
- **Output** — the schema + rationale.
- Keep it **technology-neutral**; the Tech profile carries stack specifics.

> Tip: read [`tradeoff-analyzer/SKILL.md`](../../skills/architecture/tradeoff-analyzer/SKILL.md)
> as a model of depth and structure.

## Step 4 — Fill the docs

- `README.md` — What it does, Quickstart, Inputs/outputs, Limitations, Future improvements.
- `EXAMPLES.md` — at least a happy-path + an edge + an anti-example.
- `TROUBLESHOOTING.md`, `RESOURCES.md` — fill the stubs (cross-link related skills).
- `tests/test-cases.md` — happy / edge / failure cases ([testing standard](../../standards/testing.md)).
- `CHANGELOG.md` — already has your `0.1.0` entry.

The `metadata.yaml` is already schema-valid; only edit `tags`, `tech_profile`, and
(if needed) `dependencies`.

## Step 5 — Validate

```sh
sh scripts/validate
```

Fix any **errors** (missing files, leftover `{{placeholders}}`, schema issues,
`metadata.yaml` ≠ `SKILL.md` frontmatter). **Warnings** about pending references or
missing recommended files are acceptable. Re-run until green.

> Common gotcha: keep `description` **identical** in `SKILL.md` frontmatter and
> `metadata.yaml`, and keep dates **quoted** (`created: "2026-06-26"`).

## Step 6 — Self-review

Run your skill against the checklists:
[Universal Core](../../standards/checklists/_universal.md) +
[documentation-review](../../standards/checklists/documentation-review.md) +
[testing-review](../../standards/checklists/testing-review.md). Record the verdict in
`REVIEW.md`.

## Step 7 — Register & open a PR

- Add a row to [`TAXONOMY.md`](../../TAXONOMY.md).
- Commit, push, open a PR. The [PR template](../../.github/PULL_REQUEST_TEMPLATE.md)
  embeds the checklist; CI re-runs `scripts/validate`.

🎉 **Done!** You authored a gold-standard skill. Repeat for any capability — the
generator + gate make the easy path the correct path.
