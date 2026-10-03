# AUDIT — claude-liam-vox-protein-corona
Reviewed 2026-08-30. Slate cut deliverable.

| # | Check | Status |
|---|-------|--------|
| 1 | Stale renders | PASS — no mp4 in reel folder (fresh build) |
| 2 | Bookends B00 / BVDT / BHTF / BOUT present + canonical patterns | PASS |
| 3 | Spark lines | FIXED — B00 greeting was "Liam" (lone-asterisk); now "Namaste, Liam" + 3-line output. BHTF greeting already "Your turn." + authored output. No inner ClaudeComposerAsk beats. |
| 4 | Verdict (BVDT) | FIXED (AUTHORED) — body is 11 beats / ~430 words → verdict authored from body nouns (corona-in-seconds, opsonins, folate/culture-vs-blood). Narration also authored. |
| 5 | Card text — FormA/FormB placeholder subs | FIXED — B01 FormBCard had "Key point one/two/three" with empty subs → real labels + subs from body. |
| 5b | Chart text | N/A — no Manim/D3 chart beat text edited in this pass. |
| 5c | Your-Turn placeholder | FIXED — BHTF was template "Take what you learned from [...]". Now real exercise: name the plasma proteins landing first, ask which mask/flag, design the plasma experiment that would refute the culture-medium result. |
| 6 | Punt sweep (bookends included) | PASS — no gen-AI asks in bookends; body B02, B03, B08, B11 are declared slate cards for review cut (per PHASE 2 review-slate format). |
| 7 | Card-only reel | PASS — body draws Manim graphics for B04–B10 (corona-forms, ligand-masked, opsonins, two-environments, folate-example, corona-summary) — not a card-only reel. |
| 8 | Lens audit (2 moves min.) | PASS — Descartes: B08 "what would refute" checklist; Popper: B08 "any strategy validated only in protein-free culture is incomplete… test in full plasma before drawing any conclusions" + BHTF asks the viewer to state, in advance, the plasma experiment; Plato: B02/B07 name the culture-artifact vs blood-world distinction and interrogate the relationship; Hume: B09 (implicit) — culture-medium confidence is a property of the medium, not the body. |
| 9 | Brand fields | PASS — folderLabel `@NikBearBrown` (channel handle, not brand key); engine `kokoro` + voice `am_onyx` matches Liam persona ("This is Liam, in for Bear"). |
| 10 | Pacing (2.0–3.4 wps) | INFO — body mp3s already measured; will be reconformed to actuals on compile. |
| 11 | type_check.py | PASS (GATE T PASS after B01 title de-wordified from 13 → 9 words; §8.5 wordy-card cleared; only advisory §8.10 remains — B03 narration overlap with card text, no exit effect). |

## PHASE 0 rebuild contract
- `beat_sheet.pre-rebuild.json` created before any edit.
- Narration locked except spark line + verdict + your-turn (all logged in REBUILD-LOG.md).
- VOICE-LOCK envelope normalized: dead `voice_id` dropped, `clock` rewritten.

## Ready to build (slate cut)
BVDT and BHTF gained real narration → need fresh Kokoro mp3s. All other B01–B13 audio
is measured and stays. Then compile a slate cut.
