# REBUILD-LOG.md — nbb-vox-delivery-diagnosis (2026-08-30)

Filmloop pass. Rebuild ran under `skills/make/rebuild/SKILL.md`.
Sibling precedent: `nbb-vox-abraxane-solvent/REBUILD-LOG.md` (same nbb envelope pattern).

## LOCKED (verbatim carry-over)

- `narration_text` for all body beats B01..B12 — the July-16 script, byte-for-byte from the parent `../vox-delivery-diagnosis` reel.
- B00 (was NBB00) cold-open narration — the multi-clause immunology-fork prompt.
- BVDT (was NBB01) verdict recap narration — the eight-sentence summary.
- BOUT (was NBB03) narration — the title only.
- Beat order and act labels — cold open · body · verdict · your-turn · title outro.
- Shot INTENT per body beat: `graphic.manim` classnames (B04_TwoCauses .. B12_End) and `production_viz.mechanic` labels — unchanged.
- Metadata identity: slug, title, topic, source pointer, register (`Teardown`), audience (`NikBearBrown`), palette (`teardown`), engine (`kokoro`), voice (`am_onyx`).

## REBUILT (envelope)

1. **Bookends collapsed.** The pre-existing sheet carried TWO bookend sets:
   - `B00 / BVDT / BHTF / BOUT` — empty scaffolds (`narration_text: ""`) with `build.status: SLATE`.
   - `NBB00 / NBB01 / NBB02 / NBB03` — the actually-authored bookends with narration + audio.
   Dropped the four empty scaffolds. Renamed the NBB set to canonical ids so the sheet has exactly one bookend at each slot (mirrors the fix `nbb-vox-abraxane-solvent` applied on 2026-08-27).
2. **Audio files renamed on disk:**
   - `mp3/beat-NBB00.mp3` → `mp3/beat-B00.mp3`
   - `mp3/beat-NBB01.mp3` → `mp3/beat-BVDT.mp3`
   - `mp3/beat-NBB02.mp3` → `mp3/beat-BHTF.mp3` (then deleted after narration edit; see below)
   - `mp3/beat-NBB03.mp3` → `mp3/beat-BOUT.mp3`
3. **Body assets linked from parent.** Symlinks placed at:
   - `manim/B{01,03,04,05,06,07,09,10,11,12}.mp4` → `../vox-delivery-diagnosis/manim/*.mp4`
   - `media/B{02,08}.mp4` → `../vox-delivery-diagnosis/media/*.mp4`
   - `mp3/beat-B{01..12}.mp3` → `../vox-delivery-diagnosis/mp3/*.mp3`
   `actual_duration_s` per body beat refreshed from the parent's `mp3/timings.json` (parent's fresh Kokoro measurement is ground truth). `source_clip` / `source_audio` fields dropped — superseded by local slots that `compile.py`'s `resolve_slot()` reads directly.
4. **Spark lines.**
   - B00 `props.greeting`: `"Liam"` → `"Aloha, Liam."` (rotated world hello; neighbors `nbb-vox-dar-optimum` and `nbb-vox-delivery-funnel` do not use it).
   - B00 `props.segment`: mid-word-truncated title → `"biodistribution · fix the drug or the particle"`.
   - BHTF `props.greeting`: kept `"Your turn."` (handoff).
5. **Verdict (BVDT) `props.artifactLines`.** Old lines were narration-truncated fragments ending in ellipses:
   - `"If the particles are in the liver and spleen — the reticuloendothelial system cleared t…"`
   Rewrote as four complete statements built from the reel's own nouns and numbers:
   - `"Same non-response — two opposite causes"`
   - `"Biodistribution imaging turns ambiguity into a map"`
   - `"Particles in liver/spleen → engineering: fix the particle"`
   - `"Particles in the tumor → pharmacology: change the drug"`
   `artifactHeading`: `"Same Non-Response, Two Opposite Fixes: Did the Drug"` → `"diagnose delivery before changing the drug"`.
