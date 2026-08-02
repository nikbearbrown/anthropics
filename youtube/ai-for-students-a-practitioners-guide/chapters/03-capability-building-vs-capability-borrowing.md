# Chapter 3 — Capability-Building vs. Capability-Borrowing
*The difference between a tool that grows you and a tool that replaces you.*

> The question is not whether you used AI — it is whether what you did with it increased what you can do independently.

---

Here is a puzzle worth sitting with.

Two students use the same AI tool, on the same subject, for the same number of hours, across the same semester. One of them scores substantially worse on the final exam than students who used no AI at all. The other shows no such loss. If you didn't know what was going on, you might reach for explanations — maybe the first student was lazier, maybe the second was smarter, maybe they used different tools, maybe the hours weren't really the same. But none of that is what happened. The tool was identical. The time was comparable. The students were drawn from the same school, the same classroom, the same socioeconomic distribution. The only variable was the *structure* of how the tool was used. Same tool. Different structure. Opposite outcomes.

That result is not intuitive, and it is worth taking seriously, because it tells you something precise about how learning works — not a vague warning that AI is dangerous, but a specific claim about a specific mechanism. This chapter is about that mechanism.

---

## The Distinction

Let me put the two definitions plainly and then spend the rest of the chapter showing why they are the right definitions.

**Capability-building** is any AI use that increases what you can do independently, without AI, in a novel situation. That's the whole definition. The test is forward-looking and external: could you do a similar-but-new problem without the tool? If yes, something was built.

**Capability-borrowing** is any AI use that produces correct output without the underlying cognitive structure forming in you. The output exists. The capability does not. You rented the performance for the duration of the assignment, and when the assignment was due, the rental terminated.

![Two-column comparison of capability-building and capability-borrowing workflows. Left column shows four steps — attempt cold, get stuck at a specific step, ask AI for a concept-level hint, close AI and finish — ending in a black outcome box reading "a reusable schema." Right column shows paste, read, copy, submit — ending in a brown outcome box reading "nothing transferable."](../images/03-capability-building-vs-capability-borrowing-fig-01.png)
![Same tool, different structure. The four steps decide whether a schema forms or a rental closes.](images/03-capability-building-vs-capability-borrowing-fig-01.png)
*Figure 3.1 — Same tool, different structure. The four steps decide whether a schema forms or a rental closes.*

The distinction is morally neutral on purpose. Capability-borrowing is sometimes exactly what you want. If you ask AI to fix your APA citations, you are borrowing capability — and you should. You weren't going to learn anything from doing that manually, and the mechanical friction around the work isn't what your course is trying to develop. AI handling it frees you for things that matter. The framework becomes load-bearing only when the borrowed capability is the thing your course is actually trying to build. Borrow from your growth domain and you get short-term performance and no schema. The output improves. Your cortex does not.

I also want to be clear that the distinction is independent of academic integrity. You can build capability while breaking a rule. You can borrow capability while following every rule in the handbook. This chapter is not about honesty. It is about a more self-interested question: *are you becoming more capable, or are you becoming dependent on a rental?* Those questions have different answers depending on your study habits, and the answer to the second one is what you will discover when you sit down to an exam.

---

## The Evidence: Bastani et al., 2025

The study I want to build this chapter around is a field randomized controlled trial by Bastani and colleagues, published in *PNAS* in 2025.[^bastani] They worked with roughly a thousand Turkish high school math students and randomized them into three conditions during practice: no AI, standard GPT-4 with no special instructions, and GPT-4 with a system prompt designed to make it behave as a tutor rather than an answer machine. Call these Control, GPT Base, and GPT Tutor. All three groups then took the same unassisted exam.

The numbers are worth stating directly.

During practice, GPT Base students scored about 48% above the control group. Makes sense — the AI was doing a lot of the work. GPT Tutor students scored about 127% above control. The tutor-prompted version was dramatically better during practice, because it was actually pushing students to think harder between interactions, and that thinking was showing up in performance.

Then came the exam. No AI. Same students, same content, now performing alone.

