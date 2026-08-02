# Chapter 8 — Writing and the Humanities with AI

*AI can produce an essay that reads better than yours. It cannot produce the version of you that understands the argument.*

> The essay proves the thinking only if you did the thinking. Here is the workflow that keeps the thinking yours.

---

Nicholas is a high school junior on Cape Cod with a serious interest in political science and a habit of reading footnotes. He is spending the summer on a research paper about the social and economic impacts of Syrian refugees in Jordan — part of a program designed to teach students how to use AI rigorously, treating model outputs the way a researcher treats a secondary source: as material to be verified against primary evidence, not conclusions to be borrowed. He has real sources: UNHCR registration data, World Bank labor market reports, academic papers on refugee integration in host economies. He has a view he can almost-but-not-quite articulate: something about the legal framework for work authorization, which is the binding constraint on integration, and the economic literature, which keeps circling around this constraint without landing on it as the central argument.

He opens Claude. He pastes in his evidence summary and asks it to synthesize the core argument. Claude returns two clean paragraphs: refugee labor market integration in Jordan is constrained not by refugee supply or host-country willingness but by gaps in legal work authorization — Syrian refugees without work permits are pushed into informal employment, undercutting wages for Jordanian low-income workers in ways that generate political resistance to the very integration policies that would resolve the dynamic. The synthesis is fluent. It carries his idea about the legal framework more cleanly than he had been able to carry it himself. He reads it twice. He feels that this is what he meant. He pastes it into his paper. The argument comes together. He submits it.

Three months later Nicholas is sitting an AP Human Geography free-response exam. One question asks about factors affecting refugee integration in host countries and the economic consequences for receiving communities. He starts to write. He can describe the data — UNHCR figures on registration rates, the informal labor market statistics he remembers from his sources. What he cannot reconstruct is the specific causal chain that made his paper an argument rather than a summary: why legal work authorization is the *binding* constraint specifically, how the informal-employment dynamic generates the political feedback loop that blocks reform, why the conventional framing of the issue underweights the legal-structural cause relative to cultural and housing pressures. He fills the page with accurate situation. He does not write the story. He walks out knowing the difference between what he described and what he had argued in the paper — and knowing he cannot reproduce the latter, because he did not generate it.

This chapter is for Nicholas. The argument is simple and it is the same argument Chapters 2 and 3 make, now applied at the specific resolution of a humanities essay. The artifact is not the point of writing. The cognitive structure that produces an essay is the point. That cognitive structure lives in the writer's head only if the writer built it during the writing. AI is uniquely good at producing the artifact without the cognitive structure, because LLMs are trained on the artifacts and reproduce the surface features fluently. What you cannot get from an LLM is the version of you that wrote the essay. And that version is what the AP free-response, the seminar, the oral exam, and every other high-stakes writing moment is actually testing.

---

## The Generation Effect at Essay Scale

The mechanism is the same one Chapter 2 introduced, now operating on a longer cognitive event.

Slamecka and Graf established in 1978 that information you generate yourself is retained dramatically better than information you merely read.[^slamecka1978] This is the generation effect, and it is one of the most replicated findings in memory research. The mechanism is not mysterious. Producing an answer is a deeper cognitive operation than recognizing an answer. Generation engages retrieval, integration, and effortful processing. Reading engages approximately none of these to the same degree.

When you write a thesis sentence yourself — when you sit with a blank document and a question and you draft, redraft, rewrite, until a sentence captures what you actually think — you are performing a generation event. The cognitive trace it leaves is dense. It carries the claim, the reasoning under the claim, the alternatives you considered and rejected, the words you chose and the words you didn't, and the relationship between your sentence and the specific evidence you have in your hand. When you read an AI-generated thesis and accept it, you are performing a recognition event. You can say *yes, that's roughly what I meant*. You cannot, two months later, reconstruct it under questioning.

The Kosmyna MIT Media Lab study from 2025 is the generation effect operating at essay scale.[^kosmyna2025] Fifty-four participants wrote SAT-style essays under three conditions: AI-assisted, search-engine-assisted, or brain-only. EEG measured functional connectivity across 32 channels. Brain-only participants showed the strongest, most distributed networks. LLM users showed up to 55% reduced connectivity — the upper bound across analyzed networks, not a single global average — meaning the neural events that constitute composition, synthesis, and memory formation were substantially muted in the AI-assisted writers. They were producing essays without the neurological events that produce durable comprehension.

