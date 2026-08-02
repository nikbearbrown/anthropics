# Claude for Education: A Practitioner's Guide — Claude Explainer Candidates

## C01 — The Eight-Field Instructional Brief

- **slug:** instructional-brief-eight-fields
- **source:** chapters/03-prompting-claude-like-an-instructional-designer.md §The Eight-Field Instructional Brief
- **premise:** A topic-description prompt produces plausible prose that fits nobody — the eight-field brief turns Claude into a design partner by making instructional specification explicit before any draft is generated.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Give me a lesson on opportunity cost for my intro economics class`
  - topic: `INSTRUCTIONAL BRIEFS · EDUCATION`   · segment: `Eight-Field Specification`
  - greeting: `Namaste`, Bear — Wagwan check: sum(ord(c) for c in "instructional-brief-eight-fields") % 10 == 8 → Namaste, Bear
- **spine:** B00 ASK → B01 plausible output, fits no one → B02 Marta's problem: topic not situation → B03 the eight fields → B04 misconception field = the pivotal difference → B05 teacher review criteria field → VERDICT → instructional-brief-eight-fields outro
- **callouts (≤6):**
  - [B01] "Topic vs. situation" · "Lesson on cells" vs. "cells as dynamic systems, misconception: static containers" · points at: two prompts side by side
  - [B02] "Field 3: Misconception" · What students actually believe that is wrong or incomplete · points at: field box
  - [B03] "Field 4: Outcome" · "Students will explain why a plant in the dark loses mass" — not "understand photosynthesis" · points at: outcome field
  - [B04] "Field 8: Must-not" · "Do not reduce reading level without disclosure" · points at: must-not field
  - [B05] "Plausible ≠ aligned" · Claude generates fluent language — alignment is your review job · points at: checklist
- **register notes:** The Marta/Priya contrast is the sharpest entry — the eight fields are the mechanism, but the correction is "topic prompt vs. situation brief."
- **est length:** 85s

---

## C02 — Differentiation Audit: Preserving the Intellectual Target

- **slug:** differentiation-audit
- **source:** chapters/06-differentiation-and-accessibility.md §The Human Gate
- **premise:** The most dangerous differentiation error is invisible: Claude simplifies the task so thoroughly that the student completes it without doing the thinking — and the teacher never notices because the work looks finished.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Create a plain-language version of this primary source annotation assignment for students reading two grade levels below`
  - topic: `DIFFERENTIATION · EDUCATION`   · segment: `The Five-Question Audit`
  - greeting: `Annyeong`, Bear — Wagwan check: sum(ord(c) for c in "differentiation-audit") % 10 == 5 → Annyeong, Bear
- **spine:** B00 ASK → B01 simpler language ✓ → B02 did the intellectual task survive? → B03 the five-question audit → B04 scaffolding vs. replacing thinking → B05 dignity and choice framing → VERDICT → differentiation-audit outro
- **callouts (≤6):**
  - [B01] "The target is non-negotiable" · Simpler instructions, same analytic demand · points at: learning outcome statement
  - [B02] "Claude's flag" · "The word 'assumptions' may still need defining" — use it · points at: Claude output excerpt
  - [B03] "Q1 of the audit" · Is the learning target preserved? · points at: five-question list
  - [B04] "Q3 of the audit" · Does any part do the student's thinking for them? · points at: audit checklist
  - [B05] "Dignity check" · Adaptations offered as choices, not marked as the easy version · points at: distribution question
- **register notes:** The "completed but didn't learn" failure is the honest tension — most teachers have seen it; naming it earns trust before the fix.
- **est length:** 80s

---

## C03 — Faculty: Literature Leads Are Not Citations

