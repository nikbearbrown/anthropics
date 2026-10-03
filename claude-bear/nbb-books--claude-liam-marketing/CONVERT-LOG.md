# CONVERT-LOG — books--claude-liam-marketing (nbb cut)

Converted: 2026-09-03. Voice-only rewrite; every number, name, product claim, workflow
step, and on-screen card copy carried over from the source `beat_sheet.json` unchanged.

## What changed

- **Every `narration_text` rewritten in the Teardown register.** Feynman × MKBHD
  applied per `runtime/prose/teardown/PROSE.md` — take the plugin apart, name each
  design choice, state the trade-off. Forbidden phrases replaced with the sanctioned
  patterns: "Here's what's actually happening…", "They chose X over Y", "This works
  if you value X; it fails if you need Y."
- **B00 cold open** now opens with "Liam here, in for Bear" per IN-FOR-BEAR LAW.
  Shot block (BrutalistHesitantWriter) untouched — the typed correction and timing
  hold.
- **`_variant_todo` removed** from metadata (Step 2–5 complete).
- **`register: "Plain"` → `register: "Teardown"`** in metadata; `purpose` sentence
  rewritten to reflect the Teardown angle.
- **B_LLM inserted as second-to-last beat** (replacing the source's `BHTF` slot).
  Carries the required `llm_exercise` object with `prompt` + `dig_deeper` per
  `skills/make/nbb/SKILL.md` §Step 3. The prompt is model-agnostic (Claude,
  ChatGPT, or Gemini) and produces a usable brand config on its own without the
  plugin. Dig-deeper is a real next question ("what campaign would be a bad
  first fit?"), not a summary.
- **BOUT rewritten as the NikBearBrown outro.** `handle` swapped to `@NikBearBrown`
  and `line` now ends with `brutalist.art` per `brands/nbb.md` (default channel
  www.brutalist.art). Estimated duration bumped 6→8s to fit the two-sentence Liam
  sign-off. `OutroCTA` pattern preserved.

## Judgment calls

1. **BHTF slot repurposed instead of appended.** The source `BHTF` was already a
   "your turn" handoff with a `ClaudeComposerAsk` shot and a paste-ready Claude
   prompt — the same slot the nbb SKILL asks the LLM exercise beat to occupy. I
   swapped the `beat_id` to `B_LLM`, kept the `ClaudeComposerAsk` pattern (which
   fits paste-ready UI far better than the schema's generic `type: "CARD"`), and
   added the `llm_exercise` sub-object. Net: 23 beats in, 23 beats out — no
   silent inflation.
2. **`ClaudeComposerAsk` retained for the LLM exercise shot.** SKILL.md's schema
   suggests `{ "type": "CARD", "source": "own", "motion": "hold" }`, but the same
   file's Ask/intro scene rule (2026-07) endorses `ClaudeComposerAsk` for
   paste-ready prompt beats. Since the whole point of this beat is "paste this
   into Claude," using the composer scene is more legible than a bare card.
3. **`folderLabel: "@HumanitariansAI"` left untouched on B_LLM's shot**, matching
   the metadata `folderLabel` / `channel_title` fields the scaffold did not
   change. The BOUT `handle` is the one place I flipped to `@NikBearBrown`,
   because SKILL.md §Step 4 explicitly directs the final beat to become the
   NikBearBrown outro.
4. **`build.status` on B_LLM and BOUT set to `PENDING`.** Their narration text
   changed, so the source `mp3/` and `media/` files no longer match; leaving
   `status: "VIDEO"` would falsely tell the compiler the assets were fresh. The
   audio pass (Kokoro `am_onyx`) will regenerate both. All other beats keep
   their original `build.status` because their shot blocks are unchanged — the
   audio pass will overwrite the MP3s in place.
5. **`_variant_todo` dropped, other scaffold metadata kept** (`style_preset`,
   `ground`, `folderLabel`, `channel_title`, `playlist`). The scaffold set them
   and the SKILL says "Do not re-scaffold" — they belong to the compile step,
   not the register rewrite.

## Ending order (verified)

… → `NB19` (both directions) → `BCRY` (carry-out, body) → **`B_LLM` (second-to-last)** → **`BOUT` — NikBearBrown outro (last)**
