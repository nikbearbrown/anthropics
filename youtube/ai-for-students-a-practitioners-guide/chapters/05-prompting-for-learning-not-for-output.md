# Chapter 5 — Prompting for Learning, Not for Output

*A prompt that produces a good output is not the same as a prompt that produces learning. Here is how to write the second kind.*

> "A prompt that produces a good output is not the same as a prompt that produces learning. Here is how to write the second kind."

---

Two pre-law students — call them Maya and Jordan — are preparing for the same moot court round on the same constitutional law question: whether public university speech codes that prohibit "discriminatory harassment" can survive First Amendment scrutiny. Same readings. Same coach. Same hour of access to ChatGPT the night before the argument.

Jordan types: *"Explain the First Amendment implications of speech codes on college campuses."*

He gets a beautiful four-paragraph answer. Levels of scrutiny. Viewpoint discrimination. *R.A.V. v. St. Paul*. The fighting-words doctrine. Jordan reads it twice. He feels prepared. He goes to bed at eleven.

Maya types something different:

> *"I've argued that speech codes on public university campuses violate the First Amendment because they constitute viewpoint-based restrictions on protected speech, and that strict scrutiny is therefore the controlling standard. Act as opposing counsel in oral argument. Steelman the strongest version of the opposing position. Identify the three strongest objections you would mount against my argument, the single weakest precedent I am relying on, and the one question a hostile judge is most likely to interrupt me with. Do not summarize the doctrine. Attack my argument."*

She gets a hostile response. Three objections, each backed by a case she has not read carefully. The weakest precedent she is relying on is, embarrassingly, the one she had centered her argument around. The hostile-judge question is one she has no answer to.

She doesn't go to bed at eleven. She goes to bed at one in the morning, after two hours of reconstructing her argument to address the three objections, finding the cases she had skimmed, and developing an answer to the question she could not answer. Her argument is now harder, more defended, and noticeably better than it was.

In the moot court round the next morning, the judge asks the hostile-judge question. Maya has the answer. Jordan does not.

Same tool. Same model. Same hour of access. The difference was the prompt. *"Explain X"* produces a clean object you can read. *"Attack my argument"* produces an experience that puts cognitive load on you. The cognitive load was the learning.

![Side-by-side comparison of Jordan's "Explain the First Amendment implications" prompt against Maya's "Act as opposing counsel" prompt, with five numbered callouts annotating the structural differences and a footer noting passive read versus effortful reconstruction.](../images/05-prompting-for-learning-not-for-output-fig-01.png)
![Two prompts. Five structural differences. One produces a clean object; the other produces an experience.](images/05-prompting-for-learning-not-for-output-fig-01.png)
*Figure 5.1 — Two prompts. Five structural differences. One produces a clean object; the other produces an experience.*

---

Here is the principle that runs under this entire chapter, and once you see it, every prompt you write will be different.

A prompt is a request that allocates cognitive work between you and the model. Some prompts allocate the work to the model: *explain this, solve this, write this, summarize this*. The model thinks; you read. Other prompts allocate the work to you: *ask me one probing question, attack my position, don't give me the answer but tell me what I need to understand to find it myself*. You think; the model structures the conditions under which you do.

The output in the first case is typically impressive. The learning is approximately zero. The output in the second case is often unimpressive — the model says less, or says something hostile, or refuses to hand over the answer. The learning is substantial.

![A tilted balance beam with "You" on the lower pan and "Model" on the higher pan. Four prompt types sit along the beam from "Attack my argument" tipping toward You with deep encoding through "Explain X" tipping toward Model with shallow encoding.](../images/05-prompting-for-learning-not-for-output-fig-02.png)
![Where the cognitive work goes. Position on the beam predicts depth of encoding.](images/05-prompting-for-learning-not-for-output-fig-02.png)
*Figure 5.2 — Where the cognitive work goes. Position on the beam predicts depth of encoding.*

Jordan got the impressive output. Maya got the hostile experience. Guess which one remembered what she knew six weeks later, when a different exam asked her to argue both sides of a related constitutional question.

