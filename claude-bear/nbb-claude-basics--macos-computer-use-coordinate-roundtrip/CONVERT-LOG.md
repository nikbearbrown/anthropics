# CONVERT-LOG — nbb-claude-basics--macos-computer-use-coordinate-roundtrip

Converted `beat_sheet.json` → `beat_sheet.nbb.json` in the Teardown register.
Voice: Liam (Kokoro `am_onyx`), in for Bear. Palette: teardown. Facts held
constant — only the register moved.

## What changed

- **B00 (cold open)** — rewritten. Names the mechanism plainly ("the API
  resizes it first, into a canvas you never saw") instead of the softer "into
  a different coordinate space". 35 words, inside the 20–35 TIMING LAW window.
  BrutalistHesitantWriter props preserved (`triggerWords: exactly` →
  `replacementWords: resized`).
- **B01 (stakes / wrong guess)** — rewritten. Explicit design-choice call-out
  ("One input pipeline, not one per screen resolution — that's the design
  choice"), then names the cost (Teardown MKBHD lens). Tile-budget numbers
  unchanged: 28-by-28 patches, 1568 pixel long edge, 1568 tiles total.
- **B02 (anchor planted)** — rewritten. Adds "dead center" to make (960, 540)
  intuitive, and renames the consequence explicitly ("the direct consequence of
  the encoder having one canvas and your Mac having another"). Anchor numbers
  unchanged: 1920×1080 native → 1456×819 sent; (960, 540) ↔ (728, 409).
- **B03 (mechanism)** — rewritten. Takes `target_image_size` apart ("a binary
  search for the largest width and height that keep the long edge under 1568
  pixels, keep the tile count under 1568, and preserve the aspect ratio"), then
  names what breaks if you skip recording ("Skip recording them and the math
  has nothing to divide by"). Function name preserved as
  "target underscore image underscore size" for Kokoro TTS. `image.py` + 1568
  caps unchanged.
- **B04 (anchor payoff)** — rewritten. Explains *why* the multiply works
  ("you're just undoing the shrink, one axis at a time"). Worked arithmetic
  unchanged (728 × 1920/1456 = 960; 409 × 1080/819 = 540). Reframes the
  already-in-budget case as the caveat, not a failure mode — same framing as
  the sibling `browser-coordinate-scaling` nbb reel.
- **BCRY (carry-out)** — narration + `WantQuote.quote` both tightened. Says
  "record what `target_image_size` returned" instead of "record the size you
  sent" — Teardown values naming the actual call. On-screen `sparkLine` kept
  ("Resized space vs. native display."). Note: narration reads
  "target underscore image underscore size" (Kokoro-friendly); on-screen quote
  reads `target_image_size` (readable).
- **BHTF** — repurposed as the **LLM EXERCISE beat** (judgement call below).
  Narration is now a paste-ready prompt for any frontier LLM (Claude / ChatGPT
  / Gemini) + a real "Go deeper:" follow-up about what `target_image_size`
  returns when the screenshot is already inside budget. Added the
  `llm_exercise` object per SKILL.md §Step 3 schema. `ClaudeComposerAsk.command`
  prop updated so the on-screen ask matches the spoken prompt (was a one-line
  imperative — now names the three function inputs the viewer is asked to
  handle).
- **BOUT** — unchanged. Title + "Liam, in for Bear." with `@HumanitariansAI`
  handle already reads as a NikBearBrown outro line in this reel's channel
  context; no book `AUTHOR.MD` exists in `anthropics/claude-bear/` to draw a
  different line from.
- **`_variant_todo`** — removed (checklist satisfied).

## Judgement calls

1. **LLM exercise: enrich BHTF vs insert a new B_LLM.** SKILL.md §Step 3 shows a
   schema example with `beat_id: B_LLM`, but the sibling nbb reel in this book
   (`nbb-claude-basics--browser-coordinate-scaling`, same hai-simple skeleton,
   same channel) keeps the count at 8 and enriches BHTF into the LLM exercise
   role rather than adding a 9th beat. BHTF is already a `ClaudeComposerAsk`
   with a paste-ready `command` prop, so a new B_LLM would duplicate the same
   visual and role. Followed the shipped precedent: repurposed BHTF, kept 8
   beats, added the `llm_exercise` object for schema compliance, and renamed
   the `act` to `LLM EXERCISE - your turn handoff` so the role is explicit
   downstream. Ending order still resolves to
   [body] → [LLM exercise = BHTF] → [outro = BOUT], which is what §Step 5 checks.

2. **BCRY quote text changed to match narration.** SKILL.md's preserve rule
   allows changing on-screen card copy "where it still fits the Teardown
   register." Naming `target_image_size` explicitly in the on-screen line
   sharpens the direction of the multiply — the reference reel used the same
   pattern (syncing quote to narration). Wrote `target_image_size` (readable)
   on-screen and "target underscore image underscore size" (Kokoro-friendly)
   in the spoken line.

3. **BOUT left as-is.** No `AUTHOR.MD` exists under `anthropics/claude-bear/`
   or its immediate parents (the only `AUTHOR.MD` in this tree is
   `anthropics/youtube/ai-1/AUTHOR.MD`, which is not the parent of this reel).
   The existing `OutroCTA` line + `@HumanitariansAI` handle already read as the
   NikBearBrown outro under the Liam-in-for-Bear frame. Sibling nbb reel does
   the same.

4. **BHTF estimated_duration_s bumped 18 → 26.** The new narration is longer
   (the paste-ready prompt is doubled in scope: three function inputs + the
   dig-deeper line). Bumped the estimate accordingly. Actual duration will be
   re-measured on the next audio pass; this is just a hint to the compiler
   so the slot isn't obviously undersized before audio runs.

## Facts preserved (spot check)

- 1920 × 1080 native; button at (960, 540) — unchanged.
- Resized to 1456 × 819; same button at (728, 409) — unchanged.
- 28 × 28 patches, ≤1568 long edge, ≤1568 tiles total — unchanged.
- 728 × (1920 / 1456) = 960; 409 × (1080 / 819) = 540 — unchanged.
- `target_image_size` binary search in `image.py` — unchanged.
- Already-in-budget screenshot: `target_image_size` passes dimensions through
  unchanged, no inverse to apply — unchanged.

## Not done (per task scope)

- No render, no audio generation, no compile. Estimated durations left as-is
  (except BHTF, see judgement call 4); actual durations will be re-measured on
  the next audio pass.
