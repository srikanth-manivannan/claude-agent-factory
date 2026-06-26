# {{TITLE}} — Architecture

> A design / architecture document scaffold. Use for the repo, a subsystem, a
> team, or any non-trivial design that needs a written, reviewable rationale.
> Mirrors the structure of the project's own ARCHITECTURE.md.

**Status:** Draft | Canonical · **Version:** {{VERSION}} · **Owner:** {{AUTHOR}}
**Last updated:** {{DATE}}
**Implements / depends on:** <link to the doc this must conform to, e.g. VISION.md>

---

## 0. Decisions locked in this document

| Decision | Choice | Consequence |
|----------|--------|-------------|
| … | … | … |

## 1. Guiding principles

The principles every choice below serves (trace them to the parent doc).

1. …

## 2. Overview

The big picture in a few sentences + a diagram/tree if useful.

## 3. Components

For **each** component: **why it exists**, its structure, what's in/out, ownership.

### 3.1 {{COMPONENT}}
- **Why it exists:** …
- **Structure:** …
- **In / out:** …

## 4. Data / artifact model

Schemas, formats, contracts.

## 5. Dependency map

Who may depend on whom. Must be acyclic. Diagram it.

## 6. Scale & failure considerations

How it behaves under growth/load and how it fails safely.

## 7. The expansion seam

What is allowed to change later and how, without fracturing the core
(per VISION §15).

## 8. Alternatives considered

Options weighed and why they were rejected.

## Appendix

Reference tables, glossary, open questions.
