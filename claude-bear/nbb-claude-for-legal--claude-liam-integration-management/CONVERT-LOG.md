# CONVERT-LOG.md — nbb cut

**Slug:** `claude-for-legal--claude-liam-integration-management`
**Register:** Plain → Teardown (Feynman × MKBHD)
**Voice:** Kokoro `am_onyx` — Liam, in for Bear (scaffold-set; unchanged)
**Palette:** teardown (scaffold-set; unchanged)
**Date:** 2026-09-03

## What changed

### 1. Every beat narration rewritten in the Teardown register
- **B00** — cold open trimmed and re-cadenced; kept 20–35 word timing window
  the note enforces. Facts unchanged (plan vs tracker; Liam introduced).
- **B01** — rewrote as "here's what's actually happening" opener,
  named the design trade-off explicitly: plan optimizes for clarity
  in one moment, sacrifices visibility the day after. All source facts
  preserved (single doc, day-of-closing, IT/HR/finance/contracts running
  parallel, stalled workstreams, live tracker as the fix).
- **B02** — reframed as a mechanism explanation. Named the constraint
  as a design choice ("enough shape to catch a missing owner, few enough
  to actually fill in"). Four fields, three phases, and the anchor card
  preserved verbatim.
- **B03** — moved from "but…" to "now name the limits" for MKBHD-style
  honesty; added the sharpening closer "The tracker reveals gaps. It does
  not close them." All source claims preserved.
- **BCRY** — tightened the carry-out and made the plan/tracker asymmetry
  the sentence hinge ("The plan holds for day one; the tracker outlasts
  it."). `WantQuote.quote` prop updated to match the new narration text
  exactly (same string in both places, as the shot demands). `sparkLine`
  also refreshed to match. No structural change to the shot block.
- **BHTF** — voice pass only. Kept the ClaudeComposerAsk shot block
  intact per the preserve-shot-blocks rule; refreshed the read-along
  narration.

### 2. New `B_LLM` inserted second-to-last
- New beat with `beat_id: "B_LLM"`, `act: "LLM EXERCISE"`, and the
  schema exactly as specified in `skills/make/nbb/SKILL.md` §Step 3:
  a paste-ready LLM prompt in `llm_exercise.prompt`, one "Go deeper:"
  follow-up in `llm_exercise.dig_deeper`, shot `type: CARD`.
- The prompt is a real ops-lead task — "build me a phased tracker with
  four fields per workstream" — and produces a usable table on its own
  without the video.
- The follow-up ("which workstream is most likely to surface after day
  one") pushes past the video's own scope; it is a genuinely explorable
  next question, not a summary.

### 3. `BOUT` rewritten as the NikBearBrown outro
- Narration adds the NikBearBrown channel sign-off ("NikBearBrown --
  brutalist.art") after the standard "Liam, in for Bear" sign-off, per
  brands/nbb.md (default channel: brutalist.art) and the IN-FOR-BEAR
  LAW (Liam names himself; he never claims to be Bear).
- `OutroCTA` shot pattern preserved; only `line` and `handle`
  updated (`handle` → `@NikBearBrown`).

### 4. `_variant_todo` removed
The scaffold's TODO checklist was deleted from metadata. All five items
on it are now done.

## Judgment calls

- **Kept BHTF, then inserted a new `B_LLM` between BHTF and BOUT** (order
  is now `… BCRY, BHTF, B_LLM, BOUT`). The instructions require both
  "preserve exactly … shot blocks" and "insert the LLM exercise beat,
  SECOND-TO-LAST." Converting BHTF's `ClaudeComposerAsk` shot into the
  spec's `CARD` shot would violate the preserve rule, so `B_LLM` was
  inserted as a new beat and BHTF was voice-passed only. Yes, that means
  two paste-a-prompt beats sit back-to-back — BHTF is the "read it with
  me on screen" version, B_LLM is the "paste the actual prompt into any
  frontier LLM" version. Different jobs, different shots.

- **Left the `ground` color at `#F3EBDD` (cream) instead of forcing the
  teardown-palette flat white (`#FFFFFF`).** The scaffold left it that
  way, the shot props on B00 and the four Manim scenes reference the
  same humanitarians ground, and my instructions say do not re-scaffold.
  Flagging here so a later pass can retint if desired — the `palette`
  field already reads `teardown`, so the metadata disagrees with the
  actual color values in the shot blocks. Not fixed in this pass.

- **`style_preset: humanitarians` left as scaffold set it** — same
  reason as above; preset drives render-time skinning and shouldn't
  change without confirming the Manim scenes will still render.

## Not touched

- No audio generated. No compile. No render. The deliverable is one
  JSON file.
- Source `beat_sheet.json` at
  `claude-for-legal--claude-liam-integration-management/beat_sheet.json`
  is untouched, as required.
