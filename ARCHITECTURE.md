# ARCHITECTURE

> The canonical structural specification for the repository. It **implements** `VISION.md` — specifically the naming policy (§11), two-layer versioning (§12), and the Claude-first/pluggable expansion seam (§15.2). Where this document and VISION disagree, VISION wins and this file is a bug.

**Status:** Canonical · Phase 2 · v0.1.0
**Owner:** Chief Architect
**Last updated:** 2026-06-25
**Designed for:** thousands of concurrent contributors.

---

## 0. Design decisions locked in this phase

| Decision | Choice | Consequence |
|----------|--------|-------------|
| Tooling stack | **Language-agnostic + POSIX shell** | Minimal dependency footprint; widest contributor reach; skills stay language-neutral; tooling is portable, optionally extended by per-language *adapters*. |
| `skills/` layout | **By category subfolders** | `skills/<category>/<skill-name>/` — governable per-category at scale, clean CODEOWNERS, predictable navigation. |
| AI engineering teams | **Promoted to top-level `teams/`** | Teams are a headline offering (VISION §3), so they get first-class placement instead of being buried in workflows. |

These join the Phase 1 locked decisions (MIT, Claude-first/expandable, dev-led, name = Claude Agent Factory / *Agentry* reserved).

---

## 1. Guiding architectural principles

Every structural choice below serves these, derived from VISION §5–§6:

1. **Convention over configuration.** If you've seen one skill, you can navigate them all. Structure is predictable everywhere.
2. **Locality of change.** A contributor touching one skill should edit exactly one folder. PRs don't collide. This is how thousands of contributors coexist.
3. **Format vs. runtime separation.** *What an artifact is* (portable spec) is decoupled from *what runs it* (Claude today, pluggable later). The seam lives in `shared/` and `standards/`.
4. **Self-containment.** Every skill, agent, workflow, and team carries everything needed to be understood and used in isolation (VISION §6.2).
5. **The easy path is the correct path.** `templates/` + `generators/` bake the standards in, so the lazy way is the compliant way.
6. **Tooling is portable.** No required language runtime. Shell + declarative config is the floor; language adapters are optional add-ons.
7. **Acyclic dependencies.** Directories form a one-way dependency graph (see §17). No cycles, ever.

---

## 2. Top-level repository tree

```
claude-agent-factory/
├── .claude/            # Claude Code harness config for THIS repo (contributor experience)
├── skills/             # The collection. Skills grouped by category.            ← the product
├── agents/             # Reusable agent definitions (roles) that skills/workflows use
├── workflows/          # Repeatable sequences of engineering activities (skills + agents)
├── teams/              # Coordinated collections of agents                      ← headline
├── playbooks/          # Operating guides composing teams + workflows (top tier) ← headline
├── templates/          # Blank, standards-compliant scaffolds for every artifact type
├── generators/         # The Factory: tooling that produces compliant artifacts from templates
├── shared/             # Cross-cutting reusable assets (schemas, runtime adapters, libs)
├── standards/          # The rules: specs, schemas-of-record, checklists, conventions
├── examples/           # Worked, runnable demonstrations (not part of the catalog)
├── docs/               # Human documentation (the product's manual + governance)
├── scripts/            # Repo maintenance & dev-loop commands (lint, validate, release)
├── tests/              # Validation & quality gates for the whole collection
├── ci/                 # CI pipeline definitions and reusable CI logic
├── .github/            # GitHub-native config: PR/issue templates, CODEOWNERS, workflows
│
├── VISION.md           # Phase 1 — the constitution
├── ARCHITECTURE.md     # Phase 2 — this file
├── README.md           # Branding hero + quickstart (Phase 3+)
├── CONTRIBUTING.md      # How to contribute (Phase 5/10)
├── CODE_OF_CONDUCT.md  # Community guidelines (Phase 5/10)
├── CHANGELOG.md        # Keep-a-Changelog, repo-level SemVer (VISION §12.1)
├── LICENSE             # MIT (VISION §13)
└── VERSION             # Repo-level SemVer single source of truth
```

