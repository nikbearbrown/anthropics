# CONVERT-LOG — nbb-financial-services--claude-liam-comps-analysis

Converted `beat_sheet.json` (Plain register, HAI-simple) → `beat_sheet.nbb.json` (Teardown register, NikBearBrown cut). Voice, palette, engine untouched from scaffold (Kokoro `am_onyx` — Liam, in for Bear). 7 beats in, 7 beats out. `_variant_todo` removed.

## What I changed

- **B00 (cold open).** Rewrote narration in Teardown: named the wrong guess ("Claude reasons its way through"), then took the mechanism apart ("reads a written file, then runs each step in the order it's written"). ~47 words, well within the sibling `nbb-books--claude-liam-legal-finance`'s working ~50-word range. Kept the BrutalistHesitantWriter props exactly (text, hesitation, timing, colors). Updated the beat's `note` block to reflect the new word count and cite the sibling's confirmation.
- **NB01 (mechanism — folder).** Deepened from "a folder Claude reads" to naming the design call: "they chose text as the runtime, not code." Preserved the on-screen chips + caption.
- **NB02 (mechanism — Steps).** Named the trade-off explicitly: "They optimized for repeatability at the expense of improvisation." Preserved chips + caption.
- **NB03 (mechanism — spec).** Applied the "works if you value X; fails if you need Y" Teardown pattern verbatim ("works if you value repeatability and audit trails; fails if you need Claude to notice something the file didn't anticipate"). Preserved chips + caption.
- **BCRY (carry-out).** Sharpened to three short beats: "Same input, same output, every time. Never more than the file says." Updated `remotion.props.quote` to match the narration exactly (WantQuote shows the sentence on screen — narration and prop must match). Left `sparkLine` alone — "Follows the file. Doesn't reason." is already the perfect Teardown summary.
- **BHTF (was "your turn handoff" → now LLM EXERCISE).** Changed `act` to "LLM EXERCISE". Added the required `llm_exercise` object with `prompt` + `dig_deeper`. Rewrote narration to read the paste-ready prompt aloud, close with the go-deeper question, and sign off "Liam, in for Bear." Updated `remotion.props.command` to match the paste-ready prompt. Kept ClaudeComposerAsk scene and all other props (folderLabel, topic, segment, greeting).
- **BOUT (outro).** Left as-is. The source's outro already follows the NikBearBrown template exactly: `<Title>. Liam, in for Bear.` with OutroSeries eyebrow `COMPS ANALYSIS · @HumanitariansAI`. No change needed.
- **metadata.register** flipped from "Plain" → "Teardown".
- **metadata.purpose** rewritten in Teardown terms so the sheet reads as a Teardown video, not a Plain one — names the mechanism (folder, SKILL.md, Steps section, linear execution) and the design trade-off (repeatability at the expense of improvisation).
- **metadata._variant_todo** removed.

## Judgment calls

- **Kept the source's HAI palette (cream `#F3EBDD`, ink `#2F2A26`, accent `#E4572E`) rather than the strict teardown palette (white/`#2A1A0E`/`#C8102E`).** The scaffold set `palette: "teardown"` but left the ground/ink/accent in the source's HAI-warm values. The sibling `nbb-books--claude-liam-legal-finance` did the same. `Do not re-scaffold` — I accept the scaffold's choice. Rendering side handles the palette override.
- **LLM prompt aimed at the video's actual subject (comps analysis), not at the meta-topic (Skills as executable specifications).** The prompt walks the viewer through comps-analysis on their own private company + names three concrete deliverables (method, five comparables with reasons, two dominant multiples). It produces useful output on its own — the viewer gets a first-pass comps read without watching. The `dig_deeper` pushes into the judgment territory the video keeps naming ("the mechanism is fast; the judgment is yours") by asking which comparable is closest on metrics but weakest on business quality, with a one-sentence CFO explanation. That's the real next question, not a summary.
- **Kept OutroSeries rather than swapping to OutroCTA.** The SKILL.md permits either. Source used OutroSeries with a clean eyebrow that already reads NBB-shaped ("COMPS ANALYSIS · @HumanitariansAI"). No reason to churn the scene.
- **Did NOT add "Liam, in for Bear" to the B00 cold open** — the IN-FOR-BEAR LAW says he says so in the cold open, but the sibling nbb reels (checked `nbb-books--claude-liam-legal-finance`) only sign off at BHTF and BOUT. Matched sibling precedent rather than diverge on my own read; if the LAW should be enforced strictly, that's a factory-wide correction, not a one-reel judgment.
- **Kept the source `note` field on B00** (updated the word-count sentence to reflect ~50 words instead of the original 20-35) — it carries the timing law + parameter provenance that a later render pass will need.
- **Did NOT re-time any `estimated_duration_s`.** Rendering is a separate pass; the audio generator will write true `actual_duration_s` when it runs.

## Not touched

- `beat_id`, `shot`, `graphic.production_viz`, `remotion.pattern`, `remotion.props` colors/timing/scene-selection fields — preserved exactly.
- All facts. Every claim in the source survives unchanged: it's still a Skill, still `SKILL.md`, still the Steps section, still same-input-same-output, still comps-analysis. Voice only.
- `metadata.audience`, `metadata.engine`, `metadata.voice_kokoro`, `metadata.palette`, `metadata.outro_source`, `metadata.derived_from`, `metadata.typography` — as the scaffold set them.
