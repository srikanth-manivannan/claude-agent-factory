# WORKFLOW LIBRARY

> The canonical catalog of reusable workflows. A workflow is a multi-step
> orchestration that composes skills + agents into an **outcome** (ARCHITECTURE §6,
> VISION §11.2). Workflows draw from `TAXONOMY.md` and roll up into `teams/`. The
> Factory (FACTORY.md) builds these only after their composed skills exist (§8).

**Status:** Canonical · Phase 7 · v0.1.0
**Owner:** Srikanth Manivannan
**Last updated:** 2026-06-25
**Counts:** 8 lifecycle stages · **54 workflows** (≥50 target met) · 10 flagships scaffolded.

---

## 0. How to read this document

- Grouped by **software lifecycle stage** (Plan → Build → Test → Review → Secure →
  Release → Operate → Maintain).
- Each row: **`name`** (the `workflows/<name>/` slug, outcome-based) · what it
  achieves · **composes** (real `category/skill` slugs from TAXONOMY) · **P**riority
  · **depends on** (other workflows, or `—`).
- **Composition points only *down* the ladder** to skills/agents (ARCHITECTURE §17);
  a workflow never depends on a later/heavier workflow except as noted.
- Priority tiers (P0–P3) match TAXONOMY's legend.
- ★ = one of the 10 **flagship workflows scaffolded** as real folders (see §3).

---

## 1. The library (by lifecycle stage)

### A. Plan & Design (7)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| `plan-feature` | Turn a goal into a reviewable, estimated plan | leadership/tech-spec-author, architecture/tradeoff-analyzer, leadership/roadmap-planner | P1 | — |
| `design-system-architecture` | Produce a reviewed architecture + diagrams + ADRs | architecture/system-design-reviewer, architecture/c4-diagram-generator, architecture/adr-author | P1 | — |
| `design-api-contract` | Define an API contract before implementation | architecture/api-contract-designer, backend/openapi-designer | P1 | — |
| `model-data-domain` | Model a domain into schema + entities | database/data-modeler, database/schema-designer | P1 | — |
| `spike-investigation` | Time-boxed technical spike with findings | research/spike-investigator, research/codebase-explorer | P2 | — |
| `competitive-analysis` | Compare approaches/products into a brief | research/competitive-analyzer, research/literature-synthesizer | P2 | — |
| `estimate-and-roadmap` | Build a horizon roadmap with estimates | leadership/roadmap-planner, architecture/tradeoff-analyzer | P2 | `plan-feature` |

### B. Build (8)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| ★ `build-feature` | Spec → implement → test → document → PR | backend/rest-endpoint-scaffold, frontend/component-scaffold, testing/unit-test-generator, documentation/doc-writer | P0 | `plan-feature` |
| `build-rest-api` | Stand up a documented, secured REST API | backend/openapi-designer, backend/rest-endpoint-scaffold, backend/auth-flow-builder | P1 | `design-api-contract` |
| `build-ui-component` | Ship an accessible, tested UI component | frontend/component-scaffold, accessibility/a11y-auditor, frontend/component-test-harness | P1 | — |
| `build-agent` | Build + evaluate a working agent | agentic-ai/agent-scaffold, agentic-ai/tool-definition-builder, agentic-ai/agent-memory-designer, agentic-ai/agent-eval-harness | P0 | — |
| `build-rag-system` | Build + evaluate a RAG pipeline | ai/embedding-indexer, ai/rag-pipeline-builder, ai/llm-eval-harness | P1 | — |
| `build-mcp-server` | Expose tools/resources via an MCP server | agentic-ai/mcp-server-builder, agentic-ai/tool-definition-builder | P1 | — |
| `scaffold-new-service` | Bootstrap a deployable service from zero | backend/service-bootstrapper, devops/ci-pipeline-generator, devops/dockerfile-author | P1 | — |
| `implement-auth` | Add authn + authz with secure defaults | backend/auth-flow-builder, security/authz-policy-designer, security/secure-defaults-advisor | P1 | — |

### C. Test (6)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| `generate-test-suite` | Produce a layered test suite for a unit/module | testing/unit-test-generator, testing/integration-test-builder, testing/test-data-generator | P1 | — |
| `build-e2e-suite` | Build end-to-end test coverage of a flow | testing/e2e-test-builder, testing/test-data-generator | P2 | — |
| `close-coverage-gaps` | Find + fill meaningful coverage gaps | testing/coverage-gap-finder, testing/unit-test-generator | P2 | `generate-test-suite` |
| `evaluate-llm-feature` | Build + run an eval suite for an LLM feature | ai/llm-eval-harness, ai/llm-judge-builder | P1 | — |
| `evaluate-agent` | Measure agent task success + trajectory | agentic-ai/agent-eval-harness, ai/llm-eval-harness, agentic-ai/agent-observability-tracer | P1 | `build-agent` |
| `load-test-system` | Design + run load/perf tests | testing/load-test-designer, testing/test-data-generator, devops/observability-instrumenter | P3 | — |

