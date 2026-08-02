═══════════════════════════════════════
FORMATTED VERSION (Markdown)
═══════════════════════════════════════

# Chapter 3: Confounding and Adjustment


## TL;DR

- ═══════════════════════════════════════ FORMATTED VERSION (Markdown) ═══════════════════════════════════════.
- The chapter moves through A drug that helps everyone but hurts everyone, What you'll be able to do by the end of this chapter, What you should already have, What confounding actually is, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

## A drug that helps everyone but hurts everyone

Here is a table. It describes a clinical trial of a drug for some disease. Two hundred patients. Half took the drug, half didn't. The outcome is whether they recovered.

|                | Recovered | Did not | Total | Rate |
|----------------|-----------|---------|-------|------|
| **Men, drug**      | 4         | 6       | 10    | 40%  |
| **Men, no drug**   | 54        | 36      | 90    | 60%  |
| **Women, drug**    | 72        | 18      | 90    | 80%  |
| **Women, no drug** | 9         | 1       | 10    | 90%  |
| **All, drug**      | 76        | 24      | 100   | 76%  |
| **All, no drug**   | 63        | 37      | 100   | 63%  |

Look at the drug in men alone. Forty percent of drug-takers recover; sixty percent of non-takers recover. Twenty points worse on the drug.

Look at the drug in women alone. Eighty percent of drug-takers recover; ninety percent of non-takers recover. Ten points worse on the drug.

Now look at the drug across everyone. Seventy-six percent of drug-takers recover; sixty-three percent of non-takers recover. Thirteen points *better* on the drug.

The drug is bad for men. The drug is bad for women. The drug is good for people. What does the drug actually do?

You might think this is a trick of arithmetic. It isn't. The numbers are correct. This is a real phenomenon. It has a name — Simpson's paradox — and more importantly, it has no statistical resolution. I can't tell you what the drug does by looking at the data. Neither can you. Neither can any statistical test ever invented.

To know what the drug does, I need one more thing. I need to know how the data were generated. I need the causal diagram.

Here is diagram one. Gender affects whether someone takes the drug (suppose doctors prescribed it more to women because early evidence suggested a gender-specific effect), and gender also affects recovery (women in this disease recover more easily regardless of treatment). In this diagram, gender is a *confounder*. It creates a spurious association between drug and recovery. The honest effect of the drug is the one you see after stratifying by gender. Within each gender, the drug is worse. The drug is bad.

Here is diagram two. The third column isn't gender at all — it's blood pressure, measured after taking the drug. The drug lowers blood pressure, and blood pressure affects recovery. Now the third variable is a *mediator*. It lies on the causal pathway from drug to recovery. Stratifying by it destroys the very effect we're trying to measure. The honest effect of the drug is the overall one. The drug is good.

Same numbers. Two diagrams. Opposite conclusions. The data will never tell you which diagram is right. You have to bring the diagram to the data.

That is what this chapter is about. Confounding, adjustment, and the diagram that makes the difference between "the drug works" and "the drug kills."

<!-- FIGURE: Two DAGs side by side. Left: G → X, G → Y, X → Y (G is gender, X is drug, Y is recovery) — G is a confounder. Right: X → Z → Y (X is drug, Z is blood pressure, Y is recovery) — Z is a mediator. Caption: The same data table is consistent with both diagrams. Only the causal structure, not the numbers, tells you which variable to adjust for. -->

### What you'll be able to do by the end of this chapter

- **Identify** a confounder in a causal diagram — and distinguish it from a mediator, a collider, and a plain irrelevant variable.
- **Apply** the back-door criterion to find a valid adjustment set for the causal effect of one variable on another.
- **Recognize** the three most common adjustment mistakes: conditioning on a mediator, conditioning on a collider, and M-bias.
- **Compute** an adjusted causal effect from data when given a sufficient set of deconfounders, using stratification.
- **Diagnose** when no valid adjustment set exists from the observed variables, and know what that tells you about which method to reach for next.

### What you should already have

You should have the material from Chapter 1 (the fundamental problem of causal inference, potential outcomes) and Chapter 2 (directed acyclic graphs, d-separation, paths, forks, chains, and colliders). If the words *fork*, *chain*, and *collider* don't mean anything to you yet, go back to Chapter 2. This chapter is where those tools finally do useful work, and you need them sharp.

---

## 1. What confounding actually is

Forget the word "confounding" for a minute. It's a technical term that people use to sound serious, and it obscures the simple thing underneath.

Here is the simple thing. When I observe a correlation between two variables — say, drug and recovery — that correlation could come from several sources:

1. The drug causes recovery. (This is what I want to know.)
2. Recovery causes the drug. (Impossible here: you recover *after* the drug. But in observational studies, reverse causation happens.)
3. Something else causes both the drug and recovery.
4. I've conditioned on something I shouldn't have, manufacturing a correlation out of nothing.

Confounding is option three. A confounder is a variable that causes both the treatment and the outcome. When it exists and you don't account for it, the correlation you observe between treatment and outcome is a mixture of two things — the real causal effect and a bookkeeping artifact produced by the confounder.

In diagram form: X → Y is the causal effect. The confounder Z gives you Z → X and Z → Y, which creates a second path X ← Z → Y. This second path is non-causal. It's a *back-door path* — a route from treatment to outcome that doesn't go through the causal mechanism you care about.

The association between X and Y that you measure in the data is the sum of the signal flowing down X → Y and the noise flowing along X ← Z → Y. You cannot separate them by staring at X and Y alone. You can only separate them by doing something about Z.

**Why does this matter for how you read the world?** Because almost every correlation anyone ever tells you about — in the news, in a paper, in a casual conversation — is measured without accounting for the confounders. People who eat more vegetables live longer. People who exercise get fewer colds. Kids whose parents read to them do better in school. Each of these is true as a correlation, and each of them has obvious confounders (income, general health-consciousness, parental attention in domains unrelated to reading). The correlation isn't a lie. It's just not the causal effect. It's the causal effect plus an unknown amount of confounding.

The whole project of causal inference from observational data can be summarized in one sentence: *find out how much of the observed correlation is causal and how much is the confounder talking.*

**A concrete example.** Consider the well-known observation that hormone replacement therapy (HRT) appeared to protect women from heart disease, based on decades of observational studies. Women on HRT had significantly lower rates of heart disease than women not on HRT. The correlation was real and robust.

Then the Women's Health Initiative ran a randomized trial in 2002 and found the opposite: HRT *increased* heart disease risk.

The observational studies weren't measurement errors. They were confounded. Women who took HRT in the 1980s and 1990s were disproportionately health-conscious, higher-income, better-educated, and better-connected to medical care — all of which independently lower heart disease risk. "Health-consciousness" was a fork: it caused both HRT use and lower heart disease. Remove the fork, and the protective effect vanishes. Run a randomized trial where the fork is broken, and the true causal effect comes out the opposite direction.

This is what confounding does. It isn't subtle and it isn't rare. It's the default. The question is never "is there confounding?" — there almost always is — but "what are the confounders, and can we account for them?"

**The design question.** Why is this the first real tool of causal inference? Because the alternatives are worse. Running an experiment is ideal but often impossible — ethically, practically, or both. You can't randomize people to smoke for twenty years. You can't randomize countries to different economic policies. You can't randomize children to different parents. When experiments are impossible, observational data is what we have, and confounding is the reason observational data doesn't give you the causal effect for free.

Confounding is the field's foundational problem. Every other method in this book — adjustment, instrumental variables, regression discontinuity, difference-in-differences — is a different answer to the same question: *how do I subtract the confounder's contribution from the correlation I see?* Adjustment, which we'll build next, is the most direct answer. When it works, it's clean and simple. When it doesn't, the diagram tells you why, and the other methods exist to handle the cases where adjustment breaks down.

---

## 2. The back-door criterion

Now that we know what confounding is, we need a rule for identifying which variables to adjust for. Not all variables in the data are confounders. Some are mediators (and adjusting for them destroys the effect). Some are colliders (and adjusting for them manufactures bias from nothing). Some are irrelevant. A rule that says "control for everything you measured" is catastrophically wrong, and I'll show you why in the next section.

The rule we want is Pearl's back-door criterion. I'll state it, then walk through it.

**The back-door criterion.** To estimate the causal effect of $X$ on $Y$, find a set of variables $Z$ such that:

(a) $Z$ blocks every back-door path from $X$ to $Y$, and
(b) $Z$ contains no descendants of $X$.

When such a $Z$ exists and you have measurements of it, you can compute the causal effect of $X$ on $Y$ by adjusting for $Z$. The causal effect is identified.

Let me unpack this.

**A back-door path** from $X$ to $Y$ is any path between them that starts with an arrow *into* $X$. The defining feature of a back-door path is that it doesn't start at $X$ by leaving through $X$'s own outgoing arrows — it sneaks up on $X$ from behind.

<!-- LATEX: X \leftarrow Z \rightarrow Y -->

<!-- FIGURE: A simple DAG with three nodes X, Y, Z and arrows Z→X, Z→Y, X→Y. The path X ← Z → Y is highlighted as a back-door path. Caption: A back-door path starts with an arrow pointing into X. It doesn't carry causal signal from X to Y — it carries spurious association. -->

Why does this matter? Because paths that leave $X$ through its outgoing arrows carry the causal signal we want to measure — X's effects on the world. Paths that arrive at $X$ through incoming arrows carry *other* causes of $X$, and if those other causes also affect $Y$, we get spurious association.

