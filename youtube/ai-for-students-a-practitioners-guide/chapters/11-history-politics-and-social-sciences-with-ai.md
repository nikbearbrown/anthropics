# Chapter 11 — History, Politics, and Social Sciences with AI

*The past is a foreign country. AI gives you a very fluent travel guide that has never been there.*

---

Here is an uncomfortable fact about how humans read historical documents.

When you pick up a text from 1962 — a cable, a transcript, a memorandum — the natural thing your brain does is read it the way you would read a 2026 document. You project current categories backward. You assume the writer shared your assumptions about what the stakes were, what the options were, what the words meant. You read the words. You do not read the conditions of the words' production.

Sam Wineburg spent a decade documenting this. His 1999 essay was called "Historical Thinking and Other Unnatural Acts" — the title is the argument. The natural reading is not careless. It is cognitive default. We process what is in front of us using the categories we already have. Historical thinking requires the opposite: holding the writer's world separate from ours, suspecting our own categories, asking what they could and could not have known when they wrote. That is not natural. It has to be built by training.

What builds it is doing it. Performing the moves yourself, repeatedly, on actual documents. Not reading a description of the moves. Doing them.

AI is a fluent description of historical thinking. It is not historical thinking. And the difference is exactly the one this book has been building toward since Chapter 1 — between the artifact that looks like the thing and the cortex that can produce the thing. This chapter is about where that difference matters most acutely, and what to do about it.

---

## The Three Moves That Distinguish a Historian's Reading

Wineburg and his collaborators gave the same set of historical documents to trained historians and to undergraduates. Then they watched how each group read.

The historians did something systematically different. Before reading the body of any document, they looked at who produced it, when, and to whom — what position the author was in, what stake they had. During reading, they held the historical context in active working memory: what had just happened in the weeks before? What could the author have known? After reading, they corroborated claims across documents: where two independent accounts converge, the claim is stronger; where they diverge, the *divergence* is the historical question.

The undergraduates read the words. The historians read the words *plus the conditions of the words' production*.

Wineburg named these three practices: **sourcing** (who wrote this, when, to whom, in what position), **contextualization** (what was the author responding to that we, reading now, might miss), and **corroboration** (what does this document look like against other primary sources from the same period). None of them are natural. None of them appear spontaneously. All of them are built by doing them repeatedly on actual documents until they become the automatic first move.

