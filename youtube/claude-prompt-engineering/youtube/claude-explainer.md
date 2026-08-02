# Claude Prompt Engineering — Claude Explainer Candidates

---

## C01 — Six Slots, One Better Brief

- **slug:** six-slot-anatomy
- **source:** chapters/01-anatomy-of-a-claude-prompt.md §The Six Components
- **premise:** Most Claude prompts fail not because the task is wrong but because five of the six anatomy slots are empty — showing both a weak and a specified prompt on one screen makes the gap undeniable.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Summarize this report for me. [20-page government report pasted here]`
  - topic: `PROMPT ANATOMY · CAPS`   · segment: `Six Slots, One Better Brief`
  - greeting: `Hola, Bear` — Wagwan check: sum(ord(c) for c in "six-slot-anatomy") % 10 == 1 → Hola, Bear
- **spine:** B00 ASK (vague, one slot) → B01 Task slot: specific verb → B02 Context slot: audience + source → B03 Constraints slot: prohibitions → B04 Format slot: five words, saves five minutes → B05 Examples slot: annotated, not bare → B06 Evaluation criteria: the one slot everyone skips → VERDICT: six slots filled, eight minutes of review instead of forty → Six Slots, One Better Brief outro
- **callouts (≤6):**
  - [B01] "Task verb test" · Testable verb or not? · "Help me" fails; "Summarize" passes · points at: task field in composer
  - [B02] "Context = delta" · Only info that changes output · audience, source, situation · points at: context paragraph
  - [B03] "Positive constraints" · 'Always flag assumptions' beats 'don't be vague' · perimeter tightens output · points at: constraints line
  - [B04] "Five-word format" · 'Three sections, no jargon, 400 words' · most skipped, highest ROI · points at: format spec line
  - [B05] "Annotate examples" · Name what to copy, what to skip · unannotated = unintended lesson · points at: example block
  - [B06] "Criteria precede" · 'A non-specialist explains the risk' = criterion · 'Make it good' is not · points at: evaluation criteria field
- **register notes:** Teardown judgment — the six-slot frame holds; resist calling it a 'framework' (too MBA). Land this: "Five additions took two minutes and saved thirty-two." Don't oversell the components as magic; the human still reviews.
- **est length:** 90s

---

## C02 — Context Hygiene: Prune Before You Paste

- **slug:** context-hygiene-demo
- **source:** chapters/02-context-what-claude-needs-and-what-it-does-not.md §Context Hygiene
- **premise:** Pasting six documents when one pruned excerpt is needed doesn't make Claude smarter — it makes Claude weight the wrong source, and the output fails silently.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Write a paragraph summarizing where we are. [3 status reports + project charter + 40-message email thread pasted]`
  - topic: `CONTEXT HYGIENE · CAPS`   · segment: `Prune Before You Paste`
  - greeting: `Merhaba, Bear` — Wagwan check: sum(ord(c) for c in "context-hygiene-demo") % 10 == 9 → Merhaba, Bear
- **spine:** B00 ASK (six documents, no labels) → B01 Four context types: essential / useful / neutral / harmful → B02 Harmful: false-priority and structural harm shown → B03 Label your sources (authoritative vs. background) → B04 State assumptions explicitly → B05 Declare exclusions → VERDICT: curated context outperforms comprehensive dumps → Prune Before You Paste outro
- **callouts (≤6):**
  - [B01] "Essential only" · Info that changes output if absent · audience, source, purpose · points at: context type table
  - [B02] "Harmful context" · Big formal doc outweighs recent email · Claude weights by structure, not recency · points at: document stack in composer
  - [B03] "Label before paste" · 'Source A [authoritative]' vs. 'Source B [background only]' · unlabeled = Claude guesses weight · points at: label lines in prompt
  - [B04] "Exclusion declaration" · 'Ignore the appendices' is a constraint on context · prevents Claude using what's there but shouldn't shape output · points at: exclusion instruction
  - [B05] "Prune two minutes" · Select only the section the task draws on · curated section beats full document · points at: before/after paste sizes
