# The Map Before the Territory


## TL;DR

- TL;DR: A causal model lives in three places at once — a picture, a probability factorization, and a sentence — and they say the same thing in three accents.
- The chapter moves through What an arrow says — and what a missing arrow says louder, Mid-chapter checkpoint, The probability table as a conditional-independence machine, Let me show you the calculation, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. The Map Before the Territory
2. Three Languages for One Object
3. Every Arrow Is a Claim

**TL;DR:** A causal model lives in three places at once — a picture, a probability factorization, and a sentence — and they say the same thing in three accents. The whole chapter is one long demonstration that whichever rendering you started with, you have already done the part the data could not have done for you.

**Byline:** Nik Bear Brown

**Prerequisites:**
- You can read `P(Y | X, Z)` and know what changes when the conditioning set changes.
- You have factored a joint distribution at least once, even if you called it a "Bayes net."
- You finished Chapter 2 and accept that the word you reach for is a commitment, not a label.
- You can write Python that calls a causal-inference library (`dowhy`, `causal-learn`, `pgmpy`, or equivalent). You do not have to remember the API; you have to remember that you have used one.
- You have seen the rungs of Pearl's ladder named once. We will name them again here when they do work.

**Learning objectives:**
- (Understand) Recognize that a directed acyclic graph, a factored probability table, and a prose causal claim are three representations of one object.
- (Apply) Translate a prose causal claim into a set of directed edges, and label what you committed to by which edges you did *not* draw.
- (Analyze) Identify which entries in a probability table required domain knowledge the data could not supply.
- (Evaluate) Assess a candidate causal diagram by marking edges well-supported, uncertain, or missing-but-suspicious.
- (Analyze) Distinguish a directed edge from an undirected one, and name the domain knowledge that would orient an undirected edge.

---

Open three notebooks on your desk. Look at them in this order.

**Notebook 1 — a picture.**

```
        C
       / \
      v   v
      T   |
      |\  |
      | \ |
      v  vv
      M   Y
      \   ^
       \  |
        v |
        Y (already there — M points into it)
```

Cleaned up, the picture is four boxes with five arrows:

```
        C ────────┐
        │         │
        v         v
        T ──> M ──> Y
        │           ^
        └───────────┘
```

`C → T`, `C → Y`, `T → M`, `M → Y`, `T → Y`. Four nodes. Five arrows. No arrows pointing backward anywhere; if you tried to walk in the direction of the arrows you would never come back to where you started.

**Notebook 2 — a product.**

`P(C, T, M, Y) = P(C) · P(T | C) · P(M | T) · P(Y | C, T, M)`

Four factors, multiplied together. Each factor names a variable on the left of the bar and a (possibly empty) set of variables on the right. The four-variable joint distribution is written as a product of four pieces, and each piece looks like a small conditional probability you might be able to estimate from data if you had data.

**Notebook 3 — a sentence.**

> *C influences both T and Y. T affects Y directly and also through M. M is a downstream consequence of T and has no effect of its own on anything outside Y.*

That is the whole sentence. Three notebooks. One object.

I want you to sit with the three for a minute before I name anything. Pretend you have never heard the term *directed acyclic graph*. Pretend you have not seen a factorization written that way before. Pretend the sentence is a sentence and the picture is a picture and the math is the math. Read each one. Then read the next. Then read the third. Notice what each makes easy to see and what each makes hard to see.

The picture makes the shape easy. You can see at a glance that `C` is upstream of everything, that `M` sits between `T` and `Y`, that `Y` has three things pointing at it. The shape is visible in your peripheral vision; you do not have to read it left-to-right.

The product makes the *counting* easy. There are four conditional distributions, exactly four, and each one says which variable depends on which others. If you tried to estimate the full joint by counting in a table, you would need a cell for every combination of values of `C`, `T`, `M`, `Y`. With four binary variables that is sixteen cells. The factorization lets you get away with `2 + 4 + 4 + 8 = 18` cells in the worst case, which is worse here because the variables are tiny, but with twenty variables it is the difference between `2^20` cells and a few hundred. The product is what makes the table fit on the page.

The sentence makes the *commitment* easy. When you read "T affects Y directly and also through M," you can argue with it. You can imagine showing it to a colleague who says *I don't think T affects Y directly — I think it only acts through M*. That argument is a real argument. You can imagine evidence that would settle it. You cannot have that argument with the picture or the product as easily, because they look like math, and math feels like it is not the kind of thing you argue with.

The picture and the product and the sentence are not three different things. They are one thing, looked at through three windows. The whole chapter is about looking through those windows and noticing that whichever one you started at, you have already committed to claims the data could not have given you.

