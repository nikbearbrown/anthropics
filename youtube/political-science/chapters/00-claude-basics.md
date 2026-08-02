# Chapter 00 — Claude Basics: Using LLMs in Political Science

**Suggested titles:**
1. Claude Basics: Using LLMs in Political Science
2. The Tool, the Pitfalls, and the Method
3. How to Think With (Not For) an LLM About Politics

**TL;DR.** Large language models like Claude, ChatGPT, and Gemini are extraordinarily useful tools for the work of political science — synthesizing literature, drafting analysis, comparing perspectives, summarizing primary sources. They are also dangerous if used uncritically — they fabricate citations, smooth over genuine empirical disagreements, and carry implicit framings that can substitute for thinking. This chapter establishes the rules of engagement for the rest of the book: how to use LLMs well, how to recognize where they fail, and how to use the failures themselves as a learning tool.

---

There is a real chance that a student in this class will, at some point, hand in a paper containing a citation to *Wilson, J. (1993). Reconstructing the Liberal Order: Multilateral Institutions in a Post-Hegemonic World. Cambridge University Press* — a book that does not exist. The DOI will look right. The publisher is plausible. The title fits the topic. The author has a name that sounds like a political scientist's name. The student will not have invented the citation. An LLM will have invented it, and the student will have copied it without checking, because LLM output looks authoritative and because the citation falls in the middle of an otherwise reasonable paragraph.

This is not hypothetical. It happens routinely now. It is the most common failure mode in undergraduate work that uses LLMs and has been since 2023. It is preventable. It requires a small amount of discipline and a clear understanding of what these tools are doing.

This chapter is about how to use LLMs in political science work without being misled by them. It is the first chapter in the book because the rest of the book asks you to use these tools — for Dig Deepers inside chapters, for end-of-chapter LLM Exercises, for a running project that will accumulate across the term. Before any of that work begins, you need to understand the tools, the rules of engagement, and the specific risks that political science work introduces beyond what other fields face.

If you have used Claude, ChatGPT, or Gemini casually before, parts of this chapter will be review. The political-science-specific sections will not be. Read them carefully.

## Learning objectives

By the end of this chapter you should be able to:

1. Explain in plain language what an LLM does and does not do.
2. Identify three failure modes — fabrication, false confidence, hidden framing — and recognize them in LLM output.
3. Distinguish the major LLMs (Claude, ChatGPT, Gemini) at a useful level — what each is good at, where each tends to differ.
4. Write a productive prompt for political analysis, including the moves that make LLM output more useful (specify the question, name the format, ask for sources, request opposing views).
5. Verify claims an LLM makes against primary sources — and do this routinely, not just when something seems suspicious.
6. Apply the multi-LLM comparison strategy productively rather than mechanically — using disagreement among LLMs as a signal for where to dig deeper.
7. Hold the appropriate skeptical-collaborative posture toward these tools: they are not authoritative sources; they are useful drafting and synthesis partners; the responsibility for the work remains yours.

---

## Concept 1 — What an LLM actually does

You should know, at some level of detail, what is happening when Claude responds to a prompt. Most students never learn this and end up with mistaken intuitions that produce predictable errors.

A large language model is a statistical system trained on enormous quantities of text — books, papers, websites, news articles, code, conversations. The training process produces a system that, given a sequence of words (the prompt), predicts the next word in a way that reflects the patterns of the training data. The system then takes the prompt plus its predicted next word, predicts the next-next word, and so on, generating text token by token.

What the system has learned, in this process, is a great deal of linguistic, factual, and analytical structure. It has read enough political science to know what a good political-science argument looks like, what kinds of evidence get cited in which subfields, how comparative-politics analysis differs from international-relations analysis, what frameworks are standard, what disagreements exist. It is, in many ways, a remarkably knowledgeable interlocutor about political science.

