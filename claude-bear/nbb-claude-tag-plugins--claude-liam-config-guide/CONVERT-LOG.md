# CONVERT-LOG — nbb-claude-tag-plugins--claude-liam-config-guide

Source: `../claude-tag-plugins--claude-liam-config-guide/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03, Liam-in-for-Bear.

## What changed

**Register — every narration rewritten (Teardown).** B00, NB01, NB02, NB03, BCRY all re-voiced to lead with mechanism ("Here's what's actually happening / Here's the actual machinery / Here's the failure mode"), name the design trade-off ("They optimized for a reference you can actually load into working memory; they sacrifice the coverage a monolithic doc would give you"), and judge the choice on its own terms ("Silent failure is the price of keeping the router simple"). No numbers, layer names, file counts, or Slack/debug-plugins facts were changed — only voice.

- **B00** — was: "Someone assumed Claude's settings live in one file." → "Here's what someone assumed: Claude's settings live in a file you can grep. They don't." Same beat, same visual reveal (writer hesitates on `file`, corrects to `layer`), Teardown lead-in. Duration nudged 11→14s (~40 words, still inside the ≥9s hesitant-writer window).
- **NB01** — mechanism rewritten as stacked layers with the "what sits on top / underneath / at the bottom" structure. The router-vs-database framing is now explicit. Five reference files enumerated verbatim. Duration nudged 27→30s.
- **NB02** — reframed as the deliberate design choice with its cost named: short-and-loadable vs monolithic-and-complete. Slack-only scope + fresh-thread/fresh-container behavior preserved. Duration nudged 25→27s.
- **NB03** — "Silent failure is the price of keeping the router simple." Same failure mode, Teardown framing. Duration nudged 14→16s.
- **BCRY** — already carry-out-shaped and Teardown-compatible. Left verbatim.

**BHTF repurposed as the LLM EXERCISE beat (second-to-last).** Per the nbb SKILL.md pattern the sibling `nbb-claude-basics--screenshot-prompt-caching` established: `act` → `"LLM EXERCISE"`, added `llm_exercise: { prompt, dig_deeper }`, narration extended with the paste-ready prompt + `Go deeper: …` follow-up. The prompt is a real design-your-own-layered-settings brief that produces useful output on its own (structure, resolution algorithm, silent-failure mode); the dig-deeper pushes to a genuinely explorable next question (migration path when folding two layers into one). On-screen `command` prop numbered (1)(2)(3) for readability, `folderLabel` prop flipped to `@NikBearBrown`.

**BOUT swapped to OutroCTA.** Pattern `OutroSeries` → `OutroCTA`, props switched to `{ line, handle }` with `handle: "@NikBearBrown"` — same sibling convention. Narration unchanged.

**Metadata.** `folderLabel` and `channel_title` flipped to `@NikBearBrown`. `_variant_todo` removed. `register` left as `Teardown` and `palette` left as `teardown` (both pre-set by the scaffold).

## Judgement calls

- **Did NOT touch the hesitant-writer text (`file → layer`).** It IS the Teardown-register visual — moving the viewer from the misconception ("file") to the mechanism ("layer") is exactly what the register asks for. Rewriting it would break the correction seed and the note's `>=8s` timing guarantee.
- **Did NOT retint graphic `colors` arrays.** They still carry the humanitarians `#F3EBDD / #2F2A26 / #E4572E` triplet. Followed the sibling convention: `metadata.palette = "teardown"` drives the render-time skin; per-beat color arrays are left alone (compile.py picks the palette by metadata, not by props). Retinting here would drift from every other nbb-* sheet in this book.
- **Did NOT split BHTF into a separate `B_LLM` beat + a shorter handoff.** The sibling nbb-* sheets that DID add the LLM exercise all did it by repurposing BHTF in place — one beat carrying prompt + dig_deeper + the composer visual. Kept the same shape so downstream (compile.py, ClaudeComposerAsk props) needs no changes.
- **Estimated durations bumped by ~2-3s per body beat** to match the slightly longer Teardown narrations. These are estimates only — the audio pass measures real durations and rewrites them.
- **`estimated_duration_s: 42` on BHTF** — the paste-ready prompt + dig-deeper is a long read (~135 words at ~3.5 wps). If Kokoro comes in shorter, `compile.py` will use the measured value; if longer, the composer visual holds cleanly.

Ending order verified: `B00 → NB01 → NB02 → NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`.
