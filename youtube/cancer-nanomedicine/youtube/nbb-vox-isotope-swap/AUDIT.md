# AUDIT.md — nbb-vox-isotope-swap

Invocation date: 2026-08-31
Cut produced: `vox-isotope-swap.mp4` (220.1s, 3840×2160, mean_volume −24.2 dB)

## PHASE 0 — rebuild contract

- `beat_sheet.pre-rebuild.json` created (byte-exact copy of the pre-edit
  sheet), before any edit.
- All narration LOCKED; only PHASE 1-authorized fixes made
  (spark lines, verdict/BHTF placeholder command, §8.9 truncation
  corrections on display strings).
- VOICE-LOCK envelope already clean (kokoro / am_onyx across the board;
  no ElevenLabs fields).
- shot.form derivation preserved (Claude Composer / Verdict / Title-Outro
  patterns on the NBB* bookends; source vox scenes on the body).
- Non-claude channel — kept the @NikBearBrown skin; did not Claude-wash.

## PHASE 1 — audit

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | FIXED | No pre-existing renders — folder had no `media/` before this pass. Re-rendered NBB00/NBB02/NBB03 after sheet edits so on-screen text matches props. |
| 2 | Bookends B00/BVDT/BHTF/BOUT | FIXED | Sheet carried a duplicate set of bookends: real NBB00/NBB01/NBB02/NBB03 (audio + narration + real props) and empty B00/BVDT/BHTF/BOUT (placeholder narration, template artifactLines, bracketed BHTF command). Stripped the empties; NBB* set already provides canonical cold-open / verdict / your-turn / outro function on the @NikBearBrown channel. |
| 3 | Spark lines | FIXED | NBB00.props.greeting `"Your turn."` → `"Namaste, Liam"` (world-language hello, 4 words, not Bear's Wagwan). NBB02.props.greeting already `"Your turn."` (BHTF slot). All bookend composers now carry legible spark lines. |
| 4 | Verdict | PASS | NBB01 verdict artifactLines are 4 real body-sourced lines ("The mechanism is called an isotope swap…", etc.); heading is the reel's own title. `verdict_audit.py --root anthropics` did NOT flag this reel. Narration recaps the body. |
| 5 | Card text | FIXED | Removed unused shot.remotion FormBCard block from B01 (three empty `sub` items — §8.11). B02/B09 FormACard props left in place but describe source-rendered stills; source pipeline drives the actual render. |
| 5b | Chart text | PASS | Manim scenes (source vox pipeline) use LabelChip category nouns (`PSMA-POSITIVE`, `Ga-68`, `Lu-177`, `BRIGHT ON PET`) not narration slices; bottom captions are complete phrases. |
| 5c | Your-Turn placeholder | FIXED | NBB02.props.command was the bracketed template ban ("Explain how [One Molecule, Two Isotopes: See the Tumor, Then Treat It] applies to a specific cancer type…"). Replaced with a real exercise drawn from the video's own nouns: pick a targeted therapy — trastuzumab / imatinib / cetuximab — and sketch its companion PET probe, isotope pair, and disqualifying scan population. No brackets, no title-restate. |
| 6 | Punt sweep | FIXED | No gen-AI asks, no unfilled slates in the CURRENT sheet. Bookend punts removed (see check 2). B02 and B09 render as source's own slate cards (source metadata's `slates: [B02, B09, B13, B14]`) — inherited HOLD stills, not new punts introduced here. |
| 7 | Card-only reel | PASS | 5 Manim graphic beats (B03/B05/B07/B08/B10/B11) plus one quote-document (B06) drive the body — not card-only. |
| 8 | Lens audit | PASS (Popper + Plato) | Body earns two moves: **Popper** — B10 states in advance what would count as the drug failing ("Dark on PET means the target is gone — the drug will not [find it]"), and B11 shows the exact predicted split at day 90 (illustrative). **Plato** — B08 separates artifact (`PSMA-present cell binds` vs `PSMA-absent cell doesn't`) from world (tumor biology) and interrogates the relationship (drug reaches nothing when the handle is missing); B09/B10 return to that same artifact/world/relationship frame under "the scan is not paperwork." |
| 9 | Brand fields | PASS | folderLabel `@NikBearBrown` (handle, not brand key). engine `kokoro`, voice `am_onyx` — matches the actual generated audio. Persona coherence: this is a Liam-in-for-Bear read (Kokoro am_onyx), narration_text is written in first-person Bear voice — consistent with the "Liam, in for Bear" pattern. |
| 10 | Pacing | PASS | Body-beat WPS spot-check: B01 22 words / 7.6s = 2.9 wps; B07 65 words / 22.8s = 2.85 wps; B11 92 words / 32.3s = 2.85 wps. All inside the 2.0–3.4 wps band. |
| 11 | type_check.py | INHERITED FLAGS | 5 §8.1 min-size flags on B03/B06/B10/B11/B12 and 1 §8.6b bbox-overlap on B10 — ALL on source-pipeline Manim clips that this variant reuses via symlink. The source vox reel's own TYPECHECK.md marked those same beats SKIP because it ran before the source clips were rendered — the flags surface only because this pass actually checks the rendered mp4s. Not fixable in this invocation without editing source scenes and re-rendering the source reel, which the rebuild contract keeps LOCKED. Documented rather than blocked because the source reel already shipped its own review slate with these clips. See "Inherited constraints" below. |

