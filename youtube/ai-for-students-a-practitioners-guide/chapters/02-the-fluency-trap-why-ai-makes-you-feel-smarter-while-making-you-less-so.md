# Chapter 2 — The Fluency Trap: Why AI Makes You Feel Smarter While Making You Less So

*Your metacognitive system cannot tell the difference between understanding something and reading something that sounds like you understand it.*

> The brain confuses perceptual fluency with understanding — and AI output is the most fluent thing you will ever encounter.

---

Here is a puzzle worth sitting with.

A student spends three nights on a history paper. He does real reading. He builds an actual thesis — a careful one, about proximate versus structural causes, about two historians whose readings of the same period genuinely conflict. He writes most of the paper himself, uses AI to help draft a few paragraphs where the argument got hard, reads the whole thing twice before he turns it in. At the moment of submission, he feels something specific: he feels that he understands this period of history more deeply than he ever has. The feeling is not vague. It has texture. He goes to bed proud.

Two weeks later, his teacher calls on him in class discussion. He opens his mouth to make his argument — the one he spent three nights building — and what comes out is a vague gesture toward "tensions between North and South." He cannot name his thesis. He cannot name either historian. He cannot say which one he had sided with or why. The teacher moves on. He sits there with his own paper in his binder, reading his own argument, which he cannot now defend.

The paper is on his laptop. The understanding is not in his head.

And the part that matters most: *two weeks ago, he was completely certain it was.*

What kind of mistake is that? How does a careful, diligent student — not a lazy one, not someone who just dumped a prompt and clicked accept — end up so wrong about his own understanding? And how was the error *invisible* to him at the moment it would have been most useful to catch?

This chapter is about the mechanism. Once you see it, you will not be able to stop seeing it work on yourself.

<!-- → [VISUAL: Single-panel opener — the student at his desk, confident, paper glowing on screen. Split to: the student in class, blank expression, paper open in his binder in front of him. No text. Let the contrast land.] -->

---

## The Signal Your Brain Uses

There is a piece of cognitive machinery that runs continuously below your attention, and its job is to answer a question you never explicitly ask: *how well do I know this?*

It doesn't answer the question by searching your memory and taking inventory. That would be slow, effortful, sometimes impossible. Instead, it uses a shortcut: it reads *how easily the material is processing*. If a sentence is going down smoothly — if your comprehension circuits are parsing it without friction, if the argument seems to click into place — the system returns a reading that says, roughly, *familiar, mastered, known*. If the material is resisting — if you're rereading, if things aren't connecting — the system returns *unfamiliar, foreign, not yet learned*.

The shortcut has a name in cognitive psychology: *processing fluency*. Norbert Schwarz spent decades mapping how this fluency signal propagates into judgment.[^schwarz] Fluent stimuli feel more true. Fluent explanations feel more understood. Fluent stock names feel like safer investments. The signal bleeds into every evaluation your metacognitive system makes, including the one you are making right now about whether you are learning.

For most of human history, this shortcut was approximately reasonable. When a concept processed fluently, it was usually because you had actually encountered it before — you had the schema, the neural architecture to receive it, the prior exposure that made the current pass easy. The fluency was a *symptom* of actual prior encoding. You could treat it as evidence of understanding because, most of the time, it correlated with understanding.

Alter and Oppenheimer showed in their 2009 review how broadly this bias operates.[^alter] Koriat and Bjork showed the specific mechanism that is going to get you: when you study material with the answer visible, your judgment of how well you'll recall it is *systematically inflated* relative to your actual recall at test time.[^koriat] The answer being in front of you creates fluency. The fluency fires the "I know this" signal. The signal does not discount for the fact that at test time the answer will be gone. You feel like you've learned it. You haven't. The feeling was reading the conditions of study, not the depth of encoding.

![Paired bars across three study conditions — answer visible, answer hidden, AI-drafted text — showing predicted recall (high) and actual recall at test (substantially lower), with a callout naming the gap "the illusion of competence."](../images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-01.png)
![The calibration gap. The signal "I know this" rises with fluency, not with what you can actually produce ](images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-01.png)
*Figure 2.1 — The calibration gap. The signal "I know this" rises with fluency, not with what you can actually produce at test time.*

Now here is the problem.

