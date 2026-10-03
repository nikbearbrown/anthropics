# BUILD-LOG — cc-claude-skills

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands`, film 04 · Liam, in for Bear · built 2026-09-10.

## The concept — and where the source pointed

Concept slug `claude-cowork--claude-liam-claude-skills` · title *One Prompt. Every Time.* Its 2026-07 chat-window framing named the misconception this reel had to correct — it told the viewer to "type the slash, the skill name, and one line about your task." In Claude Code that is not how skills fire. The reel kept the title and the promise; it replaced every card in the source with three real headless runs.

## The experiment

Same ask under three conditions, each a fresh `claude -p` session (Claude Code 2.1.150, 2026-09-10), from `/tmp/cc-claude-skills-scratch/` so no parent `CLAUDE.md` reached the run.

- **Run A — bare.** No `.claude/skills/`. Ask: `Please summarize article.md.` Result: Read, an ad-hoc five-sentence summary printed to the terminal with a bolded "Two takeaways:" list. No `summary.md` written. **Zero `Skill()` calls** in the transcript. 2 turns, 10.5 s, $0.109.
- **Run B — skill, natural ask.** `.claude/skills/exec-summary/{SKILL.md 27 lines, check_summary.py 31 lines}` restored, description `Utility for summarizing documents in a house style.` Same ask. Result: `Skill(exec-summary)` fires, Read, Write `summary.md` (four sections in the fixed order), Bash `python3 check_summary.py summary.md` → `PASS`. 6 turns, 25.8 s, $0.149.
- **Run C — skill, paraphrased ask.** Same folder. Ask: `Wrap article.md for a leadership audience — the CEO reads this Friday.` No `summarize`, no `TL;DR`, no `brief` in the ask. Result: `Skill(exec-summary)` **still fires** — semantic match against the description's "summarizing documents in a house style". Same four headings. Same PASS. 8 turns, 63.9 s, $0.256.

The router matches on meaning, not on word. That is the fact the reel is built to teach.

## The reel

15 beats, 270.9 s narration (measured Kokoro `am_onyx` durations, master clock). Compiled 271.9 s = 4:32, 3840×2160, h264, aac. Body: CCSession × 3 (B00 bare, B03 skill run, B05 the other ask), CCPlainShell × 4 (B01 bare-verify, B02 the folder, B04 skill-verify, BSHOW the built file). Idea: BrutalistHesitantWriter (BIDEA). Definitions: CCDefinitions (BDEFS — five terms). BFLOW: CCHarnessMap (MODEL → YOUR ASK → DESCRIPTION MATCH → SKILL LOAD → YOUR LOOP). Closing block: CCBoondoggleScore (BCOND, six steps, dangerous middle = step 4), CCHumanLedger (BHUM), ClaudeVerdictArtifact (BVDT, four lines, last one FALSIFIABLE), ClaudeComposerAsk (BHTF, the four-question your-turn prompt), ClaudeTitleOutro (BOUT).

`metadata.build: true` — armed BUILD-SHOW (BFLOW + BSHOW between the last correction cycle and CONDUCT).

## Compile

Author `author_sheet.py` (copied verbatim from `cc-skill-build-once/`; only beats and metadata changed) printed `budget: clean` first pass — no oversized text blocks, ledger rows, score steps, or shell lines. Kokoro emitted all 15 mp3s.

`art run`: one pass. Every rendering gate passed:
- GATE V: 30 frames sampled, 0 BLOCKER / 0 STRUCTURAL / 0 COSMETIC.
- GATE T: PASS. §8.10 BVDT at 0.82 is ADVISORY (verdict lines echo the recap narration — expected for a Verdict beat, not blocking).
- GATE SHARPNESS: PASS (median LV = 610.9).
- GATE BOOKEND: PASS (four bookends correct — `metadata.skill: cc-explainer` armed the CCSession cold-open override).
- GATE AUDIO / MASTER / LOUDNESS / RECEIPTS: all PASS.

Two advisory warnings, both non-blocking:
1. **SKIN LINT** flagged B00's CCSession cold open against the palette-`claude` COLD OPEN LAW default (`ClaudeComposerAsk`). This is exactly the cc-explainer skill's approved TERMINAL-FIRST override; GATE BOOKEND's per-skill logic passed it.
2. **Motion histogram**: `type` = 53 % (8/15 beats) — over the 40 % pantry cap. Kept as-is: CCPlainShell and CCSession beats are visibly "typing" content, and this is what a cc-explainer's body looks like by construction.

`art final`: written to `cc-claude-skills.mp4` (17 MB). Same gates re-run, same PASS.

## Not published

TOPOST only via `post`, only on ask. This reel's master stays in the reel folder.
