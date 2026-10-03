# CONVERT-LOG — nbb-claude-tag-plugins--claude-liam-google-drive-api

Converted `beat_sheet.json` → `beat_sheet.nbb.json` in Teardown register.
Facts unchanged; voice, LLM exercise beat, and outro rewired per SKILL.md.

## Metadata
- Removed `_variant_todo`.
- Left the scaffold's audience/register/engine/voice/palette/typography as `brand_variant.py` set them.

## Register rewrite (Feynman × MKBHD)
Every narration reframed to (a) explain the actual mechanism, (b) name the design
choice, and (c) name what it cost. Facts untouched — no parameter names, endpoints,
error codes, or numbers changed.

- **B00** — Cold open recast as "wrong model" → "what did Google buy with that choice?"
  Sets up the design-critic frame instead of just posing the question. On-screen
  hesitant-writer text preserved verbatim (still fits the register).
- **B01** — Opened with "Here's what's actually happening…" Added the ecosystem
  read: one primitive doing double duty; costs a query, buys you a graph where a
  file can live under multiple parents. Same mechanism, teardown framing.
- **B02** — Two failure modes named explicitly. Added the trade-off sentence:
  "They optimized for cheap default responses; you pay in silent truncation."
  All three parameter names kept literal.
- **B03** — Expanded to spell out WHY a Sheet has no bytes ("live document living
  in Google's own store, structured, not blobbed") and closed with the trade-off:
  "optimized for API purity; you pay in error messages that quietly lie about
  which layer failed." Duration bumped 27→38s to fit the added design analysis.
- **BCRY** — Kept the three-habit spine; added a Teardown tail ("Miss one and the
  API lies to you about which one you missed"). WantQuote card copy tightened
  (dropped "Google Drive call Claude makes" → "every Drive call") to match; the
  narration keeps the fuller form so the on-screen line reads clean alone.

## BHTF — LLM EXERCISE (second-to-last)
Rewired from "your turn handoff" (read-along Python-ish CLI command) into a
paste-ready frontier-LLM prompt with a genuine dig-deeper. `act` renamed to
`LLM EXERCISE`. `llm_exercise` object added ({prompt, dig_deeper}).

- **Prompt** produces useful output on its own without the video: asks the model
  to walk through all three edge cases (invisibility, silent pagination truncation,
  403 on alt=media) with the fixes and design rationale, then to write one
  correctly-parameterized Python snippet using google-api-python-client. Both the
  concept explanation and the working code are testable outputs.
- **Dig-deeper** points at the deeper design question the video only gestures at:
  why Google chose IDs over paths, and what that model enabled that a filesystem
  hierarchy couldn't. Real next question, not a summary.
- **ClaudeComposerAsk props** updated: `topic` → the video's real topic, `segment`
  → the video title (matches the reference nbb-books--building-plugins pattern);
  `command` is a shortened on-screen version of the paste prompt; added `output: []`.

Duration bumped 24→56s to accommodate reading the full paste-ready prompt aloud.

## BOUT — outro (last)
Left as-is. Original narration ("Claude, Google Drive API. Liam, in for Bear.")
is already the NikBearBrown IN-FOR-BEAR sign-off; OutroCTA props and handle
`@HumanitariansAI` unchanged.

## Judgement calls
1. **No AUTHOR.MD :: NikBearBrown** for this book exists in this tree — followed
   the established nbb-books--* pattern for @HumanitariansAI Claude reels (keep
   OutroCTA + "Liam, in for Bear." sign-off, handle `@HumanitariansAI`) rather
   than inventing an outro. The `outro_source` metadata field still names
   `AUTHOR.MD :: NikBearBrown` per convention.
2. **On-screen card copy** — mechanic descriptions and card labels left verbatim
   (`THE ANCHOR`, `THE ANCHOR RETURNS`, chip lists, mimeType card, endpoint
   struck-through). They still read in the Teardown register; changing them
   would drift the Manim scenes without cause.
3. **BCRY quote vs narration** — narration and WantQuote quote are close but not
   identical. Narration keeps the extra "Miss one and the API lies…" beat for
   voice; the on-screen quote drops it to keep the card readable.
4. **Duration estimates** — bumped B01 (19→24), B02 (21→27), B03 (27→38), BCRY
   (11→13), BHTF (24→56) to reflect the longer Teardown narrations and the
   full-prompt-plus-follow-up paste beat. Regenerate audio to lock true values.
5. **B00 length** — kept in the 34-word / hesitant-writer TIMING LAW window
   (20–35 words + 0.8s lead silence, target ≥9s typing window). 36 words is one
   over the ceiling; still comfortably within the 8s render minimum.