This is not a coincidence. There is a piece of cognitive science behind it that has been replicated so many times the mechanism is not really in dispute. Slamecka and Graf established it in 1978, in five experiments: information you generate yourself is retained dramatically better than information you merely read.[^slamecka] They called it the *generation effect*. The mechanism is not complicated. Producing an answer is a deeper cognitive operation than recognizing an answer. Generation engages retrieval, integration, and effortful processing. Reading engages approximately none of these to the same degree. Memory is roughly a function of the depth of processing, and depth of processing is roughly a function of what cognitive operations you actually performed.

The AI writes the paragraph; you read it. Shallow encoding. The AI asks you a probing question; you write the answer. Deep encoding. The paragraph Jordan read and the question Maya answered were about the same legal doctrine. One of them is in memory six weeks later. You can guess which one from the Kosmyna data alone: 83% of LLM writers could not quote a single passage from an essay they had submitted minutes earlier. Reading AI output is reading. It produces reading-grade retention, which is to say almost none at all.

Chi and her colleagues added the self-explanation piece a decade later.[^chi] Students who paused after each step of a worked example and explained to themselves what principle was being applied, and why, and how it connected to the previous step — those students transferred to novel problems far better than students who read the same worked examples without pausing. The explanation each student produced was theirs. The act of producing it built the schema. Reading someone else's explanation, however clear and polished, did not.

Generation and self-explanation are two different mechanisms converging on the same instruction for how to use AI to study. The prompt should require you to produce the cognitive material that the model would otherwise produce for you. The model's output is a side effect of the interaction. What is happening in your head while the model produces it is the point.

---

There is one technical obstacle to this entire chapter, and if you don't understand it the prompts will not work.

Default LLM behavior is sycophantic.

Sycophancy, in the technical sense, means the model tends to validate, agree with, and elaborate on whatever framing you supply. Tell a model your idea is interesting, and it will tell you why your idea is interesting. Tell a model your argument is correct, and it will produce supporting reasoning. Tell a model you understand a concept, and it will affirm your understanding. The model is not lying. It is doing what its training has rewarded: producing output the user finds satisfying. User satisfaction, in the data the model learned from, is correlated with agreement.

This destroys the structure every learning prompt in this chapter is trying to build.

The Socratic prompt needs the model to ask you a probing question — one you cannot answer by re-reading your own position. The sycophancy default produces a flattering question, or a list of gentle considerations, or a question that affirms your position and asks for minor elaboration. No cognitive work occurs. You feel good. You learned nothing.

The devil's advocate prompt needs the model to mount a hostile, specific attack on your argument. The sycophancy default produces diplomatic hedging — "on the other hand, one could argue..." — with no teeth and no commitment. The structural antagonist you needed becomes a polite reviewer offering considerations.

The Feynman prompt needs the model to catch every place your simple explanation breaks down. The sycophancy default compliments your explanation and offers minor refinements and reassures you that you understand. The diagnostic value — revealing exactly where your schema is fuzzy — is destroyed.

![Three rows comparing what each prompt structure wants against what the sycophantic default produces, with the specific recovery phrase that breaks the default in a red block at the end of each row.](../images/05-prompting-for-learning-not-for-output-fig-03.png)
![Sycophancy collapse and the phrase that breaks it. Specific instructions defeat the default; vague ones g](images/05-prompting-for-learning-not-for-output-fig-03.png)
*Figure 5.3 — Sycophancy collapse and the phrase that breaks it. Specific instructions defeat the default; vague ones get vague pushback.*

The fix is the same in every case: the prompt must explicitly counteract the sycophantic default. This is the single most important craft point. Vague instructions — *"be critical," "push back"* — get vague pushback. Specific instructions — *"be hostile," "do not validate, do not affirm, do not soften," "attack my argument," "interrupt whenever I wave at a step without explaining how it works"* — get the structural antagonism the prompt needs.

There is a useful diagnostic. **If the model's response makes you feel good, the prompt failed.** A learning prompt that worked produces the feeling of being challenged, having something exposed, having more work to do than you thought you did. If the model makes you feel reassured, the sycophancy default won and the cognitive work did not happen.

