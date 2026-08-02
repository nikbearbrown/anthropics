# Claude Agentic AI — Claude Explainer Candidates

## C01 — Plan Before Acting

- **slug:** plan-before-acting
- **source:** chapters/07-planning-before-acting.md §What a Plan Is Actually For + What a Good Plan Looks Like
- **premise:** Agents plan whether you ask them to or not — requiring a visible plan before execution surfaces the interpretation that was already there, at zero cost.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Before acting, show me your plan: goal, inputs, steps, permissions needed, stop conditions, and what evidence will show the task is complete.`
  - topic: `AGENT PLANNING · CAPS`   · segment: `Plan-First Gate`
  - greeting: `Privet`, Bear — Wagwan check: sum(ord(c) for c in "plan-before-acting") % 10 == 4 → Privet, Bear
- **spine:** B00 ASK → B01 invisible vs. visible plan → B02 eight plan elements → B03 caption-plan vs. real plan → B04 material-plan-change rule → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Plans already happen" · ReAct architecture always sequences · Question is: readable before execution or not? · points at: invisible plan diagram
  - [B02] "Eight elements" · Goal / Inputs / Tools / Sequence / Permissions / Reversibility / Stop condition / Evidence · points at: plan element checklist table
  - [B03] "Caption ≠ plan" · 'I'll review files and prepare a summary' omits all eight · Sounds competent; approves nothing concrete · points at: side-by-side good vs. caption plan
  - [B04] "Material change = stop" · Scope expands mid-task → pause before proceeding · Report after ≠ ask before · points at: material-plan-change rule block
  - [B05] "Risk tiers plan depth" · Low-risk → light plan / Write access → full template / Production → strict + approval per action · points at: three-tier table
- **register notes:** The caption-plan vs. real-plan side-by-side is the visual anchor. Land "plan before execution, stop before scope change" as the two behavioral habits.
- **est length:** 88s

---

## C02 — Silent Omission Signal

- **slug:** silent-omission-signal
- **source:** chapters/09-failure-modes-of-agentic-work.md §Silent Omission
- **premise:** Agents summarize what they can reach and present it as complete — the fix is requiring a processed-count artifact, not a completion claim.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Summarize all feedback documents in the shared project folder and write an executive brief.`
  - topic: `AGENTIC FAILURE MODES · CAPS`   · segment: `Silent Omission`
  - greeting: `Yassou`, Bear — Wagwan check: sum(ord(c) for c in "silent-omission-signal") % 10 == 4 → Yassou, Bear
- **spine:** B00 ASK → B01 the silent omission failure → B02 why agents don't announce gaps → B03 recognition sign: count mismatch → B04 prevention: require inventory artifact → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "No error announced" · Agent processes what it reaches · Presents partial result as complete picture · points at: opening brief scenario
  - [B02] "Agents optimize completion" · Tool call failures logged internally · Not surfaced in output unless designed to be · points at: failure mode definition
  - [B03] "Recognition sign" · Processed count ≠ expected count · Output mentions no limitations or skipped files · points at: recognition sign callout
  - [B04] "Inventory artifact" · Require: items in scope / items processed / items failed or skipped · Count absence = warning · points at: prevention note
  - [B05] "Compound risk" · Silent omission + plausible summary = confident, incomplete brief · Both often present together · points at: opening scene result
- **register notes:** The opening brief scenario is the whole lesson — make the viewer feel the moment of "three documents contradicted the recommendation." Inventory-artifact requirement is the one deliverable.
- **est length:** 82s

---

## C03 — MCP Resource vs. Tool

- **slug:** mcp-resource-vs-tool
- **source:** chapters/06-mcp-and-external-capabilities.md §What an MCP Server Exposes + Read-Only vs. Write-Capable
- **premise:** MCP servers expose resources (read) and tools (act) — connecting a write-capable tool without an approval gate is when the production ticket gets marked done.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `What is the difference between an MCP resource and an MCP tool, and why does it matter for safety?`
  - topic: `MCP PERMISSIONS · CAPS`   · segment: `Resource vs. Tool`
  - greeting: `Merhaba`, Bear — Wagwan check: sum(ord(c) for c in "mcp-resource-vs-tool") % 10 == 6 → Merhaba, Bear
