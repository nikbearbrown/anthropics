# AUDIT — claude-liam-vox-emitter-range
_Pass: 2026-08-27_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` created (byte-exact copy before first edit) ✓
- Dead ElevenLabs fields dropped: `voice_id`, `clock` — see REBUILD-LOG.md
- VOICE-LOCK fields retained: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓

---

## Phase 1 Audit

### Check 1 — Stale renders
**PASS.** No mp4 files existed in the reel directory at audit start (only `master.m4a` from Jul 16 in `clips/`). Nothing to delete.

### Check 2 — Bookends
**FIXED (B13, B14).**

Four canonical bookends present and correctly typed:
- B00: `ClaudeComposerAsk` ✓
- BVDT: `ClaudeVerdictArtifact` ✓ (content fixed in Check 4)
- BHTF: `ClaudeComposerAsk` ✓
- BOUT: `ClaudeTitleOutro` ✓

B13 `OutroSeries` and B14 `OutroCTA` were non-claude skins in a claude-palette reel (build.skin_warnings already flagged B14). Both changed to `FormACard` with narration preserved. Their falsely-stamped `build.status: "VIDEO"` (no actual media/ directory existed) corrected to `SLATE`.

### Check 3 — Spark lines
**FIXED (B00).**

- B00 greeting: `"Liam"` → `"Ciao, Liam"` (Italian hello). Adjacent reels in this series all had bare "Liam" — fixed first; "Ciao" chosen as non-repeating world-language hello.
- BHTF greeting: `"Your turn."` ✓ (already correct)
- No inner ClaudeComposerAsk body beats in this reel.

### Check 4 — Verdict
**FIXED (BVDT authored).**

Previous `artifactLines` were placeholders: `["Key finding one", "Key finding two", "Key finding three"]`. Previous `narration_text` was empty. Body has 12 beats, 180+ words — authored a real verdict.

New `artifactLines` (4 lines, drawn from B02/B05/B06/B09/B11):
1. "Alpha's 50–100 μm range is lethal per hit but confined to the bound cell."
2. "Beta's 1–2 mm crossfire reaches receptor-negative neighbors, crossing gaps the drug cannot."
3. "Heterogeneous 3 cm neuroendocrine tumor: Lu-177 (beta) ~78% vs Ac-225 (alpha) ~41% cell kill — illustrative."
4. "Geometry of target expression, not lethal force per hit, is the deciding variable."

New `narration_text`: "Alpha hits harder per cell. Beta's crossfire reaches farther. On a heterogeneous tumor — receptor-positive rim, receptor-negative core — Lu-177's one-to-two millimeter range crosses the gap that alpha's fifty micrometers cannot. The geometry of the tumor, read off a patient's scan, is what decides the emitter — not which particle shreds DNA more efficiently per hit."

Also fixed: `artifactTitle` and `BOUT.title` truncated at ~60 chars by type_check. Shortened both to `"Emitter Range, Not Lethal Force"` (31 chars).

### Check 5 — Card text
**FIXED (B01).**

B01 `FormBCard` had placeholder items: `["Key point one" / empty sub, "Key point two" / empty sub, "Key point three" / empty sub]`. Pattern changed to `FormACard` (matching locked `card.kind: "title"` intent). Lane field `"BOOKEND"` removed (B01 is a body beat).

B04 card text: `copy` and `sub` are authored real content ✓ ("Alpha delivers far more lethal energy per hit than beta…"). 
B10 card text: real content ✓.
B12 card text: real content ✓.

### Check 5b — Chart text
**PASS.** No Manim charts with axis labels. All Manim beats are particle-track diagrams or cross-sections with short categorical labels (MONO font, 1–2 words). No bar charts. No label truncation issues found in QC frames.

### Check 6 — Punt sweep
**FIXED (B04, B07, B10, B12).**

- B04: `build.needs: "YOU → 5–10s gen-AI clip → pantry"` removed. `shot.type: "CARD"` is legitimate for a question card.
- B07: `shot.type: "STILL"`, `source: "ai"` — PUNT. A heterogeneous tumor cross-section (receptor-positive rim / receptor-negative core) is fully animatable as a Manim structure/boundary diagram. Changed to `shot.type: "GRAPHIC"`, `manim: "B07_TumorGeometry"`. Scene authored and rendered.
- B10: `build.needs: "YOU → gen-AI clip"` removed. CARD is legitimate.
- B12: `build.needs: "YOU → gen-AI clip"` removed. CARD (endcard) is legitimate.

No remaining `YOU → gen-AI clip`, no `DoodleScene`, no `STILL src=archive/ai` on animatable content, no unfilled `fill_slates` or `remotion_scenes` slates.

### Check 7 — Card-only reel
**PASS.** Beats B02, B03, B05, B06, B07, B08, B09, B11 are all GRAPHIC/Manim. Not a card-only reel.

### Check 8 — Lens audit
**PASS (2+ moves present).**

- **Hume**: B11 explicitly labels numbers "illustrative" in the production_viz note, and `beat.narration_text` says "roughly seventy-eight percent" and "about forty-one percent" — confidence hedged as model-of-a-scenario, not empirical measurement. ✓
- **Plato**: The reel continuously distinguishes artifact (emitter choice/range number) from world (tumor's 3D geometry). B10 states the relationship explicitly: "Geometry is the deciding variable." B07–B09 show the spatial mismatch directly. ✓
- **Descartes**: B04 poses the falsifying question ("Why would less lethal radiation be better?") and B10 answers with the falsifying criterion (when range matches, the "weaker" wins). Implicit but present. ✓
- **Popper**: B10 names the deciding test criterion in advance ("which range matches the spatial distribution"). Partially present.

Note: No explicit "alpha wins when..." falsifiability beat — the edge case (homogeneous tumors favoring alpha) is not a dedicated beat. Logged as a scripting gap; narration is locked and cannot be augmented. Not a BLOCK.

### Check 9 — Brand fields
**FIXED.**

- `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs) → DROPPED ✓
- `clock` (ElevenLabs-era prose) → DROPPED ✓
- `folderLabel: "@NikBearBrown"` ✓
- `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓
- B13/B14 palette mismatch → FIXED (Check 2)
- Persona: narration says "This is Liam, in for Bear." → voice is `am_onyx` ✓. No Bear/Liam voice-swap.

### Check 10 — Pacing (LOG — do not fix)
**ADVISORY.** Three body beats exceed the 2.0–3.4 wps range based on measured audio:

| Beat | ~Words | actual_duration_s | ~wps |
|------|--------|-------------------|------|
| B04  | 34     | 9.64              | 3.5  |
| B05  | 38     | 11.01             | 3.5  |
| B06  | 43     | 11.95             | 3.6  |

B11 at 2.0 wps (borderline slow). These are logged; narration is locked (rebuild contract).

### Check 11 — type_check.py
**PASS.** After fixing artifactTitle/BOUT.title truncation:
```
GATE T: PASS
```
Initial run failed on two truncation warnings; fixed by shortening display titles to "Emitter Range, Not Lethal Force" (31 chars). Rerun clean.

---

## Phase 2 — Build

**Audio:** BVDT narration generated (Kokoro am_onyx, 20.27s). Beats B01–B14 had existing mp3 files from Jul 16 (predating this pass; audio correct and matches narration).

**Remotion renders:** All 7 bookend/card beats rendered via `remotion_scenes.py`:
B00, B01, B13, B14, BVDT, BHTF, BOUT → `media/*.mp4`

**Manim renders:** 8 GRAPHIC beats rendered via `scenes_std.py` (newsprint palette, self-contained):
B02, B03, B05, B06, B07 (new scene), B08, B09, B11 → `manim/*.mp4`

**Compile:** `compile.py --review`
```
GATE AUDIO: PASS  mean_volume -27.8 dB
slots: 15/18 filled
B04/B10/B12 are legitimate SLATE card beats (CARD type, not pipeline-owned)
```

**Gate V — QC frame review:**

| Beat | Status | Finding |
|------|--------|---------|
| B00  | PASS   | ClaudeComposerAsk, cream ground, "Ciao, Liam" greeting, legible ✓ |
| B01  | PASS   | FormACard title card, centered, no overflow ✓ |
| B02  | PASS   | Alpha particle track (CRIMSON), SLATE cell, cream ground, good negative space ✓ |
| B03  | PASS   | Beta particle track (TEAL), neighbor cells, cream ground ✓ |
| B04  | EXEMPT | Declared SLATE card — exempt from Gate V ✓ |
| B05  | PASS   | Split panel (Alpha/Beta), GOLD highlight bar, CRIMSON left / TEAL right, divider line, legible ✓ |
| B06  | PASS   | Crossfire mechanism, TEAL tracks and glow, cream ground ✓ |
| B07  | PASS   | New tumor cross-section: teal ring + gray core, arrows, diameter annotation ✓ |
| B08  | PASS   | Alpha fails: SLATE tumor ring, CRIMSON radial tracks, LabelChip, "core survives" CRIMSON text ✓ |
| B09  | FIXED  | "core irradiated" text was TEAL on TEAL glow (MAJOR — low contrast). Fixed to WHITE. Re-rendered. ✓ |
| B10  | EXEMPT | Declared SLATE card — exempt ✓ |
| B11  | PASS   | Lu-177/Ac-225 side-by-side panels, "78%" TEAL / "41%" CRIMSON, "illustrative numbers" header ✓ |
| B12  | EXEMPT | Declared SLATE card — exempt ✓ |
| B13  | PASS   | FormACard "Part of the Cancer Nanomedicine series." ✓ |
| B14  | PASS   | FormACard "Like and subscribe for more." ✓ |
| BVDT | PASS   | ClaudeVerdictArtifact, "Emitter Range, Not Lethal Force", 4 real verdict lines visible ✓ |
| BHTF | PASS   | ClaudeComposerAsk, "Your turn.", scaffolded rubric visible ✓ |
| BOUT | PASS   | ClaudeTitleOutro ✓ |

Zero BLOCKER on real beats. One MAJOR fixed (B09 contrast) before final compile.

**Audio presence:** `aac`, 48000 Hz stereo, mean_volume -27.8 dB (threshold: >-40 dB) ✓

**Drawon motion advisory:** 8/18 beats (44%) carry `drawon` — over the ~40% cap. Logged; fix in a future body-beat pass when Manim scenes are authored with explicit hold sequences. Not a build-fail.

**Post-build punt sweep:**

`build.status` Counter: `{'VIDEO': 7, 'MANIM': 8, 'SLATE': 3}`

Slates: B04 (question card, CARD type), B10 (section card, CARD type), B12 (endcard, CARD type) — all legitimate CARD beats, not pipeline punts.

No gen-AI slates, no unfilled remotion_scenes, no DoodleScene, no STILL src=archive in body. ✓

---

## Output

`vox-emitter-range-slate.mp4` — 209.1s, audio present (-27.8 dB), mp4 newer than beat_sheet.json (Δ+9s). DONE.
