# Chapter 13 — Academic Integrity, Privacy, and Honest Use

## TL;DR

- The professor who referred 23% of her students taught less that semester than at any point in her career.
- The chapter moves through Why detection cannot work, The Bastani result: what it actually says, What makes an assignment AI-survivable, A research paper, redesigned, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The professor who referred 23% of her students taught less that semester than at any point in her career. Her students learned less. The detector was not the wrong tool for the right job. It was the right tool for the wrong job.*

---

*Detection is the right tool for the wrong job. Design is the right tool for the right job.*

---

Here is a thing that happened, and it happened at a lot of institutions at once.

A writing professor built a workflow in August. It seemed proportional. Every essay through a commercial AI detector. Flagged papers re-read by hand. Papers that still looked AI-generated after the second read referred to Academic Integrity. She would document everything. She would not accuse without evidence. It was a reasonable response to a real problem.

By December she had referred 23% of her students.

Three were formally contesting the referrals — a senior whose graduation was contingent on the outcome, a returning adult who came to office hours crying, a sophomore whose father was an attorney. The Office of Academic Integrity was not staffed for that volume. The appeals would take four weeks. During those four weeks she stopped accepting late work because the policy felt arbitrary against the backdrop of the detection regime. She stopped writing the marginal comments she used to be proud of, because every comment felt like preparation for a hearing. Her course evaluations came back. Students who used to describe her as demanding now described her as suspicious.

She had taught less that semester than at any point in her career. Her students had learned less.

The detector was not the wrong tool for the right job. It was the right tool for the wrong job. The job she was solving was *catch the students who cheated.* The job she needed to solve was *design the assessment so that cheating and learning are not the same task.* By picking up the detector, she made the second job harder — every hour in the detection workflow was an hour not spent redesigning the assignment.

This chapter is the redesign.

---

## Why detection cannot work

![Three stacked horizontal rows, each a failure mode of AI-text detection: row one names tools as unreliable with the Weber-Wulff 2023 anchor and the OpenAI 26% withdrawal note; row two names errors as biased with the Liang 2023 anchor and the >50% TOEFL misclassification; row three names institutions walking back with the Vanderbilt arithmetic 1% × 75,000 = 750 wrongly flagged. A footer notes each row is independent.](../images/13-academic-integrity-privacy-and-honest-use-fig-01.png)
![Three independent failure modes. Any one is enough to disqualify detection as a primary tool; together th](images/13-academic-integrity-privacy-and-honest-use-fig-01.png)
*Figure 13.1 — Three independent failure modes. Any one is enough to disqualify detection as a primary tool; together they constitute a settled case.*

There are three separate reasons, and they are independent — any one of them is enough.

The first is that the tools are unreliable on their own terms. Weber-Wulff and colleagues (2023), publishing in the *International Journal for Educational Integrity*, tested twelve detection tools across 756 cases and concluded the tools are "neither accurate nor reliable," exhibiting systematic bias toward classifying outputs as human-written when subjected to even mild adversarial conditions — paraphrasing, translation, light editing. The strongest evidence came from OpenAI itself. The company launched its AI Text Classifier on January 31, 2023, and withdrew it on July 20, 2023, citing a "low rate of accuracy" — the classifier correctly identified AI-written content only 26% of the time. The company that makes GPT could not reliably detect GPT output. That is the most concise statement of the technical problem available.

The second is that the errors are biased. Liang and colleagues (2023), in the peer-reviewed Cell Press journal *Patterns*, tested seven widely-used GPT detectors on TOEFL essays written by non-native English speakers and on essays written by U.S. eighth-graders. The detectors achieved near-perfect accuracy on the eighth-grade essays. They misclassified more than half of the TOEFL essays as AI-generated.

The mechanism is plain. Detectors look for low text perplexity — prose that is too predictable. Large language models produce low-perplexity text by construction. So do non-native English writers, for entirely different reasons: a narrower vocabulary, more conventional phrasings, less surprising word order. The detector cannot distinguish "writing the model produced" from "writing that does not surprise the model." Those are different things. The detector treats them as identical. The error is not random noise. It is systematically allocated to multilingual students — which is to say, to a protected class.

The equity argument and the technical argument coincide here, and the chapter is not going to soften the coincidence. A detector that misclassifies multilingual students' writing at five times the rate of native speakers is making a measurement error and a civil-rights problem in the same operation.

