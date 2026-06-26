# Build Feature (Workflow)

> Take a planned feature from spec to a tested, documented, review-ready PR.

**Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

## What it does

Turns an approved feature plan into shippable code: implement → test → document →
open PR. The default "happy path" for delivering a feature.

## The flow

`confirm spec → implement → test → document → open PR`. See
[WORKFLOW.md](WORKFLOW.md) for the full spec.

## What it composes

- `skill:backend/rest-endpoint-scaffold` (≥ 0.1.0)
- `skill:frontend/component-scaffold` (≥ 0.1.0)
- `skill:testing/unit-test-generator` (≥ 0.1.0)
- `skill:documentation/doc-writer` (≥ 0.1.0)

## Inputs & outputs

- **Inputs:** approved feature spec, target surface (backend/frontend/both).
- **Outputs:** branch + PR with implementation, tests, docs, changelog.

## Customization

Swap the implementation skill for your stack; add an `accessibility/a11y-auditor`
step for user-facing UI.

## Limitations

- Assumes an approved plan exists (`plan-feature`). It does not do product design.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
