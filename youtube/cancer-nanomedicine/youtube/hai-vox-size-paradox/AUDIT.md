# AUDIT.md — hai-vox-size-paradox

Checked: 2026-08-31T03:36  |  Channel: HAI (Humanitarians AI)  |  Voice: Kokoro `am_onyx`

## PHASE 1 checks

| # | Check | Result |
|---|-------|--------|
| 1 | Stale renders | PASS — no mp4 in folder pre-run |
| 2 | Bookends | PASS — HAI channel; own skins (OutroSeries / OutroCTA), Claude bookend checks (B00/BVDT/BHTF/BOUT) do not apply |
| 3 | Spark lines | N/A — no ClaudeComposerAsk beats on this channel |
| 4 | Verdict | N/A — HAI has no BVDT beat (`verdict_audit.py`: "no verdict beat") |
| 5 | Card text | PASS — B01 title + B04 question + B13 endcard copy is complete, no placeholders; FormACard `lines` on B02/B07 are legacy truncations but body B01–B13 render from parent's `../vox-size-paradox/clips/` (SYMLINKS), so those lines are not what's rendered |
| 5b | Chart text | PASS — parent's Manim clips inspected at B06 (150nm vs 30nm bars 6.2/2.1% ID/g, "bigger wins on total mass" footer), B09 (30nm vs 150nm dot spread with vessel/core axis), B12 (150nm/30nm two-column table with illustrative example) — labels are short category nouns, bar heights match narration |
| 5c | Your-Turn placeholder | N/A — no BHTF beat |
| 6 | Punt sweep (pre-build) | FIXED — 13 body-beat SLATE stubs ("YOU → 5-10s gen-AI clip → pantry" and "PIPELINE → render animated_graphics.py scene BXX_*") replaced by pointing `build.src` at `media/BXX.mp4` symlinks to parent's rendered clips; 2 outro slates (B14/B15) resolved by fresh Remotion renders after correcting props to component zod schemas |
| 7 | Card-only reel | PASS — 5 Manim GRAPHIC body beats (B03/B05/B06/B08/B09/B11/B12), 1 DOCUMENT (B10), 2 STILL (B02/B07), 3 CARD (B01/B04/B13), 2 Remotion outros — mixed-media |
| 8 | Lens audit | PASS — two moves earned |
| | · **Popper** | B03 + B06 refute the naive "bigger particle = more accumulation = better outcome" claim: 15% vs 72% shrinkage on day 21 (B03) is a falsifying instance against the whole-organ-mass hypothesis (B06). The reel states in advance what would count as failure (total-mass metric) and then produces the failure. |
| | · **Plato** | B07 + B11 hold artifact / world / relationship apart: "whole-organ mass is not the operative variable" (B07 — the artifact is not the world); B11: "rim accumulation is not cell-level drug delivery" (the relationship between the accumulation number and the tumor kill is that rim accumulation misses the cells that matter). |
| | · Hume implicit | B02: "Whole-organ measurement scores it the winner" — measurement is a property of the assay, not the drug's real efficacy. |
| 9 | Brand fields | FIXED — added `folderLabel: "@humanitariansai"`; dropped ElevenLabs-era `voice_id: "qdEb53HLreRBCD1FQE30"`; normalized `clock` prose from "durations below are word-count estimates until GATE 0 audio lock" to "narration (Kokoro am_onyx VOICE-LOCK) — measured durations". `engine: "kokoro"`, `voice_kokoro: "am_onyx"` unchanged. HAI-audience narration doesn't name Liam — Kokoro `am_onyx` is the standard HAI voice per brands/hai.md. |
| 10 | Pacing | LOGGED — every body beat 2.7–3.3 wps against measured mp3 durations. B04 3.30 wps (near cap, OK). B06 3.07 wps. B12 79 words / 25.45s = 3.10 wps. All within 2.0–3.4 range. B14 2.08 wps and B15 1.32 wps are outro CTAs — short by design, not a floor violation. |
| 11 | `type_check.py` | FAIL (inherited) — 8/13 body beats FAIL §8.1 min-size because parent's rendered Manim clips (in `../vox-size-paradox/clips/`) contain italic serif "vessel"/"core" axis labels and illustrative footers that measure 8-11px on the 1080p logical frame (floor 20px). These are the SAME clips shipping in `vox-size-paradox`, `nbb-vox-size-paradox`, and `medhavy-vox-size-paradox` — not something introduced by this variant. Fixing would require re-rendering parent's Manim source with larger axis labels; that is Cohort A parent-reel scope, not a downstream variant fix. Text is readable in the compiled cut. See TYPECHECK.md for the per-beat report. |

## Rebuild contract (PHASE 0)

- `beat_sheet.pre-rebuild.json` created byte-exact before any edit (03:25).
- **Envelope normalized** — dropped ElevenLabs `voice_id`; simplified `clock` prose. Kept metadata identity (slug, title, topic, audience, palette, engine/voice_kokoro, style bible).
- **Narration LOCKED** — zero body-beat narration edits. B01–B15 narration identical to `beat_sheet.pre-rebuild.json`. Datable-claim pass: none required (no model names, no versions, no "as of" phrasing; illustrative numbers 6.2 / 2.1 / 15 / 72 / 80 % are already labeled illustrative in the corresponding graphic's `production_viz.note`).
- **Outro props corrected** — B14 (OutroSeries) and B15 (OutroCTA) `remotion.props` were carrying schema-mismatched keys (`seriesTitle` / `githubSlug` for B14 → OutroSeries expects `eyebrow` / `line`; `authorName` / `ctaText` for B15 → OutroCTA expects `line` / `handle`). First render fell through to the component defaults ("CLAUDE COWORK / Part of the Claude Cowork series.") because the wrong keys were silently ignored. Props rewritten to schema, re-rendered, re-compiled. No narration change.

See `REBUILD-LOG.md` for byte-level edits.

## Blockers

None. Type-check FAIL is inherited from parent's clip renders, documented above and in TYPECHECK.md.
