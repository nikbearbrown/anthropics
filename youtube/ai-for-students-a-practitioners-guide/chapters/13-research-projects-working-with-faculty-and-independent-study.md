# Chapter 13 — Research Projects: Working with Faculty and Independent Study
*The faculty mentor is not assessing the paper. She is assessing you.*

> *"The most important thing a young researcher can learn is what the question is."* — Peter Medawar

---

In May, Nicholas sent an email to a professor he had never met. It said:

> *I'm a high school junior on Cape Cod. I've spent the last year reading about Cold War decision-making and I'm interested in how the academic study of international relations applies to current crises. I'd like to do serious research this summer that contributes something. I've drafted a preliminary topic but I want to learn from someone who actually does this work. Would you be willing to advise me?*

The professor said yes.

What happened over the next twelve weeks is what this chapter is about. Not the paper Nicholas produced — though the paper is good — but the specific sequence of cognitive events that made it good, and the specific places where AI helped versus the specific places where AI would have destroyed it.

Independent research is the moment of truth for everything this book has argued. A polished paper that recombines what AI knows is the failure mode in its purest form. It looks like original inquiry and it isn't. The faculty mentor will eventually tell the difference. The way the mentor tells the difference is the conversation, not the paper. This chapter walks Nicholas's project from May to September with the gate state named at every phase — and by the end you will have a workflow for any independent project you care about.

---

## What the Mentor Is Actually Assessing

Before the workflow, you need to know what you are working toward. Here is what most students believe: if the paper is good, the mentor will be satisfied. Here is what is actually true: the mentor reads polish less than process. A polished paper from a student who cannot defend it in conversation is worse, not better, than a rough paper from a student who can. The mentor knows. The recommendation letter knows.

The Council on Undergraduate Research defines undergraduate research as *"a mentored investigation or creative inquiry conducted by undergraduates that seeks to make a scholarly or artistic contribution to knowledge."* The key words are *mentored* and *contribution to knowledge*. Not *polished deliverable*. The deliverable is how the work gets transmitted; the development is the point.

Faculty mentors of undergraduate researchers report, consistently, that they evaluate in roughly this order: intellectual development visible across the project; capacity to defend and revise when challenged; genuine engagement with primary materials rather than summaries of them; original interpretive contribution; methodological care; and, last, polish of writing. AI is best at the last item and worst at producing the first four. A student who uses AI to optimize the lowest-value item while bypassing the highest-value items has gotten the priority exactly wrong.

