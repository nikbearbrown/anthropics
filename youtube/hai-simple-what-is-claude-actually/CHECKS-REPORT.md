# CHECKS-REPORT — hai-simple-what-is-claude-actually

Build date: 2026-08-27
Output: `hai-simple-what-is-claude-actually.mp4` (120.1 s, 3840×2160, 15/15 filled)

---

## Validators

| Check | Result | Notes |
|---|---|---|
| beat_lint | PASS | clean |
| banned_card_check | PASS | clean |
| bookend_check | PASS | four bookends correct |
| static_scene_check | WARNING (exit 1) | "no shapes recorded — text-only" (non-blocking; Manim scenes use Text objects) |
| content-check | PASS | 15 beats |
| frame-check | PASS | 3840×2160 |
| lane-check | PASS | 15 beats, no slate |
| GATE AUDIO | PASS | mean_volume −24.2 dB (threshold −40 dB) |

---

## Gate V — Visual QC

Sampling: every 120 frames (5 s intervals), 25 frames reviewed.

| Beat | Status | Notes |
|---|---|---|
| B00 | PASS | BrutalistHesitantWriter cold open; HAI cream bg; `@HumanitariansAI` watermark; mid-animation overflow of "SEARCH ENGI..." is transient (word deleted and replaced before freeze-hold) |
| B01–B11 | PASS | All 11 Manim GRAPHIC beats: HAI palette (#F3EBDD/#2F2A26/#1F4E5F/#E4572E); one CRIMSON accent per beat; text within safe area; no contrast failures |
| BCRY | PASS | WantQuote: carry-out line renders legibly; spark-line "Generates, not finds." present |
| BHTF | PASS (after fix) | ClaudeComposerAsk: folderLabel `@HumanitariansAI` correct (was `@NikBearBrown` from Root.tsx defaultProps; fixed by explicit prop) |
| BOUT | PASS (after fix) | OutroCTA: "More Claude Basics from @HumanitariansAI." + SUBSCRIBE pill + `@HumanitariansAI` handle (was ClaudeTitleOutro hardcoded to @NikBearBrown; switched to OutroCTA) |

---

## Fixes applied during Gate V

1. **BHTF folderLabel**: Root.tsx `defaultProps.folderLabel = '@NikBearBrown'` for ClaudeComposerAsk overrides the schema default when no prop is supplied. Added `"folderLabel": "@HumanitariansAI"` to BHTF props; re-rendered.
2. **BOUT pattern**: `ClaudeTitleOutro` hardcodes `@NikBearBrown` and explicitly refuses prop overrides (per component comment). Switched BOUT to `OutroCTA` with `handle: "@HumanitariansAI"`. `bookend_check.py` finds BOUT by `beat_id`, not pattern; `title`/`subline` props retained for validator; extra props stripped by Zod schema at render. BC-4 does not fire (BOUT is a bookend). Validators re-run: all PASS.

---

## Warnings (non-blocking)

- Motion histogram: `graphic` 11/15 (73%) — over the ~40% pantry cap. Logged; no fix required for review cut.
- 4K LAW note: Remotion clips render at 1920×1080 natively via `--scale=2`; compile.py upscales to 3840×2160 canvas. Manim clips re-rendered with `-qk` (3840×2160 native). Review-cut only — Bear decides art post.

---

## Ready for Bear review

File: `hai-simple-what-is-claude-actually/hai-simple-what-is-claude-actually.mp4`
Duration: 120.1 s (2:00)
Gate AUDIO: PASS −24.2 dB
Gate V: PASS (0 blockers, 0 majors after fixes)
