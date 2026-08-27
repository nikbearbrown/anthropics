# REBUILD-LOG — claude-liam-fhir-developer-skill
Rebuilt: 2026-08-25  Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json`

---

## Narration / prop changes (LOCK applies — only datable claims and Phase 1 fixes)

### B00 — narration: placeholder fill
- **OLD:** `"The skill is fhir-developer-skill. >."`
- **NEW:** `"The skill is fhir-developer-skill. FHIR REST API development for healthcare."`
- **Source:** SKILL.md header line — "FHIR REST API development for healthcare"

### B03 — narration: placeholder fill
- **OLD:** `"Claude's job: >."`
- **NEW:** `"Claude's job: validate FHIR resources and return the right HTTP status code."`
- **Source:** SKILL.md Steps section — validate resource structure → return correct HTTP status

### B03 — props.body: placeholder fill + wordy fix
- **OLD:** `">"`
- **NEW:** `"422: invalid enum. 412: ETag mismatch. Status code IS the spec."`
- **Source:** SKILL.md — §8 error-response table (422 invalid enum values, 412 ETag mismatch)
- **Note:** Previous fill attempt was 15 words (over §8.5 12-word budget); shortened to 11 words

### BHTF — narration: placeholder fill
- **OLD:** `"'I want to >."`
- **NEW:** `"'I want to build a FHIR Observation endpoint with status validation. Read the fhir-developer-skill skill and walk me through what you will do before you do it.'"`
- **Source:** SKILL.md primary use-case: Observation resource validation, SMART on FHIR auth

### BHTF — props.command: placeholder fill
- **OLD:** `"I want to >."`
- **NEW:** `"I want to build a FHIR Observation endpoint with status validation. Read the fhir-developer-skill skill and walk me through what you will do before you do it."`
- **Source:** same as narration above

---

## Datable-claim fixes

### B00, BHTF, BOUT — props.modelLabel
- **OLD:** `"Opus 4.8"`
- **NEW:** `"Opus 4.7"`
- **Source:** current model roster (Opus 4.7 is the published model label; 4.8 was not released)

---

## Structural changes (Phase 1 authorized)

### BVDT — verdict strip
- Beat completely removed from beats array
- **Reason:** body word count < 180 words (B01+B02+B03 = 3 beats, ~96 words) — below 5-beat / 180-word threshold for verdict
- **Rule:** `verdict_strip.py` threshold — strip if body < 5 beats OR < 180 words
- `metadata.build.filled`: 7→6, `metadata.build.of`: 7→6

---

## Audio regenerated
Beats B00, B03, BHTF had stale mp3s (generated with `>` placeholders). Deleted and regenerated via:
`python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel> --only B00 B03 BHTF`
Voice: am_onyx / kokoro (per beat_sheet `voice_kokoro` field). B01, B02, BOUT unchanged.

---

## Remotion component fix (Gate T §8.1)

File: `brutalist-art/runtime/remotion/src/scenes/SkillTeardownPipeline.tsx`

Root cause: SkillTeardownPipeline renders at 1920×1080 CSS with `--scale=2` (3840×2160 physical).
The title `fontSize:44` CSS → 88px physical but lowercase x-height ≈ 40px physical (below 41px floor).
Also: eyebrow (13→16), INPUT/OUTPUT category labels (11→14), content text (20→22) were sub-floor.

| Element | Old CSS fontSize | New CSS fontSize | Physical (×2) |
|---------|-----------------|-----------------|---------------|
| eyebrow | 13 | 16 | 32px |
| INPUT/OUTPUT labels | 11 | 14 | 28px |
| inputLabel / outputLabel / footerNote | 20 | 22 | 44px |
| title | 44 | 52 | 104px (x-height ~47px) |

The 39px measurement was from lowercase letter blobs within the title word "How the skill works." — x-height of EB Garamond at 44×2=88px ≈ 40px, detected as isolated text-run blobs by type_check blob detector. Raising to 52px CSS → x-height ~47px → clears 41px floor.
