# PROMPTS — cc-skill-development

The three real Claude Code sessions (`claude -p`, headless, `Claude Code 2.1.150`, 2026-09-10). Raw stream-json is in `evidence/run-{bare,rules,checker}.jsonl`; the shipped files are in `evidence/`.

Common flags on every run:

```
--output-format stream-json --verbose
--max-turns 10..12
--permission-mode acceptEdits
--strict-mcp-config
--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(wc:*),Bash(mkdir:*)"
< /dev/null
```

## Run 1 — bare

Working directory: `scratch/run-bare/` (contains `README.md`, `csv_shape.py`, `sample.csv`, `validate_skill.py`).

```
Create a Claude Code skill at skills/csv-shape/SKILL.md that wraps
csv_shape.py so future Claude sessions know when to run it. Write only
the SKILL.md file, no other files, and do not touch csv_shape.py or the
other scratch files.
```

## Run 2 — rules (progressive disclosure)

Working directory: `scratch/run-rules/` (same four files).

```
Create a Claude Code skill at skills/csv-shape/SKILL.md that wraps
csv_shape.py. Follow these three rules from Anthropic's plugin-dev
skill-development guide: (1) the frontmatter description must be
third-person and open with 'This skill should be used when...' with
concrete trigger phrases in double quotes; (2) the body must use
imperative/infinitive form — never 'you should', 'you need', or 'you
can'; (3) keep SKILL.md lean (under 400 words) by moving detailed edge
cases to references/troubleshooting.md, and reference that file from
SKILL.md. Also create references/troubleshooting.md. Then run: python3
validate_skill.py skills/csv-shape/SKILL.md and report the result.
```

## Run 3 — checker only

Working directory: `scratch/run-checker/` (same four files).

```
Create a Claude Code skill at skills/csv-shape/SKILL.md that PASSES
python3 validate_skill.py. Read validate_skill.py to understand what to
satisfy. Do not read any other guidance — just make it pass the checker.
```

## The follow-up prompt the reel hands the viewer (BHTF)

```
For a skill I'll describe in one sentence, ask me what a user would
actually type to trigger it. Draft the frontmatter with those phrases
in quotes. Then propose which sections belong in SKILL.md and which in
references/. Don't write the skill yet.
```
