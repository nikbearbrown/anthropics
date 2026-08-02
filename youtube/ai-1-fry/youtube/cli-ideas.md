# AI+1 (Fry Edition) — CLI Video Ideas ("X with Claude")

*Note: ai-1-fry is a 14-chapter fork of ai-1, covering chapters 00-12 plus appendices. It shares the same pipeline (Tic TOC → new_book.py → Cowork → enrichment) but is a shorter, more focused variant. Cards below harvest the fry-specific exercises and pipeline steps; build lane is identical.*

## Candidate 01 — "One-Sentence Learning Outcome: Run Tic TOC /i1 Until It Passes"
- Source: ai-1-fry/chapters/04-generating-your-tiktoc.md (LLM Exercise 1)
- Lane: BUILD (Claude Code)
- Hook: "The reader learns to use AI in their freelance design practice" is a topic, not a learning outcome. Tic TOC will not let it stand — and the pushback transcript is the lesson.
- The artifact: A capability statement that passes Tic TOC's /i1 gate — a sentence of the form "The reader learns to [demonstrable verb] [specific object] under [specific condition]" — validated by a Python gate checking for prohibited vague verbs. Rendered as a terminal session with the Tic TOC exchange visible.
- Prompt seed: `claude "Run Tic TOC /i1. My book concept: [user supplies]. Push back on any capability statement using: understand, appreciate, be aware, be familiar. Require demonstrable outcome verbs. Do not advance until the statement passes." > i1-transcript.md` then `python3 -c "import re; s=open('i1-transcript.md').read(); verbs=['understand','appreciate','be aware','be familiar']; [print(f'FAIL: {v}') for v in verbs if v in s.lower()] or print('PASS: capability statement clear of vague verbs')"`
- Read / check: Verify the gate fires on a first-draft vague statement; verify the revised statement contains a demonstrable verb (defend, produce, triage, apply); verify the Python check produces a clean PASS on the final draft.
- Human supplies: A real book concept to run the session on. Synthetic is NOT acceptable — the pushback only appears when there is a real author trying to defer the hard question.
- Output medium: screen-recording mp4 — terminal showing the /i1 exchange, the failed gate, the revision, and the passed gate.
- The change: Take the final passing capability statement and ask Claude "what would it look like if the book failed to deliver on this outcome?" — run that as a stress-test in the same session.
- Teardown angle: The commitment is not a constraint on the book. It IS the book. The author who finishes /i1 in 30 seconds by accepting their first answer has not had a productive session.
- Exclusions: Full 13-gate Tic TOC walkthrough, Backward Design theory, acquisitions pragmatist discipline.
- Score: 9/10

## Candidate 02 — "Audit a Raw Pantry File with Claude: The 45-Minute Evaluation Pass"
- Source: ai-1-fry/chapters/06-research-pass.md (LLM Exercises)
- Lane: BUILD (Claude Code)
- Hook: A pantry file that says "studies show 78% of design firms are integrating AI" looks like research. Cowork will draft a chapter from it and produce authoritative-sounding prose that cites no one, sourced from nothing.
- The artifact: A Python-driven pantry auditor that flags: (a) "studies show" / "research indicates" without named study, (b) unsourced percentages, (c) examples from outside the book's domain. Output: a color-coded terminal table of flagged lines, plus a BEFORE/AFTER comparison of the pantry file flagged vs. corrected.
- Prompt seed: `claude "Audit this pantry file against three criteria: (1) every percentage or specific number must name a source with enough metadata to find it; (2) 'studies show' without a named study is a flag; (3) every example must come from [book domain]. Classify each flagged item: severity (HIGH/MEDIUM), reason. Output as JSON." < pantry/ch-03-domain-research.md`
- Read / check: Verify HIGH flags fire on "studies show 78%" and on a McKinsey reference without page or year; verify examples from outside the domain trigger reason "off-domain example"; verify JSON parses cleanly.
- Human supplies: A pantry file with planted failures (synthetic acceptable for the video — the failure patterns are illustrative, not dependent on real research content).
- Output medium: screen-recording mp4 — terminal running the audit, color-coded table, then the 45-minute evaluation pass on the top 3 flags.
- The change: Add a real citation (Adobe Firefly release notes, AIGA Design Census) to the top-flagged item; re-run to show flag drops from HIGH to cleared.
- Teardown angle: The pantry audit is the fluency trap check run on your own research before it poisons the draft. The habit starts here, not at the chapter level.
- Exclusions: Nine-section pantry structure lecture, Chapter Research Gatherer prompt internals, full three-LLM triangulation method.
- Score: 8/10

