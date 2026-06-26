# Implementation Guidance — OpenAPI Designer

> How to apply this skill. See [SKILL.md](SKILL.md) and [/standards/](../../../standards/).

## Build order

1. **Model resources + operations** from requirements → REST paths + methods.
2. **Define reusable component schemas** (DRY); types, required fields, formats.
3. **Design status codes + a consistent error schema** (success / 4xx / 5xx).
4. **Specify security** (`securitySchemes` + apply); flag if auth unspecified.
5. **Add pagination/filtering** for collections; **lint** the spec; document each operation.

## Key decisions

| Decision | Guidance |
|----------|----------|
| Schemas | Reuse via `components`, never inline-duplicate |
| Status codes | 201 create, 204 empty, 4xx/5xx with shared Error |
| Versioning | Path vs header — pick one, be consistent |

## Pitfalls

- ❌ 200 for create/errors → ✅ correct HTTP semantics.
- ❌ Unspecified auth (API open by omission) → ✅ flag + propose a default.
- ❌ Inlined duplicate schemas → ✅ `$ref` components.

## Hand-off

Feeds `backend/rest-endpoint-scaffold` (implementation), `documentation/api-reference-generator`
(docs), `testing/contract-test-builder`, and the `build-rest-api`/`design-api-contract` workflows.
