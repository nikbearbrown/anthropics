# BUILD-PROMPT.md — claude-liam-git-claude-code

Paste this prompt into Claude Code (from `books/`) to build the full review cut
end-to-end. GATE P sign-off by Bear is required before running audio at ElevenLabs
quality; Kokoro runs free during the slate.

```
Read anthropics/youtube/claude-liam-git-claude-code/beat_sheet.json and build a
slate review cut of this reel.

Steps:
1. Confirm REPO-VERIFY.md exists and all numbers match the beat_sheet.json claims.
   If any number is wrong, STOP and flag it — do NOT proceed with a wrong number.

2. Run the Manim scenes to generate the 5 body fragments:
   ART_PALETTE=teardown manim -qh --fps 24 -r 1920,1080 \
     anthropics/youtube/claude-liam-git-claude-code/manim/scenes.py \
     B04_StructureMap
   # Repeat for B05_FolderTree, B05b_ScriptFiles, B07_VelocityChart, B10_ChurnChart
   # Copy each output to manim/B04.mp4, B05.mp4, B05b.mp4, B07.mp4, B10.mp4

3. Generate Kokoro narration (free, no GATE P needed for Kokoro):
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     anthropics/youtube/claude-liam-git-claude-code

4. Run the slate compile:
   ./brutalist-art/art run anthropics/youtube/claude-liam-git-claude-code

5. After compile: run GATE T type check:
   python3 brutalist-art/scripts/type_check.py \
     anthropics/youtube/claude-liam-git-claude-code
   Check TYPECHECK.md for any FAIL.

6. Sample frames for visual QC:
   ffmpeg -i anthropics/youtube/claude-liam-git-claude-code/mp4/claude-liam-git-claude-code.mp4 \
     -vf fps=2 anthropics/youtube/claude-liam-git-claude-code/_qc/frames/%05d.png
   Read the PNGs. Check 9-point rubric (edge bleed, title-safe margins, overflow,
   collision, legibility, brand bug, aspect, canvas fill).
   Log defects in _qc/REPORT.md.

7. STOP. Write a brief completion note in BUILD-LOG.md.
   Do NOT run art final, do NOT run 4K, do NOT run art post, do NOT publish.
   Bear reviews the slate and gives next instructions.
```

## Gates summary

| Gate | Requirement | Status |
|---|---|---|
| GATE VERIFY | All numbers == REPO-VERIFY.md | Must check in step 1 |
| GATE AUDIO | Kokoro narration, mean_volume > -40 dB, never silent | Step 3 |
| GATE T | TYPECHECK.md no FAIL | Step 5 |
| GATE VISUAL QC | Frame-level 9-point rubric | Step 6 |
| GATE P | Human narration sign-off (for ElevenLabs upgrade only) | PENDING Bear review |
| NEVER PUBLISH | Output stays in reel folder | Hard rule — never override |