- **register notes:** The strongest line is "Irrelevant context doesn't just fail to help — it distorts." Don't claim Claude 'gets confused'; say it weights by structural prominence rather than relevance. Human still decides what's authoritative.
- **est length:** 85s

---

## C03 — Constraint Builder: Close the Fabrication Gap

- **slug:** constraint-builder
- **source:** chapters/03-constraints-and-boundaries.md §The "Do Not Invent" Instruction
- **premise:** A prompt without an evidence constraint doesn't fail — it produces a confident fabrication dressed in professional prose, and the researcher sends it out.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Summarize the research on remote work and productivity.`
  - topic: `CONSTRAINT TYPES · CAPS`   · segment: `Constraint Builder`
  - greeting: `Bonjour, Bear` — Wagwan check: sum(ord(c) for c in "constraint-builder") % 10 == 1 → Bonjour, Bear
- **spine:** B00 ASK (no constraints, hallucination risk) → B01 Five constraint types: scope / evidence / uncertainty / privacy / register → B02 Evidence constraint: 'using only the three reports below' → B03 Do-not-invent: mark [uncertain] not stop → B04 Refusal rule vs. flag-and-continue vs. narrow-scope → B05 Constraint checklist as review → VERDICT: constrained output is auditable; unconstrained output is interpretable → Constraint Builder outro
- **callouts (≤6):**
  - [B01] "Scope vs. evidence" · Scope = what's in the task · Evidence = what Claude may draw on · different gates, both needed · points at: constraint type list
  - [B02] "Positive constraints" · 'Always flag assumptions' · constraints aren't only prohibitions · points at: positive constraint examples
  - [B03] "Do not invent" · '[uncertain]' tag: signals, doesn't stop workflow · keeps review moving · points at: inline tag in output
  - [B04] "Refusal rules" · 'Flag and continue' vs. 'Refuse or ask' · stakes determine choice · points at: three rule options
  - [B05] "Checklist review" · Each constraint = one review question · inspection not interpretation · points at: constraint checklist
- **register notes:** The opening story (confident fabrication, researcher sends it) is the strongest moment — don't soften it. Land: "The failure was not Claude's. The failure was in the specification." Don't imply constraints are foolproof; human still checks.
- **est length:** 95s

---

## C04 — Annotate Your Example

- **slug:** examples-annotate
- **source:** chapters/04-examples-counterexamples-and-style.md §Before and After: Annotating an Example
- **premise:** An unannotated example teaches every feature it contains — including the ones you didn't mean to teach — because Claude has no way to know which features are intentional.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Here is a paragraph I wrote. Write two more paragraphs in the same style. [informal lab-grant paragraph pasted]`
  - topic: `FEW-SHOT EXAMPLES · CAPS`   · segment: `Annotate Your Example`
  - greeting: `Ciao, Bear` — Wagwan check: sum(ord(c) for c in "examples-annotate") % 10 == 6 → Ciao, Bear
- **spine:** B00 ASK (unannotated example, wrong register imported) → B01 In-context learning: example teaches format + tone + subject at once → B02 What the example taught that wasn't intended → B03 Annotation fix: name features to copy, features to exclude → B04 Counterexamples: showing bad to prevent the failure mode → B05 Style guide as condensed context → VERDICT: annotate every example; the demonstration needs a narrator → Annotate Your Example outro
- **callouts (≤6):**
  - [B01] "Everything is taught" · Format, tone, subject matter, register · unannotated example = all-in lesson · points at: paragraph example in composer
  - [B02] "Annotation format" · 'Features to copy: X · Do not copy subject matter' · three sentences changes the output · points at: annotated version
  - [B03] "Counterexample" · Show the failure mode explicitly · 'Do not write like this' beats describing the problem abstractly · points at: counterexample block
  - [B04] "Overfit check" · Does output stand without the example? · If not, Claude is mimicking, not producing · points at: output review
- **register notes:** The writing instructor story is clean — she was pleased, then surprised. Land: "The example she chose taught Claude what informal looked like, and Claude learned the lesson she did not intend to teach." Don't make it sound like Claude is misbehaving; it's learning what you showed.
- **est length:** 80s