The recall finding is what Nicholas lived. Immediately after their essay session — minutes later, on a topic they had just written about — 83% of LLM users could not quote a single passage from their own essays. Not summarize. Quote. The text they had submitted was not in their head. They felt they understood. They did not own the work.

The swap finding is the one that should make you sit with the chapter. A subset of 18 participants returned for a fourth session with conditions reversed. Participants who had been AI-assisted for sessions one through three were asked to write without the tool. They showed *weaker* neural connectivity than brain-only controls who had never used AI at all. Habitual AI-assisted writing did not leave the cognitive structures untouched. It atrophied them. Hold the specific numbers loosely — n=18, preprint, not yet peer-reviewed, the swap analysis in particular needs replication. The mechanism is not in dispute. The mechanism is Slamecka and Graf, and it runs in one direction: you own what you generated; you recognize what you read.

![Three side-by-side panels showing the Kosmyna 2025 results. Panel A: EEG functional connectivity strength across 32 channels — brain-only tallest, LLM-assisted up to 55% lower. Panel B: immediate post-session quotation recall — brain-only 89%, LLM-assisted 17%. Panel C: swap-session connectivity for habitual AI users (n=18) falling below the brain-only baseline.](../images/08-writing-and-the-humanities-with-ai-fig-01.png)
![Generation at essay scale. Brain-only writers show the strongest networks; habitual AI users carry the de](images/08-writing-and-the-humanities-with-ai-fig-01.png)
*Figure 8.1 — Generation at essay scale. Brain-only writers show the strongest networks; habitual AI users carry the deficit even after the tool is removed (Kosmyna et al. 2025, preprint).*

For humanities specifically, the consequence is sharper than for almost any other subject. Humanities grading rewards the writer's *argument*, which is the cognitive structure under the essay. Everything that distinguishes a 5 from a 3 on an AP rubric, an A from a B in a college seminar, an admit from a deny in a competitive admissions read — it lives in the argument the writer can defend. When the artifact is fluent and the argument is empty, the surface reads well and the high-stakes follow-up moments collapse. Nicholas's paper was fluent. His free-response exam was the moment the absence of the argument became visible.

---

## The Load-Bearing Move Is the Inference

The standard framework for argumentative writing is Claim–Evidence–Reasoning: what the paragraph asserts, the specific evidence, and the inference that connects the two. The inference is the load-bearing move.

Most weak humanities writing fails not at the claim and not at the evidence but at the *inferential link* between them. Hillocks's 1986 meta-analysis of writing instruction identified reasoning and elaboration as the most consistently weak component of student writing and the one most responsive to instruction.[^hillocks1986] Students under-perform at the move where the cognitive work concentrates: the specific chain that says *this evidence, properly read, given this context, implies this claim and not some other one*.

AI is structurally good at producing fluent reasoning that sounds like the inferential link without actually performing it. LLMs reproduce the surface — *this passage suggests that, which in turn indicates, demonstrating that* — without the specific inferential event in the writer's head. The C-E-R is on the page. The R that should be in the writer's network is not there.

Here is the difference in concrete form. An AP US History DBQ on the causes of the Civil War; Document 5 is a passage from Stephen Douglas's 1858 debate with Lincoln.

A weak AI-generated C-E-R: *"Popular sovereignty was a failed compromise. Douglas argued that territories should vote slavery up or down. This shows that the issue was contested."* The claim and evidence are present. The reasoning is empty — it does not connect the specific evidence to the specific claim through any inferential move.

A strong student-generated C-E-R: *"Popular sovereignty was an unstable compromise. Douglas in 1858 framed it as letting territories 'vote slavery up or down,' a procedural framing that required separating the question of slavery's expansion from the moral question of slavery itself. That separation was exactly the move the Republican coalition was forming against — the 1860 election demonstrated that voters who heard the procedural framing as evasion could no longer be brought back into the Democratic tent."* The reasoning ties the evidence to the claim through the period's specific political logic. It is specific to this passage, this election cycle, this coalition fracture.

The AI-generated version reads smoothly and sounds like the strong version. A reader trained on AP rubrics will mark it in the middle band. It sounds like an argument. It is not specific to the document. And the student who submits it cannot, in the seminar discussion the following week, reconstruct the argument, because the inferential move never happened in their head.

