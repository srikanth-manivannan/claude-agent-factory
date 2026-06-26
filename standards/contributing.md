# Contributing Standard

> How to contribute an artifact end-to-end. The canonical contribution rules; the
> repo-root `CONTRIBUTING.md` (added in a later phase) will point here.

**Min standard:** 0.1.0 · See also: [review-process.md](review-process.md),
[`/VISION.md`](../VISION.md) §9–§10.

## The flow

1. **Fork & branch.** Never work on the default branch.
2. **Scaffold from a template / the Factory.** Use
   [`/templates/`](../templates/) (or `generators/`) so you inherit the standards by
   construction — don't hand-roll structure.
3. **Build to the standards.** Conform to every doc in [this folder](README.md);
   cross-reference, don't duplicate.
4. **Self-validate.** Run `scripts/validate` locally until 100% green (== CI).
5. **Self-review.** Run the [universal core](checklists/_universal.md) + the relevant
   domain [checklist(s)](checklists/).
6. **Open a PR.** Fill the PR template (it embeds the checklist); attach validation
   output.
7. **Address review.** Resolve 🔴/🟠 findings ([review-process.md](review-process.md)).

## Licensing

All contributions are **MIT**, inbound = outbound (VISION §13). Third-party content
must be license-compatible; record provenance (see the
[Resources block](../templates/blocks/Resources.md)).

## Quality bar

- Acceptance is based on **standards compliance**, not author identity.
- The bar is identical for everyone (VISION §6) — volume never excuses a bad artifact.

## Community

Be excellent and kind; the Code of Conduct (added with the public release) applies.
Decisions are made in the open (VISION §10).

## Adding to the catalog

- A new **skill** → add a row to [`/TAXONOMY.md`](../TAXONOMY.md) first.
- A new **workflow** → add a row to [`/WORKFLOWS.md`](../WORKFLOWS.md) first.
- A new **standard/category** → propose it; it must come with its template, schema,
  and checklist updates together.
