# AUDIT — claude-liam-spec-prompt-audit

Date: 2026-08-31
Auditor: filmloop unattended run
Backup: `beat_sheet.pre-rebuild.json` (byte-exact copy, made before edits)

## Phase 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No `.mp4` files in reel folder — nothing to purge. |
| 2 | Bookends present | FIXED | B00 was `NikBearBrownOpen`; converted to `ClaudeComposerAsk` per COLD OPEN LAW (palette=claude). BVDT / BHTF / BOUT present with canonical patterns. |
| 3 | Spark lines | FIXED | B00 given world-language greeting `Sawubona, Liam` (not repeated by adjacent claude-liam-* reels). BHTF greeting `Your turn.` (canonical). YOURTURN greeting changed from `Your turn.` to arc-cue `Try this,` so it does not duplicate BHTF. B02 / B05 use `NikBearBrownTerminalAsk` (no greeting field in schema — dropped stale `"The ask,"` prop). |
| 4 | Verdict | AUTHORED | Body has 9 body-beats and ~285 words (well above 5-beats / 180-words threshold). Real verdict authored: 4 artifactLines from the body's own nouns and numbers (pandas / openpyxl / 42 lines / csv.reader / stdlib / pytest exit 0 / InstallError). Real narration (~60 words) written for BVDT — replaces empty `""`. Placeholder `Key finding one/two/three` removed. |
| 5b | Chart text | N/A | No Manim/D3 chart beats in this reel. |
| 5c | Your-Turn placeholder | FIXED | BHTF pre-rebuild command was the seeded template `"Take what you learned from [Build and Audit a Specification Prompt with Claude Code]..."` — the exact 3,472-sheet placeholder pattern. Rewrote the command as a real exercise (rewrite one weekly loose prompt as a specification; run both against Claude Code; diff the code; count retries; fewer retries wins). Wrote 3 real steps in `output` (was `[]`). Wrote real BHTF narration (was `""`). No square brackets, no title restated. |
| 5 | Card text | FIXED | B01 / B04 / B06 FormBCard items had labels that recited the narration verbatim (would clip mid-word) and subs that duplicated the labels. Rewritten: labels are 2–4 word chunks; subs are one-sentence real explanations from the beat's own narration. B08 single-item FormBCard collapsed to FormACard (one-item FormB looks starved). B07 was ClaudeTitleOutro slate duplicating BOUT; converted to FormACard with three lines that fit the narration. |
| 6 | Punt sweep | PASS | Zero gen-AI asks. Zero unfilled fill_slates / remotion_scenes slates in the sheet — every body beat carries a real Remotion pattern that renders directly from props. Zero DoodleScene / DoodleChart. Zero STILL src=archive for concepts. Zero FormA card naming a visual it never draws. Nopunt catalog: every beat routes to its correct row (claude-code / slide-a / slide-b / code). |
| 7 | Card-only reel | PASS | B03 draws real code (`NikBearBrownCodeBlock`); B02 / B05 draw real terminal `claude` invocations (`NikBearBrownTerminalAsk`). Not card-only. |
| 8 | Lens audit | PASS | Popper: reels declare falsification in advance — "run each prompt twice and check for functional equivalence" (B05/B06). Plato: the artifact–world distinction is the whole reel — the artifact is the code Claude writes; the world is the lab machine that must run it; the vague prompt's artifact (pandas import) fails the world (InstallError). Descartes implicit: "what would falsify 'both prompts produce equivalent code'" — the rerun test. Two moves cleanly present. |
| 9 | Brand fields | FIXED | `folderLabel: @NikBearBrown` (channel handle, not brand key) throughout composers. `engine: kokoro`, `voice_kokoro: am_onyx`, per-bookend `voice: am_onyx` — describes the audio that will be generated. Persona coherence: narration is Liam-in-for-Bear, voice is Kokoro am_onyx. |
| 10 | Pacing | PASS + 1 log | WPS on measured beats: B00 3.0 · B01 3.4 · B02 3.1 · B03 2.8 · B04 2.6 · B05 3.2 · B06 2.7 · B07 3.7 (marginally above 3.4) · B08 2.3. B07 flagged. Not silently retimed. New beats (BVDT/BHTF/YOURTURN) will be measured by Kokoro. |
| 11 | type_check.py | PASS | GATE T: PASS. 8 beats checked (bookends SKIP — no video), 0 FAILs. Two §8.10 advisories (B07/B08 narration recites card) — advisory, does not block cut. Not fixing: B07 and B08 are act-divider / next-teaser lines where "reading the card" is the point. |

All Phase 1 checks either PASS or FIXED. Proceeding to Phase 2 build.
