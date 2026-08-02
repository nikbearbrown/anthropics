# Render Report — who-was-max-planck MEDHAVY + HAI Variants (REPAIRED)

Generated: 2026-07-16
Repair run: replaced broken 8-beat MedhavyCard / 9-beat OutroCTA structures with correct
10-beat Claude-explainer structure matching claude-liam-who-was-max-planck.

---

## Canonical Visual Master (read-only)

`/Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/claude-liam-who-was-max-planck/`

Manim assets used:
- `manim/B02.mp4` — E=hν energy ladder
- `manim/B04.mp4` — Planck vs Rayleigh-Jeans spectral radiance

---

## MEDHAVY Variant

- **Status**: BUILT
- **Output dir**: `physics-modern-physics/youtube/medhavy-who-was-max-planck/`
- **Final MP4**: `/Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/medhavy-who-was-max-planck/who-was-max-planck-medhavy.mp4`
- **Register**: Wonder (first principles, genuine wonder, no drills)
- **Voice**: Kokoro `af_kore`
- **Palette**: medhavy (Okabe-Ito, CREAM `#F0EAD6`)
- **Brand**: `medhavy`
- **Duration**: 134.0s (~2:14)
- **Resolution**: 1920×1080
- **Audio stream**: YES (per-beat narration, Kokoro af_kore)
- **File size**: 2,238,701 bytes (~2.1 MB)
- **Authoritative beat sheet**: `beat_sheet.medhavy.json`
- **Pipeline copy**: `beat_sheet.json`
- **PEDAGOGY verdict**: PASS
- **FACTCHECK verdict**: PASS
- **QC contact sheet**: `qc-sheet.png`

### Beat structure (10 beats — all confirmed)

| Beat | Act | Pattern | Status | Source |
|------|-----|---------|--------|--------|
| B00 | ASK | ClaudeComposerAsk | VIDEO | New Remotion render (greeting "Hallo, Medhavy") |
| B01 | THE PROBLEM | CARD | SLATE | Pending gen-AI clip |
| B02 | THE GAMBIT | MANIM | MANIM | Copied from canonical manim/B02.mp4 |
| B03 | THE ASK | ClaudeComposerAsk | VIDEO | New Remotion render (folderLabel "@Medhavy") |
| B04 | THE RESULT | MANIM | MANIM | Copied from canonical manim/B04.mp4 |
| B05 | RELUCTANT REVOLUTIONARY | CARD | SLATE | Pending gen-AI clip |
| B06 | THE LEGACY | ClaudeWindow | VIDEO | New Remotion render (quantum century timeline) |
| B07 | THE MAN | CARD | SLATE | Pending gen-AI clip |
| B08 | HANDOFF | ClaudeComposerAsk | VIDEO | New Remotion render (greeting "Your turn.") |
| B09 | OUTRO | ClaudeTitleOutro | VIDEO | New Remotion render (handle "@Medhavy") |

**Slots filled**: 7/10 VIDEO/MANIM, 3/10 CARD/SLATE (same as canonical — B01, B05, B07 need gen-AI clip)

### Validation checklist

- [x] B00 uses ClaudeComposerAsk (not MedhavyOpen)
- [x] B02 uses Manim E=hν energy ladder (not MedhavyConceptCard)
- [x] B03 uses ClaudeComposerAsk (ASK micro-beat)
- [x] B04 uses Manim Planck vs Rayleigh-Jeans (not MedhavyConceptCard)
- [x] B06 uses ClaudeWindow (quantum century timeline)
- [x] B08 ClaudeComposerAsk with greeting "Your turn." (HANDOFF LAW)
- [x] B09 ClaudeTitleOutro with title "Who was Max Planck?" (OUTRO LAW)
- [x] No MedhavyOpen, MedhavyConceptCard, MedhavyOutro in sheet
- [x] No SUBSCRIBE screen
- [x] No exercise beat (correct for Wonder/Medhavy)
- [x] Audio present (af_kore, 10 beats)
- [x] 1920x1080, audio stream confirmed by ffprobe

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/medhavy-who-was-max-planck/who-was-max-planck-medhavy.mp4
```

---

## HAI Variant

- **Status**: BUILT
- **Output dir**: `physics-modern-physics/youtube/hai-who-was-max-planck/`
- **Final MP4**: `/Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/hai-who-was-max-planck/who-was-max-planck-hai.mp4`
- **Register**: Pragmatist (method, when to use, when NOT to)
- **Voice**: Kokoro `am_onyx`
- **Palette**: humanitarians (muted editorial, CREAM `#F3EBDD`)
- **Brand**: `hai`
- **Duration**: 145.2s (~2:25)
- **Resolution**: 1920×1080
- **Audio stream**: YES (per-beat narration, Kokoro am_onyx)
- **File size**: 2,361,947 bytes (~2.3 MB)
- **Authoritative beat sheet**: `beat_sheet.hai.json`
- **Pipeline copy**: `beat_sheet.json`
- **PEDAGOGY verdict**: PASS
- **FACTCHECK verdict**: PASS
- **QC contact sheet**: `qc-sheet.png`

### Beat structure (10 beats — all confirmed)

