# CONVERT-LOG — nbb-claude-for-legal--claude-liam-log-leave

Converted `beat_sheet.json` (Plain / HAI-Simple) → `beat_sheet.nbb.json` (Teardown / NikBearBrown).
No render, no audio, no compile.

## What changed

- **Every narration_text rewritten in Teardown register.** Same facts, same claims,
  same beat structure — just re-voiced (Feynman × MKBHD): take it apart, name the
  mechanism, name the trade-off. Kept every beat_id and every `act` label.
  - B00 cold open — mechanic language ("watch 'approves' get corrected to 'logs'"),
    word count trimmed to fit WRITER LAW (20–35 words + lead_silence 0.8).
  - B01–B07 — "Here's what's actually happening…" openings, "the design choice /
    trade-off" framing on B05, "the file is the program; Claude is the interpreter"
    on B04, "the value is uniformity, not intelligence" close on B06, "the behavior
    tells you about the checklist, not the situation" close on B07.
  - BCRY — carry-out re-tightened; **on-screen WantQuote `quote` prop updated to
    match the new narration verbatim** (they read as one).
  - BHTF — "your turn" rewrite; **ClaudeComposerAsk `command` prop updated to match
    the new narration's paste-ready prompt** so the on-screen text and the voice line
    up.
- **B_LLM inserted as SECOND-TO-LAST** (between BHTF and BOUT), per
  `skills/make/nbb/SKILL.md` §Step 3. A structured `llm_exercise` field carries the
  paste-ready `prompt` (three-part walk-through of skill mechanics) and the
  `dig_deeper` follow-up (system-prompt vs SKILL.md, and why the designers
  separated them). Shot: ClaudeComposerAsk (same pattern as BHTF for on-screen
  consistency), folderLabel `@NikBearBrown`.
- **BOUT (LAST) retargeted to the NikBearBrown channel.** `handle` →
  `@NikBearBrown`; narration keeps the IN-FOR-BEAR sign-off ("Liam, in for Bear")
  and adds the default NBB channel plug ("www dot brutalist dot art") per
  `brands/nbb.md`. Line prop unchanged apart from the handle underneath.
- **Channel identity fields flipped from HAI to NBB** where they're user-facing:
  `metadata.channel_title`, `metadata.folderLabel`, `BHTF.props.folderLabel`,
  `BOUT.props.handle` all → `@NikBearBrown`. `playlist: "Claude Basics"` left
  alone — it's an editorial tag, not a channel identity.
- **`_variant_todo` removed** from metadata (all five items done).
- **`metadata.purpose` rewritten** so it describes the Teardown cut, not the
  Plain-register source (mechanism + design trade-off + carry-out, in that order).

## Judgement calls

- **Kept BHTF and added B_LLM alongside, rather than replacing BHTF.** SKILL.md says
  "Insert one beat before the outro" — not replace. BHTF stays as the personal
  "your turn" ("write a SKILL.md for a record *you* log"); B_LLM adds the deeper
  mechanics probe ("what actually happens when a skill executes; system prompt vs
  SKILL.md"). Two adjacent paste-prompts risk feeling bloated, but the angles are
  distinct enough (application vs mechanism) that I let both stand. If a later pass
  wants to collapse them, B_LLM is the one to keep (structured `llm_exercise`
  schema, deeper question).
- **Left shot/graphic blocks and rendered media paths intact** (colors arrays,
  Manim scene names, chip contents, BrutalistHesitantWriter bg `#F3EBDD`). The
  scaffold flipped `palette: "teardown"` in metadata but left the visual props on
  the HAI cream — I did not retint them because the SKILL says preserve shot
  blocks, and downstream compile/render (a separate pass) is where any palette
  retinting belongs. `metadata.ground` is still `#F3EBDD`, `style_preset` still
  `humanitarians`; both are inherited from the scaffold and left for the render
  pass to decide.
- **Updated on-screen text only where it must match the rewritten narration**
  (BCRY quote, BHTF command). Every other on-screen chip, label, and caption
  already reads Teardown-clean and was preserved.

## Not done (deliberately)

- No audio regenerated.
- No compile / no `art run` / no `remotion_scenes.py`.
- No touch to the source reel at
  `anthropics/claude-for-legal/youtube/claude-liam-log-leave/`.
