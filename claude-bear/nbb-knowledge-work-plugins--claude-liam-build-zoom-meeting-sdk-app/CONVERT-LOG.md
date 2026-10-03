# CONVERT-LOG.md

Conversion: HAI (`hai-simple` / Plain register) → NikBearBrown (Teardown register).
Source: `../knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app/beat_sheet.json`
Output: `beat_sheet.nbb.json` (7 beats).

## What changed

- Rewrote every `narration_text` in the Teardown register (Feynman × MKBHD):
  take-it-apart mechanism (NB01–NB02), name the trade-off (NB03: "optimized for
  platform-accuracy at the expense of scope"), judge on its own terms
  ("works if you already know what you're building; fails if you're asking
  Claude to decide whether to build it"). Facts preserved: same 6 platforms,
  same file structure (RUNBOOK.md + SKILL.md + per-platform folders),
  same routing claim, same carry-out.
- Converted `BHTF` from a "your turn handoff" beat into a proper `LLM EXERCISE`
  beat per `skills/make/nbb/SKILL.md` §Step 3: added the `llm_exercise` block
  (paste-ready prompt + `dig_deeper` follow-up), rewrote the on-screen
  `ClaudeComposerAsk` command to match. Prompt is derived from the whole
  video's subject and produces something useful without the video (a working
  SKILL.md the viewer can execute + judge). Dig-deeper is a real next
  question, not a summary.
- Replaced `BOUT` outro: swapped `OutroSeries` for `OutroCTA` (the standard
  NBB outro pattern per the reference `nbb-cwc-workshops--claude-liam-reorder-policy`
  reel), added `handle: "@NikBearBrown"`, updated narration to close with the
  title + sparkLine echo + "Liam, in for Bear" signoff (IN-FOR-BEAR LAW).
- Removed `_variant_todo` from metadata.

## Judgment calls

- **Palette hex values on-screen were still HAI cream/terracotta** (bg
  `#F3EBDD`, accent `#E4572E`) even though the scaffold set `palette: teardown`.
  Flipped the on-screen color values in `B00` (BrutalistHesitantWriter props)
  and in `NB01`–`NB03` (`graphic.production_viz.colors`) to teardown palette
  (bg `#FFFFFF`, ink `#2A1A0E`, accent `#C8102E`). Matches the reference
  `nbb-cwc-workshops--claude-liam-reorder-policy` treatment. This is
  on-screen card copy that did not fit the Teardown register — the SKILL
  authorises replacing it. Note: `manim/NB0*.mp4` still holds the old
  HAI-palette renders on disk; those need re-rendering on the next Manim
  pass so the new palette actually appears in the master.
- **`metadata.style_preset` was `humanitarians` and `metadata.ground` was
  `#F3EBDD`** despite `palette: teardown`. Updated both to `teardown` /
  `#FFFFFF` to match the reference nbb reel and keep downstream renderers
  from crossing brand skins. Flagging as scaffolder inconsistency
  (`brand_variant.py` appears not to overwrite these two fields for
  humanitarians→teardown conversions).
- **`metadata.folderLabel` and `metadata.channel_title` were `@HumanitariansAI`.**
  Changed both to `@NikBearBrown` (this is the NBB cut; the channel identity
  cannot be HAI). Also updated the on-screen `folderLabel` in `BHTF`
  ClaudeComposerAsk props from `@HumanitariansAI` to `@NikBearBrown` for
  the same reason.
- **`playlist` left as "Extending Claude — Skills, Plugins & Connectors"** —
  this is a shared cross-brand playlist appropriate for both channels; no
  reason to fork.
- **`triggerWords` in `B00`** kept as "design" but replaced its
  `replacementWords` from "follow steps for" → "look up the rules for" to
  make the hesitant-writer correction land the specific Teardown
  observation (reference, not steps executed cold).

## Not done (out of scope for the register-conversion pass)

- No audio generated (`generate_audio_kokoro.py`).
- No compile / Manim re-render / Remotion render.
- No `staged.json` / TOPOST staging.
- `estimated_duration_s` values are ballpark estimates for the rewritten
  narrations; real durations will be set by Kokoro when audio is generated.
