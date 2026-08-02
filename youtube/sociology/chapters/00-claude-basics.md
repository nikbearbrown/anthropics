# Chapter 00 — Claude Basics: Using LLMs in Sociology

**Suggested titles:**
1. Claude Basics: Using LLMs in Sociology
2. The Tool, the Pitfalls, and the Disciplines That Make Sociological Work Possible
3. How to Think Sociologically With (Not For) an LLM

**TL;DR.** Large language models like Claude, ChatGPT, and Gemini are powerful tools for sociological work — synthesizing literature, drafting analysis, comparing frameworks, summarizing complex empirical patterns. They are also particularly dangerous for sociological work in specific ways. Sociology's vocabulary carries heavy normative weight; its empirical questions are often genuinely contested; its qualitative dimension resists what LLMs are good at. This chapter establishes the rules of engagement for the rest of the book.

---

A student in this class will, almost inevitably, hand in a paper containing a quote from "the influential 1973 ethnography by Patricia Mendoza of working-class Mexican Americans in East Los Angeles" — a book that does not exist, by an author who does not exist, about a community the LLM has constructed from the patterns of similar ethnographies it was trained on. The DOI will look right. The publisher (Stanford University Press, perhaps) will be plausible. The author has a name that fits the ethnographic-sociology field. The student will not have invented this; an LLM will have, and the student will have copied it without checking, because the citation looked right and the broader claim it was supporting fit what the student was trying to argue.

This is not hypothetical. It happens routinely. It is the most common failure mode in undergraduate sociology work that uses LLMs, and it has been since 2023. The cost is high — submitting fabricated citations is, in most institutions, treated as plagiarism or fabrication, regardless of whether the student knew. The cost is preventable with a small amount of discipline and a clear understanding of what these tools are and are not.

Sociology, as a discipline, has specific vulnerabilities to LLM-assisted work that go beyond what other fields face. The vocabulary of sociology — *power*, *privilege*, *oppression*, *marginalization*, *deviance*, *agency*, *structure*, *intersectionality*, *cultural capital* — carries heavy normative weight that LLMs absorb and reproduce without flagging. The empirical questions in sociology are often genuinely contested; the literature contains frameworks that disagree fundamentally on the same evidence. The qualitative-ethnographic dimension of sociology resists exactly what LLMs are good at; immersed knowledge of specific communities cannot be plausibly faked, but LLM output can sound plausible to a reader who has never been immersed.

This chapter is about how to use LLMs in sociological work without being misled by them. It is the first chapter in this book because the rest of the book asks you to use these tools — for Dig Deeper prompts inside chapters, for end-of-chapter LLM Exercises, for a running project that will accumulate across the term. Before any of that work begins, you need to understand what the tools are doing, what specifically goes wrong in sociological applications, and how to use them productively despite their limits.

Some material in this chapter parallels what students of the companion textbooks in this series (*Principles of Finance with LLMs*; *Introduction to Political Science with LLMs*) encounter; the disciplines and the failure modes have substantial overlap. The sociology-specific sections — particularly Concept 2 on what goes wrong in sociological work — are essential reading even if you have seen LLM-orientation material elsewhere.

## Learning objectives

By the end of this chapter you should be able to:

1. Explain in plain language what an LLM does and does not do.
2. Identify failure modes specific to sociological work — fabrication; smoothing of contested empirical findings; hidden normative framings; the qualitative-ethnographic gap.
3. Distinguish the major LLMs (Claude, ChatGPT, Gemini) at a useful level.
4. Write a productive prompt for sociological analysis — including the moves that reveal disagreement, surface framings, and force specificity.
5. Verify sociological claims an LLM makes against primary sources — and do this routinely, not just when something seems suspicious.
6. Apply multi-LLM comparison strategically rather than mechanically — using disagreement among LLMs as a signal for where to dig deeper.
7. Hold the appropriate skeptical-collaborative posture: the LLM is a synthesis and drafting partner, not an authoritative source; the responsibility for the work remains yours.

---

## Concept 1 — What an LLM actually does

