# Chapter 9 — Sciences with AI

*The discussion section is not the record of an experiment. It is the cognitive event the experiment was designed to produce.*

> AI can simulate experiments, challenge hypotheses, and explain mechanism. It cannot do the inferential work of forming a scientific claim from observations.

---

Priya is in AP Chemistry the spring of her senior year. She is a strong student with pre-med ambitions and an efficient workflow: run the experiment, photograph the data table, upload everything to Claude with the prompt *"interpret these results and draft the discussion section."* Claude returns a discussion section consistently better than what she would write herself — more confident, more fluent, more correctly framed. Her lab reports score in the high 90s.

The unit exam includes a free-response question that hands her a fresh data set: pH readings at nineteen points during the titration of a weak acid with a strong base. Identify the equivalence point. Explain why the pH at the equivalence point is above 7, not at 7. Identify the pKa from the data and justify the identification.

Priya stares at the page. She knows the words. She has written paragraphs about all of them. *Equivalence point. pKa. Henderson-Hasselbalch.* She cannot, looking at this specific curve, identify where the equivalence point is and explain *why* the conjugate base hydrolyzes water to produce basic conditions at equivalence. She has read sentences about the mechanism. She has not done the inferential work that connects *this curve* to *that explanation*. She gets partial credit for naming the right concepts. She loses most of the credit for failing to apply them to the data in front of her.

The data on the exam were the same kind of data as in her lab, with different numbers. The cognitive event that should have happened in the original lab report — *given this data, what claim does the data support, and what alternative claims does it rule out?* — never happened. Claude did it. Priya read it. The interpretation never became hers.

This chapter is for Priya. In laboratory sciences, the discussion section is the schema-construction event. The inference from data to claim is the cognitive work the lab was designed to produce. AI is uniquely good at producing the artifact without that work. And every science test you will ever take, from AP Chemistry free-response to MCAT to graduate orals, tests the cognitive structure that the lab was supposed to build.

---

## What Science Schemas Actually Are

Chi, Feltovich, and Glaser's 1981 study on expert and novice problem-solving in physics revealed a pattern that runs through every science.[^chi1981] Experts categorize problems by deep principle — conservation of energy, acid-base equilibrium, redox couple. Novices categorize by surface features — what the diagram looks like, what kind of molecule is involved. The expert sees an inclined-plane problem and thinks *energy conservation*. The novice sees the incline and thinks *inclined plane.*

What makes scientific schemas different from mathematical ones is that they are mechanistic. A schema for the citric acid cycle is not a list of intermediates. It is a causal picture: why each step happens, what enzyme drives it, what the consequence is if a cofactor is missing, where the energy goes. The mechanistic schema is what lets you predict the outcome of perturbations you have never been shown — which is exactly what every AP Biology free-response question asks.

