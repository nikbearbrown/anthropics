# CONVERT-LOG — nbb-healthcare--claude-liam-icd10-cm-skill

Converted `beat_sheet.json` (HAI-simple, Plain register, @HumanitariansAI) into
`beat_sheet.nbb.json` (Teardown register, @NikBearBrown, Liam in for Bear).

## Narration rewrites (voice only, facts unchanged)

- **B00 cold open** — Teardown-register recast of the diagnose-vs-code pivot ("Feed
  Claude a clinical note and the setup sounds like a diagnosis is coming. It isn't
  …"). Held to the ~32-word count so BrutalistHesitantWriter's TIMING LAW still
  applies (20–35 words + 0.8 s lead → ≥9 s typing window). Every prop, seed, trigger
  word and correction on the writer panel preserved verbatim.
- **B01 anatomy** — Same file tree, same callouts, same spark line. Narration now
  names the design bet: "the file IS the program, and you can read every line before
  you trust it."
- **B02 pipeline** — Adds the trade-off explicitly ("They optimized for a predictable
  pipeline at the expense of any freelance reasoning about the patient"). Phase cards
  untouched.
- **B03 mechanism** — Kept the one-line rule ("code only what's already documented");
  added the MKBHD ecosystem line ("This works if you value a coder who never
  overreaches; it fails if you were hoping the model would do the doctor's thinking
  for you").
- **BCRY carry-out** — Narration preserved verbatim; it's also the on-screen quote.
  Per SKILL.md, on-screen card copy that still fits the register stays exactly as
  written.

## BHTF → LLM EXERCISE (rebuilt in the NBB pattern)

The source's `BHTF / your turn handoff` was already a paste-ready prompt, so it
converted cleanly into the LLM EXERCISE beat rather than needing a fresh insertion.

- `act` → `LLM EXERCISE`.
- Added the `llm_exercise` object with `prompt` (three numbered parts: define the
  code-vs-diagnose line, list explicitly-documented codeables from the same clinical
  note, list tempting inferences that must NOT be coded) and `dig_deeper` (draft the
  physician query needed to get an inferred diagnosis documented and codeable next
  pass).
- Narration mirrors the prompt and appends the "Go deeper: …" line, per Step 3 of
  the SKILL.
- ClaudeComposerAsk props: `folderLabel` swapped to `@NikBearBrown`; `topic`
  trimmed to `ICD10-CM-SKILL · ANTHROPIC SKILL` (dropped the "· YOUR TURN"
  suffix — matches the reference nbb reel pattern); `segment` set to
  `Coding, Not Diagnosing.` (already on-screen as the BCRY sparkLine, no
  fabrication); command tightened for legibility on the composer card.
- `beat_id` preserved (`BHTF`) per SKILL rule.

## BOUT outro

Kept the outro's `line` verbatim (`Claude, Icd10 Cm Skill. Liam, in for Bear.`) —
it's the source's on-screen title readout and the reference nbb reels preserve
title phrasing. Swapped `handle` from `@HumanitariansAI` to `@NikBearBrown` to
match the NikBearBrown channel and the NBB outro contract.

## Metadata

- `folderLabel` / `channel_title` → `@NikBearBrown` (was `@HumanitariansAI`).
- `purpose` rewritten in Teardown terms (names the design bets: folder-as-program,
  linear Steps pipeline, one-line documentation rule; keeps the same carry-out).
- `_variant_todo` removed (all four items executed).
- Everything else `brand_variant.py` set (`audience`, `register`, `palette`,
  `engine`, `voice_kokoro`, `typography`, `outro_source`) left as scaffolded.

## Judgement calls

1. **Segment string on the composer card.** Reference nbb reels use a short punchline
   phrase (e.g. "Cached, Not Free.") rather than the full metadata title. Chose
   `Coding, Not Diagnosing.` — the BCRY sparkLine, so it's already on-screen and
   not a fabrication.
2. **Outro line left as source phrasing.** "Claude, Icd10 Cm Skill." is awkward as a
   spoken tagline but it's the source's on-screen title. Preserving it stayed inside
   the "change the voice, not the facts / on-screen card copy" rule; a cleaner
   rephrase would be a title change, not a register change.
3. **B00 word count.** Held to 32 words so BrutalistHesitantWriter's TIMING LAW still
   satisfies the ≥9 s typing window that the beat's `note` field guards.
