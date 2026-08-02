# Claude Agentic AI — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Write a Plan-First Scope Statement and Approval Gate with Claude
- Source: claude-agentic-ai/chapters/07-planning-before-acting.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: "Organize the folder" costs three hours of undo — asking for the plan first costs two minutes and a corrected scope.
- The artifact: a Python script that submits a task description to Claude with an explicit plan-first instruction, receives a structured plan (goal, inputs, steps, permissions, stop conditions, verification evidence), scores it against the eight-element checklist, and prints which elements are missing — animated as a checklist filling in green/red.
- Prompt seed: `claude "Before acting, produce a full plan for this task: 'Compile quarterly financial highlights from the files in /reports/Q3/.' Plan must include: goal statement, inputs named, excluded sources, tool sequence, permissions required, stop conditions, and verification evidence. Do not begin executing until I approve."`
- Read / check: verify the plan names specific files/folders (not just "the reports"); verify stop conditions are concrete (not "if something goes wrong"); verify verification evidence is an artifact (row count, source list) not a self-report ("I'll confirm when done"); score against the ch.7 plan checklist.
- Human supplies: nothing — the worked example task from ch.7 (Q2 customer feedback summary) is fully synthetic.
- Output medium: screen-recording mp4 (terminal: plan requested, plan returned, checklist scored)
- The change: provide the plan with one deliberately vague element (e.g., stop condition = "if needed") and verify the checker flags it as insufficient, then ask Claude to revise.
- Teardown angle: a plan is the first moment the agent's interpretation of your task becomes visible — the two minutes of review before action beats the twenty minutes of undo after it.
- Exclusions: multi-agent orchestration planning, LLM planning benchmark comparisons.
- Score: 9/10

---

