# BUILD-PROMPT — cc-claude-skills

**Skill.** `cc-explainer` (`brutalist-art/skills/make/cc-explainer/SKILL.md`).
**Tier.** Claude Code 101 · `03-hooks-skills-commands` · film 04.
**Title.** One Prompt. Every Time.
**Slug.** `cc-claude-skills`.
**Operator.** Liam, in for Bear · Kokoro `am_onyx` · Teardown register · body and closing block both.
**Concept source.** `claude-code-101/03-hooks-skills-commands/claude-cowork--claude-liam-claude-skills/beat_sheet.json` — kept the title and audience-facing promise; replaced every card with real transcripts.
**Misconception the film corrects.** "A skill is a slash command you type." Truth: a skill is a folder with a description that finds you; Claude auto-launches it on ask-match, semantic not literal.
**BUILD-SHOW.** Armed — BFLOW `CCHarnessMap` + BSHOW `CCPlainShell` between the last correction cycle and CONDUCT.

## The session, verbatim

Three fresh headless `claude -p` runs (Claude Code 2.1.150, 2026-09-10) against `/tmp/cc-claude-skills-scratch/`. Common flags: `--output-format stream-json --verbose --max-turns 12 --permission-mode acceptEdits --strict-mcp-config --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*)"`, `< /dev/null`. Full details in `PROMPTS.md`; raw stream-json in `evidence/`.

- **Run A — bare.** `.claude/skills/` absent. Ask: `Please summarize article.md.` → Read, ad-hoc text summary printed, no `summary.md` written, no `Skill()` call.
- **Run B — skill, natural ask.** `.claude/skills/exec-summary/{SKILL.md 27 lines, check_summary.py 31 lines}` restored (`description: Utility for summarizing documents in a house style.`). Same ask. → `Skill(exec-summary)`, Read, Write `summary.md` (4 sections), Bash `python3 check_summary.py summary.md` → PASS.
- **Run C — skill, paraphrased ask.** Same folder. Ask: `Wrap article.md for a leadership audience — the CEO reads this Friday.` (no literal trigger word) → `Skill(exec-summary)` fires anyway (semantic match), Read×2, Write, checker → PASS. Same four headings.

## The build

- 15 beats: B00 · BIDEA · BDEFS · B01 · B02 · B03 · B04 · B05 · BFLOW · BSHOW · BCOND · BHUM · BVDT · BHTF · BOUT.
- Measured audio 270.9 s (4:30). Body: CCSession × 3 (B00, B03, B05) plus CCPlainShell × 4 (B01, B02, B04, BSHOW), one BrutalistHesitantWriter (BIDEA), one CCDefinitions (BDEFS), one CCHarnessMap (BFLOW). Closing: CCBoondoggleScore, CCHumanLedger, ClaudeVerdictArtifact (4 lines), ClaudeComposerAsk, ClaudeTitleOutro.
- `metadata.build: true`. Palette `claude`. `metadata.skill: cc-explainer` (so GATE BOOKEND accepts the CCSession cold open).
- Author script `author_sheet.py` copied verbatim from `cc-skill-build-once/`; only beats and metadata differ. Runs clean: `budget: clean`.

## Rules that bound the build

1. **TERMINAL-FIRST.** Body defaults to `CCSession`. Every non-terminal beat names `shot.leaves_terminal_because`.
2. **REAL-SESSION.** Every tool name and one-line text is a verbatim span from `evidence/run-*.jsonl`.
3. **TYPES-NOT-NARRATES.** `prompt` blocks show what Liam typed. Narration says why.
4. **VERIFY IS A COMMAND.** B01, B04, B02, BSHOW are plain-shell `$` checks — the receipt for each session claim.
5. **LIAM LAW.** Liam, in for Bear, body and closing block both. Cold open says it. Outro says it. No second persona.
6. **OUTRO-LOCK.** `ClaudeTitleOutro`, `@NikBearBrown`, exact title, `subline: ""`.
7. **BUILD-SHOW.** BFLOW + BSHOW between last correction cycle and CONDUCT.
8. **Never publish.** Master stays in this folder. TOPOST via `post`, only on ask.
