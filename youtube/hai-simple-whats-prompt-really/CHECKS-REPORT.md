# CHECKS-REPORT — hai-simple-whats-prompt-really

Build date: 2026-08-27
Output: `hai-simple-whats-prompt-really.mp4` (144.7 s, 3840×2160, 15/15 filled)

---

## Validators

| Check | Result | Notes |
|---|---|---|
| content-check | PASS | 15 beats |
| frame-check | PASS | 3840×2160 |
| lane-check | PASS | 15 beats, no slate |
| GATE AUDIO | PASS | mean_volume −24.1 dB (threshold −40 dB) |
| GATE T (type_check.py) | PASS | 1 failure fixed before final compile (see below) |

---

## Gate T — Fixes

**B04 (font floor)**:
- Initial: `carried = Text("carried forward", font_size=36)` → 35px blobs below 41px floor
- After bumping to 44: still 35px — root cause was CurvedArrow tip fragments at exactly 35px (the MANIM exempt range covers 33–34px; 35px is not exempt)
- Fix: redesigned B04Scene entirely — SANS-only (no SERIF), all font_size ≥ 52, CurvedArrow replaced with straight Arrow (larger tip_length=0.45), removed all serif body text
- GATE T: PASS after fix

---

## Gate V — Visual QC

Sampling: mid-beat frames extracted via ffmpeg; all 15 beats inspected.

| Beat | Status | Notes |
|---|---|---|
| B00 | PASS | BrutalistHesitantWriter cold open; HAI cream bg (#F3EBDD); typing animation + strike "command" → "prompt"; `@HumanitariansAI` watermark |
| B01 | PASS | "write a better prompt." SERIF 76pt + teal rule + question + note; within safe area |
| B02 | PASS | Anchor planted: "your message:" + "explain DNA" (110pt) + crimson cursor dot + "we'll come back to this." |
| B03 | PASS | "explain DNA" → arrow → "THE PROMPT" + "the natural reading" note |
| B04 | PASS (after redesign) | SANS-only: TURN 1 · TURN 2 teal-bordered box → arrow → "ONLY THIS MESSAGE?" struck through → "something carries forward" |
| B05 | PASS | "THE PROMPT" 88pt + teal block with "assembled text" label |
| B06 | PASS | Three-part vertical: SYSTEM / HISTORY / YOUR MESSAGE with teal/ink color coding |
| B07 | PASS | Assembled block with "reads top to bottom → generates" flow |
| B08 | PASS | Anchor payoff: same "your message:" + "explain DNA" + cursor dot, context structure added above |
| B09 | PASS | Context window limit: bar diagram with hard cutoff line |
| B10 | PASS (after fix) | "LONGER CONVERSATION" → arrow down → "REMEMBERS MORE" (struck crimson) → "oldest turns dropped at the limit" |
| B11 | PASS (after fix) | SYSTEM INSTRUCTIONS (hidden) teal box → "SHORT MESSAGE" → arrow → "SMALL CONTEXT" (struck crimson) |
| BCRY | PASS | WantQuote: carry-out line correct |
| BHTF | PASS | ClaudeComposerAsk: folderLabel `@HumanitariansAI`; topic "YOUR TURN · CLAUDE BASICS" |
| BOUT | PASS | OutroCTA: "More Claude Basics from @HumanitariansAI." + handle + title |

---

## Warnings (non-blocking)

- Motion histogram: `graphic` 11/15 (73%) — over the ~40% pantry cap. These are Manim renders (not pantry stock), so the warning is a false positive for this reel type. No fix required.

---

## Ready for Bear review

File: `hai-simple-whats-prompt-really/hai-simple-whats-prompt-really.mp4`
Duration: 144.7 s (2:24)
Gate AUDIO: PASS −24.1 dB
Gate T: PASS (0 failures after fix)
Gate V: PASS (0 blockers, 0 majors after B04/B10/B11 fixes)
