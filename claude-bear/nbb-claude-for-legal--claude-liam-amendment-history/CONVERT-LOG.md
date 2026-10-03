# CONVERT-LOG — claude-for-legal--claude-liam-amendment-history

## What changed

- Rewrote every beat's `narration_text` into the Teardown register (Feynman ×
  MKBHD): explain the machinery, name the trade-off, judge the choice on its own
  terms. Facts untouched — same contract, same 30 → 60 → 45 notice-period chain,
  same clause-by-clause conclusion.
- Enhanced `BHTF` into the explicit LLM exercise beat (second-to-last):
  added an `llm_exercise` object with a paste-ready prompt for
  Claude / ChatGPT / Gemini and a `dig_deeper` follow-up per
  `skills/make/nbb/SKILL.md` §Step 3. Reworked its narration to introduce the
  prompt and read the "Go deeper" line, keeping the "Liam, in for Bear" sign-off
  in the same beat.
- Removed `_variant_todo` from metadata.

## What did NOT change

- Every `beat_id`, `act`, `shot` block, `graphic` block and on-screen card copy
  is preserved verbatim. The `WantQuote` on `BCRY` is the on-screen carry-out
  sentence, so the narration is left verbatim to match the card.
- `BOUT` outro pattern (`OutroCTA`) and line copy are preserved. The channel is
  `@HumanitariansAI` (Liam in for Bear); no reason to change the handle or swap
  to `OutroSeries`.
- No audio, no compile, no render — this pass is the beat sheet only.

## Judgement calls

1. **LLM exercise placement.** The source already had a `BHTF` "your turn
   handoff" beat with a paste-ready Claude prompt — functionally the LLM
   exercise. The reference nbb reel (`nbb-claude-for-legal--claude-liam-ip-clause-review`)
   handled this by teardown-rewriting the same beat without adding a new one.
   I did the same, but added the SKILL.md-required `llm_exercise` object
   (`prompt` + `dig_deeper`) and read the "Go deeper" line in the narration.
   Rationale: inserting a separate `B_LLM` beat before `BOUT` would duplicate
   `BHTF` (two paste-ready Claude prompts back-to-back), and the invocation
   says "preserve every `beat_id`, the act structure, `shot` blocks."
   I did rename `BHTF.act` from "your turn handoff" → "LLM EXERCISE" to match
   the SKILL.md schema; the shot block is preserved untouched.
2. **BCRY narration.** The `WantQuote` renders the exact carry-out sentence on
   screen. The narration reads the same sentence, so a teardown rewrite would
   desync narration from card. Left verbatim.
3. **Outro handle.** `@HumanitariansAI`, not `@NikBearBrown` — this reel lives
   on the HAI channel, Liam-in-for-Bear. The nbb SKILL says outro content comes
   from `AUTHOR.MD :: NikBearBrown`, but the channel_title is `@HumanitariansAI`
   and the reference reel kept the HAI handle too. Kept `@HumanitariansAI`.
