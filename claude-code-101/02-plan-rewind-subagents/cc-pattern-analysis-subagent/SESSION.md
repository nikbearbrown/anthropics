# SESSION.md — cc-pattern-analysis-subagent

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, same one-sentence ask (`evidence/ask.txt`), two conditions. Tools fenced to `Read, Write, Edit, Glob, Grep, Bash(ls|cat|python3|git|wc)` for the inline run; plus `Task` for the subagent run. `--strict-mcp-config` on both. Raw stream-json in `evidence/run-inline.jsonl` and `evidence/run-sub.jsonl`; the two produced files in `evidence/feedback_focus.{inline,sub}.md`; the deployed subagent in `evidence/pattern-analyzer.md`; Liam's post-run shell in `evidence/liam-verify.txt`.

## The ask (verbatim, `evidence/ask.txt`)

```
For the binary-search rubric in rubric.md, look at every file under
submissions/ and tell me the top three misconceptions the batch is showing,
most severe first. Write your findings to feedback_focus.md as a numbered
list, most severe first, each item one sentence.
```

## The scratch project (identical starting state, both runs)

```
README.md              3 lines
ask.txt                1 line
rubric.md             16 lines  — five criteria for a binary-search writeup
submissions/
  01-mira.md          11 lines
  02-jules.md         11 lines
  03-priya.md          8 lines
  04-omar.md           9 lines
  05-tao.md           11 lines
```

The subagent run adds one file, deployed by Liam before the run:

```
.claude/agents/pattern-analyzer.md   39 lines
```

Its YAML frontmatter (`evidence/pattern-analyzer.md`, first 5 lines):

```
---
name: pattern-analyzer
description: Scans a batch of student submissions in submissions/ against the
  criteria in rubric.md, returns the top common misconceptions the batch is
  showing — severity first — WITHOUT ever loading a submission into the main
  session. Use whenever a batch of student work must be triaged for teaching
  focus.
tools: Read, Grep, Glob
---
```

## Run: inline (session `48aef3a3-…`) — no subagent deployed

Main session tools, in order:

```
Bash ls -la scratch/
Read rubric.md
Bash ls scratch/submissions/
Read README.md
Read ask.txt
Read submissions/01-mira.md
Read submissions/02-jules.md
Read submissions/03-priya.md
Read submissions/04-omar.md
Read submissions/05-tao.md
Write feedback_focus.md
```

- **Every submission landed in the main session's context.** All eight source files were Read directly.
- Result: `evidence/feedback_focus.inline.md` — 5 lines, three numbered findings plus a title heading.
- `usage.cache_creation_input_tokens`: **35,572**.
- 12 turns, 71.6 s, $0.576.

CLAUDE's summary at the end of the run (verbatim, first two sentences):

> "Written to `feedback_focus.md`. The top three, most severe first: 1. **Midpoint overflow** — 4/5 use `(lo + hi) // 2` with no mention of overflow; only Tao uses the safe form and names why. 2. **No explicit loop invariant** — Mira, Priya, and Omar describe 'shrinking the range' without ever stating the target lives in `[lo, hi)`. …"

## Run: subagent (session `94b04c7b-…`) — the pattern-analyzer deployed

Main session tools, in order:

```
Task (subagent_type: pattern-analyzer,
      description: "Analyze binary-search misconceptions")
Write feedback_focus.md
```

That is the entire main-session tool sequence. **Two tool calls.** No submission was ever Read into the main session.

Inside the subagent (its own context, surfaced in the stream with a `parent_tool_use_id`), the pattern-analyzer's tool sequence:

```
Read rubric.md
Glob submissions/**/*
Read submissions/01-mira.md
Read submissions/02-jules.md
Read submissions/03-priya.md
Read submissions/04-omar.md
Read submissions/05-tao.md
Read scratch-sub                  # EISDIR — subagent tried to read the dir
Glob *.md
```

The subagent's return to the main session (verbatim, `evidence/subagent-return.txt`, opening + findings):

> "I only have Read, Grep, and Glob tools available — I cannot write files. I'll return the findings directly for the parent session to write.
>
> The three most severe misconceptions, most severe first:
>
> 1. Students compute the midpoint as `(lo + hi) // 2` and treat it as the correct form, unaware it can overflow on large inputs and that `lo + (hi - lo) // 2` is the safe version.
> 2. Students describe 'shrinking the range' as a process but do not state a loop invariant — specifically that the target, if present, lies within `[lo, hi)` at every step.
> 3. Students report complexity incompletely or incorrectly — omitting O(1) extra space, and in one case claiming worst case is O(n log n) instead of O(log n).
>
> Note: I do not have Write access (Read/Grep/Glob only), so `feedback_focus.md` was not written by me — the parent session will need to write it. Findings above."

- The subagent's tool whitelist enforced itself: it noticed it could not Write, and said so.
- Result: `evidence/feedback_focus.sub.md` — 3 lines, three numbered findings, no heading (the file the subagent found is exactly what the ask specified).
- `usage.cache_creation_input_tokens`: **31,942** (main-session budget). The five submissions' text lived in the subagent's context window, not the main session's.
- 3 main-session turns, 53.9 s, $0.545.

## Liam's VERIFY (plain shell, once both runs were done — `evidence/liam-verify.txt`)

```
> ls -1 submissions/
01-mira.md
02-jules.md
03-priya.md
04-omar.md
05-tao.md
> wc -l submissions/*.md rubric.md
      11 submissions/01-mira.md
      11 submissions/02-jules.md
       8 submissions/03-priya.md
       9 submissions/04-omar.md
      11 submissions/05-tao.md
      16 rubric.md
      66 total
> wc -l feedback_focus.md          # inline
       5 feedback_focus.md
> wc -l feedback_focus.md          # subagent
       3 feedback_focus.md
> cat .claude/agents/pattern-analyzer.md | head -5
---
name: pattern-analyzer
description: Scans a batch of student submissions in submissions/ against …
tools: Read, Grep, Glob
---
```

Numbers, side by side:

| Chunk of the story          | Inline | Subagent |
|---|---:|---:|
| Main-session Reads          | **8**  | **0**   |
| Main-session Writes         | 1      | 1       |
| Main-session Task/Agent calls | 0    | **1**   |
| Subagent Reads (isolated)   | —      | 7       |
| Main-session `cache_creation_input_tokens` | 35,572 | 31,942 |
| Turns (main session)        | 12     | **3**   |
| Wall time                   | 71.6 s | 53.9 s  |

## What the runs gave the film

1. **Inline** treats the batch as the main session's problem. Every submission is Read into main context, every criterion is judged in the main model's live window, and the produced `feedback_focus.md` carries five lines including a heading not asked for. **Eight Reads.**
2. **Subagent** treats the batch as a subagent's problem. The main session's tool sequence is `Task → Write`. Deploying `.claude/agents/pattern-analyzer.md` — a name, one description, a three-tool whitelist — is what routes the ask to the subagent. **Zero Reads in main; one summary landed.**
3. The subagent's Read/Grep/Glob whitelist **enforced itself**: it observed that it could not Write, said so, and returned the findings for the parent session to write. That constraint is the whole design.
4. Both runs found the same three misconceptions, in the same order, on the same batch. This film is not about who caught more — it is about **where the reading happened**. The pattern-analyzer keeps the batch out of the room the build is being made in.
