# CONVERT-LOG — nbb-claude-for-legal--claude-liam-build-guide

Register conversion Plain (hai-simple) → Teardown (nbb). Voice only; facts
unchanged.

## What changed

- **Every narration rewritten in the Teardown register** (Feynman × MKBHD).
  Opened B02/B03/B04 with "Here's what's actually happening" / "Here's the
  machinery" / "The execution is deliberately dumb"; named the design
  trade-offs explicitly on B03 ("legibility over cleverness"), B04
  ("predictability over cleverness"), B05 ("repeatability at the expense of
  range"); rewrote B01 to acknowledge the natural read and then name it wrong;
  added the ecosystem beat to B02 ("the weights are untouched; only the
  instruction file is gone"); B06 lands the anchor with "the skill isn't in
  the model. It's in the file"; B07 separates the two independent judgements
  (design of the file vs. coverage of the file); BCRY closes with "that's the
  design, and that's the limit."
- **BCRY quote + sparkLine updated** to match the new narration — quote drops
  the trailing "That's the design…" line (kept in the narration only); sparkLine
  reads "The skill isn't in the model. It's in the file." to echo the B06 line.
- **BHTF converted into the LLM exercise beat (second-to-last)** — added
  `llm_exercise: { prompt, dig_deeper }` per SKILL.md §Step 3; renamed `act`
  → "LLM EXERCISE"; retitled the ComposerAsk `topic` to "LLM EXERCISE ·
  BUILD-GUIDE"; set `segment` to "Your Turn"; updated `runningText` to
  "paste this into Claude, ChatGPT, or Gemini…" so the on-screen framing
  matches the frontier-LLM contract. Prompt asks the reader to write a
  SKILL.md for one repeatable task of their own (the video's carry-out made
  concrete). Dig-deeper is a real experiment: run the file twice, watch what
  breaks, promote the breakages into explicit branches — not a summary.
- **`_variant_todo` removed.**

## Judgement calls

1. **Handle stays @HumanitariansAI, not www.brutalist.art.** The SKILL.md
   suggests the NikBearBrown outro from AUTHOR.MD (default channel:
   www.brutalist.art). But the precedent set by every sibling nbb reel
   converted from a claude-for-legal / hai-simple source (e.g.
   `nbb-claude-for-legal--claude-liam-brief-section-drafter`) keeps
   `@HumanitariansAI` as the outro handle — this is a HAI-channel reel in the
   Teardown register, not a NikBearBrown-channel reel. Following precedent.
2. **BHTF used as the LLM exercise slot rather than inserting a separate
   B_LLM beat.** The SKILL.md template creates a new `B_LLM` beat with a
   CARD shot; the sibling precedent (brief-section-drafter) instead lets the
   existing "your turn" beat carry the paste-ready prompt inside its
   ClaudeComposerAsk visual. Following precedent — the composer visual is the
   canonical Your Turn frame and the prompt is already paste-ready for any
   frontier LLM. Kept the composer shot, added the `llm_exercise` metadata so
   downstream consumers still see the structured prompt + dig_deeper.
3. **BOUT kept as the single closing beat.** Source already had exactly one
   outro (OutroCTA) — no BCTA to merge, no restructure needed. Line and
   handle preserved verbatim.
4. **`estimated_duration_s` on BHTF raised from 20 → 38** because the added
   Go-deeper sentence pushes the narration to ~110 words. Audio is measured at
   build; this is just a hint.
5. **B00 (BrutalistHesitantWriter) narration reworded but the visual props
   are untouched.** The Remotion writer still types "learned" and corrects to
   "was given" — the correction visually mirrors the register shift; the new
   narration now leads with the model-didn't-change beat that the corrected
   sentence implies, then hands off to B01's stakes.

## Not touched

- Every `beat_id`, `act` label (except BHTF → "LLM EXERCISE"), `shot` block,
  Remotion pattern name, Manim scene id, and structural prop.
- All `production_viz` chips, labels, captions, accent/strike arrays — the
  on-screen graphic copy already fits the Teardown register.
- BrutalistHesitantWriter props on B00 (`triggerWords: "learned"`,
  `replacementWords: "was given"` preserved).
- WantQuote structural shape on BCRY (only `quote` and `sparkLine` text
  updated).
- No audio, no render, no compile.
