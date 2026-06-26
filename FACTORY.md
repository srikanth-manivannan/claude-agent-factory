# THE AGENT FACTORY

> The core engine of the project: the AI process that generates future skills,
> agents, workflows, and teams — reliably, consistently, and at the quality bar
> VISION demands. A peer document to `VISION.md` and `ARCHITECTURE.md`. Where they
> disagree, VISION wins, then ARCHITECTURE, then this file.

**Status:** Canonical · Phase 5 · v0.1.0
**Owner:** Srikanth Manivannan
**Last updated:** 2026-06-25
**Implements:** VISION (quality bar §6–7, versioning §12, expansion §15) and
ARCHITECTURE (deterministic `generators/` §9, `templates/blocks/` §8, runtime seam §19).

---

## 0. Decisions locked in this phase

| Decision | Choice | Consequence |
|----------|--------|-------------|
| Cognitive architecture | **Hybrid** | One agent runs the loop by default; it **escalates to specialized sub-agents** (e.g. a dedicated Reviewer) only when complexity warrants. Cheap path stays cheap; hard path gets more eyes. |
| Autonomy | **Gated at key checkpoints** | Autonomous *within* stages; **pauses for human approval at two gates** — the Plan gate and the Final-Review gate. |
| Intelligence ↔ tooling | **Agent orchestrates the shell** | Claude does reasoning and authors content; the deterministic shell `generators/bin/` does reproducible file/folder scaffolding. Determinism where reproducibility matters; judgment where it doesn't. |

These build on the Phase 1/2 locked decisions (MIT, Claude-first/expandable, dev-led, `metadata.yaml`, category layout, top-level `teams/` + `agents/`).

---

## 1. What the Factory *is*

The Factory is **not** a code generator that stamps out files. It is a disciplined
**reasoning process** that produces a *correct, documented, tested, standards-passing*
artifact — and a thin **deterministic toolchain** that makes the mechanical parts
reproducible.

```
                       ┌──────────────────────────────────────────┐
                       │            AGENTIC LAYER (Claude)          │
                       │  think → plan → reason → generate →        │
                       │  validate → review   (hybrid: + sub-agents) │
                       └───────────────┬───────────────────────────┘
                                       │ orchestrates (calls, reads results)
                       ┌───────────────▼───────────────────────────┐
                       │       DETERMINISTIC LAYER (shell)          │
                       │  generators/bin/*  · templates/* · scripts/ │
                       │  reproducible scaffolding + validation runs  │
                       └────────────────────────────────────────────┘
```

**Division of labor (the governing principle):**
- **Deterministic layer** owns anything that must be *identical every time*: folder creation, file copying from `templates/`, placeholder substitution, running `scripts/validate`, schema checks. No creativity, no variance.
- **Agentic layer** owns anything requiring *judgment*: understanding the request, designing the skill, writing instructions/docs/tests, interpreting validation output, deciding when to escalate, reviewing.

If a step can be made deterministic, it belongs in the shell. The agent is reserved
for what only intelligence can do.

---

## 2. How it thinks *(cognition)*

The Factory's cognition is governed by a fixed set of **operating beliefs** — the
lens through which every request is processed:

1. **The standard is the boss.** `standards/` and `shared/schemas/` are the source
   of truth. The Factory never invents structure; it conforms.
2. **Templates are the starting point, never the ending point.** A copied template
   is scaffolding; the Factory's job is to fill it with *correct, specific* content.
3. **Reproducibility over cleverness.** Prefer the deterministic path. Reach for
   reasoning only where the shell can't decide.
4. **Quality is gated, not hoped for.** Nothing advances past a gate it hasn't
   passed. "Looks done" is not "is done" (VISION §6.4).
5. **Specificity in the product, neutrality in the factory.** Templates stay
   technology-agnostic (Phase 4); the *generated skill* is concrete and opinionated.
6. **Escalate on uncertainty, not on size.** Complexity and risk — not line count —
   decide whether to pull in a sub-agent.
7. **Leave a trace.** Every decision, gate result, and escalation is recorded so a
   human reviewer can audit *why*, not just *what*.

