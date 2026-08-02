# INFO 5100: Application Engineering and Development — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a CLAUDE.md File with Claude: Define What AI May and May Not Do in Your Project

- Source: info-5100-application-engineering-and-development/chapters/95-claude-code.md  (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A CLAUDE.md that says "help me with Java" is not a design document — it is evidence that the process was not visible. A useful CLAUDE.md states what Claude may do, what it may not do, and what evidence you must produce before accepting generated code.
- The artifact: a CLI session that generates a specific, project-tailored CLAUDE.md for the INFO 5100 library domain (Patron, Book, Loan), using the three-item pre-ask structure (Requirement / Artifact / Evidence) and the module-level phase-gate ladder. The terminal shows the prompt → output → human revision cycle.
- Prompt seed: `claude "Generate a CLAUDE.md file for a graduate Java student in INFO 5100 building a library management application (domain: Patron, Book, Loan). The file must: (1) State what Claude may do as tutor (explain errors, quiz on existing code), as reviewer (find responsibility leaks), as scaffold builder (generate class stubs from specifications the student provides), as second reader (find inconsistencies). (2) State what Claude may NOT do (decide domain model, choose security behavior, select persistence policy). (3) Include the Module 4 phase gate: Claude may not identify the bug — the student must provide symptom, suspected cause, isolation evidence, and next step to check before Claude assesses. (4) State the three-question audit the student must answer before accepting any generated component. Format as a markdown file."`
- Read / check: Verify the four roles (tutor, reviewer, scaffold builder, second reader) match the chapter. Check that the phase gate text for Module 4 (debugging) is specific — "Claude does not identify the bug" is the key constraint. Confirm the three-question audit matches: explain the component without Claude's words, explain why designed this way including the alternative rejected, trace non-trivial behavior to a test or an explicit reason.
- Human supplies (Claude can't): The student's own domain model — the CLAUDE.md must be specific to the student's application, not generic. For the video demo, the library domain is used. The student writes the final CLAUDE.md for their own project from scratch.
- Output medium: screen-recording mp4 (terminal showing the prompt → CLAUDE.md output → the human revising two fields to match their specific application → saving the file)
- The change: Add the Module 6 (authentication) gate to the CLAUDE.md — "Claude must not generate authentication logic before the student states the threat model: 'if someone reads my user data file, what can they do?'"
- Teardown angle: The CLAUDE.md serves two purposes: it shapes Claude's behavior AND forces the student to articulate what they own. A student who cannot write a specific CLAUDE.md does not yet understand their application well enough to defend it.
- Exclusions: Java IDE configuration, project scaffolding beyond CLAUDE.md, specific JavaFX or Maven setup.
- Score: 9/10

---

## Candidate 02 — Build the Three-Item Pre-Ask with Claude: Require-Artifact-Evidence Before Any Code Generation

- Source: info-5100-application-engineering-and-development/chapters/95-claude-code.md  (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: When the Requirement / Artifact / Evidence are missing, Claude guesses. The guess will be fluent. That is the danger. Three sentences take three minutes and protect the difference between code you understand and code you accepted.
- The artifact: a Python CLI tool (~25 lines) that enforces the pre-ask structure: prompts the user for Requirement (what should the program do?), Artifact (where should that behavior live — name the class, method, or handler), and Evidence (what would prove the answer is acceptable — specific, not "it runs"). Only after all three fields are filled does the tool construct and send the Claude prompt. The terminal screen-recording shows the tool blocking an empty Evidence field.
- Prompt seed: `claude "Write a Python CLI tool called 'prask' that enforces the INFO 5100 pre-ask structure before sending a prompt to Claude. The tool: (1) prompts the user for Requirement (one sentence: what should the program do?), (2) prompts for Artifact (name the class, method, or handler where the behavior should live — reject if blank), (3) prompts for Evidence (what would prove the answer is acceptable — must be longer than 20 characters, reject 'it runs' or 'it works'), (4) constructs a formatted prompt: 'Requirement: [R]\nArtifact: [A]\nEvidence: [E]\n\nGenerate [A] that satisfies [R]. Include what I must verify before accepting it.' (5) prints the prompt to stdout (do not call an API — just print the prompt for paste). Keep under 30 lines."`
- Read / check: Verify that the Evidence validation rejects "it runs" and "it works" and requires >20 characters. Check that the constructed prompt includes the "what I must verify" clause — this is load-bearing. Confirm the tool is actually ~25–30 lines (the chapter says the pre-ask takes three minutes and should be minimal friction).
- Human supplies (Claude can't): The real requirement, artifact, and evidence from the student's actual project. The video demo uses the checkout transaction example from the chapter.
- Output medium: screen-recording mp4 (terminal: tool prompts for three fields → student enters them → attempts to leave Evidence blank → tool rejects → student fills it → formatted prompt appears)
- The change: Add a fourth field: "Module phase gate" — what phase of the course is this? If Module 4 (debugging), add a constraint that the student must have provided symptom and hypothesis before the tool will proceed.
- Teardown angle: The tool doesn't make you smarter. It forces three minutes of thinking that the fluency of the IDE makes it easy to skip. Three minutes of owned specification prevents hours of accepted code that doesn't hold up in defense.
- Exclusions: Claude API integration (the tool prints to stdout for paste), full course grading rubric, Java environment setup.
- Score: 9/10

---

## Candidate 03 — Build an AI Use Disclosure Generator with Claude: Turn a Vague Acknowledgment into Evidence

- Source: info-5100-application-engineering-and-development/chapters/95-claude-code.md  (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: "I used Claude to help with the code" is a confession that the process is not visible. A useful disclosure names the task, the prompt, what Claude contributed, what the student changed or rejected and why, and how they verified the accepted part. The generator enforces the format.
- The artifact: a Python CLI tool that takes user inputs (task, prompt text, Claude contribution, what was rejected and why, verification method) and generates a formatted AI use disclosure in the course's required format. A second mode reads a list of past disclosures and flags any that are too vague (under 50 words, missing "rejected" field, missing verification method).
- Prompt seed: `claude "Write a Python CLI tool called 'disclose' with two modes: (1) 'disclose new' — prompts for: task (what were you asking Claude to help with), prompt (the exact text you used), contribution (what Claude produced that you kept), rejected (what you changed or rejected and why — required, error if blank), verification (how you verified the accepted part — required, error if 'none' or 'it runs'). Outputs a formatted disclosure block. (2) 'disclose check [file]' — reads a text file of past disclosures, flags any that are fewer than 60 words, missing the word 'rejected', or missing the word 'verified'. Print the flag with the disclosure text. Keep under 50 lines."`
- Read / check: Verify that the "rejected" field is truly required and that leaving it blank produces an error (not a default). Check that "check" mode correctly flags the "I used Claude to help with the code" type disclosure (too short, no "rejected", no "verified"). Confirm the output format matches the chapter's example disclosure.
- Human supplies (Claude can't): Real interaction data — the student must actually use Claude on their project and report honestly on what they rejected. The video demo uses the Module 9 example from the chapter (test cases for Catalog.searchByTitle).
- Output medium: screen-recording mp4 (terminal: new-mode prompts → student attempts to leave "rejected" blank → error → fills it → disclosure appears; then check-mode flags a vague disclosure)
- The change: Add a third mode: "disclose summary" — reads all disclosures for the project and generates a one-page AI Use Summary that the student can include in their final project submission.
- Teardown angle: The disclosure serves two purposes: it proves to the instructor that the process was visible, and it forces the student to notice any place where they accepted without verifying. If you cannot fill in "what I changed or rejected," you probably accepted everything.
- Exclusions: LMS submission integration, plagiarism detection tool comparison, academic honesty policy details.
- Score: 8/10

---

## Candidate 04 — Build a Java Class Responsibility Auditor with Claude: Find Responsibility Leaks Before Defense

- Source: info-5100-application-engineering-and-development/chapters/03-objects-and-classes.md + 95-claude-code.md
- Lane: BUILD (Claude Code)
- Hook: Before the final project defense, the examiner will ask: "What does this component do, why did you design it this way, and what would you change?" A responsibility audit finds the leaks — where one class is doing work that belongs to another — before the examiner does.
- The artifact: a CLI tool (Python, ~35 lines) that takes a directory of Java .java files, extracts class and method names using simple text parsing, sends them to Claude with a structured reviewer prompt, and outputs a markdown report flagging potential responsibility leaks (classes with >5 methods that span unrelated domains, public fields that should be private, methods that reference foreign class data directly).
- Prompt seed: `claude "You are a Java OOP responsibility auditor. I will give you a list of Java class names and their method signatures from a project. For each class: (1) identify any methods that seem to perform work belonging to a different class (responsibility leak), (2) flag public fields that should be private, (3) flag methods with more than 3 parameters that might indicate a missing abstraction. Format as a markdown list with: class name, finding type (leak/field/overloaded), specific method/field, and a one-sentence explanation of why this belongs elsewhere. Do not rewrite the code — only identify the issues. Here are the classes: [CLASS LIST]"`
- Read / check: Verify that the parser correctly extracts method signatures from standard Java (the parsing step can be fragile — check it handles common patterns like @Override, constructors, and static methods). Confirm that Claude's findings reference the specific method/field names provided, not generic Java advice. Watch for Claude confusing helper methods with responsibility leaks.
- Human supplies (Claude can't): The actual Java project files (student's own code). The video demo uses the INFO 5100 library domain (Patron.java, Book.java, CheckoutTransaction.java, Catalog.java). Real project files are required for an authentic audit; synthetic stand-in classes are acceptable for the video.
- Output medium: screen-recording mp4 (terminal: the tool parsing the .java files → extracting signatures → sending to Claude → markdown audit report appearing)
- The change: Run the audit on the same codebase after the student fixes the three flagged issues — show a "before and after" comparing the audit reports.
- Teardown angle: A responsibility leak is not a syntax error. It doesn't prevent compilation. It prevents the student from answering the examiner's second question — "why did you design it this way?" — because they did not decide. Claude decided, and they accepted.
- Exclusions: Full design pattern analysis, UML generation, automated refactoring.
- Score: 8/10

---

## Candidate 05 — Build a Recursion Tracer with Claude: Watch the Call Stack Unwind on Factorial and Fibonacci

- Source: info-5100-application-engineering-and-development/chapters/12-recursion.md
- Lane: BUILD (Claude Code)
- Hook: Recursion is easy to memorize and hard to understand. The difference between understanding and memorizing shows up when you try to debug it. A call-stack visualizer makes the unwind visible.
- The artifact: a Python/Manim script that generates an animated call-stack visualization for recursive factorial(5): boxes appear on the stack as calls go deeper (factorial(5) → factorial(4) → … → factorial(0)), then a "base case reached" flash, then boxes pop off the stack from bottom to top with the return value propagating up. The final frame shows the complete return chain and the result.
- Prompt seed: `claude "Write a Manim Python script that animates a recursive call stack for factorial(5). Animate in two phases: (1) Push phase: boxes appear one at a time from top to bottom — factorial(5) calls factorial(4) calls factorial(3) calls factorial(2) calls factorial(1) calls factorial(0). Each box shows the function name and current n value. A connecting arrow points down. (2) Pop phase: starting from factorial(0) = 1, boxes disappear from bottom to top, with a return value label propagating upward — factorial(0) returns 1, factorial(1) returns 1×1=1, factorial(2) returns 2×1=2, factorial(3) returns 3×2=6, factorial(4) returns 4×6=24, factorial(5) returns 5×24=120. Highlight the base case box in green when reached."`
- Read / check: Verify the factorial values are correct: 0!=1, 1!=1, 2!=2, 3!=6, 4!=24, 5!=120. Check that the pop phase correctly shows the return value propagating (not the argument propagating). Confirm the base case (n=0) is highlighted distinctly from the recursive cases.
- Human supplies (Claude can't): Nothing — fully synthetic. The factorial call stack is deterministic and requires no runtime data capture. The Manim scene is generated entirely from the known recursion trace.
- Output medium: Manim (push phase animation → base case flash → pop phase with return values propagating upward → final result displayed)
- The change: Add a second animation for Fibonacci(5) — showing the branching tree structure (two recursive calls per frame) and the exponential stack growth, contrasted with the linear factorial stack.
- Teardown angle: The call stack is not an abstract concept — it is a concrete data structure the JVM maintains at runtime. Watching it push and pop makes the stack-overflow error comprehensible: it is not a mystery, it is a pile of boxes that got too tall.
- Exclusions: Tail recursion optimization, memoization vs. recursion tradeoffs, heap vs. stack memory architecture.
- Score: 8/10

---

## Candidate 06 — Build an ArrayList vs. LinkedList Race with Claude: Animate Operation Costs at Scale

- Source: info-5100-application-engineering-and-development/chapters/14-lists-stacks-queues-and-the-final-project.md + 13-collections-and-iterators.md
- Lane: BUILD (Claude Code)
- Hook: ArrayList and LinkedList both implement List. But get(i) is O(1) for ArrayList and O(n) for LinkedList — and add(0, x) is O(n) for ArrayList and O(1) for LinkedList. The tradeoff is invisible until you measure it at scale.
- The artifact: a Python script that simulates ArrayList vs. LinkedList operation costs (using Python lists as analogies), runs 1000 iterations of random-access get() and front-insertion add(0, x) on sizes N from 100 to 10,000, and produces two animated Manim curves: get() time vs. N (ArrayList flat, LinkedList linear) and add(0,x) time vs. N (ArrayList linear, LinkedList flat).
- Prompt seed: `claude "Write a Python benchmarking script that simulates ArrayList vs LinkedList operation costs. Use Python list as ArrayList analog and collections.deque as LinkedList analog. For N in [100, 500, 1000, 2000, 5000, 10000]: (1) time 1000 random-access reads (list[random index]) vs. deque traversal to the same index; (2) time 1000 front insertions (list.insert(0, x)) vs deque.appendleft(x). Record times. Then write a Manim script that animates two curves growing as N increases: get() time (ArrayList flat, LinkedList linear) and add-front() time (ArrayList linear, LinkedList flat). Use contrasting colors. Label the crossover insight."`
- Read / check: Verify that the benchmark results show the expected asymptotic behavior (ArrayList get O(1), LinkedList get O(n), ArrayList insert(0) O(n), LinkedList insert O(1)). Check that the Manim curves are smooth (not noisy from system load) — run with averaged iterations. Confirm the deque.appendleft correctly models a LinkedList prepend (not an ArrayList insert).
- Human supplies (Claude can't): Nothing — fully synthetic benchmark. The asymptotic behavior is mathematically guaranteed; the chart shows what it looks like in practice. A real Java benchmark would be more authentic but is not required for the conceptual lesson.
- Output medium: Manim (two panels: left shows get() curves, right shows add-front() curves; both animate as N grows from 100 to 10,000; a callout appears at the crossover: "Choose based on your dominant operation")
- The change: Add a third operation: iterate() — show that both structures are O(n) for full traversal, so iteration doesn't distinguish them.
- Teardown angle: The tradeoff is not about which is "faster." It is about which operation dominates your use case. The student who picks ArrayList for a queue (front-heavy insertions) and LinkedList for random-access lookup has chosen wrong — but the choice is invisible without the chart.
- Exclusions: HashMap vs. TreeMap comparisons, memory allocation mechanics, Java Collections Framework API history.
- Score: 8/10

---

## Candidate 07 — Build a JavaFX fx:id Mismatch Detector with Claude: Catch the Silent Runtime Failure

- Source: info-5100-application-engineering-and-development/chapters/12-recursion.md (the FXML/fx:id content in this chapter despite the naming)
- Lane: BUILD (Claude Code)
- Hook: You rearrange the FXML layout in Scene Builder. The checkout button does nothing. The book table is empty. No compile error — just silent failure at runtime because the fx:id names no longer match the @FXML fields. This tool catches it before you run.
- The artifact: a Python CLI tool (~30 lines) that takes an FXML file path and a Java controller file path, extracts all fx:id values from the FXML (regex on `fx:id="..."`) and all @FXML field names from the controller (regex on `@FXML` annotations), and reports: (1) fx:ids in FXML with no matching @FXML field (dangling), (2) @FXML fields with no matching fx:id (orphaned). Outputs a human-readable mismatch report.
- Prompt seed: `claude "Write a Python script called 'fxcheck.py' that takes two arguments: --fxml [path to .fxml file] and --controller [path to Java controller .java file]. The script: (1) parses the FXML file and extracts all fx:id values using regex (fx:id=\"([^\"]+)\"). (2) parses the Java controller file and extracts all @FXML annotated field names using regex (match the line after @FXML that contains the field declaration, extract the variable name as the last word before the semicolon). (3) reports: 'Dangling fx:ids (in FXML, not in controller): [list]', 'Orphaned @FXML fields (in controller, not in FXML): [list]', 'Matched: [count] connections'. Keep under 35 lines."`
- Read / check: Verify the regex patterns are robust enough to handle common JavaFX patterns (fx:id with surrounding whitespace, @FXML on its own line vs. inline, field declarations with generics like `@FXML TableView<Book> bookTable`). Test on the library domain FXML from the chapter. Check that the report format is clear enough to act on immediately.
- Human supplies (Claude can't): Real FXML and Java controller files from the student's project. The video demo uses the library checkout screen from the chapter. Real files are required for an authentic demo; synthetic stand-ins are acceptable for the video.
- Output medium: screen-recording mp4 (terminal: fxcheck.py runs on the mismatched files → mismatch report appears with dangling and orphaned lists → student fixes the FXML → re-runs → "Matched: 6 connections, no mismatches" appears)
- The change: Add a third check: for each fx:id, verify that the matching handler method (e.g., `#handleCheckout` → `handleCheckout()`) exists in the controller — catching missing handler method registrations.
- Teardown angle: The mismatch is silent because JavaFX enforces it at runtime, not compile time. The tool makes it a compile-time failure: run it before you run the application, not after you wonder why the button does nothing.
- Exclusions: Full FXML schema validation, Scene Builder integration, CSS property checking.
- Score: 8/10

---

## Candidate 08 — Build a Phase-Gate Ladder Tracker with Claude: Know What Claude May Do at Each Module

- Source: info-5100-application-engineering-and-development/chapters/95-claude-code.md  (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The phase-gate ladder relaxes AI assistance as your verification skill grows. What Claude may do in Module 0 is much narrower than Module 12 — because in Module 12 you have enough understanding to evaluate more complex outputs. The tracker shows where you are.
- The artifact: a Python CLI tool that takes the current module number (0–14) and a description of the Claude task the student wants to perform, and returns: (1) whether the task is within the current module's permissions, (2) what the student must provide before asking (the phase-gate pre-condition), (3) what they must verify after receiving the output. Draws from the module-level boundary table in the chapter.
- Prompt seed: `claude "Write a Python CLI script called 'gatecheck.py' that takes --module [0-14] and --task [description]. Based on these module phase gates, determine if the task is permitted: Module 0-2: Claude is diagnostic only (explain errors, quiz on existing code — no code generation for submission). Module 3-7: Claude generates scaffolds from student-provided specifications (screen flow table, is-a statements, threat model must be written first). Module 8-12: Claude assists with implementation if design is student-owned (persistence policy, comparators, FXML stubs). Module 13-14: Claude assists with synthesis (test cases from behavior descriptions, inconsistency review). Output: 'PERMITTED / NOT PERMITTED at Module [N]', the precondition the student must satisfy before asking, and the verification required after receiving output. Include a brief rationale."`
- Read / check: Verify that Module 4 (debugging) is correctly classified as strictest: Claude may not identify the bug — student must provide symptom, hypothesis, isolation evidence. Check that Module 6 (authentication) requires the threat model before any code generation. Confirm Module 14 correctly requires the student-written CLAUDE.md before synthesis assistance.
- Human supplies (Claude can't): The student's current module and task description. The video demo tests several boundary cases (Module 4 debugging, Module 6 auth, Module 12 FXML).
- Output medium: screen-recording mp4 (terminal: student enters module=4, task="help me find what's wrong with my login method" → NOT PERMITTED → explanation of why → student enters module=6, task="generate login form with authentication" → NOT PERMITTED → threat model required → student enters module=12, task="generate controller stub from my FXML" → PERMITTED with preconditions shown)
- The change: Add a "what can I ask at this module?" command that lists all permitted and forbidden task categories for the current module — a quick reference card.
- Teardown angle: The gate is not bureaucracy — it is calibrated to what the student can verify at each stage. A gate that prevents Claude from generating authentication logic before Module 6 is the recognition that the student cannot evaluate that output before they understand threat modeling.
- Exclusions: Full LMS integration, automated grading hooks, specific Java frameworks.
- Score: 7/10
