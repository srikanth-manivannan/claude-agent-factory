# Prompt Engineering Standard

> How to write the instructions and prompts inside skills, agents, workflows, and
> prompt blocks. These artifacts *are* prompts — their quality is the product's
> quality. Reviewed via [review-process.md](review-process.md).

**Min standard:** 0.1.0 · See also: [documentation.md](documentation.md),
[security.md](security.md), [`/templates/blocks/Prompt.md`](../templates/blocks/Prompt.md).

## Principles

1. **Imperative and ordered.** Instructions are numbered, unambiguous steps.
2. **State the contract.** Define when to use / not use, inputs, outputs, and
   constraints up front.
3. **Technology-neutral body, specifics as data.** Keep wording stack-agnostic; pass
   technology via the tech profile / variables (mirrors the
   [blocks](../templates/blocks/) approach).
4. **Progressive disclosure.** Keep the top short; push long reference material to
   `resources/` and load on demand (advanced skills).
5. **Structured output when consumed by machines.** Specify the exact format; prefer
   schema-constrained output for tool/agent use.
6. **Show, don't just tell.** Include a minimal example; full demos go in
   [`/examples/`](../examples/).

## Safety in prompts

- Treat all external/tool input as untrusted; defend against **prompt injection**
  ([security.md](security.md)).
- Disclose dual-use behavior; build in refusal paths for unsafe requests.

## Anti-patterns

- Vague directives ("handle errors appropriately") without specifics.
- Hardcoding a single technology where a variable belongs.
- Walls of prose instead of steps.
- Duplicating guidance that belongs in a standard — link instead.
