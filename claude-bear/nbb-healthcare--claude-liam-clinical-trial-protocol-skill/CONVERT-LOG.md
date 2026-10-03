# CONVERT-LOG — healthcare--claude-liam-clinical-trial-protocol-skill (nbb)

Converted `beat_sheet.json` (Plain register) → `beat_sheet.nbb.json` (Teardown
register). Voice-only rewrite — every fact, name, file-count, and claim from the
source survives unchanged.

## What changed

- **Register rewrite (B00, NB01–NB03):** every `narration_text` re-voiced in
  Teardown (Feynman × MKBHD). B00 opens with the reflex the audience arrives
  with ("Claude is picking the endpoints, sizing the arms…") and names the
  wrong verb before landing the real one. NB01 puts the "file is the program"
  mechanism in one line. NB02 names the design choice: "They optimized for
  reproducibility." NB03 names the trade-off explicitly: "you lose adaptive
  judgment, you buy a document you can review the same way twice."
- **BCRY (CARRY-OUT):** narration and on-screen quote unchanged — the sentence
  is `WantQuote` card copy that already reads in the Teardown register (bare
  mechanism, one em-dash, no fluff). Per SKILL.md: preserve on-screen card copy
  that still fits.
- **BHTF → LLM EXERCISE:** the source's "your turn handoff" beat is the natural
  home for the LLM exercise — its `ClaudeComposerAsk` shot already displays a
  paste-ready prompt. Converted in place: `act` relabeled `LLM EXERCISE`,
  `llm_exercise` object added with `prompt` (a paste-ready
  Claude/ChatGPT/Gemini prompt that produces a useful walkthrough on its own)
  and `dig_deeper` (a genuinely explorable follow-up about which sections the
  skill composes vs. which trial-design decisions it structurally leaves open).
  Narration extended to speak the "Go deeper:" follow-up out loud. The shot's
  `command` prop was updated to match the new prompt (on-screen text has to
  match the narration or the video says one thing and shows another).
  `estimated_duration_s` 26 → 40 for the added prompt + follow-up; audio-first
  pass will re-clock.
- **BOUT (outro):** left as-is — line already reads "It Drafts the Protocol.
  It Doesn't Decide the Trial. Liam, in for Bear.", IN-FOR-BEAR LAW compliant,
  `OutroSeries` scene preserved.
- **Metadata:** `_variant_todo` removed. `register` was already `Teardown` and
  `palette` `teardown` from the scaffold — untouched. `purpose` rewritten to
  match the Teardown framing (take it apart + name the design choice + judge
  the trade-off) rather than the Plain "answer one real question" framing.
  `topic` changed to `CLAUDE · SKILLS` to match the sibling nbb reels'
  convention (BHTF `ClaudeComposerAsk` topic prop was already carrying the
  clinical-trial-specific string — updated to `CLAUDE · SKILLS` too so the
  chip on-screen matches metadata).

## Judgment calls

1. **BHTF instead of new beat.** SKILL.md §Step 3 says "insert one beat" for
   the LLM exercise, but the source already carries BHTF — a "your turn" beat
   whose `ClaudeComposerAsk` shot already displays a paste-ready prompt.
   Inserting a second LLM-flavoured beat would make the ending
   "carry-out → prompt → prompt → outro" with no visual variation and no
   working shot. Converting BHTF in place preserves the beat count (7/7),
   keeps the built visual, adds the `llm_exercise` object the schema wants,
   and gets the "Go deeper" follow-up spoken out loud. Same call the sibling
   `nbb-financial-services--claude-liam-gl-recon` made.
2. **`topic` unified to `CLAUDE · SKILLS`.** Source carried
   `CLINICAL-TRIAL-PROTOCOL-SKILL · SPEC-DRIVEN DRAFTING SKILL` — accurate but
   long for the composer chip and off-shape from the sibling nbb reels. The
   metadata + BHTF composer prop both updated. The BHTF `segment` prop keeps
   the video title so the on-screen segment line still says what the video is
   about.
3. **Channel handle unchanged (`@HumanitariansAI`).** Scaffold wrote
   `audience: NikBearBrown` but did not touch `channel_title` / `folderLabel` /
   `playlist`. Brand spec `nbb.md` names `www.brutalist.art` as the default
   NBB channel, but no book-level `AUTHOR.MD` is available under
   `anthropics/claude-bear/` and the sibling nbb reels here all kept the HAI
   handle. If a later pass wants brutalist.art on the outro card, that's a
   single-field flip.
4. **Shot color arrays left at humanitarians hex (`#F3EBDD` / `#2F2A26` /
   `#E4572E`).** The metadata `palette: "teardown"` is what the renderer keys
   off; per-shot `colors` arrays are the humanitarians ground the Manim
   scenes were built for. Re-toning to strict teardown (`#FFFFFF` / `#2A1A0E`
   / `#C8102E`) would re-scaffold the shot blocks, which the invocation
   forbids. Rendering pass can decide.
5. **Kept the original Manim scene classes (`BKNB01Scene`, `BKNB02Scene`,
   `BKNB03Scene`) and the existing `media/*.mp4` refs.** Rewriting narration
   doesn't invalidate the graphics — labels and chips already read in the
   Teardown register ("A SKILL IS A FOLDER", "THREE-STEP PIPELINE", "DRAFTS TO
   SPEC, NEVER DECIDES"). Audio pass will re-time to the new narration
   lengths; visuals compose as-is.
