# College Success Bundle with LLMs — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Translate the Hidden Curriculum with Claude: What College Assumes You Already Know"
- Source: college-success-bundle-with-llms/chapters/01-exploring-college.md + chapters/01-exploring-college/01-m82018.md
- Lane: RESEARCH (Claude assistant)
- Hook: The institution never explains its own norms — because doing so is expensive and it treats you as an adult who will figure them out. The students who don't pay a hidden tax on their attention from week one. Claude translates the five terms that mislead most.
- The artifact: A sourced 5-row translation table (Syllabus, Office Hours, Plagiarism, Final Exam, Faculty) with columns: Term | What it suggests | What it means in college | Most costly first-semester mistake | What to do instead. Generated and stress-tested in the terminal using an actual syllabus passage as input. The final output is a markdown table saved to file, suitable for posting to a course management system.
- Prompt seed: `claude "I'm going to paste a college syllabus passage. Identify every hidden curriculum signal — anything communicated implicitly, not explicitly — and explain what behavior each one calls for from a student. Then generate a translation table with 5 rows: Syllabus, Office Hours, Plagiarism, Final Exam, Faculty. Columns: Term | What it suggests | What it means in college | Costly first-semester mistake | What to do instead." [paste syllabus passage from Chapter 1 — the attendance/office hours/email response time example]`
- Read / check: Verify the "Office Hours" entry correctly identifies the professor is waiting (not available); check "Final Exam" notes the 25-40% grade weight; verify "Plagiarism" distinguishes accidental (sloppy note-taking) from intentional; check each "What to do instead" entry is specific and behavioral (not vague advice); confirm the table saves correctly to a file.
- Human supplies: The syllabus passage for translation (from Chapter 1 of the bundle — paste as context). A real student would use their own course syllabus for the CHANGE beat; the video uses the chapter's worked example.
- Output medium: slate (human fills with the screen recording of the research session and the final formatted table)
- The change: Ask Claude to apply the same analysis to a real course syllabus (prompt the viewer to paste their own syllabi). What hidden signals does Claude catch that the student missed on first reading? This demonstrates the research discipline on a live document.
- Teardown angle: The hidden curriculum sorts outcomes silently. Students who arrive already fluent pay a lower attention tax — they already know what the door means. The translation table does not change the institution; it equalizes access to the operating manual.
- Exclusions: FERPA legal details, institutional policies that vary by campus, academic dishonesty adjudication procedures.
- Score: 9/10

---

## Candidate 02 — "Research the Motivation Architecture with Claude: The Five Whys Applied to College"
- Source: college-success-bundle-with-llms/chapters/01-exploring-college.md (LLM Exercise 1A equivalent)
- Lane: RESEARCH (Claude assistant)
- Hook: "I'm in college for a degree" is a strategy, not a motivation. Running the Five Whys five times finds the answer that is loud enough to power 1 AM when the cost is real and the reason feels far away.
- The artifact: A 5-round Five Whys transcript (Claude asks each follow-up question, student answers, Claude summarizes each round), plus a final synthesis paragraph naming the fifth answer and the student's evaluation of whether Claude got it right. The transcript is saved as a markdown file the student can return to in semester two.
- Prompt seed: `claude "I want to do the Five Whys exercise to find my real motivation for being in college. Start by asking me 'Why are you in college?' then, based on my answer, ask a specific follow-up question for each of 5 rounds. After 5 rounds, summarize what each round revealed — especially what the fifth answer implies about my underlying purpose. Then ask me to write a paragraph responding to your summary."`
- Read / check: Verify Claude asks substantive follow-ups (not just repeating "why?" — each follow-up should respond to the content of the previous answer); check the summary distinguishes between rounds (Round 1 = surface strategy, Round 5 = root motivation); verify the final prompt asks the student to evaluate the AI's summary critically (not just accept it); confirm the output is saved to file.
- Human supplies: The student's honest answers across all 5 rounds — this is the irreducibly human part of the exercise. Claude facilitates; the student supplies the material. The video demonstrates with the chapter's example (the speech pathology student).
- Output medium: screen-recording mp4 (terminal showing the 5-round dialogue and synthesis)
- The change: Run the Five Whys on uncertainty: "I'm not sure why I'm in college." Ask Claude to identify the structure of the indecision — what the uncertainty is made of — producing a different kind of research brief that treats uncertainty as a starting point, not a problem.
- Teardown angle: The fifth answer is the one that competes with the cost at 1 AM. The first answer ("a degree") doesn't — it is too far away, too abstract. The Five Whys is not introspection; it is a decision procedure for making the value side of the cost-benefit ledger concrete enough to act on.
- Exclusions: Career counseling frameworks, academic advising decision trees, mental health support for motivational difficulties.
- Score: 8/10