> **Naming note:** the three dirs you didn't list explicitly — `agents/` — is required by the composition model (skills compose into agents compose into workflows compose into teams). It is added here as architecturally necessary, not as scope creep. All other top-level dirs match your specification, plus the promoted `teams/`.

---

## 3. `.claude/` — Harness configuration for this repository

**Why it exists:** This repo is itself a Claude Code project that thousands of people will open in Claude Code. `.claude/` makes *contributing* a first-class, guided experience — the Factory tools are reachable as slash commands, and the harness is pre-configured so a contributor's first session "just works." It is meta: Claude Code config for the repo that produces Claude Code skills.

**Structure:**
```
.claude/
├── settings.json          # Shared, committed harness settings (permissions, env) for contributors
├── settings.local.json    # (gitignored) per-contributor overrides — never committed
├── commands/              # Repo-specific slash commands wrapping the Factory
│   ├── new-skill.md       #   /new-skill  → drives generators/ to scaffold a skill
│   ├── validate.md        #   /validate   → runs tests/ + standards checks on the diff
│   └── new-team.md        #   /new-team   → scaffolds a teams/ bundle
├── hooks/                 # Hook scripts (e.g. pre-PR validation reminder) — shell, portable
└── README.md             # Explains the contributor harness setup
```

**In / out:** In — contributor-facing harness config and command wrappers. Out — anything that ships to *users* of a forked skill (that belongs in the skill folder itself).

---

## 4. `skills/` — The collection *(the product)*

**Why it exists:** This *is* the project. Everything else exists to produce, validate, document, and compose what lives here.

**Layout — by category (locked):**
```
skills/
├── <category>/                 # e.g. testing, documentation, data, devops, code-quality …
│   ├── <skill-name>/           # one folder == one skill (folder name == frontmatter name)
│   │   ├── SKILL.md            # REQUIRED. Frontmatter + instructions (the skill itself)
│   │   ├── README.md           # REQUIRED. Human docs: what/why/usage/examples
│   │   ├── metadata.yaml            # REQUIRED. Machine metadata: version, category, deps, runtime
│   │   ├── scripts/            # OPTIONAL. Helper scripts the skill invokes (language-neutral)
│   │   ├── resources/          # OPTIONAL. Static assets, references, prompt fragments
│   │   ├── tests/              # REQUIRED. Skill-local validation fixtures + checks
│   │   └── CHANGELOG.md        # REQUIRED. Per-skill SemVer history (VISION §12.2)
│   └── README.md               # Category overview + index of its skills
└── README.md                   # Catalog root: category map + contribution pointer
```

**The skill format (the spec VISION deferred to Phase 2):**

`SKILL.md` frontmatter (YAML) — the portable contract:
```yaml
---
name: <kebab-case>            # MUST equal the folder name (VISION §11.2)
description: <one sentence>   # action-oriented, "Use this to…" — drives discovery/invocation
version: <semver>            # per-skill SemVer (VISION §12.2)
category: <category>         # MUST equal the parent category folder
runtime: claude              # the runtime seam — "claude" today; pluggable later (§15.2)
min_standard: <semver>       # minimum standards/ version this skill targets
license: MIT
tags: [..]                   # discovery aids
---
```

**Why each required file:** `SKILL.md` = the artifact; `README.md` = "undocumented = doesn't exist" (VISION §6.4); `metadata.yaml` = machine-readable so `tests/`, `generators/`, and any future catalog can index without parsing prose; `tests/` = "untested = doesn't ship" (VISION §6.4); per-skill `CHANGELOG.md` = enforces two-layer versioning.

**In / out:** In — only finished, standards-passing skills. Out — experiments (→ `examples/`), orchestration (→ `workflows/`), and reusable cross-skill assets (→ `shared/`).