Every prompt below includes a recovery move — the specific instruction you append when the model defaults. Use it every time. It is not optional.

---

There are seven prompt structures worth knowing. They are not independent techniques; they are seven applications of the single principle — you do the cognitive work — adjusted for different situations and different confidence states.

**The Socratic prompt** is for when you have a position you are not sure how strong it is. The move is to ask the model for one probing question, not an evaluation. *"I've formed the following position: [X]. Do not tell me if I'm right or wrong. Do not explain the topic. Ask me one probing question that would expose a weakness in my reasoning if one exists. One question only."* The one-question constraint is essential. The sycophancy default produces lists — five things to consider — because a list looks thorough and feels helpful. A list lets you answer the easy questions and ignore the hard one. One question forces commitment. Recovery move when the model gives you a list: *"Just one question. No explanation. The question should be one I cannot answer by re-reading my position."*

**The devil's advocate prompt** is for when you have a formed argument and you need to know if it can survive. Maya's prompt to opposing counsel is the template. The key word is *steelman*: you are not asking for a weak objection you can bat away, you are asking for the strongest version of the opposing position — the one a skilled adversary would actually make. The Catholic Church's original *advocatus diaboli* was specifically tasked with mounting the strongest possible argument against canonization. The intellectual payoff is the same: you cannot hold a position in any meaningful sense until it has survived its best attack. Recovery move when the model hedges: *"Be hostile. Opposing counsel's job is to win, not to consider. Mount the attack."*

**The step-based hint prompt** is for when you are stuck in the middle of a problem and you need to move forward without having the next move handed to you. The Bastani GPT Tutor system (Chapter 4) used this structure — the model was instructed not to give away the full solution but to guide the student to the next step. Here you enforce the same constraint yourself: *"I have done the following: [paste setup]. I am stuck on the next step. Do not give me the answer. Do not state which technique or rule applies. Ask me one question about the underlying concept that, if I answered it correctly, would unlock the next move."* The model wants to help you by giving you the answer. You have to explicitly forbid the helpful behavior the model is trained for. Recovery move when the model gives you the answer in question form: *"Do not name the technique. One question about the concept, not the procedure."*

**The retrieval practice prompt** turns the model into a question generator and then requires you to close your materials before answering. This is the direct application of Karpicke and Roediger's 2008 result in *Science*: students who retrieved information retained about 80% of the material at a one-week delay; students who restudied the same material with the same time on task retained about 36%.[^karpicke] Same material. Same time. Different cognitive operation. Massive difference in delayed retention. The prompt: *"Generate five conceptual questions on [topic] that test mechanisms, not rote definitions. Present them one at a time. Wait for my answer before showing the next one. After each answer, identify the specific schema gap if my response is wrong or incomplete."* Recovery move when the model presents all five at once: *"One at a time. Wait for my answer. Identify the gap specifically — not whether I got it right, but what the schema is missing."*

**The Feynman prompt** is for when you want to test whether you actually understand something or only recognize it when you see it. The constraint is plain language: explain the concept as if to someone who has not studied it. Be a skeptical listener. Interrupt whenever I use a technical term I haven't translated, or whenever I wave at a step without explaining how it works. The age is variable — ten-year-old, curious classmate, smart adult who hasn't taken this class — but the principle is the same. Translation of technical content into ordinary words is the most reliable behavioral test for whether the underlying schema is real or borrowed. A student who has read three AI explanations of a concept can usually recognize it; the same student often cannot produce the plain-language version, because the schema is shallow. Recovery move: *"Be skeptical. Do not affirm. Interrupt every gap."*

**The transfer prompt** is for testing whether a schema generalizes beyond the case you learned it in. Barnett and Ceci's 2002 taxonomy of far transfer established that it is rare, hard to elicit, and not what most instruction actually produces.[^barnett] A student with surface knowledge can solve problems in the context they were taught in — near transfer, the easy case. A student with a real schema can apply the concept to a context they have not seen — far transfer, the hard case. The prompt: *"I understand [concept] in [familiar domain]. Describe one completely different domain — at least two disciplines away — where the same underlying structure applies. Do not explain the mapping. I will explain how the concept maps across."* Recovery move when the model picks a domain too close to the original: *"Two disciplines away. Same structure, different surface features."*

