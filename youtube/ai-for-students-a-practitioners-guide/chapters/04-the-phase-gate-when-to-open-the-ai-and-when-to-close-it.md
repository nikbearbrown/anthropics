# Chapter 4 — The Phase Gate: When to Open the AI and When to Close It

*Gate placement is the decision. Everything else is consequences.*

---

There is a principle in experimental physics that the apparatus you use to measure something changes what you are measuring. You cannot observe an electron without bouncing a photon off it, and the photon changes the electron's momentum. The measurement problem is not a problem with your technique. It is a feature of the situation. The question is not how to measure without disturbing — you can't. The question is how to disturb in a way that still tells you something true.

The AI version of this is different but structurally related. The tool you use to learn something changes what you learn. Not a little — enormously. A thousand students studied with AI and were then tested without it, and the ones who had used unguarded AI during practice scored 17 percentage points below the students who had used no AI at all.[^bastani] The AI did not fail them. It gave correct answers throughout. The problem was not the tool. The problem was *when* the tool was open and *when* it was closed. That single variable — gate placement — is the one that determined whether they came out smarter or weaker.

This chapter is about how to place the gate.

---

## What a Gate Actually Is

The phase gate is not a philosophy. It is a sentence of the form: *AI handles X. I handle Y. The gate is at moment Z.*

If you cannot write those three things down for the task in front of you, you do not have a gate. You have a vague intention, and vague intentions lose to the path of least resistance. The path of least resistance is always AI doing everything, because AI is in your pocket and always willing.

The gate has to be explicit — written, not held in your head, where it will quietly soften the moment you are tired. It has to be specific — not "I'll use AI responsibly," which has never produced a gate in the history of students using AI, but *"AI locates the primary sources and gives me the data structure of the field. I read the primary sources. I form my own interpretation. AI does not enter again until I have a 500-word claim with three pieces of supporting evidence."* And it has to be enforced — because the moment the gate is tested will be the moment you are also tired, behind on three things, and the AI is one tap away. Pre-commitment is the gate. The wavering moment is when it matters.

Why does this need to be its own chapter? Why not just say "use AI carefully"? Because *carefully* is a feeling, and feelings are exactly what the fluency trap corrupts. Chapter 2 showed that students cannot reliably tell, from the inside, when AI is doing the learning versus when they are. The internal sense of "I'm using this responsibly" is produced by the same system that generates the sense of "I've learned this," and both can be wrong at the same moment in the same way. The phase gate is an external commitment because the internal signal is unreliable.

---

## Nicholas and the Gate He Almost Missed

Nicholas is a high school junior from Cape Cod who reaches out to a professor about a summer research project. The professor connects him with a recent master's graduate named Utkarsh, and together they work on a paper about the social and economic impacts of Syrian refugees in Jordan — part of the Crispus Project, an initiative that asks students to treat AI outputs the way a historian treats a primary source. Not as the answer. As evidence requiring verification.

The first thing Nicholas does is the thing almost every student does. He types into Claude: *"Summarize the social and economic situation for Syrian refugees in Jordan."* He gets a beautiful answer. Comprehensive, fluent, well-structured: settlement patterns, labor market integration data, strain on public services, policy frameworks. He reads it. Takes notes. Feels like he understands the terrain.

Then he stops.

He realizes something uncomfortable. The project he is supposed to be working on requires him to *form his own analytical argument* from primary sources. The AI has just handed him a pre-assembled picture of the situation. If his thesis matches the AI's synthesis, his thesis is the AI's synthesis. If his thesis differs from the AI's synthesis, he has no way to know whether he is seeing something real or just being contrarian. Either way, he has not done the analytical work that constitutes the research.

He closes the AI tab.

He opens it again ten minutes later — but differently. *"Give me a list of primary sources on Syrian refugees in Jordan — UNHCR reports, Jordanian government labor ministry publications, peer-reviewed academic papers. Include URLs where available. Do not synthesize or summarize any of them. Just the sources."* The AI gives him the list. He prints it. He closes AI again.

