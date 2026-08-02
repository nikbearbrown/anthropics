# Chapter 4: Randomization and Its Limits


## TL;DR

- ═══════════════════════════════════════ FORMATTED VERSION (Markdown) ═══════════════════════════════════════.
- The chapter moves through Opening: The Oldest Trial I Know Of, Learning Objectives, Prerequisites, Why This Chapter Matters, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

═══════════════════════════════════════
FORMATTED VERSION (Markdown)
═══════════════════════════════════════

## Opening: The Oldest Trial I Know Of

About twenty-five hundred years ago, four young men refused to eat the king's meat.

They were captives — Jewish nobles brought from Jerusalem to Babylon after Nebuchadnezzar conquered the city. Part of their preparation for royal service was a three-year training program, and part of the training was a rich diet served from the king's table. One of the four, a young man named Daniel, objected to the food for religious reasons. He proposed a bargain to the king's steward: give him and his three companions vegetables and water for ten days, and at the end of the ten days, look at them. Compare them to the others. Let the steward's own eyes decide.

The steward agreed. After ten days, according to the first chapter of the Book of Daniel, the four vegetable-eaters "appeared fairer and fatter in flesh" than the young men who had been eating the king's meat. The steward kept them on the vegetable diet.

I want you to look at what Daniel built, because it's remarkable.

He had a treatment group — four men on vegetables. He had a control group — the other captives on meat. He had a pre-specified duration of ten days. He had an outcome measure — visible health. He had a decision rule agreed to in advance — whatever the steward saw, that would govern. That is a sophisticated piece of experimental thinking, and it is roughly twenty-four hundred years older than anything comparable in the scientific record.

Now look at what it's missing.

Daniel and his three companions were not randomly selected. They volunteered for the vegetable diet. More than that, they volunteered *because* they were religiously motivated, disciplined, and probably healthier to begin with than an average cross-section of the captives. If they looked better after ten days, how much of that was the diet and how much was the kind of people who volunteered for the diet? The text can't tell us. The trial cannot separate the effect of the treatment from the effect of who chose the treatment.

This is the problem a randomized controlled trial solves. It took humanity until the twentieth century to find the solution, and the solution is elegant enough that it deserves a whole chapter. The RCT is the cleanest tool we have for answering causal questions, and when it's available, it is the method of choice.

Most of the time, it isn't available. The rest of this book is about what you do in that case. But before you can understand the alternatives — matching, weighting, instrumental variables, counterfactual analysis — you have to understand exactly what the RCT does and exactly where it breaks. Otherwise you won't know whether your observational method succeeded or failed, because you won't know what success looks like.

### Learning Objectives

By the end of this chapter you should be able to:

1. **Explain**, in the language of causal diagrams, why randomization eliminates confounding — not by correcting for it but by deleting it from the structure.
2. **Identify** which causal questions can and cannot be answered by a randomized controlled trial, and name which category a new question falls into.
3. **Read** an RCT's design and locate the points where bias can still enter despite randomization.
4. **Distinguish** internal validity (certified by randomization) from external validity (not certified by anything).
5. **Analyze** a real RCT using the vocabulary of chains, forks, colliders, and paths from Chapter 2.
6. **Explain** why observational methods must exist — what the rest of this book has to accomplish that an RCT would handle by construction.

### Prerequisites

You should have worked through Chapters 1, 2, and 3. From Chapter 2 you need the diagrammatic vocabulary — nodes, arrows, back-door paths, d-separation. From Chapter 3 you need the concept of confounding as a structural problem, not a statistical one, and you need to know why "control for covariates in a regression" is not automatically causal reasoning.

### Why This Chapter Matters

Every observational method in the rest of this book is trying to approximate what an RCT does by construction. Matching tries to approximate it by conditioning. Instrumental variables try to approximate it by finding a natural lever. Counterfactual methods try to approximate it by modeling the comparison explicitly. If you don't know what the RCT is doing, you can't tell whether your observational surrogate is doing it well, badly, or at all.

---

## Concept 1: What Randomization Actually Does

The argument for randomization is usually given in statistical language: "randomization balances the treatment and control groups on average, so any differences in outcomes must be due to the treatment." That framing is true but weak. It makes randomization sound like a convenient statistical property — something that works in expectation, on average, with enough subjects, if the stars align.

The structural framing is stronger, and it is the one I want you to take from this chapter.

Randomization is a *surgical operation on the causal diagram*. It deletes every arrow that points into the treatment variable. Not balances them. Not corrects for them. Deletes them.

Let me show you what this means concretely.

### Worked Example: What the Diagram Looks Like Before and After

Suppose you want to know whether a new drug reduces blood pressure. In the real world, without an RCT, what causes who gets the drug? Many things. The patient's current blood pressure affects it — doctors prescribe the drug more often to sicker patients. Age affects it — some drugs are preferred in older or younger patients. Insurance coverage affects it. Patient preference affects it. The doctor's training affects it. Unmeasured things — genetic predisposition, lifestyle, compliance tendencies — affect it.

Call the drug *T* (treatment), blood pressure outcome *Y*, and use *X* as a catch-all for the web of things that affect who gets *T*. Some of those things also affect *Y* directly — sicker patients have worse outcomes regardless of treatment; older patients respond differently to the drug; unmeasured lifestyle factors affect blood pressure.

Here's the observational diagram:

<!-- FIGURE 4.1: A DAG with treatment T and outcome Y, plus a cloud of variables X (including age, current blood pressure, lifestyle, genetic factors, insurance, preference) with arrows going into both T and Y. Multiple back-door paths T ← X → Y run through every variable in X. Caption: Before randomization, every variable that affects who gets the drug and also affects the outcome creates a back-door path. Many of these variables are unmeasured. -->

Every variable in *X* creates a back-door path from *T* to *Y*. To identify the causal effect by conditioning, you would need to measure every relevant confounder and block every back-door path. Miss one, and your estimate is biased. And the deepest problem is that you don't know what you've missed. Unmeasured confounders are, by definition, the ones you haven't thought of.

Now run an RCT. The drug is assigned by a coin flip — or, more likely, by a random number generator tied to a subject ID. The arrows from *X* to *T* all disappear. Age doesn't affect who gets the drug anymore. Blood pressure doesn't. Insurance doesn't. Lifestyle doesn't. Not because these variables don't exist — they still exist, and they still affect *Y* — but because a coin flip does not consult them.

Here's the post-randomization diagram:

<!-- FIGURE 4.2: The same diagram after randomization. All arrows from X to T are deleted. X still has arrows to Y. T has a direct arrow to Y. No back-door paths remain. Caption: Randomization erases every arrow into the treatment variable. Every back-door path is gone — not adjusted for, gone. The only path from T to Y is the causal path T → Y. -->

Every back-door path required an arrow into *T*. There are no arrows into *T*. Therefore there are no back-door paths. Therefore there is no confounding. The only path from *T* to *Y* is the directed causal path.

Notice what this argument does not require. It does not require me to know what the confounders are. It does not require me to measure them. It does not require me to adjust for them. The randomization handles them all at once — the known, the unknown, and the unthought-of — because it intervenes on the assignment mechanism rather than on the confounders themselves.

This is the design philosophy of the RCT. It trades flexibility for guarantee. You cannot use an RCT to study anything where you don't control the treatment assignment — that's the flexibility you give up. In exchange, you get a structural guarantee that confounding is impossible, not just that you've corrected for it. That trade is the right one often enough that the RCT became the gold standard of causal evidence. It is not the right trade always, which is why we need the rest of this book.

### Why I'm Calling This "Structural"

I want to press on the language here because it matters.

When I say the arrows into *T* are "deleted," I am not speaking loosely. The observational distribution of *T* was produced by a data-generating process in which *X* caused *T*. The randomized distribution of *T* is produced by a different data-generating process, one in which a coin flip causes *T* and *X* does not. These are two different worlds. The second world is the one the experimenter creates on purpose. In the second world, the causal diagram relating *T* to *Y* genuinely does not have the arrows that the first world has.

This is different from "adjusting for X in a regression." Adjusting for *X* tries to remove the statistical effect of the back-door paths while leaving the arrows in place. It works if you've measured all the *X*'s. If you haven't, the paths you didn't close still run. Randomization doesn't close the paths; it deletes them. It works regardless of whether you know what they are.