The third reason is that serious institutions have done the arithmetic and walked back. Vanderbilt disabled the Turnitin AI detector in August 2023 and published the reasoning. The load-bearing piece was simple multiplication: Vanderbilt processed about 75,000 student papers through Turnitin in 2022. Turnitin's own published false-positive rate at launch was approximately 1%. One percent of 75,000 is 750 wrongly-flagged students. The Office of Student Accountability would not have the bandwidth to adjudicate 750 contested cases honestly. Vanderbilt's stated alternative was investing in pedagogy and assignment design.

The pattern is not unique to Vanderbilt. Yale, Johns Hopkins, Northwestern, and others have followed. OpenAI's withdrawal was not a business decision. These are institutions that tried detection first and concluded it was not the right layer.

Even if all three problems were solved tomorrow — the tools became reliable, the bias disappeared, the institutional capacity materialized — detection would still fail the design problem. A perfect detector finds the artifact and stops. It does not tell you what to do about an educational system where the artifact is no longer evidence of learning. The question detection cannot answer is: what should writing instruction *do* in a world where a student with a chat window can produce a passable essay in twenty seconds? Design answers that question. Detection does not.

---

## The Bastani result: what it actually says

![Grouped bar chart comparing three conditions (Control, GPT Base, GPT Tutor) on two outcomes: practice performance and unaided exam score. The GPT Base practice bar rises 48% above control while its exam bar drops 17 points below; the GPT Tutor practice bar rises 127% above control while its exam bar stays at the control level. Callouts annotate each gap.](../images/13-academic-integrity-privacy-and-honest-use-fig-02.png)
![The Bastani result. Same model. Same students. The only variable was the pedagogical wrapper around the p](images/13-academic-integrity-privacy-and-honest-use-fig-02.png)
*Figure 13.2 — The Bastani result. Same model. Same students. The only variable was the pedagogical wrapper around the prompt.*

Before arriving at the design, there is one study that has to be understood precisely, because popular summaries have garbled it in both directions.

Bastani, Bastani, Sungu, Ge, Kabakcı, and Mariman (2025) ran a field experiment in a Turkish high school, approximately a thousand students across grades 9–11, multi-week math curriculum, random assignment to three conditions: a no-AI control, a "GPT Base" condition where students could use GPT-4 in a standard ChatGPT-style interface during practice, and a "GPT Tutor" condition where the same model was wrapped in a teacher-designed system prompt that refused to give complete answers and structured the interaction so the student had to externalize a reasoning step before the model advanced.

During practice, with AI available: GPT Base students performed 48% higher than the control. GPT Tutor students performed 127% higher than the control.

On the post-practice exam, with no AI available: GPT Base students scored 17 percentage points lower than the no-AI control. GPT Tutor students were statistically indistinguishable from the control.

Same underlying model. Same students, randomly assigned. Opposite durable-learning outcomes. The only variable was the wrapper — the pedagogical commitments in the system prompt.

Three precision moves before going further.

The harm is 17 percentage points, not 17 percent. On the scale of the exam, that is roughly half a standard deviation of durable learning. Popular summaries sometimes garble this.

The 127% practice gain in the tutor condition is not a footnote. It is a finding of equal weight to the 17-point loss. The Bastani study is not "AI harms learning." It is *unguarded AI harms durable learning while appearing to help in the moment, and guarded AI does not.* The distinction is the whole thing.

This is one study, one country, one subject. The strongest current evidence, but not settled science. Hold the conclusion with the certainty the evidence supports — strong, not absolute.

The mechanism the numbers exhibit is what the Preface calls the *performance paradox*: in-session performance with AI assistance feels like learning. The answers are right; the work is moving; the affect is positive. The brain receives a different signal — no prediction error, no effortful retrieval, no consolidation. Robert and Elizabeth Bjork's storage-versus-retrieval distinction is the backbone: storage strength (what is encoded) and retrieval strength (what feels fluent right now) come apart. AI-assisted practice can raise retrieval strength in the moment while leaving storage strength essentially flat. The student's confidence was an unreliable signal. It always was. AI made the signal louder.

A teaching analogy that holds up to pressure: a teacher hands a student a calculator before they understand division. The student gets every problem right on the worksheet. Two weeks later, no calculator. The student has produced a perfect worksheet and learned nothing. The artifact was the output; the learning was the process; the calculator bypassed the process. AI is the calculator at scale, and the worksheet has gotten longer. The analogy breaks down in one place worth naming: calculators do not confabulate, and AI does. The verification burden the analogy hides is the new skill the curriculum has to teach.

