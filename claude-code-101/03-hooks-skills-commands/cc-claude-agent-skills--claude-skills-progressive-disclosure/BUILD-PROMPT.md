# BUILD-PROMPT — cc-claude-agent-skills--claude-skills-progressive-disclosure

## What this reel is

A Claude Code 101 cc-explainer, tier 3 (Hooks, Skills, Commands), on **skill progressive disclosure** — how one `.claude/skills/<name>/` folder is loaded in three tiers: description (always resident), body (on `Skill()` match), references (only when the body's own conditional says so). Liam, in for Bear. Kokoro `am_onyx`, free.

The film measures. Three fresh headless `claude -p` runs against the same scratch project (`scratch/` — a Q3 platform-review article, a `check.py` definition of done, and an `exec-summary` skill with two reference files) show three different loading depths for the same skill folder:

| Run | Ask | Skill() | references/ | words of skill context loaded |
|---|---|---|---|---|
| A (bare — no skill) | `Please summarize article.md into summary.md.` | 0 | 0 | 0 |
| B (skill on natural ask) | `Write an executive summary of article.md into summary.md.` | 1 | 0 | 158 (description 8 + body 150) |
| C (skill on strict-style ask) | `Write an executive summary of article.md into summary.md, following our house style precisely.` | 1 | 1 (house-style.md) | 353 (description 8 + body 150 + house-style 195) |

`references/length.md` never fires — the body's other conditional (board/incident) never matches. One skill, three depths, decided one ask at a time. That is the claim; the transcripts are the receipt.

## Spine (15 beats · 300.6 s · 16:9 · 4K)

- B00 COLD OPEN — CCSession, Run B on-screen: the "yes, it works" opening.
- BIDEA — BrutalistHesitantWriter, the misconception `resident` reconsidered into `described`.
- BDEFS — CCDefinitions, five terms.
- B01 THE SKILL FOLDER — CCPlainShell, `wc` on the three tiers.
- B02 RUN A — CCSession, bare, no skill.
- B03 RUN A VERIFY — grep Skill=0, ##=0, check.py FAIL.
- B04 RUN B — CCSession, Skill fires, references skipped.
- B05 RUN B VERIFY — grep Skill=1, refs=0, PASS.
- B06 RUN C — CCSession, Skill fires, references/house-style.md loads.
- B07 RUN C VERIFY — grep Skill=1, refs=1, length=0, PASS.
- B08 CONDUCT — CCBoondoggleScore, dangerous middle = the body's conditional wording.
- B09 HUMAN — CCHumanLedger.
- BVDT — ClaudeVerdictArtifact, 4 lines ending in a FALSIFIABLE clause.
- BHTF — ClaudeComposerAsk, "Your turn." + the concrete paste.
- BOUT — ClaudeTitleOutro.

## Files this build touches

- `beat_sheet.json` (generated from `author_sheet.py`).
- `SESSION.md`, `FACTCHECK.md`, `CHECKS-REPORT.md`, `SHOTLIST.md`, `PROMPTS.md`, `SOURCES.md`, `BUILD-LOG.md`.
- `mp3/*.mp3` (Kokoro, 15 files).
- `evidence/` — the raw jsonl and outputs from the three real runs.
- `media/*.mp4` (Remotion + Manim per beat), `mp4/*.mp4` (audio + visuals per beat), the master.

## Rules honoured

- LIAM LAW — Liam, in for Bear, on every beat. Kokoro `am_onyx`.
- TERMINAL-FIRST — 7 CCSession beats; three off-terminal beats each carry `shot.leaves_terminal_because`; closing block off-terminal is doctrine.
- REAL-SESSION — every block in every CCSession beat traces to `SESSION.md`.
- OUTRO-LOCK — `ClaudeTitleOutro`, exact title, `@NikBearBrown`, no subline.
- BUILD-SHOW — not armed (concept film, no artifact built); CHECKS-REPORT says so.
- Never publishes. Master stays in the reel folder.
