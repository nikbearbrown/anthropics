# Claude Code for Teachers — Claude Explainer Candidates

## C01 — Skill File Anatomy: Build Once, Invoke Every Semester

- **slug:** skill-build-once
- **source:** chapters/07-skills.md §What a Skill is / §Writing your first skill
- **premise:** Teachers re-specify the same 280-word grading workflow every two weeks; a SKILL.md file stores it once, and `/grading-workflow` runs it in 90 seconds instead of 18 minutes — the file format is the whole story.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `/lesson-plan-generator`
  - topic: `SKILL FILE · CAPS`   · segment: `Build Once`
  - greeting: `Merhaba`, Bear — Wagwan check: sum(ord(c) for c in "skill-build-once") % 10 == 2 → Merhaba, Bear
- **spine:** B00 ASK (/lesson-plan-generator invocation) → B01 Claude reads SKILL.md, asks for objectives + grade level → B02 lesson plan produced and saved to lesson-plans/ → B03 SKILL.md anatomy (frontmatter + workflow + Never + Verification) → B04 disable-model-invocation flag decision → VERDICT: specification amortized across every semester → Skill outro
- **callouts (≤6):**
  - [B01] "SKILL.md loads on invocation" · Not at session start · Context cost: 0 until called · Workflow + Never rules inside · points at: SKILL.md file in .claude/skills/
  - [B02] "90 seconds vs. 18 minutes" · Same workflow · First build: 45–90 min · Every invocation after: 90 sec · points at: timer comparison
  - [B03] "Never section" · Advisory (Claude tries) · Not deterministic · Hook needed for must-hold rules · points at: Never block in SKILL.md
  - [B04] "disable-model-invocation" · true = explicit /name only · false = Claude auto-invokes · Side-effect skills: always true · points at: frontmatter flag
- **register notes:** Teardown judgment — land on Babbage's subroutine insight: the unit of work is the named reusable procedure, not the per-session command. Don't oversell "always works perfectly" — first invocation always needs refinement; factor that in.
- **est length:** 72s

---

## C02 — Hook vs. CLAUDE.md: "Do Not" Becomes "Cannot"

- **slug:** hook-advisory-vs-deterministic
- **source:** chapters/08-hooks.md §Opening / §What a Hook is / §The "ask Claude to write the hook" pattern
- **premise:** CLAUDE.md said "NEVER generate a final grade" in capital letters — two sessions later Claude wrote "Overall performance: B+" anyway; a PreToolUse hook running a bash script makes that grade physically impossible to write to disk.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `summarize this student's performance`
  - topic: `HOOK ENFORCEMENT · CAPS`   · segment: `Cannot, Not Do Not`
- **spine:** B00 ASK (summary prompt) → B01 Claude returns "Overall performance: B+" despite NEVER rule → B02 why CLAUDE.md is probabilistic, not deterministic → B03 hook anatomy (PreToolUse, stdin JSON, exit code) → B04 "ask Claude to write the hook" pattern → B05 test: ask for grade explicitly, hook fires → VERDICT: advisory vs. deterministic — Hook outro
  - greeting: `Shalom`, Bear — Wagwan check: sum(ord(c) for c in "hook-advisory-vs-deterministic") % 10 == 8 → Shalom, Bear
- **callouts (≤6):**
  - [B01] "NEVER ignored" · Claude weighted it · Prompt's pull won · Probabilistic, not absolute · points at: Claude output with B+ grade
  - [B02] "Same model, different layer" · CLAUDE.md: Claude reads & tries · Hook: script runs regardless · points at: advisory vs. deterministic table
  - [B03] "exit 1 = blocked" · Script reads stdin JSON · grep for grade pattern · non-zero = Write blocked · points at: block-grades.sh
  - [B04] "Ask Claude to write it" · Claude authors the script · Teacher reviews (10-15 min) · Commits if it works · points at: ask-Claude prompt
