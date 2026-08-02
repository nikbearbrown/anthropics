# Chapter 1: Why Causal Inference?


## TL;DR

- Here's a fact you can look up: people who go to the emergency room die at higher rates than people who don't.
- The chapter moves through What you'll be able to do by the end of this chapter, Concept 1: Why correlation doesn't transfer, The trick your brain plays, Design philosophy detour: why the field cares about this, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A Feynman-style starting point*

Here's a fact you can look up: people who go to the emergency room die at higher rates than people who don't.

Read that sentence again. It's true. Every ER in every city you can name: if you compare the mortality rate of people who walked through the door last Tuesday against a random person who didn't, the ER group dies more often.

So here's the question I want you to actually sit with for a second before you read the next paragraph. Does the emergency room kill people?

Of course not. You already know that. You know it before you know anything about statistics, anything about medicine, anything about this book. You know it because you understand something about emergency rooms that isn't in the data — namely, that sick people go to them. The mortality rate comparison isn't telling you what the ER does. It's telling you something about who ends up there.

But here's what I want you to notice. The thing you just did — dismissing a real, statistically significant, perfectly calculated correlation — is the entire subject of this book. You brought outside knowledge. You reasoned about cause and effect using information that wasn't in the numbers. You decided that one pattern in the data was about a *mechanism* (sick people choose hospitals) and that another pattern people might extract from the same data (the hospital itself) was spurious. The data didn't tell you this. You told yourself this.

Now imagine you didn't know anything about emergency rooms. Imagine you were a Martian statistician looking at American health records for the first time. What would the data say?

The data would say: going to the ER is associated with dying.

And if you were a competent Martian statistician with no medical knowledge, you would write a paper confidently announcing this association. You might even, if you were sloppy with your language — and most people are — suggest that the ER "has an effect on" mortality. Other Martians, reading your paper, would conclude that ERs are dangerous and should be avoided.

Two thousand years of medicine ran exactly this way. This chapter is about why.

## What you'll be able to do by the end of this chapter

By the time you finish this chapter, you should be able to:

- **Distinguish** a causal question from a predictive or associational question in plain English
- **Classify** any given question by which of the three levels of causation it lives on: observation, intervention, or counterfactual
- **Explain**, in your own words, why data alone cannot answer a causal question — and why this is a theorem, not a matter of needing more data
- **Identify** the causal assumptions embedded in a claim, even when the claim is phrased to hide them
- **Recognize** when a correlation is being smuggled in as a causal conclusion

**Prerequisites:** You should know what a correlation is. You should have seen the phrase "correlation is not causation" at least once in your life. That's it. The rest I'll teach you.

**Why this chapter matters:** Everything else in the book depends on the distinctions I draw here. The methods I'll teach you — diagrams, matching, weighting, instrumental variables — are techniques for answering a specific kind of question. If you can't identify which questions they answer, you'll apply them to the wrong problems and get confident, official-looking, precisely wrong answers.

---

## Concept 1: Why correlation doesn't transfer

Let me give you another correlation. This one is real. You can check it.

People who own more books live longer.

I'll pause. Think about what that sentence can and can't tell you.

What it tells you, literally, is that if I lined up a thousand bookshelves and measured their owners' lifespans, the bookshelves with more books would tend to correspond to longer lives. That's it. That's the statistical content.

What most people *hear* when I say it is something different. They hear: if you buy more books, you will live longer.

That second claim is a completely different kind of statement than the first one. The first one is about what *is*. The second one is about what *would happen if you did something*. And the move from the first to the second is not automatic. It is in fact unjustified by anything I've told you so far. The correlation is real; the intervention claim is a leap.

### The trick your brain plays

Here's where I had to stop and think carefully when I first learned this, because the mistake is so natural. Your brain is built to reason about causes. When you see two things happen together, your default mode is to hunt for the mechanism connecting them. That's a useful skill in most of life. If the baby cries when the cat jumps on the crib, you figure out pretty quickly that the cat scares the baby.