![Two stacked paragraph blocks of equal width comparing the same Claim-Evidence-Reasoning structure. The top block, labeled AI-generated, shows the Reasoning cell hollow and hatched. The bottom block, labeled student-generated, shows the Reasoning cell filled with specific inferential content about the Republican coalition forming against procedural framing.](../images/08-writing-and-the-humanities-with-ai-fig-02.png)
![Same structure, different cognitive event. The C-E-R surface is identical; only one paragraph performs th](images/08-writing-and-the-humanities-with-ai-fig-02.png)
*Figure 8.2 — Same structure, different cognitive event. The C-E-R surface is identical; only one paragraph performs the inference.*

The misconception to retire: *"AI's reasoning is usually better than mine, so I should accept it."* AI reasoning is fluent, which is not the same as better. Humanities reading rewards specificity to the case. AI reasoning is generic by construction — the Kosmyna NLP analysis confirmed that AI-group essays were linguistically homogeneous within topics, structurally similar to each other in ways brain-only essays were not. And even if AI's reasoning were sharper on this specific paragraph, accepting it builds nothing for the next paragraph, the next essay, the next interview question.

---

## Situation Versus Story

Vivian Gornick's *The Situation and the Story* is a craft book about literary nonfiction, but the distinction it makes is foundational to all humanities writing.[^gornick2001] The *situation* is the surface — what happened, the case, the text being analyzed. The *story* is what the writer is here to say *about* the situation — the claim that animates the analysis, the position the writing exists to defend.

Most weak humanities essays are situation-only. The student summarizes what happened in the historical moment, recapitulates what the philosopher argued, paraphrases the plot of the novel. There is no story — no claim the writer is making about the situation that would not be obvious from a careful reading of the source alone. The essay reports. It does not argue.

AI is structurally good at situation-summary and structurally weak at story-making. A model can produce a passable summary of any well-documented topic. It produces *generic* stories — the kinds of theses that fit any version of the case — and it produces them in a homogeneous voice. The Kosmyna NLP analysis confirmed this: AI-group essays converged in their patterns within topics. The story that would differentiate this writer's essay from the next writer's was the absent ingredient.

Nicholas's Syria/Jordan paper is exactly a situation/story failure. He had a situation he understood — the economic position of Syrian refugees in Jordan's labor market, the UNHCR data, the informal employment patterns. He had a story he had begun to form, something about legal work authorization as the binding constraint that the conventional framing in the literature keeps underweighting. AI generated a fluent synthesis that named the legal constraint without arguing *why* that constraint specifically — rather than cultural friction, housing pressure, or employer discrimination — is the load-bearing cause of the integration dynamic. The story was never on the page. On the AP exam, Nicholas could describe the situation. He could not argue the story, because the story was never his.

Take an AP English Literature essay on *Beloved*. An AI-generated thesis: *"Morrison uses fragmented narrative structure to mirror the trauma of slavery, refusing resolution as both formal choice and ethical claim."* Smooth. Generic. Almost certainly true of any number of post-traumatic novels and therefore not specific to *Beloved*.

A student-generated thesis, after three rough drafts on paper: *"The novel's refusal of chronological resolution is not just formal mimesis of trauma — it is an argument against the demand that survivors be legible to readers who require their stories. Morrison is refusing readers' epistemic access as a condition of the narrative."* This is a story. It is contestable. It commits the writer to a specific reading. A skeptical professor would push back. The student who generated it can defend it.

The story has to exist before AI is allowed in the room, because once AI is in the room, the path of least resistance is for the story to be replaced by generic competence dressed in the situation's vocabulary. That is what happened to Nicholas.

---

## The Human-Only Zone and the Seven-Step Workflow

The cognitive economics of the chapter reduce to one rule: the moves that generate the argument must happen in you, not in the model. Which moves are those?

**Thesis formulation.** The interpretive judgment about what is worth saying cannot be derived from pattern-matching on the situation. This is your story. Three raw thesis drafts on paper, by hand or in a closed document, before any AI contact. Twenty minutes. The first will be bad. The second will be better. The third will surface what you actually think.

**First-draft body paragraphs.** Each paragraph is a fresh C-E-R chain that you generate from scratch: the topic sentence (the claim), the evidence you select, the reasoning that links them. AI is not in the room during this stage. This is where the schema for argumentative writing is built. Outline-then-AI-drafting is the most common violation of this zone and the one that most consistently produces the Nicholas failure mode — fluent paragraphs on the page, empty argument in the head.