**Scale property:** every skill is an island. A PR adding `skills/testing/api-mock/` touches no other skill's files, so thousands of contributors never collide. Category subfolders map cleanly to CODEOWNERS (§16).

---

## 5. `agents/` — Reusable agent definitions

**Why it exists:** The composition hierarchy is *Skill → Agent → Team / Workflow → Playbook* (canonical: [`standards/architecture.md`](standards/architecture.md)). Agents are reusable *roles* (e.g. `code-reviewer`, `release-manager`) that wield skills. Without a home, agents would be duplicated inside every team and workflow. Centralizing them keeps roles single-sourced.

> **Hierarchy update (Phase 8.5):** the original "skills→agents→workflows→teams" ladder was refined into five tiers. **Team** = a coordinated collection of agents; **Workflow** = a sequence of activities (composes skills/agents); **Playbook** = the new top tier composing teams + workflows. The authoritative definition + composition rules live in [`standards/architecture.md`](standards/architecture.md); this document describes the folders that host them.

**Structure:**
```
agents/
├── <agent-name>/
│   ├── AGENT.md          # Role definition, responsibilities, which skills it uses, frontmatter
│   ├── README.md         # Human docs
│   ├── metadata.yaml          # version, used-skills, runtime
│   └── CHANGELOG.md
└── README.md
```

**In / out:** In — reusable roles referenced by ≥1 workflow/team. Out — one-off agent logic that belongs inside a single workflow.

---

## 6. `workflows/` — Multi-step orchestrations

**Why it exists:** Real work is multi-step. Workflows compose skills and agents into an outcome (VISION §11.2: outcome-based names like `ship-a-feature`). They are the orchestration layer below "teams."

**Structure:**
```
workflows/
├── <workflow-name>/
│   ├── WORKFLOW.md       # Steps, the skills/agents it sequences, inputs/outputs, frontmatter
│   ├── README.md
│   ├── metadata.yaml          # version, referenced skills+agents, runtime
│   └── CHANGELOG.md
└── README.md
```

**Composition rule:** a workflow *references* skills/agents by name + min-version (it does not copy them). This keeps single-source-of-truth and makes dependency validation possible (`tests/`).

---

## 7. `teams/` — AI engineering teams *(headline, promoted to top-level)*

**Why it exists:** VISION §3 names "reusable AI engineering teams" as a headline offering. A team is the top tier of composition: a curated bundle of agents + skills + workflows that solves a *whole domain* (e.g. `team-backend`, `team-data-pipeline`). Promoting it to top-level signals its importance and gives it room to grow.

**Structure:**
```
teams/
├── team-<domain>/
│   ├── TEAM.md           # The team's charter: which agents/workflows/skills, how they coordinate
│   ├── README.md         # What domain it solves + how to deploy the team
│   ├── metadata.yaml          # version, composed agents/workflows/skills (by name+version), runtime
│   ├── workflows/        # OPTIONAL team-specific orchestrations not reused elsewhere
│   └── CHANGELOG.md
└── README.md
```

**Composition rule:** teams reference reusable agents/skills/workflows from their canonical homes; team-local-only orchestration may live inside the team folder. A team is the *only* artifact allowed to contain its own private workflows, because that's its purpose.

---

## 8. `templates/` — Standards-compliant scaffolds

**Why it exists:** "The easy path is the correct path" (VISION §5.2). A template is a blank, *already-compliant* artifact. Contributors (and `generators/`) copy a template and fill it in, so compliance is the default, not an afterthought.

**Structure:**
```
templates/
├── skill/         # mirror of the skill folder spec (§4), with fill-in placeholders
├── agent/
├── workflow/
├── team/
├── category/      # scaffold for introducing a NEW category (README + folder conventions)
├── example/
└── README.md      # which template to use when + how placeholders work
```

**Invariant:** templates must always satisfy the current `standards/`. A standards change that breaks a template is incomplete until templates are updated. CI enforces this (§13/§14).

---

## 9. `generators/` — The Factory

