# Examples — Tradeoff Analyzer

> Worked examples. Technology framing comes from the inputs, so the same method
> serves any decision. See [SKILL.md](SKILL.md) for the procedure.

## Example 1 — Datastore choice (happy path)

**Inputs**
- Decision: "Which datastore for the events service?"
- Options: PostgreSQL, DynamoDB
- Constraints: must stay within current cloud; team is SQL-strong.
- Criteria/weights: operational-cost 20%, query-flexibility 30%,
  team-familiarity 20%, scalability 30%.

**Scoring matrix (1–5)**

| Criterion (weight) | PostgreSQL | DynamoDB |
|--------------------|:----------:|:--------:|
| operational-cost (20%) | 4 | 3 |
| query-flexibility (30%) | 5 | 2 |
| team-familiarity (20%) | 5 | 2 |
| scalability (30%) | 3 | 5 |
| **Weighted total** | **4.1** | **3.2** |

**Recommendation:** PostgreSQL (margin **0.9**). Top reasons: query flexibility and
team familiarity. **Primary risk:** scalability ceiling under extreme write load.
**Sensitivity:** if scalability weight rises from 30% → 50%, the result narrows but
does not flip — *robust*.

**Assumptions:** event volume stays < 10k writes/s; no multi-region requirement yet.

## Example 2 — Weight-sensitive (close call)

**Inputs:** Decision = "REST vs gRPC for the internal API"; equal-ish priorities.

| Criterion (weight) | REST | gRPC |
|--------------------|:----:|:----:|
| developer-familiarity (30%) | 5 | 3 |
| performance (30%) | 3 | 5 |
| tooling-ecosystem (20%) | 5 | 4 |
| streaming-support (20%) | 2 | 5 |
| **Weighted total** | **3.7** | **4.2** |

**Recommendation:** gRPC (margin **0.5**) — **but flagged weight-sensitive**: if
`developer-familiarity` rises to 40%, REST wins. Decision should be escalated with
the sensitivity made explicit, not auto-decided.

## Example 3 — Edge: an option eliminated by a hard constraint

**Inputs:** Decision = "Auth provider"; Options = [Vendor A, Vendor B, build-in-house];
hard constraint = "SOC 2 required at launch."

- **build-in-house** is eliminated at step 2 (cannot achieve SOC 2 by launch) — recorded,
  not silently dropped.
- Remaining two are scored normally.

**Why it's instructive:** shows constraints are applied *before* scoring, and that
eliminations are always justified in the output.

## Anti-example (what NOT to do)

- ❌ Inventing scores to make a preferred option win. The method requires a one-line
  evidence justification per score; missing evidence becomes an **assumption**, not a
  fake number.
- ❌ Reporting a 0.1 margin as a clear winner. That is a tie — say so.

## Try it yourself

- Re-run Example 1 with `team-familiarity` weighted 5% — does the recommendation flip?
- Add a `compliance` criterion to Example 2 and observe the sensitivity change.