---

## Candidate 03 — "Research Learning Styles with Claude: Why a Comfortable Story Became an Expensive Study Habit"
- Source: college-success-bundle-with-llms/chapters/02-the-truth-about-learning-styles.md
- Lane: RESEARCH (Claude assistant)
- Hook: Learning styles — visual, auditory, kinesthetic — feel intuitively true. Research says they don't predict learning outcomes. The myth persists because it flatters. Claude finds the debunking evidence and explains why the comfortable story is also the expensive one.
- The artifact: A sourced 2-page research brief: (1) the learning styles claim (what VARK and similar frameworks assert, and how they are used in education); (2) the primary debunking evidence (Pashler et al. 2008 as anchor; Rogowsky et al. 2015 as example); (3) what actually predicts learning (retrieval practice, spacing, interleaving — the evidence-based alternatives); (4) why the myth persists (cognitive ease, identity-consistency bias). Under 700 words. Formatted with section headers and a 3-row summary table: Claim | Evidence for | Evidence against.
- Prompt seed: `claude "Research the learning styles hypothesis — specifically VARK (visual, auditory, read/write, kinesthetic). Provide: (1) what the hypothesis claims and how it is taught; (2) the primary research debunking it — cite Pashler et al. 2008 as the anchor review and one additional study; (3) what actually predicts learning outcomes (retrieval practice, spacing, interleaving — cite Dunlosky et al. 2013); (4) why the myth persists despite the evidence. Format as a brief with section headers and a 3-row summary table: Claim | Evidence for | Evidence against. Flag any statistics you cannot verify."`
- Read / check: Verify Pashler et al. 2008 is cited correctly ("Learning Styles: Concepts and Evidence," Psychological Science in the Public Interest); check the debunking evidence is accurately described (the meshing hypothesis was not supported); verify the alternatives section correctly cites high-utility techniques; check the "why it persists" section is specific (not vague "it's popular").
- Human supplies: The chapter's framing as context seed. Human verification against Pashler et al. 2008 required — the abstract is freely available. The key finding (the meshing hypothesis lacks empirical support) is well-established; specific effect sizes may vary.
- Output medium: slate (human fills with the formatted brief as a one-pager)
- The change: Ask Claude to apply the evidence to a specific student scenario: "I'm a visual learner who re-reads the textbook with highlighting because that's how I learn best." What does the research say about that student's study habits? The application converts the research into specific behavioral feedback.
- Teardown angle: The learning styles myth is expensive precisely because it feels like self-knowledge. A student who identifies as a "visual learner" and organizes study time around visual materials has built a rationale for avoiding the study techniques that actually work. The myth is not harmless — it displaces effective strategies with comfortable ones.
- Exclusions: Full history of learning styles research (Dunn and Dunn, VAK, Gardner's multiple intelligences — different frameworks), specific critiques of VARK's design, the politics of education research.
- Score: 9/10

---

## Candidate 04 — "Build a Spaced Study Scheduler with Claude: Memory Engineering Before the Exam"
- Source: college-success-bundle-with-llms/chapters/06-studying-memory-and-test-taking.md (LLM Exercise equivalent — the bundle chapter)
- Lane: BUILD (Claude Code)
- Hook: A student who studies 7 hours the night before earns a 71. The same student, same 7 hours spread across 5 days, earns an 89. The schedule is the lever. Claude builds the schedule generator — the student runs it before every exam.
- The artifact: A Python script exam_scheduler.py that takes: exam date, topic list, available hours per day, and outputs: a day-by-day interleaved study schedule with specific retrieval activities per session. The schedule ensures each topic appears at least twice across sessions, the final session is a full practice test, and sleep-consolidation windows (8h between sessions) are preserved. Output is both terminal-printed and saved as a markdown file.
- Prompt seed: `claude "Write a Python script exam_scheduler.py that: (1) takes as input: exam_date (YYYY-MM-DD), topics (list of strings), hours_per_day (dict: day of week → max hours); (2) generates a spaced, interleaved study schedule ensuring each topic appears at least twice, the final day before the exam is a practice test, and no two sessions are on the same calendar day; (3) for each session, assigns a specific retrieval activity (close-and-recall, practice problems, teach-back prompt, or mixed test); (4) prints the schedule as a markdown calendar and saves it to study_schedule.md. Include a demo: exam 7 days from today, topics=['Chapter 7','Chapter 8','Chapter 9','Chapter 10','Chapter 11'], 1.5 hours per available day."`
- Read / check: Verify the demo produces a schedule with each topic appearing at least twice; check the final session is a practice test (not reading); verify the schedule respects the hours_per_day constraint; confirm the markdown calendar saves correctly; check the retrieval activity variety (should not assign "close-and-recall" to every session).
- Human supplies: Nothing for the demo run — fully synthetic. For real use, the student supplies their actual exam date and topic list. The script is the artifact; the student's calendar is the input.
- Output medium: screen-recording mp4 (terminal showing script generation, demo run, and the saved markdown calendar)
- The change: Add a --cramming-mode flag that generates the worst possible schedule (all studying the night before) and prints a comparison: total retrieval opportunities (spacing: 4+; cramming: 1) and sleep-consolidation windows (spacing: 4+; cramming: 0). The comparison is the lesson.
- Teardown angle: The research on spacing and retrieval practice is 50 years old. The schedule generator does not do the studying — it does the planning. The planning costs 5 minutes. The payoff is 4 additional retrieval exercises and 4 sleep-consolidation windows per exam, compared to cramming. The math is favorable by an order of magnitude.
- Exclusions: Spaced repetition algorithm optimization (Anki's SM-2 algorithm — product-specific), adaptive scheduling based on recall scores, integration with calendar apps.
- Score: 9/10

---

## Candidate 05 — "Build a Zero-Based Budget Stress-Tester with Claude: See the Cascade Before It Happens"
- Source: college-success-bundle-with-llms/chapters/10-understanding-financial-literacy.md (LLM Exercise equivalent — the bundle chapter)
- Lane: BUILD (Claude Code)
- Hook: Elan walked into the store with a budget and walked out $2000 in debt. Each individual decision was defensible. The cascade only became visible after it started. The budget stress-tester makes the cascade visible before the money moves.
- The artifact: A Python script budget_stress.py that: (1) accepts monthly income, savings rate, and expense categories; (2) prints a zero-based budget (income = savings + expenses); (3) runs a stress test — increases 3 variable expenses by 20% — and prints the deficit; (4) outputs a ranked list of cuts needed to restore balance (variable/wants first, then fixed/needs); (5) prints the compound-interest projection for the savings amount over 10 years at 6% annual. Terminal output + a Manim animated bar chart showing before/after the stress test.
- Prompt seed: `claude "Write budget_stress.py that: (1) takes income=2500, savings_amount=360, expenses as (category, amount, type) tuples where type is 'fixed' or 'variable'; (2) prints a zero-based budget table; (3) stress-tests by increasing all variable expenses by 20%; (4) shows the deficit and a ranked cut list (variable first, then fixed) to restore balance; (5) prints 10-year compound growth of the savings amount at 6% annually. Use the demo from the chapter: [('Housing',750,'fixed'),('Car+Insurance',450,'fixed'),('Groceries',400,'variable'),('Phone',120,'variable'),('Gas',200,'variable'),('Medical',120,'fixed'),('Restaurants',100,'variable'),('Entertainment',60,'variable')]."`
- Read / check: Verify the zero-based budget balances (2500 - 360 - expenses should equal 0; the demo should balance with Restaurants+Entertainment absorbing the remainder); check the stress-test deficit is correct (20% increase on all variable categories should produce ~-$190); verify the cut list orders correctly (variable expenses before fixed); confirm the compound growth calculation is correct (360/month for 10 years at 6% annual should produce approximately $58,000).
- Human supplies: Nothing — fully synthetic for the demo. A real student substitutes their own income and expenses. The key demonstration (stress test producing a visible deficit before the money moves) works with any numbers.
- Output medium: screen-recording mp4 (terminal showing the budget and stress-test output) + Manim (animated bar chart showing the before/after comparison)
- The change: Add a second stress-test scenario: the student gets a 10% raise but also takes on a $300/month car payment. Does the raise offset the new fixed expense? Show the net budget impact — the raise scenario often looks better than it is because the fixed expense is permanent while raises are not guaranteed.
- Teardown angle: Budgets are sensitive to small choices — this is the feature that makes them useful. The sensitivity means you can see the cascade before it starts, not after. Elan's cascade began with a decision that looked defensible in isolation. The stress-tester shows what "defensible in isolation" costs when aggregated.
- Exclusions: Investment account selection, tax optimization, graduate-level financial planning.
- Score: 8/10

---

## Candidate 06 — "Research Critical Thinking Modes with Claude: Which Tool for Which Problem"
- Source: college-success-bundle-with-llms/chapters/07-thinking.md
- Lane: RESEARCH (Claude assistant)
- Hook: Creative thinking, analytical thinking, and critical thinking feel like synonyms until you need to use them correctly. The chapter's three-mode framework distinguishes them — and Claude can run the diagnosis on a real problem to show which mode fits.
- The artifact: A sourced 3-mode framework summary (Generating/Creative, Decomposing/Analytical, Evaluating/Critical), with: definition, when to use it, and what failing to use it looks like. Plus a diagnostic exercise: Claude applies all three modes to the same academic challenge (a confusing research paper) to show how the output differs by mode. Under 500 words, formatted as a 3-row table followed by the diagnostic worked example.
- Prompt seed: `claude "Describe the three thinking modes from the college success framework: (1) Generating/Creative thinking — what it is, when to use it; (2) Decomposing/Analytical thinking — what it is, when to use it; (3) Evaluating/Critical thinking — what it is, when to use it. For each mode, add one example of what NOT using it looks like in an academic context. Then apply all three modes to this scenario: a student reads a research paper that contradicts their thesis. Show how each mode produces a different response to the same situation."`
- Read / check: Verify the three modes are correctly defined and distinct (creative = generating possibilities; analytical = breaking into parts; critical = evaluating evidence and claims); check the "what NOT using it looks like" examples are specific and recognizable; verify the worked example produces genuinely different outputs for each mode (not paraphrases of each other); confirm the format is a table followed by the diagnostic.
- Human supplies: The chapter's framing as context seed. The worked example scenario (contradicting research paper) is synthetic and can be made more concrete by providing a real paper excerpt — but the synthetic version suffices for the video.
- Output medium: slate (human fills with the formatted table and worked example as a clean one-pager)
- The change: Ask Claude to diagnose a second scenario: "A student needs to write a research paper and doesn't know where to start." Which mode should fire first? Which second? Which third? The sequencing reveals that the three modes are not interchangeable — they form a natural order for most academic tasks.
- Teardown angle: The layer above the work matters more than the work itself. A student who generates 10 thesis statements, then decomposes their strongest one, then evaluates the evidence for each sub-claim is using all three modes in sequence. Most struggling students are using only one mode — usually the wrong one for the stage they are in.
- Exclusions: Bloom's taxonomy mapping (related but different framework), formal logic and argumentation (philosophy scope), specific research paper structure.
- Score: 8/10

---

## Candidate 07 — "Research Communication Failure Modes with Claude: Why the Illusion Takes Place"
- Source: college-success-bundle-with-llms/chapters/08-communicating.md
- Lane: RESEARCH (Claude assistant)
- Hook: The most common outcome of communication is the illusion that it has taken place. Claude finds the research on why — and the specific failure modes that cost students the most in academic settings.
- The artifact: A sourced research brief (under 500 words) on academic communication failure modes: (1) the curse of knowledge — why experts assume shared context that doesn't exist; (2) the email that sounds aggressive to the reader and neutral to the sender; (3) the office hours visit that never happens because the student misread the invitation. Each failure mode is paired with a specific behavioral fix. Formatted as a 3-section brief with one cited source per section.
- Prompt seed: `claude "Research three academic communication failure modes that affect college students specifically: (1) the curse of knowledge (what it is, why it affects student-professor communication, one fix); (2) email tone misreading (why digital communication is ambiguous in ways face-to-face is not, one fix); (3) the office hours hesitation (why students misread the professor's availability signal, one fix). For each, cite one research source. Keep under 500 words total. Flag any statistics you cannot verify."`
- Read / check: Verify the curse of knowledge definition is correct (Heath & Heath "Made to Stick" or Pinker "The Sense of Style" are standard references); check the email tone research is plausible (Kruger et al. 2005 "Egocentrism over e-mail" is a peer-reviewed study on this); verify the office hours fix is specific and behavioral (not "just go"); confirm uncertainty flags appear for any specific statistics.
- Human supplies: The chapter's framing as context seed. Human verification against at least one cited source is recommended — Claude may cite real papers with slightly wrong details.
- Output medium: slate (human fills with the formatted brief)
- The change: Ask Claude to draft two versions of the same email to a professor: Version A (common failure — sounds demanding, no context) and Version B (corrected version — context, specific request, appropriate register). Then ask Claude to explain what changed between the two versions and why it matters.
- Teardown angle: The illusion of communication is the most expensive outcome because it feels like success. Both parties believe they communicated; neither adjusts. In academic settings, the cost is asymmetric: the student pays the grade consequence, not the professor. The behavioral fixes are small — the curse of knowledge yields to a single habit change.
- Exclusions: Intercultural communication differences, formal presentation skills (different chapter topic), written argumentation structure (research paper mechanics).
- Score: 7/10

---

## Candidate 08 — "Build a Study Audit Tool with Claude: Grade the Grade Using the Error Pattern"
- Source: college-success-bundle-with-llms/chapters/06-studying-memory-and-test-taking.md (LLM Exercise 6.5 equivalent)
- Lane: BUILD (Claude Code)
- Hook: Most students look at a grade, feel what they feel about it, and move on. The graded exam is a precise diagnostic — it tells you exactly which topics you missed and what kind of errors you made. Claude builds the tool that reads the diagnostic.
- The artifact: A Python script exam_audit.py that takes a list of (question_number, topic, question_type, correct/incorrect) entries and outputs: (1) miss rate by topic (coverage gaps); (2) miss rate by question type (cognitive operation mismatch); (3) miss rate by position in the test (spacing failure if late-covered material is weaker); (4) a 3-row diagnosis table (Error pattern | What it indicates | Study adjustment) printed to terminal. The same structure as the chapter's post-mortem table, automated.
- Prompt seed: `claude "Write exam_audit.py that takes a list of (question_num, topic, question_type, result) tuples — question_type is 'recall', 'application', or 'analysis'; result is 'correct' or 'incorrect'. Output: (1) miss rate by topic; (2) miss rate by question type; (3) miss rate by question number quartile (Q1, Q2, Q3, Q4 of the exam); (4) a diagnosis table: if miss rate by topic is uneven → coverage gap; if miss rate by question type is uneven → cognitive operation mismatch; if Q3/Q4 miss rate is higher → spacing failure. Print a 3-row diagnosis table with study adjustment recommendations. Include a demo with 20 questions."`
- Read / check: Verify the quartile analysis correctly flags late-exam weakness as a spacing failure; check the cognitive operation mismatch detection fires when application/analysis miss rates exceed recall miss rate; verify the diagnosis table uses the correct chapter framing (coverage gap, cognitive operation mismatch, spacing failure, retrieval deficit); confirm the demo runs without errors and produces a realistic output.
- Human supplies: A real or synthetic graded exam entry list — for the video, a synthetic 20-question demo. For real use, the student enters their actual exam results. The tool does the diagnosis; the student supplies the data.
- Output medium: screen-recording mp4 (terminal showing the demo run and the diagnosis table)
- The change: Add a --next-exam-plan flag that, based on the diagnosis, generates a targeted 5-day study schedule addressing the specific weakness pattern found. If the diagnosis is "coverage gap in Chapter 9," the plan includes two Chapter 9 sessions. The schedule output bridges to Candidate 04's scheduler.
- Teardown angle: The post-mortem is the cheapest form of improvement available. Twenty minutes with a graded exam, mapped to its error pattern, can reshape the next month of studying in ways that another hour of re-reading never would. The tool does not do the studying — it tells you exactly where to put the studying.
- Exclusions: Machine learning for grade prediction, integration with LMS gradebook systems, statistical significance of error pattern detection on small sample sizes.
- Score: 8/10

---

## Candidate 09 — "Research the Planning Process with Claude: Five Steps That Prevent Elan's Cascade"
- Source: college-success-bundle-with-llms/chapters/10-understanding-financial-literacy.md (LLM Exercise equivalent)
- Lane: RESEARCH (Claude assistant)
- Hook: Elan walked into the electronics store with a budget and walked out $2000 in debt. The planning process takes 10 minutes. Elan skipped it. Claude runs it on the laptop decision to show what 10 minutes of deliberation prevents.
- The artifact: A sourced 5-step planning process application to the Elan laptop scenario: (1) underlying need identified (machine running coursework software, not "a MacBook"); (2) alternatives list (new, refurbished, used, campus lending, library); (3) written plan (refurbished Dell, $300, paid from savings, leaving $700 emergency fund); (4) implementation gate (if the store doesn't have it, leave); (5) monitoring checkpoint. Total: under 400 words, formatted as a step-by-step markdown document with the specific dollar amounts from the chapter.
- Prompt seed: `claude "Apply the 5-step financial planning process to the following decision: I need a computer for college coursework that runs Microsoft Office and Python. My savings: $1000. I have been looking at a $2000 MacBook Pro. Steps: (1) Identify my underlying need (not the surface want); (2) List at least 5 alternatives with approximate costs; (3) Write a specific plan: item, budget, funding source; (4) Describe the implementation gate (what happens if the plan doesn't match what's available); (5) Define one monitoring checkpoint. Format as a step-by-step document with specific dollar amounts."`
- Read / check: Verify Step 1 identifies the underlying need correctly (runs Office and Python — not "a MacBook"); check Step 2 lists at least 5 alternatives including non-purchase options (library, campus lending); verify Step 3 names a specific budget under the chapter's $300 refurbished Dell benchmark; check Step 4 is specific about what the student should do if the store doesn't have the planned item (leave, not negotiate up); confirm the monitoring checkpoint is measurable.
- Human supplies: The student's actual savings balance and specific software needs — for the video, the chapter's Elan scenario is used. The process applies identically to the viewer's own decision; the NEXT STEPS prompt them to run it on a real purchase they're considering.
- Output medium: screen-recording mp4 (terminal showing the 5-step process applied, step by step, with Claude's output)
- The change: Ask Claude to deliberately skip Steps 2 and 3 (go straight from underlying need to impulse buy) and show what happens — the cascade. Then restore the full process and show the contrast. The comparison is the lesson.
- Teardown angle: The planning process is slower than impulse-buying — by about 10 minutes. The impulse can cost thousands. The math is not close. What makes the impulse attractive is that the cost is deferred and the salesperson is present. The discipline is trusting future math over present pressure.
- Exclusions: Specific product recommendations, negotiation tactics, student loan priority ordering (separate topic within the chapter).
- Score: 7/10

---

## Candidate 10 — "Research Academic Pathways with Claude: Build the Degree Map Before Drifting"
- Source: college-success-bundle-with-llms/chapters/04-planning-your-academic-pathways.md
- Lane: RESEARCH (Claude assistant)
- Hook: Most students drift through their degree — course by course, semester by semester, with no map of what leads where. The academic pathway chapter says: values before plans. Claude helps build the map — but the values have to come from you.
- The artifact: A sourced 3-section research brief and planning template: (1) the research on values-based career planning vs. credential-chasing (one cited study on career satisfaction and values alignment); (2) a values-to-pathway mapping exercise (5 values → 3 degree options → 2 specific course sequences); (3) a list of 5 campus resources for pathway planning (academic advising, major fairs, career center, alumni networks, degree audit tools). Formatted as a brief + planning template with prompts the student fills in.
- Prompt seed: `claude "Help me research and build an academic pathway planning template. Provide: (1) one study showing that values-aligned career planning predicts better career satisfaction than credential-chasing; (2) a values-to-pathway mapping template — I input 5 values, you output 3 possible degree areas and 2 specific course sequences per area; (3) a list of 5 campus resources for academic pathway planning with one-sentence descriptions of each. Format as a brief followed by a fillable template with prompts. My values to start: [helping people, scientific discovery, financial stability, creative work, teaching]."`
- Read / check: Verify the cited study is plausible and correctly attributed (career satisfaction research — Holland 1997 or Dik & Duffy 2009 are standard references); check the values-to-pathway mapping is responsive to the specific values provided (not generic); verify the campus resources list is real and accurate (academic advising, career center, degree audit are standard across institutions); confirm the template has fillable prompts for the student's own values.
- Human supplies: The student's 5 values — for the video, the demo uses the example values; a real student substitutes their own. Human verification of the cited study is recommended.
- Output medium: slate (human fills with the formatted template as a clean planning document)
- The change: Ask Claude to run the mapping on a second set of values that conflict with each other (financial stability + artistic freedom) and show how the pathway template handles the conflict. The tension reveals the real planning work — values clarification before degree selection, not the other way around.
- Teardown angle: Most career planning is aimed at the wrong target — credentials before values. The research on career satisfaction is consistent: values alignment predicts satisfaction; credential accumulation does not. The template is not a degree planner; it is a values-clarification tool that happens to produce degree suggestions as a side effect.
- Exclusions: Specific major comparisons (median salary by field — too product-specific), transfer credit evaluation, graduate school planning.
- Score: 7/10