Here is the trick, before we begin: every arrow in that picture is a sentence. Every factor in that product is the same sentence in a different accent. And every claim in the prose specifies an arrow somewhere. If they ever disagree, exactly one of them is wrong, and you have a problem worth finding.

---

## 1. What an arrow says — and what a missing arrow says louder

Let me show you why the directed edge is harder than it looks.

A directed edge `X → Y` says one specific thing: *in the population of cases this model describes, intervening on `X` changes the distribution of `Y`, holding the other modeled variables fixed.* That is what the arrow means. It does not mean `X` and `Y` are correlated. It does not mean `X` happens before `Y` in time, although usually it does. It does not mean changing `X` always changes `Y`; it means an intervention on `X` would change the distribution of `Y`, on average, given the other variables in the model.

Now I have used the word "intervening" without defining it. Intervening means *reaching in and setting the value of `X` from outside the system, ignoring whatever the system would have done on its own*. If `X` is "temperature" and `Y` is "ice-cream sales," then setting `X` to 95°F by intervention means *we made it 95°F somehow, by magic or by air conditioning failure, not because of anything else in the model*. The arrow `X → Y` says that if you did that intervention, sales would respond.

This is Pearl's Rung 2 from Chapter 1 — the rung the data alone cannot reach. We are about to draw a diagram entirely in Rung 2 vocabulary.

A directed edge is a *positive commitment*. You drew it. You will be asked to defend it.

The missing edge — the arrow you did *not* draw between two variables — is also a commitment, and a louder one. It says *in this model, the variable on the left has no direct causal influence on the variable on the right, given the other modeled variables.* "Direct" relative to the variables you put in the model. If you added a new mediating variable later and the influence ran entirely through it, the missing edge would become consistent with the data again. But for now, in the model as drawn, you have committed to *no direct effect*.

Here is what is easy to miss. A complete-graph diagram, with arrows from everything to everything else, makes almost no commitment. It is consistent with almost any data the world could throw at you. The fewer arrows you draw — the more *missing* arrows your diagram has — the stronger and more falsifiable your claim. The diagram earns its keep through what it leaves out.

Try this with the picture above. The diagram has five arrows and could have had `4 × 3 = 12` possible directed edges (with no self-loops). Seven possible arrows are missing. Each of those seven is a claim. Let me write three of them:

1. **No `M → C`.** Whatever `M` is, the model says it does not feed back into `C`. If `C` is "ambient population health" and `M` is "diagnostic test result," the model is asserting that the test result does not change the population's health. Plausible. But it is asserted, not free.
2. **No `Y → T`.** The outcome does not cause the treatment. If `T` is *prescribing a drug* and `Y` is *recovery*, this is the no-reverse-causation assumption. Plausible if the prescription happened first in time. Falsifiable, in principle, by an experiment that varied `Y` and looked for movement in `T`.
3. **No `Y → C`.** The outcome does not influence the upstream confounder. If `C` is "patient age," this is on solid ground because nobody's age responds to whether they recovered. If `C` is "physician's reputation," this becomes shakier — outcomes affect reputations — and we should worry.

The missing arrows are *also* edges; they are the negative space of the picture, and the negative space is where the strong claims live.

I learned this slowly. The first time I drew one of these graphs I drew everything I could justify and felt clever about how much I had specified. The instructor circled the *missing* edges in red and said, "what about those." I had not thought of them as anything. They were nothing. I had drawn a diagram with five arrows and considered the diagram done. The seven missing arrows were seven claims I had made without noticing.

You will do this too. Every reader of every causal diagram does this the first time. The discipline I want you to start practicing now is: for any diagram you take seriously, *list the missing edges that could plausibly have been there, and decide whether you believe the assertion that they are absent.*

This is the bookkeeping move that separates a causal diagram from a doodle. A doodle says "these things are related." A causal diagram says "these things are related *like this, and not like the seventy other ways they could have been.*"

### Mid-chapter checkpoint

Before we move on, sit with the picture from the opening for a minute and answer these to yourself.

1. The edge `T → Y` is drawn. What does it say, in plain English, about what would happen if we intervened on `T`?
2. There is no edge from `M` to `C`. Write the sentence that missing edge commits us to.
3. There is no edge from `C` to `M`. What domain claim is the diagram making, given that `C` does influence `T` and `T` does influence `M`?

If you said about (3) that the diagram is committing to *`C` affects `M` only through `T`, not directly* — yes. That is the chain `C → T → M`, and the missing `C → M` arrow says the chain is the only route. If you find that doubtful — if you can think of a way `C` could affect `M` not through `T` — your candidate diagram needs another arrow, and you have just earned the right to add one by knowing why.

---

## 2. The probability table as a conditional-independence machine

Now turn to the second notebook — the product.

`P(C, T, M, Y) = P(C) · P(T | C) · P(M | T) · P(Y | C, T, M)`

