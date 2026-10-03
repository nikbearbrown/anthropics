# CONVERT-LOG — nbb-healthcare--claude-liam-contracts

Converted `beat_sheet.json` (Plain / hai-fellows) → `beat_sheet.nbb.json`
(Teardown / NikBearBrown). Voice-only; no facts changed; no render.

## What changed

- **Narration rewritten in Teardown register** for every non-outro beat (B00,
  B01, B02, B03, BCRY, BHTF). Each now names what the skill *does mechanically*
  and what its designers *optimized for* — "text over machinery," "auditability
  over cleverness," "repeatability at the expense of range." Forbidden phrases
  ("innovative," specs-without-context, "one could argue") stayed out.
- **B_LLM inserted before the outro pair.** New beat carries a paste-ready
  prompt for any frontier LLM (Claude / ChatGPT / Gemini) about skills as a
  design pattern — plus a `dig_deeper` follow-up that pushes the viewer to
  draft a SKILL.md for one of their own weekly workflows. Shot uses
  `ClaudeComposerAsk` so it renders as a paste-prompt card (same visual family
  as BHTF); the `llm_exercise` metadata block carries the canonical prompt +
  dig-deeper text per SKILL.md §Step 3.
- **Outro (BOUT + BCTA) re-flagged for NikBearBrown.** Eyebrow
  `CLAUDE BASICS · HUMANITARIANS AI` → `CLAUDE BASICS · NIKBEARBROWN`;
  outro-CTA handle `@HumanitariansAI` → `@NikBearBrown`; BCTA sign-off extended
  from "…Liam, in for Bear." to "…Liam, in for Bear. www.brutalist.art." (NBB
  brand default channel). Content otherwise preserved.
- **Palette-consistent hex swaps in B00's BrutalistHesitantWriter props:**
  `ink #2F2A26 → #2A1A0E`, `accent #E4572E → #C8102E`, `bg #F3EBDD → #FFFFFF`
  to match the teardown palette declared in metadata. Metadata `ground`
  updated to `#FFFFFF` for the same reason.
- **`folderLabel` / `channel_title` in metadata** moved from `@HumanitariansAI`
  to `@NikBearBrown` (this is the NBB variant; NBB's channel).
- **`_variant_todo` removed.**
- **Stale `build.filled_by / status / src / at`** dropped from every beat
  (no NBB media rendered yet); `actual_duration_s` values dropped for the same
  reason. `audio_file` paths retained so a future kokoro pass has a target.

## Judgment calls

- **"Second-to-last" interpretation.** The NBB SKILL.md §Step 5 diagrams the
  ending as `body → [LLM exercise] → [outro]`, treating the outro as one slot.
  This reel's outro is two beats (`BOUT` OutroSeries + `BCTA` OutroCTA), which
  is the canonical NBB pair. Splitting `B_LLM` between them to satisfy the
  literal `[-2]` position would break that pair. `B_LLM` is placed between
  `BHTF` and `BOUT` so the OutroSeries + OutroCTA package stays intact as the
  final beat block. Body → LLM exercise → outro pair.
- **Kept BHTF alongside B_LLM even though both are paste-ready prompts.** BHTF
  is skill-specific ("run the contracts skill on your files"); B_LLM is
  design-pattern-broad ("understand skills as programs, in any LLM"). Different
  targets, different jobs. Preservation rule requires every source `beat_id`
  survives, so BHTF stays.
- **BOUT/BCTA copy left largely intact.** SKILL.md §Step 4 says to source outro
  content from `AUTHOR.MD :: NikBearBrown`. That file isn't present alongside
  this reel; the scaffold pointer `outro_source: "AUTHOR.MD :: NikBearBrown"`
  was left in metadata. Rather than fabricate NBB outro copy, I re-flagged the
  existing outro to the NBB channel and added the `www.brutalist.art` tag on
  BCTA (the brand spec's default channel). If AUTHOR.MD surfaces later, BOUT
  eyebrow + BCTA line can be replaced without touching the rest.
- **Palette hex updates in B00 props** (see above) are metadata-consistency, not
  a fact change — the visual was already declared "teardown palette" in the
  scaffold and the source hexes were the humanitarians warm-cream set.

## Order

`B00 → B01 → B02 → B03 → BCRY → BHTF → B_LLM → BOUT → BCTA`

## Not done

No audio generated. No compile. No render. The sheet is the deliverable.