What the system has *not* done is verify any of it. It has read sources that contradict each other and has no built-in mechanism for adjudicating among them. It has read sources of varying reliability and has only an indirect sense of which sources are more trustworthy. It cannot, in most current configurations, look up a fact in real time — it produces output based on what its training process produced as a likely continuation of the prompt. Whether the continuation is true is a separate question.

This has several consequences worth internalizing.

**LLMs hallucinate.** The system can produce confident-sounding text containing claims that are simply false — a citation to a book that does not exist, a statistic that was never reported, a quote that was never said. The technical name in the field is *hallucination*, though "fabrication" is closer to what is happening. The hallucination rate has been falling as the systems improve, but it has not gone to zero, and it is concentrated in exactly the kind of detailed factual claims (dates, numbers, citations, quotes) that academic work depends on.

**LLMs reflect the patterns of their training data.** If the training data over-represents one perspective on a contested question, the LLM's responses will tend to reflect that over-representation. This is not a deliberate bias in any sinister sense; it is a structural feature of statistical learning from a corpus. The corpus matters.

**LLMs can be remarkably useful at synthesis.** Asked to summarize the major positions in a political science debate, an LLM will often produce a quite good summary — capturing the central claims, the major scholars, the empirical disputes, the normative tensions. The synthesis function is one of their strongest uses. Verification of specific claims still has to happen separately.

**LLMs are not search engines.** A search engine retrieves existing documents. An LLM generates new text based on patterns learned from documents. The document the LLM appears to be quoting may not exist. The LLM's response is not itself a document you should cite; it is a generated response that may be useful for thinking but should not be treated as authoritative.

### Common misconceptions

**"The LLM is connecting to a database of facts."** Most LLM systems, in their default configuration, are not. They are generating text based on patterns. Some systems have been augmented with retrieval (asking the model to look up information from a separate corpus before responding), and the answers improve when this is done. But the default behavior of most popular LLMs is generation, not retrieval.

**"If the LLM is confident, it is probably right."** Confidence in LLM output is not calibrated to truth. The model produces fluent text whether the underlying claim is well-supported or fabricated. Tone is not evidence.

**"LLMs are replacing political analysts."** They are augmenting them, sometimes substantially. The work that LLMs are good at — synthesis, drafting, comparing perspectives, generating questions — is real work. The work they cannot do — verifying primary sources, conducting original interviews, exercising judgment about contested empirical questions, taking responsibility for conclusions — is also real work. The replacement framing oversimplifies; the augmentation framing fits the evidence better.

---

## Concept 2 — Three failure modes specific to political science work

Every academic field has to handle LLM failure modes. Political science has some that are sharper or more frequent than in other fields. Three are worth flagging.

### Fabrication of sources

This is the failure mode that has destroyed undergraduate work most reliably since 2023. Asked for citations on a political science topic, an LLM will often produce a list of plausible-sounding citations — a few that are real, a few that are partially correct (real author, wrong title; correct title, wrong author; correct article in wrong journal), and a few that are entirely fabricated. The fabricated ones look indistinguishable from the real ones. They have plausible authors, plausible titles, plausible publication years, plausible journal names.

The student who pastes a fabricated citation into a paper and submits it is not committing dishonesty in the sense of lying — they did not invent the citation. They are committing a different and equally serious error: failing to verify a claim before relying on it. In many institutions this is treated as plagiarism or as fabrication regardless of intent.

The discipline this requires: never use a citation in your own work that you have not personally located in the actual source. If an LLM gives you a citation, you must find the actual paper, journal, or book before using it. Use Google Scholar, your library catalog, the journal's website, or the author's faculty page. If you cannot find the source, do not cite it.

### Smoothing over genuine empirical disagreements

Political science contains genuine empirical disagreements — questions where serious scholars examining the same evidence reach different conclusions. The democratic peace claim, the effect of gerrymandering on polarization, the causes of authoritarian persistence, the empirical assessment of austerity policies, the magnitude of the China shock. These are not "anyone's guess" — careful empirical work narrows what positions are reasonable. But they are not settled either.

