# Corporate Finance with AI — Simulation Ideas

MANIM-lane candidates only. Score ≥ 6 required.

## Cross-book note

This book covers the same chapter content as `mba-corporate-finance/` (same protagonist, same firm Halverson, same chapter titles and equations). Rather than duplicate cards, the single genuine MANIM candidate from these shared chapters is written in full in:

`mba-corporate-finance/youtube/simulation-ideas.md` — Candidate 01: MM Proposition II WACC Invariance

The card applies equally to this book. Build it from either source; `mba-corporate-finance/` has the marginally more explicit Proposition II formula presentation.

## Assessment of remaining chapters

After reading all 19 chapters against the three-gate test:

- **Capital budgeting (Ch 4):** NPV sensitivity to terminal growth rate is pedagogically important but the animation is a static sensitivity table, not a moving artifact driven by a named equation. Better as D3.
- **WACC sensitivity (Ch 5):** The WACC grid is interactive by nature (two-axis sensitivity table). D3, not Manim.
- **Real options (Ch 6):** Decision trees animate well but the value comes from branching structure, not from a single equation producing a moving artifact. D3 or a step-by-step branching animation is natural; it passes motion but fails the "single equation → artifact" test for MANIM lane.
- **MM with taxes (Ch 7):** The tax shield V_L = V_U + T×D is a horizontal shift in firm value, not a curve. Belongs in a single Remotion card, not a Manim animation.
- **Capital structure real world (Ch 8):** Trade-off theory curve (value vs. leverage) is qualitative without a closed-form equation for the distress cost function. Fails gate 1 (simulatable from a stated equation).
- **Dividends (Ch 9), M&A (Ch 11), operational risk (Ch 12), international finance (Ch 13), behavioral finance (Ch 14):** Qualitative or empirical chapters; no pure-equation → moving artifact candidates.

This book yields **one genuine MANIM candidate** (MM Prop II, cross-referenced above). Padding beyond that would manufacture cards; the honest count is one.