---

## C05 — Criteria Before Output

- **slug:** criteria-first-habit
- **source:** chapters/05-evaluation-criteria-before-output.md §The Core Idea: Criteria-First Specification
- **premise:** The grant writer who didn't get funded had clean prose and wrong criteria — she never told Claude, or herself, what 'ready to submit' actually meant.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Write a one-page executive summary of the attached program evaluation report.`
  - topic: `EVALUATION CRITERIA · CAPS`   · segment: `Criteria Before Output`
  - greeting: `Jambo, Bear` — Wagwan check: sum(ord(c) for c in "criteria-first-habit") % 10 == 3 → Jambo, Bear
- **spine:** B00 ASK (task, no criteria) → B01 Four criteria types: accuracy / completeness / format / failure → B02 'What would make this wrong?' as design habit → B03 Rubric as prompt component: same doc serves spec and review → B04 Source-check and calculation-check criteria → B05 Criteria-first as writer's practice → VERDICT: inspection beats interpretation; criteria make review faster and harder to skip → Criteria Before Output outro
- **callouts (≤6):**
  - [B01] "Failure criteria" · 'If qualified finding presented as definitive, output fails' · names catastrophic, not optimal · points at: failure criterion in prompt
  - [B02] "'What would make this wrong?'" · Three failure modes named in advance = three prevented failures · two minutes of pre-work · points at: failure criterion list
  - [B03] "Rubric in prompt" · Table in the prompt = spec + review checklist in one · same document, both functions · points at: rubric table
  - [B04] "Calc-check criteria" · 'Show all intermediate steps' · final figures hide errors; steps reveal them · points at: calculation-check instruction
  - [B05] "Criteria precede" · Write criteria before task description · reveals requirements not yet consciously held · points at: criteria-first ordering
- **register notes:** The automation-bias point (Mosier & Skitka) is load-bearing — name it plainly: "Explicit criteria are a structural counter to the tendency to trust confident-looking output." Don't skip the grant writer's story; it's the cleanest opening in the book.
- **est length:** 90s

---

## C06 — Revision Change Log

- **slug:** revision-change-log
- **source:** chapters/06-iteration-and-revision-loops.md §The Change Log Request
- **premise:** "Make it better" tells Claude to make it different — and without a change log, you can't tell what moved, so the next revision is also blind.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Make it more engaging and fix the structure.`
  - topic: `REVISION LOOPS · CAPS`   · segment: `Revision Change Log`
  - greeting: `Hej, Bear` — Wagwan check: sum(ord(c) for c in "revision-change-log") % 10 == 5 → Hej, Bear
- **spine:** B00 ASK (vague revision, drift) → B01 Diagnose before you send: four-step revision loop → B02 Name the failure separately from the preservation constraint → B03 Change log request: what moved, what changed, what stayed → B04 Compare-and-select: two versions, one decision → B05 When to start over, not revise → VERDICT: a revision prompt is a second specification; the change log makes drift visible → Revision Change Log outro
- **callouts (≤6):**
  - [B01] "Diagnose first" · Name failure categories before typing revision · 'Tone' + 'Structure' separately, not together · points at: diagnostic revision prompt
  - [B02] "Preservation wall" · 'Keep all statistics exactly as written' · revision prompt = change + what must not change · points at: constraints block in revision
  - [B03] "Change log" · Three items: moved / changed language / kept exact · catches implicit overwrites before they compound · points at: change log request
  - [B04] "Start-over signals" · Wrong task entirely / compounding errors / constraint violations accumulate · stop and rewrite the prompt, not the output · points at: start-over checklist
- **register notes:** The strongest single line: "You have not made the work better. You have made the work different." Land it early. The self-critique caveat is important — Claude's self-assessment of factual accuracy is not reliable; don't overstate its usefulness.
- **est length:** 85s

---

## C07 — Prompt Card Builder

