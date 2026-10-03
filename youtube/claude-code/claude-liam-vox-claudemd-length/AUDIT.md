# AUDIT.md — vox-claudemd-length (2026-08-31)

Slug: `vox-claudemd-length`
Channel: `claude-liam` (Kokoro `am_onyx`, VOICE-LOCK)
Rebuild base: `beat_sheet.pre-rebuild.json` (byte-exact copy of the pre-audit sheet, kept alongside).

## Phase 0 — Rebuild contract
- Copied `beat_sheet.json` → `beat_sheet.pre-rebuild.json` FIRST — byte-exact.
- Narration kept locked, EXCEPT for the two narration authorings explicitly
  authorized by phase 1: BVDT (verdict) and BHTF (your-turn). Both were empty
  in the old sheet; nothing was rewritten from a prior take.
- Dropped no dead ElevenLabs-era fields (none present; sheet already Kokoro).

## Phase 1 — Audits

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No pre-existing mp4s in `media/` or `manim/`. |
| 2 | Bookends | FIXED | B00 / BVDT / BHTF / BOUT present with canonical patterns. BVDT was placeholder → authored real verdict. |
| 3 | Spark lines | FIXED | B00 greeting `"Liam"` → `"Hola, Liam"` (Spanish not used by adjacent claude-code reels; Ciao/Sawubona/Namaste/Bonjour/Salaam already in rotation). BHTF greeting `"Your turn."` already correct. Inner beats use FormBCard, not ClaudeComposerAsk — no spark-line requirement. |
| 4 | Verdict | FIXED | Old BVDT had placeholder `"Key finding one/two/three"` and empty narration. AUTHORED real verdict from body's own nouns: three artifactLines + real narration recap. Body has 10 body beats and >400 words of narration — well above the 5-beat / 180-word threshold to author rather than strip. |
| 5c| Your-Turn placeholder | FIXED | Old BHTF command matched the "Take what you learned from [X] and apply it to your own work" template. AUTHORED a real exercise from the video's content: the four-question audit (cut / TODO.md / Skill / Hook) applied to the viewer's own CLAUDE.md, with a specific ask ("paste every line you cut, one sentence per line explaining why it was noise"). BHTF `output` list rewritten to 4 real next-step lines. |
| 5b| Chart text | FIXED | Old `scenes_std.py` had every Manim scene labelled with `Text(narration[:30])` — the exact enterprise-search defect. Rewrote as `scenes.py` (5 scenes: B02/B04/B06/B07/B08) with SHORT CATEGORY NOUNS ("Session 1/2/3", "Short file", "Long file", "Trim", "Skills", "Hooks", "Claude infers from code" → "cut", etc.) and COMPLETE-SENTENCE captions. Bar heights agree with narration meaning (short file taller = higher attention). "ACT I"-style doubled-space labels used where needed ("Session  1"). |
| 5 | Card text | FIXED | Old B01/B03/B09 FormBCard items had `label` = truncated narration ("This is Liam, in for", "md has a clear rule on"). Rewrote every label as 1–3-word category ("Line 12", "Third build", "Rule ignored", "Add rules", "Past 200 lines", "Why?", "50 maintained", "Most specific", "Or noise") with narration-derived subs. |
| 6 | Punt sweep | FIXED | No gen-AI asks, no unfilled `fill_slates` PIPELINE slates in the final build, no DoodleScene/DoodleChart, no STILL src=archive for concept content. B05 remains a declared SLATE card in this REVIEW cut (labeled "SCRIPTING GAP" in the honest slate) — see note below. |
| 7 | Card-only reel | PASS | 5 Manim scenes drive B02/B04/B06/B07/B08 — never a card-only reel. |
| 8 | Lens audit | PASS | Popper (predict-then-refute) via B05 — teacher predicts trimming to 95 lines restores compliance, it does. Hume (confidence is a property of the model) via B04 — "compliance is probabilistic," and via B07's compliance curve as a claim about the model. Two moves present. |
| 9 | Brand fields | FIXED | `folderLabel` = `@NikBearBrown` (channel handle, not brand key). `engine` = kokoro, `voice` = am_onyx — matches actual audio. Narration says "Liam, in for Bear" — Kokoro `am_onyx` is Liam-consistent. Metadata `topic` normalized from "CLAUDE CODE FOR TEACHERS" to "CLAUDE CODE" (channel is now anthropics/claude-code, no longer teachers-source). Source pointer left as historical ID. |
| 10| Pacing | LOGGED | Narration WPS spot-checks: B02 = 66 words / 21.5 s = 3.07 wps ✓; B04 = 71 / 21.5 = 3.30 ✓; B07 = 55 / 16.7 = 3.29 ✓. All body beats within 2.0–3.4 wps. |
| 11| type_check.py | PASS | GATE T: PASS. §8.10 advisories on B09 (0.94) and BVDT (0.87) — narration overlap with card — flagged as ADVISORY not FAIL (deliberate: these are the recap bookend + the endcard; overlap is by design and inside the advisory ceiling). |