LLMs sometimes smooth these disagreements into apparent consensus. Asked "what does the literature say about X," an LLM may respond with a single coherent narrative that flattens out the genuine debate. The student who relies on this gets a misleading picture — both of what political science thinks and of how political science actually works.

The discipline this requires: ask the LLM specifically about disagreements. "Where do scholars disagree on this question?" "What is the strongest counter-argument to the position you just stated?" "What scholars or schools push back against this view?" This kind of prompting often produces dramatically better output, because it forces the LLM to surface the disagreement structure rather than producing a smoothed synthesis.

### Hidden normative framings

This is the most subtle of the three. Political science is not value-free. Many of its central concepts — democracy, justice, freedom, legitimacy, fairness — carry normative weight. Different theoretical traditions (liberal, realist, Marxist, conservative, feminist, post-colonial) carry different framings of what is worth studying, what counts as success, what counts as failure.

LLMs trained on a corpus that over-represents certain framings will reproduce those framings, often without flagging them. The "conventional wisdom" of one tradition will appear as just "the way things are." A student using an LLM uncritically may absorb framings without recognizing they are framings.

This is especially treacherous on contested current-events questions where the line between empirical and normative is itself contested. An LLM's response on a question about, say, U.S. foreign policy in the Middle East, or the politics of immigration, or the evaluation of a specific authoritarian regime, is not neutral — and is sometimes presented as if it were.

The discipline this requires: ask the LLM what tradition or perspective is implicit in its response. "From which theoretical tradition is this analysis coming?" "How would a realist (or liberal, or constructivist, or critical) scholar respond differently?" "What assumptions am I being asked to share, and are they contested?" Forcing the framing into the open is a teaching move that good political-science professors have always made; doing it with LLM output makes the LLM more useful and you a sharper analyst.