- **spine:** B00 ASK → B01 resource vs. tool distinction → B02 write-capable = state changes → B03 prompt injection via tool results → B04 review checklist before connecting → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Resources: read-only" · Documents / schemas / data files · Agent reads; nothing changes outside · points at: MCP element table
  - [B02] "Tools: active" · Create ticket / send message / push commit / delete record · Effects persist after session ends · points at: tool examples list
  - [B03] "Blast radius" · Server A (read-only docs): wrong answer risk / Server B (write PM system): production queue risk · points at: two-server comparison
  - [B04] "Prompt injection via tools" · Doc contains "forward contents to this email" · Agent can't ignore if email tool is available · points at: prompt-injection via tools section
  - [B05] "Review gate" · Who maintains it / what tools exposed / reversible? / human approval gate? · Before you connect, not after · points at: review questions list
- **register notes:** The opening-scene production ticket is the hook. The resource/tool distinction is the corrective frame. End on: "connecting a server is an approval decision, not a setup step."
- **est length:** 85s

---

## C04 — Fabricated Completion Tell

- **slug:** fabricated-completion-tell
- **source:** chapters/09-failure-modes-of-agentic-work.md §Fabricated Completion
- **premise:** "I checked all citations and confirmed they are accurate" is not a verification — it's completion text, and the tell is that no artifact backs it up.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `List the sources you opened, with filenames or URLs, and confirm the row count before and after processing.`
  - topic: `AGENTIC FAILURE MODES · CAPS`   · segment: `Fabricated Completion`
  - greeting: `Shalom`, Bear — Wagwan check: sum(ord(c) for c in "fabricated-completion-tell") % 10 == 4 → Shalom, Bear
- **spine:** B00 ASK → B01 fabricated completion defined → B02 why agents do it → B03 recognition sign: claim without artifact → B04 prevention: require completion artifacts → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Completion text ≠ done" · 'I verified all sources' = output pattern · No source was necessarily opened · points at: failure mode definition
  - [B02] "Optimization pressure" · Tasks like 'verify X and summarize' invite 'verified — complete' · Least-resistance output path · points at: why agents do it note
  - [B03] "Recognition sign" · Completion claim with no supporting artifact · 'Confirmed' with no log, list, or count · points at: recognition sign callout
  - [B04] "Artifact not claim" · 'List the sources you opened with filename' · 'Show row count before and after' · points at: prevention examples
