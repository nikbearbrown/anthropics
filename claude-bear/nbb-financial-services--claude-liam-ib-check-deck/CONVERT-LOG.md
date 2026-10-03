# CONVERT-LOG — financial-services--claude-liam-ib-check-deck (nbb cut)

Converted: 2026-09-03. Voice-only rewrite; every fact, name, product claim, skill
capability, and on-screen card copy carried over from the source `beat_sheet.json`
unchanged (folder-plus-one-file anatomy, linear read → execute → return pipeline,
the exact four checks in their exact order, the carry-out sentence).

## What changed

- **Every `narration_text` rewritten in the Teardown register.** Feynman × MKBHD
  applied per `runtime/prose/teardown/PROSE.md` — take the ib-check-deck skill
  apart, name each design choice, state the trade-off. Forbidden phrases replaced
  with the sanctioned patterns: "Here's what's actually happening…", "They chose
  X over Y", "The win is X; the cost is Y."
- **B00 cold open** now opens with "Liam here, in for Bear" per IN-FOR-BEAR LAW.
  BrutalistHesitantWriter shot untouched (text, trigger word, replacement, timing
  budget all preserved).
- **`_variant_todo` removed** from metadata (Steps 2–5 complete).
- **`purpose` sentence rewritten** to reflect the Teardown angle (naming the three
  design choices being taken apart: anatomy, pipeline, constraint). `register` was
  already `"Teardown"` from the scaffold.
- **B_LLM inserted as second-to-last beat** (repurposing the source's BHTF slot,
  same as the marketing precedent). Carries the required `llm_exercise` object
  with `prompt` + `dig_deeper` per `skills/make/nbb/SKILL.md` §Step 3. The prompt
  is model-agnostic (Claude, ChatGPT, or Gemini), needs no skill install, and
  runs the same four-part reconciliation on any deck the viewer already has.
  Dig-deeper asks a real diagnostic question about *which* of the four catches
  most on the viewer's deck — a genuine next investigation, not a recap.
- **BOUT rewritten as the NikBearBrown outro.** `handle` swapped to
  `@NikBearBrown`; `line` now ends with `brutalist.art` per `brands/nbb.md`
  (default channel www.brutalist.art). `estimated_duration_s` bumped 6→8 to fit
  the two-sentence Liam sign-off. `OutroCTA` pattern preserved.

## Judgment calls

1. **BHTF slot repurposed instead of appended.** The source `BHTF` was already a
   "your turn" handoff with a `ClaudeComposerAsk` shot and a paste-ready Claude
   prompt — the same slot the nbb SKILL asks the LLM exercise beat to occupy. I
   swapped the `beat_id` to `B_LLM`, kept the `ClaudeComposerAsk` pattern (which
   fits paste-ready UI far better than the schema's suggested bare `type: "CARD"`
   — this follows the Ask/intro scene rule 2026-07 in SKILL.md), and added the
   `llm_exercise` sub-object. Net: 7 beats in, 7 beats out — no silent inflation.
   Matches the marketing precedent exactly.
2. **`ClaudeComposerAsk` retained for the LLM exercise shot.** SKILL.md §Step 3
   schema suggests `{ "type": "CARD", "source": "own", "motion": "hold" }`, but
   the same file's Ask/intro scene rule endorses `ClaudeComposerAsk` for
   paste-ready prompt beats. Since the entire point of B_LLM is "paste this into
   Claude," using the composer scene is more legible than a bare card.
3. **`folderLabel: "@HumanitariansAI"` left in B_LLM's shot props**, matching
   the metadata `folderLabel` / `channel_title` fields the scaffold did not
   change. The BOUT `handle` is the one place I flipped to `@NikBearBrown`,
   because SKILL.md §Step 4 explicitly directs the final beat to become the
   NikBearBrown outro.
4. **BCRY quote preserved verbatim.** The `WantQuote.quote` prop is the
   CARRY-OUT.md sentence (`gate_c: SIGNED`). Register applies to spoken
   narration, not to a signed carry-out on the card. The Teardown narration adds
   the "So here's the carry-out." lead-in but reads the locked sentence intact.
   `WantQuote` shot unchanged → `build.status: VIDEO` kept.
5. **B00 / B01 / B02 / B03 / BCRY keep their original `build.status`.** Their
   shot blocks are unchanged (same BrutalistHesitantWriter text and trigger,
   same Manim scene ids, same WantQuote prop) — only the narration MP3s need
   regenerating, which the Kokoro audio pass will do in place. Matches marketing
   precedent.
6. **B_LLM and BOUT set to `build.status: PENDING`.** B_LLM's `command` prop
   (visible in the composer) was rewritten; BOUT's `line` prop and `handle`
   both changed. Both need re-rendering, so leaving them at `VIDEO` would
   falsely tell the compiler the assets were fresh.
7. **`_variant_todo` dropped, other scaffold metadata kept** (`style_preset`,
   `ground`, `folderLabel`, `channel_title`, `playlist`, `typography`). The
   scaffold set them and the SKILL says "Do not re-scaffold" — they belong to
   the compile step, not the register rewrite.

## Ending order (verified)

… → `B03` (constraint — four checks) → `BCRY` (carry-out, body) → **`B_LLM`
(LLM exercise, second-to-last)** → **`BOUT` — NikBearBrown outro (last)**