![Vertical priority stack of the six things faculty mentors assess in an undergraduate research project, ordered top to bottom by weight. Intellectual development sits at the top; polish of writing at the bottom. A bracket on the right groups the top four with the annotation that AI cannot produce them; a second bracket marks the bottom item as where AI is strongest.](../images/13-research-projects-working-with-faculty-and-independent-study-fig-01.png)
![What the mentor actually assesses. AI's strength is at the bottom of the list.](images/13-research-projects-working-with-faculty-and-independent-study-fig-01.png)
*Figure 13.1 — What the mentor actually assesses. AI's strength is at the bottom of the list.*

What exposes the difference is the conversation. The mentor asks: *"Can you state your central interpretive claim in three sentences?"* The student who built the schema can. The student who borrowed it hesitates, restarts, and summarizes the introduction. The mentor knows in about forty seconds which student is in front of her.

---

## The Citation Fabrication Problem

The most well-characterized failure mode of AI in research is citation fabrication: the model generates plausible-sounding bibliographic references to works that do not exist. This is not a quirk; it is a measured rate.

Walters and Wilder examined 636 AI-generated citations across 84 literature reviews in 2023. They found that 55% of GPT-3.5 citations and 18% of GPT-4 citations were entirely fabricated — the cited works did not exist at all. Among the real citations, 43% of GPT-3.5 entries and 24% of GPT-4 entries contained substantive errors: wrong author, wrong year, wrong volume, wrong title, wrong page numbers. The remarkable property of these fabrications is their plausibility. Journal names are real journals. Author names are real scholars in the field. Titles use the field's vocabulary correctly. Only verification against a database reveals the failure.

A separate study by Bhattacharyya and colleagues on AI-generated medical references found incorrect PMID numbers in 93% of papers, incorrect volume in 64%, incorrect year in 60%. The conclusion: AI-generated bibliographies were "mostly fabricated or inaccurate."

Together these studies establish the empirical baseline. A research paper with thirty citations, drafted with AI running at the GPT-4 rate, expects roughly five fabricated entries. The mathematical expectation matters more than the marketing claim. Newer models have reduced the rate; no major LLM has been independently shown to achieve below-1% fabrication on academic bibliographic generation. The verification is not optional. It is the work.

![Two stacked horizontal bars comparing GPT-3.5 and GPT-4 citation accuracy. GPT-3.5: 55 percent fabricated, 23 percent real but errored, 22 percent accurate. GPT-4: 18 percent fabricated, 24 percent errored, 58 percent accurate. A footnote annotates that at GPT-4 rates a 30-citation paper expects roughly five to six fabricated entries.](../images/13-research-projects-working-with-faculty-and-independent-study-fig-02.png)
![Citation accuracy rates across AI models. Walters and Wilder 2023; the rate has declined but is not zero.](images/13-research-projects-working-with-faculty-and-independent-study-fig-02.png)
*Figure 13.2 — Citation accuracy rates across AI models. Walters and Wilder 2023; the rate has declined but is not zero.*

Nicholas found this out in week one. He asked Claude for a research map of his topic — twenty-eight citations. He spent three days verifying every entry against Google Scholar, journal websites, and DOI resolution. He found three fabricated citations:

A purported 2018 joint article by Sherwin and Bird in the *Journal of Cold War Studies* — Sherwin and Bird co-authored *American Prometheus*, on Oppenheimer; no such joint article exists. A purported 2019 Stern article in *Diplomatic History* — Stern's real work is *The Week the World Stood Still* (Stanford, 2005), not this article. A purported 2021 Allison article in *International Security* — does not exist; Allison's real work is the 1999 *Essence of Decision* with Zelikow.

Three fabrications out of twenty-eight: 10.7%, slightly below the Walters and Wilder GPT-4 rate. He documented the rate in his project journal. He removed the three fabricated entries, kept the verified twenty-five, and began reading.

---

## The Four-Phase Workflow

The phase gate for independent research operates at the project scale. Four phases, sequential. The order is the methodology. Doing two in parallel collapses them.

**Phase 1 — Source location. AI open.** You ask AI to locate primary sources, secondary literature, theoretical frameworks, and key actors. You verify every citation before reading. AI acts here as a search aid plus a map of the field's terrain. This is not "AI does the literature review." This is "AI helps me find the literature, and I verify every entry before I trust it."

**Phase 2 — Interpretation. AI closed.** You read the sources. You take notes — in your own words, by you, not summarized by AI. You form an original interpretation. You commit to a written one-paragraph central claim, three supporting claims, and one acknowledged objection before Phase 3 begins. The commitment is the gate trigger. This phase cannot be shortened.

**Phase 3 — Challenge. AI open.** You ask AI to act as hostile critic of your interpretation — from one or more specific theoretical positions, as a skeptical reviewer naming evidentiary weaknesses, as a practicing scholar naming what is missing. You revise in response. AI does not write your revision; you do.

**Phase 4 — Stress test. AI open.** Before submission to the faculty mentor, you ask AI to simulate the mentor asking hard questions. You answer out loud. You record. You listen back. What you cannot answer is what you do not yet own. You return to Phase 2 for the gaps.

| Phase | Gate state | What you do | What AI does | Trigger to advance |
|---|---|---|---|---|
| 0 — Preliminary | AI closed | Refine the question with the mentor until it is specific. | Nothing. | Mentor approves topic and scope. |
| 1 — Source location | AI open | Verify every citation before reading. | Generates source map and bibliography. | Citations verified; reading list complete. |
| 2 — Interpretation | AI closed | Read sources; take handwritten notes; draft central claim. | Nothing. | Written claim committed on paper. |
| 3 — Challenge | AI open | Revise in response to theoretical challenges. | Hostile critic from named positions. | All challenges run; revisions made. |
| 4 — Stress test | AI open | Answer mentor-simulation questions aloud; listen back. | Plays mentor; asks hardest questions. | Recorded simulation complete; gaps addressed. |
| 5 — Writing | AI closed | Draft the paper. | Nothing. | Final draft composed. |
| 6 — Verification | AI open (light) | Re-verify citations; address over-claims. | Methodological-care audit. | Paper ready for submission. |

*Table 13.1 — The phase-gate sequence for independent research. Two-in-parallel collapses them; the order is the methodology.*

A note on generalization. The four-phase workflow is not specific to history. Seth has applied the same discipline in a different domain in his Zebonastic analysis of the AI-generated music industry — a piece that uses SEC Form D filings as primary documents, RIAA-versus-Suno/Udio court filings as primary legal record, and CISAC's published revenue-impact forecast (a documented 24% of music creators' revenues at risk by 2028) as primary economic data. AI helped him locate the documents and map the landscape. The interpretation was his. The phase gate held the same way it holds for Nicholas: source location with AI assistance, interpretation with AI closed, hostile critique with AI playing skeptical economist, stress test before publishing. The sources differ by domain. The method does not. The gate works because it forces the human cognitive event — the interpretive commitment, written down, before AI is opened — and AI's most-probable summary loses its capacity to foreclose interpretation once the interpretation has already arrived.

