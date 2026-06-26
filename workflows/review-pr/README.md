# Review PR (Workflow)

> Produce a structured, standards-based PR review with severity-tagged findings.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

Reviews a PR across correctness, design, security/deps, and docs, producing a
verdict and actionable, severity-tagged findings.

## The flow

`understand → correctness/design → security/deps → docs/tests → verdict`. See
[WORKFLOW.md](WORKFLOW.md).

## What it composes

- `skill:leadership/code-review-coach` (≥ 0.1.0)
- `skill:security/dependency-vuln-auditor` (≥ 0.1.0)
- `skill:documentation/doc-linter` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** a PR reference / diff.
- **Outputs:** a structured review (verdict + findings + follow-ups).

## Customization

Add `accessibility-audit` for UI PRs or `architecture-review` for large designs.

## Limitations

- Reviews what's in the diff; it is not a substitute for running the change
  (`/verify`-style validation).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
