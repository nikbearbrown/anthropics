# SESSION.md — cc-command-development

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two fresh headless `claude -p` slash-command invocations against the same scratch repo (`scratch/`, a five-function `inventory.py` with planted bugs), 2026-09-10. Tools fenced on the CLI to `Read, Glob, Grep, Bash(ls|cat|wc|git)`. Raw stream-json in `evidence/run-{v1,v2}.jsonl`; the two command files in `evidence/review-{v1,v2}.md`; Claude's outputs harvested to `evidence/out-{v1,v2}.md`; tool calls harvested to `evidence/tools-{v1,v2}.txt`; a diff of the two commands in `evidence/review-v1-v2.diff`. The scratch repo lives at `scratch/` — one file, six functions, four planted bugs plus one float-truncation.

## The two commands

**`.claude/commands/review-v1.md`** — the "message to user" pattern the source SKILL warns against. Three sentences describing what the command will do; zero sentences telling Claude what to do.

```
This command reviews Python code in this repo for bugs and security issues.
You will receive a report of any problems found, with severity ratings and
suggested fixes. The review covers common Python pitfalls, security concerns,
and correctness issues.
```

**`.claude/commands/review-v2.md`** — the imperative rewrite. Frontmatter (description, allowed-tools intent, argument-hint) plus explicit instructions: what to read, what to look for, what format to output, and what to end with.

```
---
description: Review every Python file for bugs by line number
allowed-tools: Read, Glob, Grep
argument-hint: [path]
---

Read every `.py` file at `$ARGUMENTS` (default: this repo). For each file, list
bugs and security issues with the file path, line number, and one-sentence
explanation. Rank each: HIGH, MEDIUM, LOW.

Look for at least:
- SQL injection or shell injection …
- Mutable default arguments …
- Bare `except:` that swallows errors …
- Off-by-one errors on slice bounds

Output one row per issue as: `path:line — SEV — description`. End with a
one-line count.
```

## Run: v1 (session `6317267d-…`)

- **TOOL** `Bash` `pwd && ls -la` · **Read** `inventory.py` · **Read** `README.md`
- **CLAUDE (output — 92 lines, 2319 chars):** three severity buckets with emoji headings (🔴 CRITICAL / 🟠 HIGH / 🟡 MEDIUM), a fenced code block for every issue's cause AND every suggested fix, a summary table, and a closing question — "Want me to apply the fixes?".
- **Findings:** 6 — SQL injection (line 14), shell injection (line 39), mutable default (line 6), off-by-one (line 35), bare except (line 30), and float truncation in `total_cents` (line 22) — Claude added that one on its own initiative.
- **RESULT:** success · turns=4 · 24.0 s

## Run: v2 (session `1b6108b2-…`)

- **TOOL** `Bash` `find … -name "*.py"` · **Read** `inventory.py`
- **CLAUDE (output — 6 lines, 728 chars):** five one-line rows in the exact format the command specified, then a blank line, then `5 issues found.`. No headings, no emoji, no code blocks, no closing question.
- **Findings:** 5 — the four categories the command listed by name (SQL injection, shell injection, mutable default, off-by-one) plus bare `except:` (the fifth planted bug, in the "at least" set the command opened). The float-truncation bug that v1 flagged is absent — the command didn't ask for it, and v2 didn't volunteer.
- **RESULT:** success · turns=3 · 17.1 s

## Liam's VERIFY (plain shell against `evidence/out-{v1,v2}.md`)

```
> wc -l evidence/out-v1.md evidence/out-v2.md
      92 evidence/out-v1.md
       6 evidence/out-v2.md
> grep -oE '🔴|🟠|🟡' evidence/out-v1.md | wc -l
       3
> grep -oE '🔴|🟠|🟡' evidence/out-v2.md | wc -l
       0
> grep -c '```' evidence/out-v1.md
      24
> grep -c '```' evidence/out-v2.md
       0
> grep -c '?' evidence/out-v1.md
       2
> grep -c '^inventory\.py' evidence/out-v2.md
       5
> tail -1 evidence/out-v2.md
5 issues found.
> tail -1 evidence/out-v1.md
Two critical injection vulns should be fixed before this touches any untrusted input. Want me to apply the fixes?
```

## What the runs gave the film

1. **Same model, same repo, same bugs — different output shapes.** v1 produced 92 lines of Claude's default "code-review essay" (three severity emoji, twelve code blocks, a table, a follow-up question, six findings including one it decided to add). v2 produced 6 lines in the exact format the command asked for: `path:line — SEV — description`, ending on `5 issues found.` — five findings, all in the four categories the command listed. Nothing else.
2. **The command is not a shortcut — it is a spec for the output shape.** v1 said what the command *would do* (a message to the user); Claude decided what a review "should" look like and delivered it in its own style. v2 said what Claude *should do* and how the output should look; Claude followed it exactly, including the "5 issues found." count line, and did not volunteer the float-truncation finding the command hadn't asked for.
3. **Frontmatter is metadata, not a fence.** v2's `allowed-tools: Read, Glob, Grep` intended a fenced tool set — but Claude used `Bash(find …)` first anyway, because the CLI's outer `--allowedTools` allowed it. The film says so: frontmatter describes intent (in `/help`, in autocomplete via `argument-hint`); the actual tool fence is the caller's.