I want to teach you to read this product the way a musician reads a chord. It is not just a thing you compute with. It is a *compressed statement of every conditional independence the diagram implies.* If you can read the product, you can read off, without ever drawing the graph, which variables become independent of which other variables when you condition on which other variables.

Here is the rule that makes the product mean what it means. It is called the **Markov property** of the graph, and it says:

> *Each variable is independent of all its non-descendants, given its parents.*

Three words to define. **Parents** of a variable, in a directed graph, are the variables that have arrows pointing directly into it. The parents of `Y` in our diagram are `C`, `T`, and `M` — three arrows point in. The parents of `M` are just `T`. The parents of `T` are just `C`. The parents of `C` are nothing — `C` is at the top.

**Descendants** of a variable are everything you can reach by following arrows out of it. Descendants of `T` are `M` and `Y`. Descendants of `M` are just `Y`. Descendants of `C` are everyone else: `T`, `M`, `Y`. Descendants of `Y` are nothing.

**Non-descendants** are the rest — what isn't a descendant, and isn't the variable itself. The non-descendants of `M` are `C` and `T`.

The Markov property says: `M` is independent of all its non-descendants, given its parents. The non-descendants of `M` are `C` and `T`. The parents of `M` are `T`. So:

> `M ⊥⊥ C | T`

Read aloud: "`M` is independent of `C` given `T`." Knowing `T` is enough; once you know `T`, `C` tells you nothing more about `M`. This is a *prediction the diagram is making about the data.*

Let me show you that the prediction has bite. Suppose you go to the data, you compute `P(M | T, C)` for every combination, and you find that fixing `T = 1` and varying `C` from 0 to 1 changes the distribution of `M`. The diagram is wrong. Either there is a direct edge `C → M` that you missed, or there is some other path from `C` to `M` not going through `T`, or the variables aren't what you said they were. The diagram made a falsifiable prediction. The data falsified it.

This is the move you should keep in your pocket. The factorization is not just bookkeeping; it is the diagram's testable consequences written in a form you can put in a script.

### Let me show you the calculation

Take a smaller diagram so I can run all the algebra on the page. Three nodes only:

```
    X ──> Y ──> Z
```

A chain. `X` causes `Y`, `Y` causes `Z`. No other arrows. The factorization is:

`P(X, Y, Z) = P(X) · P(Y | X) · P(Z | Y)`

The Markov property says `Z` is independent of all its non-descendants given its parents. The non-descendants of `Z` are `X` and `Y` (no descendants of `Z`, no node is its own non-descendant). The parents of `Z` are just `Y`. So:

> `Z ⊥⊥ X | Y`

Watch what happens when we verify this with the factorization. By definition, `Z ⊥⊥ X | Y` means `P(Z | X, Y) = P(Z | Y)` — once we know `Y`, knowing `X` doesn't change anything about `Z`.

`P(Z | X, Y) = P(X, Y, Z) / P(X, Y)`

Using the factorization for the numerator:

`P(Z | X, Y) = [P(X) · P(Y | X) · P(Z | Y)] / P(X, Y)`

And `P(X, Y) = P(X) · P(Y | X)`, by the same factorization (just summing out `Z`, but the result here drops out by the same product rule). So:

`P(Z | X, Y) = [P(X) · P(Y | X) · P(Z | Y)] / [P(X) · P(Y | X)] = P(Z | Y)`

The `P(X) · P(Y | X)` cancels. We are left with `P(Z | Y)`, which is what `Z ⊥⊥ X | Y` requires. The conditional independence drops out of the factorization mechanically.

I want to flag what is beautiful here and what is ugly.

The beautiful part: a *geometric* property of the graph — `Z` is not adjacent to `X`, and the path from `X` to `Z` passes through `Y` — becomes an *algebraic* property of the factorization — a term cancels — becomes a *statistical* property of the data — a conditional probability simplifies. Three languages, one fact. The diagram tells you the algebra and the algebra tells you what to check in the data.

The ugly part: the cancellation only works because we chose the right form of the factorization, the one consistent with the diagram. If we wrote `P(X, Y, Z) = P(X) · P(Y | X, Z) · P(Z | Y)` — also a valid product, but it factors according to a *different* diagram where `Z` would have an arrow to `Y` — the cancellation would not happen and we would conclude `Z` and `X` are not independent given `Y`. The factorization is the diagram. They cannot disagree, because they are the same statement.

This is the part that took me longest to internalize. The factorization is not a calculation you do *after* picking a diagram. The factorization *is* the diagram. Choosing one is choosing the other.

### Which entries required domain knowledge

Look back at our four-variable factorization:

`P(C, T, M, Y) = P(C) · P(T | C) · P(M | T) · P(Y | C, T, M)`

