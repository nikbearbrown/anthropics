# REBUILD-LOG.md — claude-liam-sales
# Pass: 2026-08-26 (Film Factory)

## Locked (unchanged)
- All narration_text per beat — no datable claims found requiring correction
- Beat order and act structure (B00, C01, B01–B24, C01–C06, V01, H01, O01, BVDT, BHTF, BOUT)
- All shot intents, visual descriptions, spark_line values
- Metadata: title "Claude, Closing", slug "claude-liam-sales", channel "claude-liam", palette "claude"

## Rebuilt / Fixed

### BVDT — template verdict → real verdict
**Old narration_text:** "" (empty)
**New narration_text:** "The sales plugin meets you where you are — no big team required. It builds briefings from public information, drafts follow-ups from your notes, and tracks the pipeline even when it lives in a spreadsheet. Configured with your process, it stops being generic. But the plugin is research-and-prep. The closing stays yours."
**Reason:** Template default. Authored from body's own nouns and numbers per audit rule.

**Old artifactHeading:** "Key findings"
**New artifactHeading:** "Sales Plugin Verdict"

**Old artifactLines:** ["Key finding one", "Key finding two", "Key finding three"]
**New artifactLines:**
1. "Meets anyone who needs clients — no sales org required"
2. "Public info → briefing; your notes → follow-up draft"
3. "Configured with your process, it stops being generic"
4. "Prep accelerator, not a closer — the relationship is yours"
**Reason:** Template defaults — verbatim in many reels, not specific to this video.

### BHTF — brand field fix
**Old folderLabel:** "@claude-liam" (brand key, not channel handle)
**New folderLabel:** "@NikBearBrown" (correct channel handle per ai-explainer SKILL.md)
**Reason:** Brand field bug — channel handles use @NikBearBrown for claude-liam reels.

## Datable claims check
Narration contains no model version numbers, prices, or "as of" claims. Clean.

## VOICE-LOCK fields
All beats use engine="kokoro", voice="am_onyx" (or inherit metadata defaults).
No ElevenLabs-era fields (voice_id, voice_env) found. Clean.
