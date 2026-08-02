# Chapter 2: The Language of Causal Diagrams


## TL;DR

- ═══════════════════════════════════════ FORMATTED VERSION (Markdown) ═══════════════════════════════════════.
- The chapter moves through Opening: A Picture Nobody Knew What to Call, Learning Objectives, Prerequisites, Why This Chapter Matters, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

═══════════════════════════════════════
FORMATTED VERSION (Markdown)
═══════════════════════════════════════

## Opening: A Picture Nobody Knew What to Call

Here is a problem that looks simple until you try to solve it.

In 1920, a thirty-one-year-old geneticist at the U.S. Department of Agriculture was staring at data on thousands of guinea pigs. His name was Sewall Wright, and he was trying to answer a question that modern statistics, as it existed at the time, could not answer. Why do some guinea pigs develop piebald coats — those irregular white-on-brown patches — and others don't? How much of the pattern comes from heredity? How much from the environment of the mother's womb? How much from pure developmental randomness?

He had the correlations. Correlations between parents and offspring, between littermates, between mothers and daughters. The numbers were real. What the numbers could not tell him was which of those correlations reflected *causation* flowing one direction, and which reflected shared causes flowing from somewhere else entirely. Correlation is symmetric. Cause is not. Wright needed a way to write down which way the arrows ran.

So he drew them.

His 1920 paper in the *Proceedings of the National Academy of Sciences* contains what I believe is the first causal diagram ever published in a scientific journal — a picture with nodes for variables and arrows for direct causal effects, with numbers on the arrows indicating the strength of each effect. He called the method "path analysis." It let him decompose the observed correlations into pieces: this much from shared genes, this much from shared environment, this much from developmental noise.

The statistics community's reaction was not warm. Two years later, a statistician named Henry Niles published a critique arguing that causation could not, in principle, be read off correlational data — that Wright was reaching for something statistics was not built to deliver. The critique stung. Wright responded. The field moved on without him. For decades, path analysis survived in genetics and, later, in a corner of sociology, but mainstream statistics treated it with something between polite indifference and outright suspicion.

It took roughly sixty years for the picture to come back. Starting in the 1980s, the computer scientist Judea Pearl formalized what Wright had been doing, extended it, connected it to probability theory in a rigorous way, and gave the field a vocabulary. The picture Wright drew in 1920 — nodes for variables, arrows for direct effects — is essentially the same picture now used to reason about causation in epidemiology, economics, machine learning, political science, and every other field where people care about "what causes what" and not just "what goes with what."

Causal diagrams are that fundamental. They are not a style of presentation. They are the *notation* for a kind of reasoning that ordinary statistical language cannot express.

This is the most technically demanding chapter in the book, and the most load-bearing. Every subsequent chapter uses the vocabulary I'll build here. If you skim this chapter, the next ten will feel like they're written in a language you half-speak. If you work through it carefully, the rest of the book will feel like the natural extension of a few simple ideas.

### Learning Objectives

By the end of this chapter you should be able to:

1. **Read** a causal diagram — identify its nodes, arrows, and what each claims about the world.
2. **Draw** a causal diagram from a verbal story, translating each causal claim into an arrow.
3. **Identify** the three elementary structures — chains, forks, and colliders — inside any diagram.
4. **Trace** paths between two variables in a diagram and distinguish directed paths from back-door paths.
5. **Apply** the idea of d-separation to determine whether two variables are statistically associated given a conditioning set.
6. **Recognize** a mediator and explain why controlling for one is usually a mistake.

### Prerequisites

You should have worked through Chapter 1, where I argued why causal inference is a distinct discipline from ordinary statistics. In particular, you should be comfortable with the distinction between an observed association and a causal effect, and you should know what I mean by "intervention" versus "observation."

### Why This Chapter Matters

Every claim you make about causation rests on assumptions about how the world is structured. Those assumptions are usually buried inside a methods section or a regression equation, invisible, unexamined, inherited from whoever wrote the previous paper. A causal diagram drags them into the open. Every arrow is a claim. Every missing arrow is a stronger claim — "I assert there is no direct effect here." Once you can draw the diagram, you can argue about the assumptions. Once you can argue about the assumptions, you can do causal inference honestly.

---

## Concept 1: What a Causal Diagram Is, and How to Draw One

Let me start with the pieces, because every piece does specific work.

A causal diagram has two ingredients. **Nodes** are variables — things in the world that can take different values for different units. "Smoking status" is a node. "Lung cancer diagnosis" is a node. "Year of birth" is a node. Anything you might put in a column of a data table is a candidate node.

**Arrows** are direct causal effects. An arrow from node $A$ to node $B$ is a claim: *changing $A$ would, under some circumstances, change $B$, and this effect does not pass through any other variable in the diagram.* That last clause is important. Directness is relative to what's in the picture. If I draw $\text{Smoking} \rightarrow \text{Cancer}$, I'm not claiming the effect is mechanistically direct at the cellular level — obviously it passes through tar deposits, inflammation, DNA damage, and so on. I'm claiming the effect is direct *relative to the other variables I've chosen to include*. If I add tar as a separate node, the arrow structure changes.

The absence of an arrow is as important as the presence. If I leave out an arrow from $A$ to $B$, I am asserting something strong: there is no direct causal effect, holding the other variables in the diagram fixed. This is why drawing a diagram is an act of intellectual commitment. You are on record about what you think the causal structure is. Hidden assumptions become visible.

A causal diagram, formally, is a **directed acyclic graph**, or DAG. "Directed" because arrows have a direction. "Acyclic" because you cannot follow the arrows and return to where you started. A variable cannot be, directly or indirectly, a cause of itself. If your diagram has a loop, you have either a feedback system that needs to be unfolded across time, or a mistake.

### Worked Example: Translating a Story to a Diagram

Let me walk through a concrete case. Here's a story about smoking and lung cancer, simplified, and I'll translate it into a diagram one claim at a time.

> A person's genetic profile influences their likelihood of becoming a smoker — some genotypes are associated with higher nicotine receptor sensitivity, which affects how rewarding the first few cigarettes feel. Smoking causes tar to accumulate in the lungs. Tar accumulation damages lung tissue and contributes to lung cancer. Genetic profile also directly affects lung cancer risk independent of smoking — certain alleles influence how efficiently cells repair DNA damage.

Let me pull out the causal claims, one at a time.

*Claim 1: Genotype causes smoking behavior.*

I draw a node for Genotype ($G$), a node for Smoking ($S$), and an arrow from $G$ to $S$.

*Claim 2: Smoking causes tar.*

I add a node for Tar ($T$) and an arrow from $S$ to $T$.

*Claim 3: Tar causes lung cancer.*

I add a node for Cancer ($C$) and an arrow from $T$ to $C$.

*Claim 4: Genotype also affects cancer directly, independent of smoking.*

I add an arrow from $G$ to $C$.

Here's the diagram:

<!-- FIGURE 2.1: A directed acyclic graph with four nodes arranged to show the causal structure of smoking and lung cancer. Node G (Genotype) has arrows pointing to S (Smoking) and C (Cancer). Node S has an arrow pointing to T (Tar). Node T has an arrow pointing to C. Caption: Genotype causes smoking; smoking causes tar; tar causes cancer; genotype also has a direct effect on cancer independent of smoking. Notice that G affects C through two separate routes. -->

Now look at what this picture is committing to — and what it is committing to *not*.

It says genotype affects cancer through two routes: indirectly, by increasing smoking (which increases tar, which increases cancer), and directly, through DNA repair efficiency. It says tar is the only route by which smoking affects cancer — there is no arrow from $S$ directly to $C$ that bypasses $T$. That is a real claim. If I believed smoking caused cancer through some mechanism not routed through tar — say, through chronic inflammation independent of tar deposition — I would need to either add a direct $S \rightarrow C$ arrow or introduce an inflammation node.

The diagram also does not say anything about things I didn't include. Air pollution, age, occupation, radon exposure — all omitted. The omission is not neutral. The diagram is claiming that, conditional on the variables shown, these other factors either don't matter or don't systematically relate to the variables that are shown. If that's wrong, the diagram is wrong, and everything I conclude from it may be wrong.

This is the uncomfortable part of drawing diagrams. You cannot hide. Every arrow is a commitment. Every missing arrow is a stronger commitment. Statistics papers often bury their assumptions in the modeling choices — in whether they included a covariate, in what functional form they used. A diagram forces you to state the assumptions up front, in a picture anyone can argue with. This is, in my view, the single most important design choice the causal inference community made when it adopted this notation. It trades the comfort of hidden assumptions for the clarity of stated ones.