There are two distinct kinds of choice baked in. Distinguishing them is the chapter's most important pedagogical move.

The *structure* of the factorization — which conditionals appear, with which variables on the right of which bars — comes from the diagram. Which comes from your judgment. The factorization has `P(M | T)` rather than `P(M | T, C)` because the diagram has no `C → M` edge. That decision was yours.

The *parameters* — the actual numbers inside `P(M | T)`, the probability of `M = 1` given `T = 0` versus given `T = 1` — those come from data, if the structure is right. Count cases. Compute proportions. The estimator is mechanical once the structure is fixed.

Both have to be right, and they fail in different ways. A correctly estimated parameter inside a wrong structural factorization is wrong in a way that no amount of data fixes — you are estimating the right number for the wrong question. A correct structure with badly estimated parameters is wrong in a way that more data does fix.

The data can give you the second. It cannot give you the first. The first is the move you supplied.

That is the identification layer, although we will not call it that yet. The next chapter does.

---

## 3. Undirected edges as honest uncertainty

Here is where things get hard, and where the chapter's most important load-bearing fact lives.

Consider three variables again: `X`, `Y`, `Z`. Suppose you go to your data — a big sample, well-collected — and you do every conditional-independence test you can think of. You find one and only one independence:

> `X ⊥⊥ Z | Y`

Knowing `Y` makes `X` and `Z` independent. Marginally they are dependent. Conditional on `Y` they are not.

What is the causal diagram?

You write down the candidates. Diagram A: `X → Y → Z`. Diagram B: `X ← Y ← Z`, i.e., `Z → Y → X`. Diagram C: `X ← Y → Z`, with `Y` causing both. Each of these *implies* `X ⊥⊥ Z | Y` — the same conditional independence drops out of all three factorizations. (Check it. The algebra works the same way for each.)

Here is the uncomfortable result, and it is a theorem, not a hand-wave. Three diagrams. Same conditional independences. *The data cannot tell you which one is right.* Not "the data is noisy." Not "you need more samples." Not "use a better algorithm." The three diagrams imply identical distributions over the observable variables, and so identical statistical behavior under any observation you could possibly make. The information that would distinguish them is *not in the joint distribution*. They are observationally indistinguishable.

This is **Markov equivalence**, the result you most need to take from this chapter. Two directed acyclic graphs are *Markov equivalent* when they imply the same set of conditional independences over the observed variables. Verma and Pearl proved (1990) that two graphs are Markov equivalent if and only if they have the same edges, ignoring direction, and the same set of *v-structures*. We will get to v-structures in a second. The point right now is that *multiple distinct causal diagrams can fit the same data perfectly,* and observational data — Rung 1 data — does not pick between them.

The honest representation of "we have data but cannot orient the edges" is an *undirected* edge:

```
    X ── Y ── Z
```

A line, not an arrow. The line says: *`X` and `Y` are connected by some causal relationship in this model; the data establishes the connection; the data does not say which direction.* Same for `Y` and `Z`. You can write the diagram down without lying about how much you know.

There is one case where the data *does* orient. Watch what happens when the conditional independence pattern is different. Suppose instead you found:

> `X ⊥⊥ Z` (marginally — without conditioning on anything)

But:

> `X` and `Z` are *dependent* once you condition on `Y`.

This is the strange pattern of two things that are unrelated until you account for a third, at which point they become related. You only get this pattern from one of the four candidate diagrams. It comes from `X → Y ← Z` — both arrows point *into* `Y`. That is a **v-structure**, also called a **collider** at `Y` (the variable two arrows collide at).

The chain `X → Y → Z` and the fork `X ← Y → Z` both produce marginal dependence and conditional independence. The v-structure `X → Y ← Z` produces marginal independence and conditional dependence. The pattern is different, and so the v-structure is the one case where observational data orients edges. (Why? Because conditioning on a collider creates dependence between its parents — Chapter 7 territory. For now, take the fact as given.)