**Blocking a path** means making it so that information doesn't flow along it. From Chapter 2: a path is blocked by conditioning on a variable $Z$ along the path if either the path goes X ... → Z → ... Y (chain — conditioning blocks it) or X ... ← Z → ... Y (fork — conditioning blocks it). A path is blocked *without conditioning* if it contains a collider that hasn't been conditioned on. Conditioning on a collider (or its descendant) *unblocks* the path — this is where the collider fallacy comes from.

**Clause (b)** — $Z$ contains no descendants of $X$ — is the guard against the mediator fallacy. Descendants of $X$ are variables that $X$ causes. If I condition on something $X$ causes, I'm conditioning on part of $X$'s effect. Some of the causal signal from $X$ to $Y$ flows through the descendant, and conditioning on it removes that signal from my estimate. I've subtracted a part of the real effect in the name of adjustment.

**Applying the criterion — a simple case.** Suppose I want the effect of a drug $X$ on recovery $Y$, and I observe gender $G$. Gender affects drug prescription (doctors prescribed more to women in this example) and gender affects recovery. The DAG is:

<!-- LATEX: G \to X, \quad G \to Y, \quad X \to Y -->

Paths from $X$ to $Y$:
- $X \to Y$. This is the causal path. I want its contribution.
- $X \leftarrow G \to Y$. This is a back-door path (it starts with an arrow into $X$).

To block the back-door path, I need a set that includes a non-collider on the path. The only non-$X$, non-$Y$ variable on this path is $G$. Conditioning on $G$ blocks the fork $X \leftarrow G \to Y$.

Is $G$ a descendant of $X$? No — the arrow goes $G \to X$, not $X \to G$.

So $Z = \{G\}$ satisfies the back-door criterion. Adjusting for gender gives me the causal effect. In the Simpson's paradox example from the opening, this is exactly the calculation that said the drug is bad — because gender was truly a confounder.

**A harder case.** Suppose now the third variable is not gender but blood pressure, $B$, measured *after* taking the drug. The drug lowers blood pressure; blood pressure affects recovery. The DAG is:

<!-- LATEX: X \to B \to Y -->

Paths from $X$ to $Y$:
- $X \to Y$. The direct causal path.
- $X \to B \to Y$. An indirect causal path — also part of the drug's effect on recovery.

Are there any back-door paths? No. No arrows point *into* $X$ in this diagram.

What if I tried to condition on $B$ anyway, thinking it looked like a confounder because it correlates with both $X$ and $Y$? $B$ is a descendant of $X$ — clause (b) rules it out. Good. Because if I had conditioned on $B$, I would have closed the indirect causal path $X \to B \to Y$ and underestimated the drug's total effect. Possibly, I'd find no effect at all and conclude the drug doesn't work.

The back-door criterion protects me from this mistake. It says: don't condition on something the treatment causes.

**A harder case still.** Real diagrams have many variables, and it's not always obvious whether a variable is ancestor, descendant, confounder, mediator, or collider. Consider:

<!-- LATEX: A \to X, \quad A \to M, \quad M \to Y, \quad X \to Y -->

Paths from $X$ to $Y$:
- $X \to Y$. Causal.
- $X \leftarrow A \to M \to Y$. Back-door (starts with arrow into $X$).

To block the back-door path, I can condition on $A$ (a fork on the path) or $M$ (a chain node on the path). Both work as *path-blockers*. But:

- $A$ is not a descendant of $X$. ✓
- $M$ is... let me check. Is there an arrow from $X$ to $M$? No. From anything $X$ causes to $M$? No. $M$ is not a descendant of $X$. ✓

So *both* $Z = \{A\}$ and $Z = \{M\}$ satisfy the back-door criterion. Either works. This is a general feature of the criterion — often multiple valid adjustment sets exist, and which you choose is a matter of convenience, statistical efficiency, or which variables you actually measured.

**The practical punchline.** The back-door criterion is a mechanical procedure. Draw the DAG. List the back-door paths (anything into $X$). Find a set that blocks all of them without including descendants of $X$. That set is a valid adjustment set. If you can find one, the causal effect is identified and you can compute it from observational data.

The criterion is also why the DAG matters so much. The same data, analyzed under two different DAGs, can give opposite answers — because the DAGs disagree about which paths are back-door paths and which variables are descendants of $X$. The Simpson's paradox example in the opening is exactly this. In diagram one, the third variable is on a back-door path. In diagram two, it's a descendant of $X$. The criterion gives different answers. The data doesn't care.

---

## 3. Adjustment as a computation

We have a rule for finding a valid $Z$. Now I'll show you how to actually compute the causal effect once you have one.

The raw form of adjustment — the version without any parametric assumptions — is called *stratification* or *standardization*. It is conceptually the cleanest form, and every fancier method is a computational shortcut for the same idea.

**The formula.** Let $X$ be a binary treatment (0 or 1), $Y$ the outcome, and $Z$ a set of deconfounders that satisfies the back-door criterion. The causal effect of $X$ on $Y$, written in potential outcomes notation as $E[Y^{X=1}] - E[Y^{X=0}]$ or in do-notation as $E[Y|do(X=1)] - E[Y|do(X=0)]$, is given by:

<!-- LATEX: E[Y | do(X=x)] = \sum_{z} E[Y | X=x, Z=z] \, P(Z=z) -->

In words: for each value of the confounder $Z$, compute the conditional average of $Y$ given $X=x$ and $Z=z$. Weight each stratum's average by the marginal probability of $Z=z$ (not the conditional probability given treatment). Sum.

That last point is the whole trick. In the raw data, when you compute $E[Y|X=1]$ you're implicitly weighting by $P(Z=z | X=1)$ — the distribution of $Z$ among the treated. This reflects the confounding — treated people have a different distribution of $Z$ than untreated people. Adjustment replaces that weighting with $P(Z=z)$, the marginal distribution of $Z$ across everyone. You force the treated and untreated groups to have the *same* distribution of $Z$ by reweighting. Once the two groups are comparable on $Z$, the difference in outcomes is the causal effect.

**Worked example — back to the drug.** Return to the table from the opening. $X$ is drug (0 or 1), $Y$ is recovery (0 or 1), $Z$ is gender. Assume the causal diagram is the first one — gender is a confounder.

Step one. Compute the stratum-specific treatment effects.

Within men: $E[Y|X=1, Z=\text{man}] = 0.40$. $E[Y|X=0, Z=\text{man}] = 0.60$. Effect in men: $0.40 - 0.60 = -0.20$.

Within women: $E[Y|X=1, Z=\text{woman}] = 0.80$. $E[Y|X=0, Z=\text{woman}] = 0.90$. Effect in women: $0.80 - 0.90 = -0.10$.

Step two. Compute $P(Z)$, the marginal distribution of gender. One hundred men (10 + 90) and one hundred women (90 + 10) — half each. $P(\text{man}) = 0.5$, $P(\text{woman}) = 0.5$.

Step three. Weighted average.

<!-- LATEX: \text{ATE} = (-0.20)(0.5) + (-0.10)(0.5) = -0.15 -->

The adjusted causal effect: the drug decreases recovery by fifteen percentage points. It's bad.

Compare to the unadjusted effect: drug-takers recover at 76%, non-takers at 63%. Unadjusted: $+0.13$. The drug looks beneficial by thirteen points. Adjusted: $-0.15$. Nearly thirty points of swing. The entire impression reverses.

This is not a rhetorical flourish. This is what confounding does. In this example, adjustment flipped the sign.

**Sanity check.** Does the adjusted effect make sense? It should be close to a weighted average of the within-stratum effects. Weight within-men effect of $-0.20$ by 0.5 and within-women effect of $-0.10$ by 0.5: average $-0.15$. ✓

**Generalization — continuous outcomes.** If $Y$ is continuous (a test score, a blood pressure measurement) the formula is the same. Within each stratum, compute the mean of $Y$ among treated and among untreated. Take the difference. Weight each stratum's difference by $P(Z=z)$. Sum.

**Generalization — continuous confounders.** If $Z$ is continuous, the sum becomes an integral, and "stratify by $Z$" becomes "bin $Z$ into small intervals and average across bins." In practice with continuous confounders, stratification becomes data-hungry quickly — you need enough treated and untreated observations *within every stratum* to get a reliable estimate. This is where regression adjustment enters: instead of non-parametrically estimating $E[Y|X=x, Z=z]$ in every bin, we fit a parametric model (say, linear regression of $Y$ on $X$ and $Z$) and use the model's predictions. Regression adjustment is the same computation as stratification, executed with a parametric assumption to smooth across the sparse regions of $Z$-space.

And propensity score methods (Chapter 5) are the same idea once more, with a different shortcut. Instead of stratifying on $Z$ directly, you stratify on a one-dimensional summary — the probability of treatment given $Z$. A deep theorem (Rosenbaum and Rubin, 1983) shows this works. The three methods — stratification, regression adjustment, propensity scores — are three faces of the same computation: reweight the treated and untreated groups so they have matching distributions of the confounders, then compare.

**Design philosophy.** Why does the field teach stratification first, even though practitioners mostly use regression or propensity scores? Because stratification makes the confounding-versus-adjustment idea transparent. You can see the weights. You can see why the adjusted effect differs from the unadjusted one. You can see the assumption being made — that within each stratum, treated and untreated are comparable. When you move to regression, the reweighting happens implicitly through the coefficients, and it becomes possible to do the adjustment *correctly* without understanding it. That's dangerous. A practitioner who doesn't understand stratification will not recognize when regression is reweighting over a region of covariate space that has no treated (or no untreated) observations — a situation called lack of *positivity* or *overlap*, where the causal effect is *not* identified, regardless of how happy the regression software looks.