GPT Base students scored seventeen percentage points *below* the control group. Students who had spent the semester with AI help were substantially worse without it than students who had received no help at all. The rental had terminated. The scaffolding had never faded. There was no capability underneath. GPT Tutor students performed at roughly the control level — the decrement was, in the study's language, "largely mitigated."

![Grouped bar chart of three Bastani conditions across two phases. Practice phase shows Control at zero, GPT Base at plus forty-eight percent, GPT Tutor at plus one hundred and twenty-seven percent. Exam phase shows Control at zero, GPT Base at minus seventeen percent, GPT Tutor at zero. An annotation arrow points from a callout reading "the seventeen-point decrement" toward the GPT Base exam bar.](../images/03-capability-building-vs-capability-borrowing-fig-02.png)
![Bastani et al. (2025). GPT Base soars during practice and crashes below control at the unassisted exam; G](images/03-capability-building-vs-capability-borrowing-fig-02.png)
*Figure 3.2 — Bastani et al. (2025). GPT Base soars during practice and crashes below control at the unassisted exam; GPT Tutor holds at the control level. The crossover is the operational signature of the building/borrowing distinction.*

Seventeen percentage points is the operational signature of the building/borrowing distinction in a live classroom over one semester. It is not a theoretical prediction. It is a measured gap. And the explanation the study points to is exactly the mechanism this chapter is about: one group was running an answer-based tutoring system, the other was running a step-based one, and those two structures produce different learning outcomes not because of anything mysterious but because of what was happening inside the students' heads during practice.

---

## Why Structure Matters: VanLehn 2011

The reason this works is old enough to predate AI by decades. Kurt VanLehn's 2011 meta-analysis in *Educational Psychologist* classified tutoring systems by what he called *granularity* — the size of the cognitive step the student takes between interactions with the tutor.[^vanlehn]

Answer-based systems see the student's final answer and respond to it. The student does the whole problem; the system says right or wrong. Step-based systems interrupt between cognitive sub-goals. The student does the first step, the system responds, the student does the second step, and so on. The student is never in a passive position for long; the gaps between tutor interactions are short enough that the student is always doing real cognitive work.

The meta-analytic effect sizes, against no-tutoring controls:

| Tutoring type   | Effect size (d) | What the student does between interactions                    | Schema formation       |
| --------------- | --------------- | -------------------------------------------------------------- | ---------------------- |
| Answer-based    | ≈ 0.31          | Solves the whole problem, then receives feedback on the answer | Low                    |
| Step-based      | ≈ 0.76          | Solves one sub-step, then receives feedback at the sub-goal    | High                   |
| Human 1:1       | ≈ 0.79          | Works with a tutor at every sub-step, in real time             | High                   |
| Substep-based   | ≈ 0.40          | Works at the working-memory level on micro-operations          | Moderate (past plateau) |

*Table 3.1 — VanLehn (2011) meta-analytic effect sizes against no-tutoring controls. Step-based ≈ 2.5× answer-based and approaches human 1:1. Substep-based comes in lower than step-based — finer is not always better. The granularity payoff plateaus at step-level.*

Step-based: **d ≈ 0.76.** Answer-based: **d ≈ 0.31.** Human tutoring: **d ≈ 0.79.** Roughly 2.5× the effect size for step-based over answer-based, with step-based approaching the effectiveness of one-on-one human tutoring.

One thing to flag, because the literature gets this wrong sometimes: VanLehn also looked at substep-based systems — tutors that modeled even finer cognitive grain, down to working-memory operations at the moment of decision. Prior theory predicted this would be even better. The actual finding was that the granularity payoff *plateaus* at step-level. Substep systems came in at around d ≈ 0.40, lower than step-based, not higher. The directional claim that survives — *step-based beats answer-based by a factor of 2.5* — is well-supported. The "finer is always better" claim is the one the review refuted.

The practical translation is immediate. If you use AI by pasting a problem and reading the solution, you are running yourself through an answer-based system. d ≈ 0.31. If you use AI by attempting a problem, getting stuck at a specific step, and asking for a hint about the *concept behind* that step — not the answer, the concept — you are running a step-based system. d ≈ 0.76. The same tool. Different granularity structure. The Bastani numbers map almost directly onto this framework: GPT Base was answer-based; GPT Tutor was step-based. The 17-point decrement vs. no decrement is what VanLehn would have predicted.

