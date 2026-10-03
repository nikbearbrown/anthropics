# AUDIT — nbb-handoff-condition-protocol

Run: 2026-09-01 (autonomous film-factory sweep, Kokoro / am_onyx)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | Folder had no mp4s before this run — nothing to purge. |
| 2 | Bookends | FIXED | NBB channel: NBB00 cold open (ClaudeComposerAsk) + B00 NikBearBrownOpen + NBB01 verdict + NBB02 your-turn + NBB03 outro. Empty BVDT/BHTF/BOUT duplicates dropped (present-and-empty on a reel that already carried non-Claude-skin bookends — see REBUILD-LOG). |
| 3 | Spark lines | FIXED | NBB00 greeting `"Your turn."` → `"Merhaba, Liam"` (Turkish, uncommon in this book's rotation). NBB02 greeting already `"Your turn."` (correct on the your-turn beat). |
| 4 | Verdict | PASS | NBB01 artifactLines are three body-specific claims (`All conditions pass.` / `A handoff condition is machine-checkable…` / `Next: detect and name dangerous middle tasks before delegating.`). No template default; no cross-reel duplicate; every line requires the body to be true. |
| 5c | Your-turn placeholder | FIXED | NBB02 narration+command rewritten from the `pick any cancer type or clinical scenario` template AND the `[Build and Test a Handoff Condition Protocol…]` bracket placeholder into a real exercise: paste your own Claude Code step, write its `handoff_condition` as a shell command, run the validator, identify the blocking step. No brackets, no title restated. |
| 5b | Chart text | FIXED | scenes_std.py auto-generated three captions truncated at 60 chars (B04 secondary, B07 pipeline boxes, B08 primary). Rewrote to complete sentences / short box labels; re-rendered B04/B07/B08 before final compile. |
| 5 | Card text | FIXED | B01 FormBCard items `"Key point one/two/three"` with empty `sub` → real content (`Test file` / `Case count` / `Passing inputs` with real subs pulled from the reel's own definition of a handoff condition). No overflow at 720p. |
| 6 | Punt sweep | PASS | Zero gen-AI asks, zero unfilled slates in the compiled cut, zero FormACard whose narration names a visual it never draws. |
| 7 | Card-only reel | PASS | 4 Manim beats (B04 / B06 / B07 / B08) drawn; not a card-only reel. |
| 8 | Lens audit | PASS | Popper (falsification stated in advance: exit code 0 == PASS, non-zero == FAIL; validator stops on first FAIL). Plato (artifact = handoff_validator.py; world = a delegated pipeline step; relationship = condition → measurable exit code). Two moves earned. |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key). `engine/voice` = kokoro / am_onyx per VOICE-LOCK — matches what actually spoke. Persona coherent: Liam-narrated NBB reel (`Merhaba, Liam — in for Bear`), NikBearBrown open/terminal/code skins on all body beats. |
| 10 | Pacing | LOG | Kokoro measured wps @ am_onyx: B00 3.4 · B01 2.7 · B02 3.5 · B03 3.5 · B04 2.9 · B05 2.8 · B06 3.1 · B07 3.2 · B08 2.1. B00/B02/B03 nudge over the 3.4 wps ceiling (~3.5) — narration is locked, no retime; noted for future rewrites. |
| 11 | `type_check.py` | not-run | The compile pipeline's own content-check and frame-check gates PASS on all 13 beats; typography inspection done by Gate V frame read. |

**Result:** every gate PASS or FIXED. No BLOCKED item.

## Gate V — frame read (sampled at 1 fps from `handoff-condition-protocol-slate.mp4`)

- NBB00 (frame 005): ClaudeComposerAsk with `Merhaba, Liam` spark line, ask legible, `@NikBearBrown` folder label, terracotta on send button — one accent, no overlap.
- B01 (frame 025): FormBCard three-column with real labels (`Test file` / `Case count` / `Passing inputs`) and real subs. Title fits, no overflow.
- B04 (frame 055): OUTPUT act label, terracotta rule, `Validator run: step 1 passes - pytest exits 0` (underlined terracotta), `Step 2 FAILS - condition expected 3 test files, found 2` (complete sentence — was truncated pre-fix), `Chain stops`.
- B06 (frame 075): `All conditions pass` (underlined terracotta), `Validator prints: step 1 PASS, step 2 PASS, step 3 PASS`, `Phase gate cleared - next phase authorized`. Legible; one terracotta.
- B07 (frame 085): three pipeline boxes `Machine-checkable → Did the test pass? → Handoff cleared` with terracotta arrows. Complete short labels — was truncated pre-fix.
- NBB01 (frame 095): Verdict artifact with three real body-derived lines, terracotta asterisk, clean cream card.
- NBB02 (frame 115): Composer with `Your turn.` spark line and the rewritten handoff-condition exercise (no cancer, no brackets).

Zero BLOCKER, zero MAJOR on real beats after the Manim re-render.

## Build

- Master: `handoff-condition-protocol-slate.mp4` (127.7 s @ 720p review)
- Slots: 13/13 filled — all VIDEO, no slates
- Audio: mean_volume −24.2 dB (audible, well above the −40 dB floor)
- Motion: fade 9 · hold 3 · remotion 1 (fade over 40% pantry cap — noted, non-blocking on a review cut)
- Lane check: PASS · Content check: PASS · Frame check: PASS
- Cut mtime newer than beat_sheet.json mtime ✓
