# Workflows

> Multi-step orchestrations that compose skills + agents into an outcome
> (ARCHITECTURE §6). The full library catalog — 54 workflows across 8 lifecycle
> stages — lives in [`/WORKFLOWS.md`](../WORKFLOWS.md). This folder holds the
> scaffolded workflow artifacts.

## Scaffolded flagships

| Workflow | Stage | Priority |
|----------|-------|----------|
| [build-feature](build-feature/) | Build | P0 |
| [fix-bug](fix-bug/) | Maintain | P0 |
| [review-pr](review-pr/) | Review | P0 |
| [refactor-module](refactor-module/) | Maintain | P0 |
| [security-audit](security-audit/) | Secure | P0 |
| [accessibility-audit](accessibility-audit/) | Review | P1 |
| [performance-optimization](performance-optimization/) | Maintain | P0 |
| [database-migration](database-migration/) | Release | P0 |
| [release-pipeline](release-pipeline/) | Release | P0 |
| [incident-response](incident-response/) | Operate | P0 |

> These reference TAXONOMY skills that are **not built yet** (declared-pending).
> `tests/links/` will pass once the composed skills exist (FACTORY §8/§10). Adding a
> workflow means adding a row to [`/WORKFLOWS.md`](../WORKFLOWS.md) first.

## Contributing a workflow

Use [`templates/workflow/`](../templates/workflow/) (which composes
[`templates/blocks/Workflow.md`](../templates/blocks/Workflow.md)). Every workflow
carries `WORKFLOW.md`, `README.md`, `metadata.yaml`, and `CHANGELOG.md`.
