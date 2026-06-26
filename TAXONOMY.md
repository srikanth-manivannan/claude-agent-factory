# SKILL TAXONOMY & BACKLOG

> The canonical map of every skill category and the seed backlog of skill ideas
> for the collection. Implements VISION (breadth *with* quality §6, naming §11) and
> ARCHITECTURE (`skills/<category>/<skill-name>/` §4). The Factory (FACTORY.md)
> consumes this as its build queue, honoring "build dependencies first" (§8).

**Status:** Canonical · Phase 6 · v0.1.0
**Owner:** Chief Architect
**Last updated:** 2026-06-25
**Counts:** 22 categories · **166 seed skills** (≥150 target met).

---

## 0. How to read this document

- Categories are **kebab-case slugs** (the `skills/<category>/` folder name) with a
  one-line **charter** (what belongs here / what doesn't).
- Each skill row: **`name`** (the `skills/<category>/<name>/` slug) · **what it does**
  · **Priority** · **Depends on**.
- Distribution is **value-weighted** (decision): flagship categories get more depth.
- **Dependencies** point only *down/sideways to already-built* skills or shared
  building blocks (ARCHITECTURE §17, FACTORY §8). `—` = no skill dependency.
- The **implementation order** (§4) turns priorities + dependencies into build waves.

### Priority legend
| Tier | Meaning | Scored on |
|------|---------|-----------|
| **P0** | Foundational or flagship — build first; high impact; frequently depended-upon | impact ↑, dependency-readiness ↑ |
| **P1** | High-value core breadth | impact ↑, effort med |
| **P2** | Solid breadth; the long-tail backbone | impact med |
| **P3** | Nice-to-have / specialized long tail | impact niche |

### Distribution summary (value-weighted)
Flagship (most depth): `agentic-ai` (14), `ai` (12), `meta` (10), `devops` (10),
`testing` (10), `backend` (10). Core: `security` (9), `frontend`/`documentation`/`cloud` (8).
Standard: `database`/`automation`/`developer-experience` (7). Focused:
`workflow`/`research`/`architecture` (6). Niche: `knowledge`/`productivity`/
`accessibility`/`mobile` (5), `desktop`/`leadership` (4).

---

## 1. Categories at a glance

| # | Category (slug) | Charter | Seed count | Flagship? |
|---|-----------------|---------|-----------:|:---------:|
| 1 | `architecture` | System/software design, ADRs, modeling, trade-off analysis | 6 | |
| 2 | `backend` | Server-side services, APIs, business logic, integration | 10 | |
| 3 | `frontend` | UI, components, state, client performance | 8 | |
| 4 | `security` | AppSec, secrets, threat modeling, secure defaults | 9 | |
| 5 | `accessibility` | a11y audits, WCAG, inclusive UX | 5 | |
| 6 | `devops` | CI/CD, IaC, release, observability | 10 | ★ |
| 7 | `ai` | LLM app patterns: prompting, RAG, evals, fine-tune prep | 12 | ★ |
| 8 | `agentic-ai` | Agents, tools, multi-agent orchestration, memory | 14 | ★ |
| 9 | `research` | Investigation, synthesis, literature/codebase research | 6 | |
| 10 | `documentation` | Docs generation, API refs, diagrams, changelogs | 8 | |
| 11 | `leadership` | Eng leadership: planning, reviews, decisions, comms | 4 | |
| 12 | `testing` | Unit/integration/e2e, coverage, test data, mutation | 10 | ★ |
| 13 | `cloud` | Cloud-native infra, serverless, cost, multi-cloud | 8 | |
| 14 | `database` | Schema, migrations, query tuning, data modeling | 7 | |
| 15 | `mobile` | iOS/Android/cross-platform app concerns | 5 | |
| 16 | `desktop` | Desktop apps (Electron/native), packaging | 4 | |
| 17 | `automation` | Scripting, scraping, batch, scheduled jobs | 7 | |
| 18 | `developer-experience` | DX: tooling, scaffolds, linters, local env | 7 | |
| 19 | `productivity` | Personal/team output: notes, triage, summaries | 5 | |
| 20 | `knowledge` | Knowledge capture, second brain, retrieval | 5 | |
| 21 | `workflow` | Reusable cross-domain process orchestration | 6 | |
| 22 | `meta` | Skills that build/validate/improve skills (the factory's hands) | 10 | ★ |

---

## 2. The backlog (by category)

### 1. `architecture` (6)
| name | does | P | depends on |
|------|------|---|------------|
| `adr-author` | Draft Architecture Decision Records from a decision + options | P1 | documentation/`doc-writer` |
| `system-design-reviewer` | Critique a design against scalability/failure/cost | P1 | — |
| `tradeoff-analyzer` | Structured weighing of N options against weighted criteria | P1 | — |
| `c4-diagram-generator` | Produce C4 (context/container/component) diagrams as code | P2 | documentation/`diagram-generator` |
| `api-contract-designer` | Design API contracts (REST/GraphQL/gRPC) before code | P2 | backend/`openapi-designer` |
| `migration-planner` | Plan a phased migration (strangler-fig) with rollback | P2 | — |

### 2. `backend` (10)
| name | does | P | depends on |
|------|------|---|------------|
| `rest-endpoint-scaffold` | Scaffold a REST endpoint (handler/validation/tests) | P0 | testing/`unit-test-generator` |
| `openapi-designer` | Author/lint an OpenAPI spec from requirements | P0 | — |
| `auth-flow-builder` | Implement auth (JWT/OAuth/session) with secure defaults | P1 | security/`secure-defaults-advisor` |
| `error-handling-standardizer` | Apply consistent error/exception patterns | P1 | — |
| `graphql-schema-builder` | Design/scaffold a GraphQL schema + resolvers | P1 | backend/`openapi-designer` |
| `background-job-designer` | Add queue/worker job processing with retries | P1 | — |
| `caching-strategy-advisor` | Choose + implement a caching layer/policy | P2 | — |
| `rate-limiter-builder` | Add rate limiting/throttling to an API | P2 | backend/`rest-endpoint-scaffold` |
| `webhook-handler-builder` | Build a verified, idempotent webhook receiver | P2 | security/`secret-scanner` |
| `service-bootstrapper` | Scaffold a new service from a chosen stack | P2 | developer-experience/`project-scaffolder` |

### 3. `frontend` (8)
| name | does | P | depends on |
|------|------|---|------------|
| `component-scaffold` | Generate a UI component (markup/state/tests/story) | P0 | testing/`unit-test-generator` |
| `state-management-advisor` | Recommend + wire a state solution for the app | P1 | — |
| `form-builder` | Build a validated, accessible form | P1 | accessibility/`a11y-auditor` |
| `responsive-layout-helper` | Produce responsive layouts from a spec | P1 | — |
| `client-perf-optimizer` | Diagnose + fix bundle/render performance | P2 | — |
| `design-token-manager` | Define + apply a design-token system | P2 | — |
| `i18n-setup` | Add internationalization scaffolding | P2 | — |
| `component-test-harness` | Set up component/visual testing | P2 | testing/`e2e-test-builder` |

### 4. `security` (9)
| name | does | P | depends on |
|------|------|---|------------|
| `secret-scanner` | Detect committed secrets/keys and remediate | P0 | — |
| `secure-defaults-advisor` | Apply secure-by-default config to a service | P0 | — |
| `threat-modeler` | Run a STRIDE threat model on a design | P1 | architecture/`system-design-reviewer` |
| `dependency-vuln-auditor` | Audit dependencies for known CVEs + fix path | P1 | — |
| `authz-policy-designer` | Design RBAC/ABAC authorization policies | P1 | backend/`auth-flow-builder` |
| `input-validation-hardener` | Add input validation/sanitization across entrypoints | P1 | — |
| `security-headers-configurer` | Set CSP/HSTS/etc. correctly | P2 | — |
| `secrets-management-setup` | Wire a secrets manager/vault | P2 | security/`secret-scanner` |
| `pentest-checklist-runner` | Guided authorized-pentest checklist | P3 | security/`threat-modeler` |

### 5. `accessibility` (5)
| name | does | P | depends on |
|------|------|---|------------|
| `a11y-auditor` | Audit UI against WCAG and report fixes | P0 | — |
| `aria-annotator` | Add correct ARIA roles/labels to markup | P1 | accessibility/`a11y-auditor` |
| `color-contrast-fixer` | Detect + fix contrast failures | P2 | — |
| `keyboard-nav-checker` | Verify/fix keyboard operability | P2 | accessibility/`a11y-auditor` |
| `screen-reader-tester` | Script screen-reader test passes | P3 | accessibility/`a11y-auditor` |

### 6. `devops` (10) ★
| name | does | P | depends on |
|------|------|---|------------|
| `ci-pipeline-generator` | Generate a CI pipeline for the repo's stack | P0 | testing/`unit-test-generator` |
| `dockerfile-author` | Write an optimized, secure multi-stage Dockerfile | P0 | security/`secure-defaults-advisor` |
| `iac-module-builder` | Author IaC (Terraform/Pulumi) modules | P0 | — |
| `release-automator` | Automate semver release + changelog + tag | P0 | documentation/`changelog-generator` |
| `cd-deployment-builder` | Build a CD/deploy workflow (with rollback) | P1 | devops/`ci-pipeline-generator` |
| `observability-instrumenter` | Add logs/metrics/traces to a service | P1 | — |
| `k8s-manifest-generator` | Generate K8s manifests/Helm charts | P1 | devops/`dockerfile-author` |
| `incident-runbook-builder` | Produce an incident response runbook | P2 | documentation/`doc-writer` |
| `feature-flag-integrator` | Add feature-flagging to a codebase | P2 | — |
| `env-config-manager` | Standardize env/config across environments | P2 | — |

### 7. `ai` (12) ★
| name | does | P | depends on |
|------|------|---|------------|
| `prompt-engineer` | Design/refine a production prompt with rationale | P0 | meta/`prompt-pattern-library` |
| `rag-pipeline-builder` | Build a retrieval-augmented generation pipeline | P0 | ai/`embedding-indexer` |
| `llm-eval-harness` | Create an eval suite for an LLM feature | P0 | testing/`test-data-generator` |
| `embedding-indexer` | Chunk + embed + index a corpus for retrieval | P1 | — |
| `structured-output-enforcer` | Enforce JSON/schema-constrained LLM output | P1 | ai/`prompt-engineer` |
| `llm-judge-builder` | Build an LLM-as-judge evaluator | P1 | ai/`llm-eval-harness` |
| `prompt-injection-defender` | Harden prompts against injection | P1 | security/`input-validation-hardener` |
| `model-router` | Route requests across models by cost/quality | P2 | — |
| `token-cost-optimizer` | Reduce token usage/cost of an LLM feature | P2 | — |
| `finetune-dataset-prepper` | Prepare/validate a fine-tuning dataset | P2 | ai/`llm-eval-harness` |
| `semantic-cache-builder` | Add semantic caching to LLM calls | P3 | ai/`embedding-indexer` |
| `hallucination-checker` | Flag/guard unsupported model claims | P3 | ai/`llm-judge-builder` |

### 8. `agentic-ai` (14) ★ *(flagship)*
| name | does | P | depends on |
|------|------|---|------------|
| `agent-scaffold` | Scaffold a single-purpose agent (role/tools/loop) | P0 | ai/`prompt-engineer` |
| `tool-definition-builder` | Define a safe, well-typed tool for an agent | P0 | ai/`structured-output-enforcer` |
| `agent-memory-designer` | Add short/long-term memory to an agent | P0 | ai/`embedding-indexer` |
| `multi-agent-orchestrator` | Coordinate multiple agents on one goal | P0 | agentic-ai/`agent-scaffold` |
| `agent-eval-harness` | Evaluate agent task success + trajectory | P1 | ai/`llm-eval-harness` |
| `planner-executor-builder` | Build a plan→execute→reflect agent loop | P1 | agentic-ai/`agent-scaffold` |
| `human-in-the-loop-gater` | Add approval gates to an agent workflow | P1 | agentic-ai/`agent-scaffold` |
| `agent-guardrails-builder` | Add safety/permission guardrails to an agent | P1 | security/`secure-defaults-advisor` |
| `mcp-server-builder` | Build an MCP server exposing tools/resources | P1 | agentic-ai/`tool-definition-builder` |
| `mcp-client-integrator` | Connect an agent to MCP servers | P2 | agentic-ai/`mcp-server-builder` |
| `agent-observability-tracer` | Trace agent steps/decisions for debugging | P2 | devops/`observability-instrumenter` |
| `retrieval-agent-builder` | Build a RAG-backed answering agent | P2 | ai/`rag-pipeline-builder` |
| `agent-cost-controller` | Budget/limit agent token + tool spend | P2 | ai/`token-cost-optimizer` |
| `agent-handoff-designer` | Design clean handoffs between agents/humans | P3 | agentic-ai/`multi-agent-orchestrator` |

### 9. `research` (6)
| name | does | P | depends on |
|------|------|---|------------|
| `codebase-explorer` | Map an unfamiliar codebase + summarize | P1 | — |
| `literature-synthesizer` | Synthesize sources into a structured brief | P1 | research/`source-evaluator` |
| `source-evaluator` | Assess source credibility/relevance | P2 | — |
| `competitive-analyzer` | Compare products/approaches systematically | P2 | research/`literature-synthesizer` |
| `spike-investigator` | Time-boxed technical spike with findings | P2 | research/`codebase-explorer` |
| `data-gatherer` | Collect + structure data for a question | P3 | automation/`web-scraper` |

### 10. `documentation` (8)
| name | does | P | depends on |
|------|------|---|------------|
| `doc-writer` | Write/refresh README/docs from code + intent | P0 | — |
| `changelog-generator` | Generate a Keep-a-Changelog entry from diffs | P0 | — |
| `api-reference-generator` | Produce API reference docs from a spec/code | P1 | backend/`openapi-designer` |
| `diagram-generator` | Generate diagrams-as-code (mermaid/PlantUML) | P1 | — |
| `docstring-writer` | Add/standardize inline docstrings | P1 | — |
| `tutorial-author` | Write a step-by-step runnable tutorial | P2 | documentation/`doc-writer` |
| `runbook-writer` | Author operational runbooks | P2 | documentation/`doc-writer` |
| `doc-linter` | Check docs for completeness/freshness | P2 | documentation/`doc-writer` |

### 11. `leadership` (4)
| name | does | P | depends on |
|------|------|---|------------|
| `tech-spec-author` | Turn a goal into a reviewable tech spec | P1 | architecture/`tradeoff-analyzer` |
| `code-review-coach` | Produce constructive, standards-based reviews | P1 | — |
| `roadmap-planner` | Build a horizon-based roadmap from goals | P2 | — |
| `stakeholder-comms-writer` | Draft status/decision comms for stakeholders | P2 | — |

### 12. `testing` (10) ★
| name | does | P | depends on |
|------|------|---|------------|
| `unit-test-generator` | Generate unit tests for a unit of code | P0 | — |
| `test-data-generator` | Produce realistic/edge-case test data + fixtures | P0 | — |
| `e2e-test-builder` | Build end-to-end test flows | P1 | testing/`test-data-generator` |
| `integration-test-builder` | Build integration tests across components | P1 | testing/`test-data-generator` |
| `coverage-gap-finder` | Find + fill meaningful coverage gaps | P1 | testing/`unit-test-generator` |
| `test-refactorer` | Improve flaky/slow/brittle tests | P1 | — |
| `contract-test-builder` | Build consumer/provider contract tests | P2 | backend/`openapi-designer` |
| `mutation-test-runner` | Run mutation testing to assess test quality | P2 | testing/`unit-test-generator` |
| `property-test-builder` | Author property-based tests | P2 | testing/`test-data-generator` |
| `load-test-designer` | Design + run load/performance tests | P3 | — |

### 13. `cloud` (8)
| name | does | P | depends on |
|------|------|---|------------|
| `serverless-function-builder` | Scaffold + deploy a serverless function | P1 | devops/`iac-module-builder` |
| `cloud-cost-optimizer` | Analyze + reduce cloud spend | P1 | — |
| `cloud-resource-provisioner` | Provision cloud resources via IaC | P1 | devops/`iac-module-builder` |
| `cdn-configurer` | Configure CDN/edge caching | P2 | — |
| `object-storage-manager` | Set up buckets/lifecycle/access | P2 | security/`secure-defaults-advisor` |
| `multi-cloud-abstractor` | Abstract a workload across providers | P2 | cloud/`cloud-resource-provisioner` |
| `cloud-iam-designer` | Design least-privilege cloud IAM | P2 | security/`authz-policy-designer` |
| `disaster-recovery-planner` | Plan backup/DR with RTO/RPO | P3 | — |

### 14. `database` (7)
| name | does | P | depends on |
|------|------|---|------------|
| `schema-designer` | Design a normalized/intentional schema | P0 | — |
| `migration-writer` | Author safe, reversible migrations | P0 | database/`schema-designer` |
| `query-optimizer` | Diagnose + optimize slow queries | P1 | — |
| `index-advisor` | Recommend/validate indexes | P1 | database/`query-optimizer` |
| `data-modeler` | Model a domain into entities/relations | P1 | architecture/`tradeoff-analyzer` |
| `orm-mapper` | Map a schema to ORM models safely | P2 | database/`schema-designer` |
| `db-seeder` | Generate seed/sample data | P2 | testing/`test-data-generator` |

### 15. `mobile` (5)
| name | does | P | depends on |
|------|------|---|------------|
| `mobile-screen-scaffold` | Scaffold a mobile screen + navigation | P1 | frontend/`component-scaffold` |
| `offline-sync-builder` | Add offline storage + sync | P2 | — |
| `push-notification-setup` | Wire push notifications | P2 | — |
| `mobile-perf-profiler` | Profile + fix mobile performance | P2 | — |
| `app-store-release-prep` | Prepare store metadata/release | P3 | documentation/`changelog-generator` |

### 16. `desktop` (4)
| name | does | P | depends on |
|------|------|---|------------|
| `desktop-app-scaffold` | Scaffold a desktop app (Electron/native) | P1 | frontend/`component-scaffold` |
| `desktop-packager` | Package/sign/distribute a desktop build | P2 | devops/`release-automator` |
| `auto-updater-builder` | Add an auto-update mechanism | P2 | desktop/`desktop-packager` |
| `native-integration-helper` | Bridge to native OS APIs safely | P3 | — |

### 17. `automation` (7)
| name | does | P | depends on |
|------|------|---|------------|
| `script-generator` | Generate a robust CLI/automation script | P0 | — |
| `web-scraper` | Build a resilient, polite web scraper | P1 | automation/`script-generator` |
| `scheduled-job-builder` | Create cron/scheduled jobs with logging | P1 | — |
| `file-batch-processor` | Batch-transform files safely | P1 | automation/`script-generator` |
| `data-pipeline-builder` | Build an ETL/ELT pipeline | P2 | database/`schema-designer` |
| `notification-dispatcher` | Send multi-channel notifications | P2 | — |
| `browser-automation-builder` | Automate browser flows (testing/RPA) | P3 | automation/`web-scraper` |

### 18. `developer-experience` (7)
| name | does | P | depends on |
|------|------|---|------------|
| `project-scaffolder` | Scaffold a new project from a stack profile | P0 | — |
| `linter-formatter-setup` | Configure lint/format/pre-commit | P0 | — |
| `dev-env-bootstrapper` | One-command local dev environment | P1 | developer-experience/`project-scaffolder` |
| `makefile-task-runner` | Standardize task running (make/just) | P1 | — |
| `git-hooks-installer` | Install useful, fast git hooks | P2 | developer-experience/`linter-formatter-setup` |
| `monorepo-organizer` | Structure/maintain a monorepo | P2 | — |
| `codegen-template-builder` | Build project-local code generators | P2 | meta/`skill-scaffolder` |

### 19. `productivity` (5)
| name | does | P | depends on |
|------|------|---|------------|
| `meeting-notes-summarizer` | Turn raw notes into decisions/actions | P1 | — |
| `task-triage-assistant` | Triage + prioritize an inbox/backlog | P1 | — |
| `email-drafter` | Draft clear, on-tone emails | P2 | — |
| `standup-reporter` | Generate standup updates from activity | P2 | — |
| `focus-planner` | Plan a focused work block/day | P3 | — |

### 20. `knowledge` (5)
| name | does | P | depends on |
|------|------|---|------------|
| `note-capturer` | Capture + structure atomic notes | P1 | — |
| `knowledge-base-organizer` | Organize/retrieve a knowledge base | P1 | knowledge/`note-capturer` |
| `glossary-builder` | Build/maintain a domain glossary | P2 | — |
| `faq-generator` | Generate an FAQ from sources/tickets | P2 | research/`literature-synthesizer` |
| `decision-log-keeper` | Maintain a searchable decision log | P3 | architecture/`adr-author` |

### 21. `workflow` (6)
| name | does | P | depends on |
|------|------|---|------------|
| `feature-delivery-workflow` | End-to-end: spec→build→test→docs→PR | P0 | testing/`unit-test-generator`, documentation/`doc-writer` |
| `bug-triage-workflow` | Reproduce→localize→fix→test→document | P1 | testing/`coverage-gap-finder` |
| `code-review-workflow` | Structured review→findings→follow-ups | P1 | leadership/`code-review-coach` |
| `incident-response-workflow` | Detect→mitigate→postmortem | P2 | devops/`incident-runbook-builder` |
| `release-workflow` | Cut→verify→announce a release | P2 | devops/`release-automator` |
| `onboarding-workflow` | Get a dev productive in a new repo | P3 | research/`codebase-explorer` |

### 22. `meta` (10) ★ *(the factory's hands)*
| name | does | P | depends on |
|------|------|---|------------|
| `skill-scaffolder` | Drive the Factory to scaffold a new skill | P0 | — |
| `skill-validator` | Run the validation wall on an artifact | P0 | meta/`skill-scaffolder` |
| `prompt-pattern-library` | Reusable prompt patterns/building blocks | P0 | — |
| `skill-reviewer` | Review an artifact against the checklist | P0 | meta/`skill-validator` |
| `metadata-linter` | Lint `metadata.yaml`/frontmatter vs schema | P1 | meta/`skill-validator` |
| `dependency-graph-checker` | Verify acyclic, down-pointing references | P1 | — |
| `catalog-indexer` | Build the discovery index from metadata | P1 | meta/`metadata-linter` |
| `skill-upgrader` | Migrate a skill to a newer standard version | P2 | meta/`skill-validator` |
| `skill-deprecator` | Deprecate + redirect a superseded skill | P2 | meta/`catalog-indexer` |
| `skill-composer` | Compose skills into an agent/workflow/team | P2 | agentic-ai/`agent-scaffold` |

---

## 3. Dependency principles

1. **Foundational primitives first.** A handful of skills are depended-upon by many:
   `testing/unit-test-generator`, `testing/test-data-generator`,
   `documentation/doc-writer`, `documentation/changelog-generator`,
   `security/secure-defaults-advisor`, `ai/prompt-engineer`,
   `ai/embedding-indexer`, `developer-experience/project-scaffolder`, and the entire
   `meta/*` P0 set. These are the **roots** of the dependency graph.
2. **The `meta/*` P0 set is special** — `skill-scaffolder`, `skill-validator`,
   `skill-reviewer`, `prompt-pattern-library` are the *operational arms of the
   Factory*. They make every later skill cheaper and safer to build, so they lead
   Wave 1.
3. **Dependencies point down/sideways to already-built skills only** (ARCHITECTURE
   §17). No skill in an earlier wave may depend on a later one.
4. **`ai` underpins `agentic-ai`.** Agentic skills depend on `ai` primitives
   (`prompt-engineer`, `embedding-indexer`, `structured-output-enforcer`), so `ai`
   leads `agentic-ai` within each wave.
5. **Cross-category links are allowed** but must respect readiness — e.g.
   `backend/auth-flow-builder` → `security/secure-defaults-advisor` means security's
   P0 ships first.

---

## 4. Recommended implementation order (waves)

Waves are ordered by **dependency-readiness, then priority**. A skill enters a wave
only once its dependencies are satisfied by an earlier wave. (Repo plumbing —
templates, standards, the Factory — is Phases 1–5/7+, prerequisite to all waves.)

### Wave 0 — Factory roots *(unblock everything)*
The dependency-free primitives the rest of the backlog needs.
`meta`: skill-scaffolder, skill-validator, prompt-pattern-library, skill-reviewer ·
`testing`: unit-test-generator, test-data-generator ·
`documentation`: doc-writer, changelog-generator ·
`security`: secret-scanner, secure-defaults-advisor ·
`developer-experience`: project-scaffolder, linter-formatter-setup ·
`ai`: embedding-indexer · `database`: schema-designer · `automation`: script-generator ·
`architecture`: tradeoff-analyzer.
→ **All P0, all dependency-free.** Build first.

### Wave 1 — Flagship P0 *(the showcase)*
The high-impact, now-unblocked P0 skills that define the collection's identity.
`ai`: prompt-engineer, rag-pipeline-builder, llm-eval-harness ·
`agentic-ai`: agent-scaffold, tool-definition-builder, agent-memory-designer,
multi-agent-orchestrator ·
`devops`: ci-pipeline-generator, dockerfile-author, iac-module-builder, release-automator ·
`backend`: rest-endpoint-scaffold, openapi-designer ·
`frontend`: component-scaffold · `accessibility`: a11y-auditor ·
`database`: migration-writer · `workflow`: feature-delivery-workflow ·
`meta`: (graph-checker, catalog-indexer, metadata-linter pulled forward to support scale).

### Wave 2 — P1 core breadth
All remaining **P1** skills across every category (auth-flow-builder,
threat-modeler, e2e/integration test builders, observability-instrumenter,
agent-eval-harness, structured-output-enforcer, api-reference-generator,
schema/query/index database skills, cloud provisioning, research primitives,
leadership specs, etc.). Build category-by-category, primitives-before-dependents.

### Wave 3 — P2 long-tail backbone
All **P2** skills — the breadth that makes us "the largest collection," each still
clearing the quality bar. Parallelizable across categories since most P2 depend only
on Wave 0–1 primitives.

### Wave 4 — P3 specialized
**P3** niche/specialized skills (semantic-cache-builder, hallucination-checker,
pentest-checklist-runner, app-store-release-prep, browser-automation-builder,
focus-planner, etc.). Built on demand / by community contribution.

### Ordering invariants
- **No forward dependencies:** a wave never depends on a later wave (FACTORY §8).
- **Primitives before dependents** *within* a wave.
- **Quality gate is constant:** every skill in every wave passes the full Factory
  loop and validation wall — waves change *order*, never the *bar* (VISION §6).

---

## Appendix — Counts by priority
| Tier | Count (approx) | Where they cluster |
|------|---------------:|--------------------|
| P0 | ~28 | meta, testing, devops, ai, agentic-ai, backend, security, db, dx, docs |
| P1 | ~58 | broad — every category's core |
| P2 | ~62 | broad — the long-tail backbone |
| P3 | ~18 | niche/specialized |

**Next phase:** the Workflow Library (Phase 8 in the roadmap) composes these skills
into the `workflow/` and `teams/` artifacts. This taxonomy is the build queue the
Factory draws from; adding a skill means adding a row here first.
