# CONVERT-LOG — claude-for-legal--claude-liam-exam-forecast → nbb

**Date:** 2026-09-03
**Source:** `anthropics/claude-bear/claude-for-legal--claude-liam-exam-forecast/beat_sheet.json` (Plain register, 13 beats)
**Output:** `beat_sheet.nbb.json` (Teardown register, 13 beats)
**Voice:** Kokoro `am_onyx` — Liam, in for Bear (unchanged; scaffold-set).

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman × MKBHD):
  named the mechanism ("Skill is a folder Claude reads before it works … SKILL.md
  is the recipe"), sharpened the design-critic framing on B06 ("They optimized the
  exam for teaching, not for prediction — and prediction is exactly what the
  forecast needs"), and swapped "pattern-not-promise"/"reorder-not-delete" into
  explicit trade-off language on B08/B09. Facts unchanged — consideration
  doctrine, four of the last five years, statute of frauds, exceptions, the
  three-step SKILL.md flow, brand-new course = no forecast, all preserved.
- **`register`** metadata already set to `Teardown` by the scaffold; left as-is.
  Added `brand: "claude-liam"` to match peer nbb sheets.
- **`purpose`** metadata rewritten to describe the Teardown take on the reel
  (counting mechanism against public course material; ranked list as output).
- **BCRY `WantQuote.quote` updated** to match the rewritten carry-out narration
  (WantQuote renders the quote on-screen; a narration/prop mismatch would put
  two different sentences on the beat).
- **BHTF turned into the LLM exercise beat** — added the `llm_exercise` object
  with `prompt` (paste-ready for any frontier LLM, mirrors the source's
  paste-in-Claude prompt) and `dig_deeper` follow-up ("take the top-ranked topic
  and give me a one-week study plan…"). `runningText` updated from
  `"paste this into Claude…"` to `"paste this into Claude, ChatGPT, or Gemini…"`
  per nbb SKILL.md §Step 3. `command` prop updated to match the new prompt.
- **`_variant_todo` removed** from metadata.
- **`estimated_duration_s`** adjusted per beat to reflect the (slightly longer)
  Teardown word counts. Actual durations will be re-measured on audio regen.

## Judgement calls

- **Outro kept as-is** (title + "Liam, in for Bear.", `handle: "@HumanitariansAI"`).
  The source outro already honors the IN-FOR-BEAR sign-off; peer nbb reels in
  this book (e.g. `nbb-…-ai-inventory`) also keep the Humanitarians handle. Per
  SKILL.md §Step 4, the outro "content from `AUTHOR.MD :: NikBearBrown`" would
  swap the channel to `www.brutalist.art` — declined here to match peer
  convention for reels that live in the HAI orbit. No `AUTHOR.MD` was found on
  disk under `anthropics/claude-bear/` to override this.
- **Scaffold fields left untouched** as instructed: `palette: "teardown"`,
  `style_preset: "humanitarians"`, `ground: "#F3EBDD"`, `folderLabel`,
  `channel_title`, `playlist`, `in_for_bear`, `engine`, `voice_kokoro`.
  Manim/graphic color arrays (`#F3EBDD` / `#2F2A26` / `#E4572E`) preserved
  unchanged so the existing rendered manim/*.mp4 files stay valid; a full
  palette re-skin to strict teardown (`#FFFFFF`/`#2A1A0E`/`#C8102E`) is a
  separate re-render pass, not this conversion.
- **B00 hesitant-writer display text unchanged** ("exactly" → "roughly"
  correction with `seed: "hai-exam-forecast"`); the narration was reshaped to
  land the Teardown frame over that same typed content plus the Liam sign-in.
- **On-screen labels/chips/captions preserved** across every GRAPHIC beat —
  they still fit the Teardown register and changing them would invalidate
  rendered manim clips.

## Ending order verified

`… B09 → BCRY (carry-out) → BHTF (LLM EXERCISE) → BOUT (outro)`

Second-to-last = LLM exercise; last = NikBearBrown outro. ✔
