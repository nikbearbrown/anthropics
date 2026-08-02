# Chapter 10 — The Headline That Says Nothing


## TL;DR

- Is the headline a topic label, or does it state the slide's claim?
- The chapter moves through The grammar of the problem, The experiment that settled it, Why the label persists, What the change does to the whole deck, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Is the headline a topic label, or does it state the slide's claim?*

---

There is a slide in almost every academic deck that looks exactly like this. The title is **Results**. Below it are three graphs. The speaker says, *As you can see in the middle panel, infection rates dropped by sixty-six percent.*

The audience could not see it. They were looking at the other two graphs.

Not because they are inattentive. Because the slide gave them no reason to look at the middle panel before anywhere else. The word "Results" told them what category of thing is happening on this slide. It did not tell them what to look for, or what the slide is asserting, or why any particular panel matters more than the others. The headline announced a subject. It did not make a claim.

Now multiply that by twelve slides. The deck opened with **Introduction** — three bullets paraphrasing the syllabus. Then **Background** — four bullets summarizing things the audience already knows. Then **Methodology** — three bullets reading *Approach. Data. Analysis.* The bullets were placeholders for sentences the speaker was about to say aloud. Before the speaker said them, the bullets said nothing. After the speaker said them, the bullets were redundant.

Every headline in that deck told you what room you were in. None of them told you what to think.

This is also where every AI slide tool starts by default. Ask for *a slide on the Calvin Cycle* and the headline comes back *The Calvin Cycle* — because the model was trained on millions of academic decks, most of them headlined with labels. The label is the statistical mode. Getting a claim out of the model requires explicitly asking for one. What that ask looks like is what this chapter is about.

---

## The grammar of the problem

The distinction is grammatical before it is pedagogical.

A **label** is a noun phrase. *Methodology. The Calvin Cycle. Q3 Performance. Results.* Labels name the subject. They tell you the topic, the region, the filing category. They are correct as the headings of book chapters and the tabs of indexes, because book chapters are navigated over time — the reader moves through at their own pace, has already read the previous section, knows where they are in the argument. The section label *Discussion* in a paper tells an experienced reader approximately what to expect and lets them navigate. It serves the artifact it lives in.

A **claim** is a complete sentence with a verb that asserts something. *We replicated three classical findings on a corpus ten times larger. The Calvin Cycle fixes carbon in three stages, each requiring ATP. Q3 revenue grew 23%, driven entirely by enterprise renewals. Infection rates dropped by sixty-six percent in the treatment group.* Claims tell you what to think. They hand the audience not just the subject but the slide's position on the subject.

Same content. Different grammar. Completely different cognitive effect.

| Topic | Label headline (wrong) | Claim headline (right) |
|---|---|---|
| Introduction | *Introduction* | *This lecture shows working-memory limits explain three slide failures.* |
| Methodology | *Methodology* | *We replicated three classical findings on a corpus ten times larger.* |
| Results | *Results* | *Infection rates dropped 66% in the treatment group.* |
| Discussion | *Discussion* | *The null result in experiment 2 reflects a ceiling effect.* |
| Conclusion | *Conclusion* | *Assertion headlines reduce load by pre-activating a schema.* |

*The grammar is the diagnostic. Same content, different commitment.*

Here is why the difference is not just rhetorical. When a student reads a label headline, they know the topic. They do not know the claim. To get the claim, they have to reconstruct it from whatever is below — parsing bullets, scanning graphs, extracting the point from the body of evidence. That reconstruction is work. It comes out of the same finite budget of working memory that should be processing the content itself. The label has spent cognitive resources on finding the point before any resources are available for engaging with the point.

When a student reads a claim headline, they receive the assertion before the evidence. The claim pre-activates a schema — a slot in working memory for this specific thought — and the evidence below fills that slot. The student does not hunt for the point. It was handed to them in the first two seconds.

