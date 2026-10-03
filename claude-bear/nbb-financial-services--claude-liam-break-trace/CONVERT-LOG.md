# CONVERT-LOG — nbb-financial-services--claude-liam-break-trace

**When:** 2026-09-03
**Source:** `anthropics/claude-bear/financial-services--claude-liam-break-trace/beat_sheet.json` (Plain register, 7 beats)
**Target:** `beat_sheet.nbb.json` (Teardown register, 7 beats — LLM exercise at BHTF, outro at BOUT)

## What changed

- **Every beat's `narration_text` rewritten in the Teardown register** (Feynman × MKBHD). Facts, beat IDs, act labels, `shot`/`graphic` blocks, on-screen chip copy, and Manim scene bindings all preserved. Voice-only change: added the *why* behind the design cut ("they chose readability over cleverness", "optimized for repeatability at the expense of cleverness", "optimized for auditability — the fix stays yours").
- **B00 (cold open)** — kept inside the 20–35 word window per the timing note so the writer's `fix` → `trace` correction still lands within the ≥9s window. 31 words, `lead_silence_s: 1.0` unchanged.
- **BCRY (carry-out)** — narration and `WantQuote.props.quote` updated together so the on-screen carry-out sentence still matches what Liam says. `sparkLine "Trace it. Don't fix it."` kept intact — it already reads as Teardown.
- **BHTF (your turn handoff) upgraded into the LLM exercise beat**:
  - `act` → `"your turn handoff (LLM exercise)"`
  - Narration now follows the "Here's a prompt you can paste directly into Claude, ChatGPT, or Gemini … Go deeper: … Liam, in for Bear." shape.
  - New `llm_exercise: { prompt, dig_deeper }` field on the beat.
  - `ClaudeComposerAsk.props`: added `segment: "Your Turn"`, changed `folderLabel: "@HumanitariansAI"` → `"@NikBearBrown"` (matches completed sibling nbb reels — nbb cut lives on the @NikBearBrown channel).
  - The paste-ready prompt is the source's own handoff prompt kept verbatim: it already runs on any frontier LLM without the video.
- **BOUT (outro)** — Remotion pattern remapped `OutroSeries` → `OutroCTA` with `line: "Trace It, Don't Fix It. Liam, in for Bear."` and `handle: "@NikBearBrown"`, matching every completed nbb sibling in this book.
- **`metadata._variant_todo` removed.** `metadata.register` flipped from `"Plain"` to `"Teardown"` (the scaffold had `"Plain"` copied from source — supervisor gate `register: Teardown` requires this).
- **`estimated_duration_s` updated** on every rewritten beat to a ~2.5-words/sec estimate — honest signal for the downstream audio pass since narration lengths grew (NB01 18→26, NB02 16→25, NB03 24→30, BCRY 8→11, BHTF 21→32). B00 and BOUT unchanged.

## Untouched (by design)

- `engine`, `voice_kokoro`, `palette`, `audience`, `derived_from`, `outro_source`, `typography` — set by scaffold; not re-scaffolded.
- Every `beat_id`, `act` label (except BHTF, which got the `(LLM exercise)` suffix), `shot.type`, Manim `scene` binding, `graphic.production_viz` chips/captions/colors/accent/strike, `note` on B00, `audio_file` paths, `build` blocks (`status`, `src`, `filled_by`, `at`).
- `metadata.folderLabel`/`channel_title`/`playlist` (`@HumanitariansAI`) — kept exactly as the scaffold set them; only the beat-level `folderLabel` inside BHTF's ClaudeComposerAsk was swapped to `@NikBearBrown`, matching every completed sibling in `anthropics/claude-bear/nbb-*/`.
- `actual_duration_s` — absent (scaffold stripped it; new audio must be regenerated before compile).

## Judgement calls

1. **BHTF as the LLM-exercise beat, not a new inserted beat.** SKILL.md §Step 3 shows a `B_LLM` beat inserted. But every completed sibling in this book (`nbb-claude-agent-sdk-demos--claude-liam-executive-briefing`, `nbb-books--claude-liam-*`) upgrades the existing `BHTF` beat instead — same `ClaudeComposerAsk` shell, adds `llm_exercise` field, tags the act. The result satisfies "second-to-last beat with paste-ready prompt + dig-deeper follow-up" without breaking beat count or shot allocation. Followed the sibling precedent.
2. **BOUT `OutroSeries` → `OutroCTA`.** SKILL.md §Step 4 says either pattern renders in teardown palette. `OutroCTA` (`line` + `handle`) is what every completed nbb sibling uses for the NBB channel handle. Went with the working precedent.
3. **No AUTHOR.MD in `anthropics/claude-bear/`.** SKILL.md §Step 4 asks for outro content sourced from `AUTHOR.MD :: NikBearBrown`. None exists at the book root here. The completed siblings resolve this by using the `[Title]. Liam, in for Bear.` line + `@NikBearBrown` handle — that is the effective NBB outro spec across every finished nbb reel in this book. Followed suit; source is documented in `metadata.outro_source` as scaffolded.
4. **`register: "Plain"` → `"Teardown"` in metadata.** The scaffold left the source's `"Plain"` in place. `brands/nbb.md` and SKILL.md are explicit that the register IS Teardown for nbb, so this had to flip. All other scaffold-set fields left alone.

## Not done (out of scope per invocation)

- No audio generated. No render. No compile.
- Manim scene rebinding not touched; existing BDNB01–NB03 scenes still bound.
- Palette-tone check on the Manim scenes not performed (source chips still reference `#F3EBDD` humanitarians cream, not teardown flat white `#FFFFFF`) — that is a render-pass concern, not a beat-sheet concern.