---

## Concept 2: The Three Building Blocks

Every causal diagram, no matter how complex, is built from three elementary structures. Once you can recognize them, you can take almost any diagram apart and see what it's doing.

### Chains: Information Flowing Through a Middleman

A **chain** is three nodes connected by arrows pointing the same direction:

$$A \rightarrow B \rightarrow C$$

Information flows from $A$ to $C$ through $B$. $B$ is a *mediator* — it sits on the causal path from $A$ to $C$ and passes the effect along.

In our smoking diagram, $S \rightarrow T \rightarrow C$ is a chain. Smoking causes tar, tar causes cancer, so smoking and cancer will be statistically associated even though there is no arrow directly from $S$ to $C$. The association runs through the middleman.

The key fact about chains: $A$ and $C$ are associated *because of* the chain. If you remove $B$ — conceptually, if you could hold $B$ fixed at one value — the association between $A$ and $C$ would be cut. Hold tar deposits fixed (imagine a perfect filter that removes all tar regardless of smoking status), and the correlation between smoking and cancer that ran through tar would disappear. Any remaining correlation would have to come from elsewhere.

This is the first of three rules I'll state: **conditioning on a mediator blocks the chain.**

### Forks: Two Effects of a Common Cause

A **fork** is three nodes where one has arrows pointing to the other two:

$$A \leftarrow B \rightarrow C$$

$B$ is a *common cause* of both $A$ and $C$. Because $B$ causes both, $A$ and $C$ will be correlated in the data — not because one causes the other, but because both are responding to changes in $B$.

A classic example: ice cream sales and drowning deaths. Both go up together. There is no causal connection between them. Hot weather ($B$) causes both. If you plot ice cream sales against drowning deaths across weeks of the year, you get a clean upward line. If you hold temperature fixed — compare ice cream sales and drowning deaths within weeks of similar temperature — the correlation collapses.

This is the second rule: **conditioning on a common cause blocks the fork.**

In the smoking diagram, $S \leftarrow G \rightarrow C$ is a fork. Genotype causes both smoking and cancer. So some of the observed correlation between smoking and cancer is not the effect of smoking at all — it's the shared genetic origin of both. When you compare smokers to non-smokers, you are partly comparing people with different genotypes, and some of what looks like the effect of smoking is actually the effect of genotype. This is the confounding problem in miniature. Chapter 3 is dedicated to it.

### Colliders: The One That Breaks Intuition

A **collider** is three nodes where two arrows point *into* the middle node:

$$A \rightarrow B \leftarrow C$$

$A$ and $C$ both cause $B$. They both "collide" at $B$, which is where the name comes from.

Here is the rule that every student I've taught finds counterintuitive:

**$A$ and $C$ are not correlated through a collider. But if you condition on the collider, they become correlated.**

Let me say that again, because it matters. The natural, unconditioned state of a collider is *no association* between its parents. Conditioning — controlling for, stratifying on, selecting based on — the collider *creates* an association that was not there before.

This is the exact opposite of what happens with chains and forks. For chains and forks, conditioning on the middle node removes association. For colliders, conditioning on the middle node adds association. Students learn the first pattern easily and then apply it to colliders, and they get everything wrong.

Here is where I'll slow down, because this is the single most common source of advanced-level errors in causal inference.

### Worked Example: Berkson's Paradox

In 1946, the Mayo Clinic biostatistician Joseph Berkson pointed out a puzzle that now carries his name. Suppose there are two diseases, $A$ and $C$, that are biologically independent. Having disease $A$ has no effect on whether you have disease $C$, and vice versa. In the general population, the two are uncorrelated.

Now you run a study using hospital patients. You look at everyone who shows up to the hospital and ask: among hospital patients, are disease $A$ and disease $C$ correlated?

They will be. *Negatively.* Inside the hospital, the two diseases appear to repel each other, as if being sick with one protected you from the other.

How can this happen if they're independent in the general population?

Here's the diagram:

<!-- FIGURE 2.2: A three-node collider structure. Node A (Disease A) has an arrow pointing to H (Hospitalization). Node C (Disease C) also has an arrow pointing to H. No arrows between A and C. Caption: Both diseases cause hospitalization; neither causes the other. H is a collider on the path from A to C. -->

Disease $A$ makes you more likely to go to the hospital. Disease $C$ also makes you more likely to go to the hospital. $H$ (hospitalization) is a collider — both diseases collide at it.

In the general population, $A$ and $C$ are independent. Fine. But now restrict your attention to hospitalized patients only — that is, condition on $H = \text{yes}$. Here's the reasoning that makes the paradox feel intuitive.

If I meet a hospitalized patient, I know they're in the hospital for *some* reason. If it's not disease $A$, it probably has to be disease $C$ (or something else sick enough to hospitalize them). Knowing they don't have $A$ raises the probability they have $C$ — not because the biology has changed, but because the selection process made it so.

Let me put numbers on it. Imagine a population of 10,000 people. Suppose 5% have disease $A$ and 5% have disease $C$, independently. So about 500 have $A$ alone, 500 have $C$ alone, 25 have both (5% of 5%), and roughly 8,975 have neither.

Suppose anyone with a disease goes to the hospital. Nobody without a disease goes. Then the hospital population consists of:

- 500 with $A$ only
- 500 with $C$ only
- 25 with both

Total hospitalized: 1,025.

Among hospitalized patients, the probability of $C$ given $A$ is $25 / 525 \approx 4.8\%$. The probability of $C$ given *not* $A$ is $500 / 500 = 100\%$. Having disease $A$, inside the hospital, looks enormously *protective* against disease $C$. In the general population, $A$ tells you nothing about $C$. Inside the hospital, it tells you almost everything.

The collider created the association. Nothing about the biology changed. The selection did the work.

### Worked Example: The Dating Pool

A less clinical version, same structure. Suppose in the general population, attractiveness and kindness are independent. Some people are both, some are neither, some are one or the other; knowing one tells you nothing about the other.

Now think about the people you actually date, or consider dating. For most people, the dating filter is roughly: *I'd date someone who is either attractive enough to catch my eye, or kind enough that I don't care.* Call the dating pool $D$.

Here's the diagram:

<!-- FIGURE 2.3: Three-node collider structure. Node A (Attractiveness) has an arrow to D (In your dating pool). Node K (Kindness) has an arrow to D. No arrows between A and K. Caption: Attractiveness and kindness are independent in the general population; both raise the chance someone enters your dating pool; D is a collider. -->

$A \rightarrow D \leftarrow K$. Colliders.

In the general population, $A$ and $K$ are uncorrelated. Inside your dating pool, they look negatively correlated. The attractive people you meet are, on average, less kind; the kind people you meet are, on average, less attractive. The people who are both are rare, not because they don't exist in the world, but because *you only notice them at the rate they exist in the world*, while you over-sample people who made the pool on the strength of just one trait.

Many of life's "you can't have everything" feelings are collider effects from selection.

### Summary of the Three Structures

Here's what you should be able to recite:

- **Chain** $(A \rightarrow B \rightarrow C)$: $A$ and $C$ are associated through $B$. Conditioning on $B$ blocks the association.
- **Fork** $(A \leftarrow B \rightarrow C)$: $A$ and $C$ are associated because of $B$. Conditioning on $B$ blocks the association.
- **Collider** $(A \rightarrow B \leftarrow C)$: $A$ and $C$ are *not* associated. Conditioning on $B$ *creates* an association.

The collider is the weird one. If you remember nothing else from this chapter, remember that conditioning is not always a good thing. It is a tool. It removes some associations and creates others. Which it does depends on the structure. You cannot know which without the diagram.

---

## Concept 3: Paths, d-Separation, and the Mediator Warning

We now have the building blocks. Let me show you how to reason about a whole diagram.

### What a Path Is

A **path** between two nodes is a sequence of edges that connects them, *regardless of the direction of the arrows*. Paths can run with the arrows, against them, or mix.

A **directed path** is a path where all the arrows point the same direction, tracing a chain of causation from the start to the end.

A **back-door path** from $A$ to $B$ is a non-directed path that starts with an arrow pointing *into* $A$. Back-door paths are the signature of confounding — they connect cause and effect through a shared origin rather than through causation.

In our smoking diagram, the path $S \rightarrow T \rightarrow C$ is a directed path from smoking to cancer — the genuine causal path. The path $S \leftarrow G \rightarrow C$ is a back-door path — it connects smoking and cancer through their shared cause, the genotype. Both paths create association between $S$ and $C$ in the data. Only one of them represents the causal effect we care about.

