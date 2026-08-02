# Chapter 7 — Math and STEM with AI

*The setup is the skill. Everything after it is arithmetic.*

---

Here is something that took me a long time to understand about physics problems. When I was learning, I thought the hard part was the math. The equations. The algebra. The integration. I would struggle through derivations and feel that the struggle was the point — grind through the calculation and come out the other side knowing something.

Then I watched an expert look at a problem.

She read it once. Glanced at the diagram space. Picked up her pen. And before she wrote a single equation, something had already happened in her head that I could not see. Within ten seconds she was not solving the kite problem or the balloon problem or the ladder problem — she was solving a *type* of problem, of which the specific scenario was just one instance. The surface was invisible to her. She saw the deep structure: two quantities related by a geometric constraint, both changing in time, differentiate the constraint. The kite, the ladder, the melting snowball, the expanding ripple — all of them lit up the same pattern.

What she had was a schema. And I did not yet have one. And the difference between us was not intelligence. It was the number of times each of us had done the setup ourselves.

---

## What a Schema Is and Why AI Is So Good at Destroying It

In 1981, Michelene Chi, Paul Feltovich, and Robert Glaser asked novice and expert physics problem-solvers to sort problems by similarity. The novices clustered them by surface: pulley problems with pulley problems, inclined planes with inclined planes. The experts clustered them by deep principle: every conservation-of-energy problem in one pile, every Newton's-second-law problem in another.[^chi1981] The surface features were invisible to the experts as organizing categories. They had been replaced by something more abstract and more useful.

