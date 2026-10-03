# AUDIT — claude-liam-vox-dar-optimum
_Pass: 2026-08-28_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` created (byte-exact copy before first edit) ✓
- Dead ElevenLabs fields dropped: `voice_id`, `clock` — see REBUILD-LOG.md
- Stale `metadata.build` stamp from 2026-07-16 dropped (will be re-stamped on this pass)
- VOICE-LOCK fields retained: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓

---

## Phase 1 Audit

### Check 1 — Stale renders
**PASS.** Zero `.mp4` files existed in this reel's directory before this pass (only `mp3/*.mp3` audio and `clips/master.m4a`, all Jul 16). Nothing older-than-sheet to delete.

### Check 2 — Bookends
**FIXED (B13, B14).**

Four canonical bookends present and correctly typed:
- B00: `ClaudeComposerAsk` ✓
- BVDT: `ClaudeVerdictArtifact` ✓ (content authored in Check 4)
- BHTF: `ClaudeComposerAsk` ✓
- BOUT: `ClaudeTitleOutro` ✓ (title shortened from 60 → 30 chars)

B13 was `OutroSeries` and B14 was `OutroCTA` — non-claude channel skins in a claude-palette reel (prior `build.skin_warnings` flagged B14). Both changed to `FormACard` with narration preserved. Their falsely-stamped `build.status: "VIDEO"` (no media/ directory existed) corrected to `SLATE`.

### Check 3 — Spark lines
**FIXED (B00).**

- B00 greeting: `"Liam"` → `"Szia, Liam"` (Hungarian). All 15+ adjacent Cancer Nanomedicine reels checked — Ciao, Aloha, Sawubona, Guten tag, Kia ora, Hola, Salaam, Konnichiwa, Bonjour, Hej, Ni hao, Merhaba, Zdravo, Jambo, Namaste were taken. Szia is unique.
- BHTF greeting: `"Your turn."` ✓ (already correct)
- No inner ClaudeComposerAsk body beats in this reel.

### Check 4 — Verdict
**FIXED (BVDT authored).**

Prior `artifactLines` were placeholders: `["Key finding one", "Key finding two", "Key finding three"]`. Prior `narration_text` was empty. Body has 12 beats and 300+ words — authored a real verdict.

New `artifactTitle`: `"DAR: An Optimum, Not a Maximum"` (was: full title — would truncate).
New `artifactHeading`: `"The DAR trade-off, in one page"` (was: `"Key findings"` — flagged as placeholder heading by verdict_audit.py).

New `artifactLines` (4 lines, drawn from B04/B06/B07/B09/B10/B11/B12):
1. "Cytotoxic payloads are hydrophobic — past DAR ~4–8 the conjugate aggregates."
2. "Liver and immune system clear aggregated ADCs in hours, not days."
3. "Illustrative DAR-4 vs DAR-8: 68% vs 11% plasma at 24h; 2.4 vs 0.3 μg/g tumor at 72h."
4. "DAR is an optimum, not a maximum: more warheads means less delivery past the sweet spot."

New `narration_text`: "Cytotoxic drug molecules are hydrophobic. Past four to eight warheads per antibody the conjugate aggregates, and the liver and immune system clear those aggregates in hours. In an illustrative comparison, DAR-four keeps sixty-eight percent of its plasma level at twenty-four hours and delivers two-point-four micrograms per gram of tumor at seventy-two hours. DAR-eight: eleven percent, then zero-point-three. The higher-payload molecule delivered less drug where it needed to go. DAR is an optimum, not a maximum."

verdict_audit.py: PASS on this reel after fix.

### Check 5 — Card text
**FIXED (B01).**

B01 `FormBCard` had placeholder items: `[{label:"Key point one",sub:""},{label:"Key point two",sub:""},{label:"Key point three",sub:""}]` — three PLACEHOLDER-pattern strings + empty subs. Pattern changed to `FormACard` (matching the locked `card.kind: "title"` intent). `lane: "BOOKEND"` removed (B01 is a body beat, not a bookend).

B03 (question), B08 (section), B12 (endcard) `card` blocks carry real authored copy from the locked narration ✓.

### Check 5b — Chart text
**PASS.**
- B09_OptimumCurve: NumberLine 0–10 + short axis label "DAR" + "tumor drug delivery"; no truncation.
- B10_ExamplePharma: category labels "DAR-4"/"DAR-8" and "68%"/"11%" — short MONO categorical labels ✓.
- B04_DARScale: NumberLine 0–10 + short bracket label ("clinical ADCs (DAR 4–8)") + "under-kill"/"over-aggregate" ✓.
- No narration fragments used as labels. Bar heights match narration semantics (DAR-4 taller, teal, "sixty-eight percent"; DAR-8 shorter, crimson, "eleven percent"). ✓

### Check 6 — Punt sweep
**FIXED (B03, B05, B08, B11, B12).**

Old sheet had six punts:
- B03: `build.needs: "YOU → 5–10s gen-AI clip → pantry"` — CARD is legitimate; needs field removed.
- B05: `shot.type: "STILL"`, `source: "ai"`, `image_prompt: "..."` — PUNT. "Cell survives because payload below threshold" is a threshold/gauge concept and is fully animatable per the nopunt catalog (Data & quantity → threshold / bracket). Converted to GRAPHIC with new Manim scene `B05_UnderKill`.
- B08: gen-AI-clip punt tag removed. CARD legitimate.
- B11: `shot.type: "DOCUMENT"` with gen-AI-clip punt tag. Converted to GRAPHIC with new Manim scene `B11_TumorQuote` (a proper quote card with gold highlight — nopunt catalog: highlight/quote → drawn on cue). Quote content and highlight semantics preserved verbatim.
- B12: gen-AI-clip punt tag removed. CARD (endcard) legitimate.

Zero remaining `YOU → gen-AI clip`, zero `DoodleScene`/`DoodleChart`, zero `STILL src=archive/ai` on animatable content, zero unfilled `fill_slates`/`remotion_scenes` slates, zero FormA/B whose narration names a visual it never draws. Every punt now maps to a drawn Manim/Remotion beat or a legitimate CARD.

### Check 7 — Card-only reel
**PASS.** Beats B02, B04, B05, B06, B07, B09, B10, B11 are all GRAPHIC/Manim — eight body beats draw real figures. Not a card-only reel.

### Check 8 — Lens audit
**PASS (2+ moves present).**

- **Descartes (radical doubt / falsification checklist)**: B03 poses the falsifying question directly — "Why does loading more warheads make it clear faster — and kill less?" — as the diagnostic that opens the mechanism reveal. B05 introduces the LEFT-edge failure (under-kill); B06–B08 introduce the RIGHT-edge failure (over-aggregation → clearance → toxicity). The reel produces a checklist of what would have to be true for "more warheads = more killing" to fail. ✓
- **Popper (falsifiability, state failure in advance)**: B10 & B11 name the deciding test in advance and quantify a discriminating outcome — DAR-4 vs DAR-8 at 24h plasma, then at 72h tumor concentration. The claim "DAR-8 kills better" is stated as measurably falsifiable: if plasma clearance is faster and tumor concentration is lower for DAR-8, the claim fails. It does. ✓
- **Hume (confidence is a property of the model)**: B10, B11, and B12 all explicitly label the numbers "illustrative" — in narration ("These are illustrative numbers, but the pattern is real"), in the `metadata.note` disclaimer, and in the on-screen chip in B10/B11 ("illustrative"). The reel refuses to let a concrete number get treated as an empirical measurement. ✓
- **Plato (artifact ≠ world)**: B01 vs B12 makes the move explicit — the artifact is "DAR = 8" on a spec sheet; the world is what reaches the tumor. B10/B11 read the two apart (specified payload per molecule vs delivered drug per gram of tissue). ✓

All four moves present; two-move minimum comfortably exceeded.

### Check 9 — Brand fields
**FIXED.**

- `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs) → DROPPED ✓
- `clock` (ElevenLabs-era prose) → DROPPED ✓
- `folderLabel: "@NikBearBrown"` ✓ (already correct)
- `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓
- Palette=claude with correct claude bookends: B00 ClaudeComposerAsk, BVDT ClaudeVerdictArtifact, BHTF ClaudeComposerAsk, BOUT ClaudeTitleOutro ✓
- B13/B14 palette mismatch → FIXED (Check 2)
- Persona: B01 narration says "This is Liam, in for Bear." → voice is `am_onyx` (Liam's Kokoro voice) ✓

### Check 10 — Pacing (LOG — do not fix)
**ADVISORY.** Body-beat words-per-second (words in narration_text / measured actual_duration_s):

| Beat | ~Words | actual_duration_s | ~wps |
|------|--------|-------------------|------|
| B01  | 33     | 10.90             | 3.0  |
| B02  | 45     | 13.99             | 3.2  |
| B03  | 25     | 8.73              | 2.9  |
| B04  | 43     | 13.91             | 3.1  |
| B05  | 41     | 12.76             | 3.2  |
| B06  | 42     | 13.40             | 3.1  |
| B07  | 38     | 11.52             | 3.3  |
| B08  | 42     | 13.53             | 3.1  |
| B09  | 42     | 14.76             | 2.8  |
| B10  | 46     | 16.30             | 2.8  |
| B11  | 54     | 18.28             | 3.0  |
| B12  | 32     | 9.96              | 3.2  |

All body beats fall inside the 2.0–3.4 wps window ✓. No pacing outliers.

### Check 11 — type_check.py
**PASS.**
```
[typecheck] GATE T: PASS
```
Ran clean on first pass — no §8.7 placeholders (removed via FormBCard→FormACard fix), no §8.5 wordy cards, no §8.9 truncation on the shortened `artifactTitle` / `BOUT.title`.

---

## Phase 2 — Build

**Audio:** BVDT authored narration rendered fresh (Kokoro `am_onyx`, 28.44s). Beats B01–B14 already had mp3s from the Jul 16 pass — locked narration matches, no regeneration needed.

**Remotion renders (7 beats):** `remotion_scenes.py` → all 7 bookend/outro Remotion beats. All succeeded on first pass:
`B00` ClaudeComposerAsk · `B01` FormACard · `B13` FormACard · `B14` FormACard · `BVDT` ClaudeVerdictArtifact · `BHTF` ClaudeComposerAsk · `BOUT` ClaudeTitleOutro

**Manim renders (8 beats):** `scenes_std.py` (newsprint palette, self-contained). B04 initially failed with a `DecimalNumber(font_size=...)` kwarg conflict — moved `font_size` to `NumberLine` top-level and re-rendered. Final set:
`B02_LoadingLogic` · `B04_DARScale` · `B05_UnderKill` · `B06_HydrophobicLoad` · `B07_ClearanceTrap` · `B09_OptimumCurve` · `B10_ExamplePharma` · `B11_TumorQuote`

**Compile:** `compile.py --review`
```
[content-check] PASS — 18 beats checked, no violations.
[frame-check]   PASS — 18 beats checked, no violations.
[lane-check]    PASS — 18 beats checked, no lane violations.
GATE AUDIO:     PASS  mean_volume -27.6 dB
slots: 15/18 filled — B03/B08/B12 legitimate CARD slates (exempt)
```

**Gate V — QC frame review:**

| Beat | Status | Finding |
|------|--------|---------|
| B00  | PASS   | ClaudeComposerAsk cream ground, "Szia, Liam" greeting, folder handle, running text ✓ |
| B01  | PASS   | FormACard title card, sub, no overflow ✓ |
| B02  | PASS   | Y-antibody + 8 TEAL warheads counter, DAR 4 / DAR 8 markers, aphorism ✓ |
| B03  | EXEMPT | Declared SLATE card ✓ |
| B04  | FIXED  | Bracket label "clinical ADCs (DAR 4–8)" collided with "under-kill"/"over-aggregate" labels. Moved bracket_lbl to UP*2.0, shortened arrows, re-rendered. ✓ |
| B05  | PASS   | Cell + gauge; GOLD threshold; TEAL delivered fill below threshold; CRIMSON "gap" arrow; "cell survives" chip ✓ |
| B06  | PASS   | Three antibodies overloaded with CRIMSON payload dots, sticky/hydrophobic label, aggregation ring ✓ |
| B07  | PASS   | Bloodstream channel; TEAL DAR-4 mid-flow past cleared box; CRIMSON DAR-8 aggregates pulled into liver/immune box; "hours, not days" clock ✓ |
| B08  | EXEMPT | Declared SLATE card ✓ |
| B09  | PASS   | Bell curve peaking at DAR 6, TEAL sweet-spot band 4–8, CRIMSON under-kill/over-aggregate arrows flanking peak ✓ |
| B10  | PASS   | Two-bar comparison: TEAL DAR-4 68% (tall) vs CRIMSON DAR-8 11% (short), "24 h", "illustrative" chip ✓ |
| B11  | FIXED  | "0.3" GOLD highlight box collided with "DAR-8:" prefix and "μg/g tumor" suffix. Increased arrange buff 0.02 → 0.55 and highlight padding, re-rendered. ✓ |
| B12  | EXEMPT | Declared SLATE card ✓ |
| B13  | PASS   | FormACard "Part of the Cancer Nanomedicine series." ✓ |
| B14  | PASS   | FormACard "Like and subscribe for more." ✓ |
| BVDT | PASS   | ClaudeVerdictArtifact "DAR: An Optimum, Not a Maximum", 4 real reel-specific verdict lines paginated ✓ |
| BHTF | PASS   | ClaudeComposerAsk "Your turn." + scaffolded 3-check ADC prompt ✓ |
| BOUT | PASS   | ClaudeTitleOutro shortened title, handle + mascot on ink ground ✓ |

Zero BLOCKER. Two MAJOR (B04, B11) fixed in Manim scene source and re-rendered before final compile. Zero MAJOR remaining on real beats.

**Audio presence:** `aac`, 48000 Hz stereo, `mean_volume -27.6 dB` (threshold >-40 dB) ✓

**Post-build punt sweep:**
`build.status` Counter: `{'VIDEO': 7, 'MANIM': 8, 'SLATE': 3}`

The 3 SLATE beats — B03 (question CARD), B08 (section CARD), B12 (endcard CARD) — are all legitimate declared CARD beats with real, non-placeholder authored `card` copy. Not pipeline punts (their `fill_plan` classifier resolves to `scripting-gap` / `author`-owned, so lane_check ignores them). Zero gen-AI slates, zero unfilled `remotion_scenes` / `fill_slates`, zero `DoodleScene`, zero `STILL src=archive` on animatable content, zero FormA/B naming a visual it does not draw. ✓

---

## Output

`vox-dar-optimum-slate.mp4` — 235.7s (3:56), audio present (-27.6 dB), mp4 mtime 17:28:33 is 10s newer than beat_sheet.json mtime 17:28:23. **DONE.**
