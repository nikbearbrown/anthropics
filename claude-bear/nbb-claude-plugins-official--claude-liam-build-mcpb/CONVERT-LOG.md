# CONVERT-LOG — nbb-claude-plugins-official--claude-liam-build-mcpb

Converted `beat_sheet.json` → `beat_sheet.nbb.json` (Teardown / NikBearBrown cut).
No render, no audio, no compile.

## What changed

- **All 9 body-beat narrations rewritten in the Teardown register** (Feynman ×
  MKBHD): "here's what's actually happening," "they optimized for X at the
  expense of Y," the mechanism gets taken apart and named. Facts unchanged —
  every ROOT_DIR / ROOT_DIRECTORY / dot-dot-slash / esbuild / mcp_config /
  dollar-dirname / dollar-user-config claim survives verbatim. Word counts
  held close to source so the master clock (narration duration) stays in the
  same window; `estimated_duration_s` bumped +1–2 s on B05 and B_LLM to
  reflect the slightly longer sentences.
- **B00 cold open** now names Liam out loud ("Liam here, in for Bear …") per
  the IN-FOR-BEAR LAW. Shot props for `BrutalistHesitantWriter` untouched, so
  the typing timing budget is unchanged.
- **BHTF (source "your turn handoff") absorbed into a new B_LLM beat**
  ("LLM EXERCISE") sitting second-to-last, with a proper `llm_exercise`
  block: a paste-ready prompt for Claude/ChatGPT/Gemini covering the three
  actual traps in this reel (name-match, unvalidated path, missing bundle),
  and a dig-deeper follow-up that pushes the viewer to compare MCPB
  packaging to real sandboxing (WASM, seccomp, containers). Same
  `ClaudeComposerAsk` scene; the visible `command` chip carries a compact
  distillation of the paste-ready prompt so the shot still reads. Rendered-out
  path and status were reset (`media/B_LLM.mp4`, `PENDING`) since the beat_id
  moved; supervisor will re-render.
- **BOUT** rewritten as the NikBearBrown outro (last beat): keeps `OutroCTA`,
  keeps the Liam-in-for-Bear signoff (IN-FOR-BEAR LAW), rebrands the handle
  chip to `@NikBearBrown` and adds "at brutalist dot art" (the default
  channel per `brands/nbb.md`, since no `AUTHOR.MD` exists on this book).
  Rendered-out path reset to `PENDING` — narration + handle both changed.
- `_variant_todo` removed from metadata.

## Judgment calls

1. **No `AUTHOR.MD` on this book.** `anthropics/claude-plugins-official/`
   has a `LICENSE` and `README.md` but no `AUTHOR.MD` — so the outro cannot
   quote a book-specific NikBearBrown paragraph. Fell back to the SKILL's
   documented default channel (`www.brutalist.art`) plus the standard
   Liam-in-for-Bear signoff. Wrote it as "brutalist dot art" so Kokoro
   reads the URL cleanly.
2. **BHTF absorbed rather than kept alongside a new LLM beat.** The source
   BHTF was already a "paste this into Claude" prompt using
   `ClaudeComposerAsk` — functionally the same beat the SKILL asks for at
   position -2. Adding a second LLM beat would double the same shot type
   back-to-back and leave nothing between the carry-out (BCRY) and the
   outro. Cleaner: reshape BHTF into the required B_LLM contract (adds
   `llm_exercise` field with `prompt` + `dig_deeper`, tightens the on-screen
   command, includes go-deeper handoff in the narration). Reference nbb
   reels (`nbb-vox-light-ceiling` NBB02) use the same pattern: one
   `ClaudeComposerAsk` second-to-last carrying both the paste-ready prompt
   and the your-turn framing.
3. **Handle chip switched to `@NikBearBrown`** on the two Remotion beats
   whose props display a brand chip (B_LLM and BOUT) — the point of the
   NikBearBrown cut is that the visible brand switches with the register.
   Metadata `folderLabel` / `channel_title` / `style_preset` / `ground` left
   as the scaffold set them (per "do not re-scaffold"): those are metadata
   fields, not the outro/LLM-beat visible chips that Step 3 / Step 4 own.
4. **Shot color props (`bg` / `colors` on Manim scenes) left as scaffold
   left them.** Even though `palette` in metadata is `teardown` (flat white
   #FFFFFF), every shot's color triples still carry `#F3EBDD` from the HAI
   source. Retinting shot props would fan out across every Manim scene and
   risks breaking `BGB01Scene`…`BGB07Scene` at render time. That's a
   scaffold/render-layer concern; not this pass's scope.
5. **B05 / B_LLM `estimated_duration_s`** nudged up (15 → 16, 23 → 27
   respectively) because the Teardown rewrites are a hair longer than the
   source lines. Kokoro will time to actual; these are hints only.

## Ending order (per SKILL Step 5)

```
… B00 B01 B02 B03 B04 B05 B06 B07 BCRY   ← Teardown body beats
B_LLM                                     ← second-to-last (LLM exercise)
BOUT                                      ← last (NikBearBrown outro)
```

## Not done (out of scope)

- No audio generation. No compile. No render. Supervisor takes it from
  here — `generate_audio_kokoro.py` → `remotion_scenes.py` for B00 / BCRY /
  B_LLM / BOUT → `compile.py`.