Here's the picture again with the paths highlighted conceptually:

<!-- FIGURE 2.4: The four-node diagram from Figure 2.1 with two paths visually distinguished. The directed path S → T → C shown in one style, the back-door path S ← G → C shown in another. Caption: The association between smoking and cancer in observational data has two sources: the real causal effect running through tar, and the confounding path running through genotype. -->

### The Idea of d-Separation

With paths defined, I can state the central idea of this chapter.

Two variables in a diagram are **d-separated** by a set $Z$ of conditioning variables if every path between them is *blocked* by $Z$. When two variables are d-separated, they are statistically independent given $Z$. When they are not — when at least one path remains open — they can be statistically associated.

A path is blocked in two ways, and this is where you have to be careful because colliders flip the rule:

- **At a chain or fork node** ($\rightarrow M \rightarrow$ or $\leftarrow M \rightarrow$): the path is blocked if you *do* condition on $M$.
- **At a collider node** ($\rightarrow M \leftarrow$): the path is blocked if you do *not* condition on $M$ (and do not condition on any descendant of $M$).

That second point about descendants deserves a note. Conditioning on a collider opens the path. So does conditioning on anything downstream of the collider — any variable the collider causes. If you condition on a variable that is a collider's descendant, you partially condition on the collider itself, and the path partially opens. For now, remember the simple version: don't condition on colliders or their descendants if you want to keep the path closed.

I'll state the full d-separation procedure as a recipe you can run by hand:

1. List all paths between the two variables.
2. For each path, go through the intermediate nodes one by one.
3. If any non-collider on the path is in $Z$, the path is blocked.
4. If the path has a collider and neither the collider nor any descendant of it is in $Z$, the path is blocked.
5. If after all that, every path is blocked, the two variables are d-separated given $Z$, and they are statistically independent given $Z$.
6. If even one path remains open, they are not d-separated, and they are likely associated given $Z$.

This is the whole engine. Everything in the next several chapters — confounding adjustment, instrumental variables, selection bias, collider control — is applied d-separation. If you can run this procedure, you can reason about when a statistical association reflects a causal effect and when it reflects something else.

### Worked Example: Running the Procedure

Let me use the smoking diagram to run through it. I want to ask: *is smoking independent of cancer if I condition on tar and genotype?*

The question is really: *is the diagram telling us that controlling for tar and genotype would leave no association between smoking and cancer?*

List the paths from $S$ to $C$:

1. $S \rightarrow T \rightarrow C$ (direct causal path through the mediator)
2. $S \leftarrow G \rightarrow C$ (back-door path through the confounder)

Conditioning set: $Z = \{T, G\}$.

Path 1: $S \rightarrow T \rightarrow C$. Pass through $T$. $T$ is a chain node (arrow in, arrow out). $T$ is in $Z$. Path blocked.

Path 2: $S \leftarrow G \rightarrow C$. Pass through $G$. $G$ is a fork node (arrows pointing out both directions). $G$ is in $Z$. Path blocked.

Both paths blocked. $S$ and $C$ are d-separated given $\{T, G\}$. The diagram is claiming that if you stratified on both tar and genotype, smoking and cancer would show no residual association.

Is this the answer we want? Only if our question is "are smoking and cancer associated once we account for everything the diagram says connects them." If our question is "what is the causal effect of smoking on cancer," then blocking *the directed path* $S \rightarrow T \rightarrow C$ is exactly the wrong thing to do — because that path *is* the causal effect. Which brings me to the warning.

### The Mediator Warning

A **mediator** is a variable on a directed path from cause to effect. In the smoking diagram, tar is a mediator: it's the middleman through which smoking causes cancer.

Controlling for a mediator, in most analyses, is a mistake.

Here's why. The causal effect of smoking on cancer runs through tar. That is the mechanism. If you condition on tar — if you compare smokers and non-smokers who have the *same tar level in their lungs* — you've removed the pathway through which smoking does its damage. You're asking: "holding constant the amount of tar in the lungs, does smoking affect cancer?" And the answer, under the diagram I drew, is *no*, because all the effect ran through tar in the first place. You'll conclude smoking has no effect on cancer. You'll be wrong, not because the data is wrong, but because you blocked the path you were trying to measure.

This is different from controlling for a confounder like genotype. Genotype is not on the causal path from smoking to cancer — it's a shared cause. Blocking the path through genotype removes confounding. Blocking the path through tar removes the signal itself.

Students confuse these two constantly. Both involve "controlling for a variable." Both look, in a regression output, identical — you add a term to the model. But one operation removes a bias you don't want, and the other operation removes the effect you were trying to see. The diagram tells you which is which. A regression equation does not.

I'll say this as plainly as I can: **do not control for variables that lie on the causal path from your treatment to your outcome.** If you're measuring the effect of smoking on cancer and someone tells you "you forgot to control for tar" — they are wrong. Tar is not a confounder. Tar is the mechanism. Chapter 3 will return to this, because the failure mode is common and expensive, and it hides inside ordinary-looking regressions.

---

## Integration: Reading a Real Diagram

Let me put everything together on a slightly bigger diagram. Here's the setup: we're interested in the effect of a job training program on wages. Participants self-select into the program. Prior work history affects both whether someone signs up and their eventual wages. Motivation (unobserved) affects both sign-up and wages. The program, if it works, affects wages by improving skills.

Variables:

- $W_0$: Prior work history
- $M$: Motivation
- $P$: Program participation
- $S$: Skills (post-program)
- $W_1$: Wages after the program

The story: prior work history affects program participation and also affects wages directly (experience matters regardless of training). Motivation affects participation and also wages directly (motivated workers earn more even without the program). Program participation raises skills. Skills raise wages.

<!-- FIGURE 2.5: A five-node DAG. W₀ (Prior Work) has arrows to P (Program) and W₁ (Wages). M (Motivation) has arrows to P and W₁. P has an arrow to S (Skills). S has an arrow to W₁. Caption: The causal structure underlying a job training program evaluation. P is the treatment, W₁ is the outcome, S is a mediator of the program's effect, and W₀ and M are confounders. -->

Let me ask the causal-inference question: *what is the effect of the program on wages?*

Paths from $P$ to $W_1$:

1. $P \rightarrow S \rightarrow W_1$ (the directed causal path — the program raises skills, which raises wages)
2. $P \leftarrow W_0 \rightarrow W_1$ (back-door through prior work)
3. $P \leftarrow M \rightarrow W_1$ (back-door through motivation)

Path 1 is the effect we want. Paths 2 and 3 are confounding.

To identify the causal effect, we want to block paths 2 and 3 without blocking path 1. Condition on $W_0$ and $M$. That blocks the two back-door paths (both are forks; conditioning on the fork node closes them) and leaves the directed path open.

What we must *not* do: condition on $S$. Skills is on the causal path. Conditioning on $S$ blocks path 1, the very thing we're trying to measure. An analyst who thinks "the more I control for, the cleaner the estimate" will put $S$ into the regression and wipe out the program's effect. The diagram says no.

There's a second issue. Motivation is unobserved. We cannot condition on what we cannot measure. If $M$ is truly unobservable, then path 3 stays open no matter what else we condition on, and the program effect is not identified from this diagram alone. We would need a different tool — a randomized trial, an instrumental variable, a natural experiment — to cut the confounding path we can't close by conditioning. This is a preview of what the rest of the book is for.

The diagram is doing an enormous amount of work here. It has separated the good thing to control for ($W_0$), the thing that must not be controlled for ($S$), and the thing we cannot control for ($M$) into three categories that look identical in a data table. Only the causal structure tells them apart.

---

## A note about AI

DAGs are the grammar of causal claims. The model can draw DAGs from a description and the drawings will look authoritative. Authority of form is not authority of content.

Where the model genuinely helps: producing several candidate DAGs for the same problem and surfacing the substantive disagreements that distinguish them. The disagreements are where the actual causal reasoning lives.

Where the model does damage: certifying a DAG as correct. A DAG is a set of substantive claims about the world — what variables exist, which arrows point which way, which arrows are absent. The model has no privileged access to any of those claims.

The rule: candidate DAGs from the model; commitment to a DAG from a domain expert who can defend the edges.

---

## Exercises

Do these with paper and pencil. The point is to move the rules from recognition to fluency.

### Warm-up

**Exercise 2.1** *(Objective 1: read a diagram.)* Given the three-node diagram $A \rightarrow B \rightarrow C$: write in plain English what causal claims this diagram is making. What is it claiming *doesn't* exist?