### D. Review (6)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| ★ `review-pr` | Structured PR review → findings → follow-ups | leadership/code-review-coach, security/dependency-vuln-auditor, documentation/doc-linter | P0 | — |
| `code-review-deep` | Deep correctness + design review of a change | leadership/code-review-coach, architecture/system-design-reviewer | P1 | `review-pr` |
| `architecture-review` | Critique a design against quality attributes | architecture/system-design-reviewer, architecture/tradeoff-analyzer | P2 | — |
| ★ `accessibility-audit` | Audit + remediate UI against WCAG | accessibility/a11y-auditor, accessibility/aria-annotator, accessibility/color-contrast-fixer, accessibility/keyboard-nav-checker | P1 | — |
| `documentation-review` | Check docs for completeness/freshness | documentation/doc-linter, documentation/doc-writer | P2 | — |
| `dependency-audit` | Audit dependencies + supply chain for CVEs, secrets, license risk | security/dependency-vuln-auditor, security/secret-scanner, documentation/doc-writer | P1 | — |

### E. Secure (6)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| ★ `security-audit` | Full security pass: threats, deps, secrets, config | security/threat-modeler, security/dependency-vuln-auditor, security/secret-scanner, security/security-headers-configurer | P0 | — |
| `threat-model-design` | STRIDE threat model on a design | security/threat-modeler, architecture/system-design-reviewer | P1 | — |
| `harden-service` | Apply secure defaults + validation + headers | security/secure-defaults-advisor, security/input-validation-hardener, security/security-headers-configurer | P1 | — |
| `rotate-secrets` | Detect + rotate + vault secrets | security/secret-scanner, security/secrets-management-setup | P2 | — |
| `secure-ai-feature` | Harden an LLM feature against abuse | ai/prompt-injection-defender, security/input-validation-hardener | P1 | — |
| `pentest-prep` | Prepare for an authorized pentest | security/pentest-checklist-runner, security/threat-modeler | P3 | `threat-model-design` |

### F. Release (7)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| ★ `release-pipeline` | Cut → verify → deploy → announce a release | devops/release-automator, documentation/changelog-generator, devops/ci-pipeline-generator, devops/cd-deployment-builder | P0 | — |
| ★ `database-migration` | Plan + apply a safe, reversible migration | database/migration-planner, database/schema-designer, database/migration-writer | P0 | — |
| `deploy-to-production` | Deploy with rollback to production | devops/cd-deployment-builder, devops/k8s-manifest-generator | P1 | `release-pipeline` |
| `containerize-app` | Containerize + orchestrate an app | devops/dockerfile-author, devops/k8s-manifest-generator | P1 | — |
| `provision-infrastructure` | Provision cloud infra via IaC | devops/iac-module-builder, cloud/cloud-resource-provisioner | P1 | — |
| `feature-flag-rollout` | Roll out behind flags with a kill switch | devops/feature-flag-integrator, devops/observability-instrumenter, devops/cd-deployment-builder | P2 | — |
| `mobile-app-release` | Prepare + ship a mobile store release | mobile/app-store-release-prep, documentation/changelog-generator | P3 | `release-pipeline` |

### G. Operate (7)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| ★ `incident-response` | Detect → mitigate → comms → postmortem | devops/incident-runbook-builder, devops/observability-instrumenter, leadership/stakeholder-comms-writer | P0 | — |
| `setup-observability` | Instrument logs/metrics/traces end-to-end | devops/observability-instrumenter, agentic-ai/agent-observability-tracer | P1 | — |
| `optimize-cloud-cost` | Analyze + reduce cloud spend | cloud/cloud-cost-optimizer, cloud/cloud-resource-provisioner, devops/observability-instrumenter | P1 | — |
| `monitor-ai-system` | Monitor cost/quality/safety of an AI system | agentic-ai/agent-observability-tracer, ai/hallucination-checker, agentic-ai/agent-cost-controller | P2 | — |
| `on-call-runbook` | Produce on-call runbooks for a service | devops/incident-runbook-builder, documentation/runbook-writer | P2 | — |
| `disaster-recovery-drill` | Run a DR drill against RTO/RPO | cloud/disaster-recovery-planner, cloud/object-storage-manager, devops/observability-instrumenter | P3 | — |
| `capacity-planning` | Plan capacity from load + growth | testing/load-test-designer, cloud/cloud-cost-optimizer | P3 | `load-test-system` |

