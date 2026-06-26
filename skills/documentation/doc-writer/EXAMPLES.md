# Examples — Doc Writer

> Worked examples. See [SKILL.md](SKILL.md) and the
> [documentation standard](../../../standards/documentation.md).

## Example 1 — README for an undocumented library (happy path)

**Subject:** a date-utils library, audience = developers.

**Produces:** title + one-sentence description; "What it does"; a 3-step Quickstart
(install → import → call); inputs/outputs table; customization; an honest Limitations
section ("no timezone support yet"); a Changelog link.

## Example 2 — Refreshing stale docs

**Subject:** a README claiming a removed `--legacy` flag.

**Behavior:** detects the mismatch against current behavior, removes the stale claim,
and updates the example — accuracy over preserving old text.

## Example 3 — Edge: thin intent

**Subject:** code with unclear purpose and no spec.

**Behavior:** documents observable behavior and explicitly asks for the intended
audience/purpose rather than inventing a narrative.

## Anti-example

- ❌ Writing "blazing-fast, enterprise-grade" without evidence. Docs describe what the
  thing does, not unverified superlatives (VISION §14 voice).
- ❌ Copying the testing rules into the README instead of linking the standard.

## Try it yourself

- Re-run Example 1 with `audience: end-users` — note the quickstart simplifies.
- Add an `existing_docs` input with a stale section — watch it get corrected.