## Candidate 03 — "Measure Cowork Draft Quality: Log.csv Is Green But Is the Chapter Good?"
- Source: ai-1-fry/chapters/07-chapter-writing.md (LLM Exercises)
- Lane: BUILD (Claude Code)
- Hook: A log.csv of 12 green rows looks like a finished book. The second paragraph of chapter 1 contains "in today's rapidly evolving design landscape." The log was honest. The chapter is not.
- The artifact: A chapter-quality script that reads chapters/*.md and outputs a quality score per chapter based on: generic-phrase count ("rapidly evolving," "in today's world"), unsourced claim count, off-domain example count, vague bridge question detection. Rendered as an animated Manim bar chart — one bar per chapter, red for flagged count, showing the distribution of quality across the manuscript.
- Prompt seed: `claude "Read this chapter draft. Score it on four quality dimensions: (1) count phrases that would work in any field ('rapidly evolving X landscape', 'in today's world'), (2) count percentage claims without named sources, (3) count examples from outside [book domain], (4) does the bridge question name a specific next capability or is it a topic? Output as JSON: {chapter, generic_phrases: N, unsourced_claims: N, off_domain_examples: N, bridge_ok: bool}." < chapters/01-draft.md`
- Read / check: Verify that "in today's rapidly evolving design landscape" increments generic_phrases; verify the bridge question "What does this mean for the future of design?" is flagged as off; verify the Manim chart renders chapter bars in correct chapter order.
- Human supplies: A set of Cowork chapter drafts (synthetic acceptable — plant the failure patterns across a 5-chapter set). Manim installed.
- Output medium: Manim (animated) — bar chart growing left to right across chapters, with the flag-count bars growing and red markers appearing.
- The change: Show the human rewrite of chapter 1 (fix all four quality dimensions), re-run the script, and show that chapter's bar shrink to zero.
- Teardown angle: The log.csv was honest. The log measures execution — chapters drafted, tokens used, runtime. Quality is what the log cannot measure. That is the human rewrite's job.
- Exclusions: Full Chapter Writer Cowork architecture, TIKTOC.md spec internals, pandoc build pipeline.
- Score: 8/10

## Candidate 04 — "Build a Bloom's Arc Checker for a 12-Chapter Textbook"
- Source: ai-1-fry/chapters/02-what-tic-toc-does.md (LLM Exercise 3)
- Lane: BUILD (Claude Code)
- Hook: A Bloom's ceiling table that clusters two Create chapters at the end of a 12-chapter book looks intentional. If neither Create chapter has an Apply prerequisite in the chapters before it, it is a defect that ships into 50,000 words of drafting.
- The artifact: A Manim step-chart animation of a Bloom's ceiling distribution across a 12-chapter textbook, with red markers on chapters that fail three checks: (a) Create without prior Apply, (b) consecutive Evaluate chapters with no Create destination, (c) unexplained downward reversals. The gate also runs a Claude critique to name the design judgment at each flag.
- Prompt seed: `claude "Here is a Bloom's ceiling distribution: [list]. Critique this distribution for a practitioner textbook: (1) flag every Create chapter that lacks a prior Apply or Analyze chapter in the sequence, (2) flag clusters of 3+ consecutive Evaluate chapters, (3) flag downward reversals (Create → Remember). Output JSON: {flags: [{chapter, type, reason}]}."` then render Manim step chart with JSON flags.
- Read / check: Verify JSON flags a Create at position 10 when the last Apply was position 4; verify the step chart renders Bloom's level names (Remember → Create) on y-axis; verify red markers align with flagged chapter positions.
- Human supplies: A Bloom's ceiling table from a real or synthetic TIKTOC.md. Fully synthetic is acceptable. Manim installed.
- Output medium: Manim (animated) — step chart sweeping left to right, red flag markers dropping onto violation chapters.
- The change: Fix the prerequisite gap (add an Apply chapter before the flagged Create), re-render — show the flag disappear and the arc smooth out.
- Teardown angle: The Bloom's arc is a prerequisite commitment, not an aesthetic. The Create chapter assumes the Apply foundation. Without it, the chapter is asking readers to synthesize material they have never applied.
- Exclusions: Full Bloom's taxonomy revision history, Gagné conditions of learning, the complete Tic TOC /l1-l4 session.
- Score: 8/10

## Candidate 05 — "Generate and Audit Chapter 00: Domain-Specific Claude Basics"
- Source: ai-1-fry/chapters/10-enrichment-for-ai.md (LLM Exercise 1)
- Lane: BUILD (Claude Code)
- Hook: A Chapter 00 that says "Claude can help with creative tasks and answer questions" is generic documentation. A Chapter 00 that says "Claude can read a client brief and tell you what the brief is not saying, but cannot tell you whether this particular client backslides on color choices" is passing the AI+1 standard.
- The artifact: A Claude-generated Chapter 00 for a specified practitioner field, followed by a three-question AI+1 audit: (1) transplant test, (2) reader-brings-something test, (3) deliverable-is-judgment test. The audit output is a per-section PASS/FAIL table rendered in the terminal.
- Prompt seed: `claude "Generate Chapter 00 'Claude Basics for [field]' for a practitioner textbook. Four sections: capabilities paired with workflow moments, when-to-use decision table (Claude / Claude Project / Claude Code), a worked example with anonymized real artifact, five field-specific failure modes with tool and workflow context. No generic claims that would work for any field."` then `claude "Run the AI+1 three-question audit on this Chapter 00: (1) transplant test — does it break if I replace '[field]' with 'accounting'? (2) reader-brings test — does each section require something only a [field] practitioner has? (3) deliverable test — are the exercises judgment calls, not model-output reads? Output per-section PASS/FAIL table."`
- Read / check: Verify transplant test fails on generic sections; verify a domain-specific capability (e.g., "read a client brief for unstated constraints") passes all three; verify the table is clean ASCII.
- Human supplies: A specific profession for [field] substitution. The more precise, the better the output. Synthetic is acceptable if the field is specified tightly.
- Output medium: screen-recording mp4 — terminal running both prompts, PASS/FAIL table, then one targeted rewrite of a flagged section.
- The change: Show the transplant-test failure on one generic paragraph; rewrite it to bind the capability to a specific workflow moment; re-audit to show PASS.
- Teardown angle: The binding of model behavior to domain workflow is the whole AI+1 distinction. Generic documentation and domain instruction look identical until you run the transplant test.
- Exclusions: Full enrichment generator three-phase pipeline, Dig Deeper vs LLM Exercise structural distinction, AI Wayback Machine section.
- Score: 8/10

## Candidate 06 — "Three-LLM Domain Research: Map What Is Settled and What Is Contested"
- Source: ai-1-fry/chapters/03-domain-research.md (LLM Exercise 2)
- Lane: BUILD (Claude Code)
- Hook: Claude qualifies and hedges. GPT enumerates confidently without sources. Gemini retrieves specific numbers from named reports. Running the same prompt across all three reveals not three answers but a topology — the settled territory, the contested edges, and the one thing one model found that the others missed.
- The artifact: A synthesis document (600–800 words) with every claim tagged ALL-THREE-AGREE / TWO-AGREE / DIVERGENT / ONE-ONLY, rendered as an animated D3 Venn-diagram showing claim counts per overlap region.
- Prompt seed: `claude "Read these three research outputs (claude-output.md, gpt-output.md, gemini-output.md). Synthesize into 600-800 words organized by the 8 research sections. For every claim, tag: ALL-THREE-AGREE, TWO-AGREE, DIVERGENT, or ONE-ONLY. For ONE-ONLY: attribute the source model. For DIVERGENT: state all positions without resolving. Output as markdown with inline tags."` then parse tag counts into D3 Venn.
- Read / check: Verify DIVERGENT rows state all positions (not "models disagree generally"); verify ONE-ONLY items are attributed; verify the D3 Venn renders three correctly-sized overlap circles with count labels.
- Human supplies: Three real LLM outputs on the same eight-section prompt for a real profession. Cannot be faked — the divergence pattern is the artifact. A synthetic set where the patterns are planted is acceptable for a demo but should be labeled as illustrative.
- Output medium: d3 (animated) — three-circle Venn diagram with count labels animating into each overlap region.
- The change: Remove the ONE-ONLY items from the synthesis and re-render the Venn — show how the synthesis degrades when the gap-finding model's unique contributions are dropped.
- Teardown angle: The synthesis is not averaging. It is reading three biased reports with professional judgment and marking confidence honestly. The Venn is a representation of epistemic confidence, not a vote count.
- Exclusions: Full 8-section prompt walkthrough, Constitutional AI background on Claude's uncertainty-hedging, Surowiecki wisdom-of-crowds theory lecture.
- Score: 8/10

## Candidate 07 — "Validate Your Book Scaffold: Run the Three-Audience Gate"
- Source: ai-1-fry/chapters/05-book-scaffold.md (Exercises 5.1-5.3)
- Lane: BUILD (Claude Code)
- Hook: The scaffold directory has 17 files in three audience groups. A metadata.yaml full of placeholders is not a scaffold — it is a gesture toward one. The three-audience gate catches the difference in under 60 seconds.
- The artifact: A Python gate script that validates a new_book.py scaffold: (a) all 17 expected files present, (b) metadata.yaml has no "<" placeholder characters in any field, (c) the chapters/ directory has the correct number of stub files matching the TIKTOC.md chapter count, (d) the build.sh is executable. Output: PASS/FAIL per check, terminal color-coded.
- Prompt seed: `python3 -c "import os, yaml, glob; root='my-book'; files=['TIKTOC.md','book.md','vision.md','architecture.md','chapters-spec.md','risks.md','outline.md','metadata.yaml','build.sh']; missing=[f for f in files if not os.path.exists(f'{root}/{f}')]; meta=yaml.safe_load(open(f'{root}/metadata.yaml')); placeholders=[k for k,v in meta.items() if '<' in str(v or '')]; chapters=glob.glob(f'{root}/chapters/*.md'); print('missing:',missing); print('placeholders:',placeholders); print('chapters:',len(chapters))"`
- Read / check: Verify the script fires on a missing risks.md; verify it catches a title field containing "<INSERT-TITLE>"; verify chapter count matches the TIKTOC.md chapter list length.
- Human supplies: A scaffold directory from new_book.py (real or synthetic — create a minimal scaffold manually for the demo). The Python gate is fully writable within the video.
- Output medium: screen-recording mp4 — terminal running the gate on a broken scaffold, then a fixed scaffold, then the clean PASS.
- The change: Remove one chapter stub from chapters/ to simulate a TIKTOC.md chapter that wasn't scaffolded; show the gate FAIL, then re-run new_book.py and show the stub appears.
- Teardown angle: The scaffold is not the output of the script. It is the output of the Tic TOC session, made visible as files. The gate is the spec held to a deterministic standard.
- Exclusions: pandoc build pipeline, full Knuth literate programming discussion, three-audience taxonomy lecture.
- Score: 7/10

## Candidate 08 — "Run the Exercise Audit: Find the Interchangeable Pattern Across 6 Chapters"
- Source: ai-1-fry/chapters/10-enrichment-for-ai.md (LLM Exercise 2)
- Lane: BUILD (Claude Code)
- Hook: Copy all six LLM Exercises from a textbook draft into one document, strip the chapter context, and read them in sequence. Two of them could swap chapter positions without losing anything. That is the interchangeable pattern — and it is invisible chapter by chapter.
- The artifact: A Claude auditor that takes a multi-chapter exercise set and applies the three-question audit per exercise, then identifies the interchangeable pattern (exercises that could swap positions), the Claude-documentation pattern (exercises that teach prompt syntax not domain integration), and the no-deliverable pattern (exercises without a saved artifact). Output: an annotated exercise file with pattern callouts.
- Prompt seed: `claude "Here are [N] LLM Exercises from a [N]-chapter textbook, stripped of chapter context. For each exercise: (1) transplant test, (2) reader-brings test, (3) deliverable test. Then identify: (a) any two exercises that could swap chapter positions without losing meaning (interchangeable pattern), (b) any exercise that teaches Claude prompt syntax rather than domain integration (documentation pattern), (c) any exercise without a saved artifact deliverable (no-deliverable pattern). Output as annotated markdown." < exercises-all-chapters.md`
- Read / check: Verify the interchangeable pattern fires when two exercises use the same generic "ask Claude to explain X" structure; verify the documentation pattern fires on "try this prompt format and observe how Claude responds"; verify the no-deliverable pattern fires on exercises that end with "read Claude's answer."
- Human supplies: A multi-chapter exercise set (synthetic with planted patterns is fully acceptable).
- Output medium: screen-recording mp4 — terminal running the auditor, pattern callouts in the annotated output, then the hand-rewrite of the worst-scoring exercise.
- The change: Run the stress-test prompt on the rewritten exercise to confirm Claude agrees it passes all three questions; compare to the original.
- Teardown angle: The audit surfaces what is invisible chapter by chapter. Interchangeable exercises are a sign that the enrichment generator is doing generic work. The rewrite is where domain specificity has to be authored, not generated.
- Exclusions: Freire's banking model lecture, bell hooks Teaching to Transgress section, AI Wayback Machine.
- Score: 7/10