Richard Mayer's Cognitive Theory of Multimedia Learning makes this precise. Learning happens in three steps: the student selects relevant information, organizes it into coherent mental representations, and integrates it with prior knowledge. The label headline disrupts the first step. Without a claim, the student has no basis for selecting which elements of the body are relevant — they would have to reconstruct the claim first. The assertion headline hands the student the organizing frame before the evidence arrives, which is the order working memory can actually use. The schema is ready; the evidence has somewhere to land.

---

## The experiment that settled it

Michael Alley and Kathryn Neeley at Penn State formalized this as the **assertion-evidence structure** in a 2005 paper in *Technical Communication*. Two rules, stated once. The headline is a single declarative sentence stating the slide's main message — not a phrase, not a label, not a topic name. The body is visual evidence for that headline: a diagram, a chart, a photograph, an annotated image, an equation. Not a bulleted list of sub-points. Evidence.

The empirical case for the rule is cleaner than most findings in educational research.

Jennifer Garner and Michael Alley ran a controlled experiment comparing assertion-evidence structure against the default topic-header-plus-bullets structure. One hundred and ten undergraduate engineering students. Parallel slide sets covering identical content. The only variable was the headline and body structure. The assertion-evidence group showed superior comprehension, fewer misconceptions, lower self-reported cognitive load, and stronger recall on both immediate and delayed post-tests. Earlier work by Garner, Alley, and colleagues found the advantage was largest for complex conceptual material — which is exactly the case academic lectures face. Later work by Wolfe and colleagues extended the finding across computer science, medical, and engineering student populations and confirmed it generalizes.

