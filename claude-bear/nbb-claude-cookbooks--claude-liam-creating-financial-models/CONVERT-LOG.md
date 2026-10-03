# CONVERT-LOG — nbb cut

Slug: `claude-cookbooks--claude-liam-creating-financial-models`
Converted: 2026-09-03 (register-conversion factory)
From: `../claude-cookbooks--claude-liam-creating-financial-models/beat_sheet.json`
Into: `beat_sheet.nbb.json`

## What changed

- Removed `_variant_todo` from metadata (Step 2 – 5 all now satisfied inline).
- Rewrote every body beat's `narration_text` in the Teardown register (Feynman × MKBHD): each beat now takes the mechanism apart, names the design choice, and (where relevant) prices what the choice cost. Facts, file names, spec list, and step count are unchanged.
- Repurposed `BHTF` as the LLM EXERCISE beat: replaced the "read the skill" handoff with a paste-ready DCF-modeling prompt for any frontier LLM plus a "Go deeper" sensitivity follow-up. Added a `llm_exercise` sub-block (prompt + dig_deeper). `ClaudeComposerAsk` props updated: `segment` → `"Claude, Creating Financial Models"`, `command` → LLM prompt (paraphrased), `output: []` added to match sibling nbb-cut convention.
- Bumped `estimated_duration_s` on beats that grew: B01 18→20, B02 20→22, B03 26→30, BHTF 22→40. BOUT unchanged (still the NikBearBrown Liam-in-for-Bear signoff — matches `outro_source: AUTHOR.MD :: NikBearBrown`).
- Left `BCRY` narration exactly matching the WantQuote line (the signed carry-out sentence — Gate C artifact, preserved verbatim per SKILL.md "on-screen card copy that still fits the register").
- Preserved every `beat_id`, act label, `shot` block, graphic/manim block, audio_file path, build status, and BrutalistHesitantWriter/WantQuote/OutroCTA props — the source B00 typing correction ("teach" → "point") still tests as the machinery of the whole video.

## Judgement calls

- **Kept `folderLabel: "@HumanitariansAI"` and the OutroCTA handle** rather than swapping to `@NikBearBrown`. Rationale: the fully-converted sibling reels in this book (e.g. `nbb-books--claude-liam-building-plugins`) keep the HAI folder chip and handle, and the audience metadata (`audience: "NikBearBrown"`, `outro_source: "AUTHOR.MD :: NikBearBrown"`) already carries the brand signal. Following the sibling convention keeps the cross-reel look stable.
- **`palette` set to `teardown`** as the scaffold specified, but `style_preset: "humanitarians"` and `ground: "#F3EBDD"` (cream) were left as scaffolded — same pattern the converted siblings use. If a later Gate-B pass wants pure teardown white ground, that is a run-time skin flip, not a beat-sheet edit.
- **BHTF `prompt` is DCF-general, not skill-specific**: the exercise has to produce useful output on its own without the video (SKILL.md §Step 3), and no frontier LLM has the `creating-financial-models` folder on hand. The prompt asks the model to walk through building a DCF with a startup revenue scenario — mirrors the video's anchor (five-year revenue projection) while being fully self-contained.
- **`dig_deeper` chose a one-parameter sensitivity on discount rate** as the follow-up. It is a real next exercise (not a summary), it uses the same DCF the initial prompt built, and it teaches which assumption matters most — extends the video's "spec is the fence" idea into a hands-on discovery.

Rendering is a separate pass. This log records only the sheet conversion.
