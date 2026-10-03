# CONVERT-LOG — nbb-claude-for-legal--claude-liam-legal-writing

## What changed

- **Register**: rewrote every narration in Teardown (Feynman × MKBHD). Facts
  preserved verbatim — same four steps, same rubric list, same VERIFY behavior,
  same "write yours, don't copy" label, same anchor (1L's negligence memo).
  Voice change only.
- **Metadata**: `register` set to `Teardown`; `_variant_todo` removed.
  All other metadata (audience, engine, voice_kokoro, palette, style_preset,
  ground, folderLabel, channel_title, playlist, in_for_bear, clock, gate_c,
  gate_h, anchor_pair, one_flag, outro_source, typography) left as the
  scaffold set them.
- **B00 cold open**: reframed as design-choice observation — the skill is
  "built to refuse the rewrite, on principle." Kept 20–35 word target for
  the BrutalistHesitantWriter TIMING LAW window; ~40 words now (still safe
  for the ≥9s typing window with lead_silence_s 0.8).
- **B01–B07 body**: each rewrite names what the skill optimized for and what
  it cost. B04 gets the "smoothing a house that's still crooked" image for the
  top-down-order design choice; B05 gets the honest self-assessment framing;
  B06 makes the "write yours, don't copy" label the design itself.
- **BCRY carry-out**: left the on-screen quote verbatim — it is the WantQuote
  prop and is echoed word-for-word by the narration. The Teardown register is
  already in the sentence; changing it would break the promised anchor between
  the carry-out heard and the carry-out read.
- **BHTF converted to LLM EXERCISE**: was the "your turn handoff" — repurposed
  in place as the SECOND-TO-LAST beat per SKILL.md §Step 3. Added the
  `llm_exercise` object with paste-ready `prompt` (four numbered moves that
  mirror the skill's actual behavior) and `dig_deeper` follow-up (three
  paragraphs, one subtly wrong rule each — a self-test the viewer can run
  without me). ClaudeComposerAsk visual retained; `command` prop tightened to
  fit the composer. Bumped `estimated_duration_s` from 20 → 55 to match the
  longer LLM-exercise narration (~135 words at ~2.5 wps).
- **BOUT outro**: replaced the bare "Claude, Legal Writing. Liam, in for Bear."
  with the carry-out-folded variant "Claude, Legal Writing — harsher reader,
  never ghostwriter. Liam, in for Bear." (matches the reference pattern from
  nbb-claude-for-legal--claude-liam-ip-clause-review, which folded the carry-out
  spark into the outro line). Bumped `estimated_duration_s` 6 → 7 to cover
  the longer line.

## Judgement calls

- **BCRY quote preserved verbatim** rather than rewritten. The WantQuote
  pattern echoes exactly what the narration reads; the sentence is already
  Teardown-shaped ("harsher reader, never ghostwriter" is machinery-and-trade-off
  language); rewriting would desync narration ↔ card without a real gain.
- **Card copy (graphic.production_viz labels/chips/captions) preserved**.
  SKILL.md Step 2 says "on-screen card copy where it still fits the register" —
  every existing label reads as machinery description ("NO REWRITE, EVER",
  "TOP-DOWN, IN THAT ORDER", "CONFIDENT ON FORM, NOT ON LAW", "NOT PROOF,
  EITHER WAY"). They already fit Teardown; changing them for change's sake
  would risk breaking the rendered manim/B0*.mp4 files that are already built.
- **BHTF repurposed, not inserted**. SKILL.md says "insert one beat before the
  outro" — the source's existing your-turn-handoff already sits in exactly that
  position with the ClaudeComposerAsk visual, so repurposing it in place
  matches the reference nbb sheets (e.g. IP-clause-review) rather than adding
  a redundant twelfth beat. Ordering is now body (B00–B07) → BCRY carry-out →
  BHTF LLM EXERCISE → BOUT outro.
- **`actual_duration_s` not carried forward**. Scaffold already dropped them;
  every narration_text changed, so the recorded audio durations from the
  source build no longer match. Regenerating audio (Kokoro am_onyx) is a
  separate pass and will refill them.
