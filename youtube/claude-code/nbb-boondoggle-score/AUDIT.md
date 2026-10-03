# AUDIT.md — nbb-boondoggle-score (2026-08-31)

Reel: `books/anthropics/youtube/claude-code/nbb-boondoggle-score`
Cut: `boondoggle-score.mp4` (140.0s, 13/13 filled, no slates)

## PHASE 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json` present (2026-08-31 10:32). Narration LOCKED verbatim.
- No datable-claim edits made this pass. Envelope already normalized to Kokoro `am_onyx`.

## PHASE 1 — Checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 older than beat_sheet remains after re-render. |
| 2 | Bookends | PASS | NBB00 ClaudeComposerAsk, NBB01 ClaudeVerdictArtifact, NBB02 ClaudeComposerAsk (Your Turn), NBB03 ClaudeTitleOutro. Note: reel uses nbb-canonical NBB00–NBB03; BVDT/BHTF/BOUT legitimately absent per notes.bookends_stripped. |
| 3 | Spark lines | FIXED | NBB00 greeting "Yassou, Liam" (Greek). NBB02 (Your-Turn) greeting "Score your plan." (≤4 words compressed from narration). |
| 4 | Verdict | PASS | NBB01 artifactLines carry three reel-specific claims from body (validator flags, diagnostic before code, three-pass verification). No placeholder, no template, not boilerplate. Body ≥5 beats, ≥180 words — verdict authored. |
| 5c | Your-Turn placeholder | PASS | NBB02 command is real exercise ("write the handoff condition as a machine-checkable assertion — a pytest file, a count, or an artifact") — no `[...]` template bracket. |
| 5b | Chart text | FIXED | B04 axis+bar labels are short category nouns (Phase, Labor, Capacity, Handoff Condition). Row 3 highlighted crimson+pink with `!` marker at left margin and inline "HIGH RISK" language dropped in favor of visual signal + narration. Critical-path caption is one complete short sentence. |
| 5 | Card text | PASS | B01 FormBCard items real subs (`pytest tests/test_x.py exits 0`, `3 apps survive reload`, `screenshot matches wireframe.png`). No placeholder, no clipped label. |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero STILL-src=archive. B04/B06/B07/B08 Manim; B00–B05 Remotion cards / composers / code-blocks. |
| 7 | Card-only | PASS | B04, B06, B07, B08 draw with Manim. |
| 8 | Lens audit | PASS | Popper: B01 states falsification rule ("assertion that exits zero or doesn't") in advance. Plato: B02–B05 name artifact (score table) vs world (build risk) vs relationship (which row every other inherits from), with B05 explicitly testing the artifact–world gap by feeding an invalid handoff condition and reading validator response. Two moves earned. |
| 9 | Brand fields | PASS | folderLabel `@NikBearBrown` (channel handle). engine kokoro / voice am_onyx — matches actual audio. Narration voiced by Liam; no "in for Bear" claim. |
| 10 | Pacing | PASS | Body beats compute at 1.9–2.9 wps against measured durations. NBB00 cold-open sits at 3.4 wps for a dense recap ask — within tolerance. |
| 11 | type_check.py | PASS | GATE T PASS after B04 render at 4K + font_size bump. TYPECHECK.md written 2026-08-31T12:41. |

## PHASE 1 — Fixes applied (this pass)

- `NBB00.props.segment`: `"Score a Build Plan Using the"` (§8.9 truncation) → `"BOONDOGGLE SCORE"`.
- `NBB02.props.segment`: same fix.
- `scenes_std.py` B07/B08: rewrote to remove on-screen "[...]" mid-sentence truncation markers that had been shipping in the previous render. New copy is short, EB Garamond, no scaling artifacts.
- `vox_scenes.py` B04_BoondoggleTable:
  - Shortened handoff strings to fit column (`test_models.py exits 0`, `3 apps survive reload`, `screenshot vs wireframe`, `n/a` replacing em-dash).
  - Widened column spacing; removed thin non-risk row strokes.
  - Replaced HIGH-RISK pill (was overflowing row and clipping "in browser") with `!` marker at row-left + pink row + crimson text.
  - Critical-path caption shortened + moved to y=−2.75 so it clears row 5.
  - Font switched from Prism → EB Garamond for kerning/blob compliance.
  - Font sizes bumped (title 24→28, headers 22→28, row data 22→28, HIGH-RISK removed, critical 20→23).
  - Row animations batched into one FadeIn per row so mid-frame lands on a fully-drawn hold.
  - Rendered at 4K (`manim -qk`) so §8.1 fragment filter correctly discards sub-glyph strokes.

## PHASE 2 — Build

Slate cut (all beats real, no slates):

| beat | slot | fill |
|---|---|---|
| NBB00 | VIDEO | remotion ClaudeComposerAsk |
| B00 | VIDEO | remotion NikBearBrownOpen (cached) |
| B01 | VIDEO | remotion FormBCard (cached) |
| B02 | VIDEO | remotion NikBearBrownTerminalAsk (cached) |
| B03 | VIDEO | remotion NikBearBrownCodeBlock (cached) |
| B04 | MANIM | B04_BoondoggleTable (re-rendered, 4K) |
| B05 | VIDEO | remotion NikBearBrownTerminalAsk (cached) |
| B06 | MANIM | B06_InvalidHandoff (cached) |
| B07 | MANIM | Scene_B07_NbbBoondoggleScore (re-rendered) |
| B08 | MANIM | Scene_B08_NbbBoondoggleScore (re-rendered) |
| NBB01 | VIDEO | remotion ClaudeVerdictArtifact |
| NBB02 | VIDEO | remotion ClaudeComposerAsk |
| NBB03 | VIDEO | remotion ClaudeTitleOutro |

- **GATE AUDIO**: PASS, mean_volume −23.9 dB.
- **GATE T**: PASS (no §8.1/§8.2/§8.3/§8.4/§8.5/§8.7/§8.9 FAILs).
- **build.status Counter**: `Counter({'VIDEO': 9, 'MANIM': 4})`.
- **Master mtime > sheet mtime**: mp4 2026-08-31 12:41:47, sheet 2026-08-31 12:07:35. STAle check: cut is NEWER.

## Advisory (not blocking)

- Compile logged: `'fade' motion carries 9/13 beats (69%) — over ~40% pantry cap`. Legacy vox motion allocation; not a Gate T concern for this pass.

Not blocked. Not published. Human review pending.