![Two-panel flow diagram. Top panel shows the historian's reading: sourcing before reading, contextualization during reading, and corroboration after reading, all branching around a central primary source and producing a reading plus schema. Bottom panel shows a single dashed arrow from primary source straight to summary, with no branching moves.](../images/11-history-politics-and-social-sciences-with-ai-fig-01.png)
![Two ways to read a primary source. The three-move path builds the historian's schema; the flat path produ](images/11-history-politics-and-social-sciences-with-ai-fig-01.png)
*Figure 11.1 — Two ways to read a primary source. The three-move path builds the historian's schema; the flat path produces fluency without it.*

Here is why this matters for the present chapter. When you ask Claude to "summarize the October 27, 1962 ExComm meeting transcript," you receive a summary that bypasses all three moves. The summary tells you the *what*. It does not perform the sourcing — Robert McNamara is Secretary of Defense, has been at the table for thirteen days, is responding in this specific moment to a U-2 shootdown that has just shifted the room's posture toward escalation. It does not perform the contextualization — this is Black Saturday; Khrushchev's formal letter demanding the Jupiter trade has just arrived; Kennedy has not decided what to do about it. It does not perform the corroboration — this transcript looks different when read against the parallel Soviet documentation that became available only after 1991.

The summary feels like understanding. The moves that constitute historical understanding never happen.

This is the Bastani performance paradox transposed into a discipline. In math, unguarded AI use lifted practice scores 48% and dropped exam scores 17 percentage points.[^bastani] In history, the equivalent is asking AI to synthesize primary sources before you read them. The student receives a paragraph that reads like comprehension. The Wineburg schema — the cognitive structure that produces comprehension — is not built.

---

## What Happened When Nicholas Read the AI Summary First

Nicholas is a high school junior from Cape Cod working on a summer research project about the resolution of the Cuban Missile Crisis. He has a mentor. He has a stack of printed ExComm transcripts from the JFK Library on his desk. He has Claude open on his laptop.

In week one he asks Claude to summarize the October 27 meeting transcript. He gets three hundred words. Clean, accurate, well-organized. He reads it. He takes notes on the summary. He feels like he understands what happened on Black Saturday.

Three weeks later, in his first weekly meeting with his research mentor Utkarsh, the mentor asks him a question: *"What's your read on why Llewellyn Thompson interrupted when he did on the 27th? What did he know about Khrushchev that the others didn't?"*

Nicholas opens his mouth. He has the meeting in his notes. He cannot answer the question. He knows what happened. He does not know what it meant, or why a specific voice intervening at a specific moment was historically significant. He has the summary. He does not have the interpretive structure that would make the summary usable when someone asks him to think with it.

He had read the words. He had not performed the moves.

The next week he reads the transcript cold — no summary first. He does the sourcing before he starts: Thompson was the former US Ambassador to Moscow, the only person in the room with a genuine personal relationship with Khrushchev, who had been watching the Soviet leader under pressure for years. He does the contextualization: the interruption happens at the moment the room is edging toward accepting Khrushchev's harder public letter over his softer personal one; Thompson's intervention is to say, in effect, *I know this man, and the public letter is negotiating posture, not final position*. He does the corroboration: the Soviet documents from 1991 suggest Thompson was right.

![Excerpt of the 27 October 1962 ExComm transcript with Llewellyn Thompson's interruption highlighted. Three margin annotations name the Wineburg moves applied to the passage: sourcing identifies Thompson's role as former US Ambassador to Moscow; contextualization names the two competing Khrushchev letters the room is choosing between; corroboration points at Soviet 1991 documentation that confirms Thompson's read.](../images/11-history-politics-and-social-sciences-with-ai-fig-02.png)
![The same passage, with the conditions of its production installed. The transcript reads differently once ](images/11-history-politics-and-social-sciences-with-ai-fig-02.png)
*Figure 11.2 — The same passage, with the conditions of its production installed. The transcript reads differently once sourcing, contextualization, and corroboration are applied to a specific moment.*

He now has something. Not a summary. A *reading* — a specific claim, grounded in the conditions of the document's production, testable against other evidence. That is what three weeks of AI-assisted study had not produced, and what two hours of primary source reading with the Wineburg posture did.

---

## Causal Arguments Are Where History Lives

History is not chronology. Chronology is the raw material. History is the construction of causal arguments about why what happened happened the way it did and not otherwise.

A causal historical argument has four parts. A claim about cause: X caused Y. An explicit counterfactual: had X not occurred, Y would have been different in specifiable ways. Evidence connecting X to Y. And an acknowledgment of competing explanations and a specific account of why each falls short. An argument missing any of these four is description with a verb.

The cognitive event that builds the ability to construct causal arguments is constructing them — being wrong, noticing what you got wrong, revising. The Slamecka and Graf generation effect, established in 1978 and replicated across four decades, is direct: information generated by the learner is retained dramatically better than information passively read.[^slamecka] Reading a well-constructed causal argument produces fluency. It does not produce the capability to construct the next one.

This is the parallel finding to the Kosmyna 2025 MIT Media Lab study on writing, which found up to 55% reduced functional brain connectivity during AI-assisted composition compared to unassisted writing, and 83% of AI-assisted writers could not quote their own essays minutes after submitting them.[^kosmyna] The students felt they understood. The neural networks that build durable understanding were not active in the way that builds anything.

![Four numbered boxes connected in sequence: claim, counterfactual, evidence, acknowledgment. Each carries a brief example from Nicholas's back-channel argument — the back channel as cause, the absence of escalation as counterfactual, the JFK Library tapes and Soviet documents as evidence, and the realist, bureaucratic-politics, and constructivist objections as acknowledgment.](../images/11-history-politics-and-social-sciences-with-ai-fig-03.png)
![A causal historical argument has four parts. Missing any of them and you have description with a verb.](images/11-history-politics-and-social-sciences-with-ai-fig-03.png)
*Figure 11.3 — A causal historical argument has four parts. Missing any of them and you have description with a verb.*

The phase gate for history follows directly. You write the causal claim and the counterfactual before AI is consulted. AI may challenge the claim after you have constructed it. AI may not construct it. The construction is what produces the capability to construct the next one.

---

## The Four IR Lenses and How to Use Them Without Borrowing Them

If you are working in international relations or political science, you need four theoretical lenses. Each makes different predictions. Each treats different facts as central. Knowing which instrument fits which question is most of the discipline.

**Realism** says states are the primary actors, security is the highest goal, and power — especially military power — determines outcomes. Structural realists (Waltz, Mearsheimer) locate the cause of state behavior in the structure of the international system itself: anarchy forces self-help regardless of regime type or leadership.

**Liberal institutionalism** says cooperation under anarchy is possible because states have shared interests, regime type matters (the democratic peace), and institutions reduce transaction costs. Keohane's *After Hegemony* and *Power and Interdependence* (with Nye) are the canonical texts.

**Constructivism** says the structures of international politics are socially constructed. Alexander Wendt's formulation — "anarchy is what states make of it" — is the foundational claim: the same distribution of capabilities can produce a Hobbesian world or a Kantian one depending on the intersubjective understandings states share about each other. Identity and norms matter, not just power.

**Critical theory and Marxian IR** asks who the international order serves and how it could be different. Robert Cox's 1981 formulation is the starting point: theory is always for someone and for some purpose. World-systems theory (Wallerstein) and dependency theory belong to this family.

| Framework | Core claim | Treated as central | Treated as secondary | Canonical text |
|---|---|---|---|---|
| **Realism** | Anarchy forces self-help; power decides outcomes. | Material capabilities, security, the structure of the system. | Regime type, norms, institutions. | Waltz, *Theory of International Politics* (1979); Mearsheimer, *Tragedy of Great Power Politics* (2001). |
| **Liberal institutionalism** | Cooperation under anarchy is achievable through shared interests and institutions. | Regime type, transaction costs, repeated interaction. | The autonomous logic of military balance. | Keohane, *After Hegemony* (1984); Keohane & Nye, *Power and Interdependence* (1977). |
| **Constructivism** | Anarchy is what states make of it; identity and intersubjective understanding configure interest. | Identity, norms, shared meanings, learning. | Brute material capability as a self-interpreting fact. | Wendt, *Social Theory of International Politics* (1999). |
| **Critical / Marxian IR** | Theory is for someone and for some purpose; the order serves specific class and core interests. | Production relations, hegemony, core–periphery dynamics. | The state as a neutral unit of analysis. | Cox, "Social Forces, States and World Orders" (1981); Wallerstein, *The Modern World-System* (1974). |

*Table 11.1 — The four IR lenses, side by side. Use this as a diagnostic instrument, not a taxonomy. The question is which lens makes the best predictions for the specific case in front of you.*

Now here is the capability-borrowing failure mode. You ask AI: *"Explain the Cuban Missile Crisis from realist, liberal, and constructivist perspectives."* You receive a clean comparative table. You feel like you understand the frameworks. On an exam where you must apply *one* framework rigorously to a new case, you produce a hybrid — vocabulary from all three, the analytic discipline of none. You borrowed the labels. You did not build the cognitive structures.

The capability-building version: write your own one-paragraph interpretation of the case first. Then ask AI to argue against it from each framework in turn, with specific evidence and specific claims. You read each counter-reading. You return to the primary sources. You revise. The frameworks now live in your head as discriminating instruments, not as labels.

![Two stacked study sequences. Top: dashed boxes from AI table of four lenses to student reads to exam to a gray output labeled hybrid mush. Bottom: solid boxes from student writes own interpretation first to AI argues against from each lens to student returns to primary sources to student revises to exam to a dark output labeled rigorous single-lens application. The bottom path also flags the key divergence in ochre — the written interpretation that AI challenges, not produces.](../images/11-history-politics-and-social-sciences-with-ai-fig-04.png)
![Same tool, opposite outcomes. The divergence is the order of operations, not the time spent.](images/11-history-politics-and-social-sciences-with-ai-fig-04.png)
*Figure 11.4 — Same tool, opposite outcomes. The divergence is the order of operations, not the time spent.*

---

## AI Will Fabricate History Confidently and Plausibly

The hallucination problem in history is worse than the general case because the fabrications wear the costume of authenticity. AI has read enormous amounts of historical text. It knows the right register for a Lincoln letter, the right vocabulary for a Cold War cable, the right structure for a primary source. When it fabricates, the fabrication sounds exactly right.

The canonical legal case is *Mata v. Avianca* — Judge Castel's 2023 sanctions order in the Southern District of New York, in which attorneys submitted a brief containing fabricated case citations generated by ChatGPT. The attorneys fined $5,000. The fabricated citations had attached real judges' names to opinions that did not exist.[^mata] The attorneys had asked ChatGPT to verify the citations, and ChatGPT confirmed them. The mechanism: the model had no way to know the citations were fake, because it was generating plausible text, not checking a database.

For history specifically, the same pathology runs. AI systems will generate quotes from historical figures the figures never said, dates for events that never occurred, citations to journal articles that do not exist, and primary source excerpts that are AI-synthesized composites of period style.

The Walters and Wilder 2023 study in *Scientific Reports* examined 636 bibliographic citations generated by ChatGPT across 84 short literature reviews: 55% of GPT-3.5 citations were entirely fabricated. Among GPT-4 citations, 18% were entirely fabricated. Among non-fabricated citations, 43% of GPT-3.5 entries and 24% of GPT-4 entries contained substantive errors in author, title, year, or pagination.[^walters] There is no reason to think the rate is lower for historical claims. The rate of *detection* is just lower because students rarely check.

The Lee et al. 2025 survey of knowledge workers at Microsoft Research and Carnegie Mellon found the inversion that makes this dangerous: higher confidence in AI predicts less critical thinking, while higher self-confidence predicts more.[^lee] The students who have built genuine competence catch the errors AI makes. The students who borrowed capability cannot catch what they cannot evaluate.

A student who has done the Wineburg moves on real primary sources can sense when an AI-generated Khrushchev quote is wrong. The register is slightly off. The phrasing uses a word that does not belong to the decade. The citation gives an archive number that does not match what the student knows about Soviet bureaucratic practice. A student who has only consumed AI summaries has no calibrated ear for authenticity.

| Model | Entirely fabricated | Errors in real citations | Combined unreliable rate |
|---|---|---|---|
| GPT-3.5 | 55% of generated citations | 43% of the non-fabricated remainder | ≈ 74% of all citations are either invented or contain a substantive error |
| GPT-4 | 18% of generated citations | 24% of the non-fabricated remainder | ≈ 38% of all citations are either invented or contain a substantive error |

*Table 11.2 — Walters & Wilder 2023 citation reliability (636 citations across 84 reviews). Verification is not optional. The rate improved from GPT-3.5 to GPT-4. It did not reach zero.*

Try this once and you will not need to be told again. Ask Claude or ChatGPT, with no special prompting, for three primary source quotes from Khrushchev about the Cuban Missile Crisis with citations. Then look up the citations. The standard finding: at least one will be a real source with a misattributed quote. At least one will be a complete fabrication that sounds exactly right.

---

## The Human-Only Zone

For history and the qualitative social sciences, the Human-Only Zone has three components.

**Primary source reading and interpretation.** The act of reading the document — the ExComm transcript, the Long Telegram, the Marshall Plan cable, the Tiananmen Papers — and forming an interpretation of what the participants meant and what the texture of the language reveals about the bureaucratic context. This is where the Wineburg schema is built. AI summary collapses the event. The student receives the interpretation without the interpretive practice.

**Causal argument construction.** Claim, counterfactual, evidence, acknowledgment. AI may challenge a causal argument after the student has constructed it. AI may not construct it. The construction is what produces the capability to construct the next one.

**Comparative analysis across cases.** Every historical claim depends implicitly on a comparison — distinctive of this case compared to *which* case? AI can help identify candidate comparable cases. The act of running the comparison — noting which structural features are shared, which differ, which features the analogy breaks down on — is the cognitive work that builds comparative judgment.

---

## The Phase Gate for History

History is one of the few subjects where the phase gate opens and closes multiple times in a single workflow. This is different from the linear writing gate in Chapter 8. The history gate is bidirectional and repeating.

| # | Phase | Gate state | What the student does |
|---|---|---|---|
| 1 | Source location | AI open | Build the reading list: primary collections, canonical secondary, theoretical frameworks. Verify every citation. |
| 2 | Primary source reading | AI closed | Read cold. Perform the three Wineburg moves. Form an interpretation. Keep a notebook. |
| 3 | Interpretation drafting | AI closed | Write the causal claim and counterfactual in your own words before opening AI. |
| 4 | Theoretical challenge | AI open | Use the four-lens prompt. AI argues against your written interpretation from each framework. |
| 5 | Revision | AI closed | Return to primary sources. Revise the argument on paper. |
| 6 | Stress test | AI open | Mentor simulation. Twenty questions. Answer out loud, without notes. |
| 7 | Final writing | AI closed | Compose prose without AI assistance. |
| 8 | Verification | AI open (light) | Citation check. Fact check. No argument generation. |

*Table 11.3 — The history phase gate. The order is the methodology. Each open-gate phase is bounded by a specific task that AI performs well and that does not substitute for the closed-gate cognitive work on either side of it.*

The order is the methodology. The gate structure is what distinguishes this workflow from both the "AI does everything" failure mode and the "AI does nothing" overcorrection. Each open-gate phase is bounded by a specific task that AI performs well and that does not substitute for the closed-gate cognitive work on either side of it.

---

## Nicholas's Project, Phase by Phase

Nicholas's project is the worked example. Here it is in compressed form.

**Week 1, gate open.** He asks Claude for a research map: primary source collections, canonical secondary works, theoretical frameworks, full bibliographic citations he will verify. He receives twenty-eight sources. He spends three days verifying each one. *Three are fabricated.* One is a Sherwin and Bird journal article that does not exist (they co-authored a book on Oppenheimer, not a Cuban Missile Crisis paper). One is a Stern *Diplomatic History* article that does not exist (Stern's Cuban Missile Crisis work is a Stanford University Press book, not a journal article). One attaches a real author to a real journal in the wrong year with the wrong title. He removes the three. He keeps the verified twenty-five. He notes the rate: roughly 11%, consistent with the Walters and Wilder GPT-4 range.

**Weeks 2–4, gate closed.** He does not open Claude or ChatGPT. He reads the JFK Library transcripts of five ExComm meetings. He reads Khrushchev's October 26 long personal letter and his October 27 formal letter. He reads the State Department record of the Dobrynin–Robert Kennedy conversation on the evening of October 27. He reads Allison and Zelikow, Stern, Sherwin. He keeps a handwritten notebook. When sources disagree, he writes the disagreement.

At the end of week four he writes a one-paragraph causal claim: the crisis resolved peacefully primarily because the back-channel meeting between Robert Kennedy and Anatoly Dobrynin created a face-saving exit the formal diplomatic record could not. He has a claim. He has an implicit counterfactual. He has not yet acknowledged competing explanations.

The gate stays closed.

**Week 5, gate open.** He pastes his paragraph into Claude. He asks AI to argue against it from Mearsheimer-style offensive realism, from Allison's bureaucratic politics model, from Wendt-style constructivism.

The realist objection is the sharpest: Khrushchev's withdrawal was driven by the underlying material balance — US naval superiority, US ICBM advantage, no Soviet second-strike capability — not by the back channel. The channel was an effect, not a cause. Even without the Dobrynin–Kennedy meeting, Khrushchev would have withdrawn because the material balance forced him to. The framework points to declassified Soviet General Staff documents from 1991 showing the internal Soviet recognition of strategic weakness.

Nicholas reads. He notices he has been treating the back channel as the cause of de-escalation rather than the route through which an already-determined de-escalation found expression. This is a real revision.

**Week 5, gate closed.** He revises on paper. His new central claim: the resolution was an interaction effect between a material balance that gave Khrushchev strong incentive to withdraw and a diplomatic structure that gave both leaders a face-saving route to act on the incentive without triggering the bureaucratic escalation logic. Neither factor alone is sufficient. The back channel was the operational mechanism through which the structural incentive expressed itself, not an independent cause.

![Two text boxes side by side. Left: Nicholas's Week 4 claim that the back channel caused peaceful resolution, with two phrases struck through. Right: the Week 5 revised claim of an interaction effect between material balance and the back-channel structure. Below, three labeled counter-readings — realist, bureaucratic politics, constructivist — sit in ochre boxes with dashed arrows targeting specific phrases in the original.](../images/11-history-politics-and-social-sciences-with-ai-fig-05.png)
![Nicholas's argument evolution. The revision is not weakening the argument. It is making it defensible.](images/11-history-politics-and-social-sciences-with-ai-fig-05.png)
*Figure 11.5 — Nicholas's argument evolution. The revision is not weakening the argument. It is making it defensible.*

The argument is now denser. It acknowledges what each counter-framework gets right.

**Week 6, gate open.** He runs the stress test — asks Claude to act as a specialist mentor and ask twenty hard questions in sequence, waiting for his answer before asking the next. Three questions he cannot answer fluently. The hardest: *"Your claim that the back channel was operationally necessary depends on the assumption that the formal record would have produced escalation. What primary source evidence do you have for the bureaucratic escalation pressure, and how do you know it would have prevailed?"* He has assumed it. He has not documented it. He returns to the JFK Library transcripts and to the Joint Chiefs' October 27 communications. He finds the evidence.

**Week 6, gate closed.** He writes the paper. No AI assistance during composition.

**Week 6, gate open (light).** Citation check. Fact check. Copy-edit.

He submits to his mentor. At their first conversation the mentor asks him about the cross-case comparison — what happens to his interaction-effect argument if you apply it to the 1961 Berlin crisis, where the back channel was also present but produced a different outcome? He says he knows the comparison. He gives it. The mentor asks where it is in the paper. He says it is not. She says that is what revision is for.

He passes the Nicholas test.

---

## Three Sanctioned Prompts

These are the prompts that operate the gate correctly. Each is designed to be used *after* you have done the cognitive work that produces the thing AI would otherwise replace.

**Prompt 1 — The Post-Interpretation Theoretical Challenge.**

```
I have written the following one-paragraph causal interpretation of [event]:

[paste your interpretation]

Act as a hostile reviewer with [realist / liberal institutionalist /
constructivist / critical theory] commitments. Identify the three
strongest objections from this theoretical position. For each:
1. The specific empirical evidence the framework would point to.
2. The assumption in my argument the framework would target.
3. What I would have to demonstrate in revision to defend my position.

Do not write the revised argument for me. Do not soften your critique.
```

**Prompt 2 — The Wineburg Pre-Reading Context Drill.**

```
I am about to read [primary source title and description].

Before I read, I want to perform the three Wineburg moves:
(a) Sourcing: Who produced this, when, to whom, in what institutional
    position? Do not summarize the content.
(b) Contextualization: The three most important contextual facts from the
    weeks or months before this document that would shape what the author
    was responding to. Do not summarize the document.
(c) Corroboration: Two other primary sources from the same period that
    would let me check the claims in this document.

I will read the document myself after you respond.
```

**Prompt 3 — The Causal Counterfactual Stress Test.**

```
I have argued that [X caused Y in case Z]. Construct the strongest
counterfactual reasoning that would test this claim:
1. What would have had to be different about X for Y to have happened
   differently?
2. What primary sources from case Z would I need to consult to defend
   the counterfactual link?
3. What alternative causes does my argument fail to engage?

Do not tell me whether my causal claim is correct. Help me see what
would test it.
```

---

## The Nicholas Test for History

You pass it if you can do three things in sequence without notes and without AI.

Explain your interpretation of the case to a skeptical scholar — five minutes, out loud, to someone who can ask hard follow-up questions. Defend it against the strongest counterargument without consulting your draft, acknowledging specifically what you have not yet defended and how you would defend it. Apply the relevant principle to a current geopolitical situation you have not formally studied — identify which features would be relevant if your principle holds, which would test it, where the analogy breaks.

If you can do all three, the knowledge is yours. If you can only describe the case you studied, you have surface knowledge — the words have arrived but not the structure that lets you use them. Return to the primary sources.

---

## LLM Exercises

**LLM Exercise 1 — The Fabricated-Quote Calibration.**
Ask your AI tool, with no special prompting: *"Give me three primary source quotes from [historical figure] about [topic], each with a specific citation including publication, date, and archive or page number."* Verify each citation against primary sources — presidential libraries, the Avalon Project at Yale, university press collected works, the relevant national archive. Document which were real, which had misattributed quotes, which were entirely fabricated. Record the rate. Run the same exercise on a different model. Compare the rates. These numbers are your personal calibration; they should inform every future research project you run.

**LLM Exercise 2 — The Post-Interpretation Four-Lens Drill.**
Pick a historical or political case you have basic familiarity with. Write a one-paragraph causal argument of your own — commit it to writing before opening AI. Then paste it into your AI tool with this prompt: *"I have written the following causal interpretation. Argue against it from realist, liberal institutionalist, and constructivist positions in turn. For each position, give me the three strongest objections, the specific evidence each framework would point to, and the assumption in my argument each would target. Do not write the revised argument for me."* Read each counter-reading. Return to primary or secondary sources where you need to. Revise your paragraph. You will know the exercise worked when your revised version specifies which framework's strongest objection you take most seriously and why.

**LLM Exercise 3 — The Mentor Stress Test.**
After completing any substantial research project, open your AI tool and use this prompt: *"I have just completed a historical analysis of [past event] arguing [your central claim]. Act as a specialist mentor in this field. Ask me your twenty hardest questions in sequence — wait for my answer before asking the next. I will answer each one without looking at my paper."* Record which questions you cannot answer fluently. Those are the gaps. Identify which ones are gaps you could close by returning to primary sources and which are genuine uncertainties at the edge of the argument. The exercise produces two outputs: a list of revision targets and a calibrated map of what you actually know versus what you assumed.

---

## What Would Change My Mind

If a large, well-designed randomized trial in college history classrooms demonstrated that students who used AI to summarize primary sources before reading them performed equally well on unassisted assessments of historical thinking compared to students who read sources cold first, I would substantially revise the order-of-operations argument in this chapter. The evidence here is by analogy from Bastani 2025 in math — a direct history-classroom RCT is not in print at the time of this writing. The argument converges from Wineburg's empirical framework, Bastani's performance paradox, the Walters and Wilder fabrication rates, and the Lee et al. critical thinking inversion — but it is not direct experimental confirmation in the discipline itself. If that confirmation arrives pointing the other way, the chapter should change.

---

## Still Puzzling

Why some students appear to recover historical schema even after AI-assisted reading and others do not. The mechanism that makes bypass damaging is consistent across the cognitive science literature. The variance in recovery is not. I do not yet know what distinguishes students who integrate AI summaries with later primary source reading from those who do not.

Whether the fabrication rate in frontier models has dropped enough to change the verification protocol. Walters and Wilder measured GPT-3.5 and GPT-4. Current models may fabricate less often. They do not fabricate zero. The verification practice should hold; the rhetoric about the rate should track the data as it arrives.

Whether AI-as-historical-roleplayer — asking AI to roleplay Khrushchev, Kennedy, Lincoln — is capability-building or capability-borrowing. It can be either. If the student is probing the figure to test their own interpretation of the figure's reasoning, it is probably capability-building. If the student is accepting the AI's roleplay as if it were data, it is capability-borrowing. The diagnostic for catching this distinction in practice is less clear than I would like.

---

## Bridge to Chapter 12

Chapter 11 has been about a discipline where the stakes of capability-borrowing are intellectual. Chapter 12 raises them considerably. The pre-med, pre-law, and engineering student is not being prepared for a seminar conversation — they are being prepared for a licensing exam and, beyond that, for a profession in which capability-borrowing produces harm to other people. The same framework applies. The cost of failure changes. We start Chapter 12 with a pre-med student who used AI to practice clinical reasoning for four months. We end with *Mata v. Avianca*. The argument between the two is the chapter.

---

**Tags:** #history #international-relations #Cuban-Missile-Crisis #Wineburg-historical-thinking #IR-theory #capability-building #phase-gate #primary-sources #AI-hallucination

---

## Footnotes

[^bastani]: Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122. <https://doi.org/10.1073/pnas.2422633122>

[^slamecka]: Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592–604. <https://psycnet.apa.org/doi/10.1037/0278-7393.4.6.592>

[^kosmyna]: Kosmyna, N., et al. (2025). Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing tasks. MIT Media Lab. arXiv:2506.08872. <https://arxiv.org/abs/2506.08872>

[^mata]: *Mata v. Avianca, Inc.*, 22-cv-1461 (PKC) (S.D.N.Y. June 22, 2023). <https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54/>

[^walters]: Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, 14045. <https://www.nature.com/articles/s41598-023-41032-5>

[^lee]: Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking. *CHI '25*. <https://dl.acm.org/doi/10.1145/3706598.3713778>

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Marc Bloch** (1886–1944) — co-founder of the *Annales* school, French Resistance fighter, executed by the Gestapo near Lyon in June 1944 — built almost the entire framework this chapter operationalises. His three projects map directly onto the three moves Wineburg later measured: *la longue durée* (read the slow structural conditions, not the surface events), *l'histoire totale* (no single document or discipline holds the whole; you must triangulate), and the posthumously published *Apologie pour l'histoire / The Historian's Craft* (1949), which is, line for line, a manual for sourcing, contextualization, and corroboration in a working historian's hands. Bloch wrote *The Historian's Craft* while in hiding; the manuscript was incomplete when he was shot. The question he set himself in the opening pages — "Tell me, daddy, what is the use of history?" — is the question this chapter is trying to answer for a different kind of student in a different kind of danger.

![Marc Bloch, French historian and Resistance fighter (1886–1944).](../images/marc-bloch.jpg)
*Marc Bloch, circa 1930. AI-generated portrait based on a public domain photograph.*

**Run this:**

```
Who was Marc Bloch, and how do his Annales-school commitments — long durée, total history, and the unfinished Historian's Craft (1949) — map onto the three Wineburg moves (sourcing, contextualization, corroboration) this chapter uses to study primary sources with AI in the room? Keep it to three paragraphs. End with the single most surprising thing about Bloch's career or method.
```

→ Search **"Marc Bloch"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to write *The Historian's Craft, chapter four: working with an AI that will fabricate a Khrushchev quote* in Bloch's own register.
- Ask it about the *Annales* method's argument with the Rankean primary-document tradition, and which side AI tools currently reinforce.
- Ask it how Bloch's work in the French Resistance — running document networks under occupation — would translate into a verification protocol for AI-generated citations.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 11.1 — Two ways to read a primary source. The three-move path builds the historian's schema; the flat path produ

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Two ways to read a primary source. The three-move path builds the historian's schema; the flat path produ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-history-politics-and-social-sciences-with-ai-fig-01.html`

---

### Figure 11.2 — The same passage, with the conditions of its production installed. The transcript reads differently once 

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "The same passage, with the conditions of its production installed. The transcript reads differently once ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-history-politics-and-social-sciences-with-ai-fig-02.html`

---

### Figure 11.3 — A causal historical argument has four parts. Missing any of them and you have description with a verb.

Create a standalone D3 v7 HTML file for a concept map titled "A causal historical argument has four parts. Missing any of them and you have description with a verb.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-history-politics-and-social-sciences-with-ai-fig-03.html`

---

### Figure 11.4 — Same tool, opposite outcomes. The divergence is the order of operations, not the time spent.

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Same tool, opposite outcomes. The divergence is the order of operations, not the time spent.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-history-politics-and-social-sciences-with-ai-fig-04.html`

---

### Figure 11.5 — Nicholas's argument evolution. The revision is not weakening the argument. It is making it defensible.

Create a standalone D3 v7 HTML file for a concept map titled "Nicholas's argument evolution. The revision is not weakening the argument. It is making it defensible.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-history-politics-and-social-sciences-with-ai-fig-05.html`
