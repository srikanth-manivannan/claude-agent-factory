# Doc Writer

> Use this to write or refresh a README and docs from code and intent, following the documentation standard.

**Category:** documentation · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Produces GitHub-quality documentation for any subject — code, a skill, or a whole
project — using the exact structure mandated by the
[documentation standard](../../../standards/documentation.md). It writes accurate,
runnable docs (not aspirational marketing), cross-references rather than duplicates,
and refreshes stale docs to match current behavior.

A **foundational primitive**: the `fix-bug`, `build-feature`, and `onboard-to-codebase`
workflows depend on it.

## Quickstart

```text
1. Copy skills/documentation/doc-writer/ into your skills directory.
2. Invoke with the subject (+ audience if not developers).
3. Receive a standards-compliant README (and any requested companion docs).
```

## How it works

Seven steps: identify subject/audience/purpose → apply required structure → runnable
quickstart → accuracy over aspiration → cross-reference → GitHub-readable → verify
links/placeholders. Authoritative procedure in [SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `subject`, optional `audience`, optional `existing_docs`.
- **Outputs:** a complete README (+ companion docs) per the documentation standard.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Audience** — tune tone/depth for end-users vs. contributors.
- **Section set** — add Troubleshooting/Resources blocks for technical artifacts.
- **Pair** with `documentation/doc-linter` to verify completeness.

## Limitations

- Documents what exists; it can't infer intent the code/inputs don't reveal.
- Not an API reference generator (use `api-reference-generator`).

## Related

See [RESOURCES.md](RESOURCES.md). Used by `fix-bug`, `build-feature`,
`onboard-to-codebase` workflows; complements `documentation/doc-linter`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Auto-extract inputs/outputs from code signatures.
- Staleness detection (diff docs vs. code) integrated with `doc-linter`.
- Multi-page docs-site generation.

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
