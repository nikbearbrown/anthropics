# The Contract the Tool Reads — Not the One You Meant


## TL;DR

- TL;DR: A defended DAG handed to a causal-inference tool without a written specification is a defended DAG the tool will quietly violate; the spec document — and especially its "do-not-add" list — is what makes Act...
- The chapter moves through Opening — The handoff failure, Concept one — The estimation specification document: what it contains, Mid-chapter checkpoint, Concept two — Why tool defaults are dangerous, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**Suggested titles:**
1. The Contract the Tool Reads — Not the One You Meant
2. From DAG to Data: What the Machine Needs (and Quietly Decides Without You)
3. The Specification Document, or: How Your Identification Work Survives the Handoff

**TL;DR:** A defended DAG handed to a causal-inference tool without a written specification is a defended DAG the tool will quietly violate; the spec document — and especially its "do-not-add" list — is what makes Act Two's identification work survive contact with the algorithmic layer in Act Three.

**Byline:** Nik Bear Brown

**Prerequisites:**
- The defended DAG from Chapter 11 — the arrows you argued for, the variables you ruled out, the unmeasured confounders you named.
- The full identification toolkit from Chapters 5–10: confounders, mediators, colliders, descendants, the backdoor criterion, minimal adjustment sets, non-identifiability.
- Python fluency at the level the rest of the course assumes. You do not have to have used [DoWhy](https://www.pywhy.org/dowhy/) or [EconML](https://www.pywhy.org/EconML/) before — we will walk through the relevant calls — but you should be comfortable reading library code.

**Learning objectives:**
- **Apply (Part A):** Produce a complete *estimation specification document* for a defended DAG — treatment, outcome, adjustment set with structural justification per variable, named identification assumptions, an explicit "do-not-add" list with per-variable justification, and an estimation method choice with its assumptions.
- **Analyze:** Explain mechanically why a causal-inference tool's defaults — automatic covariate inclusion, propensity-score variable selection by predictive accuracy, default model class — threaten each of the three identification failures from Chapter 4 (variables, arrows, conditioning).
- **Evaluate (Part B — Specification Checkpoint):** Produce the spec document for your own defended DAG, and assess where the tool you intend to use would silently violate it.

---

## 1. Opening — The handoff failure

In the summer of 2023, a small product-analytics team at a mid-sized SaaS company — call them Team Onboarding — ran what they believed was a textbook causal evaluation. They were redesigning the new-user onboarding flow, and the question was the kind every product team eventually has to answer: does the new flow actually increase seven-day retention, or does it just look like it does because the kind of user who finishes the new flow was always going to retain?

They did the right early work. They built a DAG. Pre-treatment confounders: acquisition channel, signup cohort, device type, prior product affinity. Mediators on the causal path: time-to-first-action, features touched on day one, session length on day one. Their defended DAG had three pre-treatment variables in the adjustment set and three post-treatment variables explicitly excluded. They had checked the minimal set against DAGitty. They had argued about the direction of the arrow between session length and retention for forty-five minutes in a whiteboard meeting.

Then they handed it to the tool.

The tool was a recent version of a popular causal-inference library — I will not name the version, because the specific version does not matter; what matters is the pattern. The analyst wrote five lines of Python. Load the dataset. Declare the treatment. Declare the outcome. Pass the full feature dataframe. Call `.estimate_effect()`. The library returned a number with a confidence interval and a small p-value. The new flow appeared to *decrease* seven-day retention by about 1.4 percentage points. The team, surprised, scheduled a review with a senior data scientist.

The senior data scientist asked one question: *which variables did the tool adjust for?*

The analyst pulled up the run. The library, by default, had adjusted for every variable in the dataframe numerically associated with both treatment and outcome above an internal threshold. That set included `session_length_day_1` and `features_touched_day_1` — two of the three post-treatment variables the team had explicitly excluded. The DAG said do not condition on these; they are downstream of the treatment. The tool said they look like good controls because they correlate with both. The DAG was on a piece of paper. The tool's default was in the code.

Three weeks later the team re-ran the analysis with only the three pre-treatment variables and explicit suppression of covariate auto-selection. The new flow *increased* seven-day retention by 2.1 percentage points. Same data. Same DAG. The difference between *minus 1.4* and *plus 2.1* — between killing a redesign and shipping it — was whether the tool honored the team's exclusion list or silently substituted its own.

I have changed the company name and the numbers. The pattern is real. The [py-why GitHub issue tracker](https://github.com/py-why/dowhy/issues) contains a recurring class of user reports along these lines — "I passed my dataframe to the library, the estimate was wrong, the wrong number came from a post-treatment variable I did not mean to include." `[verify-specific-issues]` Public post-mortems are rare; nobody writes a blog post titled *We Shipped The Wrong Causal Conclusion Because Our Library's Defaults Outranked Our DAG*. Internally, this happens enough that engineers burned once become evangelists for the discipline this chapter is about.

The DAG was not wrong. The defense was not wrong. What was wrong was that the team had nothing between the defended DAG and the tool except an analyst's memory of the adjustment set — and the tool was not consulting that memory.

The artifact that should have stood there is the *estimation specification document*. The "spec." A markdown file, a confluence page, a docstring at the top of the analysis script — it names every input the tool needs and every decision the tool must not make on its own. Without it, what the tool reads from the dataframe and from its own defaults is what counts.

This is the first chapter of Act Three. Acts One and Two taught you to do the identification work. Act Three teaches you how to preserve that work through the algorithmic layer. The spec is the contract. The do-not-add list is its most consequential clause.

---

## 2. Concept one — The estimation specification document: what it contains

Let me define the artifact before arguing about it.

An *estimation specification document* — I will use "spec doc" or just "spec" — is a written artifact, separable from the analysis code, that names every component a causal-inference tool needs in order to estimate the causal effect of a treatment $T$ on an outcome $Y$, *and* names the decisions the tool must not make autonomously. The spec is to a causal analysis what an API contract is to a service: it declares what the caller will provide, what the callee will return, and what behaviors are explicitly out of scope.

The minimum sections, in the order I find easiest to write:

**1. Specification ID and date.** A unique slug (e.g., `onboarding-flow-v3-retention-2026Q2`), the date, the author, and a link to the *defended DAG* this spec implements. The DAG defense should be a separate document (Chapter 11); the spec carries the reference. Without the link back, six months later someone re-running the analysis cannot check whether the spec still matches the DAG.

**2. Treatment $T$.** Named, operationalized, data-typed. Not "the new onboarding flow." `treatment_arm` ∈ {`flow_v2`, `flow_v3`}, categorical, recorded in `users.signup_flow_assigned`, populated at the moment of first signup. The operationalization is the bridge from the DAG node (a concept) to the data column (a measurement). If two people would disagree about which rows have $T=1$, the operationalization is not finished.

**3. Outcome $Y$.** Same standard. Not "retention." `retained_7d` ∈ {0, 1}, defined as "at least one session, of at least 60 seconds duration, in the window [signup + 7 days, signup + 8 days]." The window matters. The session-length threshold matters. A spec that says "retention" and lets the tool guess is a spec inviting a tool to guess wrong.

**4. Estimand.** The specific quantity. The default is the *average treatment effect (ATE)*, $E[Y \mid do(T=1)] - E[Y \mid do(T=0)]$. But you may want the ATT (effect on the treated), the *controlled direct effect* (which fixes a mediator), or a *conditional average treatment effect* (CATE) on a subgroup. The estimand drives the estimator choice. A spec that does not name it is letting the tool pick.

**5. Sample definition.** Population, selection criteria, sample size, cohort window, exclusions. "All users who signed up between 2026-03-01 and 2026-04-30, in the United States, on iOS or Android, excluding test accounts (n = 47,213)." Selection criteria sometimes condition on colliders (Chapter 8); the spec records the selection so a reviewer can check.

**6. Adjustment set $Z$.** The variables you will condition on, with *one-line structural justification per variable*. Not "we adjusted for cohort because it seemed important." Cohort, because it affects both flow assignment (routing algorithm changed over the cohort window) and retention (seasonal usage patterns); blocks the path $T \leftarrow \text{cohort} \rightarrow Y$. Device type, because it affects flow assignment (rollout schedule) and retention (device-specific baselines). Prior product affinity, because it affects both assignment (high-affinity users routed into experimental flows) and retention. Three variables. Three sentences. The structural argument is on the page.

**7. Identification assumptions.** The claims that make $Z$ valid:
- *No unmeasured confounding given $Z$* (conditional ignorability). The honest version: name the unmeasured confounders you considered and could not measure, and state the bias direction if each operates. "Intrinsic user motivation considered; motivated users may both prefer the new flow and retain more strongly; bias direction *upward*."
- *Positivity*. Every covariate stratum has both treated and untreated observations. Name how this is checked.
- *SUTVA*. One user's treatment status does not affect another's outcome. Network-effect analyses must not assume this.
- Any other assumption the chosen estimator imposes.

**8. The "do-not-add" list.** Variables the tool must not add to $Z$. Each entry carries a category and a structural justification:
- *Mediators* — on the causal path $T \to \cdots \to Y$. Conditioning destroys the total effect.
- *Colliders* — common effects of two ancestors. Conditioning induces spurious association.
- *Descendants of $T$* — post-treatment variables generally bias the estimate.
- *Instruments* — affect $T$ only, not $Y$. Adjusting can amplify bias from remaining unmeasured confounding ([Pearl 2010 UAI](https://ftp.cs.ucla.edu/pub/stat_ser/r356.pdf) `[verify-URL]`).
- *Outcome proxies* that are not confounders. Variance inflation without bias reduction.

Section 5 unpacks each. The list must be present, named, and justified.

**9. Estimation method.** Which estimator: regression with adjustment, inverse probability weighting, doubly-robust estimation, double/debiased machine learning (DML), causal forest for heterogeneous effects. The choice carries assumptions — the propensity model is correct enough, the outcome model is correct enough, the DML orthogonality holds — and the spec names which assumption the choice rests on.

**10. Planned refutation checks.** Diagnostic runs that test structural robustness. [DoWhy](https://www.pywhy.org/dowhy/) exposes these as first-class objects: *placebo treatment* (replace $T$ with random noise; estimate should collapse), *random common cause* (add an artificial confounder; estimate should be insensitive), *subset robustness*, *dummy outcome*. The spec names which checks will run and what counts as a pass.

**11. Planned sensitivity analyses.** What happens when the no-unmeasured-confounding assumption is violated. Chapter 14 teaches this in full. Name the analysis — E-value, Rosenbaum bounds, Cinelli–Hazlett sensitivity contour.

That is the full structure. Eleven sections. Most fit on two pages. A simple analysis compresses sections 6, 7, 9, 10, 11 to a paragraph each; a regulatory-grade analysis expands them. The skeleton is the same.

One methodological caution about my own prescription: *the method applies to the method*. For a randomized experiment with no covariate adjustment — identification by design — the full spec is overkill. The spec is the right discipline when identification rests on a *defended* DAG with *adjustment*; it is overhead when identification rests on randomization alone. The chapter teaches the full form because the half-form is easy to recover once you know what you are compressing.

A common misconception: students sometimes read the spec format and pattern-match it to "design doc" or "compliance form" — artifacts they have learned to produce minimally. The spec is the *proof of work* for the identification layer. Without it, Chapter 11's defense has no traceable connection to the estimation run. Treat it as paperwork and it becomes paperwork. Treat it as the contract that constrains the tool and it becomes what it is for.

---

## 3. Mid-chapter checkpoint

Three questions before we keep going. If your answers are confident, the next sections will go fast. If any answer is hesitant, re-read Section 2.

1. Could you, right now, write the eleven-section spec for a causal analysis you have already seen — Chapter 10's diabetic-coaching worked example, say? If not, the format is not yet sticky. Try it before continuing.
2. Could you name three variables on the *do-not-add* list for a typical pricing analysis, assigning each a category and a one-sentence structural justification?
3. Could you predict, for a causal-inference library you have used, what its default behavior is when `.estimate()` receives a dataframe with more columns than your adjustment set? If not, the next section will be uncomfortable. Intentionally so.

---

## 4. Concept two — Why tool defaults are dangerous

Let me show you what the tools actually do.

Three production libraries are common in the engineering reader's stack: [DoWhy](https://github.com/py-why/dowhy) ([Sharma & Kıcıman 2020 arXiv:2011.04216](https://arxiv.org/abs/2011.04216)), [EconML](https://github.com/py-why/EconML) ([Battocchi et al. 2019](https://www.microsoft.com/en-us/research/project/econml/)), and [CausalML](https://github.com/uber/causalml) (Uber). DoWhy is the most explicit about identification — its four-step workflow (model, identify, estimate, refute) makes identification a first-class API call. EconML and CausalML focus on estimation and assume identification has been settled.

Each has defaults that can violate identification, in different ways.

**Default 1: Automatic covariate inclusion from the feature pool.**

The most common failure mode. The pattern, in DoWhy-flavored code (EconML's `LinearDML` and CausalML's `BaseRRegressor` admit the same failure under similar code):

```python
import pandas as pd
from dowhy import CausalModel

df = pd.read_parquet("onboarding_data.parquet")
# df has columns: user_id, treatment_arm, retained_7d,
#                 cohort, device, prior_affinity,
#                 session_length_day_1, features_touched_day_1,
#                 sessions_day_2_to_7, support_tickets_filed

model = CausalModel(
    data=df,
    treatment="treatment_arm",
    outcome="retained_7d",
    common_causes=None,  # <-- the failure point
)
identified = model.identify_effect()
estimate = model.estimate_effect(
    identified,
    method_name="backdoor.linear_regression",
)
print(estimate.value)
```

The argument `common_causes=None` does not mean "no common causes." It means "library, please figure out which columns are the common causes." The heuristic varies by library version, but is usually some flavor of "treat every non-treatment, non-outcome column as a candidate confounder, optionally filter by univariate association with both $T$ and $Y$." `[verify-current-dowhy-default]`

If `df` contains `session_length_day_1`, the library may include it as a confounder. The library cannot know it is a post-treatment variable; the DAG that says so lives on paper, not in the dataframe. The dataframe is just columns of numbers with names attached.

The result: a biased estimate. No warning. Some library versions print the inferred common-causes list in `model.identify_effect()` output; the analyst who skips that verbose print will not see the substitution.

The fix is one line:

```python
model = CausalModel(
    data=df,
    treatment="treatment_arm",
    outcome="retained_7d",
    common_causes=["cohort", "device", "prior_affinity"],
)
```

One line, *if you have the spec*. Without the spec, the fix is one line of code the analyst did not write because they did not know which variables belonged on the list.

**Default 2: Propensity-score variable selection by predictive accuracy.**

Older — it predates current libraries and lives in any pipeline that builds a propensity score $P(T=1 \mid X)$ by selecting features for predictive accuracy of $T$. The motivation seems reasonable: we want a propensity score that predicts $T$ well, so we select strong predictors of $T$. The problem: the strongest predictors of $T$ are often *instruments* — variables that affect $T$ but not $Y$ — and selecting them *amplifies* bias from any remaining unmeasured confounding.

Feature selection that *predicts $T$ better* makes the causal estimate *worse*. The engineering intuition — bigger feature set, stronger predictor — is exactly wrong here. The correct selection criterion is *which variables are common causes of $T$ and $Y$*, not *which variables predict $T$*. The two sets overlap but are not the same.

Structural argument: [Pearl 2010](https://ftp.cs.ucla.edu/pub/stat_ser/r356.pdf) `[verify-URL]`. Practical guidance: [VanderWeele 2019, "Principles of Confounder Selection," *European Journal of Epidemiology*](https://doi.org/10.1007/s10654-019-00494-6) `[verify-pagination]`. The engineering takeaway: predictive-accuracy confounder selection is not the same as structural confounder selection, and the difference can be the sign of the answer.

**Default 3: Default model class.**

Libraries default to a specific functional form — linear regression for the outcome model, logistic regression for the propensity model, gradient-boosted trees for DML nuisance models. These defaults are sensible in the average case in the tool's design population. Your case has assumptions the tool does not know about. If your DAG implies a non-linear relationship, the default linear adjustment is mis-specified. If your DAG implies a treatment-covariate interaction, the default additive model misses it. The spec names the model class. The default does not.

**Default 4: Silent handling of missing data, imbalanced classes, and overlap violations.**

Three smaller defaults sharing a form. Missing data: impute by mean. Imbalanced classes: down-sample. Positivity violation (strata where $P(T=1 \mid X)$ is zero or one): extrapolate or silently drop. Each is reasonable for prediction; each is a structural change for identification. The spec names how each is handled. The default chooses silently and reports a number that combines the analyst's estimand with the library's data-handling choices.

The pattern across all four: the library is not buggy. The library is correct in the sense a contract is correct when it omits a clause — the contract executes, the omission has consequences, neither party is aware until something downstream goes wrong.

The engineering reader's habit, formed in supervised learning, is to trust library defaults. There, adding a feature usually does not hurt. In causal inference, adding the wrong feature is biased estimation. The libraries inherit defaults from the prediction tradition because that is where most of their authors come from. The defaults make sense in the world they came from. Not in the world you have just moved into.

This is the architectural point. *Identification precedes estimation.* The spec is the contract that imposes identification's commitments on the estimation tool. Left to itself, the tool substitutes prediction's commitments — because those are the ones baked into its defaults.

---

## 5. Concept three — The "do-not-add" list, item by item

The adjustment set names what to include. The do-not-add list names what to *exclude*, and *why*. The list is the operational consequence of every identification chapter you have read. Each item belongs in a named category, and each category implies a structural rule.

I want to give you the categories with one-sentence rules, because the rules are what survives when memory of the proof fades. The proofs are in Chapters 5–10; the rules are the artifacts.

**Mediators.** A mediator $M$ is on a causal path from $T$ to $Y$ — the path $T \to M \to Y$ exists in the DAG. *Rule: do not condition on a mediator if you are estimating the total effect.* Conditioning destroys the total effect (Chapter 6).

In flow-redesign analyses: session length, features touched, time to first action — all mediators. They sit on the causal path the redesign acts through. Conditioning estimates the redesign's effect *holding session length fixed* — not the question the VP is asking.

**Colliders.** A collider $C$ on a path is where two arrows on the path point in: $A \to C \leftarrow B$. *Rule: do not condition on a collider, and do not condition on any descendant of one.* Conditioning opens a path that was closed (Chapters 7–8).

Trap: colliders often look like good controls because they correlate with both $T$ and $Y$. The correlation is real. The structural implication is the opposite. The do-not-add list catches what the adjustment-by-correlation reflex does not.

**Descendants of $T$ (post-treatment variables).** Anything downstream of $T$. Mediators are a special case; anything else $T$ causally affects also belongs here. *Rule: do not condition on any descendant of $T$.* Bias direction varies, but bias is generic ([Cole, Platt, Schisterman et al. 2010, *IJE*](https://doi.org/10.1093/ije/dyp334) `[verify-pagination]`).

Engineering trap: in production pipelines, *most* rich features — engagement metrics, behavioral signals, downstream conversion events — are post-treatment. They look like signal because they correlate with both $T$ and $Y$, for a reason: $T$ causes them.

**Instruments.** A variable $W$ that affects $T$ but not $Y$ except through $T$. *Rule: do not condition on an instrument when adjusting for confounders.* Adjusting can amplify bias from any remaining unmeasured confounding ([Pearl 2010](https://ftp.cs.ucla.edu/pub/stat_ser/r356.pdf) `[verify-URL]`). Instruments have a separate role (instrumental-variable estimation), but belong in that method's spec, not the adjustment-set list of a backdoor analysis.

**Outcome proxies that are not confounders.** Correlate with $Y$ but are not common causes of $T$ and $Y$. Add no backdoor closure, do add noise. *Rule: do not add unless you have a specific variance-reduction argument and the proxy is pre-treatment.*

Three further pieces of discipline:

*Ambiguous causal role.* When you cannot determine whether a variable is a pre-treatment confounder or a post-assignment artifact, default to *exclusion* — not engineering's "throw it in" reflex — *and write the ambiguity into the spec.* "Considered `partner_referral_status`; role ambiguous; excluded pending investigation; if a confounder, estimate biased in direction $D$ by approximately $\delta$ under reasonable parameter assumptions." Harder to write. Defensible six months later.

*Tool-default asterisk.* Each entry deserves an asterisk if the tool you intend to use would include the variable by default. The asterisk is the prompt to write the override explicitly in code.

*Positive exclusion versus omission.* A variable absent from your adjustment-set list is not excluded — it is *omitted*. If the tool's default scans the dataframe for candidates, omission means the tool picks it up. Positive exclusion in the spec, plus pipeline enforcement, is structurally different from leaving the variable out and hoping.

A common misconception: students produce adjustment sets readily and do-not-add lists reluctantly, because the do-not-add list requires anticipating what an unchecked tool would include. Structurally harder than the include list. It is also the exercise that prevents the Section 1 failure. The Specification Checkpoint grades the do-not-add list at 25 of 100 points for this reason.

---

## 6. Concept four — Where the handoff most often fails

I have named one failure mode in Section 1 (tool defaults override exclusion) and one in Section 4 (the tool's defaults span four mechanically distinct families). Let me name the meta-pattern: the *handoff failure* taxonomy. There are three places the spec-to-tool transmission breaks down, and the practitioner needs to recognize each.

**(a) The spec doc does not exist.**

The most common failure. The analyst has the DAG, the defense, and the code. No written spec. The identification decisions live in the analyst's head, in whiteboard photos, in a slack thread from the DAG review. They do not live anywhere that can be re-read six months later or audited by a reviewer. Section 1's team did not have a spec; the team three weeks later did.

Remedy is mechanical: writing the spec is the first step of estimation, not optional cleanup. If you are about to call `.estimate_effect()` and there is no spec, stop and write one. Twenty minutes. The estimate can wait.

**(b) The spec exists, but the tool's interface does not expose every section.**

The library accepts treatment, outcome, and adjustment set. It does not accept a do-not-add list as an explicit parameter. The defense: do not have those columns in the dataframe in the first place. Project the dataframe down to {treatment, outcome, adjustment set} before passing it to the library; the library's auto-inclusion behavior has nothing to grab. The do-not-add list is enforced by the data pipeline rather than the library API.

This is the pattern I recommend for production: write the spec, then write a one-function `prepare_data_for_estimation(df, spec)` that projects the full dataframe to exactly the authorized columns. Enforce the contract upstream of the tool.

**(c) The spec exists, the interface supports it, the analyst forgets to use it.**

The boring failure. The library exposes `common_causes`; the analyst writes the call without populating it; the default fires. Remedy: code review on causal-analysis scripts checks every argument the spec named, with the spec open alongside the code. *Linting for causal analyses* — tools that read the spec and check the code against it — is emerging engineering practice `[verify-current-tooling]`.

The taxonomy matters because each failure has a different remedy. (a) is fixed by writing the spec; (b) by enforcing it in the data pipeline; (c) by reviewing code against the spec. A team that writes a spec and assumes writing is sufficient — without pipeline enforcement — has a partial fix and may still ship the wrong answer.

---

## 7. Concept five — The handoff as a structural transition

Step back. Look at the architecture.

For eleven chapters you have been doing one thing: identification. The DAG, the adjustment set, the named confounders, the named non-identifiabilities, the defense. The work has been *structural*. It produced an *expression*: under the maintained DAG, $E[Y \mid do(T=t)] = \sum_z E[Y \mid T=t, Z=z] P(Z=z)$, with $Z$ the named adjustment set.

Chapters 13–15 do a different thing: estimation. The tool, the model class, the fit, the confidence interval, the refutation check, the sensitivity analysis. *Statistical* — how a finite sample lets you compute a number that approximates the expression, and how robust that number is to assumption violations.

This chapter is the bridge. *The spec is the contract that says: here is the expression, here is what the tool must compute, here is what the tool must not do.* Without the bridge, structural and statistical work are connected only by an analyst's memory. With the bridge, the structural work persists as an auditable artifact that constrains the statistical work.

The architectural distinction matters because the engineering reader will encounter, in production, tools that *blur* the layers. A tool that accepts a dataframe and a problem description and returns "the causal effect" — increasingly common with LLM-front-ended causal libraries `[verify-current-LLM-causal-tooling]` — looks like it does identification and estimation in one step. It does not. The identification decisions are still being made; they are just being made by the LLM's defaults rather than by the analyst's reasoning. The spec is still the right contract; the question is whether the tool reads the spec the analyst wrote, or substitutes one the LLM generated.

My position, plainly: an LLM can *draft* a spec faster than I can. An LLM cannot *defend* a spec, because defending requires domain knowledge the LLM does not have and willingness to be wrong about specific arrows the LLM cannot take responsibility for. The analyst's job, in the LLM-assisted workflow, is to take the LLM's draft and defend it line by line — "is this what I would have written? if not, why, and is the difference correct?" That work is the work this chapter has been teaching. The LLM accelerates the typing, not the thinking.

[Kıcıman, Ness, Sharma, Tan 2023, "Causal Reasoning and Large Language Models"](https://arxiv.org/abs/2305.00050) `[verify-current-version]` argues this in detail: LLMs produce plausible-looking causal reasoning but cannot reliably perform identification on unfamiliar domains. LLM-assisted spec drafting is useful; LLM-replaced spec defense is not safe.

---

## 8. Worked example — A pricing analysis, with and without the spec

Let me work the full pipeline on a concrete case. I am going to use a small synthetic dataset because the point is the pipeline, not the dataset; you should run this on your machine to see the divergence.

**The scenario.** An e-commerce platform is testing a 5% price reduction on a category of mid-priced goods. Treatment $T$: whether a user saw the new (reduced) price on their first visit during the test window. Outcome $Y$: revenue per session, measured in dollars. The defended DAG, after a Chapter 11 review:

- Pre-treatment confounders: `user_segment` (high / med / low value, assigned by the CRM before the test), `temporal_trend` (a day-of-week / time-of-day index), `device_class` (mobile / desktop / tablet — different cohorts saw the test on different devices due to a rollout schedule).
- Mediator (post-treatment, on the causal path): `session_length_seconds` — reduced prices increase browsing time, which increases revenue.
- Descendant of $T$, post-treatment, not a mediator on the path to revenue but a downstream effect: `clicked_promo_banner` — the promo banner was shown to users in the treatment arm only.
- Outcome proxy: `last_session_revenue` from the prior visit. Correlated with $Y$ but not a confounder.

**The spec doc** (compressed):

```
Specification ID: pricing-test-2026-q2-v1
Date: 2026-05-13
Author: [you]
Linked DAG defense: pricing_test_dag_v3.md

Treatment T: shown_reduced_price ∈ {0, 1}, populated at first-page-render of test window
Outcome Y: revenue_per_session, dollars, measured at session end
Estimand: ATE on the test cohort
Sample: 24,891 sessions, 2026-04-15 to 2026-05-01, US users only

Adjustment set Z:
  - user_segment (CRM segment; affects both treatment assignment cohort and baseline revenue;
    blocks T <- user_segment -> Y)
  - temporal_trend (day-of-week × time-of-day; affects both rollout schedule and revenue)
  - device_class (rollout schedule × device-specific baseline revenue)

Identification assumptions:
  A1: No unmeasured confounding given Z. Considered: user-intrinsic price sensitivity. If operating,
      would bias estimate upward (price-sensitive users may both prefer treatment AND have higher 
      baseline revenue conditional on visiting).
  A2: Positivity verified — every (segment × trend × device) cell has both T=1 and T=0 (n>=30).
  A3: SUTVA — sessions are independent across users (verified: 99.7% of users in test had ≤1 session).

Do-not-add list:
  - session_length_seconds (mediator on causal path price → session length → revenue)
  - clicked_promo_banner (descendant of T; banner shown to T=1 only)
  - last_session_revenue (outcome proxy; not a confounder; variance inflation only)

Estimation method: linear regression with adjustment set, robust SE.
  Assumption: linearity of E[Y | T, Z] in Z; will check via residual plot.

Refutation checks: placebo treatment, random common cause, subset robustness (10 folds).
Sensitivity analysis: E-value on the unmeasured price-sensitivity assumption (Ch. 14).
```

**The run, with the spec enforced.** DoWhy-flavored code that honors the spec, with the dataframe projected before the call:

```python
import pandas as pd
from dowhy import CausalModel

# Load the full feature dataframe
df_full = pd.read_parquet("pricing_test.parquet")

# Per the spec, project to authorized columns only
authorized = [
    "shown_reduced_price",       # T
    "revenue_per_session",       # Y
    "user_segment",              # Z
    "temporal_trend",
    "device_class",
]
df = df_full[authorized].copy()

# Build the model with explicit common_causes (the spec's Z)
model = CausalModel(
    data=df,
    treatment="shown_reduced_price",
    outcome="revenue_per_session",
    common_causes=["user_segment", "temporal_trend", "device_class"],
)

identified = model.identify_effect(proceed_when_unidentifiable=False)
estimate = model.estimate_effect(
    identified,
    method_name="backdoor.linear_regression",
)

print(f"Spec-conformant estimate: ${estimate.value:.3f} per session")

# Refutation check
refute = model.refute_estimate(
    identified, estimate,
    method_name="placebo_treatment_refuter",
)
print(refute)
```

On synthetic data with a true ATE of $+0.42 per session: estimate approximately $+0.41, 95% CI excludes zero, placebo-refutation returns approximately $0.00 (correctly collapsing). Spec honored. Number close to truth.

**The run, without the spec.** Same call, but the analyst has not written the spec, has not projected the dataframe, and trusts the library default:

```python
model = CausalModel(
    data=df_full,                 # full feature df, all columns
    treatment="shown_reduced_price",
    outcome="revenue_per_session",
    common_causes=None,           # let the library decide
)
identified = model.identify_effect(proceed_when_unidentifiable=False)
estimate = model.estimate_effect(
    identified,
    method_name="backdoor.linear_regression",
)
print(f"Default estimate: ${estimate.value:.3f} per session")
```

With `common_causes=None`, the library may scan the dataframe and include columns with significant association to both $T$ and $Y$. On this dataset, that set includes `session_length_seconds` and `clicked_promo_banner` — both excluded by the spec. The estimate drops to approximately $+0.11; CI includes zero. The placebo refutation still passes (it tests the wrong thing — robust to confounder simulation, not mediator inclusion). The analyst reading the output concludes the price reduction has no detectable effect.

The number changes from $+0.41 to $+0.11. The decision changes from "ship" to "do not ship." Same data. Same DAG. Same defense. The spec is the difference.

One caveat: the library's auto-inclusion behavior depends on version and data. The principle — *unauthorized columns can be auto-included; auto-inclusion of mediators or descendants biases the estimate; spec plus projection prevents this* — is robust to version. The specific numbers are illustrative. Run it on your own data. The magnitude is the cost of skipping the spec.

---

## 9. Integration — The spec preserves the defense

A defended DAG without a spec is a defended DAG the tool will violate. A spec without a defended DAG is paperwork without proof of work. The two are paired: the defense (Chapter 11) makes the case; the spec (this chapter) carries it across the handoff.

What the spec preserves, by section:
- The *DAG* → the *adjustment set with structural justification* (§6) + the *do-not-add list* (§8).
- The *named confounders* → the *identification assumptions* with bias direction (§7).
- The *named non-identifiabilities* (Ch. 10) → either *instrument entries in the do-not-add list* or a *partial-identification note* (§8, §11).
- The *defended exclusions* (Ch. 11's adversarial-review move) → the *positive exclusion* in the do-not-add list (§8).
- The *measurement operationalization* → the *treatment and outcome definitions* (§2, §3).

Every part of the defense maps to a section of the spec, and vice versa. The two artifacts are isomorphic in content; what differs is the audience. The defense is for the methodologist who argues about arrows. The spec is for the tool, the code reviewer, and the analyst who picks up the analysis six months from now.

Chapter 4's three identification failures — wrong variables, wrong arrows, wrong conditioning — are each constrained by a spec section. *Wrong variables*: caught by the adjustment-set-with-justification format; an entry without justification is incomplete. *Wrong arrows*: caught by the DAG defense linked from the spec. *Wrong conditioning*: caught by the do-not-add list's explicit exclusion of mediators, colliders, and descendants.

---

## 10. Chapter summary

The estimation specification document is a written, separable artifact that names every input a causal-inference tool needs and every decision the tool must not make on its own. Eleven sections, from operational (treatment, outcome, sample) to structural (adjustment set with justification, identification assumptions, do-not-add list) to diagnostic (refutation checks, sensitivity analyses).

Causal-inference tools — DoWhy, EconML, CausalML — vary in how visible their identification step is, but all carry defaults that can violate identification: automatic covariate inclusion, propensity-score selection by predictive accuracy, default model class, silent handling of missing data and positivity violations. Each is sensible in the prediction tradition the tools inherit from. None is necessarily sensible for the causal analysis the analyst has just defined.

The do-not-add list is the spec's most consequential section. Each entry has a category — mediator, collider, descendant of treatment, instrument, outcome proxy — and each implies a structural rule from earlier chapters. The list is positive exclusion; absence from the adjustment set is not the same as positive exclusion, because auto-inclusion defaults will close that gap.

The handoff fails three ways: spec missing; spec present but interface incomplete; spec present, interface adequate, analyst forgets. Each has its own remedy — write it; enforce it in the data pipeline; review code against it.

Architecturally: identification precedes estimation. The spec is the contract between the two layers. A tool that appears to do both in one step — including LLM-assisted workflows — is making identification decisions invisibly. The analyst's job is to defend the spec, whatever drafted it.

---

## 11. Bridge to Chapter 13

The spec is written. The code is conformant. The tool returns a number. Chapter 13 asks the harder question: how do you read it? The estimate has a value, a confidence interval, a refutation report, and — if you did this right — a sensitivity-analysis attachment. What does each tell you? Where can the tool's output mislead even an analyst who wrote a clean spec? What do you do when the refutation check fails, the CI crosses zero, or sensitivity says the conclusion is fragile? The spec is the contract going in. The output report is the contract being inspected on the way out. Chapter 13 is the inspection.

---

## 12. Exercises

### Warm-up

**Exercise 12.1 — Do-not-add list, given a DAG.** Consider a DAG with nodes T, Y, A, B, M, C, D. Arrows: A → T, A → Y, B → T, B → Y, T → M, M → Y, C → A, C → Y, T → D, D → Y. Treatment is T; outcome is Y. Write the do-not-add list and assign each entry a category (mediator, collider, descendant of T, instrument, outcome proxy) with a one-sentence structural justification.

**Exercise 12.2 — Predict a tool's default failure.** Pick a causal-inference library you have used or read about (DoWhy, EconML, CausalML, scikit-uplift, or another). Read its documentation for the equivalent of `common_causes=None` (or whichever flag controls automatic covariate inclusion). State, in one paragraph: (a) what the library's default behavior is when no adjustment set is specified; (b) which variable category from the do-not-add list this default would most likely sweep in, and why; (c) the exact line of code that would override the default and enforce a spec-specified adjustment set.

### Application — Part A (instructor's domain DAG)

**Exercise 12.3 — Full estimation specification for the instructor's DAG.** The instructor will provide a defended DAG (the domain will be set at office hours). Produce the full eleven-section spec document. Grading rubric: see Section 13 (Specification Checkpoint). Include the spec in markdown form and the corresponding library call (DoWhy preferred; EconML or CausalML acceptable).

### Application — Part B (your own defended DAG) — SPECIFICATION CHECKPOINT

**Exercise 12.4 — Specification Checkpoint, 100 points.** Take the defended DAG you produced for Chapter 11's Part B. Produce the full estimation specification document. This is the chapter's terminal assessment.

### Synthesis

**Exercise 12.5 — Trace the three identification failures.** Show, by working through the spec for Exercise 12.3 or 12.4, how each section preserves protection against one of the three identification failures from Chapter 4 (wrong variables, wrong arrows, wrong conditioning). Be specific: name which section catches which failure and how. If a section catches more than one failure, name that.

### Challenge

**Exercise 12.6 — Audit a published analysis.** Find a recent applied causal-ML paper or technical report (industry blogs at Microsoft, Uber, Netflix, Booking, Meta; or papers in *KDD*, *NeurIPS*, *AAAI*). Reconstruct what the spec *should* have been from what the paper reports. Identify any section the paper skipped. Write a one-page methodological note assessing whether the adjustment-set choice, do-not-add discipline (stated or implied), and estimation method were complete. If complete, say so plainly. If not, name the missing section and the structural consequence.

---

## 13. Specification Checkpoint — Rubric (100 points)

The Specification Checkpoint is the chapter's terminal assessment, scored as follows. Each section is graded for *completeness* (does the section appear and contain the required content) and *structural justification* (does the content reference the DAG, the identification assumptions, and the relevant chapter where the structural rule was derived).

| Section | Points | Criteria |
|---|---|---|
| Treatment and outcome operationalized | 15 | $T$ and $Y$ each named, data-typed, with measurement details. A reviewer can determine, from the spec alone, which rows of data have $T=1$ and which have $Y$ measured. |
| Adjustment set with structural justification | 25 | Every entry carries a one-line structural justification referencing the DAG (which backdoor path it blocks) and the chapter where the structural rule was derived. No entry without justification. |
| Identification assumptions named | 20 | No-unmeasured-confounding (with named unmeasured candidates and bias direction); positivity (with check method); SUTVA (with justification); any estimator-specific assumptions (named explicitly). |
| Do-not-add list with per-variable justification | 25 | Every entry assigned a category (mediator, collider, descendant of $T$, instrument, outcome proxy). Every entry's justification ties to the DAG. Special credit for entries marked with the asterisk indicating tool-default-would-include. |
| Estimation method with assumption check | 15 | Estimator named; assumption named; how the assumption will be checked in the run named. |

A score of 80 or above is the pass threshold. A complete-but-thin spec earns the pass; a thorough spec with explicit handling of edge cases earns the high range. The grader will compare the spec against the linked DAG defense; mismatches between the two cost points proportionally.

---

## 14. LLM exercise

The exercise: get an LLM to draft a spec doc from a DAG, then critique the draft and produce the corrected version. The teaching point is that the LLM cannot enforce identification decisions through the spec without explicit human guidance — and identifying *where* it cannot is part of the discipline.

**Prompt to paste into Claude, ChatGPT, or Gemini:**

> I have a defended causal DAG for a product-analytics question. Treatment T: shown a new homepage layout (binary). Outcome Y: signup completion within 24 hours (binary). 
>
> DAG edges:
> - acquisition_channel → T (different channels were rolled into the test in different waves)
> - acquisition_channel → Y (channels have different baseline signup rates)
> - user_cohort → T (cohort routing)
> - user_cohort → Y (cohort baseline)
> - device → T (rollout schedule)
> - device → Y (device-specific completion rates)
> - T → time_on_homepage (new layout is faster to scan)
> - time_on_homepage → Y (longer time correlates with higher completion)
> - T → clicks_to_signup_button (new layout has the button in a different place)
> - clicks_to_signup_button → Y (more clicks = more chances to complete)
> - intrinsic_motivation → T (an unmeasured user trait that routes via behavioral segmentation)
> - intrinsic_motivation → Y (motivated users complete signup)
>
> The estimand is the ATE.
>
> Produce a complete estimation specification document with the following sections: treatment, outcome, estimand, adjustment set with structural justification per variable, identification assumptions including the unmeasured-confounder analysis, do-not-add list with category per variable, estimation method.

After the LLM responds:

1. Check the *adjustment set*. Did the LLM include `time_on_homepage` or `clicks_to_signup_button`? Either is wrong (both are mediators). Did the LLM include `acquisition_channel`, `user_cohort`, and `device`? Those are the correct entries.
2. Check the *do-not-add list*. Did the LLM categorize `time_on_homepage` and `clicks_to_signup_button` as mediators? Did it name `intrinsic_motivation` as an unmeasured confounder and route it into the identification-assumption section rather than the do-not-add list (since it cannot be added — it is not in the data)?
3. Check the *identification assumptions*. Did the LLM name the unmeasured-motivation bias direction? Did it state the positivity check? Did it state SUTVA?
4. Check the *estimation method*. Did the LLM pick a method, name its assumption, and name the assumption check?
5. Write a one-paragraph note on where the LLM's draft was correct, where it was wrong or missing, and what the consequences of accepting the wrong draft would have been. Submit the note plus the corrected spec as your exercise deliverable.

A note on what to expect: current models (Claude 4 family, GPT-4o and successors, Gemini 1.5/2 family) are usually reliable on adjustment-set composition for small DAGs with clean directionality, less reliable on *justification per variable* (they tend to give category labels without structural justifications), inconsistent on the *do-not-add list* (often produced but may miss instruments or fail to mark tool-default items), and inconsistent on bias-direction analysis for unmeasured confounders — the most useful place for the analyst to verify by hand. `[verify-current-LLM-behavior]`

---

## 15. AI Use Disclosure

This chapter was drafted with assistance from Claude (Anthropic), using the Feynman-voice scaffold in the workshop's CLAUDE.md and Chapter 12 pantry notes. The Team Onboarding opening case is a structurally accurate composite drawn from the documented "tool default silently overrides spec" pattern and from publicly visible py-why GitHub issue-tracker patterns; no specific company is identified because publicly named post-mortems for this failure mode are rare. Citations flagged `[verify]` are pending Nik's review. The LLM exercise in §14 was prototyped against Claude (version family 4); the qualitative description of where current models succeed and fail reflects that testing.

---

## 16. Key terms

- **Estimation specification document ("spec doc," "the spec").** A written, separable artifact that names every input a causal-inference tool needs and every decision the tool must not make autonomously. Eleven canonical sections. (Sections 2, 8, 9.)
- **Do-not-add list.** The spec section that names variables the tool must not include in the adjustment set, with a category and structural justification per entry. The list is positive exclusion, not omission. (Sections 2, 5.)
- **Handoff (the).** The structural transition from identification (the work of Acts One and Two) to estimation (the work of Act Three). The spec doc is the contract that constrains the handoff. (Sections 1, 7.)
- **Tool default.** A behavior the causal-inference library exhibits when an argument is not specified. Common dangerous defaults: automatic covariate inclusion, propensity-score variable selection by predictive accuracy, default model class, silent handling of missing data and positivity violations. (Section 4.)
- **Identification precedes estimation.** The architectural commitment that the structural work of Acts One and Two must be done before the statistical work of Act Three, and that the spec doc is the artifact that imposes the structural work's commitments on the statistical work. (Section 7.)
- **Positive exclusion vs. omission.** A variable's *positive exclusion* in the spec is a structural claim (this variable should not be in the adjustment set, because…); a variable's *omission* from the adjustment-set list is silent. Tools with auto-inclusion defaults can close the omission gap; only positive exclusion plus pipeline enforcement closes the structural gap. (Section 5.)
- **Refutation checks.** Diagnostic runs that test whether the estimate is structurally robust — placebo treatment, random common cause, subset robustness, dummy outcome. DoWhy exposes these as first-class API calls. (Sections 2, 11.)

---

## 17. Further reading

- Amit Sharma and Emre Kıcıman, "DoWhy: An End-to-End Library for Causal Inference," *arXiv:2011.04216* (2020). The design paper. https://arxiv.org/abs/2011.04216
- Keith Battocchi et al., *EconML: A Python Package for ML-Based Heterogeneous Treatment Effects Estimation* (2019+). https://github.com/py-why/EconML Read the README and the `LinearDML` tutorial.
- Uber Engineering, [*CausalML* repository](https://github.com/uber/causalml). Complements EconML on the meta-learner side.
- Tyler J. VanderWeele, "Principles of Confounder Selection," *European Journal of Epidemiology* 34(3), 211–219 (2019). `[verify-pagination]` https://doi.org/10.1007/s10654-019-00494-6 The clearest practical statement of confounder-selection principles.
- Judea Pearl, "On a Class of Bias-Amplifying Variables," *UAI* (2010). https://ftp.cs.ucla.edu/pub/stat_ser/r356.pdf `[verify-URL]`
- Stephen R. Cole et al., "Illustrating Bias Due to Conditioning on a Collider," *IJE* 39(2), 417–420 (2010). `[verify-pagination]` https://doi.org/10.1093/ije/dyp334
- Victor Chernozhukov et al., "Double/Debiased Machine Learning," *Econometrics Journal* 21(1), C1–C68 (2018). https://doi.org/10.1111/ectj.12097
- Chernozhukov, Hansen, Kallus, Spindler, Syrgkanis, *Applied Causal Inference Powered by ML and AI* (2026, online ed.). https://causalml-book.org/
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (Chapman and Hall / CRC, 2020). Chapters 11–13. Freely available.
- Kıcıman, Ness, Sharma, Tan, "Causal Reasoning and Large Language Models," *arXiv:2305.00050* (2023+). https://arxiv.org/abs/2305.00050 `[verify-current-version]`

---

## 18. Draft flags

The following items in this chapter were flagged for verification during drafting and remain pending Nik's review:

- The opening "Team Onboarding" case is a structurally accurate composite. The publicly named post-mortems for this exact failure mode (tool default silently overrides spec) are rare; the [py-why issue tracker](https://github.com/py-why/dowhy/issues) contains the recurring user-report pattern that motivates the composite, but specific issue references `[verify-specific-issues]`.
- Library default behavior descriptions reflect DoWhy / EconML / CausalML as of early 2026; specific defaults aged by version. The chapter directs the student to verify current defaults at run time `[verify-current-dowhy-default]`.
- Pearl 2010 UAI URL — hosted PDF at UCLA `[verify-URL]`; canonical proceedings access elsewhere.
- VanderWeele 2019 *European Journal of Epidemiology* — provisional pagination 34(3), 211–219 `[verify-pagination]`.
- Cole, Platt, Schisterman et al. 2010 *International Journal of Epidemiology* — provisional pagination 39(2), 417–420 `[verify-pagination]`.
- Kıcıman, Ness, Sharma, Tan 2023 — paper has been updated multiple times; current canonical citation `[verify-current-version]`.
- Sharma & Kıcıman DoWhy paper — chapter cites the 2020 arXiv version; a more recent journal/proceedings version may exist `[verify-current-canonical]`.
- LLM-assisted causal-tooling references in Section 7 are evolving; current tool integrations `[verify-current-LLM-causal-tooling]`.
- LLM behavior description in Section 14 reflects mid-2026 chatbot families; expect drift `[verify-current-LLM-behavior]`.
- The eleven-section spec template is a textbook contribution; no canonical literature reference exists for the precise form. The chapter takes ownership of this format honestly.

---

## What would change my mind

If a causal-inference tool emerges that ingests a DAG (in a standard exchange format), reads off the adjustment set, infers the do-not-add list from the DAG structure, and refuses to estimate when the analyst's code includes unauthorized variables — and if that tool becomes the dominant production stack rather than the optional add-on — then the spec-doc-as-separate-artifact framing in this chapter would compress. The spec would still exist conceptually; it would live inside the tool rather than in a separate markdown file. The discipline would not change. The artifact's location would.

## Still puzzling

I do not yet have a clean account of how to write the spec for an analysis whose DAG is *partially* defended — where the analyst is confident about some arrows and uncertain about others. The honest move is to write the uncertainty into the identification-assumptions section with bias-direction analysis under each possible DAG version. The practical move I see most often is to pick the most-defensible DAG and not propagate the uncertainty. The gap between the honest and the practical is the place I am still working on, chapter by chapter.

---

**Tags:** estimation-specification, do-not-add-list, DoWhy, EconML, identification-handoff