---

## What makes an assignment AI-survivable

If detection cannot work, what does? The answer is design: assignments built so the artifact alone cannot stand as evidence of learning. The artifact must come with the process that produced it, or be performed under conditions where the process is visible.

An assignment is AI-survivable if a student who outsources the entire artifact to AI is detectably worse off than a student who did the work — without requiring detection software.

![A five-stage vertical decision tree of diagnostic questions, each as a yes/no branch — defense in conversation, novel application beyond training cutoff, process trail required, real-time unassisted performance, would a good artifact alone reveal learning. Five yes nodes converge on an AI-survivable terminal; any no branches to a redesign-target terminal with a smallest-move callout.](../images/13-academic-integrity-privacy-and-honest-use-fig-03.png)
![The five-question diagnostic. Run this on one assignment at a time. The goal is the smallest move that co](images/13-academic-integrity-privacy-and-honest-use-fig-03.png)
*Figure 13.3 — The five-question diagnostic. Run this on one assignment at a time. The goal is the smallest move that converts a "no" to a "yes."*

Five questions do the diagnostic work:

Does the assignment require the student to defend claims in conversation? Does it require applying concepts to a situation that did not exist when any model was trained? Does it require a process trail — drafts, annotations, decision records? Does it require real-time, unassisted performance? If a student used AI freely and produced a good artifact, would you know whether they learned anything?

Work through what each question is actually testing.

**Defending claims in conversation.** AI produces text. It cannot sit through an oral examination on a paper it did not write. The student who can defend the claims in real time has the mental model. This is the move pre-AI doctoral defenses have always made. It generalizes downward to a high-school history class as well as a graduate seminar. The cost is class time and emotional load — defenses are stressful, particularly for students with test anxiety or processing differences. The trade-off is real.

**Novel application.** The model has a training cutoff. Apply the concept to a specific event from last month, to a dataset the class collected this week, to a reading the AI has not absorbed, and the transfer cannot be pre-baked. This is not AI-proof — students can paste the new material into the prompt — but it raises the floor: the student must at least describe the new situation accurately to get useful output. The cognitive work of encountering the situation and recognizing what is and is not analogous is the work the assignment surfaces.

**Process documentation.** The artifact used to be proof of the process. It no longer is. So the process must become its own proof. Drafts dated and submitted across weeks. Annotations on sources in the student's voice. A short decision record at each revision. The portfolio-based writing traditions have been doing this for thirty years. AI makes it necessary rather than optional.

**Real-time performance.** In-class writing. Whiteboard work. Oral defenses. The phase gate enforced by the room. This is the highest-friction option and the most legally defensible. It is also the option that disadvantages students who think slowly under pressure. A defensible regime uses real-time performance as one component, not the entire assessment.

**The diagnostic question.** If a student used AI freely and produced a good artifact, would you know whether they learned anything? This is the question the professor in the opening case never asked. If the answer is no, the assessment is measuring artifact quality, not learning. Bastani's GPT Base students produced 48% better practice performance and learned 17 points less. An assignment that cannot distinguish those students from the no-AI group is the assignment Bastani's intervention destroyed.

The framework is not *make assignments AI-proof.* Nothing is AI-proof at the artifact level. The framework is *make assessments that observe the learning, not just the artifact.*

---

## A research paper, redesigned

| Checklist question | Before — 1865–1945 research paper | After — historical-current connection + portfolio |
|---|---|---|
| Defense in conversation? | No — submitted artifact only | Yes — 10-minute Week-4 defense conference |
| Novel application beyond training cutoff? | No — 1865–1945 is deep in training | Yes — link to a current event from the last 12 months |
| Process trail required? | No — final paper only | Yes — topic memo, annotated bib, draft + reflection, disclosure |
| Real-time unassisted performance? | No — written outside class | Yes — in-class paper topic memo + live defense |
| Would good artifact alone reveal learning? | No — passable AI paper indistinguishable | Yes — portfolio + defense provide independent observations |

*Table 13.1 — The five-question checklist applied to the same assignment, before and after. The redesign does not ban AI; it changes what AI is useful for inside the assignment.*