## Candidate 02 — Map the Agentic Loop: Observe → Plan → Act → Check → Report with Claude
- Source: claude-agentic-ai/chapters/02-the-agentic-loop.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Ask Claude to narrate its own loop on a real task — then find the stage where it silently skipped a check.
- The artifact: a structured loop trace where Claude explicitly labels each stage (Observe / Plan / Act / Check / Report) for a document-assembly task, with human annotations showing which stage produced evidence vs. which produced a self-report — animated as a five-stage pipeline with color-coded evidence vs. assertion labels.
- Prompt seed: `claude "Perform this task with explicit loop narration: summarize the three documents in [folder]. Label each step as Observe / Plan / Act / Check / Report before doing it. At the Check stage, do not self-certify — list specifically what you verified and how."`
- Read / check: verify the Check stage produces a specific artifact (source list, word count, named files) not a statement like "verified successfully"; verify the Report includes which files were processed; identify any stage where the narration says "did X" without external evidence.
- Human supplies: three short text documents (any synthetic documents work — the book's example uses quarterly reports).
- Output medium: screen-recording mp4 (terminal: loop stages labeled, human annotation overlay highlighting evidence vs. assertion)
- The change: remove the loop-narration instruction and run the same task; compare the default output to the labeled version and identify what the human would not have seen without the explicit stage labels.
- Teardown angle: the loop happens whether you ask for it or not — the value of naming it is making human intervention points visible before the agent runs to completion.
- Exclusions: ReAct vs. Reflexion framework comparison, multi-step planning benchmarks.
- Score: 9/10

---

## Candidate 03 — Audit an Agent's Action Surface Before Running a Task with Claude
- Source: claude-agentic-ai/chapters/03-tools-permissions-and-the-action-surface.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Date extraction from twelve contracts requires read + one CSV write — the action surface audit cuts everything else before the agent touches a file.
- The artifact: a Python permission audit script that takes a task description and proposed tool list, outputs a scored permission matrix (access type / read-write / reversibility / blast radius / approval required) and flags any tools not needed for the stated task — animated as the matrix filling in with red flags on over-provisioned tools.
- Prompt seed: `claude "For this task: 'Extract key dates and deliverables from twelve contracts in /contracts/ and populate tracker.csv,' generate a permission matrix: list every access type needed (chat / file-read / file-write / browser / terminal), whether each is read or write, whether each action is reversible, and the blast radius if the agent makes an error on that access type. Flag any access types that are not strictly required."`
- Read / check: verify the matrix correctly identifies CSV write as the only write access needed; verify browser is flagged as not required; verify "delete" and "email" are absent; check reversibility column against the ch.3 access ladder definitions.
- Human supplies: nothing — the ch.3 worked example (contract extraction to tracker.csv) is fully synthetic.
- Output medium: Remotion (matrix cells filling in one by one, red flags appearing on over-provisioned rows)
- The change: add a "browser access to external APIs" to the proposed tool list and verify the audit flags it as both unnecessary and high-blast-radius.
- Teardown angle: the action surface is a design decision, not a default — and the blast radius of any error scales with the surface, not the task's complexity.
- Exclusions: MCP server configuration, OWASP LLM Top 10 full walkthrough, enterprise permission management.
- Score: 9/10

---

## Candidate 04 — Evaluate an MCP Server Before Connecting It with Claude
- Source: claude-agentic-ai/chapters/06-mcp-and-external-capabilities.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Server A reads. Server B reads and writes tickets — the review checklist shows you which one to connect for a status report task and why.
- The artifact: a Python MCP server evaluation script that scores two servers on six review dimensions (maintainer known / capabilities documented / resources vs. tools ratio / reversibility of tool actions / data scope / governance controls) and outputs a connect / do-not-connect recommendation with rationale — animated as a comparison table with color-coded cells.
- Prompt seed: `claude "Evaluate two MCP servers for a 'weekly status report from open tickets' task. Server A: read-only ticket resources. Server B: ticket resources + tools to update status and post comments. For each server: what can the agent do, what is the blast radius on error, name one required approval gate, and recommend connect or do-not-connect for this task with a one-sentence rationale."`
- Read / check: verify Server B receives a conditional recommendation (connect only with explicit per-action approval gate); verify the blast radius for Server B names a specific irreversible action (ticket status change); verify Server A's rationale correctly states that read-only limits damage on error.
- Human supplies: nothing — the worked example from ch.6 (project management server opening scene) is the test case — synthetic.
- Output medium: screen-recording mp4 (terminal: two-server comparison table printed, recommendation highlighted)
- The change: add a third server (Server C: reads + sends external email) and verify the evaluation flags prompt injection risk as the highest concern.
- Teardown angle: connecting an MCP server is an approval gate — the moment of connection determines every downstream risk; the review belongs to the human before the first task runs.
- Exclusions: MCP protocol implementation details, OWASP MCP Top 10 full walkthrough, custom server development.
- Score: 9/10

---

## Candidate 05 — Run a Pre-Mortem on an Agentic Task with Claude
- Source: claude-agentic-ai/chapters/09-failure-modes-of-agentic-work.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Eight failure modes, one task — the pre-mortem identifies the three live risks before the agent sends the first email.
- The artifact: a structured pre-mortem table where Claude identifies the live failure modes for a specific task (from the ch.9 taxonomy: tool overreach, stale context, plausible summary, silent omission, prompt injection, fabricated completion, irreversible action, automation bias) and assigns a mitigation for each live risk — animated as the failure-mode taxonomy populating with live/not-live verdicts for the given task.
- Prompt seed: `claude "Run a pre-mortem on this agentic task: 'Process 30 customer emails, extract complaints, draft a response for each, and save to /drafts/.' For each of the eight failure modes [list them], mark it as live or not-live for this task, and for each live mode write one concrete prevention step."`
- Read / check: verify prompt injection is marked live (the task reads external email content); verify irreversible action is marked live (draft files saved, external system); verify fabricated completion is live (draft "completion" could occur without all emails processed); verify mitigations are concrete (not "be careful").
- Human supplies: nothing — the ch.9 worked example (customer email processing) is the task description — synthetic.
- Output medium: screen-recording mp4 (terminal: eight-row table filling in, live risks highlighted)
- The change: remove "draft to /drafts/" from the task and replace with "send responses" — verify irreversible action escalates from medium to highest risk.
- Teardown angle: the failure modes are not random — they cluster by task type; a folder-summary task has different live risks than an email-processing task; naming them before the task determines what you supervise.
- Exclusions: formal agent red-teaming, AgentDojo benchmark walkthrough, full OWASP LLM Top 10.
- Score: 9/10

---

## Candidate 06 — Build an Independent Verification Protocol for Agent Outputs with Claude
- Source: claude-agentic-ai/chapters/08-verification-is-the-control-system.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The agent says "verified" — the verification protocol shows you it matched citations against its own training data, not the actual documents.
- The artifact: a Python script that takes an agent task description, determines the output type (code / research / data / file operation), and generates a specific verification protocol with named evidence artifacts — animated as a verification matrix filling in by output type.
- Prompt seed: `claude "For this task: 'Summarize literature on treatment protocol X with source citations,' generate a verification protocol. First state the output type. Then list: (1) what independent evidence confirms completion, (2) what specific check catches the most likely failure mode, (3) what evidence artifact the agent must produce (not self-certify). Use the eight-output-type evidence matrix."`
- Read / check: verify the protocol specifies "open cited documents" not "ask agent to check"; verify the evidence artifact is a source map (file → claim mapping), not a completion statement; verify the check targets citation fabrication specifically.
- Human supplies: nothing — the ch.8 literature summary worked example is fully synthetic.
- Output medium: screen-recording mp4 (terminal: protocol generated, evidence artifacts listed, self-report vs. independent evidence distinction highlighted)
- The change: apply the same protocol generation to a code-change task and verify it correctly switches to "run tests, inspect diff" as the evidence method.
- Teardown angle: verification is not the last step — it is designed before the agent starts; the evidence artifact you specify before the task runs is what makes the task verifiable rather than merely impressive.
- Exclusions: automated verification tooling, semantic entropy measurement, second-model review systems.
- Score: 9/10

---

## Candidate 07 — Simulate Least-Privilege Permission Design for a File Agent with Claude
- Source: claude-agentic-ai/chapters/03-tools-permissions-and-the-action-surface.md
- Lane: BUILD (Claude Code)
- Hook: You need to clean a folder — but the blast radius of giving the agent your full Documents directory is everything you've ever written.
- The artifact: a Python setup script that creates a minimal "working folder" for a Cowork file task (copies only the needed files, excludes everything sensitive, names forbidden files explicitly) and prints a before/after directory comparison — animated as files moving into the working folder while forbidden files stay in place.
- Prompt seed: `claude "Write cowork_prep.py: given a source directory and a task description, (1) list all files in source, (2) classify each as needed/forbidden/uncertain, (3) copy only needed files to a new /cowork-working/ subdirectory, (4) print a before/after manifest and flag any uncertain files for human review. Use filename patterns only (no reading file contents)."`
- Read / check: verify the script copies only the files matching the task description's file types; verify sensitive patterns (contracts, passwords, .env, personal names) are flagged as forbidden; verify uncertain files are listed separately for human review, not auto-excluded or auto-included.
- Human supplies: a test directory with mixed file types (dummy filenames only — synthetic; no real content needed).
- Output medium: screen-recording mp4 (terminal: directory scan, classification table, before/after manifest printed)
- The change: run the same script on a directory containing a .env file with API keys — verify it is automatically flagged as forbidden credentials regardless of task description.
- Teardown angle: the working folder is the permission boundary; setting it before the agent starts is the difference between a narrow-scope task and handing a contractor your entire office.
- Exclusions: Cowork UI setup, connector configuration, computer-use session management.
- Score: 8/10

---

## Candidate 08 — Test Automation Bias by Running the Same Output with and Without Review with Claude
- Source: claude-agentic-ai/chapters/09-failure-modes-of-agentic-work.md
- Lane: BUILD (Claude Code)
- Hook: When a policy analyst reviews an agent's brief before forming her own opinion, she accepts a wrong summary 40% more often — the Stanford SCALE finding, reproduced in a five-minute demo.
- The artifact: a Python experiment that shows two conditions: (A) human reads the agent's summary first, then the source documents; (B) human reads source documents first, then the agent's summary — and prompts the viewer to compare their verdict in each condition — rendered as a side-by-side split screen with condition labels.
- Prompt seed: `claude "Summarize these five regulatory framework descriptions [paste five short paragraphs] into a one-page brief with one recommendation. Then in a second code block, summarize the same five paragraphs with a deliberately wrong recommendation (reverse one key finding). I will use both for a demonstration of automation bias."`
- Read / check: verify the two summaries differ by exactly one reversed finding (not more); verify the correct summary is accurate to the source paragraphs; verify the wrong summary is plausible enough that it would pass a quick read.
- Human supplies: five short regulatory framework descriptions (synthetic — the book's policy analyst example from ch.9 works).
- Output medium: screen-recording mp4 (two-condition demo: read agent-first vs. source-first, viewer asked to note which condition made the error easier to catch)
- The change: add a structured review protocol (five specific claims to check against source) and run condition A again — measure whether the protocol eliminates the bias.
- Teardown angle: automation bias worsens under time pressure and expertise trust; the mitigation is not skepticism — it is a structured review protocol that forces independent engagement with source evidence.
- Exclusions: full Stanford SCALE review, formal HCI automation bias studies, eye-tracking evidence.
- Score: 8/10

---

## Candidate 09 — Design Human Approval Gates for a Multi-Step Agentic Workflow with Claude
- Source: claude-agentic-ai/chapters/07-planning-before-acting.md
- Lane: BUILD (Claude Code)
- Hook: Three gates in the right places prevent the four-hour undo — one gate in the wrong place and the agent has already written to production.
- The artifact: a Python gate-design tool that takes a workflow description (steps, tools, reversibility per step) and outputs a gate placement recommendation with rationale for each proposed gate — animated as a workflow pipeline with gate markers appearing at the recommended points.
- Prompt seed: `claude "Design approval gates for this workflow: (1) read contracts from /contracts/, (2) extract key dates, (3) populate tracker.csv, (4) email summary to finance team. For each step: is it reversible? What is the blast radius on error? Should a gate appear before or after? Output a gate-placement table with one-sentence rationale per gate."`
- Read / check: verify step 4 (email) has a mandatory pre-action gate; verify step 3 (write to CSV) has at least a light gate; verify the gate placement table correctly distinguishes pre-action (stop before) from post-action (verify after); check that gates scale with blast radius.
- Human supplies: nothing — the ch.7 contract extraction example is the test workflow — synthetic.
- Output medium: Remotion (workflow pipeline animated, gates appearing as barriers between steps)
- The change: add a step 5 (delete processed contracts from /contracts/) and verify it receives the highest-tier gate regardless of workflow position.
- Teardown angle: gate placement is a design decision made before the workflow runs — and the cheapest gate is the one before the irreversible action, not the one after it.
- Exclusions: formal human-in-the-loop system design, NIST AI RMF full implementation, enterprise approval workflows.
- Score: 8/10

---

## Candidate 10 — Compare Self-Check vs. Independent Verification on an Agent Output with Claude
- Source: claude-agentic-ai/chapters/08-verification-is-the-control-system.md
- Lane: BUILD (Claude Code)
- Hook: "Claude, check your own answer" finds two of six errors. Opening the cited papers finds five.
- The artifact: a side-by-side comparison of self-check results vs. human-source verification results on the same literature summary, with a table showing which errors each method caught — animated as an error grid filling in with checkmarks per method.
- Prompt seed: `claude "Produce a five-claim summary of this research topic [paste topic], citing one source per claim. Then, in a second pass, self-check each claim: is it supported by the source you cited? Rate each claim as verified/uncertain/unsupported." [Human then independently checks the same five claims against the actual sources.]`
- Read / check: verify the self-check misses at least two errors (expected from the ch.8 argument that self-check shares failure modes with production); verify the human check against actual sources finds additional errors; produce a comparison table: self-check caught / human check caught / both / neither.
- Human supplies: five short paragraphs from real or synthetic sources (any research domain works; synthetic is acceptable for the demo).
- Output medium: screen-recording mp4 (terminal: self-check results, then human verification results, then comparison table)
- The change: replace one self-checked claim with a deliberately wrong citation and verify the self-check rates it "verified" while the human check flags it as unsupported.
- Teardown angle: self-check improves output at the margins but cannot catch systematic errors — independent verification is not optional for consequential outputs; it is what makes "verified" mean something.
- Exclusions: second-model review architecture, automated fact-checking APIs, retrieval-augmented verification.
- Score: 8/10