**Exercise 2.2** *(Objective 3: identify elementary structures.)* For each of the following, state whether it is a chain, a fork, or a collider:

- $X \rightarrow Y \rightarrow Z$
- $X \leftarrow Y \rightarrow Z$
- $X \rightarrow Y \leftarrow Z$
- $X \leftarrow Y \leftarrow Z$

(The last one is a chain read right to left. Chains don't care which side you start from.)

**Exercise 2.3** *(Objective 3: identify structures in context.)* In the five-node job training diagram from the integration section, identify one chain, one fork, and one collider. (Hint for the collider: which node has two arrows pointing in?)

### Application

**Exercise 2.4** *(Objective 2: draw a diagram from a story.)* Translate the following story into a causal diagram. "A person's education level affects both the kind of job they get and their income directly. The kind of job they get also affects their income. Parental income affects their education level and also directly affects their eventual income through inheritance and connections." Draw the diagram. How many nodes? How many arrows? What does your diagram claim is *not* a direct cause of income?

**Exercise 2.5** *(Objectives 2 and 3.)* An epidemiologist tells you: "We looked at hospitalized patients and found that smokers had lower rates of a certain inflammatory disease than non-smokers — smoking appeared protective." Draw a diagram that could explain this finding without any protective biological effect of smoking on the disease. Name the collider in your diagram.

**Exercise 2.6** *(Objective 4: trace paths.)* In the smoking/tar/cancer/genotype diagram (Figure 2.1), list *all* paths from $S$ to $C$. For each, say whether it is a directed path or a back-door path.

**Exercise 2.7** *(Objective 6: recognize mediators.)* In each of the following pairs, state which variable (if either) is a mediator of the effect of the first variable on the last:

- Smoking → Tar → Cancer. What is the mediator?
- Smoking ← Genotype → Cancer. What is the mediator, or is there none?
- Exercise → Cardiovascular fitness → Longevity. What is the mediator?

### Synthesis

**Exercise 2.8** *(Objectives 3, 5, and 6.)* Consider this diagram: $X \rightarrow M \rightarrow Y$, and separately $X \leftarrow U \rightarrow Y$, where $U$ is unobserved. All four nodes are distinct. (a) List all paths from $X$ to $Y$. (b) Which paths are open if you condition on nothing? (c) Which paths are open if you condition on $M$? (d) Which paths are open if you condition on $U$? (e) Is the causal effect of $X$ on $Y$ identifiable by any conditioning strategy in this diagram? Justify your answer.

**Exercise 2.9** *(Objectives 3, 4, 5.)* Given the diagram $A \rightarrow B \rightarrow C \leftarrow D$, where $A$ and $D$ are otherwise unconnected:

- What kind of structure is at $C$?
- Are $A$ and $D$ associated if you condition on nothing?
- Are $A$ and $D$ associated if you condition on $C$?
- Are $A$ and $D$ associated if you condition on $B$ and $C$?

**Exercise 2.10** *(Objectives 5, 6.)* You are evaluating a weight-loss program. Participation is voluntary. You have data on starting weight, ending weight, motivation (measured by a validated survey), and program participation. Someone suggests you control for ending weight to "clean up" the analysis. Draw a diagram of this scenario and explain, using the diagram, why controlling for ending weight is the wrong move.

### Challenge

**Exercise 2.11** *(Objectives 2, 5, 6; open-ended.)* Find a real observational study in a field you know something about. Read the methods section carefully. Try to draw the causal diagram the authors implicitly assume. Then ask: do any of the variables they controlled for lie on the causal path from their treatment to their outcome? If yes, what would the diagram predict about the bias their analysis introduces? This exercise takes longer than the others and is where this chapter starts paying off.

**Exercise 2.12** *(Beyond this chapter.)* In the integration example, motivation $M$ was unobserved and so path $P \leftarrow M \rightarrow W_1$ could not be blocked by conditioning. Propose one *non-conditioning* strategy that might let you estimate the program's effect despite the unobservable confounder. (You don't need to know the formal machinery yet. Think like a researcher who wants to outwit the confounding.) We'll develop the formal tools in Chapter 5.

---

## Chapter Summary

If you've worked through this chapter, here is what you should now be able to do.

You can read a causal diagram and state, in plain English, the causal claims it is making and the claims it is implicitly denying. You can take a verbal story about how the world works and draw a diagram that captures its causal structure. You can identify chains, forks, and colliders inside any diagram and state the rule for each: chains and forks transmit association until you condition; colliders block association until you condition, at which point they start transmitting it.

You can trace paths between any two nodes and distinguish the directed paths (which represent causal effects) from back-door paths (which represent confounding). You can apply d-separation to decide whether two variables are independent given a conditioning set: a path is blocked at a chain or fork if you condition on the middle node, and blocked at a collider if you do not. When every path is blocked, the variables are d-separated and statistically independent.

Most importantly, you can recognize a mediator and resist the impulse to control for it. A mediator lies on the causal path you are trying to measure. Controlling for it removes the signal, not the noise. This is the single most common advanced-level mistake in causal inference, and it survives inside regressions where nothing else looks wrong.

The idea from this chapter that matters most is this: **conditioning is not a clean operation.** It removes some kinds of association and creates others. Which it does depends on the causal structure. No amount of sophisticated statistics recovers what the diagram tells you to do and not do.

The common mistake to watch for: *controlling for everything you measured.* The impulse is wrong. You should control for confounders and leave mediators alone, and only the diagram tells you which is which.

The Feynman test for this chapter: can you explain to someone who has never seen a causal diagram why, inside a hospital, two unrelated diseases can appear negatively correlated? If you can walk them through it using a picture and get them to see the reasoning, you understand this chapter.

---

## Connections Forward

Chapter 3 takes the biggest problem this chapter named — confounding — and gives you the tools to solve it. We'll talk about the back-door criterion, which is a precise statement of when conditioning suffices to block all confounding paths; about propensity scores, which let you handle many confounders at once; and about the two ways a regression can go wrong even when the diagram is correct.

Chapter 4 deals with what Chapter 3 cannot: situations where the confounder is unobserved and no amount of conditioning helps. That is where randomization, natural experiments, and instrumental variables come in. The diagram tells you when you need those tools.

Every chapter from here on builds on the vocabulary I just taught you. If the exercises felt hard, good — redo them. If they felt easy, you are either very fast or missing something subtle. The collider chapter, Chapter 6, will tell you which.

═══════════════════════════════════════
SUBSTACK HTML (Copy-Paste Ready)
═══════════════════════════════════════

<!-- Manual steps needed:
     1. Insert 5 figures where marked (FIGURE 2.1–2.5): causal DAGs, drawn in your diagram tool of choice (TikZ, DAGitty, Mermaid, or hand-drawn).
     2. Insert 2 LaTeX equations where marked (simple chain/fork/collider notation). Substack supports inline LaTeX via the equation block.
     3. No tables in this chapter — no Datawrapper embeds needed. -->

<h2>Chapter 2: The Language of Causal Diagrams</h2>

<h3>Opening: A Picture Nobody Knew What to Call</h3>

<p>Here is a problem that looks simple until you try to solve it.</p>

<p>In 1920, a thirty-one-year-old geneticist at the U.S. Department of Agriculture was staring at data on thousands of guinea pigs. His name was Sewall Wright, and he was trying to answer a question that modern statistics, as it existed at the time, could not answer. Why do some guinea pigs develop piebald coats — those irregular white-on-brown patches — and others don't? How much of the pattern comes from heredity? How much from the environment of the mother's womb? How much from pure developmental randomness?</p>

<p>He had the correlations. Correlations between parents and offspring, between littermates, between mothers and daughters. The numbers were real. What the numbers could not tell him was which of those correlations reflected <em>causation</em> flowing one direction, and which reflected shared causes flowing from somewhere else entirely. Correlation is symmetric. Cause is not. Wright needed a way to write down which way the arrows ran.</p>

<p>So he drew them.</p>

<p>His 1920 paper in the <em>Proceedings of the National Academy of Sciences</em> contains what I believe is the first causal diagram ever published in a scientific journal — a picture with nodes for variables and arrows for direct causal effects, with numbers on the arrows indicating the strength of each effect. He called the method "path analysis." It let him decompose the observed correlations into pieces: this much from shared genes, this much from shared environment, this much from developmental noise.</p>

