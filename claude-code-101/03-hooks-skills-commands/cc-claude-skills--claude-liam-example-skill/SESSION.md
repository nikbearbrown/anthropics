# SESSION.md — cc-claude-skills--claude-liam-example-skill

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10, same one-sentence ask (`evidence/ask.txt`), three shapes of the same skill. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|wc|grep)`; `--strict-mcp-config` (no MCP); `--permission-mode acceptEdits`. Scratch copied to `/tmp` so no parent `CLAUDE.md` reached the session. Raw stream-json in `evidence/run-{bare,full,bare-front}.jsonl`; the three `peek.md` outputs and both `SKILL.md` variants in `evidence/`.

```
Peek at sales.csv and write the result to peek.md.
```

## The scratch project (every run)

```
scratch/
├── README.md      3 lines
└── sales.csv      1 header + 9 data rows, 6 columns (rep,region,quarter,sold,returned,net)
```

## The subject — `anthropics/claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md`

The reference template shipped with Claude Code's plugin system. 84 lines. Two frontmatter fields required (`name`, `description`), two optional (`version`, `license`). The description is Anthropic's own example of the good pattern:

```
This skill should be used when the user asks to "demonstrate skills",
"show skill format", "create a skill template", or discusses skill
development patterns.
```

The rest of the file is guidance ABOUT skills — three-mode distinction (skill vs command vs agent), the optional directory structure (`references/`, `examples/`, `scripts/`), five content guidelines, and best practices. All of it prose, none of it required by the parser. The film asks the honest question: what does copying the template's pattern actually buy you?

## The skill under test — `csv-peek`

Written to `scratch/.claude/skills/csv-peek/`, following the example-skill template's description pattern verbatim (specific phrases, keywords, topic area), and adding a body: a fixed output shape (four `##`-headings — FILE, ROWS, COLUMNS, HEAD — the last with three rows) and a `check_peek.py` script as the definition of done.

- **Full form**: 40-line `SKILL.md` (frontmatter + format spec + rules + a definition of done). `evidence/csv-peek.full.SKILL.md`.
- **Bare-frontmatter form**: 4 lines total — the same frontmatter, everything else deleted. `evidence/csv-peek.bare-front.SKILL.md`.
- `check_peek.py` (19 lines): asserts `## FILE:` `## ROWS:` `## COLUMNS:` `## HEAD:` in that order, HEAD has ≥ 3 rows. `evidence/csv-peek.check_peek.py`.

## Run A — bare (no skill in folder) · session `46660809-…`

**Setup.** No `.claude/skills/` folder at all. The skill does not exist for this run.

- **Bash** `ls …` · **Read** `sales.csv` · **Bash** `wc -l sales.csv`
- **Write** `peek.md` (28 lines): title `# Peek: sales.csv`, a bullet block, a **Header** section, a **First rows** table, a **Last rows** table, and a **Quick notes** section
- **CLAUDE:** "Wrote `peek.md` with schema (6 columns), row count (9 data rows), head/tail samples, and a few quick observations about the data."
- **RESULT:** success · 5 turns · 25.0 s · $0.174

`Skill()` calls in the stream-json: **0** (`grep -c '"name":"Skill"' run-bare.jsonl` → 0). Claude picked its own shape.

## Run B — full skill (frontmatter + body + rules + check.py) · session `caf097fb-…`

**Setup.** `.claude/skills/csv-peek/SKILL.md` = the full 40-line file. Same ask.

- **TOOL** `Skill(csv-peek)` — auto-launched, args `sales.csv` (the router matched the ask "Peek at sales.csv" against the description's `"peek at a CSV"` phrase and topic `tabular data file`)
- **Bash** `ls …` · **Read** `sales.csv`
- **Write** `peek.md` (5 lines) — in the exact fixed shape:
  ```
  ## FILE: sales.csv
  ## ROWS: 9
  ## COLUMNS: rep, region, quarter, sold, returned, net
  ## HEAD:
      A. Reyes,west,Q1,148,12,136
      K. Patel,east,Q1,203,31,172
      J. Choi,west,Q1,111,4,107
  ```
- **Bash** `python3 .claude/skills/csv-peek/check_peek.py peek.md` → `PASS`
- **CLAUDE:** "Wrote `peek.md` with 9 rows, 6 columns, and the first three data rows. Check script prints `PASS`."
- **RESULT:** success · 7 turns · 19.8 s · $0.182

## Run C — bare frontmatter (4 lines total, no body) · session `670b0d5b-…`

**Setup.** Same folder, but `SKILL.md` gutted to only its frontmatter (`---` / `name: csv-peek` / `description: …` / `---`). The checker script left untouched. Same ask.

- **TOOL** `Skill(csv-peek)` — still auto-launched (the description alone triggered the router)
- **Read** `.claude/skills/csv-peek/SKILL.md` (a 4-line file — nothing in it but the frontmatter)
- **Bash** `ls …` · **Read** `sales.csv`
- **Write** `peek.md` (7 lines) — same information, DIFFERENT shape:
  ```
  file: sales.csv
  rows: 9
  columns: rep, region, quarter, sold, returned, net

  first 3 data rows:
  A. Reyes,west,Q1,148,12,136
  K. Patel,east,Q1,203,31,172
  J. Choi,west,Q1,111,4,107
  ```
- No `check_peek.py` call — the body was where the definition of done was named.
- **RESULT:** success · 7 turns · 25.7 s · $0.179

## Liam's VERIFY (plain shell against `evidence/`)

```
> wc -l evidence/example-skill.SKILL.md
      84 evidence/example-skill.SKILL.md
> head -6 evidence/example-skill.SKILL.md
---
name: example-skill
description: This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills.
version: 1.0.0
---
> wc -l evidence/csv-peek.full.SKILL.md evidence/csv-peek.bare-front.SKILL.md
      40 evidence/csv-peek.full.SKILL.md
       4 evidence/csv-peek.bare-front.SKILL.md
> grep -c '"name":"Skill"' evidence/run-bare.jsonl evidence/run-full.jsonl evidence/run-bare-front.jsonl
evidence/run-bare.jsonl:0
evidence/run-full.jsonl:1
evidence/run-bare-front.jsonl:1
> python3 evidence/csv-peek.check_peek.py evidence/peek.full.md
PASS
> python3 evidence/csv-peek.check_peek.py evidence/peek.bare-front.md
FAIL: heading order [] != ['FILE', 'ROWS', 'COLUMNS', 'HEAD']
> python3 evidence/csv-peek.check_peek.py evidence/peek.bare.md
FAIL: heading order [] != ['FILE', 'ROWS', 'COLUMNS', 'HEAD']
> wc -l evidence/peek.bare.md evidence/peek.full.md evidence/peek.bare-front.md
      28 evidence/peek.bare.md
       5 evidence/peek.full.md
       7 evidence/peek.bare-front.md
```

## What the runs gave the film

1. **The template's description pattern works** as the template promises. Both runs where the skill was installed — full body and bare frontmatter — routed. `Skill(csv-peek)` fires on "Peek at sales.csv" from the description alone. The parser really does treat everything after the frontmatter as optional.
2. **The description does not lock the shape**. With no body, csv-peek produced `file: / rows: / columns: / first 3 data rows:` — the same information under different headings, and no automatic call to the checker. The definition of done was named in the body Liam deleted.
3. **The teardown is honest, not a takedown.** The template's central claim — description-as-trigger — is verified. Its silent claim — that everything else is decoration — is not. The body is where two runs of the same skill become the same shape.
