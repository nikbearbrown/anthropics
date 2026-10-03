# SESSION.md — cc-skill-development

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10. Same task — wrap a local helper in a Claude Code skill — with three different asks. Raw stream-json in `evidence/run-{bare,rules,checker}.jsonl`; the three shipped SKILL.md files (and one references/ file) in `evidence/SKILL.{bare,rules,checker}.md` and `evidence/troubleshooting.rules.md`; the scratch inputs (`README.md`, `csv_shape.py`, `sample.csv`, `validate_skill.py`) also in `evidence/`.

## The scratch project — what the skill wraps

`csv_shape.py` — a 40-line standard-library script that prints the shape of a CSV: rows, columns, and a per-column dtype guessed from the first non-empty value (`int`, `float`, `bool`, `str`, `empty`). `sample.csv` — a 3-row test file. `validate_skill.py` — the skill's definition of done. It checks six rules distilled from Anthropic's own `plugin-dev/skills/skill-development/SKILL.md`:

1. YAML frontmatter with `name:` and `description:`.
2. Description opens with **This skill should be used** (third person).
3. Description contains at least **two** trigger phrases in double quotes.
4. Body contains **none** of `you should`, `you need`, `you can`, `you must`, `you may`.
5. Body references `csv_shape.py`.
6. Body is 200–2000 words.

## The one-line task

Each run got a different ask, in three fresh working directories:

| Run | Ask |
|---|---|
| **bare** | "Create a Claude Code skill at `skills/csv-shape/SKILL.md` that wraps `csv_shape.py` so future Claude sessions know when to run it." |
| **rules** | Same, plus **three rules**: (a) third-person description with quoted trigger phrases; (b) imperative body; (c) keep SKILL.md under 400 words by moving detail to `references/troubleshooting.md` and reference it. |
| **checker** | "Create a skill at `skills/csv-shape/SKILL.md` that PASSES `python3 validate_skill.py`. Read the checker to see what to satisfy." |

Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|wc|mkdir)`; `--strict-mcp-config`.

## Run: bare (session `a3462115-…`)

- **TOOL** `Bash` `ls …` · **Read** `README.md` · **Read** `csv_shape.py` · **Read** `sample.csv` · **Read** `validate_skill.py`
- **TOOL** `Bash` `mkdir -p skills/csv-shape` · **Write** `skills/csv-shape/SKILL.md` (106 lines)
- **TOOL** `Bash` `python3 validate_skill.py skills/csv-shape/SKILL.md` → `PASS: 630 words, all six rules satisfied`
- **CLAUDE:** *"Validator reports PASS — SKILL.md at `skills/csv-shape/SKILL.md` meets all six rules (630 words, both trigger phrases quoted, third-person description, references `csv_shape.py`, no second-person forms)."*
- **RESULT:** success · turns=10 · 73.7 s · $0.5406

What it wrote: one file, 630 words. Frontmatter has four quoted triggers and reads third-person. Body covers purpose, when-to-invoke, how-to-run, interpreting output, when-output-looks-wrong, boundaries, and related-follow-ups — all inline. No `references/` folder.

## Run: rules (session `9bb75a97-…`)

- **TOOL** `Bash` `ls -la …` · **Read** `README.md` · **Read** `csv_shape.py` · **Read** `validate_skill.py` · **Read** `sample.csv`
- **TOOL** `Bash` `mkdir -p skills/csv-shape/references` · **Write** `skills/csv-shape/SKILL.md` (50 lines) · **Write** `skills/csv-shape/references/troubleshooting.md` (52 lines)
- **TOOL** `Bash` `python3 validate_skill.py skills/csv-shape/SKILL.md` → `PASS: 367 words, all six rules satisfied`
- **CLAUDE:** *"Result: `PASS: skills/csv-shape/SKILL.md meets all six rules (367 words)`."*
- **RESULT:** success · turns=10 · 83.7 s · $0.5661

What it wrote: **two** files. `SKILL.md` at 367 words — the description, one paragraph of when-to-reach-for-it, how-to-run, one interpret-output block, a one-line hand-off to `references/troubleshooting.md`, and a boundaries paragraph. `references/troubleshooting.md` at 552 words carries every edge case: no header, ragged rows, quoted numbers, weird encodings, tab-separated data. Progressive disclosure, made real: SKILL.md loads on every trigger; the reference loads only when Claude actually hits an edge case.

## Run: checker (session `166703a2-…`)

- **TOOL** `Bash` `ls …` · **Read** `csv_shape.py` · **Read** `validate_skill.py`
- **TOOL** `Bash` `mkdir -p skills/csv-shape` · **Write** `skills/csv-shape/SKILL.md` (110 lines)
- **TOOL** `Bash` `python3 validate_skill.py` → `PASS: 635 words, all six rules satisfied`
- **CLAUDE:** *"PASS: 635 words, all six rules satisfied. The skill at `skills/csv-shape/SKILL.md` has third-person frontmatter with 5 quoted trigger phrases, references `csv_shape.py` in the body, avoids all banned second-person forms."*
- **RESULT:** success · turns=7 · 63.9 s · $0.4401

What it wrote: one file, 635 words — the shape of the bare run. Passed every rule the checker knows. But no `references/` — the progressive-disclosure principle the checker cannot see was skipped. The checker verifies the letters of Anthropic's rules; it cannot verify the spirit.

## Liam's VERIFY (plain shell, in `evidence/`)

```
> for r in bare rules checker; do wc -w SKILL.$r.md; done
     630 SKILL.bare.md
     367 SKILL.rules.md
     635 SKILL.checker.md
> ls SKILL.rules.md troubleshooting.rules.md
SKILL.rules.md              troubleshooting.rules.md
> wc -w troubleshooting.rules.md
     552 troubleshooting.rules.md
> ls scratch/run-bare/skills/csv-shape
SKILL.md
> ls scratch/run-rules/skills/csv-shape
SKILL.md   references
> ls scratch/run-checker/skills/csv-shape
SKILL.md
> for r in bare rules checker; do
    python3 validate_skill.py SKILL.$r.md | tail -1
  done
PASS: SKILL.bare.md meets all six rules (630 words)
PASS: SKILL.rules.md meets all six rules (367 words)
PASS: SKILL.checker.md meets all six rules (635 words)
> for r in bare rules checker; do
    grep -Ec "you should|you need|you can|you must|you may" SKILL.$r.md
  done
0
0
0
> grep -c '"' SKILL.bare.md          # count of double quotes (triggers × 2)
8
> grep -c '"' SKILL.rules.md
12
> grep -c '"' SKILL.checker.md
10
> grep -in "reference" SKILL.rules.md | head -2
46:For unexpected results …, consult `references/troubleshooting.md` in this skill folder.
> grep -in "reference" SKILL.bare.md
> grep -in "reference" SKILL.checker.md
```

## What the runs gave the film

1. **All three passed the checker.** The six rules are not the argument; a rule-list is not the pedagogy. Passing them is table stakes.
2. **The rules run made a folder; the other two made a file.** Only the rules run wrote `references/troubleshooting.md` — the pattern Anthropic actually teaches (progressive disclosure): SKILL.md lean, details in `references/` loaded on demand. 367 words in the always-loaded body vs 630 in the bare and 635 in the checker.
3. **The checker case is the trap.** Given only the checker and told to pass it, Claude passed it — and produced a 635-word monolith. The letters, none of the spirit. That's why validate_skill.py by itself does not name a good skill; "who this is for and what done means" (PROJECT.md's job in the exemplar reel) has no analogue inside the checker.
