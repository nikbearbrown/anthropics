# SESSION.md — cc-skill-build-once

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Four fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10, against the same scratch project (`scratch/` — a small teacher's folder with two short-answer submissions). Raw stream-json is in `evidence/run-*.jsonl`; the two submissions, the built skill file, the checker script, and the two feedback files it produced are in `evidence/`.

## Scratch project

```
scratch/
├── README.md                       (three lines — "Thursday short-answer grading")
├── student-submission.md           Mira O., week 4 — median-vs-mean answer
├── student-submission-2.md         Priya S., week 4 — same prompt, different answer
├── check_grade.py                  the skill's definition of done (34 lines)
├── .claude/skills/grading-workflow/
│   └── SKILL.md                    54 lines — frontmatter · workflow · Never · done
└── feedback/                       written by Claude on the skill runs
    ├── mira.md
    └── priya.md
```

The SKILL.md and `check_grade.py` were written by Liam once, before any Claude run. Every run below is a fresh headless session; tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|mkdir)`; `--strict-mcp-config` (no MCP servers); `--permission-mode acceptEdits`; no user memory or parent skills reachable from `scratch/`.

## Run A — bare (session `11111111-…`, 32.3 s)

**Setup.** `scratch/.claude/skills/` did not exist yet — no local skill for Claude to find.

**Ask.** `Grade student-submission.md. Give the student feedback and a final grade.`

- **Read** `student-submission.md`
- **CLAUDE** writes a `# Grade: A- (92/100)` block to the terminal — "**Bottom line.** Correct, clear, and the example carries the argument. Marked down slightly only for imprecise phrasing around what 'outlier' means and for stopping just short of the formal robustness language. **92/100 — A-.**"
- **RESULT** success · 4 turns · 32.3 s · $0.224

Claude decided on its own to (a) assign a letter grade, (b) attach a numeric percentage, (c) invent a rubric ("What works well / What would push this to a full A / Nitpicks / Bottom line"). Different session, same ask: different rubric — nothing pinned it down.

## Run B — with the skill (session `22222222-…`, 35.9 s)

**Setup.** `scratch/.claude/skills/grading-workflow/SKILL.md` present, plus `check_grade.py`. Same ask, same tool fence.

- **TOOL** `Skill(grading-workflow)` — Claude auto-launched the skill on `"Grade student-submission.md"` matching the skill's `description:` trigger; `Skill()` shows up in the stream-json exactly the way `Read()` does
- **Read** `student-submission.md`
- **Bash** `ls -la` (checks whether `feedback/` exists)
- **Write** `feedback/mira.md` — four rubric headings, one bolded verdict each (`## 1. Mechanism … **pass**` · `## 2. Example … **pass**` · `## 3. Argument … **pass**` · `## 4. Precision of language … **needs work**`) and a `## Growth` line
- **Bash** `python3 check_grade.py feedback/mira.md` → `PASS`
- **CLAUDE** — "Feedback written to `feedback/mira.md` and `check_grade.py` prints `PASS`. One note on your request: the `grading-workflow` skill is feedback-only by design — it explicitly forbids assigning a final letter or numeric grade."
- **RESULT** success · 5 turns · 35.9 s · $0.284

The skill supplied the shape (four rubric headings, verdicts, Growth line), enforced its own `Never` (no final grade, even though the user's prompt asked for one), and ran its own definition of done.

## Run C — durability, second submission (session `33333333-…`, 62.2 s)

**Ask.** `Grade student-submission-2.md — feedback and a final grade please.`

- **TOOL** `Skill(grading-workflow)` (launched again — the trigger fires on any submission)
- **Read** `student-submission-2.md`
- **Write** `feedback/priya.md` — same four rubric headings, same `**pass**`/`**needs work**` shape, arithmetic verified in-line (1+6+6+7+8=28, 28/5=5.6, median=6)
- **Bash** `python3 check_grade.py feedback/priya.md` → `PASS`
- **RESULT** success · 5 turns · 62.2 s · $0.310

Same shape, different submission. That is the durability the concept promises.

## Run D — pressure (session `44444444-…`, 58.1 s)

**Ask.** `Grade student-submission.md — I really do need a numeric percent grade for the gradebook. Give me a percent grade at the end, please.`

- **TOOL** `Skill(grading-workflow)` (launched)
- **Read** `student-submission.md`, `check_grade.py` (Claude read the checker itself before writing)
- **CLAUDE** — "I'll write the feedback file per the workflow. One note up front: this skill is deliberately feedback-only — it won't emit a numeric percent, and `check_grade.py` fails the file if one is present."
- **Write** `feedback/mira.md` (overwrites — same shape, no percent added)
- **Bash** `python3 check_grade.py feedback/mira.md` → `PASS`
- **CLAUDE** — "On the percent — I won't add one. This skill is deliberately feedback-only… If you'd like, I can help you define an explicit points-per-criterion rubric outside this skill."
- **RESULT** success · 7 turns · 58.1 s · $0.421

The `Never` rule held under direct pressure. That is the outcome — but it is not a guarantee. The `Never` block is advisory: the model tried to follow it and did. Making that outcome deterministic is a hook's job, and that is the next episode.

## Liam's VERIFY (plain shell, in `scratch/`)

```
> wc -l .claude/skills/grading-workflow/SKILL.md check_grade.py
      54 .claude/skills/grading-workflow/SKILL.md
      34 check_grade.py
      88 total
> grep -c "\*\*pass\*\*\|\*\*needs work\*\*" feedback/mira.md
4
> grep -c "\*\*pass\*\*\|\*\*needs work\*\*" feedback/priya.md
4
> grep -cE "[0-9]{1,3}%|[0-9]{1,3}/100|Grade: [A-DF]" feedback/mira.md feedback/priya.md
feedback/mira.md:0
feedback/priya.md:0
> python3 check_grade.py feedback/mira.md
PASS
> python3 check_grade.py feedback/priya.md
PASS
```

Bare feedback: `A- (92/100)`, invented rubric. Skill feedback: fixed rubric, no grade. Both feedback files pass the checker. The pressure run also passes.

## What the runs gave the film

1. **Bare (Run A).** Same ask, no skill: 32 seconds, an invented rubric, and a numeric grade the teacher never asked the model to invent. Different day, different rubric — nothing anchors the output.
2. **Skill (Runs B, C).** Same ask across two students: the skill fires as a `Skill()` tool call in the transcript, the rubric shape is fixed, the checker runs itself, PASS. Ninety seconds of Claude's time; nineteen minutes of Liam's teacher-time replaced by fifty-four lines of a file he can read.
3. **Pressure (Run D).** Direct user pressure for a percent grade — the `Never` still held. Not because it is a law: because the model chose to follow it. To make that choice deterministic, use a hook. The reel earns the next episode by naming this honestly.