Then he reads the primary documents. Three weeks. UNHCR displacement reports, labor ministry restrictions, academic papers on integration outcomes, news accounts from Jordanian journalists. He writes down what *he* sees — not what the synthesis said, what *he* notices. He finds something. The AI synthesis had said "Jordan has integrated refugees into the labor market." The primary sources showed something much more complicated: specific sectors, specific wage restrictions, specific legal frameworks that created a two-tier labor market the synthesis had compressed into a single optimistic phrase. That compression was his thesis. The gap between what the official synthesis said and what the primary data showed was the argument.

Only then did he open AI again. *"Here is my thesis about the gap between official policy narratives on refugee labor market integration and the actual data from primary sources. Challenge this reading. What would a researcher who disagreed with me say? What is my reading of the UNHCR data weakest on?"* The AI pushed back hard. He revised twice. He submitted.

The gate opened twice and closed twice in a single project. Where Nicholas placed it determined what he learned. That is the only lesson in this chapter — everything else is working out the implications.

---

## The Same Gate, in a Different Domain

The phase gate is not a humanities trick. The same placement decision happens, with the same consequences, in domains where the work product is code rather than prose. Seth is a high school senior who has been shipping games for several years — a co-op horror survival game in Godot 4 migrated system-by-system out of Unreal, a horror title on Roblox, a mobile arcade game on Google Play. He has also co-built two production AI agents — Walker, a senior Unity refactoring agent, and Zelda, a senior game design document consultant. Both are documented in the appendix to this book (`chapters/98-appendix-walker-and-zelda.md`) and both encode the phase-gate discipline directly in their system prompts.

The decision that recurs in his work is the same decision Nicholas made over the UNHCR documents, structurally. A playtest of the co-op horror game surfaces a bug: the AI-driven enemy state machine occasionally locks into pursuit mode after the player has left line of sight, producing a flat rather than escalating tension curve. The path of least resistance — Seth's first instinct, the one he had to train himself out of — is to paste the script and the bug description into Claude Code and ask for a fix. A patch arrives in fifteen seconds. The behavior changes. The bug is gone. The session ends.

The session ends with no schema. Seth has the patch; he does not have a model of why the state machine entered the bad state, and the next time a related bug appears — a different enemy archetype, a different transition — the same fifteen-second loop runs again, and again no schema forms. After enough cycles, Seth has shipped a game whose AI behavior he cannot explain in an interview and cannot extend without re-opening Claude every time.

The gated version: AI closes. Seth reads the state-machine code himself, traces the transition logic by hand, and writes a one-paragraph hypothesis about which condition is failing to fire. *The pursuit-to-search transition depends on a line-of-sight raycast that returns true for one frame inside thin cover, so the timer never starts and the enemy never drops out of pursuit.* The hypothesis is on paper before AI opens. Then AI opens — not to produce the fix, but to challenge the hypothesis. *Here is my theory. What in the code would falsify it? What is the alternative explanation I am underweighting?* The model pushes back, names a second condition Seth had not considered, and Seth revises. Only then does the fix get written. The schema is in his cortex, not in the patch.

The gate placement in Walker and Zelda is exactly this discipline turned into a prompt. Walker's five-phase model — Audit, Restructure, CLAUDE.md, Refactor, Verify — refuses to design a refactor step before the audit script has been run. Zelda's phase-gate enforcement layer refuses to produce design output before the user has committed to a phase. Both agents encode, in the system prompt, the rule that the human's first attempt must precede the AI's contribution. The discipline this chapter is teaching is the discipline those agents were built to enforce when a tired or rushed user tries to skip the gate.

---

## Why the Gate, Not the Tool, Is the Decision

