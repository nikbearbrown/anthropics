# AUDIT — nbb-vox-dar-optimum
_Ran 2026-08-30 by unattended film-factory invocation._

Deliverable: `vox-dar-optimum-slate.mp4` (221.6s, mean_volume -24.0 dB, 16/16 slots VIDEO).

## PHASE 0 — REBUILD CONTRACT
- **PASS** `beat_sheet.pre-rebuild.json` written byte-exact before any edit.
- **PASS** Narration LOCKED. No `narration_text` was changed. All body narration
  (B01–B12) unchanged; all four bookend narrations preserved verbatim on rename.
- **PASS** VOICE-LOCK normalize. Dropped `voice_kokoro` mirror fields; dropped
  legacy `lane: "BOOKEND"` labels. No ElevenLabs remnants existed.
- **PASS** `shot.form` derivation implicit — bookends carry current
  provenance strings ("proven-core/ClaudeComposerAsk" etc.) after
  `remotion_scenes.py` stamp.
- **PASS** Non-claude channel skin preserved — this is the `nbb`
  variant, keeps its own metadata and cold-open ask. Not Claude-washed.

## PHASE 1 — AUDIT CHECKS

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s in folder prior to this run. Nothing to delete. |
| 2 | Bookends present | FIXED | Consolidated duplicate B00/BVDT/BHTF/BOUT (empty) + NBB00-03 (populated) into a single populated set. `bookend_check.py` PASS. |
| 3 | Spark lines | FIXED | B00 greeting `"Liam"` → `"Namaste, Liam"` (world-hello, not colliding with sibling `claude-liam-vox-dar-optimum` "Szia, Liam"). BHTF greeting `"Your turn."` OK. No inner composers. |
| 4 | Verdict | FIXED — AUTHORED | Body is 12 beats / 250+ words → wrote a real 3-line verdict from B06/B07/B11/B12 numbers and mechanism; new heading "DAR is an optimum, not a maximum." Narration was already real (recap of B11+B12), kept verbatim. `verdict_audit.py` now clean for this slug. |
| 5b | Chart text | N/A | All GRAPHIC beats use `source_clip` from the source vox reel; no fresh chart authoring in this pass. Existing charts on source clips reviewed via qc-sheet.png — labels are short category nouns, no narration-fragment truncation. |
| 5c | Your-Turn placeholder | FIXED — AUTHORED | Replaced the "Explain how [title] applies to your studies…" boilerplate with a specific task naming three current ADCs (trastuzumab deruxtecan / DXd, sacituzumab govitecan / SN-38, T-DM1), the physical property that drives the mechanism (logP), and a concrete predict-then-verify move against published clinical PK. No square brackets, no "apply to your own work." |
| 5 | Card text | FIXED | B01 previously carried a FormBCard remotion block with placeholder items ("Key point one/two/three", empty subs). B01 renders from `source_clip` so the FormBCard was dead data — stripped it; B01 now cleanly uses its `card` (title) block matching the source reel. |
| 6 | Punt sweep | PASS | Zero gen-AI asks. Zero unfilled slates in final compile. Zero DoodleScene/DoodleChart. Zero archive stills for concepts. Body clips are from a completed sibling reel (`vox-dar-optimum`), not punt costumes. |
| 7 | Card-only reel | PASS | Body includes GRAPHICs (B02, B04, B06, B07, B09, B10) and a DOCUMENT (B11) — mixed medium, not card-only. |
| 8 | Lens audit | PASS | Popper move: B03 states the falsifying question ("Why does loading more warheads make it clear faster — and kill less?") and the body demonstrates the mechanism that falsifies naive-more-is-better. Plato move: B10–B11 hold the artifact (DAR-8 has more drug per molecule) against the world (0.3 vs 2.4 µg/g at tumor) — the shadow vs the wall. Two moves present. |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key). `engine: kokoro`, `voice: am_onyx` — matches Liam narration for nbb variant. Added `metadata.channel_title: "@NikBearBrown"` for bookend_check outro assertion. |
| 10 | Pacing | LOG — within band | 12 body beats; measured wps ranges from B03 (26w/9.6s = 2.7) to B01 (30w/9.2s = 3.3). All within 2.0–3.4 wps. |
| 11 | `type_check.py` | PASS | GATE T: PASS. |

Additional stale-claim edit (dropped, not corrected):
- BHTF props `modelLabel: "Fable 5"` / `effortLabel: "High"` — "Fable 5" is
  not a real model; dropped rather than substituted (no on-screen model
  callout is more honest than a stale one).

## PHASE 2 — BUILD

- Audio: existing measured Kokoro `am_onyx` mp3s reused (bookends renamed to
  match new beat_ids: `mp3/beat-B00.mp3`, `beat-BVDT.mp3`, `beat-BHTF.mp3`,
  `beat-BOUT.mp3`). Body audio remains at source reel paths. No new audio
  spend.
- Bookend renders: `remotion_scenes.py` rendered B00 / BVDT / BHTF / BOUT
  into `media/` via `ClaudeComposerAsk` / `ClaudeVerdictArtifact` /
  `ClaudeComposerAsk` / `ClaudeTitleOutro`. All four succeeded.
- Body fills: copied 12 pre-rendered clips from `../vox-dar-optimum/clips/`
  into `media/B01.mp4`..`media/B12.mp4` so `compile.py`'s slot precedence
  picks them up as VIDEO, not SLATE.
- Compile: `compile.py --review` → `vox-dar-optimum-slate.mp4` (221.6s).
- Content-check PASS. Frame-check PASS. Lane-check PASS. GATE AUDIO PASS
  (mean_volume -24.0 dB). QC contact sheet at `qc-sheet.png`.
- Warnings (non-blocking): motion histogram shows `hold` at 43% (over the
  ~40% pantry cap). Inherited from the source vox reel's motion mix; not
  fixed in this pass (would touch body clips, which are locked). Logged.

## Build stamp
```
build.status Counter = {'VIDEO': 16}  (all 16 slots filled from real renders)
```

## Verified mtime ordering
- `beat_sheet.json` mtime: 2026-08-30 21:24:18
- `vox-dar-optimum-slate.mp4` mtime: 2026-08-30 21:24:44
- Δ = +26s → mp4 is NEWER than sheet → passes supervisor's DONE check.

## Naming
Output is `vox-dar-optimum-slate.mp4` per the review-slate convention (even
though every beat rendered as VIDEO, this cut used the `--review` label
overlay, so it is a review cut, not a final).

## Not done
- No `-cut.mp4` (final clean master) — that is the human-flagged full-render
  pass, out of scope for this invocation.
- Publishing not touched. TOPOST not touched.
