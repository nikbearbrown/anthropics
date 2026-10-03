# CONVERT-LOG — financial-services--claude-liam-gl-recon (nbb)

Converted `beat_sheet.json` (Plain register) → `beat_sheet.nbb.json` (Teardown
register). Voice-only rewrite — every number, name, API, and claim from the
source survives unchanged.

## What changed

- **Register rewrite (B00–B07):** every narration_text re-voiced in Teardown
  (Feynman × MKBHD). Take-it-apart openings, mechanism named as
  three-steps-in-fixed-order, design choice named ("optimized for
  reproducibility, not detective work"), trade-off named explicitly on B05
  ("The payoff… The trade-off…").
- **BCRY (CARRY-OUT):** narration and on-screen quote unchanged — the sentence
  is on-screen card copy and already fits the Teardown register (bare
  mechanism, no fluff).
- **BHTF → LLM EXERCISE:** converted the existing "your turn handoff" beat
  into the second-to-last LLM exercise beat. Added `llm_exercise` object with
  `prompt` (the paste-ready Claude/ChatGPT/Gemini prompt already in the shot
  `command` prop) and `dig_deeper` (a real next question about what gl-recon
  does when GL and subledger disagree at both position and transaction level).
  Narration extended to speak the "Go deeper:" follow-up out loud. Act
  relabeled `LLM EXERCISE`. Estimated duration bumped 23 → 32s to fit the
  added follow-up sentence; audio-first pass will re-clock.
- **BOUT (outro):** left as-is. Line already reads "Claude, Gl Recon. Liam,
  in for Bear." — IN-FOR-BEAR LAW compliant. Ordering is correct: BHTF (LLM
  exercise) is second-to-last, BOUT is last.
- **Metadata:** `_variant_todo` removed. `register` was already "Teardown" and
  `palette` "teardown" from the scaffold — untouched. `purpose` rewritten to
  match the Teardown framing (explain machinery + name the design choice + judge
  the trade-off) rather than the Plain "answer one real question" framing.

## Judgment calls

1. **BHTF instead of new beat.** SKILL.md §Step 3 says "insert one beat" for the
   LLM exercise, but the source already carried BHTF — a "your turn" beat whose
   `ClaudeComposerAsk` shot already displays a paste-ready prompt. Inserting a
   second LLM-flavoured beat would have made the ending "prompt → prompt → outro"
   with no visual variation. Converting BHTF preserves the beat count (11/11),
   keeps the working visual, adds the `llm_exercise` object the schema wants, and
   speaks the "Go deeper" follow-up out loud so the second half is authored, not
   merely metadata.
2. **BCRY quote unchanged.** The `quote` prop drives the on-screen carry-out
   card; SKILL.md preserves on-screen card copy that fits the register, and this
   sentence does (direct mechanism, one em-dash, no fluff).
3. **Channel handle unchanged (`@HumanitariansAI`).** Scaffold wrote
   `audience: NikBearBrown` but did not touch `channel_title` / `folderLabel` /
   `playlist`. brand spec nbb.md says the NBB default channel is
   `www.brutalist.art`, but there is no book-level AUTHOR.MD available here and
   the scaffold's decision to leave the channel fields alone reads as
   intentional (this reel lives under `claude-bear/`, aimed at the same audience
   as the HAI source). Left the outro handle as scaffold set it. If a later pass
   wants brutalist.art on the outro card, it's a single-field flip.
4. **Shot color arrays left at humanitarians hex (`#F3EBDD` /
   `#2F2A26` / `#E4572E`).** The metadata `palette: "teardown"` is what the
   renderer keys off; the per-shot `colors` arrays are the humanitarians ground
   the Manim scenes were built for. Re-toning those to strict teardown
   (`#FFFFFF` / `#2A1A0E` / `#C8102E`) would re-scaffold the shot blocks, which
   the invocation forbids. Rendering pass can decide.