You should know, at some level of detail, what is happening when Claude responds to a prompt. Most students never learn this and end up with mistaken intuitions that produce predictable errors.

A large language model is a statistical system trained on enormous quantities of text — books, papers, websites, news articles, code, conversations. The training process produces a system that, given a sequence of words (the prompt), predicts the next word in a way that reflects patterns in the training data. The system then takes the prompt plus its predicted next word, predicts the next-next word, and so on, generating text token by token.

What the system has learned, in this process, is a great deal of linguistic, factual, and analytical structure. It has absorbed enormous amounts of sociology — what good sociological argument looks like, what frameworks dominate which subfields, what disagreements exist in the literature, what specific scholars have argued. It is, in many ways, a remarkably knowledgeable interlocutor about sociology.

What the system has *not* done is verify any of it. It has read sources that contradict each other and has no built-in mechanism for adjudicating among them. It has read sources of varying reliability and has only an indirect sense of which sources are more trustworthy. It cannot, in most current configurations, look up a fact in real time — it produces output based on what its training process produced as a likely continuation of the prompt. Whether the continuation is true is a separate question.

This has several consequences worth internalizing.

**LLMs hallucinate.** The system can produce confident-sounding text containing claims that are simply false — a citation to an ethnography that doesn't exist, a statistic that was never reported, a quote that was never said by the scholar who supposedly said it. The technical name in the field is *hallucination*, though *fabrication* is closer to what is happening. The hallucination rate has been falling as the systems improve, but it has not gone to zero, and it is concentrated in exactly the kind of detailed factual claims (citations, statistics, quotes from specific studies) that academic work depends on.

**LLMs reflect the patterns of their training data.** If the training data over-represents one perspective on a contested question, the LLM's responses will tend to reflect that over-representation. This is not a deliberate bias in any sinister sense; it is a structural feature of statistical learning from a corpus. The corpus matters. For sociological work, this is particularly consequential — the contemporary sociology corpus represented in LLM training data does not capture the full range of perspectives in the field, and certain framings dominate.

**LLMs can be remarkably useful at synthesis.** Asked to summarize the major positions in a sociological debate, an LLM will often produce a quite good summary — capturing the central claims, the major scholars, the empirical disputes, the normative tensions. The synthesis function is one of their strongest uses. Verification of specific claims still has to happen separately.

**LLMs are not search engines.** A search engine retrieves existing documents. An LLM generates new text based on patterns learned from documents. The document the LLM appears to be quoting may not exist. The LLM's response is not itself a document you should cite; it is a generated response that may be useful for thinking but should not be treated as authoritative.

### Common misconceptions

**"The LLM is connecting to a database of sociological research."** Most LLM systems, in their default configuration, are not. They are generating text based on patterns. Some systems have been augmented with retrieval (asking the model to look up information from a separate corpus before responding), and the answers improve when this is done. But the default behavior of most popular LLMs is generation, not retrieval.

**"If the LLM is confident, it is probably right."** Confidence in LLM output is not calibrated to truth. The model produces fluent text whether the underlying claim is well-supported or fabricated. Tone is not evidence.

**"LLMs are replacing sociologists."** They are augmenting them, sometimes substantially, particularly for specific tasks (literature synthesis; preliminary analysis; first-draft writing). The work that LLMs are good at — synthesis, drafting, comparing frameworks — is real work. The work they cannot do — original empirical research; verifying primary sources; extended ethnographic immersion; exercising judgment about contested empirical and theoretical questions; taking responsibility for conclusions — is also real work and is what sociology is centrally about.

---

## Concept 2 — Four failure modes specific to sociological work

Every academic field has to handle LLM failure modes. Sociology has some that are sharper or more frequent than what other fields face. Four are worth flagging carefully.

### Fabrication of sources, scholars, ethnographies, and statistics

This is the failure mode that has destroyed undergraduate sociology work most reliably since 2023. Asked for citations, ethnographic studies, specific statistics, or quotes from sociologists, an LLM will produce a list of plausible-sounding items. Some will be entirely real; some will be partially correct (real author wrong title; correct title wrong year; real concept attributed to wrong scholar); some will be entirely fabricated.