**The hybrid stance:** the default cognition is a single agent running the full
loop. It self-monitors against an **escalation rubric** (§4.4) and spins up a
specialized sub-agent (Planner, Validator, or Reviewer) only when a trigger fires.

---

## 3. Reasoning process

How the agent moves from a request to a decision at any step. A consistent
reasoning discipline applied throughout the loop:

1. **Ground in the standard.** Before reasoning about content, load the relevant
   `standards/` spec + `shared/schemas/`. The rules frame the problem.
2. **Restate the intent.** Convert the request into an explicit *artifact contract*:
   what it does, its inputs/outputs, its category, its tech profile, what it must
   NOT do.
3. **Search for prior art.** Check the catalog index — does a skill already cover
   this? If so, the right answer may be *extend/compose*, not *create* (avoids
   duplication; honors VISION breadth-with-quality).
4. **Reason from contract to design**, not from blank page to text. Decide the
   shape (standard vs advanced skill; whether it needs scripts/resources) *before*
   writing prose.
5. **Make assumptions explicit.** Anything not given is recorded as a stated
   assumption, surfaced at the Plan gate for human confirmation.
6. **Decide, then justify.** Each non-obvious choice is paired with a one-line
   rationale in the trace.
7. **Check against the operating beliefs (§2).** A choice that violates a belief is
   wrong by construction — revisit it.

> Reasoning is **bounded**: the agent reasons to a *decision and a rationale*, then
> acts. It does not loop indefinitely. Unresolved questions become Plan-gate items,
> not analysis paralysis.

---

## 4. Planning process

Planning is the **first gated stage**. No file is created until the plan is approved.

### 4.1 Inputs to planning
The request, the relevant `standards/`, the catalog index (prior art), and the
target category's conventions.

### 4.2 The plan artifact
The Planner produces a structured **Build Plan** containing:
- **Artifact contract** — name (kebab-case), title, one-sentence description,
  type (skill/agent/workflow/team), category, tech profile.
- **Shape decision** — standard vs advanced; needs `scripts/`? `resources/`?
- **Composition** — which existing skills/agents it will reference (with min
  versions), or "none."
- **Dependency resolution result** (§8) — confirmed, version-pinned, acyclic.
- **Versioning decision** (§9) — new artifact `0.1.0`, or a bump to an existing one.
- **Cross-linking targets** (§10) — what it will link to / be linked from.
- **Test plan** — the behavior cases that will prove it works.
- **Assumptions & open questions** — explicit.
- **Risk/complexity rating** — drives escalation (§4.4).

### 4.3 ⛔ GATE 1 — Plan approval
The Build Plan is surfaced to a human for approval (per the autonomy decision).
Approve / amend / reject. **Nothing is scaffolded before this gate passes.** This is
where assumptions are corrected cheaply, before any content exists.

