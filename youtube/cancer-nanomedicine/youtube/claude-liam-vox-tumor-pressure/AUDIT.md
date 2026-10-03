# AUDIT — claude-liam-vox-tumor-pressure
_Pass: 2026-08-28_

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` created (byte-exact copy of pre-edit sheet) ✓
- Dead ElevenLabs field dropped: `voice_id: "TyW6NH39JcFb5M3xdIIk"` — see REBUILD-LOG.md
- VOICE-LOCK fields retained: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓
- Palette=claude preserved; skin_warnings from prior build (B01 cold open, B13 outro) all resolved.

---

## Phase 1 Audit

### Check 1 — Stale renders
**PASS.** No mp4 files at the reel top level. `clips/master.m4a` and `clips/_work/*` from July 16 exist but predate the sheet edit; compile.py's SHA1 manifest will regenerate anything whose input changed.

### Check 2 — Bookends
**PASS.** Four canonical bookends present and correctly typed:
- B00: `ClaudeComposerAsk` ✓
- BVDT: `ClaudeVerdictArtifact` ✓ (verdict authored in Check 4)
- BHTF: `ClaudeComposerAsk` ✓
- BOUT: `ClaudeTitleOutro` ✓

### Check 3 — Spark lines
**FIXED (B00).**

- B00 `greeting: "Liam"` → `"Merhaba, Liam"` (Turkish, one word). Surveyed all sibling cancer-nanomedicine B00 greetings — Merhaba is unused; adjacent reels use Namaste / Jambo / Sawubona / Hola / Salaam / Ciao / Konnichiwa / Bonjour / Hej / Olá / Vanakkam / Kia ora / Ni hao.
- BHTF `greeting: "Your turn."` ✓ (already correct)
- No inner ClaudeComposerAsk body beats.

### Check 4 — Verdict
**FIXED (BVDT authored — real content).**

Previous state: `artifactLines: ["Key finding one", "Key finding two", "Key finding three"]`, `artifactHeading: "Key findings"` (placeholder per verdict_audit), `narration_text: ""` (empty). Body: 11 beats, ~441 words — qualifies for authored verdict, not strip.

New `artifactTitle`: `"Accumulation Is Not Delivery"`
New `artifactHeading`: `"The outward-pressure mechanism"`
New `artifactLines` (5 lines derived from B05–B10):
1. "Leaky vessels + broken lymphatics build core interstitial pressure 5–10× normal."
2. "Net flow is outward — particles that extravasate get carried back to the rim."
3. "The unreached hypoxic core selects for stress-tolerant, drug-resistant cells."
4. "Rim shrinks ~60%; core IFP 25 vs rim 5 mmHg; tumor doubles by week 8 from the core."
5. "The drug arrived. The delivery failed. Accumulation is not delivery."

New `narration_text` states the finding aloud (not "here is what the evidence shows" — that's in the EMPTY_NARRATION list).

`verdict_audit.py` post-fix: no violation returned for this reel.

### Check 5 — Card text
**FIXED (B01, B03, B11).**

- B01: `FormBCard` with placeholder `items` (`"Key point one/two/three"`) → `FormACard` with real title and sub. `lane: BOOKEND` removed (B01 is a body beat, not a bookend).
- B03: CARD with new `card.copy` / `sub` (was empty CARD body).
- B11: CARD with new `card.copy` / `sub` (was empty CARD body).

No FormA/FormB card carries a placeholder `sub` or overflowing `label`.

### Check 5b — Chart text
**N/A.** No Manim chart with axis or bar labels in this reel (all Manim scenes are structural diagrams and cross-sections). No `Text(narration[:30])` truncation risk.

### Check 6 — Punt sweep
**FIXED (B02, B04, B05, B06, B07, B08, B09, B10).**

Pre-fix, all these beats carried `build.needs: "YOU → 5–10s gen-AI clip → pantry (as BXX.mp4)"` (the banned gen-AI punt costume) plus, for B02, an additional `FormACard` fallback with truncated narration ("MRI shows a two-millimeter viable core at week three. The drug…") — the second banned punt costume ("FormA card whose narration names a visual it never draws").

All `needs`/`suggested` fields removed. B02's punt FormACard removed. Each beat now carries a `graphic.manim` scene name + `production_viz` block matching the locked narration intent — mapped to nopunt catalog rows (structural cross-section, leaky-vessel schematic, pressure-gauge + arrows, two-panel timeline, editorial highlight-quote).

Also B03 and B11 had `build.needs: "YOU → gen-AI clip"` on CARD beats — punt tag removed, CARDs are legitimate for question / endcard.

Zero remaining `YOU → gen-AI`, `fill_slates`, `remotion_scenes` slates, `DoodleScene`/`DoodleChart`, or `STILL src=archive/ai` on animatable content.

### Check 7 — Card-only reel
**PASS.** 7 body beats (B02, B04, B05, B06, B07, B08, B10 — plus B09's quote card) route to Manim GRAPHIC scenes. Not a card-only reel.

### Check 8 — Lens audit
**PASS (2+ moves present, one lens partially).**

- **Plato (artifact vs world):** central to the reel. The whole-organ MRI signal (artifact — "the drug has accumulated") ≠ the actual particle distribution (world — particles piled at the rim, core empty). B01, B02, B07, B11 all name this gap. "The accumulation was real. The delivery was not." IS Plato's move in one sentence. ✓
- **Descartes (radical doubt / falsifying question):** B03 poses the falsifying question ("Why did the core survive?") after B01 sets up the paradox. The whole reel is Descartes on "the drug accumulated" as a claim about the tumor. ✓
- **Popper (falsifiability, criterion in advance):** B10 gives the measurable criterion — if core IFP > rim IFP by 5–10×, particles cannot cross. That is the a-priori test. Partially present (the criterion is named but not framed as a pre-registered test).
- **Hume (confidence is a property of the model):** implicit — B10 labels numbers "illustrative scenario," B06 gives pressure as a 5–10× range not a point value. Present but not foregrounded.

Two moves clearly present (Plato + Descartes). No BLOCK.

### Check 9 — Brand fields
**FIXED.**

- `voice_id` (ElevenLabs) → DROPPED ✓
- `folderLabel: "@NikBearBrown"` ✓ (was already correct — channel handle, not brand key)
- `engine: kokoro`, `voice_kokoro: am_onyx` ✓
- Persona coherence: narration says "This is Liam, in for Bear" → voice is `am_onyx` ✓
- Prior `metadata.build.skin_warnings` (B01 cold open, B13 outro) both resolved by rebuilding B01 as FormACard and B12/B13 as FormACard bodies with BOUT as the canonical ClaudeTitleOutro.

### Check 10 — Pacing (LOG — do not fix)
**ADVISORY.** Words-per-second against measured audio:

| Beat | ~Words | actual_duration_s | ~wps | Verdict |
|------|--------|-------------------|------|---------|
| B01 | 42 | 12.74 | 3.30 | OK |
| B02 | 30 | 10.05 | 2.99 | OK |
| B03 | 33 | 10.77 | 3.06 | OK |
| B04 | 33 | 11.69 | 2.82 | OK |
| B05 | 34 | 11.11 | 3.06 | OK |
| B06 | 44 | 14.76 | 2.98 | OK |
| B07 | 44 | 14.87 | 2.96 | OK |
| B08 | 39 | 14.31 | 2.72 | OK |
| B09 | 36 | 10.45 | 3.44 | slightly hot |
| B10 | 63 | 20.16 | 3.13 | OK |
| B11 | 43 | 13.72 | 3.13 | OK |

All within or at 2.0–3.4 wps range. B09 is at 3.44 (marginal) — narration is locked, cannot retime.

### Check 11 — type_check.py
**PASS.**
```
[typecheck] GATE T: PASS
```
Ran cleanly on first attempt after sheet rewrite. No wordy-card, overflow, contrast, or kerning FAILs. See TYPECHECK.md.

---

## Phase 2 build follows in FILMLOOP-LOG entry.
