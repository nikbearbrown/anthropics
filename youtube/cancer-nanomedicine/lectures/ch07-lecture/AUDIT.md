# AUDIT — cancer-nanomedicine-ch07-radioligand-theranostics (2026-08-31)

**Format:** HTML lecture deck (12 segments S01–S12 · `deck.html` → `slides/*.png`
→ per-segment ElevenLabs audio → concat mp4). NOT a claude-liam Remotion beat
sheet — most PHASE 1 checks (bookends, ClaudeComposerAsk / ClaudeVerdictArtifact,
spark lines, Your-Turn, chart-text audit, punt sweep on card structure,
card-only test, computational-skepticism lens) do not apply and are marked N/A
below. Same lecture-deck pipeline as sibling ch01–ch06 + ch08–ch12.

**Voice:** ElevenLabs `TyW6NH39JcFb5M3xdIIk` (Bear's own clone) — legitimate
paid default for @NikBearBrown per AGENTS.md; audio already generated Jul 11
(measured mean_volume −16.6 dB to −20.4 dB, all well above the −40 dB floor).
`voice_id` retained in envelope as in sibling reels.

## PHASE 0 — REBUILD CONTRACT

- `beat_sheet.pre-rebuild.json` created byte-exact from `beat_sheet.json`
  (sha1 `8a661ba7982446ff29f7a271aa2bae8303be3025`).
- No narration edits made. Sheet locked.
- No metadata write-back needed — all 12 segments already carry measured
  `actual_duration_s` from the Jul 11 audio run (verified against ffprobe).

## PHASE 1 — audit

| # | Check | Result | Note |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists in folder. Nothing to purge. |
| 2 | Bookends B00/BVDT/BHTF/BOUT | N/A | Lecture-deck format has no bookend beats. |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats. |
| 4 | Verdict card | N/A | No ClaudeVerdictArtifact beat. S11 THESIS + S12 CLOSE segments carry the thesis and recap. |
| 5c | Your-Turn placeholder | N/A | No BHTF beat. |
| 5b | Chart text | N/A | No Manim/D3 charts — rendered HTML slides only. |
| 5 | Card sub/label | N/A | No FormA/FormB card beats. |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled slates — every slide is a rendered HTML deck page. |
| 7 | Card-only reel | N/A | Lecture-deck format is HTML slides by design (not a claude-liam card fallback). |
| 8 | Lens audit | N/A | Domain lecture (cancer-nanomedicine), not a computational-skepticism reel. Chapter itself runs a Descartes-lite move (S01 opening — PSMA-negative patient would have been harmed had they skipped the scan; falsifiability made concrete) and a Popper-lite move (S11 THESIS — two named findings that would force revision: PSMA-negative comparable survival; alpha-outperforming-beta in heterogeneous tumors). |
| 9 | Brand fields | PASS | No `folderLabel` field in this schema. Metadata `title/slug/playlist/hashtags` all @NikBearBrown-consistent. Voice = EL Bear clone, correct paid default. |
| 10 | Pacing (2.0–3.4 wps) | LOG | Eight of twelve segments in range; four under floor: S03 1.88 · S04 1.77 · S10 1.99 · S11 2.01. All four are mechanism-dense (radioisotope pharmacology of the DOTATATE pair, translation-gap argument, chapter thesis) and read slow on purpose — same pattern documented on sibling ch06 (which had S03 2.02 / S04 2.05). No retiming. |
| 11 | `type_check.py` | N/A | GATE T applies to per-beat Remotion kerning — not applicable to HTML deck slides. |

## Assets

- 12/12 segments have `audio/S**.mp3` (ElevenLabs Bear, Jul 11).
- 12/12 segments have `slides/S**.png` (Jul 11) — stale vs `deck.html` mtime
  Jul 15 but `render.py` re-screenshots each slide before concat, so re-render
  picks up any post-Jul-11 deck changes automatically.
- `deck.html` last edit Jul 15 14:54 (post-anim / post-idea passes present).
- Total measured narration: 534.9 s ≈ 8.9 min (audio-first clock respected).

## Decision

Proceed to PHASE 2 (render via `runtime/scripts/render.py`, the pipeline this
reel was authored for). Deliverable is a review cut with real audio and
re-screenshot slides. Named `cancer-nanomedicine-ch07-radioligand-theranostics.mp4`
(no `-slate` suffix — every slide is a real screenshot, not a placeholder card).