AI text is the highest-fluency material your brain has ever encountered. Every sentence is grammatically smooth. Every explanation is syntactically clean. Every argument is structured. There is no friction anywhere in the interaction — these models are trained, explicitly and at enormous scale, to produce text that humans experience as well-written. From your metacognitive system's point of view, AI output is like nothing it has ever processed. The fluency signal fires continuously. The "I understand this deeply" reading comes back strong, because the fluency is strong, because the fluency is *by design*.

But the fluency belongs to the model, not to you.

The metacognitive system cannot distinguish between fluency that comes from your own understanding and fluency that comes from the sophistication of a language model. It reads fluency. It finds fluency. It returns the "known" signal. And you — the student, the careful reader who went back twice — have no internal alarm to tell you that the signal is wrong.

This is the fluency trap: *your brain reads the fluency of AI output as evidence of your own understanding, because the same metacognitive machinery fires whether the fluency comes from inside you or outside you.*

<!-- → [VISUAL: Two-column diagram. Left: "Fluency from your own schema" → metacognitive system → "I know this ✓". Right: "Fluency from AI output" → same metacognitive system → "I know this ✓". Both arrows identical. No way to tell them apart from inside.] -->

That is what happened to the student with the history paper. When he read the AI-drafted paragraph integrating the two historians, the sentences flowed. His metacognitive system read the flow and said: *I know this. I have this.* The signal was real. It was generated honestly, by a brain doing exactly what it was built to do. It was also completely wrong about the question that actually mattered — *what can I do with this when the AI is not in the room?*

---

## What the Brain Was Actually Doing

In June 2025, a group at the MIT Media Lab did something that turned this behavioral argument into a direct measurement.[^kosmyna]

Fifty-four participants wrote SAT-style essays under three conditions: brain-only (no tools), search engine (Google but not AI), or LLM (ChatGPT). A 32-channel EEG cap recorded brain activity throughout. After each essay, participants were asked to recall and quote what they had just written.

The key measurement is *functional connectivity* — the statistical coupling between activity in different brain regions during the task. This is not "brain activity" in the pop-science sense of a region "lighting up." It is coordination. When you are doing a genuinely hard cognitive task — writing a paragraph that requires you to comprehend what you've written so far, synthesize new ideas with old ones, retrieve the right word, and form a memory of what you produced — different networks have to fire in coordinated patterns. High coupling on that kind of task means the networks that should be doing the work are talking to each other. Low coupling means they are not.

The brain-only writers showed the strongest, most distributed networks. The LLM users showed *up to 55% reduced connectivity* compared to the brain-only writers. (That "up to" is doing real work — it is the upper bound across analyzed networks and frequency bands, not a single average. Remember that every time someone quotes the number without the qualifier.)

![Three-column comparison of the Kosmyna 2025 study conditions — Brain-only, Search Engine, and LLM — with per-column EEG and recall expectations, plus a footer summarizing the two outcome measures (functional connectivity and quotation recall).](../images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-05.png)
![Kosmyna study design at a glance. n = 54, 32-channel EEG, SAT-style writing, post-task recall.](images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-05.png)
*Figure 2.5 — Kosmyna study design at a glance. n = 54, 32-channel EEG, SAT-style writing, post-task recall.*

What that 55% means: the coordinated multi-network coupling that *constitutes the cognitive work of writing* was substantially muted in the LLM group. The act of composition — the actual neural labor of producing prose — was happening in the model, not in the person supervising the model. The networks that a brain-only writer had to recruit and synchronize to generate a paragraph did not have to recruit and synchronize for an LLM writer, because the model was doing the recruiting.

This matters enormously for students, because writing is one of the rare tasks that forces comprehension *and* synthesis *and* memory formation to happen simultaneously. When the model is doing the production, those networks don't couple. The work that would have built the relevant memory — and the relevant capability — gets done in the model, not in your head.

The recall results are the hammer of the study. After each session, participants were asked to quote from the essay they had just submitted. Minutes earlier. Their own work.

*Eighty-three percent of LLM users could not quote a single passage.*

![Three bars on a zero-baseline percentage axis showing the share of writers who could not quote a single line from the essay they had just submitted: brain-only writers around 12 percent, search-engine users around 36 percent, and large-language-model users at 83 percent.](../images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-02.png)
![Eighty-three percent. Their own essay. Minutes earlier. The generation event happened in the model, not i](images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-02.png)
*Figure 2.2 — Eighty-three percent. Their own essay. Minutes earlier. The generation event happened in the model, not in the writer.*

