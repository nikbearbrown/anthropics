# Confounders: The Variable You Forgot


## TL;DR

- TL;DR: A confounder is not a variable that correlates with both treatment and outcome — that definition is wrong, and the chapter shows why.
- The chapter moves through Opening — A model that learned the wrong job, Concept one — A confounder is a structural position, not a correlation, Mid-chapter checkpoint, Concept two — Backdoor paths, and three diagnostic questions, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. Confounders: The Variable You Forgot
2. The Back Door: How Bias Sneaks In When You Aren't Watching
3. The Variable That Wasn't in the Data

**TL;DR:** A confounder is not a variable that correlates with both treatment and outcome — that definition is wrong, and the chapter shows why. A confounder is a *structural* common cause sitting on an open backdoor path, and identifying one requires the DAG and the domain knowledge to write it down — work no algorithm performs for you.

**Byline:** Nik Bear Brown

**Prerequisites:**
- Read a directed acyclic graph: nodes, edges, the direction of an arrow, the meaning of a path. (Ch. 3.)
- State the three identification-failure types from Ch. 4: wrong variables, wrong functional form, wrong conditioning.
- Use one of the three vocabularies — potential outcomes, structural equations, or graphs — without panic. The chapter speaks graphs.
- Comfortably stipulate that an arrow `A → B` means "A is part of what produces B," not "A and B are correlated."

**Learning objectives:**
- **Apply (Part A):** Given a DAG, apply three diagnostic questions to identify backdoor paths between treatment and outcome.
- **Analyze (Part A):** Determine a valid adjustment set for a specified treatment–outcome pair and defend its minimality.
- **Analyze (Part B):** Name one unmeasured confounder for a treatment–outcome pair in your own domain and state the bias direction it implies.
- **Evaluate (Part B):** Assess whether the adjustment decisions in your own candidate DAG are valid — close every backdoor, open no new ones.

---

## 1. Opening — A model that learned the wrong job

In October 2018, Jeffrey Dastin published a story in Reuters reporting that Amazon had quietly scrapped an internal recruiting model the company had been building since 2014. ([Dastin, Reuters, 2018](https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/) `[verify-URL-stability]`) The model's job, as the team described it, was to rank applicants — to look at a résumé and assign a score from one to five. Inside the team they joked that the goal was to "give me the top five and I'll hire them."

The model worked. It produced rankings. The rankings were consistent. The training set was real — ten years of résumés, paired with hiring outcomes from real Amazon recruiters and real Amazon managers. By every metric the team had thought to apply, it was doing what they wanted.

Then the audit landed.

The model penalized résumés that contained the word "women's" — as in "women's chess club captain." It downgraded graduates of two all-women's colleges. It rewarded verbs more common in men's résumés. The team patched the obvious patterns. Then the audit found more. The model had learned, from ten years of training data, that being male was a feature that made you more like a successful Amazon hire. The team eventually disbanded the project.

Sit with what happened here. Nobody on the team wrote a line of code that read `if gender == "female": subtract_points`. Nobody had to. The training data did the work. The historical hiring decisions reflected a decade of human choices — choices in which gender played a role, sometimes acknowledged, sometimes not. The model learned the relationship between résumé features and *who got hired in the past*. It then deployed that relationship to recommend *who should get hired in the future*. The two things look identical until you look at them structurally. They are not the same.

Here is what makes this a confounder problem rather than, say, a model-architecture problem. The variable that was distorting the output — historical gender bias in past hiring decisions — was not in the dataset. There was no column called `bias_of_2009_manager`. There was no feature called `gender_penalty_applied_during_screening`. The variable that mattered most was the one nobody had measured, because nobody measures the thing that doesn't have a name yet on the spreadsheet.

When I read this story I had to think about it for a few days before I could say cleanly what had gone wrong. The temptation is to call it "biased data" and stop. But "biased data" names the symptom, not the structure. The structure is this: a single unmeasured variable — let me call it *H*, for historical hiring practice — affected both what the training labels were ("was this person hired?") and what the deployed model would predict ("should this person be hired?"). One variable. Two effects. A common cause sitting upstream of everything the analyst could see.

That is a confounder. Not in the loose sense of "something correlated with bad outcomes." In the structural sense the rest of the chapter unpacks.

I open with this case because the lesson generalizes uncomfortably. Many models that ML engineers ship every week have an *H* like this. A pricing model trained on past prices. A churn model trained on past retention decisions. A fraud model trained on past human reviewers' approvals. Each one inherits a confounder it cannot see. Each one is in the same trouble Amazon's model was in. The trouble is not visible from the loss curve. It is visible from the DAG.

We are going to learn to find the variable you forgot.

---

## 2. Concept one — A confounder is a structural position, not a correlation

Here is the textbook definition you have probably already met:

> *A confounder is a variable that is correlated with both the treatment and the outcome.*