> ### Dig Deeper — Test your LLM on a contested question
> Pick a political-science question with genuine empirical or normative disagreement (the effect of voter ID laws on turnout; the causes of populism's recent rise; the assessment of a specific U.S. military intervention). Ask Claude (or your preferred LLM): "What does the political-science literature say about [question]?" Then ask a follow-up: "Where do scholars disagree on this question, and what are the strongest arguments on each side?" Compare the two responses. Did the second prompt produce substantially more useful output? What did the first response leave out?

### Common misconceptions

**"Just use the most recent LLM and these problems go away."** They are reduced; they are not eliminated. Even the best current systems hallucinate, smooth over disagreements, and carry framings. The discipline of verification and adversarial prompting is not a temporary workaround; it is a permanent feature of using these tools well.

**"If multiple LLMs agree, the claim is probably true."** Not necessarily. Multiple LLMs trained on similar corpora may share the same biases, the same omissions, the same fabrication patterns. Agreement is suggestive but not definitive. Primary-source verification still wins.

**"The LLM cannot be biased — it has no opinions."** It does not have opinions in the human sense, but it has training data, and the training data has structure. The output reflects that structure. "Not having opinions" does not make the output neutral.

---

## Concept 3 — How to prompt productively

Productive prompting is a skill. Most students develop it informally over months of use. The deliberate version compresses that timeline and produces consistently better output.

A few moves matter most.

**Specify the question.** "Tell me about gerrymandering" is a weak prompt. "Explain the empirical evidence on whether partisan gerrymandering meaningfully affects polarization in U.S. House elections, focusing on work from the past decade" is a strong prompt. The specificity forces the LLM into useful territory rather than generic territory.

**Name the format you want.** "In two paragraphs," "as a numbered list of the major positions," "with three concrete examples," "in the form of a memo for a policy-maker." Naming the format produces output you can use rather than output you have to substantially rework.

**Ask for sources, then verify them.** "Cite three peer-reviewed political science papers on this question." Then look them up. Don't paste the citations into your work without verification. The LLM is better at suggesting where to look than at being the authoritative reference itself.

**Ask for opposing views explicitly.** "What is the strongest counter-argument to this position?" "Which scholars push back, and on what grounds?" This is the single highest-yield prompt move for political-science work, because it forces the LLM to surface disagreement rather than producing smoothed consensus.

**Use the LLM iteratively.** Don't expect the first response to be the final answer. Ask follow-up questions. Push back when something seems wrong. Ask for examples, then ask for the strongest counter-examples. Use the conversation to narrow toward what you actually want.

**Give the LLM context.** "I am a third-year political science undergraduate working on a paper about ___. I have read these specific texts. I am trying to develop an argument that ___. Help me think through ___." Specific context produces specific responses.

**Tell the LLM what you've already considered.** "I have already considered the standard liberal-IR explanation. I am specifically interested in alternatives." This stops the LLM from producing the standard answer you already know and pushes it toward additional substance.

**Distinguish "summarize this" from "what do you think about this."** Summary tasks are where LLMs are strong and verification is most important; opinion-seeking tasks invite the LLM to produce text that has the form of judgment without the substance of expertise. For political science work, lean heavily on synthesis tasks and verify their factual content; treat opinion-seeking output skeptically.

> ### Dig Deeper — Test your prompting
> Pick a political-science question you genuinely want to learn about. Write your first prompt — what comes naturally. Then write a deliberate version using at least three of the moves above. Submit both to Claude. Compare the responses. The exercise reveals how much prompting structure shapes output quality.

### Multi-LLM comparison

A specific use case for the rest of the book: comparing responses across different LLMs.

The major LLMs you will likely have access to: **Claude** (made by Anthropic), **ChatGPT** (OpenAI), and **Gemini** (Google). Other systems (Mistral, Llama, others) exist; the three above are the most widely used for academic work as of this writing.

The systems are similar enough that, on most questions, their responses converge. They differ in characteristic ways: Claude tends toward more cautious framings and more explicit acknowledgment of uncertainty; ChatGPT tends toward more confident framings; Gemini's behavior varies more depending on the version. These are tendencies, not universal patterns.

The productive use of multi-LLM comparison is *not* to mechanically run every prompt through all three and average the responses. The productive use is targeted: when an LLM gives you a response that seems suspiciously confident, ask another LLM the same question. Where they agree, the claim is more likely to be supported (though this is not certainty). Where they disagree, you have identified a question worth investigating directly.

This is a particular form of the more general advice: use disagreement as a signal. When two reasonable analyses produce different conclusions, the difference itself is informative — it tells you where the genuine question is. The LLMs are not infallible analysts, but their disagreements often point at real disputes worth thinking about.

### Common misconceptions

**"Better prompting eliminates all the failure modes."** It reduces them substantially. It does not eliminate them. Verification of primary sources is still required.

**"Run everything through all three LLMs to be safe."** This is wasteful and produces a false sense of rigor. Targeted multi-LLM use on specific suspicious responses is valuable; mechanical use across the board is busy-work.

**"The LLM gets better the longer the prompt."** Up to a point. Very long prompts can produce diffuse responses that try to address everything at once. Better to ask one focused question, get a focused response, and follow up with another focused question.

---

## Synthesis — the rules of engagement for the rest of this book

This book uses LLMs as a structured part of its pedagogy. Most chapters contain Dig Deeper prompts (inline suggestions to use an LLM to extend a specific point) and end with an LLM Exercise (a more substantial assignment using an LLM as part of the analytical work). The running project — proposed at the end of this chapter or after — extends this across the term.

The rules of engagement, distilled:

1. **Treat LLM output as a draft, not an authority.** Useful for synthesis, not citable as a source. You may build on it; you may not rely on it without verification.

2. **Verify every factual claim that matters.** Citations, statistics, quotes, dates, attributions. If you cannot find it in a primary source, do not include it in your work.

3. **Surface disagreement actively.** Ask the LLM where scholars disagree, what the counter-arguments are, what tradition the analysis is coming from. Treat smoothed consensus as suspicious.

4. **Verify against primary sources, not just other LLMs.** Multiple LLMs may share biases. Primary sources — the actual paper, the actual treaty text, the actual government document — are the verification level that matters.

5. **Document your LLM use in your work.** When you use an LLM as part of a process — to draft, to synthesize, to compare perspectives — say so in your work. Many institutions now require this; it is good practice regardless. The LLM is a tool you used, like a library database or a statistical package; transparency about tools is part of academic work.

6. **Take responsibility for the output.** The LLM did not write your paper. You did, using the LLM as one tool among others. The conclusions are yours. The errors are yours. The judgment is yours. The LLM's role is to help, not to be blamed when something goes wrong.

7. **Notice your own thinking.** The most insidious use of LLMs is when they substitute for your thinking rather than supporting it. When you find yourself accepting LLM output without engagement, slow down. When you find yourself unable to explain in your own words what you are claiming, you have not yet thought it. The LLM is a partner; the thinking is still yours.

This is not, fundamentally, a different posture from how a thoughtful student should approach any source — books, papers, lectures, classmates' arguments. Critical engagement with sources is the core of academic work. LLMs are unusual sources because they generate fluent and confident-sounding text on demand, and that fluency invites a posture of acceptance that is not warranted. Resisting that posture is the discipline this chapter is asking you to internalize before any of the chapters that follow.

---

## Exercises

### Warm-up

1. Explain in your own words, in two paragraphs, what an LLM is doing when it generates text.
2. List the three failure modes specific to political science work and give one concrete example of each you can imagine encountering.
3. State four prompting moves that produce better output. For each, give an example of a weak prompt and the corresponding stronger version.

### Application

4. Pick a political-science topic from any chapter in this book. Generate a first prompt, then a deliberate prompt using at least three of the moves from Concept 3. Submit both to Claude (or your preferred LLM). Hand in: the two prompts, the two responses, and a paragraph comparing them.
5. Pick a fabricated-citation example from your own LLM use (or generate one fresh by asking an LLM for sources on an obscure political-science question). For each citation in the response, verify whether it actually exists. Hand in: the prompt, the response, and your verification results.
6. Pick a contested empirical question in political science (e.g., the China shock's political effects; the effect of voter ID on turnout; the causes of authoritarian persistence). Submit it to two different LLMs. Compare the responses. Where do they agree? Where do they disagree? What does the disagreement tell you about where to dig deeper?

### Synthesis

7. Argue for and against the following claim: "LLMs should be banned from undergraduate political-science work because they undermine the development of analytical skills." Take both sides seriously. Land on a specific recommendation about how undergraduate work should incorporate LLMs.
8. Pick a piece of political analysis (an op-ed, a blog post, a think-tank report, an article in a magazine like *Foreign Affairs* or *The Atlantic*). Read it carefully. Then ask an LLM to summarize the same topic. Compare. What did the LLM capture? What did it miss? What does the comparison tell you about LLM strengths and weaknesses for political analysis?

### Challenge

9. Develop a personal "prompting workflow" for political-science work — a documented sequence of moves you will use across the rest of the book's chapters. Include: how you will phrase initial questions, how you will request sources, how you will surface disagreements, how you will verify, and how you will document LLM use in your work. Hand in: the workflow document, with one worked example showing each step.
10. The "AI safety" / "AI risks" debate is itself a political question with ongoing scholarly and policy disagreement. Use the methods in this chapter (specific prompting, asking for opposing views, multi-LLM comparison, primary-source verification) to investigate one specific question — say, "is current LLM technology a risk to democratic deliberation?" Produce a short analytical memo (1,500 words) summarizing what you found, what you verified, where the genuine disagreement is, and where you land.

### LLM exercise — Build your verification habit

This exercise is the foundational one for the rest of the course. The habit it builds will save you from most of the failure modes that destroy LLM-augmented work.

Pick any chapter from this book that interests you (Chapter 5 on ideology is a good choice; Chapter 18 on regimes is another). Ask Claude:

> "I am studying [chapter topic] for an introductory political science course. Walk me through:
> 1. The major scholarly positions on this topic.
> 2. The key empirical findings that have shaped the current debate.
> 3. The specific scholars and works most associated with each position.
> 4. The current points of genuine disagreement in the literature.
> 5. The strongest argument against the position you just laid out as 'mainstream.'"

Then verify, item by item:

- For each scholar named, search for their actual academic work. Are they real? Is the work real? Is it about what the LLM said it was about?
- For each empirical finding, find the actual paper or report. Does it say what the LLM claimed?
- For each disagreement named, find a recent review article or handbook chapter that maps the disagreement. Does the LLM's framing of the disagreement track what the field thinks?

Hand in: your prompt sequence, the LLM's response, your verification results (specific citations that checked out, specific claims that did not), and a paragraph identifying which parts of the LLM's response you found most reliable and least reliable.

**Project prompt — Policy Issue Tracker (Chapter 00 task):** The running project for this book is a 25-page policy memo on a contested policy issue, accumulated across the term. The demonstration issue is **U.S. immigration policy**; you may substitute another contested issue (climate, AI governance, healthcare, gun policy, criminal justice, voting rights). See `_project-guide.md` for the full description.

Your Chapter 00 contribution: scope your slice. Ask Claude to walk you through the major sub-areas of your chosen issue, the data sources you'll need, and where empirical disagreement lives vs. where the disagreement is mostly normative. Pick one specific slice, write a two-sentence project statement, and start your project notebook. The disciplines from this chapter — verification, surfacing disagreement, transparency, ownership — apply to every subsequent chapter's project work.

---

## Chapter summary

LLMs like Claude, ChatGPT, and Gemini are powerful tools for political science work. They synthesize, draft, compare, and ideate well. They also fabricate sources, smooth over genuine disagreements, and carry implicit framings. Productive use requires understanding the tools — what they are doing technically — and developing specific disciplines: deliberate prompting, primary-source verification, active surfacing of disagreement, transparency about use, and ultimate responsibility for conclusions. The rest of this book uses LLMs as a structured part of its pedagogy; the rules of engagement laid out here apply to all of that work.

## What would change my mind

If a sustained period of empirical evidence showed that LLM output had become reliably accurate on factual claims, with hallucination rates near zero on specific topical content (citations, statistics, quotes), I would relax the verification discipline this chapter recommends. The current evidence does not support that — even the strongest current systems hallucinate at non-trivial rates on detailed factual content. The discipline of verification is justified by the current state of the technology; if the technology improves substantially, the discipline can adjust.

## Still puzzling

I do not have a confident view on how LLM use will reshape undergraduate education over the next five years. Possible trajectories range from successful integration (the tools are used productively, with appropriate discipline, and student capabilities are enhanced) to substantive degradation (students rely on the tools to substitute for thinking, and analytical capabilities decline). The answer depends on choices made by institutions, professors, and students that have not yet been made — and on technology trajectories that are not predictable. The students of this course are part of that determination.

## Connections forward

Chapter 1 — Introduction to Political Science — opens the substantive work of the book. From this point on, the rules of engagement laid out here apply: every Dig Deeper, every LLM Exercise, every assignment that uses these tools assumes the disciplines this chapter has established. If you find yourself slipping — pasting unverified citations, accepting LLM output without engagement, treating fluent text as authoritative — return here and recalibrate.

---

**Tags:** Claude, ChatGPT, Gemini, LLMs, large-language-models, prompting, fabrication, hallucination, multi-LLM-comparison, verification, primary-sources, academic-integrity, AI-in-education, political-science-pedagogy, methods
---

## LLM Exercise — Chapter 00: Claude Basics (Election Tracker Project)

**Project:** Election Tracker — across the semester, track one real election (recent or upcoming) through every chapter's lens. Final deliverable: 25-page post-election analysis.
**What you're building this chapter:** the project's foundation — pick the election, set up verification discipline, write the project charter.
**Tool:** **Claude Project** "Election Tracker — [Election]" — every later chapter adds a section.

---

**The Prompt:**

```
I'm starting a semester-long Election Tracker project. I'll pick
one specific election in this chapter and track it through all 22
chapters. Final deliverable: 25-page post-election analysis.

Help me set up. Ask me ONE question at a time, waiting for my
answer.

1. Pick the election. Pick ONE — must be recent enough that
   primary sources exist OR upcoming during the course. Options:
   - 2026 U.S. midterm (in progress as you take the course).
   - 2025 German federal election (just happened — full sources
     available).
   - 2024 U.S. presidential (retrospective with hindsight).
   - 2024 Indian general election.
   - 2024 UK general election.
   - 2024 Mexican presidential election.
   - 2025 or 2026 election in another country you care about.
   - State-level or mayoral election (if a major election in your
     city/state — useful when local politics matters most to you).

2. Why this election. One paragraph: what's at stake, why you
   care, what you'll learn from a 22-chapter analysis.

3. The verification discipline. Politics is information-warfare-
   adjacent. Commit to:
   - Verifying every claim against primary sources (electoral
     commissions, FEC, official transcripts, peer-reviewed
     research).
   - Marking unverified claims as [verify] inline.
   - Refusing partisan-motivated framings without acknowledging
     the partisan source.
   - Surfacing genuine disagreement rather than papering over it.

4. The deliverable. The 25-page final post-election analysis will
   include:
   - Executive summary (1-2 pages).
   - Election context (1-2 pages).
   - 22 chapter-derived sections (1 page average).
   - Post-election consequences and implications (3-5 pages).
   - Bibliography of primary sources actually used.
   Confirm the structure or adjust.

5. Primary sources. Identify 3-5 primary-source repositories you'll
   rely on:
   - Electoral commission for the country (FEC, ONS, ECI, etc.).
   - Polling aggregators (FiveThirtyEight, RealClearPolitics,
     Politico, country-specific equivalents).
   - Official campaign materials (manifestos, debate transcripts).
   - V-Dem / Freedom House for regime assessment.
   - Major news outlets across the political spectrum.
   - Peer-reviewed political-science journals.

After all five answers, write a 600-800 word **Election Tracker
Charter**:
- The election and its date.
- The stakes (what's being decided).
- The verification commitment.
- The deliverable structure.
- The named primary sources.
- The "what makes this hard" honest paragraph — name the
  challenges this specific election poses (LLM training-cutoff
  issues; partisan source-bias; rapidly-changing situation; etc.).

Save the Charter as the first section of your analysis document.
```

---

**What this produces:** A 600-800 word Charter — the project's foundation. The verification commitment is the project's most consequential single decision.

**How to adapt this prompt:**

- *For your own project:* Pick an election you have ongoing engagement with (you'll be reading news about it anyway). The 22-chapter engagement is much easier on a real election you care about.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the right tool here.
- *For a Claude Project:* Essential. The Charter goes in the project-level instructions.

**Connection to previous chapters:** This is the project's opening.

**Preview of next chapter:** Chapter 1 introduces political science as a discipline. You'll write the central political question this election is deciding — the one a political scientist would identify as the structural-significance core.


---

##  AI Wayback Machine
**Harold Lasswell** was political scientist who defined politics as "who gets what, when, how" — and pioneered content analysis as a tool for the discipline.

![Harold Lasswell](../images/harold-lasswell-0pz.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Harold Lasswell, and how does their work connect to political science with tools we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Harold Lasswell"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Harold Lasswell's framework to a current political question.
- Add a constraint: "Answer including criticisms or limits of Harold Lasswell's framework."

What changes? What gets better? What gets worse?