- **slug:** faculty-literature-lead
- **source:** chapters/11-research-advising-and-faculty-workflows.md §Workflow 1: Literature Exploration
- **premise:** Claude will name real scholars in plausible-sounding citations that do not exist — treating a literature map as a bibliography is a credibility error, and the verification step is not optional.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Map the major debates in adaptive feedback research for first-year writing courses, with key scholars and journals`
  - topic: `RESEARCH WORKFLOWS · EDUCATION`   · segment: `Literature Leads vs. Citations`
  - greeting: `Merhaba`, Bear — Wagwan check: sum(ord(c) for c in "faculty-literature-lead") % 10 == 5 → Merhaba, Bear
- **spine:** B00 ASK → B01 confident map with scholar names and journal titles → B02 two of five citations do not exist → B03 lead vs. citation distinction → B04 verification workflow → B05 gap flags as search signals → VERDICT → faculty-literature-lead outro
- **callouts (≤6):**
  - [B01] "Plausible ≠ real" · Claude attaches real names to titles that don't exist · points at: citation list
  - [B02] "Lead-generation use" · Conceptual terrain, search terms, scholar names to check · points at: output frame
  - [B03] "Every citation gets a database check" · Before it enters your work · points at: verification step
  - [B04] "Use the gaps" · "I'm less confident about recent empirical work" = search harder there · points at: hedged output line
  - [B05] "COPE rule" · Human author responsible for all cited content regardless of AI assist · points at: integrity boundary
- **register notes:** The "hallucinated citation" is now well-known — the sharper correction here is using Claude's own hedges as search intelligence, which is less familiar.
- **est length:** 75s

---

## C04 — Stress-Test the Assignment Before Students Do

- **slug:** assignment-stress-test
- **source:** chapters/11-research-advising-and-faculty-workflows.md §Workflow 5: Assignment Redesign
- **premise:** Asking Claude to read your assignment as a student who wants to avoid intellectual work reveals every place AI output satisfies the requirement — and that audit is higher leverage than any AI-use policy.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Read this assignment prompt as a student who would rather use AI than do the intellectual work — where does AI output satisfy the requirement without demonstrating learning?`
  - topic: `ASSIGNMENT DESIGN · EDUCATION`   · segment: `AI Stress-Test`
  - greeting: `Shalom`, Bear — Wagwan check: sum(ord(c) for c in "assignment-stress-test") % 10 == 5 → Shalom, Bear
- **spine:** B00 ASK → B01 Claude identifies three exploit points → B02 product not process → B03 three redesign moves → B04 process evidence as the fix → VERDICT → assignment-stress-test outro
- **callouts (≤6):**
  - [B01] "What Claude finds" · "State a thesis" — any AI can; no process evidence required · points at: prompt excerpt
  - [B02] "Product vs. process" · Final essay → revision memo + annotated draft + peer comment · points at: redesign list
  - [B03] "Redesign move 1" · Build in a step only the student who did the thinking can complete · points at: redesigned prompt
  - [B04] "Higher leverage than policy" · Detecting the exploit before students do beats punishing it after · points at: comparison frame
- **register notes:** The adversarial framing (Claude playing the lazy student) is novel and memorable — don't over-explain it, let the viewer feel the jolt.
- **est length:** 70s

---

## C05 — Advising Privacy Gate: Anonymize Before Prompting

- **slug:** advising-privacy-gate
- **source:** chapters/11-research-advising-and-faculty-workflows.md §Workflow 3: Advising Preparation
- **premise:** Entering a student's name, ID, or grades into Claude may constitute a FERPA disclosure — and the workaround is not a lesser approach, it is the correct one: anonymized composites preserve everything useful.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Help me prepare for a difficult advising meeting with a junior student considering late withdrawal from a science course`
  - topic: `ADVISING · EDUCATION`   · segment: `Privacy-Safe Advising Prep`
  - greeting: `Salaam`, Bear — Wagwan check: sum(ord(c) for c in "advising-privacy-gate") % 10 == 6 → Salaam, Bear
- **spine:** B00 ASK → B01 useful meeting prep arrives → B02 the identity risk — what not to type → B03 anonymized composite prompt → B04 opening questions that invite student framing → B05 Claude as thought partner not advising record → VERDICT → advising-privacy-gate outro
- **callouts (≤6):**
  - [B01] "What not to type" · Name, student ID, grades, declared major, disclosed disability · points at: redacted field list
  - [B02] "FERPA boundary" · Entry into a third-party AI tool may constitute disclosure · points at: policy note
  - [B03] "The anonymized prompt" · "A junior student in a science course" — everything you need · points at: anonymized composer
  - [B04] "Opening curiosity questions" · Invite the student to frame the situation themselves · points at: output questions
  - [B05] "Thought partner, not record" · Judgment in the meeting stays entirely yours · points at: gate statement
- **register notes:** The FERPA angle is concrete and underappreciated among faculty — pair it with the positive (anonymized prompts work well) to avoid a doom-only read.
- **est length:** 75s

---

## C06 — UDL Choice Board in One Prompt

- **slug:** udl-choice-board
- **source:** chapters/06-differentiation-and-accessibility.md §Core Concepts
- **premise:** Universal Design for Learning choice boards often fail because the paths look equivalent but aren't — one prompt can draft the board, but a teacher must verify that all three options actually require the same intellectual work.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Draft a UDL choice board for my unit on argument writing — three ways students can demonstrate their understanding`
  - topic: `UDL · EDUCATION`   · segment: `Choice Board Audit`
  - greeting: `Jambo`, Bear — Wagwan check: sum(ord(c) for c in "udl-choice-board") % 10 == 4 → Jambo, Bear
