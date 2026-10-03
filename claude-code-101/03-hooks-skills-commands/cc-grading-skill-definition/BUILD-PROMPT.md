# BUILD-PROMPT — cc-grading-skill-definition

For a future session that wants to rebuild or riff this reel.

## The film's job

Show that a **reusable skill definition** in Claude Code — the file at `.claude/skills/<name>/SKILL.md` — has an anatomy, and each of its four fields earns its keep by what breaks when the field is missing.

The proof is four real headless `claude -p` runs against the same one-sentence teacher's ask, differing only in what the SKILL.md file contains:

1. **Bare** — no `.claude/skills/`. Claude reads the rubric, follows its shape, adds a `## Final grade` because the ask asked. The checker fails.
2. **Minimal skill** (frontmatter + workflow, 14 lines). `Skill()` fires. Shape holds. `## Final grade` still lands. Checker still fails.
3. **Full skill** (frontmatter + workflow + `## Never` + `## Definition of done`, 27 lines). `Skill()` fires. Never refuses the grade. Claude reads `check_feedback.py` itself and runs it. PASS.
4. **Durability** — full skill on a different student. Same shape, same refusal. PASS.

## The one word to reconsider

BIDEA corrects **"reads"** to **"obeys"**. A rubric is *read*; a skill is *obeyed*. That is the film's misconception.

## The four fields (BFLOW anatomy)

```
frontmatter: name              → the handle
description:                   → the trigger (Claude matches your ask to it)
## Workflow                    → the shape
## Never                       → the refusal, even under pressure
## Definition of done          → the check the skill runs on itself
```

## The scratch project

`scratch/` — a teacher's folder: `submissions/{mira,priya}.md` (two week-4 writing responses on median vs mean), `rubric/rubric.md` (four criteria + Growth, "never a percent"), `check_feedback.py` (fails the file if any grade appears), `.claude/skills/grading-feedback/SKILL.md` (rewritten between runs).

## Voice

Liam, Kokoro `am_onyx`, Teardown register. First person, present tense. Cold open: "This is Liam, in for Bear." BVDT starts "Let's recap with Claude." BOUT ends "Liam, in for Bear."

## Rebuild pointers

- **Compile:** from `books/`, `./brutalist-art/art run anthropics/claude-code-101/03-hooks-skills-commands/cc-grading-skill-definition` then `./brutalist-art/art final <path>`.
- **Audio:** `python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>`. Never re-run `author_sheet.py` inside the reel folder after audio is generated (regenerate to a temp dir and merge props, or the audio stamps get wiped).
- **Fact-check:** `python3 brutalist-art/runtime/qc/factcheck_check.py <reel>` must print `clean`.
