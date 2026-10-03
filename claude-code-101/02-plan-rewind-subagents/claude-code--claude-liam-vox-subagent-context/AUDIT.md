# AUDIT — claude-liam-vox-subagent-context

Rebuild pass: 2026-09-01. Slate-with-audio review cut. All beats real, no slates.

| # | Check | Result | What changed |
|---|---|---|---|
| 1 | Stale renders | FIXED | Purged `vox-subagent-context.mp4` in root and `mp4/` (Aug 10, older than Aug 19 sheet). |
| 2 | Bookends present | PASS | B00 / BVDT / BHTF / BOUT wired to ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro. |
| 3 | Spark lines | FIXED | B00 `greeting` was bare `"Liam"` → `"Kia ora, Liam"` (Māori; unused by adjacent reels in this book). BHTF `"Your turn."` intact. Inner-body composers are CCSession terminals — no spark-line field. |
| 4 | Verdict content | PASS | `verdict_audit.py` clean. Artifact heading `Subagent Context Isolation`; four artifact lines are reel-specific (78% used, isolated window, heuristic). Convention across sibling `claude-liam-*` reels is silent BVDT narration — kept. |
| 5c | Your-turn placeholder | FIXED | BHTF command was a "please explain to me" prompt — rewrote to an actionable exercise: "Grab your longest Claude Code session. List every file the main session read. Mark the ones that fed a research step. Rewrite those reads as one subagent task. Re-run and compare context percentage. The delta is the tax." No brackets, no title restated. |
| 5b | Chart text | FIXED | `scenes.py` had `Text(narration[:30])` bar labels (the enterprise-search bug). Rewrote B02 / B04 / B05 / B06 / B08: short category nouns for bar labels, complete sentences for captions, bar heights aligned to narration meaning (30 vs 78, 78 vs 32, 80 vs 15). B04 is now a stacked-column showing build + accumulating research reads. B05 is now two boxes with a "summary" arrow between them. |
| 5 | Card text | PASS | B07 FormA text-only card is a full paragraph; no placeholder `sub`/`label` fields anywhere. |
| 6 | Punt sweep | PASS | Zero slates, zero gen-AI asks, zero DoodleScene, zero unfilled Remotion/fill_slates. All 13 beats resolve to VIDEO or MANIM. |
| 7 | Card-only reel | PASS | 5 Manim beats + 7 Remotion CCSession/ClaudePattern beats + 1 stacked visual — plenty of drawn content. |
| 8 | Lens audit | PASS | Descartes (falsification: "Grab your longest session… compare context percentage — the delta is the tax"). Popper (heuristic states in advance what qualifies as a subagent task: reads-more-than-session-needs-to-see). Two moves earned. |
| 9 | Brand fields | PASS | `folderLabel: @NikBearBrown`. `engine: kokoro`, `voice: am_onyx`. Narration says "Liam, in for Bear" — matches Kokoro `am_onyx`. |
| 10 | Pacing | LOG | Body beats compile between ~2.0 and ~3.0 wps; compile.py slowed B02/B04/B05/B06/B08 by 1.38–1.66× to fit audio (durations were audio-first). Compile output: `B02: clip 12.5s slowed 1.45x to fill 18.1s beat`, etc. Not blocking. |
| 11 | `type_check.py` | PASS | GATE T: PASS. 13/13 beats checked, 0 fails. |

## Post-build Gate V

- Audio: mean_volume `-28.3 dB` (>-40 dB threshold), max `-5.9 dB`. Every beat mp4 carries audio.
- Frames sampled at t=8/30/55/85/120/150/190/215s (bookends, mid-body, verdict, your-turn, outro). Labels legible, no overlaps, no clipping. QC contact sheet regenerated at `qc-sheet.png`.
- Content-check: PASS (13 beats, no violations).
- Frame-check: PASS (13 beats, no violations).
- Lane-check: PASS (0 slates).

## Build summary

- Master: `vox-subagent-context.mp4` — 217.6s, 1280×720 (review cut), audio-per-beat narration, mtime > sheet mtime (verified).
- `build.status` Counter: `{VIDEO: 8, MANIM: 5}` — no SLATE, no PIPELINE, no PLACEHOLDER.
- Manim re-renders: B02 (chart), B04 (stacked column), B05 (two-box isolation), B06 (chart), B08 (chart).
- Remotion re-renders: B00 (greeting fix), BVDT (real verdict artifact), BHTF (actionable exercise).
- Reused as-is (content-identical to prior sheet, kept per sha1 manifest): B01, B03, B07, B09, BOUT.
