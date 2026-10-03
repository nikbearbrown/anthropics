# CONVERT-LOG — claude-for-legal--claude-liam-gaps → nbb

Register: Plain (Liam/HAI) → **Teardown** (Feynman × MKBHD, Liam in for Bear).

## What changed

- **Every beat's `narration_text` rewritten** in the Teardown register. Same
  argument, same facts (gaps = single SKILL.md; open a tracker, report
  what's flagged and not yet closed, update on close/risk-accept; read
  top-to-bottom, no branching unless the file says branch; consistency payoff
  vs. off-the-map cost). Voice moved to: "machinery down… the execution model
  is dead simple… that trade-off cuts two ways… what you're actually buying
  is consistency… what you're evaluating is the fit between the routine and
  the situation." No new facts. No fabrication.
- **`_variant_todo` removed** from metadata.
- **`BHTF` promoted to the LLM EXERCISE beat** (SKILL.md Step 3):
  - `act` → `"LLM EXERCISE"`.
  - Narration extended with the "Paste this into Claude, ChatGPT, or Gemini"
    framing and a real "Go deeper" follow-up that pushes the viewer to probe
    the seam where a codified skill quietly starts inventing judgment.
  - `llm_exercise` block added (`prompt` + `dig_deeper`) matching the SKILL.md
    schema; existing `ClaudeComposerAsk` prop set left intact (the on-card
    command already reads exactly like the paste-ready prompt).
  - `estimated_duration_s` bumped 20 → 33 to match the longer narration.
- **`BOUT` left as the NBB outro**: `OutroCTA` with
  `"Claude, Gaps. Liam, in for Bear."` and handle `@HumanitariansAI`. Already
  the NBB outro pattern; no rewrite needed.
- **`BCRY` narration and `WantQuote.quote` prop kept identical** — the carry-out
  sentence is already Teardown-clean, and both fields must match.

## Judgement calls

- **Kept `BrutalistHesitantWriter` on B00, not `ClaudeComposerAsk`.** SKILL.md's
  ask/intro rule prefers `ClaudeComposerAsk` for new NBB sheets, but the source
  is a hai-simple reel whose cold-open visual arc (typing "learned" → correcting
  to "was given") is the whole rhetorical move here. Swapping to the composer
  would break the "wrong branch → real question" gag the whole reel pivots off.
  Preserved per the instruction's "shot blocks stay" rule; matches how the
  earlier `nbb-…-ip-clause-review` conversion handled its B00.
- **Kept `@HumanitariansAI` on BOUT and `folderLabel`, and the humanitarians
  cream ground `#F3EBDD`.** Metadata already sets `palette: "teardown"` +
  `style_preset: "humanitarians"` — this reel lives on the HAI channel; the NBB
  register is being applied without repainting the channel identity. Matches
  the sibling `nbb-…-client-letter` convention.
- **No source `AUTHOR.MD` exists at `anthropics/claude-bear/AUTHOR.MD` or the
  parent book paths.** The BOUT scaffold was already the standard "Claude,
  <Title>. Liam, in for Bear." NBB sign-off in `OutroCTA`, so I preserved it
  rather than invent unsourced outro copy. If a NikBearBrown AUTHOR.MD block
  turns up later, BOUT can be re-authored from it.
- **Bumped several `estimated_duration_s` values** where the Teardown rewrite is
  longer than the Plain source (B01, B02, B03, B04, B05, B06, B07). These are
  planning estimates — the real clock lands when Kokoro measures the MP3s.