![Two columns sorting six physics problems twice — the novice column groups by surface features (inclined planes, pulleys, springs), the expert column regroups the same cards by deep principle (conservation of energy, Newton's second law, equilibrium). A dashed arrow connects the two organizations.](../images/09-sciences-with-ai-fig-01.png)
![Expert vs novice problem sorting (Chi, Feltovich &amp; Glaser, 1981). The schema is what makes the second](images/09-sciences-with-ai-fig-01.png)
*Figure 9.1 — Expert vs novice problem sorting (Chi, Feltovich &amp; Glaser, 1981). The schema is what makes the second organization possible.*

The whiteboard reconstruction test, which the chapter returns to at the end, is the operational version of this distinction. If you can sketch the pathway from memory and explain the causal sequence — *here is where the electron enters, here is where the proton is pumped, here is where the gradient drives ATP synthesis* — you have the mechanistic schema. If you can name the steps in order, you have rote knowledge. The exam asks: *what happens to ATP yield if the inner mitochondrial membrane becomes leaky to protons?* The list-of-intermediates student cannot answer. The mechanistic-schema student traces the consequence in twenty seconds: the leak destroys the gradient; no gradient means ATP synthase stops running; oxidative phosphorylation collapses while substrate-level phosphorylation continues briefly; the cell shifts toward anaerobic metabolism if the perturbation persists. That is what a schema does that a list cannot.

Priya had the list. She was missing the schema. The reason she was missing it is the reason the rest of this chapter exists.

---

## The Cognitive Crux: Dual-Space Search

In 1988, David Klahr and Kevin Dunbar gave participants a programmable robot whose hidden rules they had to discover.[^klahr1988] Some participants — the *theorists* — spent time in the hypothesis space: they formed specific candidate rules and ran experiments designed to discriminate among them. Others — the *experimenters* — ran many experiments without coordinating toward any specific hypothesis. The theorists did dramatically better. Their paper title is the claim: *Dual Space Search During Scientific Reasoning*.

The deep point, extended by Dunbar's in-vivo studies of working molecular biology labs in the 1990s, is that scientific reasoning is not primarily data interpretation. It is hypothesis-driven cycling between two distinct cognitive spaces — the hypothesis space (the set of candidate claims about what is going on) and the experiment space (the set of possible experiments to discriminate among the candidates) — with the data as the *discriminating event* in that cycle. The cognitive event that constitutes scientific reasoning is the *coordination*: forming a hypothesis specific enough to be falsifiable, designing an experiment that would distinguish it from alternatives, predicting what each hypothesis implies for the data, then comparing actual data against those predictions.

This is the cognitive event AI cannot perform for you. AI can suggest hypotheses. It can suggest experiments. It can even describe what the data looks like. It cannot do the *coordination* — the move that asks: *given my specific theoretical commitment and my specific data, which hypothesis remains viable and which is ruled out?* That move is the inference event. That inference event builds the schema. When AI produces the discussion section, it produces the inference without the event occurring in your head.

Here is the difference in concrete form. A kinetics lab measures how reaction rate of crystal violet dye changes across four concentrations of hydroxide ion. The data: rate increases approximately linearly with [OH⁻].

An AI-generated discussion: *"The data are consistent with first-order kinetics in hydroxide."* Smooth. Correct. Does no discrimination.

A student-generated discussion, the dual-space coordination written down: *"The approximately linear increase in rate with [OH⁻] is consistent with a first-order dependence on hydroxide. This distinguishes the first-order hypothesis from a zeroth-order hypothesis, which would predict no change in rate with [OH⁻], and from a second-order hypothesis, which would predict quadratic increase. It does not yet discriminate first-order from a saturable mechanism that appears approximately linear at low concentrations; a wider concentration range would be needed to make that discrimination."*

Both will receive good lab-report grades. Only one builds the schema the exam tests. The student who wrote the second version can answer: *"what additional data would you need to confirm the rate law?"* The student who submitted Claude's version cannot, because the discrimination event never happened in their head.

The misconception to retire: *"Interpretation is describing what the data shows."* It is not. The data does not show anything by itself. It shows something only relative to the hypotheses it could discriminate. The discussion section is the dual-space coordination committed to writing — or it is AI's generation committed to writing, with no cognitive residue in you.

![Two overlapping ellipses representing hypothesis space and experiment space, with a vertical coordination zone in the middle marked as where the schema forms. A dashed arrow shows an AI-generated discussion section landing outside both circles.](../images/09-sciences-with-ai-fig-02.png)
![Dual-space coordination (Klahr &amp; Dunbar, 1988). AI produces the artifact. The coordination event has ](images/09-sciences-with-ai-fig-02.png)
*Figure 9.2 — Dual-space coordination (Klahr &amp; Dunbar, 1988). AI produces the artifact. The coordination event has to happen in you.*

---

## Why the Discussion Section Matters So Much

The discussion section of a lab report is the locus of dual-space coordination. It is also the section students most consistently outsource to AI. The cognitive demands are specific and stackable:

What does the data support, and what does it rule out? What alternative explanations could have produced the same pattern — confounds, instrumental artifacts, hidden variables? Where does the inference run out — what does the data *not* discriminate? Does the result support, complicate, or fail to engage with the theoretical model the experiment was testing? And what would you need to do next to resolve what remains open?

Each of these is an inference event. Each is a place where AI can produce a fluent paragraph with the form of an inference without the cognitive substrate. The Kosmyna result from Chapter 2 operates here exactly as it operates in essay writing: the discussion section is on the page; the cognitive structure that should have produced it is not in the writer's head.[^kosmyna2025]

This is what Priya ran into. Her titration lab's discussion section, drafted by Claude, contained the sentence *"the equivalence point above pH 7 reflects the basicity of the conjugate base at the equivalence point."* That sentence is correct. Priya read it. She could not, on the exam, reconstruct *why* the conjugate base is basic — that acetate ion hydrolyzes water, accepting a proton to form acetic acid and producing hydroxide, shifting pH above 7. The sentence was in her lab report. The mechanism was not in her head. The difference between those two locations is the whole chapter.

The defense students sometimes mount: *"AI's discussion is more accurate than mine, so I should learn from it."* The accuracy is not the variable that matters. The variable is whether the inference event happened in your head. Reading a correct discussion section is recognition. Recognition does not build the schema. If you want to learn from AI's interpretation, the right move is to write your own first and then compare — the comparison is a learning event. Reading without writing first is not.

---

## What AI Is Actually Good at in Sciences

The constructive case matters as much as the cautionary one.

Where AI genuinely accelerates scientific learning is *outside* the dual-space coordination event. The strongest contribution is **parametric simulation**: asking AI to model what would happen under extreme or hypothetical conditions you cannot easily set up at the bench.

What happens to an enzyme-catalyzed reaction rate if temperature goes to 60°C? How does a chemical reaction proceed at high altitude with reduced atmospheric pressure? What happens to a planet's orbit if its sun loses 10% of its mass? AI works through the thermodynamics, the Le Chatelier analysis, the conservation laws. You build intuition for systems you cannot directly experiment on.

The cognitive load profile is favorable: AI handles the computational work, you handle the prediction and the integration with existing schema. But there is a load-bearing detail, and it is this: **you predict before AI computes.** You say what you expect will happen. AI shows the model output. You notice where your intuition matched and where it diverged. You update the schema.

Without the prediction step, parametric simulation is information consumption — a more sophisticated form of the same problem as AI-drafted discussion sections. With the prediction step, it is a schema-building exercise. The prediction is the cognitive event. AI is the engine that produces the outcome you compare your prediction against.

Kestin and colleagues' 2025 Harvard physics RCT is the strongest evidence for what this kind of interaction can produce.[^kestin2025] Students using a purpose-built AI tutor showed more than double the median learning gain of students in active-learning sessions led by experienced instructors using research-based pedagogy. That comparison condition was not lecture — it was already evidence-based teaching. The AI tutor still beat it. The seven design principles Kestin's team built into the tutor all share one structure: preserve the cognitive work for the student, use AI to scaffold the conditions around that work. The prediction-first parametric simulation protocol is the same principle, built by you at the user-prompt level.

The second genuine contribution is the **safety audit**. Before running any procedure with chemical, electrical, biological, or physical hazards, paste the procedure into AI and ask for hazards and incompatibilities specific to your experiment — not generic lab safety advice, but what is specific to your reagents, your concentrations, your equipment, your setting.

The electrolysis of brine is the illustration. A student has designed a U-tube cell with saturated NaCl, carbon electrodes, and a 9V battery. The headline hazard she might not have foregrounded: even at 9V, visible chlorine gas evolution begins within seconds at the anode, and chlorine is toxic at low concentrations. Without a fume hood, this experiment should not run on an open bench. AI flags this specifically, names the IDLH, names the cathode's NaOH production and its caustic implications, names the disposal requirement (neutralize before drain). The student adjusts the setup. No one loses their eyebrows.

This is the AI use that produces the largest concrete benefit per dollar of cognitive effort, and where the cost of bypassing is not a grade but physical harm. The chapter advocates it unconditionally — as one layer of protection, not the only layer.

---

## The Cyclical Phase Gate

The science phase gate is more complex than the math or writing gates because it opens and closes multiple times across a single lab cycle. The gate opens briefly before the experiment for design review and safety audit. The gate closes completely during data collection and initial interpretation — no mid-experiment consultation, no AI-assisted first pass at the data. The gate opens again after you have formed an independent interpretation, for the hostile critic and parametric deepening. The gate closes for the final write-up of substantive sections, and opens one final time for a mechanics-only pass.

The failure mode most specific to sciences is mid-experiment consultation. The student gets an unexpected observation and reaches for AI. The cost is contamination of the hypothesis space — AI's framing colonizes the student's thinking before the data are fully recorded, and the dual-space coordination that should happen between observations and hypotheses gets replaced by AI's pattern-matching. Keep AI closed during the experiment. Record observations as they happen. Ask AI later.

![Six horizontal bands across one lab cycle: pre-experiment (AI on), data collection (AI off), initial interpretation (AI off), post-interpretation (AI on), write-up (AI off), mechanics (AI on). Annotations mark the AI-off bands as the schema-construction window and the AI-on bands as scaffolding moments.](../images/09-sciences-with-ai-fig-03.png)
![The cyclical phase gate, one lab cycle. The gate state changes six times. Mid-experiment consultation is ](images/09-sciences-with-ai-fig-03.png)
*Figure 9.3 — The cyclical phase gate, one lab cycle. The gate state changes six times. Mid-experiment consultation is the failure mode specific to sciences.*

---

## The Whiteboard Reconstruction Test

The verification protocol for sciences is the whiteboard reconstruction test. Sketch the mechanism from memory and explain the causal sequence aloud. If you cannot, the AI processed the mechanism without you.

Close everything — textbook, notes, all tabs. Pick something specific: the citric acid cycle, the light reactions of photosynthesis, the electrolysis of brine, a series-parallel circuit, projectile motion with air resistance. Draw the diagram. Label the components. Mark the directions of energy or material flow. Then walk through the causal sequence aloud: what happens first, what triggers the next event, what the immediate consequence is, what would happen if a specific component were removed or a specific step were blocked.

Three categories of gap: a *component gap* (you forgot a specific enzyme or coefficient — memorization issue, routine review fixes it), a *causal gap* (you named all the components but cannot explain why one step follows another or what a perturbation would produce — this is the schema gap the chapter is centrally about), and a *direction gap* (you can trace the sequence forward but not backward — partial schema, fixable with reverse-direction perturbation practice). The causal gap is the one that matters. It is the gap that costs Priya her exam points. It is also the gap that the mechanism prober prompt, run after you have attempted the reconstruction, is specifically designed to close.

![A three-row table comparing component gap, causal gap, and direction gap across columns for what the gap sounds like during reconstruction and the recovery move. The causal-gap row is highlighted with an ochre border as the AI-bypassed schema this chapter is about.](../images/09-sciences-with-ai-fig-04.png)
![Three gap types in the whiteboard reconstruction test. Only the causal-gap row tells you whether AI proce](images/09-sciences-with-ai-fig-04.png)
*Figure 9.4 — Three gap types in the whiteboard reconstruction test. Only the causal-gap row tells you whether AI processed the mechanism without you.*

---

## Priya Redoes the Workflow

Three weeks after the titration exam, Priya is assigned a buffer-capacity lab: the same acetic acid system, now probed at three different initial concentrations to measure how buffer capacity scales with concentration.

Before the experiment, AI on briefly. She runs the experimental design prompt. Claude flags one concern: her plan to add titrant in 0.5 mL increments throughout will not resolve the curvature near the buffer transition — she needs 0.1 mL increments within ±2 mL of the expected equivalence point. She adjusts. She runs the safety audit; the procedure is low-risk, and the audit returns a short list (eye protection, careful pipetting of glacial acetic acid, dilute before titrating, no serious incompatibilities).

During the experiment, AI off. She uses the fine increments near the transition. She notices the pH electrode stabilizes slowly near the equivalence point and gives it thirty seconds per reading instead of the ten her procedure specified. The data table is more detailed than her previous ones. She does not consult AI.

After the experiment, initial interpretation, AI off. She looks at her three runs — 0.05 M, 0.10 M, 0.20 M initial acetic acid. The buffering region is wider, in terms of mL titrant, at higher concentrations. She drafts the interpretation on paper: *"Buffering capacity increases with initial concentration of the weak acid. This is consistent with the Henderson–Hasselbalch model — the pKa region depends on the [HA]/[A⁻] ratio, but resistance to pH change per unit of added base should scale with total concentration of the conjugate pair. The data discriminate capacity-scales-with-concentration from capacity-independent-of-concentration."* She is doing dual-space coordination on paper.

AI on briefly, hypothesis challenger. Claude returns: the apparent widening of the buffer region with concentration could partly reflect the electrode stabilization change she made — longer stabilization times at higher concentrations might produce a systematic broadening independent of real buffer capacity. To discriminate: run a replicate at highest concentration with the short stabilization time, or at lowest concentration with the long one, and compare. There is also a temperature confound she did not address — buffer capacity is mildly temperature-dependent and her procedure lacks constant-temperature control. Which issue does she want to address first?

She cannot rerun the experiment in this lab cycle. She addresses it in the discussion section by naming the electrode-response concern explicitly and stating that the measured concentration effect is therefore an upper bound. She updates the interpretation accordingly.

Discussion section, AI off. She writes it by hand. She names what the data support. She names the discrimination. She names the boundary of the inference (the electrode confound, the temperature confound). She proposes the next experiments. Eight hundred words. Her own dual-space coordination committed to writing.

Mechanics pass, AI on, light touch. Two grammar fixes. One citation format correction.

The unit exam, three weeks later, hands her a titration curve of a different weak acid — one she has never seen, with a different pKa and a different conjugate base. She reads the data. She identifies the buffer region. She identifies the equivalence point. She explains why the equivalence point is above pH 7. She names the limits of her inference. Full credit.

The schema is hers because the inference was hers.

![Six-stage pipeline of Priya's buffer-capacity lab arranged in a 3-by-2 grid: design review (AI on, Prompt 1), safety audit (AI on, Prompt 2), experiment (AI off), initial interpretation (AI off), hypothesis challenger (AI on, Prompt 3), discussion section (AI off). An outcome bar across the bottom shows the exam result three weeks later: full credit on a fresh weak-acid curve.](../images/09-sciences-with-ai-fig-05.png)
![Priya redoes the workflow. AI scaffolds three moments; the four schema-bearing moves stay on Priya's pape](images/09-sciences-with-ai-fig-05.png)
*Figure 9.5 — Priya redoes the workflow. AI scaffolds three moments; the four schema-bearing moves stay on Priya's paper, under her hand.*

---

## Exercises

### Warm-Up — The Pre-Prediction Lab Notebook Entry

Before your next lab, on the first page of your lab notebook, write your predicted result: what data values do you expect, and what claim about the world will they support if they come out that way? Be specific — not "I expect the rate to increase" but "I expect the rate to approximately double when I double the concentration of X, which would support a first-order rate law." After the experiment, compare prediction to outcome.

The gap between prediction and outcome is the schema-building event. A prediction that matches perfectly is a schema confirmed. A prediction that diverges is a schema that needs updating. A student who had no prediction before looking at the data is a student who cannot have a schema confirmed or updated — they can only read what the data says, which is not the same cognitive operation as comparing the data against something they thought they knew.

This is the Klahr-Dunbar theorist habit, made into a routine by a single line in your lab notebook written before the experiment begins.

---

### Application — The Whiteboard Reconstruction

Pick a mechanism from your current unit — citric acid cycle, light reactions of photosynthesis, electrochemical cell, free-body diagram on an inclined plane with friction, Henderson-Hasselbalch buffering. Close everything. Sketch it from memory on paper or a whiteboard. Label the components. Walk through the causal sequence aloud, ideally recording yourself.

Then check against the textbook. Classify each gap you find: component gap (memorization), causal gap (schema), or direction gap (partial schema). Write one sentence for each causal gap: *I can name this step, but I cannot explain why it happens or what a perturbation would produce.* That sentence is the precise location of the schema that AI processed without you.

The recording matters. Silent self-review produces overconfidence — the eyes fill in gaps the voice cannot bridge. The recording surfaces causal gaps that internal reading does not.

---

### LLM Exercise — The Prediction-First Parametric Simulator

This is the protocol that converts AI from an answer machine into an intuition-tester. The prediction is the cognitive event; AI is the engine you compare it against.

```
The system I'm studying: [describe — e.g., enzyme-catalyzed reaction, projectile motion
with air resistance, acid-base buffer, electrical circuit, photosynthesis under varied
light intensity].

The model / equation I'm using: [paste or describe].

Here's how this works:
1. I name a parameter to vary and predict — qualitatively — what the system will do.
2. You run the calculation under the variation and give me the answer.
3. If my prediction was wrong, I'll reconcile the difference.
   If my reconciliation is incomplete, ask me one probing question.

Wait for my prediction before computing each variation.

First parameter: [name it and predict what happens]. Run it.
```

Recovery move when AI runs multiple variations without waiting: *"Wait for my prediction each time. The prediction is the point. Don't compute until I say what I expect."*

The diagnostic: if you are never surprised, the exercise is not building anything. The schema-building event is the reconciliation between prediction and model output — especially the reconciliation you had to work for. Run six to eight variations per session. Write one sentence after the session: *which prediction was most wrong, and why?* That sentence is the schema update.

---

### Synthesis — The Dual-Interpretation Exercise

Take a lab data set — your own from this week, or any one from your textbook. Write the discussion section yourself, AI off, performing the dual-space coordination explicitly on paper: *this data is consistent with X; this data discriminates X from Y; this data does not discriminate X from Z; this additional measurement would resolve the open question.*

Then run the Hypothesis Challenger prompt (Prompt 3 in the reference section) on your interpretation. Compare AI's alternative hypothesis against the alternatives you considered. If AI's alternative is one you had already addressed, your schema is forming. If AI's alternative surprises you, that is the schema-extension event — incorporate it into your understanding before revising the written version.

The combination is more powerful than either move alone. Your interpretation builds the schema through generation. AI's challenge extends the schema into territory your pattern-recognition had not reached. The revision that closes the gap is yours.

---

### Challenge — The Teaching Test

Find a peer who has not yet done the current unit. Teach them the mechanism for ten minutes using a whiteboard or a piece of paper. Field their questions without notes. Record the conversation if you can.

The places where you cannot answer their question — where you said the step but cannot explain why it happens, or where their follow-up sends you somewhere you had not anticipated — are the places where the mechanism is in your hand-eye memory but not in your causal schema. A student with a genuine mechanistic schema handles unexpected questions by tracing the causal structure forward from the perturbation. A student with rote knowledge stalls when the question is not the one they rehearsed.

The teaching test surfaces gaps that the whiteboard reconstruction alone does not, because the listener's questions land in the specific places your own reconstruction was fluent over. Run it on the mechanism you are most confident about. The gaps that appear are the ones most worth returning to.

---

## Prompt Reference

Six prompts for the six AI-on moments across the lab cycle. Each is a structural move — the constraint language ("do not interpret," "do not redesign," "wait for my prediction") is doing real cognitive work and should not be softened.

**Prompt 1 — Experimental Design Reviewer.** Use before the experiment. Describe the procedure, hypothesis, controlled and measured variables, and what you expect to see if the hypothesis is right versus wrong. Ask AI to identify confounds, measurements too imprecise to discriminate hypotheses, and predictions too vague to be falsifiable. No redesign — located concerns only, one question per concern.

**Prompt 2 — Safety Auditor.** Use before any procedure with chemical, electrical, biological, or physical hazards. Paste the full procedure including reagents, concentrations, equipment, setting, PPE planned, and disposal plan. Ask for hazards ranked by severity — specific, not generic — and what to do when a specific failure mode occurs. If the procedure should not run in the described setting, AI should say so explicitly.

**Prompt 3 — Hypothesis Challenger.** Use before committing the interpretation to writing, after you have looked at the data and have a candidate claim. Describe the experiment, your working hypothesis, and the data pattern you see. Ask AI for the strongest alternative hypothesis that predicts the same pattern; what additional data would discriminate them; and one source of error that would reduce confidence in your hypothesis. Do not let AI interpret the data — you are asking what alternatives you should rule out, not what the data means.

**Prompt 4 — Mechanism Prober.** Use after you have drawn or articulated a mechanism, for deepening rather than initial learning. Describe the mechanism and your causal explanation. Ask AI to ask you one perturbation question per step — what if a reagent is removed, what if temperature changes, what if an enzyme is inhibited — waiting for your answer before proceeding. After the full walkthrough, AI identifies the step your answers were least confident on and asks one follow-up. AI assesses only whether your causal reasoning is sound, not whether the final answer matches the textbook.

**Prompt 5 — Parametric Simulator.** Full text above in the LLM Exercise section.

**Prompt 6 — Discussion-Section Hostile Critic.** Use after you have drafted the discussion section. Ask AI to act as a hostile but fair lab instructor: identify any claim that overruns what the data support; any alternative hypothesis the data would also be consistent with; any source of error an experienced reader would notice that you did not name; any place where the causal reasoning is fuzzy. Quoted sentences, no rewriting, one question about which issue to address first.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Richard Feynman (1918–1988)** spent two years rebuilding Caltech's introductory physics course around a single discipline: the moment when a student goes from naming a thing to explaining it. The *Feynman Lectures on Physics* turned that discipline into a textbook. His maxim — *"if you can't explain it simply, you don't understand it"* — is the whiteboard reconstruction test in one sentence. He also formulated what he called the first principle of science: *"you must not fool yourself, and you are the easiest person to fool."* That is the diagnostic this chapter has been describing. When AI writes a fluent discussion section and you read it and feel that you understand it, you have just fooled yourself about whether the inference event happened in your head. The Feynman technique — pick a concept, explain it in plain language to an imagined beginner, find the gap, return to the source, repeat — is the same loop as the recorded reconstruction. The point of the recording is that you cannot fool yourself about whether you said the sentence, only about whether you understood it.

![Richard Feynman, mid-lecture, circa 1965. AI-generated portrait based on a public domain photograph.](../images/richard-feynman.jpg)
*Richard Feynman, circa 1965. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

![Richard Feynman (1918–1988)](../images/richard-feynman-dcq.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Richard Feynman, and how do his Caltech lectures and the maxim
"if you can't explain it simply, you don't understand it" connect to the
science-with-AI workflow in this chapter — the dual-space coordination,
the whiteboard reconstruction test, and the AI-off bands? Keep it to
three paragraphs. End with the single most surprising thing about how
Feynman approached learning a subject he didn't yet understand.
```

→ Search **"Richard Feynman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to rewrite the whiteboard reconstruction test as a Feynman-technique procedure, then mark which step is the AI-off step that AI use most reliably erodes.
- Ask it about the Cornell sabbatical episode when Feynman, demoralized about research, decided to play with physics again "for fun" — what does that say about how schema-building feels when the cognitive event is yours?

What changes? What gets better? What gets worse?

---

## Notes

[^chi1981]: Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science*, 5(2), 121–152. <https://doi.org/10.1207/s15516709cog0502_2>

[^klahr1988]: Klahr, D., & Dunbar, K. (1988). Dual space search during scientific reasoning. *Cognitive Science*, 12(1), 1–48. <https://doi.org/10.1207/s15516709cog1201_1>

[^kosmyna2025]: Kosmyna, N., et al. (2025). Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task. *arXiv* preprint arXiv:2506.08872.

[^kestin2025]: Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports*, 15, Article 17458. <https://doi.org/10.1038/s41598-025-97652-6>

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 9.1 — Expert vs novice problem sorting (Chi, Feltovich &amp; Glaser, 1981). The schema is what makes the second

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Expert vs novice problem sorting (Chi, Feltovich &amp; Glaser, 1981). The schema is what makes the second". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-sciences-with-ai-fig-01.html`

---

### Figure 9.2 — Dual-space coordination (Klahr &amp; Dunbar, 1988). AI produces the artifact. The coordination event has 

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Dual-space coordination (Klahr &amp; Dunbar, 1988). AI produces the artifact. The coordination event has ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-sciences-with-ai-fig-02.html`

---

### Figure 9.3 — The cyclical phase gate, one lab cycle. The gate state changes six times. Mid-experiment consultation is 

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "The cyclical phase gate, one lab cycle. The gate state changes six times. Mid-experiment consultation is ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-sciences-with-ai-fig-03.html`

---

### Figure 9.4 — Three gap types in the whiteboard reconstruction test. Only the causal-gap row tells you whether AI proce

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Three gap types in the whiteboard reconstruction test. Only the causal-gap row tells you whether AI proce". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-sciences-with-ai-fig-04.html`

---

### Figure 9.5 — Priya redoes the workflow. AI scaffolds three moments; the four schema-bearing moves stay on Priya's pape

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Priya redoes the workflow. AI scaffolds three moments; the four schema-bearing moves stay on Priya's pape". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-sciences-with-ai-fig-05.html`
