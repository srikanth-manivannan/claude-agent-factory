# OpenAPI Designer

> Use this to design and lint an OpenAPI specification from requirements before any code is written.

**Category:** backend · **Version:** 0.1.0 · **Runtime:** claude · **License:** MIT

[![standard](https://img.shields.io/badge/standard-0.1.0-blue)](../../../standards/README.md)
[![status](https://img.shields.io/badge/status-active-brightgreen)](#version-history)

## What it does

Turns API requirements into a clean, lint-passing **OpenAPI 3.1** contract — paths,
reusable component schemas, a consistent error model, explicit security, and
pagination — *before* a line of server code exists. Contract-first means consumers and
implementers build against one agreed source of truth.

It is a foundational backend skill: `backend/rest-endpoint-scaffold`,
`documentation/api-reference-generator`, and the `build-rest-api` workflow build on its output.

## Quickstart

```text
1. Copy skills/backend/openapi-designer/ into your skills directory.
2. Invoke with the API requirements (+ resources/auth model if known).
3. Receive a validated OpenAPI 3.1 spec + a lint summary.
```

## How it works

Seven steps: model resources/operations → define component schemas → status codes &
errors → security → pagination/filtering → lint → document with examples.
Authoritative procedure in [SKILL.md](SKILL.md).

## Inputs & outputs

- **Inputs:** `requirements`, optional `resources`, optional `auth_model`.
- **Outputs:** a valid OpenAPI 3.1 document + lint summary.

See [EXAMPLES.md](EXAMPLES.md).

## Customization

- **Versioning style** — path vs. header versioning.
- **Error model** — adopt your org's standard error schema.
- **Chain** into `rest-endpoint-scaffold` (implementation) and `api-reference-generator` (docs).

## Limitations

- REST/OpenAPI only (not GraphQL/gRPC).
- Designs the contract; it does not implement endpoints.

## Related

See [RESOURCES.md](RESOURCES.md). Feeds `backend/rest-endpoint-scaffold` and the
`build-rest-api` / `design-api-contract` workflows; pairs with `architecture/api-contract-designer`.

## Validation & review

- **Validation:** [tests/test-cases.md](tests/test-cases.md).
- **Review guidance + self-review:** [REVIEW.md](REVIEW.md).
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Future improvements

- Spec-to-mock-server generation for early consumer testing.
- Breaking-change detection between spec versions.
- Linter rule presets (e.g. Spectral rulesets).

## Version history

See [CHANGELOG.md](CHANGELOG.md). Current: **0.1.0**.
