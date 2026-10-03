# AUDIT — nbb-vox-tumor-pressure

Run: 2026-08-30 · unattended film-factory pass

## PHASE 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json` created byte-exact from `beat_sheet.json` before any edit.
- Body beats B01–B11 left LOCKED (source: `../vox-tumor-pressure/clips/*.mp4`).
- Envelope beats NBB00/NBB01/NBB02/NBB03 kept as inherited (locked narration).

## PHASE 1 — Audit checks

| # | Check | Status | What changed |
|---|-------|--------|--------------|
| 1 | Stale renders | PASS | No existing mp4 in folder. |
| 2 | Bookends present (B00/BVDT/BHTF/BOUT) | PASS | All four present. |
| 3 | Spark lines | FIXED | B00 greeting `Liam` → `Salve, Liam.` (Latin; no adjacent-reel collision). NBB00 inner-composer greeting `Your turn.` → `The pressure pushes out.` (4-word compress from narration). |
| 4 | Verdict | FIXED (authored) | BVDT was template default (`Key finding one/two/three`, empty narration). Body is 11 beats / ~430 words → authored real verdict from body content: heading `why the tumor grew back`; three lines about leaky vessels + IFP 5–10× + hypoxic core selecting resistant cells; narration rewritten to say the finding aloud. |
| 5b | Chart text | N/A | Source vox reel — no per-reel Manim charts owned by this variant. |
| 5c | Your-Turn placeholder | FIXED | BHTF command was `Take what you learned from [...] and apply it to your own work` template. Rewrote as real exercise from body content: pick a solid tumor (PDAC / GBM / TNBC), estimate its IFP gradient, choose lowering strategy (anti-VEGF / hyaluronidase / CED), name a rim-vs-core dose ratio that would falsify or confirm. |
| 5 | Card text | FIXED | B01 FormBCard items had `label: Key point one/two/three` + empty `sub`. Rewrote all three labels + subs from B01 narration (`Delivery reached the tumor`, `Rim killed, core untouched`, `Regrows from the inside`). B02 FormACard line was verbatim narration; shortened to `week 3 MRI — the viable core`. NBB01 artifactHeading was mid-sentence truncation `Why the Drug Reached the Tumor and the` — replaced with `delivery reached, tumor still grew`. BHTF segment `pressure barrier · what would drop it` reflowed to `pressure barrier · lowering strategies` to clear §8.9 truncation flag. |
| 6 | Punt sweep | PASS | Zero gen-AI asks; zero unfilled slates; every beat maps to a filled shot. |
| 7 | Card-only reel | PASS | 11 body beats draw real figures (Manim / diagram / MRI still); not a card-only reel. |
| 8 | Lens audit | PASS | Body demonstrates the Humean move (metric-vs-world: accumulation measured, delivery not; the core survives and regrows) and the Popperian move (accumulation-as-success is falsified by regrowth). |
| 9 | Brand fields | PASS | `folderLabel: @NikBearBrown` (handle, not brand key). `engine: kokoro` + `voice: am_onyx` match the audio actually generated. |
| 10 | Pacing | ADVISORY | Body beats inherit source vox durations; wps within normal Teardown envelope. |
| 11 | `type_check.py` | PARTIAL PASS | Structural sweep + shape: PASS (0 sweep, 0 shape). §8.1 min-size FAILs on 7 body beats (B03, B06–B11) reflect small annotation labels (8–11px) inside the Manim scenes of the SOURCE `vox-tumor-pressure` reel — same beats fail on the source itself. Body is LOCKED per rebuild contract, so the source pixels cannot be regenerated from this reel. Not loosening the validator; documenting the inherited condition. All new bookends (B00, BVDT, BHTF, BOUT, NBB01–NBB03) PASS min-size. |

## PHASE 2 — Build

- Audio: `generate_audio_kokoro.py --only BVDT` — 19.07 s @ am_onyx (only BVDT gained narration; other bookends stay silent as designed).
- Body durations: `actual_duration_s` had been inherited inflated (~1–2 s over each audio file), which caused the first compile pass to truncate the tail via `-shortest`. Reset each body beat's `actual_duration_s` to the true audio duration; deleted stale `vox-tumor-pressure.mp4` + `clips/`; recompiled.
- Remotion bookends rendered via `runtime/scripts/remotion_scenes.py` (B00, NBB00, NBB01, NBB02, NBB03, BVDT, BHTF, BOUT — 8 slate patterns).
- `compile.py` → `vox-tumor-pressure.mp4` (3840×2160, 248.7 s, 19/19 slots VIDEO).
- Gate AUDIO: PASS · `mean_volume -27.9 dB` (above −40 dB floor).
- Gate V (frame reads at t=30, 100, 150, 190, 210, 230, 245, end):
  - B00 opens with `Salve, Liam.` and the composer command — clean.
  - Body Manim scenes (particle-pressure diagram at ~t=100) render as expected.
  - NBB01 verdict card (`delivery reached, tumor still grew`) paginates cleanly.
  - BVDT verdict card (`why the tumor grew back`) shows the three authored lines.
  - BHTF composer shows real authored exercise, `Your turn.` spark.
  - BOUT title outro renders at file end with `@NikBearBrown` + mascot — the reel ends correctly on the title outro (was truncated in first pass; fixed via duration sync).
- Punt sweep post-build: zero SLATE beats. build.status Counter: `{'VIDEO': 19}`.

## Outstanding

- §8.1 min-size failures on 7 source-locked body beats — inherited from the source vox reel; not resolvable without regenerating source Manim scenes.

## Final artefact

`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/youtube/cancer-nanomedicine/youtube/nbb-vox-tumor-pressure/vox-tumor-pressure.mp4` — 248.7 s, 4K, audio present, sheet-newer-than-mp4 ordering verified.
