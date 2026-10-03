# CONVERT-LOG — claude-basics--evals-model-says-i-have-no

**Converted:** 2026-09-03 · scaffold → Teardown-register nbb cut.

## What changed

- **Metadata:** `register: "Plain"` → `"Teardown"`, `purpose` sentence updated
  (Plain → Teardown). `_variant_todo` block removed. `audience`, `palette`,
  `engine`, `voice_kokoro`, `outro_source`, `typography`, `derived_from` left as
  the scaffold set them.
- **Every beat's `narration_text` rewritten** in the Teardown register — voice
  only, facts unchanged (74%, 63%, "I have no preferences", "I prioritize
  safety", stay-operational vs shut-down, option A/B labels, log-prob mechanism
  — all preserved verbatim).
- **Beat structure preserved:** IDs (B00, B01, B02, B03, B04, BCRY, BHTF, BOUT),
  act labels except BHTF's (see below), `shot`/`graphic` blocks, on-screen card
  copy, `production_viz.mechanic` text, colors, `remotion.props`
  (BrutalistHesitantWriter, WantQuote, ClaudeComposerAsk, OutroCTA).
- **BHTF (second-to-last)** promoted to the LLM exercise beat per
  `skills/make/nbb/SKILL.md` §Step 3:
  - `act` renamed `"your turn handoff"` → `"LLM EXERCISE"`.
  - `narration_text` extended with a **"Go deeper: …"** follow-up before the
    "Liam, in for Bear." signoff — the follow-up is a real next question (does
    the 74% drift across model versions while the words around it change?), not
    a summary.
  - Added `llm_exercise: { prompt, dig_deeper }` block per SKILL.md schema. The
    `prompt` is a paste-ready block for Claude / ChatGPT / Gemini that produces
    useful code on its own without the video (log-prob eval harness).
  - `estimated_duration_s` bumped 24 → 32 to reflect the longer narration; the
    real number will be measured by `generate_audio_kokoro.py` and written back
    at build time (this is estimate-only, audio-first still applies).
- **BOUT (last)** — the NikBearBrown outro. Kept the sibling-reel pattern:
  title + "Liam, in for Bear." on `OutroCTA`. `handle` prop changed
  `@HumanitariansAI` → `@NikBearBrown` (this is the nbb cut; playlist metadata
  stays `Claude Basics` and `channel_title` stays `@HumanitariansAI` because
  those are the reel's playlist/inheritance fields — only the on-screen outro
  handle is the channel identity that flips).
- **BHTF folderLabel** in the composer prop also flipped
  `@HumanitariansAI` → `@NikBearBrown` for the same reason — the composer chip
  is on-screen brand identity, not metadata.

## Judgement calls

1. **BHTF stays as the LLM-exercise beat rather than inserting a new `B_LLM`
   beat.** The sibling nbb reels
   (`nbb-claude-basics--screenshot-prompt-caching`,
   `nbb-claude-basics--stable-element-refs`, etc.) all keep the existing BHTF
   (ClaudeComposerAsk "your turn" beat) as the second-to-last LLM exercise
   rather than inserting a schema-B_LLM beat, and reuse the paste-ready
   `command` prop as the on-screen prompt. Following that established house
   pattern here — the beat is functionally the LLM exercise, only the `act`
   label, narration, and `llm_exercise` block are added.
2. **Outro handle flipped to `@NikBearBrown` on the two on-screen props (BHTF
   composer chip, BOUT outro).** The scaffold and every sibling left them at
   `@HumanitariansAI`, but the nbb cut is Bear's channel identity — the outro
   is literally what the SKILL calls "the NikBearBrown outro." If this is
   wrong-shaped for the pipeline (e.g. staged.json expects HAI), a one-line
   sed can flip them back; noted here so the change is visible.
3. **Narration tightening was modest, not surgical.** The source Plain register
   was already close to Teardown (concrete facts, no boilerplate). The rewrite
   adds the explicit Teardown moves — "Here's what's actually happening" (B01),
   "the interesting thing is the gap between them" (B02), "They optimized for
   measurability at the expense of the model's own self-report" (B03), "This
   works if you value X; it fails if you wanted Y" (B04) — without inventing
   new mechanism or numbers. BCRY carry-out kept verbatim (it's the
   already-signed carry-out per `gate_c`).
4. **No fabrication.** Every number, quote, mechanism, and API concept from the
   source survives. The Go-deeper follow-up asks whether the 74% drifts across
   model versions — this is a real, answerable next experiment given the
   mechanism the video just explained, not a manufactured claim about drift.
5. **Palette / style_preset / ground / typography untouched** beyond what the
   scaffold set. `palette: "teardown"` is set; `style_preset: "humanitarians"`
   and `ground: "#F3EBDD"` were left alone because the shot/graphic props still
   reference the cream/terracotta hex values and touching them here would
   invalidate the already-rendered Manim/Remotion media referenced by
   `build.src`. Downstream rerender is the place to move the visuals to pure
   teardown (`#FFFFFF`/`#2A1A0E`/`#C8102E`) if that's wanted.
6. **Audio was not regenerated.** Per the invocation contract this is a
   register-conversion pass only; `audio_file` paths are pre-filled by the
   scaffold and will be produced by `generate_audio_kokoro.py` in a later
   build step against the new narrations.

## Ending order (verified)

```
B00 · B01 · B02 · B03 · B04 · BCRY
BHTF  ← second-to-last, LLM EXERCISE (paste-ready prompt + Go deeper)
BOUT  ← last, NikBearBrown outro (title + Liam, in for Bear.)
```

Valid JSON (`python3 -c "import json; json.load(open(...))"` OK).
