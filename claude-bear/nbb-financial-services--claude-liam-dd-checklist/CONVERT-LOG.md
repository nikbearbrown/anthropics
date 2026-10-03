# CONVERT-LOG — nbb-financial-services--claude-liam-dd-checklist

Converted from `../financial-services--claude-liam-dd-checklist/beat_sheet.json`
(Plain / hai-simple / claude-liam) → `beat_sheet.nbb.json` (Teardown / nbb /
Liam-in-for-Bear). No rendering, no audio.

## What changed

- **Narration (every beat)** rewritten from Plain → Teardown register per
  `runtime/prose/teardown/PROSE.md` + `brands/nbb.md`. Machinery first, then the
  design choice and its trade-off — no fabrication, every fact from the source
  preserved (three-input read: sector / deal type / complexity; workstreams pulled
  from templates; four states requested → received → reviewed → flagged;
  software-acquisition anchor with the customer-contracts revenue-concentration
  flag; run-twice reproducibility; mineral-rights-transfer as the miss).
- **B00** trimmed to hold the 20–35 word TIMING LAW so the BrutalistHesitantWriter
  correction ('judgment' → 'the file') still lands before the beat ends.
- **BCRY** WantQuote `quote` prop updated to mirror the rewritten carry-out
  sentence (`flags` → `escalates` — same claim, keeps parity with the narration
  above and the B03 phrasing).
- **BHTF re-cast as the LLM EXERCISE beat (second-to-last)** rather than
  inserting a new beat. Judgment call: the source's BHTF was already a
  paste-ready ClaudeComposerAsk with a "Your turn" prompt — inserting a fresh
  BLLM alongside it would have duplicated the same role. Keeping BHTF preserves
  its render infrastructure (ClaudeComposerAsk / `media/BHTF.mp4`); the beat now
  carries the full `llm_exercise` schema (`prompt` + `dig_deeper`), the narration
  ends on a "Go deeper:" follow-up per SKILL.md Step 3, and the on-screen
  `command` was tightened into a self-contained paste-ready LLM prompt that
  works without the video.
- **BOUT** rewritten as the NikBearBrown outro — title re-read + "Liam, in for
  Bear" (IN-FOR-BEAR LAW) + `brutalist.art` CTA. Handle flipped @HumanitariansAI
  → @NikBearBrown.
- **Metadata** touched to match the NBB audience the scaffold declared:
  `brand: claude-liam` → `nbb`; `folderLabel` and `channel_title`
  @HumanitariansAI → @NikBearBrown; `playlist` → "Anthropic Skills — Teardown".
  `_variant_todo` removed. `audience`, `register`, `palette`, `engine`,
  `voice_kokoro`, `outro_source`, `typography`, `derived_from` left exactly as
  `brand_variant.py` set them.

## What did not change (deliberately)

- **Shot / graphic props** — BrutalistHesitantWriter styling (`ink`, `accent`,
  `bg`, hesitation params), `production_viz.colors` arrays on B01/B02/B03,
  Manim scene names (`DDCB01Scene`, `DDCB02Scene`, `DDCB03Scene`), all
  `rendered.out` paths, and the `build` blocks. The sheet declares
  `palette: "teardown"` but the visual colors are still the HAI ground/ink/
  terracotta triple from the source. Retinting is a render-pass concern (the
  Manim scenes and the Remotion component may or may not honor prop overrides
  without their own edits); the register conversion pass leaves them alone
  rather than risk silently breaking a re-render.
- **Beat IDs**, `act` labels other than BHTF, `audio_file` paths, `metadata.build`
  provenance, `gate_c`, `gate_h`, `anchor_pair`, `source_sheet` all preserved.

## Verified

- `python3 -c 'import json; json.load(open(...))'` — valid JSON.
- Ending order: `… BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`.
- `llm_exercise.prompt` + `llm_exercise.dig_deeper` present on the
  second-to-last beat.
- `_variant_todo` absent.
- Every beat's `narration_text` rewritten in Teardown register.
