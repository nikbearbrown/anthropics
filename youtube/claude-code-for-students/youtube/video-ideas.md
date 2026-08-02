# Claude Code for Students Video Ideas

## Candidate 01 — Why Doing Homework With AI Makes You Worse at the Test
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/ai-homework-fluency-trap/ai-homework-fluency-trap-review.mp4`
- Source: `claude-code-for-students/chapters/01-homework-quiz-gap.md`
- Topic: CLAUDE CODE
- Hook: A student who scores 48% better on AI-assisted practice scores 17 points lower on the unassisted exam — and feels like they learned more, not less.
- Key case: D in AP CS finishes a six-function problem set in 18 minutes using Claude, gets a 100, then stares at an easier quiz for 12 minutes and scores a 41 — because the practice was done by Claude, not by D.
- The Question: Practice should predict exam performance. D's AI-assisted practice predicted higher performance. His exam score was dramatically lower. Why?
- Core idea: Cognitive struggle is not the price of learning — it is the mechanism of learning. When Claude removes the struggle, it removes the neurological events (error signals, synaptic adjustment) that consolidate skill; the output is produced but the capability never arrives.
- Visual object: Two parallel paths — Path A: struggle → consolidation → durable capability; Path B: delegation → fluent output → no consolidation → atrophy.
- Manim move: split
- Example seed: Maya pastes a sorting-algorithm problem into Claude, reads the clean solution, nods, moves on. 100 on the homework. Three weeks later, closed laptops. The quiz has the same algorithm in a slightly different context. Maya writes "for i in range..." crosses it out, sits still. The skill was never hers — it lived in Claude for 30 seconds and she handed it back.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: None — accessible to any high school student who has used an AI assistant.
- Exclusions: No deep neuroscience of synaptic plasticity; no formal statistics on effect size; no history of cognitive-load theory; no Bjork's full desirable-difficulties taxonomy.
- Score: 10/10

---

## Candidate 02 — Why the Code Runs Fine and Still Ships Wrong
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/code-runs-ships-wrong/code-runs-ships-wrong-review.mp4`
- Source: `claude-code-for-students/chapters/02-division-of-labor.md`
- Topic: CLAUDE CODE
- Hook: Claude produces a sort function that compiles, passes tests, and quietly returns the wrong order the moment real data contains a tie — and Claude's own audit says it looks fine.
- Key case: Seth writes a GPA-ranking function. Claude returns a tuple-sort key `(-gpa, last_name)`. All test rows have unique GPAs. The sort looks correct. Seth nearly ships. He adds one tie-case: Bell ranks above Adams on equal GPA. The spec said alphabetical. The bug was invisible until the edge case.
- The Question: A working sort function should pass an audit of itself. Claude's function passed every test and passed Claude's own review. Why did it still ship the wrong order?
- Core idea: Claude's audit has the same architecture as Claude's production — the same weights that wrote the bug are the only weights available to check it. Independent verification requires a process with access to something Claude cannot see: the spec that lives in the developer's head.
- Visual object: Two lines on a graph — Claude's solve speed rising steeply over time, human verification capacity roughly flat. The gap between them is widening.
- Manim move: transform
- Example seed: Priya builds a leaderboard for a school quiz app. Claude sorts by score descending. All 12 test rows have unique scores. Deploy. A week later two students tie at 94 — Zhao ranks above Amir, but the spec says alphabetical on ties. Priya finds out because Amir's parent emails the teacher. The bug was in the code the day it was written. No test caught it because the test set had no ties.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic familiarity with what a function is and what a test does.
- Exclusions: No formal proof theory; no full taxonomy of LLM hallucination types; no Copilot vulnerability statistics; no discussion of retrieval-augmented generation as a fix.
- Score: 9/10

---

