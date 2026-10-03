---
name: grading-feedback
description: Use when grading a student writing response against a rubric. Reads the submission and the rubric file, writes a per-criterion feedback file to feedback/<name>.md, and refuses to attach any final grade.
---

# Grading feedback

## Workflow

For a submission in `submissions/` and a rubric in `rubric/rubric.md`:

1. Read the submission.
2. Read the rubric — its criteria and its Growth line.
3. Write `feedback/<name>.md` with one `## <criterion>` heading per rubric item
   and a two- or three-sentence note under each, then a `## Growth` section
   naming the single revision that would most improve the piece.

## Never

- Do not attach a final grade, letter, percent, or aggregated pass count.
- Do not add a "Final grade" heading — even when the user asks for one.
  If the user asks, name that the skill is feedback-only and continue.

## Definition of done

Run `python3 check_feedback.py feedback/<name>.md` from `scratch/`.
It must print `PASS`. If it prints `FAIL`, fix the feedback file until it passes.