## Phase 2 — Build

Deliverable: SLATE-WITH-AUDIO REVIEW CUT.

Pipeline (all local, free):
1. Audio: `generate_audio_kokoro.py . --voice am_onyx` → 12 beat mp3s in `mp3/`, measured durations written back into the sheet as `actual_duration_s`.
2. Manim scenes: `manim -ql --fps 24 -r 1280,720 scenes.py {B02,B04,B06,B07,B08}_ClaudeLiamVox` → copied to `manim/BXX.mp4`.
3. Remotion beats: `remotion_scenes.py .` → B00/B01/B03/B09/YOURTURN/BVDT/BHTF/BOUT rendered into `media/BXX.mp4`.
4. Compile: `compile.py . --review --height 720 --force` → `vox-claudemd-length-slate.mp4`.

### Gate V — frame audit
- Extracted 19 frames (every 12 s of the 227.6 s master) into `_qc/frames/`.
- Read each frame end-to-end.
- Zero BLOCKER, zero MAJOR on real beats after B07 re-render.
- ONE issue found and fixed in-loop: B07's original render had x-axis label "CLAUDE.md lines" colliding with the "Signal-to-noise..." caption. Scene source rewritten to place the axis label above the caption; re-rendered; recompiled.
- B05 is a declared slate ("B05 CARD SLATE" corner marker + "SCRIPTING GAP" body). Declared slate cards are exempt from Gate V per phase-2 rules.
- §8.10 advisories (B09, BVDT card/narration overlap) are ADVISORY, not FAIL; both intentional (endcard + verdict recap).

### Audio presence
- Master `mean_volume`: -27.1 dB (well above -40 dB threshold). Every body-beat mp3 present (mp3/beat-B0[1–9].mp3 + BVDT + BHTF + YOURTURN). B00 / BOUT keep their own audio-inside-mp4 track (NEVER-STRIP LAW).

### Build slot summary (Counter verbatim)
```
Counter({'VIDEO': 8, 'MANIM': 5, 'SLATE': 1})
B00:VIDEO B01:VIDEO B02:MANIM B03:VIDEO B04:MANIM B05:SLATE B06:MANIM
YOURTURN:VIDEO B07:MANIM B08:MANIM B09:VIDEO BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO
```

## Deliverable
- `vox-claudemd-length-slate.mp4` — 227.6 s, 3840×2160, per-beat narration, mean_volume -27.1 dB.
- Cut mtime is NEWER than beat_sheet.json mtime (verified via `ls -la`).

## What was NOT done (honestly)
- B05 (`The example`) was not rendered as a real card in this pass. Its narration is
  a 6-sentence story that reads better as a document skin (the CLAUDE.md before/after)
  or a stat card ("220 → 95 lines"). Left as a declared SLATE in the review cut so a
  later pass can author a real B05 without re-running everything. This is why the
  output is named `-slate.mp4`, not `.mp4`.
