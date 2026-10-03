# CONVERT-LOG — books--claude-liam-installing-plugins → nbb

Converted `beat_sheet.json` (Plain register) into `beat_sheet.nbb.json`
(Teardown register). Source is unmodified.

## What changed

- **All 23 narrations rewritten in Teardown register** (Feynman × MKBHD):
  explain the machinery, name the design choice, judge the trade-off. Facts
  unchanged — every number, name, mechanism, and worked example from the source
  survives. Same ~word-count budget per beat so the 8s+ B00 timing window
  still lands.
- **B00 cold open** — reframed as "here's the mistake — thinking installing
  is the customization," which lines up with the on-screen `install`→`customize`
  correction the BrutalistHesitantWriter performs. Preserved lead_silence_s
  and the TIMING LAW note.
- **BCRY carry-out** — narration tightened; the `WantQuote.quote` prop is
  updated to match, so the on-screen quote and the spoken line stay identical.
- **BHTF upgraded to the LLM exercise beat (SECOND-TO-LAST)** per SKILL.md
  §Step 3:
  - `act` changed from "your turn handoff" → `"LLM EXERCISE"`.
  - Added `llm_exercise` block with `prompt` (paste-ready, works on its own
    without the video) and `dig_deeper` follow-up.
  - Narration now reads the prompt and appends the "Go deeper: …" question
    before signing off as "Liam, in for Bear."
  - `ClaudeComposerAsk.command` prop refined to match the narrated prompt
    (marketing plugin made explicit, so the paste-ready prompt is self-standing).
  - `estimated_duration_s` bumped 30→34 to account for the added
    "Go deeper" line.
- **BOUT outro** — kept as `OutroCTA` with the title+subtitle+Liam form,
  matching the pattern used by other nbb sheets (e.g. nbb-claude-basics
  --screenshot-prompt-caching). `handle: @HumanitariansAI` preserved.
- **`_variant_todo` removed** — checklist complete.

## Preserved exactly

- Every `beat_id`, the act names on all body beats, all `shot` blocks, all
  `graphic.production_viz` structures (labels, chips, arrows, accents, strikes,
  captions, colors), all Remotion patterns and prop shapes, and all on-screen
  card copy (chip labels, captions, spark line). Only the spoken/narrated
  content was re-voiced. The `graphic.production_viz.label` fields on the
  Manim beats are ALL-CAPS chip headers and read fine in the Teardown palette
  as-is — no change needed.
- Scaffold-set metadata (`audience`, `register`, `palette`, `engine`,
  `voice_kokoro`, `typography`, `outro_source`, `derived_from`, plus the
  original `channel_title`, `folderLabel`, `ground`, `style_preset`, `playlist`,
  `gate_c`/`gate_h`/`anchor_pair`/`one_flag`) — all untouched.

## Judgement calls

1. **Kept `folderLabel: @HumanitariansAI`** on BHTF (and `handle` on BOUT), even
   though SKILL.md §"Ask/intro scene rule" mentions a `@NikBearBrown` folder
   chip. Every existing nbb- sheet in this book keeps `@HumanitariansAI`
   because the channel identity stays HAI for these Liam-in-for-Bear reels;
   only the register moves to Teardown. Followed precedent over the SKILL.md
   line rather than diverging silently.
2. **BCRY quote prop updated in lockstep** with the rewritten narration.
   Leaving the old Plain-register quote on screen while Liam speaks the
   Teardown version would fight itself; the spoken and shown carry-out have
   to match.
3. **BOUT `line` prop left literal** — the outro isn't prose to Teardown-ify;
   it's a sign-off in the fixed "Title — subtitle. Liam, in for Bear." form.
4. **Metadata `purpose` field rewritten in Teardown register** — it's authored
   prose describing the reel's intent, so it moves with the voice. Every
   other metadata string is machine-readable state and stays as-is.
5. **`_variant_todo` deleted rather than emptied.** The supervisor check treats
   its absence as done.
