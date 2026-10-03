# CONVERT-LOG — knowledge-work-plugins--claude-liam-account-research (nbb cut)

Converted: 2026-09-03. Voice-only rewrite; every fact, name, trigger phrase, pipeline
step, and on-screen card copy carried over from the source `beat_sheet.json` unchanged.

## What changed

- **Every `narration_text` rewritten in the Teardown register** per
  `runtime/prose/teardown/PROSE.md` and `brands/nbb.md` — take the skill apart,
  explain the machinery (SKILL.md file → trigger-phrase match → Read/Execute/Return
  pipeline), name the design choice ("they chose a written spec over teaching the
  model"), state the trade-off ("the price is exact-match triggers only; the gain is
  that every run is identical and inspectable"). Sanctioned patterns used: "Here's
  what's actually happening…", "They chose X over Y", "This works if you value X;
  it fails the moment you need Y."
- **B00 cold open** now opens with "Liam here, in for Bear" per IN-FOR-BEAR LAW.
  Shot block (BrutalistHesitantWriter, 'remember' → 'check' correction) untouched;
  narration stays inside the 20–35 word TIMING LAW window.
- **BCRY carry-out** `WantQuote.quote` updated to match the new narration verbatim
  so the on-screen sentence and the voice line stay in sync. `sparkLine` ("Looked
  up, not remembered.") preserved — it still fits.
- **B_LLM inserted as second-to-last beat**, carrying the required `llm_exercise`
  object with `prompt` + `dig_deeper` per `skills/make/nbb/SKILL.md` §Step 3. The
  prompt is model-agnostic (Claude / ChatGPT / Gemini) and reproduces the skill's
  three-step Read/Execute/Return pipeline against a company the viewer names — so
  it produces a useful account brief on its own, without the plugin installed.
  Dig-deeper is a real next question ("which signals gave you real information vs.
  filled space?"), not a summary.
- **BOUT rewritten as the NikBearBrown outro.** `OutroCTA.handle` swapped from
  `@HumanitariansAI` to `@NikBearBrown` and `line` now ends with `brutalist.art` per
  `brands/nbb.md` (default channel www.brutalist.art). `estimated_duration_s`
  bumped 6 → 10 to fit the two-sentence Liam sign-off. `OutroCTA` pattern kept.
- **`_variant_todo` removed** from metadata (Steps 2–5 complete).
- **`purpose` sentence rewritten** to reflect the Teardown angle (machinery + trade-off
  + carry-out) instead of the source's Plain-register framing.
- **`register` was already `"Teardown"`** on the scaffolded sheet — left as-is.

## Judgment calls

1. **BHTF slot repurposed as B_LLM** instead of appending a new beat before BOUT.
   The source `BHTF` was already a "your turn" handoff with a `ClaudeComposerAsk`
   shot and a paste-ready Claude prompt — the same slot §Step 3 asks the LLM
   exercise beat to occupy. I swapped `beat_id` BHTF → B_LLM, kept the
   `ClaudeComposerAsk` pattern (fits paste-ready UI better than the schema's bare
   `type: "CARD"`), and added the `llm_exercise` object with `prompt` + `dig_deeper`.
   Net: 7 beats in, 7 beats out — no silent inflation. Follows the sibling
   `nbb-books--claude-liam-marketing` convention for the same reason.
2. **`ClaudeComposerAsk` retained for the LLM exercise shot.** SKILL.md's schema
   example suggests `{ "type": "CARD", "source": "own", "motion": "hold" }`, but
   the file's Ask/intro scene rule (2026-07) endorses `ClaudeComposerAsk` for
   paste-ready prompt beats. Since the whole point of B_LLM is "paste this into
   Claude / ChatGPT / Gemini," the composer scene reads more clearly than a bare
   card.
3. **`folderLabel: "@HumanitariansAI"` left on the B_LLM shot.** Matches the
   metadata `folderLabel` / `channel_title` fields the scaffold did not change.
   The BOUT `handle` is the one place I flipped to `@NikBearBrown` — SKILL.md §Step
   4 explicitly directs the final beat to become the NikBearBrown outro.
4. **`build.status` on B_LLM and BOUT set to `PENDING`.** Their `command` / `line`
   props changed, so the source `media/*.mp4` no longer matches; leaving `VIDEO`
   would falsely tell the compiler the assets were fresh. All other beats keep
   their original `build.status` — their shot / graphic blocks are unchanged, and
   the audio pass (Kokoro `am_onyx`) will overwrite the MP3s in place.
5. **`brand: "claude-liam"` left in metadata.** The scaffold preserved it from the
   source; the SKILL says "Do not re-scaffold." `audience: "NikBearBrown"` is the
   field the pipeline reads for the nbb cut, and it is set correctly.
6. **`estimated_duration_s` bumped on B01 (19 → 22), B02 (23 → 30), B03 (24 → 30),
   B_LLM (new, 25), BOUT (6 → 10)** to match the longer Teardown-register narration
   in each beat. These are hints; the audio pass will overwrite them with measured
   durations from the Kokoro MP3s.

## Ending order (verified)

… → `B03` (anchor payoff / both directions) → `BCRY` (carry-out, body) → **`B_LLM`
(second-to-last)** → **`BOUT` — NikBearBrown outro (last)**