The order I teach in is the order that makes the assumptions visible. Regression is faster. Stratification is clearer. For learning, clarity wins.

---

## 4. Three ways to get adjustment wrong

A back-door criterion that rejects the wrong variables is only half the discipline. You also have to resist adjusting for variables that *look* like confounders but aren't. There are three classic mistakes, and they account for the majority of errors in published observational research. Learn to spot them.

### The mediator fallacy

A mediator is a variable on the causal pathway from $X$ to $Y$. $X \to M \to Y$. Some (or all) of the effect of $X$ on $Y$ flows through $M$.

Conditioning on a mediator blocks the causal path. Any effect that flowed through $M$ disappears from the estimate. If the entire effect flows through $M$, adjusting for $M$ makes the effect vanish completely.

**Concrete case.** A researcher studies whether a job-training program increases income. She has data on participants and non-participants, along with their employment status one year later. She reasons: "I should control for whether they're employed, because employment affects income."

She fits the model: $\text{Income} = \beta_0 + \beta_1 \text{Training} + \beta_2 \text{Employed} + \varepsilon$.

She finds $\beta_1 \approx 0$. She concludes the training has no effect on income.

What happened? The training's main effect on income is through employment — training helps people get jobs, jobs produce income. By controlling for employment, she's asking "among people with the same employment status, does training change income?" If training's mechanism *is* helping people get employed, the within-employment-status comparison shows almost nothing. The training didn't fail. The adjustment destroyed the effect.

The back-door criterion would have caught this. Employment is a descendant of training — $\text{Training} \to \text{Employed}$. Clause (b) says don't include descendants of $X$ in $Z$. The researcher violated clause (b).

**The harder version.** It's not always so obvious. A variable measured *after* treatment is suspicious by default, but post-treatment timing isn't sufficient — you need the DAG to know whether the variable is a mediator (don't adjust) or a confounder of some downstream effect (maybe adjust, carefully). The safest default: if a variable is potentially on the causal pathway, don't adjust for it when estimating the total effect of $X$ on $Y$. If you want to isolate the effect *not* flowing through $M$ (the "direct effect"), you're doing mediation analysis, which is a different and more delicate task — and one where the assumptions are much stronger.

### The collider fallacy

A collider is a variable with two arrows pointing into it. $X \to C \leftarrow Y$, or more generally, a variable that two different causal paths converge on.

By default, a path through a collider is *blocked*. Conditioning on a collider *unblocks* it, creating a non-causal association between its parents. This is the opposite of what conditioning usually does, and it catches people by surprise.

**Concrete case — Berkeley admissions, 1973.** Graduate admissions data at UC Berkeley showed that men were admitted at a rate of 44% and women at 35% — a nine-point gap that looked like gender discrimination. Reanalysis by Bickel, Hammel, and O'Connell (1975) showed that when you looked department by department, most departments either admitted men and women at roughly equal rates, or favored women slightly. The overall gap was an artifact of which departments men and women applied to. Women disproportionately applied to highly competitive departments (low acceptance rates overall), while men disproportionately applied to less competitive ones.

Here's the DAG. Gender affects department choice. Department affects admission rate. Gender, in this story, does *not* directly affect admission rate within a department.

<!-- LATEX: \text{Gender} \to \text{Department} \to \text{Admission} -->

In this diagram, department is a mediator for any effect of gender on admission. The total effect of gender *flows through department choice*. If you want to measure whether the university is discriminating *in admissions decisions*, you should condition on department — and if you do, the discrimination mostly disappears, because department-specific admission rates weren't biased against women.

But there's a second story, and this is where colliders enter. Suppose we also think both gender and admission-worthiness (unobserved, but real) independently affect which department someone applies to. Competitive departments attract both the most-qualified applicants and, disproportionately, men. Now department is a collider on the path $\text{Gender} \to \text{Department} \leftarrow \text{Qualifications} \to \text{Admission}$. Conditioning on department opens this path and creates an artificial association between gender and qualifications — *within a department*, women might appear less qualified than men (because the men who applied there were unusually strong, while the women were more representative), or more, depending on the direction.

The lesson is not that we should or shouldn't adjust for department in the Berkeley case. The lesson is that *you cannot tell* from the data alone. The DAG you believe determines whether department is a mediator (don't adjust if you want the total effect) or a collider in some path (adjust creates bias).

### M-bias

M-bias is the case that catches experts off-guard, because it looks like an obvious confounder and is actually a collider.

<!-- FIGURE: An M-shaped DAG. Nodes A (upper left), B (upper right), M (center), X (lower left), Y (lower right). Arrows: A → M, B → M, A → X, B → Y, X → Y. Caption: M looks like a pre-treatment variable that might be a confounder — it's measured before X, and correlates with both X and Y. But M is a collider between A and B. Conditioning on it opens the path A → M ← B, creating a non-causal association between A and B that flows through to X and Y. -->

Read the diagram carefully. $M$ is measured before treatment $X$. $M$ correlates with $X$ (through $A$). $M$ correlates with $Y$ (through $B$). Every classical rule of thumb for identifying a confounder — "a variable measured before treatment that correlates with both treatment and outcome" — flags $M$ as a confounder.

It is not a confounder. It is a collider in the path $A \to M \leftarrow B$.

Look at the back-door paths from $X$ to $Y$:
- $X \leftarrow A \to M \leftarrow B \to Y$. This path contains the collider $M$.

Is this path open or closed? A path through an unconditioned collider is *closed* by default. So this path doesn't transmit spurious association. $A$ and $B$ are uncorrelated (they have no common cause in the diagram), and since $M$ is a collider, information from the $A$-side doesn't leak to the $B$-side.

But if I "control for $M$" — if I include it in my regression, if I stratify by it, if I match on it — I condition on the collider. The path opens. A non-causal association between $A$ and $B$ is now active, and that association induces a non-causal association between $X$ and $Y$ that flows through $A$ and $B$.

The adjustment I made to "control for a potential confounder" *created* bias that wasn't there before.

**Why generations of statisticians got this wrong.** Before the DAG framework, the classical definition of a confounder was distributional: a pre-treatment variable associated with both treatment and outcome. By that definition, $M$ is a confounder. People taught "control for potential confounders" as a general principle, and $M$ was the kind of variable they meant. The causal diagram shows that this advice, applied without thinking, is wrong — sometimes destructively so.

M-bias is rare enough in practice that most analyses don't trigger it, but when it does occur, it's invisible without the DAG. This is one of the cleanest arguments for why the field needed to adopt causal diagrams: without them, you cannot distinguish a confounder from a collider, and the cost of the confusion is adjusting yourself into a wrong answer.

### What if no valid adjustment set exists?

Sometimes no combination of observed variables blocks every back-door path. There's a back-door path through an unobserved variable, and nothing you measured sits on it in a way that blocks it. The back-door criterion returns no valid $Z$.

This does not mean causal inference is impossible. It means *adjustment* is not the right tool for this problem, and trying to force an adjustment with the variables you have will give you a biased answer while looking statistically fine.

The honest response is to reach for a different method. If there's an instrument — a variable that affects treatment but has no direct effect on outcome — use instrumental variables (Chapter 6). If there's a threshold in treatment assignment that creates local randomization — use regression discontinuity (Chapter 7). If you have repeated observations over time and the confounding is stable — use difference-in-differences (Chapter 8). The diagram that tells you adjustment won't work usually also tells you which method will.

The worst response, and unfortunately a common one, is to adjust for the variables you have anyway, report the number, and hope. This gives a confidence interval around a biased estimate, which is the statistical equivalent of a confident wrong answer.

---

## 5. Putting it all together: one worked case

Consider a retrospective observational study of a new surgical technique. $X$ is whether a patient received the new technique (versus the standard). $Y$ is survival at one year.

The observed variables are: age, sex, hospital volume (how many of these surgeries the hospital does per year), surgeon experience (years practicing), pre-operative disease severity (a composite score), and post-operative complications (yes or no).

Draw the DAG you believe. Here's one plausible version, built from clinical reasoning:

- Age affects disease severity, probability of receiving the new technique (older patients less likely), and survival directly.
- Sex affects survival.
- Hospital volume affects probability of offering the new technique and affects survival (high-volume centers have better outcomes generally).
- Surgeon experience affects both probability of using the new technique and survival.
- Disease severity affects probability of receiving the new technique and survival.
- Post-operative complications are caused by the surgery (new or standard) and affect survival.

Which variables should I adjust for?

**Back-door paths from $X$ (technique) to $Y$ (survival):**
- $X \leftarrow \text{Age} \to Y$. Open fork. Need to block.
- $X \leftarrow \text{Age} \to \text{Severity} \to Y$. Open. Need to block.
- $X \leftarrow \text{Hospital volume} \to Y$. Open. Need to block.
- $X \leftarrow \text{Surgeon experience} \to Y$. Open. Need to block.
- $X \leftarrow \text{Severity} \to Y$. Open. Need to block.

**Candidate adjustment set.** $Z = \{\text{Age, Hospital volume, Surgeon experience, Severity}\}$.

Does this block all back-door paths? Yes — every back-door path has either age, hospital volume, surgeon experience, or severity on it as a non-collider, and conditioning on that variable blocks the path.

Does $Z$ contain any descendants of $X$? Age, no. Hospital volume, no. Surgeon experience, no. Severity... this one's borderline. Severity is measured *pre-operatively*, so it's pre-treatment, so it's not a descendant of $X$. ✓

What about sex? Sex affects $Y$ but in this DAG doesn't affect $X$. No back-door path runs through sex. Adjusting for sex is optional — it doesn't bias the estimate, but it also isn't required by the back-door criterion. In practice, adjusting for sex can improve statistical precision even when it isn't required for identification; this is one of the legitimate reasons to include a variable beyond the minimal adjustment set.