But the correlation-to-cause move that works so well in daily life fails when you move to statistics about populations. Here's why. When I say "people who own more books live longer," I'm giving you one number — a correlation. That number is consistent with many different underlying stories:

- **Story A: Books cause longevity.** Reading is mentally stimulating, reduces dementia risk, extends life. Intervention works: buy more books, live longer.
- **Story B: Longevity causes books.** People who live longer have more years to accumulate books. Intervention fails: buying more books doesn't change your lifespan; it just makes your shelves crowded.
- **Story C: Something else causes both.** People with higher education tend to buy more books AND have better health care AND live longer. Books and longevity both respond to education. Intervention fails: buying books without the education doesn't do anything.
- **Story D: Selection.** Maybe the survey only includes people who responded, and responders are different from non-responders in ways that correlate with both books and health. Intervention is meaningless because the correlation is an artifact.

Four different stories. All consistent with the same correlation. The data cannot tell you which one is right.

This is the core problem, and I want you to hold it firmly in mind because I'll come back to it through the whole book. A correlation is one number. The causal structures that could produce it are many. If you want to know what happens when you *do* something — buy books, take aspirin, raise the minimum wage — you need information beyond the correlation itself.

### Design philosophy detour: why the field cares about this

Here's something I want to note, MKBHD-style, because it reveals a choice the field made. Classical statistics — the stuff you may have learned in an intro course — largely chose to stay out of this problem. For about eighty years, serious statistics departments taught correlation, regression, hypothesis testing, and confidence intervals, and kept the word "causation" at arm's length. "Correlation is not causation" was the warning label, not the beginning of an investigation.

This was a design decision, and it had costs. The field optimized for mathematical rigor at the level of "what can we compute from the data?" and it sacrificed the ability to answer the questions that scientists, doctors, and policymakers actually ask. A medical researcher does not want to know the correlation between a drug and recovery. They want to know whether the drug *caused* the recovery, because that's the question that tells them whether to prescribe it to the next patient.

Causal inference, as a field, is the answer to the question: what do we need to add to statistics to recover our ability to answer these questions? Not an abandonment of statistical rigor — a supplement to it.

### Worked example 1

Let me show you how to walk through a correlation carefully. Here's the claim:

> In a study of a thousand elementary schools, schools with more art programs had higher standardized test scores.

Take a minute. What does this tell you?

Here's my reasoning, step by step.

**Step 1: What is the literal statistical content?** The data shows that art-program-count and test-score are positively correlated across schools. That is a description of what was measured. Nothing more.

**Step 2: What causal stories are consistent with this?** I can think of at least four.

1. Art programs improve cognitive skills that show up on tests. (Art → scores.)
2. High-performing schools have budget surplus and use it for art programs. (Scores → art.)
3. Wealthy districts have both better-funded arts programs and students who test better due to home resources. (Wealth → both.)
4. Schools that attract engaged parents get more art programs (PTA funded) and higher test scores (parental involvement). (Parent engagement → both.)

**Step 3: What would I need to distinguish these?** To tell story 1 from story 3, I'd need data on district wealth and a way to compare similar-wealth districts that differ in art programs. To tell story 1 from story 2, I'd need art programs introduced in previously low-scoring schools and see if scores rise afterward.

**Step 4: What should I NOT conclude?** I should not conclude, from this correlation alone, that adding art programs to a low-scoring school will raise its scores. That's an intervention claim, and the data as described can't support it.

**The general lesson:** A correlation is a starting point for an investigation, not the conclusion of one. The question you should ask when you see a correlation is not "what does this mean?" but "what are the candidate stories, and what would I need to distinguish them?"

### Common mistakes with Concept 1

Students new to this tend to make two errors in opposite directions.

The first error is the sophomore's error: throwing out all correlations as "meaningless." This is wrong. Correlations are extremely useful. They narrow the space of possible causal structures, flag associations worth investigating, and provide the raw material that — combined with causal assumptions — produces causal knowledge. The slogan "correlation is not causation" doesn't mean correlation is nothing. It means correlation is not *automatically* causation.

