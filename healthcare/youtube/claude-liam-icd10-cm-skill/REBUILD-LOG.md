# REBUILD-LOG.md — claude-liam-icd10-cm-skill
Rebuild: 2026-08-25 (film-factory unattended run)
Original sheet backed up: beat_sheet.pre-rebuild.json

---

## Datable claim fixes (narration unchanged; props only)

| Field | Old | New | Source |
|-------|-----|-----|--------|
| metadata.modelLabel | "Opus 4.8" | "Opus 4.7" | Opus 4.8 does not exist as of 2026-08-25; Opus 4.7 is current latest (claude-opus-4-7) |
| B00 props.modelLabel | "Opus 4.8" | "Opus 4.7" | Same |
| BHTF props.modelLabel | "Opus 4.8" | "Opus 4.7" | Same |

## Props re-shaped to current schema (idea locked, representation fixed)

| Beat | Field | Old | New | Reason |
|------|-------|-----|-----|--------|
| BOUT | props | {title, handle, subline} | {title, slug} | ClaudeTitleOutro schema: handle is hardcoded, subline is locked-not-rendered; slug seeds mascot animation |
| B03 | props.body | "Extract billable ICD-10-CM diagnosis codes from a clinical note the…" (truncated) | Full sentence through "builds the claim." | Truncation artifact from generator; full idea restored |
| B03 | props.quote (added) | — | "What it gets right: repeatable results. What it bites: anything outside the spec." | Verbatim from locked narration; restores underfilled canvas |
| B03 | props.cite (added) | — | "icd10-cm-skill SKILL.md" | Source attribution for quote |
| B03 | props.verdictLabel (added) | — | "Repeatable" | Design-tell verdict derived from locked narration |
| B03 | props.verdictPositive (added) | — | true | Positive framing per narration |
| BVDT | artifactLines[1] | "…the way a professional cod" (truncated mid-word) | "…the way a professional coder builds the claim" | Truncation artifact |
| BHTF | props.command | "…the way a profes." (truncated) | "…the way a professional coder builds the claim." | Truncation artifact — full pasteable prompt for viewer |
| B00 | props.output[1] | "Extract billable ICD-10-CM diagnosis codes from a." (truncated) | "Extract billable ICD-10-CM diagnosis codes." | Clean CLI-style truncation |

## Narration locked — known artifacts (cannot fix under rebuild contract)

The generator truncated several narration_text fields. These are LOCKED and NOT changed:
- B03 narration: "…the way a professional coder builds ." (missing "the claim")
- BVDT narration: "…the way a profes." (truncated mid-word)
- BHTF narration: "…the way a profes." (truncated mid-word)

Audio will faithfully render these truncations. Future rebuild/re-script would fix at the source.

## VOICE-LOCK normalized
- engine: "kokoro", voice: "am_onyx" — already correct for claude-liam
- No ElevenLabs fields found to drop
