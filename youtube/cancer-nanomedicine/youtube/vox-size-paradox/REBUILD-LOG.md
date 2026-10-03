# REBUILD-LOG.md — vox-size-paradox

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-27 before any edit.

## LOCKED (unchanged)

- Every body narration_text (B01–B15) is verbatim from the pre-rebuild sheet.
- Beat order and act labels: B01/B02/B03 COLD OPEN · B04 THE QUESTION · B05/B06 THE PROBLEM · B07/B08/B09 THE MECHANISM · B10/B11 THE IMPLICATION · B12 THE EXAMPLE · B13 RECAP · B14/B15 OUTRO.
- Metadata identity: title, slug, topic, color semantics, style bible.
- Non-Claude channel skins retained: OutroSeries (B14) and OutroCTA (B15) — NOT Claude-washed. This reel has no Claude bookends (B00/BVDT/BHTF/BOUT) — legit for the vox-explainer format on a non-claude channel.
- Illustrative numbers (150 nm / 30 nm; 6.2% / 2.1% ID/g; 15% / 72% shrink; 80% even) are the chapter's teaching example; card metadata already labels them illustrative in `FACTCHECK.md`.

## REBUILT (regenerated)

- Metadata voice envelope normalized (`engine: kokoro`, `voice: nbbhuman`, `voice_kokoro: am_onyx`). ElevenLabs `voice_id: TyW6NH39JcFb5M3xdIIk` DROPPED. Dead `clock` prose DROPPED.
- Metadata `folderLabel: "@NikBearBrown"` added (was implicit via OutroCTA `handle`).
- Metadata `short_title: "Distribution Beats Total Mass"` added.
- Metadata `source: "cancer-nanomedicine/chapters/02-tumor-transport-barriers.md"` added.
- `vox_scenes.py` import path — replaced the brittle `parents[3]` shortcut with a walk-up search that locates `books/vox/aspects/explainer/vox-explainer/manim/vox_graphics.py` regardless of where the file is invoked from. Matches the pattern already used in the rebuilt sibling `vox-endosomal-escape`.
- Fresh Kokoro audio → `mp3/beat-*.mp3` regenerated with `am_onyx`; `mp3/timings.json` rewritten; `actual_duration_s` per beat rewritten from measured values.
- Fresh Manim renders → `manim/B01…B13.mp4` (excluding B02, B07 which are AI stills); old `media/videos/` cache purged first.
- Fresh compile → `vox-size-paradox-review.mp4` and `vox-size-paradox-slate.mp4` at reel root.

## Datable-claim edits

None. Narration cites tumor-transport biology (leaky vasculature, elevated interstitial pressure, hypoxic core, ~72% vs ~15% tumor-volume reduction as an illustrative case) that are chapter-textbook mechanism, not versioned. No model names, prices, or "as of" phrasing.

## Card-text edits (per PHASE 1 §5)

The two `FormACard` slates (B02, B07) had narration-truncated `lines[]` values ending with "…" (from an earlier authoring cutoff). Rewrote both as complete narration-derived sentences:
- B02 lines[0]: old `"Two mouse tumors. Same injected dose. The big particle — 150…"` → new `"Two mouse tumors. Same injected dose. The big particle piles up at the rim in higher numbers."`
- B07 lines[0]: old `"But total mass measured on the whole organ is not what…"` → new `"Total mass on the whole organ is not what kills cells. The tumor is a landscape with an edge and a core."`

## Scene edits (per PHASE 1 §5b, Gate B)

- B10 attribution: old `"— cancer-nanomedicine chapter 2"` → new `"— tumor transport barriers"` (CHAPTER-ON-SLIDE law violation; changed in both `vox_scenes.py` and `beat_sheet.json` `document.attribution`).
- B08: axis `vessel` / `core` labels moved from UP-buff to DOWN-buff of the horizontal axis line (labels were sitting on the line); `outward pressure` label moved to interior position below the arrows (was crossing arrows/zone border).
- B10: replaced `_quote_scene(...)` call with an inline B10_HypoxicCore that marks the highlight `Rectangle` as `_qc_intentional = True` so the layout audit exempts the deliberate gold highlight from the text-on-curve rule.
- B11: `TOTAL MASS` / `DISTRIBUTION` panel headers moved up above the panel top border; verdict `Distribution beats total mass.` moved from `to_edge(DOWN, buff=0.35)` (outside ±3.4 safe area) to y=-3.15 (inside safe area).
- B12: central divider marked `_qc_intentional = True` (row labels sit on it by design); `illustrative example` header moved from `to_edge(UP, buff=0.4)` (outside safe area) to y=3.15 (inside safe area).

## Dropped fields

- `metadata.voice_id` — ElevenLabs identifier; superseded by Kokoro voice-lock.
- `metadata.clock` — ElevenLabs-era prose about the clock; the clock is now measured Kokoro audio.

## Reel-level notes

- Persona coherence: narration is third-person explainer voice with no persona claim; outros carry NikBearBrown attribution — voice-lock `nbbhuman` (→ Kokoro `am_onyx`) is coherent.
- `vox_scenes.py` already had scene classes for every drawn body beat (B01_Title, B03_OutcomeContrast, B04_Question, B05_LeakyVessel, B06_TotalMassBars, B08_OutwardPressure, B09_PenetrationCompare, B10_HypoxicCore, B11_DistributionVerdict, B12_Example, B13_End). B02 and B07 are AI-still slates. B14/B15 are Remotion OutroSeries/OutroCTA, rendered as declared slates by `vox_compile.py` in this Manim-only compile.
