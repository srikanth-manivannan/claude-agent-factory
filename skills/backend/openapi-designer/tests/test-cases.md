# Tests & Validation Guidance — OpenAPI Designer

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover
   template placeholders).
3. **Behavior:** run each case below; validate the produced spec against OpenAPI 3.1.

## Behavior cases

### 1 — Happy path
- **Given:** CRUD requirements for a resource + bearer auth.
- **Then:** produces a valid OpenAPI 3.1 spec with reusable schemas, correct status
  codes, security, pagination, and per-operation docs; lint clean.

### 2 — Edge: auth unspecified
- **Given:** no `auth_model`.
- **Then:** flags the gap and proposes a default rather than leaving the API open.

### 3 — Edge: formalize existing API
- **Given:** prose description of an implicit API.
- **Then:** produces a spec and surfaces inconsistencies as lint findings.

### 4 — Failure/refusal: non-REST request
- **Given:** a GraphQL requirement.
- **Then:** declines and points to `graphql-schema-builder`.

### 5 — Correctness: HTTP semantics
- **Given:** create + error operations.
- **Then:** uses 201/204/4xx/5xx appropriately with a shared Error schema.

## Fixtures

Sample requirement sets under `fixtures/`; validate outputs with an OpenAPI validator.
