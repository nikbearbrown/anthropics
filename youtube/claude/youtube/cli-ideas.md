# Claude — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Route Any Task to the Right Claude Surface with Claude
- Source: claude/chapters/01-the-work-chooses-the-tool.md
- Lane: BUILD (Claude Code)
- Hook: Five questions, thirty seconds, and you never open the wrong Claude window again — the routing table is runnable code.
- The artifact: a Python CLI tool that takes a task description as input, runs it through the five routing dimensions (output type, context source, risk, reversibility, verification path), and outputs a surface recommendation (Claude AI / Claude Code / Claude Cowork / Human-only) with one-sentence rationale — rendered as an animated decision tree lighting up the chosen branch.
- Prompt seed: `claude "Build a Python CLI routing_advisor.py that takes a task description as stdin and evaluates five dimensions: output_type (text/code/file), context_source (conversation/repo/filesystem), risk_level (low/medium/high), reversibility (reversible/irreversible), verification_path (domain-check/tests/manual). Print the recommended surface and the determining factor."`
- Read / check: verify the routing logic correctly identifies code tasks → Claude Code, file-assembly tasks → Cowork, and sensitive decisions → human-only; test with at least three worked examples from ch.1's routing table; check that the output matches the book's five-dimension framework.
- Human supplies: nothing — fully synthetic; the five example tasks from ch.1 are the test cases.
- Output medium: screen-recording mp4 (terminal running three task descriptions through the tool, routing decisions appearing)
- The change: add a "risk override" flag — any task with irreversible + high-risk routes to human-only regardless of other dimensions — and verify it triggers correctly.
- Teardown angle: routing by habit (everything to chat) is the most common Claude failure mode; the five-question filter takes under a minute and prevents hours of underpowered or dangerous delegation.
- Exclusions: full automation bias literature, surface feature comparison across Claude versions.
- Score: 9/10

---

## Candidate 02 — Build a Six-Component Specification Prompt Generator with Claude
- Source: claude/chapters/03-prompting-as-specification.md (Try This exercises)
- Lane: BUILD (Claude Code)
- Hook: Every vague Claude prompt has six missing components — a two-minute specification rewrite turns three wrong drafts into one right artifact.
- The artifact: a Python CLI that takes a weak prompt and a domain description, then outputs a fully specified six-component prompt (task, context, source material, constraints, output format, evaluation criteria) — with a before/after comparison showing word count and component density.
- Prompt seed: `claude "Write prompt_spec.py: takes a weak prompt string and a domain description as arguments, outputs a six-component specification: (1) task (one sentence), (2) context (who/what/why), (3) source material (what Claude should use), (4) constraints (what it must not do), (5) output format (exact structure), (6) evaluation criteria (how to judge success). Include a before/after word-count table."`
- Read / check: verify all six components appear in the output; check that constraints are negative (what not to do) and distinct from the task; verify evaluation criteria are measurable, not vague ("good" is not acceptable); test on the book's grant-report example from ch.3.
- Human supplies: nothing — the book's grant report / literature review examples are fully usable synthetic test cases.
- Output medium: screen-recording mp4 (terminal: weak prompt in → six-component spec out → before/after table)
- The change: add a "diagnosis mode" that takes an existing Claude output and a specification, then identifies which of the six components was violated — rendering the diagnosis as a checklist.
- Teardown angle: prompting as specification is not about longer prompts — it is about making the evaluation criteria legible before the artifact is produced; the criteria you cannot write are the ones you cannot supervise.
- Exclusions: XML prompt structures for Claude's API, system-prompt engineering for production deployments.
- Score: 9/10

---

