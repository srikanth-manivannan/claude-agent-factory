# Examples — System Design Reviewer

> Worked reviews. The method is technology-agnostic; specifics come from the design
> under review. See [SKILL.md](SKILL.md).

## Example 1 — Scaling risk (happy path)

**Input:** "A single API instance writes to one relational DB. We expect 50× traffic
growth in 12 months." Goal: handle growth without redesign.

**Critical path:** client → API instance → single DB (write + read).

**Findings**
| Sev | Area | Finding | Recommendation |
|-----|------|---------|----------------|
| 🔴 | Reliability | DB is a single point of failure | Add replica + failover; define RPO/RTO |
| 🟠 | Scalability | API holds session state → blocks horizontal scaling | Externalize state; make API stateless |
| 🟠 | Scalability | Single DB for read+write won't take 50× reads | Add read replicas / caching layer |
| 🟡 | Operability | No mention of metrics/tracing | Instrument before scaling (observability) |

**Strengths:** simple, well-understood stack; clear data ownership.
**Verdict:** **needs-rework** (open 🔴). **Assumptions:** 50× is read-heavy; no
multi-region requirement.

## Example 2 — Mostly-sound design (approve-with-changes)

**Input:** event-driven design with a queue, stateless workers, and a partitioned store.

**Findings:** 🟠 no dead-letter queue for poison messages; 🟡 retry policy unspecified.
**Strengths:** stateless workers scale horizontally; partitioning matches access pattern.
**Verdict:** **approve-with-changes** (no 🔴; fix the 🟠 DLQ before launch).

## Example 3 — Edge: ambiguous design

**Input:** a one-paragraph description with no data flow.

**Behavior:** the skill does **not** invent a design. It returns clarifying questions
(What is the write path? Expected scale? Consistency needs?) and pauses — per the
method's step 1.

## Anti-example

- ❌ "This design is bad, rework it." — no severity, no location, no recommendation.
  Every finding must cite a part of the design and propose a fix.

## Try it yourself

- Add a `compliance: PCI` constraint to Example 1 — note the new security finding.
- Re-run Example 2 assuming 100× traffic — does any 🟡 become 🟠?