The fabrications are particularly difficult to detect in sociology because:

- The discipline includes an enormous number of specific ethnographic studies, demographic-data analyses, and case-study sociology — the LLM can invent plausible new ones that fit the general patterns
- Sociologists' names often follow specific demographic patterns (the academy has had specific waves of incorporation of different populations); the LLM can invent plausibly-named scholars
- The discipline's writing conventions are recognizable, so plausibly-formatted fake citations look right at a glance
- Specific empirical findings in sociology are often unique single-study results; the LLM can invent plausible new findings

The discipline this requires: never use a citation, statistic, or specific finding in your own work that you have not personally located in the actual source. If an LLM gives you an ethnographic study, find the actual book in your library catalog or Google Scholar before using it. If it gives you a specific statistic, find the underlying data source. If it quotes a specific scholar, find the actual passage. If you cannot find the source, do not cite it.

A small but important refinement: even when the LLM cites a real scholar and a real work, the quote it provides may not be what the scholar actually wrote, or may be from a different work than cited, or may be subtly distorted. Always read the actual passage before quoting.

### Smoothing of contested empirical findings

Sociology contains genuine empirical disagreements — questions where careful researchers examining the same evidence reach different conclusions. The relationship between family structure and child outcomes (Ch 14); the magnitude of gender pay-gap discrimination (Ch 12); the social-vs.-individual contributions to specific health gaps (Ch 19); the empirical effects of social media on adolescent mental health (Ch 8); the relative weights of structural-vs.-individual factors in racial inequality (Ch 11); the empirical record on movement effectiveness (Ch 21). These are not "anyone's guess" — careful empirical work narrows what positions are reasonable. But they are not settled.

LLMs frequently smooth these disagreements into apparent consensus. Asked "what does the literature say about X," an LLM may respond with a single coherent narrative that flattens the genuine contestation. The student who relies on this gets a misleading picture of how sociology actually operates.

The discipline this requires: ask the LLM specifically about disagreements. *"Where do scholars disagree on this question?"* *"What is the strongest counter-argument to the position you just stated?"* *"What scholars or schools push back against this view?"* This kind of prompting often produces dramatically better output, because it forces the LLM to surface the disagreement structure rather than producing smoothed synthesis.

### Hidden normative framings

This is perhaps the most distinctive sociological failure mode. Sociology is not value-free, and its central vocabulary carries normative weight. *Inequality, oppression, privilege, marginalization, structural racism, exploitation, hegemony, internalized misogyny, deviance, agency, intersectionality* — each of these terms organizes some empirical phenomenon and also implies a specific normative orientation toward it.

An LLM trained on a corpus that over-represents certain framings will reproduce those framings, often without flagging that it is doing so. The "conventional wisdom" of one tradition will appear as just "the way things are," and the contested framings of competing traditions will be presented as if they were the discipline's settled view. A student using LLM output uncritically may absorb framings without recognizing they are framings.

This is especially treacherous on contested current-events questions where the line between empirical and normative is itself contested. An LLM's response on questions about the gender pay gap, contemporary racial inequality, the politics of immigration, the assessment of a specific social movement, family-policy debates — none of these is neutral, and many are presented as if they were.

The discipline this requires: ask the LLM what tradition or perspective is implicit in its response. *"From which theoretical tradition is this analysis coming?"* *"How would scholars in different traditions (functionalist, conflict-theoretic, interactionist, intersectional, biosocial, etc.) respond differently?"* *"What assumptions am I being asked to share, and are they contested?"* *"What is the strongest version of the position the LLM seems less inclined to support?"* Forcing the framing into the open is a teaching move that good sociology professors have always made; doing it with LLM output makes the LLM more useful and you a sharper analyst.

### The qualitative-ethnographic gap

Sociology has a major tradition of qualitative work — ethnography, in-depth interviews, archival research, immersive observation in specific communities. This work produces knowledge that LLMs are particularly poorly equipped to simulate.