The clearest data on this is the study I described in the opening. Hamsa Bastani and her colleagues ran a randomized controlled trial in a Turkish high school with nearly a thousand 9th–11th-grade math students.[^bastani] Three groups practiced math with the same material: one with no AI (the control), one with a standard GPT-4 interface where students could ask whatever they wanted (GPT Base), and one with the same GPT-4 configured to give hints, ask Socratic questions, and refuse to hand over the final answer (GPT Tutor).

During practice, GPT Base students scored about 48% higher than control. GPT Tutor students scored about 127% higher. Both AI groups looked substantially smarter with the tool on.

Then came the unassisted exam.

GPT Tutor students performed at roughly control level — no learning loss, no gain either, but the practice advantages didn't cost them anything. GPT Base students scored **17 percentage points worse than the students who had never used AI at all**.

![Grouped bar chart of three conditions (Control, GPT Base, GPT Tutor) across two phases (During practice, Unassisted exam). GPT Tutor is highest during practice; GPT Base falls 17 points below control on the exam while GPT Tutor lands on the control line.](../images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-01.png)
![Bastani et al. (2025). Same tool, same students. Where the gate sat decided the outcome.](images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-01.png)
*Figure 4.1 — Bastani et al. (2025). Same tool, same students. Where the gate sat decided the outcome.*

Same tool. Same GPT-4 model. Same students. Same problems. The only variable was where the gate sat — which cognitive work the model did versus which the student did. In GPT Base, there was no gate; students asked, the model answered. In GPT Tutor, the gate was hard-coded into the prompt: the model would explain a concept but wouldn't give the final answer; the student had to produce each inferential step. One design. 17 percentage points. On the exam that mattered.

There is a second study that tells the other side of the same story. Kestin and colleagues at Harvard ran a within-subjects randomized trial in the introductory physics course.[^kestin] Students alternated weeks between active-learning sessions led by trained instructors using research-based pedagogy, and sessions with a purpose-built AI tutor designed around seven explicit principles — facilitating active learning, scaffolding, refusing to give away the full solution, growth-mindset framing. The AI tutor produced **more than double the median learning gain** of the active-learning sessions, in less time, with higher engagement. The comparison condition was not lecture — it was already-evidence-based active-learning instruction by trained Harvard physics educators.

What explains double the gain? The AI tutor's system prompt included this: *"DO NOT give away the full solution."* That is a gate. The students had to do the final cognitive work. The tool was present, helpful, enormously capable — and gated at exactly the right moment.

The full spread — from 17 points below control to double the control gain — is explained by a single variable: where the gate sits. AI gets the extraneous friction; you get the thinking that builds the schema. The gate is the line between them.

---

## The Cognitive Architecture Behind the Gate

Why does it matter so much where the gate sits? The clearest answer comes from John Sweller's cognitive load theory, developed at UNSW in the late 1980s.

Working memory is small. For novel material, somewhere around 3–4 chunks simultaneously. That is the entire workspace you have to think with at any given moment. When you are learning something, three different kinds of demand compete for that workspace.

**Intrinsic load** is the difficulty inherent in the material itself — the number of interacting elements you must hold in mind to make sense of the concept. Analyzing the gap between official refugee policy and primary labor market data has higher intrinsic load than reading a summary of that gap, because you must hold the policy framework, the data, and the relationship between them in working memory simultaneously while forming a judgment. You cannot reduce intrinsic load without reducing what is being learned.

**Extraneous load** is the cognitive cost of how the material reaches you, separate from the material itself — the source you cannot locate, the citation format you keep looking up, the data table whose structure you have to decode before you can read it. These costs are real; they consume working memory. But they contribute nothing to learning. They are pure friction with no signal.

**Germane load** is the cognitive work that *constitutes* learning — the synthesizing, the schema construction, the connecting-the-new-thing-to-the-old-thing that builds durable structure. This is the load that does the work. This is what your working memory is for in a study session.

If extraneous load fills your working memory, nothing is left for germane load, and no learning occurs. The phase gate sits exactly at the boundary between extraneous and germane. AI gets the extraneous side. You get the germane side. That is the conceptual answer to "where does the gate go?"

