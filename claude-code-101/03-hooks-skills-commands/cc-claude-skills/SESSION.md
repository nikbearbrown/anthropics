# SESSION.md — cc-claude-skills

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10, against the same scratch project (`scratch/` — a small folder with one article to summarise). Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|wc)`; `--strict-mcp-config` (no MCP servers); `--permission-mode acceptEdits`; scratch copied to `/tmp` so no parent `CLAUDE.md` reached the session. Raw stream-json is in `evidence/run-{bare,skill,nomatch}.jsonl`; the article, the two summaries Claude wrote, and the skill folder are in `evidence/`.

## Scratch project

```
scratch/
├── README.md                             three lines
├── article.md                            24 lines — Q3 platform review
└── .claude/skills/exec-summary/          added between Run A and Run B
    ├── SKILL.md                          27 lines — frontmatter · Format · Rules · Done
    └── check_summary.py                  31 lines — the definition of done
```

`SKILL.md` and `check_summary.py` were written by Liam once, before the skill runs. The `description:` field in the frontmatter says:

```
Utility for summarizing documents in a house style.
```

Vague. Nine words. No trigger phrases. This vagueness is deliberate — the film tests whether Claude finds the skill anyway.

## Run A — bare (session `1111…`, 10.5 s)

**Setup.** No `.claude/skills/` folder in `scratch/` at all. The skill does not exist for this run.

**Ask.** `Please summarize article.md.`

- **Read** `article.md`
- **CLAUDE** writes to the terminal — a five-sentence summary with a bolded "Two takeaways:" list. No `summary.md` file is written. No headings from the exec-summary format.
- **RESULT** success · 2 turns · 10.5 s · $0.109

No `Skill()` call in the stream-json (`grep '"name":"Skill"' run-bare.jsonl` → 0). Claude decided on its own that a summary is a bullet list.

## Run B — skill fires on the natural ask (session `2222…-aaaaaa`, 25.8 s)

**Setup.** `scratch/.claude/skills/exec-summary/SKILL.md` restored, description unchanged (`Utility for summarizing documents in a house style.`). Same ask, same tool fence.

- **TOOL** `Skill(exec-summary)` — Claude auto-launched the skill on `"Please summarize article.md"`; the routing matched on the description's word `summarizing` and the ask's word `summarize`. `Skill()` shows up in the stream-json exactly the way `Read()` does.
- **Read** `article.md`
- **Write** `summary.md` — four sections, in the fixed order: `## What` · `## Why it matters` · `## What's new` · `## What to do`. Verified: `grep '^## ' summary.md` → four headings, no others.
- **Bash** `python3 .claude/skills/exec-summary/check_summary.py summary.md` → `PASS`
- **CLAUDE** — "Summary written to `summary.md` — PASS."
- **RESULT** success · 6 turns · 25.8 s · $0.149

The user never typed a slash. The skill routed itself.

## Run C — skill fires without the trigger word (session `3333…`, 63.9 s)

**Setup.** Same skill folder, same vague description. Different ask.

**Ask.** `Wrap article.md for a leadership audience — the CEO reads this Friday.`

The word `summarize` is not in this ask. Neither is `TL;DR`, `brief`, `summary`, `recap`. If the router were literal, the skill would not fire.

- **TOOL** `Skill(exec-summary)` (launched again — the router matched semantically, on `wrap … for a leadership audience` against `summarizing documents in a house style`)
- **Read** `article.md`, `check_summary.py`
- **Write** `summary.md` — same four sections, same order. Content tuned for a CEO reader (business consequences, decisions to endorse).
- **Bash** `python3 .claude/skills/exec-summary/check_summary.py summary.md` → `PASS`
- **RESULT** success · 8 turns · 63.9 s · $0.256

Same folder. Different ask. Same shape. That is the promise the film's title is claiming.

## Liam's VERIFY (plain shell, in `scratch/`)

```
> wc -l .claude/skills/exec-summary/SKILL.md .claude/skills/exec-summary/check_summary.py article.md
      27 .claude/skills/exec-summary/SKILL.md
      31 .claude/skills/exec-summary/check_summary.py
      24 article.md
> head -3 .claude/skills/exec-summary/SKILL.md
---
name: exec-summary
description: Utility for summarizing documents in a house style.
> grep -c '"name":"Skill"' ../evidence/run-bare.jsonl
0
> grep -c '"name":"Skill"' ../evidence/run-skill.jsonl
1
> grep -c '"name":"Skill"' ../evidence/run-nomatch.jsonl
1
> grep '^## ' ../evidence/summary.skill.md
## What
## Why it matters
## What's new
## What to do
> grep '^## ' ../evidence/summary.nomatch.md
## What
## Why it matters
## What's new
## What to do
> python3 .claude/skills/exec-summary/check_summary.py ../evidence/summary.skill.md
PASS
> python3 .claude/skills/exec-summary/check_summary.py ../evidence/summary.nomatch.md
PASS
```

The `Skill()` call is the router's signature. It fires zero times in the bare run and once each in the two skill runs — including the one whose ask omits every literal trigger word. The four headings land in the same order both times; the checker passes both files.

## What the runs gave the film

1. **Bare (Run A).** No skill in the folder: 10 seconds, an ad-hoc five-sentence summary with the model's chosen structure, and no `summary.md` file. Different day, different structure — nothing anchors the output. `Skill()` in the transcript: zero.
2. **Skill on the natural ask (Run B).** Same ask, skill in the folder: `Skill(exec-summary)` fires as a tool call, Claude reads the folder's SKILL.md, writes `summary.md` in the fixed four-section shape, runs `check_summary.py` itself, and reports PASS. No slash typed.
3. **Skill on the paraphrased ask (Run C).** The ask says "wrap for a leadership audience" — no literal trigger word — and the skill fires anyway, on semantic match. Same four sections. Same PASS. That is why the reel's misconception is "a skill is a slash command": in the terminal, the skill is a description that finds you, and the description reads asks by meaning.