<p>The statistics community's reaction was not warm. Two years later, a statistician named Henry Niles published a critique arguing that causation could not, in principle, be read off correlational data — that Wright was reaching for something statistics was not built to deliver. The critique stung. Wright responded. The field moved on without him. For decades, path analysis survived in genetics and, later, in a corner of sociology, but mainstream statistics treated it with something between polite indifference and outright suspicion.</p>

<p>It took roughly sixty years for the picture to come back. Starting in the 1980s, the computer scientist Judea Pearl formalized what Wright had been doing, extended it, connected it to probability theory in a rigorous way, and gave the field a vocabulary. The picture Wright drew in 1920 — nodes for variables, arrows for direct effects — is essentially the same picture now used to reason about causation in epidemiology, economics, machine learning, political science, and every other field where people care about "what causes what" and not just "what goes with what."</p>

<p>Causal diagrams are that fundamental. They are not a style of presentation. They are the <em>notation</em> for a kind of reasoning that ordinary statistical language cannot express.</p>

<p>This is the most technically demanding chapter in the book, and the most load-bearing. Every subsequent chapter uses the vocabulary I'll build here. If you skim this chapter, the next ten will feel like they're written in a language you half-speak. If you work through it carefully, the rest of the book will feel like the natural extension of a few simple ideas.</p>

<h4>Learning Objectives</h4>

<p>By the end of this chapter you should be able to:</p>

<ol>
<li><strong>Read</strong> a causal diagram — identify its nodes, arrows, and what each claims about the world.</li>
<li><strong>Draw</strong> a causal diagram from a verbal story, translating each causal claim into an arrow.</li>
<li><strong>Identify</strong> the three elementary structures — chains, forks, and colliders — inside any diagram.</li>
<li><strong>Trace</strong> paths between two variables in a diagram and distinguish directed paths from back-door paths.</li>
<li><strong>Apply</strong> the idea of d-separation to determine whether two variables are statistically associated given a conditioning set.</li>
<li><strong>Recognize</strong> a mediator and explain why controlling for one is usually a mistake.</li>
</ol>

<h4>Prerequisites</h4>

<p>You should have worked through Chapter 1, where I argued why causal inference is a distinct discipline from ordinary statistics. In particular, you should be comfortable with the distinction between an observed association and a causal effect, and you should know what I mean by "intervention" versus "observation."</p>

<h4>Why This Chapter Matters</h4>

<p>Every claim you make about causation rests on assumptions about how the world is structured. Those assumptions are usually buried inside a methods section or a regression equation, invisible, unexamined, inherited from whoever wrote the previous paper. A causal diagram drags them into the open. Every arrow is a claim. Every missing arrow is a stronger claim — "I assert there is no direct effect here." Once you can draw the diagram, you can argue about the assumptions. Once you can argue about the assumptions, you can do causal inference honestly.</p>

<hr>

<h3>Concept 1: What a Causal Diagram Is, and How to Draw One</h3>

<p>Let me start with the pieces, because every piece does specific work.</p>

<p>A causal diagram has two ingredients. <strong>Nodes</strong> are variables — things in the world that can take different values for different units. "Smoking status" is a node. "Lung cancer diagnosis" is a node. "Year of birth" is a node. Anything you might put in a column of a data table is a candidate node.</p>

<p><strong>Arrows</strong> are direct causal effects. An arrow from node <em>A</em> to node <em>B</em> is a claim: <em>changing A would, under some circumstances, change B, and this effect does not pass through any other variable in the diagram.</em> That last clause is important. Directness is relative to what's in the picture. If I draw Smoking → Cancer, I'm not claiming the effect is mechanistically direct at the cellular level — obviously it passes through tar deposits, inflammation, DNA damage, and so on. I'm claiming the effect is direct <em>relative to the other variables I've chosen to include</em>. If I add tar as a separate node, the arrow structure changes.</p>

<p>The absence of an arrow is as important as the presence. If I leave out an arrow from <em>A</em> to <em>B</em>, I am asserting something strong: there is no direct causal effect, holding the other variables in the diagram fixed. This is why drawing a diagram is an act of intellectual commitment. You are on record about what you think the causal structure is. Hidden assumptions become visible.</p>

<p>A causal diagram, formally, is a <strong>directed acyclic graph</strong>, or DAG. "Directed" because arrows have a direction. "Acyclic" because you cannot follow the arrows and return to where you started. A variable cannot be, directly or indirectly, a cause of itself. If your diagram has a loop, you have either a feedback system that needs to be unfolded across time, or a mistake.</p>

<h4>Worked Example: Translating a Story to a Diagram</h4>

<p>Let me walk through a concrete case. Here's a story about smoking and lung cancer, simplified, and I'll translate it into a diagram one claim at a time.</p>

<blockquote>A person's genetic profile influences their likelihood of becoming a smoker — some genotypes are associated with higher nicotine receptor sensitivity, which affects how rewarding the first few cigarettes feel. Smoking causes tar to accumulate in the lungs. Tar accumulation damages lung tissue and contributes to lung cancer. Genetic profile also directly affects lung cancer risk independent of smoking — certain alleles influence how efficiently cells repair DNA damage.</blockquote>

<p>Let me pull out the causal claims, one at a time.</p>

<p><em>Claim 1: Genotype causes smoking behavior.</em> I draw a node for Genotype (<em>G</em>), a node for Smoking (<em>S</em>), and an arrow from <em>G</em> to <em>S</em>.</p>

<p><em>Claim 2: Smoking causes tar.</em> I add a node for Tar (<em>T</em>) and an arrow from <em>S</em> to <em>T</em>.</p>

<p><em>Claim 3: Tar causes lung cancer.</em> I add a node for Cancer (<em>C</em>) and an arrow from <em>T</em> to <em>C</em>.</p>

<p><em>Claim 4: Genotype also affects cancer directly, independent of smoking.</em> I add an arrow from <em>G</em> to <em>C</em>.</p>

<!-- FIGURE 2.1: A directed acyclic graph with four nodes. G (Genotype) has arrows pointing to S (Smoking) and C (Cancer). S has an arrow pointing to T (Tar). T has an arrow pointing to C. Caption: Genotype causes smoking; smoking causes tar; tar causes cancer; genotype also has a direct effect on cancer independent of smoking. Notice that G affects C through two separate routes. -->

<p>Now look at what this picture is committing to — and what it is committing to <em>not</em>.</p>

<p>It says genotype affects cancer through two routes: indirectly, by increasing smoking (which increases tar, which increases cancer), and directly, through DNA repair efficiency. It says tar is the only route by which smoking affects cancer — there is no arrow from <em>S</em> directly to <em>C</em> that bypasses <em>T</em>. That is a real claim. If I believed smoking caused cancer through some mechanism not routed through tar — say, through chronic inflammation independent of tar deposition — I would need to either add a direct S → C arrow or introduce an inflammation node.</p>

<p>The diagram also does not say anything about things I didn't include. Air pollution, age, occupation, radon exposure — all omitted. The omission is not neutral. The diagram is claiming that, conditional on the variables shown, these other factors either don't matter or don't systematically relate to the variables that are shown. If that's wrong, the diagram is wrong, and everything I conclude from it may be wrong.</p>

<p>This is the uncomfortable part of drawing diagrams. You cannot hide. Every arrow is a commitment. Every missing arrow is a stronger commitment. Statistics papers often bury their assumptions in the modeling choices — in whether they included a covariate, in what functional form they used. A diagram forces you to state the assumptions up front, in a picture anyone can argue with. This is, in my view, the single most important design choice the causal inference community made when it adopted this notation. It trades the comfort of hidden assumptions for the clarity of stated ones.</p>

<hr>

<h3>Concept 2: The Three Building Blocks</h3>

<p>Every causal diagram, no matter how complex, is built from three elementary structures. Once you can recognize them, you can take almost any diagram apart and see what it's doing.</p>

<h4>Chains: Information Flowing Through a Middleman</h4>

<p>A <strong>chain</strong> is three nodes connected by arrows pointing the same direction:</p>

<!-- LATEX: A → B → C -->

<p>Information flows from <em>A</em> to <em>C</em> through <em>B</em>. <em>B</em> is a <em>mediator</em> — it sits on the causal path from <em>A</em> to <em>C</em> and passes the effect along.</p>

<p>In our smoking diagram, S → T → C is a chain. Smoking causes tar, tar causes cancer, so smoking and cancer will be statistically associated even though there is no arrow directly from <em>S</em> to <em>C</em>. The association runs through the middleman.</p>

