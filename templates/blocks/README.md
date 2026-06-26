# Reusable Document Blocks

> A library of **standalone, technology-agnostic** document templates. These are
> the canonical prose for each document type; the artifact bundle templates
> (`templates/skill/`, `templates/agent/`, …) **compose** these blocks instead of
> re-inventing them. One source of truth (VISION §6.3, ARCHITECTURE §6).

## Why "technology-agnostic"

A block must work for **any future technology** — a language, framework, cloud,
CLI, protocol, data store, or something that doesn't exist yet. We achieve this by
**never naming a concrete technology** in a block. Instead, blocks use a neutral
**tech-profile placeholder set**, and the consumer fills it in.

### Tech-profile placeholders

| Placeholder | Meaning | Example fill (not in the template) |
|---|---|---|
| `{{TECHNOLOGY}}` | The thing the artifact targets, broadly | "a REST API", "a container runtime" |
| `{{LANGUAGE}}` | Programming/markup language, if any | "Python", "Go", "n/a" |
| `{{STACK}}` | Framework / platform / ecosystem | "React", "Kubernetes", "n/a" |
| `{{TOOLCHAIN}}` | Build/test/run tooling involved | "npm", "make", "n/a" |
| `{{DOMAIN}}` | Problem domain | "testing", "data pipelines" |

Plus the global placeholders from [`../README.md`](../README.md)
(`{{NAME}}`, `{{TITLE}}`, `{{DESCRIPTION}}`, `{{VERSION}}`, …).

### The "Tech profile" header

Document blocks that describe technical behavior begin with a small, optional
**Tech profile** block. Filling it in adapts the whole document to a stack without
editing the body. Leaving every field `n/a` yields a perfectly valid tech-neutral
document. This is the mechanism that lets one template serve all technologies.

```
> **Tech profile** — Technology: {{TECHNOLOGY}} · Language: {{LANGUAGE}} ·
> Stack: {{STACK}} · Toolchain: {{TOOLCHAIN}} · Domain: {{DOMAIN}}
```

## Blocks in this library

| Block | Use for |
|---|---|
| [SKILL.md](SKILL.md) | The skill instruction document |
| [README.block.md](README.block.md) | Human-facing overview of any artifact (copy as `README.md`) |
| [Workflow.md](Workflow.md) | Multi-step orchestration spec |
| [Checklist.md](Checklist.md) | A verifiable quality gate |
| [Metadata.yaml](Metadata.yaml) | Machine metadata (mirrors `_meta/metadata.yaml`) |
| [Examples.md](Examples.md) | A set of worked examples |
| [Prompt.md](Prompt.md) | A reusable prompt building block |
| [Architecture.md](Architecture.md) | A design/architecture document |
| [Implementation.md](Implementation.md) | How to apply a skill (required for skills) |
| [Troubleshooting.md](Troubleshooting.md) | Symptom → cause → fix guidance |
| [Resources.md](Resources.md) | Curated references & further reading |

**Rule:** a leftover `{{PLACEHOLDER}}` is a lint failure. Tech-profile fields may be
set to `n/a`, but the placeholder braces must be gone.
