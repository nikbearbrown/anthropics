# AUDIT — claude-liam-vox-abraxane-solvent
_Pass: 2026-08-28_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` created (byte-exact copy before first edit) ✓
- Dead ElevenLabs fields dropped: `voice_id`, `clock`, `_variant_todo`, stale `build` block — see REBUILD-LOG.md
- VOICE-LOCK fields retained: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓

## Phase 1 Audit

### Check 1 — Stale renders
**PASS.** No mp4 files existed in the reel directory at audit start (no `media/`, no `manim/`, no master). `mp3/` and `clips/master.m4a` are Jul 16 audio — older than the new sheet, but they're audio not renders and get rebuilt.

### Check 2 — Bookends
**FIXED (B16, B17).**

Four canonical bookends present and correctly typed:
- B00: `ClaudeComposerAsk` ✓
- BVDT: `ClaudeVerdictArtifact` ✓ (content authored in Check 4)
- BHTF: `ClaudeComposerAsk` ✓
- BOUT: `ClaudeTitleOutro` ✓

B16 `OutroSeries` and B17 `OutroCTA` were non-claude skins in a claude-palette reel. Both changed to `FormACard` with narration preserved. Their falsely-stamped `build.status: "VIDEO"` (no `media/` directory existed at rebuild start) corrected to `SLATE`.

### Check 3 — Spark lines
**FIXED (B00).**

- B00 greeting: `"Liam"` → `"Aloha, Liam."` (Hawaiian). Adjacent claude-liam reels use Ciao, Bonjour, Konnichiwa, Namaste, Sawubona, Salaam, Hej, Merhaba, Jambo, Hola — Aloha is unused. Wagwan is Bear's.
- B00 segment: `"The Cancer Drug Where the Solvent, Not…"` (ellipsis-truncated mid-word) → `"Solvent, Not Drug"` (fits, no clip).
- BHTF greeting: `"Your turn."` ✓ (already correct).
- No inner ClaudeComposerAsk body beats in this reel — spark-line-per-beat rule N/A.

### Check 4 — Verdict
**FIXED (BVDT authored).**

Previous `artifactLines` were placeholders: `["Key finding one", "Key finding two", "Key finding three"]`. Previous `narration_text` was empty. Body has 15 beats, ~700 words — well over threshold; authored a real 4-line verdict + 5-sentence narration.

`artifactTitle`: `"The Cancer Drug Where the Solvent, Not the Drug, Was the Danger"` (63 chars, one-line lint fail) → `"Solvent, Not Drug, Was the Danger"` (33 chars). Same shortening applied to `BOUT.props.title`.

New `artifactLines`:
1. "Cremophor EL — not paclitaxel — triggered the bronchospasm and hypotension that shadowed Taxol."
2. "Albumin replaced the solvent; the drug molecule is identical in Taxol and Abraxane."
3. "Hypersensitivity: ~10% (Taxol) → <1% (Abraxane); infusion: 3 h with premeds → 30 min without."
4. "Abraxane's undisputed benefit is a formulation fix, not tumor targeting."

New `narration_text` (5 sentences, ~30 s at Kokoro pacing): "The drug never changed. The solvent did. Cremophor EL — a castor-oil surfactant used to dissolve paclitaxel — was the trigger for the bronchospasm and hypotension that shadowed Taxol infusions for decades. Abraxane replaced the solvent with albumin, the body's own carrier protein. Hypersensitivity dropped from roughly ten percent to under one percent, and a three-hour premedicated drip became a thirty-minute infusion. Abraxane's benefit is not tumor targeting. It is a pure formulation fix."

### Check 5 — Card text
**FIXED (B01, B04, B12).**

B01 `FormBCard` had placeholder items `[{label: "Key point one", sub: ""}, ...]` (CHECK 5 violation). Pattern changed to `FormACard` with two real lines derived from locked narration. `lane: "BOOKEND"` removed (B01 is a body exec-summary beat, not a bookend).

B02 and B10 carried `FormACard` fallback with a single line `"…"`-truncated mid-sentence (from `narration_text[:60]`) — a card-lint violation. These beats are now GRAPHIC/Manim (see Check 6), so the fallback was dropped.

B04, B12 had empty `card.sub`. Filled with short honest subs.

### Check 5b — Chart text
**FIXED (B09).**

B09 `graphic.production_viz.label` was narration-style: `"hypersensitivity rate: Taxol vs Abraxane"`. Shortened to `"HYPERSENSITIVITY RATE"` (short category noun). Bar labels in `scenes_std.py` are 1-word category nouns (`Taxol` / `Abraxane`). Numbers (`~10%` / `<1%`) sit above bars. Bar heights match narration meaning (TAXOL taller — the favored-safe thing is shorter). Footer is one complete sentence: `"Illustrative comparison — order of magnitude, not clinical trial data."` No mid-word truncation. TEAL/CRIMSON respect color law.

Other GRAPHIC beats reviewed for chart-text rule: B11 uses column headers `"Taxol"` / `"Abraxane"` (short nouns) with bullet lists 1–3 words each. B13 uses `"Taxol era"` / `"Abraxane era"` chip labels. B14 uses `"Bag A: Taxol"` / `"Bag B: Abraxane"` headers. All comply.

### Check 6 — Punt sweep, bookends included
**FIXED (B02, B10, and 8 body beats' `build.needs`).**

Gen-AI clip PUNTS (`shot.type=STILL`, `source=ai`, `build.needs="YOU → 5–10s gen-AI clip → pantry"`) removed:
- B02: STILL/ai (nurse at bedside) → GRAPHIC/Manim (`B02_PaclitaxelMechanism` — mitotic spindle freeze). The narration is about the drug's mechanism, not a photojournalism moment — a conceptual animation earns the beat.
- B10: STILL/ai (two IV bags on pharmacy bench) → GRAPHIC/Manim (`B10_TwoBagsSetup` — two IV bag isotypes on a shelf line, Bag A detailed). This is the visual SETUP for the B10 → B11 → B14 two-bag comparison; it's a diagram, not archival photography.

`build.needs` (PIPELINE/YOU-style pipeline stamps) removed from body beats: B03, B04, B05, B06, B07, B08, B09, B10, B11, B12, B13, B14, B15. The `production_viz` block is the rendering contract; `needs` was legacy stamping.

No DoodleScene/DoodleChart. No unfilled `fill_slates`/`remotion_scenes` slates. No `STILL src=archive` for conceptual content. No FormA card whose narration names a visual it never draws. No BOOKEND punt.

### Check 7 — Card-only reel
**PASS.** 10 body beats draw real figures via Manim (B02, B03, B05, B07, B08, B09, B10, B11, B13, B14). Not a card-only reel. Cards used only for legitimate rhetorical purposes: B04 question, B06 highlighted document, B12 section transition, B15 endcard.

### Check 8 — Lens audit
**PASS (2+ moves present).**

- **Plato (artifact / world / relationship)**: The reel's core move. B12 states it explicitly — "This is what makes Abraxane different from most nanoparticle stories. We usually talk about nanoparticles accumulating at tumors, exploiting leaky blood vessels. That may play a role. But Abraxane's primary, undisputed benefit has nothing to do with tumor biology. It is a pure formulation fix." Artifact = the "nanoparticle" label / marketing story; World = the actual mechanism (solvent replacement); Relationship = the relationship is much narrower than the artifact implies. ✓
- **Descartes (falsifying question)**: B04 frames the falsifying question: "The drug didn't change. What did — and why did the reactions stop?" — asked as a diagnostic, not a mystery. B15 answers with the falsifier: "The drug never changed. The solvent did." ✓
- **Hume (confidence is a property of the model, not the world)**: Numbers hedged in narration ("roughly ten percent", "under one percent") and explicitly labeled "illustrative comparison" / "illustrative example" in production_viz for B09 and B14. ✓ (partial — Hume's move is implicit)
- **Popper (falsifying in advance)**: The stated test would be — if hypersensitivity persisted with Abraxane, the "solvent-caused" theory would fail. Not stated as a formal in-advance failing test; implicit in the causal claim. Partial.

Two moves clearly present (Plato + Descartes); one weakly (Hume). ≥2 threshold met.

### Check 9 — Brand fields
**FIXED.**

- `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs) → DROPPED ✓
- `clock` (ElevenLabs-era prose) → DROPPED ✓
- `folderLabel: "@NikBearBrown"` on B00 and BHTF ✓
- `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓
- B16/B17 palette mismatch → FIXED (Check 2)
- Persona: narration says "This is Liam, in for Bear." → voice is `am_onyx` ✓. No Bear/Liam voice-swap.

### Check 10 — Pacing (LOG — do not fix)
**ADVISORY.** Against Kokoro-measured `actual_duration_s`, four body beats exceed the 3.4 wps ceiling:

| Beat | Words | actual_duration_s | wps |
|------|-------|-------------------|------|
| B01  | 51    | 10.65             | 4.8  |
| B03  | 51    | 14.78             | 3.4 (edge) |
| B12  | 60    | 17.17             | 3.5  |
| B14  | 122   | 29.61             | 4.1  |

B01 and B14 are the two biggest misses. Narration is locked (rebuild contract). Not fixed. Logged.

### Check 11 — type_check.py
**PASS.**
```
GATE T: PASS
```
Advisories only: §8.10 recite score B01 = 0.80 ("narration recites the card") and BVDT = 0.69 — both under the fail threshold. Narration is locked; the exec-summary beat's FormACard lines do echo the narration's punchline by design.

---

## Phase 2 — Build

**Audio:** BVDT mp3 generated via Kokoro `am_onyx` (26.94 s). Beats B01–B17 have existing mp3 files from Jul 16 whose narration is byte-identical to the locked script — reused (would be identical if regenerated).

**Manim renders:** 10 GRAPHIC beats rendered via `scenes_std.py` at 1080p24 to `manim/`:
- B02 (PaclitaxelMechanism), B03 (InsolubilityProblem), B05 (CremophorCascade), B07 (AlbuminBinding), B08 (SolventDrain — CRIMSON drain, TEAL remains — the sheet's `manim_move: "drain"`), B09 (ComparisonBars), B10 (TwoBagsSetup), B11 (TwoBagComparison), B13 (TimelineSummary), B14 (ExampleSideBySide).

**Remotion renders:** bookend + FormACard beats rendered via `remotion_scenes.py`:
- B00 (ClaudeComposerAsk), B01 (FormACard), B16 (FormACard series tag), B17 (FormACard CTA), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk), BOUT (ClaudeTitleOutro).

**Legitimate SLATE cards (declared, not punts):** B04 (question card), B06 (document quote), B12 (section card), B15 (endcard) — compile.py draws these from `card.copy`/`card.sub`. Exempt from Gate V (declared placeholders by design).

**Compile:** `compile.py . --review --height 720 --fps 24`

```
GATE CONTENT:  PASS (21/21 beats)
GATE FRAME:    PASS (21/21 beats, canvas 3840×2160)
GATE LANE:     PASS (known_slates=['B04','B06','B12','B15'])
GATE T:        PASS (advisories only: B01=0.80, BVDT=0.69 recite; narration locked)
GATE AUDIO:    PASS (mean_volume −27.5 dB, threshold −40 dB)
slots:         17/21 filled — 5 VIDEO (Remotion) + 10 MANIM + 4 declared SLATE + 2 VIDEO (FormACard outros)
Deliverable:   vox-abraxane-solvent-slate.mp4 (314.0 s, 720p review cut)
```

**Gate V — QC frame review** (1-fps sample into `_qc/frames/`, 314 frames + spot mids):

| Beat | Status | Finding |
|------|--------|---------|
| B00  | PASS   | ClaudeComposerAsk; "Aloha, Liam." greeting; segment "Solvent, Not Drug"; @NikBearBrown ✓ |
| B01  | PASS   | FormACard, 2 real lines from locked narration, centered, no overflow ✓ |
| B02  | PASS   | Mitotic spindle w/ paclitaxel squares; "Division halted" TEAL chip ✓ |
| B03  | PASS   | Insoluble clumped drug particles in wave-line water; CRIMSON chip ✓ |
| B04  | EXEMPT | Declared SLATE (question card) ✓ |
| B05  | PASS   | Cremophor pool → mast cell → radiating cascade; CRIMSON risk chips ✓ (Manim uppercase-chip kerning baseline artifacts present in-channel — same as sibling emitter-range shipped cut) |
| B06  | EXEMPT | Declared SLATE (document quote) ✓ |
| B07  | PASS   | Teal albumin blob with docked INK drug squares; "Albumin nanoparticle ~130 nm" chip ✓ |
| B08  | PASS   | Drain move: CRIMSON pool drops off-screen; TEAL "Albumin" remains; "No hypersensitivity" chip ✓ |
| B09  | FIXED  | First render placed "~10%" INSIDE the crimson bar (crimson-on-crimson, low contrast — MAJOR). Fixed: moved both numbers ABOVE the bars, size 32→36. Re-rendered. Now clean high-contrast crimson/teal on cream. ✓ |
| B10  | PASS   | Two IV bag isotypes on shelf line; Bag A detailed (5 icons); Bag B "…filled in next"; "Same drug" footer ✓ |
| B11  | PASS   | Two-column checklist: TAXOL 5 bullets / ABRAXANE 5 bullets; "Same drug." italic footer ✓ |
| B12  | EXEMPT | Declared SLATE (section card) ✓ |
| B13  | PASS   | Timeline: TAXOL ERA (CRIMSON zone, "Cremophor solvent") / ABRAXANE ERA (TEAL zone, "Albumin carrier"); paclitaxel icon spans both ✓ |
| B14  | PASS   | Illustrative example: two big panels; TAXOL panel 5 icons + "~10% hypersensitivity"; ABRAXANE panel 4 icons + "<1% hypersensitivity"; "Same drug." serif footer ✓ |
| B15  | EXEMPT | Declared SLATE (endcard) ✓ |
| B16  | PASS   | FormACard "Part of the Cancer Nanomedicine series." ✓ |
| B17  | PASS   | FormACard "Like and subscribe for more." ✓ |
| BVDT | PASS   | ClaudeVerdictArtifact "Solvent, Not Drug, Was the Danger" — 4 real verdict lines across pages 1/2 and 2/2 ✓ |
| BHTF | PASS   | ClaudeComposerAsk "Your turn." + real scaffolded 4-part rubric (vehicle, reaction, test) ✓ |
| BOUT | PASS   | ClaudeTitleOutro, shortened title, @NikBearBrown handle, pixel-bear mascot ✓ |

Zero BLOCKER. One MAJOR fixed on B09 before final compile.

**Audio presence:** aac, 48000 Hz stereo, 314.04 s, mean_volume −27.5 dB, max_volume −5.8 dB — passes −40 dB floor ✓.

**Post-build punt sweep** (all beats, bookends included):

`build.status` Counter: `Counter({'MANIM': 10, 'VIDEO': 7, 'SLATE': 4})`

- MANIM (10): B02, B03, B05, B07, B08, B09, B10, B11, B13, B14 — all drawn figures.
- VIDEO (7): B00, B01, B16, B17, BVDT, BHTF, BOUT — Remotion renders.
- SLATE (4): B04 (question card), B06 (document quote), B12 (section card), B15 (endcard) — declared CARD/DOCUMENT beats; legitimate for a review-slate cut; the invocation's PIPELINE-CARD RULE ban on slates in a FINAL doesn't apply here.

Zero gen-AI clip PUNTS. Zero DoodleScene. Zero `STILL src=archive/ai` in body. Zero placeholder verdict. Zero unfilled `fill_slates`/`remotion_scenes`. No BOOKEND punt.

**Staleness check:** mp4 mtime `2026-08-28 08:50:45` vs sheet mtime `2026-08-28 08:50:33` (+12 s) — mp4 newer than sheet ✓. No post-compile sheet edits.

**Drawon motion advisory:** 9/21 beats (42%) — over the ~40% pantry cap. Native vox-explainer language for a mechanism-heavy chapter; logged, not downgraded. Same advisory shipped on peer emitter-range.

**Downgrade justification:** none. No gates weakened.

## Output

`vox-abraxane-solvent-slate.mp4` — 314.0 s, 720p review-slate cut. Audio present at −27.5 dB. mp4 newer than beat_sheet.json (Δ+12 s). DONE.

