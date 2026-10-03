# SOURCES — cc-claude-skills

## Primary (this reel)

- `SESSION.md` — the three fresh headless `claude -p` runs this reel reconstructs, and Liam's plain-shell verification against `evidence/`. Every `CCSession` block traces here.
- `evidence/run-bare.jsonl`, `evidence/run-skill.jsonl`, `evidence/run-nomatch.jsonl` — raw stream-json for the three runs (Claude Code 2.1.150, 2026-09-10). Every tool name and every one-line assistant text on screen is a verbatim span from these.
- `evidence/.claude/skills/exec-summary/SKILL.md` — the 27-line skill file Liam wrote before the runs. The frontmatter, sections, and description shown on screen come from this file.
- `evidence/.claude/skills/exec-summary/check_summary.py` — the 31-line definition-of-done script. Every checker result in the reel is this script's actual output.
- `evidence/article.md` — the 24-line document the runs summarize.
- `evidence/summary.skill.md`, `evidence/summary.nomatch.md` — the two summaries Claude wrote across Runs B and C. The four headings and the paraphrased opening lines shown in `BSHOW` come from these.

## Doctrine (CONDUCT and HUMAN)

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — CONDUCT's frame: programming as conducting; the human's supervisory capacities (`[PF]`, `[TO]`, `[PA]`, `[IJ]`, `[EI]`); the dangerous middle.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — HUMAN's frame: the model cannot reliably report its own uncertainty; the metacognitive burden is the human's; verification is not the leftover work.
- `brutalist-art/skills/make/cc-explainer/reference/three-beats.md` — the three-beats doctrine (SKEPTIC retired) and the CCHarnessMap ring convention.

## Source concept (retitled and rebuilt from real runs)

- `claude-code-101/03-hooks-skills-commands/claude-cowork--claude-liam-claude-skills/beat_sheet.json` — the 2026-07 chat-window framing of "One Prompt. Every Time." The **misconception this reel corrects** ("A skill is a slash command") is the framing that beat sheet used verbatim in B02. This reel keeps the title and the audience-facing promise; it replaces every card with real transcripts from `SESSION.md`.