Brain-only participants showed normal recall. The search-engine group fell between, closer to brain-only. And the LLM writers — who had just submitted polished essays, who had read them over, who had edited them — could not, minutes later, produce a single sentence from their own writing.

This is not a memory failure in any ordinary sense. This is the generation effect running in reverse. Slamecka and Graf demonstrated in 1978 that self-generated information is recalled substantially better than passively read information.[^slamecka] The mechanism is straightforward: when you produce something from inside your own mind, against the friction of retrieval, you lay down a richer, more cue-accessible memory trace. The struggling-to-find-the-word *is* the encoding event. When the model produces the prose and you supervise — even carefully, even with multiple edits — the generating is not happening in you. The trace that would have formed during generation does not form. The essay exists. The memory does not.

The student with the history paper is the 83%. Two weeks after submission, he sat in class with his own paper in his binder and could not reconstruct his own argument, because he had not generated it. He had supervised someone else generating it. Those are different cognitive events with different downstream consequences, and the difference is not accessible from inside the feeling you have while doing the work.

---

## The Debt That Accumulates

Eighteen participants returned for a fourth session in a swapped condition. Habitual LLM users wrote without the tool. Habitual brain-only writers were given the tool. This is the most important part of the study and the one that gets cited the most, and it needs the most care, because n=18 means the specific magnitudes should be held loosely.

The pattern was striking anyway.

People who had spent three sessions writing cold — who had built strong functional connectivity on the task — showed *increased* connectivity across EEG frequency bands when given the model. Their writing networks were already engaged; the tool slotted into a working cognitive system without disrupting it. They were using the AI while still doing the thinking.

People who had spent three sessions writing with the tool — whose composition networks had been quiet for three sessions — showed *reduced* alpha and beta connectivity relative to the brain-only baseline. Not reduced relative to themselves. Reduced relative to people who had never used the tool at all. Their networks had been quiet, and when the tool came off, they were still quiet.

The researchers call this accumulation of cognitive debt. The metaphor is from software engineering — shortcuts taken now that compound into costs later. Each session of delegating composition to the model deepens the gap between what the writer can do with the tool and what the writer can do without it. And the cost shows up exactly when the tool is gone, which is exactly when the high-stakes evaluation typically happens.

Hold the specific numbers loosely — four sessions, eighteen participants in the swap. But sit with the direction. The student who has been using AI for every essay all semester does not start at baseline when the in-class exam comes. They may start *below* baseline, because the networks they intended to switch back on have been quiet for months. "I'll stop when it matters" assumes that capability is a switch. The swap data suggest it is more like a muscle — and a muscle that hasn't been used doesn't snap back the moment you call for it.

The frictional principle from Chapter 1 gets sharper here. The struggle is not just the trigger for learning *in this session*. It is what maintains the capability over time. Cognitive friction is not an event-level requirement for a single learning outcome. It is a developmental requirement for not losing what you have already built.

![Two trajectories of functional connectivity across four writing sessions, with a shaded band at session four marking the tool swap. Brain-only writers, given the LLM at session four, hold or rise. LLM users, with the tool removed at session four, dip below the starting baseline.](../images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-03.png)
![The debt made visible. The networks that were quiet during delegation do not turn back on the moment the ](images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-03.png)
*Figure 2.3 — The debt made visible. The networks that were quiet during delegation do not turn back on the moment the tool is removed.*

---

## The Confidence That Hurts You

The last piece is the one that determines what kind of student you become, and it comes from a 2025 CHI paper by Hao-Ping Lee and colleagues at CMU and Microsoft Research.[^lee] They surveyed 319 knowledge workers who used generative AI at work weekly, collecting 936 examples of real AI-supported tasks, rated against Bloom's taxonomy for critical thinking engagement. They measured two kinds of confidence and looked at how each predicted critical thinking.