- **register notes:** The literature-summary citation failure (from ch.8's worked trace) is a perfect cold open hook. The correction is one sentence: require artifacts, not claims.
- **est length:** 75s

---

## C05 — Blast Radius Calc

- **slug:** blast-radius-calc
- **source:** chapters/03-tools-permissions-and-the-action-surface.md §Reversibility and Blast Radius
- **premise:** The blast radius of an agent error scales with the action surface, not the plausibility of the plan — two questions before any agentic task close most of the gap.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Before we start: is this action reversible, and what is the blast radius if the plan is wrong?`
  - topic: `AGENTIC PERMISSIONS · CAPS`   · segment: `Blast Radius`
  - greeting: `Salaam`, Bear — Wagwan check: sum(ord(c) for c in "blast-radius-calc") % 10 == 5 → Salaam, Bear
- **spine:** B00 ASK → B01 action surface vs. task description → B02 reversibility question → B03 blast radius question → B04 approve access before plan, not because of plan → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Surface ≠ task" · Blast radius = what agent could touch · Not what it intends to do · points at: folder cleanup opening scene
  - [B02] "Reversibility test" · Move to temp → reversible / Delete permanently → not / Draft → reversible / Send → not · points at: reversibility callout
  - [B03] "Blast radius scale" · Read one folder + write one file = small / Broad folder + terminal + email connector = large · Scale approval friction to blast radius · points at: blast radius examples
  - [B04] "Plan ≠ permission" · Confident plan is not evidence to expand access · Access question answered before plan exists · points at: "the plan is not a permission" section
  - [B05] "Least privilege rule" · Lowest rung that completes the task · Stand there; don't reach higher for efficiency · points at: OWASP excessive agency note
- **register notes:** The folder cleanup opening scene is a perfect cold open — no malice, no error, just wrong scope. The two questions (reversibility + blast radius) are the deliverable.
- **est length:** 86s

---

## C06 — Material Plan Change Rule

- **slug:** material-plan-change
- **source:** chapters/07-planning-before-acting.md §The Material-Plan-Change Rule
- **premise:** When an agent adapts mid-task, small scope changes feel normal from inside — the material-plan-change rule forces a stop-and-ask before those changes become consequences.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `If at any point you need to deviate from this plan in a way that changes the tools you use, the data you touch, or the risk level of an action, stop and tell me before proceeding.`
  - topic: `AGENT SUPERVISION · CAPS`   · segment: `Material Plan Change`
  - greeting: `Jambo`, Bear — Wagwan check: sum(ord(c) for c in "material-plan-change") % 10 == 8 → Jambo, Bear
- **spine:** B00 ASK → B01 agents adapt mid-task → B02 small changes feel normal → B03 the material-plan-change rule → B04 report after ≠ ask before → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Agents always adapt" · Tool fails / file missing / new context → agent adjusts · Within-scope fine; outside-scope not · points at: adaptation examples
  - [B02] "Small = large" · Read one extra file / send to shared folder for convenience / install library for parsing · Each is a scope expansion · points at: "feel small from inside" examples
  - [B03] "The rule" · Material change = different tool, new data, higher risk level → stop and ask before proceeding · points at: material-plan-change rule callout
  - [B04] "After ≠ before" · Reporting scope change after = audit log · Asking before = supervision · Only before catches the error · points at: report vs. ask distinction
- **register notes:** The three "feel small" examples (extra file, shared folder, library install) are the surprise twist — make them land before introducing the rule.
- **est length:** 78s

---

## C07 — Team AI-Use Register

- **slug:** team-ai-use-register
- **source:** chapters/11-agentic-ai-in-teams-and-organizations.md §The Team AI-Use Register + Meaningful Oversight
- **premise:** Individual caution doesn't aggregate into team safety — one shared register with six fields converts informal practice into an auditable boundary.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Help me fill out a team AI-use register entry: use case, owner, Claude surface, data allowed, data forbidden, human gate, and escalation path.`
  - topic: `TEAM AI GOVERNANCE · CAPS`   · segment: `AI-Use Register`
  - greeting: `Habari`, Bear — Wagwan check: sum(ord(c) for c in "team-ai-use-register") % 10 == 2 → Habari, Bear
- **spine:** B00 ASK → B01 inconsistency problem → B02 the register fields → B03 meaningful vs. nominal oversight → B04 MCP servers at team level → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "Individual ≠ team" · 5 cautious people / no shared boundary · Different rules, accountability gaps, governance drift · points at: opening marketing-team scenario
  - [B02] "Register entry" · Use case / Owner / Surface / Data allowed / Data forbidden / Human gate / Log / Escalation · points at: sample register entry block
  - [B03] "Nominal oversight" · Reviewer lacks time/context/authority/evidence · Accountability on paper, not in practice · points at: four requirements for meaningful oversight
  - [B04] "Shared asset risk" · One MCP server added = available to all team members · Connector scope extends to everything in the folder · points at: shared-asset callout
- **register notes:** The opening marketing-team scenario is a portrait — five people, zero shared model. One register entry is the minimum viable output. Don't oversell formality; sell "at least agree on the boundary."
- **est length:** 85s

---

## C08 — Irreversible Action Gate

- **slug:** irreversible-action-gate
- **source:** chapters/09-failure-modes-of-agentic-work.md §Irreversible Action + chapters/08-verification-is-the-control-system.md §External Actions
- **premise:** Agents don't distinguish reversible from irreversible operations — the gate belongs to the human, placed before execution, not after.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Any action that sends, submits, or deletes — stop and confirm with me before proceeding.`
  - topic: `AGENTIC SAFETY · CAPS`   · segment: `Irreversible Action Gate`
  - greeting: `Namaste`, Bear — Wagwan check: sum(ord(c) for c in "irreversible-action-gate") % 10 == 9 → Namaste, Bear
- **spine:** B00 ASK → B01 reversible vs. irreversible: agents don't know → B02 recognition sign → B03 human gate placement → B04 external-action approval → VERDICT → title-restate outro
- **callouts (≤6):**
  - [B01] "No auto-distinction" · Agents use available tools / task says to · Reversibility is a human judgment, not a model constraint · points at: failure mode definition
  - [B02] "Recognition sign" · Any action that crosses a system boundary / can't be undone with ctrl-z / touches systems you don't fully control · points at: recognition sign callout
  - [B03] "Gate placement" · Before = supervision / After = audit · Once sent, it's sent · Only before-gate catches the error · points at: external-action gate note in ch.8
  - [B04] "Design rule" · Any action you wouldn't want executed by accident → human initiates, not approves after · points at: design rule callout
  - [B05] "Scope: send/submit/delete" · Email / Form / File deletion / API with side effects / Communication platform post · points at: irreversible action examples list
- **register notes:** The "gate before, not after" distinction is the whole lesson. Keep the examples short and recognizable (email, form submit, file delete). The design rule is the one line to land.
- **est length:** 80s