<p>The key fact about chains: <em>A</em> and <em>C</em> are associated <em>because of</em> the chain. If you remove <em>B</em> — conceptually, if you could hold <em>B</em> fixed at one value — the association between <em>A</em> and <em>C</em> would be cut. Hold tar deposits fixed (imagine a perfect filter that removes all tar regardless of smoking status), and the correlation between smoking and cancer that ran through tar would disappear. Any remaining correlation would have to come from elsewhere.</p>

<p>This is the first of three rules I'll state: <strong>conditioning on a mediator blocks the chain.</strong></p>

<h4>Forks: Two Effects of a Common Cause</h4>

<p>A <strong>fork</strong> is three nodes where one has arrows pointing to the other two:</p>

<!-- LATEX: A ← B → C -->

<p><em>B</em> is a <em>common cause</em> of both <em>A</em> and <em>C</em>. Because <em>B</em> causes both, <em>A</em> and <em>C</em> will be correlated in the data — not because one causes the other, but because both are responding to changes in <em>B</em>.</p>

<p>A classic example: ice cream sales and drowning deaths. Both go up together. There is no causal connection between them. Hot weather (<em>B</em>) causes both. If you plot ice cream sales against drowning deaths across weeks of the year, you get a clean upward line. If you hold temperature fixed — compare ice cream sales and drowning deaths within weeks of similar temperature — the correlation collapses.</p>

<p>This is the second rule: <strong>conditioning on a common cause blocks the fork.</strong></p>

<p>In the smoking diagram, S ← G → C is a fork. Genotype causes both smoking and cancer. So some of the observed correlation between smoking and cancer is not the effect of smoking at all — it's the shared genetic origin of both. When you compare smokers to non-smokers, you are partly comparing people with different genotypes, and some of what looks like the effect of smoking is actually the effect of genotype. This is the confounding problem in miniature. Chapter 3 is dedicated to it.</p>

<h4>Colliders: The One That Breaks Intuition</h4>

<p>A <strong>collider</strong> is three nodes where two arrows point <em>into</em> the middle node:</p>

<!-- LATEX: A → B ← C -->

<p><em>A</em> and <em>C</em> both cause <em>B</em>. They both "collide" at <em>B</em>, which is where the name comes from.</p>

<p>Here is the rule that every student I've taught finds counterintuitive:</p>

<p><strong>A and C are not correlated through a collider. But if you condition on the collider, they become correlated.</strong></p>

<p>Let me say that again, because it matters. The natural, unconditioned state of a collider is <em>no association</em> between its parents. Conditioning — controlling for, stratifying on, selecting based on — the collider <em>creates</em> an association that was not there before.</p>

<p>This is the exact opposite of what happens with chains and forks. For chains and forks, conditioning on the middle node removes association. For colliders, conditioning on the middle node adds association. Students learn the first pattern easily and then apply it to colliders, and they get everything wrong.</p>

<p>Here is where I'll slow down, because this is the single most common source of advanced-level errors in causal inference.</p>

<h4>Worked Example: Berkson's Paradox</h4>

<p>In 1946, the Mayo Clinic biostatistician Joseph Berkson pointed out a puzzle that now carries his name. Suppose there are two diseases, <em>A</em> and <em>C</em>, that are biologically independent. Having disease <em>A</em> has no effect on whether you have disease <em>C</em>, and vice versa. In the general population, the two are uncorrelated.</p>

<p>Now you run a study using hospital patients. You look at everyone who shows up to the hospital and ask: among hospital patients, are disease <em>A</em> and disease <em>C</em> correlated?</p>

<p>They will be. <em>Negatively.</em> Inside the hospital, the two diseases appear to repel each other, as if being sick with one protected you from the other.</p>

<p>How can this happen if they're independent in the general population?</p>

<!-- FIGURE 2.2: A three-node collider. A (Disease A) → H (Hospitalization) ← C (Disease C). No arrows between A and C. Caption: Both diseases cause hospitalization; neither causes the other. H is a collider on the path from A to C. -->

<p>Disease <em>A</em> makes you more likely to go to the hospital. Disease <em>C</em> also makes you more likely to go to the hospital. <em>H</em> (hospitalization) is a collider — both diseases collide at it.</p>

<p>In the general population, <em>A</em> and <em>C</em> are independent. Fine. But now restrict your attention to hospitalized patients only — that is, condition on H = yes. Here's the reasoning that makes the paradox feel intuitive.</p>

<p>If I meet a hospitalized patient, I know they're in the hospital for <em>some</em> reason. If it's not disease <em>A</em>, it probably has to be disease <em>C</em> (or something else sick enough to hospitalize them). Knowing they don't have <em>A</em> raises the probability they have <em>C</em> — not because the biology has changed, but because the selection process made it so.</p>

<p>Let me put numbers on it. Imagine a population of 10,000 people. Suppose 5% have disease <em>A</em> and 5% have disease <em>C</em>, independently. So about 500 have <em>A</em> alone, 500 have <em>C</em> alone, 25 have both (5% of 5%), and roughly 8,975 have neither.</p>

<p>Suppose anyone with a disease goes to the hospital. Nobody without a disease goes. Then the hospital population consists of:</p>

<ul>
<li>500 with <em>A</em> only</li>
<li>500 with <em>C</em> only</li>
<li>25 with both</li>
</ul>

<p>Total hospitalized: 1,025.</p>

<p>Among hospitalized patients, the probability of <em>C</em> given <em>A</em> is 25 / 525 ≈ 4.8%. The probability of <em>C</em> given <em>not A</em> is 500 / 500 = 100%. Having disease <em>A</em>, inside the hospital, looks enormously <em>protective</em> against disease <em>C</em>. In the general population, <em>A</em> tells you nothing about <em>C</em>. Inside the hospital, it tells you almost everything.</p>

<p>The collider created the association. Nothing about the biology changed. The selection did the work.</p>

<h4>Worked Example: The Dating Pool</h4>

<p>A less clinical version, same structure. Suppose in the general population, attractiveness and kindness are independent. Some people are both, some are neither, some are one or the other; knowing one tells you nothing about the other.</p>

<p>Now think about the people you actually date, or consider dating. For most people, the dating filter is roughly: <em>I'd date someone who is either attractive enough to catch my eye, or kind enough that I don't care.</em> Call the dating pool <em>D</em>.</p>

<!-- FIGURE 2.3: Three-node collider. A (Attractiveness) → D (Dating pool) ← K (Kindness). No arrows between A and K. Caption: Attractiveness and kindness are independent in the general population; both raise the chance someone enters your dating pool; D is a collider. -->

<p>A → D ← K. Colliders.</p>

<p>In the general population, <em>A</em> and <em>K</em> are uncorrelated. Inside your dating pool, they look negatively correlated. The attractive people you meet are, on average, less kind; the kind people you meet are, on average, less attractive. The people who are both are rare, not because they don't exist in the world, but because <em>you only notice them at the rate they exist in the world</em>, while you over-sample people who made the pool on the strength of just one trait.</p>

<p>Many of life's "you can't have everything" feelings are collider effects from selection.</p>

<h4>Summary of the Three Structures</h4>

<p>Here's what you should be able to recite:</p>

<ul>
<li><strong>Chain</strong> (A → B → C): <em>A</em> and <em>C</em> are associated through <em>B</em>. Conditioning on <em>B</em> blocks the association.</li>
<li><strong>Fork</strong> (A ← B → C): <em>A</em> and <em>C</em> are associated because of <em>B</em>. Conditioning on <em>B</em> blocks the association.</li>
<li><strong>Collider</strong> (A → B ← C): <em>A</em> and <em>C</em> are <em>not</em> associated. Conditioning on <em>B</em> <em>creates</em> an association.</li>
</ul>

<p>The collider is the weird one. If you remember nothing else from this chapter, remember that conditioning is not always a good thing. It is a tool. It removes some associations and creates others. Which it does depends on the structure. You cannot know which without the diagram.</p>

<hr>

<h3>Concept 3: Paths, d-Separation, and the Mediator Warning</h3>

<p>We now have the building blocks. Let me show you how to reason about a whole diagram.</p>

<h4>What a Path Is</h4>

<p>A <strong>path</strong> between two nodes is a sequence of edges that connects them, <em>regardless of the direction of the arrows</em>. Paths can run with the arrows, against them, or mix.</p>

<p>A <strong>directed path</strong> is a path where all the arrows point the same direction, tracing a chain of causation from the start to the end.</p>

<p>A <strong>back-door path</strong> from <em>A</em> to <em>B</em> is a non-directed path that starts with an arrow pointing <em>into</em> <em>A</em>. Back-door paths are the signature of confounding — they connect cause and effect through a shared origin rather than through causation.</p>

