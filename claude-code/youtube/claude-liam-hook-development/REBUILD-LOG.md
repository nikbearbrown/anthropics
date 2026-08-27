# REBUILD-LOG — claude-liam-hook-development

**Date:** 2026-08-25
**Auditor:** filmloop (unattended)

---

## What was locked (carried over verbatim)
- All narration_text fields (no narration changes)
- Beat order and act labels
- Shot patterns and intent
- Metadata identity: title, slug, topic, source pointer, channel

## What was rebuilt / fixed

### Beat-sheet edits

| Field | Old value | New value | Reason |
|---|---|---|---|
| B00.props.modelLabel | "Opus 4.8" | "Opus 4.7" | Datable claim: Opus 4.8 does not exist; latest is claude-opus-4-7 (Aug 2026) |
| B01.props.sparkLine | "Nine events. Two types. Prompt for judgment, command for speed." | "Nine events. Two types." | SPARK-LINE LAW: inner beats ≤4 words |
| B02.props.sparkLine | "Format mismatch is silent. Parallel hooks cannot coordinate." | "Format mismatch: silent failure." | SPARK-LINE LAW: inner beats ≤4 words |
| B05.props.sparkLine | "Event model complete. Format mismatch: silent failure." | "Complete model. Real gaps." | SPARK-LINE LAW: inner beats ≤4 words |
| BHTF.props.greeting | "Your Turn" | "Your turn." | HANDOFF LAW: lowercase t, period |
| BHTF.props.modelLabel | "Opus 4.8" | "Opus 4.7" | Datable claim: same as B00 |

### Remotion component edits

| File | Change | Reason |
|---|---|---|
| runtime/remotion/src/scenes/HookDevConfig.tsx | SERIF title fontSize 42 → 48 | GATE T §8.1 precaution: fontSize 42 Tiempos Text failed on SkillDev* reel (2026-08-25); 48px confirmed passing |

---

## Voice-lock
VOICE-LOCK fields correct: engine kokoro, voice am_onyx, voice_kokoro am_onyx. No dead ElevenLabs fields (voice_id, voice_env) present.

## Pre-rebuild backup
`beat_sheet.pre-rebuild.json` — byte-exact copy (MD5: 0b5260ff82b29a57d2fa077be0363c25).
