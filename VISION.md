# VISION

> The foundational document for the project. Every later phase — architecture, repository, templates, standards, factory, skills, workflows, docs, automation, release — must trace back to this file. When in doubt, this document wins.

**Status:** Canonical · Phase 1 · v0.1.0
**Owner:** Chief Architect
**Last updated:** 2026-06-25

---

## 0. How to read this document

This is not a README and not a pitch. It is the **constitution** of the project. It defines *why we exist*, *who we serve*, *what we refuse to compromise on*, and *how the project is allowed to grow*. Sections 1–7 set direction. Sections 8–15 set the operating rules that make the direction durable.

Three decisions are already locked and shape everything below:

1. **License:** MIT — optimized for maximum adoption and forking.
2. **Model scope:** Claude-first, architected to be expandable to other models/agents later.
3. **Primary users:** Both individual developers and enterprise AI teams — **developer-led adoption** as the engine, **enterprise-grade quality** as the standard.

---

## 1. Mission

**To give every developer and AI team a free, production-ready foundation for building reliable agentic software — so that nobody has to reinvent the same Claude Code Skills, agents, and workflows ever again.**

We turn the hard-won, repeatedly-rebuilt patterns of agentic engineering into reusable, forkable, battle-tested building blocks.

---

## 2. Vision

**A world where starting an agentic AI project means forking a proven foundation, not staring at a blank file.**

Within three to five years, when a developer or team sets out to build with Claude Code — or agentic AI more broadly — the default first move is to reach for this ecosystem the way web developers reach for a package registry or a component library today. The collection is large enough to cover the long tail, curated enough to trust blindly, and structured enough that contributions compound instead of collide.

We are building the **standard library for agentic engineering**: the place where the community's best skills, agents, and workflows are gathered, hardened, versioned, and made free.

---

## 3. Goals

Goals are organized by horizon. Each is intended to be measurable (see §7).

### Near-term (0–6 months) — *Foundation*
- Ship a **public, MIT-licensed repository** with a complete architecture, templates, and contribution standards.
- Establish the **Factory** — the meta-tooling and conventions that let anyone produce a compliant, high-quality skill in minutes.
- Publish an initial set of **flagship skills and workflows** that demonstrate the quality bar (set by example, not by promise).
- Make the **first-fork experience** frictionless: a developer can fork, customize, and run a skill in under 10 minutes.

### Mid-term (6–18 months) — *Adoption*
- Become the **most-referenced open collection** of Claude Code Skills by breadth *and* quality.
- Grow a **contributor base** that sustains the quality bar without founder bottleneck.
- Provide **reusable "AI engineering teams"** — composable bundles of agents + skills + workflows that solve whole problem domains.
- Establish **trust signals**: every skill is documented, tested, versioned, and reviewed.

### Long-term (18+ months) — *Standard*
- Be recognized as **the standard library for agentic engineering**.
- Support **expansion beyond Claude** without fracturing the core (per §15).
- Sustain a **governance model** that survives the founders.

---

## 4. Target Users

**Primary axis: developer-led, enterprise-grade.** We win individual developers first because they are the adoption engine; we hold an enterprise quality bar so teams can standardize on us without fear.

### Persona A — The Individual Developer *(adoption engine)*
- **Who:** Solo builders, indie hackers, engineers prototyping agentic features.
- **Needs:** Fork fast, customize freely, see working examples, low ceremony, no lock-in.
- **We win when:** They go from "interesting repo" to "running in my project" in minutes.

### Persona B — The Enterprise AI Team *(quality bar)*
- **Who:** Platform/AI teams building internal agentic systems at companies.
- **Needs:** Standards, governance, security posture, reliability, versioning, auditability, license clarity.
- **We win when:** They adopt our conventions as their internal standard.

### Secondary personas
- **The AI Engineer / Agent Builder** — composes agents and workflows into reusable "teams." Optimizes our composability surface.
- **The Contributor / Maintainer** — extends the collection. Optimizes our templates, standards, and Factory tooling.
- **The Educator / Evaluator** — learns or teaches agentic patterns from our examples.

> **Design tension we accept:** simplicity for Persona A vs. rigor for Persona B. We resolve it by making *the simple path the rigorous path* — templates and the Factory bake in the standards so doing it the easy way is doing it the right way.

---

## 5. Design Philosophy

The taste that shapes every decision:

1. **Fork-first, not framework-first.** People should be able to take one piece and run, without adopting the whole. Loose coupling over grand frameworks.
2. **The easy path is the correct path.** Quality comes from templates and tooling, not from documentation nobody reads.
3. **Convention over configuration.** Predictable structure everywhere. If you've seen one skill, you can navigate them all.
4. **Production-ready means proven.** "Production-ready" is a claim we earn with tests, docs, and review — never a label we self-apply.
5. **Composability is a first-class feature.** Skills compose into agents; agents compose into workflows; workflows compose into "AI engineering teams."
6. **Opinionated core, open edges.** Strong opinions about structure and quality; permissive about what you build with it.
7. **Claude-native today, not Claude-trapped tomorrow.** Build deeply for Claude now; keep the seams clean so expansion later doesn't require a rewrite.
8. **Documentation is part of the product.** An undocumented skill does not exist.

---

## 6. Core Principles

The non-negotiables. These are the constitution; violating one is a release blocker.

1. **Quality over quantity — but pursue both.** We want the *largest* collection, but every item clears the bar. Volume never excuses a bad skill.
2. **Every artifact is self-contained and forkable.** A skill carries everything it needs to be understood and used in isolation.
3. **Consistency is sacred.** Naming, structure, frontmatter, and versioning are uniform across the entire collection.
4. **Nothing ships undocumented and untested.** No exceptions, including flagship/internal items.
5. **Backwards compatibility is a promise, not a courtesy.** Versioning rules (§12) are enforced, not aspirational.
6. **Security and safety are defaults, not features.** Skills must not encourage unsafe patterns; dual-use tooling is documented responsibly.
7. **No vendor lock-in for the user.** MIT, no hidden dependencies, no required SaaS.
8. **Transparency in governance.** Decisions, roadmaps, and standards are public.

---

## 7. Success Metrics

We measure adoption, quality, and community health — not vanity.

### Adoption
- **Forks and clones** (the truest signal for a fork-first project).
- **Time-to-first-working-skill** for a new user (target: < 10 minutes).
- **External references** (projects, articles, talks citing us).

