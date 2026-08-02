# Claude — Claude Explainer Candidates

## C01 — The Five-Question Surface Router

- **slug:** surface-router
- **source:** chapters/01-the-work-chooses-the-tool.md §The Five Routing Dimensions
- **premise:** Most users pick the Claude surface closest at hand — but five sixty-second questions determine the right surface before you type a single word.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Which Claude surface should I use to assemble a grant report from 12 PDFs in a folder?`
  - topic: `SURFACE ROUTING · CAPS`   · segment: `Five-Question Sprint`
  - greeting: `Hola`, Bear — Wagwan check: sum(ord(c) for c in "surface-router") % 10 == 3 → Hola, Bear
- **spine:** B00 ASK → B01 output type determines surface → B02 context location locks it in → B03 risk + reversibility add gates → B04 no verification path = no delegation → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Output type first" · Text→Chat / Code→Code / File→Cowork / Decision→Human · points at: routing table
  - [B02] "Context location" · Files on disk → Cowork not Chat · Repo → Code · Head/clipboard → Chat · points at: routing diagram branch
  - [B03] "Risk ≠ difficulty" · Low complexity can be high privacy risk · Assess before you open a window · points at: healthcare case-notes callout
  - [B04] "Verification path" · Can't describe how you'd check it? · Don't delegate it · points at: the one rule text
  - [B05] "Reversibility gap" · Draft is reversible; sent email is not · Downstream consequence counts · points at: reversibility dimension
- **register notes:** The five-question sprint is the whole lesson — land it as a checklist you can run in one minute. Don't oversell as a guarantee; sell it as "what to ask before you touch the keyboard."
- **est length:** 85s

---

## C02 — The Six-Component Prompt

- **slug:** six-component-prompt
- **source:** chapters/03-prompting-as-specification.md §The Six Components of a Well-Specified Prompt
- **premise:** "Improve this intro" is a wish, not a work order — the six-component table turns any vague ask into an inspectable specification.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Evaluate the methods section below before rewriting anything. [paste]`
  - topic: `PROMPTING AS SPEC · CAPS`   · segment: `Six-Component Work Order`
  - greeting: `Olá`, Bear — Wagwan check: sum(ord(c) for c in "six-component-prompt") % 10 == 3 → Olá, Bear
- **spine:** B00 ASK → B01 wish vs. work order → B02 the six components → B03 most-missed: source, constraints, criteria → B04 XML tags: when and why → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Wish vs. spec" · "Improve this" = vague frame · Claude fills gaps with best guess · points at: before/after prompt pair
  - [B02] "The six boxes" · Task / Context / Source / Constraints / Output / Criteria · points at: component table
  - [B03] "Most skipped" · Source material + constraints + criteria · Omit them → Claude invents norms · points at: highlighted table rows
  - [B04] "Diagnosis first" · Ask for diagnosis before rewrite · Inspect the plan, not the artifact · points at: XML example prompt
  - [B05] "XML = clarity" · Use when 3+ components · Tags separate source from instructions · Not magic — clarity only · points at: XML vs prose note
- **register notes:** The core correction is "diagnosis before artifact" — land that one behavior change. Don't make it about memorizing a template.
- **est length:** 80s

---

## C03 — The Cowork Access Ladder

- **slug:** cowork-access-ladder
- **source:** chapters/05-claude-cowork-as-file-and-workflow-agent.md §The Access Ladder
- **premise:** Every rung of Cowork's access ladder brings more capability and more risk — the discipline is standing on the lowest rung that completes the task.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Read the 12 meeting notes in /weekly-notes and tracker.csv, extract completed items, gaps, and open action items, save as status-report-[date].md. Do not access other folders.`
  - topic: `COWORK ACCESS · CAPS`   · segment: `Lowest-Rung Rule`
  - greeting: `Bonjour`, Bear — Wagwan check: sum(ord(c) for c in "cowork-access-ladder") % 10 == 7 → Bonjour, Bear