- **register notes:** Teardown judgment — Shannon gate analogy from the chapter is excellent: high-level decisions probabilistic; inviolable constraints enforced by the physical layer underneath. Name what hooks can't enforce (conversational output, implicit grade-like statements).
- **est length:** 75s

---

## C03 — Plan Mode: The Interruption That Saves the Build

- **slug:** plan-mode-interruption
- **source:** chapters/02-first-terminal-session.md §Plan mode: the demonstration
- **premise:** Claude Code reads files, edits files, runs commands, and loops autonomously before reporting back — Shift+Tab twice freezes all writes and lets the teacher edit the plan before a single byte changes on disk.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `I want to add a Contact page to this site`
  - topic: `PLAN MODE · CAPS`   · segment: `Freeze Before Execute`
  - greeting: `Salaam`, Bear — Wagwan check: sum(ord(c) for c in "plan-mode-interruption") % 10 == 9 → Salaam, Bear
- **spine:** B00 ASK (add Contact page) → B01 agentic loop: gather → act → verify → loops before reporting → B02 Shift+Tab ×2: plan mode on → B03 plan appears (assumptions visible) → B04 Ctrl+G edit: teacher changes one thing → B05 approve → loop executes edited plan → VERDICT: edit the plan, own the build → Plan Mode outro
- **callouts (≤6):**
  - [B01] "Agentic loop" · Gather context · Take action · Verify result · Loops autonomously · points at: loop diagram
  - [B02] "Shift+Tab ×2" · Read-only mode · Cannot edit, run, or change · Until you approve · points at: plan mode indicator
  - [B03] "Assumptions visible" · Where page lives · What it links to · Which styles it inherits · points at: Claude's proposed plan
  - [B04] "Ctrl+G edit" · Opens plan in editor · Teacher changes one step · Saves, returns · points at: diff between proposed and approved plan
- **register notes:** Teardown judgment — the chapter's framing is correct: "the act of editing forces you to think about what you actually want." Don't let it become a tutorial on keybindings — the insight is cognitive, not mechanical. Name the three interruption points (Esc, plan mode, handoff conditions) as a system.
- **est length:** 68s

---

## C04 — Agentic Loop vs. Chatbot: Why the First Session Is Calibration

- **slug:** agentic-loop-not-chatgpt
- **source:** chapters/02-first-terminal-session.md §What the agentic loop is / §Questions before code
- **premise:** Claude.ai is turn-based — you read and reject bad output before it acts; Claude Code loops through gather-act-verify autonomously, so wrong actions accumulate on disk before you see an explanation — the five-question first session is the protection.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `What is the file structure of this project? List directories and tell me what each is for.`
  - topic: `AGENTIC LOOP · CAPS`   · segment: `Not ChatGPT`
  - greeting: `Jambo`, Bear — Wagwan check: sum(ord(c) for c in "agentic-loop-not-chatgpt") % 10 == 2 → Jambo, Bear
- **spine:** B00 ASK (question 1 of 5) → B01 chatbot: produce text → you reject → no harm → B02 agentic: gather → act → verify → consequences accumulate → B03 /init: Claude's first reading in CLAUDE.md form → B04 five questions, no changes: calibration → B05 wrong assumption surfaced (CSS approach) → VERDICT: calibration first, build second → Agentic Loop outro
- **callouts (≤6):**
  - [B01] "Chatbot vs. agent" · Chat: text output, you reject · Agent: file edits run before you read · points at: split comparison
  - [B02] "Consequences accumulate" · Modified files · Executed commands · Changed state · points at: file system diff
  - [B03] "/init" · Claude reads project · Generates starter CLAUDE.md · First reading, not finish · points at: /init command
  - [B05] "Wrong assumption surfaced" · CSS approach mismatch · Would have caused first build error · Surfaced in 10 min · points at: Claude's calibration answer
