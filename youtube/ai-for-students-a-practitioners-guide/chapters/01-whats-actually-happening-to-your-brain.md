# Chapter 1 — What's Actually Happening to Your Brain

*The struggle is not the obstacle to learning. It is the mechanism.*

---

There is a moment every student knows. You have just read something — a summary, a solution, an explanation — and it is clear. It makes sense. You follow it all the way through. You close the tab feeling like you have the thing. Then someone asks you about it two weeks later and you open your mouth and nothing comes out. Not nothing exactly — a few words, the general shape of the argument — but the architecture is not there. You have the outline of a building and no building.

Here is what I want to tell you: that is not a memory problem in the casual sense. It is not that you forgot. It is that the event that would have built the memory did not happen. The building was never constructed. You experienced the blueprint and confused it for the structure.

This chapter is about the difference between those two things, at the level of cells.

---

## The Brain Is a Prediction Machine That Updates on Mistakes

In the mid-1990s, Wolfram Schultz and his colleagues were recording from individual dopamine neurons in the midbrains of monkeys. The folk theory at the time was simple: dopamine fires when you get something good. Reward in, dopamine out.

The data said something more interesting.

The neurons fired strongest not when the reward arrived — but when the reward arrived *unexpectedly*. Once the monkey learned to predict the reward, the neurons stopped firing at delivery and started firing at the *cue* that predicted it. When the predicted reward failed to appear, the firing rate dropped below baseline. The neurons were not tracking reward. They were tracking *prediction error* — the gap between what was expected and what actually happened.[^schultz]

Yael Niv's 2009 review showed that this signal is mathematically identical to the temporal-difference update rule used in reinforcement learning algorithms.[^niv] Your brain, among its many jobs, is continuously generating predictions about what will happen next. When the prediction is right, nothing changes — the existing model is good enough. When the prediction is wrong, a phasic burst of dopamine opens a modification window in the synapses that produced the wrong prediction. The window is brief. During it, those specific connections can be updated. After it closes, they cannot — not by that event, not anymore.

This is why confusion is not the enemy of learning. It is the trigger.

When a prediction fires and gets confirmed, no update happens. When a prediction fires and gets *violated*, the update window opens. The moment of being wrong is the moment of being teachable. Not before it, not after it — at it.

Now consider what happens when you use AI to answer a question you do not yet know how to answer. The answer arrives. It is correct. It is fluent. Your brain reads it and comprehends it. But comprehension is not a prediction followed by an error — it is pattern-matching against what you already know. The sequences of neurons that would have generated your wrong attempt, gotten the violation signal, and updated — those sequences never fired. The window never opened. You have the answer. The synapses are unchanged.

This is not a metaphor. It is a description of what physically did not happen.

![A two-path flow diagram from cue through prediction to outcome. The confirmed-prediction branch shows no error signal, dopamine at baseline, and no synaptic update. The violated-prediction branch shows a phasic dopamine burst, a brief modification window, and synapses updating.](../images/01-whats-actually-happening-to-your-brain-fig-01.png)
![The prediction-error loop. The update happens only on the violated path.](images/01-whats-actually-happening-to-your-brain-fig-01.png)
*Figure 1.1 — The prediction-error loop. The update happens only on the violated path.*

---

## The Molecule That Only Shows Up When You're Doing the Work

A prediction error opens the modification window. Something has to walk through it. That something is, in significant part, a protein called Brain-Derived Neurotrophic Factor — BDNF.

BDNF is synthesized in neurons, often directly at the dendrite — the receiving end of the cell — and released during certain patterns of activity. It binds to a receptor on neighboring cells and initiates the biochemical cascade that strengthens specific synapses. The canonical review by Lu, Christian, and Lu (2008) established BDNF as the primary molecular regulator of activity-dependent plasticity at excitatory synapses, with the highest concentrations in the hippocampus and prefrontal cortex — the regions doing the most learning work.[^bdnf]

Three things matter here.