**Why it exists:** This is the "Factory" of Claude Agent Factory (VISION roadmap Phase 6). It turns the *manual* template-copy into *tooling*: answer a few prompts, get a compliant artifact. Language-agnostic by decision — implemented as portable shell driving declarative config, with optional per-language adapters.

**Structure:**
```
generators/
├── bin/                # Portable shell entrypoints (no required runtime)
│   ├── new-skill       #   scaffolds skills/<category>/<name>/ from templates/skill/
│   ├── new-agent
│   ├── new-workflow
│   ├── new-team
│   └── new-category
├── lib/                # Shared shell functions (prompting, templating, slug validation)
├── config/             # Declarative generation config (placeholder maps, prompts) — YAML/JSON
├── adapters/           # OPTIONAL language adapters (e.g. python/, node/) for richer generation
│                       #   The shell path always works without these.
└── README.md
```

**Why language-agnostic:** maximizes contributor reach (VISION §4 dev-led) and avoids forcing a runtime on people who just want to write a skill. Adapters are additive, never required — same philosophy as the runtime seam (§15.2).

**Relationship:** `generators/` consume `templates/`, enforce `standards/`, and are wrapped by `.claude/commands/`.

---

## 10. `shared/` — Cross-cutting reusable assets *(the seam)*

**Why it exists:** Two needs: (1) genuinely shared assets used across many skills (common prompt fragments, reference data), and (2) the **runtime seam** that keeps the project Claude-first but expandable (VISION §15.2). This is where "what runs a skill" is abstracted.

**Structure:**
```
shared/
├── schemas/            # The schemas-of-record for frontmatter/metadata.yaml (machine-validated)
│                       #   referenced by standards/ and enforced by tests/
├── runtime/            # The pluggable runtime seam
│   ├── claude/         #   Claude adapter (the only one today)
│   └── README.md       #   how to add a new runtime WITHOUT changing the skill format
├── lib/                # Reusable, language-neutral helpers shared by skills (opt-in)
├── prompts/            # Reusable prompt fragments / building blocks
└── README.md
```

**Why the seam lives here:** keeping `runtime/` separate from the skill format means adding a model later is *additive* — drop in `shared/runtime/<model>/`, no skill rewrites (VISION §15.2 non-negotiable). Schemas live here (not in `standards/`) because they're *consumed* by tooling; `standards/` *documents* and points to them.

---

## 11. `standards/` — The rules *(the enforceable spec)*

**Why it exists:** Consistency is sacred (VISION §6.3) and quality is gated, not hoped for (VISION §7). `standards/` is the single source of truth for *the rules every artifact must satisfy* — the human-readable spec plus the checklists CI and reviewers run against.

**Structure:**
```
standards/
├── skill-spec.md           # The full skill format spec (canonical prose for §4)
├── agent-spec.md
├── workflow-spec.md
├── team-spec.md
├── naming.md               # Implements VISION §11.2 naming conventions
├── versioning.md           # Implements VISION §12 (repo + per-skill SemVer, deprecation)
├── documentation.md        # What every README must contain
├── testing.md              # What every artifact's tests/ must cover
├── security.md             # Safe-by-default rules; dual-use disclosure (VISION §6.6)
├── checklists/             # The release gates — machine-checkable where possible
│   ├── skill-checklist.md
│   ├── pr-checklist.md
│   └── …
├── VERSION                 # standards SemVer (skills declare min_standard against this)
└── README.md
```

**Relationship to `shared/schemas/`:** `standards/` is the *law* (human-readable + checklists); `shared/schemas/` is the *machine-enforceable subset*. They must agree; CI verifies it.

---

## 12. `examples/` — Worked, runnable demonstrations

**Why it exists:** Examples teach and prove (VISION §4 educator persona; §7 time-to-first-skill). They are explicitly **not** part of the catalog — they may take shortcuts a real skill may not, and they're free to demonstrate *composition* end-to-end.

