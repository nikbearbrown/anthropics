# AUDIT.md — vox-tumor-pressure

Ran 2026-08-27, unattended film-factory pass.

## Phase 0 — rebuild contract

- Snapshot: `beat_sheet.pre-rebuild.json` written byte-exact from old sheet — DONE (before any edit).
- Dead ElevenLabs field `voice_id: TyW6NH39JcFb5M3xdIIk` — DROPPED.
- Metadata voice envelope normalized: `voice: nbbhuman`, `engine: kokoro`, `voice_kokoro: am_onyx`.
- `folderLabel: "@NikBearBrown"` + `short_title: "The Pressure That Pushed the Drug Back Out"` + `source: "cancer-nanomedicine/chapters/02-tumor-transport-barriers.md"` added.
- Non-Claude channel skins retained: OutroSeries (B12) + OutroCTA (B13) — NOT Claude-washed. Mirrors sibling `vox-endosomal-escape`.
- `vox_scenes.py` toolkit import — brittle `parents[3]`-relative path replaced with parent-walk pattern used by sibling reel (finds `books/vox/aspects/explainer/vox-explainer/manim/vox_graphics.py` reliably regardless of depth).
- Narration is LOCKED. No datable claims found — pure biology mechanism (leaky vessels, IFP 5–10× normal, hypoxic core selection, illustrative IFP numbers labeled as `illustrative`).

## Phase 1 — checks

1. Stale renders — PASS. No mp4s on disk at audit start (never rendered — the Jul-2025 pass wrote scenes + mp3s only).
2. Bookends — PASS (per amendment). No Claude bookends (B00/BVDT/BHTF/BOUT). Legacy vox-explainer format on the NikBearBrown channel; rebuild contract keeps the channel's own skins (OutroSeries B12, OutroCTA B13). BVDT legitimately absent.
3. Spark lines — N/A. No `ClaudeComposerAsk` beats in the reel.
4. Verdict — N/A. No BVDT beat. Body ends with B11 recap-card ("The accumulation was real. The delivery was not.") — the reel already carries a stated conclusion in its own idiom. Vox-explainer format does not run a Claude verdict artifact.
5. Card text — PASS. B01 title-card is the reel title (7 words). B03 question-card is 6 lines of ≤10 words each. B11 endcard is 5 sentences of ≤5 words each. B02 FormACard `lines` is a 12-word line summarizing narration; PIPELINE slate label authored below (not a placeholder — the PIPELINE row IS the honest slate spec). No `sub` = TBD/"see narration"/empty across the reel.
5b. Chart text — PASS after B06/B07 fix. Chart axis / core labels in `vox_scenes.py` are short category nouns (`unreached core`, `particle-free core`, `drug accumulates`, `rim cleared`, `hypoxic core`, `25 mmHg`, `5 mmHg`, `rim`, `Week 3: rim -60%, core intact`, `Week 8: volume doubled`, `growth from core`). Bottom captions are complete phrases (`outward fluid pressure`, `pushed back to rim`, `hypoxia selects for resistant cells`). Bar heights / concentric ring sizes agree with narration meaning (favored thing = larger). No `Text(narration[:30])` truncations. See BLOCKER FIXED note below.
6. Punt sweep — PASS. Zero gen-AI asks in the sheet. Every body beat draws real content: B01/B03/B11 title-question-endcard scenes; B04–B10 native Manim scenes; B12/B13 declared slates in place of Remotion outros (accepted for slate-review cut format). B02 remains a declared slate (AI-still slot — future gen brief carried in `image_description`). No unfilled `fill_slates` / `remotion_scenes`. No DoodleScene/DoodleChart. No `STILL src=archive` for conceptual content. No FormACard names a visual it never draws.
7. Card-only reel — PASS. Nine drawn Manim beats (B01, B03, B04, B05, B06, B07, B08, B09, B10, B11) plus one AI-still (B02) and two outros. Not a card-only reel.
8. Lens audit — PASS. **Descartes**: the cold open runs radical doubt — "The drug was there. The whole-organ measurement said it had accumulated. The core is untouched." What would have to be true for the whole-organ ID/g measurement to predict per-region delivery? It doesn't; the artifact averages over a spatial gradient. **Popper**: the illustrative IFP numbers (25 mmHg core vs 5 mmHg rim, week 8 doubling from core origin) are stated as measurable failure criteria in advance — "the growth originates from the core" is the exact predicted observation that would refute the whole-organ accumulation model. **Plato**: the artifact is "the drug reached the tumor" (whole-organ % ID/g); the world is a pressure-partitioned interior with an unreached hypoxic core; the relationship is that the artifact conflates rim accumulation with core delivery. Three moves earned.
9. Brand fields — FIXED. `folderLabel: "@NikBearBrown"` added (matches OutroCTA `handle`). `engine: kokoro` + `voice: nbbhuman` + `voice_kokoro: am_onyx` describe the actual generated audio. Persona coherence: narration is explainer voice with no first-person claim; NikBearBrown attribution appears only in outros — voice-lock `nbbhuman`/`am_onyx` is coherent.
10. Pacing — LOG. WPS scan (words / actual_duration_s):
    - B01 33w/11.16s = 2.96 · B02 33w/10.05s = 3.28 · B03 37w/10.77s = 3.44 (0.04 over ceiling) · B04 40w/11.69s = 3.42 (0.02 over ceiling) · B05 37w/11.11s = 3.33 · B06 48w/14.76s = 3.25 · B07 48w/14.87s = 3.23 · B08 42w/14.31s = 2.94 · B09 35w/10.45s = 3.35 · B10 66w/20.16s = 3.27 · B11 42w/13.72s = 3.06 · B12 7w/2.88s = 2.43 · B13 5w/2.37s = 2.11.
    B03 (3.44) and B04 (3.42) are marginally above 3.4 ceiling — same-order slight rush from Kokoro's `am_onyx` cadence on short declarative sentences. LOGGED only; not retiming. Everything else inside the 2.0–3.4 window.