That distinction — statistical correction versus structural intervention — is what makes the RCT qualitatively different from observational adjustment, not just quantitatively cleaner.

---

## Concept 2: Fisher, Rothamsted, and the Skillful Interrogation of Nature

I want to show you where this idea came from, because knowing the problem Fisher was actually solving makes the solution clearer.

Ronald Fisher was a statistical prodigy, a geneticist, and a famously combative scientific personality. He's worth mentioning with one piece of biographical honesty: he spent his later years arguing against the evidence that smoking causes cancer, and he was wrong about that. The man had blind spots. His contributions to experimental design, however, are foundational, and they survive his other mistakes.

In the 1920s, Fisher was working at the Rothamsted Experimental Station in England, the oldest agricultural research station in the world. His job was to help design and analyze experiments on crops — which fertilizer produces the best yield, which variety of wheat resists drought, which planting pattern survives pest infestations. The experiments at Rothamsted had historically been run the obvious way: apply treatment A to some plots and treatment B to others, harvest, weigh the output, compare.

The difficulty, which Fisher saw immediately, was that the plots weren't identical.

Some plots were on higher ground with better drainage. Some had been heavily fertilized in previous seasons and still carried the residue. Some had better sun exposure. Some had more clay in the soil, some more sand. If you applied fertilizer A to a good plot and fertilizer B to a bad plot, you were measuring a mixture — the fertilizer effect plus the plot effect — and you couldn't separate them after the fact. Whatever the yields told you, they told you about the combination, not the fertilizers alone.

Fisher's response was three techniques, which together define the modern experimental design. I want to walk through each because each one solves a specific problem.

### Randomization

Randomization is the core move. Assign each fertilizer to a random selection of plots. Don't put fertilizer A on the good plots; don't put fertilizer B on the bad plots; don't let the researcher's implicit theories about which fertilizer "should" work where drive the assignment. Let a random process do the assigning.

The argument for randomization is that it solves a problem no other method could solve: the problem of *unmeasured* plot differences. Fisher could not possibly measure everything that made one plot different from another. Soil chemistry, microbial composition, past history, water table depth, bird traffic — the list is endless. With non-random assignment, those unmeasured differences could systematically favor one fertilizer over another in ways nobody would notice. With random assignment, the unmeasured differences distributed evenly, in expectation, across all treatments. Whatever made one plot different, on average, was as likely to end up under fertilizer A as fertilizer B.

This is exactly the structural argument I gave above, transposed to 1920s agriculture. Fisher didn't have the diagrammatic language — Wright was publishing path diagrams in the same decade, but Fisher and Wright were not exactly friends, and Fisher did not adopt the graphical approach. But the logic of his argument is the logic of deleting arrows into *T*.

### Replication

Randomization handles confounding on average. It does not handle noise. Any single plot has its own individual noise — a passing storm, a gopher invasion, an accidentally trampled row. If you only had one plot per treatment, the noise could swamp the signal.

Fisher's answer was to replicate. Run many plots of each treatment. Average across them. The plot-level noise averages out, leaving the treatment effect visible against a smaller residual.

Replication is not a fix for confounding. It is a fix for *precision*. Randomization without replication gives you unbiased but imprecise estimates — the right answer in expectation, but possibly far off in any single experiment. Replication tightens the interval around the estimate.

### Blocking

Blocking is the clever move that adds efficiency without sacrificing randomization.

Fisher observed that plot-level variation wasn't random — it was structured. Nearby plots were similar to each other. Plots on the same side of the field were similar. So instead of randomizing across all plots, Fisher proposed organizing plots into *blocks* of similar quality, then randomizing within each block.

A block might be a contiguous strip of land with similar soil and drainage. Inside the block, each fertilizer is applied to one plot, selected randomly. Across blocks, every fertilizer appears in every block. When you analyze the data, you can remove block-level variation — which doesn't tell you anything about fertilizers anyway — and focus on the within-block comparisons, where the fertilizers are competing on similar ground.

Blocking is efficient because it reduces the noise against which the treatment effect must be detected. It preserves randomization because within each block, assignment is random. And it handles an important class of confounders — the ones that cluster spatially or temporally — without needing to name them.

### The Skillful Interrogation of Nature

Fisher's daughter, Joan Fisher Box, later wrote his biography, and the phrase I remember from it is that her father saw experimental design as "the skillful interrogation of nature." The idea is that nature answers whatever question you ask, but only the exact question you ask. If you ask a confused question — one that mixes fertilizer with plot quality — you get a confused answer. Nature does not do you the favor of interpreting what you meant.

Randomization is the technique for asking the question you actually want to ask. When fertilizer assignment is random, you are asking: "if fertilizer choice were unrelated to plot quality, what would the yields be?" And that is the causal question. Nature obliges.

The streptomycin trial in 1948 — the Medical Research Council's test of streptomycin for pulmonary tuberculosis — is usually cited as the first modern randomized controlled trial in medicine. The MRC made a deliberate choice to randomize rather than let physicians assign treatment by clinical judgment. The trial produced a clean result: streptomycin worked. The design Fisher invented for crops migrated to medicine, and it has been the regulatory gold standard ever since.

Here's the MKBHD-style evaluation of Fisher's design choice: he optimized hard for robustness against unknown confounding and accepted the cost, which is that you have to be able to control the assignment mechanism. In agricultural research that cost is usually acceptable; you can randomize plots. In medicine that cost is sometimes acceptable; you can randomize patients when the ethics are clear. In economics, politics, history, and the study of human life choices, that cost is usually prohibitive. Fisher's design doesn't fail on those questions — it simply doesn't apply. That is the trade the RCT makes. It is an enormously good trade when the trade is available.

---

## Concept 3: The Limits

So the RCT is structurally superior to observational methods when both are available. Why isn't it always available? The limits sort into three categories, and I want to name each one clearly because the rest of the book is organized around them.

### Limit 1: You Can't Randomize It (Impossibility)

Some treatments cannot be randomized because assigning them would be unethical, impossible, or meaningless.

**Ethical impossibility.** You cannot randomize people to behaviors or exposures that might harm them. You cannot assign people to smoke for twenty years to see if smoking causes cancer. You cannot assign pregnant women to drink during pregnancy. You cannot assign children to lead-paint exposure. These aren't hypothetical objections — they are the actual reason that most of epidemiology, occupational health, and environmental science runs on observational data. Every causal claim in those fields is an observational claim, because the ethical constraints don't allow the experiment that would settle it.

**Practical impossibility.** You cannot randomize countries to different monetary policies. You cannot randomize cities to different crime rates. You cannot randomize the Industrial Revolution. Some treatments are too large, too diffuse, or too tied to history to be assignable by any experimenter. When the unit of analysis is a country or an era, random assignment is not on the table.

**Structural impossibility.** Some "treatments" aren't coherent as assignable interventions. You cannot randomize people to be different ages. You cannot randomize them to different genders, different races, different native languages. These are not treatments; they are characteristics. The concept of an RCT on race does not make sense, because the proposed intervention — "assign this person to be a different race" — does not correspond to any actual operation.

The first big chunk of causal questions that motivate this book — does smoking cause cancer, does air pollution cause asthma, do class sizes affect learning — falls into this category. You will not randomize them. The rest of this book exists because of this category.

### Limit 2: You Randomized But Things Got Messy (Execution)

Even when an RCT is possible in principle, real human behavior contaminates the design in predictable ways.

**Non-compliance.** You randomized Alice to the drug arm. Alice does not take the drug. You randomized Bob to the placebo arm. Bob obtains the drug elsewhere and takes it. When you analyze the data, are Alice and Bob in the arms they were assigned to or the arms they actually experienced?

This matters more than it sounds. If you analyze by assignment — the *intent-to-treat* analysis — you are estimating the effect of *being offered* the treatment, not the effect of actually taking it. That's a different number. If you analyze by what actually happened — the *per-protocol* analysis — you have broken the randomization, because the people who took the drug and the people who didn't may differ for reasons that also affect the outcome. Compliance is itself a trait; analyzing by compliance reintroduces the selection you were trying to avoid.

The honest answer in practice is to report both, and to use instrumental variables methods (which Chapter 7 covers) to estimate the effect of actual treatment receipt on the subgroup that complied with assignment. This gives you something called the Local Average Treatment Effect, the LATE, which is the causal effect on compliers — not on everyone, but on the people whose treatment was determined by the randomization. We'll develop this formally later.