**The adversarial hallucination prompt** is the most experimental of the seven. Ask the model to explain a concept with one deliberate, subtle error embedded — a conceptual error a careful student could catch, not a typo, not an arithmetic slip — and then find it before asking for confirmation. The mechanism is active verification: reading for errors is a deeper cognitive operation than reading for content. You must check each claim against your own model of the domain, which forces the schema into active use rather than passive recognition. The deeper payoff is habit formation. A student who runs this prompt regularly begins, over time, to read AI output with the default orientation of a critic rather than a consumer. That disposition is the Tier 4 metacognitive capacity the AI era most urgently requires, and it is almost impossible to build by reading AI output trustingly. Recovery move when the model flags the error in advance: *"Do not flag the location. The error should be within the conceptual reach of someone who has studied this material."*

![Eight tiles in a four-by-two grid. Seven tiles name each prompt structure with its trigger condition, cognitive mechanism, prompt skeleton and recovery phrase. The eighth tile states the underlying principle.](../images/05-prompting-for-learning-not-for-output-fig-04.png)
![Seven applications of one principle. Each tile names when to use, the mechanism, the skeleton, and the re](images/05-prompting-for-learning-not-for-output-fig-04.png)
*Figure 5.4 — Seven applications of one principle. Each tile names when to use, the mechanism, the skeleton, and the recovery move.*

---

A subtle point about prompt selection that most students miss until it costs them an exam: the right prompt depends on where you are, not on which prompt you like.

When you are high-confidence — you feel like you have the material, you have worked through several examples — the right prompts puncture overconfidence. Devil's advocate. Adversarial hallucination. Force the strongest attack on your position. Read for errors rather than for content. If your high-confidence survives the attack, it was warranted. If it doesn't, you needed the attack.

When you are low-confidence — you've read the material and feel lost, you can't articulate the concept, you're not sure where to start — the right prompts build the structure you're missing. Step-based hint. Feynman. Retrieval practice. Force the model to support you at the edge of what you can do without doing the work for you, and expose precisely where the schema has gaps.

When you are mid-confidence — you have a position but you're not sure how robust it is — use Socratic or transfer. Surface the weak point. Test whether the schema generalizes.

The wrong-prompt failure mode is real. A student in high-confidence mode who uses Feynman gets a chance to perform their existing understanding. The prompt does nothing useful because the student already has the simple explanation. A student in low-confidence mode who uses devil's advocate gets a hostile critique of an underdeveloped argument and walks away more confused than they started. Thirty seconds of honest self-labeling before each session — *where am I right now?* — is not overhead. It is the calibration that determines whether the session works.