![Two horizontal bars on a zero-centered axis. Confidence in the AI extends leftward toward "less critical thinking"; confidence in yourself extends rightward toward "more critical thinking." Similar magnitudes, opposite signs.](../images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-04.png)
![Two confidences, opposite signs. Trust in the tool quiets the checking-mechanism; competence in yourself ](images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-04.png)
*Figure 2.4 — Two confidences, opposite signs. Trust in the tool quiets the checking-mechanism; competence in yourself supplies the ground truth that makes you a good critic of AI output.*

One sentence carries the whole finding:

*Confidence in the AI was associated with less critical thinking. Confidence in yourself was associated with more.*

Two confidence variables. They point in opposite directions.

When you trust the tool — when you believe the output is likely right, that the model has the answer — you do less auditing, less verification, less of the cognitive activity that would catch an error. Not because you are lazy. Because you have no reason to doubt. The checking-mechanism never fires, because the trusting-mechanism already fired.

When you trust yourself — when you have independent competence in the domain, built through prior unassisted work — you bring something the AI cannot supply for you: a ground truth to compare against. You know what the correct answer should look like. You can feel when something is off, because you have an internal version of "right" to check the external output against. That independent competence is what makes you a good critic of AI output. It is also what AI most easily erodes.

There is a loop here that is worth spelling out because it is the mechanism behind every student who thinks they are learning well and is not.

Low independent competence means you have nothing to compare the AI's output against. You cannot catch a hallucination because you do not know what the correct version looks like. The output is fluent, so the metacognitive signal says "correct." You trust the tool. You do less critical thinking. You accept more. The work you would have done to build independent competence — the struggling, the retrieval, the generation — does not happen. The competence does not build. Next time, you still have nothing to compare against.

This is not a stupidity loop. It is a structural loop. The student who is most at risk is the one who is the most trusting, the most collaborative, the most willing to incorporate AI assistance fluidly into their work — because those are the conditions under which the fluency signal is strongest, the tool-confidence is highest, and the critical-thinking rate is lowest.

The student who has done the hard unassisted work — who has struggled through the draft, who has generated the argument themselves, who has built the independent competence that feels slow and inefficient compared to AI — is the student who is safe to use AI. Because they have the ground truth. They can compare. They can catch the errors that the model cannot catch in its own output, because the model is using the same weights that produced the error to audit the error.

The most useful skill in an AI-saturated world turns out to be the one AI most efficiently erodes: knowing the domain well enough to know when you're being told something wrong.

<!-- → [VISUAL: Closed loop diagram. Nodes: "Low independent competence" → "Nothing to compare against" → "High tool confidence" → "Less critical thinking" → "No effortful encoding" → back to "Low independent competence." Label it: "The loop you need to break." Arrow to break point: between "No effortful encoding" and "Low competence" — label it "Generation. Struggle. This is the exit."] -->

---

## What You Cannot Feel From Inside

There is a student defense against this chapter that I want to take seriously before I explain why it doesn't work.

The defense is: *I edited it. I read it twice. I rewrote two paragraphs. It is mine.*

Editing is a real cognitive operation. The parts you rewrote got generation-effect encoding. You will remember those parts better than the parts you left alone. This is real and should not be dismissed.

But editing does not produce generation-effect encoding on the full content. The Kosmyna participants were also editing — that is the job description of AI-assisted writing. They still failed to quote 83% of the time. The sense that "I have processed this carefully enough that I know it" is exactly the feeling the fluency trap produces, in exactly the students who have processed it most carefully. The diligence is not a defense. It is, in a specific and uncomfortable way, the *condition* for the trap to fire most cleanly — because diligent students are the ones who engage closely enough with AI output for the fluency signal to be strongest.

The question you actually need to answer is not *did I process this carefully?* It is: *did I generate it?* The generation is the encoding event. Processing fluent output carefully is not generation. And the signal that tells you how well you've learned something cannot, from inside, tell you which of those two things just happened.

This is the reason external verification is not paranoia. It is calibration. Your metacognitive system is running an instrument that was calibrated for a world where fluency correlated with your own prior encoding, in a world where the most fluent thing you will ever encounter was produced by someone else. The instrument is giving you honest readings of the wrong quantity. You need a different test — one that bypasses the feeling entirely.

That test is simple. It is the one the student in the opening failed without knowing he was taking it. *Can you reproduce the argument, without notes, in your own words, for someone who wasn't there?* Not "do you recognize it as correct when you read it back." Recognize is the wrong question. Recall is the question. Recognition tells you about fluency. Recall tells you about storage.

