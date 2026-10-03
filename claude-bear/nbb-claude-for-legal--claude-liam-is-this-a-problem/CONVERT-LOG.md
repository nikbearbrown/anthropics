# CONVERT-LOG — nbb-claude-for-legal--claude-liam-is-this-a-problem

Source: `../claude-for-legal--claude-liam-is-this-a-problem/beat_sheet.json`
Converted: 2026-09-03

## What changed

- Rewrote all 5 body-beat narrations (B00, B01, B02, B03, BCRY) in the Teardown
  register. Explained the machinery (a Skill is a folder + one plain-language
  file; the Steps section is a numbered pipeline run top to bottom; the middle
  check is a lookup against pre-authored conditions, not a runtime judgment);
  named the design choice at each step (text you can audit vs. hidden logic;
  judgment paid once at authoring time so every run is reproducible; the
  consistency-for-silence trade the checklist form makes on purpose).
- Facts unchanged: skill name (`is-this-a-problem`), single file (`SKILL.md`),
  Steps-section semantics (read → check against conditions → answer), the
  same-input-same-output-every-run property, and the "not wrong, just silent
  when not named" behavior all survive verbatim from source. B00's Remotion
  props (`text`, `triggerWords`, `replacementWords`, seed, timings) are
  untouched — the correction lands identically.
- Replaced BHTF from a CLI-style "paste this into Claude" prompt to a proper
  **LLM EXERCISE** beat (act renamed to `LLM EXERCISE`; `llm_exercise` block
  added with `prompt` + `dig_deeper`). The prompt is paste-ready for any
  frontier LLM (Claude / ChatGPT / Gemini) and produces useful output without
  the video: viewer names a gut-feel decision, model helps write out the actual
  silent-checklist they're running (in order, with coverage boundaries per
  item), then walks three real cases through it. Dig-deeper inverts the
  exercise — have the model do the same three cases by gut feel first, then
  compare; the gaps are where either the list or the gut is incomplete.
- Replaced BOUT line with a Teardown outro that carries the payoff forward:
  "Claude, Is This A Problem — checked, not judged. Liam, in for Bear."
  OutroCTA scene and `@HumanitariansAI` handle unchanged (source-channel
  convention — matches the sibling `nbb-...-ip-clause-review` pattern; the
  human can flip `handle` at post-time if the intent is a NikBearBrown channel
  post).
- Added `subtitle`: "The Is-This-A-Problem Skill" to metadata (matches sibling
  nbb reference pattern).
- Removed `_variant_todo` from metadata.
- Bumped `estimated_duration_s` on the beats that grew (B01 17→24, B02 17→22,
  B03 20→28, BCRY 11→12, BHTF 27→60, BOUT 6→7). Kokoro will re-measure at
  audio time; these are hints only.

## Judgement calls

- **B00 word budget.** BrutalistHesitantWriter TIMING LAW says 20–35 words.
  Source was 36; my rewrite is 32. Under-limit end preserves the correction
  pivot ("weighs a situation" → "running a written checklist"), which maps
  cleanly onto the writer's on-screen "decide → check" replacement.
- **BCRY quote = narration.** The `WantQuote.quote` prop must match the spoken
  line exactly (source pattern, preserved here), so I kept both to the same
  rewritten sentence. `sparkLine` "Checked, not judged." from source is already
  Teardown-shaped — kept it and reused the phrase in the outro.
- **BHTF ClaudeComposerAsk `command`.** Slightly shortened from the narration
  so the composer card is readable in the frame — the paste-ready long form
  lives in `llm_exercise.prompt`. Added `"output": []` per the sibling
  reference (some Remotion versions require the field even when empty; harmless
  when present).
- **LLM prompt subject.** The source's own carry-out is "Claude checks a
  written list; you should probably audit your own gut-feel lists the same
  way." I built the LLM exercise around exactly that — no Skill file required
  — so the exercise reinforces the video's payoff and stands on its own
  without needing to have watched.
- **Handle stayed `@HumanitariansAI`** rather than switching to
  `@NikBearBrown` — matched the sibling nbb reference in this book, which
  keeps the source channel on OutroCTA even after Teardown-register
  conversion.

Done. Not rendered, not compiled, no audio generated. Next pass:
`generate_audio_kokoro.py` → compile.