First: BDNF release is *activity-dependent*. Not all activity triggers it equally. The patterns that release it most strongly are the ones associated with effortful processing — working at the edge of what you can currently do. Coasting through familiar material produces much weaker signals.

Second: the protein is produced and consumed *locally*, at the specific dendrite that participated in the activity. The synapses that did the work get the protein and get stronger. The ones that did not do the work, do not. You cannot pre-load BDNF. You cannot borrow it from last week's studying and apply it to this week's exam. It shows up *if and only if* the effortful activity shows up.

Third: the chain from BDNF to long-term potentiation (LTP) — the cellular process that converts a brief experience into a durable synaptic change — is one of the most-studied pathways in molecular neuroscience. Block BDNF signaling in lab animals and LTP is impaired. The chain is not speculative; it is load-bearing.

A fair caution: we cannot currently open a calculus student's hippocampus and watch BDNF in real time. The inference from rodent LTP studies to human study habits is an inference, not a direct measurement. Mark it accordingly. But the behavioral evidence — which we will see in a moment — is entirely consistent with what this molecular story predicts, and the inference is widely accepted in the field.

The operational implication is direct. When AI does the cognitive work in your place — solves the problem, synthesizes the data, drafts the analysis — the activity pattern that would have produced BDNF release at the specific synapses encoding *your attempt* does not fire. Those synapses do not get the protein. They do not strengthen. The argument is biochemical, not motivational. The question is not whether you tried hard enough. The question is whether the neurons were in the right state at the right moment, and they were not, because the cognitive event that state is conditional on did not occur.

![A horizontal chain of five labeled boxes — effortful activity, BDNF release, TrkB binding, LTP cascade, synapse stronger — above a dendrite diagram with one active branch receiving BDNF and three inactive branches receiving nothing.](../images/01-whats-actually-happening-to-your-brain-fig-02.png)
![The BDNF chain runs only where the activity runs.](images/01-whats-actually-happening-to-your-brain-fig-02.png)
*Figure 1.2 — The BDNF chain runs only where the activity runs.*

---

## Memory Has a Physical Address

If you ask where a memory lives — physically, specifically — the closest current answer is: at synapses, on dendritic spines, in the pattern of which connections strengthened and which did not.

A dendritic spine is a tiny protrusion on the receiving end of a neuron, a few micrometers long. It is where most excitatory synapses live. When you learn something, two things happen at the spine level that have been *directly observed in living animals* through transparent windows surgically placed in the skull. Existing spines enlarge. And entirely new spines sprout from previously bare sections of dendrite.

Most of the new spines disappear within hours or days. The ones that survive are the ones that participated in the learning activity that mattered.

Yang, Pan, and Gan (2009) in *Nature* taught mice a forelimb-reaching task while imaging motor cortex in real time. New spines formed within hours of training. Most vanished. The ones that survived weeks later were on the neurons controlling the trained behavior. Different tasks produced new spines on different dendrites. The behavioral retention curve and the spine survival curve tracked each other.[^yang]

![Side-by-side schematic of a motor-cortex dendrite before training, with six baseline spines, and after weeks of training, with more spines and larger heads. Below, a control dendrite in the same animal that did no work and is unchanged.](../images/01-whats-actually-happening-to-your-brain-fig-03.png)
![A learned skill has a physical address. The trained dendrite grew. The control dendrite, in the same anim](images/01-whats-actually-happening-to-your-brain-fig-03.png)
*Figure 1.3 — A learned skill has a physical address. The trained dendrite grew. The control dendrite, in the same animal, did not.*

Two things to notice about this.

One: you cannot grow a spine for a skill you did not practice. There is no shortcut at the cellular level. The architecture you carry into the exam is the architecture your study sessions built — not the architecture AI's sessions built while you watched. If your study sessions consisted of reading AI-generated analyses, the architecture you have is whatever "reading fluent text" builds. Which, as we are about to see measured in a controlled trial, is not much.