## Candidate 03 — Why "Write Me a Login Function" Is Not a Prompt
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/prompt-is-a-wish-spec-is-a-contract/prompt-is-a-wish-spec-is-a-contract-review.mp4`
- Source: `claude-code-for-students/chapters/04-conducting-not-prompting.md`
- Topic: CLAUDE CODE
- Hook: One sentence produces a function that hashes passwords with MD5 — broken for a decade. Six sentences produce a function Seth puts his name on.
- Key case: Seth asks Claude "write me a login function." 11 seconds later: a 12-line function using MD5, storing users in a global dict, accepting empty strings, with no session token. It runs. He almost commits. Same day, same Claude, six sentences of spec: bcrypt, parameterized queries, identical error strings for security, token with expiry. Claude asks one clarifying question Seth hadn't thought to ask. Five tests pass.
- The Question: A prompt should specify the task clearly enough to get the right output. "Write me a login function" is a clear request. Why did it produce a function that would fail in production?
- Core idea: A prompt is a wish — it delegates to Claude's training distribution. A specification is a contract — it names the invariants, the boundary, the success criterion, leaving Claude nothing to fill in that wasn't authorized. Same model; different artifact.
- Visual object: Two columns on a whiteboard: on the left, one-sentence "prompt" with arrows pointing to six different possible outputs; on the right, a six-element "specification" with one arrow pointing to exactly one output.
- Manim move: compare
- Example seed: Tomas is building a personal study tracker. He asks Claude "add a login." Claude returns a function storing passwords in plaintext in a Python dict. Tomas reads it, it looks like a login. He takes 8 minutes to write a spec: bcrypt, SQLite, session token, identical failure strings. Same Claude returns a 30-line function with every security property named. Tomas can defend every line.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Viewer has used Claude or another AI assistant to write code at least once.
- Exclusions: No OAuth flows; no full security audit methodology; no prompt engineering "tricks" or jailbreaks; no history of password-hashing algorithms.
- Score: 9/10

---

## Candidate 04 — Why the Student Who Knows More Than the Teacher Is in the Most Danger
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/fluency-trap-danger-zone/fluency-trap-danger-zone-review.mp4`
- Source: `claude-code-for-students/chapters/03-teacher-student-ai-gap.md`
- Topic: CLAUDE CODE
- Hook: The student who runs Claude more fluently than his teacher is also less able to catch Claude's mistakes — and his teacher, who could catch them, is not in the loop.
- Key case: The night before an AP Chemistry test, Seth asks Claude to explain Le Chatelier's principle for inert gas at constant volume. Claude's answer is mostly correct — one sentence in the middle quietly merges the constant-volume and constant-pressure cases. Seth reads it at midnight, nods, closes the tab. On the test, he writes the right answer with a justification that smears both cases together. He loses most of the explanation points.
- The Question: Technical fluency should make AI tools safer to use. Seth can run Claude better than his teacher. Yet he got a worse answer than he would have gotten by reading the textbook. Why?
- Core idea: Technical fluency (operating the tool) and domain depth (evaluating the output against the world) are different skills that don't transfer between each other. Claude sounds authoritative in every domain; you have depth in only a few. The gap between "sounds right" and "is right" is exactly where the harm lives — and the teacher who could close it isn't in the room.
- Visual object: A two-axis quadrant: horizontal = technical fluency (low → high), vertical = domain depth (low → high). Teacher sits in low-fluency / high-depth. Student sits in high-fluency / low-depth — marked as the danger zone.
- Manim move: scan
- Example seed: Jada is writing a history essay with Claude's help. Claude cites a secondary source fluently. Jada has high fluency — she knows how to prompt, she knows Claude sometimes hallucinates — but she hasn't yet read primary sources on this period. The citation sounds real. She includes it. The teacher marks it incorrect. The citation never existed. Jada could operate the tool. She couldn't evaluate the output.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: None — general audience who has used any AI assistant.
- Exclusions: No institutional AI policy debate; no discussion of specific school regulations; no deep dive into hallucination rates by model; no history of tool-use in education.
- Score: 9/10

---