![Two columns of the same twelve physics-problem cards. On the left, novices group by surface — pulley with pulley, incline with incline, spring with spring. On the right, experts regroup the same cards by deep principle — conservation of energy, Newton's second law, momentum. The cards are identical; the categories are different.](../images/07-math-and-stem-with-ai-fig-01.png)
![Chi, Feltovich & Glaser (1981). Twelve cards, two organizations; only one is available to the schema-bear](images/07-math-and-stem-with-ai-fig-01.png)
*Figure 7.1 — Chi, Feltovich & Glaser (1981). Twelve cards, two organizations; only one is available to the schema-bearer.*

A schema is that more abstract thing. It is a chunk of cognitive structure organized around the deep principle of a problem class, not around its cover story. It is what makes transfer possible. Without a schema for related rates, every new problem is a novel object — the kite problem and the ladder problem are just two different stories, and you cannot see that they are the same question in different costumes. With the schema, the kite problem is immediately recognizable as an instance of a type you already understand, and the solution path is visible before you write anything.

Schemas are not memorized. They are not given. They are constructed, one effortful problem at a time, by the cognitive work of looking at an unfamiliar surface and selecting and mapping the right principle to it.[^sweller1998] The selection event — "this is a Pythagorean constraint with two time-varying quantities" — is the schema-construction event. It is what happens inside your head when you draw the picture, name the variables, and write the constraint equation yourself.

When AI draws the picture, names the variables, and writes the constraint equation, the selection event is outsourced. The schema-construction event does not happen. The schema does not form.

![Two parallel paths starting from one problem statement. The top path passes through draw-the-picture, name-the-variables, and write-the-constraint and ends at a black box labelled schema forms. The bottom path goes through paste-into-AI, read-the-solution, and copy-into-notebook and ends at a dashed box labelled recognition memory only. The divergence point between the two paths is labelled the setup.](../images/07-math-and-stem-with-ai-fig-02.png)
![Two paths from one problem statement. The divergence point is the setup, and the cognitive work that buil](images/07-math-and-stem-with-ai-fig-02.png)
*Figure 7.2 — Two paths from one problem statement. The divergence point is the setup, and the cognitive work that builds the schema is exactly the work AI most readily replaces.*

This is what happened to Maya.

Maya is taking AP Calculus AB. She wants a 5. Related rates feels like the unit where AI most obviously saves time — every problem follows the same shape, the steps are numbered, the reasoning is explained. She has assigned every homework problem to ChatGPT for two weeks. Every solution comes back clean. She copies them into her notebook and feels, accurately, that she now has a clean notebook full of clean solutions.

Then the unit test arrives.

The first problem is a kite released at 200 feet above the ground; a horizontal wind pulls the kite away at 5 ft/s; the string is 250 feet long at the instant in question. How fast is the kite descending? Maya stares at the page. She knows it is a related rates problem. She does not know how to draw it. Should the 200 feet be a vertical leg? Should the 250 feet be the hypotenuse? What is the variable for the horizontal distance — is that something she chooses, or is that what the wind speed refers to? She has watched AI label diagrams a hundred times. She has never labeled one herself. Two minutes pass. She skips it.

After the test she opens ChatGPT and types the problem. The solution arrives in twelve seconds: draw a right triangle with vertical leg 200, horizontal leg $x$, hypotenuse $z$; the Pythagorean constraint is $x^2 + 200^2 = z^2$; differentiate implicitly; at $z = 250$, $x = 150$; plug in $dx/dt = 5$; solve. Maya reads it and feels, again accurately, that she understands every step.

She did understand every step. The trouble is that the exam was not testing whether she could understand a solution. It was testing whether she could produce one. The setup was the skill. AI had been eating it every night for two weeks. She had been keeping the parts she thought were hard — reading and understanding — and discarding the part she thought was easy — the setup. The exam revealed the inversion.

---

## The Bastani Numbers, Specifically for Math

The Bastani study has been cited throughout this book. In this chapter it is most directly relevant, because it was run on math students.

Nearly a thousand 9th–11th-grade students at a Turkish high school were randomly assigned to three conditions during math practice: no AI (control), standard GPT-4 freely available (GPT Base), or GPT-4 configured as a teacher-designed tutor that gave hints but withheld answers (GPT Tutor). Then all three groups took the same unassisted exam.[^bastani2025]

GPT Base students scored 48% higher during practice. On the unassisted exam, they scored **17 percentage points below the control group**. GPT Tutor students performed at roughly control level — no loss, no gain.

Two numbers from the supplementary materials are worth knowing precisely. In the GPT Base arm, **67% of students' first interactions** with the model were either re-pasting the problem or directly requesting the answer. They were not using the tool as a tutor. They were using it as a solver. And GPT-4 produced logical or arithmetic errors in **49% of the math problems** in the study. The students who had offloaded their critical evaluation copied those errors directly into their work. They had no schema with which to catch them.

![Grouped bar chart comparing three conditions across practice and unassisted exam scores. GPT Base has the highest practice score and the lowest exam score, with a labelled 17-point drop between them. GPT Tutor and Control hold roughly level between practice and exam.](../images/07-math-and-stem-with-ai-fig-03.png)
![Bastani et al. (2025), math arm. Practice gains do not transfer to unassisted performance when the model ](images/07-math-and-stem-with-ai-fig-03.png)
*Figure 7.3 — Bastani et al. (2025), math arm. Practice gains do not transfer to unassisted performance when the model is doing the schema work.*

A common objection at this point: frontier reasoning models are much better at math than the 2024 GPT-4 base model studied in Bastani. True. They score substantially higher on AMC problems, AIME problems, competition math benchmarks. The raw capability has improved dramatically.

This does not rescue you. The Bastani mechanism is not about model accuracy. It is about what happens in your head when AI does the work. Even if a frontier model hits 99% on standard math problems, the student who copies its solutions does not build the schema. The model gets better. The student's ability to catch the remaining 1% stays where it was — or deteriorates further, because the schema that would catch errors is the same schema that AI use prevents from forming. The Lee et al. (2025) finding from Chapter 2 applies here with particular sharpness: higher confidence in AI predicts lower critical thinking, and lower critical thinking means the fluent errors that remain are invisible.[^lee2025] The gap between model capability and student verification capacity *widens* with each model release. You cannot trust what you have not built.

---

## The Human-Only Zone

The phase gate for math is more precise than the general gate from Chapter 4 because math gives us a clean test for what counts as schema-bearing work. The test is: *if I removed AI and gave you the same problem cold tomorrow, could you reproduce this move?* Whatever requires genuine thinking to produce — that is in the Human-Only Zone. Whatever is mechanical once that thinking is done — that is where AI can help.

For nearly every problem in AP Calculus, AP Chemistry, AP Physics, college math, and engineering coursework, the Human-Only Zone contains the same four moves.

**The picture.** Drawing or imagining the geometric situation. The right triangle with its legs and hypotenuse. The reaction arrow with reactants and products. The block on the incline with every force as a labeled arrow in the right direction. The picture is the schema's external scaffold. Once it is wrong, everything downstream is wrong. Maya had watched AI draw pictures a hundred times. She could not draw one herself. That is a schema gap, not a drawing gap.

**The variables.** Naming the changing quantities and the constants. *Let $x$ be the horizontal distance from the point directly below the kite to Maya's hand. Let $y$ be the kite's height. Let $z$ be the length of the string.* This step looks trivial and is not. Choosing $x$ as the horizontal distance rather than the wind speed commits you to a coordinate system that makes the constraint equation tractable. Students who skip variable definitions do not skip them because the step is easy; they skip them because they have never had to make the choice themselves. Making the choice is the schema-construction event.

**The constraint equation.** The relationship that holds at every instant, not just the one being asked about. For Maya: $x^2 + 200^2 = z^2$. The 200 is constant — fixed by the problem. The $x$ and $z$ are functions of time; both are changing. The cognitive event here is the recognition that the wind-driven horizontal motion and the string-length growth are linked by Pythagoras. Without that recognition there is nothing to differentiate. AI performing this recognition means you never have it.

**The first attempt at each subsequent step.** Differentiating implicitly. Plugging in the given rate. Solving for the unknown rate. Each of these has a moment where you make a substep-level decision: *do I substitute $z = 250$ before or after I differentiate?* (After. Always after. $z$ is a function of time, not a constant.) That decision is where schema lives. If AI makes it, the schema does not get built.

The rule is: **complete all four moves on paper, without consulting AI, before any prompt is typed.** Not "mostly." Not "until I get stuck." All four. The temptation to type "is my setup right so far?" mid-stream is the most common gate violation in math and the most damaging, because the moment you ask is the moment you offload the strategic doubt that was about to drive your next decision.

The common objection: *"The harder problems require AI help with the setup — they're beyond me."* They are not beyond you. They are at the edge of what your current schema can handle, which is exactly where the schema-construction event needs to happen. If a problem is so far beyond you that you cannot make any move at all, the right response is to drop one level — find an easier isomorphic problem, build the schema there, climb back. The wrong response is to bring AI in to do the schema work. One builds capacity; the other builds the appearance of capacity, which is what produces the 17-point exam gap.

---

## When the Gate Opens

Once the Human-Only Zone has done its work, AI becomes genuinely useful for three things, and three things only.

**Substep-level hints.** Kurt VanLehn's 2011 meta-analysis of tutoring systems classified tutoring by granularity: answer-based systems (the tutor sees only your final answer, effect size $d \approx 0.31$ against no-tutoring controls), step-based systems (the tutor sees each step, $d \approx 0.76$), and substep-based systems (the tutor asks probing questions within each step, approximately $d \approx 0.40$).[^vanlehn2011] The popular claim that substep-based systems hit $d > 1.0$ was the field's *prediction* before VanLehn ran the numbers; the data did not support it. The robust finding is simpler: step-based tutoring decisively outperforms answer-based tutoring; asking "what is the answer?" puts you in the $d \approx 0.31$ regime; asking "given my setup, ask me one question about the next decision" puts you in the $d \approx 0.76$ regime. That is the regime where real learning happens.

**Arithmetic verification.** Once you have set up the problem, differentiated, and produced a candidate answer independently, AI can check the arithmetic. This is specific and narrow: *given my complete, independently-produced setup and solution, does the arithmetic work?* It is not *"is my setup right?"* — that is the slippery slope that ends with AI doing the setup. Arithmetic verification, after the setup is complete and independent, is what calculators have always been for.

**Isomorphic practice generation.** This is the strongest positive case for AI in math, and the most underused. The cognitive-load literature is clear that schemas develop through surface variation — encountering the same deep structure in many different covers.[^sweller1985] Twenty related-rates problems about ladders teach you ladder problems. Twenty problems spanning ladders, kites, cones, melting ice cubes, expanding balloons, draining tanks, walking shadows, and currency-conversion-rate problems teach you *related rates*. Generating that variety by hand is laborious; textbooks rarely include enough of it; AI produces it in seconds. This is the AI use the cognitive-load literature most directly supports.

**Table 7.1 — The phase gate for math.** The Human-Only Zone is everything that builds the schema. The AI-on Zone is everything that mechanizes once the schema has done its work.

| Step in the math workflow      | Human-Only Zone (gate closed)                                | AI-on Zone (gate open)                                                |
|--------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------|
| Picture / diagram              | Drawing the geometry; labelling the constraint visually     | —                                                                     |
| Variable definitions           | Choosing $x$, $y$, $z$; committing to a coordinate system   | —                                                                     |
| Constraint equation            | Recognizing the Pythagorean / similar-triangle / rate link  | —                                                                     |
| First attempt at each step     | Differentiate; substitute; solve — student moves first      | —                                                                     |
| Substep decisions              | "Substitute $z=250$ before or after differentiating?" — you | —                                                                     |
| Substep-level hint when stuck  | —                                                            | One conceptual question, after Prompt 1, when the stuck point is named |
| Arithmetic verification        | —                                                            | After a complete independent solution; check arithmetic only           |
| Isomorphic practice generation | —                                                            | Generate surface-varied problems sharing the deep structure            |

The gate trigger to rehearse before every homework session: **"Have I done the setup? Have I attempted the next step? Can I name what I am stuck on?"** Three yeses and the gate opens. Anything less and the tab stays closed.

![Three-question decision tree. Each question on the right branches sideways to a prominent black "close the tab" box on a no answer and continues downward on a yes answer. After three yeses the path narrows to a single "open AI with Prompt 1" node. A side panel explains why the close-the-tab branches dominate by design.](../images/07-math-and-stem-with-ai-fig-04.png)
![The gate trigger. Three close-the-tab boxes, one open-AI box. The proportion is the design, not the failu](images/07-math-and-stem-with-ai-fig-04.png)
*Figure 7.4 — The gate trigger. Three close-the-tab boxes, one open-AI box. The proportion is the design, not the failure mode.*

---

## The Hallucination Problem Is a Schema Problem

Math hallucinations are unusually toxic, for three reasons that compound each other.

First, they look correct to a student who does not yet have the schema, because the prose around them is fluent and the solution's structure mimics every solution the student has ever seen. The fluency is not a signal of accuracy. It is a feature of language models operating on well-represented training data. A math error in step 3 produces a wrong-but-internally-consistent step 4 and step 5 and final answer, with no surface disruption that anything went wrong.

Second, they propagate deterministically. There is no graceful degradation. The error compounds through every downstream step and arrives at a final answer that is confident, cleanly formatted, and wrong.

Third — and this is the part that matters most — the diagnostic for a math error is exactly the verification step the student offloaded. The way you catch a wrong answer in a math derivation is by having a schema that generates an internal prediction the wrong answer contradicts. *This answer should be smaller than the input rate, because the hypotenuse grows more slowly than the leg.* That internal check is schema-based. The student who has built the schema catches the error. The student who borrowed the schema cannot.

A concrete instance: a student asks AI to evaluate $\int \sec^3(x)\,dx$. The classical move is integration by parts with $u = \sec(x)$ and $dv = \sec^2(x)\,dx$, producing a recursive identity that must be solved algebraically — you add the original integral back to both sides and divide by 2. The divide-by-2 step is the one that drops the factor of $\frac{1}{2}$ that everyone forgets. AI returns a plausible-looking three-line solution that omits this step; the final answer is off by a factor of 2. The student who has worked through the derivation once knows exactly where the $\frac{1}{2}$ comes from. The student who has only read solutions finds no error to flag, because the visible algebra is internally consistent. On the exam the problem appears with limits — a definite integral — and the missing factor of 2 produces a numerical answer that is exactly twice what it should be. There is no recovery without the schema.

![Two parallel chains. The top chain — with schema — moves from "schema is built" to "prediction generated" to "AI output compared" to a filled black box reading "error caught." The bottom chain — without schema — moves through "no schema built," "no prediction generated," and "AI output read fluently" to a dashed box reading "fluent error passes." A callout marks the bottom branch as where the 49% of Bastani math errors lands.](../images/07-math-and-stem-with-ai-fig-05.png)
![The schema is the verification organ. An internal prediction is what the wrong step can disagree with; wi](images/07-math-and-stem-with-ai-fig-05.png)
*Figure 7.5 — The schema is the verification organ. An internal prediction is what the wrong step can disagree with; without one, fluent errors pass undetected.*

![Two derivations side by side. The left panel shows the correct integration of sec cubed x by parts, with the divide-by-two step highlighted; the final answer carries the factor of one-half. The right panel shows the AI hallucinated version with the addition step quietly skipped and a dashed box marking the missing divide-by-two step; the final answer is presented in white on black, verdict "off by a factor of two."](../images/07-math-and-stem-with-ai-fig-06.png)
![Both look like correct mathematics until you know where the ½ lives. The schema is what locates the missi](images/07-math-and-stem-with-ai-fig-06.png)
*Figure 7.6 — Both look like correct mathematics until you know where the ½ lives. The schema is what locates the missing step.*

The misconception to retire: *"frontier models are accurate enough now that the hallucination problem is solved."* The model accuracy improved. Your verification capacity did not — and in fact, under conditions of high AI use, it has likely atrophied. The residual errors that remain in current models are, almost by selection, the ones that look most plausible. They are the fluent errors, the ones that require a schema to catch. The student who has been borrowing schema from AI is the student least equipped to catch the errors that current models still make. The gap widens.

---

## Maya Redoes the Problem

A week after the unit test, Maya tries again with the workflow. Same deep structure, different surface: a hot-air balloon rises vertically at 8 ft/s; an observer stands 100 feet from the launch point; how fast is the distance between the observer and the balloon increasing when the balloon is 60 feet high?

AI is off. Maya draws a right triangle on paper. The horizontal leg is the fixed 100 feet between the observer and the launch point — she writes "100 ft, constant" next to it. The vertical leg she labels $y$, with "$y$ = height of balloon, function of $t$." The hypotenuse is $z$, "$z$ = distance from observer to balloon, function of $t$." She writes the constraint: $100^2 + y^2 = z^2$. She differentiates implicitly:

$$2y\,\frac{dy}{dt} = 2z\,\frac{dz}{dt}$$

She is solving for $\frac{dz}{dt}$ at the instant $y = 60$. She needs $z$ at that instant: $z = \sqrt{100^2 + 60^2} = \sqrt{13600} \approx 116.6$ ft. She has $\frac{dy}{dt} = 8$ ft/s. She solves:

$$\frac{dz}{dt} = \frac{y}{z}\cdot\frac{dy}{dt} = \frac{60}{116.6}\cdot 8 \approx 4.12\text{ ft/s}$$

She has a candidate answer. She wants to verify the arithmetic, not the setup. She opens ChatGPT:

*I solved this problem independently and got $\frac{dz}{dt} \approx 4.12$ ft/s when $y = 60$, given $\frac{dy}{dt} = 8$ ft/s and the constraint $100^2 + y^2 = z^2$. Verify my arithmetic only. Do not re-derive the setup.*

ChatGPT confirms. AI closes.

Maya writes one sentence in her notebook: *"Makes sense — the horizontal distance is fixed, so $z$ always grows slower than $y$, because the same vertical rise gets spread over a longer diagonal."* That sentence is her schema rebuilding itself in plain English. It is a sentence she could not have written before the unit test.

![Right triangle drawn from Maya's balloon problem. The horizontal leg from the launch point to the observer is dashed and labelled 100 ft, constant. The solid vertical leg rises from launch to a small balloon at the top, labelled y, height of balloon, function of t. The solid hypotenuse connects the balloon to the observer, labelled z. Arrows mark dy/dt = 8 ft/s along the vertical and dz/dt along the hypotenuse. A side panel records the constraint, the differentiated form, the substitution at y = 60, and the answer dz/dt ≈ 4.12 ft/s.](../images/07-math-and-stem-with-ai-fig-07.png)
![The diagram is the schema's external form. Drawing it is not decoration; it is the cognitive event.](images/07-math-and-stem-with-ai-fig-07.png)
*Figure 7.7 — The diagram is the schema's external form. Drawing it is not decoration; it is the cognitive event.*

Then she opens ChatGPT again for surface variation:

*Generate 6 related-rates problems with the same deep structure — two quantities related by Pythagoras, both changing in time, find the rate of the hypotenuse or a leg at a specific instant. Vary the scenarios: include geometries beyond ladder problems. Present one at a time. After I attempt each on paper and give my answer, just say "correct" or "incorrect." Do not explain.*

She works through six problems over 90 minutes. By the third she is no longer drawing the diagram as a deliberate effort — the picture is forming reflexively. By the sixth she recognizes the deep structure within the first ten seconds of reading the problem statement.

AI did three things in this session: confirmed arithmetic, generated varied practice, and waited. AI did not draw the picture. AI did not name the variables. AI did not write the constraint. AI did not differentiate. The four schema-bearing moves stayed on Maya's paper, under Maya's hand — the only place they could stay.

---

## Three Prompts

These are the sanctioned prompts for math. Each maps to one of the three AI-on uses. Copy them. Adapt the bracketed contents.

### Prompt 1 — The Substep Hint

Use when you have completed the setup, attempted the next step, and can name the specific decision you cannot make.

```
I'm working on: [paste problem statement].

My setup:
- Diagram: [describe in words]
- Variables: [list with units]
- Constraint equation: [write it]
- My attempt at the next step: [show work]
- Stuck point: [name the specific substep decision]

Do NOT give me the answer.
Do NOT write the next equation.
Do NOT tell me what technique to use.
Ask me ONE conceptual question about the decision I cannot make.
After I answer, do not give me the right answer if I was wrong — ask a follow-up.
```

Good output: a single question that points at the strategic choice, not the procedural next move. For Maya's kite problem: *"When you substitute $z = 250$, are you describing $z$ at all instants or at one specific instant? What does that tell you about whether you can substitute before differentiating?"* That question makes Maya generate the schema-bearing distinction herself.

Bad output: a hint that is really an answer in disguise — *"remember to plug in after differentiating, because $z$ is a function of time."* Recovery: *"Don't tell me what to do. Ask me a question about why one ordering would be wrong. Force me to generate the reasoning."*

### Prompt 2 — The Isomorphic Practice Generator

Use after you have rough-formed a schema and want to surface-vary it into durability.

```
Deep structure I am internalizing: [1–2 sentences — e.g., "two quantities related by a Pythagorean constraint, both changing in time, find the rate of one given the rate of the other at a specific instant"].

Generate 8 problems with this structure. Vary the surface as much as possible:
- At least 3 different geometries (right triangle, cone, sphere, similar triangles, rectangle).
- Vary which rate is given and which is sought.
- At least one problem where the constraint involves a fixed ratio rather than a fixed sum.
- At least one problem from a non-physical domain (currency, biology, chemistry).

Do NOT solve any of them. Present problem 1 only.
After I give you my answer, say "correct" or "incorrect" — no explanation.
Then present problem 2.
```

Good output: genuinely varied problems that share the deep structure. Bad output: eight variations on "ladder against a wall." Recovery: *"These share too much surface. Vary the geometry. Vary the domain. Keep only the deep structure identical."*

### Prompt 3 — The Derivation Explainer (Socratic mode)

Use when you have applied a formula procedurally and want to understand why it works — as a derivation you can rebuild, not a recipe you memorize.

```
Explain why [formula or theorem] works, starting from first principles.
Do not give me the formula and show me how to use it.
Give me the derivation that produces it. Name the load-bearing assumptions.

Structure:
1. Give me ONE conceptual step.
2. Stop and ask me to predict the next step.
3. I attempt it. You evaluate, then give the actual step — right or wrong.
4. Repeat until complete.
At the end: ask me what would change if one of the load-bearing assumptions were relaxed.
```

Bad output: the full derivation in three paragraphs. Recovery: *"Stop after the first step. Ask me what comes next. I predict; you evaluate; then continue."*

---

## The Math Self-Test

Before any high-stakes math moment — unit test, AP exam, calc final, engineering placement — you owe yourself this verification. Solve a structurally parallel problem, unassisted, under timed, closed-book conditions.

How to run it: identify the schema you are testing (specific and narrow — not "related rates" but "two Pythagorean quantities both changing in time"). Use Prompt 2 to generate a parallel problem with a surface you have not seen. Set it aside. Set the timer to match what the actual exam allows. Close everything. Pen on paper. When the timer runs out, stop.

Then compare. There are three categories of gap and they require different responses.

**Schema gap.** You did not know how to set up the problem. The picture did not come. The constraint equation did not surface. This is the most serious gap and the one AI-as-bypass most reliably produces. The fix is not to study more solutions. The fix is more independent setups on isomorphic problems until the picture forms reflexively. Prompt 2 generates them.

**Procedural gap.** You set up correctly and got stuck on a specific step — couldn't apply the chain rule cleanly, couldn't solve the algebra. This is a genuine practice gap and easier to close. Do 5–10 isomorphic problems focused on that specific step.

**Arithmetic gap.** Your setup and strategic moves were right; you dropped a sign or miscomputed. This is the least serious gap. Deliberate practice with Prompt 1's arithmetic-verification mode is the routine fix.

If you cannot complete the problem in 1.5× the allotted time, the schema is not there. Do not move on to harder material. Repeat the cycle on easier isomorphic problems. Retest in three days.

![Decision tree starting from the question "Can you do the setup cold?" The no branch goes left into a prominent filled-black box marked Schema gap, which feeds down into a fix node prescribing more independent setups on easier isomorphic problems using Prompt 2. The yes branch goes right into a sub-question that splits into Procedural gap and Arithmetic gap, each with its own fix. A bottom strip states the 1.5× rule: if you cannot complete the problem in 1.5× the allotted time, the schema is not there.](../images/07-math-and-stem-with-ai-fig-08.png)
![Three gaps, three responses. The schema branch is widest because that is the gap AI use most reliably pro](images/07-math-and-stem-with-ai-fig-08.png)
*Figure 7.8 — Three gaps, three responses. The schema branch is widest because that is the gap AI use most reliably produces.*

---

## LLM Exercises

**LLM Exercise 1 — The Substep Interrogation (Apply).**
Take a problem at the edge of your current capability. Complete the setup yourself — diagram, variables, constraint — then attempt the next step and get genuinely stuck. Use Prompt 1 verbatim. After AI asks its question, answer from your head before continuing. At the end, write down: *which of the questions AI asked could I now ask myself on a new problem?* Those internalized questions are the schema-bearing moves you have acquired.

**LLM Exercise 2 — The Isomorphic Week (Apply → Synthesize).**
Pick one schema — narrow, specific, like "stoichiometry with limiting reagents in precipitation reactions" or "force diagrams on inclines with kinetic friction." Use Prompt 2 to generate eight surface-varied problems. Work one per day, timed, AI closed during the setup. At the end of the week, write one paragraph: what changed between problem 1 and problem 8? Where did the setup start to feel reflexive? That transition is schema formation made visible.

**LLM Exercise 3 — The Derivation Rebuild (Analyze).**
Pick a formula you have applied many times but cannot currently derive from scratch: the quadratic formula, implicit differentiation, the ideal gas law, Henderson-Hasselbalch. Use Prompt 3. After the Socratic exchange is complete, close the conversation. On blank paper, without reviewing, rebuild the derivation yourself in full. If you cannot, the Socratic exchange did not produce storage strength. Return to the derivation from scratch — not the conversation — and try again.

---

## What Would Change My Mind

If a well-designed RCT, larger than Bastani and run on contemporary frontier reasoning models with a multi-month follow-up, showed that students who used AI freely during math practice performed equivalently on unassisted exams to students who used AI only after independent setup attempts — that would weaken this chapter's central claim. The mechanism (schema construction requires the student to perform the identification-layer work) is robust across the cognitive-science literature. But if the longitudinal performance pattern did not appear at all with current models, I would have to revise the strong version of the argument and concede that contemporary AI may be approaching the $d \approx 0.76$ step-based regime even under free use. I do not expect this result. I would update on it if it appeared.

---

## Still Puzzling

Whether AI-generated isomorphic practice problems are pedagogically equivalent to teacher-curated ones is not directly studied. The surface-variation principle is well-established; whether AI generates the right *kind* of variation reliably is not. AI sometimes generates problems that share only surface features and not deep structure, or varies the surface trivially. The chapter advocates the use; the empirical case is reasoned from cognitive load theory, not directly tested.

I also do not know how much of the Bastani finding generalizes beyond high-school students to college calculus or upper-division engineering. The mechanism should generalize — schema construction is the same biological process — but the magnitude of the effect under different populations, problem difficulties, and time horizons is an open empirical question. Treat the 17-point decrement as a directional warning, not a precise prediction for your own case.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **George Pólya (1887–1985)** spent a career arguing that mathematical thinking is a teachable process — not a gift you have or don't. His *How to Solve It* (1945) compressed the process into four moves: **understand the problem, devise a plan, carry out the plan, look back.** Read that list next to this chapter's Human-Only Zone and the resemblance is exact. *Understand* is the picture and the variables. *Devise a plan* is the constraint equation and the strategic substep decision. *Carry out the plan* is the differentiation and the algebra. *Look back* is the schema check — *should this answer be larger or smaller than the input rate?* Pólya's heuristics were a curriculum for the schema-construction event before anyone had called it that. The temptation to outsource any one of them to AI is a temptation Pólya would have recognized as the bypass of the whole.

![George Pólya, circa 1955. AI-generated portrait based on a public domain photograph.](../images/george-polya.jpg)
*George Pólya, circa 1955. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

![George Pólya (1887–1985)](../images/george-plya-977.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was George Pólya, and how do the four moves in How to Solve It (1945) — understand, plan, execute, look back — map onto the math/AI workflow in this chapter (picture, variables, constraint, first attempt; substep hint, arithmetic verification, isomorphic practice)? Where does AI use most directly threaten each Pólya move, and which of the four does it threaten worst? Keep it to three paragraphs. End with the single most surprising thing about Pólya's career or ideas.
```

→ Search **"George Pólya"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to rewrite one of Pólya's worked examples from *How to Solve It* as a related-rates problem, then walk you through which moves AI must not touch.
- Ask it about Pólya's later book *Mathematics and Plausible Reasoning* — and how its account of inductive guesswork relates to the schema-as-prediction framing in this chapter.

What changes? What gets better? What gets worse?

---

## Bridge to Chapter 8

The math chapter operationalized the phase gate at the highest mechanical precision in the book — coordinate systems, variable definitions, constraint equations, substep granularity. The setup is the schema-bearing move; AI must not do it. The next chapter applies the same logic to writing, where the schema-bearing move is *the thesis* and the seductive failure mode is AI drafting a paragraph that reads better than yours. The cognitive economy is identical. The Human-Only Zone is different. Chapter 8 builds the gate for argument.

---

**Tags:** #math #stem #schema #phase-gate #bastani #vanlehn #sweller #chi #isomorphic-practice #human-only-zone

---

## Footnotes

[^chi1981]: Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science*, 5(2), 121–152. <https://doi.org/10.1207/s15516709cog0502_2>

[^sweller1998]: Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review*, 10(3), 251–296.

[^bastani2025]: Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122. <https://doi.org/10.1073/pnas.2422633122> (Correction: <https://doi.org/10.1073/pnas.2518204122>.)

[^lee2025]: Lee, H.-P., Sarkat, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking. *CHI '25*. <https://doi.org/10.1145/3706598.3713778>

[^sweller1985]: Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction*, 2(1), 59–89.

[^vanlehn2011]: VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221. <https://doi.org/10.1080/00461520.2011.611369>

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 7.1 — Chi, Feltovich & Glaser (1981). Twelve cards, two organizations; only one is available to the schema-bear

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Chi, Feltovich & Glaser (1981). Twelve cards, two organizations; only one is available to the schema-bear". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-01.html`

---

### Figure 7.2 — Two paths from one problem statement. The divergence point is the setup, and the cognitive work that buil

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "Two paths from one problem statement. The divergence point is the setup, and the cognitive work that buil". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-02.html`

---

### Figure 7.3 — Bastani et al. (2025), math arm. Practice gains do not transfer to unassisted performance when the model 

Create a standalone D3 v7 HTML file for a concept map titled "Bastani et al. (2025), math arm. Practice gains do not transfer to unassisted performance when the model ". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-03.html`

---

### Figure 7.4 — The gate trigger. Three close-the-tab boxes, one open-AI box. The proportion is the design, not the failu

Create a standalone D3 v7 HTML file for a phase-gate flow diagram titled "The gate trigger. Three close-the-tab boxes, one open-AI box. The proportion is the design, not the failu". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-04.html`

---

### Figure 7.5 — The schema is the verification organ. An internal prediction is what the wrong step can disagree with; wi

Create a standalone D3 v7 HTML file for a concept map titled "The schema is the verification organ. An internal prediction is what the wrong step can disagree with; wi". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-05.html`

---

### Figure 7.6 — Both look like correct mathematics until you know where the ½ lives. The schema is what locates the missi

Create a standalone D3 v7 HTML file for a concept map titled "Both look like correct mathematics until you know where the ½ lives. The schema is what locates the missi". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-06.html`

---

### Figure 7.7 — The diagram is the schema's external form. Drawing it is not decoration; it is the cognitive event.

Create a standalone D3 v7 HTML file for a concept map titled "The diagram is the schema's external form. Drawing it is not decoration; it is the cognitive event.". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-07.html`

---

### Figure 7.8 — Three gaps, three responses. The schema branch is widest because that is the gap AI use most reliably pro

Create a standalone D3 v7 HTML file for a bar or learning-curve chart titled "Three gaps, three responses. The schema branch is widest because that is the gap AI use most reliably pro". Use student AI-learning data or workflow states: attempt, AI scaffold, prediction, retrieval, transfer, and no-AI exam. Encode the primary risk or leverage point with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/07-math-and-stem-with-ai-fig-08.html`
