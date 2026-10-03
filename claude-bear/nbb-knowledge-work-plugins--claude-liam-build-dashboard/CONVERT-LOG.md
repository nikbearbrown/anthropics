# CONVERT-LOG — knowledge-work-plugins--claude-liam-build-dashboard → nbb

Converted from `claude-bear/knowledge-work-plugins--claude-liam-build-dashboard/beat_sheet.json`
into the NikBearBrown cut. Voice: Kokoro `am_onyx` (Liam, in for Bear). No render.

## What changed

- **Register** → Teardown (Feynman × MKBHD). Every `narration_text` rewritten:
  - B00 sets up the naive reading ("running app on a server") then flips it and cues the takedown ("Let's take that file apart.").
  - B01 names the design choice out loud: "put the routine on the page, not in the weights."
  - B02 explains the pipeline as three moves with no branching — reveals what linear execution costs and what it buys.
  - B03 names the optimize-for/at-expense-of trade explicitly: "reliability inside the four at the expense of anything general beyond them."
  - BCRY tightened for the WantQuote card — verdict form kept, wording sharpened; the `remotion.props.quote` was updated to match the new narration verbatim.
- **BHTF transformed into the LLM EXERCISE beat** (second-to-last slot, per the reference nbb pattern in `nbb-financial-services--claude-liam-deal-sourcing`). No new beat inserted — BHTF already occupied the pre-outro slot as a paste-ready-prompt beat, so it was re-scoped from a Claude-specific "your turn" into a Claude/ChatGPT/Gemini LLM exercise. Added an `llm_exercise` object with `prompt` (a self-contained, useful-on-its-own SKILL.md-writing task) and `dig_deeper` (a real next question, not a summary).
- **BOUT (outro)** — text unchanged; `handle` swapped from `@HumanitariansAI` to `@NikBearBrown`.
- **ClaudeComposerAsk props on BHTF**: `folderLabel` → `@NikBearBrown`, `runningText` → "paste this into Claude, ChatGPT, or Gemini…", `command` chip rewritten to match the new LLM exercise.
- **Metadata**: added `subtitle` ("One File, Not a Server"), updated `channel_title`/`folderLabel` → `@NikBearBrown`, `playlist` → `Claude Basics`, rewrote `purpose` in Teardown terms. `_variant_todo` removed.
- **Preserved unchanged**: every `beat_id`, act order, all `shot`/`graphic` blocks and their visuals, on-screen card copy that still reads Teardown (BrutalistHesitantWriter text "Can Claude / build me a / live dashboard / app?" — the naive-reading-corrected setup fits the register), Manim scene names, build src/status/at fields, audio_file paths.

## Judgement calls

- **BHTF re-scoped rather than a new B_LLM inserted**: the source already had a "your turn handoff" beat in the pre-outro slot with a paste-ready Claude prompt. Inserting a separate B_LLM would have created two consecutive prompt beats. The reference nbb reel (`nbb-financial-services--claude-liam-deal-sourcing/BHTF`) resolves this the same way — retitle the existing beat `LLM EXERCISE`, add the `llm_exercise` object, broaden the prompt to any frontier LLM. Followed that pattern.
- **B00 estimated_duration_s** bumped 14 → 15 for the slightly longer teardown-register opener (still inside the WRITER LAW ≥9s window; narration ~50 words). Similar small bumps on B01 (19→20), B02 (12→13), B03 (20→21), BHTF (22→42, since the LLM prompt read-aloud is genuinely longer). All are estimates; `generate_audio_kokoro.py` measures the truth downstream.
- **`ground` and BrutalistHesitantWriter `bg` left at `#F3EBDD` (cream)** even though the teardown-palette spec is `#FFFFFF` white. The reference nbb reel keeps these fields as-scaffolded (`style_preset: "humanitarians"`, `ground: "#F3EBDD"`); not correcting palette drift in this register pass.
- **`gate_c` em-dash re-normalised** ("SIGNED — CARRY-OUT.md") — matches the source; the scaffold had swapped it to a hyphen. Cosmetic only.

## Ending order (verified)

… BCRY (CARRY-OUT) → BHTF (LLM EXERCISE) → BOUT (outro). Second-to-last is the LLM exercise; last is the NikBearBrown outro.
