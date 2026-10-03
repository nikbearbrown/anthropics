# AUDIT — claude-liam-psma-theranostic-loop
_Pass: 2026-08-28 (filmloop unattended)_

## Phase 0 — Rebuild Contract
- `beat_sheet.pre-rebuild.json` created byte-exact before first edit ✓
- Dead ElevenLabs field dropped: `voice_id` — see REBUILD-LOG.md
- VOICE-LOCK: `engine=kokoro`, `voice_kokoro=am_onyx` ✓
- `metadata.voice` normalized `nbbhuman` → `am_onyx`

## Phase 1 Audit

### Check 1 — Stale renders
**PASS.** No mp4 files existed in the reel directory at audit start (only `clips/master.m4a` from Jul 16, predating sheet). Nothing to delete.

### Check 2 — Bookends
**FIXED (B00).** Four canonical bookends now present and correctly typed:
- B00: `ClaudeComposerAsk` ✓ (was `NikBearBrownOpen` — build.skin_warnings flagged this)
- BVDT: `ClaudeVerdictArtifact` ✓ (verdict authored in Check 4)
- BHTF: `ClaudeComposerAsk` ✓
- BOUT: `ClaudeTitleOutro` ✓

### Check 3 — Spark lines
**FIXED (B00, B02, B05).**
- B00 greeting: none → `"Zdravo, Liam."` (Serbo-Croatian hello). Alphabetical adjacents are protein-corona (empty) and vox-abraxane-solvent ("Aloha") — no collision.
- B02 greeting: `"The ask,"` → `"Research the pair."` (3 words, drawn from beat narration)
- B05 greeting: `"The ask,"` → `"Compare the pairs."` (3 words, drawn from beat narration)
- BHTF greeting: `"Your turn."` ✓ (already correct)

### Check 4 — Verdict
**FIXED (BVDT authored).** Previous `artifactLines` were the shipped placeholder `["Key finding one", "Key finding two", "Key finding three"]`; previous `narration_text` was empty. Body has 10 beats, ~400+ words — qualifies to author.

New `artifactLines` (4 lines, drawn from B01/B04/B06/B08):
1. "PSMA-617: Ga-68 for imaging, Lu-177 for therapy — one scaffold, two isotopes."
2. "VISION trial (NEJM 2021): Lu-177-PSMA-617 improved OS by ~4 months in mCRPC."
3. "DOTATATE mirrors it in neuroendocrine tumors — two validated pairs, one rule."
4. "The loop works when a quantifiable membrane target shares its scaffold with an imaging isotope."

New `narration_text`: "Two isotopes, one scaffold. Gallium sixty-eight images the tumor; lutetium one seventy-seven treats it. The VISION trial added four months of overall survival in metastatic castration-resistant prostate cancer. DOTATATE mirrors the pattern in neuroendocrine tumors — two validated pairs, one rule: image to confirm the target, treat only what you can see, then image the response."

Also fixed: `artifactTitle` and `BOUT.title` and `B09.title` shortened from the 76-char reel title (typecheck golden-strings LONGEST overflow risk) to `"PSMA Theranostics: Image, Then Treat"` (36 chars).

### Check 5 — Card text
**FIXED (B01).** B01 `FormBCard` had placeholder items `["Key point one/two/three"]` with empty subs. Authored real items from locked narration_text:
- Ga-68-PSMA-617 / "Images every PSMA-positive metastasis."
- Lu-177-PSMA-617 (Pluvicto) / "Delivers targeted beta radiation to the same cells."
- VISION trial (NEJM 2021) / "OS 15.3 vs 11.3 mo in mCRPC."

`lane: "BOOKEND"` removed (B01 is a body beat, not a bookend). `visual_intent` stub cleared.

### Check 5b — Chart text
**N/A.** No Manim/D3 chart beats. All GRAPHIC beats are Remotion FormBCard / composer / code skins. No axis labels or bar charts.

### Check 6 — Punt sweep
**FIXED (B04, B06, B07, B08).**
- B04: SLATE Manim scene `B04_TheranosticLoop` in phantom `vox_scenes.py` (no per-reel scenes_std.py, no rendered mp4) → converted to `FormBCard` with 4 items: IMAGE / TREAT / ASSESS / REPEAT-or-ESCALATE. Matches pattern of accepted sibling reels `her2-low-bystander` and `nanomedicine-translation-gap`.
- B06: `YOU → 5–10s gen-AI clip → pantry` costume → `FormBCard` with 3 items: Ga-68-DOTATATE / Lu-177-DOTATATE (Lutathera) / NETTER-1 trial.
- B07: `YOU → gen-AI clip` → `FormBCard` with 3 items: CONFIRM TARGET / TREAT ONLY THE CONFIRMED / CONFIRM RESPONSE.
- B08: `YOU → gen-AI clip` → `FormBCard` with 3 items: Membrane-facing target / Low in normal tissue / Imaging isotope on same scaffold.

No remaining `YOU → gen-AI clip`, no `DoodleScene`, no `STILL src=archive/ai` on animatable content, no unfilled `fill_slates` or `remotion_scenes` slates.

### Check 7 — Card-only reel
**PASS.** B02 (real research prompt in NikBearBrownTerminalAsk), B03 (real Python code in NikBearBrownCodeBlock), B05 (real research prompt). Not a card-only reel.

