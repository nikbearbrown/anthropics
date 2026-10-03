# CONVERT-LOG — books--claude-liam-sales → nbb

Register conversion only. No render, no audio, no compile.

## Steps performed

- **Step 2 — Teardown register rewrite.** Every beat's `narration_text` rewritten
  in Feynman × MKBHD register. Machinery explained (what the bundle actually
  does, how each piece operates), design choices named ("optimize for the person
  who needs clients but never studied pipeline management", "no lock-in on
  infrastructure you don't have", "relevance over reusability", "reply rate, not
  volume"), trade-offs stated on their own terms ("works if you value the
  honesty; fails if what you actually needed was the coaching"). Facts preserved
  exactly — every claim, number, name, and mechanism in the source survives.
  All `shot`/`graphic` blocks, on-screen card copy, chip lists, and captions
  preserved verbatim per the SKILL preservation rule (siblings show the scaffold
  intentionally keeps HAI-cream visual props even under `palette: "teardown"`).

- **Step 3 — LLM exercise beat, second-to-last.** BHTF (already the handoff
  slot) transformed into the LLM exercise beat: `act` → `"LLM EXERCISE"`; added
  the `llm_exercise: { prompt, dig_deeper }` block; extended narration to
  include "Go deeper: after the call, hand the model your raw notes and ask it
  to draft the follow-up email — then compare its draft against what you'd have
  written cold, and name what actually changed." Existing `ClaudeComposerAsk`
  visual retained (it IS the paste-ready-in-Claude visual the SKILL asks for);
  `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…" to
  match the frontier-LLM neutrality the exercise requires.

- **Step 4 — NikBearBrown outro, last.** BOUT rewritten. `narration_text` and
  Remotion `line` prop now: "Claude, Closing — the sales plugin. Liam, in for
  Bear. More reels at brutalist.art." (default channel per SKILL, no AUTHOR.MD
  in the book folder). `handle` prop switched from `@HumanitariansAI` to
  `@NikBearBrown` (nbb outro-brand override, only place channel branding
  changes).

- **Step 5 — Ending order verified.** … NB18 → BCRY (carry-out) → BHTF (LLM
  exercise) → BOUT (nbb outro). 22 beats total, same as source.

- `_variant_todo` removed.

## Judgement calls

- **Preserve BHTF's beat_id and its Remotion `ClaudeComposerAsk` visual** rather
  than inserting a new `B_LLM` CARD beat. The nbb SKILL shows `B_LLM` as a
  schema example (CARD-motion-hold), but this source's `hai-simple` handoff
  already had a purpose-built LLM-prompt scene in exactly the same slot. Adding
  a second B_LLM would have duplicated the visual and violated the "preserve
  every beat_id" rule. Ruling: BHTF's role IS the LLM exercise; upgrade it in
  place with the required `llm_exercise` block + "Go deeper" tail. The
  ClaudeComposerAsk is a legitimate implementation of "a paste-ready prompt for
  Claude, ChatGPT, or Gemini."

- **Preserved shot-block visual props (`bg: #F3EBDD`, chip colors, folderLabel
  `@HumanitariansAI`, `ground` metadata, `style_preset: "humanitarians"`).**
  The SKILL preservation rule explicitly names shot blocks; siblings show the
  scaffold does not repaint props even under `palette: "teardown"`. The
  metadata `palette: "teardown"` remains the declared render palette; any
  actual repaint is a downstream concern.

- **Outro handle changed to `@NikBearBrown`** while other channel/folder labels
  stayed HAI. Step 4 explicitly says "add/replace the final beat with the
  NikBearBrown outro" — the outro is the one authorized brand-swap. Rest of the
  sheet's channel labels remain as scaffolded.

## Sanity numbers

- 22 beats total (matches source).
- Ending order: BCRY (carry-out) → BHTF (LLM exercise) → BOUT (outro). ✓
- `llm_exercise` object present on BHTF only. ✓
- Total `estimated_duration_s` ≈ 395s (~6:35). Longer than the source's ~230s
  measured total because Teardown register runs denser prose per beat; Kokoro
  will measure real durations at build time.

Done. Nothing rendered.