That definition is wrong. I do not mean "imprecise" or "incomplete." I mean wrong in a way that gives you the wrong answer in real cases. Tyler VanderWeele and Ilya Shpitser established this carefully in 2013 in the *Annals of Statistics*, in a paper titled "On the definition of a confounder." ([VanderWeele & Shpitser, 2013](https://doi.org/10.1214/12-AOS1058)) The correlation-based definition has been the standard since at least the 1950s. They showed it fails as a complete characterization in two ways at once: it misses cases where the confounder structure is real but the simple correlation is absent (so-called *M-bias* structures, which we will see in Chapter 7), and it over-counts variables that are correlated with both treatment and outcome but should not be conditioned on (mediators, colliders, instruments — Chapters 6, 7, and 10).

Watch what happens when we apply the wrong definition to the Obermeyer case.

Ziad Obermeyer and colleagues published in *Science* in 2019 a study of a commercial risk-prediction algorithm used by health systems serving about 200 million people in the United States. ([Obermeyer, Powers, Vogeli & Mullainathan, 2019](https://doi.org/10.1126/science.aax2342)) The algorithm assigned risk scores that determined which patients got referred to "high-risk care management" programs — extra clinical attention, extra coordination, extra nurses. The algorithm's input was, in effect, projected healthcare costs. The thought was a reasonable one: sicker people cost more, so cost is a proxy for sickness, so high projected cost identifies the sickest patients, who get the extra care.

What the audit found: at any given risk score, Black patients were considerably sicker than White patients. Among patients flagged as needing extra help, only 17.7% were Black. If the algorithm's risk score were re-calibrated to track actual illness rather than projected cost, the share would have been 46.5%. Roughly two and a half times more Black patients would have been flagged for the extra care than the algorithm flagged.

Now look at this through the broken definition. Treatment: enrollment in high-risk care management. Outcome: future health. Candidate "confounder": prior healthcare spending. Is prior spending correlated with treatment? Yes — the algorithm used it as the input to the assignment. Is prior spending correlated with future health? Yes — sicker people had spent more historically. By the correlation-based definition, you would say *control for prior spending* and move on. You would believe you had handled the confounding.

You would be wrong.

Here is the structural picture.

```
   (race / historical access to care) ──┐
                ↓                       ↓
        (prior spending) ────→  (algorithm score)  ────→  (care assignment)  ────→  (future health)
                                                                                      ↑
                                                                                      │
                                                                                 (true illness)
```

Prior spending is *downstream* of the variable that actually confounds — historical access to care — and *part of the mechanism* by which the algorithm makes decisions. Conditioning on prior spending does not close the bias path. It freezes the bias path at the point the algorithm uses it. The variable you wanted to neutralize (historical access) lives upstream and remains unmeasured. The "control for the correlated variable" reflex does the wrong thing here. It locks the bias in instead of breaking it.

The structural definition gives a different answer. A confounder of the treatment–outcome relationship is a variable that occupies a particular *position* on the graph: it sits at the head of an open path between treatment and outcome that does not go *through* treatment in the causal direction. Pearl named these *backdoor paths*. The position is what makes a variable a confounder. The correlation is a downstream consequence of being in that position, and many other things produce the same correlation without being in that position.

Here's the trick. The structural definition tells you what *to do* with each variable on the DAG. The correlation definition tells you only what is statistically associated with what — which the data already knows and the model already exploits. The structural definition is a different kind of object. It lives one level up from the data. That is exactly what makes it the layer the algorithm cannot perform for you.

Let me make this concrete. The simplest possible confounding structure is three variables:

```
            U
          /   \
         ↓     ↓
         X ───→ Y
```

`U` is a common cause of treatment `X` and outcome `Y`. The arrow `U → X` says: when `U` is present, that makes `X` more (or less) likely. The arrow `U → Y` says: when `U` is present, that makes `Y` more (or less) likely. Now consider what we observe in the data: `X` and `Y` covary. Part of that covariation is the *real* effect of `X` on `Y` (any direct arrow `X → Y` we haven't drawn). Part of that covariation is the *spurious* part contributed by `U`'s simultaneous push on both. The data cannot separate the two parts. The model cannot separate the two parts. Only structural knowledge — knowledge that `U` exists, knowledge that the two arrows from `U` exist — can separate them. That structural knowledge is the DAG.

Here is the move you should hold onto: a confounder is the variable whose *role on the graph* is to be a common cause of treatment and outcome. Its correlation properties follow from the role. The role does not follow from the correlation properties.

---

## Mid-chapter checkpoint

Stop here. I want to make sure something has landed before we go further.

A correlation-based definition of confounder asks: *is this variable statistically related to both X and Y?* A structural definition asks: *does this variable occupy a common-cause position relative to X and Y on the DAG?* The two questions have different answers on the same data. The structural answer is what the rest of causal inference machinery — backdoor adjustment, propensity scoring, instrumental variables, sensitivity analysis — was built to operate on. The correlation answer is what a regression coefficient operates on. They are not the same machine. If you have been working in the regression world, the change you are being asked to make is not "be more careful." It is "use a different machine."

You should be able to say in your own words: *the Amazon recruiter case had a common-cause structure in which historical hiring decisions caused both the training labels and the deployment-time predictions.* If you can say that, the structural framing is doing its work. If you cannot say it yet, reread Section 2 before going further. The next sections build on it.

---

## 3. Concept two — Backdoor paths, and three diagnostic questions

Now I am going to introduce the procedure you will use on Monday.

A *path* in a DAG is just a sequence of edges connecting two variables, ignoring direction. A *backdoor path* is a path between treatment `X` and outcome `Y` that starts with an arrow *into* `X`. The door image is Pearl's, and it works because the physical intuition is correct: if the only path between `X` and `Y` is the front door (`X → ... → Y`), the signal you measure is the causal effect of `X` on `Y`. If a back door is open — a path beginning with an arrow into `X` and ending somewhere on `Y` — then signal sneaks through that path, and the association you measure includes that smuggled-in piece.

`[verify-pedagogical-priority]` The three-question phrasing below is the one I find most useful. I have not found it stated exactly this way in a published source — Pearl's *Causality* §3.3, Hernán and Robins's *What If* Ch. 7, and Greenland & Robins's 1986 *International Journal of Epidemiology* paper all teach the same machinery in adjacent language. Treat the phrasing as the book's contribution to pedagogy, not as a canonical formula.

Given any path between `X` and `Y`, the three diagnostic questions are:

**Q1. Does the path start with an arrow into X?**
If yes, it is a backdoor path. (Otherwise it is either the causal path itself, `X → ... → Y`, or a forward path from `X` that does no confounding work.) Backdoor paths are the ones that can carry confounding bias.

**Q2. Is the path currently open or closed?**
A path is *open* if signal can flow along it. Signal flows along a chain `A → B → C` and a fork `A ← B → C` unless we condition on the middle variable. Signal does *not* flow along an inverted fork (a *collider*) `A → B ← C` — unless we condition on the collider or one of its descendants, in which case the collider opens up. Hold the collider rule for now; Chapter 7 is its own chapter. For this chapter, take it on stipulation that conditioning on a non-collider on the path *closes* the path, and conditioning on a collider on the path *opens* it.

**Q3. Will the conditioning set we are proposing close every open backdoor path without opening any new ones?**
This is the check on candidate adjustment sets. Closing requires putting at least one non-collider on every open backdoor path into the conditioning set. *Not* opening requires keeping every collider, and every descendant of every collider, *out* of the conditioning set.

That is the whole procedure. The work is in tracing the paths.

Here is a worked example. Treatment `X`: a supplier-quality program enrollment. Outcome `Y`: on-time delivery rate next quarter. The candidate DAG has five variables: `X` (program enrollment), `Y` (delivery rate), `C` (supplier capacity), `F` (supplier financial health), `M` (a mediator: number of warehouse checkpoints the supplier upgrades during the program).

```
              F (supplier financial health)
            /   \
           ↓     ↓
          C      C? — wait. Let me redraw.

```

I'll do it cleanly.

```
    F ──→ C
    │     │
    ↓     ↓
    X ──→ M ──→ Y
    │           ↑
    └───────────┘  (direct effect X → Y, alongside mediated effect through M)

    C also has an arrow C → Y (capacity affects delivery directly, independent of M).
```

So the edges are: `F → C`, `F → X`, `C → X`, `C → Y`, `X → M`, `X → Y`, `M → Y`. Six variables would be cleaner; I have used five. Let me just list the edges so the picture is unambiguous.

Edges in our example DAG:
1. `F → C` (financial health affects capacity)
2. `F → X` (financial health affects whether the supplier enters the program — healthier suppliers self-select)
3. `C → X` (capacity affects whether they enter — bigger suppliers more likely)
4. `C → Y` (capacity affects on-time delivery directly)
5. `X → M` (enrollment causes checkpoint upgrades)
6. `M → Y` (checkpoint upgrades cause on-time delivery)
7. `X → Y` (program has some direct effect on delivery not routed through `M`)

Now let me run the three questions for the effect of `X` on `Y`.

**Paths from X to Y:**

- Path A: `X → Y` — direct causal. *Not a backdoor* (starts with arrow out of X). Q1: no. Skip.
- Path B: `X → M → Y` — causal through mediator. *Not a backdoor.* Q1: no. Skip.
- Path C: `X ← C → Y` — *backdoor* (starts with arrow into X). Q1: yes. Q2: open (C is a fork, not currently conditioned on). Conclusion: a backdoor we must close.
- Path D: `X ← F → C → Y` — *backdoor* (starts with arrow into X). Q1: yes. Q2: open (F is a fork; C is a chain; neither currently conditioned on). Conclusion: a backdoor we must close.
- Path E: `X ← C ← F → ?` — wait, this is the same nodes as Path D in different order; the path itself is determined by the sequence of edges. Let me make sure I have not double-counted. Path D: `X ← F → C → Y`, traversing nodes X, F, C, Y. Path C: `X ← C → Y`, traversing nodes X, C, Y. These are different paths. Path D is *not* the same as Path C even though both pass through C.
- Path F: `X ← F → C → X` — this loops back to X, so it is not a path from X to Y. Skip.

So we have two open backdoor paths: Path C through C alone, and Path D through F and C.

**Q3 — choose an adjustment set that closes both without opening new ones.**

Candidate set 1: `{C}`. Does conditioning on C close Path C? Yes (C is a non-collider on Path C, conditioning on it blocks signal). Does conditioning on C close Path D? Yes (C is also on Path D as a non-collider). Does conditioning on C open any new path? No (C is not a collider on any path here, so no new path opens). **`{C}` is a valid adjustment set.**

Candidate set 2: `{F, C}`. Both closed, no new opening. **Valid.** But `{C}` already closed both paths; `F` is redundant. The set is valid but *not minimal*.

Candidate set 3: `{F}`. Does conditioning on F close Path C (`X ← C → Y`)? No — F does not lie on Path C. **Invalid.** Path C remains open.

Candidate set 4: `{M}`. Does conditioning on M close any backdoor path? `M` is not on Path C or Path D. **Invalid** as a backdoor adjustment — and worse, conditioning on `M` blocks part of the forward effect `X → M → Y`. We would be measuring the direct effect of `X` on `Y`, not the total effect. That distinction is Chapter 6's business; flag it now and we will be careful then.

Notice three things from this trace.

First, the procedure was mechanical. Once the DAG was on the table, the path enumeration and the close-or-open check ran themselves. A tool like DAGitty or `pgmpy` will perform this enumeration for you. ([DAGitty](https://www.dagitty.net/); van der Zander, Liśkiewicz, & Textor introduced the algorithm in 2014, "Constructing Separators and Adjustment Sets in Ancestral Graphs," in *UAI 2014*.)

Second, multiple adjustment sets were valid. `{C}` worked. `{F, C}` worked. The valid set is *not unique*. This matters in practice — Athey, Tibshirani, and Wager noted that heterogeneous-treatment-effect estimates from causal forests can move materially across defensible-looking adjustment sets. ([Athey, Tibshirani & Wager, 2019, *Annals of Statistics*](https://doi.org/10.1214/18-AOS1709)) When that happens, the choice between valid sets becomes its own identification-layer judgment.

Third, the procedure depended on the DAG. Every step. The path enumeration depended on which edges existed. The "is this variable a collider on this path?" check depended on edge directions. Change the DAG and every answer changes. The DAG, in turn, did not come from the data. The data showed correlations. The data did not show which variable was upstream of which. That is the question the engineer answers using domain knowledge — the question this book exists to ask.

---

## 4. Concept three — Valid adjustment sets, and why bigger isn't better

The naive rule from the regression world is *control for everything you can measure*. The structural framework says: bigger is not better. Sometimes bigger is worse.

Schisterman, Cole, and Platt published a clean treatment of this in 2009 in *Epidemiology*, in a paper called "Overadjustment Bias and Unnecessary Adjustment in Epidemiologic Studies." ([Schisterman, Cole, & Platt, 2009](https://doi.org/10.1097/EDE.0b013e3181a819a1)) Their point in plain English: adjusting for variables that are not on a backdoor path between treatment and outcome can be wasteful (more variance, no bias reduction) or actively harmful (introduce bias that was not there before).

Three failure modes get you "actively harmful." The structural mechanism for each is different, and each is the subject of a later chapter, but you should have the headlines now.

**Failure mode 1 — adjusting for a mediator.** If the variable is on a forward path from treatment to outcome (`X → M → Y`), conditioning on it blocks the part of the causal effect that flows through it. You end up estimating the direct effect only. If your question was about the total effect, you have answered the wrong question. (Chapter 6.)

**Failure mode 2 — adjusting for a collider.** If the variable is a common *effect* of two other variables on the path, conditioning on it opens a path that was previously closed. The classic example: hospital admission is caused by injury severity and by insurance status; conditioning on the hospitalized subset induces a spurious negative association between severity and insurance even when none exists in the population. (Chapter 7.)

**Failure mode 3 — adjusting for an instrument.** If the variable affects treatment but does not affect outcome except through treatment, conditioning on it can amplify bias from any *unmeasured* confounding that remains. Pearl calls this *Z-bias*. The effect is counterintuitive enough that engineers often discover it by accident — the more controls they add, the less stable the estimate becomes. (Chapter 10.)

The unifying lesson: an adjustment set is valid if every backdoor path is closed *and* no new path is opened. Both clauses matter. Forget the second, and you can adjust your way into worse estimates than you started with.

This is also where the dispute between Pearl-camp and Hernán-camp lives. Miguel Hernán and James Robins, in *What If* Ch. 18 ([Hernán & Robins, 2020](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)), defend a pragmatic engineering-grade rule: *adjust for any pre-treatment common cause of treatment and outcome.* Their argument is that this rule is usually safe, that the M-bias structures where it fails are rare in real epidemiological problems, and that worrying about M-bias in the rare case is less costly than the routine confounding you fail to control if you wait for the DAG to be perfect.

The Pearl camp pushes back that "usually safe" is not a foundation; that the moment you adopt a heuristic, you have given up the ability to detect when the heuristic fails; and that the few cases where M-bias matters are exactly the cases where the analyst most wants the structural framework. ([VanderWeele & Shpitser, 2013](https://doi.org/10.1214/12-AOS1058))

My reading: both camps are right about most of the cases and both camps are arguing in good faith about the edge. The structural framework lets you *see* whether you are in the edge case or not. The heuristic does not. For an engineering reader whose models will be audited, deployed at scale, and revisited under hostile questioning, I want the framework — even when the heuristic would have sufficed nine times out of ten. The tenth time is the time that ends up in *Reuters*. The dispute is real; do not pretend it is settled; pick the tool for the job.

Note one practical implication. The algorithms that enumerate minimal adjustment sets — the ones inside DAGitty and `pgmpy` — *find* sets given the DAG. They do not *write* the DAG for you. The hard part is the input. The chapter's recurring move is to make the input visible.

---

## 5. Concept four — Unmeasured confounders with bias direction

Now the move that distinguishes this chapter from a regression class.

You are at the whiteboard. The DAG is up. You have written down every variable you measured. You have run the three diagnostic questions. You have a valid adjustment set. The procedure says you are done.

Then a domain expert walks in. The expert points at empty space on the whiteboard, between treatment and outcome, and says: "There is a variable here. I cannot give you a column for it. It exists. It pushes treatment in one direction and outcome in another. Your estimate is biased."

That is the move only a domain expert can make. The data does not contain the variable. The model cannot infer it. The identification-layer claim — *U exists, U → X is positive, U → Y is positive, therefore the naive estimate of X's effect on Y is biased upward* — is a claim only the expert can write down.

Let me show this work explicitly.

Consider the simplest unmeasured-confounder structure:

```
        U
      /   \
     +     +
    ↓       ↓
    X ──→ Y
```

The `+` next to each edge says: *when U increases, the variable at the end of the arrow tends to increase, holding other inputs fixed.* (This is a *monotonic* assumption — the relationship is in one consistent direction across the range of U. Non-monotonic relationships are harder; we will pick them up in Chapter 14 with sensitivity analysis. For now stay in the monotonic case.) Suppose we estimate the effect of `X` on `Y` from the data — say we run a regression of `Y` on `X` and get a coefficient `β̂`. The naive estimate `β̂` decomposes into the true causal effect plus a confounding term:

`β̂ = β_true + (covariance contribution from the path X ← U → Y)`

The covariance contribution along `X ← U → Y` carries the *product* of the two edge signs. Both edges positive → contribution positive → `β̂` is biased *upward* relative to `β_true`. One edge positive and one negative → contribution negative → `β̂` is biased *downward*. (This is the monotonic-case version of an argument Sander Greenland laid out carefully in "Quantifying biases in causal models," *Epidemiology*, 2003 — and his 1986 paper with Robins set up the formal machinery. ([Greenland & Robins, 1986](https://doi.org/10.1093/ije/15.3.413)))

That sign claim — "biased upward" — is the thing the data alone cannot make. The data can give you `β̂`. It cannot give you whether the bias adds or subtracts. The expert's claim about the signs of the edges does that.

Let me redo the Amazon recruiter case with the signs visible.

Treatment `X`: model recommends this résumé (1 = yes, 0 = no).
Outcome `Y`: realized one-year performance, however we measure it.
Unmeasured confounder `U`: candidate's industry network strength prior to applying.

- `U → X`: more network strength means more network-shaped résumé features (referrals visible, conference talks, GitHub contributions, all the things the model rewards). Sign: positive.
- `U → Y`: more network strength means more post-hire support, faster onboarding, better internal mentorship, higher rated performance. Sign: positive.

Both edges positive → product positive → naive `β̂` for `X` on `Y` is biased *upward*. The model's apparent recommend-to-performance link is partly real causal effect of the model's screening choices, and partly the inherited correlation with a variable nobody put in the dataset.

You should now be able to do this for any DAG with a named `U` and signed edges. The procedure has three steps:

1. Name the unmeasured `U`. (Domain knowledge.)
2. Sign each edge `U → X` and `U → Y`. (Domain knowledge.)
3. Multiply the signs. Positive product → bias upward. Negative product → bias downward.

Step 1 is the hardest. It is also the chapter's thesis. The variable is not on your spreadsheet. The expert has to be in the room. And the expert's claim is auditable: a hostile reviewer can disagree about whether `U` exists or about which sign each edge takes, and the disagreement becomes a research conversation rather than a model bug.

Chapter 14 will give you the quantitative follow-up — VanderWeele and Ding's E-value lets you ask *how strong* `U` would have to be on each edge to nullify your estimate. ([VanderWeele & Ding, 2017](https://doi.org/10.7326/M16-2607)) That is the empirical extension of the move you are learning here. The structural claim — `U` exists, edges signed thus, bias direction thus — has to come first. The number comes after.

---

## 6. Integration — The first identification-layer skill an algorithm does not perform

I want to gather what we just did and name what kind of skill it is.

You did four things across Sections 2–5. You replaced the correlation definition of confounder with the structural one. You learned to trace backdoor paths and apply three diagnostic questions. You learned the failure modes of the "control for everything" reflex. You learned to name an unmeasured confounder and assign a bias direction to it.

What kind of work is that? At every step, the *machinery* was either trivial or automatable. Trace paths: mechanical. Check open/closed: mechanical. Find minimal adjustment set given DAG: an algorithm. Compute bias direction given signs: arithmetic. Every piece of work after the DAG existed was either pencil-and-paper procedure or a function call.

But every piece of work *before* the DAG existed required something different. Writing down the variables. Drawing the arrows. Knowing which way each arrow points. Knowing whether to draw a particular arrow at all. Knowing that historical access to care is a parent of prior spending and not a child. Knowing that the supplier's financial health pushes capacity, not the other way. Knowing that the industry-network strength of a job candidate affects performance through channels nobody recorded in HR's database. None of that is in the data. None of that is in the algorithm. All of that is in the head of someone who has lived in the domain long enough to see how the variables generate each other.

This is the identification layer Chapter 4 named. Chapter 5 has now made it specific for the first time. *Variable selection* — the first failure mode on Chapter 4's taxonomy — is *confounder selection*, and confounder selection is the work the analyst does with the domain expert before the model is fit. Every chapter from here forward is going to add another skill that lives at this layer. Mediators next, then colliders, then instruments. The pattern repeats: each variable's role on the graph determines what the analyst should do with it, and each role requires structural knowledge the data cannot supply.

I want to give you one heuristic to take into your next analysis. When you finish writing down your candidate DAG, before you run anything, ask yourself one question: *What variable would the domain expert add if they were standing here?* If the answer is "I do not know any domain experts for this problem," that is a finding, not a setback. It tells you exactly which conversation needs to happen before the model ships.

---

## 7. Worked example — Obermeyer 2019 in full

I want to walk one case end to end. Obermeyer 2019 is the cleanest engineering-domain confounder case I know, and the public reanalysis means we can show the work.

**Setup.** Optum's risk-prediction algorithm assigns risk scores to patients. Patients above a threshold get referred to high-risk care management programs — extra clinical attention. Treatment `T`: enrolled in the high-risk program. Outcome `Y`: health outcomes over the following year.

**Question.** What is the effect of enrollment on health outcomes? Or, as the deployer would phrase it: how much does the program help?

**Variables measured in the algorithm's training data:**
- Demographic features.
- Prior healthcare spending (the algorithm's chief input).
- Prior diagnoses, claims.
- Whatever else Optum had in its claims data.

**Variables not measured, named by clinicians:**
- *A* — historical access to healthcare. The patient's neighborhood, insurance trajectory, transportation access, language access at clinics, the cumulative effect of decades of differential clinical attention.
- *I* — true underlying illness severity, the thing you actually want to identify and treat.

**Initial DAG, before audit:**

```
              A (access)
            /      \
           ↓        ↓
       (race)     (spending) ──→ (algorithm score) ──→ T ──→ Y
                                                              ↑
                                                              I (illness)
                                                              ↑
                                                              A
```

Let me redraw this as a list of edges so it is unambiguous.

1. `A → race`? No — race is upstream of access in most demographic readings; let me redraw. `race → A` (historical patterns of access are caused in part by race through structural mechanisms outside this DAG).
2. `A → spending` (lower historical access produced lower historical spending even at similar illness).
3. `A → I` (lower historical access produced higher accumulated illness over time).
4. `spending → algorithm_score` (the algorithm's mechanism).
5. `algorithm_score → T` (the threshold rule).
6. `T → Y` (the effect we want to estimate).
7. `I → Y` (illness affects future health regardless of treatment).
8. `I → spending` (sicker people spend more).

**Run the three diagnostic questions for the effect of T on Y.**

Backdoor paths from T to Y? A backdoor path must start with an arrow into T. The only arrow into T is `algorithm_score → T`. So every backdoor path passes back through `algorithm_score`, then through `spending`, then up through `A` and `I`, and finally down into Y. Let me enumerate the open ones.

- Path P1: `T ← algorithm_score ← spending ← I → Y`. Backdoor (Q1: yes). Open? I is a fork on this path; spending and algorithm_score are chains. None conditioned on. **Open.** Conclusion: must close.
- Path P2: `T ← algorithm_score ← spending ← A → I → Y`. Backdoor. A is a fork; I is a chain. **Open.** Must close.
- Path P3: `T ← algorithm_score ← spending ← A → ... wait, is there an A → Y path that does not go through I?` Inspect: in my DAG, no. A reaches Y only through I. So P2 is the only A-routed open path.

**Valid adjustment sets.**

Candidate set `{spending}`. Does conditioning on `spending` close P1? Spending is on P1 as a chain (`algorithm_score ← spending ← I`). Conditioning on a non-collider in a chain closes that segment. So yes — P1 closes. Does it close P2? Spending is also on P2 as a chain (`algorithm_score ← spending ← A`). Closes. Does conditioning on `spending` open a new path? Spending is not a collider on any path here, so no. **`{spending}` is a valid adjustment set in this DAG.**

But here is the thing. This DAG presumes `spending` is measured and `I` and `A` are not. *Within this DAG*, adjusting for spending closes the visible backdoors. The estimate you compute is unbiased *given this DAG is correct*.

It is not correct.

The clinician's audit move: there is a direct arrow `A → I` that does not pass through `spending`. Historical access affects illness through channels other than spending — through delayed diagnosis, through under-treatment of chronic conditions, through the stress effects of inaccessible care. If `A → I` is a direct edge (not mediated through spending), then conditioning on spending does *not* close the path `T ← algorithm_score ← spending ← A → I → Y` — because that path is no longer the path. The real path is `T ← algorithm_score ← spending → (close here) ← A → I → Y`, with a direct `A → I` jump. Conditioning on spending blocks the segment from spending leftward, but the path can be redrawn: `T ← algorithm_score ← (mechanism) ← A → I → Y`, where the mechanism is the algorithm's reliance on spending as a proxy. The structural rewrite reveals that `A` is the *real* confounder, and `spending` is part of the algorithm's mechanism for being fooled by `A`.

**The bias-direction analysis.**

Sign the edges on the open path `T ← (algorithm score mechanism) ← A → I → Y` from `T` back to `Y` through `A`:

- `A → algorithm_score` (via spending): historically lower-access patients had lower spending and therefore *lower* algorithm scores at the same true illness level. So as `A` decreases (less access), algorithm score decreases — they push in the same direction. Sign of the effect of `A` on `T` (through the algorithm): positive.
- `A → I`: less access leads to more illness. As `A` decreases (less access), `I` increases. Sign: negative.
- `I → Y`: more illness leads to worse health. Sign: negative.

Multiplying signs along the path: positive × negative × negative = positive. The naive estimate of the program's effect is biased *upward* — but wait, more carefully: the algorithm's *assignment* mechanism is what we are auditing, not the program's effect, and the question to ask of the algorithm is whether its risk score tracks `I` or whether it tracks `I` mixed with `A`. Obermeyer's reanalysis showed that the algorithm tracked something closer to `spending`, which is `I`-modulated-by-`A`. At the same risk score, patients with lower `A` had higher true `I`. The bias of the algorithm's allocation: *under-allocation to patients with low historical access.* Quantified by the paper: from 17.7% Black patients in the high-risk group to 46.5% in the re-calibrated allocation.

**The lesson the case teaches.**

The DAG that the engineering team used did not have a node for `A`. The variable was unmeasured. It was *namable* by anyone who had read the literature on healthcare disparities — anyone who had spent time in clinic. It was missable by anyone who optimized inside the boundaries of the training data. The engineering work that closed the gap, in the published correction, was not "improve the model architecture." It was "expand the DAG." Add the node, redraw the arrows, see the open backdoor, adjust differently. The fix lived at the identification layer.

I will say this directly because it matters: the team that built this algorithm was not negligent in the loose sense. They had built a sensible-looking proxy for need. The structural failure was invisible from inside the data they had. It became visible only when domain reasoning about access pulled the new variable onto the DAG. That is the move every engineering team will need to make on the next high-stakes model. That is the work nobody else does for you.

---

## 8. Chapter summary

What you can do at the end of this chapter that you could not do at the start:

- **State the structural definition** of a confounder — common cause occupying a position on an open backdoor path — and explain why the correlation-based definition fails in real cases.
- **Trace backdoor paths** on a DAG using three diagnostic questions: is the path a backdoor, is it currently open, will a candidate adjustment set close every open backdoor without opening new ones.
- **Find valid adjustment sets** for a treatment–outcome pair, recognize that valid sets are not unique, and prefer minimal sets that close backdoors without inflating variance or introducing collider bias.
- **Name an unmeasured confounder** in a problem in your own domain. Assign signs to its arrows. State the implied bias direction in the naive estimate.
- **See the limit of automated tools** — DAGitty and `pgmpy` find adjustment sets given a DAG; they do not give you the DAG. The DAG is the artifact of the identification-layer conversation between analyst and domain expert.

This is the first toolkit-building chapter of Act Two, and it is the first chapter that gives you something concrete to do on Monday. Take a model you already work with. Draw a small DAG around it. Run the three diagnostic questions. Name one unmeasured confounder. Sign the bias direction. The exercise will take you under an hour. The conversations it provokes with the domain experts on your team are the actual artifact.

---

## 9. Bridge to Chapter 6

A reader who has paid close attention has a problem.

In Section 3 the program-enrollment DAG had a variable `M` — the checkpoint upgrades — that was on a path from treatment to outcome. I told you adjusting for `M` would block part of the causal effect, and we set it aside. In Section 7 I drew an Obermeyer DAG where `spending` was both downstream of `A` and an input to the algorithm — partly a mediator of the bias, partly itself measured.

The pattern: some variables on the path from `X` to `Y` are confounders to be controlled away. Some are mediators carrying the actual effect we want to measure. They can be hard to distinguish by inspection. They are easy to distinguish if you know the DAG. But how do you decide which variable is which, before you condition on it?

That is Chapter 6.

A mediator is a variable through which the treatment exerts its effect — `X → M → Y`. A confounder is a common cause — `M ← U → Y`. Sometimes the same variable plays one role on one path and the other role on another. The graph tells you. The data does not. Next chapter we will work out the distinction precisely and learn what happens if you condition on a mediator when you meant to condition on a confounder, or vice versa.

The short preview: conditioning on a confounder removes bias. Conditioning on a mediator removes effect. The two operations look identical in code and produce opposite errors.

---

## Exercises

**Warm-up.**

1. **(Apply)** Given the DAG with edges `U → X`, `U → Y`, `Z → X`, `X → M`, `M → Y`, `Z → Y`, list every path from `X` to `Y`. Classify each as a directed (causal) path or a backdoor path. Identify the open backdoor paths if no variables are conditioned on.

2. **(Apply)** Using the same DAG, propose a minimal adjustment set for the effect of `X` on `Y`. Defend the choice using the three diagnostic questions. State explicitly which paths your adjustment closes and confirm no new paths open.

**Application (Part A).**

3. **(Analyze)** Find a published causal claim from an ML or applied-statistics paper — anything from a recent issue of *JMLR*, *AISTATS*, *NeurIPS*, or *Operations Research*. Identify the confounders the authors adjusted for. Propose one confounder they did *not* adjust for and explain whether you think the adjustment set is sufficient. Cite the paper. State whether your proposed addition is measured in the paper's dataset or unmeasured.

**Application (Part B — own domain).**

4. **(Analyze)** Pick a treatment–outcome pair from a model you have worked on (or one in your current role). Draw the DAG. Identify the measured variables and the candidate adjustment set. Then name one *unmeasured* confounder. Assign signs to its two edges (treatment side and outcome side). State the implied bias direction in the naive estimate. This exercise becomes the first artifact in your Defend-Your-DAG portfolio in Chapter 11.

**Synthesis.**

5. **(Analyze)** Chapter 4 named three identification failure types: wrong variables, wrong functional form, wrong conditioning. Which of those failure types are addressed by today's confounder work? Which are not addressed and require later chapters? Give an example of each, drawing on cases from this chapter where possible.

**Challenge.**

6. **(Evaluate)** Read Obermeyer et al. 2019 carefully. ([DOI: 10.1126/science.aax2342](https://doi.org/10.1126/science.aax2342)) The authors' reanalysis adjusted for an alternative target variable — illness severity rather than cost. Express their fix in this chapter's vocabulary. Did they change the adjustment set? Did they change the outcome? Did they change the DAG? Give a one-paragraph answer that uses the structural language taught here. Note any places where the paper's framing and this chapter's framing diverge and say which you find more useful for an engineering reader and why.

---

## LLM exercise

Open Claude, ChatGPT, or Gemini. Paste this prompt exactly.

```
I am building a causal analysis. The treatment variable is [PICK ONE: a new
supplier-quality program enrollment / a new pricing-policy rollout in a
specific region / a model-recommended candidate hire / a credit-line-increase
decision]. The outcome variable is [PICK CORRESPONDING: on-time delivery
rate / revenue per session / 12-month performance review / 24-month default
rate].

Please give me:
(1) A list of at least five candidate confounders for this analysis.
(2) For each, state whether you believe it is typically measured or
unmeasured in industry datasets.
(3) For any you mark as unmeasured, sign the two edges (effect on treatment,
effect on outcome) and state the implied bias direction in the naive estimate.

Be specific about what could cause your sign assignments to be wrong.
```

Now critique what you get back. The LLM will produce a plausible-looking list. For each candidate:

- Is it *structurally* a confounder (common cause), or is it merely correlated with treatment and outcome? Apply the three diagnostic questions on your own.
- Is the LLM's sign assignment defensible, or is it guessing from generic priors?
- For the unmeasured ones: would your team be able to name this variable to a domain expert? Would the expert agree it is the right unmeasured variable to worry about?

Write a one-paragraph note on where the LLM was useful (probably: enumeration breadth) and where it was not (probably: domain-specific sign claims, knowledge of which variables your industry actually measures). Save the note for your portfolio.

---

## AI Use Disclosure (Part A standard form)

Per the course's AI Use Disclosure standard:

1. Name the LLM(s) used and the date of each session.
2. State which exercises you used an LLM for and what you used it for in each.
3. For each LLM-generated claim that survived into your final submission, state the source you used to verify it.
4. For each LLM-generated claim that did not survive, state briefly why you removed it.

**Part B bonus criterion:** Submissions naming a specific unmeasured confounder *with bias direction* in their own domain receive Part B credit. The named variable must (a) be plausibly real in the domain, (b) carry signed edges to both treatment and outcome, and (c) imply a stated bias direction (upward, downward, or — for non-monotonic relationships — flagged as Chapter 14 work).

---

## Key terms

- **Confounder** — a variable occupying a common-cause position relative to treatment and outcome on a DAG. Structurally defined; correlation is a consequence, not a definition.
- **Backdoor path** — any path between treatment and outcome that starts with an arrow *into* treatment. Backdoor paths are the routes through which non-causal association can flow.
- **Adjustment set** — a set of variables you condition on in order to close every open backdoor path without opening new ones. Valid adjustment sets are not unique.
- **Common cause** — a variable that has arrows into two other variables. The simplest confounder structure.
- **Bias direction** — the sign (upward, downward) of the difference between the naive estimate and the true causal effect, determined by the product of the signs of edges along the open backdoor path under monotonic assumptions.
- **Unmeasured confounder** — a variable that occupies a confounder position but is not present in the dataset. The expert can name it and sign its edges; the algorithm cannot infer it.
- **Overadjustment** — controlling for a variable that is not a confounder, in a way that introduces bias rather than removes it. The non-confounder may be a mediator, a collider, an instrument, or a descendant of one of these.
- **Minimal adjustment set** — a valid adjustment set such that no proper subset is also valid. Multiple minimal sets can exist for the same DAG.

---

## Further reading

1. **VanderWeele, T. J., & Shpitser, I. (2013).** "On the definition of a confounder." *Annals of Statistics* 41(1), 196–220. [https://doi.org/10.1214/12-AOS1058](https://doi.org/10.1214/12-AOS1058). The canonical paper for the structural definition; mathematically careful, philosophically clean. Read after Sections 2–3 of this chapter for the formal version.

2. **Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019).** "Dissecting racial bias in an algorithm used to manage the health of populations." *Science* 366(6464), 447–453. [https://doi.org/10.1126/science.aax2342](https://doi.org/10.1126/science.aax2342). The case Section 7 walks. The supplementary materials show the reanalysis numerically.

3. **Hernán, M. A., & Robins, J. M. (2020).** *Causal Inference: What If*, Chapters 7 and 18. [Free PDF](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/). The contemporary epidemiology treatment of confounder selection. Read Chapter 18 for the pragmatic-heuristic argument against pure structural identification; read it next to VanderWeele & Shpitser 2013 to see the dispute live.

4. **Schisterman, E. F., Cole, S. R., & Platt, R. W. (2009).** "Overadjustment Bias and Unnecessary Adjustment in Epidemiologic Studies." *Epidemiology* 20(4), 488–495. [https://doi.org/10.1097/EDE.0b013e3181a819a1](https://doi.org/10.1097/EDE.0b013e3181a819a1). Short, decisive, and the right antidote to the "control for everything" reflex.

5. **Pearl, J. (2009).** *Causality: Models, Reasoning, and Inference*, 2nd ed., Section 3.3, "The Back-Door Criterion." The formal statement of the criterion we approximated here. Chapter 9 will return to it in full.

---

## Draft flags

- `[verify-URL-stability]` — Reuters URL for Dastin 2018 has been unstable historically. If the link rots, cite as: Dastin, J. (2018, October 10). "Insight: Amazon scraps secret AI recruiting tool that showed bias against women." Reuters. (Archive copies on archive.org may be needed.)
- `[verify-pedagogical-priority]` — The "three diagnostic questions" phrasing in Section 3 may be original to this chapter rather than canonical. Pearl, Hernán-Robins, and Greenland-Robins teach the same machinery in adjacent language; if the phrasing is original, it should be flagged as such in the book's introduction.
- `voice-anchored: partial` — Root `style/VOICE.md` is the fry-voice spec; this chapter is written in the feynman default voice. No per-book style folder exists for `causal-reasoning`. The chapter relied on §6 of CLAUDE.md and the explicit feynman-voice directive in the chapter brief.

---

**What would change my mind:** If a careful re-reading of VanderWeele & Shpitser 2013 alongside Hernán-Robins Ch. 18 showed that the M-bias edge cases are essentially absent from engineering-domain DAGs at the level of detail engineers actually draw, I would soften the chapter's preference for the structural framework and let the pragmatic heuristic carry more of the weight.

**Still puzzling:** I do not yet fully understand how to teach the bias-direction step to students whose domain involves non-monotonic relationships — pricing, dosing, anything U-shaped — without sending them straight to sensitivity analysis. The monotonic case is clean; the non-monotonic case is harder than the chapter admits.

---

**Tags:** confounder, backdoor-path, adjustment-set, Obermeyer-2019, identification-layer
