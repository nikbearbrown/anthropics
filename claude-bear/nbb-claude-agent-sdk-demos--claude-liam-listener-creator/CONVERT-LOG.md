# CONVERT-LOG — claude-agent-sdk-demos--claude-liam-listener-creator

Converted `beat_sheet.json` → `beat_sheet.nbb.json` on 2026-09-03.
Register: Plain → Teardown (Feynman × MKBHD). Voice: Liam / Kokoro `am_onyx`
(unchanged; scaffold-set). No render, no audio regen — beat sheet only.

## What changed

- **B00** — narration rewritten in Teardown register (30 words, holds the
  BrutalistHesitantWriter TIMING LAW window of 20–35). Shot block preserved
  verbatim; the on-screen typed text ("watcher" → "template" correction) is
  the writer widget's own copy, not the narration, so it stays as-is.
- **B01** — narration rewritten to name the mechanism (SKILL.md re-read on
  every run; disk file, not a daemon) and the design trade-off (auditability
  vs always-on watch). Shot + graphic block preserved.
- **B02** — narration rewritten as a mechanism explanation of the Steps
  section, closed on the deterministic "same words in, same action out"
  cadence. Shot + graphic block preserved.
- **B03** — narration rewritten to hit the Teardown lens: "reliable, and also
  why it can betray you" → "predictability at the expense of judgment." Shot
  + graphic block preserved.
- **BCRY** — narration LEFT UNCHANGED. The WantQuote card's `quote` prop
  displays this line on screen; changing the narration without changing the
  prop would desync. The line already reads as Teardown (crisp, mechanical,
  names the shape of the thing). Judgment call: preserving on-screen sync
  wins over a marginal register touch-up.
- **BHTF** — narration LEFT UNCHANGED (already fits register; also
  displayed verbatim as the `command` prop on the ClaudeComposerAsk card).
  `folderLabel` prop flipped `@HumanitariansAI` → `@NikBearBrown` per
  `skills/make/nbb/SKILL.md` "Ask/intro scene rule" — the ClaudeComposerAsk
  chip on a NBB reel is `@NikBearBrown`.
- **B_LLM** — NEW beat inserted second-to-last per SKILL.md §Step 3. Contains
  `llm_exercise.prompt` (paste-ready compare-and-contrast of a file-based
  listener vs a live event-watcher — designed to produce useful output on its
  own without the video) and `llm_exercise.dig_deeper` (a real follow-up: how
  to make one listener catch 'contract renewal' AND its paraphrases without
  over-firing). `shot.type = "CARD"` per SKILL.md's literal schema; no
  Remotion pattern yet — the renderer chooses one at build time.
- **BOUT** — replaced with the NikBearBrown outro. `narration_text` and
  `remotion.props.line` now read: "Claude, Listener Creator. Liam, in for
  Bear. Nik Bear Brown, at brutalist dot art." `handle` prop flipped
  `@HumanitariansAI` → `@NikBearBrown`. Estimated duration bumped 6→8s to
  fit the longer line. IN-FOR-BEAR LAW preserved (Liam signs off as himself).
- **metadata** — `_variant_todo` array removed. Everything else the scaffold
  set (audience, register, palette, engine, voice_kokoro, style_preset,
  ground, folderLabel, channel_title, typography, outro_source,
  derived_from) left untouched per the "do not re-scaffold" rule.

## Judgment calls

1. **Metadata `folderLabel` / `channel_title` stayed `@HumanitariansAI`.**
   The scaffold set both. Only the two per-beat props that render on screen
   (BHTF `folderLabel`, BOUT `handle`) were flipped to `@NikBearBrown` — the
   scene-level branding required by the NBB brand for the ClaudeComposerAsk
   chip and the outro CTA. If the metadata channel is meant to describe the
   delivery channel rather than the brand, this split is correct; if it's
   meant to match, the scaffold should be updated (out of scope for this
   register conversion).
2. **BCRY narration preserved unchanged** to keep on-screen quote sync — see
   the beat-by-beat note above. The line already carries the register.
3. **BHTF narration preserved unchanged** for the same reason (on-screen
   `command` prop match) and because a Your Turn handoff has a fixed shape
   (greeting → prompt read → walkthrough ask → Liam sign-off) that already
   reads as Teardown when Liam speaks it.
4. **B_LLM given its own beat rather than folded into BHTF.** BHTF is a
   "hand off to Claude to build the thing" beat (specific to Claude, single
   task); B_LLM is a "paste into any frontier LLM to explore the design
   space" beat (any model, self-contained compare-and-contrast + a dig-deeper
   question). SKILL.md treats them as different beats and prescribes both
   for a NBB reel.
5. **Facts unchanged.** Every number, path, and API detail in the source
   (SKILL.md ~9k, two-file folder, Steps section, boss+urgent condition,
   client counter-example) survives the rewrite. Only the voice changed.

## Not done here

- No audio regenerated (`generate_audio_kokoro.py` still owed on the rewritten
  beats; existing `mp3/beat-*.mp3` paths are stale for B00–B03 and BOUT).
- No new render for BOUT (line changed) or B_LLM (no media exists).
- Directory contains only `beat_sheet.nbb.json` and this log — no build
  scripts, media, or mp3 folder yet. The rendering pass is a separate job.
