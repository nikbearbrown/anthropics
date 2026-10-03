# CONVERT-LOG — nbb-claude-for-legal--claude-liam-brief-section-drafter

Register conversion Plain (hai-simple) → Teardown (nbb). Voice only; facts unchanged.

## What changed

- **Every narration rewritten in the Teardown register** (Feynman × MKBHD).
  Opened with "Here's what's actually happening" / "Here's the machinery" / "Here's
  the interesting constraint"; named the design trade-offs on B01 ("legibility
  over cleverness"), B02 ("predictability over cleverness"), B03
  ("reproducibility at the expense of reach"); reframed BCRY carry-out as
  deliberate by design.
- **B03 sparkLine** updated from "Same input, same shape, every time." →
  "Reproducibility over reach — same shape, every run." to mirror the narration's
  trade-off framing (on-screen text was register-adjacent and worth aligning).
- **BCRY quote + sparkLine** rewritten to match the new narration.
- **BHTF converted into the LLM exercise beat (second-to-last)** — added
  `llm_exercise: { prompt, dig_deeper }` per SKILL.md §Step 3; renamed `act` to
  "LLM EXERCISE"; retitled the ComposerAsk `topic` to
  "LLM EXERCISE · BRIEF-SECTION-DRAFTER"; updated `runningText` to
  "paste this into Claude, ChatGPT, or Gemini…" so the on-screen framing matches
  the frontier-LLM contract. The narration adds a "Go deeper" follow-up
  (counterfactual: draft both versions if the case theory shifts, mark every
  citation the change forces).
- **Merged BOUT + BCTA into one outro beat** as the LAST beat: single OutroCTA
  with line "Claude, Brief Section Drafter. Liam, in for Bear." and handle
  "@HumanitariansAI".
- **`_variant_todo` removed.**

## Judgement calls

1. **Handle stays @HumanitariansAI, not www.brutalist.art.** The SKILL.md
   suggests the NikBearBrown outro from AUTHOR.MD (default channel:
   www.brutalist.art). But the precedent set by the nearest sibling nbb reels
   converted from hai-simple sources (e.g.
   `nbb-financial-services--claude-liam-deal-sourcing`) keeps `@HumanitariansAI`
   as the outro handle — this is a HAI-channel reel in the Teardown register,
   not a NikBearBrown-channel reel. Following precedent.
2. **BHTF used as the LLM exercise slot rather than adding a separate B_LLM
   beat.** The SKILL.md template creates a new `B_LLM` beat with a CARD shot;
   the precedent (deal-sourcing) instead lets the existing "your turn" beat
   carry the paste-ready prompt inside its ClaudeComposerAsk visual. Following
   precedent — the composer visual is the canonical Your Turn frame and the
   prompt is already paste-ready for any frontier LLM. Kept the composer shot,
   added the `llm_exercise` metadata so downstream consumers still see the
   structured prompt + dig_deeper.
3. **Merged the two source outro beats (BOUT OutroSeries + BCTA OutroCTA) into
   one outro.** SKILL.md requires the outro as the LAST beat (singular); the
   deal-sourcing sibling collapses them the same way. Result: fewer outro
   scenes, but the LLM exercise cleanly lands as second-to-last.
4. **`estimated_duration_s` on BHTF raised from 28 → 32** because the added
   Go-deeper sentence pushes the narration to ~95 words. Audio is measured at
   build; this is just a hint.

## Not touched

- Every `beat_id`, `act` label (except BHTF → "LLM EXERCISE"), `shot` block,
  Remotion pattern name, and structural prop.
- On-screen card copy on B01 and B02 (already fits the register).
- BrutalistHesitantWriter props on B00 (`triggerWords: "WRITE"` preserved; the
  visual correction still lands).
- No audio, no render, no compile.
