# CONVERT-LOG — nbb-cwc-workshops--eval-driven-six-agent-variants

Source: `../cwc-workshops--eval-driven-six-agent-variants/beat_sheet.json` (Plain register, HAI-fellows cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take the setup apart", "Here's what the glance misses",
"The eval runs in two layers, and they're doing different jobs"), mechanism-first
framing, and the trade-off named out loud at S08 ("rules in a prompt survive as
long as the prompt does, no further"). BCRY carry-out kept the source's central
claim and added the mechanism it names ("that's how you tell a prompt win from a
model win"). Facts, numbers, filenames, .pptx checks, the 9pt / 10pt floor
example, the four-round structure, and beat ordering all preserved from the
source verbatim.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already there at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual and its "looks" → "scores" trigger word (the
on-screen conceit still fits the register — a glance vs. a measurement is the
Teardown thesis).

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt for the same
subject, so I made it the LLM exercise beat in place rather than inserting a
new B_LLM. Preserving `beat_id: BHTF` (the "preserve every beat_id" rule beat
the SKILL's suggested `B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from the source's "run against fixed test + baseline"
  narration into a substantive **build-me-an-eval-harness** paste-ready block
  that produces something useful on its own (a two-layer harness with a code
  check, a judge rubric, a fixed test set, and a table separating prompt-only
  wins from model-only wins). The video's central mechanism is demonstrated by
  running the exercise, not by describing it.
- `dig_deeper`: pick one rule that only lives in your prompt, strip it, swap
  the model, does it hold — that's the S08 trade-off re-tested by the viewer.
- Kept ClaudeComposerAsk visual (it IS the paste-into-Claude UX); left the
  `command` prop close to the source (a shorter, tighter paste-block that
  still shows on-screen) and updated `folderLabel` → `@NikBearBrown`.

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown: "Six Agent Variants — how to measure what
a prompt change actually did. Same test, same baseline, or you're guessing.
Liam, in for Bear." Kept OutroSeries pattern per the "preserve shot blocks"
rule (didn't switch to OutroCTA); updated `eyebrow` from `AGENT EVALS ·
@HumanitariansAI` → `AGENT EVALS · @NikBearBrown` and `line` to match the
Teardown title.

## Judgment calls

1. **Retinted every hard-coded hex to teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#1F4E5F` teal / `#E4572E` accent).
   If those aren't remapped, a render will visually be a humanitarians reel with
   a teardown metadata label. Remapped every `production_viz.colors[]` in S01–S10
   to `[#FFFFFF, #2A1A0E, #C8102E]` (ground / ink / crimson — the teardown
   palette; teal in this palette IS ink, per the palette doc). Also remapped B00
   BrutalistHesitantWriter `bg`/`ink`/`accent` and `metadata.ground`. The
   `production_viz.mechanic` text descriptions that reference "teal" are left as
   written — they're advisory notes for the Manim scene, and colors[] is the
   authoritative palette source at render time.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source `folderLabel`
   / `channel_title` / OutroSeries `eyebrow` all pointed at `@HumanitariansAI`.
   For an NBB cut those need to point at Bear's channel or the visual chip and
   sign-off will contradict the outro voice. Changed `folderLabel`,
   `channel_title`, `beats[BHTF].shot.remotion.props.folderLabel`, and
   `beats[BOUT].shot.remotion.props.eyebrow` all to `@NikBearBrown`. Also
   updated `metadata.style_preset` from `humanitarians` → `teardown` for the
   same reason.

3. **`brand` field: `hai-fellows` → `nbb`.** The scaffold set `audience:
   NikBearBrown` but left `brand: hai-fellows` from the source. Left as
   hai-fellows would risk downstream tooling applying HAI palette or templates
   over an NBB cut. Changed to `nbb` to match the palette/register intent.

4. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting a
   duplicate beat. Result: BHTF is now the LLM exercise (second-to-last) and
   BOUT the outro (last), matching the ending order the SKILL asks for.

5. **Cold-open "Liam here, in for Bear."** Not literally required by
   IN-FOR-BEAR LAW at B00 (the law says "says so out loud in the cold open") —
   added it because the source didn't and the sibling nbb-reorder-policy
   precedent added it. The BOUT sign-off was already present in the source.

6. **B00 `seed` prop** changed from `cwc-eval-six-variants` →
   `nbb-cwc-eval-six-variants`. Cosmetic — keeps the writer's deterministic
   timing distinct from the source render's cache so the two variants don't
   collide.

7. **BCRY WantQuote `quote`** rewritten to match the new BCRY narration (that's
   the WantQuote contract — spoken sentence and on-screen quote are the same
   sentence). This is on-screen copy, but it *is* the narration, so it moves
   with it. Kept `sparkLine: "Same test. Same baseline."` — punchy,
   mechanism-carrying, still fits the Teardown register verbatim.

8. **BHTF and BOUT `estimated_duration_s` bumped modestly** (24→26 for BHTF,
   6→8 for BOUT) to reflect the slightly longer Teardown-voice rewrites. These
   are estimates — real durations get measured when audio is regenerated in
   the render pass.

9. **Removed `_variant_todo`** — checklist complete.

## Not touched (intentionally)

- Every `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`,
  `remotion.pattern`, `graphic.manim` scene names,
  `graphic.production_viz.label` / `mechanic`. On-screen text descriptions are
  preserved verbatim; only color hex values inside the props were remapped and
  BCRY's `quote`/`sparkLine` were updated to match the new spoken carry-out.
- `metadata.build` block (source render snapshot), `audio_file` paths, `build`
  blocks per beat. These will get overwritten when this nbb- dir is actually
  rendered. Rendering is a separate pass; this factory converts only.
- `metadata.purpose` was tightened slightly to describe the Teardown cut's
  angle (two layers, four rounds, the S08 trade-off) rather than the source's
  Plain-register framing. All grounding claims are unchanged.
