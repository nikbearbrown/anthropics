# AUDIT — cancer-nanomedicine-ch08-theranostic-nanoparticles (2026-08-31)

**Format:** HTML lecture deck (12 segments S01–S12 · deck.html → slides/*.png →
per-segment audio → concat mp4). NOT a claude-liam Remotion beat sheet — most
PHASE 1 checks (bookends, ClaudeComposerAsk, ClaudeVerdictArtifact, spark lines,
Your-Turn, chart-text audit, punt sweep, card-only test) do not apply and are
marked N/A below.

**Voice:** ElevenLabs `TyW6NH39JcFb5M3xdIIk` (Bear's own clone). This is the
legitimate paid default for the @NikBearBrown channel per AGENTS.md — not a
migration debt. Existing audio is EL Bear voice from Jul 12, kept.

## PHASE 0 — REBUILD CONTRACT

- `beat_sheet.pre-rebuild.json` created (byte-exact of `beat_sheet.json`, sha1 `39a50c89…`).
- No narration edits made. Sheet locked.

## PHASE 1 — audit

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists yet. Nothing to purge. |
| 2 | Bookends B00/BVDT/BHTF/BOUT | N/A | Lecture-deck format has no bookend beats. |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats. |
| 4 | Verdict card | N/A | No ClaudeVerdictArtifact beat. |
| 5c | Your-Turn placeholder | N/A | No BHTF beat. |
| 5b | Chart text | N/A | No Manim/D3 charts — rendered HTML slides only. |
| 5 | Card sub/label | N/A | No FormA/FormB card beats. |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled slates — every slide is a rendered HTML deck page. |
| 7 | Card-only reel | N/A | Lecture-deck format is HTML slides by design (not a claude-liam card fallback). |
| 8 | Lens audit | N/A | Cancer-nanomedicine domain lecture, not a computational-skepticism reel. |
| 9 | Brand fields | PASS | No `folderLabel` field in this schema. Metadata `title/slug/playlist/hashtags` all @NikBearBrown-consistent. |
| 10 | Pacing (2.0–3.4 wps) | INFO | S02 1.93 wps and S07 1.95 wps sit just below the floor — measured from Bear's own EL read, whose cadence is slower than Kokoro's. Rest 2.03–2.70. Not retimed. |
| 11 | type_check.py | PASS | GATE T: PASS (no per-beat kerning surface — HTML deck). |

## Assets

- 12/12 segments have `audio/S**.mp3` (ElevenLabs Bear, Jul 12).
- 12/12 segments have `slides/S**.png` (Jul 11 — stale vs deck.html but `render.py` re-screenshots each slide before concat, so re-render picks up any deck.html changes automatically).
- `deck.html` last edit Jul 15 (post-anim / post-idea passes present).
- Total measured narration: 477.7 s ≈ 8.0 min (audio-first clock respected).

## Decision

Proceed to PHASE 2 (render via `runtime/scripts/render.py`, the pipeline this
reel was authored for). The deliverable is a review cut with real audio and
re-screenshot slides.
