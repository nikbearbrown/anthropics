# BUILD-LOG — cc-grading-skill-definition

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · built 2026-09-10.

## What the sessions gave the film

One teacher's ask — *grade Mira's paper, feedback and a final grade* — run four times against the same `scratch/` project (two week-4 writing responses on median vs mean, a rubric that says the criteria are pass/needs-work "never a percent," and `check_feedback.py` — a script that fails a feedback file if a grade appears).

The differences are in `.claude/skills/grading-feedback/SKILL.md`:

- **Run A (bare, 65.3 s · $0.432).** No skill file. Claude read the rubric, followed its shape well, and appended `## Final grade / 4/4 pass — meets every criterion.` The checker fails.
- **Run B (minimal skill, 14 lines, 51.7 s · $0.394).** Frontmatter + workflow only. `Skill(grading-feedback)` fires as a tool call in the stream-json. The shape holds. The grade still lands: `## Final grade / 3 pass / 1 needs work`. The checker still fails.
- **Run C (full skill, 27 lines, 62.2 s · $0.437).** Added `## Never` (three bullets forbidding grades even when asked) and `## Definition of done` (run `check_feedback.py`). Skill fires, reads the checker itself, refuses the grade, runs the checker. **PASS**. Claude then says on its own: *"per the skill's rules I did not attach a final grade."*
- **Run D (durability, second student, 54.6 s · $0.420).** Same skill, `priya.md`, ask still requests a grade. Same shape, same refusal, checker PASS.

The film's argument is the diff between these four runs and the checker's verdict on each output.

## Compile

- **Pass 1.** `art run`: Gate V 0/0/0 defects, GATE T PASS, BOOKEND PASS, SHARPNESS PASS, LOUDNESS PASS -24.25 LUFS, MASTER 3840×2160 h264, 317.7 s. Frame reads: score/ledger/verdict clean; **BFLOW blank** — used the wrong CCPlanCard schema (`{title, rows, footer}` instead of `{sections: [{title, numbered, items: [{text, path?}]}]}`).
- **Fix.** Patched BFLOW's props in `beat_sheet.json` directly (preserving all other build stamps and `actual_duration_s`), also updated `author_sheet.py` for future rebuilds. Cleared `shot.remotion.rendered` and deleted `media/BFLOW.mp4`.
- **Pass 2.** `art run` again. Only BFLOW re-rendered. All gates PASS. Frame read: BFLOW now renders "SKILL.md — anatomy" with five numbered items.
- **Final.** `art final`: master `cc-grading-skill-definition.mp4` — 317.7 s (5:17), 3840×2160, h264+aac.

## Two non-blocking warnings (checked and accepted)

- `SKIN LINT: cold open is CCSession not ClaudeComposerAsk` — cc-explainer explicitly overrides this in GATE BOOKEND (see `skills/make/cc-explainer/SKILL.md` §GATE BOOKEND). Cold open is a `CCSession` by design.
- `motion histogram: type carries 58%` — the film IS a sequence of typed-terminal sessions; `type` is the correct motion for `CCSession`/`CCPlainShell` beats. The 40% cap is a pantry-diversity heuristic; on this genre it does not apply.

## Not published

TOPOST only via `post`, only on ask. Master stays in the reel folder. `CC-BUILT.txt` is the supervisor's receipt.