![Two stacked-bar containers representing working memory. Left container, no gate: intrinsic load at base, extraneous above it, an AI-occupied germane region, and only a sliver of empty space at top. Right container, gated: intrinsic load at base, a thin extraneous band absorbed by AI, and a tall germane region carried by the student.](../images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-02.png)
![Working memory is a small container. The gate decides what fills the germane region.](images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-02.png)
*Figure 4.2 — Working memory is a small container. The gate decides what fills the germane region.*

The move that confuses students is treating intrinsic load as extraneous. When Nicholas asked AI to synthesize the refugee situation in week one, he was asking it to reduce intrinsic load — to spare him the difficulty of holding the policy framework, the UNHCR data, and the labor market restrictions in working memory simultaneously while forming a judgment. The result was a feeling of clarity and no real analytical capacity. The AI had replaced the argument with a summary, and Nicholas had mistaken the summary for understanding. The intrinsic difficulty was the point.

The test: after AI's synthesis or explanation, can you produce the full analysis yourself — the specific claims, the specific evidence, the specific judgment about where they agree and where they diverge? If yes, AI reduced extraneous load and you learned. If no, AI replaced the analysis with a thinner version and you are carrying a map of a territory that doesn't match the exam.

---

## The Scaffold That Doesn't Come Down

The second theoretical frame that explains the gate comes from Vygotsky's concept of the *zone of proximal development* — the gap between what a learner can do alone and what they can do with support. The ZPD is where learning lives. Below it, the task is too easy and nothing is learned. Above it, the task is too hard and the learner has no traction. Inside it, with the right support, the learner does something they could not do alone — and over repeated cycles, the supported ceiling becomes the new independent ceiling.

Wood, Bruner, and Ross (1976) named the support mechanism *scaffolding*. They borrowed the word from construction sites deliberately. Scaffolding holds the structure up *while the structure is being built*. Once the structure is self-supporting, the scaffolding comes down. That is the defining property of pedagogical scaffolding: it fades. A scaffold that never fades is not training wheels. It is a different vehicle. The student doesn't become a cyclist; they become someone who rides a tricycle.

Unguarded AI is a scaffold that doesn't come down. The Bastani GPT Base condition is exactly this — the model provided the answer at every level of demand, no pressure ever accumulated for the student to produce more independently, and when the scaffold was removed on exam day the structure collapsed by 17 percentage points relative to students who had never used a scaffold in the first place.

The GPT Tutor condition is what a proper scaffold looks like. Hints inside the student's ZPD: enough to take the next step, not enough to skip it. The student produced each intermediate move. The scaffold supported, the student built, the scaffold receded. No learning loss because the structure had been built during practice.

Here is the uncomfortable implication: **fading does not happen on its own.** Students routinely tell themselves, *"I'll use AI a lot at the start while I'm learning, and use it less as I get better."* This sounds like fading. It almost never works. As the work gets harder, you reach for AI more, not less — because AI is always willing, the assignments are harder, and time is shorter. There is no mechanism inside the AI use itself that creates the upward pressure on independent performance that the ZPD requires.

The fading has to come from outside. From the gate. The gate is the mechanism that does what unconstrained AI cannot: it imposes the condition that you must produce the first attempt without help.

---

## The First Attempt Is the Whole Game

The pedagogical literature has a name for the rule that makes the gate work. Manu Kapur called it *productive failure*, developed in controlled studies starting with his 2008 paper in *Cognition and Instruction*.[^kapur] His question was simple: which is better — teach the concept first, then practice; or have students attempt problems first (under-prepared), then teach?

The intuition is obvious. Teach first, then practice. Every textbook in the history of education does this. Kapur's data said the intuition was wrong. Students who attempted complex problems before instruction — who *failed*, in the sense of not producing correct solutions — outperformed students who got instruction first on every measure that mattered: correct solutions on the final assessment, depth of conceptual understanding, and transfer to novel problems. The failure was not a side effect to be tolerated. It was the mechanism.