Why? Because qualitative knowledge is fundamentally about specifics — what specific people in specific places said and did, with specific contexts, specific tones, specific reactions. An LLM can produce text that sounds like ethnographic observation but cannot have observed anything. It can describe what an ethnographer might have found in a particular community but cannot generate genuine knowledge of that community.

The risk: a student using an LLM to write about an ethnographic study, an interview-based study, or a community they don't personally know may produce text that sounds knowledgeable but is in fact superficial or fabricated. The patterns the LLM uses are general; they cannot capture the specific texture of the specific community studied in the specific work.

The discipline this requires: when working with qualitative sociology, focus the LLM on synthesis and concept-application tasks, not on producing what reads like ethnographic content. Always read the actual ethnography or interview-based study you are discussing before relying on LLM output about it. Recognize that the qualitative dimension is precisely where LLM assistance is most likely to produce hollow-sounding plausibility.

> ### Dig Deeper — Test your LLM on a contested question
> Pick a sociological question with genuine empirical or normative disagreement (the family-structure/child-outcomes debate; the magnitude of contemporary structural racism; the empirical effects of social media; the contemporary debates about gender categorization). Ask Claude (or your preferred LLM): "What does the sociological literature say about [question]?" Then ask follow-ups: "Where do scholars disagree, and what are the strongest arguments on each side?" *and* "From which theoretical tradition is your analysis coming, and how would scholars from other traditions push back?" Compare the two responses. Did the more pointed questions produce substantially better output? What did the first response leave out?

### Common misconceptions

**"Just use the most recent LLM and these problems go away."** They are reduced; they are not eliminated. Even the best current systems hallucinate, smooth over disagreements, and carry framings. The discipline of verification and adversarial prompting is not a temporary workaround; it is a permanent feature of using these tools well in sociological work.

**"If multiple LLMs agree, the claim is probably true."** Not necessarily. Multiple LLMs trained on similar corpora may share the same biases, the same omissions, the same fabrication patterns, the same dominant framings. Agreement is suggestive but not definitive. Primary-source verification still wins.

**"The LLM cannot be biased — it has no opinions."** It does not have opinions in the human sense, but it has training data, and the training data has structure. The output reflects that structure. "Not having opinions" does not make the output neutral, especially on questions where the discipline itself is contested.

---

## Concept 3 — How to prompt productively

Productive prompting is a skill. Most students develop it informally over months of use. The deliberate version compresses that timeline and produces consistently better output.

A few moves matter most for sociological work.

**Specify the question.** "Tell me about racial inequality" is a weak prompt. "Walk me through the empirical evidence on the Black-white wealth gap in the United States since 2000, identifying the major proposed mechanisms and where the empirical literature is most contested" is a strong prompt. The specificity forces the LLM into useful territory rather than generic territory.

**Name the format you want.** "In two paragraphs," "as a numbered list of the major theoretical positions," "with three concrete examples from named scholars," "in the form of a literature-review section." Naming the format produces output you can use rather than output you have to substantially rework.

**Ask for sources, then verify them.** "Cite three peer-reviewed sociology articles or books that establish this claim." Then look them up. Don't paste the citations into your work without verification. The LLM is better at suggesting where to look than at being the authoritative reference itself.

**Ask for opposing views and contested framings explicitly.** "What is the strongest counter-argument to this position?" "Which scholars push back, and on what grounds?" "From which theoretical tradition is your analysis coming?" This is the highest-yield prompt move for sociological work, because it forces the LLM to surface disagreement and framing rather than producing smoothed orthodoxy.

**Use the LLM iteratively.** Don't expect the first response to be the final answer. Ask follow-up questions. Push back when something seems wrong. Ask for examples, then ask for the strongest counter-examples. Use the conversation to narrow toward what you actually want.

**Give the LLM context.** "I am a third-year sociology undergraduate working on a paper about ___. I have read these specific texts. I am trying to develop an argument that ___. Help me think through ___." Specific context produces specific responses.

**Tell the LLM what you've already considered.** "I have already engaged with the standard structural-racism explanation. I am specifically interested in how cultural-conservative and integrative frameworks would handle this case." This stops the LLM from producing the standard answer you already know and pushes it toward additional substance.