![The label makes finding the point the reader's job. The claim does it for them.](images/10-the-headline-that-says-nothing-fig-01.png)
*Figure 10.1 — Schematic of how the assertion-evidence structure processes in*

The mechanism in one sentence: the headline gives the student a schema before they see the evidence, so they encode the evidence into the schema rather than hunting for one.

Cliff Atkinson arrived at the same prescription from the other end — working with management consultants rather than engineers, developing what he called "Beyond Bullet Points" for business presentation. Engineering professors at Penn State, management consultants trained at McKinsey, journalists writing nut grafs — they all face the same constraint, which is that audience attention and working memory are finite, and they all arrive at the same solution, which is to lead with the claim. The prescription is not a stylistic preference. It is the solution to a structural problem in how working memory processes information under time pressure.

---

## Why the label persists

If assertion headlines are demonstrably better, why does every AI slide generator produce labels?

The answer is that the tools are trained on academic decks, and academic decks use labels. The tool learned the default. The default is the failure mode.

But the deeper reason labels persist — in human-authored decks, not just AI-generated ones — is that they are easier to write in a specific, uncomfortable sense. A label requires no commitment. *Methodology* can go on the slide before you have decided what your methodology *is*, before you have figured out what it *shows*, before you know what you are claiming about it. The label is a placeholder for a decision that hasn't been made yet. An assertion, by contrast, requires you to know what the slide is for. *We sampled 10,000 participants across six countries using stratified randomization.* That is a decision. The commitment might be uncomfortable if you are not yet sure whether that is the most important thing about your methodology. The label lets you defer. The assertion forces you to decide.

This is actually diagnostic. When you cannot write an assertion headline for a slide, it usually means the slide does not yet know what it is claiming. That is information about the slide's readiness, not about your ability to write headlines. A slide that cannot produce an assertion may be two slides that need to be separated. It may be a reference slide — agenda, glossary, term list — where a label is the correct form. Or it may be a slide that should be cut entirely, whose content belongs in the notes field or not in the deck at all.

The assertion test is, among other things, a curation tool. When you cannot write the assertion, you have learned something the label was hiding.

![The assertion test is a curation tool. Failure to produce an assertion is a signal about the slide, not the author.](images/10-the-headline-that-says-nothing-fig-02.png)
*Figure 10.2 — Decision flowchart for what to do when a*

---

## What the change does to the whole deck

The change happens at the headline, but its effects propagate.

When the lecture-opening Introduction slide becomes an assertion — *This lecture will show that working-memory limits explain three failure modes in slide design* — it does several things simultaneously. It gives the rest of the deck somewhere to land. Every subsequent slide either advances the claim or extends it. The student receives the organizing frame for the lecture in the first ten seconds of attention, when prior knowledge is unattached and schema formation is most plastic. The opening slide is the highest-leverage real estate in the deck. A topic label wastes it.

When the Results slide becomes *Infection rates dropped 66% in the treatment group*, the three graphs lose their ambiguity. The student does not need to scan all three looking for the finding. The claim directed them to the middle panel before the speaker said a word. The visual hierarchy follows from the rhetorical hierarchy.

When the Methodology slide becomes *We replicated three classical findings on a corpus ten times larger*, the three sub-elements become evidence rather than bullet points. They are not indexing sub-topics; they are labeled blocks of visual evidence supporting a specific claim. The student reads each one knowing what it evidences.

There is a compounding effect here worth naming explicitly. When every slide states its claim in the headline, the deck becomes readable without the speaker. A student who missed class can read the deck and extract the argument — not just the topics, the argument — because the claims are in the headlines in sequence.

![A deck of assertion headlines is an argument. A deck of label headlines is a table of contents.](images/10-the-headline-that-says-nothing-fig-03.png)
*Figure 10.3 — Two versions of the same five-slide deck shown*

A deck of assertion headlines is an argument. A deck of label headlines is a table of contents. The same slide file, the same content, the same visual evidence — but one has a logical structure that is visible in thirty seconds, and the other doesn't.

This is also what makes the two-artifact solution from Chapter 1 work cleanly. The assertion headline carries the claim. The notes field carries the explanation. Together they produce a deck that functions as a live lecture aid — assertion gives the student the frame, explanation is delivered verbally — and as a study artifact — claim in the headline, explanation in the notes, visual evidence in the body. The assertion headline is the load-bearing element that makes both functions possible. A label headline produces neither.

---

## The limits of the rule

Two limits are worth naming, because applying the rule without them produces different mistakes.

The first is reference slides. An agenda slide is a reference slide. A glossary is a reference slide. A key-terms recap is a reference slide. These serve a navigation or lookup function, not a teaching function. Forcing assertions onto them produces awkward fictions: *The agenda for today is six items long* is not a useful headline. The rule is: teaching slides default to assertions, reference slides correctly use labels, and the difference between them should be an explicit decision rather than a per-slide guess. Most decks have three to five reference slides in fifty. The default is assertion; the exception is label; the exception should be named.

The second limit is length. An assertion that runs to twenty words usually contains either two claims — which want two slides — or an unnecessary clause — which wants cutting. The practical ceiling is around twelve words. Not because twelve is magic, but because a headline that exceeds it is usually telling you something. Either the claim is genuinely too complex to state simply, which means the slide may be trying to do two things; or the author is hedging, adding qualifications that belong in the body or the notes. When the headline runs long, the question is not *how do I shorten this?* It is *is this one slide or two, and what am I hedging?*

Short complete sentences do most of the work most of the time. *The proton gradient powers ATP synthase.* Six words. *We replicated three classical findings on a corpus ten times larger.* Twelve words. Each earns its length.

---

## Two honest disagreements

Two faculty members who have read everything above can still disagree. Naming where matters more than picking a side.

The first disagreement is about what belongs in the body. Alley's strict assertion-evidence structure excludes bullets from the body entirely — evidence means a diagram, a chart, a labeled image, not a vertical list of text fragments. A more relaxed reading says the crucial move is the assertion headline, and the body can contain labeled blocks of evidence in whatever form fits the content. The defensible position in framework terms: bullets are usually a tell that the author has not chosen a visual form. When content is genuinely enumerative, labeled evidence blocks typically outperform bullets because they name what each block evidences; a diagram or chart typically outperforms both. The position you cannot defend is bullets because they are the default.

The second disagreement is whether slides and papers should share a headline grammar. The common faculty objection is that papers use section labels — Introduction, Methods, Results — and asking slides to use full sentences feels inconsistent with academic writing conventions. The objection is real and resolves the moment you name the artifacts. A paper is read over minutes per page, often re-read, with the section header serving as a navigational anchor for a reader who has been following an argument for ten pages. A slide is scanned in three seconds, with no prior context, no opportunity to re-read, no navigation available. Different artifacts, different reading conditions, different headline grammars. The label is correct for the section header of a paper. It is not correct for the title of a slide. Once you name which artifact you are designing for, the disagreement dissolves.

| Dimension | Paper section header | Slide title |
|---|---|---|
| Reading distance | Arm's length, eyes on page | Across a room, projected |
| Dwell time | Minutes per page, often re-read | Three seconds, scanned once |
| Reader controls pace | Yes — flip back, slow down | No — speaker controls advance |
| Re-reading available | Yes, freely | No, the slide is gone |
| Navigational role | Anchor inside a sustained argument | First (and possibly only) signal of intent |
| Correct headline grammar | Label (noun phrase) | Claim (full sentence) |

*Same information, different artifact, different grammar. Naming the artifact resolves the disagreement.*

---

## The test

The chapter is a long argument for one short test.

*Is the headline a claim or a label?*

A claim has a verb and asserts something. A label is a noun phrase that names the subject. The grammar is the diagnostic. Apply it to the next deck. Find the slides with topic labels. For each one, ask: what is this slide claiming? If you can answer, write the answer as the headline. If you cannot, the slide does not yet know what it is claiming — and the right response is to ask whether the slide should be cut or split before it is rewritten.

Most of the slides that fail the test are not poorly executed. They are poorly specified. The author knows what the slide is about but has not committed to what the slide is *saying*. The assertion headline is not a design fix. It is a commitment — to have figured out, before the slide reaches an audience, what the slide is for.

Once you have the claim in the headline, the body usually knows what to do. The evidence organizes itself around something it is evidencing. The visual form follows from the claim. The slide stops being a hat rack and becomes an argument.

---

**What would change my mind:** A replication of Garner and Alley's experiment in an asynchronous study-artifact condition — slides read without a speaker — that finds the assertion-evidence advantage does not hold when the slide is the only source of explanation. The existing evidence is from live or recorded-lecture conditions, which is the strongest case for assertion headlines. The asynchronous case is plausibly assertion-favorable but empirically thinner. A strong null there would narrow the prescription to live-lecture decks.

**Still puzzling:** I do not have a clean rule for the length ceiling on an assertion. The chapter sets twelve words as a working maximum, but the number is a convention, not a finding. The assertion-evidence literature is mostly silent on length thresholds. A defensible benchmark would require an empirical study I have not found.

---

## LLM Exercises

**Exercise 1 — Label audit**
Take any deck you have built or received. Paste the slide titles — just the titles, nothing else — to an LLM with this prompt: *"For each of these slide titles, classify it as a label (noun phrase naming a topic) or a claim (complete sentence asserting something). Count how many are labels and how many are claims. For each label, ask: what is this slide likely claiming? If you can infer a claim, write it as an assertion headline. If you cannot, flag the slide as 'claim not recoverable.'"* Use the output as a deck-level audit before the lecture.

**Exercise 2 — Assertion rewrite**
Choose three slides from your deck that currently have label headlines. For each slide, paste the title and the body content to an LLM with this prompt: *"Rewrite this slide's headline as a single declarative sentence — a claim, not a topic label. The headline should state what the body substantiates. Maximum 12 words. If the body does not contain a recoverable claim, say so explicitly rather than inventing one."* If the LLM cannot recover a claim from the body, treat that slide as a candidate for cutting or splitting.

**Exercise 3 — Opening slide diagnosis**
Paste your deck's first content slide (after any title slide) to an LLM with this prompt: *"This is the opening content slide of a lecture deck. Does the headline state a claim the rest of the lecture will substantiate, or does it announce a topic? If it announces a topic, rewrite it as an assertion that gives the rest of the deck somewhere to land. The rewritten headline should make a student reading only this slide know what argument they are about to follow."* Use the rewritten opening as the frame the deck is organized around.

**Exercise 4 — Reference slide classification**
Paste your full deck's slide titles to an LLM with this prompt: *"Classify each slide title as: (a) a teaching slide that should have an assertion headline, (b) a reference slide (agenda, glossary, key-terms list, section divider) where a label headline is correct, or (c) ambiguous. For category (a) slides that currently have label headlines, write the assertion. For category (b) slides, confirm the label is appropriate. For category (c) slides, ask: what is this slide's function — teaching something new or providing something for lookup?"* Use the classification to distinguish where the assertion rule applies.

**Exercise 5 — Deck argument extraction**
After rewriting your deck's headlines as assertions, paste all the new assertion headlines in sequence to an LLM with this prompt: *"Read these slide headlines in order. Do they form a coherent argument — each claim following from or building on the previous? Or are they a sequence of independent claims with no visible logical connection? If the latter, identify where the argument breaks and what connecting claim is missing between those two slides."* A deck of assertion headlines should read as an argument. If it does not, the deck has a sequencing problem the assertion rewrite has now made visible.

---

## Tier Connection

The headline-as-claim rule is the chapter where Tier 7 judgment is forced to the top of every slide. A claim is the author's interpretive position — *what this slide is saying that the audience should think* — written where the audience can read it and the author can be held to it. A label is the absence of that position. The model can produce both. Asked for either, it produces the requested grammar. Asked for "a good title," it produces a label most of the time, because labels are what most of its training data looks like.

The Tier 4 plausibility audit runs against the claim. A claim is auditable — you can check whether the body supports it, whether the evidence presented is sufficient, whether a hostile reader could falsify it. A label is not auditable. It is a category, not an assertion. The discipline of writing claims is therefore also the discipline of making the slide's argument auditable in real time — by the speaker, by a student, by anyone who looks at the slide and asks *is this true?* See *Appendix A — The Fundamental Themes*.

---

## Exercises

### Warm-up

**1.** Below are eight slide headlines from a real academic deck. Classify each as a label (noun phrase naming a topic) or a claim (complete sentence asserting something). For each label, write a one-sentence assertion that could replace it — using only the information the headline itself provides, without inventing content.

- *Background*
- *Working memory limits determine what a student can learn from a slide.*
- *The Calvin Cycle*
- *Infection rates dropped 66% in the treatment group.*
- *Implications*
- *Methods*
- *Three structural failures explain why AI-generated decks underperform.*
- *Results*

*(Tests: label vs. claim classification, assertion writing from minimal input)*

**2.** The chapter distinguishes two artifacts: a paper section header and a slide title. Give one reason the label *Methods* is the correct form for a paper section header and the wrong form for a slide title. Your answer must name the specific reading condition that differs between the two artifacts. *(Tests: artifact-type distinction, the reading-conditions argument)*

**3.** A colleague defends the label *Results* on their slide by saying: "The audience will figure out the finding when I explain it." Identify which step of Mayer's three-step learning model this defence violates, and explain why the burden of reconstruction lands on working memory rather than on long-term understanding. *(Tests: Mayer's three-step model applied to the label-vs-claim distinction)*