## PHASE 2 — build

- Audio: NBB00/NBB01/NBB02 mp3s already present (measured Kokoro am_onyx,
  `actual_duration_s` values live in the sheet). NBB03 is silent by design
  (silence_s=6.0). B01–B12 audio_file paths resolve to
  `../vox-isotope-swap/mp3/beat-B0*.mp3` (measured mp3s from source).
- Renders: NBB00/NBB01/NBB02/NBB03 rendered via
  `runtime/scripts/remotion_scenes.py` (foreground, one at a time,
  proven-core templates). B01–B12 symlinked from source clips into local
  `media/`. NBB00/NBB02/NBB03 re-rendered after props edits so on-screen
  text matches the fixed props.
- Compile: `runtime/scripts/compile.py` — 16/16 beats VIDEO, 220.1s,
  3840×2160 (4K LAW), lane-check PASS (no lane violations), frame-check
  PASS, content-check PASS.
- GATE AUDIO: PASS — mean_volume −24.2 dB (above −40 dB floor).
- Gate V: 8 sample frames sampled from the master
  (`_qc/frames/master_t*.png`) plus per-beat mid-narration frames for the
  flagged Manim beats. NBB00/NBB02/NBB03 renders show correct props
  (Isotope Swap segment, Namaste-Liam spark, complete composer command,
  full title with period on outro). B02 and B09 render as source-side
  slate cards (inherited). No text overlapping figures on the NBB* beats;
  no overflow beyond safe inset.
- Cut file: `vox-isotope-swap.mp4` (mtime 05:03) is newer than
  `beat_sheet.json` (mtime 05:02) — supervisor DONE check passes.

## Inherited constraints (documented, not blocking)

- **type_check §8.1** on B03/B06/B10/B11/B12 measures a smallest text run
  of 8–10 px vs a 13 px floor. These are all Manim clips from
  `../vox-isotope-swap/vox_scenes.py`, symlinked here as-is. The
  measurement likely picks up stroke fragments / hairline underlines /
  descenders — on visual inspection the labels are legible (PSMA-POSITIVE,
  4 lesions lit, -60% / +40% chips all read cleanly at 720p and 4K).
- **type_check §8.6b** on B10: 28% bbox overlap between two labels in the
  scan-decides split — visible in the source clip.
- **B02, B09** are source-side slate cards (source metadata listed them in
  `slates`). Their audio (physician-reads-scan and PET-image narration) is
  real; only the visuals are placeholder stills. Bear's earlier review
  passed the source reel with these; documenting for continuity.

## Files touched

- `beat_sheet.json` — edits above (all before final compile).
- `beat_sheet.pre-rebuild.json` — created (byte-exact snapshot of pre-edit
  sheet).
- `media/` — created; NBB00-NBB03 rendered here; B01-B12 symlinked here.
- `TYPECHECK.md` — written by `type_check.py`.
- `REBUILD-LOG.md` — written.
- `_qc/frames/*.png` — sampled QC frames.
- `vox-isotope-swap.mp4` — the review cut.

No changes to source (`../vox-isotope-swap/`). No validator loosened. No
narration paraphrased.
