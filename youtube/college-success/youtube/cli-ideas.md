# College Success: with LLMs — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Research the Hidden Curriculum with Claude: Translate Five College Terms That Mislead"
- Source: college-success/chapters/01-exploring-college.md (LLM Exercise 1B)
- Lane: RESEARCH (Claude assistant)
- Hook: "Office hours" is not the hours the office is open. "Faculty" is not your teacher. "Syllabus" is not a schedule. The institution never explains the gap — and students who arrive not knowing pay a silent tax from week one.
- The artifact: A sourced 5-entry translation table comparing "what the word suggests" vs. "what it actually means in college" — for Syllabus, Office Hours, Plagiarism, Final Exam, Faculty. Generated and refined in the terminal. Each entry includes one behavioral implication (what the student should do differently, knowing the real meaning). Formatted as a clean markdown table with a column for "Common first-semester mistake."
- Prompt seed: `claude "I'm going to paste a college syllabus passage. Identify every hidden curriculum signal — anything communicated implicitly, not explicitly — and explain what behavior each one calls for from a student. Then generate a 5-row translation table: columns are Term | What it suggests | What it means in college | Common first-semester mistake | What to do instead. Rows: Syllabus, Office Hours, Plagiarism, Final Exam, Faculty." [paste the example syllabus passage from Chapter 1]`
- Read / check: Verify all 5 terms are present; check that "Office Hours" correctly identifies the professor is waiting (not just available); verify the "Plagiarism" entry distinguishes malicious vs. sloppy (most college plagiarism is sloppy); check the "Final Exam" entry notes the 25-40% grade weight; confirm behavioral implications are specific (not generic advice).
- Human supplies: The Chapter 1 syllabus passage for translation (text from the chapter — paste directly into the prompt). No external data needed; this is a text analysis task.
- Output medium: slate (human fills with screen recording of the Claude session and the formatted table as a final still)
- The change: Ask Claude to apply the translation table to a real syllabus from the viewer's institution (prompt the viewer to paste their own course syllabus). What hidden signals does Claude catch that the student missed? The revision demonstrates the research discipline applied to a live document.
- Teardown angle: The hidden curriculum sorts outcomes silently from week one. Students who arrive already fluent have a lower attention tax — they already know what the door is for. The translation table is not about the vocabulary; it is about equalizing access to the institution's unwritten operating manual.
- Exclusions: FERPA legal details, specific plagiarism software mechanics, institutional policies that vary by campus.
- Score: 9/10

---

