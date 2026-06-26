# {{TITLE}} — Architecture

> A design/architecture document scaffold for any subsystem, team, or non-trivial
> design. Technology-agnostic: capture the stack in the Tech profile + "Technology
> choices" section, keeping the structure reusable for any technology.

**Status:** Draft | Canonical · **Version:** {{VERSION}} · **Owner:** {{AUTHOR}}
**Last updated:** {{DATE}} · **Implements / depends on:** <link to parent doc>

> **Tech profile** — Technology: {{TECHNOLOGY}} · Language: {{LANGUAGE}} ·
> Stack: {{STACK}} · Toolchain: {{TOOLCHAIN}} · Domain: {{DOMAIN}}

## 0. Decisions locked here

| Decision | Choice | Consequence |
|----------|--------|-------------|
| … | … | … |

## 1. Guiding principles

Principles every choice serves (trace to the parent doc).

## 2. Overview

Big picture + diagram/tree.

## 3. Components

For **each**: why it exists, structure, in/out, ownership.

### 3.1 {{COMPONENT}}
- **Why it exists:** …
- **Structure / In-out / Ownership:** …

## 4. Data / artifact model

Schemas, formats, contracts.

## 5. Technology choices

The **only** place concrete technologies are named, with rationale and the
alternatives rejected. Keeps the rest of the doc reusable.

## 6. Dependency map

Who may depend on whom. Must be acyclic.

## 7. Scale & failure considerations

Behavior under growth/load; how it fails safely.

## 8. The expansion seam

What may change later without fracturing the core (VISION §15).

## Appendix

Glossary, open questions.
