# BUILD-PROMPT — Every Cell a Live Formula

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** claude-cowork
**Source:** `anthropics/financial-services/plugins/vertical-plugins/financial-analysis/skills/dcf-model/SKILL.md`

## One idea
The DCF is a ten-checkpoint chain where every cell references an earlier cell and show-and-confirm pauses gate each stage, so the valuation is auditable end to end.

## The question (cold open)
A valuation is a single dollar figure; this workflow says it is trustworthy only if every upstream stage exposes its own live math. Why can't the agent just compute it and write it down?

## Key case
The implied-share-price cell is the live product of a WACC cell, a terminal-value cell, and a net-debt bridge, and the center of the sensitivity table must equal it or the model is wrong.

## Acts
1. Pull and validate historicals
2. Project revenue and margins
3. Build the free-cash-flow schedule
4. Research WACC and discount each year
5. Terminal value, equity bridge, self-checking sensitivity

## Worked example (illustrative)
Revenue $400M growing 12%, EBIT 18%, WACC 9%, terminal growth 3%; terminal value = final FCF x1.03 / (0.09-0.03), discounted and summed, less $120M net debt, over 40M shares — the center of the WACC x growth table reads back the same price.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
