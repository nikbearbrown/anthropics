# AUDIT — cancer-nanomedicine-ch04-targeting-epr (2026-08-31)

**Format:** HTML lecture deck (12 segments S01–S12 · `deck.html` → `slides/*.png`
→ per-segment audio → concat mp4). NOT a claude-liam Remotion beat sheet — most
PHASE 1 checks (bookends, ClaudeComposerAsk, ClaudeVerdictArtifact, spark lines,
Your-Turn, chart-text audit, punt sweep, card-only test, computational-skepticism
lens) do not apply and are marked N/A below.

**Voice:** ElevenLabs `TyW6NH39JcFb5M3xdIIk` (Bear's own clone). Legitimate paid
default for the @NikBearBrown channel per AGENTS.md — not a migration debt.
Existing audio is EL Bear voice from Jul 11, kept. `voice_id` intentionally kept
in the envelope for the same reason ch01–ch03 and ch05 kept it in earlier
filmloop passes.

**Series precedent:** ch01, ch02, ch03, ch05 of this same lecture course were
built by the factory as lecture-deck review cuts via `runtime/scripts/render.py`
(see `FILMLOOP-LOG.md`). Same pipeline applied here.

## PHASE 0 — REBUILD CONTRACT

- `beat_sheet.pre-rebuild.json` created byte-exact of `beat_sheet.json`
  (sha1 `c712fd87532dd857c60b93f5a35539fcd39ca648`).
- No narration edits made. Sheet locked.
- All 12 `actual_duration_s` values already present and match ffprobe to 0.01 s:
  S01 30.51 · S02 43.05 · S03 43.28 · S04 42.49 · S05 51.13 · S06 52.90 ·
  S07 52.71 · S08 50.11 · S09 50.20 · S10 57.21 · S11 52.85 · S12 33.11
  (total narration 559.55 s ≈ 9.33 min).

## PHASE 1 — audit

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists in folder. Nothing to purge. |
| 2 | Bookends B00/BVDT/BHTF/BOUT | N/A | Lecture-deck format has no bookend beats. |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats. |
| 4 | Verdict card | N/A | No ClaudeVerdictArtifact beat. S12 CLOSE segment carries the summary ("Know where each mechanism acts. Then measure — don't assume."). |
| 5c | Your-Turn placeholder | N/A | No BHTF beat. |
| 5b | Chart text | N/A | No Manim/D3 charts — rendered HTML slides only. |
| 5 | Card sub/label | N/A | No FormA/FormB card beats. |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled slates — every slide is a rendered HTML deck page. |
| 7 | Card-only reel | N/A | Lecture-deck format is HTML slides by design (not a claude-liam card fallback). |
| 8 | Lens audit | N/A | Cancer-nanomedicine domain lecture (EPR / protein corona / active ligands), not a computational-skepticism reel. |
| 9 | Brand fields | PASS | No `folderLabel` field in this schema. Metadata `title/slug/playlist/hashtags` all @NikBearBrown-consistent. Voice = EL Bear clone, correct paid default for the channel. |
| 10 | Pacing (2.0–3.4 wps) | PASS (S09 logged) | 11/12 segments 2.11–2.85 wps. S09 (THE FOLATE CASE — EC145 vs mirvetuximab soravtansine, 99 words / 50.20 s = 1.97 wps) sits 0.03 wps below the floor — deliberate slow-read on the segment carrying two long clinical drug names side-by-side. Same pattern as ch05 S06. Not retimed. |
| 11 | `type_check.py` | PASS | GATE T: PASS (no per-beat kerning surface — HTML deck). |

## Assets

- 12/12 segments have `audio/S**.mp3` (ElevenLabs Bear, Jul 11).
- 12/12 segments have `slides/S**.png` (Jul 11 — stale vs `deck.html` mtime
  Jul 15 but `render.py` re-screenshots each slide before concat, so re-render
  will pick up any `deck.html` changes automatically).
- `deck.html` last edit Jul 15 14:54 (post-anim / post-idea passes present).
- Total measured narration: 559.55 s ≈ 9.33 min (audio-first clock respected).

## Decision

Proceed to PHASE 2 (render via `runtime/scripts/render.py`, the pipeline this
reel was authored for). Deliverable is a review cut with real audio and
re-screenshot slides. Named `cancer-nanomedicine-ch04-targeting-epr.mp4`
(no `-slate` suffix — every slide is a real screenshot, not a placeholder card).