So *some* edges, the data can orient — the ones that form v-structures. The rest, the data cannot orient. The discovery algorithms that put this together — the PC algorithm, FCI, and their successors (Spirtes, Glymour, and Scheines, [*Causation, Prediction, and Search*](https://www.cmu.edu/dietrich/philosophy/docs/scheines/causation%2C%20prediction%2C%20and%20search.pdf), MIT Press, 2000) — return a **completed partially directed acyclic graph**, or CPDAG, with some arrows and some lines. The arrows are the ones the data oriented (via v-structures and downstream propagation). The lines are the ones the data left underdetermined.

What do you do with the lines? Two honest options.

You intervene. An experiment can break the symmetry — randomly setting `X` and watching `Y` move tells you `X → Y`; the reverse experiment tells you `Y → X`. Intervention works precisely because it puts you on a different rung than observation, and the data on that rung is the data the lines were missing.

Or you supply the orientation from domain knowledge. You say: *I know temperature affects ice-cream sales and not the other way around because temperature is set by the weather and ice-cream sales cannot warm the air.* The orientation comes from you. The diagram now has an arrow where it had a line, and the arrow is supported by *your judgment*, not the data. The diagram should still tell its reader that, somehow — by annotation, by a footnote, by a different line style. Lying about which edges the data oriented and which you oriented is the easiest mistake to make and the hardest to recover from later.

I want to flag where the field gets argumentative. There is a counter-current of techniques that claim to orient more edges than v-structures alone allow. LiNGAM (Shimizu et al., *Journal of Machine Learning Research*, [2006](https://www.jmlr.org/papers/v7/shimizu06a.html)) and additive-noise models exploit non-Gaussianity of the noise to identify directions inside Markov equivalence classes. NOTEARS (Zheng et al., NeurIPS [2018](https://arxiv.org/abs/1803.01422)) uses continuous optimization to search the DAG space. Both work. Both rest on *strong* distributional assumptions — non-Gaussianity, additive noise, model class restrictions — that the analyst supplies. The data does not magically start telling you direction. The analyst's modeling assumption tells you direction. If the assumption is right, the orientation is recovered; if the assumption is wrong, you have just dressed up your prior as a discovery.

This is not a complaint about LiNGAM or NOTEARS. It is the necessary qualification on any claim that "the algorithm discovered the causal structure." The algorithm discovered it *given* the assumptions you supplied. Without those assumptions, Markov equivalence is the ceiling.

My reading: undirected edges are not a weakness of causal discovery. They are the *correct output* under general assumptions. A tool that hands you a fully directed graph without saying which edges came from v-structures, which came from assumed-non-Gaussian-noise, and which came from a tiebreaker is concealing something the engineering reader needs to see. The honest output is the one with lines in it. Lines are humility on the page.

---

## 4. Three windows on one room — putting it together

We have spent the chapter building one diagram, one factorization, and one set of sentences. They are all the same object. Let me show you how to look at a new system through all three windows at once, and how each window pulls something out that the others hide.

The system: a small hiring pipeline. Three variables.

- `R` — résumé score (0–100), produced by a screening model from the applicant's résumé.
- `I` — interview rating (0–100), assigned by a human interviewer.
- `H` — hire decision (yes/no), made by the hiring manager after seeing both scores.

Here is a candidate prose claim, which I am putting on the page first because the engineer writing this system probably starts there.

> *The résumé score is the first signal we see. The interviewer reads the résumé before the interview, so the résumé score influences the interview rating. The hire decision is made looking at both signals.*

Now translate to a diagram. The sentence names three causal edges:

1. *"The résumé score ... influences the interview rating"* → `R → I`.
2. *"The hire decision is made looking at both signals"* → `R → H` and `I → H`.

Three arrows. Diagram:

```
    R ──> I
    │     │
    │     v
    └───> H
```

What missing edges did we just commit to?

- No `I → R`. The interview rating does not change the résumé score. Solid — the résumé score was computed and stored before the interview.
- No `H → R` and no `H → I`. The hire decision does not feed back into the earlier scores. Solid in this snapshot of one applicant. *Not* solid across applicants over time — if a model retrains on past hire decisions, future résumé scores will be influenced by the past `H` distribution, and we have introduced feedback the diagram is not capturing. The acyclicity assumption is honest for one applicant in one cycle. It would be a lie if the boundary of the model were "the whole hiring pipeline over time." Where you draw the boundary determines whether acyclicity is true.

Now the factorization. List variables in topological order (parents before children): `R, I, H`. Write `P(variable | parents)` for each:

`P(R, I, H) = P(R) · P(I | R) · P(H | R, I)`

Three factors. Each one corresponds to a node and its incoming arrows.

What does each factor require?

- `P(R)` — the marginal distribution of résumé scores in the applicant population. Estimable from a log of past applicants. The data can supply this.
- `P(I | R)` — the conditional distribution of interview ratings given résumé scores. Estimable from interview records, *if* you have them paired with the original résumé scores. Note that the factorization assumes interviewers see only the résumé score, not any other feature of the applicant. This is a domain claim. If interviewers also see the applicant's name or photograph, *and* if names or photographs influence ratings independently of résumé content, then the factor should be `P(I | R, N)` where `N` is the additional variable, and we have under-specified the model.
- `P(H | R, I)` — the conditional probability of being hired given both signals. Estimable from past hiring decisions paired with the two scores.

The data can give you the parameters. The data cannot give you the *structure of the factorization itself.* That the model includes `R, I, H` and not also `N` (name), or `D` (date of interview), or `B` (interviewer's mood) is a domain decision you made by what you put in and what you left out.

Now check the Markov property. The diagram says `H` should be independent of nothing given its parents, because `H` has no non-descendants other than `R` and `I` and those are already its parents. The diagram says `I` should be independent of its non-descendants given its parents — non-descendants of `I` are nothing (the only other nodes are its parent `R` and its descendant `H`). The diagram says `R` should be independent of its non-descendants given its parents — non-descendants are nothing again.

The diagram makes essentially no testable independence claim. With only three variables and three edges that form an arrowhead at `H`, the diagram is barely constrained — it is close to a saturated model. This is itself a finding: *a diagram with too few missing edges is making weak claims*, and the data can barely falsify it. If you wanted strong claims you would have to add more variables, see if some edges drop out, or find structure.

Add a fourth variable: `S`, the school the applicant attended. Suppose `S` influences both `R` (because the screening model uses school as a feature) and `H` (because the hiring manager directly favors certain schools). Suppose `S` does *not* influence `I`, because the interviewer is masked to school.

```
    S ──> R ──> I
    │     │     │
    │     │     v
    └─────┴────>H
```

`S → R`, `S → H`, `R → I`, `R → H`, `I → H`. No `S → I`. Factorization:

`P(S, R, I, H) = P(S) · P(R | S) · P(I | R) · P(H | S, R, I)`

The diagram now has a missing edge `S → I` that is a real commitment. The Markov property says:

> `I ⊥⊥ S | R`

Once you know the résumé score, school adds no information about the interview rating. This is a falsifiable claim. Run the test: in the data, compute `P(I | R, S)` and `P(I | R)` and see if they differ. If they do, `S → I` is missing from your diagram and you need to add it. If they don't, the diagram survives the test — not "is proven," survives the test.

The diagram is now doing work. You can see which adjustments would be needed for which questions. To estimate the causal effect of `R` on `H` you would need to handle `S` as a confounder. To estimate the effect of `I` on `H` you would need to handle both `S` and `R` as confounders. We will name the criterion that tells you which variables to adjust on in a later chapter; for now, you can see that the diagram already encodes the information.

Three windows. One room. Let me say once what each window made easy and what each one hid.

The prose made the *commitments* easy to argue with. "I assume interviewers are masked to school" is a sentence someone can disagree with.

The diagram made the *shape* easy. You could see at a glance that `S` was a fork — pointing at both `R` and `H` — and that anything trying to use `R` to predict `H` causally needed to handle `S`.

The factorization made the *testable predictions* easy. `I ⊥⊥ S | R` came right out of the product, and that is the kind of statement you can put in a script and run.

Each window is the same room. Choose the window that makes the next move easy.

---

## Chapter summary — capabilities gained

You can now do five specific things you could not do at the start of this chapter.

You can read a directed graph and write down what each present arrow claims and what each missing arrow claims, recognizing both as commitments.

You can take a prose causal statement and translate it into a graph, and read a graph back into prose, and notice when the two disagree.

You can write down the factorization of a joint distribution implied by a graph, and read off conditional independencies the graph predicts the data will exhibit.

You can identify which entries in a factored probability table required the analyst to supply structural knowledge the data could not have produced.

You can recognize an undirected edge as honest reporting of Markov-equivalent alternatives the observational data could not distinguish, and name the kinds of additional information — intervention, domain knowledge, distributional assumptions — that could orient it.

The skill you do not yet have a name for is the act of writing arrows in the first place. You have been doing it. The next chapter calls it by its right name.

---

## Bridge to Chapter 4

You just did identification. You did not call it that. You took a prose claim, you turned it into a graph, you listed the missing edges, you committed to a factorization, and you marked which entries the data could supply and which entries you had to supply. That whole process — choosing what is in the model, drawing the arrows, justifying the missing edges, orienting what the data alone cannot orient — is *identification*. Chapter 4 takes the activity you just performed and gives it a vocabulary, a checklist, and a place inside the larger argument about what causal AI tools can and cannot do.

When you read Chapter 4, you will recognize the moves. You have already made them.

---

## Exercises

**Warm-up.**

1. (Apply) *Prose to graph.* Translate the following into a directed graph and list all the missing edges as commitments. "Caffeine consumption affects sleep quality. Sleep quality affects next-day productivity. Caffeine consumption also directly affects next-day productivity, separate from any effect through sleep."

2. (Apply) *Graph to prose.* Write the prose claim for this graph in two or three sentences. Then list at least three missing edges and what each one commits the model to.

   ```
       A ──> B ──> D
       │           ^
       └────> C ───┘
   ```

**Application (Part A — provided scenario).**

3. (Analyze) *Conditional independence from a graph.* For the graph in exercise 2, write the factorization of the joint `P(A, B, C, D)` according to the graph. List two conditional independencies the factorization implies. State, for each, what you would compute from data to test it.

**Application (Part B — your own domain).**

4. (Analyze) *Three representations in your domain.* Choose one. *Either* take the output of your causal-interview tool (if you ran it in the prior chapter), *or* sketch a 4–6 variable causal scenario from a system you have worked on (a model you have deployed, an experiment you have run, a metric you have tracked). Produce all three representations on the same page — diagram, factorization, prose. Label each conditional in the factorization with one of three tags: *data-only* (the data could estimate the parameters once structure is fixed), *structure-from-domain* (you supplied the parent set), *value-from-domain* (a prior or known mechanism supplies the distribution itself). Surface which parts of your model the data could not have produced.

**Synthesis.**

5. (Analyze) *Three vocabularies vs. three representations.* Chapter 2 named three different *vocabularies* — the statistical, the experimental, and the structural — for the same problem of causation. This chapter names three *representations* — diagram, factorization, prose — for the same causal model. They are not the same trio. Write 300–500 words explaining the difference. The vocabularies are about how to *talk about* causal questions; the representations are about how to *write down* one specific causal model. Show, with one example, how all three representations from this chapter sit inside the *structural* vocabulary from Chapter 2.

**Challenge.**

6. (Evaluate) *Orienting an equivalence class.* The three diagrams below are Markov equivalent — they all imply the same single conditional independence `X ⊥⊥ Z | Y` and no others.

   ```
   A:  X ──> Y ──> Z
   B:  X <── Y <── Z
   C:  X <── Y ──> Z
   ```

   Suppose `X` is "household income," `Y` is "neighborhood school quality," `Z` is "child's test score." Name one piece of domain knowledge that would orient between A, B, and C. Then change the variables: let `X` be "ad spend," `Y` be "site traffic," `Z` be "purchase rate." Name the domain knowledge that would orient between A, B, and C *in this case*. Do the orientations match across the two scenarios? Explain.

   Now an extension: name one intervention you could run (in principle, ignoring cost) that would distinguish between A, B, and C without needing domain knowledge.

---

## LLM exercise

Copy the prompt below into Claude, ChatGPT, or Gemini. The exercise is to use the LLM as a candidate-DAG generator and then critique its output the way you critique a junior analyst.

```
You are a causal inference assistant. I am going to describe a system in plain English.
Your job is to produce: (1) a directed acyclic graph naming the variables and edges
in plain ASCII (X --> Y format); (2) the factorization of the joint distribution
implied by your DAG; and (3) for each edge, a one-sentence justification.

Constraints:
- Name only variables I named. Do not add latent variables unless you flag them
  separately as "candidate additions, not in the requested DAG."
- For any edge whose direction you cannot determine from the description, draw an
  undirected edge (X --- Y) and state what additional information would orient it.
- Do not produce a fully directed graph unless every direction has a justification.

System: [paste your own description of a 4-6 variable system, e.g., a recommender,
an A/B test, a retrieval pipeline, a hiring pipeline]
```

After you have the LLM's output, do three things and write up what you find.

1. Find one edge the LLM drew confidently that you believe should have been undirected. Explain why the data the LLM "has" cannot orient it.
2. Find one missing edge — a pair of variables the LLM left unconnected — that you believe should be there. Explain why.
3. Find one variable the LLM omitted that, if included, would change the conditional independences implied by the diagram. Explain how.

**Assessment line.** A strong response identifies at least one edge the LLM oriented without justification, at least one structural assumption hiding in a missing edge, and at least one omitted variable whose inclusion changes the diagram's predictions. A diagram critique that says "looks fine" is a critique that has not yet started.

---

## AI Use Disclosure

**Part A standard form.** If you used an LLM to help draft any answer in this exercise set, attach a one-paragraph disclosure naming the tool, the prompts, and one specific edit you made to the LLM's output.

**Part B bonus criterion.** If your Part B scenario was produced or refined using an LLM, name the prompt you used and identify at least one edge the LLM drew that you changed before submitting, and one edge it omitted that you added. The grader is looking for evidence that you exercised judgment over the tool's output, not that you minimized tool use.

---

## Key terms

- **Directed acyclic graph (DAG).** A picture of variables (nodes) and direct causal influences (arrows), with the constraint that you cannot follow arrows around any loop back to where you started. The acyclicity rules out feedback within the modeled instant; feedback over time is modeled by unrolling the loop across time-indexed copies of the variables.
- **Directed edge.** An arrow `X → Y` claiming that intervening on `X` would change the distribution of `Y`, holding other modeled variables fixed.
- **Missing edge.** The absence of an arrow between two variables — a positive commitment that the source variable has no direct effect on the target variable in the model as drawn.
- **Conditional independence.** A relation between variables `X ⊥⊥ Y | Z` meaning that once `Z` is known, `X` and `Y` carry no further information about each other. Testable from data.
- **Factorization.** The joint distribution written as a product of conditional distributions, one per variable, where each variable is conditioned on its parents in the graph: `P(X₁, ..., Xₙ) = Π P(Xᵢ | Pa(Xᵢ))`.
- **Markov property.** The structural claim that each variable is independent of its non-descendants given its parents in the graph. Connects the graphical and probabilistic representations.
- **V-structure (collider).** A configuration `X → Y ← Z` with two arrows pointing into the same node from non-adjacent sources. Generates a distinctive independence pattern — marginal independence between `X` and `Z`, conditional dependence given `Y` — that observational data can detect and orient.
- **Markov equivalence.** Two directed acyclic graphs are Markov equivalent if they imply exactly the same conditional independencies over the observed variables, and therefore cannot be distinguished from each other by observational data alone (Verma & Pearl 1990).
- **Undirected edge.** A line between two variables — used in partially directed graphs to represent a connection the data establishes but cannot orient. Resolved by intervention, by additional domain knowledge, or by stronger distributional assumptions.
- **CPDAG.** A completed partially directed acyclic graph: the natural output of constraint-based causal discovery (the PC algorithm and its descendants), with arrows on edges that v-structures orient and lines on edges that the equivalence class leaves undetermined.

---

## Further reading

1. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press. Chapter 1, especially §1.4, on the formal equivalence between graphical and structural representations. The foundational treatment.
2. Spirtes, P., Glymour, C., & Scheines, R. (2000). *Causation, Prediction, and Search* (2nd ed.). MIT Press. The PC algorithm, Markov equivalence, and CPDAGs in full detail. Open access at https://www.cmu.edu/dietrich/philosophy/docs/scheines/causation%2C%20prediction%2C%20and%20search.pdf
3. Verma, T., & Pearl, J. (1990). "Equivalence and Synthesis of Causal Models." *Proceedings of the Sixth Conference on Uncertainty in Artificial Intelligence* (UAI '90), pp. 220–227. The theorem that establishes Markov equivalence. https://arxiv.org/abs/1304.1108
4. Koller, D., & Friedman, N. (2009). *Probabilistic Graphical Models: Principles and Techniques*. MIT Press. The canonical reference for the factorization representation in graduate machine learning curricula.
5. Textor, J., van der Zander, B., Gilthorpe, M. S., Liśkiewicz, M., & Ellison, G. T. H. (2016). "Robust causal inference using directed acyclic graphs: the R package 'dagitty'." *International Journal of Epidemiology* 45(6), 1887–1894. https://doi.org/10.1093/ije/dyw341. The standard pedagogical tool; the web version at https://dagitty.net is free and worth a hands-on hour.
6. Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall. Open PDF at https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/. Chapter 6 on graphs is the most accessible introduction in the applied literature.

---

**What would change my mind:** A demonstration that a tool which presents fully directed graphs from observational data alone is doing so by transparent, defensible, and inspectable use of domain or distributional assumptions — visible to the user, audited, and overridable — would substantially weaken my claim that lines are the more honest output.

**Still puzzling:** I do not yet know how to teach the move from "I drew a diagram" to "I trust this diagram enough to act on it." The diagram is the artifact; the trust is the judgment; the chapter explains how to build the artifact but I cannot yet write the rule that says when to act on it.

---

**Tags:** directed-acyclic-graph, Markov-equivalence, conditional-independence, identification, causal-discovery

---

**Draft flags:**
- `[verify]` — None of the contestable factual claims are flagged; all cite primary sources directly.
- *Markov equivalence theorem citation.* Verma & Pearl 1990 is in the UAI '90 proceedings; I have linked to the arXiv preprint that hosts the canonical text. If a different archival URL is preferred, swap in the ACM Digital Library link (https://dl.acm.org/doi/10.5555/647233.719736).
- *LiNGAM and additive-noise framing.* I named these as a counter-current under strong assumptions. If you want a fuller exposition (one paragraph more), say so and I will add a worked illustration; otherwise the current treatment is calibrated to "name it, do not teach it."
- *Interview tool licensing.* Per TIKTOC Risk 6, the chapter's Part B exercise accommodates students who did not run the tool ("either your interview-tool output OR a 4–6 variable scenario from your domain"). No further action needed unless the licensing situation resolves and you want to lean harder on the tool in revision.
- *Engineer vs. causal diagram vs. data-flow diagram framing.* The pantry notes flagged this as a likely failure mode; I addressed it implicitly (the hiring-pipeline example shows where acyclicity holds and where it doesn't) but did not name "data-flow diagram" as a contrastive object. If you want an explicit side-by-side, add it as a one-paragraph aside in the missing-arrow section.
