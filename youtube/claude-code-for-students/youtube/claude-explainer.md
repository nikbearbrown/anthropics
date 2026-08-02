# Claude Code for Students — Claude Explainer Candidates

## C01 — Gru's /v0 Gate: One Sentence or You Don't Build

- **slug:** gru-slash-v0-gate
- **source:** chapters/06-gru-tool.md §/v0 is the first command in the Gru sequence
- **premise:** Students skip /v0 and immediately type into Claude, building four things at once and calling them one — the gate forces the one-sentence commitment that makes scope real.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `/v0 I want to build an agent to help with Unity projects.`
  - topic: `GRU GATE · CAPS`   · segment: `One Sentence`
  - greeting: `Hola`, Bear — Wagwan check: sum(ord(c) for c in "gru-slash-v0-gate") % 10 == 1 → Hola, Bear
- **spine:** B00 ASK → B01 Gru refuses (three questions failed) → B02 second attempt: four "ands" exposed → B03 fourteen-minute pivot to one system → B04 why the sentence is the most expensive work → VERDICT: the gate's unhelpfulness is the feature → Gru's /v0 Gate outro
- **callouts (≤6):**
  - [B01] "All 3 failed" · No single system · No named user · No done-condition · points at: Gru refusal message
  - [B02] "4 'ands'" · Auditor, refactor agent · test generator, CLAUDE.md author · points at: second /v0 attempt
  - [B03] "14 min, no code" · Only artifact: 28-word sentence · Revealed: 3 scope mistakes · points at: passing /v0 sentence
  - [B04] "Essential vs. accidental" · Brooks: deciding what to build · is harder than building it · points at: the /v0 command in terminal
- **register notes:** Teardown judgment — the refusal mechanism is the real payload; don't oversell Gru as magic, land on "unhelpfulness is the feature." The one oversell risk: claiming /v0 is always 14 minutes — some users will knock it out in 2.
- **est length:** 75s

---

## C02 — Spec vs. Prompt: Same Claude, Different Login

- **slug:** spec-vs-prompt-live
- **source:** chapters/04-conducting-not-prompting.md §Attempt one: the prompt / Attempt two: the specification
- **premise:** "Write me a login function" gets MD5 hashes and a global dict; the same Claude 20 minutes later, with a spec, gets bcrypt, parameterized queries, and a clarifying question — the difference is entirely in what the human does first.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `write me a login function`
  - topic: `PROMPT VS. SPEC · CAPS`   · segment: `Same Claude`
  - greeting: `Olá`, Bear — Wagwan check: sum(ord(c) for c in "spec-vs-prompt-live") % 10 == 1 → Olá, Bear
- **spine:** B00 ASK (the bad prompt) → B01 Claude returns MD5 + global dict → B02 Seth almost commits → B03 ten-minute Gru part first → B04 eight-sentence spec → B05 Claude asks clarifying question → VERDICT: the spec is what you say after you decide → Spec vs. Prompt outro
- **callouts (≤6):**
  - [B01] "MD5 is broken" · Cryptographically broken · for password storage · since ~2010 · points at: hashlib.md5 in output
  - [B01] "Global dict" · Doesn't persist · across restarts · accepts empty string · points at: USERS dict
  - [B03] "4 min of Gru work" · Read 3 files · Name boundary · Write handoff condition · points at: spec writing block
  - [B05] "Claude asks first" · "Should token be stored?" · Not in attempt 1 · Spec unlocked the Q · points at: Claude's clarifying question
- **register notes:** Teardown judgment — land on "same model, different artifact" not "prompts are bad." The one oversell risk: making it seem like all specs prevent all bugs — the chapter is honest that bcrypt still needs a test.
- **est length:** 80s

---

## C03 — Rewind, Not Fix-Forward: The Andon Cord

- **slug:** rewind-not-fix-forward
- **source:** chapters/12-running-the-build.md §The condition fails. What now.
- **premise:** Appending a complaint to a failed prompt adds tokens to a context that already contains the misunderstanding — Esc-Esc rewinds both the conversation and the code to before the mistake, then you respecify.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `the toggle function isn't working on an empty array, please fix it`
  - topic: `REWIND LAW · CAPS`   · segment: `Andon Cord`
  - greeting: `Bonjour`, Bear — Wagwan check: sum(ord(c) for c in "rewind-not-fix-forward") % 10 == 5 → Bonjour, Bear
- **spine:** B00 ASK (forward-correction prompt) → B01 context now contains both failure + misunderstanding → B02 quality degrades with length (Liu 2025) → B03 Esc-Esc: conversation + code restored → B04 new prompt = old prompt + one constraint sentence → B05 tests pass → VERDICT: rewind is the cheapest move → Rewind outro
- **callouts (≤6):**
  - [B01] "Forward-correction" · Fixes symptom · leaves misunderstanding · compounds in context · points at: growing conversation thread
  - [B02] "Liu 2025 finding" · Quality degrades · monotonically with length · even with perfect retrieval · points at: context window bar chart
  - [B03] "Esc-Esc" · Restores to checkpoint · code on disk reverts · conversation wipes · points at: terminal command
  - [B04] "Diff = constraint" · Not a complaint sentence · One added invariant · "use immutable updates" · points at: diff between prompts