Two: when popular writing about learning says "your brain is plastic," it usually means this — spine formation, spine enlargement, changes in synaptic strength — not the more controversial claim about adult neurogenesis (new neurons). The spines are the well-documented, directly-observed mechanism. They are what the evidence actually shows. They matter because they are *structural*. Memory is not a file stored somewhere. It is a physical shape the brain has grown into. Growing that shape requires the activity that triggers the growth.

---

## Two Strengths, Not One

The neurobiology gives us the mechanism. Robert Bjork and Elizabeth Bjork's 1992 paper gives us the framework that makes it personally actionable.[^bjork92]

Their central claim: memory is not one thing with one strength. It is two things with two independent strengths.

**Storage strength** is how deeply embedded something is in long-term memory. It builds slowly, through effortful engagement. Once built, it does not decay — not in any timescale that matters for a student.

**Retrieval strength** is how accessible something is *right now*. It spikes fast under good conditions. It also decays fast without practice.

The two strengths are *independent*. You can have high retrieval strength and low storage strength — you can have the material fluent right now and gone in two weeks. Cramming is this. Cramming the night before an exam produces high retrieval strength tomorrow and low storage strength next month. It feels productive. It is the wrong shape.

![A two-axis chart with time after study on the x-axis and performance on the y-axis. A dashed gray curve labeled retrieval strength rises sharply from study and falls steeply across two weeks. A solid dark curve labeled storage strength rises gradually and decays slowly. A vertical dashed line marks the exam day; the cortex has only the storage curve to draw on.](../images/01-whats-actually-happening-to-your-brain-fig-04.png)
![Storage strength is the curve the exam asks for. Retrieval strength is the curve cramming and AI feel lik](images/01-whats-actually-happening-to-your-brain-fig-04.png)
*Figure 1.4 — Storage strength is the curve the exam asks for. Retrieval strength is the curve cramming and AI feel like.*

Here is the counterintuitive move the Bjorkes made: the subjective experience of studying is dominated by retrieval strength. When retrieval is easy, study feels productive. When retrieval is hard, study feels unproductive. So the conditions that build the *most* storage strength — retrieval practice, spacing, interleaving — tend to feel the *most* difficult. And the conditions that build the *least* storage strength — massed review, re-reading, reading AI-generated syntheses — tend to feel the *most* fluent.

This is the structural trap. The feeling of learning and the fact of learning come apart. And AI has made the gap between them as large as it has ever been.

Every time you ask AI to provide an analysis before you have genuinely attempted to form one, retrieval strength on the result feels infinite — the answer is right there, fluent, correct. Storage strength gain on your own ability to produce that analysis: near zero. The subjective experience says "I understand this." The cortex says "I watched someone else understand this."

---

## The Data: What Happened When a Thousand Students Used Unguarded AI

This is not a theoretical worry. It was measured.

In June 2025, Hamsa Bastani, Osbert Bastani, and colleagues published a randomized controlled trial in *PNAS* with nearly a thousand 9th–11th-grade math students at a Turkish high school.[^bastani] Three conditions during normal practice sessions:

- **Control.** No AI. Standard practice.
- **GPT Base.** Standard GPT-4, no guardrails. Students could ask it whatever they wanted.
- **GPT Tutor.** GPT-4, but prompted to give hints, ask Socratic questions, and refuse to hand over the final answer.

After the practice sessions, all three groups took the same exam. Without AI. This is the point — the exam tested what the students had actually built, not what they could produce while the tool was on.

The numbers:

- During practice, GPT Base students scored about **48% higher** than control. GPT Tutor students scored about **127% higher**. Both AI groups looked substantially smarter with the tool on.
- On the unassisted exam, GPT Base students scored about **17 percentage points worse** than control. GPT Tutor students performed at roughly control level.

Read that again. The students with unguarded AI access scored 48% better during practice and 17 percentage points worse on the exam. The same students. The same material. The only variable was access to unguarded AI.

Two follow-on numbers worth knowing. Across the first session, 67% of GPT Base students' first interactions with the tool were either re-pasting the problem or directly requesting the answer. They did not use it as a tutor. They used it as an oracle. And GPT-4 produced logical or arithmetic errors in approximately 49% of the math problems in the study. Because the students had offloaded their critical evaluation to the model, many of them copied these errors as if they were correct — they did not catch them, because catching a math error requires the kind of schema that detects when something is off, and they had not built that schema.