**Distinguish "summarize this" from "what do you think about this."** Summary tasks are where LLMs are strongest; verification of factual content is most important there. Opinion-seeking tasks invite the LLM to produce text that has the form of judgment without the substance of expertise. For sociological work, lean heavily on synthesis tasks and verify their factual content; treat opinion-seeking output skeptically.

**Force the qualitative dimension into appropriate territory.** When working with ethnographic, interview-based, or community-specific sociology, use the LLM for what it can do (concept application; comparing frameworks; identifying connections across studies) rather than what it cannot (simulating immersed knowledge of specific communities).

> ### Dig Deeper — Test your prompting
> Pick a sociological question you genuinely want to learn about. Write your first prompt — what comes naturally. Then write a deliberate version using at least four of the moves above. Submit both to Claude. Compare the responses. The exercise reveals how much prompting structure shapes output quality.

### Multi-LLM comparison

A specific use case for the rest of the book: comparing responses across different LLMs.

The major LLMs you will likely have access to: **Claude** (made by Anthropic), **ChatGPT** (OpenAI), **Gemini** (Google). Other systems exist; the three above are the most widely used for academic work as of this writing.

The systems are similar enough that, on most questions, their responses converge. They differ in characteristic ways: Claude tends toward more cautious framings and more explicit acknowledgment of uncertainty; ChatGPT tends toward more confident framings; Gemini's behavior varies more depending on the version. These are tendencies, not universal patterns. They can shift as the systems are updated.

The productive use of multi-LLM comparison is *not* mechanical (running every prompt through all three and averaging the responses). The productive use is targeted: when an LLM gives you a response that seems suspiciously confident, or that seems to reproduce a particular framing without acknowledging contestation, ask another LLM the same question. Where they agree, the claim is more likely to be supported (though this is not certainty). Where they disagree, you have identified a question worth investigating directly.

This is a particular form of the more general advice: use disagreement as a signal. When two reasonable analyses produce different conclusions, the difference itself is informative — it tells you where the genuine question is. The LLMs are not infallible analysts, but their disagreements often point at real disputes worth thinking about.

For sociological work specifically, multi-LLM comparison is particularly useful for questions where you suspect a dominant framing may be operating. Asked the same question, different LLMs may produce subtly different framings; the variation reveals what is contested.

### Common misconceptions

**"Better prompting eliminates all the failure modes."** It reduces them substantially. It does not eliminate them. Verification of primary sources is still required.

**"Run everything through all three LLMs to be safe."** This is wasteful and produces a false sense of rigor. Targeted multi-LLM use on specific suspicious responses is valuable; mechanical use across the board is busy-work.

**"The LLM gets better the longer the prompt."** Up to a point. Very long prompts can produce diffuse responses that try to address everything at once. Better to ask one focused question, get a focused response, and follow up.

---

## Synthesis — the rules of engagement for the rest of this book

This book uses LLMs as a structured part of its pedagogy. Most chapters contain Dig Deeper prompts (inline suggestions to use an LLM to extend a specific point) and end with an LLM Exercise (a more substantial assignment using an LLM as part of the analytical work). The running project — proposed at the end of this chapter or after — extends this across the term.

The rules of engagement, distilled:

1. **Treat LLM output as a draft, not an authority.** Useful for synthesis, not citable as a source. You may build on it; you may not rely on it without verification.

2. **Verify every factual claim that matters.** Citations, statistics, quotes, dates, attributions, study findings. If you cannot find it in a primary source, do not include it in your work.

3. **Surface disagreement and framing actively.** Ask the LLM where scholars disagree, what the counter-arguments are, what tradition the analysis is coming from. Treat smoothed consensus as suspicious.

4. **Verify against primary sources, not just other LLMs.** Multiple LLMs may share biases. Primary sources — the actual ethnography, the actual paper, the actual data report — are the verification level that matters.

5. **Recognize the qualitative gap.** When working with ethnographic, interview-based, or community-specific sociology, use the LLM for synthesis and concept-application; recognize that LLM output cannot substitute for actual knowledge of the community studied.

