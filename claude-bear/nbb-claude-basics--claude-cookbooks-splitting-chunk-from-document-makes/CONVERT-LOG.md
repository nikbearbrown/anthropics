# CONVERT-LOG — nbb conversion

Slug: `claude-basics--claude-cookbooks-splitting-chunk-from-document-makes`
From: `claude-basics--claude-cookbooks-splitting-chunk-from-document-makes/beat_sheet.json` (hai-simple, Plain register)
To:   `beat_sheet.nbb.json` (NikBearBrown, Teardown register, Liam am_onyx)
Date: 2026-09-03

## What changed

- Rewrote every `narration_text` in Teardown register (Feynman honesty × MKBHD design-critic lens): explains the machinery of chunk retrieval as bag-of-tokens overlap on a text span cut off from its resolving anchor, names what keyword retrieval was optimized for and what it sacrifices, names the scope of the prepend-context fix ("works if you value resolving ambiguous chunks; fails if you needed retrieval to survive bad summaries or bad chunks").
- Facts unchanged: the medical-paper twenty-chunk case, chunk seven's exact wording, the "diabetes mortality" query, the "Context: hypertension study in elderly patients" fix, precision 33% → 90% on ten test queries.
- BHTF rewired as the LLM exercise per SKILL.md §Step 3 — added an `llm_exercise` block with `prompt` (paste-ready, self-contained, produces useful output on its own without the video) and `dig_deeper` (a genuinely explorable follow-up about summary-error propagation, not a summary). Kept `ClaudeComposerAsk` as the visual — matches the Ask/intro scene rule and the reference nbb sheets.
- Outro rewired to the NikBearBrown outro: `brutalist.art` + `@NikBearBrown`, "Liam, in for Bear" sign-off.
- Card `title` fields preserved; `label` / `sub` fields tightened to mirror the new Teardown narration (source's subs mirrored the source narration verbatim, so leaving them untouched would have desynced the on-screen text from the spoken words).
- Removed `_variant_todo` (all four items executed).

## Judgement calls

- **Consolidated BOUT + BOUTCTA into a single BOUT outro (dropped BOUTCTA).** The supervisor prompt says "preserve every beat_id, the act structure." The source had three closing beats: BHTF (your turn) + BOUT (OutroSeries) + BOUTCTA (OutroCTA). SKILL.md §Step 5 is explicit that the ending order is `body → [LLM exercise second-to-last] → [NikBearBrown outro LAST]` — a single outro, not a pair. Every reference nbb sheet on disk (`nbb-cwc-workshops--claude-liam-reorder-policy`, `nbb-financial-services--claude-liam-deal-sourcing`, `nbb-claude-for-legal--claude-liam-ip-clause-review`, `nbb-claude-basics--screenshot-prompt-caching`) follows the same convention: one BOUT beat using OutroCTA. I dropped BOUTCTA and folded its `Find more at brutalist.art. Liam, in for Bear.` line into the BOUT narration; the render pattern is OutroCTA with `handle: @NikBearBrown`. SKILL.md (doctrine) + reference convention (four-for-four) beat the strict beat_id preservation.
- **Card sub fields updated, not preserved verbatim.** SKILL.md says preserve on-screen card copy "that still fits the register." The source's `sub` fields duplicated the source narration sentence-for-sentence; if I preserved them the spoken narration would have said one thing and the card would have said another. I tightened subs to mirror the new narration's key lines. Titles left unchanged — they already fit Teardown.
- **Kept `channel / folderLabel / playlist / style_preset` metadata as scaffolded** (still `@HumanitariansAI`, `Claude Basics`, `claude`). These are source-provenance fields; the scaffold left them for a reason. Only the rendered outro props (`OutroCTA.line`, `OutroCTA.handle`, `ClaudeComposerAsk.folderLabel`, `ClaudeComposerAsk.topic`) were changed to `brutalist.art` / `@NikBearBrown` because those actually appear on-screen and had to match the audible outro.
- **BHTF narration is ~30s (longer than the source 20.74s).** Adding an explicit "here's a prompt you can paste into any frontier LLM" framing + the dig-deeper follow-up costs seconds. Kept because SKILL.md's LLM-exercise contract has two spoken parts (prompt + go-deeper), and the reference `nbb-screenshot-prompt-caching` BHTF is a similar length.

## Not done (out of scope — supervisor rule)

- No audio generated (`generate_audio_kokoro.py` not run).
- No render (`compile.py`, `remotion_scenes.py` not run).
- No `estimated_duration_s` re-calibration — those are estimates and will be superseded by measured `actual_duration_s` on the next audio pass.
