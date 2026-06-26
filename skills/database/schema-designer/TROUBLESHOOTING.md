# Troubleshooting — Schema Designer

> Symptom → cause → fix. See [SKILL.md](SKILL.md) and [IMPLEMENTATION.md](IMPLEMENTATION.md).

## Quick diagnostics

- [ ] Are relationships modeled with correct cardinalities (M:N via join table)?
- [ ] Do FKs declare `ON DELETE`/`ON UPDATE` behavior?
- [ ] Is every index justified by an access pattern?
- [ ] Is every denormalization recorded with a rationale?

## Common issues

### Symptom: Data anomalies / duplicated facts
- **Cause:** under-normalized schema.
- **Fix:** normalize to 3NF; one fact in one place; denormalize only deliberately.

### Symptom: Slow reads on the key query
- **Cause:** missing/poorly-ordered index for the access pattern.
- **Fix:** add a composite index (equality cols first, then sort/range); see IMPLEMENTATION.

### Symptom: Writes got slow after "adding indexes to be safe"
- **Cause:** speculative over-indexing.
- **Fix:** drop indexes not serving a stated query; index access patterns only.

### Symptom: Orphaned/cascading-delete surprises
- **Cause:** unspecified or wrong FK delete behavior.
- **Fix:** choose `RESTRICT` vs `CASCADE` deliberately per relationship.

### Symptom: Invalid data slipped in
- **Cause:** invariants enforced only in app code.
- **Fix:** add `CHECK`/`UNIQUE`/`NOT NULL`/enum constraints in the schema.

### Symptom: PII exposure risk
- **Cause:** sensitive columns unmarked / in search indexes/logs.
- **Fix:** flag PII; encrypt at rest; restrict access; keep out of logs.

## Getting more help

- Re-read [SKILL.md](SKILL.md); for application, the `database-migration` workflow.
- Open an issue with requirements + access patterns + the produced DDL.