- **slug:** prompt-card-builder
- **source:** chapters/12-building-a-reusable-prompt-library.md §The Prompt Card Format
- **premise:** Every professional has a prompt that worked buried in chat history — the cost of treating successful prompts as disposable chat is rewriting from scratch every time.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Here are some meeting notes. Can you pull out the action items?`
  - topic: `PROMPT LIBRARY · CAPS`   · segment: `Prompt Card Builder`
  - greeting: `Hallo, Bear` — Wagwan check: sum(ord(c) for c in "prompt-card-builder") % 10 == 7 → Hallo, Bear
- **spine:** B00 ASK (one-off prompt, no card) → B01 Eight card fields: purpose / inputs / constraints / format / review criteria / example / failure modes / revision history → B02 Before/after: one-off vs. card version → B03 Three library needs: naming / index / tested flag → B04 Why the review criteria field is the one people skip → B05 Stale cards: the quarterly review habit → VERDICT: the card transfers the prompt and the standard — without review criteria, only the prompt travels → Prompt Card Builder outro
- **callouts (≤6):**
  - [B01] "Eight fields" · Purpose · Inputs · Constraints · Format · Review criteria · Example · Failure modes · Revision history · points at: card template
  - [B02] "Review criteria field" · 'Most writers skip; most important for maintaining quality' · transfers the standard not just the text · points at: review criteria row in card
  - [B03] "Tested flag" · 'Last tested: date / Status: Active or Review needed' · untested card = false confidence · points at: index table
  - [B04] "Failure modes honest" · 'Tends to merge action items when notes are paraphrased' · tested on edge case, not just clean example · points at: known failure modes field
- **register notes:** The SOP binder / style guide / pattern library analogy at the end of chapter 13 is worth a brief nod — the prompt card isn't new, it's the same discipline in a new medium. Land: "Don't start from zero next time." Resist making the card sound like bureaucracy; emphasize the fifteen minutes paid back.
- **est length:** 90s

---

## C08 — Agentic Approval Gate

- **slug:** agentic-approval-gate
- **source:** chapters/11-prompts-as-handoffs-to-claude-code-and-cowork.md §The After Prompt
- **premise:** "Clean up this folder" is a wish — when handed to an agent that can actually delete files, the distance between what you meant and what happens becomes consequential and sometimes unrecoverable.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Clean up the reports folder. The filenames are inconsistent and there are some duplicates.`
  - topic: `AGENTIC HANDOFFS · CAPS`   · segment: `Agentic Approval Gate`
  - greeting: `Hei, Bear` — Wagwan check: sum(ord(c) for c in "agentic-approval-gate") % 10 == 7 → Hei, Bear
- **spine:** B00 ASK (conversational request → agent deletes files) → B01 What changes with agentic tools: actions vs. answers → B02 The handoff template: workspace / authorized / prohibited / decision rule / gate / verify / uncertainty → B03 Approval gate: list proposed renames, wait → B04 Verification: 'done' ≠ 'correct' → B05 When to use conversation before handoff → VERDICT: a handoff is a change request; scope, authorization, gate, and verify are non-negotiable → Agentic Approval Gate outro
- **callouts (≤6):**
  - [B01] "Acts, not answers" · Chat → text to discard · Agent → renames, deletes, moves · miscalibration cost is higher · points at: agentic risk framing
  - [B02] "Authorization list" · 'Rename: Yes · Move: No · Delete: No · New folders: No' · explicit prohibition = required, not redundant · points at: authorization block in handoff
  - [B03] "Gate before action" · 'List proposed renames, wait for approval' · gate after batch action = too late · points at: approval gate instruction
  - [B04] "Verification step" · 'List every file with new name after completion' · completion ≠ correctness; read the list · points at: verification requirement
  - [B05] "Chat first" · Underspecified task → conversation → then handoff · handing underspecified task to agent makes underspecification consequential · points at: workflow order
- **register notes:** The communications manager story is the coldest open — some deletions are not recoverable. Don't soften it. The human-in-the-loop point (NIST AI RMF) is accurate but name it plainly: "Gates only protect you if you read what's proposed." The calibration-to-stakes principle is the nuanced landing: not every handoff needs every element.
- **est length:** 95s