---

## The Transfer Test

If capability-building is forward-looking, you need a test that looks forward. The test is old; it predates AI by a long way. Sharon Barnett and Stephen Ceci gave it its most careful taxonomy in a 2002 *Psychological Bulletin* paper.[^barnett] The version I want is the practical one.

Transfer is the application of learning in a context different from the original learning context. Near transfer: same underlying structure, different surface story. You learned related rates with a ladder problem; you are tested with a water-tank problem. Far transfer: different domain, different surface, and you have to recognize that the principle applies at all. Far transfer is famously hard to demonstrate. Near transfer is hard enough.

![A horizontal arrow runs left to right with four labelled nodes — Original, Near Transfer, Mid Transfer, Far Transfer — each accompanied by a small example box. Original shows a ladder-related-rates problem; near transfer shows a water-tank problem; mid transfer shows physics kinematics; far transfer shows economics marginal cost. A gradient band beneath the arrow darkens to lighten, suggesting decreasing visibility of the underlying principle as the surface drifts.](../images/03-capability-building-vs-capability-borrowing-fig-03.png)
![The transfer spectrum (after Barnett & Ceci 2002). Same capability, different surface. The transfer test ](images/03-capability-building-vs-capability-borrowing-fig-03.png)
*Figure 3.3 — The transfer spectrum (after Barnett & Ceci 2002). Same capability, different surface. The transfer test removes AI and asks what remains.*

Here is the test applied to any AI-assisted task:

1. Identify the underlying capability — not the specific output, the *capability*. If you did a related-rates problem, the capability is "setting up and solving related-rates problems." If you wrote a thesis paragraph on Reconstruction, the capability is "constructing a defensible historical argument from sources."
2. Construct a parallel task: same capability, different surface. New numbers, new sources, new cover story.
3. Without AI, in timed conditions, attempt the parallel task.
4. Pass or fail.

Pass: capability was built. Fail: it was borrowed. There is no third option. The test bypasses the fluency trap — the phenomenon, which Chapter 2 established, that working alongside AI produces exactly the feeling of understanding without the understanding. The feeling lives in the assisted performance. The transfer test removes the assistance and asks what remains.

One objection comes up constantly: "Doing the parallel problem with AI would also show me whether I understand it." No. Doing the parallel problem with AI is structurally identical to doing the original problem with AI. The AI is still doing the cognitive work. The transfer test exists precisely because the AI must be absent. If you can't bring yourself to remove it, that is itself information about what you are afraid to find.

---

## What Step-Based AI Looks Like: The Kestin Harvard Physics Result

The Bastani GPT Tutor arm told us that step-based AI can prevent the 17-point decrement. A second study told us what happens when you engineer step-based AI well from scratch and measure it against the strongest available baseline.

Greg Kestin and colleagues at Harvard ran a within-subjects RCT in Physical Sciences 2, the university's largest introductory physics course.[^kestin] Students were randomized each week to either a standard in-class active-learning session with trained instructors — already the best-evidence instructional condition available — or a self-paced session with a GPT-4 tutor engineered around seven specific design principles. Topics were the same in both conditions; pre- and post-tests on identical items measured normalized learning gains.

The headline result: median learning gains in the AI-tutored condition were more than double those in the active-learning condition. Students spent less time on the AI-tutored material and reported higher engagement.

I want to be precise about what that means and doesn't mean. "Double the median gain" is the median, not the mean, so the typical student saw more than twice the learning gain — but the distribution matters and individuals varied. The comparison is against active-learning instructors, not lecture, which is an unusually strong baseline. And the study covers one unit of one course at one university with high-preparation students. The right reading is: *when AI is engineered around step-based scaffolding and a set of principled design choices, it can outperform even very strong human instructional baselines on the specific tasks it was built for*. Not "AI replaces teachers."

The seven design principles Kestin's team used are worth naming because they are reproducible:

