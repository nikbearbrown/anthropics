# AI for Coding: A Practitioner's Guide — CLI Video Ideas ("X with Claude")

*Note: This book has 3 chapters (introduction + 2 chapters). The intro establishes the execution-vs-judgment frame. Chapters 1 and 2 develop working methods. Cards below are drawn from the book's core concepts plus the judgment-frame exercises implied by the text.*

## Candidate 01 — "Ask Claude: What Would Have to Be True for This Code to Be Trusted?"
- Source: ai-for-coding-a-practitioners-guide/chapters/00-introduction.md
- Lane: BUILD (Claude Code)
- Hook: The draft looks clean. The code runs. The plan has phases. Nothing in the surface announces that a human still has work to do — until you ask the question the book opens with: "What would have to be true for this to be trusted?"
- The artifact: A Claude-powered code-review prompt that for any code artifact asks: (1) what assumptions does this code make that the machine could not know? (2) what failure modes does this hide that a domain expert would catch? (3) what consequences follow from using this output? Output: a structured judgment report (3 sections, bullet-point findings per question), rendered in the terminal.
- Prompt seed: `claude "Read this code. Answer three judgment questions: (1) What assumptions does this code make that cannot be verified from the code itself — domain knowledge, data contracts, environmental dependencies? (2) What failure modes would an expert in [domain] catch that this code does not surface? (3) What are the consequences if this output is wrong — who is affected, what decisions does it feed? Output as a structured judgment report: 3 sections, bullet-point findings." < my_code.py`
- Read / check: Verify the report names at least one domain-specific failure mode (not just "syntax error" or "edge case"); verify the consequences section names an actual downstream decision or user; verify the assumptions section names at least one thing the code cannot check about its own inputs.
- Human supplies: A real piece of code from the viewer's domain — the judgment report is only valuable when the code is real. A synthetic placeholder script produces generic output. Real code is required; synthetic code is NOT acceptable for the core lesson.
- Output medium: screen-recording mp4 — terminal running the prompt on a real script, structured report output, then the human annotating one finding.
- The change: Ask Claude to propose a test that would check one of its own assumptions; run the test; show whether the assumption holds or breaks.
- Teardown angle: The judgment frame is the part that cannot be delegated. Claude can name the assumptions — but whether those assumptions are acceptable is a decision that requires knowing who is responsible when the output leaves the screen.
- Exclusions: Specific language/framework tutorials, model internals, prompt engineering for accuracy (not judgment).
- Score: 9/10

## Candidate 02 — "Execution vs. Judgment: Build a Code Review Classifier with Claude"
- Source: ai-for-coding-a-practitioners-guide/chapters/00-introduction.md (recurring concept)
- Lane: BUILD (Claude Code)
- Hook: Execution is the production of an artifact. Judgment is the disciplined decision about whether that artifact should exist, whether it is right, and what consequences follow. The same code review comment can be either one — and mixing them is where AI-assisted review goes wrong.
- The artifact: A Claude-powered classifier that reads a code review comment and classifies it as: EXECUTION (syntactic correction, efficiency optimization, best-practice pattern) or JUDGMENT (ethical implication, domain-incorrect assumption, consequence for downstream user). Output: an annotated code-review document with E/J labels, plus a summary count showing the execution/judgment ratio.
- Prompt seed: `claude "Read these code review comments. For each, classify as EXECUTION (syntactic, efficiency, best-practice pattern — the machine can verify this) or JUDGMENT (domain-specific correctness, ethical implication, consequence for downstream decisions — requires a human with domain knowledge). Output annotated list with E/J labels and one-sentence reason. Then give the execution/judgment ratio and flag any JUDGMENT items that are currently written as if they were EXECUTION." < review_comments.txt`
- Read / check: Verify that "missing null check on line 14" is classified as EXECUTION; verify that "this model assumes the user consented to data collection" is classified as JUDGMENT; verify JUDGMENT items written in EXECUTION voice are flagged.
- Human supplies: A set of real code review comments from a domain the viewer works in. Synthetic comments with planted examples (one clear EXECUTION, one clear JUDGMENT, one ambiguous) are acceptable for the demo.
- Output medium: screen-recording mp4 — terminal running the classifier, annotated output, then a discussion of one mislabeled JUDGMENT-as-EXECUTION comment.
- The change: Take a JUDGMENT item currently written in EXECUTION voice ("change this variable name") and rewrite it as a judgment claim ("this variable name hides the ethical weight of the decision — the model is classifying a person, not a data point"); re-run classifier to confirm it now registers as JUDGMENT.
- Teardown angle: The execution/judgment boundary is where human competence lives. When review comments collapse all feedback into execution language, judgment gets automated away without anyone noticing.
- Exclusions: Specific code language tutorials, static analysis tooling, full code-quality rubric beyond E/J classification.
- Score: 9/10

