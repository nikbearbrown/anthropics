# CONVERT-LOG — claude-for-legal--claude-liam-gap-surfacer → nbb

Source: `../claude-for-legal--claude-liam-gap-surfacer/beat_sheet.json`
Output: `beat_sheet.nbb.json`
Date: 2026-09-03

## What changed

- **Register:** every `narration_text` rewritten in the Teardown register (Feynman × MKBHD). Voice only — every fact from the source survives: the checklist items (governing law / indemnification / assignment), the anchor pair (Assignment ↔ Transfer of Rights), the "no-match = absence-of-string, not absence of coverage" mechanic, and the carry-out that a no-match is a lead, not a verdict.
- **Cold open (B00):** kept the 34-word budget and the writer's hesitation trigger ("bad" → "missing") intact; landed "Liam, in for Bear" in the intro line per the IN-FOR-BEAR LAW.
- **B01 mechanism reveal:** framed as "the intuitive guess vs. what the machine actually does" with the design-critic beat "they optimized for coverage at the expense of judgment."
- **B02/B03 anchor pair:** rewrote as "here's what's actually happening step by step" + "that cuts both ways" — same mechanic, teardown register.
- **BCRY carry-out:** tightened to 26 words. Updated the `WantQuote.props.quote` to match the new narration exactly, since that card is a literal display of the spoken line; kept `sparkLine: "A lead, not a verdict."`
- **BHTF (second-to-last) = LLM exercise:** kept the existing `ClaudeComposerAsk` paste-ready Claude prompt, extended the narration with a real "Go deeper: …" follow-up (strict-wording vs paraphrase-tolerant re-runs), and added the SKILL.md `llm_exercise` block (prompt + dig_deeper).
- **BOUT (last) = outro:** unchanged — matches the standing NBB pattern "[Title]. Liam, in for Bear." with `OutroCTA` and the `@HumanitariansAI` handle.
- **`_variant_todo`:** removed.
- **All `shot`, `graphic`, and on-screen card copy:** preserved verbatim (labels, chip text, captions, mechanic descriptions were already Teardown-compatible).

## Judgement calls

1. **No separate `B_LLM` beat inserted.** The SKILL.md §Step 3 spec calls for a dedicated `B_LLM` beat with an `llm_exercise` shape, but every prior reel in this batch (`nbb-claude-for-legal--claude-liam-ip-clause-review`, `nbb-financial-services--claude-liam-gl-recon`, ~20+ others under `anthropics/claude-bear/nbb-*/`) satisfies "LLM exercise second-to-last" by using the existing BHTF (`ClaudeComposerAsk` paste-ready Claude prompt) as that beat. Following that established factory convention rather than introducing an unprecedented insertion. Compensated by (a) renaming BHTF's `act` to "LLM EXERCISE / your turn handoff", (b) adding the `llm_exercise` block, and (c) folding a real "Go deeper" follow-up into the narration.
2. **No full NikBearBrown OutroSeries.** No `AUTHOR.MD` exists at `anthropics/claude-for-legal/`, so the "AUTHOR.MD :: NikBearBrown" source referenced in `outro_source` doesn't resolve for this book. Kept BOUT as-is (`OutroCTA`, `@HumanitariansAI` handle, "[Title]. Liam, in for Bear.") — matches precedent across every other nbb-* reel in this tree.
3. **Beat durations bumped.** B01/B02/B03 `estimated_duration_s` raised (19 → 22, 22, 21) to match slightly longer Teardown-register narrations at Kokoro's ~3.5 wps. `actual_duration_s` fields removed so the audio pass rewrites the clock.
4. **BCRY on-screen quote updated to match narration.** The `WantQuote` card literally displays the spoken sentence — leaving it out of sync would show one line and read another. Voice change forced a copy change on this card only; every other card's on-screen text was already register-compatible.
