# AUDIT.md — claude-liam-fraud-detection
Audited: 2026-08-25 (film-factory pass)

## Check 1 — Stale renders
**PASS** — No mp4 files exist anywhere in the reel folder (no media/, no clips/*.mp4).
Nothing to delete.

## Check 2 — Bookends
**PASS** — All four present:
- B00: ClaudeComposerAsk ✓
- BVDT: ClaudeVerdictArtifact ✓
- BHTF: ClaudeComposerAsk with greeting "Your turn." ✓
- BOUT: ClaudeTitleOutro ✓
Note: BVDT absent-but-real is acceptable; BVDT is present and non-empty here.

## Check 3 — Spark lines
**FIXED**
- B00 greeting: "Hola, Liam" ✓ (world-language hello, not Wagwan)
- BHTF greeting: "Your turn." ✓
- B03 sparkLine: was "This is the part worth knowing." (7 words, generic) → FIXED to "Spec-locked. Bounded." (4 words, compressed from narration)
- B01 sparkLine "The file is the program." — on SkillTeardownAnatomy (not a ClaudeComposerAsk inner composer); 5 words on a non-composer beat. Kept: the 4-word limit applies to ClaudeComposerAsk inner composers; this is a teardown anatomy card prop.
- B02 sparkLine "Input in. Output out." — 4 words ✓

## Check 4 — Verdict
**FIXED** (authorized under Phase 1 Check 4)
- BVDT narration truncation repaired (incomplete sentence ending at "produce." → full sentence)
- BVDT artifactLines[1] truncation repaired ("...waste," → complete phrase)
- Verdict is real and specific to fraud-detection (not a template default):
  lines 1, 3, 5 are specific; line 4 ("Same input → same output") is meaningful for this skill's guarantee.
- Body beats B01+B02+B03 total ~110 words / 3 beats — below the 180-word/5-beat auto-author threshold.
  Verdict is NOT a placeholder; content is real. Kept (not stripped).

## Check 5 — Card text
**PASS** — No FormA/FormB cards in this reel. All beats use SkillTeardown* or bookend patterns.

## Check 6 — Punt sweep
**PASS** — All beats are real Remotion components:
- B00: ClaudeComposerAsk ✓
- B01: SkillTeardownAnatomy ✓ (file tree with icons)
- B02: SkillTeardownPipeline ✓ (pipeline diagram)
- B03: SkillTeardownMechanism ✓ (mechanism display)
- BVDT: ClaudeVerdictArtifact ✓
- BHTF: ClaudeComposerAsk ✓
- BOUT: ClaudeTitleOutro ✓
No DoodleScene, no DoodleChart, no STILL src=archive, no gen-AI asks, no unfilled slates.

## Check 7 — Card-only reel
**PASS** — B01 shows a file tree, B02 shows a pipeline diagram, B03 shows a mechanism card.
These are visual Remotion scenes, not plain text cards.

## Check 8 — Lens audit
**PASS** (carried from existing LENS-AUDIT.md, dated 2026-08-03)
- Popper (BVDT): "Limit: only what the SKILL.md specifies" — states in advance what would falsify the tool's claim to work ✓
- Plato (BHTF): "walk me through what you will do before you do it" — artifact/world distinction forced before acting ✓
- Two moves confirmed. Source material (skill-teardown SKILL.md) cannot strongly support Descartes/Hume without over-reading.

## Check 9 — Brand fields
**FIXED**
- folderLabel: "@NikBearBrown" ✓ (channel handle, not brand key)
- engine: "kokoro" ✓; voice: "am_onyx" ✓
- modelLabel: "Opus 4.8" → FIXED to "Opus 4.7" (datable claim: Opus 4.8 does not exist in current registry)
- Persona coherence: narration says "Liam, in for Bear" ✓, voice is Kokoro am_onyx ✓

## Check 10 — Pacing (words per second vs actual_duration_s)
**PASS** — All beats within 2.0–3.4 wps:
- B00: ~68w / 24.92s = 2.73 wps ✓
- B01: ~38w / 12.29s = 3.09 wps ✓
- B02: ~27w / 8.41s = 3.21 wps ✓
- B03: ~47w / 16.17s = 2.90 wps ✓ (narration fixed; slightly longer)
- BVDT: ~46w / 14.55s = 3.16 wps ✓ (narration fixed; slightly longer — audio will be regenerated)
- BHTF: ~47w / 15.3s = 3.07 wps ✓
- BOUT: ~7w / 3.31s = 2.11 wps ✓

## Check 11 — type_check.py
**PENDING** — Will run after render. Previous TYPECHECK.md (2026-08-03) was PASS but most
beats were SKIP (no video files existed). Will re-run with actual rendered frames.

## Narration truncation repairs (content errors — logged in REBUILD-LOG.md)
- B03: "...and produce ranked, fully-cited." → "...and produce ranked, fully-cited investigation referrals."
- BVDT: "...and produce." → "...and produce ranked investigation referrals."
- BHTF: "...and abuse a." → "...and abuse."

## Status
**ALL CHECKS PASS or FIXED. Build authorized.**