The failure mode that destroys independent research is collapsing Phase 1 and Phase 2 — reading AI summaries to "orient," then reading the sources. Once the AI summary has been read, the interpretive event is foreclosed. You are no longer interpreting; you are checking AI's interpretation against the source. The cognitive event the project is supposed to produce does not occur. This is the Nicholas failure from Chapter 1 — the UNHCR report summary, the professor's question three weeks later, the inability to say anything beyond the shape of the argument. At the project scale, the same failure produces a September meeting where the student cannot defend any of the paper's central claims.

---

## The Three Independent Claims Test

The chapter's verification protocol, applied at the project scale. The test asks: can you state three claims that are specifically yours, identify the evidence for each, and explain why a knowledgeable person who hadn't read your paper wouldn't have made the same claim?

Three filters, all required. *"Specifically yours"* rules out field consensus restated. *"Identify the evidence"* rules out free-floating opinion. *"Why a knowledgeable person wouldn't have made the same claim"* rules out the obvious. Three is the threshold: below it, the project is synthesis; above it, something original is happening.

The test is brutal by design. Most undergraduate research papers fail it on the first pass. The students who run it, fail it, and revise are the students whose September conversations go well.

Nicholas tried the test on his draft in week eight. He had a twenty-page paper. Three claims:

*Claim 1.* Khrushchev's October 26 letter shows a leader closer to compromise than the historiographic consensus suggests, based on linguistic features specific to Khrushchev's prose style across the period. Evidence: Nicholas had run a small linguistic comparison across five Khrushchev documents from 1961–1962 himself. Why this is his: the move is not in the secondary literature. *Verdict: original.*

*Claim 2.* The role of Dobrynin's October 27 meeting with Robert Kennedy has been underweighted because the Soviet documentation became available only after 1991. Evidence: post-1991 declassified Soviet documents from the Wilson Center archive. Why this is his: a version of this claim exists in Sherwin (2020), but Nicholas had gone further on the specific mechanism. *Verdict: half original, half synthesis.*

*Claim 3.* The crisis offers a counter-case to offensive realism. Evidence: standard realist literature and standard Cuban Missile Crisis primary sources. Why this is his: it is not specifically his. Wendt and others have made this in print. *Verdict: not specifically his.*

Nicholas has 1.5 original claims, not 3. He returns to the sources. He works on the second half of Claim 2 — what is specifically his beyond what Sherwin says? He drops Claim 3 and replaces it with a claim about *time pressure* as the feature distinguishing back-channel from failed-channel resolution — something he genuinely arrived at from his own primary-source reading and that the secondary literature had not developed. On the second pass, he has three claims that pass all three filters.