![Side-by-side comparison of recognition and recall across four diagnostic rows — prompt provided, what it measures, predictive value, and the feeling it produces — with a final verdict row pointing to recall as the real test.](../images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-06.png)
![Recognition vs. recall. Two retrieval modes, only one predicts exam performance.](images/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-06.png)
*Figure 2.6 — Recognition vs. recall. Two retrieval modes, only one predicts exam performance.*

The difference is the whole chapter.

---

## Exercises

### Warm-Up — The Recognition Trap

Before your next study session, pick one concept you reviewed with AI help in the last week. Do not look at it. On a blank page, write everything you know about it from memory. Give yourself five minutes.

Then look at the original material. Compare what you wrote against what was there.

The gap between the two is not a study failure. It is a measurement. You are reading the recognition/recall asymmetry on your own material. Recognition says "yes, that's right" when you see it again. Recall is what you actually own. If the gap is large, the fluency trap was running on that material. If it's small, you generated enough of it yourself that the encoding stuck. The warm-up is just calibration — now you know which of your recent studying was real.

---

### Application — The Lee Diagnostic

Pick a recent AI-assisted task — a paragraph, a problem set, a set of notes. Score yourself on two questions, honestly, 1 to 10:

**(a)** How confident am I that the AI got this right?

**(b)** How confident am I that I would catch a subtle error if there was one?

If (a) is high and (b) is low, you are in the Lee high-tool-confidence, low-self-confidence quadrant. The data predict you did less critical thinking on this task than you believe. Either build the independent competence — so (b) goes up — or start treating the AI output as a draft to be tested, not a source to be trusted.

Run this diagnostic on three tasks from the past month. Look for the pattern. Not every task will show the same gap. The ones that do are the ones to watch.

---

### LLM Exercise — The Kosmyna Test on Yourself

Pick a topic in a course you are taking. Set a timer for twenty minutes. No AI: write on the topic. Note the friction — where you stall, where you don't know what comes next, where you have to reread to remember what you were arguing. Let the friction happen.

Now pick the same topic and do twenty minutes with AI. Note the fluency. Notice how the argument assembles itself.

Twenty-four hours later, without your notes, recall what you produced in each session out loud, into your phone's voice recorder. Do not review either version before recording.

Play them back. The asymmetry between what you remember from each session is not an abstraction. It is the fluency trap, running on your own material, in your own head. Once you have heard it, you will know what you are dealing with, and you will not need anyone to tell you it is real.

---

### Synthesis — Map Your Own Loop

Draw the Lee confidence loop from memory — the one that runs from low independent competence through high tool-confidence through less critical thinking and back. You do not need to reproduce the exact version from the chapter. Draw it as you understand it.

Then place yourself in it. For one specific domain you are currently studying, mark where you are on each node. Is tool-confidence high? Is your ability to catch errors low? Is the struggle happening or not?

The point is not to feel bad about where you land. The point is to locate the exit. The exit is always the same place: the node between "no effortful encoding" and "low competence." Generation is the exit. Where in your current studying are you generating, and where are you supervising?

---

### Challenge — The Two-Week Unassisted Stretch

Pick one routine task you would normally do with AI — a paragraph of an essay, a problem set, a set of study notes — and do it entirely without for two weeks.

Notice the friction in the first three days. It will be real. Write it down: what specifically is hard, where you stall, what you do not know.

Check again on day ten. Notice whether the friction has decreased. It should. The decrease is not the task getting easier. It is the network recovering. The friction on day one was the diagnostic that the network had atrophied. The recovery by day ten is the diagnostic that the network can come back — which is the good news this exercise exists to deliver.

If the friction has not decreased by day ten, you have found something more important: a competence gap that AI had been papering over. That gap was always there. Now you can do something about it.

---

## Notes

[^schwarz]: Schwarz, N. (2010). Feelings-as-information theory. In P. Van Lange et al. (Eds.), *Handbook of Theories of Social Psychology*. <https://dornsife.usc.edu/norbert-schwarz/wp-content/uploads/sites/231/2023/11/schwarz_feelings-as-information_7jan10.pdf>