## Candidate 05 — Why String Similarity Is Not Semantic Equivalence (and How to Catch the Difference Before You Ship)
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/string-similarity-semantic-gap/string-similarity-semantic-gap-review.mp4`
- Source: `claude-code-for-students/chapters/05-five-supervisory-capacities.md`
- Topic: CLAUDE CODE
- Hook: A classifier scores 85% accuracy on 12 test pairs and 0.93 similarity between "hunting" and "haunting" — two NPC states that are completely different in the game.
- Key case: Seth builds a tag-normalizer for Haunt & Harvest — a Python function using `difflib.SequenceMatcher` with a 0.7 threshold. 12 test pairs, 85% accuracy, all pass. He almost ships. An itch makes him type one more pair: `("hunting", "haunting")`. The function returns 0.93. "Hunting" means the ghost is actively chasing a player. "Haunting" is the ambient-presence tag. Claude wrote tests for what the function does. Seth wrote a probe for what he actually needed.
- The Question: An 85%-accurate classifier should be reliable enough to review. All 12 tests passed. Why was it not ready to ship?
- Core idea: Tests verify the problem Claude solved — not the problem you needed to solve. The function did exactly what the spec said (string similarity). The spec was the wrong frame. Plausibility auditing is the capacity to hear the wrong note before any test confirms it — and it only works if you bring domain knowledge Claude doesn't have.
- Visual object: A single text pair on screen: "hunting" ↔ "haunting" with a similarity score of 0.93 in red, vs. a semantic diagram showing them in completely different behavior-tree branches.
- Manim move: compare
- Example seed: Leila is building a quiz-answer grader. Claude uses fuzzy string matching. All 10 test answers pass. She runs one more: student wrote "photosynthesis" — the correct answer is "cellular respiration." Similarity score: 0.67 — above the threshold. The grader marks it correct. String similarity doesn't know biology. Leila's domain knowledge does.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic familiarity with what a function and a test are.
- Exclusions: No full NLP embedding methodology; no semantic similarity model comparisons; no formal taxonomy of NLP tasks; no Polanyi's epistemology at length.
- Score: 9/10

---

## Candidate 06 — Why the Most Dangerous Claude Output Is the One That Passes Every Test
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/pagination-bug-dangerous-middle/pagination-bug-dangerous-middle-review.mp4`
- Source: `claude-code-for-students/chapters/09-handoff-conditions-dangerous-middle.md`
- Topic: CLAUDE CODE
- Hook: Seth's pagination function compiles, passes all tests, and silently drops the 251st item from Avery's inventory — because every test was a multiple of 50.
- Key case: Seth writes a `get_page` function for Haunt & Harvest inventory pagination. Tests: page 1 of 50 returns 50 items, page 2 of 100 returns items 51–100, 247 items paginate cleanly 4 pages of 50 plus one of 47. All pass. Six days later Avery joins a session with 251 items. The calling loop uses `while page.size() == size` as its termination condition. Page 5 returns 50 items — loop stops. The 251st item — a flashlight — disappears from Avery's client. The bug took 40 minutes to find. The handoff condition that would have caught it was never written.
- The Question: A test suite that passes all cases should confirm correctness. Every pagination test passed. Why did a session with 251 items fail in production?
- Core idea: The dangerous middle is the region where code compiles, passes, looks right, and is wrong in a way you weren't equipped to see — because the test set only covered the "obvious" cases. A handoff condition written before the step runs names the non-obvious case (total = page_size × n + 1) that exposes the bug; a condition written after rationalizes the artifact that already exists.
- Visual object: A number line of inventory sizes: multiples of 50 are colored green (tests pass), 251 is colored red (bug fires) — with an arrow pointing at exactly the gap between 250 and 251.
- Manim move: accumulate
- Example seed: Priya builds a paginated leaderboard for her school's quiz app. She tests page 1 of 20, page 2 of 40. All pass. She deploys. A tournament ends with 41 players. The 41st player — ranked 41st — never appears on any page. Her test set was all multiples of 20. The handoff condition she needed: "given total = page_size × 3 + 1, the final page returns exactly 1 entry and the loop terminates."
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Basic familiarity with loops and pagination concepts.
- Exclusions: No formal Hoare-triple proof notation; no security vulnerability taxonomy (slopsquatting covered in separate candidate); no full discussion of property-based testing frameworks.
- Score: 9/10

---

