# CONVERT-LOG — books--claude-liam-troubleshooting → nbb

Converted `beat_sheet.json` (Plain register) into `beat_sheet.nbb.json`
(Teardown register). Source is unmodified.

## What changed

- **All 19 narrations rewritten in Teardown register** (Feynman × MKBHD):
  explain the machinery, name the design choice, judge the trade-off. Facts
  unchanged — every failure shape, every diagnostic step, every source in the
  "check the live sources" list survives. Word budgets held close to source so
  the audio window per beat lands in the same neighborhood.
- **B00 cold open** — narrowed to the ≤35-word TIMING LAW window (34 words).
  Reframed as "here's what breaks first — the instinct." Lands on the same
  corrected question the BrutalistHesitantWriter types on screen ("Where's the
  fix that matches the concept?"). All Remotion props (triggerWords "screen" →
  replacementWords "concept", seed, sizes, timing) preserved verbatim, and the
  full TIMING LAW note is carried through.
- **BCRY carry-out** — tightened; the `WantQuote.quote` prop is updated in
  lockstep so the on-screen quote matches the spoken line exactly. `sparkLine`
  ("The interface dates. The model doesn't.") preserved.
- **BHTF upgraded to the LLM exercise beat (SECOND-TO-LAST)** per SKILL.md
  §Step 3:
  - `act` changed from "your turn handoff" → `"LLM EXERCISE"`.
  - Added `llm_exercise` block with `prompt` (paste-ready, works on its own
    without the video — asks for the five failure modes broken down three ways,
    plus a numbered four-step diagnostic loop) and `dig_deeper` follow-up
    (asks which failure mode gets *worse* as ecosystems mature — a genuine
    next question, not a summary).
  - Narration now reads the prompt through, appends the "Go deeper: …" line,
    then signs off as "Liam, in for Bear."
  - `ClaudeComposerAsk.command` prop refined to match the paste-ready prompt
    exactly so the composer on screen and the paste text are the same thing.
  - `estimated_duration_s` bumped 30 → 45 to cover the longer narration.
- **BOUT outro** — kept as `OutroCTA` with the title+subtitle+Liam form
  ("Claude, Unstuck — troubleshooting and staying current. Liam, in for
  Bear."), matching the pattern used by every other nbb sheet in this book.
  `handle: @HumanitariansAI` preserved.
- **Metadata `purpose` rewritten in Teardown register** — it's authored prose
  describing the reel's intent, so it moves with the voice.
- **`_variant_todo` removed** — checklist complete.

## Preserved exactly

- Every `beat_id`, the act names on all body beats (B00, NB01–NB15, BCRY,
  BOUT), all `shot` blocks, all `graphic.production_viz` structures (labels,
  chips, arrows, accents, strikes, captions, colors, manim scene names), all
  Remotion patterns and prop shapes, and all on-screen card copy. Only the
  spoken/narrated content was re-voiced. The `production_viz.label` fields
  are ALL-CAPS chip headers and read fine in the Teardown palette as-is.
- Scaffold-set metadata (`audience`, `register`, `palette`, `engine`,
  `voice_kokoro`, `typography`, `outro_source`, `derived_from`, plus the
  original `channel_title`, `folderLabel`, `ground`, `style_preset`,
  `playlist`, `gate_c`/`gate_h`/`anchor_pair`/`one_flag`) — all untouched.

## Judgement calls

1. **Kept `folderLabel: @HumanitariansAI`** on BHTF (and `handle` on BOUT),
   following precedent set by every other nbb- sheet in this book. The
   channel identity stays HAI for these Liam-in-for-Bear reels; only the
   register moves to Teardown. Followed sibling precedent over the SKILL.md
   line about `@NikBearBrown` rather than diverging silently.
2. **BCRY quote prop updated in lockstep** with the rewritten narration.
   Leaving the old Plain-register quote on screen while Liam speaks the
   Teardown version would fight itself; the spoken and shown carry-out have
   to match.
3. **BOUT `line` prop left literal** — the outro isn't prose to Teardown-ify;
   it's a sign-off in the fixed "Title — subtitle. Liam, in for Bear." form
   used by every sibling nbb sheet.
4. **B00 held to 34 words** — the TIMING LAW note in the source explicitly
   caps narration at 20–35 words so the BrutalistHesitantWriter typing window
   stays ≥ 9s. The Teardown rewrite still lands on the same on-screen
   correction beat ("concept").
5. **BHTF narration reads the prompt in full.** Alternative was a short
   "paste this" gesture, but the beat's job in a Teardown reel is to make the
   exercise *feel* like a real thing to do — reading it makes the "go deeper"
   line land as a follow-up rather than a footnote. `estimated_duration_s`
   bumped to 45 to accommodate.
6. **`_variant_todo` deleted rather than emptied.** The supervisor check
   treats its absence as done.