**Structure:**
```
examples/
├── using-a-skill/          # minimal: fork one skill, run it
├── composing-a-workflow/   # skills+agents → workflow
├── deploying-a-team/       # a full team in action
├── authoring-a-skill/      # the Factory loop, start to finish
└── README.md
```

**In / out:** In — demonstrations and tutorials. Out — anything meant to be forked as a dependency (that's a real skill/workflow/team).

---

## 13. `scripts/` — Repo maintenance & dev loop

**Why it exists:** The day-to-day commands that keep the repo healthy, separate from CI definitions (`ci/`) and from artifact generation (`generators/`). Portable shell by decision.

**Structure:**
```
scripts/
├── validate            # run all standards + schema checks locally (mirrors CI)
├── lint                # structural lint (folder shape, frontmatter presence, naming)
├── test                # run tests/ across the collection
├── release             # cut a repo release: bump VERSION, update CHANGELOG, tag
├── new-version         # bump a single artifact's SemVer + changelog
├── index               # (re)build the catalog index from metadata.yaml files
├── lib/                # shared shell helpers for the above
└── README.md
```

**Principle:** `scripts/validate` and CI must run the *same* logic so "passes locally" means "passes CI" (VISION: easy path = correct path).

---

## 14. `tests/` — Quality gates for the whole collection

**Why it exists:** "Nothing ships untested" (VISION §6.4) and "100% pass the checklist" is a release gate (VISION §7). This holds *collection-wide* validation; per-artifact fixtures live in each artifact's own `tests/`.

**Structure:**
```
tests/
├── structural/         # folder shape, required files present, naming matches frontmatter
├── schema/             # validate frontmatter + metadata.yaml against shared/schemas/
├── links/              # cross-reference integrity (workflows/teams point to real, versioned artifacts)
├── docs/               # README completeness per standards/documentation.md
├── runtime/            # the active runtime adapter loads/validates each artifact
├── fixtures/           # shared test fixtures
└── README.md
```

**Two-tier testing model:** *local* tests live in each skill/agent/workflow/team `tests/` (behavior); *global* tests live here (consistency, integrity, schema). CI runs both.

---

## 15. `ci/` — Pipeline definitions & reusable CI logic

**Why it exists:** Separates *what the pipeline does* (`ci/`, reusable, host-neutral) from *where GitHub wires it up* (`.github/workflows/`). This keeps CI logic portable if the project ever moves hosts and avoids dumping shell into YAML.

**Structure:**
```
ci/
├── pipelines/          # logical pipeline stages (validate → test → docs → release)
├── actions/            # reusable composite steps invoked by .github/workflows/
├── config/             # CI configuration (matrix, thresholds, quality gates)
└── README.md
```

**Relationship:** `.github/workflows/*.yml` are thin and call into `ci/` and `scripts/`. The real logic lives in `scripts/` + `ci/`, so it's runnable locally and host-portable.

---

## 16. `.github/` — GitHub-native contributor surface

**Why it exists:** At thousands of contributors, the *intake* must be automated and self-explanatory. This is where contribution is shaped, routed, and reviewed.

**Structure:**
```
.github/
├── workflows/              # thin YAML entrypoints → ci/ + scripts/
│   ├── validate.yml        #   on PR: structural + schema + docs + link checks
│   ├── test.yml            #   on PR: run collection + artifact tests
│   └── release.yml         #   on tag: build index, publish release
├── ISSUE_TEMPLATE/
│   ├── new-skill-request.yml
│   ├── bug-report.yml
│   └── …
├── PULL_REQUEST_TEMPLATE.md   # embeds the standards/checklists/pr-checklist.md
├── CODEOWNERS                 # per-category & per-area ownership → routes reviews
├── labeler.yml                # auto-label PRs by touched category/area
└── FUNDING.yml                # (optional) sustainability (VISION §9)
```

**Scale property — CODEOWNERS by category:** because `skills/` is split by category (§4), `CODEOWNERS` can assign `skills/testing/**` to the testing maintainers, etc. This is the structural mechanism behind VISION §9's "area maintainers" governance stage — architecture enabling governance.

---

## 17. Directory dependency map (acyclic)

Who is allowed to depend on whom. Arrows = "may reference / depend on." No cycles.

```
standards/  ─────────────┐  (the law; depends on nothing)
shared/schemas/ ◄────────┘  (machine form of the law)
        ▲
        │ enforce
templates/ ──► standards/ , shared/
generators/ ──► templates/ , standards/ , shared/
        ▲
.claude/commands ──► generators/ , scripts/

skills/   ──► shared/ (opt-in) , standards/ (conform)
agents/   ──► skills/ , shared/
teams/    ──► agents/ , shared/
workflows/──► skills/ (≥2) , agents/ , shared/
playbooks/──► teams/ , workflows/ , shared/
examples/ ──► (any of the above; depends-down only, never depended-upon)

tests/    ──► everything (validates it)         [test-only, no runtime dep]
scripts/  ──► tests/ , standards/ , shared/
ci/       ──► scripts/ , tests/
.github/  ──► ci/ , scripts/ , standards/
```

**Rules enforced by `tests/links/`:**
- Composition only points *down* the hierarchy (playbook→{team,workflow}→{agent}→skill→shared). Never up. See [`standards/architecture.md`](standards/architecture.md).
- No artifact depends on `examples/`.
- Every reference includes a name **and** a min-version (VISION §12).

---

## 18. How the scale goal is met ("thousands of contributors")

Concrete structural mechanisms, not aspirations:

1. **One-folder-per-artifact + category split** → PRs are isolated; merge conflicts are near-impossible between different skills.
2. **CODEOWNERS per category** → reviews auto-route to the right maintainers (enables VISION §9 maintainer tiers).
3. **Templates + generators** → contributions arrive already-compliant, making review mechanical.
4. **`standards/` + `shared/schemas/`** → a single, machine-checkable source of truth; "is this acceptable?" is answered by CI, not opinion.
5. **`scripts/validate` == CI** → contributors self-verify before opening a PR; less reviewer load.
6. **Acyclic dependency map** → the codebase can't rot into spaghetti as it grows.
7. **Self-contained artifacts** → onboarding to one skill never requires understanding the whole repo.

---

## 19. The expansion seam (VISION §15.2 implemented)

- **Skill format is portable:** `SKILL.md` frontmatter carries `runtime:` and `min_standard:` but no model-specific coupling in the *format*.
- **Runtime is pluggable:** all model-specific behavior is isolated in `shared/runtime/<model>/`. Today only `shared/runtime/claude/` exists.
- **Adding a model is additive:** create `shared/runtime/<new>/`, add a `tests/runtime/` case — **zero changes to existing skills**. If a new model ever *requires* changing the skill format, that's a Phase 2 design failure to be fixed here, per the VISION non-negotiable.
- **Brand seam:** the future agent-neutral umbrella (*Agentry*, VISION §11) maps to this same separation — Claude-first work and multi-model work share one format, different runtimes.

---

## Appendix — Required-file matrix

| Artifact | Spec file | README | metadata.yaml | tests/ | CHANGELOG |
|----------|-----------|--------|----------|--------|-----------|
| skill    | `SKILL.md` | ✅ | ✅ | ✅ | ✅ |
| agent    | `AGENT.md` | ✅ | ✅ | ✅ (recommended) | ✅ |
| workflow | `WORKFLOW.md` | ✅ | ✅ | ✅ (recommended) | ✅ |
| team     | `TEAM.md` | ✅ | ✅ | ✅ (recommended) | ✅ |

**Next phase:** Phase 3 — Repository. It materializes this tree as actual directories with README stubs and root files (LICENSE, VERSION, CHANGELOG, README hero), implementing — not redesigning — what this document specifies. Nothing in Phase 3 may deviate from this architecture without amending this file.