- **register notes:** Teardown judgment — Kay's Dynabook framing from the chapter's Wayback Machine is the right register: the five questions are the medium being used as it was intended. Don't over-dramatize "consequences accumulate" — name the Esc interrupt as the safety valve.
- **est length:** 70s

---

## C05 — Writer/Reviewer Pattern: Same Model, Clean Context

- **slug:** writer-reviewer-pattern
- **source:** chapters/10-subagents.md §Pattern 3: review subagent (the Writer/Reviewer pattern)
- **premise:** The session that wrote the grading tool contains all the writer's reasoning — a reviewer subagent spawned with a clean context window has never seen the decisions and applies fresh judgment, catching bugs the writer-session validates away.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Use the reviewer subagent to review grading-tool code from clean context`
  - topic: `WRITER/REVIEWER · CAPS`   · segment: `Clean Context Review`
  - greeting: `Habari`, Bear — Wagwan check: sum(ord(c) for c in "writer-reviewer-pattern") % 10 == 8 → Habari, Bear
- **spine:** B00 ASK (spawn reviewer subagent) → B01 main session: wrote the code + all the reasoning → B02 same-context review validates the reasoning → B03 reviewer subagent: fresh window, no history → B04 reviewer finds bug writer-session validated → B05 writer responds, fixes → VERDICT: context difference is the independent check → Writer/Reviewer outro
- **callouts (≤6):**
  - [B01] "Writer-session bias" · Context contains rationale · Same-context review agrees with it · Independence is gone · points at: context window diagram
  - [B02] "Subagent" · Own context window · Own system prompt · Returns summary only · points at: .claude/agents/reviewer.md
  - [B03] "Reviewer definition" · tools: Read, Grep only · No Write, no Edit · Narrower = safer · points at: subagent frontmatter
  - [B04] "Context ≠ model" · Underlying model: same · Context: clean · Fresh judgment fires · points at: reviewer finding bug
- **register notes:** Teardown judgment — Simon's nearly-decomposable-systems insight is the structural argument: boundary between inside and outside is what makes complex systems thinkable. Don't oversell as "always finds bugs" — name the use case clearly: high-stakes code, grading tool, simulation launcher.
- **est length:** 72s

---

## C06 — /context Check: Reading Your Window Before It Fills

- **slug:** slash-context-window-check
- **source:** chapters/10-subagents.md §Opening / chapters/02-first-terminal-session.md §The context window: your primary resource
- **premise:** A teacher's grading session hit 78% context from reading policy docs — the build itself had used 30%; a subagent would have kept the main session clean by reading 25 submissions in its own isolated window and returning only a three-section report.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `/context`
  - topic: `CONTEXT WINDOW · CAPS`   · segment: `Read Before Full`
  - greeting: `Namaste`, Bear — Wagwan check: sum(ord(c) for c in "slash-context-window-check") % 10 == 1 → Namaste, Bear
- **spine:** B00 ASK (/context) → B01 78% used: conversation history 48%, build 30% → B02 why quality degrades as window fills → B03 three tools: /context, /clear, /compact → B04 subagent alternative: read docs in own window, return summary → VERDICT: treat window like a kitchen counter — /context outro
- **callouts (≤6):**
  - [B01] "78% from research" · Policy doc + LMS export · Meeting notes + revisions · 48% from one investigation · points at: /context output bar
  - [B02] "Degradation" · Claude references dropped constraints · Repeats work · Quality drops monotonically · points at: degradation curve
  - [B03] "Three tools" · /context: see what fills · /clear: wipe between tasks · /compact: shrink + keep gist · points at: command list
  - [B04] "Subagent: main session sees 3 paragraphs" · Not the policy docs · Not 25 submissions · Only the summary · points at: subagent isolation diagram
- **register notes:** Teardown judgment — the kitchen counter metaphor is the right frame; keep it concrete. The subagent callout is a preview/bridge, not the full topic — name it as "the tool that solves this structurally" without full treatment.
- **est length:** 65s

