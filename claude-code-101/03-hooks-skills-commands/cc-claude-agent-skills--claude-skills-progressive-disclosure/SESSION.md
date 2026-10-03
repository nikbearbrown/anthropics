# SESSION.md — cc-claude-agent-skills--claude-skills-progressive-disclosure

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10, against the same scratch project (`scratch/` — one article to summarise, a definition-of-done `check.py`, and a two-tiered `exec-summary` skill). Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config` (no MCP servers); `--permission-mode acceptEdits`; scratch copied to `/tmp` so no parent `CLAUDE.md` reached the session. Raw stream-json in `evidence/run-{a-bare,b-skill,c-strict}.jsonl`; the three `summary.*.md` files, the article, the checker, and the skill folder are in `evidence/`.

## Scratch project (tiered skill)

```
scratch/
├── README.md                                    3 lines
├── article.md                                   21 lines · 193 words — Q3 platform review
├── check.py                                     18 lines — definition of done
└── .claude/skills/
    ├── exec-summary/                            the tiered skill
    │   ├── SKILL.md                             30 lines · 150 words · description = 8 words
    │   └── references/
    │       ├── house-style.md                   35 lines · 195 words — voice, tense, forbidden words
    │       └── length.md                        24 lines · 105 words — audience adaptation
    └── csv-summarize/
        └── SKILL.md                             10 lines — a second, unrelated skill; never fires here
```

The **description** in `exec-summary/SKILL.md`'s frontmatter (`Summarize a document in the house executive-summary style.`) is what the router sees at all times — eight words. The **body** (the rest of the file, ~150 words) is loaded only when the description matches and `Skill(exec-summary)` fires as a tool. The **references** are loaded only when the body's own conditional says to: "Read `references/house-style.md` only if the ask uses the words 'house style', 'style guide', or 'strict style'." Three tiers; three different runs pull three different depths.

## Run A — bare (session `b99597fd-…`, 14.6 s, 3 turns, $0.130)

**Setup.** No `.claude/skills/` folder in the run's cwd at all. Just `README.md`, `article.md`, `check.py`. The skills do not exist for this run — not description, not body, not references.

**Ask.** `Please summarize article.md into summary.md.`

- **Read** `article.md`
- **Write** `summary.md` (130 words, single `# Summary — Q3 platform review` heading, three prose paragraphs)
- **CLAUDE** — "Wrote `summary.md` — condenses the article into the problem (backlog + causes), what was tried, what worked (per-plan priority floor), and the takeaway."
- **RESULT** success · 3 turns · 14.6 s · $0.130

`Skill()` in the transcript: zero. No `## ` headings; `check.py summary.md` → `FAIL: headings — got []`. Claude decided on its own that a summary is prose.

## Run B — skill fires; body loads; no references (session `7b42e54e-…`, 25.8 s, 5 turns, $0.123)

**Setup.** Full scratch copied to `/tmp/cc-pd-skill`, including both skills.

**Ask.** `Write an executive summary of article.md into summary.md.`

The ask names none of the reference-trigger words (`house style`, `style guide`, `strict style`, `board`, `director`, `incident`, `postmortem`, `outage`).

- **TOOL** `Skill(exec-summary)` — the router matched `executive summary` against the description `Summarize a document in the house executive-summary style.` The body of `SKILL.md` (150 words) enters context.
- **Read** `article.md`
- **Write** `summary.md` — four sections, in the fixed order: `## What` · `## Why it matters` · `## What's new` · `## What to do`. Verified: `grep '^## ' summary.b.md` → four headings, no others.
- **CLAUDE** — "Wrote `summary.md` in the four-section house shape (What / Why it matters / What's new / What to do)."
- **RESULT** success · 5 turns · 25.8 s · $0.123

No `references/house-style.md` or `references/length.md` in the stream-json's Read calls. The body's own instruction — "Do NOT read them for a plain summary — they are large and cost tokens" — held. Tier 3 stayed unloaded.

## Run C — skill fires; body loads; one reference loads (session `e470fb9f-…`, 16.3 s, 6 turns, $0.161)

**Setup.** Same skill folder, same `article.md`.

**Ask.** `Write an executive summary of article.md into summary.md, following our house style precisely.`

The words `house style` are in this ask.

- **TOOL** `Skill(exec-summary)` (fires again — description match)
- **Read** `.claude/skills/exec-summary/references/house-style.md` — the body's conditional matched on `house style` in the ask
- **Read** `article.md`
- **Write** `summary.md` — same four-section shape; tuned to the style guide's rules
- **CLAUDE** — "Wrote `summary.md` in the four-section shape, past tense for outcomes, present for the diagnosis, imperative for the recommendations, exact numbers preserved in Why and What's new, and none of the forbidden words."
- **RESULT** success · 6 turns · 16.3 s · $0.161

The closing sentence recites the rules from `house-style.md` verbatim — proof the file entered context. `references/length.md` was NOT read: no `board`, no `incident` in the ask.

## Liam's VERIFY (plain shell, in `evidence/`)

```
> wc -w skills/exec-summary/SKILL.md skills/exec-summary/references/house-style.md skills/exec-summary/references/length.md
     150 skills/exec-summary/SKILL.md
     195 skills/exec-summary/references/house-style.md
     105 skills/exec-summary/references/length.md
> head -3 skills/exec-summary/SKILL.md
---
name: exec-summary
description: Summarize a document in the house executive-summary style.
> grep -c '"name":"Skill"' run-a-bare.jsonl
0
> grep -c '"name":"Skill"' run-b-skill.jsonl
1
> grep -c '"name":"Skill"' run-c-strict.jsonl
1
> grep -c 'references/' run-b-skill.jsonl
0
> grep -c 'references/' run-c-strict.jsonl
1
> grep '^## ' summary.a.md
> grep '^## ' summary.b.md
## What
## Why it matters
## What's new
## What to do
> grep '^## ' summary.c.md
## What
## Why it matters
## What's new
## What to do
> python3 check.py summary.a.md
FAIL: headings — got []
> python3 check.py summary.b.md
PASS
> python3 check.py summary.c.md
PASS
```

`Skill()` fires zero times in the bare run and once each in the two skill runs. `references/` appears in the reads only when the body's conditional matched the ask. Three tiers, three depths.

## What the runs gave the film

1. **Run A — no skill in the folder.** 14.6 s, ad-hoc prose, no `## ` headings, `check.py` fails. Zero skill words loaded because the skill doesn't exist for this run.
2. **Run B — skill fires on the natural ask.** 25.8 s, `Skill(exec-summary)` in the stream-json, four house sections, checker passes. Description (8 words) matched; body (150 words) loaded; references (300 words combined) stayed on disk.
3. **Run C — skill fires, and one reference loads.** 16.3 s, `Skill(exec-summary)` fires again, and the body's own conditional (`if 'house style' in the ask`) triggers `Read references/house-style.md`. Description (8) + body (150) + house-style (195) = 353 words of skill context loaded — for the SAME skill folder that cost 158 words in Run B and 0 in Run A.

That is progressive disclosure by tier: one skill, three depths, decided by the ask.
