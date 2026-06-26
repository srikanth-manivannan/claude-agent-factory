# Resources — OpenAPI Designer

> References and cross-links, grouped by purpose.

## Internal references

- **Spec:** [SKILL.md](SKILL.md).
- **Standards:** [security](../../../standards/security.md),
  [naming](../../../standards/naming.md),
  [documentation](../../../standards/documentation.md),
  [testing](../../../standards/testing.md),
  [architecture](../../../standards/architecture.md).
- **Schema:** [/shared/schemas/skill.schema.yaml](../../../shared/schemas/skill.schema.yaml).

## Cross-linked artifacts (the hierarchy)

| Relation | Artifact | How they connect |
|----------|----------|------------------|
| **Feeds** | `backend/rest-endpoint-scaffold` *(planned)* | implements the contract |
| **Feeds** | `documentation/api-reference-generator` *(planned)* | generates reference docs |
| **Pairs with** | `architecture/api-contract-designer` *(planned)* | higher-level contract design |
| **Used by workflow** | `build-rest-api`, `design-api-contract` ([/WORKFLOWS.md](../../../WORKFLOWS.md)) | contract step |

## Concepts & background (vendor-neutral)

- **Contract-first / API-first** design.
- **OpenAPI 3.1**; reusable **components**; consistent **error models**.
- **REST semantics** (status codes, idempotency, pagination).

## Provenance & credits

- Method synthesized from OpenAPI 3.1 and standard API-design practice. No third-party
  content copied; MIT (VISION §13).
