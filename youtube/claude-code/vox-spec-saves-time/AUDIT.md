# AUDIT.md — vox-spec-saves-time

Checked: 2026-08-31 by nopunt filmloop.

## Phase 1 audit

| # | Check | Result | Note |
|---|-------|--------|------|
| 1 | Stale renders | PASS | No mp4s in reel folder — nothing to delete. |
| 2 | Bookends present | FIXED | B00 / BVDT / BHTF / BOUT all present with canonical patterns. B07 previously carried a duplicate ClaudeTitleOutro on top of its Manim comparison graphic and an errant `act: OUTRO` — both removed; B07 is now GRAPHIC only. |
| 3 | Spark lines | FIXED | B00 `props.greeting` was persona-only ("Liam") — updated to `"Jambo, Liam"` (world-language hello, Swahili — not used by any adjacent claude-code reel). BHTF greeting already `"Your turn."` ✓. YOURTURN inner composer already carries a 2-word spark ("Your turn.") ≤4-word rule ✓. |
| 4 | Verdict | FIXED (AUTHOR) | Body = 11 beats / ~597 words → real verdict authored. Old lines were pure template default (`Key finding one/two/three`). New artifactLines drawn from body's own nouns/numbers: 8 words → 45 min; 90 words → 12 min; the five cells reclaim the four decisions. BVDT narration rewritten to DISCUSS the card (§8.10 score dropped 0.86 → 0.24). |
| 5c | Your-Turn placeholder | FIXED (AUTHOR) | BHTF command was the "Take what you learned from [ ... ] and apply it to your own work" placeholder (with brackets). Rewritten as a real exercise using the video's own five-cell method. `output: []` filled with 3 real next-step lines. BHTF narration authored (was empty) to speak the exercise aloud. |
| 5b | Chart text | PASS | No axis/bar labels in the sheet contain narration fragments; production_viz labels are short and category-shaped. No "ACT I" style labels. |
| 5 | Card text | PASS | B03 FormA copy is the beat's narration string (no `sub` placeholder). B04 / B11 cards use short copy. |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled fill_slates/remotion_scenes, zero DoodleScene/DoodleChart. B03 is a FormA text card mapped to its content (design-v1 explicitly downgraded from AI still → FormA). Every other body beat is Manim GRAPHIC. |
| 7 | Card-only reel | PASS | 7 of 11 body beats render as Manim GRAPHIC (B02, B05, B06, B08, B09, B10, plus B07 after fix). |
| 8 | Lens audit | PASS | Reel runs Popper explicitly (predicts the 90-second cost, then produces the falsifying case where 8 words = 45 minutes — B04 "More words, less time. Why?" and B08 timeline comparison are the falsification move). Runs Plato's move by holding artifact (the delivered page) apart from world (school server that blocks the CDN, B02/B09) — the eight-word request's success as an *artifact* and its failure in the *world* are named separately. Two moves earned. |
| 9 | Brand fields | PASS | folderLabel `@NikBearBrown` on every composer ✓. metadata engine=kokoro, voice=am_onyx — matches the audio that will be generated. No "Liam, in for Bear" narration line (B00 narration is empty), so no persona/voice coherence conflict. |
| 10 | Pacing | LOG | B08 narration: 60 words / 16.02s = **3.75 wps** — above the 3.4 ceiling. Not silently retimed; noted here per the instruction. Every other beat sits between 2.7 and 3.3 wps. |
| 11 | type_check.py | PASS | GATE T PASS, 0 FAILs. Two §8.6 golden-string overflow risks on YOURTURN + BOUT headline (76 chars) noted as risk, not blocker. §8.10 advisory on BVDT resolved by narration rewrite. |

## Rebuild-contract compliance (Phase 0)

- `beat_sheet.pre-rebuild.json` created byte-exact from the incoming sheet.
- Narration edits restricted to bookends previously carrying empty or placeholder strings (BVDT, BHTF); no inner-beat narration touched.
- Envelope: VOICE-LOCK was already correct (metadata.engine=kokoro, voice=am_onyx; each bookend carries `voice`, `engine`, `voice_kokoro`). No dead ElevenLabs fields present to drop.
- All edits logged in `REBUILD-LOG.md`.

## Result

**BLOCKED?** No.  Proceeding to Phase 2 build.