### Application

**4.** Take any five consecutive slides from a deck you have built or used. Paste only the headline of each slide. Classify each as label or claim. For each label, write the assertion — the actual claim the slide is making — using your knowledge of the content. Then ask: do the five assertion headlines, read in sequence, form a coherent argument? If not, identify where the logical connection between slides is missing. *(Tests: label audit, assertion writing from own material, argument-coherence check)*

**5.** The chapter argues that inability to write an assertion is diagnostic: it signals that the slide does not yet know what it is claiming. Apply this to a slide you currently have labeled *Introduction* or *Background*. Try to write the assertion. If you succeed, rewrite the headline. If you cannot, state which of the three curation outcomes applies: (a) two claims competing that want two slides, (b) a reference slide where a label is correct, or (c) a slide that should be cut. *(Tests: assertion test as curation tool, ability to reach a verdict and act on it)*

**6.** The chapter sets a working ceiling of twelve words for an assertion headline. Take the following twenty-two-word assertion and cut it to twelve words or fewer without losing the claim: *"Our analysis suggests that, given sufficient sample size, the effect of sleep deprivation on working memory capacity appears to be statistically significant."* Then identify which words were hedges that belonged in the body or notes rather than in the headline. *(Tests: assertion length ceiling, distinguishing claim from qualification)*