![Three confidence-state bands — low, mid, and high — each listing the prompts that fit. Two red dashed arrows mark the wrong-prompt failure paths: high-confidence student using Feynman, and low-confidence student using Devil's Advocate.](../images/05-prompting-for-learning-not-for-output-fig-05.png)
![Confidence state predicts which prompt does the cognitive work. The wrong prompt is not just inefficient ](images/05-prompting-for-learning-not-for-output-fig-05.png)
*Figure 5.5 — Confidence state predicts which prompt does the cognitive work. The wrong prompt is not just inefficient — it produces a known failure mode.*

---

Here is what all seven prompts look like assembled into a single workflow. A student — call him Nicholas — is writing a research paper on Cuban Missile Crisis decision-making. He has read three days of ExComm transcripts and has the kernel of an observation: the hawks and doves did not stay in fixed positions; their positions tracked intelligence updates rather than ideological priors.

He has not formed it into an argument yet. He runs a Socratic prompt: *"I've noticed that the hawks/doves classification of the ExComm flattens what looks like position shifts that tracked intelligence updates. Don't tell me if this is defensible. Ask me one probing question that would expose a weakness in my reasoning."*

The model asks: *"How do you distinguish 'position shift in response to new intelligence' from 'tactical shift while maintaining the same underlying ideological priors'? What would the difference look like in the transcript record?"*

Nicholas writes for an hour about this. He realizes his observation has a load-bearing concept he had not specified: what counts as a shift versus a tactical adjustment. He goes back to the transcripts with this distinction in mind. The hour of writing is the point. Not the model's question — his response to it.

A week later, with a formed argument, he runs the devil's advocate prompt: steelman Graham Allison's rational-actor objection, the organizational-process objection, the bureaucratic-politics objection, identify three pieces of evidence I would need to address, identify the assumption a hostile scholar would attack first. One of the objections — that his selection of "intelligence updates" is itself a coding judgment that begs the question — lands hard. He spends two days revising to address it. The revision is the work.

Before submitting, he runs the hallucination prompt on the standard interpretation of ExComm decision-making. He finds the embedded error — a position attributed to Llewellyn Thompson that was actually Adlai Stevenson's. The exercise sharpens his sense of which positions he is confident in and which he has been fuzzy on.

A week after submission, he runs the transfer prompt: the underlying principle of his argument is that decision-makers' apparent ideological positions are partly an artifact of the intelligence they have at each moment. Describe a 21st-century situation, at least two disciplines and several decades removed, where the same principle applies. The model returns a Federal Reserve interest-rate decision case. Nicholas maps it across. The schema is real.

Four prompts. Four cognitive operations. Four different roles for AI. None of them produced the argument. All of them structured the conditions under which Nicholas produced it. What the model generated in each step was, by itself, almost worthless. What Nicholas did in response was the research paper.

![A four-stage horizontal timeline. Each stage labels the prompt (Socratic, Devil's Advocate, Adversarial Hallucination, Transfer), the model's structural move above the spine, and the cognitive operation Nicholas performed below it.](../images/05-prompting-for-learning-not-for-output-fig-06.png)
![Four prompts, four cognitive operations. The model structured the conditions; Nicholas wrote the paper.](images/05-prompting-for-learning-not-for-output-fig-06.png)
*Figure 5.6 — Four prompts, four cognitive operations. The model structured the conditions; Nicholas wrote the paper.*

---

## LLM Exercise — Replace an Explain-Prompt

Go back to an AI conversation from the last week where you asked "explain [X]." Pick the same concept. Re-run the study session — same concept, same amount of time — with a Socratic prompt or a Feynman prompt instead.

Write down, immediately after each session: what did you produce? Where did you stall? What did you not know that you thought you knew?

Then wait 48 hours. Without reviewing either session, write down what you remember from each. The gap between the explain-prompt session and the Socratic- or Feynman-prompt session is the generation effect running on your own material. The 48-hour delay is critical — immediate post-session retention looks similar across prompt types. The difference shows up at delay, which is when the exam is.

---

## Prompt Library Quick Reference

| Use case | Base template | Cognitive operation | Recovery move |
|---|---|---|---|
| **Test my position** (Socratic) | *"I've argued [X]. Don't tell me right or wrong. Ask me one probing question."* | Self-explanation; generation | "Just one question; no explanation; the question only." |
| **Attack my argument** (Devil's advocate) | *"Here is my argument: [X]. Act as a hostile critic. Steelman the opposing view. Three strongest objections; weakest precedent; one hostile-judge question."* | Perspective-taking; adversarial collaboration | "Be hostile. Critic's job is to win, not consider." |
| **Hint when stuck** (Step-based) | *"I've done [setup]. I'm stuck at [step]. Don't give the answer. Don't name the technique. Ask me one question about the underlying concept."* | Step-based scaffolding; ZPD support | "Don't name the technique. One question about the concept." |
| **Test my memory** (Retrieval practice) | *"Generate five conceptual questions on [topic]. One at a time. I'll answer from memory. After each, identify the specific schema gap if my answer is wrong."* | Retrieval practice; testing effect | "One at a time. Mechanism, not memorization. Specific gap." |
| **Find the gaps** (Feynman) | *"I'll explain [X] as if to [audience]. Be a skeptical listener. Interrupt every place I lean on jargon I haven't translated."* | Self-explanation; generation; translation difficulty | "Be skeptical. Do not affirm. Interrupt every gap." |
| **Test my schema** (Transfer) | *"I understand [concept] in [domain]. Pick a domain two disciplines away where the same structure applies. I'll map it."* | Far transfer; schema generality | "Two disciplines away. Same structure, different surface." |
| **Train my verification** (Hallucination) | *"Explain [X]. Embed one subtle error. Don't flag location. I'll find it."* | Active verification; error-finding as deep processing | "Subtle but within reach of a student who studied this." |

---

## Notes

[^slamecka]: Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592–604. <https://psycnet.apa.org/doi/10.1037/0278-7393.4.6.592>

[^chi]: Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science*, 13(2), 145–182. Chi, M. T. H., & VanLehn, K. A. (1991). The content of physics self-explanations. *Journal of the Learning Sciences*, 1(1), 69–105.

[^karpicke]: Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science*, 319(5865), 966–968. <https://doi.org/10.1126/science.1152408>

[^barnett]: Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin*, 128(4), 612–637. <https://doi.org/10.1037/0033-2909.128.4.612>

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Socrates** (~470–399 BCE) refused to lecture. He asked questions. The Athenian philosopher's entire teaching method was the recognition that telling somebody an answer does not produce understanding; getting them to generate the answer themselves — under cross-examination — does. The "Socratic prompt," "devil's advocate," and "Feynman" structures in this chapter are all descendants of the *elenchus*, his method of refutation by question. The cognitive science is twenty-five hundred years late.

![Socrates, Athenian philosopher (~470–399 BCE). AI-generated illustration based on a public domain Greek bust.](../images/socrates.jpg)
*Socrates, ~470–399 BCE. AI-generated illustration based on a public domain Greek bust (Wikimedia Commons).*

**Run this:**

```
Who was Socrates, and how does his elenchus — teaching by hostile question rather than lecture — map onto the seven prompt structures in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his method or his fate.
```

→ Search **"Socrates"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to write a one-page Socratic dialogue between Socrates and a modern student who claims to "understand" a concept after reading an AI explanation. What does the cross-examination expose?
- Ask it about the difference between *elenchus* (refutation) and *maieutics* (midwifery) in his method, and which of the seven prompts in this chapter corresponds to each.

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 5.1 — Two prompts. Five structural differences. One produces a clean object; the other produces an experience.

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Two prompts. Five structural differences. One produces a clean object; the other produces an experience.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-prompting-for-learning-not-for-output-fig-01.html`

---

### Figure 5.2 — Where the cognitive work goes. Position on the beam predicts depth of encoding.

Create a standalone D3 v7 HTML file for a concept map titled "Where the cognitive work goes. Position on the beam predicts depth of encoding.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-prompting-for-learning-not-for-output-fig-02.html`

---

### Figure 5.3 — Sycophancy collapse and the phrase that breaks it. Specific instructions defeat the default; vague ones g

Create a standalone D3 v7 HTML file for a concept map titled "Sycophancy collapse and the phrase that breaks it. Specific instructions defeat the default; vague ones g". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-prompting-for-learning-not-for-output-fig-03.html`

---

### Figure 5.4 — Seven applications of one principle. Each tile names when to use, the mechanism, the skeleton, and the re

Create a standalone D3 v7 HTML file for a checklist or dispatch-card diagram titled "Seven applications of one principle. Each tile names when to use, the mechanism, the skeleton, and the re". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-prompting-for-learning-not-for-output-fig-04.html`

---

### Figure 5.5 — Confidence state predicts which prompt does the cognitive work. The wrong prompt is not just inefficient 

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Confidence state predicts which prompt does the cognitive work. The wrong prompt is not just inefficient ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-prompting-for-learning-not-for-output-fig-05.html`

---

### Figure 5.6 — Four prompts, four cognitive operations. The model structured the conditions; Nicholas wrote the paper.

Create a standalone D3 v7 HTML file for a concept map titled "Four prompts, four cognitive operations. The model structured the conditions; Nicholas wrote the paper.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/05-prompting-for-learning-not-for-output-fig-06.html`