**Blinding failures.** If patients know which arm they're in, they may behave differently in ways that affect the outcome. If doctors know which arm their patient is in, they may treat the patient differently, monitor more carefully, or report symptoms differently. A well-run trial blinds both — a double-blind design — using placebos indistinguishable from the active treatment. This works well for pills. It works poorly for surgeries, devices, and behavioral interventions, where blinding is often impossible. When blinding fails or isn't feasible, the design has to use objective outcomes (mortality, lab values) that aren't subject to judgment bias, or accept some contamination.

**Dropout.** Subjects leave the trial before it ends. If dropout is random, fine — you lose precision. If dropout correlates with outcome — if people who feel worse drop out of the drug arm and people who feel fine drop out of the placebo arm — you've broken the randomization, because the comparison now reflects who stayed rather than who was assigned. Good trials track dropout aggressively and run sensitivity analyses assuming different patterns of missingness.

None of these execution problems invalidates randomization as a concept. But every real RCT has them to some degree, and the quality of a real trial is partly about how honestly it handles them.

### Limit 3: The RCT Answered a Different Question Than You Think (External Validity)

This is the RCT's deepest limitation, and the one I want you to take most seriously, because it doesn't go away with better trial design.

An RCT estimates the causal effect *in the population of subjects who were actually in the trial*. Those subjects volunteered. They passed the inclusion criteria. They consented to the protocol. They showed up. They are, in most trials, systematically different from the population that will actually receive the treatment in practice.

Clinical trials often exclude: patients over 75, patients under 18, pregnant women, patients with kidney problems, patients on other medications, patients with any comorbidity the sponsor worries about. Those exclusions produce a clean trial population — low heterogeneity, predictable responses, cooperative subjects. They also produce a trial population that doesn't look like the people who will take the drug in the real world.

The RCT's internal validity — the trustworthiness of the causal conclusion *within the trial population* — is certified by randomization. Its *external validity* — the applicability of that conclusion to other populations — is certified by nothing. It requires judgment. It requires follow-up studies. It requires, in many cases, years of post-marketing surveillance to find out what happens when the drug hits the messier world outside the trial.

This is the trade the RCT makes, and it is the one MKBHD-style evaluation is most relevant to. Internal validity is the feature the RCT optimizes for. External validity is what it sacrifices to get there. The sacrifice is usually worth it for drug regulation, where the clean internal answer is the prerequisite and the FDA can require Phase IV studies to probe external validity. The sacrifice is often not worth it for education research, policy research, or development economics, where the populations of interest are heterogeneous and representative sampling matters more than experimental control. In those fields, observational methods that use representative populations often give more useful answers than RCTs that use convenient populations.

Knowing which trade is right for your question is part of knowing the tool.

---

## Integration: The Palm Trial

Let me run everything in this chapter through one worked example: the Pamoja Tulinde Maisha trial, commonly called the Palm trial, which tested four treatments for Ebola virus disease during the 2018–2020 outbreak in the Democratic Republic of Congo.

The question was causal: do any of these four drugs reduce mortality from Ebola, and which works best? The four arms were ZMapp (an antibody combination), Remdesivir (an antiviral), MAb114 (a single monoclonal antibody), and REGN-EB3 (a three-antibody cocktail). Patients arriving at treatment centers during the outbreak were randomized to one of the four arms. The primary outcome was mortality at 28 days.

Run the randomization argument. In the observational baseline, who gets which treatment would depend on which center they showed up at, what was in stock, what the attending physician preferred, how sick they were on arrival, and other things. All of those variables plausibly affect mortality. Each one creates a back-door path between treatment choice and outcome. Because randomization breaks all of those arrows at once, the trial's estimate of each treatment's effect on mortality is not contaminated by any of them.

The trial was not fully double-blinded — the four treatments were administered differently enough that blinding was impossible. The design handled this by using an objective primary outcome. You can bias a subjective symptom score when you know what arm a patient is in. You can't easily bias whether a patient is alive at day 28.

At an interim analysis after roughly 500 patients had been enrolled, the data monitoring board saw differences large enough to act on. Mortality ran around 49% in the ZMapp arm, 53% in Remdesivir, 34% in MAb114, and 29% in REGN-EB3. The ethical logic was that continuing to randomize patients to the two worse arms, now that evidence had accumulated, was no longer defensible — patients arriving tomorrow should get the better treatments. So enrollment in ZMapp and Remdesivir stopped, and the trial continued with the two winners.

The final published results confirmed both MAb114 and REGN-EB3 as effective treatments. MAb114 was licensed by the FDA as Ebanga in 2020. REGN-EB3 was licensed the same year as Inmazeb. The trial converted observational uncertainty about four candidate therapies into regulatory certainty about two approved ones.

Now the external validity question. The trial was run in the DRC during an active outbreak, on patients recruited from conflict-affected regions, many of them seriously ill on arrival, most of them younger than the average patient in high-resource clinical settings. The drugs work for the population actually in the trial. Do they work as well for a hypothetical future outbreak among, say, aging healthcare workers in Europe? The trial does not say, because it did not sample that population. Emergency deployment accepts the external validity gap because the alternative — no approved treatment at all — is worse. That's a judgment call, not a trial result.

What I want you to see from this example is that Palm is a model RCT precisely because it handles each of the three categories of limit honestly. Randomization handled the confounding that would have contaminated observational comparison. Execution risk — blinding, dropout — was mitigated by the objective outcome and the interim stopping rule. The external validity gap was acknowledged, and follow-up work is ongoing. The trial did not pretend to answer a question bigger than the one it had posed. That is the posture of a well-designed study, and it is the posture you should be looking for when you read any RCT.

---

## A note about AI

Randomization solves the confounding problem at the design stage. The model can write fluently about both the strength and the limits. The interesting question is which limit applies to your specific study.

Where the model genuinely helps: walking through the structural arguments for and against randomization in a given case (feasibility, ethics, external validity, selection effects).

Where the model does damage: declaring a randomized design feasible or ethical in your context. Feasibility and ethics are local, regulatory, and political — none of which the model has access to.

The rule: arguments from the model; the feasibility call from the team that would actually run the trial.

---

## Exercises

Work these with paper. The first two are about moving randomization's logic from recognition to fluency.

### Warm-up

**Exercise 4.1** *(Objective 1.)* Draw a causal diagram with treatment *T*, outcome *Y*, and two confounders *X₁* and *X₂* that each cause both *T* and *Y*. Then draw the same diagram as it looks after *T* is randomized. State in one sentence what changed and why that change eliminates confounding.

**Exercise 4.2** *(Objective 1.)* Explain in plain English why "randomization averages out confounders" is a weaker statement than "randomization deletes arrows into *T*." Under which statement is it clearer why unmeasured confounders don't matter?

**Exercise 4.3** *(Objective 2.)* For each of the following, state whether an RCT is (a) ethically possible, (b) practically possible, (c) both, or (d) neither. Justify briefly:

- Testing whether a new blood pressure drug reduces stroke risk
- Testing whether lead paint exposure reduces childhood IQ
- Testing whether a new math curriculum improves eighth-grade test scores
- Testing whether immigration policies affect wage growth
- Testing whether childhood trauma causes adult depression
- Testing whether a new UI design increases user retention on a website

### Application

**Exercise 4.4** *(Objective 3.)* A startup runs an A/B test on a new checkout flow. Users visiting the site are randomly assigned to the old flow or the new flow. The company measures conversion rate over two weeks. The new flow wins by 4%. The CEO declares victory. Identify at least three ways bias could still be present despite the randomization, and describe what you'd want to check before accepting the conclusion.

**Exercise 4.5** *(Objective 3, and preview of Chapter 7.)* A researcher runs an RCT of a job training program for ex-offenders. Participants are randomized to training or control. At follow-up, only 60% of the training arm actually completed the program, and 5% of the control arm obtained similar training on their own. Explain (a) what an intent-to-treat analysis estimates; (b) what a per-protocol analysis estimates; (c) why the per-protocol number might be biased even though the trial was randomized; (d) what question you'd need to use instrumental variables methods (Chapter 7) to answer.