**7.** Rewrite the following label headlines as assertions for each scenario described. Write a full declarative sentence in twelve words or fewer.

- *Methodology* — for a slide explaining that participants were recruited via stratified random sampling across six countries.
- *Discussion* — for a slide arguing that the null result in experiment 2 is explained by a ceiling effect in the measure.
- *Conclusion* — for a slide claiming that assertion headlines reduce cognitive load by pre-activating a schema before evidence is presented.

*(Tests: assertion writing across the three hardest academic section labels — the ones most likely to stay as labels because the section boundary feels like an excuse)*

### Synthesis

**8.** The chapter presents convergent evidence from three independent sources — Alley and Neeley (2005) from engineering education, Garner and Alley from experimental research, and Atkinson from management consulting — all arriving at the same prescription. What does convergence across such different domains and methods tell you about whether the claim is a stylistic preference or a structural constraint? Make the argument in your own words. *(Tests: ability to read cross-domain convergence as mechanistic evidence, not just a pile of citations)*

**9.** The "two honest disagreements" section presents the paper-vs-slide objection and resolves it by naming the artifact. Apply the same move to a different domain: a book chapter heading versus a PowerPoint slide title versus the subject line of a professional email. For each artifact, name the reading condition, state whether a label or a claim is the correct form, and give the one-sentence reason. *(Tests: ability to generalize the artifact-naming resolution to new cases)*