### 4.4 Escalation rubric (hybrid trigger)
The single agent escalates to a **dedicated Planner sub-agent** when ≥1 trigger fires:
- The artifact composes **3+ other artifacts** or introduces a **new category**.
- It's a **team** or a multi-step **workflow** (inherently higher-order).
- **Security-sensitive or dual-use** behavior is involved (VISION §6.6).
- The request is **ambiguous** after one clarification pass.
- Estimated blast radius touches **shared/** or **standards/**.

Otherwise, the single agent plans inline. (Validator/Reviewer escalation: §6.4.)

---

## 5. Skill generation workflow

The end-to-end loop. Stages are deterministic-or-agentic as marked. Two human
gates (⛔). The same loop generates agents/workflows/teams with the matching
template + spec.

```
 ① INTAKE ───► ② PLAN ──⛔GATE1──► ③ SCAFFOLD ───► ④ AUTHOR ───►
 ⑤ SELF-VALIDATE ───► ⑥ REVIEW ──⛔GATE2──► ⑦ FINALIZE ───► ⑧ HANDOFF
```

| # | Stage | Layer | What happens |
|---|-------|-------|--------------|
| ① | **Intake** | agent | Parse request → artifact contract (§3.2). One clarification pass if needed. |
| ② | **Plan** | agent (±Planner sub-agent) | Produce the Build Plan (§4). Resolve dependencies (§8), versioning (§9), cross-links (§10). |
| | **⛔ GATE 1** | human | Approve/amend the plan. No files exist yet. |
| ③ | **Scaffold** | **shell** | `generators/bin/new-<type>` copies the right `templates/` bundle (composing `templates/blocks/`), creates the folder at the correct path, substitutes the known placeholders. **Reproducible, no judgment.** |
| ④ | **Author** | agent | Fill the scaffold with real content: instructions, README, examples, `tests/`, `metadata.yaml` values, CHANGELOG entry, tech profile. This is the core creative work. |
| ⑤ | **Self-validate** | **shell** + agent | Run `scripts/validate` (structural, schema, links, docs, placeholders). Agent interprets failures and fixes (§3, §11). Loop ③–⑤ until green. |
| ⑥ | **Review** | agent (±Reviewer sub-agent) | Run the review process (§6) against `standards/checklists/`. Produce a Review (Phase 4 review block). |
| | **⛔ GATE 2** | human | Final approval. Approve / request changes (loops to ④) / reject. |
| ⑦ | **Finalize** | shell + agent | Lock versions (§9), finalize CHANGELOG, update the catalog index, wire cross-links (§10). |
| ⑧ | **Handoff** | shell | Open a PR with the Build Plan + Review + validation report attached. CI re-runs the same gates (ARCHITECTURE §13/§18: `scripts/validate == CI`). |

**Invariant:** every artifact that exits stage ⑧ has passed *the exact checks CI
will re-run*. The Factory never produces something it expects CI to reject.

---

## 6. Validation process

Validation is **automated, layered, and deterministic-first**. It answers "does
this conform?" — distinct from review (§7), which answers "is this good?".

### 6.1 The validation layers (all via `scripts/validate`, mirrored by CI)
1. **Structural** — required files present; folder shape matches the type;
   folder name == `name` == frontmatter `name` (ARCHITECTURE §14).
2. **Placeholder** — zero leftover `{{...}}` (tech-profile fields may be `n/a`,
   braces gone). A leftover placeholder is a hard failure.
3. **Schema** — `metadata.yaml` + frontmatter validate against `shared/schemas/`.
4. **Consistency** — `metadata.yaml` agrees with the spec frontmatter.
5. **Cross-reference / links** (§10) — every referenced artifact exists at the
   declared min version; composition points only *down* the ladder; the graph is
   acyclic (ARCHITECTURE §17).
6. **Documentation** — README completeness per `standards/documentation.md`.
7. **Tests present & meaningful** — `tests/` exists and covers the required cases
   (`standards/testing.md`).
8. **Security** — no patterns disallowed by `standards/security.md`; dual-use
   disclosed.

### 6.2 When validation runs
- Continuously during stage ⑤ (the author↔validate loop).
- Again at finalize (⑦).
- Again in CI at handoff (⑧). Three chances; the same logic each time.

### 6.3 Validation is binary
Each check **passes or fails** — no "mostly." The artifact does not advance until
every applicable check is green or explicitly marked N/A with a recorded reason.

---

## 7. Quality gates

The non-negotiable bars between stages. **Two human gates + the automated wall.**

| Gate | Type | Blocks until | Rationale |
|------|------|--------------|-----------|
| **G1 — Plan** | ⛔ human | the Build Plan is approved | Catch wrong direction before any cost (VISION: cheap to change early). |
| **G-Auto — Validation wall** | automated | `scripts/validate` is 100% green | Conformance is mechanical and must not rely on opinion (VISION §7: 100% checklist pass is a release gate). |
| **G2 — Review** | ⛔ human | the Review verdict is Approve | Quality is *earned*, judged by a human against the checklist (VISION §6). |
| **G-CI — Handoff** | automated | CI re-runs all gates green | Defense in depth; "passes locally == passes CI." |

**Gate rules:**
- Gates are **ordered and non-skippable**. You cannot review what hasn't validated;
  you cannot finalize what hasn't been reviewed.
- A failed gate **routes backward** to the responsible stage (§11), never forward.
- Gate outcomes are **recorded in the trace** and attached to the PR.

---

## 8. Dependency resolution

How the Factory wires an artifact to the ones it builds on, safely.

1. **Discover.** From the Build Plan's composition, list intended dependencies
   (skills/agents/workflows by name).
2. **Resolve existence + version.** For each, confirm it exists in the catalog and
   select a **min version** to pin (default: the current released version).
3. **Direction check.** Composition may only point **down** the ladder
   (team→workflow→agent→skill→shared). An upward or sideways reference is rejected
   (ARCHITECTURE §17).
4. **Acyclicity check.** Adding this artifact must not create a cycle in the
   dependency graph. The Factory computes the would-be graph and rejects cycles.
5. **Missing-dependency policy.** If a needed dependency doesn't exist, the Factory
   does **not** silently inline it. It either (a) recommends building that
   dependency first (a separate Factory run) or (b) records it as a Plan-gate
   decision. No hidden copies — single source of truth (ARCHITECTURE §6).
6. **Pin and record.** Approved dependencies are written to `metadata.yaml`
   (`dependencies` / `uses_skills` / `composes`) with `name + min_version`.
7. **Re-validate on change.** `tests/links/` re-checks the whole graph in CI, so a
   later breaking change upstream is caught (§9).

---

## 9. Versioning

The Factory enforces VISION §12's two-layer SemVer; it never versions by feel.

- **New artifact** → starts at **`0.1.0`**, `status: active`, with a CHANGELOG
  "Initial release" entry and a `min_standard` set to the current `standards/`
  version.
- **Modifying an existing artifact** → the Factory classifies the change and bumps:
  - **MAJOR** — breaking change to behavior, inputs, or contract.
  - **MINOR** — backward-compatible new capability.
  - **PATCH** — fix or docs-only.
  The classification is *derived from the diff against the contract*, not guessed,
  and is shown at the Plan gate.
- **Repo-level version** is bumped separately by `scripts/release` (the Factory
  produces artifacts; it does not cut repo releases).
- **Dependency version impact.** If a change is MAJOR, the Factory flags every
  downstream artifact that pins it, so maintainers can plan migrations.
- **Deprecation, not deletion** (VISION §12.3) — superseding an artifact sets the
  old one's `status: deprecated` + `deprecated_by`, kept for ≥1 MINOR cycle.

---

## 10. Cross-linking

The Factory keeps the collection a *connected* web, not a pile of folders.

1. **Outbound links.** In the artifact's docs, link to: its dependencies, its
   category index, the `standards/` it conforms to, and any natural "see also"
   siblings.
2. **Inbound links.** Register the new artifact in its **category README index**
   and the **catalog index** (`scripts/index`), so it is discoverable.
3. **Composition links.** Workflows/teams link to the agents/skills they compose
   (mirroring `metadata.yaml`), and those targets optionally list "used by".
4. **Memory/relationship hygiene.** Links use canonical `name`s; a link to a
   not-yet-existing artifact is allowed only as an explicit Plan-gate action item, never
   silently dangling.
5. **Validation.** `tests/links/` verifies every cross-link resolves to a real,
   correctly-versioned target before handoff (§6.1.5). Broken links fail the gate.

> Cross-linking is what turns "the world's largest collection" from a junk drawer
> into a navigable library (VISION §2).

---

## 11. Error handling

How the Factory behaves when something goes wrong — predictable, recoverable,
auditable.

**Principles:** fail loud, fail backward, never fail silently, never ship broken.

| Failure | Detected at | Response |
|---------|-------------|----------|
| Ambiguous/under-specified request | Intake | One clarification pass; if still unclear → escalate to Plan gate as open question. Never guess silently. |
| Plan rejected | Gate 1 | Return to Intake/Plan with the human's feedback. No scaffolding occurs. |
| Scaffold failure (shell) | Stage ③ | Deterministic error from `generators/bin`; abort cleanly, surface the exact shell error, no partial folder left behind. |
| Validation failure | Stage ⑤ / G-Auto | Route **back to Author (④)**. Agent reads the specific failing check, fixes the *cause* (not the symptom), re-validates. Bounded retry count; if exceeded → escalate to human. |
| Review requests changes | Gate 2 | Route back to Author with the Review's findings (severity-tagged). Re-run from ④. |
| Dependency missing/cyclic | Stage ② / §8 | Reject the plan path; recommend building the dependency first or composing differently. Never inline a hidden copy. |
| CI failure at handoff | Stage ⑧ | Treated as a validation failure that escaped local checks → fix locally so `scripts/validate` catches it next time (closes the gap). |
| Repeated failure / loop | any | Hard stop with a full trace; hand to a human. The Factory does not spin. |

**No-partial-artifact rule:** a run either produces a *complete, gate-passing*
artifact or *nothing merged*. Half-built artifacts never reach `skills/` et al.

**Auditability:** every failure and its resolution is recorded in the run trace and
attached to the PR, so reviewers see how the artifact reached "done."

---

## 12. Future extensibility

How the Factory grows without being rewritten (VISION §15: expansion must never
fracture the core).

1. **New artifact types** — adding a type (e.g. a future `evaluator/`) means adding
   a `templates/<type>/` bundle, a `standards/<type>-spec.md`, a `shared/schemas/`
   entry, and a `generators/bin/new-<type>`. The *loop in §5 is unchanged.* The
   workflow is type-agnostic by design.
2. **New runtimes (multi-model)** — the Factory authors against the **portable skill
   format**, not a model. Supporting another model = adding
   `shared/runtime/<model>/` + a `tests/runtime/` case (ARCHITECTURE §19). The
   Factory's reasoning and gates don't change; only the runtime adapter it targets.
3. **Stronger automation** — deterministic checks can migrate from "agent
   interprets" to "shell decides" over time. The boundary in §1 is *meant* to move
   toward determinism as patterns stabilize. Each migration shrinks the agentic
   surface and increases reproducibility.
4. **Deeper hybrid** — the escalation rubric (§4.4, §6.4) is data-driven; new
   sub-agent roles (e.g. a Security sub-agent, a Docs sub-agent) can be added
   without touching the default single-agent path.
5. **Factory-builds-factory** — because the Factory follows the same standards it
   enforces, its own tooling and sub-agents can be authored *by the Factory*. The
   engine is self-hosting in principle.
6. **Catalog/discovery growth** — `scripts/index` output is the seam for a future
   searchable catalog/marketplace; the Factory already feeds it at finalize (§10).

> **The extensibility invariant:** new capability arrives as *new templates,
> standards, schemas, adapters, or sub-agent roles* — **additively**. If extending
> the Factory requires changing the §5 loop or the §7 gates, that is a design
> failure to be fixed here, not worked around.

---

## Appendix A — The Factory in one paragraph

The Agent Factory is a gated, hybrid reasoning loop that turns a request into a
production-ready artifact: it **thinks** through a fixed set of standard-anchored
beliefs, **plans** a version-pinned, dependency-resolved Build Plan (human-approved
at Gate 1), uses the **deterministic shell** to scaffold from `templates/`,
**authors** real content, **validates** automatically against `shared/schemas/` and
`standards/` until green, **reviews** against the checklist (human-approved at Gate
2), **finalizes** versions and cross-links, and **hands off** a PR that CI re-checks
with the same gates — escalating to specialized sub-agents only when complexity or
risk demands, and never shipping a partial or unvalidated artifact.

## Appendix B — Trace contract (what every run records)

`request → contract → build-plan(+assumptions) → gate1 outcome → scaffold result →
author decisions(+rationales) → validation report → review(+findings) → gate2
outcome → version+links finalized → PR link`. Attached to the PR for audit.

**Next phase:** Phase 6+ implements this engine — the `generators/bin/` scaffolders,
the `standards/` the Factory anchors to, and the `scripts/validate` it runs. Nothing
implemented may contradict this loop or these gates without amending this file.
