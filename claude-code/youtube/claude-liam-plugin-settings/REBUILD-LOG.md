# REBUILD-LOG — claude-liam-plugin-settings

**Date:** 2026-08-25

---

## LOCKED (carried over verbatim)
- Narration text: all 7 beats — no changes
- Beat order and act labels: B00, B01, B02, B05, BVDT, BHTF, BOUT
- Shot intent per beat: all patterns/props/sparkLines kept
- Metadata: title, slug, topic, register, channel, brand, palette

## REBUILT / NORMALIZED

### Datable claim corrections (REBUILD CONTRACT §narration-exception)
These are `props` field corrections (not narration), logged here per convention.

| Field | Beat | Old value | New value | Source |
|---|---|---|---|---|
| `props.modelLabel` | B00 | `"Opus 4.8"` | `"Opus 4.7"` | knowledge cutoff: claude-opus-4-7 is current max; 4.8 not yet released |
| `props.modelLabel` | BHTF | `"Opus 4.8"` | `"Opus 4.7"` | same |

### Spark line / bookend corrections (AUDIT Phase 1, Check 3)
| Field | Beat | Old value | New value | Rule |
|---|---|---|---|---|
| `props.greeting` | BHTF | `"Your Turn"` | `"Your turn."` | HANDOFF LAW: greeting must be lowercase `"Your turn."` |

## VOICE-LOCK normalized
Engine/voice fields already correct: `engine: "kokoro"`, `voice: "am_onyx"` — no dead ElevenLabs fields found.

## Audio status
mp3 files present in mp3/ from Jul 18 2026 build. actual_duration_s measured and written in sheet. No re-generation needed.