Honest caveats: this is one school, one country, one age range, math only. There is a published correction to the paper; if you cite specific numbers, check the corrected version.[^bastanicorrection] The 49% error rate reflects GPT-4 at that moment; newer models do better on math benchmarks. The direction of the finding is what to anchor on.

Now connect it to the neurobiology. The 17-percentage-point exam decrement is not a mystery once you have the mechanism. The GPT Base students did not experience the prediction-error events that would have built the schema. The BDNF release at the specific synapses encoding their attempt did not occur. The dendritic spines for the procedure did not grow. Two weeks later, reaching for the material on the unassisted exam, they reached into cortex that was never built for this purpose. The gap between the practice score and the exam score is the behavioral signature of the neural events that did not happen.

The GPT Tutor result is the finding that tells you what to do about it. Same model, same students, same problems. With prompting that forced the tool to ask questions instead of giving answers, the practice gains were *larger* and the exam loss disappeared. The tool was not the problem. The mode of use was the problem. That is a fixable thing.

![Grouped bar chart with three groups — Control, GPT Base, GPT Tutor — each showing a dark practice bar and a lighter exam bar. Practice bars are highest for GPT Tutor and high for GPT Base; the exam bar for GPT Base is 17 points below control while the GPT Tutor exam bar matches control. A callout names the GPT Base exam decrement the schema gap.](../images/01-whats-actually-happening-to-your-brain-fig-05.png)
![The schema gap. The tool was the same; the mode of use changed everything.](images/01-whats-actually-happening-to-your-brain-fig-05.png)
*Figure 1.5 — The schema gap. The tool was the same; the mode of use changed everything.*

---

## What Happened in Nicholas's Summer

Nicholas is a high school junior from Cape Cod with interests in political science and international relations — the kind of student who reads the news the way other people follow sports. In the summer before his senior year, he reaches out to a professor at a nearby university and asks to collaborate on a research project. The professor connects him with a recent master's graduate named Utkarsh, and the two of them spend the summer working on a paper about the social and economic impacts of Syrian refugees in Jordan — part of a broader initiative called the Crispus Project, which asks students to build and document AI tools that enhance learning rather than replace it.

The premise of the project is exact: treat AI outputs the way a historian treats a primary source. Not as the answer. As evidence requiring verification.

In the first week, Nicholas asks Claude to summarize the humanitarian and economic situation for Syrian refugees in Jordan. He gets a clean, fluent, three-page synthesis. Policy frameworks, settlement patterns, labor market integration data, strain on Jordanian public services. He reads it. Takes notes. Feels like he understands the terrain.

Then Utkarsh asks him a question in their weekly meeting: *"What's your read on the tension between the Jordanian government's official welcome policy and the actual labor restrictions? What do you think is driving that gap?"*

Nicholas opens his mouth. Gets partway into the answer. Stops. He has the synthesis in his notes. He does not have a *position* on the tension — because forming a position requires comparing what the AI told him against primary sources, finding where they agree, where they diverge, and making a judgment about why. He had skipped all of that. The synthesis felt like understanding. It was, in fact, a fluent description of someone else's understanding, handed to him ready-made.

He spent the next two weeks reading primary documents: UNHCR reports, Jordanian labor ministry data, academic papers on labor market integration, news accounts of individual refugees. He wrote down what *he* saw — not what the synthesis said, what *he* noticed. He found places where the AI synthesis was accurate. He found places where it was misleadingly compressed — where "Jordan has integrated refugees into the labor market" obscured a much more complicated picture of which sectors, at what wage levels, under what legal constraints. That compression mattered for his argument.

Only then did he open the AI again. Not to summarize. To challenge. *"Here is my thesis about the gap between official policy and labor market reality. What is the strongest counterargument? What would a researcher who disagreed with me say? Where is my reading of the UNHCR data weakest?"*