6. **Document your LLM use in your work.** When you use an LLM as part of a process — to draft, to synthesize, to compare frameworks — say so in your work. Many institutions now require this; it is good practice regardless. The LLM is a tool you used, like a library database or a statistical package; transparency about tools is part of academic work.

7. **Take responsibility for the output.** The LLM did not write your paper. You did, using the LLM as one tool among others. The conclusions are yours. The errors are yours. The judgment is yours. The LLM's role is to help, not to be blamed when something goes wrong.

8. **Notice your own thinking.** The most insidious use of LLMs is when they substitute for your thinking rather than supporting it. When you find yourself accepting LLM output without engagement, slow down. When you find yourself unable to explain in your own words what you are claiming, you have not yet thought it. The LLM is a partner; the thinking is still yours.

This is not, fundamentally, a different posture from how a thoughtful student should approach any source — books, papers, lectures, classmates' arguments. Critical engagement with sources is the core of academic work. LLMs are unusual sources because they generate fluent and confident-sounding text on demand, and that fluency invites a posture of acceptance that is not warranted. Resisting that posture is the discipline this chapter is asking you to internalize before any of the chapters that follow.

---

## Exercises

### Warm-up

1. Explain in your own words, in two paragraphs, what an LLM is doing when it generates text.
2. List the four failure modes specific to sociological work and give one concrete example of each you can imagine encountering.
3. State five prompting moves that produce better output. For each, give an example of a weak prompt and the corresponding stronger version.

### Application

4. Pick a sociological topic from any chapter in this book. Generate a first prompt, then a deliberate prompt using at least four of the moves from Concept 3. Submit both to Claude (or your preferred LLM). Hand in: the two prompts, the two responses, and a paragraph comparing them.
5. Pick a fabricated-citation example from your own LLM use (or generate one fresh by asking an LLM for sources on an obscure sociological question). For each citation in the response, verify whether it actually exists. Hand in: the prompt, the response, and your verification results.
6. Pick a contested empirical question in sociology (the family-structure debate; the magnitude of various inequality gaps; the empirical effects of specific reforms). Submit it to two different LLMs. Compare the responses. Where do they agree? Where do they disagree? What does the disagreement tell you about where to dig deeper?

### Synthesis

7. Argue for and against the following claim: "LLMs should be banned from undergraduate sociology work because they undermine the development of analytical skills and produce fabricated citations." Take both sides seriously. Land on a specific recommendation about how undergraduate sociology work should incorporate LLMs.
8. Pick a piece of sociological writing (an op-ed; a magazine article; a blog post; a popular-press book chapter). Read it carefully. Then ask an LLM to summarize the same topic. Compare. What did the LLM capture? What did it miss? What does the comparison tell you about LLM strengths and weaknesses for sociological analysis?

### Challenge

9. Develop a personal "prompting workflow" for sociological work — a documented sequence of moves you will use across the rest of the book's chapters. Include: how you will phrase initial questions, how you will request sources, how you will surface disagreements and framings, how you will handle qualitative-sociology questions, how you will verify, and how you will document LLM use in your work. Hand in: the workflow document, with one worked example showing each step.
10. The "AI in education" debate is itself a sociological question with ongoing disagreement about effects on learning, equity, and academic integrity. Use the methods in this chapter (specific prompting; asking for opposing views; multi-LLM comparison; primary-source verification) to investigate one specific question — say, "what does the empirical research show about LLM use and undergraduate writing skills?" Produce a short analytical memo (~1,500 words) summarizing what you found, what you verified, where the genuine disagreement is, and where you land.

### LLM exercise — Build your verification habit

This exercise is the foundational one for the rest of the course. The habit it builds will save you from most of the failure modes that destroy LLM-augmented work.