![Three-row scorecard of Nicholas's first-pass three-claims test. Claim 1 — Khrushchev's October 26 letter — verdict ORIGINAL. Claim 2 — Dobrynin meeting underweighted — verdict HALF-ORIGINAL, because Sherwin already published a version. Claim 3 — counter-case to offensive realism — verdict NOT HIS, because Wendt and others have published this. A result row beneath reads: 1.5 original claims, not 3. Return to sources.](../images/13-research-projects-working-with-faculty-and-independent-study-fig-03.png)
![Nicholas's first-pass three-claims test. The test is a calibration instrument; fail it early.](images/13-research-projects-working-with-faculty-and-independent-study-fig-03.png)
*Figure 13.3 — Nicholas's first-pass three-claims test. The test is a calibration instrument; fail it early.*

The test is the chapter's specialization of Chapter 6's verification protocols. It is the research-project equivalent of the Spoken Feynman Test: out loud, in your own words, defending claims you actually own. The mentor will run a version of it in September. Run it yourself first.

---

## Nicholas's Summer, Phase by Phase

**Phase 0 — The question (late May).** The professor's first question in their Zoom meeting was: *"What is the question you are actually trying to answer?"* Nicholas did not have a clean answer. Over two weeks of back-and-forth, with the professor pushing, the question became sharp: *Under what conditions do unofficial communication channels between nuclear-armed adversaries enable de-escalation, and what features of those channels distinguish them from failed channels?* No project has begun until the question is this specific. No AI has been opened. There is nothing to apply AI to yet.

**Phase 1 — Sources (early June).** AI open. Nicholas drafted the source-location prompt and verified twenty-eight citations over three days. Three fabrications removed. Reading list finalized. He printed what was printable and requested interlibrary loan for what wasn't.

**Phase 2 — Interpretation (June–July, five weeks).** AI closed.

Nicholas read. He read the JFK Library transcripts of the October 16, 18, 22, 26, and 27 ExComm meetings. He read Khrushchev's October 26 "long letter" — the personal, almost confessional one written under acute pressure — and his October 27 formal letter demanding the Jupiter trade. He read the State Department's record of the Dobrynin–Robert Kennedy meeting on the evening of October 27. He read contemporaneous CIA briefings. He kept a handwritten notebook, one idea per page, in his own words. By week six he had 187 notes, each tied to a specific source page.

In week six he drafted his central interpretive claim three times before he was satisfied:

> *"The Cuban Missile Crisis resolved peacefully in October 1962 through an interaction effect between (a) a material balance that gave Khrushchev strong incentive to withdraw, and (b) a back-channel diplomatic structure (the Dobrynin–Robert Kennedy meeting of October 27) that gave both leaders a face-saving route to act on that incentive without triggering the bureaucratic escalation logic the formal record would have forced. Neither factor alone is sufficient. The back-channel was the operational mechanism through which the structural incentive expressed itself, not an independent cause."*

He wrote three supporting claims. He wrote one acknowledged objection — offensive realism's reply: the back-channel did not cause the de-escalation; the material balance did, and the channel is post-hoc rationalization. He wrote them on paper. The gate trigger for Phase 3 was met.

**Phase 3 — Challenge (early August).** AI open. Nicholas ran the hostile-critic prompt three times — once for Mearsheimer-style offensive realism, once for Allison's bureaucratic politics model, once for Wendt-style constructivism.

The realist challenge was the strongest: Khrushchev's withdrawal was a function of the underlying material balance — US naval superiority, ~17:1 ICBM superiority, no Soviet second-strike capability. The Dobrynin meeting was an effect, not a cause. Without it, Khrushchev still withdraws because the material balance forces him to. Nicholas sat with this for a day. He realized it had surfaced a genuine weakness: he had been treating the back-channel as *the cause* rather than *the route through which an already-determined de-escalation found expression*. He revised Claim 1 accordingly — the version that ended up in his paper is the interaction-effect version, not the back-channel-as-independent-cause version.

The constructivist challenge asked why the back-channel worked, not just that it did. Without the shared identity of "responsible nuclear powers who cannot be the first to use nuclear weapons in anger," the same channel produces different content. Nicholas added a paragraph engaging this.

The bureaucratic-politics challenge pointed to Berlin 1961 as a comparison case he hadn't engaged. He added it to his list.

**Phase 4 — Stress test (mid-August).** AI open. Nicholas recorded twenty-five minutes of himself answering AI-as-mentor questions out loud. Three he couldn't answer fluently. The hardest:

> *"Your claim that the back-channel was operationally necessary depends on the assumption that the formal record would have produced escalation. What primary source evidence do you have for the bureaucratic escalation pressure, and how do you know it would have prevailed?"*

He had assumed it. He had not documented it. He returned to the JFK Library transcripts and found the evidence — the Joint Chiefs' October 27 push for air strikes, LeMay's specific dissent against the blockade, McNamara's documented concern about bureaucratic momentum toward Sunday-morning military action, contemporaneous Soviet military communications showing similar momentum. He revised the relevant paragraph.

**Phases 5–6 — Writing and verification (late August–early September).** AI closed for writing, light touch for the final citation re-check and methodological-care audit. The paper was twelve pages. The argument was his.

---

## The September Meeting

Nicholas submitted the paper. A week later he met with the mentor.

She asked: *"Your central claim has the form of an interaction effect. What is your evidence that both factors are necessary — that you can't get the outcome from either alone?"*

Nicholas thought for a moment. He said:

> *"The clearest counterfactual is Berlin 1961. The material balance was less favorable for withdrawal. There was less bureaucratic time pressure. There was a back-channel — Robert Kennedy and Georgi Bolshakov — but the underlying structural pressure on Khrushchev to withdraw was weaker, and the channel produced different content. The comparison suggests the channel is necessary but not sufficient. I argue back-channel plus material incentive is the combination, and the 1961 case is where the channel without the incentive produced a different outcome."*

The mentor paused. She asked: *"Where in the paper do you make that comparison explicit?"*

He said: *"I don't. I should."*

She nodded. They spent the next forty-five minutes on the Berlin comparison — what additional primary sources he would need, whether the paper should be tightened around the interaction effect or expanded to include Berlin as a second case. He left with a clearer project and an enthusiastic mentor. The recommendation letter she wrote in October was detailed and strong. It noted specifically that Nicholas "demonstrated unusual capacity to engage with hostile theoretical challenges and revise his position based on evidence."

That is what the four-phase workflow produces: a student who has genuinely developed the position and can defend it. Not a student who has produced a polished document and cannot speak past it.

---

## The Prompts

Four prompts for the four phases where AI is open.

### Phase 1 — Source Location

```
I am beginning a research project on [topic]. My preliminary interpretive
direction is [one sentence]. Build a research map:

1. The 5–8 primary source collections most relevant, with access info.
2. The 8–12 canonical secondary works, with full bibliographic citations
   I will verify against Google Scholar and the journal's website.
3. The 3–5 theoretical frameworks the field uses to interpret this material.
4. The 2–3 most recent (last 5 years) contributions that would change how
   a 2026 paper engages this topic.

For each citation: author, year, title, journal/publisher, DOI or stable URL.
I will verify every citation before reading.
```

### Phase 3 — Hostile Critic from Theoretical Position

```
I have written the following one-paragraph central interpretive claim
on [topic]:

[paste your claim]

Act as a hostile reviewer with [specific theoretical commitment —
e.g., "a Mearsheimer-style offensive realist position," "a Bayesian
empiricist position in psychology of judgment"]. Identify:

1. The two assumptions in my claim this position would reject.
2. The strongest piece of evidence that contradicts my claim from
   this position.
3. The one move I make most vulnerable to "your evidence doesn't
   establish what you claim it establishes."

Do not steelman my position. Do not write my response. I will revise.
```

### Phase 4 — Mentor Simulation

```
I have completed a draft research paper on [topic]. My faculty mentor
is a specialist in [mentor's field, theoretical orientation, known
publications — as specific as you can be].

My central claim: [paste]
Three supporting claims: [paste]

Act as my mentor reading this paper for the first time. Ask me your
hardest 20 questions in sequence. Wait for my answer before asking
the next. Be as the mentor would be — specific, demanding, unwilling
to accept hand-waving.

If my answer is strong, ask the next question.
If my answer reveals a gap, name the gap and ask me to account for it.
If I cannot answer, note it explicitly.

I will record this exchange and listen back. What I cannot answer
is what I do not yet own.
```

### Three Claims Test — Verification

```
I will state three claims I believe are specifically mine in my
research paper on [topic]. For each I will identify the evidence
and explain why a knowledgeable reader would not have made the
same claim.

After I state my three:
1. Push back on whether each is genuinely original — is it already
   in the secondary literature in a form I am not citing?
2. Push back on whether my evidence actually supports the claim —
   is the evidence consistent with my claim and with competing claims?
3. Identify the weakest claim and explain specifically why.

Do not soften your critique.

Claim 1: [...] Evidence: [...] Why this is mine: [...]
Claim 2: [...] Evidence: [...] Why this is mine: [...]
Claim 3: [...] Evidence: [...] Why this is mine: [...]
```

---

## Exercises

### Warm-Up

**1.** Ask AI to generate ten bibliographic citations on any topic you are currently studying. Verify each against Google Scholar and the journal's website. Record the fabrication rate — how many do not exist, and how many exist but contain errors (wrong year, wrong volume, wrong pages). Compare to the Walters and Wilder baseline (55% fabricated for GPT-3.5, 18% for GPT-4). Run the exercise again with a different model or prompt. The numbers you collect are a personal calibration you will carry into every research project going forward. *(Tests the empirical foundation of Phase 1; produces a lived experience of why verification is non-negotiable.)*

**2.** Take any paper you have written or are writing — a class paper, a draft, a completed assignment from any course. Without notes, state your central interpretive claim in two sentences. Then state one acknowledged objection to it. If you cannot do both without opening the paper, the central claim was never yours — it was in the artifact. *(Tests whether the student has internalized the distinction between owning an argument and having produced text about one.)*

**3.** Describe, in plain language, why collapsing Phase 1 and Phase 2 destroys independent research even when the student reads every source on the list. What specifically is foreclosed once the AI summary has been read first? *(Tests whether the student can articulate the mechanism, not just follow the rule.)*

---

### Application

**4.** Apply the three-claims test to a paper you have written this semester. State three claims you believe are specifically yours, identify the evidence for each, and explain why a knowledgeable reader wouldn't have made the same claim. Be honest about the verdicts: original, half-original, or not specifically yours. If you cannot reach three claims that pass all three filters, the paper is synthesis with original framing — not a research paper yet. What would you need to do to make it one? *(Operationalizes the three-claims test on real work; forces discrimination between original contribution and synthesis.)*

**5.** Use the Phase 4 mentor simulation prompt on a paper, argument, or project you are preparing to present or submit. Record yourself answering the questions out loud. Listen back. Write down: the three questions you answered least fluently, what specifically you could not retrieve, and what primary or secondary source you would need to return to in order to close each gap. *(Operationalizes Phase 4; produces actionable revision targets.)*

**6.** For a current or upcoming independent project, write a one-paragraph central interpretive claim on paper — without AI — before opening any AI tool. Time how long this takes. Note what you could and could not say. Then use the Phase 3 hostile-critic prompt to stress-test the claim from one specific theoretical position. Note what changed in your claim after the challenge. *(Tests the Phase 2 commitment event and the Phase 2→3 gate trigger; shows the student what revision from genuine challenge looks like.)*

---

### Synthesis

**7.** A classmate argues: "I use AI to generate a summary of each primary source before I read it, so I know what to look for. Then I read the source itself. That's not skipping Phase 2 — I'm still reading the primary sources." Using the chapter's argument about the interpretive event, evaluate this claim. What does the classmate get right? What is structurally wrong with the workflow even when the sources are all read? *(Tests integration of the chapter's core mechanism with a realistic rationalization; requires applying the foreclosure argument, not just citing it.)*