| Beat | Act | Pattern | Status | Source |
|------|-----|---------|--------|--------|
| B00 | ASK | ClaudeComposerAsk | VIDEO | New Remotion render (greeting "Hallo, HAI") |
| B01 | THE PROBLEM | CARD | SLATE | Pending gen-AI clip |
| B02 | THE METHOD | MANIM | MANIM | Copied from canonical manim/B02.mp4 |
| B03 | THE ASK | ClaudeComposerAsk | VIDEO | New Remotion render (folderLabel "@HumanitariansAI") |
| B04 | THE RESULT | MANIM | MANIM | Copied from canonical manim/B04.mp4 |
| B05 | RELUCTANT REVOLUTIONARY | CARD | SLATE | Pending gen-AI clip |
| B06 | THE LEGACY | ClaudeWindow | VIDEO | New Remotion render (quantum tech stack timeline) |
| B07 | THE MAN | CARD | SLATE | Pending gen-AI clip |
| B08 | HANDOFF | ClaudeComposerAsk | VIDEO | New Remotion render (greeting "Your turn.") |
| B09 | OUTRO | ClaudeTitleOutro | VIDEO | New Remotion render (handle "@HumanitariansAI") |

**Slots filled**: 7/10 VIDEO/MANIM, 3/10 CARD/SLATE (same as canonical — B01, B05, B07 need gen-AI clip)

### Validation checklist

- [x] B00 uses ClaudeComposerAsk (not MedhavyConceptCard)
- [x] B02 uses Manim E=hν energy ladder (not MedhavyConceptCard)
- [x] B03 uses ClaudeComposerAsk (ASK micro-beat)
- [x] B04 uses Manim Planck vs Rayleigh-Jeans (not MedhavyConceptCard)
- [x] B06 uses ClaudeWindow (quantum technology stack)
- [x] B08 ClaudeComposerAsk with greeting "Your turn." (HANDOFF LAW)
- [x] B09 ClaudeTitleOutro with title "Who was Max Planck?" (OUTRO LAW)
- [x] No MedhavyOpen, MedhavyConceptCard, OutroCTA in sheet
- [x] No B_CLI terminal exercise (per task instructions — no CLI exercise in this repair)
- [x] No SUBSCRIBE screen
- [x] Audio present (am_onyx, 10 beats)
- [x] 1920x1080, audio stream confirmed by ffprobe

### Notes

- B04 Manim (6.5s clip) slowed 3.2x to fill the 20.4s HAI narration beat. compile.py logged a WARNING (extreme slow-mo). Visually acceptable in the slate cut; to fix, add narration-synced Manim or drop a longer B04.mp4 from pantry/.
- "When to use / when NOT to" is embedded in B04 narration (decision boundary: hν vs kT) and B05 (quantum hypothesis limits — not position/momentum). PASS.

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/hai-who-was-max-planck/who-was-max-planck-hai.mp4
```

---

## Repairs Made

### Previous broken state (both variants)

**Medhavy (8 beats):**
- B00 → MedhavyOpen (wrong — should be ClaudeComposerAsk)
- B01–B06 → MedhavyConceptCard (wrong — B02/B04 should be Manim; B03 should be ClaudeComposerAsk; B06 should be ClaudeWindow)
- B07 → MedhavyOutro (wrong — should be ClaudeTitleOutro)
- Missing: B08 (HANDOFF/ClaudeComposerAsk "Your turn."), B09 (ClaudeTitleOutro)
- Missing: both Manim simulations

**HAI (9 beats):**
- B00 → MedhavyConceptCard (wrong — should be ClaudeComposerAsk)
- B01–B06 → MedhavyConceptCard (wrong — B02/B04 should be Manim; B03 should be ClaudeComposerAsk; B06 should be ClaudeWindow)
- B_CLI → MedhavyConceptCard terminal card (wrong pattern)
- B_OUTRO → OutroCTA (wrong — should be ClaudeTitleOutro)
- Missing: B08 (HANDOFF/ClaudeComposerAsk "Your turn."), B09 (ClaudeTitleOutro)
- Missing: both Manim simulations

### What was done

1. Read all skill/brand/voice documentation before touching files
2. Read canonical claude-liam-who-was-max-planck/beat_sheet.json as the structural source of truth
3. Rewrote both beat sheets from canonical 10-beat structure:
   - Medhavy: narration rewritten in Wonder register, persona "Hallo, Medhavy" / "@Medhavy"
   - HAI: narration rewritten in Pragmatist register, persona "Hallo, HAI" / "@HumanitariansAI"
4. Cleared stale media files from wrong-pattern builds
5. Copied Manim renders from canonical: manim/B02.mp4, manim/B04.mp4
6. Copied scenes.py from canonical to both variants
7. Rendered 5 Remotion beats per variant: B00, B03, B06, B08, B09 — all ClaudeComposerAsk/ClaudeWindow/ClaudeTitleOutro
8. Generated Kokoro audio: af_kore (Medhavy, 10 beats), am_onyx (HAI, 10 beats)
9. Compiled at 1080p with --allow-slates (B01, B05, B07 are CARD/SLATE — correct, same as canonical)
10. Copied final cuts to required filenames: who-was-max-planck-medhavy.mp4, who-was-max-planck-hai.mp4
11. Updated PEDAGOGY.md, FACTCHECK.md, MEDIA-LEDGER.md for both variants

---

## Remaining Concerns

- **B04 HAI slow-motion warning**: 6.5s Manim clip slowed 3.2x to fill 20.4s HAI narration. Acceptable for review cut. Drop a longer B04.mp4 from pantry/ to fix.
- **B01, B05, B07 slates (both variants)**: These CARD/SLATE beats are pending human-supplied gen-AI clips. Same status as canonical. Drop clips into pantry/ as B01.mp4, B05.mp4, B07.mp4 and recompile.

---

## Open commands

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/medhavy-who-was-max-planck/who-was-max-planck-medhavy.mp4
open /Users/bear/Documents/CoWork/bear-textbooks/books/physics-modern-physics/youtube/hai-who-was-max-planck/who-was-max-planck-hai.mp4
```
