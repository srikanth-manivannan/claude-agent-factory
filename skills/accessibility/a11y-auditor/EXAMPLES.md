# Examples — Accessibility Auditor

> Worked audits. Target level configurable; method is framework-agnostic. See [SKILL.md](SKILL.md).

## Example 1 — Form audit (happy path, WCAG AA)

**Input:** a sign-up form: an `<input>` with no label, placeholder-only; submit button
contrast 3.1:1; custom dropdown not keyboard-operable.

**Findings**
| Sev | Element | WCAG | Fix (skill) |
|-----|---------|------|-------------|
| 🔴 | email `<input>` | 3.3.2 Labels | add a `<label>` (`aria-annotator`) |
| 🔴 | custom dropdown | 2.1.1 Keyboard | make focusable + arrow-key operable (`keyboard-nav-checker`) |
| 🟠 | submit button | 1.4.3 Contrast | raise to ≥4.5:1 (`color-contrast-fixer`) |
| 🟡 | placeholder as label | 1.3.1 | keep label visible, not placeholder-only |

**Passed:** headings hierarchical; images have alt text.
**Manual verification:** screen-reader pass on the full submit flow.

## Example 2 — Mostly accessible (approve-with-changes)

**Input:** a card component with good semantics but a 🟠 focus indicator removed via CSS.

**Finding:** 🟠 2.4.7 Focus Visible — restore a visible focus style. No 🔴.

## Example 3 — Edge: AAA requested

**Input:** `wcag_level: AAA` for a marketing page.

**Behavior:** audits to AAA (e.g. contrast ≥7:1), and clearly marks which findings are
AAA-only vs. AA so the team can decide scope.

## Anti-example

- ❌ "Improve accessibility." Every finding must cite an element and a WCAG criterion
  with a concrete fix.
- ❌ Claiming "fully accessible" from automated checks alone — screen-reader UX needs a
  human pass.

## Try it yourself

- Re-run Example 1 at `wcag_level: A` — which findings drop out of scope?
- Add `context` describing a keyboard-only user — note prioritization shift.