- **spine:** B00 ASK → B01 three options appear → B02 one option is actually lower demand → B03 all paths must reach the same learning outcome → B04 the equity check → VERDICT → udl-choice-board outro
- **callouts (≤6):**
  - [B01] "UDL principle" · Multiple means of representation, action, engagement — not easier vs. harder · points at: UDL definition
  - [B02] "The demand check" · Do all three paths require the same intellectual labor? · points at: side-by-side options
  - [B03] "Not busywork" · More questions or longer responses ≠ deeper thinking · points at: extension trap
  - [B04] "Equity risk" · If students consistently choose the lower-demand path, the board has reproduced the problem · points at: usage observation
- **register notes:** The "looks equal but isn't" failure is the honest tension; keep the equity note brief — the core lesson is the audit question, not the equity lecture.
- **est length:** 70s

---

## C07 — Capstone Unit Builder: Coherence Is the Human's Job

- **slug:** capstone-unit-builder
- **source:** chapters/12-capstone-a-claude-supported-unit.md §What This Chapter Produces
- **premise:** Seven components — outcomes, sequence, materials, feedback, assessment, AI policy, verification checklist — can each be drafted by Claude, but only the teacher can check that they cohere, because coherence requires knowing what learning is actually for.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Draft learning outcomes for a three-week argument writing unit, then flag any that might be hard to assess`
  - topic: `UNIT DESIGN · EDUCATION`   · segment: `The Seven-Component Capstone`
  - greeting: `Konnichiwa`, Bear — Wagwan check: sum(ord(c) for c in "capstone-unit-builder") % 10 == 2 → Konnichiwa, Bear
- **spine:** B00 ASK → B01 five outcomes plus a flag → B02 teacher accepts flag and adds revision memo → B03 seven components must cohere → B04 assessment must measure the outcomes → B05 verification checklist as the record → VERDICT → capstone-unit-builder outro
- **callouts (≤6):**
  - [B01] "Claude's flag" · Outcome 5 (revision) is process evidence — hard to assess from final draft alone · points at: flagged outcome
  - [B02] "Accepting the flag" · Teacher checks timeline, adds revision memo — human decision · points at: acceptance moment
  - [B03] "Coherence test" · Does the assessment actually measure the outcomes? · points at: component map
  - [B04] "Verification checklist" · Record of where Claude helped, where human judgment decided · points at: checklist field
  - [B05] "Claude as co-author?" · No — Claude drafts seven components; you decide what learning is for · points at: authorship boundary
- **register notes:** The capstone frame earns its place as the synthesis card — position this as the "now put it all together" beat, not another pattern drill.
- **est length:** 80s

---

## C08 — Manuscript Reviewer Response: Claude as First Draft, You as Final Author

- **slug:** manuscript-reviewer-response
- **source:** chapters/11-research-advising-and-faculty-workflows.md §Workflow 4: Manuscript Feedback and Reviewer-Response Planning
- **premise:** Claude can help you find the strongest version of a skeptical reviewer's concern before you defend against it — but the methodological claim in your response must be verified against your actual data, not against Claude's draft.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `Here are Reviewer 2's comments — summarize the underlying concern, then draft a paragraph explaining why we used this methodology`
  - topic: `FACULTY WRITING · EDUCATION`   · segment: `Reviewer Response Scaffold`
  - greeting: `Habari`, Bear — Wagwan check: sum(ord(c) for c in "manuscript-reviewer-response") % 10 == 6 → Habari, Bear
- **spine:** B00 ASK → B01 organized response structure arrives → B02 the methodological claim must be verified → B03 Claude as adversarial reader → B04 COPE authorship rule → VERDICT → manuscript-reviewer-response outro
- **callouts (≤6):**
  - [B01] "The underlying concern" · Not what reviewer said — what they actually wanted · points at: summary output
  - [B02] "Acknowledge before defending" · Response structure: concern acknowledged first · points at: draft structure
  - [B03] "Verify against your data" · Claude drafts; you check whether the revision claim is actually true · points at: verification step
  - [B04] "COPE rule" · Responsible for all content regardless of AI assist · points at: authorship note
  - [B05] "Claude as adversarial reader" · Useful rehearsal — not a verdict on your methodology · points at: critique framing
- **register notes:** The "rehearsal not verdict" framing is the sharpest correction — academics often either under-trust AI critique or over-trust it; name the correct position.
- **est length:** 75s
