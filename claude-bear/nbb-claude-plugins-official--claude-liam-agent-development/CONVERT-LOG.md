# CONVERT-LOG — nbb cut of `claude-plugins-official--claude-liam-agent-development`

Converted the scaffold into the NikBearBrown cut. Facts unchanged; register
rewritten; LLM exercise slotted in second-to-last; NikBearBrown outro last.

## What changed

- **All seven `narration_text` fields rewritten in the Teardown register.**
  Feynman × MKBHD — take the file apart, name what each field does, reveal the
  design choice (they optimized dispatch-time context by putting the trigger in
  the description alone), then name the cost (two locations, no sync). No new
  facts, no removed facts. The frontmatter fields, the format convention
  (`Use this agent when...` / `Typical triggers include`), the "two audiences"
  split (description = Claude's dispatch decision; body = agent at runtime), and
  the hand-maintained-mirror maintenance cost from NB03 all survive verbatim in
  substance.
- **BCRY quote sharpened** in the same register. Original: "…never fires if its
  description only lists capabilities." New: "…never gets dispatched if its
  description reads like a résumé." Same fact; sharper Teardown line. The
  `WantQuote` prop `quote` was updated to match so the on-screen and spoken
  lines agree.
- **BHTF converted from "your turn handoff" to the LLM exercise beat**
  (SECOND-TO-LAST). Act renamed to `LLM EXERCISE`. Added the required
  `llm_exercise` object with `prompt` + `dig_deeper`. The prompt is a
  paste-ready block for Claude / ChatGPT / Gemini that produces a real,
  useful artifact on its own (a well-formed agent file, plus a self-critique).
  The dig-deeper is a genuinely next question about description↔body drift and
  a pre-commit check for it — not a summary. Narration reads the prompt in full
  and closes with the "Go deeper: …" follow-up. The on-screen
  `ClaudeComposerAsk.command` prop was rewritten as a tightened, numbered
  version of the same prompt so the composer card doesn't overflow.
- **BOUT switched from `OutroSeries` to `OutroCTA`** (matches the standard NBB
  outro pattern used by the sibling nbb reels). Props are `line` (title +
  "Liam, in for Bear.") and `handle: "@NikBearBrown"`. Narration text unchanged.
- **`folderLabel` and `channel_title` metadata switched from `@HumanitariansAI`
  to `@NikBearBrown`** — this is the NBB cut, so the channel chip and title
  live under the NikBearBrown handle. The BHTF composer's `folderLabel` prop
  was updated the same way.
- **`_variant_todo` removed** from metadata. `purpose` was reworded to describe
  the Teardown framing (take apart the file, evaluate the two-location design,
  name what it costs) so the metadata line no longer reads as a Plain-register
  summary.
- **Stale `actual_duration_s` fields left as the scaffold left them** (absent).
  `estimated_duration_s` values were nudged up on the rewritten body beats
  (NB01 to 32s, NB02 to 30s, NB03 to 25s, BHTF to 55s) to reflect the longer
  Teardown prose; these are only estimates — audio-first regeneration is a
  separate render pass and will overwrite the real durations.

## Judgment calls

- **Rebrand to `@NikBearBrown` on the metadata + composer chips.** The scaffold
  left the source `@HumanitariansAI` labels in place. Following the
  properly-converted sibling `nbb-claude-basics--screenshot-prompt-caching`
  (which changed both) rather than the incomplete `nbb-cwc-workshops--…-reorder-policy`
  (which didn't rewrite anything). Brand spec at `brands/nbb.md` and the NBB
  `SKILL.md` outro rule both point at the NikBearBrown channel as the default,
  so the labels match the destination channel.
- **Kept the `BrutalistHesitantWriter` on-screen text verbatim** (`skills` →
  `triggers` correction). It is the entire visual mechanic of the cold open and
  the corrected question still lands the reel's real subject in the Teardown
  rewrite. The narration around it was reworked to Teardown voice while
  landing on the same final question the writer types.
- **Kept the graphic `production_viz` labels, chips, captions, and Manim scene
  IDs (`BDNB01Scene`/`BDNB02Scene`/`BDNB03Scene`) unchanged.** Those are
  on-screen card copy that already reads cleanly in the Teardown register
  ("description decides dispatch", "dispatch decision vs. worked scenarios",
  "nothing keeps them in sync") and re-labeling them would force a re-render
  of the Manim scenes without changing anything the viewer sees differently.
- **Left `playlist: "Extending Claude — Skills, Plugins & Connectors"`
  unchanged.** The scaffold set it and it is a plausible playlist on the NBB
  channel too; the sibling screenshot-caching reel set a different playlist
  ("Claude Basics") because its content fits there. This one fits Extending
  Claude, so I left it.
- **Left `style_preset: "humanitarians"` and `ground: "#F3EBDD"` as the
  scaffold set them.** The palette field is already `teardown`, which is the
  color law of record; the `style_preset` / `ground` fields appear to be
  used by the source hai-simple compositions and don't conflict with the
  teardown palette at runtime (same pattern in the sibling nbb sheets).

## Not done here (deliberate)

Rendering, audio generation, and compilation. Per the supervisor's brief, this
pass is beat-sheet-only. `generate_audio_kokoro.py` and `compile.py` are a
separate render pass.
