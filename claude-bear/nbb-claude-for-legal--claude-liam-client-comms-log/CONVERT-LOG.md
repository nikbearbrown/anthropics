# CONVERT-LOG — nbb-claude-for-legal--claude-liam-client-comms-log

Register conversion (Plain → Teardown) of the client-comms-log reel. Voice only;
every fact preserved. No render, no audio, no compile.

## What changed

- **metadata.register**: `Plain` → `Teardown`.
- **metadata.purpose**: rewritten to describe the Teardown framing (take the skill
  apart, name the design choice) — same landing carry-out.
- **metadata._variant_todo**: removed.
- **B00–B07, BCRY**: `narration_text` rewritten in the Teardown register
  (Feynman × MKBHD). Machinery-first ("Here's what's actually happening…",
  "The machinery is boring on purpose…"), design choice named explicitly at B05
  ("So the design choice is: a skill is a specification, not a memory. Payoff
  — X. Cost — Y."), forbidden phrases avoided. Every claim in the source is
  intact: same anchor pair (B03 planted → B06 paid off), same mechanism
  (top-to-bottom read, no branching unless the file says branch), same both-
  directions caveat at B07, same carry-out at BCRY.
- **BCRY WantQuote**: `quote` prop resynced to the rewritten narration;
  `sparkLine` changed from "Same file, same structure." to "Spec, not memory."
  to match the beat's design-choice framing. On-screen card copy that still
  fit the register (all Manim `production_viz` labels, chips, captions) left
  untouched.
- **BHTF**: recast from "your turn handoff" to the nbb `LLM EXERCISE` beat.
  `act` → `LLM EXERCISE`; added `llm_exercise` object with `prompt` +
  `dig_deeper`; narration reads the prompt aloud then a "Go deeper: …"
  follow-up. ClaudeComposerAsk `command` prop resynced to the new prompt.
  Prompt derives from the whole video's subject (a skill is a
  spec-not-memory): viewer picks a recurring record, gets a SKILL.md written
  in numbered steps, then makes the model read it back and narrate what it
  will do *before* it does anything — the same "read before it starts"
  mechanic the reel teaches. Dig-deeper pushes on where a SKILL.md silently
  assumes human judgment.
- **BOUT**: outro reworded from bare title + persona line to the
  sibling-nbb pattern ("Title — tagline. Liam, in for Bear."), matching
  e.g. `nbb-books--claude-liam-building-plugins` ("Claude, Built —
  building your own plugins. Liam, in for Bear.").

## Judgement calls

- **Outro handle stays `@HumanitariansAI`** rather than routing to
  `www.brutalist.art` (the default nbb channel in `skills/make/nbb/SKILL.md`
  §Step 4). Every sibling `nbb-*` reel in `anthropics/claude-bear/` keeps
  `@HumanitariansAI` — matched the local convention. If the channel needs
  to flip to brutalist.art, it's a one-line `handle` swap on BOUT.
- **On-screen card copy left alone**: Manim `production_viz` labels/chips
  are terse and still fit the Teardown register ("NOTHING TO FORGET",
  "SPEC, NOT MEMORY", "READ, THEN FOLLOW IN ORDER"). Rewriting them would
  invalidate the existing `manim/*.mp4` renders for no register gain.
- **Graphic palette hexes left as humanitarians** (`#F3EBDD` ground,
  `#2F2A26` ink, `#E4572E` accent) inside the beat `graphic.colors` arrays,
  matching sibling `nbb-*` reels in this book. Metadata `palette` is
  `teardown` per the scaffold. If a true teardown recolor is wanted
  (`#FFFFFF` / `#2A1A0E` / `#C8102E`), it's a separate re-render pass on
  the Manim beats — not a beat-sheet rewrite.
- **B00 word count**: kept in the 30–35-word window the note flags
  (>=9s typing window with `lead_silence_s: 0.8`). Original was 40 words;
  new is 33 — still supports the correction ("remembers" → "logs") beat.
