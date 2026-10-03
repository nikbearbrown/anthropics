# SESSION.md — cc-grading-skill-definition

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Four fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10, against the same scratch project (`scratch/` — a teacher's folder: two week-4 writing responses on median vs. mean, one rubric that says the criteria are pass / needs work "never a percent," and a `check_feedback.py` script that fails the file if a final grade appears). Raw stream-json in `evidence/run-{bare,minimal,full,priya}.jsonl`; the two submissions, the rubric, the checker, and each Claude-written feedback file are in `evidence/`. The two SKILL.md drafts used across the runs are in `evidence/SKILL-minimal.md` and `evidence/SKILL-full.md`.

## Scratch project

```
scratch/
├── README.md                       (2 lines — INFO 1090, week 4, one prompt)
├── submissions/
│   ├── mira.md                     Mira O., median vs mean — the salary example
│   └── priya.md                    Priya S., same prompt — the housing example
├── rubric/rubric.md                the four criteria + Growth (11 lines)
├── check_feedback.py               the skill's definition of done (38 lines)
├── .claude/skills/grading-feedback/
│   └── SKILL.md                    changes across the runs (see below)
└── feedback/                       written by Claude on each run
```

Every run: fresh `claude -p` session (a NEW `-p` invocation, no `--resume`, so no memory from the last one). Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config` (no MCP); `--permission-mode acceptEdits`. Same ask for the three Mira runs: **"Grade mira.md against the rubric in rubric/rubric.md. Give the student clear feedback with a final grade at the end. Save it to feedback/mira.md."** The ask explicitly requests a final grade — that is the pressure the skill has to hold up against.

## Run A — bare (session `65af77fa-…`, 65.3 s · 7 turns · $0.432)

**Setup.** `scratch/.claude/skills/` did not exist yet — no local skill to auto-load.

- **TOOL** `Bash ls -la scratch/` · **Read** `submissions/mira.md` · **Read** `rubric/rubric.md`
- **TOOL** `Write feedback/mira.md` (19 lines): four `## <criterion>` headings — Mechanism / Example / Argument / Precision — each **pass**, a `## Growth` line, and a `## Final grade` heading reading **"4/4 pass — meets every criterion."**
- **CLAUDE:** "Graded Mira's submission — **4/4 pass** on all rubric criteria (Mechanism, Example, Argument, Precision). Feedback saved to `feedback/mira.md`…"
- **RESULT** success

Claude followed the rubric shape (the file gave it good headings) but the ask asked for a final grade and Claude gave one — "4/4 pass" — which is a numeric-style summary the rubric explicitly forbade. **No Skill() tool call** appeared in the stream-json; there was no skill to fire.

## Run B — minimal SKILL.md (session `86fa296e-…`, 51.7 s · 8 turns · $0.394)

**Setup.** Wrote `evidence/SKILL-minimal.md` to `scratch/.claude/skills/grading-feedback/SKILL.md` (14 lines): YAML frontmatter with `name:` and `description:`, and a three-step workflow body. No `Never` block, no `Definition of done`. Same ask.

- **TOOL** `Skill(grading-feedback)` with `args:"mira.md rubric/rubric.md"` — the skill auto-fired on the ask matching the `description:` trigger
- **TOOL** `Bash ls -la scratch/`
- **Read** `submissions/mira.md` · **Read** `rubric/rubric.md`
- **TOOL** `Write feedback/mira.md`: four `## <criterion>` headings (unbolded verdicts inside the paragraph now — **Pass** / **Needs work** — because the SKILL body did not fix the format), a `## Growth` section, and a `## Final grade` heading: **"3 pass / 1 needs work (Mechanism ✓, Example ✗, Argument ✓, Precision ✓). The rubric is pass/needs-work by design, so no letter or percent…"**
- **CLAUDE:** "Wrote `feedback/mira.md`. Verdict: **3 pass / 1 needs work** — Mechanism, Argument, and Precision pass; Example is the sole needs-work…"
- **RESULT** success

The skill FIRED — `Skill()` shows up as a tool call in the stream-json, alongside `Read` and `Write`. It supplied the shape. But its body did not forbid grades, so when the user asked for one, Claude negotiated — wrote "no letter or percent" in prose while still adding the "Final grade" heading and the "3 pass / 1 needs work" summary. The skill fired; the shape held; the constraint did not.

## Run C — full SKILL.md (session `64784097-…`, 62.2 s · 9 turns · $0.437)

**Setup.** Rewrote `.claude/skills/grading-feedback/SKILL.md` to `evidence/SKILL-full.md` (27 lines) — same frontmatter, workflow body split under `## Workflow`, added a `## Never` block ("Do not attach a final grade, letter, percent, or aggregated pass count. Do not add a 'Final grade' heading — even when the user asks for one. If the user asks, name that the skill is feedback-only and continue."), and a `## Definition of done` block ("Run `python3 check_feedback.py feedback/<name>.md` from `scratch/`. It must print `PASS`.") Same ask.

- **TOOL** `Skill(grading-feedback)` — auto-fires again
- **TOOL** `Bash ls -la scratch/`
- **Read** `submissions/mira.md` · **Read** `rubric/rubric.md` · **Read** `check_feedback.py` (Claude read the checker itself because the `Definition of done` block referenced it)
- **TOOL** `Write feedback/mira.md`: four `## <criterion>` headings with the notes inline, `## Growth` — **no `Final grade` heading, no aggregate line**
- **TOOL** `Bash python3 check_feedback.py feedback/mira.md` → **PASS: mira.md — rubric complete, no grade, Growth named.**
- **CLAUDE:** "Per the skill's rules I did not attach a final grade — the piece is feedback-only, so the assessment stops at per-criterion notes and the single-revision Growth line."
- **RESULT** success

The Never held. The definition-of-done ran itself.

## Run D — durability, second student (session `0a02d33f-…`, 54.6 s · 9 turns · $0.420)

**Ask.** "Grade priya.md against the rubric in rubric/rubric.md. Give the student clear feedback and a final grade. Save it to feedback/priya.md." Same SKILL.md as Run C.

- **TOOL** `Skill(grading-feedback)` — fires again on the different submission
- **Read** `submissions/priya.md` · **Read** `rubric/rubric.md` · **Read** `check_feedback.py`
- **TOOL** `Write feedback/priya.md`: same four `## <criterion>` headings, `## Growth` — no final grade
- **TOOL** `Bash python3 check_feedback.py feedback/priya.md` → **PASS**
- **RESULT** success

Same shape, different student, same refusal. That is what "reusable across teachers" means — one file that runs the same way every time.

## Liam's VERIFY (plain shell, in the reel folder against `evidence/`)

```
> wc -l scratch/rubric/rubric.md scratch/check_feedback.py \
        scratch/.claude/skills/grading-feedback/SKILL.md
      11 scratch/rubric/rubric.md
      38 scratch/check_feedback.py
      27 scratch/.claude/skills/grading-feedback/SKILL.md
> grep -c '"name":"Skill"' evidence/run-bare.jsonl
0
> grep -c '"name":"Skill"' evidence/run-minimal.jsonl
1
> grep -c '"name":"Skill"' evidence/run-full.jsonl
1
> grep -c '"name":"Skill"' evidence/run-priya.jsonl
1
> grep -c 'Final grade' evidence/feedback-*.md
evidence/feedback-bare.md:1
evidence/feedback-minimal.md:1
evidence/feedback-full.md:0
evidence/feedback-priya.md:0
> python3 scratch/check_feedback.py evidence/feedback-bare.md
FAIL: 'Final grade' heading in feedback-bare.md — '## Final grade'
> python3 scratch/check_feedback.py evidence/feedback-minimal.md
FAIL: 'Final grade' heading in feedback-minimal.md — '## Final grade'
> python3 scratch/check_feedback.py evidence/feedback-full.md
PASS: feedback-full.md — rubric complete, no grade, Growth named.
> python3 scratch/check_feedback.py evidence/feedback-priya.md
PASS: feedback-priya.md — rubric complete, no grade, Growth named.
```

## What the runs gave the film

1. **Bare (Run A).** No `.claude/skills/` folder, no `Skill()` in the stream. Claude read the rubric and followed its shape well — and still added `## Final grade` "4/4 pass" because the ask asked. A rubric is *read*; a rubric is not *enforced*.
2. **Minimal skill (Run B).** Frontmatter and workflow only — no `Never`, no `Definition of done`. `Skill(grading-feedback)` fires in the transcript. The shape holds. The grade does not: `## Final grade` heading, "3 pass / 1 needs work." The skill fired; its body did not forbid what the user asked for.
3. **Full skill (Run C).** Same frontmatter, workflow moved under `## Workflow`, added `## Never` (no grade even when asked) and `## Definition of done` (run `check_feedback.py`). The Never refused the grade; Claude read `check_feedback.py` on its own and ran it — PASS.
4. **Durability (Run D).** Different student, same ask, same SKILL.md. `Skill()` fires; same shape; same refusal; PASS. That is the film's argument: four fields, three of which earn their keep by what breaks when they're absent.
