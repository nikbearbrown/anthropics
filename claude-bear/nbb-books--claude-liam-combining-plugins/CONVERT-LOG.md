# CONVERT-LOG — books--claude-liam-combining-plugins → nbb

**Source:** `../books--claude-liam-combining-plugins/beat_sheet.json` (36 beats, Plain register, hai-simple)
**Output:** `beat_sheet.nbb.json` (35 beats, Teardown register, NikBearBrown audience)
**Voice:** Liam / Kokoro `am_onyx` — IN-FOR-BEAR (scaffold-set, unchanged)

## What changed

- **Register rewrite (Step 2).** Every body-beat narration re-voiced into Teardown (Feynman × MKBHD): explain the machinery, name the trade-off, no "innovative"/"one could argue" hedges. Facts, numbers, and named domains preserved verbatim. Six one-line act-header narrations (`C02–C06`, plus `B18` payoff) left as-is — they were already mechanical/register-neutral and passed the Teardown gate on read-through. Preserving them is explicitly allowed by SKILL.md ("on-screen card copy where it still fits the Teardown register").
- **B00 cold-open (34 → 33 words).** Kept the >=9s TIMING-LAW window flagged in the source `note` intact.
- **LLM exercise beat (Step 3).** Repurposed the existing `BHTF` (Your Turn) as the second-to-last beat. Added a proper `llm_exercise` block with `prompt` + `dig_deeper` per SKILL.md schema, and folded the "Go deeper: …" follow-up into the narration. Kept `ClaudeComposerAsk` as the shot pattern (matches peer nbb-claude-bear reels, e.g. `nbb-financial-services--claude-liam-deal-sourcing`). Act renamed to `LLM EXERCISE`.
- **Outro consolidation (Step 4).** Source had two outro beats (`BOUT` OutroSeries + `BCTA` OutroCTA). SKILL.md wants LLM at N-2 and outro at N-1 — one outro beat. Collapsed to a single `BOUT` using `OutroCTA` (peer-nbb-claude-bear convention), line `"Claude, In Concert. Liam, in for Bear."`, `tail_silence_s: 1.0` preserved. Total beats: 36 → 35.
- **`_variant_todo` removed** (Step 5 gate).

## Judgement calls

- **Kept `handle` / `folderLabel` as `@HumanitariansAI`** rather than switching to `@NikBearBrown`. Reason: every peer `nbb-*` reel in the same book folder (`claude-bear/`) uses `@HumanitariansAI` in the OutroCTA and ClaudeComposerAsk chip. No `AUTHOR.MD` exists on this book path to source a `NikBearBrown` block from, and the scaffold left channel_title/folderLabel untouched. Matching the peer convention keeps the reel consistent with the shipped @HumanitariansAI channel this book publishes to.
- **Kept source `ground` (`#F3EBDD`) and beat `production_viz.colors` (hai palette)** rather than retinting to teardown white/ink/red. Same reason: matches peer nbb-claude-bear reels that also carry the source palette in metadata while `palette: teardown` is authoritative for the compile step. Re-tinting the color arrays was not one of the mandated Step 2–5 operations and I don't have a scaffold instruction to change them.
- **`brand: "hai-fellows"` and `style_preset: "humanitarians"` preserved.** These are source-provenance fields the scaffold didn't touch; audience/register/palette carry the NBB switch.

## Not done (out of scope for this pass)

- No audio regeneration, no compile, no render — instructions explicit: rewrite only.
- New `BHTF` narration is ~130 words vs. source's ~85; `estimated_duration_s` bumped 30 → 34 as a rough marker only. The renderer will re-measure from the actual Kokoro mp3 in the build pass.
