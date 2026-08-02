# The Backdoor Criterion (Part 1): Writing the Rule Down


## TL;DR

- TL;DR: For four weeks you have been blocking confounders, leaving mediators alone, and refusing to condition on colliders — a stack of intuitions that worked case by case.
- The chapter moves through Opening — You have been doing this informally for four weeks, Concept one — Backdoor paths defined precisely, Concept two — The criterion's first condition, Mid-chapter checkpoint, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. The Backdoor Criterion (Part 1): Writing the Rule Down
2. Path-Tracing as a Procedure: Pearl's Backdoor Criterion in One Page
3. The Rule You Have Been Following Already

**TL;DR:** For four weeks you have been blocking confounders, leaving mediators alone, and refusing to condition on colliders — a stack of intuitions that worked case by case. Pearl's backdoor criterion is the single rule those intuitions were converging on: a set Z is a valid adjustment set for the effect of T on Y if Z blocks every backdoor path from T to Y, and the procedure for checking that condition is mechanical the moment the DAG is fixed.

**Byline:** Nik Bear Brown

**Prerequisites:**
- Trace paths on a directed acyclic graph and classify intermediate variables as forks, chains, or colliders. (Ch. 3.)
- State the structural definition of a confounder and find a valid adjustment set by inspection. (Ch. 5.)
- Distinguish a confounder from a mediator on the basis of structural position rather than correlation. (Ch. 6.)
- State why conditioning on a collider opens a path that was closed. (Ch. 7–8.)
- Comfortably read `T ← Z → Y` as "Z is a common cause of T and Y" and `T → M → Y` as "M is on the causal path from T to Y."

**Learning objectives:**
- **Apply (Part A):** Given a 5–7 node DAG, enumerate every backdoor path from a treatment T to an outcome Y.
- **Apply (Part A):** Given a candidate adjustment set Z, verify whether Z satisfies the backdoor criterion's first condition — every backdoor path is blocked.
- **Apply (Part A):** Carry the path-tracing procedure end-to-end on a multi-confounder scenario, including one with an unmeasured variable.
- **Analyze (Part B):** Apply the criterion to your own candidate DAG from Chapters 5–8 and assess whether the adjustment decisions you have already made are valid.
- **Evaluate (Part B):** Identify a published causal claim, draw the implied DAG, and run path-tracing on it. State whether the authors' adjustment set satisfies the criterion or fails it.

---

## 1. Opening — You have been doing this informally for four weeks

Pull up the DAGs you have been drawing since Chapter 5. The Amazon recruiting case with the unmeasured `H` for historical hiring practice. The Obermeyer scenario where `spending` looked like a confounder until the access variable `A` pulled the structure apart. The mediator examples from Chapter 6 where conditioning on a node carrying part of the causal effect quietly amputated the estimand. The collider examples from Chapters 7 and 8 where conditioning *opened* a path you thought you were closing.

Look at the motions your hand was making. *Trace this path. Block this one. Do not condition on that one. Watch out for this collider.* You had a procedure. You did not call it a procedure. You ran it on each DAG that came in front of you, and you mostly got the right answer, and on the cases where you got the wrong answer you went back and you noticed the structural feature you had missed — the M-bias path, the inadvertent collider opening, the mediator masquerading as a confounder. The procedure was real. It lived in your head as a collection of heuristics anchored to a specific kind of object.