Why? Three things happen during a failed first attempt that don't happen when you receive instruction cold.

The failed attempt activates prior knowledge. When Nicholas tried to form an argument about Jordanian refugee economics before reading the primary sources, he mobilized everything he already knew about labor markets, immigration policy, humanitarian economics — into the workspace. Those frameworks were warm and available when the primary sources arrived.

The experience of insufficiency creates a need for structure. When the AI synthesis produced a clean picture Nicholas could not interrogate, he discovered viscerally that he could not get from "I have read a summary" to "I have an argument." He felt the gap. When the primary sources arrived, the specific details that contradicted the synthesis landed on a question his brain was already asking.

The comparison between the AI synthesis and the primary source evidence was the schema-construction event. Nicholas saw where the synthesis was accurate, where it was compressed, where it had made a judgment call that he could evaluate and dispute. That comparison — not the synthesis alone — was where his analytical understanding of the refugee situation got built.

![Two horizontal timelines stacked. Top timeline: read synthesis, recognise structure, attempt, fail, exam — ends in recognition memory only. Bottom timeline: attempt, feel insufficiency, read sources, compare against synthesis, exam — the compare node is marked as the schema-construction event and tagged "the gate opens here for critique".](../images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-03.png)
![Synthesis first vs. attempt first. Same materials, different order, different schema.](images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-03.png)
*Figure 4.3 — Synthesis first vs. attempt first. Same materials, different order, different schema.*

The phase gate is, structurally, a productive failure design. You attempt first. You encounter the limits of what you can do with what you currently have. Then AI enters — either to help you locate sources, or to challenge an argument you have already formed. The Bastani GPT Tutor arm is exactly this pipeline. The 127% practice gain with no learning loss is the signature.

The common objection: *"Productive failure is just letting students flounder."* No. Kapur's designs are structured. The failure is bounded — a fixed time window — and the AI's entry is part of the design. The point is not to make you suffer. The point is to put your brain in the receptive state that makes the AI assistance actually do something rather than replacing the event it was supposed to follow.

---

## Where the Gate Goes: Four Task Types

The general principle — AI gets the extraneous side, you get the germane side, your first attempt is unassisted — generates specific gate positions for the kinds of tasks you actually do.

**Research and analysis.** The germane work is forming an interpretation from primary materials. The extraneous work is locating sources, identifying key actors, getting a sense of the field's landscape.

AI opens for source location and field mapping — primary and secondary sources, key actors, relevant theoretical frameworks. AI closes during reading and interpretation. AI re-opens *after* you have a developed thesis, to challenge it — present the strongest opposing reading, identify where your evidence is weakest.

The failure mode is asking AI to synthesize the sources before you have read them. The synthesis becomes your reading. You have notes; you do not have an analytical relationship with the documents. Nicholas almost made this error. The correct version was: AI provides the source list; you read the sources; you form your argument; then AI re-enters as hostile critic.

![Three side-by-side phase boxes. Phase 1 (light): source location, AI open, extraneous load. Phase 2 (dark): reading and interpretation, AI closed, germane load. Phase 3 (light): argument challenge, AI open again, extraneous load. Arrows mark the gate closing between 1 and 2 and re-opening between 2 and 3. An ochre-bordered callout below names the central failure mode: asking AI to synthesise sources before reading them.](../images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-04.png)
![Research and analysis. Two gates, one workflow; the order is the lesson.](images/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-04.png)
*Figure 4.4 — Research and analysis. Two gates, one workflow; the order is the lesson.*

**STEM problems.** The germane work is the *setup*: identifying what is being asked, choosing variables, drawing the diagram, selecting the relevant equation. Once the setup is correct, the execution is often mechanical. The setup is the schema-construction event.

