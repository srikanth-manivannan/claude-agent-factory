# Contributing

Thanks for your interest in the **Claude Agent Factory**! Contributions are welcome
under the [MIT License](LICENSE) (inbound = outbound).

**Start here:** the practical [Contributor Guide](docs/guides/contributor-guide.md).
The canonical rules live in [standards/contributing.md](standards/contributing.md).

## 60-second version

```sh
# 1. Scaffold (inherits the standards by construction)
sh generators/bin/new-skill <category> <name> "Use this to ..."
# 2. Fill in the scaffold, conform to /standards/
# 3. Register it: add a row to TAXONOMY.md (skills) or WORKFLOWS.md (workflows)
# 4. Prove it
sh scripts/validate          # this is exactly what CI runs
# 5. Self-review with standards/checklists/, then open a PR
```

## Before you open a PR
- `scripts/validate` is green (errors fail; *pending-reference* and *recommended-file*
  warnings are OK).
- You followed the relevant author guide:
  [skill](docs/guides/skill-author-guide.md) ·
  [agent](docs/guides/agent-author-guide.md) ·
  [workflow](docs/guides/workflow-author-guide.md) ·
  [playbook](docs/guides/playbook-author-guide.md).
- You read the [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting issues
Use the [issue templates](.github/ISSUE_TEMPLATE/). Security issues: see
[SECURITY.md](SECURITY.md) — **do not** open a public issue for vulnerabilities.
