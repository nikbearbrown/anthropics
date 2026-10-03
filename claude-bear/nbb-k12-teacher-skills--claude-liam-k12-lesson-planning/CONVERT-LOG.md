# CONVERT-LOG — nbb-k12-teacher-skills--claude-liam-k12-lesson-planning

Source: `../k12-teacher-skills--claude-liam-k12-lesson-planning/beat_sheet.json`
Target: `beat_sheet.nbb.json`
Register: Plain → Teardown (Feynman × MKBHD). Voice: Liam / Kokoro `am_onyx`.

## What changed

- **Metadata**
  - `subtitle` "The K12 Lesson Planning Skill" → "A List, Not a Freshly-Reasoned Plan" (Teardown hook — the animating trade-off, not a topic label).
  - `purpose` rewritten in the Teardown register; names the design trade-off explicitly ("optimized for repeatability at the expense of coverage").
  - `style_preset` humanitarians → teardown.
  - `ground` `#F3EBDD` → `#FFFFFF` (teardown ground).
  - `folderLabel` / `channel_title` `@HumanitariansAI` → `@NikBearBrown`.
  - `_variant_todo` removed.
- **B00 (cold open, BrutalistHesitantWriter)**
  - Narration rewritten; opens "Liam here, in for Bear" per IN-FOR-BEAR LAW, then "Here's what's actually happening under the hood" (Teardown opener).
  - WRITER text preserved verbatim (`When Claude plans / a lesson for my class, / does it improvise?`) so the trigger-word contract still holds: `improvise` is a single token immediately before terminal `?`, per the existing `note`.
  - Palette flipped to teardown: ink `#2F2A26` → `#2A1A0E`, accent `#E4572E` → `#C8102E`, bg `#F3EBDD` → `#FFFFFF`.
  - `seed` `hai-k12-lesson-planning` → `nbb-k12-lesson-planning` so the render is deterministically different from the HAI sibling.
  - `estimated_duration_s` 13 → 15 (narration grew from ~34 to ~46 words; still inside the 20–35 → ≥9s WRITER TIMING LAW window with `lead_silence_s` 0.8).
- **NB01 / NB02 / NB03 (mechanism)** — narrations rewritten in Teardown ("take a Claude skill apart…", "here's the mechanism, in full", "that's what they optimized for"). Beat IDs, `act`, `shot.type`, `graphic.production_viz.label`, `chips`, `arrows`, `accent`, `strike`, `caption`, and `graphic.manim` scene names preserved verbatim so the Manim renderer keeps producing the same figures. Only the `colors` triple was re-skinned to the teardown palette (`#FFFFFF / #2A1A0E / #C8102E`).
- **BCRY (carry-out)** — narration rewritten; the `WantQuote.quote` was updated to match the new narration verbatim, and `sparkLine` "Written steps, not improvisation." → "A list, not improvisation." — same claim, sharper Teardown phrasing.
- **BHTF** — repurposed from "your turn handoff" to **LLM EXERCISE** (per SKILL.md §Step 3, matching the sibling nbb-cwc-workshops--claude-liam-reorder-policy pattern):
  - `act` "your turn handoff" → "LLM EXERCISE".
  - Added the required `llm_exercise` object: `prompt` (paste-ready, useful on its own — asks the model to author a SKILL.md, run it twice on identical inputs, then run it on an uncovered case) and `dig_deeper` (adds a "use your judgment" step and asks whether the list still behaves like a list).
  - `narration_text` rewritten to speak the prompt out loud in the Teardown register, closing with the "Go deeper" question. Length grew from ~54 to ~124 words; `estimated_duration_s` 18 → 32 to match.
  - `ClaudeComposerAsk.command` shortened to a card-legible version of the prompt (composer text has to fit on screen). `folderLabel` swapped to `@NikBearBrown`. `greeting`, `topic`, `segment`, `runningText`, `output` preserved.
- **BOUT (outro)** — switched from `OutroSeries` (eyebrow + line) to `OutroCTA` (line + handle) to match the NikBearBrown outro contract in `brands/nbb.md` (`www.brutalist.art` NikBearBrown default). Narration rewritten to the three-part NikBearBrown sign-off form used across the batch: `<title>. <sparkLine>. Liam, in for Bear.` → "Claude, K12 Lesson Planning. A list, not improvisation. Liam, in for Bear." `handle`: `@NikBearBrown`.

## Ending order

Body (B00 → NB01 → NB02 → NB03 → BCRY) → LLM EXERCISE (BHTF, second-to-last) → NikBearBrown outro (BOUT, last). ✓

## Facts preserved

Every source claim survives: the skill is named `k12-lesson-planning`; SKILL.md holds the instruction set in plain language with no hidden logic; the Steps section is a numbered list run top to bottom, linear with no branching unless a step says otherwise; the folder also ships a `references/` folder of source material and a `scripts/` folder of runnable code; where a step can run as code it does, so the same input produces the same output; anything the steps don't cover falls back to Claude's own judgment, not the skill's playbook. All beat IDs, `act` labels (except BHTF, per SKILL.md §Step 3), Manim scene names, and `production_viz.chips` copy are unchanged.

## Judgement calls

- **BHTF `act` was renamed** ("your turn handoff" → "LLM EXERCISE") because SKILL.md §Step 3 requires the second-to-last beat to be an LLM exercise; the sibling nbb-cwc-workshops--claude-liam-reorder-policy did the same. The "your turn" framing survives inside the narration ("Your turn. Paste this into…") so the handoff intent is preserved.
- **`llm_exercise.prompt` was made concretely runnable** by hard-coding the sample inputs `grade 7, science, water cycle` — echoing the seventh-grade water-cycle example the source's BHTF already used, so no new fact is introduced.
- **BOUT pattern change** (`OutroSeries` → `OutroCTA`) mirrors the sibling nbb reels and lines up with the NikBearBrown handle-based outro; the `line` still leads with the source title verbatim.
- **`topic` metadata was left as `K12-LESSON-PLANNING · ANTHROPIC SKILL`** — it describes the subject, not the audience, so the audience swap doesn't touch it. Only channel/folder/handle strings flipped to `@NikBearBrown`.

## Not done (correct per contract)

No audio was generated. No render, compile, or `art run` was invoked. Deliverable is `beat_sheet.nbb.json` only.