**Evidence selection.** Which quote, which datum, which specific phrase from the primary source — these are interpretive choices that constitute the argument. AI can locate sources. AI cannot select what among them most decisively supports your claim, because that selection requires your story.

What goes in the AI-on zone, after the cognitive structure is on the page: critique of your completed drafts for logical gaps, unstated assumptions, and evidence-claim mismatches; structural suggestions for reorganization after a draft is complete; mechanics passes for grammar, punctuation, and citation format.

![A horizontal seven-step workflow bar with steps 1, 3, 4, and 6 filled dark to mark Human-Only steps (three thesis drafts; rewrite thesis; body paragraphs; revise) and steps 2, 5, and 7 shown as outlined boxes to mark AI-on steps (AI critiques thesis; AI finds logical gaps; AI mechanics pass). Below the bar, a four-node phase-gate cycle shows the gate closing after each AI-on step.](../images/08-writing-and-the-humanities-with-ai-fig-03.png)
![Seven steps, two zones, one gate cycle. AI is only ever in the room during steps 2, 5, and 7; the schema ](images/08-writing-and-the-humanities-with-ai-fig-03.png)
*Figure 8.3 — Seven steps, two zones, one gate cycle. AI is only ever in the room during steps 2, 5, and 7; the schema gets built in steps 1, 3, 4, and 6.*

The discipline that makes the workflow work is the phase-gate principle from Chapter 4: AI opens only after independent work has been produced that can be critiqued. AI closes immediately after critique is delivered; revision is human work. AI's final-pass role is strictly mechanical; substantive editing is human work.

---

## The Oral Defense Test

The verification protocol for this chapter is the oral defense test, and it is the sharpest single instrument in the book for detecting the Nicholas failure mode before the interview.

Explain your argument in five minutes without notes to a skeptical listener. They ask two follow-up questions — one that pushes your strongest point harder, one that asks you to extend the argument to a case the essay didn't cover. You answer without notes. If you can do this, the work is yours.

Record yourself. Listen back. Where did you stumble? Where did you summarize the situation rather than argue the story? Where did the follow-up question exceed what you could say?

Three categories of gap, each with a different implication.

*Ownership gap.* You can describe what happened but not what you claimed about it. This is the Kosmyna gap. The cognitive structure was not generated during writing. The fix is not to re-read the essay — the gap is in the network, not in the document. The fix is to redo the workflow on a different essay, holding the Human-Only Zone strictly.

*Extension gap.* You can defend the argument as written but cannot apply it to a novel case. The argument is yours; it has not yet generalized. The fix: apply the argument to one new case per week, in conversation or writing, until extension becomes reflexive.

*Specificity gap.* You can argue the story and extend it, but your speech is more general than your essay — you've lost the specific evidence chains. This is normal in spoken versus written argument and is not a sign of borrowed capability. Rehearse the specific examples once before high-stakes oral moments; the underlying capability is intact.

If you cannot complete the five-minute defense at all, the argument is not yet yours.

---

## Nicholas Redoes the Workflow

The following semester, Nicholas applies the chapter's workflow to a developed version of the same argument — a research competition paper with a faculty panel as the audience. Same topic, Syria and Jordan. Different process.

Step 1, AI off. He spends thirty minutes on paper.

*Draft 1: "Syrian refugees in Jordan face economic integration challenges due to legal barriers and labor market pressures."* Situation, not story. "Face challenges" describes a condition, not a causal argument.

*Draft 2: "Jordan's legal framework for refugee work authorization is the primary barrier to Syrian refugee economic integration, more significant than cultural or housing factors."* Closer. Specific. But "more significant than" claims a comparative weight the paper will need to actually establish from the evidence.

*Draft 3: "Syrian refugee labor market integration in Jordan fails primarily because refugees without work permits are pushed into informal employment — undercutting wages for Jordanian low-income workers and generating the political opposition that blocks the legal reforms that would resolve the dynamic. The conventional framing describes symptoms. This paper argues the cause."* This is a story. Contestable. He commits.