11. `type_check.py` — N/A. The Brutalist `type_check.py` measures Remotion pattern typography on rendered PNGs; this reel is Manim-driven with only two Remotion outros (rendered as declared slates in this pass, so no Remotion PNG surface to type-check). Gate V (manual PNG frame read below) covers Manim scenes end-to-end.

## Gate V — post-compile frame read

Read every ~5th frame from `_qc/frames/frame_*.png` on the compiled `vox-tumor-pressure-slate.mp4` (148 frames total, 1 fps sample).

- **B01 (00:00–00:11)** — CLEAN. Title stack, TEAL "CANCER NANOMEDICINE" eyebrow, INK primary, CRIMSON kicker with GOLD underline. One terracotta moment (the CRIMSON kicker).
- **B02 (00:11–00:21)** — Declared SLATE (STILL src=ai slot). PIPELINE label present, narration head shown. Exempt per Gate V rules — placeholder by design.
- **B03 (00:21–00:32)** — CLEAN. Five stacked SERIF lines flowing into a bold ITALIC/BOLD question with CRIMSON underline. Legible, no overlap, one terracotta moment.
- **B04 (00:32–00:44)** — CLEAN. Three-element schematic (leaky vessel rectangle · particles-enter arrow · CORE circle). Labels are chips; arrow reads clearly.
- **B05 (00:44–00:55)** — CLEAN. Vessel + inflow arrows + lymph symbol + pressure fill build correctly.
- **B06 (00:55–01:10)** — CLEAN after fix. BLOCKER on first pass: `Text("unreached core")` at ORIGIN was drawn as thin CRIMSON text sitting directly on the horizontal outward-flow arrows — the arrow lines struck through the letters, breaking legibility. FIX: converted `rim_label` and `core_label` in `vox_scenes.py` `B06_PressureFlow` from `Text(...)` → `LabelChip(...)` (solid ink chip that hides the arrow behind it) and moved `core_label` from ORIGIN → `DOWN * 1.35` (below the arrow field, in the white gap between core radius 1.1 and rim inner radius 1.6). Re-rendered B06 and re-compiled. Now: CORE label sits cleanly below the arrows, DRUG ACCUMULATES chip sits at the rim edge.
- **B07 (01:10–01:24)** — CLEAN after fix. Same BLOCKER as B06 (particle-free core text struck through by outward arrows). Same FIX applied: `core_label` → `LabelChip` at `DOWN * 1.35`. Re-rendered. One minor: at frame 77 the chip corner just touches a rim particle dot at 6 o'clock — MINOR (dot is still readable as a filled circle; chip label is readable in full). No further fix.
- **B08 (01:24–01:39)** — CLEAN. Solid-ink RIM CLEARED chip at rim corner; solid-ink HYPOXIC CORE chip at center of core with radiating resistant-cell dots. The dots at r=0.55 sit above/below the chip and don't overlap the chip glyphs.
- **B09 (01:39–01:49)** — CLEAN. Quote scene with "core cells" highlight and italic attribution below.
- **B10 (01:49–02:09)** — CLEAN. Two-panel layout: left is the pressure diagram (`25 mmHg` core, `5 mmHg` rim, arrow between); right is a three-line timeline (Week 3 / Week 8 / growth from core). The IFP arrow starts right after "25 mmHg" so it grazes the "g" of "mmHg" — MINOR, still readable. Numbers are MONO. One terracotta moment per beat sub-frame (core value + week 8 origin line).
- **B11 (02:09–02:23)** — CLEAN. Recap card mirrors B01 layout — same eyebrow, INK/CRIMSON kicker split, GOLD underline on kicker, italic subline.
- **B12 (02:23–02:26)** — Declared SLATE (Remotion OutroSeries slot). Exempt per Gate V rules — placeholder by design.
- **B13 (02:26–02:28)** — Declared SLATE (Remotion OutroCTA slot). Exempt per Gate V rules — placeholder by design.

Result: 0 BLOCKER, 0 MAJOR on real beats after B06/B07 fix. 2 MINOR logged (B07 chip-corner particle graze, B10 arrow-glyph graze). 3 declared slates (B02/B12/B13) exempt.

## Audio presence

`vox-tumor-pressure-slate.mp4` — 148.3s, video+audio streams present, mean_volume −23.9 dB (well above −40 dB floor), max_volume −0.9 dB. Kokoro `am_onyx` narration, per-beat mp3s concat'd through vox_run compile.

## Freshness

`beat_sheet.json` mtime: Aug 27 23:27. `vox-tumor-pressure-slate.mp4` mtime: Aug 27 23:35. mp4 is 8 minutes newer than the sheet — DONE-check will pass.

## Blocked?

No. All Phase 1 checks either FIXED, PASS, LOGGED, or N/A. Gate V read clean after B06/B07 label-chip fix. Reel built.

## Build status (Counter)

`Counter({'MANIM': 10, 'SLATE': 3})` — B01/B03/B04/B05/B06/B07/B08/B09/B10/B11 MANIM · B02/B12/B13 declared SLATE.