The AI pushed back hard. He revised twice. The paper he submitted was one he could defend in a conversation — because the analysis in it was his, built from the primary sources, tested against counterarguments. The AI was a tool at both ends. It was not the middle.

Here is what happened, at the level of cells.

When Nicholas read the AI synthesis in week one, his brain was doing comprehension work. Parsing sentences. Integrating them with background knowledge. But it was not generating predictions about what the primary sources would show and discovering it was wrong. The surprise events that would have opened modification windows in the neurons encoding his understanding of the refugee situation — those events did not occur. The BDNF did not show up at the synapses that would have processed his failed prediction. The spines that would have grown to encode the argument never grew.

The two weeks of primary source reading were different. Every place where the primary sources contradicted the AI synthesis was a prediction-error event. Every place where his initial reading of a UNHCR table was wrong was a prediction-error event. The spines for *his* understanding of Jordanian refugee economics grew in those moments — not in the week when the synthesis arrived clean and required nothing of him.

His notes from week one are in his notebook. His analysis is in his cortex. Only one of those goes with him into the room when someone asks him to defend the work.

This is what "you don't actually know it" means at the level of the cell. It is not a criticism of his effort. It is a description of what his neurons did and did not do — and when.

---

## The Nicholas Test

Here is a diagnostic you can run on yourself right now.

Take one concept you studied with AI assistance in the last week. Close your laptop. Close your notes. Close the AI conversation. On a blank piece of paper, write down everything you remember about that concept from memory: the mechanism, the definition, a worked example, why it matters. Then compare to your AI conversation history and your notes.

What is on the paper that was in your head? What is not?

The gap is the gap in your cortex. It is not a moral failing. It is information about what your study sessions did and did not build. The only question is what you do with the information.

The students in Bastani's GPT Tutor condition did not take longer or work harder than the GPT Base students. They used the same tool on the same problems. The difference was whether the tool was allowed to bypass the moment of productive failure or was forced to route through it. The GPT Tutor condition, essentially, made the tool behave the way a good human tutor would: ask questions, give hints, make you do the reaching. The cognitive events still happened. The cortex still got built.

That is the available resolution. Not abstinence. Not unlimited oracle access. Using the tool in a way that preserves the events it is otherwise designed to bypass. The rest of this book is a detailed description of how to do that — chapter by chapter, skill by skill, in the specific domains where the bypass is most costly and the workaround is most tractable.

But first: run the Nicholas Test. Find out where you are.

---

## Exercises

The following exercises are designed for use with an LLM tutor. For each one, paste the prompt into your AI tool and engage with the questions it asks rather than asking the AI to answer for you. The goal is to generate prediction-error events — to be wrong about something, get the signal, and update. The AI's job in these exercises is to ask, not to tell.

**LLM Exercise 1 — The Schultz Mechanism (Apply).**
Paste this into your AI tool: *"I'm trying to understand why the dopamine prediction-error signal is the learning update, not just the reward signal. Ask me a series of questions to help me figure this out — don't explain it to me, just ask questions and let me work through it."* Work through it until you can explain the mechanism to the AI in your own words without prompting. Stop when you could teach it to a friend.

**LLM Exercise 2 — The Bastani Numbers (Analyze).**
Paste this: *"I need to understand why the GPT Base students scored 48% higher during practice and 17 points lower on the exam. Ask me questions about what was happening in the neurons during the practice sessions, and don't give me the answer — help me figure it out."* The goal: you should be able to reconstruct the causal story from prediction error through BDNF to the exam gap without prompting.

**LLM Exercise 3 — The Bjork Paradox (Analyze).**
Storage strength and retrieval strength are independent. That is the claim. Paste this: *"I'm trying to understand why the conditions that feel the most productive while studying often build the least durable memory. Challenge my understanding. Ask me what I think and then poke holes in it until I get it right."* You will know you have it when you can predict, from the two-strength framework, which study behavior produces which exam outcome and why.

