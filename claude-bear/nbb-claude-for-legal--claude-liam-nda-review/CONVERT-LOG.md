# CONVERT-LOG — nbb-claude-for-legal--claude-liam-nda-review

Source: `../claude-for-legal--claude-liam-nda-review/beat_sheet.json`
Converted: 2026-09-03

## What changed

- Rewrote all 5 body-beat narrations (B00, B01, B02, B03, BCRY) in the Teardown
  register. Explained the machinery of a working NDA review (three parts:
  clauses in / baseline of standard terms / flag list out) and named the design
  choice at each step. Called out the honest gap: a baseline scan detects what's
  *off* in the text and cannot detect what's simply *absent* from it — a
  competitor publishes something first, the clause that should have carved it
  out reads like an ordinary complete definitions section, nothing gets flagged.
  Named the trade-off in B03: the whole system is optimized to surface what
  deserves a lawyer's eye at the expense of ever giving you a straight yes.
- Facts unchanged: the three-parts mechanism (clauses / baseline of standard
  terms — definitions, carve-outs, duration, mutuality / flag list), the anchor
  (same confidentiality clause stamped FLAGGED → CHECKED across B02→B03), the
  both-directions payoff (nothing-flagged isn't nothing-wrong; heavily-flagged
  isn't automatically a bad deal), and the applicable-law dependency
  ("reasonable" carve-out / duration is a property of the clause plus the
  jurisdiction plus the deal, not the clause alone) all survive verbatim.
- Replaced BHTF from a CLI-style handoff into a proper **LLM EXERCISE** beat.
  Act renamed to `LLM EXERCISE`; `llm_exercise` block added with `prompt` +
  `dig_deeper`. The prompt is paste-ready for any frontier LLM (Claude /
  ChatGPT / Gemini) and produces useful output on its own: the viewer pastes an
  actual NDA and gets three separate outputs — (1) carve-out coverage check
  against the four standard carve-outs, (2) unusual-clause flag list against a
  standard mutual-NDA baseline, (3) the specific questions to bring a lawyer,
  because "reasonable" isn't a property of the clause alone. The prompt
  explicitly bars the model from telling the user whether to sign — that's the
  video's carry-out, and hardcoding it into the exercise reinforces it. Dig-
  deeper flips the exercise into a redline generator: paste the NDA back in,
  ask for track-changes edits that close every gap, hand that to the other
  side or the lawyer.
- Rewrote BOUT (line and narration): "Does a Clean NDA Review Mean It's Safe
  to Sign? Not until the flagged clauses get checked. Liam, in for Bear." —
  title + one-line carry-out + Liam sign-off, matching the sibling
  nbb-claude-for-legal reel's outro pattern (`nbb-…-ip-clause-review`).
- Updated `WantQuote.quote` (BCRY) to match the rewritten carry-out narration
  exactly; sparkLine "Flagged isn't checked." kept — still the right anchor.
- Updated `ClaudeComposerAsk.command` (BHTF) to the shortened composer-form of
  the same LLM prompt (line-length constraint on the composer scene means the
  narration carries the full three-part prompt; the composer shows a condensed
  version).
- Removed `_variant_todo` from metadata. Left the scaffold-set fields
  (`audience`, `register`, `engine`, `voice_kokoro`, `palette`) untouched.
- Bumped `estimated_duration_s` on the beats that grew — B01 24→28, B02 18→24,
  B03 22→34, BCRY 8→10, BHTF 21→65, BOUT 6→8. Kokoro re-measures at audio
  time; these are hints only.

## Judgement calls

- **B00 word budget.** BrutalistHesitantWriter TIMING LAW says 20–35 words.
  Source was 32; my rewrite is 32. Preserved the "CLEAR → REVIEW" correction
  moment — the writer's `text`, `triggerWords`, `replacementWords` props are
  untouched.
- **BCRY = narration = quote.** The `WantQuote.quote` prop must match the
  spoken line exactly (sibling nbb reel enforces this). Kept both to the
  rewritten two-sentence version — "a first pass, not a verdict" is a cleaner
  Teardown-register phrasing than the source "isn't a green light" cliché.
- **Handle stayed `@HumanitariansAI`** — matched sibling nbb-legal reel, which
  keeps the source channel on OutroCTA even after Teardown-register conversion.
  If the intent is a NikBearBrown-channel post, the human can flip `handle` at
  post-time.
- **LLM prompt shape.** Video's whole subject is "an NDA review that flags
  nothing isn't proof of safety; a heavily flagged one isn't proof of trouble;
  the actual check is a human against applicable law." Built the exercise
  around that same shape but reframed as work the viewer does with their own
  NDA and any frontier LLM — no proprietary skill file required. Deliberately
  told the model *not* to say whether to sign, so the exercise reinforces the
  video's carry-out instead of undercutting it.
- **Composer command length.** ClaudeComposerAsk renders the command as
  on-screen text, so I shortened it to the essentials (three numbered outputs,
  same order) while the narration carries the full paste-ready prompt. Same
  practice as the sibling reel.
- **Metadata kept.** Preserved everything `brand_variant.py` set —
  `audience: NikBearBrown`, `register: Teardown`, `palette: teardown`,
  `engine: kokoro`, `voice_kokoro: am_onyx`, `outro_source`, `typography`,
  `derived_from`. Left the pre-existing `brand: claude-liam`, `style_preset:
  humanitarians`, and `ground: #F3EBDD` alone — sibling nbb reel does the same
  (the teardown *palette* is set; downstream `ground` and `style_preset`
  survive because they're a downstream compile concern, not a register/voice
  concern).

Done. Not rendered, not compiled, no audio generated. Next pass:
`generate_audio_kokoro.py` → compile.
