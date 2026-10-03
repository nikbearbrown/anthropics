# PROMPTS — cc-claude-skills--claude-liam-skill-creator

The prompts on screen — every user turn Liam pastes into Claude Code (real, or reconstructed for a beat).

## Real headless runs (SESSION.md)

Six fresh `/tmp/sc-<skill>-<ask>/` dirs; the two SKILL.md files copied to `.claude/skills/meeting-actions/SKILL.md` per cell; then one `claude -p "<ask>" --output-format stream-json --verbose --max-turns 16 --permission-mode acceptEdits --strict-mcp-config --allowedTools "Read,Write,Edit,Glob,Grep,Skill,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*)" < /dev/null` per cell.

The three asks, verbatim:

- **A1 obvious:** `Extract action items from notes.txt.`
- **A2 paraphrase:** `I have a meeting write-up in notes.txt — pull out who agreed to do what.`
- **A3 near-miss:** `Summarize notes.txt for someone who missed the meeting.`

## Beats

- **B00, B03** — the A1 ask, shown in a `prompt` block: `Extract action items from notes.txt.`
- **B04** — the A3 ask, shown in a `prompt` block: `Summarize notes.txt for someone who missed the meeting.`
- **B01, B05** — bang commands run in a session (typed after the ask, following the CC session-input convention): `!grep -c '"name":"Skill"' run-vague-a1.jsonl`, `!wc -l actions.vague-a1.md`, `!python3 check_actions.py actions.vague-a1.md`; `!grep -c '"name":"Skill"' run-*.jsonl`.
- **B02** — plain-shell commands, outside any session: `wc -l SKILL-vague.md SKILL-pushy.md`, `head -3 SKILL-vague.md`, `sed -n '3p' SKILL-pushy.md | wc -w`.
- **BHTF** — the viewer's paste: `I'll give you a folder with a SKILL.md and three asks — one obvious, one paraphrased, one adjacent negative. Run each in a fresh temp dir with only that skill installed. Count the Skill events per run. Show me the six-cell tally.`

No prompt in the reel is invented; each traces to `SESSION.md` or to Liam's plain-shell VERIFY.