**LLM Exercise 4 — Design Your Own Guardrail (Synthesize).**
Paste this: *"I want to use AI to help me study [topic you are currently learning] without letting it bypass the neural events that build durable memory. Help me design a protocol — but do this by asking me questions about what I understand about my own learning, not by giving me a ready-made protocol."* The output should be something specific to your subject and your current gaps, not a generic set of tips.

**LLM Exercise 5 — The Nicholas Test Debrief (Challenge).**
Run the Nicholas Test first (no AI, blank paper, ten minutes). Then bring the gap to your AI tool: *"I just ran a memory diagnostic on a concept I studied with AI help. Here is what I remembered and here is what I missed. Help me figure out what I should have done differently during the original study session — ask me questions about my process, don't just give me advice."* The goal is to reconstruct, in specific terms, which moments in your original session were prediction-error events and which were not.

---

## What Would Change My Mind

The central claim of this chapter is that unguarded AI use during study bypasses the neural events that build durable capability, and that the Bastani 17-point exam decrement is the population-level signature of that bypass.

Two specific findings would force a revision.

The first: a well-powered, peer-reviewed replication of Bastani — same design, randomized control, AI-on practice followed by AI-off exam — that found no meaningful exam decrement with current-generation models. If multiple independent labs ran the experiment and the gap had closed, the empirical anchor would be weaker. The mechanism story (Schultz, Lu, Yang, Bjork-Bjork) is older and broader than any single study and would not be undone by a failure to replicate the specific numbers. But the framing — "the data on this is not currently ambiguous" — would need a hedge.

The second: direct neuroimaging evidence that students using AI for hard cognitive work show normal prediction-error signaling and normal memory consolidation, not the reduced connectivity the literature currently points toward. If the predicted neural signature of bypass turned out not to be there, the inferential chain from cellular LTP to human study habits would need to be rebuilt.

What would not change my mind: individual students who used AI heavily and feel they have learned a lot. The Bjork-Bjork framework predicts this self-report regardless of underlying storage strength. The feeling of understanding and the fact of understanding come apart. The self-report is not the diagnostic. The unassisted test is.

---

## Still Puzzling

I do not fully understand why some students appear more resistant to the bypass effect than others. The Bastani study reports population averages and does not break out the high-performing or highly skeptical subgroups. My guess — and it is a guess — is that students who enter with strong independent capability use AI as a verification tool rather than an oracle, and therefore experience less of the bypass. But the individual-difference structure of this effect is not yet nailed down.

I also do not fully understand the writing-versus-STEM transfer. Bastani is math. The mechanism should generalize — prediction-error signaling is not a math-specific process — but no one has run the equivalent randomized trial on research and writing tasks that would let me say the mechanism is identical rather than parallel. The book treats them as one phenomenon. The literature has not yet fully earned that simplification.

---

## Bridge to Chapter 2

This chapter established what learning is at the level of cells, and what the specific bypass event looks like when AI removes the friction the cells depend on. The Bastani numbers are the behavioral signature. The molecular story is the mechanism.

The next problem is harder: *if the bypass is happening, why can't you feel it happening?* Nicholas felt he understood the refugee situation after reading the AI synthesis. The GPT Base students felt they had learned the math. The feeling was not dishonest — it was the accurate read of a real signal. It was just the wrong signal. The subjective experience of studying is not connected to the signal that matters; it is connected to a different signal that AI has made nearly infinitely strong.

Chapter 2 is about that signal. It has a name — the fluency trap — and it sits inside the metacognitive system, the part of the brain that evaluates its own knowledge. The trap is not a reasoning error you can think your way out of. It is a structural feature of how the monitoring system reads its own inputs. AI is the most powerful trigger of the fluency trap ever built, and understanding the trap is how you begin to work around it.

---