- **spine:** B00 ASK → B01 the ladder rungs → B02 prefer lowest rung → B03 stop conditions → B04 what Cowork should never touch → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Six rungs" · Chat → File → Connector → Browser → Computer use → Scheduled · points at: access ladder table
  - [B02] "Lowest rung wins" · Connector beats browser · Browser beats screen · Each rung = more blast radius · points at: rung comparison
  - [B03] "Task packet anatomy" · Named inputs / bounded folders / forbidden actions / output path · points at: worked task packet
  - [B04] "Stop conditions" · Unexpected folder access → stop · Browser for no stated reason → stop · Treat stopping as supervision · points at: stop condition list
  - [B05] "Never-delegate list" · Health/finance/legal data · Credentials · Irreversible external actions · points at: what Cowork should not handle
- **register notes:** The reel's job is to make "lowest rung" a reflex. Don't catalog every rung in depth — show the escalation cost and let the principle land.
- **est length:** 90s

---

## C04 — Diagnosis Before Rewrite

- **slug:** diagnosis-before-rewrite
- **source:** chapters/03-prompting-as-specification.md §Worked Workflow + Common Mistakes
- **premise:** Asking for the finished artifact first is the most common prompting mistake — one habit (diagnosis before rewrite) fixes it.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Evaluate the methods section below. Return a bullet-point diagnosis (issue, severity, reason), then a prioritized revision plan. Do not rewrite yet.`
  - topic: `PROMPT MISTAKES · CAPS`   · segment: `Diagnosis First`
  - greeting: `Ciao`, Bear — Wagwan check: sum(ord(c) for c in "diagnosis-before-rewrite") % 10 == 8 → Ciao, Bear
- **spine:** B00 ASK → B01 artifact-first failure mode → B02 diagnosis → plan → artifact order → B03 requirement-gathering conversation → B04 inspectable vs. accepted output → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Artifact first = blind" · Can't correct a plan you never saw · Diagnosis surfaces assumptions before they harden · points at: before/after prompt
  - [B02] "Three-step order" · Diagnose → Plan → Rewrite · Each step is cheaper to correct than the next · points at: output structure in XML example
  - [B03] "Role prompt trap" · 'Act as expert' ≠ task specification · Roles supplement; task + criteria come first · points at: common mistakes list
  - [B04] "Requirements first" · Ask 3 clarifying questions before producing · Build spec from answers · points at: requirement-gathering prompt
- **register notes:** One behavior change to sell: request the plan before the artifact. The requirement-gathering prompt is a nice bonus kicker at the end.
- **est length:** 75s

---

## C05 — The Cowork Task Packet

- **slug:** cowork-task-packet
- **source:** chapters/05-claude-cowork-as-file-and-workflow-agent.md §Worked Workflow: Assembling a Status Report
- **premise:** A Cowork task without a written packet is guessing — five fields in the packet scope the work, bound the access, and give you something to verify against.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Read the twelve meeting notes in /weekly-notes and tracker.csv. Extract: completed items, tracker gaps, open action items. Save as status-report-[date].md in /project-data/outputs. Do not access other folders. Do not send anything.`
  - topic: `COWORK DELEGATION · CAPS`   · segment: `Task Packet Build`
  - greeting: `Hallo`, Bear — Wagwan check: sum(ord(c) for c in "cowork-task-packet") % 10 == 8 → Hallo, Bear
- **spine:** B00 ASK → B01 packet vs. vague ask → B02 the five packet fields → B03 run + monitor → B04 verify before use → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Packet = spec" · Inputs named / folders bounded / forbidden actions / output path / verify criteria · points at: worked packet block
  - [B02] "Scope by naming" · Grant access only to named folders · Everything else excluded by omission · points at: access restriction line
  - [B03] "Monitor, don't trust" · Watch the task log · Unexpected folder or browser → stop · points at: step 2 monitor block
  - [B04] "Verify before share" · Three-section check / spot-check 5 tracker items / scan for PII · Output file ≠ verified file · points at: step 3 verify list
  - [B05] "Common mistake" · Granting folder access without checking contents · Sensitive drafts may be in scope · points at: common mistakes #2
- **register notes:** The task packet format is the deliverable for the viewer — make it feel copy-paste usable. The "do not send anything" line is the kicker that lands the safety point.
- **est length:** 85s

---

## C06 — The Verification Matrix

