# CONVERT-LOG — nbb-financial-services--claude-liam-morning-note

Register conversion: Plain (hai-simple) → Teardown (nbb). 2026-09-03.

## What changed

- **All 7 narrations rewritten in Teardown register.** Same facts, same beat IDs,
  same act structure, same shot/graphic blocks. Voice pivot: from
  Plain-register "here's the thing, plainly" to Teardown "here's the machinery
  + here's the design choice + here's what it cost." No fabricated facts —
  every number, wake phrase, and step order carried over from the source.
- **BHTF repurposed as the LLM EXERCISE beat** (second-to-last). Act renamed
  from `your turn handoff` → `LLM EXERCISE`. Added the `llm_exercise` block
  (paste-ready prompt + `dig_deeper`) matching the pattern from the finished
  `nbb-financial-services--claude-liam-deal-sourcing` reel. Prompt asks the
  viewer to have any frontier LLM draft a SKILL.md for one repeatable morning
  routine they already run — produces a useful artifact on its own, without
  the video. Dig-deeper pushes the viewer to find the seam between spec and
  judgment. Updated `runningText` from "paste this into Claude…" to "paste
  this into Claude, ChatGPT, or Gemini…" and shortened the composer `command`
  to fit the on-screen card. `estimated_duration_s` bumped from 27 → 42 to
  match the longer LLM-exercise narration.
- **BOUT switched from `OutroSeries` → `OutroCTA`** with `handle:
  "@NikBearBrown"`, matching the NikBearBrown outro convention used across
  finished nbb reels (per SKILL.md §Step 4 + AUTHOR.MD :: NikBearBrown).
  Narration line unchanged.
- **Channel metadata pivoted to NikBearBrown.** `folderLabel` and
  `channel_title` updated from `@HumanitariansAI` → `@NikBearBrown` in both
  metadata and the BHTF composer props.
- **Metadata `purpose` rewritten** to name the Teardown-register framing
  (guaranteed reproducibility at 7am at the expense of judgment about which
  overnight developments actually matter today).
- **`_variant_todo` removed** — all four items completed.

## What did NOT change

- `palette: "teardown"` was already set by the scaffold; kept as-is.
- `ground: "#F3EBDD"` and the manim `colors` triples kept as scaffolded —
  matches the finished nbb reels in this book (deal-sourcing, gl-recon,
  deal-screening etc.). Palette metadata says teardown; render pipeline still
  produces the humanitarians ground on the manim beats. Not my call to change
  it in a register-conversion pass.
- `engine`, `voice_kokoro`, `in_for_bear`, all beat IDs, all
  `shot`/`graphic`/`remotion` blocks (patterns, props except the four fields
  called out above), all `production_viz` labels/chips/captions kept. Voice is
  Liam / Kokoro `am_onyx` throughout, per the IN-FOR-BEAR LAW.
- `actual_duration_s` fields from the source were dropped (they were the old
  Plain-register audio measurements — new Teardown audio will be re-measured
  when someone runs `generate_audio_kokoro.py`). No render/audio work done in
  this pass, per the register-conversion contract.

## Judgment calls

- **BCRY quote updated to match the new narration.** The `WantQuote.quote`
  prop and the beat narration are the same sentence rendered on-screen; when I
  rewrote the narration in Teardown register, I updated the on-screen quote to
  match. `sparkLine: "A file, not a mode."` left alone — it's the reel's
  spine and works in both registers.
- **On-screen card copy on B00 left intact.** The `BrutalistHesitantWriter`
  text still reads "Is there a special mode for morning notes in Claude?"
  with the `mode` → `file` hesitation. That copy is register-agnostic — it's
  the *question* the reel opens on, not the narrator's voice — and rewording
  it would break the visual timing (`triggerWords`, `hesitateBetween`,
  `charMs`, `seed`). Kept.
- **Composer `command` on BHTF trimmed vs the narration.** The full LLM
  prompt lives in `llm_exercise.prompt`; the on-screen `command` string is a
  tighter version so it reads cleanly in the composer card without wrapping
  off the frame.