### Check 8 — Lens audit
**PASS (2+ moves earned).**
- **Descartes / falsifying question**: B08 poses the falsifying checklist ("does the tumor have a membrane-facing overexpressed target with low dose-limiting normal tissue AND an imaging isotope on the same scaffold?" — three conditions any of which would falsify candidacy).
- **Plato / artifact–world**: The whole reel distinguishes the imaging *artifact* (the PET scan showing PSMA uptake) from the *world* (the tumor cells actually expressing PSMA). B04 makes it explicit: image → treat only what the image confirms → image again to confirm the response is real, not just prescribed.
- **Popper / validated failure test**: The VISION trial is named as the pre-specified failure test — "OS 15.3 vs 11.3 mo" is the specific quantitative outcome that either confirmed or refuted the loop's clinical value.

### Check 9 — Brand fields
**FIXED.**
- `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs) → DROPPED
- `voice: "nbbhuman"` → `"am_onyx"`
- `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓
- `folderLabel: "@NikBearBrown"` ✓ on all Claude bookends
- Persona: narration says "This is Liam, in for Bear" (B00) — voice is Kokoro `am_onyx` (Liam). Coherent.

### Check 10 — Pacing (LOG — do not fix)
Beat / words / actual_s / wps:
| Beat | words | actual_s | wps |
|------|-------|----------|-----|
| B00 | 16 | 4.99 | 3.2 |
| B01 | 66 | 22.76 | 2.9 |
| B02 | 30 | 9.60 | 3.1 |
| B03 | 43 | 13.46 | 3.2 |
| B04 | 82 | 27.69 | 3.0 |
| B05 | 39 | 12.69 | 3.1 |
| B06 | 74 | 22.91 | 3.2 |
| B07 | 52 | 17.88 | 2.9 |
| B08 | 61 | 17.73 | 3.4 |
| B09 | 18 | 6.51 | 2.8 |
| BVDT | 71 | 21.10 | 3.4 |

All beats within 2.0–3.4 wps. No outliers.

### Check 11 — type_check.py
**PASS.** GATE T: PASS. Zero FAILs across 13 beats. One advisory (§8.10 B06 redundancy 0.87 — advisory only). B09 golden-strings LONGEST overflow risk fixed by shortening title.

---

## Phase 2 — Build

**Audio.** `generate_audio_kokoro.py --only BVDT` — BVDT narration generated (21.10s, am_onyx). Existing per-beat mp3s for B00–B09 (Jul 16, matched locked narration) reused.

**Renders.** `remotion_scenes.py` rendered all 13 beats (`media/*.mp4`).

**Compile.** `compile.py` (no `--review` since all 13 beats are real content, per naming rule).
```
slots: 13/13 filled — every beat VIDEO
GATE AUDIO: PASS  mean_volume -24.6 dB
motion histogram: fade:5  remotion:4  hold:4
```

**Gate V — QC frame review** (midpoint of every beat + contact sheet at `qc-sheet.png`):

| Beat | Status | Finding |
|------|--------|---------|
| B00 | PASS | ClaudeComposerAsk, "Zdravo, Liam." greeting, cream ground, folder chip visible ✓ |
| B01 | PASS | 3-card FormB, real Ga-68/Lu-177/VISION labels & subs, no clipping ✓ |
| B02 | PASS | NikBearBrown terminal, real research prompt readable at 1080p ✓ |
| B03 | PASS | NikBearBrown code block, syntax highlighted Python, no overflow ✓ |
| B04 | PASS | 4-card FormB loop (IMAGE/TREAT/ASSESS/REPEAT-or-ESCALATE), balanced grid ✓ |
| B05 | PASS | NikBearBrown terminal, DOTATATE comparison prompt legible ✓ |
| B06 | PASS | 3-card FormB, DOTATATE-mirrors-PSMA content, no clipping ✓ |
| B07 | PASS | 3-card FormB, theranostic-rule (confirm/treat/confirm) ✓ |
| B08 | PASS | 3-card FormB, candidate criteria, all 3 subs fit their cards ✓ |
| B09 | PASS | NikBearBrown outro, brand/tagline/handle/url ✓ |
| BVDT | PASS | ClaudeVerdictArtifact, "PSMA Theranostics: Image, Then Treat" title, 4 real verdict lines (paginated 1/2 → 2/2) ✓ |
| BHTF | PASS | "Your turn." composer, scaffolded prompt visible ✓ |
| BOUT | PASS | ClaudeTitleOutro, mascot + short title ✓ |

Zero BLOCKER, zero MAJOR. Zero downgrades from strict mode.

**Audio presence.** aac 48000 Hz mono, `mean_volume -24.6 dB` (threshold: > −40 dB) ✓

**Post-build punt sweep.**

`build.status` Counter: `{'VIDEO': 13}`

No slates, no gen-AI clip needs, no `DoodleScene`, no `STILL src=archive/ai`. ✓

---

## Output

`psma-theranostic-loop.mp4` — 206.3s, audio present (-24.6 dB), mp4 mtime 29 s newer than beat_sheet.json (14:48:53 vs 14:48:24). DONE.