| Principle                       | What it means in practice                                       | What this forces the student to do                       |
| ------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------- |
| Avoid giving away solutions     | Guide, never hand over the worked answer                        | Generate the step themselves                             |
| Step-by-step guidance           | Interrupt at sub-goals, not at the end of the problem           | Commit to a partial attempt before getting feedback      |
| Brief targeted responses        | Address the specific point of confusion, not the whole problem  | Localise their own gap and pose a narrow question        |
| Growth-language framing         | Treat ability as developable; no "you're not good at this"      | Stay engaged after a wrong step instead of disengaging   |
| Cognitive load management       | Avoid information dumps; one idea at a time                     | Process each idea fully before the next arrives          |
| Pre-loaded expert content       | Constrain the model with vetted material to limit hallucination | Trust the substrate so they spend effort on the concept  |
| Student-controlled pace         | Learner sets the tempo, no forced auto-advance                  | Decide when they understand and when to ask again        |

*Table 3.2 — Kestin et al. (2025) — the seven principles behind the Harvard PS2 tutor. None of them produce an answer the student can copy. All seven force cognitive work onto the learner.*

The tutor was instructed to avoid giving away solutions, to guide students through problems step by step, to give brief targeted responses at the specific point of confusion rather than end-of-problem summaries, to use language that treats ability as developable rather than fixed, to manage cognitive load by avoiding information dumps, to pre-load expert-authored content to constrain hallucination, and to let students control pace. All seven of these require the student to do cognitive work. None of them produce an answer the student can copy. The tutor was not solving problems — it was running structured interactions that forced the student to solve them.

---

## The Deeper Frame: Germane Load and Scaffolding That Fades

Two older frameworks from learning science make the building/borrowing distinction precise enough to act on.

The first is Cognitive Load Theory, developed by John Sweller and colleagues since the 1980s and most recently restated in 2019.[^sweller] Sweller's framework partitions the demand on working memory into three types. Intrinsic load is the inherent difficulty of the material — calculus is harder than arithmetic and there is nothing you can do about that except sequence it. Extraneous load comes from how the material is presented: bad notation, irrelevant detail, confusing layout. This can be reduced by better design. Germane load is the load that contributes to schema construction. This is the load you *want* to bear, because bearing it is the mechanism of learning.