### Quality
- **% of skills that pass the standard checklist** (target: 100% — it's a release gate).
- **Test coverage / validation pass rate** across the collection.
- **Documentation completeness** (every skill has the required docs sections).
- **Defect/regression rate** per release.

### Breadth
- **Number of skills, agents, workflows, and "engineering teams"** — growing, but gated by quality.
- **Category coverage** — how much of the agentic problem space we span.

### Community health
- **Number of active contributors** and **contributor retention**.
- **Median time-to-review** for contributions.
- **Bus factor** — how dependent the project is on any one maintainer (target: trending down).

> A metric only counts if it's published. We report against these openly.

---

## 8. Long-term Roadmap

Horizon-based, not date-locked. Dates are intentions, not commitments.

### NOW — Foundation *(the 12-phase build)*
Vision → Architecture → Repository → Templates → Standards → Factory → Skill Categories → Workflow Library → Examples → Documentation → Automation → GitHub Release. (This document is Phase 1.)

### NEXT — Adoption & depth
- Broaden skill categories to cover the common agentic long tail.
- Mature the Factory into a tool a contributor can run end-to-end.
- Establish "AI engineering teams" as a headline offering.
- Add CI-enforced quality gates and automated validation.

### LATER — Standard & ecosystem
- Discovery surface (searchable index/catalog of skills).
- Multi-model expansion seams (per §15) without fracturing the core.
- Federated/community-curated collections under a shared standard.
- Self-sustaining governance independent of founders.

---

## 9. Open-source Strategy

**License:** MIT (see §13). Maximum permissiveness to maximize forking, embedding, and adoption — directly serving the "world's largest collection" goal.

**Governance model — staged maturity:**

1. **Stage 1 — Benevolent stewardship (now).** A small core team (the Chief Architect + founding maintainers) sets standards and reviews contributions. Speed and a clear quality bar matter most early.
2. **Stage 2 — Maintainer tiers.** As contribution volume grows, introduce *area maintainers* (per category/domain) with merge rights, plus a published *contribution ladder* (contributor → trusted contributor → maintainer).
3. **Stage 3 — Formal governance.** A lightweight steering model with public decision records, so the project survives any individual leaving (driving down bus factor, §7).

**Contribution flow:** Fork → branch → build with the Factory/templates → pass the standards checklist + automated checks → PR → review against the standard → merge. The standards and Factory make most reviews mechanical.

**Quality gating:** Contributions are accepted on *standard compliance*, not on author identity. The bar is public and uniform.

**Sustainability:** MIT keeps the door open for an optional future commercial layer (hosted catalog, premium support, certified collections) **without ever restricting the open core**. We will not retroactively close what we open.

---

## 10. Community Guidelines

The culture, in brief (full `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` come in later phases):

- **Be excellent and be kind.** A welcoming, harassment-free community is a precondition, not a nice-to-have. We adopt a standard Code of Conduct.
- **Quality is a shared responsibility.** Reviewers and contributors both own the bar. Feedback is about the work, never the person.
- **Make it easy to say yes.** Clear templates, clear standards, fast and respectful reviews. We optimize for first-time contributor success.
- **Document as you go.** Every contribution explains itself.
- **Credit generously.** Contributors are acknowledged; "AI engineering teams" and skills carry attribution.
- **Decide in the open.** Significant decisions are discussed and recorded publicly.

---

## 11. Naming Strategy

A naming system, not just a name. Consistency here is a §6 non-negotiable.

### 11.1 Project name — three candidates

The working name is **Claude Agent Factory**. Per the decision to evaluate options, here are three candidates with rationale:

| Candidate | Rationale | Risk |
|-----------|-----------|------|
| **Claude Agent Factory** *(recommended)* | Descriptive and immediately legible: it *produces* agents/skills. "Factory" captures the meta-tooling (the Factory phase) and the production-line quality bar. Strong Claude alignment for a Claude-first project. | "Factory" leans industrial; "Claude" must be used per Anthropic brand guidelines (community project, not official). |
| **Agentry** | Short, brandable, memorable, model-neutral — ages well if we expand beyond Claude (§15). "-ry" evokes a collection/place (like *library*). | Less self-explanatory; needs a tagline to convey purpose. |
| **SkillForge** | Evokes craftsmanship and creation; "forge" is familiar to developers (e.g. code forges). Communicates "where skills are made." | "Forge" is common in dev tooling (possible collision); slightly less tied to the agent/team concept. |

**Recommendation:** Ship as **Claude Agent Factory** for clarity and Claude-first alignment now, while **reserving an agent-neutral brand (e.g., _Agentry_)** as the umbrella for any future multi-model expansion (§15). This lets us be unambiguous today without painting ourselves into a corner.

> Note on trademark: As a community/open-source project, any use of "Claude" follows Anthropic's brand/trademark guidelines and clearly states it is unofficial and community-built.

### 11.2 Naming conventions for artifacts

Uniform across the collection:

- **Skills:** `kebab-case`, verb-or-noun-phrase describing the capability (e.g., `pdf-extract`, `api-scaffold`). Folder name == skill name == frontmatter `name`.
- **Agents:** `kebab-case` role-based names (e.g., `code-reviewer`, `release-manager`).
- **Workflows:** `kebab-case` outcome-based names (e.g., `ship-a-feature`, `triage-incident`).
- **AI Engineering Teams:** `kebab-case` domain names, prefixed `team-` (e.g., `team-backend`, `team-data-pipeline`).
- **Categories:** plural nouns, `kebab-case` (e.g., `documentation`, `testing`, `data`).
- **Descriptions:** every artifact's frontmatter `description` is a single, action-oriented sentence ("Use this to…"), because that's what drives discovery and invocation.

The exact frontmatter schema and folder layout are defined in **Phase 2 (Architecture)** and enforced by **Phase 5 (Standards)** — this section sets the naming *policy* they implement.

---

## 12. Versioning Strategy

Two layers, both SemVer (`MAJOR.MINOR.PATCH`).

### 12.1 Repository / ecosystem version
- The collection as a whole is versioned with SemVer.
- **MAJOR:** breaking changes to the *architecture, standards, or skill format* that require contributors/users to migrate.
- **MINOR:** new skills, agents, workflows, categories, or backward-compatible standard additions.
- **PATCH:** fixes, doc improvements, non-breaking corrections.
- Releases are tagged and accompanied by a `CHANGELOG.md` (Keep a Changelog style).

### 12.2 Per-skill version
- **Every skill carries its own SemVer** in its frontmatter, independent of the repo version.
- **MAJOR:** breaking change to a skill's behavior, inputs, or contract.
- **MINOR:** new capability, backward-compatible.
- **PATCH:** fix or doc update.
- A skill declares the **minimum architecture/standard version** it targets, so compatibility is explicit.

### 12.3 Policy
- **Backwards compatibility is a promise (§6).** Breaking changes require a MAJOR bump and a documented migration note.
- **Deprecation, not deletion.** Items are marked deprecated for at least one MINOR cycle before removal, with a stated replacement.

---

## 13. Licensing Recommendation

**Recommended (and locked): MIT License.**

**Rationale:**
- **Maximum adoption & forking.** MIT imposes the fewest restrictions, directly serving the core goal of becoming the *largest, most-forked* collection.
- **Enterprise-friendly.** Legal teams approve MIT trivially; this removes friction for Persona B.
- **No lock-in (§6).** Users can embed, modify, and redistribute freely, commercially or not.
- **Future optionality.** MIT does not preclude a later optional commercial layer (§9) built *around* the open core.

**Trade-offs considered:**
- *Apache 2.0* offers an explicit patent grant and trademark protection — a stronger enterprise legal posture. It remains a reasonable alternative; we chose MIT for simplicity and ubiquity. (We may add a `NOTICE`/trademark note to cover the "Claude" naming concern without changing the license.)
- *Copyleft (GPL/AGPL)* was rejected: it would suppress the embedding and forking that our adoption strategy depends on.

**Implementation:** `LICENSE` file (MIT) at repo root; SPDX identifier `MIT`; contribution terms clarify that contributions are made under MIT (inbound = outbound). Third-party content must be license-compatible.

---

## 14. Repository Branding

The first impression must signal *trustworthy, production-grade, and easy to start*.

- **Name:** Claude Agent Factory (per §11).
- **Tagline:** *"Build enterprise-grade Claude Code Skills, agentic AI workflows, and reusable AI engineering teams."*
- **One-liner / mission line:** *"The open-source standard library for agentic engineering — fork, customize, extend."*
- **Voice & tone:** Confident, precise, developer-respectful. We show, not tell. No hype words we can't back with tests.
- **Visual direction:** Clean, technical, "engineering-grade." A simple, memorable mark (a stylized factory/forge or modular-blocks motif). Consistent badges (license, version, build/validation status, contributions welcome).
- **README hero:** Tagline → 30-second "what & why" → a *fork-and-run in 3 commands* quickstart → links to categories, the Factory, and contribution guide. The quickstart proves the §3 "under 10 minutes" goal on the front page.
- **Consistency:** Branding (name, tagline, badges, structure) appears identically across README, docs, and per-skill pages — branding is part of the §6 consistency mandate.

---

## 15. Future Expansion Strategy

How the project is *allowed* to grow without breaking what makes it work.

### 15.1 Expansion vectors
1. **Depth:** more skills and categories across the agentic long tail.
2. **Composition:** richer "AI engineering teams" (agents + skills + workflows bundled to solve whole domains).
3. **Tooling:** the Factory grows from conventions into runnable tooling; add a discovery/catalog surface.
4. **Multi-model (the big one):** expand beyond Claude — *Claude-first, expandable* (locked decision).
5. **Ecosystem:** community-curated collections under the shared standard; optional commercial layer around the open core (§9).

### 15.2 The expansion rule (non-negotiable)
**Expansion must never fracture the core.** Concretely:
- Keep a **clean seam between "what a skill is" (the standard/format) and "what runs it" (Claude today, others later).** The format is portable; the runtime is pluggable.
- Multi-model support arrives as an **additive layer**, not a rewrite. If supporting another model requires breaking the skill format, we have designed it wrong (revisit Phase 2).
- A future agent-neutral umbrella brand (e.g., *Agentry*, §11) can sit above "Claude Agent Factory" so Claude-first work and multi-model work coexist.

### 15.3 What we will *not* do
- We will not chase breadth at the cost of the quality bar (§6).
- We will not close the open core (§9).
- We will not couple skills to proprietary infrastructure that creates lock-in (§6).

---

## Appendix — Locked decisions (Phase 1)

| Decision | Choice | Section |
|----------|--------|---------|
| License | MIT | §13 |
| Model scope | Claude-first, expandable | §15 |
| Primary users | Both, developer-led | §4 |
| Project name | Claude Agent Factory (recommended); *Agentry* reserved as neutral umbrella | §11 |

**Next phase:** Phase 2 — Architecture. It must implement the naming policy (§11), versioning (§12), and the expansion seam (§15.2), and define the concrete skill format, repository layout, and conventions. Nothing in Phase 2 may contradict this document without an explicit amendment here.
