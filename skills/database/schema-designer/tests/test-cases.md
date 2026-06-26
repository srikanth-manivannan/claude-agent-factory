# Tests & Validation Guidance — Schema Designer

> Behavior cases + validation. Conforms to [/standards/testing.md](../../../../standards/testing.md).

## How to validate

1. **Schema:** `metadata.yaml` validates against
   [skill.schema.yaml](../../../../shared/schemas/skill.schema.yaml).
2. **Structure:** `scripts/validate` (folder == name, required files, no leftover placeholders).
3. **Behavior:** run each case; the produced DDL should parse on the target engine.

## Behavior cases

### 1 — Happy path
- **Given:** entities + access patterns + engine.
- **Then:** produces 3NF DDL with keys, FKs (with delete behavior), constraints, an
  access-pattern index, and a rationale.

### 2 — Edge: M:N relationship
- **Given:** two entities with a many-to-many relationship.
- **Then:** produces a join table with a composite PK.

### 3 — Edge: deliberate denormalization
- **Given:** a read-heavy aggregate need.
- **Then:** denormalizes with a recorded read/write trade-off (not silently).

### 4 — Safety: sensitive data
- **Given:** a PII column (e.g. tax_id).
- **Then:** flags it, recommends encryption + access restriction.

### 5 — Discipline: no speculative indexes
- **Given:** columns with no stated access pattern.
- **Then:** does not add indexes for them; indexes map to access patterns only.

### 6 — Integrity in schema
- **Given:** an enum/range invariant.
- **Then:** enforces it with CHECK/constraints, not app code alone.

## Fixtures

Sample requirement + access-pattern sets under `fixtures/`; validate DDL with the engine.
