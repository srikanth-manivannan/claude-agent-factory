---
name: openapi-designer
description: Use this to design and lint an OpenAPI specification from requirements before any code is written.
version: 0.1.0
category: backend
runtime: claude
min_standard: 0.1.0
license: MIT
tags: [backend, api, openapi, rest, contract-first]
---

# OpenAPI Designer

> Use this to design and lint an OpenAPI specification from requirements before any code is written.

> **Tech profile** — Technology: REST API · Language: n/a · Stack: OpenAPI 3.1 · Toolchain: any · Domain: backend
> *(Contract-first: produces a portable OpenAPI spec, independent of server language.)*

## When to use this skill

- Designing a new REST API contract-first, before implementation.
- Formalizing an existing/implicit API into a reviewable OpenAPI spec.
- Producing the contract that `backend/rest-endpoint-scaffold` and consumers build against.

## When NOT to use this skill

- GraphQL/gRPC — use `backend/graphql-schema-builder` (or the gRPC equivalent).
- Implementing endpoints — use `backend/rest-endpoint-scaffold`.
- Generating reference docs from a spec — use `documentation/api-reference-generator`.

## Prerequisites

- The API's purpose, its resources, and the operations clients need.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `requirements` | yes | What the API must let clients do |
| `resources` | no | Domain resources/entities, if known |
| `auth_model` | no | Auth scheme (e.g. bearer/OAuth); flagged if unspecified |

## Instructions

1. **Model resources + operations.** Derive resources and their CRUD/actions from the
   requirements; map to REST paths and methods.
2. **Define schemas.** Specify request/response schemas as reusable `components`
   (DRY); include types, required fields, formats, and constraints.
3. **Design status codes + errors.** Use correct HTTP semantics; define a consistent
   error response schema; cover success, client-error, and server-error cases.
4. **Specify auth + security.** Add `securitySchemes` and apply them; if `auth_model`
   is unspecified, flag it (don't leave the API open by omission —
   [/standards/security.md](../../../standards/security.md)).
5. **Add pagination/filtering** for collection endpoints; be consistent across the API.
6. **Lint the spec.** Validate OpenAPI 3.1 correctness; check naming consistency,
   missing descriptions, and unused components.
7. **Document** each operation with a summary + example; produce an example request/response.

## Output

A valid **OpenAPI 3.1** document: paths + operations, reusable component schemas,
consistent error model, security schemes, pagination, and per-operation
descriptions/examples — plus a lint summary. Ready for
`backend/rest-endpoint-scaffold` and `documentation/api-reference-generator`.

## Constraints & safety

- **Correct HTTP semantics** (status codes, idempotency, methods).
- **Security explicit, never implicit** — unspecified auth is flagged.
- **DRY schemas** via `components`; consistent naming
  ([/standards/naming.md](../../../standards/naming.md)).

## Examples

Minimal below; full examples in [EXAMPLES.md](EXAMPLES.md).

**Given:** "Clients manage `tasks` (list, create, get, complete)."
**Produces:** an OpenAPI 3.1 spec with `/tasks` + `/tasks/{id}` operations, a `Task`
component schema, a shared `Error` schema, bearer auth, and paginated list responses.