## Candidate 02 — "Research the Five Whys with Claude: Find the Motivation Behind the Motivation"
- Source: college-success/chapters/01-exploring-college.md (LLM Exercise 1A)
- Lane: RESEARCH (Claude assistant)
- Hook: "I'm in college for a degree" is the surface answer. Running the Five Whys five times gets to the answer loud enough to power midnight when the cost of staying up is real and the reason feels vague. Claude runs the exercise — and the research is on you.
- The artifact: A 5-round Five Whys transcript — Claude asks each follow-up question, the student answers, Claude summarizes what each round revealed. Final output is a 2-paragraph synthesis: the fifth answer (the root motivation) and the student's reflective response (where the AI got it right, where it missed). The transcript is saved as a markdown file the student can return to in semester two.
- Prompt seed: `claude "I want to do the Five Whys exercise to understand my reason for being in college. Start by asking me 'Why are you in college?' then ask a follow-up question based on my answer for each of 5 rounds. After 5 rounds, summarize what each round revealed — specifically what the fifth answer implies about my underlying motivation. Then ask me to write a paragraph responding to that summary."`
- Read / check: Verify Claude asks genuine follow-up questions (not just "why" repeatedly — the follow-up should respond to the content of the student's answer); check the summary distinguishes between rounds (Round 1 = strategy, Round 5 = root motivation); verify the final synthesis paragraph prompt asks the student to evaluate the AI's summary (not just accept it).
- Human supplies: The student's honest first answer, and honest answers for each subsequent round — this is the irreducibly human part. Claude facilitates; the student supplies the material. This video demonstrates the process with a worked example (the student from the chapter who wants to be a speech pathologist).
- Output medium: screen-recording mp4 (terminal showing the 5-round dialogue, the synthesis, and the student's reflective response typed in)
- The change: Ask Claude to run the Five Whys on the student's uncertainty instead: "I'm not sure why I'm in college." Ask Claude to identify the structure of the indecision — what the uncertainty is made of — following the chapter's guidance that uncertainty is itself information.
- Teardown angle: The specified "why" is not a vow. It is the best current reading — revisable on evidence. But the fifth answer is what makes the value side of the cost-benefit ledger concrete enough to compete with 1 AM fatigue. Vague purpose loses to immediate cost. Specific purpose competes.
- Exclusions: Career counseling frameworks (Ikigai, Holland codes — different tools for a different question), goal-setting research, academic advising workflow.
- Score: 8/10

---

## Candidate 03 — "Research Study Technique Effectiveness with Claude: What the Science Actually Says"
- Source: college-success/chapters/06-studying-memory-and-test-taking.md (LLM Exercises 6.1–6.5)
- Lane: RESEARCH (Claude assistant)
- Hook: Two students study 7 hours each. One earns a 71; the other earns an 89. The difference is not intelligence or time — it is the activity. The cognitive-science literature has been saying this for 50 years. Claude synthesizes it in 10 minutes.
- The artifact: A sourced research brief (under 600 words) comparing 5 study techniques: re-reading, highlighting, spacing, interleaving, and practice testing. For each, Claude finds: the evidence base, the typical effect size vs. the control, and the most common reason students don't use it despite knowing it works. Formatted as a 5-row table: Technique | Evidence base | Effect (strong/moderate/weak) | Why students avoid it.
- Prompt seed: `claude "Synthesize the cognitive-science research on 5 study techniques: re-reading, highlighting, spaced practice, interleaved practice, and retrieval/practice testing. For each technique, provide: (1) the primary research support (author, year, key finding); (2) comparative effectiveness vs. a baseline; (3) one specific reason students avoid it despite knowing it works. Format as a 5-row markdown table. Cite Dunlosky et al. 2013 as the anchor review. Flag any claims you cannot verify."`
- Read / check: Cross-reference the generated table against Dunlosky et al. 2013 (the 10-technique review paper) for the effectiveness ratings; verify the spacing and retrieval practice entries are rated "high utility" (they are, per Dunlosky); check that the "why students avoid it" column is specific (not generic "it's hard") — retrieval practice avoidance is because it feels harder than re-reading even when it works better; verify uncertainty flags are present.
- Human supplies: The chapter's LLM Exercise 6.1 framing as seed context (paste the exercise text as project context). Human verification required against Dunlosky et al. 2013 — Claude may mis-cite specific studies; the overall ratings are well-established and verifiable.
- Output medium: slate (human fills with a screen recording of the research session and the final formatted table)
- The change: Ask Claude to generate a personalized 5-day study schedule for a biology exam using only the 3 high-utility techniques (spacing, interleaving, practice testing) — applying the research to a concrete exam prep plan. The plan becomes the NEXT STEPS beat.
- Teardown angle: The most popular study habits — re-reading, highlighting — produce the feeling of learning without the substance. The research on retrieval practice is 50 years old. The gap between what the science says and what students do is not a knowledge gap; it is a discomfort gap. Retrieval feels harder than re-reading because it is — and that discomfort is the mechanism.
- Exclusions: Neuroscience of long-term potentiation (deeper than the video needs), interleaving mathematics (separate BUILD candidate from the algebra book), spaced repetition software (Anki, etc.) — product-specific, out of scope.
- Score: 9/10

---

## Candidate 04 — "Research the Hazard-Carter Adjustment Framework with Claude: Name What's Hard"
- Source: college-success/chapters/01-exploring-college.md (LLM Exercise 1C)
- Lane: RESEARCH (Claude assistant)
- Hook: "I'm failing at college" is unsolvable. "I'm struggling in the academic domain and the financial domain" is solvable — because each domain has a door on campus. The Hazard-Carter framework converts a monolith into a map.
- The artifact: A sourced decomposition of a fictional hard week using the 6 Hazard-Carter adjustment domains (Academic, Cultural, Emotional, Financial, Intellectual, Social). Each event in the hard week is mapped to its domain, and one campus resource is identified per domain. Final output: a 6-row markdown table (Domain | What qualifies | Example from the hard week | Campus door) plus a one-paragraph reflection on why the mapping helps.
- Prompt seed: `claude "Using the Hazard and Carter (2018) framework of 6 college adjustment domains — Academic, Cultural, Emotional, Financial, Intellectual, Social — map the following hard week to its domains and identify one campus resource for each: [Student failed a chemistry exam, roommate conflict, financial aid email about missing form, confusing lecture on a topic that felt settled, homesick, new friend group forming without them]. Format as a 6-row table: Domain | What qualifies | This week's event | Campus door. Add a paragraph on why domain decomposition helps more than the single sentence 'I'm struggling.'"`
- Read / check: Verify all 6 domains are present; check that each event is mapped to the correct domain (failed exam → academic; financial aid email → financial); verify the campus resources named are real and plausible (tutoring center, counseling center, financial aid office, etc.); check the reflection paragraph distinguishes decomposition from naming ("I'm struggling" is not decomposition).
- Human supplies: The fictional hard-week scenario (provided in the prompt) — OR the student's own real week if they choose to use a real example. For the video demonstration, a synthetic scenario is acceptable. The chapter's Hazard-Carter citation (2018) is available as verification.
- Output medium: slate (human fills with the session screen recording and the formatted table as the output beat)
- The change: Ask Claude to apply the same framework to a second scenario: a student who is performing fine academically but feels invisible and exhausted. Which domains are active? Which campus resources match? The contrast shows the framework applies to non-academic struggle, not just grade problems.
- Teardown angle: The map doesn't solve the problems. The address does. But to get to the address you have to know which door. The framework converts "I'm failing at college" — unsolvable — into 2-3 specific domains, each with a corresponding campus office that was paid for in tuition and is waiting for you to show up.
- Exclusions: Specific counseling modalities (CBT, DBT — clinical, not appropriate here), the full FERPA legal framework, academic probation procedures.
- Score: 8/10

---

## Candidate 05 — "Build a Zero-Based Budget with Claude: Make the Arithmetic Visible"
- Source: college-success/chapters/10-understanding-financial-literacy.md (LLM Exercise 10B)
- Lane: BUILD (Claude Code)
- Hook: A budget that runs $190 short per month doesn't feel like a crisis when you're building it. It feels like three small adjustments. Claude builds a zero-based budget with a stress-test that makes the sensitivity visible before the money is spent.
- The artifact: A Python script that takes monthly income, savings rate, and a list of expense categories/amounts, and outputs: (1) a zero-based budget table (income = savings + expenses = 0 balance); (2) a stress-test that increases 3 variable expense lines by 20% and shows the resulting deficit; (3) a prioritized list of expense cuts needed to restore balance. The script also generates a Manim bar chart showing the before/after stress-test comparison.
- Prompt seed: `claude "Write a Python script budget_tool.py that: (1) takes monthly net income, a savings rate (%), and a list of (category, amount) expense tuples; (2) prints a zero-based budget table with balance=0 (adjust 'discretionary' category to balance); (3) runs a stress test increasing restaurants, phone, and gas by 20%; (4) prints the stressed budget with the deficit highlighted and a list of the smallest cuts needed to restore balance. Include a demo with income=2500, savings_rate=14.4%, expenses=[('Housing',750),('Car+Insurance',450),('Groceries',400),('Phone',120),('Gas',200),('Medical',120),('Restaurants',100),('Entertainment',60)]."`
- Read / check: Verify the demo budget balances to $0 before stress test (check the math: 2500 - (120+240) - expenses = 0); check the stressed budget correctly shows the -$190 deficit; verify the cut recommendations prioritize variable/wants over fixed/needs; confirm the Manim bar chart renders and shows both before/after states.
- Human supplies: Nothing — fully synthetic. The demo uses chapter numbers verbatim; a real student would substitute their own numbers (the NEXT STEPS beat prompts this).
- Output medium: screen-recording mp4 (terminal showing the budget tables and stress-test output) + Manim (animated bar chart comparing before/after)
- The change: Add a 10-year compound interest projection for the savings amount: if the $360/month (savings + investments) grows at 6% annually, what does the student have at graduation + 10 years? Show the compound growth curve. This bridges the budget chapter to the compound interest content.
- Teardown angle: Budgets are sensitive to small choices — this is a feature, not a flaw. Small adjustments in either direction produce real consequences, and you can see them before they happen rather than after. The stress test is the tool that makes the future visible before the money moves.
- Exclusions: Investment account selection (ETFs, index funds — product-specific), tax optimization strategies, graduate-level financial planning (401k matching, HSAs — beyond the chapter's scope).
- Score: 8/10

---

## Candidate 06 — "Research the Cost of Student Debt with Claude: The Matching Principle"
- Source: college-success/chapters/10-understanding-financial-literacy.md (LLM Exercise 10C)
- Lane: RESEARCH (Claude assistant)
- Hook: The matching principle says total student debt should not exceed your expected first-year salary. Most students borrow without checking. Claude builds the comparison table — and the number that comes back is not what most students expect.
- The artifact: A sourced comparison table showing two loan scenarios against the matching principle: Scenario A ($30k at 5%, 10 years) and Scenario B ($60k at 6%, 10 years). For each: monthly payment, total paid, total interest paid, and the salary that makes each defensible (per the matching principle). A third row shows the "forgone optionality" — what the monthly payment forecloses (down payment pace, retirement contribution rate, emergency fund timeline). Final output: a go/no-go verdict for a student expecting $45k starting salary under each scenario.
- Prompt seed: `claude "Calculate and compare two student loan scenarios: Scenario A: $30,000 at 5% APR, 10-year repayment. Scenario B: $60,000 at 6% APR, 10-year repayment. For each: monthly payment, total paid, total interest paid. Then apply the matching principle: for a student expecting $45,000 starting salary, is each scenario defensible? Show the math. Add a third column: 'Forgone optionality' — what the monthly payment prevents (express as: months to save a $3,000 emergency fund, percent of gross income, years to a $10k car down payment). Format as a markdown table. Cite the Bureau of Labor Statistics Occupational Outlook Handbook as the salary reference tool."`
- Read / check: Verify monthly payment calculations are correct (Scenario A: ~$318/month; Scenario B: ~$666/month — use standard amortization formula); check the matching principle verdict is correct (Scenario A: $30k < $45k salary → defensible; Scenario B: $60k > $45k salary → not defensible); verify the forgone-optionality column is mathematically derived, not estimated; confirm the BLS reference is named.
- Human supplies: Nothing requiring real data — the scenarios use fixed numbers. Human verification of the amortization calculations is recommended (Claude sometimes errors on financial math — the CHANGE beat demonstrates this risk explicitly).
- Output medium: screen-recording mp4 (terminal showing the calculation, the table, the go/no-go verdict)
- The change: Ask Claude to show the calculation WITH an error deliberately introduced (e.g., using simple interest instead of compound amortization). Then show the correct calculation. This demonstrates the chapter's warning that Claude is unreliable for financial arithmetic — explanation from Claude; the math from your own verification.
- Teardown angle: The amount you can borrow is rarely the amount you should. The monthly payment doesn't just cost money — it forecloses optionality. The matching principle is the heuristic that converts an abstract loan number into a concrete monthly obligation measured against your actual earning trajectory. It is not optional; most students skip it.
- Exclusions: PSLF eligibility and navigation (complex and highly specific), income-driven repayment plan selection, private vs. federal loan comparison beyond the priority ladder.
- Score: 7/10

---

## Candidate 07 — "Research Spaced Practice Scheduling with Claude: Build the Study Plan Before the Exam"
- Source: college-success/chapters/06-studying-memory-and-test-taking.md (LLM Exercise 6.3)
- Lane: RESEARCH (Claude assistant)
- Hook: A student who studies 7 hours the night before earns a 71. A student who studies 7 hours across 5 days earns an 89. The research is clear. The implementation takes 10 minutes with Claude. Here is how to build the plan.
- The artifact: A complete 5-day spaced study schedule for a biology exam covering 5 chapters, generated by Claude: each day has a session length, a mix of chapters (interleaved), and at least one retrieval activity. Day 5 is a full practice test. The schedule is formatted as a markdown calendar with time allocations. A second output: a checklist for each session (read → close book → recall → check gaps → review gaps only → done).
- Prompt seed: `claude "Design a 5-day spaced study schedule for a biology exam covering chapters 7–11. Total available hours: 9 hours across 5 days. Requirements: (1) interleave chapters across sessions (not blocked by chapter); (2) at least one retrieval activity per session (describe the specific activity, not just 'review'); (3) Day 5 is a 2-hour mixed practice test covering all 5 chapters. Format as a markdown calendar showing day, time, chapters covered, and retrieval activity. Also output a per-session checklist: 6 steps from reading to gap-focused review."`
- Read / check: Verify the schedule sums to 9 hours; check that no day has only one chapter (interleaving requires at least 2 per session); verify each retrieval activity is specific (not "study" — should say "close book and write everything recalled from Chapter 7"); confirm Day 5 is a full practice test, not more reading; verify the checklist has exactly 6 steps.
- Human supplies: The student's actual exam date and real hours available — the video uses the chapter's example scenario; a real student would substitute their own parameters. The AI cannot know the student's schedule; that substitution is the human's work.
- Output medium: slate (human fills with a clean formatted version of the schedule, possibly typeset in a calendar tool)
- The change: Ask Claude to redesign the same 9 hours as a single-day cramming session and then compare total retrieval opportunities: 5-day plan has 4+ retrieval exercises and 4+ sleep-consolidation windows; 1-day cram has 1 retrieval exercise and 0 consolidation windows before the exam. The comparison makes the research concrete.
- Teardown angle: The total hours can be the same. The distribution is what matters. Each interval between study sessions contains forgetting — and the act of retrieving after forgetting strengthens the memory more than studying it fresh. The schedule is not time management; it is memory engineering.
- Exclusions: Spaced repetition software (Anki intervals — product-specific), specific retrieval techniques beyond self-quizzing (interleaved vs. blocked for mathematics requires a different framing), test anxiety management (separate topic).
- Score: 8/10

---

## Candidate 08 — "Research Imposter Syndrome with Claude: The Name for the Tax on Competence"
- Source: college-success/chapters/01-exploring-college.md (imposter syndrome section)
- Lane: RESEARCH (Claude assistant)
- Hook: The students who would benefit most from campus support are the most convinced they don't deserve it. Imposter syndrome is not a feeling of failure — it is a feeling of fraud in the presence of actual success. Claude finds the research; the research changes the framing.
- The artifact: A sourced 3-section research brief: (1) definition and prevalence (who experiences imposter syndrome and how common it is among high-performing students); (2) the two failure modes it produces (avoidance of help-seeking, over-preparation that masks rather than resolves the feeling); (3) the single most evidence-supported intervention. Under 500 words, with 2 cited sources. Formatted as a readable brief with one-sentence section summaries in bold.
- Prompt seed: `claude "Research imposter syndrome in college students. Provide: (1) definition and prevalence — who experiences it and what the research says about its frequency among high-achieving students; (2) two specific behavioral consequences that harm academic performance; (3) the most evidence-supported intervention (cognitive reframing, normalization, or another approach — cite one study). Keep under 500 words. Flag any statistics you cannot verify. Use Clance and Imes 1978 as the anchor reference for the original definition."`
- Read / check: Verify the Clance and Imes 1978 reference is cited correctly (they coined the term "impostor phenomenon" in that paper); check the prevalence figures are plausible (70% of people experience it at some point is the commonly cited figure — Claude may over- or under-state this); verify the intervention recommendation is evidence-based (normalization / shared disclosure is well-supported); confirm uncertainty flags appear for any specific statistics.
- Human supplies: The chapter's text as context seed. Human verification required for specific prevalence statistics — the exact figures vary widely across studies; Claude may conflate them.
- Output medium: slate (human fills with the formatted brief as a readable one-pager)
- The change: Ask Claude to apply the brief to a specific scenario: a first-generation college student who just earned an A on their midterm but still feels like they don't belong. What does the research say they should do, concretely, this week? The application bridges research to action.
- Teardown angle: Imposter syndrome is asymmetric: it is most intense in the people performing most competently in environments new to them. The tax is paid by the students who arguably deserve to be there the most. The research-informed reframe: the feeling is normal, it is not a signal of incompetence, and it goes away with normalization — not with proving yourself repeatedly.
- Exclusions: Clinical treatment of anxiety disorders (imposter syndrome is not a clinical diagnosis), gender-specific research (the chapter's framing is general), the specific mechanics of help-seeking programs.
- Score: 7/10
