# Batch Status — Playlist Intro Reels
Voice switched: Liam/Kokoro (free) — resuming build
Updated: 2026-07-24 — switched Bear/ElevenLabs → Liam/Kokoro (am_onyx); all 10 beat_sheets updated
TTS characters used: 0 (starting fresh with Kokoro — no quota, no spend gate)

## STATUS: COMPLETE — all 50 empty beats filled (2026-07-24)

| Playlist | Slug | Beats | Slates | Status | Notes |
|---|---|---|---|---|---|
| claude-basics | what-is-claude-basics | 8 | 0 | PASS | 87.6s · 8/8 filled · Manim+Remotion |
| claude-prompting | what-is-claude-prompting | 8 | 0 | PASS | 86.1s · 8/8 filled · Manim+Remotion |
| claude-agent-skills | what-is-claude-agent-skills | 8 | 0 | PASS | 84.9s · 8/8 filled · Manim+Remotion |
| claude-skills | what-is-claude-skills | 8 | 0 | PASS | 88.5s · 8/8 filled · Manim+Remotion |
| claude-plugins | what-is-claude-plugins | 8 | 0 | PASS | 82.6s · 8/8 filled · Manim+Remotion |
| claude-mcp-connectors | what-is-claude-mcp-connectors | 8 | 0 | PASS | 100.0s · 8/8 filled · Manim+Remotion |
| claude-research | what-is-claude-research | 8 | 0 | PASS | 89.8s · 8/8 filled · Manim+Remotion |
| behind-the-model | what-is-behind-the-model | 8 | 0 | PASS | 84.3s · 8/8 filled · Manim+Remotion |
| claude-for-education | what-is-claude-for-education | 8 | 0 | PASS | 89.2s · 8/8 filled · Manim+Remotion |
| claude-youtube | what-is-claude-youtube | 8 | 0 | PASS | 84.1s · 8/8 filled · Manim+Remotion |

## Fill strategy (50 beats across 10 reels)
- B01: Manim scene (wrong-model diagram) — 10 unique scenes, one per reel
- B02: Manim scene (right-model diagram) — 10 unique scenes, one per reel
- B03: Remotion ChipGrid — playlist overview chips + sparkLine
- B04: Manim scene (do-this-now diagram) — 10 unique scenes, one per reel
- B05: Remotion ClaudeWindow (artifact view) — verdict card
- All 30 Manim renders: 4K (3840x2160), 24fps, cream/ink/terracotta palette
- All 20 Remotion renders: extended to match actual audio duration

## DECISION FOR BEAR (morning)
claude-skills vs claude-agent-skills scope collision:
- claude-agent-skills reel: WRITING your own skills — "when does a folder of instructions beat a better prompt?"
- claude-skills reel: JUDGING and USING skills someone else wrote — "how do I judge a skill before I trust it?"
Differentiation is baked into the B05 narration of what-is-claude-skills. If Bear disagrees with
this split, what-is-claude-skills is the reel to rebuild.

## What's complete
- LENS-NOTES.md — written (four moves, fluency trap, Ash case, asymmetry, discrepancy flag)
- 10 x beat_sheet.json — written and voice_id fields verified
- 10 x PEDAGOGY.md — written (VERDICT: PASS in all)
- 10 x SOURCES.md — written
- 10 x BUILD-LOG.md — written (GATE P recorded)
- 10 x NARRATION.md — written

## Final summary — 2026-07-24 beat-fill complete
- TTS characters generated: 0 (Kokoro is local, no API calls; audio untouched)
- Slates per reel: 0 (all 50 filled)
- Manim renders: 30 (B01+B02+B04 x 10 reels), 4K/24fps, cream/ink/terracotta
- Remotion renders: 20 (B03 ChipGrid + B05 ClaudeWindow x 10 reels), audio-extended
- Remotion pre-existing: 30 (B00+B06+B07 x 10 reels, untouched)
- All 10 reels compiled: 8/8 filled, zero slate fallbacks used
- Zero Manim failures, zero Remotion failures
- QC frames sampled: confirmed no PIPELINE text, canvas filled, terracotta accent present

## Remaining work
None for visual fill. Reels are watch-ready.
Next gate: Bear watches, signs off, then `art final <reel>` for clean 4K masters before staging.
