# AUDIT — medhavy-vox-complexity-yield
_Pass: 2026-08-27_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` created byte-exact before any edit ✓
- Envelope stripped of dead ElevenLabs-era fields:
  - DROPPED `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs id)
  - DROPPED `clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations below…")
  - DROPPED `_variant_todo` (migration-scaffolding checklist)
  - DROPPED stale `build{}` block (falsely claimed B12/B13 as VIDEO though media/ did not exist)
- KEPT: `engine: kokoro`, `voice_kokoro: af_kore` (VOICE-LOCK); title/slug/topic/source/register/palette/audience intact
- ADDED: `folderLabel: "@MedhavyAI"` (was missing)
- Narration LOCKED — every B01–B13 `narration_text` verbatim from pre-rebuild. Zero datable-claim edits needed.

## Phase 1 Audit

### 1. Stale renders — PASS
No `*.mp4` in the reel folder pre-run. Only `clips/master.m4a` (Jul 16, pre-dating this pass — informational, not a stale render). Nothing to delete.

### 2. Bookends — PASS (legitimately absent)
Non-Claude channel (medhavy palette). Rebuild contract §3 exempts non-claude channels from Claude bookends. Format is body beats + `OutroSeries` + `OutroCTA` (matching hai/medhavy vox pattern). No `ClaudeComposerAsk`, no BVDT, no BHTF, no BOUT — as designed for this channel.

### 3. Spark lines — PASS (N/A)
No `ClaudeComposerAsk` beats in reel.

### 4. Verdict — PASS (N/A)
No BVDT beat by channel design; the closing FormACard B11 already carries the compressed claim ("More functions, more ways to fail. Simple designs translate."). `verdict_audit.py` reports nothing to audit.

### 5b. Chart text — PASS (N/A after conversion)
No Manim charts on disk. B04–B07/B09/B10 originally called out Manim scenes (`B04_GateMultiply`, `B05_YieldCollapse`, `B06_MathCard`, `B07_OneVsSix`, `B09_ProgramAB`, `B10_DesignChoice`) but no `scenes_std.py`/`scenes.py` exists in the folder or its neighbors. Converted to `FormACard` text summaries of the visual (see Check 6). Category labels are 1–3 word tokens ("Program A · 1 function · 11 of 12 pass"), numbers written literally ("0.9⁶ = 53%"). Bottom line is a full sentence.

### 5. Card text — FIXED (all beats)
All FormACard `lines` are real content, no placeholder subs. B02 line ("Six functions in one particle / gold core · iron shell · dye / drug · pH linker · antibody") condenses the narration's six-item list, since the manim schematic does not exist.

### 6. Punt sweep — FIXED (11 beats)
Original sheet had `YOU → 5–10s gen-AI clip → pantry` on B01/B02/B03/B08/B11 and `PIPELINE → render animated_graphics.py scene B*` on B04–B07/B09/B10. Both are punt costumes. Fixed as follows:
- **B01, B03, B08, B11** — CARD beats: added `shot.remotion.pattern=FormACard` with real lines drawn from `card.copy`/`card.sub`. Now render as real Remotion mp4s, not slates.
- **B02** — was `STILL src=ai` for a six-function nanoparticle schematic (a Manim structure diagram per nopunt catalog). No manim scene exists on disk. Converted to `FormACard` naming the six components explicitly. Logged as scripting gap (real schematic would upgrade this beat).
- **B04–B07, B09, B10** — were `GRAPHIC` with named Manim scenes that do not exist on disk. Compile lane-check refused them as PIPELINE-SLATE-IN-CUT. Converted to `FormACard` text summaries of what the chart should show (the narration's numbers written explicitly: 90/81/73/66/59/53; 0.9⁶=53%; Program A vs B counts). This is an honest text substitute — every one of these beats logged as needing a Manim upgrade in a future body-beat pass.
- **B12, B13** — OutroSeries/OutroCTA props were wrong schema (`seriesTitle/tagline/githubSlug`, `authorName/handle/ctaText`) — the Remotion components would silently fall back to Claude defaults, Claude-washing a Medhavy reel. Fixed to correct schema (`{eyebrow, line}` / `{line, handle}`) with Medhavy content ("CANCER NANOMEDICINE" / "@MedhavyAI").

Zero remaining `YOU → gen-AI clip`, zero `DoodleScene`, zero `STILL src=archive/ai` on animatable content, zero unfilled `remotion_scenes` slates in the final build.

### 7. Card-only reel — LOGGED
Every body beat now renders as `FormACard` (text). This IS a card-only reel in the current pass — a consequence of no Manim scene library existing for these six visualization beats. Scripting gap logged: the reel wants at least three drawn figures (the yield-collapse bar chart B05, the 0.9⁶ math card B06, the Program A/B batch grid B09). Would upgrade to a mixed-media reel with a proper scenes_std.py pass.

### 8. Lens audit — PASS (2+ moves present)

- **Hume (confidence is a property of the model):** B09 explicitly labels the batch counts "illustrative" ("Program A · 1 function · 11 of 12 pass / Program B · 6 functions · 7 of 12 pass / illustrative — same per-function quality"). The 0.9⁶ = 53% math is a modeled prediction, not an empirical measurement. ✓
- **Popper (state in advance what would count as failure):** B04 names the falsification criterion in advance ("Six gates. Every one must open."). The reel then plays out that criterion in B05 (yield collapses to 53%) and confirms the design fails the criterion. ✓
- **Descartes (checklist):** the six-function decomposition (B02) is a Cartesian checklist made structural — each function is independently characterizable, each independently fails, and the multiplication is the whole. Implicit but present. ✓
- **Plato (artifact vs world):** B10 distinguishes the artifact (the elegant six-function design in the paper) from the world (batches on the manufacturing floor). Partial.

### 9. Brand fields — FIXED
- `voice_id: "1sgY6Voq1aexKOB1IJ2D"` (ElevenLabs) → DROPPED ✓
- `clock` (ElevenLabs prose) → DROPPED ✓
- `folderLabel: "@MedhavyAI"` ✓ (added)
- `engine: kokoro`, `voice_kokoro: af_kore` ✓ (medhavy voice)
- B12/B13 Medhavy channel branding restored (was silently Claude-defaulting)
- Persona: narration is third-person ("A research team builds…"). No Bear/Liam/persona claim — no voice-swap risk. `af_kore` is a female Kokoro voice; consistent with medhavy channel default.

### 10. Pacing — LOG
Using measured audio durations (kokoro af_kore) vs word counts:

| Beat | ~Words | actual_duration_s | ~wps | Note |
|------|--------|-------------------|------|------|
| B01  | 32     | 12.76             | 2.51 | ✓    |
| B02  | 51     | 16.92             | 3.01 | ✓    |
| B03  | 39     | 13.97             | 2.79 | ✓    |
| B04  | 43     | 15.02             | 2.86 | ✓    |
| B05  | 55     | 17.64             | 3.12 | ✓    |
| B06  | 55     | 17.13             | 3.21 | ✓    |
| B07  | 55     | 18.37             | 2.99 | ✓    |
| B08  | 42     | 17.02             | 2.47 | ✓    |
| B09  | 57     | 18.75             | 3.04 | ✓    |
| B10  | 48     | 16.38             | 2.93 | ✓    |
| B11  | 47     | 18.47             | 2.54 | ✓    |
| B12  | 11     |  4.29             | 2.56 | ✓    |
| B13  |  7     |  2.45             | 2.86 | ✓    |

All beats within 2.0–3.4 wps. No pacing flags.

### 11. type_check.py — GATE T: PASS
Ran on final sheet. Four §8.10 ADVISORIES (B02/B03 = 1.00, B04 = 0.89, B10 = 0.91 — narration recites the card). Structural, expected: these beats' FormACard text is a compressed transcript of the narration by construction (the numbers/lists in the narration ARE the visual since the manim charts do not exist). Logged, not a FAIL. Zero validators loosened.

## Phase 2 — Build

- **Audio:** Kokoro af_kore, 13/13 mp3 files generated fresh, durations measured back into sheet (drops the pre-existing ElevenLabs-era mp3s from Jul 16).
- **Remotion:** all 13 pattern beats rendered → `media/B*.mp4` (FormACard × 11 + OutroSeries + OutroCTA).
- **Compile:** `compile.py . --review` — content-check PASS, frame-check PASS, lane-check PASS (13/13 filled, known_slates=[]).
- **Output:** `vox-complexity-yield-slate.mp4` — 190.2 s, 1280×720 review cut with per-beat labels and timecodes.
- **Gate audio:** `mean_volume -23.9 dB` (threshold: > −40 dB) ✓
- **Gate V — frame read (7 sampled frames across timeline):**
  - B01 (0s) — title, cream ground, EB Garamond serif, legible, well within safe area ✓
  - B03 (30s) — question card, legible ✓
  - B05 (60s) — yield collapse numbers, all six percentages readable ✓
  - B07 (95s) — Doxil vs six-function contrast, legible ✓
  - B11 (165s) — endcard, legible ✓
  - B13 (187s) — Medhavy OutroCTA — "Explore the full course at medhavy.com" + SUBSCRIBE pill + @MedhavyAI handle. Note: OutroCTA renders on WHITE not cream (component default); consistent across siblings. ✓
  - Zero BLOCKER, zero MAJOR on any real beat.
- **Post-build punt sweep:** `build.status` Counter: `{'VIDEO': 13}`. Zero slates. Zero pipeline-owned SLATE, zero gen-AI-in-master.
- **Stale check:** mp4 mtime `1787867002` vs sheet mtime `1787866996` — mp4 is 6 s NEWER ✓

## Output

`vox-complexity-yield-slate.mp4` — 190.2 s, audio present (−23.9 dB), mp4 newer than beat_sheet.json (Δ+6s). DONE (as a text-heavy card-only review slate cut; six drawn-graphic beats are honest text substitutes pending a scenes_std.py pass).
