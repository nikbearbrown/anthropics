# REBUILD-LOG.md — medhavy-vox-endosomal-escape

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-30 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B13) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01/B02 COLD OPEN · B03 THE QUESTION · B04/B05 THE PROBLEM · B06/B07 THE MECHANISM · B08 THE IMPLICATION · B09/B10 THE EXAMPLE · B11 RECAP · B12/B13 OUTRO.
- Metadata identity: title, slug (`vox-endosomal-escape`), topic, source pointer, color semantics, style bible, audience=MEDHAVY, register=Wonder.
- Non-Claude vox-editorial channel skins retained: OutroSeries (B12) and OutroCTA (B13) — NOT Claude-washed. Legit legacy vox-explainer format on @NikBearBrown.

## REBUILT (regenerated)

- Metadata voice envelope normalized: `engine=kokoro`, `voice=af_kore`, `voice_kokoro=af_kore` (matches on-disk Jul-16 mp3s generated with af_kore for MEDHAVY audience).
- Metadata `channel=@NikBearBrown` and `folderLabel=@NikBearBrown` added.
- Metadata `build` block DROPPED (pre-rebuild `filled: 2/13, slates: [B01..B11]` was stale; compile restamps).
- Per-beat `build` stamps DROPPED (all claimed SLATE with gen-AI/pipeline needs; fresh compile restamps to VIDEO/MANIM).
- **B02 FormACard `props.lines`** — replaced the truncated ellipsis punt-costume line ("The team spent months looking for a better target. But they…") with three real narration-derived summary lines. The old ellipsis fragment is the exact §nopunt punt-costume: a FormACard whose text is a mid-sentence slice.
- **B12 OutroSeries `props`** — old props `seriesTitle`/`tagline`/`githubSlug` did NOT match the component's zod schema (`eyebrow`/`line`). Remotion would silently fall back to `defaultProps` and render foreign copy ("CLAUDE COWORK / Part of the Claude Cowork series."). Rewritten to `eyebrow="CANCER NANOMEDICINE"`, `line="Part of the Cancer Nanomedicine series."`. Same fix pattern as vox-protein-corona (2026-08-30) and vox-epr-gap.
- **B13 OutroCTA `props`** — old props `authorName`/`handle`/`ctaText` did NOT match the component's zod schema (`line`/`handle`). Rewritten to `line="Explore the full course at medhavy.com."`, `handle="@MedhavyAI"`.

## Datable-claim edits

None. Narration cites biology-mechanism facts (pH 7.4→5.5 endosome, ionizable-lipid charge flip, ~1–2% escape rate, LNP-A vs LNP-B illustrative 8% vs 84% silencing) that are chapter-textbook constants — no model names, versions, prices, or "as of" phrasing.

## Dropped fields

- `metadata.voice_id` = `"1sgY6Voq1aexKOB1IJ2D"` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio (per-mp3 duration).
- `metadata.build` — stale (claimed 2/13 filled with 11 SLATE at 2026-07-16; no cut on disk before rebuild).
- Every `beats[].build` — same stale claim per beat.

## Reel-level notes

- Persona coherence: narration is explainer voice (no persona claim); outros carry @NikBearBrown attribution (OutroSeries+OutroCTA); MEDHAVY audience → af_kore is coherent per VOICE-LOCK.
- MEDHAVY palette swap was NEVER applied to this variant — the sheet's `accents.data` still lists vox teal/crimson (`#1F6F5C`/`#BF3339`) on cream `#F3EBDD` ground. The `metadata.palette: "medhavy"` field is aspirational. Not corrected in this pass — the parent's Manim renders (reused) are vox-colored, and swapping palette would require re-rendering. Logged for a future medhavy-palette pass; not a blocker for this review cut.
- Body Manim renders (`manim/B01–B11.mp4`) are COPIES from the sibling `../vox-endosomal-escape/manim/` (parent reel, built 2026-08-27). The parent was rendered against nbbhuman-voice audio (~13–18 s beats); medhavy af_kore audio is ~15–20 s per beat. `compile.py` slows each clip 1.07×–1.52× to fit — well within the pipeline's slow-mo cap (3.0×). No re-render needed for the review pass.

## Reel-level notes — Remotion renders

- `media/B02.mp4` FormACard, `media/B12.mp4` OutroSeries, `media/B13.mp4` OutroCTA rendered fresh via `runtime/scripts/remotion_scenes.py` after prop fixes above.