What about post-operative complications? They are caused by $X$ (the surgery causes complications or doesn't). That makes them a descendant of $X$. Clause (b) says don't include them. If I had adjusted for complications — common in published studies, because it "sounds relevant" — I would have conditioned on a mediator and possibly a collider, and my estimate would be biased. The back-door criterion protects me.

So the final answer: adjust for age, hospital volume, surgeon experience, and pre-operative severity. Don't adjust for post-operative complications. Sex is optional.

This is what working with the back-door criterion feels like in practice. Draw the DAG. Enumerate the paths. Decide which ones to block. Check the descendant rule. The DAG does the thinking — your job is to have drawn it honestly.

---

## A note about AI

Confounding is the most-named threat in observational research and the most-fudged. The model has read every adjustment strategy and will recommend them confidently for problems it does not understand.

Where the model genuinely helps: enumerating the canonical confounders for a known study type, and the standard adjustment moves for each.

Where the model does damage: declaring an analysis adequately adjusted. Adequacy depends on whether the adjustments capture the actual confounding structure, which depends on substantive knowledge the model approximates rather than holds.

The rule: confounder catalog from the model; the claim that adjustment is sufficient is for the analyst defending the study.

---

## Exercises

Solutions are not provided here. That's deliberate. If you want to check your answers, build the DAG in your head, write down the paths, apply the criterion, and see whether your answer satisfies it. That process is the skill. Having the answer handed to you doesn't build it.

### Warm-up: mechanical application of definitions

**Exercise 3.1.** *(Objective: identify variable types)*
In the diagram $A \to B \to C$, identify $B$'s role in the relationship between $A$ and $C$. Is $B$ a confounder, mediator, collider, or none of these?

**Exercise 3.2.** *(Objective: recognize back-door paths)*
In the diagram $X \leftarrow Z \to Y$, $X \to Y$, list all back-door paths from $X$ to $Y$.

**Exercise 3.3.** *(Objective: compute stratified adjustment)*
Using the Simpson's paradox table from the chapter opening, compute the adjusted effect of the drug on recovery under the confounder diagram. Then compute it under the assumption that the third variable is a mediator. Confirm you get $-0.15$ and $+0.13$ respectively.

### Application: using the concepts on new problems

**Exercise 3.4.** *(Objective: apply back-door criterion)*
Draw a DAG with four variables: $X$ (treatment), $Y$ (outcome), $A$ (affects $X$ and $Y$), and $M$ (caused by $X$, causes $Y$). List all back-door paths from $X$ to $Y$. Find a valid adjustment set. Verify it satisfies both clauses of the back-door criterion.

**Exercise 3.5.** *(Objective: spot the mediator fallacy)*
A study reports that a new medication has no effect on five-year cardiovascular mortality, after adjusting for cholesterol levels measured one year after treatment initiation. What's wrong with this analysis? Draw the DAG you believe and explain which clause of the back-door criterion is violated.

**Exercise 3.6.** *(Objective: spot the collider fallacy)*
In a hospital-based study, researchers find that diabetes is negatively associated with influenza severity. Patients with diabetes in this sample have milder flu than patients without. They conclude diabetes is protective against severe flu. Hospital-based samples condition on admission. What collider structure might explain this finding? (Hint: consider why a patient ends up in the hospital in the first place.)

**Exercise 3.7.** *(Objective: recognize M-bias)*
Given the DAG $A \to X$, $A \to M$, $B \to M$, $B \to Y$, $X \to Y$, should you adjust for $M$ when estimating the effect of $X$ on $Y$? Justify in terms of the back-door criterion. What is the nature of the error if you do adjust for it?

### Synthesis: combining concepts across the chapter

**Exercise 3.8.** *(Objective: diagnose an adjustment analysis)*
A researcher studies the effect of graduate education ($X$) on lifetime earnings ($Y$). She has data on: pre-college standardized test scores, parental income, college major, undergraduate GPA, and first-job salary. For each variable, classify it as (a) a confounder to adjust for, (b) a mediator not to adjust for, (c) a collider not to adjust for, or (d) ambiguous without further assumptions. Justify each choice by sketching the plausible DAG.

**Exercise 3.9.** *(Objective: integrate back-door criterion with stratification)*
Given this data on job training and post-training income, with race as a putative confounder:

<!-- TABLE: Use Datawrapper embed instead. Table: Race × Training × Income bin. Within each stratum, show counts treated/untreated and mean income. -->

(Construct a synthetic version of this table yourself, with race balanced but training imbalanced across races.) Compute the unadjusted difference in income between trained and untrained. Then compute the race-adjusted difference by stratification. Explain what the difference between the two estimates tells you about the magnitude and direction of the confounding.

**Exercise 3.10.** *(Objective: recognize when adjustment isn't enough)*
A researcher wants to estimate the effect of neighborhood poverty on a child's educational outcomes. She has data on family income, parental education, and child's school quality. She suspects there's also an unobserved variable — family social networks — that affects both neighborhood choice and child outcomes and that she cannot measure. Can she identify the causal effect by adjustment alone? Explain using the back-door criterion. What methods from later chapters might she reach for instead?

### Challenge: open-ended or beyond-chapter

**Exercise 3.11.** *(Objective: extrapolate beyond the chapter)*
The back-door criterion is sufficient but not necessary for identification. Pearl's do-calculus provides a more general set of rules for when a causal effect can be identified from observational data, including via "front-door" paths. Sketch an example where the back-door criterion fails but a causal effect is still identified through a mediator on the front door. (Look up "front-door criterion" if you want a hint.) What does this tell you about the scope of adjustment as a tool?

**Exercise 3.12.** *(Objective: apply the material to your own work)*
Take a research question you care about — from your field, your job, or a news article you read recently that made a causal claim from observational data. Draw the DAG you believe. Identify the back-door paths. Determine whether a valid adjustment set exists among the variables that were or could plausibly have been measured. If yes, what would the adjusted analysis look like? If no, what would you need — different data, a different method, a different research design?

---

## Chapter summary

You walked in able to draw a DAG and reason about paths. You walk out able to do the following things you couldn't do before.

You can look at a correlation and ask: *which back-door paths are generating this association?* — then find the set of variables that closes those paths without destroying the signal you're trying to measure.

You can take a dataset and an assumed DAG, compute the causal effect by stratification, and explain why the answer differs from the raw correlation. You can do this by hand on a small example, and you can recognize what regression and propensity score methods are doing as computational shortcuts for the same operation.

You can spot the three classic mistakes — mediator conditioning, collider conditioning, and M-bias — and explain in each case which clause of the back-door criterion was violated.

You can identify when adjustment won't work and know that this is a signal to change methods, not a signal to force it.

**The one idea from this chapter that matters most**: *the data cannot tell you which variables to adjust for; the DAG does that, and the DAG is an assumption you make about how the world works.* Different DAGs on the same data give different answers. You have to choose.

**The common mistake to watch for.** Do not adjust for variables that look relevant because they correlate with both $X$ and $Y$. Correlation with both is not what makes something a confounder. Being on a back-door path and not being a descendant of $X$ is what makes something a legitimate target for adjustment. The distinction is invisible without the DAG. Draw it.

**The Feynman test.** Can you explain, to someone who has never studied causal inference, why the same drug trial data can mean opposite things depending on whether the third column is gender or blood pressure? If you can, you have the chapter. If not, go back to the opening and work it through until you can.

---

## Connections forward

This chapter gave you the theoretical rule — the back-door criterion — and the rawest computation — stratification. The next chapter is about what happens when your confounders are continuous and multidimensional, and stratification breaks down from data sparsity. We'll develop regression-based adjustment as a parametric shortcut that works when stratification can't, and we'll see exactly when that shortcut silently fails — the overlap problem, model misspecification, and extrapolation into regions with no data.

Chapter 5 takes the same idea again from a different angle: instead of summarizing the relationship between confounders and outcome, summarize the relationship between confounders and *treatment* — the propensity score. You'll see why this is sometimes more robust, sometimes less, and how the two strategies combine into what are called *doubly robust* estimators.

The later chapters — instrumental variables, regression discontinuity, difference-in-differences — are for the cases where the back-door criterion returns no valid set. When you can't close the back-door paths with the variables you have, you need another door in or another way to isolate the effect. The rule for choosing the right alternative method always returns to the DAG. Every time you reach for one of those tools, you're reaching for it because the diagram told you that adjustment alone won't do.

---

═══════════════════════════════════════
SUBSTACK HTML (Copy-Paste Ready)
═══════════════════════════════════════

<!-- Manual steps needed:
  1. Insert opening data table — recommend Datawrapper embed (Simpson's paradox table)
  2. Insert Exercise 3.9 table — recommend Datawrapper embed
  3. Insert figures (marked <!-- FIGURE: ... --> in text): 3 figures total
  4. Insert LaTeX equations (marked <!-- LATEX: ... -->): render in Substack's math block
-->

<h2>Chapter 3: Confounding and Adjustment</h2>

<h3>A drug that helps everyone but hurts everyone</h3>

<p>Here is a table. It describes a clinical trial of a drug for some disease. Two hundred patients. Half took the drug, half didn't. The outcome is whether they recovered.</p>

<!-- TABLE: Use Datawrapper embed instead. Columns: Stratum, Recovered, Did not, Total, Rate. Rows: Men/drug (4/6/10/40%), Men/no drug (54/36/90/60%), Women/drug (72/18/90/80%), Women/no drug (9/1/10/90%), All/drug (76/24/100/76%), All/no drug (63/37/100/63%). -->

<p>Look at the drug in men alone. Forty percent of drug-takers recover; sixty percent of non-takers recover. Twenty points worse on the drug.</p>

<p>Look at the drug in women alone. Eighty percent of drug-takers recover; ninety percent of non-takers recover. Ten points worse on the drug.</p>

<p>Now look at the drug across everyone. Seventy-six percent of drug-takers recover; sixty-three percent of non-takers recover. Thirteen points <em>better</em> on the drug.</p>

<p>The drug is bad for men. The drug is bad for women. The drug is good for people. What does the drug actually do?</p>

<p>You might think this is a trick of arithmetic. It isn't. The numbers are correct. This is a real phenomenon. It has a name — Simpson's paradox — and more importantly, it has no statistical resolution. I can't tell you what the drug does by looking at the data. Neither can you. Neither can any statistical test ever invented.</p>

<p>To know what the drug does, I need one more thing. I need to know how the data were generated. I need the causal diagram.</p>

<p>Here is diagram one. Gender affects whether someone takes the drug (suppose doctors prescribed it more to women because early evidence suggested a gender-specific effect), and gender also affects recovery (women in this disease recover more easily regardless of treatment). In this diagram, gender is a <em>confounder</em>. It creates a spurious association between drug and recovery. The honest effect of the drug is the one you see after stratifying by gender. Within each gender, the drug is worse. The drug is bad.</p>

<p>Here is diagram two. The third column isn't gender at all — it's blood pressure, measured after taking the drug. The drug lowers blood pressure, and blood pressure affects recovery. Now the third variable is a <em>mediator</em>. It lies on the causal pathway from drug to recovery. Stratifying by it destroys the very effect we're trying to measure. The honest effect of the drug is the overall one. The drug is good.</p>

<p>Same numbers. Two diagrams. Opposite conclusions. The data will never tell you which diagram is right. You have to bring the diagram to the data.</p>

<p>That is what this chapter is about. Confounding, adjustment, and the diagram that makes the difference between "the drug works" and "the drug kills."</p>

<!-- FIGURE: Two DAGs side by side. Left: G → X, G → Y, X → Y (G is gender, X is drug, Y is recovery) — G is a confounder. Right: X → Z → Y (X is drug, Z is blood pressure, Y is recovery) — Z is a mediator. Caption: The same data table is consistent with both diagrams. Only the causal structure, not the numbers, tells you which variable to adjust for. -->

<h4>What you'll be able to do by the end of this chapter</h4>

<ul>
  <li><strong>Identify</strong> a confounder in a causal diagram — and distinguish it from a mediator, a collider, and a plain irrelevant variable.</li>
  <li><strong>Apply</strong> the back-door criterion to find a valid adjustment set for the causal effect of one variable on another.</li>
  <li><strong>Recognize</strong> the three most common adjustment mistakes: conditioning on a mediator, conditioning on a collider, and M-bias.</li>
  <li><strong>Compute</strong> an adjusted causal effect from data when given a sufficient set of deconfounders, using stratification.</li>
  <li><strong>Diagnose</strong> when no valid adjustment set exists from the observed variables, and know what that tells you about which method to reach for next.</li>
</ul>

<h4>What you should already have</h4>

<p>You should have the material from Chapter 1 (the fundamental problem of causal inference, potential outcomes) and Chapter 2 (directed acyclic graphs, d-separation, paths, forks, chains, and colliders). If the words <em>fork</em>, <em>chain</em>, and <em>collider</em> don't mean anything to you yet, go back to Chapter 2. This chapter is where those tools finally do useful work, and you need them sharp.</p>

<hr>

<h3>1. What confounding actually is</h3>

<p>Forget the word "confounding" for a minute. It's a technical term that people use to sound serious, and it obscures the simple thing underneath.</p>

<p>Here is the simple thing. When I observe a correlation between two variables — say, drug and recovery — that correlation could come from several sources:</p>

<ol>
  <li>The drug causes recovery. (This is what I want to know.)</li>
  <li>Recovery causes the drug. (Impossible here: you recover <em>after</em> the drug. But in observational studies, reverse causation happens.)</li>
  <li>Something else causes both the drug and recovery.</li>
  <li>I've conditioned on something I shouldn't have, manufacturing a correlation out of nothing.</li>
</ol>

<p>Confounding is option three. A confounder is a variable that causes both the treatment and the outcome. When it exists and you don't account for it, the correlation you observe between treatment and outcome is a mixture of two things — the real causal effect and a bookkeeping artifact produced by the confounder.</p>

<p>In diagram form: X → Y is the causal effect. The confounder Z gives you Z → X and Z → Y, which creates a second path X ← Z → Y. This second path is non-causal. It's a <em>back-door path</em> — a route from treatment to outcome that doesn't go through the causal mechanism you care about.</p>

<p>The association between X and Y that you measure in the data is the sum of the signal flowing down X → Y and the noise flowing along X ← Z → Y. You cannot separate them by staring at X and Y alone. You can only separate them by doing something about Z.</p>

<p><strong>Why does this matter for how you read the world?</strong> Because almost every correlation anyone ever tells you about — in the news, in a paper, in a casual conversation — is measured without accounting for the confounders. People who eat more vegetables live longer. People who exercise get fewer colds. Kids whose parents read to them do better in school. Each of these is true as a correlation, and each of them has obvious confounders (income, general health-consciousness, parental attention in domains unrelated to reading). The correlation isn't a lie. It's just not the causal effect. It's the causal effect plus an unknown amount of confounding.</p>

<p>The whole project of causal inference from observational data can be summarized in one sentence: <em>find out how much of the observed correlation is causal and how much is the confounder talking.</em></p>

<p><strong>A concrete example.</strong> Consider the well-known observation that hormone replacement therapy (HRT) appeared to protect women from heart disease, based on decades of observational studies. Women on HRT had significantly lower rates of heart disease than women not on HRT. The correlation was real and robust.</p>

<p>Then the Women's Health Initiative ran a randomized trial in 2002 and found the opposite: HRT <em>increased</em> heart disease risk.</p>

<p>The observational studies weren't measurement errors. They were confounded. Women who took HRT in the 1980s and 1990s were disproportionately health-conscious, higher-income, better-educated, and better-connected to medical care — all of which independently lower heart disease risk. "Health-consciousness" was a fork: it caused both HRT use and lower heart disease. Remove the fork, and the protective effect vanishes. Run a randomized trial where the fork is broken, and the true causal effect comes out the opposite direction.</p>

<p>This is what confounding does. It isn't subtle and it isn't rare. It's the default. The question is never "is there confounding?" — there almost always is — but "what are the confounders, and can we account for them?"</p>

<p><strong>The design question.</strong> Why is this the first real tool of causal inference? Because the alternatives are worse. Running an experiment is ideal but often impossible — ethically, practically, or both. You can't randomize people to smoke for twenty years. You can't randomize countries to different economic policies. You can't randomize children to different parents. When experiments are impossible, observational data is what we have, and confounding is the reason observational data doesn't give you the causal effect for free.</p>

<p>Confounding is the field's foundational problem. Every other method in this book — adjustment, instrumental variables, regression discontinuity, difference-in-differences — is a different answer to the same question: <em>how do I subtract the confounder's contribution from the correlation I see?</em> Adjustment, which we'll build next, is the most direct answer. When it works, it's clean and simple. When it doesn't, the diagram tells you why, and the other methods exist to handle the cases where adjustment breaks down.</p>

<hr>

<h3>2. The back-door criterion</h3>

<p>Now that we know what confounding is, we need a rule for identifying which variables to adjust for. Not all variables in the data are confounders. Some are mediators (and adjusting for them destroys the effect). Some are colliders (and adjusting for them manufactures bias from nothing). Some are irrelevant. A rule that says "control for everything you measured" is catastrophically wrong, and I'll show you why in the next section.</p>

<p>The rule we want is Pearl's back-door criterion. I'll state it, then walk through it.</p>

<p><strong>The back-door criterion.</strong> To estimate the causal effect of X on Y, find a set of variables Z such that:</p>

<p>(a) Z blocks every back-door path from X to Y, and<br>
(b) Z contains no descendants of X.</p>

<p>When such a Z exists and you have measurements of it, you can compute the causal effect of X on Y by adjusting for Z. The causal effect is identified.</p>

<p>Let me unpack this.</p>

<p><strong>A back-door path</strong> from X to Y is any path between them that starts with an arrow <em>into</em> X. The defining feature of a back-door path is that it doesn't start at X by leaving through X's own outgoing arrows — it sneaks up on X from behind.</p>

<!-- LATEX: X \leftarrow Z \rightarrow Y -->

<!-- FIGURE: A simple DAG with three nodes X, Y, Z and arrows Z→X, Z→Y, X→Y. The path X ← Z → Y is highlighted as a back-door path. Caption: A back-door path starts with an arrow pointing into X. It doesn't carry causal signal from X to Y — it carries spurious association. -->

<p>Why does this matter? Because paths that leave X through its outgoing arrows carry the causal signal we want to measure — X's effects on the world. Paths that arrive at X through incoming arrows carry <em>other</em> causes of X, and if those other causes also affect Y, we get spurious association.</p>

<p><strong>Blocking a path</strong> means making it so that information doesn't flow along it. From Chapter 2: a path is blocked by conditioning on a variable Z along the path if either the path goes X ... → Z → ... Y (chain — conditioning blocks it) or X ... ← Z → ... Y (fork — conditioning blocks it). A path is blocked <em>without conditioning</em> if it contains a collider that hasn't been conditioned on. Conditioning on a collider (or its descendant) <em>unblocks</em> the path — this is where the collider fallacy comes from.</p>

<p><strong>Clause (b)</strong> — Z contains no descendants of X — is the guard against the mediator fallacy. Descendants of X are variables that X causes. If I condition on something X causes, I'm conditioning on part of X's effect. Some of the causal signal from X to Y flows through the descendant, and conditioning on it removes that signal from my estimate. I've subtracted a part of the real effect in the name of adjustment.</p>

<p><strong>Applying the criterion — a simple case.</strong> Suppose I want the effect of a drug X on recovery Y, and I observe gender G. Gender affects drug prescription (doctors prescribed more to women in this example) and gender affects recovery. The DAG is:</p>

<!-- LATEX: G \to X, \quad G \to Y, \quad X \to Y -->

<p>Paths from X to Y:</p>
<ul>
  <li>X → Y. This is the causal path. I want its contribution.</li>
  <li>X ← G → Y. This is a back-door path (it starts with an arrow into X).</li>
</ul>

<p>To block the back-door path, I need a set that includes a non-collider on the path. The only non-X, non-Y variable on this path is G. Conditioning on G blocks the fork X ← G → Y.</p>

<p>Is G a descendant of X? No — the arrow goes G → X, not X → G.</p>

<p>So Z = {G} satisfies the back-door criterion. Adjusting for gender gives me the causal effect. In the Simpson's paradox example from the opening, this is exactly the calculation that said the drug is bad — because gender was truly a confounder.</p>

<p><strong>A harder case.</strong> Suppose now the third variable is not gender but blood pressure, B, measured <em>after</em> taking the drug. The drug lowers blood pressure; blood pressure affects recovery. The DAG is:</p>

<!-- LATEX: X \to B \to Y -->

<p>Paths from X to Y:</p>
<ul>
  <li>X → Y. The direct causal path.</li>
  <li>X → B → Y. An indirect causal path — also part of the drug's effect on recovery.</li>
</ul>

<p>Are there any back-door paths? No. No arrows point <em>into</em> X in this diagram.</p>

<p>What if I tried to condition on B anyway, thinking it looked like a confounder because it correlates with both X and Y? B is a descendant of X — clause (b) rules it out. Good. Because if I had conditioned on B, I would have closed the indirect causal path X → B → Y and underestimated the drug's total effect. Possibly, I'd find no effect at all and conclude the drug doesn't work.</p>

<p>The back-door criterion protects me from this mistake. It says: don't condition on something the treatment causes.</p>

<p><strong>A harder case still.</strong> Real diagrams have many variables, and it's not always obvious whether a variable is ancestor, descendant, confounder, mediator, or collider. Consider:</p>

<!-- LATEX: A \to X, \quad A \to M, \quad M \to Y, \quad X \to Y -->

<p>Paths from X to Y:</p>
<ul>
  <li>X → Y. Causal.</li>
  <li>X ← A → M → Y. Back-door (starts with arrow into X).</li>
</ul>

<p>To block the back-door path, I can condition on A (a fork on the path) or M (a chain node on the path). Both work as <em>path-blockers</em>. But:</p>

<ul>
  <li>A is not a descendant of X. ✓</li>
  <li>M is... let me check. Is there an arrow from X to M? No. From anything X causes to M? No. M is not a descendant of X. ✓</li>
</ul>

<p>So <em>both</em> Z = {A} and Z = {M} satisfy the back-door criterion. Either works. This is a general feature of the criterion — often multiple valid adjustment sets exist, and which you choose is a matter of convenience, statistical efficiency, or which variables you actually measured.</p>

<p><strong>The practical punchline.</strong> The back-door criterion is a mechanical procedure. Draw the DAG. List the back-door paths (anything into X). Find a set that blocks all of them without including descendants of X. That set is a valid adjustment set. If you can find one, the causal effect is identified and you can compute it from observational data.</p>

<p>The criterion is also why the DAG matters so much. The same data, analyzed under two different DAGs, can give opposite answers — because the DAGs disagree about which paths are back-door paths and which variables are descendants of X. The Simpson's paradox example in the opening is exactly this. In diagram one, the third variable is on a back-door path. In diagram two, it's a descendant of X. The criterion gives different answers. The data doesn't care.</p>

<hr>

<h3>3. Adjustment as a computation</h3>

<p>We have a rule for finding a valid Z. Now I'll show you how to actually compute the causal effect once you have one.</p>

<p>The raw form of adjustment — the version without any parametric assumptions — is called <em>stratification</em> or <em>standardization</em>. It is conceptually the cleanest form, and every fancier method is a computational shortcut for the same idea.</p>

<p><strong>The formula.</strong> Let X be a binary treatment (0 or 1), Y the outcome, and Z a set of deconfounders that satisfies the back-door criterion. The causal effect of X on Y, written in potential outcomes notation as E[Y^{X=1}] − E[Y^{X=0}] or in do-notation as E[Y|do(X=1)] − E[Y|do(X=0)], is given by:</p>

<!-- LATEX: E[Y | do(X=x)] = \sum_{z} E[Y | X=x, Z=z] \, P(Z=z) -->

<p>In words: for each value of the confounder Z, compute the conditional average of Y given X=x and Z=z. Weight each stratum's average by the marginal probability of Z=z (not the conditional probability given treatment). Sum.</p>

<p>That last point is the whole trick. In the raw data, when you compute E[Y|X=1] you're implicitly weighting by P(Z=z | X=1) — the distribution of Z among the treated. This reflects the confounding — treated people have a different distribution of Z than untreated people. Adjustment replaces that weighting with P(Z=z), the marginal distribution of Z across everyone. You force the treated and untreated groups to have the <em>same</em> distribution of Z by reweighting. Once the two groups are comparable on Z, the difference in outcomes is the causal effect.</p>

<p><strong>Worked example — back to the drug.</strong> Return to the table from the opening. X is drug (0 or 1), Y is recovery (0 or 1), Z is gender. Assume the causal diagram is the first one — gender is a confounder.</p>

<p>Step one. Compute the stratum-specific treatment effects.</p>

<p>Within men: E[Y|X=1, Z=man] = 0.40. E[Y|X=0, Z=man] = 0.60. Effect in men: 0.40 − 0.60 = −0.20.</p>

<p>Within women: E[Y|X=1, Z=woman] = 0.80. E[Y|X=0, Z=woman] = 0.90. Effect in women: 0.80 − 0.90 = −0.10.</p>

<p>Step two. Compute P(Z), the marginal distribution of gender. One hundred men (10 + 90) and one hundred women (90 + 10) — half each. P(man) = 0.5, P(woman) = 0.5.</p>

<p>Step three. Weighted average.</p>

<!-- LATEX: \text{ATE} = (-0.20)(0.5) + (-0.10)(0.5) = -0.15 -->

<p>The adjusted causal effect: the drug decreases recovery by fifteen percentage points. It's bad.</p>

<p>Compare to the unadjusted effect: drug-takers recover at 76%, non-takers at 63%. Unadjusted: +0.13. The drug looks beneficial by thirteen points. Adjusted: −0.15. Nearly thirty points of swing. The entire impression reverses.</p>

<p>This is not a rhetorical flourish. This is what confounding does. In this example, adjustment flipped the sign.</p>

<p><strong>Sanity check.</strong> Does the adjusted effect make sense? It should be close to a weighted average of the within-stratum effects. Weight within-men effect of −0.20 by 0.5 and within-women effect of −0.10 by 0.5: average −0.15. ✓</p>

<p><strong>Generalization — continuous outcomes.</strong> If Y is continuous (a test score, a blood pressure measurement) the formula is the same. Within each stratum, compute the mean of Y among treated and among untreated. Take the difference. Weight each stratum's difference by P(Z=z). Sum.</p>

<p><strong>Generalization — continuous confounders.</strong> If Z is continuous, the sum becomes an integral, and "stratify by Z" becomes "bin Z into small intervals and average across bins." In practice with continuous confounders, stratification becomes data-hungry quickly — you need enough treated and untreated observations <em>within every stratum</em> to get a reliable estimate. This is where regression adjustment enters: instead of non-parametrically estimating E[Y|X=x, Z=z] in every bin, we fit a parametric model (say, linear regression of Y on X and Z) and use the model's predictions. Regression adjustment is the same computation as stratification, executed with a parametric assumption to smooth across the sparse regions of Z-space.</p>

<p>And propensity score methods (Chapter 5) are the same idea once more, with a different shortcut. Instead of stratifying on Z directly, you stratify on a one-dimensional summary — the probability of treatment given Z. A deep theorem (Rosenbaum and Rubin, 1983) shows this works. The three methods — stratification, regression adjustment, propensity scores — are three faces of the same computation: reweight the treated and untreated groups so they have matching distributions of the confounders, then compare.</p>

<p><strong>Design philosophy.</strong> Why does the field teach stratification first, even though practitioners mostly use regression or propensity scores? Because stratification makes the confounding-versus-adjustment idea transparent. You can see the weights. You can see why the adjusted effect differs from the unadjusted one. You can see the assumption being made — that within each stratum, treated and untreated are comparable. When you move to regression, the reweighting happens implicitly through the coefficients, and it becomes possible to do the adjustment <em>correctly</em> without understanding it. That's dangerous. A practitioner who doesn't understand stratification will not recognize when regression is reweighting over a region of covariate space that has no treated (or no untreated) observations — a situation called lack of <em>positivity</em> or <em>overlap</em>, where the causal effect is <em>not</em> identified, regardless of how happy the regression software looks.</p>

<p>The order I teach in is the order that makes the assumptions visible. Regression is faster. Stratification is clearer. For learning, clarity wins.</p>

<hr>

<h3>4. Three ways to get adjustment wrong</h3>

<p>A back-door criterion that rejects the wrong variables is only half the discipline. You also have to resist adjusting for variables that <em>look</em> like confounders but aren't. There are three classic mistakes, and they account for the majority of errors in published observational research. Learn to spot them.</p>

<h4>The mediator fallacy</h4>

<p>A mediator is a variable on the causal pathway from X to Y. X → M → Y. Some (or all) of the effect of X on Y flows through M.</p>

<p>Conditioning on a mediator blocks the causal path. Any effect that flowed through M disappears from the estimate. If the entire effect flows through M, adjusting for M makes the effect vanish completely.</p>

<p><strong>Concrete case.</strong> A researcher studies whether a job-training program increases income. She has data on participants and non-participants, along with their employment status one year later. She reasons: "I should control for whether they're employed, because employment affects income."</p>

<p>She fits the model: Income = β₀ + β₁ Training + β₂ Employed + ε.</p>

<p>She finds β₁ ≈ 0. She concludes the training has no effect on income.</p>

<p>What happened? The training's main effect on income is through employment — training helps people get jobs, jobs produce income. By controlling for employment, she's asking "among people with the same employment status, does training change income?" If training's mechanism <em>is</em> helping people get employed, the within-employment-status comparison shows almost nothing. The training didn't fail. The adjustment destroyed the effect.</p>

<p>The back-door criterion would have caught this. Employment is a descendant of training — Training → Employed. Clause (b) says don't include descendants of X in Z. The researcher violated clause (b).</p>

<p><strong>The harder version.</strong> It's not always so obvious. A variable measured <em>after</em> treatment is suspicious by default, but post-treatment timing isn't sufficient — you need the DAG to know whether the variable is a mediator (don't adjust) or a confounder of some downstream effect (maybe adjust, carefully). The safest default: if a variable is potentially on the causal pathway, don't adjust for it when estimating the total effect of X on Y. If you want to isolate the effect <em>not</em> flowing through M (the "direct effect"), you're doing mediation analysis, which is a different and more delicate task — and one where the assumptions are much stronger.</p>

<h4>The collider fallacy</h4>

<p>A collider is a variable with two arrows pointing into it. X → C ← Y, or more generally, a variable that two different causal paths converge on.</p>

<p>By default, a path through a collider is <em>blocked</em>. Conditioning on a collider <em>unblocks</em> it, creating a non-causal association between its parents. This is the opposite of what conditioning usually does, and it catches people by surprise.</p>

<p><strong>Concrete case — Berkeley admissions, 1973.</strong> Graduate admissions data at UC Berkeley showed that men were admitted at a rate of 44% and women at 35% — a nine-point gap that looked like gender discrimination. Reanalysis by Bickel, Hammel, and O'Connell (1975) showed that when you looked department by department, most departments either admitted men and women at roughly equal rates, or favored women slightly. The overall gap was an artifact of which departments men and women applied to. Women disproportionately applied to highly competitive departments (low acceptance rates overall), while men disproportionately applied to less competitive ones.</p>

<p>Here's the DAG. Gender affects department choice. Department affects admission rate. Gender, in this story, does <em>not</em> directly affect admission rate within a department.</p>

<!-- LATEX: \text{Gender} \to \text{Department} \to \text{Admission} -->

<p>In this diagram, department is a mediator for any effect of gender on admission. The total effect of gender <em>flows through department choice</em>. If you want to measure whether the university is discriminating <em>in admissions decisions</em>, you should condition on department — and if you do, the discrimination mostly disappears, because department-specific admission rates weren't biased against women.</p>

<p>But there's a second story, and this is where colliders enter. Suppose we also think both gender and admission-worthiness (unobserved, but real) independently affect which department someone applies to. Competitive departments attract both the most-qualified applicants and, disproportionately, men. Now department is a collider on the path Gender → Department ← Qualifications → Admission. Conditioning on department opens this path and creates an artificial association between gender and qualifications — <em>within a department</em>, women might appear less qualified than men (because the men who applied there were unusually strong, while the women were more representative), or more, depending on the direction.</p>

<p>The lesson is not that we should or shouldn't adjust for department in the Berkeley case. The lesson is that <em>you cannot tell</em> from the data alone. The DAG you believe determines whether department is a mediator (don't adjust if you want the total effect) or a collider in some path (adjust creates bias).</p>

<h4>M-bias</h4>

<p>M-bias is the case that catches experts off-guard, because it looks like an obvious confounder and is actually a collider.</p>

<!-- FIGURE: An M-shaped DAG. Nodes A (upper left), B (upper right), M (center), X (lower left), Y (lower right). Arrows: A → M, B → M, A → X, B → Y, X → Y. Caption: M looks like a pre-treatment variable that might be a confounder — it's measured before X, and correlates with both X and Y. But M is a collider between A and B. Conditioning on it opens the path A → M ← B, creating a non-causal association between A and B that flows through to X and Y. -->

<p>Read the diagram carefully. M is measured before treatment X. M correlates with X (through A). M correlates with Y (through B). Every classical rule of thumb for identifying a confounder — "a variable measured before treatment that correlates with both treatment and outcome" — flags M as a confounder.</p>

<p>It is not a confounder. It is a collider in the path A → M ← B.</p>

<p>Look at the back-door paths from X to Y:</p>
<ul>
  <li>X ← A → M ← B → Y. This path contains the collider M.</li>
</ul>

<p>Is this path open or closed? A path through an unconditioned collider is <em>closed</em> by default. So this path doesn't transmit spurious association. A and B are uncorrelated (they have no common cause in the diagram), and since M is a collider, information from the A-side doesn't leak to the B-side.</p>

<p>But if I "control for M" — if I include it in my regression, if I stratify by it, if I match on it — I condition on the collider. The path opens. A non-causal association between A and B is now active, and that association induces a non-causal association between X and Y that flows through A and B.</p>

<p>The adjustment I made to "control for a potential confounder" <em>created</em> bias that wasn't there before.</p>

<p><strong>Why generations of statisticians got this wrong.</strong> Before the DAG framework, the classical definition of a confounder was distributional: a pre-treatment variable associated with both treatment and outcome. By that definition, M is a confounder. People taught "control for potential confounders" as a general principle, and M was the kind of variable they meant. The causal diagram shows that this advice, applied without thinking, is wrong — sometimes destructively so.</p>

<p>M-bias is rare enough in practice that most analyses don't trigger it, but when it does occur, it's invisible without the DAG. This is one of the cleanest arguments for why the field needed to adopt causal diagrams: without them, you cannot distinguish a confounder from a collider, and the cost of the confusion is adjusting yourself into a wrong answer.</p>

<h4>What if no valid adjustment set exists?</h4>

<p>Sometimes no combination of observed variables blocks every back-door path. There's a back-door path through an unobserved variable, and nothing you measured sits on it in a way that blocks it. The back-door criterion returns no valid Z.</p>

<p>This does not mean causal inference is impossible. It means <em>adjustment</em> is not the right tool for this problem, and trying to force an adjustment with the variables you have will give you a biased answer while looking statistically fine.</p>

<p>The honest response is to reach for a different method. If there's an instrument — a variable that affects treatment but has no direct effect on outcome — use instrumental variables (Chapter 6). If there's a threshold in treatment assignment that creates local randomization — use regression discontinuity (Chapter 7). If you have repeated observations over time and the confounding is stable — use difference-in-differences (Chapter 8). The diagram that tells you adjustment won't work usually also tells you which method will.</p>

<p>The worst response, and unfortunately a common one, is to adjust for the variables you have anyway, report the number, and hope. This gives a confidence interval around a biased estimate, which is the statistical equivalent of a confident wrong answer.</p>

<hr>

<h3>5. Putting it all together: one worked case</h3>

<p>Consider a retrospective observational study of a new surgical technique. X is whether a patient received the new technique (versus the standard). Y is survival at one year.</p>

<p>The observed variables are: age, sex, hospital volume (how many of these surgeries the hospital does per year), surgeon experience (years practicing), pre-operative disease severity (a composite score), and post-operative complications (yes or no).</p>

<p>Draw the DAG you believe. Here's one plausible version, built from clinical reasoning:</p>

<ul>
  <li>Age affects disease severity, probability of receiving the new technique (older patients less likely), and survival directly.</li>
  <li>Sex affects survival.</li>
  <li>Hospital volume affects probability of offering the new technique and affects survival (high-volume centers have better outcomes generally).</li>
  <li>Surgeon experience affects both probability of using the new technique and survival.</li>
  <li>Disease severity affects probability of receiving the new technique and survival.</li>
  <li>Post-operative complications are caused by the surgery (new or standard) and affect survival.</li>
</ul>

<p>Which variables should I adjust for?</p>

<p><strong>Back-door paths from X (technique) to Y (survival):</strong></p>
<ul>
  <li>X ← Age → Y. Open fork. Need to block.</li>
  <li>X ← Age → Severity → Y. Open. Need to block.</li>
  <li>X ← Hospital volume → Y. Open. Need to block.</li>
  <li>X ← Surgeon experience → Y. Open. Need to block.</li>
  <li>X ← Severity → Y. Open. Need to block.</li>
</ul>

<p><strong>Candidate adjustment set.</strong> Z = {Age, Hospital volume, Surgeon experience, Severity}.</p>

<p>Does this block all back-door paths? Yes — every back-door path has either age, hospital volume, surgeon experience, or severity on it as a non-collider, and conditioning on that variable blocks the path.</p>

<p>Does Z contain any descendants of X? Age, no. Hospital volume, no. Surgeon experience, no. Severity... this one's borderline. Severity is measured <em>pre-operatively</em>, so it's pre-treatment, so it's not a descendant of X. ✓</p>

<p>What about sex? Sex affects Y but in this DAG doesn't affect X. No back-door path runs through sex. Adjusting for sex is optional — it doesn't bias the estimate, but it also isn't required by the back-door criterion. In practice, adjusting for sex can improve statistical precision even when it isn't required for identification; this is one of the legitimate reasons to include a variable beyond the minimal adjustment set.</p>

<p>What about post-operative complications? They are caused by X (the surgery causes complications or doesn't). That makes them a descendant of X. Clause (b) says don't include them. If I had adjusted for complications — common in published studies, because it "sounds relevant" — I would have conditioned on a mediator and possibly a collider, and my estimate would be biased. The back-door criterion protects me.</p>

<p>So the final answer: adjust for age, hospital volume, surgeon experience, and pre-operative severity. Don't adjust for post-operative complications. Sex is optional.</p>

<p>This is what working with the back-door criterion feels like in practice. Draw the DAG. Enumerate the paths. Decide which ones to block. Check the descendant rule. The DAG does the thinking — your job is to have drawn it honestly.</p>

<hr>

<h3>Exercises</h3>

<p>Solutions are not provided here. That's deliberate. If you want to check your answers, build the DAG in your head, write down the paths, apply the criterion, and see whether your answer satisfies it. That process is the skill. Having the answer handed to you doesn't build it.</p>

<h4>Warm-up: mechanical application of definitions</h4>

<ol>
  <li><strong>Exercise 3.1.</strong> <em>(Objective: identify variable types)</em> In the diagram A → B → C, identify B's role in the relationship between A and C. Is B a confounder, mediator, collider, or none of these?</li>
  <li><strong>Exercise 3.2.</strong> <em>(Objective: recognize back-door paths)</em> In the diagram X ← Z → Y, X → Y, list all back-door paths from X to Y.</li>
  <li><strong>Exercise 3.3.</strong> <em>(Objective: compute stratified adjustment)</em> Using the Simpson's paradox table from the chapter opening, compute the adjusted effect of the drug on recovery under the confounder diagram. Then compute it under the assumption that the third variable is a mediator. Confirm you get −0.15 and +0.13 respectively.</li>
</ol>

<h4>Application: using the concepts on new problems</h4>

<ol start="4">
  <li><strong>Exercise 3.4.</strong> <em>(Objective: apply back-door criterion)</em> Draw a DAG with four variables: X (treatment), Y (outcome), A (affects X and Y), and M (caused by X, causes Y). List all back-door paths from X to Y. Find a valid adjustment set. Verify it satisfies both clauses of the back-door criterion.</li>
  <li><strong>Exercise 3.5.</strong> <em>(Objective: spot the mediator fallacy)</em> A study reports that a new medication has no effect on five-year cardiovascular mortality, after adjusting for cholesterol levels measured one year after treatment initiation. What's wrong with this analysis? Draw the DAG you believe and explain which clause of the back-door criterion is violated.</li>
  <li><strong>Exercise 3.6.</strong> <em>(Objective: spot the collider fallacy)</em> In a hospital-based study, researchers find that diabetes is negatively associated with influenza severity. Patients with diabetes in this sample have milder flu than patients without. They conclude diabetes is protective against severe flu. Hospital-based samples condition on admission. What collider structure might explain this finding? (Hint: consider why a patient ends up in the hospital in the first place.)</li>
  <li><strong>Exercise 3.7.</strong> <em>(Objective: recognize M-bias)</em> Given the DAG A → X, A → M, B → M, B → Y, X → Y, should you adjust for M when estimating the effect of X on Y? Justify in terms of the back-door criterion. What is the nature of the error if you do adjust for it?</li>
</ol>

<h4>Synthesis: combining concepts across the chapter</h4>

<ol start="8">
  <li><strong>Exercise 3.8.</strong> <em>(Objective: diagnose an adjustment analysis)</em> A researcher studies the effect of graduate education (X) on lifetime earnings (Y). She has data on: pre-college standardized test scores, parental income, college major, undergraduate GPA, and first-job salary. For each variable, classify it as (a) a confounder to adjust for, (b) a mediator not to adjust for, (c) a collider not to adjust for, or (d) ambiguous without further assumptions. Justify each choice by sketching the plausible DAG.</li>
  <li><strong>Exercise 3.9.</strong> <em>(Objective: integrate back-door criterion with stratification)</em> Given this data on job training and post-training income, with race as a putative confounder (construct a synthetic version of this table yourself, with race balanced but training imbalanced across races). Compute the unadjusted difference in income between trained and untrained. Then compute the race-adjusted difference by stratification. Explain what the difference between the two estimates tells you about the magnitude and direction of the confounding.</li>
  <li><strong>Exercise 3.10.</strong> <em>(Objective: recognize when adjustment isn't enough)</em> A researcher wants to estimate the effect of neighborhood poverty on a child's educational outcomes. She has data on family income, parental education, and child's school quality. She suspects there's also an unobserved variable — family social networks — that affects both neighborhood choice and child outcomes and that she cannot measure. Can she identify the causal effect by adjustment alone? Explain using the back-door criterion. What methods from later chapters might she reach for instead?</li>
</ol>

<h4>Challenge: open-ended or beyond-chapter</h4>

<ol start="11">
  <li><strong>Exercise 3.11.</strong> <em>(Objective: extrapolate beyond the chapter)</em> The back-door criterion is sufficient but not necessary for identification. Pearl's do-calculus provides a more general set of rules for when a causal effect can be identified from observational data, including via "front-door" paths. Sketch an example where the back-door criterion fails but a causal effect is still identified through a mediator on the front door. (Look up "front-door criterion" if you want a hint.) What does this tell you about the scope of adjustment as a tool?</li>
  <li><strong>Exercise 3.12.</strong> <em>(Objective: apply the material to your own work)</em> Take a research question you care about — from your field, your job, or a news article you read recently that made a causal claim from observational data. Draw the DAG you believe. Identify the back-door paths. Determine whether a valid adjustment set exists among the variables that were or could plausibly have been measured. If yes, what would the adjusted analysis look like? If no, what would you need — different data, a different method, a different research design?</li>
</ol>

<hr>

<h3>Chapter summary</h3>

<p>You walked in able to draw a DAG and reason about paths. You walk out able to do the following things you couldn't do before.</p>

<p>You can look at a correlation and ask: <em>which back-door paths are generating this association?</em> — then find the set of variables that closes those paths without destroying the signal you're trying to measure.</p>

<p>You can take a dataset and an assumed DAG, compute the causal effect by stratification, and explain why the answer differs from the raw correlation. You can do this by hand on a small example, and you can recognize what regression and propensity score methods are doing as computational shortcuts for the same operation.</p>

<p>You can spot the three classic mistakes — mediator conditioning, collider conditioning, and M-bias — and explain in each case which clause of the back-door criterion was violated.</p>

<p>You can identify when adjustment won't work and know that this is a signal to change methods, not a signal to force it.</p>

<p><strong>The one idea from this chapter that matters most</strong>: <em>the data cannot tell you which variables to adjust for; the DAG does that, and the DAG is an assumption you make about how the world works.</em> Different DAGs on the same data give different answers. You have to choose.</p>

<p><strong>The common mistake to watch for.</strong> Do not adjust for variables that look relevant because they correlate with both X and Y. Correlation with both is not what makes something a confounder. Being on a back-door path and not being a descendant of X is what makes something a legitimate target for adjustment. The distinction is invisible without the DAG. Draw it.</p>

<p><strong>The Feynman test.</strong> Can you explain, to someone who has never studied causal inference, why the same drug trial data can mean opposite things depending on whether the third column is gender or blood pressure? If you can, you have the chapter. If not, go back to the opening and work it through until you can.</p>

<hr>

<h3>Connections forward</h3>

<p>This chapter gave you the theoretical rule — the back-door criterion — and the rawest computation — stratification. The next chapter is about what happens when your confounders are continuous and multidimensional, and stratification breaks down from data sparsity. We'll develop regression-based adjustment as a parametric shortcut that works when stratification can't, and we'll see exactly when that shortcut silently fails — the overlap problem, model misspecification, and extrapolation into regions with no data.</p>

<p>Chapter 5 takes the same idea again from a different angle: instead of summarizing the relationship between confounders and outcome, summarize the relationship between confounders and <em>treatment</em> — the propensity score. You'll see why this is sometimes more robust, sometimes less, and how the two strategies combine into what are called <em>doubly robust</em> estimators.</p>

<p>The later chapters — instrumental variables, regression discontinuity, difference-in-differences — are for the cases where the back-door criterion returns no valid set. When you can't close the back-door paths with the variables you have, you need another door in or another way to isolate the effect. The rule for choosing the right alternative method always returns to the DAG. Every time you reach for one of those tools, you're reaching for it because the diagram told you that adjustment alone won't do.</p>

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **James Heckman** developed the sample selection model that bears his name and shaped modern thinking about adjustment and confounding in observational data — Nobel Prize 2000. His work made it possible to draw careful causal inferences from non-experimental data.

**Run this:**

```
Who is James Heckman, and how does his work on selection and adjustment connect to confounding we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"James Heckman"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the Heckman correction with a specific applied example (wage analysis with selection into employment).
- Ask it to compare Heckman selection models with the modern propensity-score and DAG-based approaches.

What changes? What gets better? What gets worse?
