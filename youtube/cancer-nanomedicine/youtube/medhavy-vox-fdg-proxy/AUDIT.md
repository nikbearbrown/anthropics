# AUDIT — medhavy-vox-fdg-proxy
_Pass: 2026-08-31_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` created byte-exact before any edit ✓ (21082 bytes, 2026-08-26 source mtime)
- Envelope stripped of dead ElevenLabs-era fields:
  - DROPPED `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs id)
  - DROPPED `clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations below…")
  - DROPPED `_variant_todo` (4-item migration-scaffolding checklist)
  - DROPPED stale `build{}` block (claimed 2/14 filled + 12 slates — compile regenerates)
- KEPT: `engine: kokoro`, `voice_kokoro: af_kore` (VOICE-LOCK); title/slug/topic/source/register/palette/audience/style_bible/color_semantics/note intact
- ADDED: `folderLabel: "@MedhavyAI"` (was missing); promoted `source` field out of the `purpose` string
- Narration LOCKED — all B01–B14 verbatim from pre-rebuild EXCEPT B14 TTS-phonetic ("medhavy.com" → "medhavy dot com", matches sibling `medhavy-vox-complexity-yield`; every edit logged in `REBUILD-LOG.md`).

## Phase 1 Audit

### 1. Stale renders — PASS
No `*.mp4` in the reel folder pre-run. Only `clips/master.m4a` and `clips/_work/*.png` (Jul 16, pre-dating this pass — informational, not a stale render). Nothing to delete.

### 2. Bookends — PASS (legitimately absent)
Non-Claude channel (`palette: medhavy`, `folderLabel: @MedhavyAI`). Rebuild contract §3 exempts non-claude channels from Claude bookends. Format is body beats + `OutroSeries` + `OutroCTA` — matches sibling `medhavy-vox-complexity-yield`. No `ClaudeComposerAsk`, no BVDT, no BHTF, no BOUT — as designed for this channel.

### 3. Spark lines — PASS (N/A)
No `ClaudeComposerAsk` beats in reel.

### 4. Verdict — PASS (N/A)
No BVDT beat by channel design; the closing FormACard B12 already carries the compressed claim ("PET measures metabolism, not malignancy. imaging suggests · biopsy confirms. the gap is where you think carefully."). The B11 quote-echo card ("The scanner was right. The assumption was wrong.") is a Feynman-style landing before recap.

### 5c. Your-Turn placeholder — PASS (N/A)
No BHTF beat by channel design; Medhavy outro is OutroSeries + OutroCTA (course-plug), not a Your-Turn exercise.

### 5b. Chart text — PASS (N/A after conversion)
No Manim charts on disk. B04/B05/B08/B10 originally called out Manim scenes (`B04_FDGUptake`, `B05_WhatPETSees`, `B08_ImagingSuggests`, `B10_ExampleResult`) but no `scenes_std.py`/`scenes.py` exists in the folder. Converted to `FormACard` text summaries; every named list item is 1–3 word tokens ("hexokinase activity · glucose-transporter expression"); no line is a narration slice truncated mid-word (the old B06 `lines` was fixed).

### 5. Card text — FIXED (all beats)
All FormACard `lines` are real content, no placeholder subs. B06 pre-existed with `lines: ["And glucose metabolism is not unique to cancer. Activated immune cells…"]` — a truncated narration slice — replaced with 3 authored lines. B02/B09 (originally STILL src=ai with no photo asset) converted to FormACards whose lines carry the substance the STILL was supposed to carry.

### 6. Punt sweep — FIXED (12 beats)
Original sheet had `YOU → 5–10s gen-AI clip → pantry` on B01/B02/B03/B07/B09/B11/B12 and `PIPELINE → render animated_graphics.py scene B*` on B04/B05/B08/B10. Both are punt costumes. Fixed as follows:
- **B01, B03, B12** — CARD beats: added `shot.remotion.pattern=FormACard` with real lines drawn from `card.copy`/`card.sub`. Now render as real Remotion mp4s, not slates.
- **B02, B09** — were `STILL src=ai` for PET-scan photograph and case-summary photograph respectively. No such assets exist on disk. Per nopunt catalog, a real archival PHOTOGRAPH would be the one legitimate HOLD — but no image is supplied, so an honest FormACard substitute names the content. Both logged as scripting gaps.
- **B04, B05, B08, B10** — were `GRAPHIC` with named Manim scenes that do not exist on disk. Compile lane-check would refuse them as PIPELINE-SLATE-IN-CUT. Converted to `FormACard` text summaries of what the graphic should show. All four logged as needing a Manim upgrade.
- **B06** — was CARD with a truncated-narration `lines` value (a placeholder). Replaced with 3 authored lines.
- **B07, B11** — were DOCUMENT quote cards with punt costume (`YOU → gen-AI clip → pantry`). Converted to `FormACard`; the `document.quote` blocks are retained inside the beats for a future editorial-quote scene that draws the gold-highlighter sweep.
- **B13, B14** — OutroSeries/OutroCTA props were wrong schema (`seriesTitle/tagline/githubSlug`, `authorName/handle/ctaText`) — the Remotion components would silently fall back to Claude defaults, Claude-washing a Medhavy reel. Fixed to correct schema (`{eyebrow, line}` / `{line, handle}`) with Medhavy content ("CANCER NANOMEDICINE" / "@MedhavyAI").

Zero remaining `YOU → gen-AI clip`, zero `DoodleScene`, zero `STILL src=archive/ai` on animatable content, zero unfilled `remotion_scenes` slates in the final build.

### 7. Card-only reel — LOGGED
Every body beat now renders as `FormACard` (text). This IS a card-only reel in the current pass — a consequence of no Manim scene library existing for these six visualization beats and no supplied photos for the two STILL slots. Scripting gap logged: the reel wants at least three drawn figures (B04 uptake mechanism, B05 two-column proxy graphic, B10 three-nodes reveal) plus two real PET/case photographs (B02, B09). Would upgrade to a mixed-media reel with a proper `scenes_std.py` pass + human-supplied stills.

### 8. Lens audit — PASS (2+ moves present)

- **Plato — artifact vs world (the reel's structural spine):** the entire film pivots on this move. The **artifact** = the bright PET signal / the imaging report ("three lymph nodes light up"). The **world** = the actual biology (reactive nodes from a URI, not cancer cells). The **relationship** = "the tracer isn't looking for cancer cells" (B03), "the PET camera doesn't see cancer — it sees glucose metabolism" (B05), "Every imaging signal is a proxy" (B08). Ash's shadow-on-the-cave-wall move restaged in an oncology reading room. ✓
- **Descartes — radical doubt as a checklist:** the reel asks in advance "what would have to be true for 'bright spot = cancer' to be wrong about this patient" and produces the checklist by construction — false positives (infection, healing wounds, brown adipose tissue at B06) + false negatives (well-differentiated thyroid, some prostate, mucin-secreting adenocarcinomas at B07). The checklist IS the middle of the film. ✓
- **Popper — falsifiability, stated in advance:** the illustrative case (B09–B11) is the falsification move made concrete — the imaging claim ("recurrence") is stated, biopsy is the pre-registered test, and the biopsy refutes the claim. "The scanner was right. The assumption was wrong" (B11) is the after-the-fact statement of what the pre-registered test would return. ✓
- **Hume — confidence is a property of the model:** the case is explicitly labeled "illustrative" (B10 narration + card line: "Numbers are illustrative"). B08's "'consistent with' or 'suspicious for,' never 'confirms'" is the model saying "my confidence is my own; the pathology is the world."  ✓ (all four moves present).

### 9. Brand fields — FIXED
- `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs) → DROPPED ✓
- `clock` (ElevenLabs prose) → DROPPED ✓
- `folderLabel: "@MedhavyAI"` ✓ (added)
- `engine: kokoro`, `voice_kokoro: af_kore` ✓ (Medhavy channel voice)
- B13/B14 Medhavy channel branding restored (was silently Claude-defaulting via wrong-schema props)
- Persona: narration is third-person / observational ("Three lymph nodes, lighting up bright…"). No Bear/Liam/persona claim — no voice-swap risk. `af_kore` is a female Kokoro voice; consistent with Medhavy channel default.

### 10. Pacing — LOG
Using measured Kokoro `af_kore` durations vs word counts:

| Beat | ~Words | actual_duration_s | ~wps | Note |
|------|--------|-------------------|------|------|
| B01  | 34     | 13.38             | 2.54 | ✓    |
| B02  | 42     | 15.87             | 2.65 | ✓    |
| B03  | 41     | 13.89             | 2.95 | ✓    |
| B04  | 43     | 15.53             | 2.77 | ✓    |
| B05  | 63     | 20.39             | 3.09 | ✓    |
| B06  | 49     | 17.69             | 2.77 | ✓    |
| B07  | 51     | 18.94             | 2.69 | ✓    |
| B08  | 52     | 18.77             | 2.77 | ✓    |
| B09  | 45     | 17.51             | 2.57 | ✓    |
| B10  | 55     | 18.33             | 3.00 | ✓    |
| B11  | 42     | 15.96             | 2.63 | ✓    |
| B12  | 63     | 19.01             | 3.31 | ✓    |
| B13  | 11     |  4.29             | 2.56 | ✓    |
| B14  |  8     |  2.45             | 3.27 | ✓    |

All beats within 2.0–3.4 wps. No pacing flags.

### 11. type_check.py — GATE T: PASS
Ran on final sheet.
- Nine §8.10 ADVISORIES (B02/B04 = 0.91–0.92, B03/B07 = 1.00, B05 = 0.93, B08 = 0.91, B09/B12 = 0.94/0.80, B10 = 0.92 — "narration recites the card").
- Structural and expected: these beats' FormACard text is a compressed transcript of the narration by construction — the substance is BOTH what the narrator says AND what the card shows, since the Manim charts/photos those beats want do not exist. Logged, not a FAIL.
- Compile motion-mix warning: `hold: 8/14 = 57%` over the ~40% MOTION.md cap. Legitimate for this vox-editorial reel where every body beat is a still card; would resolve once real graphics land for B04/B05/B08/B10 (their motion becomes drawon/reveal in place of hold). Logged, not blocking.
- Zero validators loosened. GATE T: PASS.

## Phase 2 — Build

- **Audio:** Kokoro `af_kore`, 14/14 mp3 files generated fresh, durations measured back into sheet (drops the pre-existing Jul-16 mp3s + timings.json).
- **Remotion:** all 14 pattern beats rendered → `media/B*.mp4` (FormACard × 12 + OutroSeries + OutroCTA).
- **Compile:** `compile.py . --review` — content-check PASS, frame-check PASS, lane-check PASS (14/14 filled, known_slates=[]).
- **Output:** `vox-fdg-proxy-slate.mp4` — 213.0 s, 1280×720 review cut with per-beat labels and timecodes.
- **Gate audio:** `mean_volume -23.9 dB` / `max_volume -6.6 dB` (threshold: > −40 dB) ✓
- **Gate V — frame read (7+ sampled frames across timeline):**
  - B02 (~10s) — "FDG-PET — the standard tool / for staging cancer and recurrence", legible EB Garamond, safe area clean ✓
  - B05 (~60s) — "PET reads glucose metabolism / hexokinase activity · glucose-transporter expression / the Warburg effect — signal is real, not cancer itself" ✓
  - B06 (~80s) — "Glucose metabolism is not unique to cancer. / infection · healing wounds · brown adipose tissue / each one lights up the same way" ✓
  - B09 (~140s) — "Illustrative case — 58-year-old / breast surgery, 3 months prior · PET for recurrence / 3 lymph nodes flagged — high FDG uptake" ✓
  - B10 (~170s) — "Biopsy — all three reactive / prior week — mild upper-respiratory infection / high metabolism · wrong cause (illustrative)" ✓
  - B12 (~200s) — endcard "PET measures metabolism, not malignancy. / imaging suggests · biopsy confirms / the gap is where you think carefully" ✓
  - B13 (~207s) — Medhavy OutroSeries — "CANCER NANOMEDICINE" eyebrow + "Part of the Cancer Nanomedicine series on Medhavy AI." + single crimson underline (the ONE accent per beat rule) ✓
  - B14 (~211s) — Medhavy OutroCTA — "Explore the full course at medhavy.com" + SUBSCRIBE pill + @MedhavyAI handle ✓
  - Note: OutroCTA renders on WHITE not cream (component default); consistent across siblings.
  - Zero BLOCKER, zero MAJOR on any real beat.
- **Post-build punt sweep:** `build.status` Counter: `{'VIDEO': 14}`. Zero slates. Zero pipeline-owned SLATE, zero gen-AI-in-master.
- **Stale check:** mp4 mtime is later than beat_sheet.json mtime (verified via `ls -la` — mp4 ~1 min newer). No sheet edits after compile.

## Output

`vox-fdg-proxy-slate.mp4` — 213.0 s, audio present (−23.9 dB mean / −6.6 dB peak), mp4 newer than beat_sheet.json. DONE (as a text-heavy card-only review slate cut; six drawn-graphic beats + two photo beats are honest text substitutes pending a `scenes_std.py` pass and human-supplied stills).