**Tags:** #learning-science #neuroplasticity #bastani #bjork #ai-and-students #prediction-error #cognitive-friction

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Donald Hebb (1904–1985)** was a Canadian psychologist whose 1949 book *The Organization of Behavior* proposed the rule that became neuroscience shorthand for everything in this chapter: *cells that fire together, wire together*. Hebb argued that learning lives in the strengthening of specific synapses through coincident activity — decades before anyone could image a dendritic spine in a living animal. The Schultz prediction-error story, the BDNF cascade, the Yang spine-survival imaging, and the Bjorkes' two-strengths framework are all, in some sense, Hebb's claim shown to be physically correct. When AI does the firing for you, your cells do not fire together, and they do not wire together — which is just Hebb, in 2026, with a chatbot.

![Donald Hebb, circa 1955. AI-generated portrait based on a public domain photograph.](../images/donald-hebb.jpg)
*Donald Hebb, circa 1955. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Donald Hebb, and what did he actually claim in his 1949 book The
Organization of Behavior? Be precise about the original rule, not the
"cells that fire together, wire together" paraphrase. Why did it take
forty years for the experimental neuroscience to catch up to him? Keep
it to three paragraphs. End with the single most surprising thing about
his career or his ideas.
```

→ Search **"Donald Hebb"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to compare Hebb's original 1949 framing against the modern dendritic-spine and BDNF literature — where was he right, where was he too imprecise, and where did the evidence force a revision?
- Ask it about Hebb's work at the McGill Sensory Deprivation experiments in the 1950s — what did those studies reveal about the brain's hunger for input, and how does that connect to what AI does to a student who never has to generate their own answer?

What changes? What gets better? What gets worse?

---

## Footnotes

[^schultz]: Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593–1599. <https://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.pdf>

[^niv]: Niv, Y. (2009). Reinforcement learning in the brain. *Journal of Mathematical Psychology*, 53(3), 139–154. <https://www.princeton.edu/~yael/Publications/Niv2009.pdf>

[^bdnf]: Lu, Y., Christian, K., & Lu, B. (2008). BDNF: A key regulator for protein synthesis-dependent LTP and long-term memory? *Neurobiology of Learning and Memory*, 89(3), 312–323. <https://pubmed.ncbi.nlm.nih.gov/17911219/>

[^yang]: Yang, G., Pan, F., & Gan, W. B. (2009). Stably maintained dendritic spines are associated with lifelong memories. *Nature*, 462(7275), 920–924. <https://www.nature.com/articles/nature08577>

[^bjork92]: Bjork, R. A., & Bjork, E. L. (1992). A new theory of disuse and an old theory of stimulus fluctuation. In A. F. Healy, S. M. Kosslyn, & R. M. Shiffrin (Eds.), *From Learning Processes to Cognitive Processes* (Vol. 2, pp. 35–67). Erlbaum.

[^bastani]: Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122. <https://www.pnas.org/doi/10.1073/pnas.2422633122>

[^bastanicorrection]: PNAS correction: <https://www.pnas.org/doi/10.1073/pnas.2518204122>

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 1.1 — The prediction-error loop. The update happens only on the violated path.

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "The prediction-error loop. The update happens only on the violated path.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-whats-actually-happening-to-your-brain-fig-01.html`

---

### Figure 1.2 — The BDNF chain runs only where the activity runs.

Create a standalone D3 v7 HTML file for a concept map titled "The BDNF chain runs only where the activity runs.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-whats-actually-happening-to-your-brain-fig-02.html`

---

### Figure 1.3 — A learned skill has a physical address. The trained dendrite grew. The control dendrite, in the same anim

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "A learned skill has a physical address. The trained dendrite grew. The control dendrite, in the same anim". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-whats-actually-happening-to-your-brain-fig-03.html`

---

### Figure 1.4 — Storage strength is the curve the exam asks for. Retrieval strength is the curve cramming and AI feel lik

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Storage strength is the curve the exam asks for. Retrieval strength is the curve cramming and AI feel lik". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-whats-actually-happening-to-your-brain-fig-04.html`

---

### Figure 1.5 — The schema gap. The tool was the same; the mode of use changed everything.

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "The schema gap. The tool was the same; the mode of use changed everything.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/01-whats-actually-happening-to-your-brain-fig-05.html`
