# AUDIT.md — medhavy-vox-tumor-pressure

**Path**: anthropics/youtube/cancer-nanomedicine/youtube/medhavy-vox-tumor-pressure
**Date**: 2026-08-27
**Verdict**: BLOCKED — do NOT build.

## Pipeline classification

This reel is **NOT a Claude/Liam Brutalist bookend reel** — it is a **Vox-style medhavy
audience variant** scaffolded by `books/vox/scripts/vox_variant.py`. Its parent is
`vox-tumor-pressure` (a Vox editorial explainer, cream/newsprint ground, isotype +
Ken Burns + STILL/GRAPHIC/DOCUMENT axis).

Because of that, the PHASE 1 checks in the factory prompt map only partially:

| Check | Applies? | Result |
|---|---|---|
| 1 stale renders | yes | PASS — no `*.mp4` exists in the reel dir to be stale (never compiled) |
| 2 bookends B00/BVDT/BHTF/BOUT | **N/A** | Vox format uses OUTRO B12/B13 (`OutroSeries` + `OutroCTA`). Correct for this pipeline. |
| 3 spark lines / ClaudeComposerAsk | **N/A** | No ClaudeComposerAsk beats — different skin. |
| 4 verdict / BVDT | **N/A** | Vox recap is B11, not a Claude verdict artifact. |
| 5b chart text | N/A | No Manim rendered yet. |
| 5 card text | partial | B02 FormACard `lines` is a single narration slice ending "The drug…" — that is a **placeholder slate**, not a real card. |
| 6 punt sweep | **FAIL — BLOCKING** | 11 of 13 beats (B01–B11) carry `"YOU → 5–10s gen-AI clip → pantry"` — the exact §6 punt costume. Only B12 (OutroSeries) and B13 (OutroCTA) are real. |
| 7 card-only reel | FAIL | Every content beat is a slate placeholder; no beat currently draws anything. |
| 8 lens audit | out of scope | This is a scientific mechanism explainer, not a computational-skepticism reel. |
| 9 brand fields | mostly ok | metadata still carries dead ElevenLabs `voice_id: 1sgY6Voq1aexKOB1IJ2D`; engine=kokoro + `voice_kokoro: af_kore` (Medhavy voice) is authoritative for the mp3s. |
| 10 pacing | LOG | Ratio audit skipped — content is placeholder; would remeasure only after real narration passes. |
| 11 `type_check.py` | **N/A** | The Brutalist runtime `type_check.py` does not apply to Vox reels. The Vox equivalents are Gate A / Gate W / Gate B inside `vox_run.sh`, which cannot fire without a `vox_scenes.py`. |

## What actually exists

- `beat_sheet.json` — variant sheet, palette=medhavy, register=Wonder, 13 beats, audio measured.
- `mp3/beat-B01.mp3` … `beat-B13.mp3` + `mp3/timings.json` — per-beat Kokoro audio (Jul 16).
- `clips/master.m4a`, `clips/manifest.json`, per-beat slate PNGs in `clips/_work/` — an
  audio-only assembly plus slate stills, no video ever composited.
- **No `vox_scenes.py`** in this directory. The variant needs its OWN medhavy-palette
  scenes; `vox_run.sh` REFUSES with exit 2 when a reel lacks `vox_scenes.py`.
- **No `media/` dir, no Manim renders, no `<slug>.mp4`, no `<slug>-slate.mp4`.**
- **No paperwork set** (`FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`) — GATE F would fail
  in `vox_run.sh` even if `vox_scenes.py` existed.
- Parent `vox-tumor-pressure/` itself has never rendered a cut either — its
  `vox_scenes.py` exists (B01/B03/…/B11 authored) but nothing has been compiled from it.

## Why this stops here

Bringing this reel to a review slate cut requires the Vox pipeline, not the Brutalist
scripts named in the factory prompt (`stale_check.py`, `spark_line_fix.py`,
`verdict_audit.py`, `verdict_strip.py`, `runtime/scripts/type_check.py`,
`runtime/scripts/compile.py` — none of these apply here). The Vox pipeline needs, at
minimum:

1. A `medhavy-vox-tumor-pressure/vox_scenes.py` authoring one Scene per GRAPHIC/CARD
   beat in the **medhavy palette** (parent's `vox_scenes.py` is in the default palette
   and cannot be reused as-is; deriving 11 scenes is a creative task).
2. `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` (GATE F prerequisite).
3. `bash books/vox/scripts/vox_run.sh <this reel>` → Manim render → Gate A/W/B →
   `vox_compile.py --review`.

That is a multi-hour authoring + rendering job, not a single unattended pass, and doing
it under the wrong SKILL contract would either (a) silently downgrade to a card-only
slate that violates §7 or (b) invent Manim scenes without a factcheck. Both are worse
than logging the block.

## What was NOT touched

- `beat_sheet.json` — NOT edited (freshness rule + rebuild contract; no
  `beat_sheet.pre-rebuild.json` snapshot created because no rebuild was attempted).
- No renders deleted, no validator loosened, no gen-AI clip authored, no publish action.

## Handoff

The right next actor is the Vox pipeline (or Bear directly). Recommended sequence for
that actor:

1. Author `medhavy-vox-tumor-pressure/vox_scenes.py` in the medhavy palette by
   adapting the parent's scenes; render targets are the same 11 GRAPHIC/CARD beats.
2. Write `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`.
3. `bash books/vox/scripts/vox_run.sh books/anthropics/youtube/cancer-nanomedicine/youtube/medhavy-vox-tumor-pressure`.
4. Gate V manually.

Until (1) exists, `vox_run.sh` exits 2 by design and no cut can be produced.