- **slug:** verification-matrix
- **source:** chapters/06-the-human-gate.md §The Verification Matrix
- **premise:** Proofreading is not auditing — each output type requires a different evidence check, and the matrix tells you which one before you act.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Summarize these five remote-work productivity papers with citations.`
  - topic: `OUTPUT VERIFICATION · CAPS`   · segment: `Verification Matrix`
  - greeting: `Hej`, Bear — Wagwan check: sum(ord(c) for c in "verification-matrix") % 10 == 9 → Hej, Bear
- **spine:** B00 ASK → B01 fluency ≠ accuracy → B02 editing vs. auditing → B03 matrix by output type → B04 risk-tiered gate → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Fluency is not signal" · Hallucinations match fluent prose · Semantic entropy research: can't tell from surface · points at: opening citation failure
  - [B02] "Edit ≠ audit" · Editing: is it clear? Auditing: is it true? · Most people only edit · points at: editing vs auditing callout
  - [B03] "Matrix row: citation" · Open the source / confirm title + author + year / check it says what Claude claims · points at: matrix table citation row
  - [B04] "Matrix row: number/table" · Recompute a sample / check denominator logic · Clean format ≠ correct formula · points at: matrix table number row
  - [B05] "Risk-tiered gate" · Light / Moderate / Strict by consequence · Short email to client = strict, not low · points at: three-tier callout
- **register notes:** Lead with the opening-scene citation failure — it's visceral. The matrix is the tool to hand the viewer. One rule to land: "no verification path, no delegation."
- **est length:** 88s

---

## C07 — The Scope Stack Setup

- **slug:** scope-stack-setup
- **source:** chapters/09-building-a-personal-claude-workflow.md §The Scope Stack
- **premise:** Cramming every rule into every prompt makes long, fragile prompts — the scope stack splits stable preferences from task-specific instructions so each level does its job.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `What is the best way to keep my Claude preferences consistent without rewriting them in every prompt?`
  - topic: `WORKFLOW DESIGN · CAPS`   · segment: `Scope Stack`
  - greeting: `Hei`, Bear — Wagwan check: sum(ord(c) for c in "scope-stack-setup") % 10 == 3 → Hei, Bear
- **spine:** B00 ASK → B01 the "one big prompt" failure → B02 four levels of the scope stack → B03 projects as the organizing unit → B04 memory: useful and risky → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "One big prompt fails" · Long prompts are fragile · Claude skips parts when instructions crowd out context · points at: common mistake #1
  - [B02] "Four levels" · Account → Project → Task prompt → Human gate · Stable at top, specific at bottom · points at: scope stack table
  - [B03] "Project = workstream" · Persistent context / stable instructions / approved sources · One project per recurring workstream · points at: project setup criteria
  - [B04] "Memory has staleness" · Role changed? Project ended? Memory doesn't know · Review monthly; use for non-sensitive preferences only · points at: memory risk callout
- **register notes:** The scope stack table is the visual anchor. Keep it concrete: account-level = your tone defaults, project-level = audience + format rules, task = the actual ask.
- **est length:** 80s

---

## C08 — The Fluency Correction

- **slug:** fluency-trap-correction
- **source:** chapters/06-the-human-gate.md §Why Fluency Is Not a Verification Signal + Common Mistakes
- **premise:** A smooth, confident Claude output is not evidence of a correct one — fluency is a training artifact, not an accuracy signal.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Is this citation accurate? [paste citation]`
  - topic: `HALLUCINATION LITERACY · CAPS`   · segment: `Fluency vs. Accuracy`
  - greeting: `Ahoj`, Bear — Wagwan check: sum(ord(c) for c in "fluency-trap-correction") % 10 == 7 → Ahoj, Bear
- **spine:** B00 ASK → B01 fluency vs. accuracy → B02 asking Claude to check itself → B03 the one rule → B04 what actually counts as verification → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Fluency ≠ accuracy" · Trained to produce human-confident text · High-entropy outputs match low-entropy fluency · points at: Farquhar 2024 finding
  - [B02] "Self-check is not independent" · Same weights, same failure modes · Asking "is this correct?" ≠ checking the source · points at: common mistake: asking Claude to check itself
  - [B03] "Six false checks" · 'Sounds right' / 'Claude cited it' / 'Table looks clean' / 'Chart is beautiful' / 'Test passed' / 'Claude said it reviewed' · points at: common mistakes list
  - [B04] "The one rule" · No verification path → no delegation · Define evidence before you delegate · points at: rule callout box
- **register notes:** The six false checks are the visual anchor — a quick list that should feel uncomfortable. Land the rule ("no verification path, no delegation") as the corrective reflex.
- **est length:** 78s