AI does not see the problem until you have done the setup and gotten stuck on a specific step. AI's role is to ask a guiding question about the concept behind the next step — not to state the technique, not to walk through the solution.

**Writing.** The germane work is the formation of the argument: thesis, body paragraphs, evidence selection. The extraneous work is source location, citation formatting, copy-editing.

AI does not enter until you have written three raw thesis drafts and at least one first-pass body paragraph. AI enters only to critique what you have written. AI does not draft.

**Exam preparation.** The germane work is *retrieval* — bringing the material back from memory under conditions that approximate the test.

AI generates the question. You close AI. You answer from memory. You re-open AI for evaluation afterward. The failure mode is asking AI to "explain this unit to me" the night before the test. This is restudy, not retrieval.

| Task type | AI opens (extraneous side) | AI closes (germane side) | Common failure mode |
|---|---|---|---|
| Research and analysis | Source location, field mapping, identifying key actors and frameworks | Reading primary documents, forming interpretation, building the argument | Asking AI to synthesize sources before you read them — the synthesis becomes your reading |
| STEM problems | After the setup is done and you are stuck on one step, asking for a guiding question about the concept | Identifying what is asked, choosing variables, drawing the diagram, selecting the equation | Pasting the problem cold — AI does the setup, which is the schema-construction event |
| Writing | Source location, citation formatting, copy-editing, critique of what you have already written | Thesis formation, body-paragraph drafting, evidence selection | Asking AI to draft before you have written three raw thesis attempts |
| Exam preparation | Generating practice questions, evaluating your answers after the fact | Answering each question from memory, without AI in the room | "Explain this unit to me" the night before — restudy, not retrieval |

*Table 4.1 — Where the gate sits, by task type. Extraneous load is AI's side; germane load is yours.*

---

## Nicholas Takes the AP History Free-Response

Two months after the summer project, Nicholas takes his AP World History exam. One of the free-response questions asks about the economic and social integration challenges facing refugee populations in host countries, with reference to specific historical and contemporary cases.

Nicholas has a choice he has already made. He does not have AI. He has a pen and a blank answer booklet. He has whatever he built over the summer.

He writes for twenty-two minutes. His thesis: that the gap between official host-country policy narratives and actual labor market outcomes for refugee populations is a structural feature of the political economy of humanitarian reception, not a failure of implementation. Evidence: the Jordanian case, specific labor ministry restrictions, the two-tier wage structure. Counterargument: he names it explicitly — the argument that the gap reflects security concerns rather than economic protectionism — and addresses it with the UNHCR data that distinguishes the two explanations. He writes the sentence, *"The compression of this distinction in most policy summaries reflects a political interest in maintaining the official welcome narrative while restricting labor market competition."* He does not look it up. It is in his cortex, not his notes.

He has no way to know that week whether his response was good. What he knows is that he had something to say. The argument was his. He formed it from primary documents over three weeks, tested it against counterarguments, and revised it twice. It did not arrive in his head clean and fluent from a synthesis. It arrived the way all real understanding arrives: with difficulty, with specific errors that got corrected, with the friction that left spines on his dendrites.

That is the gate. The summer project was the practice. The AP free-response was the unassisted exam. What the gate protected in July was still there in October.

---

## What Would Change My Mind

The central claim of this chapter is that gate placement — not tool selection — determines learning outcomes, and that the difference is large enough to matter (Bastani's 17-percentage-point swing, Kestin's doubled median gain). This would need revision if a well-powered RCT, in a population other than Turkish high school math students or Harvard physics undergraduates, found that **unguarded AI assistance produced equivalent or better unassisted-exam performance than control conditions across multiple subjects and stages**. The directional pattern — in-practice gain, out-of-practice loss — is consistent across the studies that exist as of mid-2026, but the evidence base is thin and recent.

---

## Still Puzzling