## Candidate 03 — "Build a Code Audit That Asks: What Did the Machine Not Know?"
- Source: ai-for-coding-a-practitioners-guide/chapters/00-introduction.md + chapters/00-introduction.md recurring concept
- Lane: BUILD (Claude Code)
- Hook: A Claude-generated function is often technically correct and contextually wrong. The correctness is visible. The wrongness is invisible until someone with domain knowledge reads it and says: "This is correct code for a problem that doesn't exist in our system."
- The artifact: A two-pass code audit: Pass 1 (Claude-solo) asks Claude to review its own generated code for correctness. Pass 2 (Human-framed) runs the judgment questions — what domain knowledge was assumed, what data contracts were presumed, what edge cases require expertise to define. Output: a delta report showing what Pass 2 found that Pass 1 missed, rendered as a side-by-side markdown diff.
- Prompt seed: Pass 1: `claude "Review this function for correctness: syntax, edge cases, efficiency." < function.py` then Pass 2: `claude "Now review the same function for judgment failures: (1) What does this function assume about the domain that is not in the code? (2) What data contracts does it presume that a non-expert would not know to check? (3) What would an expert in [domain] catch that a generalist would miss? Label each finding MISSED-IN-PASS-1 if it was not caught in the first review." < function.py`
- Read / check: Verify Pass 2 names at least one domain-specific assumption not caught in Pass 1; verify the MISSED-IN-PASS-1 label appears on genuinely novel findings; verify the diff format shows the delta clearly.
- Human supplies: A real domain-specific function where the correctness/judgment gap is non-trivial. A synthetic function with a planted domain-incorrect assumption is acceptable.
- Output medium: screen-recording mp4 — terminal running both passes, the delta report, then the human annotating one MISSED-IN-PASS-1 finding.
- The change: Fix the top MISSED-IN-PASS-1 finding (add a domain-specific guard clause or annotation); re-run both passes; verify the gap narrows.
- Teardown angle: The two-pass structure is not about making Claude smarter. It is about making the human's domain knowledge visible at the moment it is needed — after execution is done and before judgment is outsourced.
- Exclusions: Specific language frameworks, static analysis tools, full code quality rubric, prompt engineering for accuracy improvement.
- Score: 8/10

## Candidate 04 — "Generate a Judgment Frame for Any Code Task Before Writing a Line"
- Source: ai-for-coding-a-practitioners-guide/chapters/00-introduction.md (Closing Return)
- Lane: BUILD (Claude Code)
- Hook: "Return to the polished artifact. Do not ask first whether it is impressive. Ask what would have to be true for it to be trusted." That question, run before writing a single line of code, changes what gets built.
- The artifact: A pre-task judgment brief: a Claude-generated document that, given a coding task description, produces: (1) the domain constraints the code must respect, (2) the failure modes that require expert sign-off before deployment, (3) the consequences if the output is wrong, (4) the question to ask the machine that it cannot answer. The brief is generated before any code is written and becomes the acceptance criteria.
- Prompt seed: `claude "I am about to write code to [task description]. Before I write a line, produce a judgment brief: (1) domain constraints the code must respect — list any rules from the domain that are not specifiable in pure code, (2) failure modes requiring expert sign-off — list what could go wrong that I would need a domain expert to assess, not just a test suite, (3) consequences if wrong — who is affected, what decisions does this output feed, (4) the one question I must answer myself that you cannot answer for me. Format as a structured brief I can use as acceptance criteria." > judgment-brief.md`
- Read / check: Verify the brief names domain-specific constraints (not just "handle null inputs"); verify the expert sign-off section names a real domain judgment (not just "add error handling"); verify the "question you must answer" is genuinely outside the machine's scope.
- Human supplies: A real coding task description from the viewer's domain. The brief is only valuable with a real task — synthetic is NOT acceptable; a placeholder produces generic output.
- Output medium: screen-recording mp4 — terminal generating the brief, then using it to annotate the eventual code output against its acceptance criteria.
- The change: After writing the code, compare the output against each point of the judgment brief; flag any criterion that the code does not address; revise or document the gap.
- Teardown angle: The judgment brief inverts the workflow. Most developers write code, then check if it's correct. The judgment brief asks the hardest questions first and lets the code answer them.
- Exclusions: Specific frameworks, TDD methodology, code quality metrics beyond the judgment frame.
- Score: 8/10