The second error is the practitioner's error: treating every correlation in your own research area as causal because "we all know" the mechanism. You don't know. You have a hypothesis. The whole point of causal inference is that "we all know" is not a substitute for an argument you can write down and defend.

---

## Concept 2: The three rungs of causation

I've been writing as if there are two kinds of questions — statistical and causal. There are actually three. The distinction matters because the techniques needed, and the assumptions required, are different at each level.

I owe this framing to Judea Pearl, the computer scientist whose work anchors most of modern causal inference. He called it the **ladder of causation**. Three rungs, each demanding more than the last.

### Rung 1: Seeing

The first rung is the world of observation. Questions here ask what *is*.

- What fraction of smokers develop lung cancer?
- How often does rain follow a red sky at morning?
- What is the average income of people with college degrees?
- Given that a patient has a certain set of symptoms, what is the probability they have the flu?

These are all statistical questions. They ask about associations, conditional probabilities, patterns in existing data. You can answer them with classical statistics and no causal reasoning at all.

Notice what rung 1 questions have in common: they ask about the world *as it is*, not about what would happen if you changed it. "What is the probability a patient with these symptoms has the flu?" is a question about the set of people with those symptoms. It is not a question about what would happen if you gave someone the symptoms (that would be the wrong intervention), nor is it a question about what would happen if you treated the flu (that's a different question at a different rung).

Most of what's called "machine learning" and "predictive analytics" lives on rung 1. It's enormously powerful — I can predict what movie you'll like, what ad you'll click, which credit applicant will default — without ever asking a causal question. Pure prediction is a rung 1 activity.

### Rung 2: Doing

The second rung is the world of intervention. Questions here ask what will happen if we *do* something.

- If this patient takes aspirin, will her headache go away?
- If we raise the minimum wage, will employment fall?
- If we ban smoking indoors, will lung cancer rates decline?
- If we send this child to a smaller school, will her test scores rise?

These are questions about actions, policies, treatments. They are questions about changing the world — reaching in, flipping a switch, seeing what happens.

Here's the crucial point: **rung 2 questions cannot be answered with rung 1 tools alone.** Not "can't be answered easily." Can't be answered, period, without additional assumptions.

Why not? Remember the emergency room example. The rung 1 fact is: ER visits and mortality are correlated. But the rung 2 question — "what happens if we send *this* patient to the ER" — cannot be answered from that correlation, because the correlation reflects who goes to the ER, not what the ER does. You have to add information beyond the correlation itself to bridge the gap.

The classical answer to rung 2 questions is the randomized controlled trial. If I want to know whether aspirin relieves headaches, I randomly assign headache sufferers to aspirin or placebo and compare the outcomes. The randomization is doing specific work: it breaks the connection between taking aspirin and all the other things that normally correlate with choosing aspirin (being health-conscious, being able to afford it, whatever). Chapter 4 will spend a lot of time on exactly why this works. For now, just note that we've *had* to introduce something new — the randomization — to get off rung 1.

Most of this book is about methods for answering rung 2 questions when you *can't* randomize. You can't randomly assign people to smoke for twenty years. You can't randomly assign countries to different minimum wage laws. So the question becomes: what can you do instead, and under what assumptions?

### Rung 3: Imagining

The third rung is the world of counterfactuals. Questions here ask what would have happened if things *had been* different.

- Would Washington have survived if he hadn't been bled?
- Did this particular chemotherapy cause this particular patient's recovery, as opposed to the patient would have recovered anyway?
- Was the defendant's action a necessary cause of the plaintiff's injury?
- Would this heat wave have occurred without climate change?

These questions are about specific individuals in specific hypothetical worlds. They're the hardest questions in causal inference, and for most of scientific history they were treated as unanswerable — not hard, but outside the scope of rigorous analysis.

The difficulty is obvious once you stare at it. The counterfactual world — where Washington wasn't bled — doesn't exist. We can't measure what happened there. Washington existed once and was bled once. The thing we want to compare against is not available.

And yet: we answer counterfactual questions all the time. Juries do it to assign liability. Doctors do it when they tell a patient "the surgery saved your life." Historians do it when they say "without Pearl Harbor, the US would have entered the war later." The human mind reaches the third rung instinctively. What we lack is the discipline to check whether our counterfactual reasoning is sound.

Chapter 8 develops the machinery for this formally. The short version: counterfactual questions can be answered when you have a detailed enough causal model, because the model lets you simulate the world under alternative conditions. The assumptions required are strong. The payoff is enormous — the third rung is where blame, responsibility, and individual-level reasoning live.

### The ladder is ordered

Here's a fact that matters and that I want you to internalize: **the rungs are strictly ordered, not parallel.** 

A method that works only with rung 1 information cannot answer rung 2 questions. A method that works only with rung 2 information cannot answer rung 3 questions. The tools get more powerful as you climb, but they also demand more. More assumptions, more structure, more explicit causal reasoning.

This isn't a convention or a terminology choice. It's a theorem. Pearl and his collaborators proved it in the 1990s. No amount of cleverness at rung 1 will ever produce a rung 2 answer, and no amount of cleverness at rung 2 will ever produce a rung 3 answer. You *have* to bring additional assumptions to climb.

This is also why, for most of the twentieth century, so many researchers made causal claims based on pure correlation analysis and got away with it intellectually — the field didn't have a way to check. The ladder wasn't articulated until recently. Now that it is, papers that make rung 2 claims based on rung 1 methods stick out.

### Worked example 2

I'll walk you through classifying a set of questions by rung. This is the kind of exercise that looks trivial when I do it and takes practice when you try it yourself.

**Question:** Among patients who took drug X, what was the recovery rate?

This is rung 1. It's a pure statistical question about the observed data. No intervention, no counterfactual. The answer is just a count divided by another count.

**Question:** If we give drug X to the next patient with this condition, what's the probability she recovers?

This looks similar but it's rung 2. The word "if we give" is an intervention. You're asking about the result of a deliberate action. This cannot be answered from the recovery rate alone if the people who received drug X differ systematically from the next patient.

**Question:** This patient recovered after taking drug X. Would she have recovered without it?

Rung 3. It's about a specific individual and an alternative world where that individual didn't take the drug. You need a causal model of that individual's situation to answer it.

**Question:** What's the correlation between hours of sleep and test scores in this dataset?

Rung 1. Pure statistical description.

**Question:** If we made students sleep more, would their test scores go up?

Rung 2. An intervention question.

**Question:** This particular student got a bad grade. Would she have gotten a better grade if she'd slept more the night before?

Rung 3. Specific individual, specific counterfactual.

The general skill I'm trying to build here is noticing the verbal cues. "Among," "what is the rate of," "how often" — these tend to be rung 1. "If we do," "what happens when," "will X cause Y" — rung 2. "Would this particular case have been different if" — rung 3.

### Design philosophy detour: why three rungs, not two?

A reasonable student might ask: why not just two categories — descriptive (rung 1) and causal (rungs 2 and 3 combined)?

The honest answer is that you *could* do it that way, and some older texts do. But the field has moved toward three rungs because the assumptions required for rung 3 really are stronger than for rung 2, and bundling them hides the difference. A randomized controlled trial answers rung 2 questions without much causal modeling — randomization does the heavy lifting. But the same RCT doesn't automatically answer rung 3 questions about individuals. If you want to know whether *this* patient, specifically, benefited from the treatment, the average treatment effect from the RCT doesn't tell you.

So the three-rung design reflects a real distinction in how much you need to assume. It's a design choice by the field that optimizes for precision about what each method can and can't do — at the cost of more terminology to learn. A trade-off, like all design choices.

---

## Concept 3: Why data alone cannot do it

Now I want to show you something that trips up most people when they first see it, and that I think is the single most important idea in this chapter.

**No amount of observational data, no matter how large, can by itself distinguish between causal structures that produce the same data.**

This is not a practical limitation. It's not "we need bigger datasets" or "we need better algorithms." It's a mathematical fact about what data can tell you. Two different causal worlds can produce exactly the same statistical patterns. If the patterns are all you have, you can't tell which world you're in.

Let me show you this concretely.

### The setup

Imagine two different possible causal worlds involving three variables: let's call them A, B, and C.

**World 1:** A causes B. A causes C. There's no direct connection between B and C.

Diagrammatically: <!-- FIGURE: Three-node DAG. A at top with two arrows: one down-left to B, one down-right to C. No arrow between B and C. Caption: World 1. A is a common cause of B and C. -->

**World 2:** B and C both have some direct influence on A. Neither causes the other.

Diagrammatically: <!-- FIGURE: Three-node DAG. A at bottom with two arrows pointing INTO it: one from B (top-left) and one from C (top-right). No arrow between B and C. Caption: World 2. A is a common effect of B and C. -->

These are structurally very different. In World 1, A is the cause and B, C are effects. In World 2, B and C are causes and A is the effect.

Now here's the puzzle. If you collect data on A, B, and C and compute all the correlations — correlation between A and B, correlation between A and C, correlation between B and C, conditional correlations given the third variable, every statistical summary you can think of — **the two worlds can produce identical numbers.**

I mean this precisely. There exist parameter settings for World 1 and parameter settings for World 2 such that every joint probability over A, B, C is identical. If you only had the data, you could not tell which world you were in. No statistical test can distinguish them.

### Why does this matter?

Because the two worlds answer causal questions differently.

In World 1, intervening on A will change B and change C (A causes both).
In World 2, intervening on A will NOT change B or C (A is an effect; B and C are upstream causes).

Same data. Completely different answer to the rung 2 question "what happens if I intervene on A?" 

The data cannot tell you. You must know — from outside the data — whether A is upstream or downstream. That outside knowledge is the causal assumption. It is the thing the analyst brings to the problem that the statistician alone cannot bring.

### Worked example 3

Let me make this concrete with numbers.

Suppose I tell you the following. In a dataset of 10,000 people, I measured three variables:

- Income (high or low)
- Exercise (yes or no)
- Heart attack within five years (yes or no)

And I computed the following correlations:
- Income and exercise: positive. Richer people exercise more.
- Income and heart attack: negative. Richer people have fewer heart attacks.
- Exercise and heart attack: negative. Exercisers have fewer heart attacks.

Now, two candidate causal stories:

**Story I:** Income causes exercise (gym memberships cost money). Income causes fewer heart attacks (better nutrition, less stress). Exercise has no direct effect on heart attacks — it only looks like it does because both are downstream of income.

**Story II:** Income causes exercise (same reason). Exercise causes fewer heart attacks (cardiovascular conditioning). Income has no direct effect on heart attacks beyond its effect through exercise.

These two stories both predict exactly the pattern of correlations I described. From the correlations alone, you cannot tell them apart.

But they answer a different question differently:

**If we built a program to get low-income people to exercise more, would heart attacks drop?**

Under Story I: No. Exercise is a marker of income, not a cause of heart health. Making poor people exercise without raising their income wouldn't help.

Under Story II: Yes. Exercise causes the reduction directly. Get them to exercise and heart attacks drop regardless of income.

This is why the assumption matters. This is why you cannot skip it. A public health authority that runs this analysis purely statistically gets identical numbers under both stories — and implements either the right or wrong policy depending on which story is actually true.

### How do we ever learn anything, then?

I've just told you that data alone can't get you to causation. So how does causal inference ever produce answers?

The answer is that we bring additional knowledge to the problem. That knowledge comes in several forms:

1. **Domain expertise about mechanisms.** A cardiologist knows that exercise affects the heart through specific physiological pathways. That knowledge rules out Story I and favors Story II. The knowledge isn't in the data; it's in what we know about how hearts work.

2. **Temporal ordering.** If A happened before B, then B can't cause A. This alone eliminates many candidate structures.

3. **Known interventions.** If in other contexts, changing A has been observed to change B, we have evidence that A can cause B.

4. **Natural experiments.** Sometimes the world produces something close to a randomization by accident — a policy change that affected some people and not others, a lottery that assigned treatments. These can give us rung 2 leverage without a formal experiment. Chapter 7 is about this.

5. **Explicit randomization.** When we *can* randomize, we build the causal conclusion into the design. Chapter 4 is about this.

Every method in this book is a way of combining one or more of these kinds of outside knowledge with observational data to answer causal questions. The methods differ in which assumptions they require, how strong those assumptions are, and what happens when the assumptions fail. Learning the methods means learning to choose the right one for the assumptions you're actually willing to defend.

### Common mistakes with Concept 3

Two errors to watch for.

First, some students, once they learn that causal inference requires outside assumptions, conclude that "it's all assumptions, so nothing is really provable." This is wrong and unhelpfully cynical. *Every* empirical claim — including claims in physics, chemistry, and mathematics — rests on assumptions. The question is whether the assumptions are explicit, checkable, and defensible. Causal inference's demand that you state your assumptions clearly is a feature, not a bug.

Second, some students, having learned that the data alone is insufficient, swing to the opposite error: they decide that the causal assumptions are the *whole* story and the data is almost incidental. This is also wrong. The data matters enormously. Given a set of causal assumptions, the data does the work of producing the numerical answer. The assumptions tell you what to compute; the data tells you what the number is. You need both.

---

## Integration: Putting the three concepts together

Let me now show you how the three concepts work together on a single example.

Suppose you read a study with the following claim:

> Employees who participated in the company's optional wellness program had 15% lower healthcare costs than employees who did not. We estimate that the program saves the company $800 per participant per year.

Now, using what you've learned, walk through this claim with me.

**Step 1: What's the statistical content?** There's a correlation between participating in the program and lower costs. That's rung 1. True, assuming their data is correct.

**Step 2: What's the causal claim being made?** The 15% number is rung 1. But the phrase "saves the company $800 per participant per year" is rung 2. It's a claim about what would happen under intervention — specifically, under the intervention of enrolling someone in the program. The paper has moved from rung 1 to rung 2 without flagging that it did so.

**Step 3: What causal stories are consistent with the correlation?** Let me think of at least three.

- *Story A:* The program genuinely improves health, which reduces costs. Intervention works. The paper is right.
- *Story B:* Healthy people self-select into the program. Their costs were going to be low anyway. Intervention does nothing — you can't pay healthy people to get healthier by enrolling the sick ones in the same program.
- *Story C:* People who are already engaged with their health — reading health websites, going to doctors — are more likely to enroll AND to have lower costs for other reasons (regular checkups catching problems early). Intervention probably doesn't capture this effect; you can't enroll the disengaged and make them engaged.

**Step 4: What additional information would I need to distinguish these?** 

The cleanest thing would be a randomized controlled trial — randomly assigning some employees to the program and others not. The paper's description doesn't mention this. If the program is "optional" and employees chose to enroll, Stories B and C are alive, and the $800 estimate is unreliable.

Less clean but still useful: comparing participants to non-participants *among employees with similar baseline health*. If wellness participants still have lower costs even when compared against non-participants who had identical health profiles at baseline, that's some evidence against Story B. This is the logic of matching (Chapter 5) and weighting (Chapter 6).

Even less clean but still informative: looking at what happened to costs *before* people joined the program. If future participants already had lower costs than future non-participants in the year before joining, that's strong evidence for Story B — self-selection was already there before the program started.

**Step 5: What should you conclude?**

You should conclude that the $800 number is a correlation-based estimate, not a causal estimate, and that the three stories above are alive until addressed. You should not conclude that the program is useless; you should conclude that this analysis doesn't tell you whether it works. The company should either run a randomization, or apply the observational methods in Chapters 5–8 with explicit assumptions about which story is true.

**The design-philosophy observation:** Notice that the paper's *rhetorical structure* smuggled the rung 2 claim in the second sentence after establishing the rung 1 correlation in the first sentence. This move — quietly shifting rungs — is ubiquitous in applied research, business reports, and journalism. A big part of what this book is trying to build in you is the reflex to spot this shift. When you see it, you stop trusting the numbers until the rung-2 claim is justified on its own terms.

---

## A note about AI

Causal inference exists because correlation is not causation, and language is structurally biased toward causal claims. The model is the most fluent producer of causal-shaped language in history. The discipline of this book is the discipline of resisting that fluency.

Where the model genuinely helps: producing canonical examples of confused causal claims from published research, and the specific evidence that would have to be in hand to upgrade an association to a cause.

Where the model does damage: declaring something causal from associational data. The model's training corpus is full of writers who collapsed correlation into causation, and the model has absorbed both the collapse and the confidence.

The rule: causal language requires a causal warrant. The model has the language. The warrant is yours.

---

## Exercises

These are graduated. Start with the warm-ups. Don't skip to the challenges — the payoff of the later exercises depends on the work you did on the earlier ones.

### Warm-up: Classifying rungs

**Exercise 1.1** *(Objective: classify questions by rung)* For each of the following questions, identify which rung of the ladder it lives on. Justify your answer in one sentence.

1. Among patients hospitalized last year, what fraction were readmitted within 30 days?
2. If we give this new patient the discharge protocol, what's the probability she'll be readmitted within 30 days?
3. This patient was readmitted within 30 days. Would she have been readmitted if she'd received the discharge protocol instead of the one she received?
4. What's the average starting salary of computer science majors from public universities?
5. Will the new statistical requirement for CS majors raise average starting salaries?

**Exercise 1.2** *(Objective: classify questions by rung)* Find a news article that makes a quantitative claim about some social, economic, or health phenomenon. Identify at least one rung 1 claim and at least one rung 2 or rung 3 claim in the article. (Most journalism mixes the two freely.)

### Application: Candidate causal stories

**Exercise 1.3** *(Objective: generate alternative causal stories for a correlation)* For each of the following correlations, generate at least three plausible causal stories that could produce it. At least one of your three stories should NOT have the first-mentioned variable as the cause.

1. Countries with more lawyers per capita have higher GDP.
2. Children who have more books at home score higher on reading tests.
3. Cities with more parks have lower crime rates.

**Exercise 1.4** *(Objective: identify the intervention implied by a causal claim)* For each of the following statements, identify the intervention implicitly claimed, and state what data would be needed to support the intervention claim.

1. "Mindfulness meditation reduces anxiety."
2. "Economic sanctions reduce authoritarianism."
3. "Social media use decreases teen happiness."

### Synthesis: Reading a real claim

**Exercise 1.5** *(Objective: integrate all three concepts on a real analysis)* Find a published empirical paper in your field of interest. (If you don't have a field, use a paper from a major public health, economics, or education journal.) Do the following:

a. Identify the main causal claim the paper makes.
b. Identify which rung of the ladder that claim lives on.
c. Identify what statistical method the authors used.
d. Identify what causal assumptions the authors make, either explicitly or implicitly.
e. Identify at least one alternative causal story consistent with their data.
f. State what additional evidence would help distinguish the authors' preferred story from your alternative.

Write this up in 500 words or less. This exercise is the test of whether you've actually absorbed this chapter. If you can do it once comfortably, you can do it on every paper you read for the rest of your career.

### Challenge: Designing around the problem

**Exercise 1.6** *(Objective: imagine causal structures from scratch)* Pick a correlation from your own life — something you've personally observed about two variables that seem to move together. (Example: "I sleep worse when I drink coffee after 3 p.m.")

a. Write out at least four distinct causal stories that could produce your correlation.
b. For each story, describe what intervention evidence would look like.
c. For each story, describe what observational evidence beyond the correlation itself would support or undermine it.
d. Which story do you actually believe, and what's the weakest point in your evidence for it?

**Exercise 1.7** *(Objective: extend the framework)* The ladder of causation has three rungs. Some researchers have proposed that there should be a fourth rung — questions about what different agents would do given their different beliefs and goals. These are sometimes called "agentic" or "decision-theoretic" counterfactuals.

a. Write down a question that would live on such a rung but not on rungs 1, 2, or 3 as I've described them.
b. Argue briefly (one paragraph) for or against treating this as a separate rung.

*(This exercise has no single right answer. I'm testing whether you've understood the framework well enough to extend it.)*

---

## Chapter summary

You came into this chapter knowing something about correlation. You're leaving it, I hope, with something more valuable: the ability to tell what a correlation can and can't do for you, and to recognize when someone is trying to use a correlation to answer a question it can't answer.

**The one idea from this chapter that matters most.** Causal questions cannot be answered by data alone. They require causal assumptions — knowledge about how the world works — combined with data. This is a theorem, not a matter of taste or methodology. Any claim to the contrary is either confused or trying to sell you something.

**The common mistake to watch for.** The most common and dangerous error is shifting rungs without flagging that you've done so. A sentence like "participants had 15% lower costs, saving the company $800 per person per year" shifts from rung 1 to rung 2 between the comma. Watch for this shift. You'll see it every day for the rest of your career.

**What you should be able to teach someone else.** The Feynman test. If I drop you at a dinner party and someone tells you about a study they read, you should be able to say, in plain English: "That's interesting. But what they measured is a correlation. The causal interpretation they're giving it depends on assumptions they didn't state. Can we think about what those assumptions are and whether they're reasonable?" If you can do that — if you can translate the framework of this chapter into normal human conversation without sounding like a statistics textbook — you've got it.

**What you can now do that you couldn't before.** You can classify any question by its rung. You can identify the causal assumptions smuggled into a study's language. You can generate alternative causal stories consistent with a given correlation. You can articulate, in English, why the gap between correlation and causation is not closable by collecting more data.

Those are real capabilities. They are also the minimum you need before I can teach you anything else in this book.

---

## Connections forward

Chapter 1 has left you with a problem, not a solution. I've told you that data alone can't answer causal questions and that you need to bring causal assumptions to the table. I have not yet given you a way to *state* those assumptions precisely, check whether they're sufficient for your question, or compute an answer from them.

That's Chapter 2. In Chapter 2 I'll teach you causal diagrams — directed acyclic graphs, or DAGs — which are the language the rest of this book is written in. A DAG is a picture with nodes for variables and arrows for direct causal effects. That sounds simple, and the picture itself is simple, but the rules for reading a DAG tell you an enormous amount: which variables are associated, which are independent, which you have to adjust for to get a causal effect, and which questions are impossible to answer no matter what you do with the data.

Chapter 2 is the most technically demanding chapter in the book. I'll warn you now: the payoff is in Chapter 3 onward, where every method we discuss gets expressed in the language of DAGs and becomes clearer as a result. Invest in Chapter 2. It's the chapter everything else rides on.

One last thing. The three rungs I taught you here were articulated by Judea Pearl, and the framework is his. But the insight that causal inference requires causal assumptions is older — it goes back at least to Sewall Wright's path analysis in the 1920s, Jerzy Neyman's potential outcomes in 1923, and through a half-century of scattered work before Pearl and Rubin consolidated it in the 1990s. You're learning a field with a long history, articulated late. Don't let the recent vintage of the textbook version fool you into thinking the underlying ideas are new. They've been there. They were just hard to see.

Turn the page. Let's build the language.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Judea Pearl** wrote *Causality* in 2000 — formalizing the do-calculus and reshaping computer science, statistics, and epidemiology around graphical causal models. His insistence that correlation is not causation, but that causation can be precisely defined, founded modern causal inference.

**Run this:**

```
Who is Judea Pearl, and how does his work on the do-calculus connect to the case for causal inference we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Judea Pearl"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain the difference between P(Y|X) and P(Y|do(X)) using a specific real-world example.
- Ask it about Pearl's earlier work on Bayesian networks and probabilistic reasoning — and how he transitioned to causality.

What changes? What gets better? What gets worse?