**Exercise 4.6** *(Objectives 2, 4.)* A drug trial for Alzheimer's medication excludes patients over 85, patients with kidney disease, patients on more than three concurrent medications, and patients whose caregivers don't speak English. The trial shows the drug reduces cognitive decline by 20%. The FDA approves it for general use in Alzheimer's patients. Name the internal validity of this trial. Name the external validity concern. Describe one person for whom you would not, personally, trust the trial's estimate.

### Synthesis

**Exercise 4.7** *(Objectives 1, 2, 3.)* Design an RCT to test whether moderate red wine consumption reduces cardiovascular disease. Specify: treatment arms, randomization mechanism, duration, primary outcome, how you'd handle blinding, expected non-compliance, how you'd analyze. Then argue — using the concepts of this chapter — why this trial will probably never be run. Connect your argument to what Chapter 7 will need to accomplish.

**Exercise 4.8** *(Objectives 2, 4, 6.)* Three causal questions: (i) Does this specific hypertension drug reduce stroke risk? (ii) Does universal pre-K improve lifetime earnings? (iii) Did the Marshall Plan cause European postwar recovery? For each, state: whether an RCT is possible; if possible, what it would look like; if not possible, what kind of observational method (of the ones I've previewed: matching, weighting, IV, counterfactual) would be the most plausible substitute and why.

**Exercise 4.9** *(Objectives 3, 5.)* Re-read my analysis of the Palm trial. Identify: (a) the confounders randomization handled; (b) the execution risks the design mitigated and how; (c) the external validity gap that remains; (d) the ethical constraint that determined how the trial was stopped. Then write one paragraph evaluating the trial's design in the voice of a reader who has just finished this chapter.

### Challenge

**Exercise 4.10** *(Open-ended, beyond the chapter.)* Find a published RCT in a field you know something about — ClinicalTrials.gov indexes many; your own field likely has a canonical example. Read the paper carefully. Write a 500-word critique that evaluates three things: the internal validity (was the randomization clean and preserved?); the external validity (who isn't in this trial who should matter to the conclusion?); and the honesty of the paper's own discussion of its limits. Compare the paper's stated limits to the ones you would flag using this chapter.

**Exercise 4.11** *(Beyond this chapter, pointing forward.)* In an RCT with imperfect compliance, we noted that intent-to-treat and per-protocol analyses give different answers. Propose — without using the formal machinery of instrumental variables, which comes in Chapter 7 — a strategy for estimating the causal effect of actually receiving the treatment, rather than merely being assigned to it. What assumption does your strategy rest on? What could go wrong with that assumption?

---

## Chapter Summary

If you've worked through this chapter, here is what you should now be able to do.

You can explain, in diagrammatic terms, why randomization eliminates confounding. The structural argument — randomization deletes every arrow into the treatment variable, and without arrows into *T*, there are no back-door paths — is stronger than the statistical argument that randomization balances confounders on average. The structural argument makes clear why unmeasured confounders don't matter: they existed in the world before and after randomization, but the randomization cut their connection to the treatment, so they can't confound the treatment-outcome comparison.

You can identify which causal questions admit randomization and which don't. The first category of limits is impossibility — ethical, practical, structural. Smoking cannot be randomized because assigning it would cause harm. Monetary policy cannot be randomized because countries cannot be experimentally assigned. Race cannot be randomized because there is no coherent intervention corresponding to it. Most of the interesting causal questions in social science, epidemiology, and policy fall here.

You can read an RCT's design and find the places where bias can still enter. Non-compliance breaks the equivalence between assignment and treatment received. Blinding failures let subjective outcomes leak judgment bias into the data. Dropout, if it correlates with outcome, breaks randomization after the fact. Intent-to-treat analysis preserves the randomization but answers a different question than per-protocol analysis does.

You can distinguish internal validity from external validity. Internal validity is what the randomization certifies: within the trial, the causal effect is correctly estimated. External validity is what nothing certifies: whether that estimate applies to populations outside the trial. Every RCT has an external validity gap because every RCT uses a selected population. Honesty about that gap is part of reading a trial well.

The one idea from this chapter that matters most: **randomization is a structural intervention on the causal diagram, not a statistical correction.** It erases arrows. It makes confounding impossible rather than adjusting for it. Everything else follows from that.

The common mistake to watch for: treating the RCT as a source of clean numbers that require no judgment. Every RCT makes external validity claims that aren't certified by randomization. Every real RCT has non-compliance, dropout, or blinding issues that require honest analysis. The RCT is the cleanest tool in the kit; it is not an infallible one.

The Feynman test for this chapter: can you explain to a friend, without using the word "confounding," why a coin-flipped trial is more trustworthy than an observational comparison? If you can walk them through the arrow-deletion picture without jargon, and get them to see why it doesn't matter what you haven't measured, you understand this chapter.

---

## Connections Forward

The rest of this book exists because most causal questions cannot be randomized. Chapters 5 through 8 are a systematic tour of what observational methods do instead, and each of them is trying, in its own way, to approximate the structural property Fisher built into the RCT — the absence of arrows into the treatment variable.

Chapter 5 takes up **matching**. The intuition: if you can construct a comparison group that looks, on the measured variables, just like the treated group, you are approximating what randomization would have produced — a comparison group that differs from the treated group only in the treatment. The assumption that carries all the weight is that the *measured* variables include all the important confounders.

Chapter 6 extends this to **weighting**, which uses the same conceptual apparatus with different computational trade-offs. Matching discards subjects who don't have good matches; weighting keeps everyone but down-weights subjects who aren't comparable. Both are doing the same structural work by different mechanics.

Chapter 7 handles the case where you can't measure the confounders: **instrumental variables**. The instrument plays the role randomization plays in the RCT. It induces variation in the treatment that is, by assumption, not contaminated by confounding. Snow's cholera study, with choice of water company as an instrument, is the historical touchstone. Mendelian randomization, using genetic variants as instruments, is the modern workhorse. IV methods are the most elegant observational approach and the hardest to apply well.

Chapter 8 pushes to the third rung of the causal ladder with **counterfactuals** and mediation — asking not just about average effects but about what would have happened to specific individuals under specific alternative treatments.

The through-line across all four chapters: every observational method is trying to simulate the structural property Fisher built into the RCT. Some do it by conditioning on measured confounders. Some do it by finding a natural lever. Some do it by explicit counterfactual modeling. None is as clean as randomization. All are necessary because randomization isn't always available.

The RCT remains the reference standard. When an observational method works, it produces results that would have matched a hypothetical RCT. When an observational method fails, it deviates from the RCT in specific, diagnosable ways. The RCT is the North Star — not always reachable, but always the direction we are navigating toward.

═══════════════════════════════════════
SUBSTACK HTML (Copy-Paste Ready)
═══════════════════════════════════════

<!-- Manual steps needed:
     1. Insert 2 figures where marked (FIGURE 4.1, 4.2): pre-randomization DAG with confounders pointing into T and Y, then post-randomization DAG with arrows into T deleted. Draw in DAGitty, TikZ, or Mermaid.
     2. No tables. No LaTeX equations in this chapter.
     3. One direct quote is cited inline: "the skillful interrogation of nature" attributed to Joan Fisher Box's biography of R. A. Fisher. -->

<h2>Chapter 4: Randomization and Its Limits</h2>

<h3>Opening: The Oldest Trial I Know Of</h3>

<p>About twenty-five hundred years ago, four young men refused to eat the king's meat.</p>

<p>They were captives — Jewish nobles brought from Jerusalem to Babylon after Nebuchadnezzar conquered the city. Part of their preparation for royal service was a three-year training program, and part of the training was a rich diet served from the king's table. One of the four, a young man named Daniel, objected to the food for religious reasons. He proposed a bargain to the king's steward: give him and his three companions vegetables and water for ten days, and at the end of the ten days, look at them. Compare them to the others. Let the steward's own eyes decide.</p>

<p>The steward agreed. After ten days, according to the first chapter of the Book of Daniel, the four vegetable-eaters "appeared fairer and fatter in flesh" than the young men who had been eating the king's meat. The steward kept them on the vegetable diet.</p>

<p>I want you to look at what Daniel built, because it's remarkable.</p>

<p>He had a treatment group — four men on vegetables. He had a control group — the other captives on meat. He had a pre-specified duration of ten days. He had an outcome measure — visible health. He had a decision rule agreed to in advance — whatever the steward saw, that would govern. That is a sophisticated piece of experimental thinking, and it is roughly twenty-four hundred years older than anything comparable in the scientific record.</p>

<p>Now look at what it's missing.</p>

<p>Daniel and his three companions were not randomly selected. They volunteered for the vegetable diet. More than that, they volunteered <em>because</em> they were religiously motivated, disciplined, and probably healthier to begin with than an average cross-section of the captives. If they looked better after ten days, how much of that was the diet and how much was the kind of people who volunteered for the diet? The text can't tell us. The trial cannot separate the effect of the treatment from the effect of who chose the treatment.</p>

<p>This is the problem a randomized controlled trial solves. It took humanity until the twentieth century to find the solution, and the solution is elegant enough that it deserves a whole chapter. The RCT is the cleanest tool we have for answering causal questions, and when it's available, it is the method of choice.</p>

<p>Most of the time, it isn't available. The rest of this book is about what you do in that case. But before you can understand the alternatives — matching, weighting, instrumental variables, counterfactual analysis — you have to understand exactly what the RCT does and exactly where it breaks. Otherwise you won't know whether your observational method succeeded or failed, because you won't know what success looks like.</p>

<h4>Learning Objectives</h4>

<p>By the end of this chapter you should be able to:</p>

<ol>
<li><strong>Explain</strong>, in the language of causal diagrams, why randomization eliminates confounding — not by correcting for it but by deleting it from the structure.</li>
<li><strong>Identify</strong> which causal questions can and cannot be answered by a randomized controlled trial, and name which category a new question falls into.</li>
<li><strong>Read</strong> an RCT's design and locate the points where bias can still enter despite randomization.</li>
<li><strong>Distinguish</strong> internal validity (certified by randomization) from external validity (not certified by anything).</li>
<li><strong>Analyze</strong> a real RCT using the vocabulary of chains, forks, colliders, and paths from Chapter 2.</li>
<li><strong>Explain</strong> why observational methods must exist — what the rest of this book has to accomplish that an RCT would handle by construction.</li>
</ol>

<h4>Prerequisites</h4>

<p>You should have worked through Chapters 1, 2, and 3. From Chapter 2 you need the diagrammatic vocabulary — nodes, arrows, back-door paths, d-separation. From Chapter 3 you need the concept of confounding as a structural problem, not a statistical one, and you need to know why "control for covariates in a regression" is not automatically causal reasoning.</p>

<h4>Why This Chapter Matters</h4>

<p>Every observational method in the rest of this book is trying to approximate what an RCT does by construction. Matching tries to approximate it by conditioning. Instrumental variables try to approximate it by finding a natural lever. Counterfactual methods try to approximate it by modeling the comparison explicitly. If you don't know what the RCT is doing, you can't tell whether your observational surrogate is doing it well, badly, or at all.</p>

<hr>

<h3>Concept 1: What Randomization Actually Does</h3>

<p>The argument for randomization is usually given in statistical language: "randomization balances the treatment and control groups on average, so any differences in outcomes must be due to the treatment." That framing is true but weak. It makes randomization sound like a convenient statistical property — something that works in expectation, on average, with enough subjects, if the stars align.</p>

<p>The structural framing is stronger, and it is the one I want you to take from this chapter.</p>

<p>Randomization is a <em>surgical operation on the causal diagram</em>. It deletes every arrow that points into the treatment variable. Not balances them. Not corrects for them. Deletes them.</p>

<p>Let me show you what this means concretely.</p>

<h4>Worked Example: What the Diagram Looks Like Before and After</h4>

<p>Suppose you want to know whether a new drug reduces blood pressure. In the real world, without an RCT, what causes who gets the drug? Many things. The patient's current blood pressure affects it — doctors prescribe the drug more often to sicker patients. Age affects it — some drugs are preferred in older or younger patients. Insurance coverage affects it. Patient preference affects it. The doctor's training affects it. Unmeasured things — genetic predisposition, lifestyle, compliance tendencies — affect it.</p>

<p>Call the drug <em>T</em> (treatment), blood pressure outcome <em>Y</em>, and use <em>X</em> as a catch-all for the web of things that affect who gets <em>T</em>. Some of those things also affect <em>Y</em> directly — sicker patients have worse outcomes regardless of treatment; older patients respond differently to the drug; unmeasured lifestyle factors affect blood pressure.</p>

<p>Here's the observational diagram:</p>

<!-- FIGURE 4.1: A DAG with treatment T and outcome Y, plus a cloud of variables X (age, current blood pressure, lifestyle, genetic factors, insurance, preference) with arrows going into both T and Y. Multiple back-door paths T ← X → Y run through every variable in X. Caption: Before randomization, every variable that affects who gets the drug and also affects the outcome creates a back-door path. Many of these variables are unmeasured. -->

<p>Every variable in <em>X</em> creates a back-door path from <em>T</em> to <em>Y</em>. To identify the causal effect by conditioning, you would need to measure every relevant confounder and block every back-door path. Miss one, and your estimate is biased. And the deepest problem is that you don't know what you've missed. Unmeasured confounders are, by definition, the ones you haven't thought of.</p>

<p>Now run an RCT. The drug is assigned by a coin flip — or, more likely, by a random number generator tied to a subject ID. The arrows from <em>X</em> to <em>T</em> all disappear. Age doesn't affect who gets the drug anymore. Blood pressure doesn't. Insurance doesn't. Lifestyle doesn't. Not because these variables don't exist — they still exist, and they still affect <em>Y</em> — but because a coin flip does not consult them.</p>

<p>Here's the post-randomization diagram:</p>

<!-- FIGURE 4.2: The same diagram after randomization. All arrows from X to T are deleted. X still has arrows to Y. T has a direct arrow to Y. No back-door paths remain. Caption: Randomization erases every arrow into the treatment variable. Every back-door path is gone — not adjusted for, gone. The only path from T to Y is the causal path T → Y. -->

<p>Every back-door path required an arrow into <em>T</em>. There are no arrows into <em>T</em>. Therefore there are no back-door paths. Therefore there is no confounding. The only path from <em>T</em> to <em>Y</em> is the directed causal path.</p>

<p>Notice what this argument does not require. It does not require me to know what the confounders are. It does not require me to measure them. It does not require me to adjust for them. The randomization handles them all at once — the known, the unknown, and the unthought-of — because it intervenes on the assignment mechanism rather than on the confounders themselves.</p>

<p>This is the design philosophy of the RCT. It trades flexibility for guarantee. You cannot use an RCT to study anything where you don't control the treatment assignment — that's the flexibility you give up. In exchange, you get a structural guarantee that confounding is impossible, not just that you've corrected for it. That trade is the right one often enough that the RCT became the gold standard of causal evidence. It is not the right trade always, which is why we need the rest of this book.</p>

<h4>Why I'm Calling This "Structural"</h4>

<p>I want to press on the language here because it matters.</p>

<p>When I say the arrows into <em>T</em> are "deleted," I am not speaking loosely. The observational distribution of <em>T</em> was produced by a data-generating process in which <em>X</em> caused <em>T</em>. The randomized distribution of <em>T</em> is produced by a different data-generating process, one in which a coin flip causes <em>T</em> and <em>X</em> does not. These are two different worlds. The second world is the one the experimenter creates on purpose. In the second world, the causal diagram relating <em>T</em> to <em>Y</em> genuinely does not have the arrows that the first world has.</p>

<p>This is different from "adjusting for X in a regression." Adjusting for <em>X</em> tries to remove the statistical effect of the back-door paths while leaving the arrows in place. It works if you've measured all the <em>X</em>'s. If you haven't, the paths you didn't close still run. Randomization doesn't close the paths; it deletes them. It works regardless of whether you know what they are.</p>

<p>That distinction — statistical correction versus structural intervention — is what makes the RCT qualitatively different from observational adjustment, not just quantitatively cleaner.</p>

<hr>

<h3>Concept 2: Fisher, Rothamsted, and the Skillful Interrogation of Nature</h3>

<p>I want to show you where this idea came from, because knowing the problem Fisher was actually solving makes the solution clearer.</p>

<p>Ronald Fisher was a statistical prodigy, a geneticist, and a famously combative scientific personality. He's worth mentioning with one piece of biographical honesty: he spent his later years arguing against the evidence that smoking causes cancer, and he was wrong about that. The man had blind spots. His contributions to experimental design, however, are foundational, and they survive his other mistakes.</p>

<p>In the 1920s, Fisher was working at the Rothamsted Experimental Station in England, the oldest agricultural research station in the world. His job was to help design and analyze experiments on crops — which fertilizer produces the best yield, which variety of wheat resists drought, which planting pattern survives pest infestations. The experiments at Rothamsted had historically been run the obvious way: apply treatment A to some plots and treatment B to others, harvest, weigh the output, compare.</p>

<p>The difficulty, which Fisher saw immediately, was that the plots weren't identical.</p>

<p>Some plots were on higher ground with better drainage. Some had been heavily fertilized in previous seasons and still carried the residue. Some had better sun exposure. Some had more clay in the soil, some more sand. If you applied fertilizer A to a good plot and fertilizer B to a bad plot, you were measuring a mixture — the fertilizer effect plus the plot effect — and you couldn't separate them after the fact. Whatever the yields told you, they told you about the combination, not the fertilizers alone.</p>

<p>Fisher's response was three techniques, which together define the modern experimental design. I want to walk through each because each one solves a specific problem.</p>

<h4>Randomization</h4>

<p>Randomization is the core move. Assign each fertilizer to a random selection of plots. Don't put fertilizer A on the good plots; don't put fertilizer B on the bad plots; don't let the researcher's implicit theories about which fertilizer "should" work where drive the assignment. Let a random process do the assigning.</p>

<p>The argument for randomization is that it solves a problem no other method could solve: the problem of <em>unmeasured</em> plot differences. Fisher could not possibly measure everything that made one plot different from another. Soil chemistry, microbial composition, past history, water table depth, bird traffic — the list is endless. With non-random assignment, those unmeasured differences could systematically favor one fertilizer over another in ways nobody would notice. With random assignment, the unmeasured differences distributed evenly, in expectation, across all treatments. Whatever made one plot different, on average, was as likely to end up under fertilizer A as fertilizer B.</p>

<p>This is exactly the structural argument I gave above, transposed to 1920s agriculture. Fisher didn't have the diagrammatic language — Wright was publishing path diagrams in the same decade, but Fisher and Wright were not exactly friends, and Fisher did not adopt the graphical approach. But the logic of his argument is the logic of deleting arrows into <em>T</em>.</p>

<h4>Replication</h4>

<p>Randomization handles confounding on average. It does not handle noise. Any single plot has its own individual noise — a passing storm, a gopher invasion, an accidentally trampled row. If you only had one plot per treatment, the noise could swamp the signal.</p>

<p>Fisher's answer was to replicate. Run many plots of each treatment. Average across them. The plot-level noise averages out, leaving the treatment effect visible against a smaller residual.</p>

<p>Replication is not a fix for confounding. It is a fix for <em>precision</em>. Randomization without replication gives you unbiased but imprecise estimates — the right answer in expectation, but possibly far off in any single experiment. Replication tightens the interval around the estimate.</p>

<h4>Blocking</h4>

<p>Blocking is the clever move that adds efficiency without sacrificing randomization.</p>

<p>Fisher observed that plot-level variation wasn't random — it was structured. Nearby plots were similar to each other. Plots on the same side of the field were similar. So instead of randomizing across all plots, Fisher proposed organizing plots into <em>blocks</em> of similar quality, then randomizing within each block.</p>

<p>A block might be a contiguous strip of land with similar soil and drainage. Inside the block, each fertilizer is applied to one plot, selected randomly. Across blocks, every fertilizer appears in every block. When you analyze the data, you can remove block-level variation — which doesn't tell you anything about fertilizers anyway — and focus on the within-block comparisons, where the fertilizers are competing on similar ground.</p>

<p>Blocking is efficient because it reduces the noise against which the treatment effect must be detected. It preserves randomization because within each block, assignment is random. And it handles an important class of confounders — the ones that cluster spatially or temporally — without needing to name them.</p>

<h4>The Skillful Interrogation of Nature</h4>

<p>Fisher's daughter, Joan Fisher Box, later wrote his biography, and the phrase I remember from it is that her father saw experimental design as <em>"the skillful interrogation of nature."</em> The idea is that nature answers whatever question you ask, but only the exact question you ask. If you ask a confused question — one that mixes fertilizer with plot quality — you get a confused answer. Nature does not do you the favor of interpreting what you meant.</p>

<p>Randomization is the technique for asking the question you actually want to ask. When fertilizer assignment is random, you are asking: "if fertilizer choice were unrelated to plot quality, what would the yields be?" And that is the causal question. Nature obliges.</p>

<p>The streptomycin trial in 1948 — the Medical Research Council's test of streptomycin for pulmonary tuberculosis — is usually cited as the first modern randomized controlled trial in medicine. The MRC made a deliberate choice to randomize rather than let physicians assign treatment by clinical judgment. The trial produced a clean result: streptomycin worked. The design Fisher invented for crops migrated to medicine, and it has been the regulatory gold standard ever since.</p>

<p>Here's the MKBHD-style evaluation of Fisher's design choice: he optimized hard for robustness against unknown confounding and accepted the cost, which is that you have to be able to control the assignment mechanism. In agricultural research that cost is usually acceptable; you can randomize plots. In medicine that cost is sometimes acceptable; you can randomize patients when the ethics are clear. In economics, politics, history, and the study of human life choices, that cost is usually prohibitive. Fisher's design doesn't fail on those questions — it simply doesn't apply. That is the trade the RCT makes. It is an enormously good trade when the trade is available.</p>

<hr>

<h3>Concept 3: The Limits</h3>

<p>So the RCT is structurally superior to observational methods when both are available. Why isn't it always available? The limits sort into three categories, and I want to name each one clearly because the rest of the book is organized around them.</p>

<h4>Limit 1: You Can't Randomize It (Impossibility)</h4>

<p>Some treatments cannot be randomized because assigning them would be unethical, impossible, or meaningless.</p>

<p><strong>Ethical impossibility.</strong> You cannot randomize people to behaviors or exposures that might harm them. You cannot assign people to smoke for twenty years to see if smoking causes cancer. You cannot assign pregnant women to drink during pregnancy. You cannot assign children to lead-paint exposure. These aren't hypothetical objections — they are the actual reason that most of epidemiology, occupational health, and environmental science runs on observational data. Every causal claim in those fields is an observational claim, because the ethical constraints don't allow the experiment that would settle it.</p>

<p><strong>Practical impossibility.</strong> You cannot randomize countries to different monetary policies. You cannot randomize cities to different crime rates. You cannot randomize the Industrial Revolution. Some treatments are too large, too diffuse, or too tied to history to be assignable by any experimenter. When the unit of analysis is a country or an era, random assignment is not on the table.</p>

<p><strong>Structural impossibility.</strong> Some "treatments" aren't coherent as assignable interventions. You cannot randomize people to be different ages. You cannot randomize them to different genders, different races, different native languages. These are not treatments; they are characteristics. The concept of an RCT on race does not make sense, because the proposed intervention — "assign this person to be a different race" — does not correspond to any actual operation.</p>

<p>The first big chunk of causal questions that motivate this book — does smoking cause cancer, does air pollution cause asthma, do class sizes affect learning — falls into this category. You will not randomize them. The rest of this book exists because of this category.</p>

<h4>Limit 2: You Randomized But Things Got Messy (Execution)</h4>

<p>Even when an RCT is possible in principle, real human behavior contaminates the design in predictable ways.</p>

<p><strong>Non-compliance.</strong> You randomized Alice to the drug arm. Alice does not take the drug. You randomized Bob to the placebo arm. Bob obtains the drug elsewhere and takes it. When you analyze the data, are Alice and Bob in the arms they were assigned to or the arms they actually experienced?</p>

<p>This matters more than it sounds. If you analyze by assignment — the <em>intent-to-treat</em> analysis — you are estimating the effect of <em>being offered</em> the treatment, not the effect of actually taking it. That's a different number. If you analyze by what actually happened — the <em>per-protocol</em> analysis — you have broken the randomization, because the people who took the drug and the people who didn't may differ for reasons that also affect the outcome. Compliance is itself a trait; analyzing by compliance reintroduces the selection you were trying to avoid.</p>

<p>The honest answer in practice is to report both, and to use instrumental variables methods (which Chapter 7 covers) to estimate the effect of actual treatment receipt on the subgroup that complied with assignment. This gives you something called the Local Average Treatment Effect, the LATE, which is the causal effect on compliers — not on everyone, but on the people whose treatment was determined by the randomization. We'll develop this formally later.</p>

<p><strong>Blinding failures.</strong> If patients know which arm they're in, they may behave differently in ways that affect the outcome. If doctors know which arm their patient is in, they may treat the patient differently, monitor more carefully, or report symptoms differently. A well-run trial blinds both — a double-blind design — using placebos indistinguishable from the active treatment. This works well for pills. It works poorly for surgeries, devices, and behavioral interventions, where blinding is often impossible. When blinding fails or isn't feasible, the design has to use objective outcomes (mortality, lab values) that aren't subject to judgment bias, or accept some contamination.</p>

<p><strong>Dropout.</strong> Subjects leave the trial before it ends. If dropout is random, fine — you lose precision. If dropout correlates with outcome — if people who feel worse drop out of the drug arm and people who feel fine drop out of the placebo arm — you've broken the randomization, because the comparison now reflects who stayed rather than who was assigned. Good trials track dropout aggressively and run sensitivity analyses assuming different patterns of missingness.</p>

<p>None of these execution problems invalidates randomization as a concept. But every real RCT has them to some degree, and the quality of a real trial is partly about how honestly it handles them.</p>

<h4>Limit 3: The RCT Answered a Different Question Than You Think (External Validity)</h4>

<p>This is the RCT's deepest limitation, and the one I want you to take most seriously, because it doesn't go away with better trial design.</p>

<p>An RCT estimates the causal effect <em>in the population of subjects who were actually in the trial</em>. Those subjects volunteered. They passed the inclusion criteria. They consented to the protocol. They showed up. They are, in most trials, systematically different from the population that will actually receive the treatment in practice.</p>

<p>Clinical trials often exclude: patients over 75, patients under 18, pregnant women, patients with kidney problems, patients on other medications, patients with any comorbidity the sponsor worries about. Those exclusions produce a clean trial population — low heterogeneity, predictable responses, cooperative subjects. They also produce a trial population that doesn't look like the people who will take the drug in the real world.</p>

<p>The RCT's internal validity — the trustworthiness of the causal conclusion <em>within the trial population</em> — is certified by randomization. Its <em>external validity</em> — the applicability of that conclusion to other populations — is certified by nothing. It requires judgment. It requires follow-up studies. It requires, in many cases, years of post-marketing surveillance to find out what happens when the drug hits the messier world outside the trial.</p>

<p>This is the trade the RCT makes, and it is the one MKBHD-style evaluation is most relevant to. Internal validity is the feature the RCT optimizes for. External validity is what it sacrifices to get there. The sacrifice is usually worth it for drug regulation, where the clean internal answer is the prerequisite and the FDA can require Phase IV studies to probe external validity. The sacrifice is often not worth it for education research, policy research, or development economics, where the populations of interest are heterogeneous and representative sampling matters more than experimental control. In those fields, observational methods that use representative populations often give more useful answers than RCTs that use convenient populations.</p>

<p>Knowing which trade is right for your question is part of knowing the tool.</p>

<hr>

<h3>Integration: The Palm Trial</h3>

<p>Let me run everything in this chapter through one worked example: the Pamoja Tulinde Maisha trial, commonly called the Palm trial, which tested four treatments for Ebola virus disease during the 2018–2020 outbreak in the Democratic Republic of Congo.</p>

<p>The question was causal: do any of these four drugs reduce mortality from Ebola, and which works best? The four arms were ZMapp (an antibody combination), Remdesivir (an antiviral), MAb114 (a single monoclonal antibody), and REGN-EB3 (a three-antibody cocktail). Patients arriving at treatment centers during the outbreak were randomized to one of the four arms. The primary outcome was mortality at 28 days.</p>

<p>Run the randomization argument. In the observational baseline, who gets which treatment would depend on which center they showed up at, what was in stock, what the attending physician preferred, how sick they were on arrival, and other things. All of those variables plausibly affect mortality. Each one creates a back-door path between treatment choice and outcome. Because randomization breaks all of those arrows at once, the trial's estimate of each treatment's effect on mortality is not contaminated by any of them.</p>

<p>The trial was not fully double-blinded — the four treatments were administered differently enough that blinding was impossible. The design handled this by using an objective primary outcome. You can bias a subjective symptom score when you know what arm a patient is in. You can't easily bias whether a patient is alive at day 28.</p>

<p>At an interim analysis after roughly 500 patients had been enrolled, the data monitoring board saw differences large enough to act on. Mortality ran around 49% in the ZMapp arm, 53% in Remdesivir, 34% in MAb114, and 29% in REGN-EB3. The ethical logic was that continuing to randomize patients to the two worse arms, now that evidence had accumulated, was no longer defensible — patients arriving tomorrow should get the better treatments. So enrollment in ZMapp and Remdesivir stopped, and the trial continued with the two winners.</p>

<p>The final published results confirmed both MAb114 and REGN-EB3 as effective treatments. MAb114 was licensed by the FDA as Ebanga in 2020. REGN-EB3 was licensed the same year as Inmazeb. The trial converted observational uncertainty about four candidate therapies into regulatory certainty about two approved ones.</p>

<p>Now the external validity question. The trial was run in the DRC during an active outbreak, on patients recruited from conflict-affected regions, many of them seriously ill on arrival, most of them younger than the average patient in high-resource clinical settings. The drugs work for the population actually in the trial. Do they work as well for a hypothetical future outbreak among, say, aging healthcare workers in Europe? The trial does not say, because it did not sample that population. Emergency deployment accepts the external validity gap because the alternative — no approved treatment at all — is worse. That's a judgment call, not a trial result.</p>

<p>What I want you to see from this example is that Palm is a model RCT precisely because it handles each of the three categories of limit honestly. Randomization handled the confounding that would have contaminated observational comparison. Execution risk — blinding, dropout — was mitigated by the objective outcome and the interim stopping rule. The external validity gap was acknowledged, and follow-up work is ongoing. The trial did not pretend to answer a question bigger than the one it had posed. That is the posture of a well-designed study, and it is the posture you should be looking for when you read any RCT.</p>

<hr>

<h3>Exercises</h3>

<p>Work these with paper. The first two are about moving randomization's logic from recognition to fluency.</p>

<h4>Warm-up</h4>

<p><strong>Exercise 4.1</strong> <em>(Objective 1.)</em> Draw a causal diagram with treatment <em>T</em>, outcome <em>Y</em>, and two confounders <em>X₁</em> and <em>X₂</em> that each cause both <em>T</em> and <em>Y</em>. Then draw the same diagram as it looks after <em>T</em> is randomized. State in one sentence what changed and why that change eliminates confounding.</p>

<p><strong>Exercise 4.2</strong> <em>(Objective 1.)</em> Explain in plain English why "randomization averages out confounders" is a weaker statement than "randomization deletes arrows into <em>T</em>." Under which statement is it clearer why unmeasured confounders don't matter?</p>

<p><strong>Exercise 4.3</strong> <em>(Objective 2.)</em> For each of the following, state whether an RCT is (a) ethically possible, (b) practically possible, (c) both, or (d) neither. Justify briefly:</p>

<ul>
<li>Testing whether a new blood pressure drug reduces stroke risk</li>
<li>Testing whether lead paint exposure reduces childhood IQ</li>
<li>Testing whether a new math curriculum improves eighth-grade test scores</li>
<li>Testing whether immigration policies affect wage growth</li>
<li>Testing whether childhood trauma causes adult depression</li>
<li>Testing whether a new UI design increases user retention on a website</li>
</ul>

<h4>Application</h4>

<p><strong>Exercise 4.4</strong> <em>(Objective 3.)</em> A startup runs an A/B test on a new checkout flow. Users visiting the site are randomly assigned to the old flow or the new flow. The company measures conversion rate over two weeks. The new flow wins by 4%. The CEO declares victory. Identify at least three ways bias could still be present despite the randomization, and describe what you'd want to check before accepting the conclusion.</p>

<p><strong>Exercise 4.5</strong> <em>(Objective 3, and preview of Chapter 7.)</em> A researcher runs an RCT of a job training program for ex-offenders. Participants are randomized to training or control. At follow-up, only 60% of the training arm actually completed the program, and 5% of the control arm obtained similar training on their own. Explain (a) what an intent-to-treat analysis estimates; (b) what a per-protocol analysis estimates; (c) why the per-protocol number might be biased even though the trial was randomized; (d) what question you'd need to use instrumental variables methods (Chapter 7) to answer.</p>

<p><strong>Exercise 4.6</strong> <em>(Objectives 2, 4.)</em> A drug trial for Alzheimer's medication excludes patients over 85, patients with kidney disease, patients on more than three concurrent medications, and patients whose caregivers don't speak English. The trial shows the drug reduces cognitive decline by 20%. The FDA approves it for general use in Alzheimer's patients. Name the internal validity of this trial. Name the external validity concern. Describe one person for whom you would not, personally, trust the trial's estimate.</p>

<h4>Synthesis</h4>

<p><strong>Exercise 4.7</strong> <em>(Objectives 1, 2, 3.)</em> Design an RCT to test whether moderate red wine consumption reduces cardiovascular disease. Specify: treatment arms, randomization mechanism, duration, primary outcome, how you'd handle blinding, expected non-compliance, how you'd analyze. Then argue — using the concepts of this chapter — why this trial will probably never be run. Connect your argument to what Chapter 7 will need to accomplish.</p>

<p><strong>Exercise 4.8</strong> <em>(Objectives 2, 4, 6.)</em> Three causal questions: (i) Does this specific hypertension drug reduce stroke risk? (ii) Does universal pre-K improve lifetime earnings? (iii) Did the Marshall Plan cause European postwar recovery? For each, state: whether an RCT is possible; if possible, what it would look like; if not possible, what kind of observational method (of the ones I've previewed: matching, weighting, IV, counterfactual) would be the most plausible substitute and why.</p>

<p><strong>Exercise 4.9</strong> <em>(Objectives 3, 5.)</em> Re-read my analysis of the Palm trial. Identify: (a) the confounders randomization handled; (b) the execution risks the design mitigated and how; (c) the external validity gap that remains; (d) the ethical constraint that determined how the trial was stopped. Then write one paragraph evaluating the trial's design in the voice of a reader who has just finished this chapter.</p>

<h4>Challenge</h4>

<p><strong>Exercise 4.10</strong> <em>(Open-ended, beyond the chapter.)</em> Find a published RCT in a field you know something about — ClinicalTrials.gov indexes many; your own field likely has a canonical example. Read the paper carefully. Write a 500-word critique that evaluates three things: the internal validity (was the randomization clean and preserved?); the external validity (who isn't in this trial who should matter to the conclusion?); and the honesty of the paper's own discussion of its limits. Compare the paper's stated limits to the ones you would flag using this chapter.</p>

<p><strong>Exercise 4.11</strong> <em>(Beyond this chapter, pointing forward.)</em> In an RCT with imperfect compliance, we noted that intent-to-treat and per-protocol analyses give different answers. Propose — without using the formal machinery of instrumental variables, which comes in Chapter 7 — a strategy for estimating the causal effect of actually receiving the treatment, rather than merely being assigned to it. What assumption does your strategy rest on? What could go wrong with that assumption?</p>

<hr>

<h3>Chapter Summary</h3>

<p>If you've worked through this chapter, here is what you should now be able to do.</p>

<p>You can explain, in diagrammatic terms, why randomization eliminates confounding. The structural argument — randomization deletes every arrow into the treatment variable, and without arrows into <em>T</em>, there are no back-door paths — is stronger than the statistical argument that randomization balances confounders on average. The structural argument makes clear why unmeasured confounders don't matter: they existed in the world before and after randomization, but the randomization cut their connection to the treatment, so they can't confound the treatment-outcome comparison.</p>

<p>You can identify which causal questions admit randomization and which don't. The first category of limits is impossibility — ethical, practical, structural. Smoking cannot be randomized because assigning it would cause harm. Monetary policy cannot be randomized because countries cannot be experimentally assigned. Race cannot be randomized because there is no coherent intervention corresponding to it. Most of the interesting causal questions in social science, epidemiology, and policy fall here.</p>

<p>You can read an RCT's design and find the places where bias can still enter. Non-compliance breaks the equivalence between assignment and treatment received. Blinding failures let subjective outcomes leak judgment bias into the data. Dropout, if it correlates with outcome, breaks randomization after the fact. Intent-to-treat analysis preserves the randomization but answers a different question than per-protocol analysis does.</p>

<p>You can distinguish internal validity from external validity. Internal validity is what the randomization certifies: within the trial, the causal effect is correctly estimated. External validity is what nothing certifies: whether that estimate applies to populations outside the trial. Every RCT has an external validity gap because every RCT uses a selected population. Honesty about that gap is part of reading a trial well.</p>

<p>The one idea from this chapter that matters most: <strong>randomization is a structural intervention on the causal diagram, not a statistical correction.</strong> It erases arrows. It makes confounding impossible rather than adjusting for it. Everything else follows from that.</p>

<p>The common mistake to watch for: treating the RCT as a source of clean numbers that require no judgment. Every RCT makes external validity claims that aren't certified by randomization. Every real RCT has non-compliance, dropout, or blinding issues that require honest analysis. The RCT is the cleanest tool in the kit; it is not an infallible one.</p>

<p>The Feynman test for this chapter: can you explain to a friend, without using the word "confounding," why a coin-flipped trial is more trustworthy than an observational comparison? If you can walk them through the arrow-deletion picture without jargon, and get them to see why it doesn't matter what you haven't measured, you understand this chapter.</p>

<hr>

<h3>Connections Forward</h3>

<p>The rest of this book exists because most causal questions cannot be randomized. Chapters 5 through 8 are a systematic tour of what observational methods do instead, and each of them is trying, in its own way, to approximate the structural property Fisher built into the RCT — the absence of arrows into the treatment variable.</p>

<p>Chapter 5 takes up <strong>matching</strong>. The intuition: if you can construct a comparison group that looks, on the measured variables, just like the treated group, you are approximating what randomization would have produced — a comparison group that differs from the treated group only in the treatment. The assumption that carries all the weight is that the <em>measured</em> variables include all the important confounders.</p>

<p>Chapter 6 extends this to <strong>weighting</strong>, which uses the same conceptual apparatus with different computational trade-offs. Matching discards subjects who don't have good matches; weighting keeps everyone but down-weights subjects who aren't comparable. Both are doing the same structural work by different mechanics.</p>

<p>Chapter 7 handles the case where you can't measure the confounders: <strong>instrumental variables</strong>. The instrument plays the role randomization plays in the RCT. It induces variation in the treatment that is, by assumption, not contaminated by confounding. Snow's cholera study, with choice of water company as an instrument, is the historical touchstone. Mendelian randomization, using genetic variants as instruments, is the modern workhorse. IV methods are the most elegant observational approach and the hardest to apply well.</p>

<p>Chapter 8 pushes to the third rung of the causal ladder with <strong>counterfactuals</strong> and mediation — asking not just about average effects but about what would have happened to specific individuals under specific alternative treatments.</p>

<p>The through-line across all four chapters: every observational method is trying to simulate the structural property Fisher built into the RCT. Some do it by conditioning on measured confounders. Some do it by finding a natural lever. Some do it by explicit counterfactual modeling. None is as clean as randomization. All are necessary because randomization isn't always available.</p>

<p>The RCT remains the reference standard. When an observational method works, it produces results that would have matched a hypothetical RCT. When an observational method fails, it deviates from the RCT in specific, diagnosable ways. The RCT is the North Star — not always reachable, but always the direction we are navigating toward.</p>

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Esther Duflo** built the modern field of randomized controlled trials in development economics — running large-scale field experiments in education, health, and microfinance. She won the 2019 Nobel Prize at 46, making her the youngest economist Nobel laureate.

![Esther Duflo](../images/esther-duflo-ot5.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Esther Duflo, and how does her work running RCTs in development economics connect to randomization we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Esther Duflo"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Duflo's J-PAL field RCTs — a specific intervention, a specific outcome.
- Ask it to engage the critique of RCTs in development (Angus Deaton, others) — when do they oversimplify?

What changes? What gets better? What gets worse?