## Candidate 03 — Run the Engineering Partner Loop with Claude Code
- Source: claude/chapters/04-claude-code-as-engineering-partner.md
- Lane: BUILD (Claude Code)
- Hook: The verification oracle runs first — then Claude fixes the code — then the oracle runs again. This is the diff you can trust.
- The artifact: a screen-recording of a six-step engineering partner loop: define the oracle (failing test), scope the task, approve Claude's plan, inspect the diff, run the oracle, decide — using a real small bug and Claude Code's diff output — rendered as a split-screen terminal session.
- Prompt seed: `claude "We have a failing test in test_auth.py: test_empty_password_rejected. Follow the engineering partner loop: (1) confirm which file to edit, (2) propose a plan before touching any code, (3) after I approve, make the minimal edit, (4) run the test suite and report exit code, (5) show me the diff. Do not touch any file outside auth/."`
- Read / check: verify Claude shows a plan before editing; verify the diff is minimal (only the failing function touched); verify the oracle (test) passes after the edit; verify no files outside auth/ were modified.
- Human supplies: a small codebase with one known failing test (a 20-line example from the book's worked walkthrough is sufficient — synthetic).
- Output medium: screen-recording mp4 (split terminal: left = Claude output, right = test runner output)
- The change: introduce a second failing test that requires a different fix; verify Claude's plan correctly identifies both and does not over-fix.
- Teardown angle: the oracle is the control system — without it, "Claude fixed the bug" is unverifiable; with it, the human's job is approving scope, not debugging code.
- Exclusions: full CI/CD pipeline integration, automated code review, multi-file refactors.
- Score: 9/10

---

## Candidate 04 — Build the AI-Use Log Habit with Claude
- Source: claude/chapters/07-research-writing-and-analysis-workflows.md
- Lane: BUILD (Claude Code)
- Hook: A six-column log turns "Claude helped" into auditable evidence — and takes forty seconds to fill in.
- The artifact: a Python script that appends a timestamped entry to an AI-use log CSV (columns: date, tool, purpose, input_type, output_used, human_verification) and prints a summary table of the current session's entries — animated as rows appearing in a running log.
- Prompt seed: `claude "Write ai_log.py: a CLI that takes six arguments (tool, purpose, input_type, output_used, human_verification) and appends a dated row to ai_use_log.csv in the current directory. Also add a --report flag that prints the last 10 entries as a formatted markdown table."`
- Read / check: verify the CSV appends correctly without overwriting; verify the timestamp uses ISO 8601; verify the --report flag prints valid markdown; test with three realistic entries from a research workflow.
- Human supplies: nothing — fully synthetic; the book's literature review workflow provides realistic test entries.
- Output medium: screen-recording mp4 (terminal: three log entries appended, --report summary printed)
- The change: add a --summary flag that groups entries by tool and counts total uses — rendering a frequency bar chart using matplotlib or Manim.
- Teardown angle: disclosure norms are evolving but the verification column is the constant — it is the difference between AI-assisted and AI-produced, and no log omits it.
- Exclusions: institutional policy compliance, full systematic review audit trails.
- Score: 8/10

---

## Candidate 05 — Design and Audit a Claude Cowork Task Packet with Claude
- Source: claude/chapters/05-claude-cowork-as-file-and-workflow-agent.md
- Lane: BUILD (Claude Code)
- Hook: One wrong folder permission and a Cowork session reads three years of personnel files — the task packet audit catches it in sixty seconds.
- The artifact: a Python validator that reads a Cowork task packet (plain text: inputs, access level, forbidden actions, output spec, verification checks) and scores it on six dimensions (inputs named, forbidden actions explicit, irreversible actions gated, output format specified, verification steps listed, sensitive data excluded) — animated as a checklist filling in with pass/fail per dimension.
- Prompt seed: `claude "Write task_packet_audit.py: reads a Cowork task packet from stdin as plain text, then scores it on six dimensions with pass/fail and a one-sentence explanation for each fail. Dimensions: inputs_named, forbidden_explicit, irreversibles_gated, output_format, verification_steps, no_sensitive_data."`
- Read / check: verify the validator correctly fails the opening-scene example from ch.5 (full Documents folder, no forbidden actions listed); verify it passes the correctly specified status-report example; check that sensitive data detection flags at least PII patterns and credential keywords.
- Human supplies: nothing — the book's two worked examples (bad task packet and good task packet) are the test cases — synthetic.
- Output medium: screen-recording mp4 (terminal: bad packet → six fails; good packet → six passes)
- The change: add a seventh dimension — "stop conditions defined" — and verify it catches the book's opening-scene failure mode.
- Teardown angle: the task packet is not bureaucracy — it is the specification that makes supervision possible; without it, you have handed a capable agent a vague mandate and broad permissions.
- Exclusions: Cowork connector configuration, MCP server setup, computer-use sessions.
- Score: 8/10

---

## Candidate 06 — Build a Risk-Tiered Verification Checklist with Claude
- Source: claude/chapters/06-the-human-gate.md
- Lane: BUILD (Claude Code)
- Hook: Reading Claude's output is not reviewing it — the verification matrix turns "looks right" into a checkable protocol.
- The artifact: a Python CLI that takes an output type (summary / citation / number / chart / code / recommendation) and a risk level (low / medium / high), then prints a tailored verification checklist — animated as checklist items appearing under each output type category.
- Prompt seed: `claude "Build verification_gate.py: takes --output-type and --risk-level as arguments, prints a verification checklist from the ch.6 matrix. Output types: summary, citation, number, chart, code, recommendation. Risk levels: light (skim), moderate (spot-check), strict (full audit). Print 3-5 concrete checkable steps for each combination."`
- Read / check: verify the citation output type always includes "open the source" as a step; verify strict risk always includes "independent recalculation" for numbers; verify the chart output type includes axis-label and denominator checks; test all six output types.
- Human supplies: nothing — fully synthetic; the verification matrix from ch.6 is the source of truth.
- Output medium: screen-recording mp4 (terminal: three different output/risk combinations run, checklists printed)
- The change: add a --log flag that exports the completed checklist with timestamps as a markdown file for audit purposes.
- Teardown angle: the human gate is not distrust — it is the design of your supervisory role; the checklist makes that role automatic rather than effortful.
- Exclusions: automated hallucination detection tools, semantic entropy measurement, citation grounding services.
- Score: 8/10

---

## Candidate 07 — Build a Privacy Classification Scanner for Cowork Folders with Claude
- Source: claude/chapters/08-privacy-permissions-and-sensitive-work.md
- Lane: BUILD (Claude Code)
- Hook: You think your working folder is safe — the scanner finds patient identifiers in three files you forgot to redact.
- The artifact: a Python script that scans a directory listing file names and extensions, classifying each into the book's sensitivity taxonomy (Public / Internal / Confidential / Personal / Regulated / Credentials) and printing a summary table with counts — animated as a folder tree being scanned with color-coded verdicts.
- Prompt seed: `claude "Write privacy_scanner.py: takes a directory path, lists all files, and classifies each by the sensitivity taxonomy: Public (no PII, no credentials), Internal (draft/memo/notes), Confidential (contract/nda/client), Personal (names/emails/SSN patterns), Regulated (HIPAA/FERPA keywords), Credentials (password/api_key/token patterns). Print a grouped summary table."`
- Read / check: verify the regex patterns for each category produce no false negatives on the book's scenario examples (tax records → Regulated, client contracts → Confidential, API keys → Credentials); verify the tool does not read file contents for Personal/Regulated classification (filename + extension only for privacy).
- Human supplies: a test directory with dummy files (filename-only, no real PII needed — synthetic filenames match patterns).
- Output medium: screen-recording mp4 (terminal: scan runs, color-coded table prints showing category distribution)
- The change: add a --cowork-ready flag that outputs only the files safe for a Cowork session and a --working-folder flag that copies them to a new directory.
- Teardown angle: "I can access this file" and "I should give Claude access to this file" are different questions — the scanner makes the difference visible before the session begins.
- Exclusions: content-level PII scanning (just filenames), GDPR compliance workflows, enterprise DLP integration.
- Score: 8/10

---

## Candidate 08 — Design a Personal Workflow Canvas with Claude
- Source: claude/chapters/09-building-a-personal-claude-workflow.md
- Lane: BUILD (Claude Code)
- Hook: Fifteen tasks, four buckets, two surprises — the workflow canvas reveals which Claude surface you should have been using all along.
- The artifact: a Python CLI that walks through the Personal Workflow Canvas (10 fields: workstream, surface, allowed inputs, forbidden inputs, output artifact, constraints, human gate, memory scope, failure signal, improvement note) and generates a markdown workflow document — animated as fields filling in one by one.
- Prompt seed: `claude "Write workflow_canvas.py: an interactive CLI that prompts for 10 fields of the Personal Workflow Canvas, validates that 'forbidden inputs' and 'human gate' are non-empty, and writes a formatted markdown file workflow-[name].md. Refuse to save if human_gate is blank."`
- Read / check: verify the tool correctly refuses to save when human_gate is empty; verify the output markdown matches the canvas template from ch.9; test with one realistic workflow (e.g., weekly status report using Cowork).
- Human supplies: nothing — the user fills in their own workflow during the video demo; the book's client-briefing example serves as the worked demonstration.
- Output medium: screen-recording mp4 (terminal: interactive prompts, markdown file generated and displayed)
- The change: add a --retrospective flag that loads an existing workflow file and prompts for improvement notes after three runs.
- Teardown angle: building a system around Claude is not about more automation — it is about making your delegation decisions repeatable and auditable; the canvas forces both.
- Exclusions: Claude Projects setup UI walkthrough, memory management settings, enterprise account configuration.
- Score: 7/10

---

## Candidate 09 — Audit a Completed AI Task for Process Evidence with Claude
- Source: claude/chapters/10-capstone-one-project-three-claude-surfaces.md
- Lane: BUILD (Claude Code)
- Hook: A polished briefing note is not evidence of a trustworthy workflow — the process audit reveals what was actually checked.
- The artifact: a Python CLI that reads a completed AI-use log CSV and scores the session on four process dimensions (task routing documented / gate checks performed / errors corrected / verification evidence present) — with a bar chart showing the session's process score vs. the "trusted output" threshold.
- Prompt seed: `claude "Write process_audit.py: reads ai_use_log.csv, scores each session entry on four dimensions (task_routed, gate_check, error_corrected, verification_evidence) by checking for non-empty values in those columns, prints a per-session summary table and an overall process score out of 4. Add a Manim or matplotlib bar chart comparing session score to the threshold of 3/4 required for 'shareable output'."`
- Read / check: verify the scoring correctly gives 0 for blank verification_evidence; verify the threshold logic flags sessions scoring < 3/4 as "not ready to share"; test on the worked example log from Candidate 04.
- Human supplies: a filled ai_use_log.csv from a real or synthetic session (the book's briefing note example is the test case).
- Output medium: Manim (bar chart with session scores, horizontal threshold line, color-coded bars)
- The change: add a --recommend flag that outputs one concrete improvement for the lowest-scoring dimension.
- Teardown angle: assessments in the age of generative AI should evaluate process evidence — the audit makes the human's supervisory role the deliverable, not the AI's artifact.
- Exclusions: institutional AI policy compliance, formal audit trail systems.
- Score: 7/10