## Candidate 07 — Why AI Creative Work Is Beautiful and Belongs to Nobody
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/ai-creative-work-belongs-to-nobody/ai-creative-work-belongs-to-nobody-review.mp4`
- Source: `claude-code-for-students/chapters/10-brutalist-creative-builds.md`
- Topic: CLAUDE CODE
- Hook: A piece of AI-assisted art wins a blue ribbon at a state fair, then the Copyright Office rules the human author contributed too little to own it.
- Key case: Jason Allen iterates 624 times on a Midjourney prompt, post-processes in Photoshop, spends 80 hours — and wins first prize at the Colorado State Fair. He files for copyright. The U.S. Copyright Office Review Board rules in September 2023: the human authorship was "de minimis." The 80 hours of prompt iteration, by the Office's analysis, did not constitute authorship of the resulting image.
- The Question: 80 hours of creative work should constitute authorship. Allen iterated hundreds of times, chose, refined, post-processed. The Copyright Office ruled he did not author the work. Why?
- Core idea: AI tools have aesthetic defaults — a particular register, palette, rhythm drawn from their training distribution. When the human does not contest these defaults in writing (in a DESIGN.md, a CLAUDE.md, an intent document), the model makes every micro-decision, and "the work" is the model's aggregate, not the human's choices. Authorship requires decisions, not iterations on a model's proposals.
- Visual object: Three nested boxes labeled: outer = CLAUDE.md (what the work is made of), middle = DESIGN.md (what it looks like), inner = PROJECT.md INTENT LAYER (what it is for — written by the human, never the model).
- Manim move: split
- Example seed: Marcus pastes a prompt into an AI image tool for his school's literary magazine cover. He picks from eight options, asks for variations, picks again. Two hours later he has a polished cover image. A classmate asks why the palette is blue. Marcus shrugs — the model picked it. Why is the layout centered? The model decided. The cover looks professional and belongs to nobody in particular.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: General familiarity with AI image tools; no coding required.
- Exclusions: No deep copyright law history; no Midjourney legal case details; no full Brutalist framework spec; no history of conceptual art (LeWitt, Ono); no aesthetic theory.
- Score: 8/10

---

## Candidate 08 — Why Slopsquatting Turns Claude's Wrong Answer Into a Security Hole
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/slopsquatting-hallucinated-package/slopsquatting-hallucinated-package-review.mp4`
- Source: `claude-code-for-students/chapters/05-five-supervisory-capacities.md`
- Topic: CLAUDE CODE
- Hook: Claude imports `requests_oauth_helper` — a package that didn't exist until an attacker registered it after seeing models repeatedly hallucinate the name.
- Key case: Across 576,000 code samples from 16 language models, researchers found that 58% of hallucinated package names recur across queries. An attacker mines the common hallucinations, registers the popular names on PyPI with malicious code, and waits. The student runs `pip install requests_oauth_helper` on Claude's say-so — the install succeeds, the tests pass, and the attacker's code runs with the student's permissions.
- The Question: A student running `pip install` on a Claude-suggested package should be safe if the package exists. The package exists — an attacker put it there. Why does the install succeed and execute malicious code?
- Core idea: Hallucinated package names are predictable and repeatable — 58% of them recur. Attackers can mine the common hallucinations in advance, register those exact names, and the student's install succeeds against the wrong package. The defense is cheap: verify every package name against the real registry before installing, never let Claude's suggested import be the only source of truth.
- Visual object: Three-step diagram: (1) model hallucinates package name → (2) attacker registers that name on PyPI → (3) student runs `pip install`, gets attacker's code. The loop closes silently.
- Manim move: trace
- Example seed: Fatima asks Claude to help her process OAuth tokens. Claude writes `import requests_oauth_helper`. She runs `pip install requests_oauth_helper`. It installs without error. She runs her script. In the background, the package exfiltrates her environment variables to an external server. She has no idea. The import line was the only check she ran.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Viewer has used `pip install` or `npm install` at least once.
- Exclusions: No full supply-chain security methodology; no deep dive into PyPI moderation policy; no formal threat-modeling framework; no comparison across package ecosystems.
- Score: 8/10

---