Step 2, AI on. He runs the Thesis Critique prompt. Claude returns: *"Draft 3 makes a contestable structural claim — that the informal-employment dynamic generates the political opposition, which in turn blocks legal reform. The contestable element is the causal direction: does your evidence show that political opposition is generated by wage competition, or could political opposition be independently driven by other factors — cultural, demographic, electoral — that your argument doesn't address? Question: what in your sources most directly supports the causal arrow from informal employment to political opposition, rather than from some third variable to both?"*

He goes back to the sources. Two of the labor market papers he had been relying on show only correlation — wage depression co-occurs with political resistance, but neither establishes the direction. One 2021 World Bank working paper does trace the mechanism through survey data on Jordanian low-income worker attitudes toward refugee employment. That paper is the load-bearing source. He had not made it the center of the argument.

Step 3, AI off. He rewrites the thesis to foreground the survey-data mechanism rather than the aggregate labor statistics.

Step 4, AI off. Five body paragraphs over three days. Each one a C-E-R chain from the real sources, the inferential reasoning his. He treats every claim that appeared in his summer AI synthesis as a claim to re-verify against the original source before it enters this draft. This is the AI-as-primary-source discipline: model output is a starting hypothesis, not a finding.

Step 5, AI on. Hostile-critic prompt. Claude returns three located gaps: the World Bank survey data shows Jordanian worker attitudes but he has not established that those attitudes translate into the specific legislative opposition he's claiming; the steelman of the opposing view — that informal employment is secondary and the primary barrier is employer discrimination, which no work-permit reform would change — is absent from the draft; paragraph 3 uses a UNHCR registration figure in a way that conflates registered with documented, which are different populations in the Jordanian context.

Step 6, AI off. He adds a paragraph engaging the employer-discrimination objection. He fixes the UNHCR conflation with a footnote clarifying the population definition. He revises the policy-opposition section to trace the specific legislative history that links worker-attitude surveys to committee votes.

Step 7, AI on. Mechanics pass. Two citation format issues, one grammar error, "integration" appearing nineteen times. He fixes the mechanics. Three sentences where "integration" was carrying vague argumentative weight get rewritten to make the claim explicit instead.

At the faculty panel, one judge pushes him: *"Your legal-framework argument predicts that Jordan's 2016 work permit reforms should have started resolving the dynamic you describe. They didn't produce the outcome you'd expect. Does that falsify your argument?"* Nicholas has the answer — the 2016 reforms were implemented with sector restrictions that preserved the informal-employment pressure for the largest refugee employment categories. The legal reform was partial, not the full intervention his causal model requires. He extends the argument in real time. The panel continues for fifteen minutes.

The version of Nicholas at that panel is the version that wrote that paper. The version that sat the AP exam was the version that read a Claude synthesis.

---

## Exercises

### Warm-Up — The Situation/Story Split