- **register notes:** Teardown judgment — the Toyota andon cord analogy is load-bearing; don't drop it. The oversell risk: students may think every rewind is free — name the two-rewind rule (third failure means the spec is broken, not the model).
- **est length:** 70s

---

## C04 — /clear vs. /compact: Context Window Hygiene

- **slug:** clear-vs-compact
- **source:** chapters/12-running-the-build.md §After any group of unrelated rows, /clear
- **premise:** Students keep typing into a filled context window wondering why quality drops — /clear wipes the conversation (safe because durable rules live in CLAUDE.md, not the chat), while /compact summarizes when the gist still matters.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `/context`
  - topic: `WINDOW HYGIENE · CAPS`   · segment: `Clear vs. Compact`
  - greeting: `Ciao`, Bear — Wagwan check: sum(ord(c) for c in "clear-vs-compact") % 10 == 5 → Ciao, Bear
- **spine:** B00 ASK (/context check) → B01 window at 78%, quality degrading → B02 /clear — what it wipes and what survives → B03 /compact — when the gist still earns its place → B04 why CLAUDE.md makes /clear safe → VERDICT: the conversation is not the build → /clear outro
- **callouts (≤6):**
  - [B01] "78% full" · Conversation: 48% · Build itself: 30% · 22% left · points at: /context output bar
  - [B02] "/clear" · Wipes conversation · code on disk survives · CLAUDE.md reloads · points at: clear command
  - [B03] "/compact focus on X" · Keeps gist · shrinks budget · use when history earns its place · points at: compact command
  - [B04] "Chat ≠ progress" · Code on disk = progress · Instructions in CLAUDE.md = progress · Chat = disposable infrastructure · points at: CLAUDE.md file
- **register notes:** Teardown judgment — the "kitchen counter" metaphor from the chapter is excellent; use it. Don't present /clear as failure — it's discipline. The one gap to name: /clear doesn't work mid-task if context is still load-bearing.
- **est length:** 65s

---

## C05 — Conducting, Not Prompting: The Gru/Minion Split

- **slug:** conducting-not-prompting
- **source:** chapters/04-conducting-not-prompting.md §The Minion Part / The Gru Part
- **premise:** The conductor on a small box doesn't play better than the cellist — she holds the piece; the orchestra can't; that exact division between deciding and executing is what separates a Claude session that ships from one that boondoggles.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `write me a sort function for students by GPA`
  - topic: `CONDUCTING · CAPS`   · segment: `Gru vs. Minion`
  - greeting: `Hallo`, Bear — Wagwan check: sum(ord(c) for c in "conducting-not-prompting") % 10 == 9 → Hallo, Bear
- **spine:** B00 ASK (vague sort prompt) → B01 Claude returns a sort (correct but Bell before Adams on tie) → B02 Gru lane: deciding, naming scope, writing handoff → B03 Minion lane: typing, editing, running tests → B04 the boondoggle defined (fluent activity, no verified output) → VERDICT: slow at start, real at end — Conducting outro
- **callouts (≤6):**
  - [B01] "Bell before Adams" · Spec said alphabetical on tie · Test set had no tie · Bug invisible until real data · points at: sort output with tied GPAs
  - [B02] "Gru lane" · Decides what's built · Names scope boundary · Writes handoff condition · points at: left column of Gru/Minion table
  - [B03] "Minion lane" · Typing · Editing named files · Running handoff condition · points at: right column
  - [B04] "Boondoggle" · Looks like work · Has deliverables · Nothing verified underneath · points at: etymological callout
- **register notes:** Teardown judgment — the conductor metaphor is the load-bearing image; commit to it fully. The risk of oversell: "Gru lane" could make students think they never type — clarify that typing specs IS the Gru work.
- **est length:** 72s

---

## C06 — Brutalist Three-File System: Who Owns the Creative Decisions

- **slug:** brutalist-three-file
- **source:** chapters/10-brutalist-creative-builds.md §The Brutalist framework is operationally three files
- **premise:** When Claude picks the palette, the chord progression, the essay register — the work is polished but belongs to nobody; three files written before Claude touches anything (CLAUDE.md, DESIGN.md, PROJECT.md) keep every aesthetic decision traceable to a human choice.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `write me a system prompt for a senior game designer agent`
  - topic: `BRUTALIST · CAPS`   · segment: `Three Files`
  - greeting: `Hej`, Bear — Wagwan check: sum(ord(c) for c in "brutalist-three-file") % 10 == 8 → Hej, Bear
