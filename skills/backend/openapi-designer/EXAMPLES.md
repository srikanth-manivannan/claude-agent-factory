# Examples — OpenAPI Designer

> Worked examples. Output is OpenAPI 3.1, independent of server language. See [SKILL.md](SKILL.md).

## Example 1 — Tasks API (happy path)

**Input:** "Clients can list, create, get, and complete `tasks`." Auth = bearer token.

**Produces (sketch):**
```yaml
openapi: 3.1.0
paths:
  /tasks:
    get:    { summary: List tasks, parameters: [page, per_page], responses: { '200': {...} } }
    post:   { summary: Create task, requestBody: {...}, responses: { '201': {...}, '400': {...} } }
  /tasks/{id}:
    get:    { responses: { '200': {...}, '404': {...} } }
  /tasks/{id}/complete:
    post:   { responses: { '200': {...}, '404': {...}, '409': {...} } }
components:
  schemas:
    Task:  { type: object, required: [id, title, status], properties: {...} }
    Error: { type: object, required: [code, message], properties: {...} }
  securitySchemes:
    bearerAuth: { type: http, scheme: bearer }
security: [ { bearerAuth: [] } ]
```
Plus a lint summary (no errors; all operations documented).

## Example 2 — Edge: auth unspecified

**Input:** requirements omit auth.

**Behavior:** designs the spec but **flags** "no auth model specified — endpoints would
be unauthenticated" and proposes a default (bearer), rather than silently leaving the
API open.

## Example 3 — Edge: formalizing an existing API

**Input:** an implicit/undocumented API described in prose.

**Behavior:** reverse-models resources into a spec, surfaces inconsistencies (mixed
status codes, ad-hoc error shapes) as lint findings to fix.

## Anti-example

- ❌ Returning `200` for a creation (should be `201`) or for errors. Correct HTTP
  semantics are required.
- ❌ Inlining the same object schema in five places instead of a reusable `component`.

## Try it yourself

- Add a `DELETE /tasks/{id}` — note the `204`/`404` responses generated.
- Switch `auth_model` to OAuth2 — see `securitySchemes` change.
