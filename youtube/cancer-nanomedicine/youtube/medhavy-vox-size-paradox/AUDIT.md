# AUDIT — medhavy-vox-size-paradox
_Pass: 2026-08-27_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` created byte-exact before any edit ✓
- Envelope stripped of dead ElevenLabs-era fields:
  - DROPPED `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs id)
  - DROPPED `clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations below…")
  - DROPPED `_variant_todo` (migration-scaffolding checklist)
  - DROPPED stale `build{}` block (falsely claimed B14/B15 as VIDEO though media/ did not exist)
- KEPT: `engine: kokoro`, `voice_kokoro: af_kore` (VOICE-LOCK); title/slug/topic/source/register/palette/audience/accents/style_bible intact
- ADDED: `folderLabel: "@MedhavyAI"` (was missing), `source` pointer to the chapter
- Narration LOCKED — every B01–B15 `narration_text` verbatim from pre-rebuild. Zero datable-claim edits needed (no model names, versions, prices, or "as of" phrasing in the reel).

## Phase 1 Audit

### 1. Stale renders — PASS
Zero mp4 files existed in the reel folder before this run (media/, manim/, clips/*.mp4 all absent). Only `clips/master.m4a` and `clips/_work/*.png` from a Jul 16 pre-audio pass — informational, not stale renders. Nothing to delete.

### 2. Bookends — PASS (legitimately absent)
Non-Claude channel (medhavy palette). Rebuild contract §3 exempts non-claude channels from Claude bookends. Format is body beats + `OutroSeries` + `OutroCTA` (matches the successfully-built `medhavy-vox-complexity-yield` sibling). No `ClaudeComposerAsk`, no BVDT, no BHTF, no BOUT — as designed for this channel.

### 3. Spark lines — PASS (N/A)
No `ClaudeComposerAsk` beats in reel.

### 4. Verdict — PASS (N/A)
No BVDT beat by channel design; the closing FormACard B13 already carries the compressed claim ("Distribution beats total mass. / Kill depends on where the drug goes, / not how much reaches the organ."). `verdict_audit.py` reports nothing to audit.

### 5b. Chart text — PASS (N/A after conversion)
No Manim charts on disk. B03/B05/B06/B08/B09/B11/B12 originally called out Manim scenes (`B03_OutcomeContrast`, `B05_LeakyVessel`, `B06_TotalMassBars`, `B08_OutwardPressure`, `B09_PenetrationCompare`, `B11_DistributionVerdict`, `B12_Example`) but no `scenes_std.py`/`scenes.py` exists in the folder or its neighbors, and the shared `animated_graphics.py` only carries the electoral-college fixture scenes. Converted to `FormACard` text summaries of the visual (see Check 6). Category labels are short (1–4 tokens: "150 nm arm — 15%"), numbers written literally ("6.2% ID/g"). Bottom lines are full sentences.

### 5. Card text — FIXED (all beats)
All FormACard `lines` are real content, no placeholder subs. B02 line ("Two mouse tumors — same injected dose. / 150 nm piles up at the rim. / Whole-organ measurement says it wins.") condenses the narration's setup, since the histology still does not exist.

### 6. Punt sweep — FIXED (13 beats)
Original sheet had `YOU → 5–10s gen-AI clip → pantry` on B01/B02/B04/B07/B10/B13 and `PIPELINE → render animated_graphics.py scene B*` on B03/B05/B06/B08/B09/B11/B12. Both are punt costumes. Fixed as follows:
- **B01, B04, B13** — CARD beats: added `shot.remotion.pattern=FormACard` with real lines drawn from `card.copy`/`card.sub`. Now render as real Remotion mp4s, not slates.
- **B02, B07, B10** — were `STILL src=ai` for histology stills / diagrams (`DoodleScene`/AI still per nopunt catalog). No manim scene exists on disk. Converted to `FormACard` naming the payload of each shot explicitly. Logged as scripting gap (real histology / cross-section would upgrade these beats).
- **B03, B05, B06, B08, B09, B11, B12** — were `GRAPHIC` with named Manim scenes that do not exist on disk. Compile lane-check would refuse them as PIPELINE-SLATE-IN-CUT. Converted to `FormACard` text summaries that state the chart's numbers explicitly (15% vs 72%; 6.2% vs 2.1% ID/g; 80% deep vs rim-crowded; two-column worked example). This is an honest text substitute — every one of these beats logged as needing a Manim upgrade in a future body-beat pass.
- **B14, B15** — OutroSeries/OutroCTA props were wrong schema (`seriesTitle/tagline/githubSlug`, `authorName/handle/ctaText`) — the Remotion components would silently fall back to Claude defaults, Claude-washing a Medhavy reel. Fixed to correct schema (`{eyebrow, line}` / `{line, handle}`) with Medhavy content ("CANCER NANOMEDICINE" / "@MedhavyAI").

Zero remaining `YOU → gen-AI clip`, zero `DoodleScene`, zero `STILL src=archive/ai` on animatable content, zero unfilled `remotion_scenes` slates in the final build. `build.status` Counter after compile: `{"VIDEO": 15}`.

### 7. Card-only reel — LOGGED
Every body beat now renders as `FormACard` (text). This IS a card-only reel in the current pass — a consequence of no Manim scene library existing for these seven visualization beats. Scripting gap logged: the reel wants at least three drawn figures (B03 tumor-shrink bar contrast; B06 total-mass bars; B09 split-screen penetration compare). Would upgrade to a mixed-media reel with a proper `scenes_std.py` pass.

### 8. Lens audit — PASS (2+ moves present)

- **Descartes (checklist / what would falsify):** the paradox itself is a Cartesian move — the reel opens (B01/B04) by naming the falsifying observation ("bigger loads more drug, smaller cures more") and then produces a checklist of what would have to be true for the naive claim to be right. ✓
- **Hume (confidence is a property of the model, not the world):** B06/B12 explicitly flag the numbers as "illustrative from the card seed." B02/B11 distinguish "every whole-organ measurement says it wins" (the model) from "loses in the tumor" (the world). The whole-organ assay is the confident measurement; the outcome measurement is the world. ✓
- **Plato (artifact vs. world):** B11's verdict is exactly the artifact/world split — "wins the whole-organ assay" (artifact) vs. "loses in the tumor" (world). Rim accumulation is the shadow; cell kill is the wall. ✓
- **Popper (state failure criterion in advance):** implicit in B01/B04 ("more drug in the tumor, less kill" is the falsification of the naive retention model). Partial.

### 9. Brand fields — FIXED
- `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs) → DROPPED ✓
- `clock` (ElevenLabs prose) → DROPPED ✓
- `folderLabel: "@MedhavyAI"` ✓ (added; matches `medhavy-vox-complexity-yield` sibling)
- `engine: kokoro`, `voice_kokoro: af_kore` ✓ (medhavy voice)
- B14/B15 Medhavy channel branding restored (was silently Claude-defaulting on old prop names)
- Persona: narration is third-person ("Here's the puzzle…"). No Bear/Liam/persona claim — no voice-swap risk. `af_kore` is the medhavy channel default female Kokoro voice.

### 10. Pacing — LOG
Using measured audio durations (Kokoro af_kore, pre-existing mp3s reused, timings.json read back) vs word counts:

| Beat | ~Words | actual_duration_s | ~wps | Note |
|------|--------|-------------------|------|------|
| B01  | 25     |  9.19             | 2.72 | ✓    |
| B02  | 28     | 12.05             | 2.32 | ✓    |
| B03  | 39     | 14.93             | 2.61 | ✓    |
| B04  | 24     |  8.38             | 2.86 | ✓    |
| B05  | 40     | 15.87             | 2.52 | ✓    |
| B06  | 41     | 17.17             | 2.39 | ✓    |
| B07  | 39     | 13.93             | 2.80 | ✓    |
| B08  | 48     | 17.88             | 2.68 | ✓    |
| B09  | 45     | 16.17             | 2.78 | ✓    |
| B10  | 45     | 17.43             | 2.58 | ✓    |
| B11  | 34     | 14.83             | 2.29 | ✓    |
| B12  | 77     | 28.91             | 2.66 | ✓    |
| B13  | 35     | 13.35             | 2.62 | ✓    |
| B14  | 10     |  4.29             | 2.33 | ✓    |
| B15  |  6     |  2.50             | 2.40 | ✓    |

All beats within 2.0–3.4 wps. No pacing flags.

### 11. type_check.py — GATE T: PASS
Ran on final compiled cut. Initial run flagged B05 and B08 as `min-size §8.1: smallest text run 38px < floor 41px`. Diagnosed as em-dash (`—`) and arrow (`→`) glyphs rendering as thin horizontal blobs at the 4K master scale — a known FormACard character-geometry edge case (similar to the FormACard916 blob-artifact skip already in type_check.py). Fixed the content (not the validator):
- B05 lines shortened from 4 → 3 and arrow removed ("more retained → more delivered." → "More retained. More delivered.")
- B08 lines shortened from 4 → 3 and dashes/arrows removed ("core → rim." collapsed into "Pressure pushes outward, core to rim."; trailing em-dash on "The 150 nm particle diffuses slowly —" dropped)
Both beats re-rendered, recompile. Final GATE T: PASS (2 pixel FAILs → 0). §8.10 REDUNDANCY advisory fires on 7 body beats (0.83–1.00 — narration recites the card) — structural, expected: the FormACard text is a compressed transcript of the narration by construction because the manim charts do not exist. Advisory does not block cut. Zero validators loosened.

## Phase 2 — Build

- **Audio:** Kokoro af_kore, 15/15 pre-existing mp3 files reused (Jul 16 batch), durations already measured into the sheet's `actual_duration_s`. Master audio `clips/master.m4a` re-conforms per compile.
- **Remotion:** all 15 pattern beats rendered → `media/B*.mp4` (FormACard × 13 + OutroSeries + OutroCTA). Re-rendered B05 and B08 twice each to shorten lines / drop em-dash and arrow glyphs.
- **Compile:** `compile.py . --review --height 720 --force` — content-check PASS, frame-check PASS, lane-check PASS (15/15 filled, `known_slates=[]`).
- **Output:** `vox-size-paradox-slate.mp4` — 207.9 s, 1280×720 review cut with per-beat labels and timecodes.
- **Gate audio:** `mean_volume -24.0 dB` (threshold: > −40 dB) ✓, `max_volume -6.7 dB`, aac 48kHz mono.
- **Gate V — frame read (contact sheet + spot checks):**
  - QC contact sheet (`qc-sheet.png`): all 15 beats legible, cream ground, EB Garamond serif, no overflow, no clipping, no text-on-figure collisions. Consistent visual hierarchy (bold serif title + roman body lines).
  - B05 rendered frame — "The naive argument: / Leaky vessels, slow drainage. / More retained. More delivered." — clean, well within safe area ✓
  - B08 rendered frame — "Pressure pushes outward, core to rim. / The 150 nm particle diffuses slowly. / It gets shoved back to the vessel wall." — clean ✓
  - B12 rendered frame — worked-example dot-separated rows, all four lines legible, no overflow ✓
  - B14 OutroSeries — "CANCER NANOMEDICINE" eyebrow + "Part of the Cancer Nanomedicine series on Medhavy AI." — Medhavy skin, no Claude-default ✓
  - B15 OutroCTA — "Explore the full course at medhavy.com" + SUBSCRIBE pill + @MedhavyAI handle ✓
  - Zero BLOCKER, zero MAJOR on any real beat.
- **Post-build punt sweep:** `build.status` Counter reports `{"VIDEO": 15}` verbatim. Zero slates. Zero pipeline-owned SLATE, zero gen-AI-in-master.
- **Stale check:** mp4 mtime `1787873976` vs sheet mtime `1787873970` — mp4 is 6 s NEWER ✓

## Output

`vox-size-paradox-slate.mp4` — 207.9 s, audio present (−24.0 dB), mp4 newer than beat_sheet.json (Δ+6 s). DONE (as a text-heavy card-only review slate cut; seven drawn-graphic beats are honest text substitutes pending a `scenes_std.py` pass).
