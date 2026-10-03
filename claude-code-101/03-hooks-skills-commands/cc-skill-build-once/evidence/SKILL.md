---
name: grading-workflow
description: >
  Grade a Thursday short-answer submission from `student-submission*.md`
  in this folder against a fixed four-part rubric and write the feedback
  to `feedback/<student>.md`. Use when the user says "grade the submission",
  "grade this", "grade <name>'s submission", or names a `student-submission*.md`
  file to grade. Feedback-only: no final grade is ever assigned by this skill.
---

# grading-workflow — Thursday short-answer feedback, feedback-only

You grade one short-answer submission at a time against the same four-part
rubric, and write the feedback to `feedback/<student-slug>.md`. The skill's
job is feedback, not scoring — the teacher assigns the final grade after
reading it.

## Workflow

1. **Read** the target `student-submission*.md` file (the one the user named,
   or the only one that matches).
2. **Extract** the student's name (from the `# Student submission — <Name>, …`
   heading) and the prompt (from the `**Prompt.**` line).
3. **Grade against the rubric** — one heading per criterion, one paragraph
   each, ending each with a bolded verdict `**pass**` or `**needs work**`:
     - `## 1. Mechanism` — does the answer state the underlying reason
       correctly? Cite the sentence.
     - `## 2. Example` — does the numeric example check out? Verify the
       arithmetic explicitly.
     - `## 3. Argument` — does the example actually support the claim,
       or is it a decorative aside?
     - `## 4. Precision of language` — technical vocabulary used correctly;
       any imprecise phrasing flagged with a specific rewrite.
4. **One growth line** — a `## Growth` heading with exactly one sentence
   naming the next thing this student should learn to say.
5. **Write** the result to `feedback/<student-slug>.md`, where
   `<student-slug>` is the student's first name lowercased.
6. **Verify** — before saying "done", run `python3 check_grade.py <path>`
   on the file you wrote. It must print `PASS`. If it prints `FAIL`, fix
   the feedback file until it passes.

## Never

- **Never** assign a final letter grade (A, B, C, D, F) or a numeric grade
  (e.g. `92/100`, `85%`) anywhere in the feedback file. Feedback only.
- **Never** invent a submission — only grade a file that exists in the folder.
- **Never** exceed one paragraph per rubric criterion.
- **Never** paraphrase the student's example to make it look worse; quote it.

## Definition of done

`python3 check_grade.py feedback/<student-slug>.md` prints `PASS`. That
means: four rubric headings present, each with a bolded verdict; a `Growth`
line; no letter grade; no numeric grade.
