# CONVERT-LOG — nbb cut of claude-cookbooks--claude-liam-cookbook-audit

Converted from the Plain (hai-simple / claude-liam) source into the NikBearBrown
Teardown register per `skills/make/nbb/SKILL.md`.

## What changed

- **Rewrote narration on every beat** in the Teardown register — machinery
  named, design choice + trade-off called out, forbidden phrases avoided.
  Facts unchanged: three files (SKILL.md, style_guide.md, validate_notebook.py),
  twelve-kilobyte instruction set, three linear steps, anchor pair B02→B03,
  validate_notebook.py's three checks.
- **BHTF is now the LLM exercise beat** (second-to-last): `act` renamed to
  `LLM EXERCISE`, `llm_exercise.{prompt, dig_deeper}` block added per SKILL §Step 3,
  ClaudeComposerAsk `command` prop rewritten as a standalone paste-ready prompt
  (produces useful output without the video), `segment` set to "LLM Exercise",
  `folderLabel` moved to @NikBearBrown.
- **BOUT** narration + line + handle switched to the NikBearBrown outro
  (`@NikBearBrown`, "More teardowns at…"), IN-FOR-BEAR signoff preserved.
- **Removed** `metadata._variant_todo`.

## Judgement calls

- **Morphed the existing BHTF into the LLM exercise beat rather than inserting
  a new B_LLM.** BHTF was already a paste-ready-prompt-for-Claude your-turn
  handoff — functionally the same beat the SKILL asks for. Inserting a second
  one would have created a redundant your-turn moment. Preserved the `BHTF`
  beat_id per the "preserve every beat_id" rule.
- **Kept BCRY narration verbatim.** The WantQuote scene displays the exact
  carry-out sentence and the sentence is already Teardown-shaped — names
  the mechanism ("SKILL.md, a rubric Claude reads, applies, and checks…"),
  calls out the design choice ("isn't Claude forming its own opinion"). No
  rewrite needed; changing it would break the on-screen quote / narration
  alignment.
- **Preserved every `shot` block verbatim,** including humanitarians-palette
  colors (`#F3EBDD` ground, `#E4572E` accent) on Manim beats B01–B03 and
  BrutalistHesitantWriter on B00, per the SKILL's "preserve shot blocks"
  rule. `metadata.palette` is now "teardown"; compile pass owns any
  palette override at render time.
- **Left top-level `folderLabel` / `channel_title` / `playlist` /
  `style_preset` / `ground` untouched.** The scaffold left them alone; I only
  changed what the SKILL asked me to change. The NBB handle change is scoped
  to the beats that display it (BHTF composer footer, BOUT outro).

## Ending order (verified)

```
B00 → B01 → B02 → B03 → BCRY → BHTF (LLM exercise) → BOUT (NBB outro)
```

Second-to-last = LLM exercise. Last = NBB outro. ✓
