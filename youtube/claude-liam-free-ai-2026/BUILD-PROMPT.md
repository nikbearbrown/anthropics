# BUILD-PROMPT.md — Free AI in 2026: What You Actually Get

Paste this into Claude Code from `books/` to build the final cut end to end.  
Run with `claude --dangerously-skip-permissions` (pipeline meets seatbelt rules: git-tracked, regenerable outputs, GATE P still requires a human signature before spend).

---

```
Build the deep-explainer reel at:

  anthropics/youtube/claude-liam-free-ai-2026/

CHANNEL: claude-liam | VOICE: Kokoro am_onyx | PALETTE: claude

PRE-FLIGHT CHECKS (stop and report if any fail):
1. FACTCHECK.md exists and has no FAIL verdicts → verified
2. CHECKS-REPORT.md exists and teaching arc PASS → verified
3. BUILD-LOG.md Gate P shows Bear's signature → if unsigned, STOP here and wait for approval

SEQUENCE:
1. Gate F + CHECKS-REPORT: already written — confirm they exist before proceeding
2. Gate P — display the narration for human review on an animated slate; DO NOT spend on audio until Bear signs
3. Audio: python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/claude-liam-free-ai-2026
4. Audio lock — measure MP3 durations; update beat_sheet.json actual_duration_s fields
5. Gate D2 — pantry search for each VOX beat:
   python3 brutalist-art/runtime/scripts/pantry_search.py "<vox_description terms>"
   Then write SHOPPING.md with locked durations (NOT before this step)
6. Gate D1 — full-length slate previz:
   ./brutalist-art/art run anthropics/youtube/claude-liam-free-ai-2026
7. Pantry fill — place human-supplied or generated stills into pantry/; run intake
8. Manim renders:
   python3 brutalist-art/runtime/scripts/remotion_scenes.py anthropics/youtube/claude-liam-free-ai-2026
   (Remotion scenes render automatically via art run — Manim scenes use animated_graphics.py)
9. Review cut compile:
   python3 brutalist-art/runtime/scripts/compile.py anthropics/youtube/claude-liam-free-ai-2026
10. GATE T type-lock:
    python3 brutalist-art/scripts/type_check.py anthropics/youtube/claude-liam-free-ai-2026
    → must produce TYPECHECK.md with no FAIL before proceeding
11. GATE SHARPNESS: run.sh Laplacian audit (after GATE T)
12. VISUAL QC LAW:
    ffmpeg -i <slug>-slate.mp4 -vf fps=2 _qc/frames/%05d.png
    Read sample PNGs; audit 9-point rubric; log defects in _qc/REPORT.md
    Fix root causes in scene source and re-render until zero BLOCKER/MAJOR defects
13. Final cut (only after VISUAL QC clean):
    ./brutalist-art/art final anthropics/youtube/claude-liam-free-ai-2026
14. TOPOST staging (HARD GLOBAL RULE — NEVER skip):
    art post skill only; staged master must land in books/youtube/TOPOST/
    with matching staged.json entry before any upload

NEVER publish directly. Public is a manual Studio flip by Bear.

VOX BEATS AWAITING PANTRY STILLS:
B03 — three access-pass objects (wristband, ticket, key) | kenburns | tier-1
B10 — tall stack of document pages | kenburns | tier-1
B13 — abstract coding interface on monitor | kenburns | tier-1 (no real product UI)
B24 — sealed envelope with wax seal | kenburns | tier-1 [R1 start]
B25 — closed laptop on desk | cutout (alpha required) | tier-1 [R1 end]
B29 — compass on folded map | kenburns | tier-1 [R2 start]
B30 — open laptop showing docs page | annotate | tier-1 [R2 end]
B18 — layered trays (stacking metaphor) | parallax (needs 3 layers: bg/mid/fg) | tier-1

All tier-1 generic — AI-generate. SHOPPING.md entries will specify minimum resolution
after audio lock measures beat windows.
```
