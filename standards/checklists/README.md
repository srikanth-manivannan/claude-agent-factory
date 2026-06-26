# Engineering Review Checklists

> Reusable, technology-agnostic review gates **shared across all skills, workflows,
> and teams**. Derived from `templates/blocks/Checklist.md`. They implement the
> quality bar from VISION §6–7 and are consumed by the Factory's review stage
> (FACTORY §6–7) and CI (ARCHITECTURE §11/§16).

## How these work

Every review runs **two layers** (per the universal+domain decision):

1. **[Universal Core](_universal.md)** — the items *every* artifact must pass
   (structure, naming, required files, metadata, versioning, links, validation).
   Run this first, always.
2. **The domain checklist** for what you're reviewing (architecture, security, …).

A reviewer (or the Factory's Reviewer) records a verdict; CI runs every `[auto]`
item automatically.

## Item annotations

Each item is **objectively verifiable** and carries:

| Marker | Meaning |
|--------|---------|
| `[auto]` | Machine-checkable — enforced by `scripts/validate` / CI |
| `[manual]` | Requires human (or agent) judgment |
| 🔴 blocker | Must pass — fails the gate; cannot merge/ship |
| 🟠 major | Should pass — fix before merge unless explicitly waived |
| 🟡 minor | Nice to fix — track as follow-up if deferred |

**Verdict rule:** any unresolved 🔴 = **request changes**. Open 🟠 = **approve with
changes**. Only 🟡 remaining = **approve**. Every item is checked or marked **N/A
with a reason**.

## The checklists

| Checklist | Reviews | Backs workflow |
|-----------|---------|----------------|
| [_universal.md](_universal.md) | Any artifact (always run) | — |
| [architecture-review.md](architecture-review.md) | System/software design | `architecture-review` |
| [security-review.md](security-review.md) | AppSec posture | `security-audit` |
| [accessibility-review.md](accessibility-review.md) | a11y / WCAG | `accessibility-audit` |
| [performance-review.md](performance-review.md) | Performance | `performance-optimization` |
| [testing-review.md](testing-review.md) | Test quality | `generate-test-suite` |
| [documentation-review.md](documentation-review.md) | Docs completeness | `documentation-review` |
| [release-review.md](release-review.md) | Release readiness | `release-pipeline` |
| [deployment-review.md](deployment-review.md) | Deploy safety | `deploy-to-production` |
| [maintenance-review.md](maintenance-review.md) | Long-term health | `refactor-module`, `tech-debt-paydown` |

> These reference other `standards/` docs (`naming.md`, `versioning.md`,
> `documentation.md`, `testing.md`, `security.md`) and `shared/schemas/` that are
> authored in the broader Standards phase. The checklists define what those
> standards must make true.
