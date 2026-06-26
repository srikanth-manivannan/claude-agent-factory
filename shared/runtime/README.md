# Runtime Seam

> The pluggable runtime layer — where "what runs an artifact" is isolated from "what an
> artifact is." This is the mechanism that keeps the project **Claude-first but
> expandable** (VISION §15, ARCHITECTURE §19, standards/architecture.md).

## Why this exists

The artifact **format** (SKILL.md, metadata.yaml, schemas) is portable and runtime-
agnostic. The **runtime** — how an artifact is actually executed — lives here, behind a
clean seam. Adding support for another model/runtime later is **additive**: drop in a new
`shared/runtime/<name>/` adapter; **no existing artifact changes**.

Every artifact declares its target runtime via `runtime:` in `metadata.yaml`
(`runtime: claude` today; the schema currently allows `claude`).

## Adapters

| Runtime | Status | Adapter |
|---------|--------|---------|
| `claude` | ✅ active (the only runtime today) | [claude/](claude/) |

## Adding a runtime (future)

1. Create `shared/runtime/<name>/` with an adapter README describing how the portable
   format maps to that runtime.
2. Extend the `runtime` enum in [shared/schemas/metadata.schema.yaml](../schemas/metadata.schema.yaml).
3. Add a `tests/runtime/` case proving each artifact loads under the new runtime.

> **Invariant:** if supporting a new runtime requires changing the skill *format*, that
> is a design failure to fix in ARCHITECTURE — not a reason to fork the format.