---

## C07 — Spec Writing IS CS Education: What Changes When AI Does the Coding

- **slug:** spec-writing-is-cs-ed
- **source:** chapters/15-teaching-the-discipline.md §Specification writing IS CS education
- **premise:** Geoffrey Challen's 2026 claim — "the challenge is no longer turning specs into code; AI does that; the challenge is getting ideas out of students' brains and into specifications" — restructures what CS class should assess.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Rewrite this vague prompt as a five-element specification`
  - topic: `SPEC IS CS ED · CAPS`   · segment: `What Changes`
  - greeting: `Annyeong`, Bear — Wagwan check: sum(ord(c) for c in "spec-writing-is-cs-ed") % 10 == 4 → Annyeong, Bear
- **spine:** B00 ASK (rewrite prompt → spec) → B01 Challen quote: "spec writing IS CS education" → B02 what the spec exercise requires (PF + IJ, not just syntax) → B03 build-log rubric: five dimensions, none require looking at code → B04 peer-review model: specs reviewed before code runs → VERDICT: grade the discipline, not the output → Spec IS CS Ed outro
- **callouts (≤6):**
  - [B01] "Challen 2026" · "Turning specs into code: AI does that" · "Getting ideas into specs: humans" · points at: quote on screen
  - [B02] "Five-element spec" · Operation / Invariants · Context / Output format · Negative constraint · points at: spec template
  - [B03] "Build-log rubric" · 5 dimensions, 0–4 · Spec quality · Handoff conditions · Capacity labeling · points at: rubric table
  - [B04] "Grade the log, not the code" · Code generatable in one prompt · Build log requires lived process · points at: build log excerpt
- **register notes:** Teardown judgment — Shulman's PCK framing (teacher's lived practice = the irreplaceable pedagogical content) is the deeper claim; surface it briefly. Don't let it become a policy lecture — land on the concrete classroom move: spec review before any code runs.
- **est length:** 73s

---

## C08 — Five Questions Before Code: The Calibration Session

- **slug:** five-questions-before-code
- **source:** chapters/02-first-terminal-session.md §Questions before code: five questions, no changes
- **premise:** The teacher opened Claude Code, saw Claude had read all the files and was ready to build — the discipline is to ask five questions first, read the assumptions Claude makes, and find the one wrong assumption that would have broken the first build prompt.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `What is the one thing about this project that, if I don't tell you, you'd probably get wrong on the first build?`
  - topic: `CALIBRATION · CAPS`   · segment: `Five Questions`
  - greeting: `Sawadee`, Bear — Wagwan check: sum(ord(c) for c in "five-questions-before-code") % 10 == 2 → Sawadee, Bear
- **spine:** B00 ASK (question 5 of 5) → B01 Claude names a wrong assumption (CSS approach) → B02 why "Claude looks ready to build" is the dangerous moment → B03 five questions in order → B04 calibration: what Claude can see vs. what lives in your head → VERDICT: 10-minute calibration, hours saved downstream → Five Questions outro
- **callouts (≤6):**
  - [B01] "Wrong CSS assumption" · Claude assumed inline styles · Project uses external stylesheet · Would have broken first build → points at: Claude's calibration answer
  - [B02] "Dangerous moment" · Claude has read everything · Looks ready · This is when to slow down · points at: terminal with Claude ready
  - [B03] "Five questions" · File structure · Styling approach · What would you change? · Inconsistencies? · What would go wrong? · points at: question list
  - [B04] "Two things Claude can't see" · Your intent (in your head) · Your project's local exceptions · Spec bridges the gap · points at: split diagram
- **register notes:** Teardown judgment — Kay's Dynabook frame is right: the five questions are the medium being used as intended, not the fastest path to execution. Name the economics explicitly: "10 minutes of questions, not guessing for 2 hours."
- **est length:** 65s