Here is the thing I want to say at the front of this chapter, because it changes how you read the rest of it. You have been approximating a single criterion. It has a name. Judea Pearl introduced it in a 1995 *Biometrika* paper ([Pearl, 1995](https://doi.org/10.1093/biomet/82.4.669)) and gave it its definitive statement in *Causality* §3.3 ([Pearl, 2009](https://bayes.cs.ucla.edu/BOOK-2K/)). It is called the *backdoor criterion*, and the moves you have been making — block this, not that, never the collider — are the criterion under the hood.

Why does this matter? Because when the procedure has a name, you can write it down. You can hand it to a colleague. You can hand it to software. You can prove things about it. You can audit your work against it. You can teach it to a student in an afternoon instead of in four weeks of careful structural intuition-building.

I want you to feel two things at once as you read this chapter. The first is relief. The procedure was always there; you have already been running it; now you get to know what it is called. The second is a sober recognition. The criterion is a *graphical* criterion. It tells you what to do given a DAG. It does not give you the DAG. The DAG is still the artifact of the conversation between the analyst and the domain expert, and a wrong DAG produces a confidently wrong adjustment set when you push the procedure through it. The four-week build was not wasted effort. It was the training that lets you spot when the criterion's input is bad.

This chapter teaches the criterion's first condition — the path-blocking condition. The second condition (no descendants of T in Z) gets its full unpacking in Chapter 10, which also handles the harder questions: when is there a *minimal* valid Z, and what do you do when no valid Z exists at all? The chapter you are reading is the integrating chapter. Five through eight built the pieces. Nine names the rule.

Let us begin where the rule begins: with what counts as a backdoor path.

---

## 2. Concept one — Backdoor paths defined precisely

A backdoor path from a treatment T to an outcome Y is any path connecting T and Y that *starts with an arrow into T*.

Read that sentence twice. The defining feature is not "the path goes through a confounder." It is not "the path is correlation-bearing." It is a *structural* feature of the path's first edge at the T end: the arrowhead points *into* T.

Why is that the right definition? Because every path from T to Y either starts with an arrow out of T or an arrow into T. The paths starting with an arrow out of T are the *causal* routes — T pushes into something, which pushes into something, which eventually pushes into Y. Those are the paths whose effect you are trying to estimate. You do not want to block them. The paths starting with an arrow into T are everything else — the routes by which non-causal association can flow between T and Y. Those are the paths that need blocking.

Here is the simplest possible picture.

```
        Z
       / \
      ↓   ↓
      T   Y
      └───→  (the causal arrow)
```

`Z` is a common cause of `T` and `Y`. The path `T ← Z → Y` is a backdoor path: at T's end, the arrowhead points *into* T (the arrow goes `Z → T`, so the T-end of the path is an into-arrow). The path `T → Y` is causal: at T's end, the arrow points *out of* T. The graph has exactly two paths from T to Y. One is backdoor. One is causal. The criterion is going to tell you to block one and leave the other open.

Now a slightly bigger example, to make sure the definition has teeth.

```
       Z1       Z2
       |        |
       ↓        ↓
       T ───→ M ───→ Y
       ↑              ↑
       └──── Z3 ──────┘
```

Edges: `Z1 → T`, `Z2 → M`, `T → M`, `M → Y`, `Z3 → T`, `Z3 → Y`.

Paths from T to Y:

- `T → M → Y` — causal (out of T at T's end).
- `T ← Z1 → ?` — Z1 has no other outgoing edges in this diagram, so this is not a complete path to Y. Skip.
- `T ← Z3 → Y` — backdoor (into T at T's end). Z3 is a common cause.
- `T → M ← Z2` — partial; Z2 has no path to Y here. Skip.

So this DAG has one backdoor path: `T ← Z3 → Y`. The criterion is going to tell us to block it. The causal path `T → M → Y` we leave alone.

One more piece of vocabulary, because we are going to use it constantly. Walking along a backdoor path, each non-endpoint variable plays one of three roles, determined by the directions of the two arrows it sits between:

- **Chain (`→ V →`)** — the arrows pass through V. V is a *non-collider*.
- **Fork (`← V →`)** — the arrows diverge from V. V is a *non-collider*.
- **Collider (`→ V ←`)** — the arrows collide at V. V is a *collider*.

A path is *open* (also called "d-connected") when association can flow along it. The rules are the ones you learned in Chapters 5–8 and are about to see consolidated:

- A non-collider on the path is open unless you condition on it. Conditioning on it closes the path at that point.
- A collider on the path is closed unless you condition on it (or any of its descendants). Conditioning opens it.

That is the entire local rule. Block the path means: somewhere along the path, the flow is interrupted by these conditioning rules. A backdoor path is blocked when at least one of its non-colliders is in the conditioning set Z, *or* it contains a collider with no descendants in Z (and is not itself in Z).

Read those two bullets one more time. Then forget them as words and remember them as motion. *Non-collider you condition on → flow stops there. Collider you do not condition on → flow stops there.* That is the entire path-blocking machinery you have been running for four weeks.

**Common misconception:** "A backdoor path is any path through a confounder." Close, but the definition fails. *A path is backdoor if and only if its first edge at the T end points into T.* A path that happens to contain a common ancestor of T and Y is a backdoor path only if it enters T from an arrowhead. The structural definition is sharper, and the chapter's procedure needs the sharper version.

---

## 3. Concept two — The criterion's first condition

Here is the rule, stated formally.

> **The backdoor criterion (Pearl 1995, 2009 §3.3) — first condition.** A set Z of variables satisfies the first condition of the backdoor criterion for the effect of T on Y if Z *blocks every backdoor path* from T to Y.

That is it. One sentence. The condition reduces the entire problem of "what should I adjust for" to the problem of "did I block every backdoor path with this Z."

(There is a second condition — Z contains no descendants of T — which we will mention briefly later and unpack fully in Chapter 10. Hold it aside for now.)

What does it mean for Z to *block* a backdoor path? You already know the local rule from §2. Let me say it once more in the form you will use:

> A backdoor path is **blocked by Z** if either (a) the path contains a non-collider that is in Z, or (b) the path contains a collider such that neither the collider nor any of its descendants is in Z.

Both conditions count. The path is blocked if *any* point along it is closed by the rules. The path is *open* — fails to be blocked — only if every non-collider on the path is outside Z and every collider on the path has the collider itself or one of its descendants inside Z.

When the criterion's first condition is satisfied, *and* the second condition holds (no descendants of T in Z), Pearl's adjustment formula identifies the causal effect from observational data:

$$
P(Y \mid \mathrm{do}(T = t)) \;=\; \sum_{z} P(Y \mid T = t,\, Z = z)\, P(Z = z)
$$

The right side is computable from the joint distribution `P(T, Y, Z)`. The left side is the interventional quantity you wanted. The formula trades the experiment you did not run for an adjustment you can compute, provided the criterion holds and the DAG is right. ([Pearl 2009](https://bayes.cs.ucla.edu/BOOK-2K/) §3.3.)

Watch the criterion do its work on a small case.

```
       T ←── U ──→ Y
       │            ↑
       └── M ───────┘
```

Edges: `U → T`, `U → Y`, `T → M`, `M → Y`.

Paths from T to Y:

- `T → M → Y` — causal.
- `T ← U → Y` — backdoor (into T at T-end), U is a fork (non-collider).

Backdoor paths: one. Candidates for Z that block it:

- `Z = {U}` — U is a non-collider on the backdoor path and is in Z. Block achieved. The first condition is satisfied.
- `Z = {M}` — M is not on the backdoor path. The backdoor path is not blocked. First condition fails.
- `Z = {U, M}` — U blocks the backdoor path. M is on the *causal* path. Including M does not violate the first condition (which speaks only about backdoor paths). But conditioning on M would amputate the estimand — it would block part of the causal effect we are trying to measure. The first condition does not catch this; the second condition (no descendants of T in Z) does. We will return to this in §6.
- `Z = ∅` — no variables conditioned on. The backdoor path is open at U (a fork that is not in Z is open). First condition fails.

So in this DAG, `Z = {U}` is a valid adjustment set under the criterion's first condition, and it is the only minimal set that satisfies it.

**Common misconception:** "If I condition on every variable I have data for, the criterion is satisfied." It is not. The criterion is about path-blocking, not variable-listing. A variable that is a collider on a backdoor path *opens* the path when conditioned on, and "I have data for it" is not a reason to include it. Inclusion is a decision, not a default. (You knew this from Chapters 7–8. The criterion encodes the discipline rather than relieving you of it.)

A second common misconception: "If I cannot measure the confounder, the criterion automatically fails." It depends on the structure. If an unmeasured variable sits on a backdoor path *and no other variable on that path can block it*, then yes, the criterion is unsatisfiable in the observed variables. But many backdoor paths can be blocked at multiple points; an unmeasured upstream variable does not always doom the analysis if a downstream non-collider on the same path is measured. This is one of the reasons path-tracing on the actual DAG matters more than "do I have every confounder in my data."

---

## Mid-chapter checkpoint

Stop for a moment. You can now do two things you could not do reliably at the start of the chapter.

You can *recognize* a backdoor path by inspecting its first edge at the T end — arrow pointing into T, backdoor path.

You can *state the first condition* of the criterion as a single sentence — block every backdoor path from T to Y — and apply it to a candidate Z.

What remains is to turn those two skills into a procedure you can run in order, end to end, on any DAG someone hands you. That is the next section.

---

## 4. Concept three — Path-tracing as a procedure (the chapter's mechanism)

This is the section where the chapter earns its place. Everything before was setup. Everything after follows.

Here is the procedure, stated as steps you can run on paper, on a whiteboard, or in code:

1. **Enumerate every path from T to Y.** Walk the DAG. List all simple paths (no repeated nodes) connecting T and Y, regardless of arrow direction.
2. **Classify each path.** For each path, look at the edge incident to T. If the arrow points *out of* T, the path is causal — leave it alone. If the arrow points *into* T, the path is a backdoor path — needs blocking.
3. **For each backdoor path, identify the variables on it and their roles** (chain, fork, collider) based on the directions of the two adjacent arrows at each variable.
4. **Choose a candidate adjustment set Z.** Z should include at least one non-collider on every backdoor path; Z should *not* include any collider on a backdoor path (or any descendant of such a collider) unless you have a specific structural reason.
5. **Verify.** For each backdoor path, check the block condition: is at least one non-collider in Z, OR is there a collider on the path with neither itself nor its descendants in Z? If yes, the path is blocked. If every backdoor path is blocked, the first condition is satisfied.
6. **Check the second condition.** Confirm no variable in Z is a descendant of T. (Full treatment in Chapter 10. Today: just check.)
7. **Done.** If every backdoor path is blocked and no descendants of T are in Z, Z is a valid adjustment set. The adjustment formula identifies `P(Y | do(T))`.

Let me run the procedure end-to-end on a six-node DAG. I will use a pricing scenario because it is engineering-native and because the pantry notes lay out the structure cleanly.

**Scenario.** A pricing team has logged six months of data on a regional product. They want to estimate the causal effect of price `P` on revenue `R` so they can decide whether a planned 5% price increase is wise. The data is observational — the price was set by an existing pricing algorithm, not randomized.

**Variables and edges.** The team's pricing scientist draws the DAG below after a conversation with the demand-modeling lead and the regional sales head:

- `T` (time-of-day) `→ P`: the pricing algorithm raises prices at peak hours.
- `T → R`: revenue at peak hours is higher because more customers are shopping.
- `G` (geography) `→ P`: the algorithm sets different prices in different metros.
- `G → R`: revenue varies by metro for reasons independent of price.
- `C` (customer segment) `→ P`: the algorithm price-discriminates by segment.
- `C → R`: segments have different baseline purchase rates.
- `P → R`: this is the causal effect we want to estimate.
- `U` (latent demand state) `→ P`: when demand is unusually high, the algorithm raises prices.
- `U → R`: when demand is unusually high, revenue rises independent of price.

`U` is unmeasured. The other five variables are in the data.

**Step 1: enumerate paths from P to R.**

```
P → R                            [direct causal path]
P ← T → R
P ← G → R
P ← C → R
P ← U → R
```

I am not claiming these are the only paths — they are the simple ones a careful tracer finds. Longer paths might exist if the DAG had more edges, but with the edges listed, these five are the simple paths from P to R.

**Step 2: classify each.**

| Path             | First edge at P end | Classification |
|------------------|---------------------|----------------|
| `P → R`          | out of P            | causal         |
| `P ← T → R`      | into P              | backdoor       |
| `P ← G → R`      | into P              | backdoor       |
| `P ← C → R`      | into P              | backdoor       |
| `P ← U → R`      | into P              | backdoor       |

Four backdoor paths. One causal path. Good — we know what we are working with.

**Step 3: roles on each backdoor path.**

- `P ← T → R`: T is a fork (`← T →`), non-collider.
- `P ← G → R`: G is a fork, non-collider.
- `P ← C → R`: C is a fork, non-collider.
- `P ← U → R`: U is a fork, non-collider.

No colliders on any backdoor path. Every intermediate variable is a fork.

**Step 4: choose a candidate Z.**

The straightforward play: `Z = {T, G, C}`. Each is a non-collider on a distinct backdoor path. If all three are in Z, those three paths each have at least one non-collider in Z and so each is blocked. The fourth path — through U — has no measured variable on it. We cannot include U in Z, because U is not in the data.

**Step 5: verify.**

- `P ← T → R`: T is a non-collider in Z. **Blocked.**
- `P ← G → R`: G is a non-collider in Z. **Blocked.**
- `P ← C → R`: C is a non-collider in Z. **Blocked.**
- `P ← U → R`: U is a non-collider *not* in Z. No other variable on this path. **Not blocked.**

Three blocked. One open. The first condition is *partially* satisfied — every visible backdoor path is closed, and one path through an unmeasured variable remains open.

**Step 6: descendants of T (the second condition).** None of T, G, C is a descendant of P. The second condition is satisfied for our Z. (Chapter 10 will give this condition its full weight.)

**Step 7: state honestly what we have.**

If the DAG is correct *and U does not exist* — or if U exists but its effects on P and R are negligible — then `Z = {T, G, C}` identifies the causal effect of P on R via the adjustment formula. The estimate `Σ_z P(R | P, Z = z) P(Z = z)` is unbiased.

If U exists and has non-trivial effects, the estimate is biased. The bias is the contribution of the open `U`-path. We will get to Chapter 14 to quantify how much U would have to influence P and R to nullify our estimated effect — that is the E-value, planted here as a seed and harvested then.

This is the realistic case the engineering reader will face. The criterion is *not* a magic wand. It is a precise statement of what the analyst has accomplished and what remains unaccomplished. *Three of four visible backdoor paths blocked. One path through an unmeasured variable open.* Saying that sentence honestly is a more useful artifact than pretending the adjustment is complete.

**A note on the engineering reflex.** When I run this procedure with engineering teams, the most common move at step 5 is to look at the one open path and ask "well, can we get more data?" Sometimes yes. Sometimes the latent demand state is measurable through search-query volume or marketing-spend timing or upstream-channel telemetry that the team has but has not used. The procedure tells you where to look. It is not just a checklist; it is a diagnostic.

**Common misconception:** "Software finds the right adjustment set." Software — DAGitty ([Textor et al. 2016](https://doi.org/10.1093/ije/dyw341)), pgmpy ([pgmpy.org](https://pgmpy.org/)), DoWhy ([Sharma & Kiciman 2020](https://arxiv.org/abs/2011.04216)) — finds the right adjustment set *given a DAG*. The DAG comes from you. The most expensive moment in this procedure is not step 5 (verify); it is the prior step nobody numbered: "the team draws the DAG." Misdraw an arrow there and the criterion's output is precisely as wrong as the misdrawn arrow.

The van der Zander, Liśkiewicz, and Textor 2014 paper ([van der Zander et al. 2014](https://event.cwi.nl/uai2014/papers/63.pdf), UAI '14) gives polynomial-time algorithms for finding minimal adjustment sets given the DAG. The algorithms are clever. They are not, however, in the business of supplying the DAG. DAGitty exposes their algorithms through a browser interface at [dagitty.net](https://www.dagitty.net/), and the engineering reader can run this chapter's pricing example there in five minutes. The output will tell you `Z = {T, G, C}` is a valid set under your DAG. It will not tell you whether your DAG has `U`.

That is the chapter's mechanism. The procedure is mechanical the moment the DAG is fixed. Fixing the DAG is the irreducibly human work.

---

## 5. Concept four — The criterion as integrator of Chapters 5–8

I want you to feel the relief of seeing four weeks of intuition collapse into one rule.

**Confounders (Chapter 5)** are variables that sit as forks or as chain-passers on backdoor paths. The criterion's first condition tells you what to do with them: include enough non-colliders on each backdoor path to block it. Every adjustment-set decision you made in Chapter 5 was an instance of "block the open backdoor path through this confounder."

**Mediators (Chapter 6)** are variables on the *causal* path from T to Y — `T → M → Y`. They are not on any backdoor path. The criterion does not ask you to include them or exclude them; it simply does not mention them, because the first condition is about backdoor paths only. The reason you *should not* include mediators is the second condition: M is a descendant of T, and the second condition excludes descendants of T from Z. (Full unpacking: Chapter 10.) For now, the criterion's silence about mediators in its first condition reflects the fact that mediators sit on causal paths, and causal paths are not the object the criterion is trying to block.

**Colliders (Chapters 7–8)** are the most subtle case. A collider on a backdoor path keeps the path *closed* — until you condition on it. Then the path *opens*. The criterion handles this perfectly in its first condition: blocking is by non-collider conditioning *or* by leaving a collider un-conditioned. The collider rule is the part of the criterion that engineering reflexes most often violate, because "more controls" feels safer than "fewer controls." It is not. Conditioning on a collider creates spurious association. The criterion makes the discipline explicit.

The relief is real. *One sentence — block every backdoor path — encompasses three weeks of structural categories.* The categories were never really separate. They were always pieces of the same machinery. You needed to see the pieces first to recognize the machine.

I want to make this concrete with a single DAG that has all three structures on it.

```
       Z1 ──→ T ──→ M ──→ Y
        │           ↑     ↑
        │           │     │
        └────────→ Z2 ←── Z3
                          │
                          ↓
                          Y
```

Let me redraw the edges as a clean list because the box is starting to lie:

- `Z1 → T`
- `Z1 → Z2`
- `T → M`
- `M → Y`
- `Z3 → Z2`
- `Z3 → Y`

Backdoor paths from T to Y (starting with arrow into T):

- `T ← Z1 → Z2 ← Z3 → Y`. Z1 is a fork (non-collider). Z2 is a collider (`Z1 → Z2 ← Z3`). Z3 is a fork (non-collider). The path has a collider, and the collider is not in Z by default, so the path is *closed* — unless we condition on Z2 (or a descendant of Z2). Do not put Z2 in Z.

Causal path: `T → M → Y`. Do not block.

Adjustment: `Z = {Z1}` blocks the backdoor path (Z1 is a non-collider in Z). Equally, `Z = {Z3}` blocks it (Z3 is a non-collider in Z). Or `Z = ∅` *also* blocks it (the path is closed by the un-conditioned collider Z2). The criterion does not require a non-empty Z. It requires every backdoor path to be blocked, however it is blocked.

If a careless engineer adds Z2 to the adjustment set because "Z2 looks predictive of Y," they have opened the backdoor path that was closed. The criterion catches the move. The engineer who has not learned the criterion does not catch it.

This is the integration. The three structural categories — confounder, mediator, collider — were each a hypothesis about how to act on a particular kind of variable. The criterion is the unified rule that subsumes the three hypotheses into one. *Block every backdoor path without opening new ones.* You have been running this rule, in pieces, since Chapter 5. The chapter you are reading is its consolidation.

---

## 6. Concept five — The E-value seed

I owe you a specific commitment.

At step 5 of the pricing example, we ended with one open path: through the unmeasured `U`. We said the estimate is biased if U exists and has non-trivial effects. We did not say *how* biased.

That is the question Chapter 14 answers. The tool is called the E-value, introduced by VanderWeele and Ding in 2017 in *Annals of Internal Medicine* ([VanderWeele & Ding, 2017](https://doi.org/10.7326/M16-2607)). The E-value tells you: given an observed treatment-outcome association after adjustment, how strongly would an unmeasured confounder have to be associated with both T and Y to fully nullify the association? It converts the worry "what if I missed a confounder" from a vague unease into a number — the minimum strength of confounding required to overturn your conclusion.

I am planting this here because it is the natural completion of the procedure. The backdoor criterion tells you whether your adjustment set blocks every backdoor path *in your DAG*. The E-value tells you how much you should worry about a backdoor path through a variable you did not include in the DAG. The two tools are partners. The criterion handles the visible structure; the E-value handles the structural uncertainty about what you did not see.

When we get to Chapter 14, the pricing example with `U` is the case we will quantify. For now, hold the question. *Three of four visible backdoor paths blocked. One path through an unmeasured variable open. We will quantify the robustness of the estimate in Week 14.* The chapter you are reading does not yet give you the quantification. It gives you the procedure for finding the case where you need it.

---

## 7. Concept six — The criterion is sufficient, not necessary

I have one more piece of honesty to deliver before the worked example.

The backdoor criterion is *sufficient* for identification. If you find a Z satisfying both conditions, the effect is identifiable from observational data via the adjustment formula. But the converse is not true. There are DAGs where no Z satisfies the backdoor criterion, and yet the causal effect is still identifiable by other means.

Three examples of "other means":

- **The front-door criterion**, also Pearl ([1995](https://doi.org/10.1093/biomet/82.4.669); [2009](https://bayes.cs.ucla.edu/BOOK-2K/) §3.3.2). When there is an unblockable backdoor path from T to Y but a fully-mediated chain `T → M → Y` whose intermediate `M` is unconfounded with Y given T, the effect is identified through `M`. The cleanest example in Pearl's exposition is smoking → tar in lungs → lung cancer, where the front-door path through "tar" identifies the smoking → cancer effect even when genetic predisposition is an unmeasured confounder.
- **Instrumental variables**, an econometric tradition older than the graphical framework but expressible in it. When a variable `I` affects T but reaches Y only through T (and no backdoor paths connect `I` to Y), `I` identifies the T → Y effect under additional structural assumptions. Imbens 2014 gives the modern treatment ([Imbens, 2014](https://doi.org/10.1257/jep.28.3.49)).
- **The full identification algorithm** of Shpitser and Pearl ([Shpitser & Pearl, 2008](https://www.jmlr.org/papers/v9/shpitser08a.html), JMLR). For any causal query and any DAG, there is a complete polynomial-time algorithm — the ID algorithm — that determines whether the effect is identifiable and produces an expression for it if so. Shpitser-VanderWeele-Robins 2010 ([arxiv 1203.3515](https://arxiv.org/abs/1203.3515), UAI '10) gives the *Generalized Adjustment Criterion* (GAC), a graphical condition that is *necessary and sufficient* for identification by covariate adjustment. The backdoor criterion is a special case.

This is not a complaint about the criterion. It is a calibration. The backdoor criterion is the criterion you use in practice on most engineering DAGs — its conditions are interpretable, its procedure is mechanical, its failure modes are diagnostic. The GAC and the ID algorithm are the criterion you reach for when the backdoor criterion fails *and you want to know whether identification is still possible*.

The chapter you are reading is part one of the criterion. Chapter 10 deals with two harder questions: what is the *minimal* Z satisfying the criterion, and what do you do when *no* Z satisfies it? It is in the second question that GAC and front-door enter as candidate next moves.

**Common misconception:** "If the backdoor criterion fails, the effect is unidentifiable." False. The backdoor criterion's failure means *adjustment via backdoor-style covariate selection has failed*. The effect may still be identifiable by front-door, by instrumental variables, by mediation analysis, or by the full ID algorithm. The criterion is the first tool. It is not the last.

I want to be honest about this, because the relief framing risks oversell. The criterion is a unification, not a totality. You now have a rule. You do not yet have *the* rule for every situation. That work is the rest of the book.

---

## 8. Worked example — The pricing pipeline, end to end

The pricing DAG in §4 was a clean introduction. Let me extend it to a case closer to what an engineering team would actually meet, and walk the criterion end-to-end with the messy parts included.

**Scenario.** The pricing team's planned 5% increase is for a subscription product in three regional markets. The historical data is observational (the algorithm sets the prices). The team wants to estimate the causal effect of a price increase on monthly revenue per customer.

**Variables.**

- `P`: price (treatment).
- `R`: monthly revenue per customer (outcome).
- `T`: time-of-month indicator (early-month customers have different purchase patterns).
- `G`: regional market (three categories).
- `C`: customer tenure segment (new, mid, long-term).
- `Q`: query-volume signal (a leading indicator of latent demand, partially captured by marketing data).
- `M`: marketing spend in the week before the observation (campaigns can shift both pricing decisions and customer behavior).
- `U`: residual latent demand state (the part of demand `Q` and `M` do not capture).

**The team's DAG after a careful conversation between the pricing scientist, the demand-modeling lead, and the marketing analytics lead:**

- `T → P`, `T → R` (time-of-month affects both pricing rules and customer patterns).
- `G → P`, `G → R` (regional pricing tier; regional baseline revenue).
- `C → P`, `C → R` (tenure segment affects both algorithmic price and revenue baseline).
- `Q → P`, `Q → R` (query volume drives algorithmic price adjustments and reflects underlying willingness to pay).
- `M → P` (marketing-driven traffic shifts cause the algorithm to adjust prices upward).
- `M → R` (marketing also shifts customer willingness to pay, directly).
- `U → P`, `U → R` (residual demand state — unmeasured).
- `P → R` (the causal effect we want).

**Step 1: enumerate backdoor paths.**

Each variable with an arrow into P contributes at least one backdoor path. The variables with arrows into P are: T, G, C, Q, M, U. Each is also a parent of R or has a path to R, so each generates a backdoor path:

- `P ← T → R`
- `P ← G → R`
- `P ← C → R`
- `P ← Q → R`
- `P ← M → R`
- `P ← U → R`

Six backdoor paths. One causal path (`P → R`).

**Step 2: classify variables on each path.**

All six paths are two-edge paths with a single intermediate variable that is a fork (`P ← X → R`). Every intermediate variable is a non-collider.

**Step 3: candidate Z.**

The natural choice: `Z = {T, G, C, Q, M}`. The five measured non-colliders, each blocking its own backdoor path.

**Step 4: verify.**

- `P ← T → R`: T is a non-collider in Z. **Blocked.**
- `P ← G → R`: G is a non-collider in Z. **Blocked.**
- `P ← C → R`: C is a non-collider in Z. **Blocked.**
- `P ← Q → R`: Q is a non-collider in Z. **Blocked.**
- `P ← M → R`: M is a non-collider in Z. **Blocked.**
- `P ← U → R`: U is a non-collider *not* in Z. **Open.**

Five out of six. The team has measured every visible backdoor variable. The path through U is the one path the data cannot close.

**Step 5: second condition.** None of T, G, C, Q, M is a descendant of P. (Check: P has only the outgoing edge to R. None of the five candidate Z-members is downstream of P in this DAG.) Second condition: satisfied.

**Step 6: what the team has.**

Under the DAG as drawn, `Z = {T, G, C, Q, M}` identifies the causal effect of P on R via adjustment *up to the contribution of `U`*. The estimate is unbiased if and only if either (a) U does not exist (the team's DAG has captured the structure completely), or (b) U exists but is conditionally independent of P given Z, or independent of R given P and Z, or both.

**Step 7: what the team should do next.**

Three honest actions:

1. **Defend the DAG.** Have a domain expert challenge the absence of an edge. Is there a confounder the team has not named? A path the DAG misses? This is the same conversation Chapter 5 ended with, and it does not go away.
2. **Quantify the U-risk.** Compute an E-value (Chapter 14) for the planned price-increase decision. State the minimum strength of confounding by U that would be required to overturn the conclusion. If the E-value is small, the conclusion is fragile. If it is large, the conclusion is robust to plausible U-strengths.
3. **Plan the experiment that resolves it.** If U-risk matters, the team can plan a randomized price test in one region. Randomization closes *all* backdoor paths, including the U-path. The criterion's value here is diagnostic: it tells the team exactly which question the experiment needs to answer.

**The lesson.** The procedure does not promise to identify every effect. It promises to state precisely what is identified and what is not. The team that ran the procedure has a *cleaner* artifact than the team that did not — they know which backdoor paths are closed, which remain open, and what they would need to do next. That is the engineering value of the criterion.

The DAG itself — that they had to draw. The criterion did not draw it. Domain experts drew it. The pricing scientist who knew that the algorithm uses query volume drew the `Q → P` edge. The demand-modeling lead who knew the campaigns shift customer behavior drew the `M → R` edge. The criterion processed their commitments into a verdict. Without their commitments, the criterion would have had nothing to process.

I will state this directly because it matters and the chapter cannot afford to lose it: *the criterion is mechanical the moment the DAG is fixed. Fixing the DAG is not mechanical. That is where this book lives.*

---

## 9. Chapter summary

What you can do at the end of this chapter that you could not do at the start:

- **State the backdoor criterion's first condition** in one sentence: Z is a valid adjustment set if every backdoor path from T to Y is blocked by Z.
- **Trace every backdoor path** on a 5–7 node DAG using the procedure in §4. Identify which paths are causal (out of T at T's end) and which are backdoor (into T at T's end).
- **Verify a candidate Z** against the first condition: for each backdoor path, check whether at least one non-collider is in Z, OR whether a collider on the path has no descendant in Z.
- **Recognize when the criterion is partially satisfied** — every visible backdoor path closed, one path through an unmeasured variable open — and articulate the limit honestly rather than pretending the adjustment is complete.
- **See the integration**: confounders are forks/chains on backdoor paths (block by non-collider conditioning); mediators are on causal paths (not on backdoor paths, so the first condition is silent about them); colliders are on backdoor paths in a way that conditioning would *open* (so the first condition implicitly tells you not to add them).
- **Hold an honest calibration**: the backdoor criterion is sufficient but not necessary. When it fails, the front-door criterion, instrumental variables, and the Shpitser-Pearl ID algorithm may still identify the effect. The criterion is the first tool; not the last.
- **Run the criterion in software**: DAGitty, pgmpy, and DoWhy implement the procedure. The software is fast. The DAG it takes as input is still your work, and a wrong DAG produces a confidently wrong adjustment set.

You can write the rule down now. The rule was always there in the moves you were making. Now the rule is named, the procedure is mechanical, and the case where the procedure cannot give you a clean answer is exactly the case Chapter 14 will quantify.

---

## 10. Bridge to Chapter 10

You finished §8 with a Z of five variables. A reader who has been paying close attention is asking two questions.

First: *Is the five-variable Z the smallest Z that satisfies the criterion?* Maybe four variables would do. Maybe three. The criterion does not, in its statement, prefer minimal sets — but every additional variable in Z costs variance in the estimate, costs interpretability, and risks accidentally including a collider or a descendant of T. The literature on *minimal valid adjustment sets* answers this question precisely. Polynomial-time algorithms (van der Zander, Liśkiewicz, & Textor 2014) compute the minimal-set candidates from the DAG. Chapter 10 walks the algorithms and the trade-offs.

Second: *What happens when no Z satisfies the criterion?* In our pricing example, the U-path remained open. We named it honestly and pointed to the E-value. But there are cases where no observational adjustment can work — the structure of unmeasured confounding is fundamentally adversarial. Chapter 10 deals with the diagnostic question: when do you stop, declare the effect unidentifiable from this DAG and this data, and either expand the data, expand the DAG, or shift to a different identification strategy (front-door, instruments, mediation formula)? Knowing when to stop is its own engineering skill.

Chapter 10 also gives the second condition of the backdoor criterion its full unpacking. We mentioned the second condition in §3 and §4 — Z contains no descendants of T — and we used it implicitly to exclude mediators from adjustment sets. The condition deserves its own treatment, because the failure mode it prevents is one of the most expensive: *including a post-treatment variable in Z* is, in production ML, the most common identification mistake an engineering team makes.

Chapter 10 is the criterion's other half. Together, Chapter 9 and Chapter 10 give you the full backdoor framework. Chapter 11 begins the toolkit for the cases where backdoor adjustment cannot close the gap — instrumental variables, front-door, mediation. The chapters compose. The procedure you learned today is the rule that everything else either extends or replaces.

---

## Exercises

**Warm-up.**

1. **(Apply)** Given the DAG with edges `Z1 → T`, `Z1 → Y`, `Z2 → T`, `Z2 → Y`, `T → M`, `M → Y`, list every backdoor path from `T` to `Y`. For each, identify the intermediate variable's role (fork, chain, collider).

2. **(Apply)** Using the same DAG, propose one valid adjustment set Z that satisfies the criterion's first condition. State which backdoor paths your Z blocks. State explicitly that your Z contains no descendants of T (the second condition, which we will deepen in Chapter 10).

**Application (Part A).**

3. **(Apply)** Apply the path-tracing procedure from §4 to the following six-node DAG. Edges: `A → T`, `B → T`, `A → Y`, `B → Y`, `T → M`, `M → Y`, `A → B`. Trace every path from T to Y. Classify each. For each backdoor path, name the intermediate variables and their roles. Propose two distinct valid adjustment sets and verify each against the first condition. State which set you would prefer and why.

**Application (Part B — own domain).**

4. **(Analyze)** Take the candidate DAG you drew for your own treatment-outcome problem in Chapter 5's Part B exercise (or, if you skipped it, draw one now for a treatment-outcome pair from your current role). Run the path-tracing procedure end-to-end. List every backdoor path. State your current adjustment set. Apply the criterion's first condition. State which backdoor paths are blocked, which are open, and what you would need to do (measure a new variable, run an experiment, accept the limit) to close the open ones. This artifact extends your Defend-Your-DAG portfolio.

**Synthesis.**

5. **(Analyze)** Chapter 4 named three identification failure types: wrong variables, wrong functional form, wrong conditioning. Map each failure type to a specific way the backdoor criterion can fail. *Wrong variables* corresponds to which step of the path-tracing procedure? *Wrong conditioning* corresponds to which? *Wrong functional form* — does the criterion catch this, or is it silent about it? (Hint: the criterion is a graphical criterion. It does not specify how variables in Z enter the regression.) Write one paragraph per failure type.

**Challenge.**

6. **(Evaluate)** Find a published causal claim from a recent ML or applied-statistics paper — *NeurIPS*, *ICML*, *JMLR*, or an applied econometrics venue. Draw the implied DAG from the authors' description of their adjustment strategy. Apply the path-tracing procedure. State whether the authors' adjustment set satisfies the criterion's first condition. If yes, state any backdoor paths the authors did not name explicitly that their adjustment still closes. If no, state which path is open and what an audit reviewer would ask. Cite the paper.

---

## LLM exercise

Open Claude, ChatGPT, or Gemini. Paste this prompt exactly.

```
I have a directed acyclic graph for a causal analysis. The DAG has the
following variables and edges:

Variables: T (treatment), Y (outcome), and five other variables labeled
A, B, C, D, E.

Edges:
- A → T
- A → Y
- B → T
- B → C
- C → Y
- D → A
- D → Y
- T → E
- E → Y

I want to estimate the causal effect of T on Y.

Please give me:
(1) A list of every backdoor path from T to Y. For each, identify which
    variable is the intermediate and its role (fork, chain, or collider).
(2) A valid adjustment set Z that blocks every backdoor path under
    Pearl's backdoor criterion's first condition.
(3) For each variable NOT in your Z, state explicitly why you excluded
    it (e.g., "E is a descendant of T," "C is on the causal path").

Be specific about whether your Z is minimal, and identify any other
adjustment sets that would also satisfy the criterion.
```

Now critique what you get back.

Run the path-tracing procedure on the DAG yourself before reading the LLM's answer. (The DAG has at least three backdoor paths and at least one collider on a path; this is not a trivial case.) Then compare.

- Did the LLM enumerate every backdoor path, or did it miss some?
- Did the LLM correctly classify each intermediate as fork, chain, or collider? Pay attention to any variable that sits as a collider on one path and a non-collider on another.
- Did the LLM correctly exclude E (a descendant of T, violating the second condition)?
- Did the LLM hallucinate edges or paths that are not in the spec? Did it add a constraint you did not give it?

Write a one-paragraph note on where the LLM was useful (probably: rapid enumeration, prose explanation of the criterion) and where it was not (probably: collider-on-multiple-paths cases, minimality claims, anything requiring careful inspection of the DAG's actual edges rather than its plausible structure). Save the note for your portfolio.

---

## AI Use Disclosure (Part A standard form)

Per the course's AI Use Disclosure standard:

1. Name the LLM(s) used and the date of each session.
2. State which exercises you used an LLM for and what you used it for in each.
3. For each LLM-generated claim that survived into your final submission, state the source you used to verify it.
4. For each LLM-generated claim that did not survive, state briefly why you removed it.

**Part B bonus criterion:** Submissions that apply the backdoor criterion to a DAG drawn for the student's own work *and* honestly state which backdoor paths remain open after the candidate adjustment receive Part B credit. The artifact must (a) include the DAG, (b) enumerate every backdoor path, (c) state the proposed Z, (d) name the paths Z blocks and the paths Z leaves open (if any), and (e) propose at least one concrete next step (new measurement, experiment, sensitivity analysis) for the open paths.

---

## Key terms

- **Backdoor path** — any path from T to Y whose first edge at the T end is an arrow *into* T. Backdoor paths are the routes through which non-causal association can flow between T and Y.
- **Backdoor criterion (first condition)** — a set Z is a valid adjustment set for the effect of T on Y if every backdoor path from T to Y is blocked by Z. Pearl 1995, 2009 §3.3.
- **Backdoor criterion (second condition)** — Z contains no descendants of T. Treated briefly in this chapter; deepened in Chapter 10.
- **Blocked path** — a path along which conditional association does not flow, given the conditioning set Z. Achieved by conditioning on a non-collider, or by leaving a collider (and its descendants) un-conditioned.
- **Adjustment formula** — `P(Y | do(T = t)) = Σ_z P(Y | T = t, Z = z) P(Z = z)`. Identifies the interventional distribution from observational data when Z satisfies the backdoor criterion.
- **Path-tracing** — the procedure (steps 1–7 of §4) of enumerating paths from T to Y, classifying each as causal or backdoor, identifying variable roles, and verifying whether a candidate Z blocks every backdoor path.
- **Sufficient but not necessary** — the backdoor criterion identifies a class of valid adjustment sets, but its failure does not imply the effect is unidentifiable. Front-door, instrumental variables, mediation formula, and the Shpitser-Pearl ID algorithm cover other cases.
- **Generalized Adjustment Criterion (GAC)** — Shpitser, VanderWeele, & Robins 2010 ([arxiv 1203.3515](https://arxiv.org/abs/1203.3515)). A graphical condition for valid adjustment that is *necessary and sufficient*. The backdoor criterion is a special case.

---

## Further reading

1. **Pearl, J. (1995).** "Causal diagrams for empirical research." *Biometrika* 82(4), 669–688. [https://doi.org/10.1093/biomet/82.4.669](https://doi.org/10.1093/biomet/82.4.669). The earliest published formal statement of the backdoor criterion. Read for the original framing and the historical context of where the graphical approach came from.

2. **Pearl, J. (2009).** *Causality: Models, Reasoning, and Inference*, 2nd ed., §3.3 ("The Back-Door Criterion"). Cambridge University Press. The definitive technical reference, including the adjustment formula derivation and the comparison with the front-door criterion. (Note: §3.3 is paywalled in the book; older versions of the chapter circulate as Pearl's UCLA technical reports, [bayes.cs.ucla.edu](https://bayes.cs.ucla.edu/csl_papers.html).)

3. **Shpitser, I., VanderWeele, T. J., & Robins, J. M. (2010).** "On the validity of covariate adjustment for estimating causal effects." *Proceedings of UAI '10*. [arxiv.org/abs/1203.3515](https://arxiv.org/abs/1203.3515). The Generalized Adjustment Criterion — the necessary-and-sufficient condition that the backdoor criterion is a special case of. Read after Chapter 10 for the full picture.

4. **Shpitser, I., & Pearl, J. (2008).** "Complete identification methods for the causal hierarchy." *Journal of Machine Learning Research* 9, 1941–1979. [https://www.jmlr.org/papers/v9/shpitser08a.html](https://www.jmlr.org/papers/v9/shpitser08a.html). The ID algorithm: a complete procedure for determining whether any causal effect is identifiable from observational data, for any DAG. The backdoor criterion is one case the algorithm handles.

5. **van der Zander, B., Liśkiewicz, M., & Textor, J. (2014).** "Constructing Separators and Adjustment Sets in Ancestral Graphs." *Proceedings of UAI '14*. [event.cwi.nl/uai2014/papers/63.pdf](https://event.cwi.nl/uai2014/papers/63.pdf). Polynomial-time algorithms for finding minimal valid adjustment sets given a DAG. Underpins DAGitty's adjustment-set discovery.

6. **Textor, J., van der Zander, B., Gilthorpe, M. S., Liśkiewicz, M., & Ellison, G. T. H. (2016).** "Robust causal inference using directed acyclic graphs: the R package 'dagitty'." *International Journal of Epidemiology* 45(6), 1887–1894. [https://doi.org/10.1093/ije/dyw341](https://doi.org/10.1093/ije/dyw341). The DAGitty paper. The browser-based tool ([dagitty.net](https://www.dagitty.net/)) implements the path-tracing procedure and adjustment-set search. Engineering reader's first stop for running the criterion on their own DAGs.

7. **Hernán, M. A., & Robins, J. M. (2020).** *Causal Inference: What If*, Chapter 7. [Free PDF](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/). The epidemiology contemporary treatment of backdoor adjustment. Complementary to Pearl's graph-first framing; useful for the potential-outcomes equivalence.

8. **Sharma, A., & Kiciman, E. (2020).** "DoWhy: An End-to-End Library for Causal Inference." [arxiv.org/abs/2011.04216](https://arxiv.org/abs/2011.04216). The DoWhy library implements backdoor identification, frontdoor identification, and instrumental-variables identification end-to-end. Engineering reader's Python toolchain.

---

## Draft flags

- `[verify-Pearl-1995-DOI]` — The DOI `10.1093/biomet/82.4.669` was supplied in the chapter brief and matches the canonical Biometrika reference for Pearl 1995. The URL resolves through DOI.org. If a hostile reviewer challenges, the JSTOR fallback is [https://www.jstor.org/stable/2337329](https://www.jstor.org/stable/2337329) (may require verification on access).
- `[verify-van-der-Zander-URL]` — The UAI '14 paper URL `event.cwi.nl/uai2014/papers/63.pdf` is from the pantry research notes. If unstable, an alternative is the authors' homepages or a Semantic Scholar mirror.
- `[verify-DoWhy-DAGitty-pgmpy-claims]` — The chapter states that DAGitty, pgmpy, and DoWhy each implement the backdoor procedure. DAGitty is verified by the Textor 2016 paper. DoWhy is verified by the Sharma & Kiciman 2020 paper. pgmpy's backdoor support is documented in the project's docs at [pgmpy.org](https://pgmpy.org/) — a direct doc URL would tighten the claim; left as the project homepage here.
- `voice-anchored: partial` — Root `style/VOICE.md` is the fry-voice spec; this chapter is written in the feynman default voice, matching Chapters 1–8. No per-book style folder exists for `causal-reasoning`. The chapter relied on §6 of CLAUDE.md and the explicit feynman-voice directive in the brief.

---

**What would change my mind:** If a careful reading of Shpitser-VanderWeele-Robins 2010 alongside applied case studies showed that the GAC routinely identifies effects the backdoor criterion misses *on engineering-domain DAGs at the level of detail engineers actually draw*, I would change the chapter's framing from "the backdoor criterion is the formal tool you have been approximating" to "the backdoor criterion is one of several formal tools you might reach for, and on engineering DAGs the choice of which tool matters." My current reading is that on the DAGs engineering teams actually draw — moderately sized, with a small number of identified confounders and one or two unmeasured ones — the backdoor criterion is the practical default and GAC's marginal value is mostly in pathological cases. I hold this reading lightly.

**Still puzzling:** I do not yet fully understand how to teach the difference between a DAG that is *wrong about an edge* (one arrow misdrawn) versus a DAG that is *wrong about a variable* (a variable missing entirely) in a way that gives the student the right diagnostic instincts for each. The first failure mode produces a procedure output that is locally plausible and globally biased. The second produces a procedure output that looks complete and silently leaves a backdoor path open. The two failures call for different next moves — the first wants a DAG audit by a domain expert; the second wants a sensitivity analysis. The chapter handles both implicitly but does not teach the distinction explicitly. Chapter 10 may be where this gets named.

---

**Tags:** backdoor-criterion, path-tracing, adjustment-set, Pearl-1995, identification-procedure