- **spine:** B00 ASK (no files) → B01 Claude returns warm encouraging agent with 3 commands → B02 Nicholas: "you didn't design this, you received it" → B03 three files written (CLAUDE.md + DESIGN.md + PROJECT.md) → B04 same prompt → B05 Claude refuses once (path-forward rule gap), then proceeds → VERDICT: maximally informed, minimally autonomous → Brutalist outro
- **callouts (≤6):**
  - [B01] "Claude's defaults" · Warm persona · 3 commands (not 34) · Suggestions not refusals · points at: first build output
  - [B03] "DESIGN.md" · Every aesthetic named · Escalation list · Silence = ask human · points at: DESIGN.md excerpt
  - [B03] "PROJECT.md Intent Layer" · 5 Qs, human voice · Written before Claude sees anything · Cannot be delegated · points at: Intent Layer block
  - [B05] "Claude refused once" · Path-forward rule gap · Named the ambiguity · Seth answered, build proceeded · points at: refusal message in session
- **register notes:** Teardown judgment — the Copyright Office de minimis finding is the steel-man for why this matters; use it but don't lead with law. Land on "intent is authorship" as the frame.
- **est length:** 78s

---

## C07 — The Boondoggle Score: Labeling Who Does Each Step

- **slug:** boondoggle-score-anatomy
- **source:** chapters/06-gru-tool.md §The Boondoggle Score / chapters/11-planning-first-build.md §What the Score Tells You
- **premise:** Before writing a line, the Score table maps each build step to Claude-only, human-only, or Claude-with-review — and a score where every row says Claude-only is either trivial or dishonest.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `/boondoggle`
  - topic: `SCORE ANATOMY · CAPS`   · segment: `Who Does What`
  - greeting: `Hei`, Bear — Wagwan check: sum(ord(c) for c in "boondoggle-score-anatomy") % 10 == 7 → Hei, Bear
- **spine:** B00 ASK (/boondoggle command) → B01 Score table rendered (five rows, labor column) → B02 Step 3: formula choice → Human-only (essential complexity) → B03 Step 5: threshold → Human-only (domain judgment) → B04 "all Claude-only" failure mode → VERDICT: the Score is a prompt for your own judgment → Score outro
- **callouts (≤6):**
  - [B01] "5 columns" · Step / Phase / Who / Why / Handoff condition · points at: score table
  - [B02] "Essential vs accidental" · Claude eats accidental · Essential: deciding what to build · Brooks 1986 · points at: Step 3 row
  - [B03] "Human-only" · Threshold encodes judgment · Claude cannot supply domain judgment it doesn't have · points at: Step 5 row
  - [B04] "All Claude-only = lie" · Either trivial or · you handed over the human work · score is a detector · points at: warning callout
- **register notes:** Teardown judgment — the table is the visual anchor; don't let the reel become abstract. Land on "the Score cannot lie — you can write a vague SDD but you can't write a vague handoff condition without hearing the vagueness."
- **est length:** 68s

---

## C08 — Intent Layer: What the Copyright Office Cares About

- **slug:** intent-layer-authorship
- **source:** chapters/10-brutalist-creative-builds.md §PROJECT.md — the project state / §The Brutalist commitment
- **premise:** The Copyright Office's de minimis ruling on Théâtre D'Opéra Spatial says prompt iteration isn't authorship — the Intent Layer of PROJECT.md (five questions, human voice, written before Claude sees anything) is the documentary proof that a person decided what the work is for.
- **channel:** claude
- **ask beat (B00, COLD OPEN LAW — always the composer, never a brand card):**
  - command: `generate a PROJECT.md for my data visualization project`
  - topic: `INTENT LAYER · CAPS`   · segment: `Authorship Proof`
  - greeting: `Ahoj`, Bear — Wagwan check: sum(ord(c) for c in "intent-layer-authorship") % 10 == 4 → Ahoj, Bear
- **spine:** B00 ASK (letting Claude generate intent) → B01 Claude writes a plausible PROJECT.md → B02 Copyright Office 2023: de minimis — prompt iteration ≠ authorship → B03 Intent Layer structure (5 Qs, non-delegable) → B04 Claude can copy-edit it; Claude cannot generate it → VERDICT: intent is authorship; the document is the proof → Intent Layer outro
- **callouts (≤6):**
  - [B01] "Received, not made" · Polished surface · No trace of choosing · Could be anyone's project · points at: Claude-generated PROJECT.md
  - [B02] "de minimis" · U.S. Copyright Office · Sept 2023 ruling · 80h of iteration ≠ authorship · points at: ruling text excerpt
  - [B03] "5 Qs (human only)" · Who is this for? · What should they feel? · What does it refuse? · points at: Intent Layer template
  - [B04] "Claude can copy-edit" · Cannot generate the intent · Refusal when Intent Layer empty · points at: Brutalist refusal message
- **register notes:** Teardown judgment — don't become a legal lecture; the Copyright Office point is a hook, not the thesis. The thesis is operational: "if you can't answer the 5 Qs, you don't yet have a project."
- **est length:** 70s