Take a piece of writing you completed this semester — any essay, any subject. Read it once. Then, on a blank sheet, answer two questions without looking back at the essay: what is the *situation* (what is the essay about)? What is the *story* (what does the essay *claim* about the situation, specifically, that a reader couldn't get from reading the source alone)?

If you can answer both questions in one sentence each, without hedging, the essay has a story. If the "story" answer comes out as a longer description of the situation with slightly more analysis, the essay was situation-only.

This is not a judgment about the grade it got. It is a diagnostic about whether the story was yours. A situation you can articulate is a situation you read. A story you can articulate in one committed sentence is a story you generated.

---

### Application — Three Thesis Drafts Before AI Contact

Pick an essay currently in progress — anything with at least a week until it's due. Before opening any AI tool, write three rough thesis drafts on paper or in a closed document. Twenty minutes total. No research, no notes, just what you think right now. They will be uneven. Let them be.

After twenty minutes, run the Thesis Critique prompt (Prompt 1 in the reference section). Compare AI's identification of each draft's contestable element against your own intuition about which was strongest. Note the gaps between what you thought was your best draft and what the critique surfaces.

Then close AI and write a fourth thesis yourself, incorporating what the critique showed. Do not paste any of AI's language. The fourth thesis is a generation event. The critique was reconnaissance.

---

### LLM Exercise — The Hostile Critic Protocol

Wait until you have a complete draft: thesis, body paragraphs, all generated by you without AI. Then paste the following:

```
I've drafted this essay's argument as follows: [paste thesis + one-paragraph summary of the argument structure].

The full draft is pasted below.

Act as a hostile, highly logical critic of my argument. Specifically:

1. Identify the three most significant logical gaps or unstated assumptions. For each, name the gap precisely — not "you could elaborate" but "the leap from the evidence in paragraph 2 to the claim in paragraph 3 assumes X, which the essay never argues" — and identify the specific sentence or paragraph where the gap appears.

2. Steelman the opposing view. What is the strongest version of the argument against my thesis? Give me the version I have to take seriously, not the strawman I would dismiss easily.

3. Identify one place where my evidence does not actually support the claim I am using it for — where the evidence is consistent with my claim but also consistent with several other claims.

4. Do NOT rewrite any paragraph. Do NOT propose alternative phrasings. Do NOT tell me how to fix anything.

After your critique, ask me one question: which of the three gaps am I least sure I can close?
```

Recovery move when the model hedges: *"Be specific. Cite the paragraph. Name the assumption. Quote the sentence. Opposing counsel's job is to win, not to consider."*

The diagnostic is the same as Chapter 5: if the model's response makes you feel good about your draft, the prompt failed. A working hostile-critic prompt produces the feeling of having more work to do than you thought you had. The gaps it surfaces are the Human-Only Zone work you still owe the essay.

---

### Synthesis — Run the Full Seven-Step Workflow

Apply the chapter's workflow to a current assignment from start to finish. At each stage, note in a running document: what was hard in the Human-Only steps; what AI added in the AI-on steps that you could not have generated yourself; where the AI critique surprised you.

At the end, write one paragraph answering this question: *which step in the workflow changed the essay most, and was that change something you could have made without AI's input at that stage?* The answer tells you where your capability ends and where the tool is filling a genuine gap versus one that would have closed if you'd pushed harder.

---

### Challenge — The Oral Defense, Recorded

Take a completed essay — ideally one that was AI-assisted in any way. Record yourself defending the argument for five minutes without notes. Then either find a skeptical listener or run the Oral Defense Simulator prompt (Prompt 4) with AI as the listener. Answer the two follow-up questions, recorded, without notes.

Listen back. Identify each stumble point. For each one, write a single sentence: is this an ownership gap, an extension gap, or a specificity gap?

If you find an ownership gap — you could describe the situation but not argue the story — that essay is not ready for a high-stakes context (admissions submission, scholarship application, oral exam). The workflow exists to prevent this. Run it on the next essay before you run it on the one that matters most.

---

## Prompt Reference

Five prompts for the five AI-on moments in the workflow. Each one is a structural move, not a recipe — modify the framing for your subject, your essay type, your confidence state.

**Prompt 1 — Thesis Critique.** Use after Step 1 (three raw thesis drafts). Ask AI to identify the contestable element of each draft and whether the evidence base supports each claim. Do not let AI pick a winner or propose a fourth draft. Close with: *"Ask me ONE question about what I am most committed to in any of the three drafts."*

**Prompt 2 — Hostile Critic ("Explain It Like I'm Wrong").** Full text above. Use after Step 4 (body paragraphs completed). Three located logical gaps. Steelman of opposing view. One evidence-claim mismatch. No rewrites. One closing question about your weakest point.

**Prompt 3 — Logical Gap Finder.** Use after Step 4, focused on paragraph-level issues rather than overarching argument. Ask AI to identify: topic sentences that don't match what follows; paragraphs that end broader than they started; transitions that assume connections never established; conclusions that outrun the argument. Located quotes, specific gaps, no fixes proposed.

**Prompt 4 — Oral Defense Simulator.** Use the night before or morning of an oral context. You type a five-minute defense. AI asks two follow-up questions: one that pushes your strongest point, one that asks you to extend the argument to a case you didn't discuss. After you answer, one diagnostic only — did your answer extend the argument or repeat it? Did it apply the principle or get stuck in the original case? No evaluation. No scoring. No suggested fixes.

**Prompt 5 — Mechanics Pass.** Use after Step 6 (revision complete). Grammar errors, punctuation errors, citation format issues, word repetition within paragraphs — specified, not fixed. Output a numbered list. No phrasing changes for "clarity" or "flow." No substantive interference. Recovery move when AI "improves the prose": *"Mechanics only. Do not touch phrasing."*

![A five-by-seven grid with the seven workflow steps on the vertical axis and the five prompts on the horizontal axis. Human-Only step rows carry a dark left band; AI-on rows carry an outlined band. Filled cells mark Prompt 1 at Step 2, Prompts 2 and 3 at Step 5, and Prompts 4 and 5 at Step 7.](../images/08-writing-and-the-humanities-with-ai-fig-04.png)
![The dispatch table. Each prompt enters at one specific gate; the rest of the workflow is the discipline t](images/08-writing-and-the-humanities-with-ai-fig-04.png)
*Figure 8.4 — The dispatch table. Each prompt enters at one specific gate; the rest of the workflow is the discipline that keeps every other gate closed.*

---

## Notes

[^slamecka1978]: Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592–604. <https://doi.org/10.1037/0278-7393.4.6.592>

[^kosmyna2025]: Kosmyna, N., Hauptmann, E., Yuan, Y. T., Situ, J., Liao, X.-H., Beresnitzky, A. V., Braunstein, I., & Maes, P. (2025). Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task. *arXiv* preprint arXiv:2506.08872. MIT Media Lab. Preprint, not yet peer-reviewed; 55% is the upper-bound reduction across analyzed connectivity networks; swap analysis uses 18 participants.

[^hillocks1986]: Hillocks, G. (1986). *Research on Written Composition: New Directions for Teaching.* ERIC Clearinghouse on Reading and Communication Skills.

[^gornick2001]: Gornick, V. (2001). *The Situation and the Story: The Art of Personal Narrative.* Farrar, Straus and Giroux.

---

## AI Wayback Machine

The argument of this chapter — that you do not own a text until you have done the cognitive work of producing it — has a longer history than the Kosmyna preprint. **Mortimer Adler** spent fifty years arguing that reading itself comes in levels, and that the highest level is not absorption but construction. His *How to Read a Book* (1940, revised with Charles Van Doren in 1972) names four: elementary reading (decoding), inspectional reading (skimming for structure), analytical reading (interrogating a single text until you can defend its argument as your own), and *syntopical* reading (placing multiple texts in conversation around a question the books themselves never quite asked). Syntopical reading is precisely the move an AI synthesis cannot do for you — the reader generates a question that no source answers directly, and constructs the argument by making the sources speak to each other. The four-level scheme is, structurally, the same gradient this chapter draws between recognizing a synthesis and owning one.

![Mortimer Adler, 1902–2001. AI-generated portrait based on a public-domain photograph.](../images/mortimer-adler.jpg)
*Mortimer Adler, 1902–2001. AI-generated portrait based on a public-domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Mortimer Adler, and how do the four levels of reading in How to Read a Book (1940/1972) — elementary, inspectional, analytical, syntopical — map onto the framework in this chapter for AI-assisted writing and humanities work? Keep it to three paragraphs. End with the single most surprising thing about his career or method.
```

→ Search **"Mortimer Adler"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask the model to translate Adler's syntopical reading procedure into a step-by-step workflow a student could apply to a five-source humanities essay — and to mark which steps would survive AI assistance and which must remain Human-Only by the logic of this chapter.
- Ask the model about Adler's Great Books project and the *Syntopicon* — and whether the index of 102 "Great Ideas" he co-edited is closer to an LLM's training distribution or to the kind of cognitive structure this chapter argues only the writer can build.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 8.1 — Generation at essay scale. Brain-only writers show the strongest networks; habitual AI users carry the de

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Generation at essay scale. Brain-only writers show the strongest networks; habitual AI users carry the de". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/08-writing-and-the-humanities-with-ai-fig-01.html`

---

### Figure 8.2 — Same structure, different cognitive event. The C-E-R surface is identical; only one paragraph performs th

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Same structure, different cognitive event. The C-E-R surface is identical; only one paragraph performs th". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/08-writing-and-the-humanities-with-ai-fig-02.html`

---

### Figure 8.3 — Seven steps, two zones, one gate cycle. AI is only ever in the room during steps 2, 5, and 7; the schema 

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Seven steps, two zones, one gate cycle. AI is only ever in the room during steps 2, 5, and 7; the schema ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/08-writing-and-the-humanities-with-ai-fig-03.html`

---

### Figure 8.4 — The dispatch table. Each prompt enters at one specific gate; the rest of the workflow is the discipline t

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "The dispatch table. Each prompt enters at one specific gate; the rest of the workflow is the discipline t". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/08-writing-and-the-humanities-with-ai-fig-04.html`