<p>In our smoking diagram, the path S → T → C is a directed path from smoking to cancer — the genuine causal path. The path S ← G → C is a back-door path — it connects smoking and cancer through their shared cause, the genotype. Both paths create association between <em>S</em> and <em>C</em> in the data. Only one of them represents the causal effect we care about.</p>

<!-- FIGURE 2.4: The four-node diagram from Figure 2.1 with two paths visually distinguished. The directed path S → T → C shown in one style, the back-door path S ← G → C shown in another. Caption: The association between smoking and cancer in observational data has two sources: the real causal effect running through tar, and the confounding path running through genotype. -->

<h4>The Idea of d-Separation</h4>

<p>With paths defined, I can state the central idea of this chapter.</p>

<p>Two variables in a diagram are <strong>d-separated</strong> by a set <em>Z</em> of conditioning variables if every path between them is <em>blocked</em> by <em>Z</em>. When two variables are d-separated, they are statistically independent given <em>Z</em>. When they are not — when at least one path remains open — they can be statistically associated.</p>

<p>A path is blocked in two ways, and this is where you have to be careful because colliders flip the rule:</p>

<ul>
<li><strong>At a chain or fork node</strong> (→ M → or ← M →): the path is blocked if you <em>do</em> condition on <em>M</em>.</li>
<li><strong>At a collider node</strong> (→ M ←): the path is blocked if you do <em>not</em> condition on <em>M</em> (and do not condition on any descendant of <em>M</em>).</li>
</ul>

<p>That second point about descendants deserves a note. Conditioning on a collider opens the path. So does conditioning on anything downstream of the collider — any variable the collider causes. If you condition on a variable that is a collider's descendant, you partially condition on the collider itself, and the path partially opens. For now, remember the simple version: don't condition on colliders or their descendants if you want to keep the path closed.</p>

<p>I'll state the full d-separation procedure as a recipe you can run by hand:</p>

<ol>
<li>List all paths between the two variables.</li>
<li>For each path, go through the intermediate nodes one by one.</li>
<li>If any non-collider on the path is in <em>Z</em>, the path is blocked.</li>
<li>If the path has a collider and neither the collider nor any descendant of it is in <em>Z</em>, the path is blocked.</li>
<li>If after all that, every path is blocked, the two variables are d-separated given <em>Z</em>, and they are statistically independent given <em>Z</em>.</li>
<li>If even one path remains open, they are not d-separated, and they are likely associated given <em>Z</em>.</li>
</ol>

<p>This is the whole engine. Everything in the next several chapters — confounding adjustment, instrumental variables, selection bias, collider control — is applied d-separation. If you can run this procedure, you can reason about when a statistical association reflects a causal effect and when it reflects something else.</p>

<h4>Worked Example: Running the Procedure</h4>

<p>Let me use the smoking diagram to run through it. I want to ask: <em>is smoking independent of cancer if I condition on tar and genotype?</em></p>

<p>The question is really: <em>is the diagram telling us that controlling for tar and genotype would leave no association between smoking and cancer?</em></p>

<p>List the paths from <em>S</em> to <em>C</em>:</p>

<ol>
<li>S → T → C (direct causal path through the mediator)</li>
<li>S ← G → C (back-door path through the confounder)</li>
</ol>

<p>Conditioning set: Z = {T, G}.</p>

<p>Path 1: S → T → C. Pass through <em>T</em>. <em>T</em> is a chain node (arrow in, arrow out). <em>T</em> is in <em>Z</em>. Path blocked.</p>

<p>Path 2: S ← G → C. Pass through <em>G</em>. <em>G</em> is a fork node (arrows pointing out both directions). <em>G</em> is in <em>Z</em>. Path blocked.</p>

<p>Both paths blocked. <em>S</em> and <em>C</em> are d-separated given {T, G}. The diagram is claiming that if you stratified on both tar and genotype, smoking and cancer would show no residual association.</p>

<p>Is this the answer we want? Only if our question is "are smoking and cancer associated once we account for everything the diagram says connects them." If our question is "what is the causal effect of smoking on cancer," then blocking <em>the directed path</em> S → T → C is exactly the wrong thing to do — because that path <em>is</em> the causal effect. Which brings me to the warning.</p>

<h4>The Mediator Warning</h4>

<p>A <strong>mediator</strong> is a variable on a directed path from cause to effect. In the smoking diagram, tar is a mediator: it's the middleman through which smoking causes cancer.</p>

<p>Controlling for a mediator, in most analyses, is a mistake.</p>

<p>Here's why. The causal effect of smoking on cancer runs through tar. That is the mechanism. If you condition on tar — if you compare smokers and non-smokers who have the <em>same tar level in their lungs</em> — you've removed the pathway through which smoking does its damage. You're asking: "holding constant the amount of tar in the lungs, does smoking affect cancer?" And the answer, under the diagram I drew, is <em>no</em>, because all the effect ran through tar in the first place. You'll conclude smoking has no effect on cancer. You'll be wrong, not because the data is wrong, but because you blocked the path you were trying to measure.</p>

<p>This is different from controlling for a confounder like genotype. Genotype is not on the causal path from smoking to cancer — it's a shared cause. Blocking the path through genotype removes confounding. Blocking the path through tar removes the signal itself.</p>

<p>Students confuse these two constantly. Both involve "controlling for a variable." Both look, in a regression output, identical — you add a term to the model. But one operation removes a bias you don't want, and the other operation removes the effect you were trying to see. The diagram tells you which is which. A regression equation does not.</p>

<p>I'll say this as plainly as I can: <strong>do not control for variables that lie on the causal path from your treatment to your outcome.</strong> If you're measuring the effect of smoking on cancer and someone tells you "you forgot to control for tar" — they are wrong. Tar is not a confounder. Tar is the mechanism. Chapter 3 will return to this, because the failure mode is common and expensive, and it hides inside ordinary-looking regressions.</p>

<hr>

<h3>Integration: Reading a Real Diagram</h3>

<p>Let me put everything together on a slightly bigger diagram. Here's the setup: we're interested in the effect of a job training program on wages. Participants self-select into the program. Prior work history affects both whether someone signs up and their eventual wages. Motivation (unobserved) affects both sign-up and wages. The program, if it works, affects wages by improving skills.</p>

<p>Variables:</p>

<ul>
<li><em>W₀</em>: Prior work history</li>
<li><em>M</em>: Motivation</li>
<li><em>P</em>: Program participation</li>
<li><em>S</em>: Skills (post-program)</li>
<li><em>W₁</em>: Wages after the program</li>
</ul>

<p>The story: prior work history affects program participation and also affects wages directly (experience matters regardless of training). Motivation affects participation and also wages directly (motivated workers earn more even without the program). Program participation raises skills. Skills raise wages.</p>

<!-- FIGURE 2.5: A five-node DAG. W₀ (Prior Work) has arrows to P (Program) and W₁ (Wages). M (Motivation) has arrows to P and W₁. P has an arrow to S (Skills). S has an arrow to W₁. Caption: The causal structure underlying a job training program evaluation. P is the treatment, W₁ is the outcome, S is a mediator of the program's effect, and W₀ and M are confounders. -->

<p>Let me ask the causal-inference question: <em>what is the effect of the program on wages?</em></p>

<p>Paths from <em>P</em> to <em>W₁</em>:</p>

<ol>
<li>P → S → W₁ (the directed causal path — the program raises skills, which raises wages)</li>
<li>P ← W₀ → W₁ (back-door through prior work)</li>
<li>P ← M → W₁ (back-door through motivation)</li>
</ol>

<p>Path 1 is the effect we want. Paths 2 and 3 are confounding.</p>

<p>To identify the causal effect, we want to block paths 2 and 3 without blocking path 1. Condition on <em>W₀</em> and <em>M</em>. That blocks the two back-door paths (both are forks; conditioning on the fork node closes them) and leaves the directed path open.</p>

<p>What we must <em>not</em> do: condition on <em>S</em>. Skills is on the causal path. Conditioning on <em>S</em> blocks path 1, the very thing we're trying to measure. An analyst who thinks "the more I control for, the cleaner the estimate" will put <em>S</em> into the regression and wipe out the program's effect. The diagram says no.</p>

<p>There's a second issue. Motivation is unobserved. We cannot condition on what we cannot measure. If <em>M</em> is truly unobservable, then path 3 stays open no matter what else we condition on, and the program effect is not identified from this diagram alone. We would need a different tool — a randomized trial, an instrumental variable, a natural experiment — to cut the confounding path we can't close by conditioning. This is a preview of what the rest of the book is for.</p>