**8.** Design a four-phase research plan for a project you could realistically undertake — a substantial essay, a capstone, a summer independent study, a thesis chapter. Specify for each phase: the gate state, the cognitive event that ends the phase and triggers advancement, the verification protocol, and a realistic timeline. Identify the phase most likely to be violated under time pressure, and describe the specific pre-commitment you would make to hold it. *(Tests whether the student can operationalize the workflow at project scale; the pre-commitment question tests whether they understand why the gate fails under pressure.)*

---

### Challenge

**9.** Take the Nicholas September-meeting scenario and replay it with a different research project — your own, or a hypothetical. The mentor asks: *"Can you state your central interpretive claim in three sentences, name the strongest objection to it, and explain why the objection does not succeed?"* Write the answer you would give if you had done the project with the four-phase workflow. Then write the answer you would give if you had done it with AI handling Phases 1 and 2 together. The difference between those two answers is the difference the workflow makes. *(Open-ended; tests whether the student can model both outcomes and articulate the cognitive difference, not just the procedural one.)*

---

## LLM Exercises

**Exercise: The Mentor Simulation Before the Meeting.** Before any conversation with a faculty mentor that matters — this semester, this year, ever — spend 20 minutes with AI playing the mentor using the Phase 4 prompt. Record. Listen back. The gaps in your answers reveal what you do not yet own. Return to the sources for the gaps. Then meet the mentor. The students who run this exercise do better in mentor conversations. The students who skip it discover the gaps in real time, in front of the mentor, when it is too late to close them.