### H. Maintain & Improve (7)
| name | achieves | composes | P | depends on |
|------|----------|----------|---|------------|
| ★ `fix-bug` | Reproduce → localize → fix → test → document | research/codebase-explorer, testing/coverage-gap-finder, testing/unit-test-generator, documentation/doc-writer | P0 | — |
| ★ `refactor-module` | Safely refactor under a test safety-net | research/codebase-explorer, testing/test-refactorer, testing/unit-test-generator | P0 | `generate-test-suite` |
| ★ `performance-optimization` | Profile → fix → verify performance | database/query-optimizer, frontend/client-perf-optimizer, database/index-advisor, testing/load-test-designer | P0 | — |
| `upgrade-dependencies` | Upgrade deps safely with test verification | security/dependency-vuln-auditor, testing/unit-test-generator | P1 | — |
| `migrate-skill-standard` | Migrate an artifact to a newer standard | meta/skill-upgrader, meta/skill-validator | P2 | — |
| `onboard-to-codebase` | Get a dev productive in a new repo | research/codebase-explorer, documentation/doc-writer | P2 | — |
| `tech-debt-paydown` | Identify + retire prioritized tech debt | architecture/tradeoff-analyzer, testing/test-refactorer | P2 | — |

---

## 2. Workflows → Playbooks roll-up

> **Hierarchy note (Phase 8.5):** per [`standards/architecture.md`](standards/architecture.md),
> a **Team** is a coordinated collection of *agents* (not workflows); a **Playbook** is
> the top tier that composes *teams + workflows* into a complete outcome. So domain
> bundles of workflows roll up into **playbooks**, while teams group agents.

**Playbooks** (`playbooks/play-<objective>/`) compose teams + workflows. Indicative
mapping (built in a later phase):

| playbook | composes workflows | with team(s) |
|----------|--------------------|--------------|
| `play-ship-backend-service` | design-api-contract, build-rest-api, implement-auth, database-migration | team-backend |
| `play-ship-frontend-app` | build-ui-component, accessibility-audit, performance-optimization | team-frontend |
| `play-zero-to-production` | release-pipeline, deploy-to-production, provision-infrastructure, incident-response | team-platform |
| `play-secure-launch` | security-audit, threat-model-design, harden-service, dependency-audit | team-security |
| `play-ship-ai-feature` | build-rag-system, build-agent, evaluate-llm-feature, secure-ai-feature, monitor-ai-system | team-ai |
| `play-quality-gate` | generate-test-suite, review-pr, fix-bug, refactor-module | team-quality |

> **Teams** (`teams/team-<domain>/`) group the *agents* that staff these playbooks
> (e.g. `team-backend` = the backend agents). Agents are defined in a later phase.

---

## 3. Flagship workflows scaffolded

The 10 workflows you named are scaffolded as real folders under `workflows/`
(WORKFLOW.md + README.md + metadata.yaml + CHANGELOG.md, from `templates/workflow/`):

`build-feature` · `fix-bug` · `review-pr` · `refactor-module` · `security-audit` ·
`accessibility-audit` · `performance-optimization` · `database-migration` ·
`release-pipeline` · `incident-response`.

> These reference TAXONOMY skills by name + min version. The skills are **not built
> yet**, so the references are *declared-pending*: `tests/links/` will pass once the
> composed skills exist (FACTORY §8/§10). This is intentional — the workflows define
> the contract the skills must satisfy.

---

## 4. Recommended build order

Workflows can only be built after their composed skills exist (FACTORY §8). So the
order follows TAXONOMY's skill waves:

1. **After Wave 0–1 skills** → build the **P0 flagships** whose skills are ready:
   `build-feature`, `fix-bug`, `review-pr`, `refactor-module`,
   `performance-optimization`, `database-migration`, `release-pipeline`,
   `incident-response`, `security-audit`, `build-agent`. (The accessibility-audit
   flagship needs the a11y P1 skills — early Wave 2.)
2. **After Wave 2 skills** → P1 workflows across all stages.
3. **After Wave 3 skills** → P2 workflows.
4. **On demand / community** → P3 workflows.
5. **Last** → `teams/` roll-ups, once their member workflows are stable.

### Invariants
- **Every workflow orchestrates ≥2 skills.** A workflow is a *multi-step
  orchestration* by definition (ARCHITECTURE §6); a single-skill "workflow" should
  be a skill instead. Enforced by `tests/links/`.
- **No workflow ships with unresolved composition** (every composed skill exists at
  its declared min version, validated by `tests/links/`).
- **Composition points down only** (ARCHITECTURE §17).
- **Same quality bar** as skills — every workflow passes the Factory loop + gates.

**Next:** Examples (Phase 9) demonstrate these workflows end-to-end; Documentation
(Phase 10) surfaces them. Adding a workflow means adding a row here first.
