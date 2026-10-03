# CONVERT-LOG — claude-liam-investigation-summary → nbb

Source: `../claude-for-legal--claude-liam-investigation-summary/beat_sheet.json` (Plain register, HAI brand, 11 beats, all beats built).
Target: `beat_sheet.nbb.json` (Teardown register, NikBearBrown brand, 11 beats).

## What changed

- **Register — every beat's `narration_text` rewritten** in Teardown (Feynman × MKBHD): explain the machinery, reveal what was optimized for, name the trade-off. Facts unchanged: one file, `SKILL.md`, no branching in the engine, one summary per audience per run, privilege as the boundary, neither output audits itself.
- **B00 cold open** — added "Liam, in for Bear." per IN-FOR-BEAR LAW. Rewrote in Teardown voice while keeping the 20–35-word/8–9s window for the `BrutalistHesitantWriter` typing beat. All Remotion props preserved verbatim (including the seed) so `media/B00.mp4` still renders identically if re-run.
- **B02** — added the design-critic sentence: "One summary optimizes for uniformity at the expense of the boundary that makes the record legally safe to hold."
- **B03/B04/B05** — anchor + mechanism rewritten to expose "the machinery is boring on purpose" and "they optimized for predictability at the expense of judgment; the file is the whole policy — if it doesn't cover a case, nothing does."
- **B07** — closed with the "this works if you value X; it fails if you need Y" cadence tied directly to what the artifact can and cannot certify.
- **BCRY** — carry-out already blunt; light punctuation edit only; `WantQuote` prop `quote` left unchanged (it's on-screen card copy and reads correctly as Teardown).
- **BHTF → LLM EXERCISE** (second-to-last). Reshaped the existing "your turn" beat into the nbb LLM-exercise contract: added a structured `llm_exercise` object with `prompt` + `dig_deeper`; narration reads the prompt out loud and ends "Go deeper: …". Prompt is paste-ready for any frontier LLM (Claude/ChatGPT/Gemini) — asks for two SKILL.md-style instruction files for two audiences, then a read-back and one clarifying question, mirroring the video's central point that the file (not the model in the moment) decides where the line falls. Kept the `ClaudeComposerAsk` shot; updated `folderLabel` to `@NikBearBrown` to match the brand, shortened `command` to match the new narration, kept `runningText`/`greeting`/`segment`/`topic` intact.
- **BOUT → NikBearBrown outro** (last). Replaced the Liam-in-for-Bear HAI sign-off with the NBB channel sign-off: "Claude, Investigation Summary. Liam, in for Nik Bear Brown. brutalist.art." Handle changed to `@NikBearBrown`. Kept the `OutroCTA` pattern; bumped `estimated_duration_s` from 6 to 7 to match the slightly longer line.
- **Metadata** — dropped `_variant_todo` (scaffold checklist complete); set `register: "Teardown"` and `purpose` rewritten to name the design choice being taken apart; updated `folderLabel` and `channel_title` to `@NikBearBrown` for brand identity. Left `audience`, `engine`, `voice_kokoro`, `palette`, `typography`, `outro_source`, `derived_from` exactly as the scaffold set them. Left `ground: "#F3EBDD"` and `style_preset: "humanitarians"` in place because those are the physical background/preset of the already-rendered Manim/Remotion frames — teardown palette overrides at compile time; changing `ground` here would misrepresent the built media.

## Judgement calls

- **BHTF `beat_id` preserved, `act` changed to "LLM EXERCISE"** rather than inserting a new `B_LLM` beat. The nbb SKILL.md schema example uses `B_LLM`, but the instruction says "preserve every `beat_id`, the act structure, `shot` blocks." Existing BHTF was already a paste-into-Claude "your turn" beat with the right Remotion pattern (`ClaudeComposerAsk`); reshaping it in place — keep the id, keep the shot, add the structured `llm_exercise` object, upgrade the act label — matched the preservation rule better than inserting a new beat and orphaning BHTF.
- **Outro CTA text**: no `AUTHOR.MD` was read (not present in the target path scope) so used the default channel from `brands/nbb.md` — `brutalist.art` / `@NikBearBrown` — and formed the sign-off from the pattern in the sibling scaffold: `"<Segment title>. Liam, in for Nik Bear Brown. brutalist.art."` Consistent with IN-FOR-BEAR LAW (Liam names Bear, does not imitate him).
- **`ground` and `style_preset` left as `humanitarians`**: this reel's Manim frames were already rendered against the humanitarians ground. The palette metadata is `teardown` per the scaffold, so a rebuild would use teardown; the render metadata reflects what's on disk.
- **B01 narration lengthened by ~10 words** — the new "That's the picture the name pushes, and it's the wrong one" sentence pushes duration closer to `estimated_duration_s: 11` from the original 8.94s render; audio will re-measure at build.
- **B02 narration lengthened by ~20 words** for the added trade-off sentence; still within its 16s estimate. B05 lengthened similarly for "the file is the whole policy" sentence; within its 15s estimate. B07 lengthened for the "this works if… it fails if…" closer; still within its 18s estimate.
- **BHTF `estimated_duration_s` bumped 20 → 26** to reflect the longer paste-ready prompt narration.

## What was NOT changed

- Every `beat_id`, every `act` structure (except BHTF's act relabel to `LLM EXERCISE`), every `shot`/`graphic`/`remotion` props block, all on-screen card copy (chip text, labels, captions, quote text, pair strings), Manim scene names, audio file paths, build stubs, `actual_duration_s` fields were dropped by the scaffold and are not restored — audio will re-measure on rebuild.
