# CONVERT-LOG — claude-basics--claude-constitution-one-narrow-safety-rule-make

Converted from `../claude-basics--claude-constitution-one-narrow-safety-rule-make/beat_sheet.json`
(Plain register, hai-simple) into `beat_sheet.nbb.json` (Teardown register, NBB cut).
No renders, no audio, no compile.

## What changed

### 1. Register rewrite (voice only, facts intact)

Every beat's `narration_text` rewritten in the Teardown register (Feynman ×
MKBHD): take it apart, explain the machinery, reveal the design philosophy,
judge the trade-off.

- **B00** (cold open) — added "Liam, in for Bear" up front so the IN-FOR-BEAR
  LAW is honoured at the cold open (source only signed off at BOUT). Held word
  count to 35 to keep the TIMING LAW window (20–35 words + 0.8s lead) so the
  BrutalistHesitantWriter typing has ≥9s to hit the `behavior → identity`
  correction on a late frame. Remotion props left untouched.
- **B01** — reframed the "safety rule as patch" assumption as a design bet
  ("clean, minimal, engineer-friendly") and then broke it, per the Teardown
  register.
- **B02** — added "here's what's actually happening under the hood" + named
  "the design cost of the rule" as a belief-about-identity quietly attached to
  the training objective.
- **B03** — explained the mechanism directly, then labelled the ONE FLAG
  precisely: "identity" is the shape the generalization takes, not a variable
  anyone has found in the network.
- **B04** — named the trade-off in Teardown terms: identity-shaped rules
  generalize (feature) *and* leak (cost). Kept the same first-aid example.
- **BCRY** — narration kept **verbatim**. It's a WantQuote card and the
  on-screen quote must match the read; the source line already reads as
  Teardown (crisp, mechanism-revealing) so preserving it satisfies the
  "on-screen card copy that still fits the register" rule.

### 2. LLM exercise (BHTF, second-to-last)

BHTF was the source's `your turn handoff` beat with a paste-ready
ClaudeComposerAsk prompt. Repurposed as the LLM exercise beat:

- `act` renamed `your turn handoff` → `LLM EXERCISE`.
- Added the structured `llm_exercise: { prompt, dig_deeper }` block per
  SKILL.md §Step 3.
- Rewrote the narration so it (a) frames the prompt as pasteable into
  Claude / ChatGPT / Gemini, and (b) ends with a real "Go deeper: …"
  follow-up — rewrite the same rule as a narrow situational trigger with no
  identity reason, and predict which behaviors would still generalize vs.
  stay contained. Genuinely explorable, not a summary.
- `estimated_duration_s` bumped 24 → 30 to reflect the longer read.
- ClaudeComposerAsk props left untouched (shot block preserved).

### 3. NikBearBrown outro (BOUT, last)

Kept the source OutroCTA and its `line` (the video title + "Liam, in for
Bear."). Only change: `handle` switched `@HumanitariansAI` → `@NikBearBrown` so
the closing plate matches the NBB brand per SKILL.md §Step 4 and AUTHOR.MD ::
NikBearBrown. Rest of the shot preserved.

### 4. Metadata

- `register`: `Plain` → `Teardown`.
- `purpose`: language updated to "Teardown register" (facts unchanged).
- `_variant_todo`: removed (all four items satisfied).
- `audience`, `outro_source`, `derived_from`, `typography`, `palette`,
  `engine`, `voice_kokoro`: left exactly as the scaffold set them.
- Everything else (channel_title, folderLabel, playlist, ground, anchor_pair,
  one_flag, gate_c/h, build metadata) preserved verbatim.

## Judgement calls

- **B00 word budget.** The BrutalistHesitantWriter TIMING LAW (per the beat's
  own `note`) requires 20–35 words to give typing ≥9s. Added the Liam sign-in
  at the cold open (IN-FOR-BEAR LAW) *and* stayed at 35 by cutting a
  "changes" and tightening the last clause. Not ideal — tight against both
  ceilings — but it satisfies both laws.
- **BCRY preserved verbatim.** The WantQuote card bakes the quote as a prop;
  narration and card have to agree. The source quote already reads as
  Teardown (mechanism, cost, no filler), so rewriting it just to rewrite
  would break the card contract without register benefit.
- **BOUT handle switched, line kept.** SKILL.md §Step 4 says the outro
  becomes the NikBearBrown outro. The full `line` is the video title, which
  survives across cuts; only the channel handle changes. Kept OutroCTA
  (not adding a second OutroSeries beat as the reference nbb-splitting-chunk
  reel did) because the source only has a single outro beat and the SKILL.md
  contract is "add/replace the final beat", not "expand it."
- **ClaudeComposerAsk `folderLabel: @HumanitariansAI` on BHTF left untouched.**
  Shot blocks are preserved by rule; the composer chip reflects where the
  viewer is pasting the prompt from (the HAI feed context), not the outro
  brand.
