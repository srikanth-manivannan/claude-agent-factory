# Standards

> The rules every artifact in this repository must satisfy — the single source of
> truth for consistency and quality. Standards are **referenced, never duplicated**:
> templates, the Factory, the checklists, and every future skill point *here* rather
> than restating guidance. Implements VISION §6–§7, §11–§12 and ARCHITECTURE §11.

**Standards version:** see [`VERSION`](VERSION) (`0.1.0`). Artifacts declare the
minimum standard they target via `min_standard` (see [versioning.md](versioning.md)).

---

## How standards are applied (the inheritance model)

A standard is "inherited automatically" by every artifact through three mechanisms,
so contributors never copy rules around:

1. **Templates embed the references.** [`/templates/blocks/`](../templates/blocks/)
   point at these docs instead of restating them — author from a template and you
   inherit the standards by construction.
2. **Schemas enforce the machine-checkable parts.**
   [`/shared/schemas/`](../shared/schemas/) is the formal, validatable form of these
   rules; `scripts/validate` and CI run them.
3. **Checklists gate the judgment parts.** [`checklists/`](checklists/) turn these
   docs into reviewable pass/fail items (run the universal core + the domain review).

> **Rule for authors and standards themselves:** cross-reference, don't duplicate.
> If a rule would appear in two places, it lives in one standard and the other links
> to it.

---

## The standards

| Standard | Defines | Enforced by |
|----------|---------|-------------|
| [naming.md](naming.md) | Names for every artifact, file, category | metadata schema + universal checklist |
| [versioning.md](versioning.md) | Two-layer SemVer, deprecation, `min_standard` | schema + release/maintenance checklists |
| [metadata.md](metadata.md) | The `metadata.yaml` contract (companion to the schemas) | [schemas](../shared/schemas/) |
| [documentation.md](documentation.md) | Required docs per artifact | documentation-review checklist |
| [testing.md](testing.md) | What `tests/` must cover | testing-review checklist |
| [security.md](security.md) | Secure defaults, secrets, dual-use | security-review checklist |
| [accessibility.md](accessibility.md) | WCAG target + a11y rules | accessibility-review checklist |
| [performance.md](performance.md) | Measure-first performance rules | performance-review checklist |
| [architecture.md](architecture.md) | The artifact hierarchy + composition rules | dependency-graph checks |
| [prompt-engineering.md](prompt-engineering.md) | How to write instructions/prompts | review-process |
| [review-process.md](review-process.md) | How reviews + gates work | the Factory (FACTORY.md) |
| [contributing.md](contributing.md) | How to contribute end-to-end | `.github/` intake |

**Also here:** [`checklists/`](checklists/) — the 9 review checklists + universal core
(Phase 8). The machine schemas live in [`/shared/schemas/`](../shared/schemas/).

---

## The artifact hierarchy (at a glance)

Defined fully in [architecture.md](architecture.md):

```
Skill     → a reusable capability
Agent     → an AI specialist that applies one or more skills
Team      → a coordinated collection of agents
Workflow  → a repeatable sequence of engineering activities (composes skills/agents)
Playbook  → a higher-level operating guide composing teams + workflows for a full outcome
```

Each tier has its own schema in [`/shared/schemas/`](../shared/schemas/).

---

## Changing a standard

Standards are versioned (`VERSION`). A change that would break existing artifacts is
a **MAJOR** standards bump and requires a migration note; additive clarifications are
**MINOR**; fixes are **PATCH** (see [versioning.md](versioning.md)). When a standard
changes, its template, schema, and checklist must be updated in the same change —
they are three views of one rule.
