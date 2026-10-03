# CONVERT-LOG — nbb-claude-quickstarts--feature-list-checkpoint-persistence

Register conversion from Plain (HAI) → Teardown (NBB). Voice-only pass; facts, beat_ids, act structure, `shot` / `graphic` / `remotion.props` (visual) blocks preserved verbatim.

## What changed

- **Every beat narration rewritten in Teardown register.** Feynman × MKBHD lens — take it apart, name the design choice, name the trade-off. Facts, numbers (200 features, boundary at 50, resume at 51), file names (`feature_list.json`, git), and mechanism preserved unchanged.
- **B00 cold open** — opens with "This is Liam, in for Bear." per IN-FOR-BEAR LAW. Kept the BrutalistHesitantWriter visual (`text`, `triggerWords: remembers → rereads`) intact.
- **BCRY carry-out** — left the on-screen `quote` prop **verbatim** (already Teardown-native: "workspace, not memory") so audio matches the visual quote card. Narration mirrors it exactly.
- **BHTF repurposed as the LLM EXERCISE beat (second-to-last).** Replaces the HAI "your turn" restatement. Added the `llm_exercise` block (paste-ready prompt + `dig_deeper` follow-up). Composer `command` prop rewritten as the ready-to-paste NBB brief; `folderLabel` → `@NikBearBrown`.
- **BOUT outro (last)** — rewritten as the NikBearBrown outro from `AUTHOR.MD :: NikBearBrown`; `handle` → `@NikBearBrown`; narration adds the `brutalist.art · @NikBearBrown` sign-off. `estimated_duration_s` bumped 6 → 9 to fit the longer line.
- **`_variant_todo` removed** from metadata (steps 1–4 complete; build is a separate pass).

## Judgement calls

- **Metadata `folderLabel` / `channel_title` left as `@HumanitariansAI`.** The only beat that actually surfaces a folder chip is BHTF; I updated that beat's own `folderLabel` prop to `@NikBearBrown` and left the metadata-level fields alone rather than re-scaffolding.
- **Estimated durations bumped** on beats whose Teardown rewrite added a design-critique clause (B00 14→18, B01 17→22, B02 20→26, B03 20→22, B04 17→18). Kokoro will produce the real numbers at audio-gen time; these are hints for the compiler, not commitments.
- **BCRY narration is verbatim** with the source (and with its own `quote` prop). Rewriting it would desync audio from the anchor visual for no register gain — the sentence is already Feynman × MKBHD in shape.
- **LLM exercise scoped tight** to the video's actual subject (checkpoint file schema + git ledger + resume algorithm + write/lock discipline). The `dig_deeper` follow-up pushes to concurrent sessions — the natural next design decision the video explicitly declines to cover.

## Not done here

Audio generation, compile, and render are a separate pass (per the register-conversion factory brief). This file is `beat_sheet.nbb.json` only.
