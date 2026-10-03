# CONVERT-LOG — nbb cut of `claude-for-legal--claude-liam-leave-tracker`

Converted 2026-09-03. Source: `../claude-for-legal--claude-liam-leave-tracker/beat_sheet.json` (Plain / hai-fellows, 8 beats). Output: this dir's `beat_sheet.nbb.json` (Teardown, 7 beats). Source beat sheet untouched.

## What changed

- **Register:** every `narration_text` rewritten Feynman × MKBHD per `prose/teardown/PROSE.md`. Facts, numbers, and mechanism preserved verbatim (accrual rules / eligibility windows / blackout dates; single-file SKILL.md; linear Steps section). Voice-only change.
- **B00 (cold open):** rebuilt on the "obvious guess is X — wrong branch — actual mechanism is Y" pattern so the wrong-guess word `APPROVE` still lands in the writer, then gets corrected to `check`. BrutalistHesitantWriter props unchanged.
- **B01–B03:** stripped hai-simple's naming-not-explaining phrasing; added the design-cost sentence to each (auditability, repeatability, "stays inside the written policy — costs judgment calls the policy didn't foresee, buys the same shape of report every time"). Remotion props unchanged.
- **BCRY:** carry-out expanded from a two-sentence lands-it into the standard nbb WantQuote form — names what Claude IS doing (running the list against accrual / eligibility / blackout), then hands the approval decision back. `WantQuote.quote` and `sparkLine` updated to match the new narration.
- **BHTF → LLM EXERCISE (second-to-last):** promoted from the hai-simple "Your Turn" handoff to the nbb LLM-exercise contract. Added the `llm_exercise` object (paste-ready `prompt` + `dig_deeper` follow-up). Narration reads out the whole prompt with cadence, closing on "Go deeper: …". `ClaudeComposerAsk.command` shortened to a screen-fitting version; `folderLabel` swapped from `@HumanitariansAI` to `@NikBearBrown` per audience.
- **BOUT + BCTA → BOUT (last):** collapsed the source's `OutroSeries` + `OutroCTA` pair into a single `OutroCTA` beat matching the nbb sibling `nbb-claude-for-legal--claude-liam-ip-clause-review` — one line, title + one-clause carry-out + "Liam, in for Bear." Handle swapped to `@NikBearBrown`.
- **Metadata:** `register` Plain → Teardown; `palette` humanitarians → teardown; `build.filled`/`of` 8 → 7 (outro collapse); `_variant_todo` removed. Kept `style_preset:"humanitarians"` and `ground:"#F3EBDD"` because the scaffold set them and the Remotion patterns already reference them — teardown palette here means the register + type/accent are teardown, on the cream ground the scaffold established. `engine` and `voice_kokoro` left exactly as scaffolded (kokoro / am_onyx).

## Judgement calls

1. **Outro collapse (BOUT + BCTA → single BOUT).** SKILL.md says "add/replace the final beat with the NikBearBrown outro" (singular). The one existing nbb sibling on disk (`ip-clause-review`) uses one `OutroCTA` with the full sign-off, not the source's two-beat Series+CTA. Went with the sibling pattern rather than keeping both slots; deleted BCTA.
2. **AUTHOR.MD scope.** No `AUTHOR.MD` sits under `books/anthropics/claude-bear/`. The nearest is `books/anthropics/youtube/ai-1/AUTHOR.MD` (channel `@NikBearBrown`, brutalist.art). Used that handle in the outro `handle` field and BHTF `folderLabel` — the outro content itself is the standard "title + carry-out — Liam, in for Bear" sign-off, not book-specific copy.
3. **Ground colour left as `#F3EBDD` (cream), not flipped to `#FFFFFF` (teardown flat white).** The BrutalistHesitantWriter and every other Remotion pattern here already reads `bg`/`ground` from the scaffold. Flipping to white would recolor B00 mid-conversion; the scaffold set `palette:"teardown"` on the metadata to change register and typography without repainting the ground. If the audit wants strict flat-white teardown ground, that's a separate palette pass — flagged, not silently changed.
4. **`estimated_duration_s` bumped** on B01 (16→20), B02 (10→18), B03 (16→22), BCRY (9→13), BHTF (24→60) to reflect longer Teardown narration. Not authoritative — narration is the master clock, and `generate_audio_kokoro.py` will overwrite `actual_duration_s` from the measured MP3 on the next audio pass.

## Not touched

Every `beat_id`. Every `shot.remotion.pattern`. Every existing Remotion prop except `WantQuote.quote/sparkLine` (BCRY), `ClaudeComposerAsk.topic/segment/command/folderLabel` (BHTF), and the outro `line/handle` (BOUT) — all downstream of the narration rewrite. No rendering, no audio, no compile.
