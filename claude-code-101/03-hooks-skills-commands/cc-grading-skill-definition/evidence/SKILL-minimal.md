---
name: grading-feedback
description: Use when grading a student writing response against a rubric. Reads the submission and the rubric file, writes a per-criterion feedback file to feedback/<name>.md.
---

# Grading feedback

For a submission in `submissions/` and a rubric in `rubric/rubric.md`:

1. Read the submission.
2. Read the rubric — its criteria and its Growth line.
3. Write `feedback/<name>.md` with one `## <criterion>` heading per rubric item,
   a two- or three-sentence note under each, and a `## Growth` section at the end
   naming the single revision that would most improve the piece.