---

## AI Wayback Machine

The four-phase workflow has a deeper ancestor than the contemporary literature on AI-assisted research suggests. **Vannevar Bush (1890–1974)** ran the U.S. Office of Scientific Research and Development during the Second World War — the program that built radar, proximity fuses, and the bomb — and in 1945 published two documents that still describe what AI is supposed to do for a serious researcher and what it must never replace.

The first, *Science: The Endless Frontier*, was a report to President Truman. Its argument: a wealthy society that wants new knowledge has to fund the people who do the searching, not the products that come out of the search. The mentor relationship Nicholas built that summer — the question first, the methodology second, the deliverable third — is exactly the social architecture Bush was trying to underwrite at the national scale. The second, *As We May Think* in the *Atlantic*, described a hypothetical desk-sized machine Bush called the **memex**: a personal library that stored every document a researcher had ever read and let them link associations between them. The associative trails, not the storage, were the point. The memex would let a researcher follow another researcher's reasoning the way a student today follows footnotes, but instantly and at the speed of thought.

The memex is not what AI is. AI is closer to a co-author than a library. But the warning Bush did not write — and the one that turns out to matter most for this chapter — is that an instrument that follows other people's trails can become a substitute for forming your own. The four-phase workflow is the discipline that keeps the trail yours.