<p>The diagram is doing an enormous amount of work here. It has separated the good thing to control for (<em>W₀</em>), the thing that must not be controlled for (<em>S</em>), and the thing we cannot control for (<em>M</em>) into three categories that look identical in a data table. Only the causal structure tells them apart.</p>

<hr>

<h3>Exercises</h3>

<p>Do these with paper and pencil. The point is to move the rules from recognition to fluency.</p>

<h4>Warm-up</h4>

<p><strong>Exercise 2.1</strong> <em>(Objective 1: read a diagram.)</em> Given the three-node diagram A → B → C: write in plain English what causal claims this diagram is making. What is it claiming <em>doesn't</em> exist?</p>

<p><strong>Exercise 2.2</strong> <em>(Objective 3: identify elementary structures.)</em> For each of the following, state whether it is a chain, a fork, or a collider:</p>

<ul>
<li>X → Y → Z</li>
<li>X ← Y → Z</li>
<li>X → Y ← Z</li>
<li>X ← Y ← Z</li>
</ul>

<p>(The last one is a chain read right to left. Chains don't care which side you start from.)</p>

<p><strong>Exercise 2.3</strong> <em>(Objective 3: identify structures in context.)</em> In the five-node job training diagram from the integration section, identify one chain, one fork, and one collider. (Hint for the collider: which node has two arrows pointing in?)</p>

<h4>Application</h4>

<p><strong>Exercise 2.4</strong> <em>(Objective 2: draw a diagram from a story.)</em> Translate the following story into a causal diagram. "A person's education level affects both the kind of job they get and their income directly. The kind of job they get also affects their income. Parental income affects their education level and also directly affects their eventual income through inheritance and connections." Draw the diagram. How many nodes? How many arrows? What does your diagram claim is <em>not</em> a direct cause of income?</p>

<p><strong>Exercise 2.5</strong> <em>(Objectives 2 and 3.)</em> An epidemiologist tells you: "We looked at hospitalized patients and found that smokers had lower rates of a certain inflammatory disease than non-smokers — smoking appeared protective." Draw a diagram that could explain this finding without any protective biological effect of smoking on the disease. Name the collider in your diagram.</p>

<p><strong>Exercise 2.6</strong> <em>(Objective 4: trace paths.)</em> In the smoking/tar/cancer/genotype diagram (Figure 2.1), list <em>all</em> paths from <em>S</em> to <em>C</em>. For each, say whether it is a directed path or a back-door path.</p>

<p><strong>Exercise 2.7</strong> <em>(Objective 6: recognize mediators.)</em> In each of the following pairs, state which variable (if either) is a mediator of the effect of the first variable on the last:</p>

<ul>
<li>Smoking → Tar → Cancer. What is the mediator?</li>
<li>Smoking ← Genotype → Cancer. What is the mediator, or is there none?</li>
<li>Exercise → Cardiovascular fitness → Longevity. What is the mediator?</li>
</ul>

<h4>Synthesis</h4>

<p><strong>Exercise 2.8</strong> <em>(Objectives 3, 5, and 6.)</em> Consider this diagram: X → M → Y, and separately X ← U → Y, where <em>U</em> is unobserved. All four nodes are distinct. (a) List all paths from <em>X</em> to <em>Y</em>. (b) Which paths are open if you condition on nothing? (c) Which paths are open if you condition on <em>M</em>? (d) Which paths are open if you condition on <em>U</em>? (e) Is the causal effect of <em>X</em> on <em>Y</em> identifiable by any conditioning strategy in this diagram? Justify your answer.</p>

<p><strong>Exercise 2.9</strong> <em>(Objectives 3, 4, 5.)</em> Given the diagram A → B → C ← D, where <em>A</em> and <em>D</em> are otherwise unconnected:</p>

<ul>
<li>What kind of structure is at <em>C</em>?</li>
<li>Are <em>A</em> and <em>D</em> associated if you condition on nothing?</li>
<li>Are <em>A</em> and <em>D</em> associated if you condition on <em>C</em>?</li>
<li>Are <em>A</em> and <em>D</em> associated if you condition on <em>B</em> and <em>C</em>?</li>
</ul>

<p><strong>Exercise 2.10</strong> <em>(Objectives 5, 6.)</em> You are evaluating a weight-loss program. Participation is voluntary. You have data on starting weight, ending weight, motivation (measured by a validated survey), and program participation. Someone suggests you control for ending weight to "clean up" the analysis. Draw a diagram of this scenario and explain, using the diagram, why controlling for ending weight is the wrong move.</p>

<h4>Challenge</h4>

<p><strong>Exercise 2.11</strong> <em>(Objectives 2, 5, 6; open-ended.)</em> Find a real observational study in a field you know something about. Read the methods section carefully. Try to draw the causal diagram the authors implicitly assume. Then ask: do any of the variables they controlled for lie on the causal path from their treatment to their outcome? If yes, what would the diagram predict about the bias their analysis introduces? This exercise takes longer than the others and is where this chapter starts paying off.</p>

<p><strong>Exercise 2.12</strong> <em>(Beyond this chapter.)</em> In the integration example, motivation <em>M</em> was unobserved and so path P ← M → W₁ could not be blocked by conditioning. Propose one <em>non-conditioning</em> strategy that might let you estimate the program's effect despite the unobservable confounder. (You don't need to know the formal machinery yet. Think like a researcher who wants to outwit the confounding.) We'll develop the formal tools in Chapter 5.</p>

<hr>

<h3>Chapter Summary</h3>

<p>If you've worked through this chapter, here is what you should now be able to do.</p>

<p>You can read a causal diagram and state, in plain English, the causal claims it is making and the claims it is implicitly denying. You can take a verbal story about how the world works and draw a diagram that captures its causal structure. You can identify chains, forks, and colliders inside any diagram and state the rule for each: chains and forks transmit association until you condition; colliders block association until you condition, at which point they start transmitting it.</p>

<p>You can trace paths between any two nodes and distinguish the directed paths (which represent causal effects) from back-door paths (which represent confounding). You can apply d-separation to decide whether two variables are independent given a conditioning set: a path is blocked at a chain or fork if you condition on the middle node, and blocked at a collider if you do not. When every path is blocked, the variables are d-separated and statistically independent.</p>

<p>Most importantly, you can recognize a mediator and resist the impulse to control for it. A mediator lies on the causal path you are trying to measure. Controlling for it removes the signal, not the noise. This is the single most common advanced-level mistake in causal inference, and it survives inside regressions where nothing else looks wrong.</p>

<p>The idea from this chapter that matters most is this: <strong>conditioning is not a clean operation.</strong> It removes some kinds of association and creates others. Which it does depends on the causal structure. No amount of sophisticated statistics recovers what the diagram tells you to do and not do.</p>

<p>The common mistake to watch for: <em>controlling for everything you measured.</em> The impulse is wrong. You should control for confounders and leave mediators alone, and only the diagram tells you which is which.</p>

<p>The Feynman test for this chapter: can you explain to someone who has never seen a causal diagram why, inside a hospital, two unrelated diseases can appear negatively correlated? If you can walk them through it using a picture and get them to see the reasoning, you understand this chapter.</p>

<hr>

<h3>Connections Forward</h3>

<p>Chapter 3 takes the biggest problem this chapter named — confounding — and gives you the tools to solve it. We'll talk about the back-door criterion, which is a precise statement of when conditioning suffices to block all confounding paths; about propensity scores, which let you handle many confounders at once; and about the two ways a regression can go wrong even when the diagram is correct.</p>

<p>Chapter 4 deals with what Chapter 3 cannot: situations where the confounder is unobserved and no amount of conditioning helps. That is where randomization, natural experiments, and instrumental variables come in. The diagram tells you when you need those tools.</p>

<p>Every chapter from here on builds on the vocabulary I just taught you. If the exercises felt hard, good — redo them. If they felt easy, you are either very fast or missing something subtle. The collider chapter, Chapter 6, will tell you which.</p>

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Sander Greenland** spent decades teaching epidemiologists to read causal diagrams properly — and translated Pearl's mathematical formalism into language working researchers could use. His papers on confounding, selection bias, and effect modification taught a generation.

**Run this:**

```
Who is Sander Greenland, and how does his work on causal diagrams in epidemiology connect to the diagram language we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Sander Greenland"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Greenland's distinctions among confounding, selection bias, and effect modification to one specific applied example.
- Ask it about Greenland's critique of the standard p-value culture in observational epidemiology.

What changes? What gets better? What gets worse?