## Candidate 09 — Why the Build Passes Its Tests and Fails Its User
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/tests-pass-user-fails/tests-pass-user-fails-review.mp4`
- Source: `claude-code-for-students/chapters/13-verification.md`
- Topic: CLAUDE CODE
- Hook: Nine of nine tests pass. The application tracker is "done." Then Seth reads the SDD aloud and sees that the user need for "at a glance" fails — because insertion order scatters submitted and unsubmitted apps together.
- Key case: Seth finishes Phase 1 of his college application tracker. Nine tests pass, the page loads, persistence works. He re-reads the SDD user needs section aloud against the running build. Sentence: "The user should be able to see at a glance which applications remain to submit and which are already in, without scrolling." Six applications, submitted ones scattered in insertion order. With 20 applications across November–January, "at a glance" fails. The test suite was structurally incapable of catching it — because no test in the suite tests for the user need, only for the code behavior.
- The Question: A test suite passing all cases should confirm the build works. Nine tests passed. Why did the build fail the user?
- Core idea: Tests verify code against tests. A build is done when it passes the needs the SDD named — a strictly larger claim. The gap is Pass 3: reading user-need sentences aloud against the running build, using eyes and judgment, not a test runner. Some needs can't be tested — they have to be experienced.
- Visual object: Three stacked verification passes — Pass 1 (functional, green), Pass 2 (edge cases, green), Pass 3 (SDD needs, red) — with a branch from Pass 3 to "fix code" that loops back to Pass 1.
- Manim move: accumulate
- Example seed: Dani builds a library book checkout app for her school. 12 tests pass — adding a book, removing, checking out. She submits. A teacher opens it and can't tell which books are currently checked out vs. available without reading every row. The SDD said "librarian can see at a glance what's available." No test tested "at a glance." Dani had verified the code. She hadn't verified the need.
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: Viewer has written or used tests for code at least once.
- Exclusions: No formal Hoare-triple notation; no ISO/IEC 25010 standard detail; no Therac-25 or Mars Climate Orbiter history; no mutation-testing tooling tutorial.
- Score: 8/10

---

## Candidate 10 — Why the One-Sentence Problem Statement Is the Most Expensive Thing You Write
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/claude-code-for-students/youtube/one-sentence-problem-statement/one-sentence-problem-statement-review.mp4`
- Source: `claude-code-for-students/chapters/06-gru-tool.md`
- Topic: CLAUDE CODE
- Hook: Seth spends 14 minutes on one sentence — and discovers he was about to build four projects at once, one of which had no valid inputs yet.
- Key case: Seth opens Gru and types `/v0 An agent that audits Unity scripts and refactors them and writes the missing tests and generates a CLAUDE.md.` Gru refuses: the sentence describes four systems. Seth stares at the screen. He realizes he had thought he was building one thing. He stares for several minutes, decides which one he actually wants, and types: `/v0 A senior-architect agent that audits a Unity developer's C# project and produces a five-phase refactor plan with named hotspots, so the developer can decide which file to restructure next.` The whole interaction took 14 minutes. No code. The most valuable 14 minutes of the build.
- The Question: A one-sentence description should be easy to write — it's just a sentence. Seth had been thinking about this project for three days. Why did it take 14 minutes and two refusals to produce one valid sentence?
- Core idea: The one-sentence constraint is not about writing style — it is an elevator test for whether you know what you're building. A sentence with multiple "ands" is multiple projects disguised as one; the refusal forces the decision that the list of features was deferring. The sentence that passes is the moment you take ownership of the project's conceptual integrity.
- Visual object: A single sentence with two conjunctions highlighted in red, each "and" branching into a separate project box — four boxes from one sentence. Then the revised sentence with one box.
- Manim move: split
- Example seed: Omar wants to build a study tool. He types: "An app that makes flashcards and schedules reviews and tracks which subjects need more time and sends reminders." A tool with that description is four tools. He has to choose. He cuts three things he actually wants. He writes: "A local flashcard app that shows me the one card I'm most likely to forget today." That sentence passes. He has a project.
- Length band: 1 min
- Still lanes: geo
- Prerequisites: None — accessible to anyone who has started a project and let it grow.
- Exclusions: No full Gru command syntax; no Brooks' Mythical Man-Month history; no formal requirements-engineering methodology; no discussion of arc42 or ADR templates.
- Score: 8/10