Take one assignment nearly every teacher reading this has given some version of. A research paper. Before, why it fails, what changes when the checklist is applied.

**Before.** Choose a topic from American history between 1865 and 1945. Write a 1,500–2,000-word research paper using at least five academic sources. Make an argument. Cite using Chicago style. Due in four weeks.

This is a well-written assignment by every pre-2022 measure. Apply the checklist: no defense conversation, no novel application (1865–1945 is deeply in every model's training data), no process documentation, no real-time performance, and the artifact alone is not diagnostic. Five no's. A student can produce a passable paper through the AI pathway and the teacher cannot tell.

**After.** Choose a topic from American history between 1865 and 1945 that connects to one event or trend from the last twelve months in our local community, state, or national news. A paper on the 1934 Reciprocal Trade Agreements Act might connect to a current trade dispute. A paper on the 1908 White House Conservation Conference might connect to a local land-use decision currently before the city council. Write a 1,500–2,000-word paper using at least five academic sources. Make an argument that explicitly links the historical material to the current event you chose.

Required process portfolio, submitted with the final paper: a one-page topic memo due in class on paper in Week 1 naming the historical topic, the current event, and the connection you intend to argue; an annotated bibliography due Week 2 with two sentences per source in your own voice; a full draft with a 200-word reflection memo in Week 3 identifying what you still do not know and what you plan to change; an AI use disclosure naming any tool used and what you used it for; a 10-minute defense conference in Week 4 in office hours.

Apply the checklist to the redesign: defense conference, yes. Novel application through the link to a current event, yes. Process documentation across four submission points, yes. Real-time performance through the in-class topic memo and the defense, yes. The artifact is diagnostic because the portfolio and the conference each provide independent observations of the student's mental model, yes.

Five yes's.

The redesign costs something. The assignment has more parts. The grading involves more submissions. The defense conference takes ten minutes per student. What it does not cost is the detection-and-discipline workflow the professor in the opening case spent her semester on. The trade is good.

The limit is honest. This works for a seminar of twenty-five. It requires structural adaptation for 150 students — capstone defense rather than every paper, peer defense with the teacher observing, written meta-analytical memos as a defense-shaped artifact when live conversation is not possible. The partial implementations are real. So is the cost.

---

## Privacy: the operating habits that keep your AI use legal

| Routine AI use | Stop and check |
|---|---|
| Generating practice problems, no student names in prompt | Summarizing a specific student's progress report — FERPA disclosure |
| Drafting feedback on de-identified work | Pasting names and grades into a free consumer LLM — FERPA violation |
| Building a slide outline on a public topic | Sharing a roster, IEP, or 504 plan with an unvetted tool — FERPA / IDEA |
| Translating an anonymized parent message into another language | Setting up shared consumer logins for students under 13 — COPPA violation |
| Producing differentiated practice from a generic prompt | Using a tool with no Data Processing Agreement on identifiable records |

*Table 13.2 — The distinction is not which tool you use. It is whether identifiable student information leaves your control.*

The legal layer has to be present and principle-level. What follows is not legal advice. The specifics are state-variable, district-variable, contract-variable, and changing month by month. What the chapter can give you is the set of operating habits that keep most everyday teacher AI use defensible, and the moments to stop and call counsel.

FERPA — the Family Educational Rights and Privacy Act — protects education records containing personally identifiable student information. Three principles are defensible.

Identifiable student data submitted to a consumer AI tool is a disclosure to a third party. A free ChatGPT, Claude, or Gemini account that has no data-processing agreement with your school is a third party with no authorization to receive the record. When you paste a student's name and grade into the prompt window, you have made the disclosure. The act is small. The legal frame is not.

The "school official" exception requires a contract. FERPA allows disclosure to a school official with legitimate educational interest, and extends this to external vendors only when the vendor is under the direct control of the school with respect to the use and maintenance of the records. A signed Data Processing Agreement is what triggers the exception. A district-licensed educational platform typically has the DPA in place. A teacher's personal ChatGPT subscription does not.

Anonymization is the operational fix. Strip names, IDs, and identifying details; replace with generic placeholders before any external AI interaction. The teacher who uses AI to generate differentiated practice problems does not need student names in the prompt. The teacher who uses AI to summarize a specific student's progress report does. The first is routine. The second is the moment to stop, anonymize, or use only vetted district tools.

COPPA — the Children's Online Privacy Protection Act — restricts collection of personal information from children under 13. The FTC finalized amendments in April 2025 that include the first explicit treatment of children's data used to train algorithms. The operational implication for elementary teachers: default consumer AI tools require users to be at least 13. A fourth-grade teacher who sets up shared ChatGPT logins for the class is asking students to violate the service's terms and exposing the school to COPPA risk. For students under 13, AI use should run through education-specific products with COPPA-compliant data agreements, or through the teacher operating the AI on the students' behalf with anonymized inputs and reviewed outputs.

Say it plainly: FERPA and COPPA application to AI is legal-stakes, state-variable, and rapidly evolving. The principles above are the starting point. The specifics belong to your district counsel and privacy officer.

---

## The policy paragraph and the reflexive commitment

The working artifact of this chapter is a policy paragraph. Here is what one looks like for the redesigned research paper.

*You may use AI tools for brainstorming, outlining, source identification, and grammar review. You may not use AI to write paragraphs you submit as your own writing. Your AI use disclosure and prompt log entry are required components of the assignment — incomplete or inaccurate disclosure is the integrity violation, not the AI use itself. The defense conference is the point at which I will see whether the paper represents your mental model of the historical-current connection you argued. If it does, the AI use that helped you get there is acknowledged and credited. If it does not, no detection software is needed; the conversation will show. I use AI tools to draft slide outlines, generate practice problems, and respond to routine emails. I do not use AI to grade your work or write the substantive comments you receive on your drafts.*

Three properties to notice. Specific: it names tools and names permitted and forbidden uses. Enforceable: the violations are observable through the disclosure and the defense without a detector. Pedagogically motivated: the rule cites the learning mechanism it protects — the defense conference shows the mental model — rather than asserting a prohibition.

And there is the reflexive commitment in the last two sentences. If you use AI to draft your feedback, generate practice problems, build your slides, and never tell your students, you are asking them to disclose what you conceal. That asymmetry is noticed. It corrodes the policy faster than any failure of enforcement.

The teacher transparency move has three layers. Disclose at the syllabus level — what AI does and does not do in your teaching. Disclose at the artifact level — when a handout was AI-drafted and teacher-edited, note it. Disclose the boundary, not just the tool — what you used AI for, what you did not, where your judgment lives. The disclosure pattern you ask of students is the pattern you live yourself.

---

## Three misconceptions worth addressing directly

The first is that detection software works well enough and the false positives are rare. The peer-reviewed evidence does not support this. Liang 2023 found greater than 50% misclassification on TOEFL essays — that is not a rare-event problem, it is systematic bias. Weber-Wulff 2023 found the class of tools "neither accurate nor reliable." OpenAI withdrew its own classifier in July 2023 citing 26% true-positive accuracy. Even taken at face value, the institutional arithmetic is brutal: a 1% false-positive rate at Vanderbilt's 2022 paper throughput produces 750 wrongly-flagged students. The fix is not a better detector.

The second is that banning AI in the classroom solves the integrity problem. It does not. The Pew January 2025 data shows approximately 26% of teens use ChatGPT for schoolwork; the ban is counterfactual at the population level. It punishes the students who follow it and rewards those who do not. The equity pattern is non-obvious: higher AI use among Black and Hispanic teens than White teens, higher use among higher-income families. A blanket ban interacts asymmetrically with what students have at home. And even a perfectly enforced in-class ban does not address the assignment-level problem — students write papers outside of class. The ban is a category error.

The third is that more enforcement equals more integrity. The opening case is the counterexample. The professor enforced harder; her students learned less. Past a threshold, the enforcement workflow consumes the teaching time that would have produced the learning the policy was supposed to protect. When the integrity workflow grows large enough to dominate the teaching workflow, both fail at once. The durable response is to lower the enforcement burden by raising the design floor.

---

## The equity dimension

![Horizontal bar chart of ChatGPT-for-schoolwork usage rates by demographic group from Pew January 2025: Black teens 31%, Hispanic teens 31%, White teens 22%, overall teens 26%, alongside higher-income vs lower-income family rates. Zero baseline; the all-teen average bar uses the red accent.](../images/13-academic-integrity-privacy-and-honest-use-fig-04.png)
![Teen ChatGPT-for-schoolwork use by group (Pew 2025). Bans and requirements both interact asymmetrically w](images/13-academic-integrity-privacy-and-honest-use-fig-04.png)
*Figure 13.4 — Teen ChatGPT-for-schoolwork use by group (Pew 2025). Bans and requirements both interact asymmetrically with what students have at home.*

The chapter has to hold a difficult finding: AI use among teens is not uniformly distributed, and the patterns matter for policy.

Pew Research (January 2025) reported that the share of U.S. teens aged 13–17 who have used ChatGPT for schoolwork rose from 13% in 2023 to 26% in 2024. The cross-tabs are non-obvious: Black and Hispanic teens (31% each) report higher use than White teens (22%); higher-income families show higher rates than lower-income families. Banning AI in a context where roughly a quarter of students use it anyway produces a policy that punishes the compliant. Requiring AI without addressing differential home access — broadband, device, paid-tier models — widens the gap rather than closing it.

A defensible policy names both directions and adjusts. AI-survivable design is more equitable than detection-first precisely because it shifts the burden from catching students to designing learning. A student who uses AI as a Socratic partner to strengthen an argument is doing something educationally valuable that the assignment should credit. A student who uses AI to generate an artifact they cannot defend is doing something the design will make visible without requiring a detector.

---

## LLM-assisted exercises

**Exercise 1 — Draft a student AI-use policy.** Choose one course you teach. Write one paragraph of an AI-use policy, 150–300 words. Evaluate it against three criteria: specific (names actual tools and specific permitted and forbidden uses), enforceable (violations are observable without detection software), and pedagogically motivated (the rule cites the learning mechanism it protects). Add one sentence of your own AI-use disclosure — what you use AI for in your teaching, what you do not. Test it the same way. Then paste both into an LLM and ask it to play a student trying to find a loophole. Iterate until the loopholes close.

**Exercise 2 — Redesign one assignment for AI-survivability.** Take one assignment from your current semester. Apply the five-question checklist. For each question scoring "no," write the single smallest redesign move that would change the answer to "yes." Do not redesign more than you have to — minimum-viable redesign to five yes's, not a wholesale overhaul. Then write the policy paragraph that goes with it using the format from the worked example. Paste both into an LLM and ask it to play a student trying to game the assignment without doing the underlying learning. For each attack the LLM identifies, either add a friction layer or decide the attack is expensive enough to be acceptable.

**Exercise 3 — Audit three detection-tool accuracy claims.** Find three publicly-stated accuracy claims from AI-detection vendors. For each claim, ask an LLM to help you evaluate the basis of the claim (independent peer-reviewed or internal benchmark?), how the stated false-positive rate compares to the Liang 2023 and Weber-Wulff 2023 findings, and what the Vanderbilt arithmetic looks like for your own course throughput at the vendor's stated false-positive rate. Write one paragraph summary of what the audit tells you about whether any of these tools can serve as primary evidence in an integrity case.

---

## What would change my mind

A well-designed replication of Bastani et al. (2025) in a different context — different country, different subject, different age band — that failed to find the performance paradox in the unguarded AI condition, particularly if it found that students who used AI freely during practice performed at or above the no-AI control on a delayed unassisted test. That finding would substantially weaken the empirical case for design-over-detection by undermining the load-bearing reason design is necessary. The chapter's framework would still be defensible on the institutional-retreat and detector-bias grounds, but the central pedagogical argument would have to be rebuilt on a narrower base.

---

## Still puzzling

The K-8 generalization. Most of the AI-survivable framework's published evidence comes from college and late-secondary contexts. The process-documentation and novel-application moves are clearly portable downward. The calibration of the framework to a third-grade or fifth-grade context is something the chapter does not have a confident answer for.

What process documentation actually costs at scale. The research paper redesign adds four checkpoints to one assignment. A teacher with 150 students and four preps cannot do this for every assignment. The equilibrium for a full teaching load has not been worked out in the published literature.

The teacher-transparency-as-mandatory question. The reflexive argument says teachers should disclose their own AI use. Whether that disclosure should be required by institutional policy, encouraged but not required, or left fully to instructor discretion is not settled.

Whether the framework holds as AI capability advances. The five-question checklist works because of specific 2026 limits — training cutoffs, inability to defend claims in conversation, inability to produce authentic process records. If those limits shift, the checklist needs revision. The framework is robust to incremental capability increases. It is not robust to qualitative shifts that cannot be predicted.

---

## References

- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning. *PNAS* 122(26): e2422633122. https://www.pnas.org/doi/10.1073/pnas.2422633122 — correction: https://www.pnas.org/doi/10.1073/pnas.2518204122
- Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns* 4(7): 100779. https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7
- Weber-Wulff, D., et al. (2023). Testing of detection tools for AI-generated text. *International Journal for Educational Integrity* 19(1): 26. https://link.springer.com/article/10.1007/s40979-023-00146-z
- Pew Research Center. (2025, January 15). About a quarter of US teens have used ChatGPT for schoolwork. https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/
- Vanderbilt University. (2023, August 16). Guidance on AI detection and why we're disabling Turnitin's AI detector. https://www.vanderbilt.edu/brightspace/2023/08/16/guidance-on-ai-detection-and-why-were-disabling-turnitins-ai-detector/
- OpenAI. (2023, updated July 20). New AI classifier for indicating AI-written text. https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/
- U.S. Department of Education, Office of Educational Technology. (2023). Artificial intelligence and the future of teaching and learning. https://www.ed.gov/sites/ed/files/documents/ai-report/ai-report.pdf
- FTC. (2025). COPPA final rule amendments. https://www.ftc.gov/system/files/ftc_gov/pdf/coppa_sbp_1.16_0.pdf
- Student Privacy Compass. State guidance on generative AI in K-12. https://studentprivacycompass.org/state-guidance-on-the-use-of-generative-ai-in-k-12-education/

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Plato** (~428–348 BCE) recorded the first sustained argument that a new communication technology might *appear* to produce knowledge while corroding it. In the *Phaedrus*, Socrates tells the myth of the god Theuth presenting writing to King Thamus as a remedy for memory. Thamus refuses: writing, he says, produces "forgetfulness in the souls of those who learn it," because they will trust the external marks rather than do the internal work — they will "have the appearance of wisdom, not the reality." That argument is the load-bearing structure under the Bastani result. Detection looks for the external marks. Design asks whether the internal work happened.

![Plato, Athenian philosopher (~428–348 BCE). AI-generated portrait based on a public domain engraving of the classical bust.](../images/plato.jpg)
*Plato, ~428–348 BCE. AI-generated portrait based on a public domain engraving of the classical bust (Wikimedia Commons).*

**Run this:**

```
Who was Plato, and how does the Phaedrus dialogue's critique of writing — that it produces "forgetfulness of memory" and "the appearance of knowledge, not the reality" — map onto this chapter's framework for academic integrity with AI? Keep it to three paragraphs. End with the single most surprising thing about how Plato's own use of the written dialogue contradicts the argument he puts in Socrates's mouth.
```

→ Search **"Plato"** and **"Phaedrus (dialogue)"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to rewrite the Theuth and Thamus myth with AI as Theuth and a 2026 teacher as Thamus — what does the king refuse, and on what grounds?
- Ask it about the difference between *anamnesis* (recollection as recovering knowledge the soul already has) and the externalized "knowledge" the dialogue criticizes — which of this chapter's five diagnostic questions tests for the difference?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 13.1 — Three independent failure modes. Any one is enough to disqualify detection as a primary tool; together th

Create a standalone D3 v7 HTML file for a concept map titled "Three independent failure modes. Any one is enough to disqualify detection as a primary tool; together th". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/13-academic-integrity-privacy-and-honest-use-fig-01.html`

---

### Figure 13.2 — The Bastani result. Same model. Same students. The only variable was the pedagogical wrapper around the p

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "The Bastani result. Same model. Same students. The only variable was the pedagogical wrapper around the p". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/13-academic-integrity-privacy-and-honest-use-fig-02.html`

---

### Figure 13.3 — The five-question diagnostic. Run this on one assignment at a time. The goal is the smallest move that co

Create a standalone D3 v7 HTML file for a checklist or diagnostic card titled "The five-question diagnostic. Run this on one assignment at a time. The goal is the smallest move that co". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/13-academic-integrity-privacy-and-honest-use-fig-03.html`

---

### Figure 13.4 — Teen ChatGPT-for-schoolwork use by group (Pew 2025). Bans and requirements both interact asymmetrically w

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "Teen ChatGPT-for-schoolwork use by group (Pew 2025). Bans and requirements both interact asymmetrically w". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/13-academic-integrity-privacy-and-honest-use-fig-04.html`
