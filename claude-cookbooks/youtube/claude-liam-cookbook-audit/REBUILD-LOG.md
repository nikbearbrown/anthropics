# REBUILD-LOG — claude-liam-cookbook-audit

**Rebuild date:** 2026-08-25  
**Rebuilder:** film-factory (unattended)

---

## LOCKED (carried verbatim)
- Narration for B00, B01, B02 (after text repairs noted below)
- Beat order and act labels
- Shot patterns and visual intent for all beats

## TEXT REPAIRS (truncation correction — original intent restored, not changed)

| Beat | Field | Old | New | Source |
|---|---|---|---|---|
| B03 | narration_text | "...audit is r." | "...audit is requested." | Context: skill description ends "...notebook review or audit is requested." |
| BHTF | narration_text | "...use whenever a notebook ." | "...use whenever a notebook review or audit is requested." | Same source |
| BHTF | shot.remotion.props.command | "...use whenever a." | "...use whenever a notebook review or audit is requested." | Same source |

## SPARK LINE FIXES (Check 3 — ≤4 word rule)

| Beat | Old sparkLine | New sparkLine | Word count |
|---|---|---|---|
| B01 | "The file is the program." | "File is the program." | 5→4 |
| B03 | "This is the part worth knowing." | "Spec defines the limit." | 6→4 |

## VERDICT STRIPPED (Check 4)

BVDT beat removed. Reasons:
1. Body is 3 beats / ~119 words — below the 5-beat / 180-word threshold for authoring a verdict
2. Lines 3-4 ("Same input → same output, every run" / "Limit: only what the SKILL.md specifies") are true of any skill-teardown reel — fail the "would still be true of a different video" test
3. Line 2 was truncated ("...Use whenever a notebook review or ")

Per audit rules: thin body → strip. A placeholder verdict is worse than none.  
BVDT mp3 (beat-BVDT.mp3) removed as orphan.

## VOICE-LOCK
Engine/voice already correct: `kokoro` / `am_onyx`. No dead ElevenLabs fields present.

## AUDIO REGENERATION REQUIRED
- B03: narration changed (truncation repaired); existing mp3 generated from truncated text
- BHTF: narration changed (truncation repaired, ~6 words added); existing mp3 generated from truncated text