Pick any chapter from this book that interests you (Chapter 1's introduction is a good choice; Chapter 11 on Race and Ethnicity, Chapter 12 on Gender, or Chapter 18 on Work are all good stress tests). Ask Claude:

> "I am studying [chapter topic] for an introductory sociology course. Walk me through:
> 1. The major scholarly positions on this topic.
> 2. The key empirical findings that have shaped the current debate.
> 3. The specific scholars and works most associated with each position.
> 4. The current points of genuine disagreement in the literature.
> 5. The strongest argument against the position you just laid out as 'mainstream.'
> 6. From which theoretical tradition is your analysis primarily coming?"

Then verify, item by item:

- For each scholar named, search for their actual academic work. Are they real? Is the work real? Is it about what the LLM said it was about?
- For each empirical finding, find the actual paper or report. Does it say what the LLM claimed?
- For each disagreement named, find a recent review article or handbook chapter that maps the disagreement. Does the LLM's framing of the disagreement track what the field thinks?
- For the framing question: was the LLM honest about the tradition it was operating in?

Hand in: your prompt sequence, the LLM's response, your verification results (specific citations that checked out, specific claims that did not), and a paragraph identifying which parts of the LLM's response you found most reliable and least reliable.

**Project prompt — Social-Problem Tracker (Chapter 00 task):** The running project for this book is a 25-page sociological analysis of a contested social problem, accumulated across the term. The demonstration problem is **homelessness in the United States**; you may substitute another contested social problem (the opioid epidemic, gentrification of a specific neighborhood, food insecurity, mental-health crisis among adolescents, an environmental-justice case, the loneliness epidemic, etc.). See `_project-guide.md` for the full description.

Your Chapter 00 contribution: scope your slice. Ask Claude to walk you through the major sub-areas of your chosen problem, the data sources you'll need, and where empirical disagreement lives vs. where the disagreement is mostly normative. Pick one specific slice, write a two-sentence project statement, and start your project notebook. The disciplines from this chapter — verification, surfacing disagreement and framing, transparency, ownership, recognition of the qualitative gap — apply to every subsequent chapter's project work.

---

## Chapter summary

LLMs like Claude, ChatGPT, and Gemini are powerful tools for sociological work — synthesizing literature, drafting analysis, comparing frameworks. They are also particularly dangerous in sociological applications: they fabricate sources, smooth over genuine empirical disagreements, carry hidden normative framings that the discipline's value-laden vocabulary makes especially treacherous, and cannot substitute for the immersed knowledge that qualitative sociology depends on. Productive use requires understanding the tools and developing specific disciplines: deliberate prompting; primary-source verification; active surfacing of disagreement and framing; recognition of the qualitative gap; transparency about use; and ultimate responsibility for conclusions. The rest of this book uses LLMs as a structured part of its pedagogy; the rules of engagement laid out here apply to all of that work.

## What would change my mind

If sustained empirical evidence showed that LLM output had become reliably accurate on factual claims and reliably balanced across competing framings — with hallucination rates near zero and substantive presentation of contested positions — I would relax the verification discipline this chapter recommends. The current evidence does not support that. Even the strongest current systems hallucinate at non-trivial rates on detailed factual content and reproduce dominant framings without reliable acknowledgment.

## Still puzzling

I do not have a confident view on how LLM use will reshape undergraduate sociology education over the next five years. Possible trajectories range from successful integration (the tools are used productively, with appropriate discipline, and student capabilities are enhanced) to substantive degradation (students rely on tools to substitute for thinking, analytical capabilities decline, the qualitative-imagination dimension of sociology weakens). The answer depends on choices made by institutions, professors, and students that have not yet been fully made. The students of this course are part of that determination.

## Connections forward

Chapter 1 — An Introduction to Sociology — opens the substantive work of the book. From this point on, the rules of engagement laid out here apply: every Dig Deeper, every LLM Exercise, every assignment that uses these tools assumes the disciplines this chapter has established. If you find yourself slipping — pasting unverified citations, accepting LLM output without engagement, treating fluent text as authoritative — return here and recalibrate.

---

**Tags:** Claude, ChatGPT, Gemini, LLMs, large-language-models, prompting, fabrication, hallucination, multi-LLM-comparison, verification, primary-sources, academic-integrity, AI-in-education, sociology-pedagogy, methods, qualitative-research, normative-framings
---

## LLM Exercise — Chapter 00: Claude Basics (Social-Problem Tracker Project)

**Project:** Social-Problem Tracker — across the semester, track one specific social problem through every chapter, building toward a 25-page sociological analysis with policy implications.
**What you're building this chapter:** the project's foundation — the Claude Project, the verification discipline, the analytical framework, and the deliverable target.
**Tool:** **Claude Project** "Sociology Tracker — [Your Problem]" — every later chapter adds a section.

---

**The Prompt:**

```
I'm starting a semester-long Social-Problem Tracker project. I'll
pick a specific social problem in Chapter 1 and track it across all
22 chapters of an Intro Sociology course. Final deliverable: 25-page
analysis with policy implications.

Help me set this up. Ask me ONE question at a time, waiting for my
answer.

1. Tool choice. The project will live as a Claude Project (one
   I'll come back to over months, with persistent context). Confirm
   the format:
   - Single growing markdown document (recommended).
   - Folder of section files (more flexible for late-stage
     restructuring).
   - Mix (one document, with images/data in companion files).

2. Verification discipline. The book argues for primary-source
   verification, surfacing genuine disagreement, recognition of
   the qualitative gap, transparency about LLM use. State a
   verification commitment in your own words — what you will do
   when Claude makes a factual claim or cites a study. (Standard:
   verify against named primary sources; mark unverified claims
   as [verify]; refuse to assert quantitative claims without a
   source.)

3. The analytical frame. Sociology has competing theoretical
   traditions:
   - Structural functionalism (Durkheim, Parsons): what role does
     the problem play in the system? what dysfunctions reveal?
   - Conflict theory (Marx, Mills): who benefits from the problem
     existing in its current form? what power structures
     produce it?
   - Symbolic interactionism (Mead, Goffman): how do people
     interpret and respond to the problem in everyday life?
   - Feminist / intersectional theory (Crenshaw, Collins): how do
     gender, race, class compound the problem?
   The 25-page final analysis should pull from all four when
   relevant, not just one. State your starting bias (most
   students arrive with one tradition more accessible) and your
   commitment to engaging the others.

4. The deliverable shape. The 25-page final will have:
   - Executive summary (1-2 pages).
   - The problem defined (1 page).
   - 22 chapter-derived sections (1 page each average; some longer,
     some shorter).
   - Policy implications (2-3 pages).
   - References (a real list of primary sources you actually
     consulted).
   Confirm or adjust the structure.

After all four answers, write a 600-800 word **Project Charter**:
- The project name and target deliverable.
- The verification discipline (your commitment).
- The theoretical-frame commitment (you'll engage all four
  traditions).
- The structure of the final 25-page document.
- The "Honest LLM Use" section — what role Claude plays, what
  role only you can play (direct observation, defensible argument,
  the qualitative judgment that distinguishes sociology from
  data summarization).

Save the Charter as the first section of your project document.
Every later chapter's prompt assumes this Charter is in place.
```

---

**What this produces:** A 600-800 word Project Charter — the project's foundation document. The "Honest LLM Use" section is the discipline-enforcing piece.

**How to adapt this prompt:**

- *For your own project:* The verification discipline is the project's most consequential commitment. Don't make it weaker than you'll actually honor.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the right tool here.
- *For a Claude Project:* Essential. The Charter goes in the Project's project-level instructions.

**Connection to previous chapters:** This is the project's opening.

**Preview of next chapter:** Chapter 1 introduces the sociological imagination (Mills's personal trouble vs. public issue translation). You'll pick your specific social problem here and write the foundational framing applying Mills.


---

##  AI Wayback Machine
**Harriet Martineau** was wrote How to Observe Morals and Manners in 1838 — the first methodological treatise of sociology, decades before the term was widely adopted.

![Harriet Martineau](../images/harriet-martineau-4y6.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Harriet Martineau, and how does their work connect to sociology with tools we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Harriet Martineau"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Harriet Martineau's framework to a contemporary sociological question.
- Add a constraint: "Answer including criticisms or limits of Harriet Martineau's framework."

What changes? What gets better? What gets worse?
