# AUDIT.md — five-supervisory-capacities (FILMLOOP 2026-09-01)

Reel: `anthropics/youtube/claude-code/five-supervisory-capacities`
Contract: FILMLOOP PHASE 1 checks (1–11).

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists in the reel folder or `clips/`; only PNG label placeholders in `clips/_work/`. Nothing to delete. |
| 2 | Bookends present | FIXED | B00 (NikBearBrownOpen — channel-appropriate NBB skin, not Claude-washed), BVDT, BHTF, BOUT all present. BOUT was missing `handle`; added `@NikBearBrown`. |
| 3 | Spark lines | FIXED | B02 greeting changed `"The ask,"` → `"Labels first,"` (beat-specific, 2 words); B05 greeting changed `"The ask,"` → `"Now, no labels,"` (3 words). Both compressed from the beat's own narration, not the topic. YOURTURN + BHTF greetings `"Your turn."` (canonical). B00 is a NikBearBrownOpen (uses `lines`), not a ClaudeComposerAsk, so the world-language spark does not apply here. |
| 4 | Verdict | FIXED (AUTHORED) | Body carries 7+ beats and >300 words → verdict authored. BVDT `artifactLines` rewritten with 3 real lines from body content (five moves; labeled vs unlabeled result; PF as the single delta). BVDT narration rewritten to speak that verdict. `verdict_audit.py --root .../claude-code` reports no violation. |
| 5c | Your-Turn placeholder | FIXED (AUTHORED) | BHTF command was the "Take what you learned from [ ... ] and apply it" template. Replaced with a real exercise from the reel's own artifact (walk the last Claude Code session, tag each prompt PF/PA/TO/IJ/EI, note the skipped moves and the failure each hides). BHTF `output` populated with the concrete rubric lines. |
| 5b | Chart text | N/A | No Manim or D3 chart in this reel. |
| 5 | Card text | FIXED | B01 FormBCard placeholder items ("Key point one/two/three", empty `sub`) replaced with 5 real capacities and 1-line subs each; icons drawn from `runtime/remotion/public/form-b-icons/`. B08 promoted from `source:null` to a FormACard with real content. |
| 6 | Punt sweep | FIXED | Punts authored: B04 (`source:null` → NikBearBrownCodeBlock, labeled-run output); B06 (`source:null` → NikBearBrownCodeBlock, unlabeled-run output); B08 (`source:null` → FormACard); B01 (placeholder card → real 5-item FormB). Zero gen-AI asks. Zero unfilled slates. No DoodleScene, no `STILL src=archive`, no card that names a visual it doesn't draw. |
| 7 | Card-only reel | PASS | Reel is now dominated by NikBearBrownCodeBlock terminals / code blocks and one FormB — not a card parade. |
| 8 | Lens audit | PASS | The reel enacts TWO moves against the source chapter: **Popper** (falsifiability — the labeled run *tries to break* the sort with an explicit tie case up front; the unlabeled run does not, and ships) and **Descartes** (radical doubt — the PA move produces a checklist item, the "tie case" probe, that would falsify the naive test set). The verdict and BHTF ask the viewer to run the same falsification test on their own transcript. |
| 9 | Brand fields | FIXED | `folderLabel: "@NikBearBrown"` in metadata and on each bookend (@NikBearBrown, not a brand key). Metadata `engine: kokoro` + `voice: am_onyx` matches the audio actually being generated. Persona coherence enforced: B00 says "This is Liam, in for Bear."; B07 signs off "Liam, in for Bear." — matches Kokoro `am_onyx` (IN-FOR-BEAR LAW). |
| 10 | Pacing | PASS | Word counts vs estimated_duration_s ratios (WPS): B00 32w/10s=3.2 ✓; B01 33w/12s=2.75 ✓; B02 17w/12s=1.4 ← LOG (below 2.0 — this beat is a slow, deliberate cold ask; a short terminal render is fine at this pace); B03 41w/14s=2.93 ✓; B04 57w/20s=2.85 ✓; B05 24w/10s=2.4 ✓; B06 51w/16s=3.19 ✓; YOURTURN 62w/18s=3.44 ← LOG (just above 3.4); B07 34w/14s=2.43 ✓; B08 8w/6s=1.33 ← LOG (short breather beat, acceptable); BVDT 33w/14s=2.36 ✓; BHTF 46w/14s=3.29 ✓; BOUT 11w/8s=1.38 ← LOG (short outro). Under Kokoro conform-to-audio, durations are output not input; measured mp3s will overwrite. |
| 11 | type_check | PASS | `runtime/scripts/type_check.py` → GATE T: PASS. Two §8.10 recite advisories (B08 next-step and BVDT verdict) — both are legitimate for their beat class (a next-step card SHOULD say the next step; a verdict SHOULD state the verdict). |

## Actionable summary
- 4 punts authored (B01, B04, B06, B08).
- Verdict + Your-Turn + BOUT narration authored from scratch (all three had empty narration; verdict + Your-Turn also had template placeholders).
- 2 spark lines de-genericized (B02, B05).
- IN-FOR-BEAR LAW applied to B00 + B07 (datable narration edits, logged).
- All gates green. Reel cleared for build.