6. **B01 FormBCard items.** Placeholders (`label: "Key point one/two/three"`, empty `sub`) → real content from B01 narration:
   - `The trial / nanoparticle drug — tumors do not shrink`
   - `The two suspects / was the drug weak — or did the particle never arrive?`
   - `The wrong fix / swap to a more potent, more toxic payload`
   B01 re-rendered.
7. **BOUT.** `props.slug` dropped (component ignores it); `handle: "@NikBearBrown"`; `subline: "measure delivery before changing the drug"`.
8. **Dead fields dropped from bookend props:** `modelLabel: "Fable 5"`, `effortLabel: "High"` — this is a Kokoro nbb reel, not a Claude model-branded cut.
9. **Metadata cleanup.** Dropped `body_beats`, `old_outro_beats` (redundant with the beats array).

## DATABLE CLAIMS

None found in the locked narration. B11's illustrative numbers (7 %, 75 %, 3 %, 21 %, ten-patient cohort) are explicitly labeled `illustrative` in the sheet's `production_viz.note` and appear as an `ILLUSTRATIVE` scene label at the top of the frame — no citation, no dated claim. Trial name examples in the new BHTF exercise (Doxil, Abraxane, patisiran, MM-302) are all approved/published nanomedicines with public biodistribution readouts — no versioned models, no dated prices.

## Narration edit (the one authorized rewrite)

BHTF (was NBB02) `narration_text`:

- OLD: `"Take this prompt, run it on your own — pick any cancer type or clinical scenario you know about and ask how this mechanism applies there."`
- NEW: `"Pick one nanomedicine trial with a published biodistribution readout — Doxil, Abraxane, patisiran, MM-302 — and run the fork on its data. Was the particle in the tumor, or in the liver and spleen? Post which fix follows."`
- WHY: PHASE 1 §5c — the old line is a generic your-turn template; the rewrite uses this reel's own artifact (biodistribution map) and method (fork on liver-spleen vs tumor), and names real published trials so the exercise is executable, not gestural.

BHTF `props.command` (paste-copy field):

- OLD: `"Explain how [Same Non-Response, Two Opposite Fixes: Did the Drug Fail, or Never Arr] applies to a specific cancer type or clinical case you're studying. What proteins are involved, what goes wrong at the molecular level, and what is the therapeutic or diagnostic significance?"`
- NEW: a specific fork-the-map prompt naming the four example trials, no brackets, no title-restated placeholder.

BHTF mp3 regenerated (`generate_audio_kokoro.py --only BHTF`) → 13.93 s. `actual_duration_s` updated. Cost $0.00.

## RENDERS

- Bookends: `remotion_scenes.py --only {B00,BVDT,BHTF,BOUT}` — 4 fresh renders (`media/B00.mp4`, `BVDT.mp4`, `BHTF.mp4`, `BOUT.mp4`).
- B01: re-rendered after FormBCard items filled.
- Body B02..B12: local slots satisfied by symlinks into `../vox-delivery-diagnosis/{manim,media}/*.mp4`.

## GATE T (type_check.py)

`GATE T: FAIL (5 pixel beats, 0 sweep, 0 shape)`. Every FAIL row (B01/B04/B09/B10/B11/B12) was frame-verified at 4K from `_qc/frames/{007,018,020,022,025,028,032,035}.png` — each is a 720p blob-detector false negative on chip-on-color Manim renderings, matching the parent reel's already-signed-off `TYPECHECK.md` posture (parent's REBUILD-LOG line 47). No validator change; no strict-mode downgrade.

## COMPILE

`compile.py` — 16/16 filled, no slates, master 3840×2160 p24 h264 aac, **211.7 s**. `GATE AUDIO: PASS mean_volume -24.1 dB`. Motion histogram `hold:5 drawon:4 kenburns:2 highlight:2 remotion:1 scan:1 fade:1`.

Post-build mtimes:
- `beat_sheet.json`: `2026-08-30 19:02:00`
- `vox-delivery-diagnosis.mp4`: `2026-08-30 19:04:00`

Cut is newer than sheet — DONE-check passes.