**10.** The chapter argues that a deck of assertion headlines "is an argument" while a deck of labels "is a table of contents." Identify one situation where you would actually want a table of contents rather than an argument — where the label-deck structure is the correct design choice — and explain what the audience's task is in that situation that makes labels the right form. *(Tests: ability to identify the genuine exception to the assertion rule, not just accept the claim as absolute)*

### Challenge

**11.** The "what would change my mind" section identifies one evidentiary gap: no strong test of assertion-evidence advantage in an asynchronous study-artifact condition — slides without a speaker. Design that study. Specify the independent variable, the control condition, the outcome measures (at minimum: immediate recall, delayed transfer, cognitive load rating), and what you would control for to isolate the headline effect from the body structure effect. State what finding would narrow the chapter's prescription to live-lecture decks only. *(Tests: ability to identify and close an evidentiary gap through research design — requires engaging with what the existing experiments did and did not test)*

**12.** The "still puzzling" section admits there is no empirically grounded ceiling for assertion headline length — twelve words is a convention. Design a minimal experiment that would produce a defensible length threshold. What would you vary, what would you measure, and how would you operationalize "the headline has become too complex" as a measurable outcome rather than an editorial judgment? *(Tests: ability to convert an open methodological question into a testable design — the chapter admits uncertainty; the exercise asks the student to close it)*

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 10.1 — Schematic of how the assertion-evidence structure processes in

Create a standalone D3 v7 HTML file for a left-to-right flow diagram titled "Schematic of how the assertion-evidence structure processes in". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-the-headline-that-says-nothing-fig-01.html`

---

### Figure 10.2 — Decision flowchart for what to do when a

Create a standalone D3 v7 HTML file for a left-to-right flow diagram titled "Decision flowchart for what to do when a". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-the-headline-that-says-nothing-fig-02.html`

---

### Figure 10.3 — Two versions of the same five-slide deck shown

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Two versions of the same five-slide deck shown". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/10-the-headline-that-says-nothing-fig-03.html`
