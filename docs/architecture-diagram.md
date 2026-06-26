# Architecture Diagrams

> Visual companion to [ARCHITECTURE.md](../ARCHITECTURE.md) and
> [standards/architecture.md](../standards/architecture.md). Mermaid renders natively on
> GitHub; ASCII fallbacks are included for plain-text viewers.

## 1. The artifact hierarchy (5 tiers)

```mermaid
graph TD
    P[Playbook<br/><i>complete engineering outcome</i>]
    T[Team<br/><i>collection of agents</i>]
    W[Workflow<br/><i>sequence of activities, ≥2 skills</i>]
    A[Agent<br/><i>AI specialist</i>]
    S[Skill<br/><i>reusable capability</i>]
    SH[(shared/)]

    P -->|composes| T
    P -->|composes| W
    T -->|composes| A
    W -->|composes| S
    W -.->|optional| A
    A -->|applies| S
    S -->|opt-in| SH

    classDef top fill:#1f2937,stroke:#111,color:#fff;
    classDef mid fill:#374151,stroke:#111,color:#fff;
    classDef leaf fill:#2563eb,stroke:#111,color:#fff;
    class P top; class T,W mid; class A,S leaf;
```

**Rule:** composition points **down** only; the graph is acyclic (enforced by
`scripts/check-links`).

ASCII fallback:
```
Playbook ── composes ──▶ Team ── composes ──▶ Agent ── applies ──▶ Skill ─▶ shared/
   └─────── composes ──▶ Workflow ──▶ Skill (≥2) [+ Agent] ───────────────▶
```

## 2. Repository structure

```mermaid
graph LR
    subgraph Product["The framework (the product)"]
        STD[standards/]
        SCH[shared/schemas/]
        TPL[templates/]
        GEN[generators/]
        SCR[scripts/]
    end
    subgraph Collection["The collection (generated)"]
        SK[skills/]
        WF[workflows/]
        AG[agents/]
        TM[teams/]
        PB[playbooks/]
    end
    DOCS[docs/] --- Product
    GEN -->|scaffold from| TPL
    GEN -->|create| SK & WF & AG & TM & PB
    SCR -->|validate against| SCH & STD
    SK & WF & AG & TM & PB -->|conform to| STD
```

## 3. The authoring + validation loop

```mermaid
flowchart LR
    idea([Idea]) --> gen[generators/bin/new-*]
    gen --> author[Fill in scaffold<br/>conform to standards/]
    author --> val{{scripts/validate}}
    val -- errors --> author
    val -- green --> review[Self-review<br/>standards/checklists/]
    review --> pr[Open PR]
    pr --> ci{{CI: scripts/validate}}
    ci -- green --> merge([Merge])
    ci -- red --> author
```

`scripts/validate == CI` — the same gate runs locally and in CI, so "passes locally"
means "passes CI."

## 4. Validation pipeline (what `scripts/validate` runs)

```
check-placeholders  (pure shell)  ─┐
lint                (pure shell)   ├─▶ PASS/FAIL
schema + links      (Python adapter, graceful degrade) ─┘
                    │
   errors → fail (missing files, bad naming, placeholders,
                  schema violations, metadata≠frontmatter, cycles)
   warnings → pass (missing recommended files, pending references)
```