[^alter]: Alter, A. L., & Oppenheimer, D. M. (2009). Uniting the tribes of fluency to form a metacognitive nation. *Personality and Social Psychology Review*, 13(3), 219–235. <https://pages.stern.nyu.edu/~aalter/tribes.pdf>

[^koriat]: Koriat, A., & Bjork, R. A. (2005). Illusions of competence in monitoring one's knowledge during study. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 31(2), 187–194. <https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/Koriat_RBjork_2005.pdf>

[^kosmyna]: Kosmyna, N., Hauptmann, E., Yuan, Y. T., Situ, J., Liao, X.-H., Beresnitzky, A. V., Braunstein, I., & Maes, P. (2025). Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task. *arXiv* preprint arXiv:2506.08872. <https://arxiv.org/abs/2506.08872> · MIT Media Lab project: <https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/>. Note: arXiv preprint, not yet peer-reviewed as of writing; n=18 for the fourth-session swap analysis.

[^slamecka]: Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592–604. <https://psycnet.apa.org/doi/10.1037/0278-7393.4.6.592>

[^lee]: Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. <https://dl.acm.org/doi/10.1145/3706598.3713778>

---

## AI Wayback Machine

The mechanism this chapter describes — a fluency signal that the metacognitive
system reads as evidence of knowing — was named in cognitive psychology in the
1980s. But the deep architecture sits a century earlier. **William James** (1842–1910)
spent the 1880s and 1890s mapping how attention selects, how habit grooves the
nervous system, and how the stream of consciousness is constantly producing a
feeling of authorship that may or may not match the underlying work. The
*Principles of Psychology* (1890) treats the "fringe" of consciousness — that
penumbra of felt familiarity around the focal object — as a real psychological
quantity. That fringe is the ancestor of what Schwarz a century later called
processing fluency: a non-propositional signal the mind reads as a verdict on
how well it knows the thing in front of it. James also argued, against the
introspectionists who trusted those signals at face value, that habit can produce
the feeling of effortful thought while the cognitive labor is being done by
something else entirely — a worn groove, an automatism, a routine running below
attention. Read him today and the fluency trap is sitting right there, waiting
for the language model.

![William James, circa 1890. AI-generated portrait based on a public domain photograph.](../images/william-james.jpg)
*William James, circa 1890. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

![William James](../images/william-james-1gl.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was William James, and how do his ideas on attention, habit, and the
stream of consciousness connect to the fluency trap and illusion of
competence we covered in this chapter? Keep it to three paragraphs. End
with the single most surprising thing about James's career or thinking.
```

→ Search **"William James"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to map James's "fringe of consciousness" onto Schwarz's processing
  fluency — what is preserved, what is added, what is lost in the translation?
- Ask about James's chapter on habit in *Principles of Psychology* and apply
  it to the four-session swap study: what would James predict for a student
  who had outsourced essay-writing to an LLM for a semester?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 2.1 — The calibration gap. The signal "I know this" rises with fluency, not with what you can actually produce 

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "The calibration gap. The signal "I know this" rises with fluency, not with what you can actually produce ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-01.html`

---

### Figure 2.2 — Eighty-three percent. Their own essay. Minutes earlier. The generation event happened in the model, not i

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Eighty-three percent. Their own essay. Minutes earlier. The generation event happened in the model, not i". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-02.html`

---

### Figure 2.3 — The debt made visible. The networks that were quiet during delegation do not turn back on the moment the 

Create a standalone D3 v7 HTML file for a concept map titled "The debt made visible. The networks that were quiet during delegation do not turn back on the moment the ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-03.html`

---

### Figure 2.4 — Two confidences, opposite signs. Trust in the tool quiets the checking-mechanism; competence in yourself 

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Two confidences, opposite signs. Trust in the tool quiets the checking-mechanism; competence in yourself ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-04.html`

---

### Figure 2.5 — Kosmyna study design at a glance. n = 54, 32-channel EEG, SAT-style writing, post-task recall.

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Kosmyna study design at a glance. n = 54, 32-channel EEG, SAT-style writing, post-task recall.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-05.html`

---

### Figure 2.6 — Recognition vs. recall. Two retrieval modes, only one predicts exam performance.

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Recognition vs. recall. Two retrieval modes, only one predicts exam performance.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-the-fluency-trap-why-ai-makes-you-feel-smarter-while-making-you-less-so-fig-06.html`
