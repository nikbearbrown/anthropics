# REBUILD-LOG.md — claude-liam-writing-rules

**Rebuilt:** 2026-08-21  
**Contract:** skills/make/rebuild/SKILL.md  
**Pre-rebuild backup:** beat_sheet.pre-rebuild.json (byte-exact copy, made before any edit)

---

## LOCKED (carried over verbatim)

- All `narration_text` per beat — script unchanged.
- Beat order: B00, B01, B02, B05, BVDT, BHTF, BOUT.
- Act labels and shot intents — unchanged.
- Metadata identity: title, slug, topic, source_skill, brand, channel.

---

## REBUILT / FIXED (machinery changes)

### 1. Datable claim — modelLabel (B00 and BHTF)

| Field | Old value | New value | Source |
|---|---|---|---|
| B00 `props.modelLabel` | `"Opus 4.8"` | `"Opus 4.7"` | System context: current model as of 2026-08-21 is `claude-opus-4-7`; Opus 4.8 does not exist |
| BHTF `props.modelLabel` | `"Opus 4.8"` | `"Opus 4.7"` | Same |

Logged per the DOUBLE-CHECK LAW (rebuild contract §: The one exception to the narration lock — DATABLE CLAIMS).

### 2. Spark line / BHTF greeting — audit fix

| Beat | Field | Old value | New value | Reason |
|---|---|---|---|---|
| BHTF | `props.greeting` | `"Your Turn"` | `"Your turn."` | spark_line_fix.py BOOKEND_GREETINGS requires `"Your turn."` (lowercase, period) |
| B01 | `props.sparkLine` | `"Name it. Event it. Pattern it. Message it. One markdown file, immediate effect."` (13 words) | `"File. Fields. Pattern. Message."` (4 words) | type_check.py §8.5 fail: sparkLine 13 words > 12-word pull-quote limit; also satisfies ≤4-word spark line law |

---

## VOICE-LOCK

Envelope already correct: `engine: "kokoro"`, `voice: "am_onyx"` at metadata and per-beat.  
No dead ElevenLabs fields found (`voice_id`, `voice_env`). No changes needed.

---

## GATES

- REBUILD-LOG.md: this file.
- TYPECHECK.md: run 2026-08-21 (initial FAIL on B01 sparkLine; fixed; rerun pending).
- FACTCHECK.md: datable claims verified above (Opus 4.7 is current as of 2026-08-21).