![Vannevar Bush, circa 1940. AI-generated portrait based on public-domain photographs.](../images/vannevar-bush.jpg)
*Vannevar Bush, circa 1940. AI-generated portrait based on public-domain photographs (Library of Congress).*

![Vannevar Bush](../images/vannevar-bush-mwt.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Vannevar Bush, and how do "Science: The Endless Frontier" (1945)
and "As We May Think" (1945) connect to the four-phase research workflow
in this chapter? Keep it to three paragraphs. End with the single most
surprising thing about his career or his ideas.
```

→ Search **"Vannevar Bush"** and **"As We May Think"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it whether the memex anticipated hypertext, AI assistants, or neither — and how the answer changes if you read Bush's later 1967 essay *Memex Revisited*.
- Ask it about Bush's role in the Manhattan Project and how it shaped his postwar argument that government funding for basic research had to be insulated from immediate application.

What changes? What gets better? What gets worse?

---

## Bridge to Chapter 14

Chapter 13 has been about the project scale — twelve weeks, four phases, one mentor relationship, one paper. Chapter 14 is about the long game. The student who builds the phase-gated workflow into a research project does it once and the project benefits. The student who builds the discipline into a *system* — a per-subject prompt library, a verification schedule, a personal knowledge archive, a habit pattern that holds across semesters — sees the discipline compound. Year three of college looks different. Year five of work looks different. The 56% AI wage premium the labor-market data describe goes to the practitioners who built the underlying capability rather than borrowing it. We close Part III by walking through Seth Brown one year later. His roommate has been using AI to do his work all year and cannot explain his work in office hours. Seth has been using AI as a sparring partner and can argue both sides of every case he has studied. He is not smarter. He has a different system. Chapter 14 is how you build the system.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 13.1 — What the mentor actually assesses. AI's strength is at the bottom of the list.

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "What the mentor actually assesses. AI's strength is at the bottom of the list.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/13-research-projects-working-with-faculty-and-independent-study-fig-01.html`

---

### Figure 13.2 — Citation accuracy rates across AI models. Walters and Wilder 2023; the rate has declined but is not zero.

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Citation accuracy rates across AI models. Walters and Wilder 2023; the rate has declined but is not zero.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/13-research-projects-working-with-faculty-and-independent-study-fig-02.html`

---

### Figure 13.3 — Nicholas's first-pass three-claims test. The test is a calibration instrument; fail it early.

Create a standalone D3 v7 HTML file for a checklist or dispatch-card diagram titled "Nicholas's first-pass three-claims test. The test is a calibration instrument; fail it early.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/13-research-projects-working-with-faculty-and-independent-study-fig-03.html`