The Bastani GPT Tutor result preserved performance but did not improve it on the unassisted exam. The Kestin result doubled the median gain. Both are scaffolded-AI conditions. What explains the gap? Is it the seven design principles in the Kestin tutor, the cognitive demand of physics versus high-school math, the cohort, or something about how the tutor was engineered that has not yet been isolated?

The "first attempt unassisted" rule is the most consequential design rule in this chapter and the one students most resist. Is the discomfort itself a useful signal that the gate is in the right place, or is there a way to make productive failure less aversive without losing the cognitive benefit?

---

## Bridge to Chapter 5

The phase gate decides *when* AI is open and when it is closed. That is half of the framework. The other half is what AI actually does when it is open. The same gate, opened at the same moment in the same workflow, can host a Socratic question that drives germane load up — or an answer-producing prompt that drains germane load to zero. Same gate. Different prompt. Different cognitive outcome. Chapter 5 takes the gate as given and asks the next question: when AI is open, what should you actually say to it?

---

**Tags:** #phase-gate #cognitive-load #productive-failure #bastani #kestin #sweller #vygotsky #kapur #ai-and-students #study-design

---

## Footnotes

[^bastani]: Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122. <https://www.pnas.org/doi/10.1073/pnas.2422633122>

[^kestin]: Kestin, G., Miller, S. T., McCarty, L. S., Callaghan, K., & Deslauriers, L. (2025). AI tutoring outperforms active learning. *Scientific Reports*, 14, 38151. <https://www.nature.com/articles/s41598-024-79270-w>

[^kapur]: Kapur, M. (2008). Productive failure. *Cognition and Instruction*, 26(3), 379–424.

[^karpicke]: Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science*, 319(5865), 966–968.

---

## AI Wayback Machine

The idea that the *environment* — not the lecture — does most of the teaching is older than AI by a century. **Maria Montessori** (1870–1952), the first woman to qualify as a physician in Italy, turned her clinical attention to children and built a pedagogy around one structural claim: the room is the teacher. Her *prepared environment* is a space where every material is sized, weighted, and presented to invite exactly one kind of work, and a child chooses freely among materials that have been chosen for them. The teacher is mostly silent. The materials have a built-in feedback signal — the puzzle does not fit unless you place it correctly — so error correction happens between the child and the object, not between the child and the adult. That is the phase gate, rendered in wood and metal, half a century before anyone wrote "system prompt."

![Maria Montessori, circa 1913. AI-generated portrait based on a public-domain photograph.](../images/maria-montessori.jpg)
*Maria Montessori, circa 1913. AI-generated portrait based on a public-domain photograph (Wikimedia Commons).*

![Maria Montessori](../images/maria-montessori-b57.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Maria Montessori, and how does her "prepared environment" concept connect to the phase-gate idea — designing when AI is open and when it is closed? Keep it to three paragraphs. End with the single sharpest sentence you can about what her materials would look like if she designed them for a student studying with an LLM today.
```

→ Search **"Maria Montessori"** and **"prepared environment"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to design a Montessori-style "AI material" for one task you're currently working on — what would the built-in feedback signal be?
- Ask it where Montessori's framework breaks for adolescents and adults, and what part of her design would still survive that translation.

What changes? What gets better? What gets worse?

---

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 4.1 — Bastani et al. (2025). Same tool, same students. Where the gate sat decided the outcome.

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Bastani et al. (2025). Same tool, same students. Where the gate sat decided the outcome.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-01.html`

---

### Figure 4.2 — Working memory is a small container. The gate decides what fills the germane region.

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Working memory is a small container. The gate decides what fills the germane region.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-02.html`

---

### Figure 4.3 — Synthesis first vs. attempt first. Same materials, different order, different schema.

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Synthesis first vs. attempt first. Same materials, different order, different schema.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-03.html`

---

### Figure 4.4 — Research and analysis. Two gates, one workflow; the order is the lesson.

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Research and analysis. Two gates, one workflow; the order is the lesson.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-the-phase-gate-when-to-open-the-ai-and-when-to-close-it-fig-04.html`
