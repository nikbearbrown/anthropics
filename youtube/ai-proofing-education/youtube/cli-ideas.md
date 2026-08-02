# AI-Proofing Education — CLI Video Ideas ("X with Claude")

> Note: This book's chapter content (beyond the introduction) is placeholder.
> Cards are derived from the introduction's core argument: the boundary between
> execution and judgment, and what a reader needs to decide before delegating to AI.
> All cards are RESEARCH lane — the book is humanities/pedagogy.

## Candidate 01 — "Research the Execution vs Judgment Boundary with Claude"
- Source: ai-proofing-education/chapters/00-introduction.md
- Lane: RESEARCH (Claude assistant)
- Hook: The first sign of trouble isn't failure — it's fluency. The draft looks clean, the answer sounds reasonable, the chart has labels. Nothing in the surface announces that a human still has work to do.
- The artifact: A sourced research brief synthesizing the academic evidence for where AI execution ends and human judgment begins in educational contexts — covering at minimum three domains (writing, coding, data analysis) with one concrete failure-of-fluency example per domain. Displayed as a three-column Manim table: task / what AI produces / what judgment the human must supply.
- Prompt seed: `claude "Research the academic and practitioner literature on the boundary between AI execution and human judgment in educational assessment. For at least three domains (writing, coding, data analysis), find a documented case where AI output was fluent and plausible but required human judgment to validate. For each: (1) what the AI produced, (2) what it could not know, (3) what the human had to supply. Cite sources."`
- Read / check: Verify cited cases are real and documented (not AI-generated examples). Confirm the "what the human had to supply" column names something genuinely beyond pattern completion. Check that at least two of the three domains have peer-reviewed or practitioner-documented sources.
- Human supplies (Claude can't): Verification that cited studies exist and that the failure-of-fluency examples are accurately described — Claude may confabulate specific cases. Human must click through to confirm.
- Output medium: Manim (animated three-column table building domain by domain)
- The change: Ask Claude to add a fourth column: "how would you know the AI output is wrong without domain knowledge?" — force the question of what meta-cognitive capacity the evaluator needs.
- Teardown angle: The danger isn't that the machine writes. The danger is that the human stops noticing which parts of the work still require judgment. Fluency hides the gap.
- Exclusions: Don't go into specific EdTech tools; don't cover cheating/plagiarism detection; don't review K-12 vs higher-ed policy differences.
- Score: 8/10

---

## Candidate 02 — "Build a Judgment vs Execution Classifier with Claude"
- Source: ai-proofing-education/chapters/00-introduction.md
- Lane: BUILD (Claude Code)
- Hook: "Decide what question matters. Decide what evidence counts. Decide what tradeoffs are acceptable. Decide who is responsible." These four moves are in every assignment — and they're the four moves AI cannot make for you.
- The artifact: A Python script that takes any assignment prompt as input and classifies each component task as "execution" (AI-handleable) or "judgment" (human-required), outputting a two-column breakdown with an explanation for each classification. Displays as an animated Manim table filling row by row.
- Prompt seed: `claude "You are an educational judgment analyst. Given this assignment prompt, decompose it into individual component tasks. For each task, classify it as: EXECUTION (AI can handle reliably — pattern matching, formatting, summarization, generation) or JUDGMENT (human must supply — what question matters, what evidence counts, what tradeoffs are acceptable, who is responsible). Explain each classification in one sentence. Output as a two-column table."`
- Read / check: Verify the classification is meaningful (not that all creative work is "judgment" and all mechanical work is "execution" — the interesting cases are in between). Confirm the explanations are specific, not generic. Check that at least one task is misclassified initially and gets revised in the change beat.
- Human supplies (Claude can't): A real or realistic assignment prompt from an actual course — something specific enough that the classification is non-trivial. Synthesize from common assignment types if needed. Synthetic is acceptable.
- Output medium: Manim (animated two-column table, EXECUTION in blue, JUDGMENT in amber)
- The change: Feed the same assignment prompt to Claude from the perspective of "a student trying to delegate as much as possible" — show how the boundary shifts depending on who is doing the classifying, and why that shift is itself a judgment call.
- Teardown angle: The recurring concept of the book: execution is the production of an artifact, judgment is the disciplined decision about whether that artifact should exist, whether it is right, and what consequences follow. The classifier forces the question.
- Exclusions: Don't go into academic integrity policy; don't cover specific assignment types in depth; don't build a grading tool.
- Score: 8/10

---

## Candidate 03 — "Research What Disciplined Delegation Looks Like with Claude"
- Source: ai-proofing-education/chapters/00-introduction.md
- Lane: RESEARCH (Claude assistant)
- Hook: Avoidance is not a strategy. The strategy is disciplined use — knowing what to delegate, what to inspect, what to refuse, and what to practice until it becomes part of your own competence.
- The artifact: A sourced brief synthesizing documented examples of disciplined AI delegation in professional and educational contexts — cases where someone had an explicit policy (not just intuition) for what AI handles and what they handle personally. Three cases, each with: the delegation rule, the inspection step, the refusal condition, the competence maintained. Displayed as a three-case animated comparison.
- Prompt seed: `claude "Research documented cases of disciplined AI delegation — professionals or educators who have articulated an explicit policy for what AI may handle vs what they must handle personally. Find three cases with: (1) the stated delegation rule, (2) the described inspection step, (3) what they explicitly refuse to delegate, (4) what competence they report maintaining by not delegating. Cite sources. If published examples are scarce, note that honestly and describe the framework that well-documented cases use."`
- Read / check: Verify that cited cases are real and documented (not illustrative fictions). If Claude acknowledges scarcity of primary sources, that acknowledgment is the lesson — the absence is itself informative. Check that the four-element framework (delegate rule / inspection step / refusal condition / competence maintained) is populated for each case.
- Human supplies (Claude can't): Verification that cited cases are accurately described — Claude may conflate sources. Human must confirm at least one case is primary-source verifiable.
- Output medium: Manim (animated three-case comparison table, building case by case)
- The change: Ask Claude to draft a one-paragraph "disciplined delegation policy" for a specific professional role (educator, analyst, designer) — force the synthesis from research to personal application.
- Teardown angle: The book's method: a way to decide what to delegate, what to inspect, what to refuse, and what to practice. The research brief shows what that looks like in practice, not just in theory.
- Exclusions: Don't go into organizational AI governance frameworks; don't cover specific EdTech tools; don't review cheating detection.
- Score: 7/10

---

## Candidate 04 — "Build the Trust Test for AI Output with Claude"
- Source: ai-proofing-education/chapters/00-introduction.md
- Lane: BUILD (Claude Code)
- Hook: Don't ask first whether the output is impressive. Ask what would have to be true for it to be trusted. Ask what the machine could not know. Ask what you are now responsible for.
- The artifact: A Python script that takes any AI-generated text as input and runs three trust tests: (1) What claims does this make? (extract as a list), (2) Which claims require domain knowledge to verify? (classify), (3) What does the machine not have access to that would change these claims? (generate). Outputs a structured trust-evaluation document. Displays as an animated Manim three-step reveal.
- Prompt seed: `claude "You are a trust auditor for AI-generated educational content. Given this AI-generated text, perform three steps: (1) Extract every factual or evaluative claim as a numbered list. (2) For each claim, classify it as VERIFIABLE FROM PUBLIC SOURCES, REQUIRES DOMAIN KNOWLEDGE, or CANNOT BE VERIFIED WITHOUT CONTEXT THE AI LACKS. (3) For the third category, name specifically what the AI could not know. Output as a structured trust-evaluation document."`
- Read / check: Verify the claim extraction is complete (no claims missed). Confirm the classification is meaningful — not all claims should land in the same category. Check that "what the AI could not know" is specific (not just "local context" — name what kind of local context specifically).
- Human supplies (Claude can't): The AI-generated text to audit — use a realistic synthetic output (a paragraph from a student-AI collaboration, or an AI-generated lesson plan). Synthetic is fully acceptable.
- Output medium: Manim (animated three-step reveal: claims list appears, then classifications animate, then the "could not know" column fills in)
- The change: Run the same trust test on a human-written text — show that the third category (cannot be verified without context the AI lacks) is often smaller for human-written content because humans signal their context explicitly.
- Teardown angle: The closing return from the introduction: return to the polished artifact. Do not ask first whether it is impressive. Ask what would have to be true for it to be trusted.
- Exclusions: Don't go into plagiarism detection; don't cover specific disciplines; don't build a grading rubric.
- Score: 7/10

---

## Candidate 05 — "Research the Intelligent Textbook: What Medhavy Adds and Doesn't Add with Claude"
- Source: ai-proofing-education/chapters/00-introduction.md + chapters/00-frontmatter.md
- Lane: RESEARCH (Claude assistant)
- Hook: Even in an adaptive learning system with hints, quizzes, and feedback loops — the learning target remains human. The intelligent textbook doesn't change what judgment means; it changes who gets practice reaching it.
- The artifact: A sourced research brief on adaptive learning systems — what they demonstrably improve (engagement, pacing, identification of gaps), what they cannot improve (judgment, situated knowledge, responsibility for consequences), and one concrete study for each category. Displayed as a two-column Manim comparison: what adaptive systems change / what they don't change.
- Prompt seed: `claude "Research the peer-reviewed evidence on what adaptive learning systems (intelligent tutoring systems, AI-powered textbook platforms) demonstrably improve vs what they cannot improve in educational outcomes. Find: (1) at least two studies showing measurable improvements in specific learning outcomes, (2) at least one documented case where adaptive systems failed to develop or measure higher-order judgment. Cite sources. Be honest about evidence quality."`
- Read / check: Verify that cited studies are real and accurately summarized. Check that the "what they cannot improve" column is evidence-based, not just speculative. Confirm that at least one source is peer-reviewed (not just practitioner commentary).
- Human supplies (Claude can't): Verification of cited studies — Claude may conflate or confabulate specific research findings. Human must confirm at least two studies exist and say what the abstract claims.
- Output medium: Manim (two-column animated comparison table)
- The change: Ask Claude to add a third column: "what Medhavy/ITS design would need to change to address the gap" — force the synthesis from critique to design implication.
- Teardown angle: The intelligent textbook is infrastructure for open learning. It extends the reach of judgment practice; it does not substitute for judgment. The learning target remains human even inside the adaptive loop.
- Exclusions: Don't review specific ITS platforms commercially; don't go into LMS policy; don't cover K-12 vs higher-ed differences.
- Score: 7/10

---

## Candidate 06 — "Map the Judgment Curriculum: What Can't Be Delegated in Your Field with Claude"
- Source: ai-proofing-education/chapters/00-introduction.md
- Lane: RESEARCH (Claude assistant)
- Hook: The book's deeper concern is the work that remains after execution becomes cheap: deciding what question matters, what evidence counts, what tradeoffs are acceptable, what failure would look like, and who is responsible when the output leaves the screen.
- The artifact: A field-specific judgment curriculum map — for a chosen discipline (education, medicine, law, engineering), a sourced list of the judgment moves that cannot be delegated: what question matters, what evidence counts, what tradeoffs are acceptable, what failure looks like, who is responsible. Five moves, five sourced examples per discipline.
- Prompt seed: `claude "For the discipline of [EDUCATION], map the five judgment moves that cannot be delegated to AI: (1) What question matters — how do educators decide what is worth asking?, (2) What evidence counts — what counts as evidence of learning?, (3) What tradeoffs are acceptable — between coverage and depth, between efficiency and understanding?, (4) What failure looks like — how do educators recognize that something has gone wrong that data won't catch?, (5) Who is responsible — when an AI-assisted assessment fails, where does accountability land? For each: one specific sourced example from the research or practitioner literature."`
- Read / check: Verify that examples are specific (not generic) and sourced. Confirm the five moves are populated for the chosen discipline. Check that "what failure looks like" includes a case where AI output appeared successful but wasn't.
- Human supplies (Claude can't): Verification of cited examples — Claude may illustrate rather than cite. Human must confirm at least three examples are traceable to actual sources.
- Output medium: Manim (animated five-row table building row by row, one judgment move at a time)
- The change: Run the same mapping for a second discipline — show how the five judgment moves manifest differently in education vs medicine vs law, and what that variation reveals about the structure of judgment.
- Teardown angle: The curriculum that matters is the one that trains judgment, not execution. The field-specific map shows what that looks like before a student or practitioner ever touches an AI tool.
- Exclusions: Don't go into specific curriculum standards; don't review accreditation requirements; don't cover assessment design in depth.
- Score: 7/10

---

## Candidate 07 — "Build a Fluency vs Trust Detector with Claude"
- Source: ai-proofing-education/chapters/00-frontmatter.md + chapters/00-introduction.md
- Lane: BUILD (Claude Code)
- Hook: Speed without judgment simply accelerates error. The draft looks clean. The answer sounds reasonable. The chart has labels. Nothing in the surface announces that a human still has work to do.
- The artifact: A Python script that takes two versions of the same document (AI-generated and human-written on the same topic) and scores them on two independent dimensions: FLUENCY (surface quality: grammar, structure, format) and TRUST (substantive accuracy: claims traceable to sources, appropriate uncertainty, specificity about context). Outputs a 2x2 scatter plot where the AI output and human output are plotted by both scores.
- Prompt seed: `claude "I am going to give you two versions of a document on the same topic: one AI-generated, one human-written. Score each on two dimensions: (1) FLUENCY (0-10): grammar, coherence, structure, appropriate register. (2) TRUST (0-10): factual accuracy (claims verifiable), appropriate uncertainty (hedged where evidence is limited), specificity (not generic). Output a comparison table with both scores and one sentence of justification per score."`
- Read / check: Verify the trust score distinguishes between fluency and accuracy (they should not always correlate). Confirm the AI-generated document scores higher on fluency than the human document in at least some cases — that's the point. Check the justification sentences are specific.
- Human supplies (Claude can't): A pair of documents (AI-generated and human-written) on the same topic. Synthesize using a realistic domain (an AI-generated lesson plan vs a teacher's lesson plan on the same topic). Synthetic is fully acceptable.
- Output medium: Manim (animated 2x2 scatter plot with points appearing and axes labeled)
- The change: Add a third document — a heavily edited AI output — and show how editing moves the trust score without always moving the fluency score. The edit is the human's work.
- Teardown angle: Fluency is what AI optimizes. Trust is what judgment supplies. The 2x2 plot makes visible what the polished surface hides.
- Exclusions: Don't go into plagiarism detection; don't cover specific grading rubrics; don't build for automated assessment use.
- Score: 7/10

---

## Candidate 08 — "Research What AI Cannot Know: The Situated Knowledge Gap with Claude"
- Source: ai-proofing-education/chapters/00-introduction.md
- Lane: RESEARCH (Claude assistant)
- Hook: "Ask what the machine could not know." The book's closing question — and the hardest one to answer, because the machine's ignorance is invisible in its output.
- The artifact: A sourced research brief on three categories of knowledge that AI systems structurally lack: (1) situated/local knowledge (what's true for this specific student, school, community), (2) tacit knowledge (what experts know but cannot fully articulate), (3) temporal knowledge (what just happened that changes everything). Three categories, one concrete educational example each, sourced. Displayed as a three-panel Manim animation.
- Prompt seed: `claude "Research the three categories of knowledge that AI systems structurally cannot access in educational contexts: (1) situated knowledge — knowledge about specific students, schools, or communities that is not in any training corpus, (2) tacit knowledge — expertise that is held by practitioners but not fully articulable in text, (3) temporal/current knowledge — what just happened that changes the context. For each category: define it precisely, give one concrete educational example where the absence caused a problem, and cite the research or theoretical source for the category."`
- Read / check: Verify that the three categories are theoretically grounded (not just invented) — Polanyi for tacit knowledge, Lave & Wenger or situated cognition literature for situated knowledge. Confirm the educational examples are specific and traceable. Check that the "absence caused a problem" framing is concrete.
- Human supplies (Claude can't): Verification of theoretical sources — Claude may cite Polanyi correctly or may slightly mischaracterize the concept. Human must confirm at least the tacit knowledge citation is accurate.
- Output medium: Manim (three-panel animated table, one panel per knowledge category)
- The change: Ask Claude to describe what a "knowledge gap disclosure" would look like — an AI output that explicitly names what it cannot know about the specific situation. Show what that looks like and why it's rare.
- Teardown angle: The machine's ignorance is invisible in its output. The skill this book teaches is making that ignorance visible — asking what the machine could not know before trusting what it produced.
- Exclusions: Don't go into AI training methodology; don't cover specific AI safety research; don't review EdTech products.
- Score: 7/10