![A stacked working-memory bucket on the right with a hard ceiling line above it. Three bands inside, bottom to top: intrinsic load in black, extraneous load in grey, germane load in red. On the left, a labelled box reading "AI assistance." Two arrows leave the box: one solid arrow points into the extraneous band labelled "reduces extraneous (good)"; one dashed red arrow points into the germane band labelled "reduces germane (capability-borrowing)."](../images/03-capability-building-vs-capability-borrowing-fig-04.png)
![Sweller's three loads share one ceiling. AI is a faucet pointed at the bucket; you choose which load it d](images/03-capability-building-vs-capability-borrowing-fig-04.png)
*Figure 3.4 — Sweller's three loads share one ceiling. AI is a faucet pointed at the bucket; you choose which load it drains.*

The rule: reduce extraneous, preserve germane. AI can reduce either kind, and reducing the wrong one is the precise mechanism of capability-borrowing. When AI handles formatting and citation lookup and background summary, it is taking extraneous load — the friction around the learning, not the learning. When AI handles the synthesis, the argument formation, the interpretation of data, it is taking germane load — the work that would have built the schema. The artifact improves. The cortex does not.

The second framework is scaffolding, from Vygotsky's zone of proximal development and operationalized by Wood, Bruner, and Ross in 1976.[^scaffolding] The scaffolding concept has a second word that usually gets dropped: *fading*. Real scaffolding fades. The support is provided within the zone of proximal development and removed as competence grows. The endpoint is independent performance. A scaffold that never fades is not a scaffold — it is a permanent crutch wearing the word "scaffold" for respectability.

AI does not automatically fade. The tool is always available at the same intensity. If you start using it for a task and your competence grows, the AI does not notice this and reduce its contribution. It continues giving you exactly the same depth of answer. You have to impose the fading yourself, deliberately, because the tool will not do it. The phase gate in Chapter 4 is how you impose it: a specific point in each workflow where you close the AI and your own processing takes over, with the boundary explicitly defined and moved closer to the start of the problem as your competence increases.

---

## What Actually Happened With Those Two Students

Earlier chapters introduced Student A and Student B. I want to return to them now with the framework in hand, because the story reads differently once you know what you are looking at.

Student A used AI to generate summaries, produced flashcards from the summaries, and reviewed the flashcards before tests. Her test grades were excellent. Her notes were clean. She felt prepared. She was running an answer-based system on germane-load tasks: every study session was a *consumption event*. Read the output, encode the output, reproduce the output on a matching test. No argument was formed. No thesis was constructed. No counter-evidence was considered. The AI removed all germane load every time she opened it.

Student B wrote rough drafts and asked AI to argue against her. She generated practice prompts and answered them cold before checking. Her sessions were *production events*. The AI played critic and prompt-generator — roles that require the student to do the cognitive work the roles are structured around. She built schemas for argument construction, not schemas for summary retrieval.

| Dimension                       | Student A — capability-borrowing       | Student B — capability-building              |
| ------------------------------- | -------------------------------------- | -------------------------------------------- |
| Session type                    | Consumption event                      | Production event                             |
| AI role                         | Generator (writes summaries, answers)  | Critic and prompt-generator                  |
| Cognitive load taken by AI      | Germane (synthesis, argument)          | Extraneous (formatting, lookup, scaffolding) |
| Tutoring granularity            | Answer-based                           | Step-based                                   |
| Scaffolding fading              | Never — tool stays at full intensity   | Deliberately imposed by closing the AI       |
| Transfer test result            | Fail — no parallel-task performance    | Pass — handles a new surface cold            |
| AP exam (DBQ) score             | 3                                      | 5                                            |
| **Summary**                     | **The variable was not effort, intelligence, or time — it was interaction structure.** | |

*Table 3.3 — Student A vs. Student B. Same tool, same time, same school. The two-point gap is the transfer-test result of a year of studying.*

The AP exam's DBQ — the document-based essay, which asks students to construct a historical argument from primary sources they've never seen, under time pressure, with nothing but their own head — does not test summary retrieval. It tests argument construction. Student A did not have a schema for that operation. Student B did. The 2-point score gap (a 3 versus a 5) is the transfer-test result of a year of studying.

The variable was not effort. It was not intelligence. It was not even, precisely, time. It was the cognitive structure of the interactions with the tool: answer-based vs. step-based, extraneous load taken vs. germane load taken, scaffold that never faded vs. scaffold that faded every time she pressed herself cold.

---

## A Note on the Limits of This Framework

The building/borrowing distinction is clean for tasks where the underlying capability is well-defined and the test conditions can be made sharp. It is less clean for diffuse capabilities — deep reading comprehension, conceptual understanding in philosophy, the kind of judgment that develops from years of clinical exposure. What parallel task operationalizes "I deeply understand this argument"? The chapter can tell you to construct one; constructing the right one is genuinely hard and the book will work through specific cases later.

The boundary between germane and extraneous load is sharp in theory and fuzzy in practice. The same task — reading the background section of a chemistry paper — is extraneous load for a senior chemistry major and germane load for a freshman. The framework is conditional on what you are trying to build. That context-dependence is not a weakness in the framework; it is a feature. It means you have to think about what your growth domain actually is, which is thinking you should be doing anyway.

The compounding claim — that the gap between a capability-builder and a capability-borrower grows larger over years — is the most extrapolated piece of the argument. The mechanism makes it plausible. Bastani covers one semester; Kestin covers one unit. The longitudinal evidence does not yet exist. Treat the compounding argument with appropriate skepticism until it does.

---

## Bridge to Chapter 4

The framework this chapter establishes runs the rest of the book. Capability-building increases what you can do independently. Capability-borrowing produces output without the increase. The transfer test is the diagnostic. The Bastani and Kestin evidence are existence proofs that the structure of the interaction — not the tool itself — determines the learning outcome. The deeper frame from Sweller and Vygotsky tells you where the boundary should sit: AI takes extraneous load, you bear germane load, the scaffolding fades.

These are the right principles. This chapter gives you them conceptually. Chapter 4 makes them structural by locating a specific point in each workflow — the phase gate — where AI processing stops and your cognitive work begins. The gate is not a commitment to use AI responsibly. It is a specification: AI handles this, I handle that, the line is here, and the line moves as I become more capable. For every subject and task type in Part III, that gate sits in a different specific place. But the move is always the same: name the cognitive event that constitutes the learning, draw a line in front of it, and put the AI on the other side of the line.

---

## Exercises

### Warm-Up

**1.** In your own words, state the transfer test. What two things must be true for the test to count as evidence of capability-building? *(Tests the core definition — no framework vocabulary allowed in your answer; use plain language.)*

**2.** A student uses AI to generate an outline for a history essay, then writes the paragraphs herself from the outline without looking at the AI again. Classify this as capability-building, capability-borrowing, or a mix of both. Name which part of the cognitive load framework explains your answer. *(Tests germane vs. extraneous load distinction.)*

**3.** VanLehn found that substep-based tutoring produced a *lower* effect size than step-based tutoring. What prior assumption did this result overturn, and what is the practical implication for how granular your AI interactions should be? *(Tests precise reading of the VanLehn findings — the answer is not "finer is better.")*

---

### Application

**4.** You are learning to write Python functions and you have been using AI by pasting a problem and reading the solution. Design a specific restructuring of this workflow that moves you from answer-based to step-based interaction. Your answer should name: (a) what you do before opening AI, (b) the exact form of the question you ask AI, and (c) the point at which you close the AI and work alone. *(Tests translation of granularity framework to a concrete study practice.)*

**5.** You are studying for an exam on cell biology and you have been using AI to generate summaries of each chapter. Using the Sweller framework, identify which load category the summary-generation is reducing, and explain whether that is the right load to reduce for the cognitive capability your exam will test. Then propose one change that would redirect AI toward a different load category. *(Tests germane vs. extraneous distinction applied to a realistic study scenario.)*

**6.** Construct a near-transfer test for one skill you are currently learning — in any subject. Your answer must name the underlying capability (not the specific task), the original task you practiced, and the parallel task you would use for the test. Explain why the parallel task tests the same capability and not just the same surface content. *(Tests the student's ability to operationalize transfer — the hardest practical move in this chapter.)*

---

### Synthesis

**7.** Bastani found that GPT Base produced a 17-point decrement at the unassisted exam, while GPT Tutor produced no significant decrement. Using the VanLehn granularity framework and the Sweller load framework together, explain why the two conditions produced different outcomes — not just at the level of "one was step-based and one wasn't" but at the level of what was happening cognitively in the student during each type of practice session. *(Tests integration of both frameworks against the primary evidence.)*

**8.** Vygotsky's scaffolding concept requires fading; AI does not fade automatically. A student argues that this is actually fine: "I can just choose not to use AI as I get better." Evaluate this argument. What does it get right? What does it get wrong? What structural commitment would need to be in place for the argument to hold? *(Tests understanding of the fading problem and why voluntary restraint is insufficient without a structural solution — bridges to Chapter 4.)*

---

### Challenge

**9.** The chapter claims that the building/borrowing distinction is "less clean for diffuse capabilities" such as philosophical understanding or clinical judgment. Design a protocol that would let a student run something like a transfer test on a diffuse capability — one where there is no obvious parallel problem with a right answer. Your protocol should specify: how you define the capability, how you construct an analog task, what counts as evidence that the capability transferred, and what the main weakness of your protocol is. *(Open-ended — there is no single right answer; tests whether the student can extend the framework past its stated limits.)*

---

## LLM Exercises

**Exercise: Build Your Own GPT Tutor.** Write a system prompt for one subject you are currently studying. The prompt should refuse to give direct answers, ask Socratic questions, target step-level granularity, and give feedback after your attempt rather than instead of it. Use the prompt for two weeks. Before you start, run a transfer test on a parallel problem — no AI, timed conditions. After two weeks, run the same transfer test again. Document the change. Chapter 5 gives you templates if this feels too open-ended; the point here is to start the experiment early so the data exist by the time you read that chapter.

---

**Tags:** #capability-building #capability-borrowing #bastani #kestin #vanlehn #transfer-test #cognitive-load #scaffolding

---

## AI Wayback Machine

The capability-building idea didn't start with cognitive load theory. **John Dewey (1859–1952)** was already saying most of it in 1916. Dewey's central claim — *we do not learn from experience, we learn from reflecting on experience* — is the same distinction this chapter draws between consumption events and production events. A student who pastes a problem into AI and reads the solution has had an experience. A student who attempts the step, gets stuck, isolates the gap, asks AI about the concept, and then finishes alone has reflected on one. Dewey called the first *passive reception* and the second *active inquiry*. He warned, a century ago, that schools were good at producing the first and rare at producing the second. The framework in this chapter is, more or less, Dewey re-derived with effect sizes attached.

![John Dewey, circa 1902. AI-generated portrait based on a public domain photograph (Wikimedia Commons).](../images/john-dewey.jpg)
*John Dewey, circa 1902. AI-generated portrait based on a public domain photograph.*

![John Dewey (1859–1952)](../images/john-dewey-7x5.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was John Dewey, and how does his idea that "we learn by doing — and
by reflecting on what we did" connect to the capability-building vs
capability-borrowing distinction in this chapter? Three paragraphs.
End with the single thing about Dewey's career or thought that most
surprises you.
```

→ Search **"John Dewey"** on the Stanford Encyclopedia of Philosophy or Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask the model to map Dewey's *Experience and Education* (1938) onto a real AI-assisted study session you ran this week. What was experience? What was reflection? Where did the workflow collapse the two?
- Ask the model what Dewey would say about a student who runs Student A's workflow with perfect grades. Does the schoolwork count as education?

What changes? What gets better? What gets worse?

---

## Footnotes

[^barnett]: Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin*, 128(4), 612–637. <https://pubmed.ncbi.nlm.nih.gov/12081085/>

[^bastani]: Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122. <https://www.pnas.org/doi/10.1073/pnas.2422633122>

[^bastanicorrection]: PNAS correction: <https://www.pnas.org/doi/10.1073/pnas.2518204122>

[^vanlehn]: VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221. <https://eric.ed.gov/?id=EJ946764>

[^kestin]: Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports*, 15, Article 17458. <https://www.nature.com/articles/s41598-025-97652-6>

[^sweller]: Sweller, J., van Merrienboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review*, 31, 261–292.

[^scaffolding]: Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100. Vygotsky's foundational concept of the zone of proximal development appears in Vygotsky, L. S. (1978). *Mind in Society*. Harvard University Press.

[^ma]: Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *Journal of Educational Psychology*, 106(4), 901–918. <https://www.apa.org/pubs/journals/features/edu-a0037123.pdf>

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 3.1 — Same tool, different structure. The four steps decide whether a schema forms or a rental closes.

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Same tool, different structure. The four steps decide whether a schema forms or a rental closes.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/03-capability-building-vs-capability-borrowing-fig-01.html`

---

### Figure 3.2 — Bastani et al. (2025). GPT Base soars during practice and crashes below control at the unassisted exam; G

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Bastani et al. (2025). GPT Base soars during practice and crashes below control at the unassisted exam; G". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/03-capability-building-vs-capability-borrowing-fig-02.html`

---

### Figure 3.3 — The transfer spectrum (after Barnett & Ceci 2002). Same capability, different surface. The transfer test 

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "The transfer spectrum (after Barnett & Ceci 2002). Same capability, different surface. The transfer test ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/03-capability-building-vs-capability-borrowing-fig-03.html`

---

### Figure 3.4 — Sweller's three loads share one ceiling. AI is a faucet pointed at the bucket; you choose which load it d

Create a standalone D3 v7 HTML file for a concept map titled "Sweller's three loads share one ceiling. AI is a faucet pointed at the bucket; you choose which load it d". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/03-capability-building-vs-capability-borrowing-fig-04.html`
