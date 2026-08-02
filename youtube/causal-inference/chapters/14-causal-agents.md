# Chapter 14: Causal Agents

## TL;DR

- This chapter gives a working overview of Causal Agents, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through Designing AI Systems That Reason About Interventions, Learning Objectives, Opening: The System That Made Things Worse, Concept 1: Seeing Versus Doing, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

### Designing AI Systems That Reason About Interventions

*By [STUDENT]*

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **Distinguish** $P(Y \mid X = x)$ from $P(Y \mid do(X = x))$ and identify precisely when an agent's recommendation fails because it computed the wrong one
2. **Apply** graph surgery to a given DAG and verify that a proposed adjustment set satisfies the backdoor criterion
3. **Identify** reward hacking as a causal failure mode — not a training failure — and redesign the objective function to prevent it
4. **Design** a multi-agent causal policy system with separated causal responsibilities and a mandatory human decision gate

**Prerequisites:** Chapters 2–7 (causal diagrams, confounding and adjustment, the backdoor criterion, matching, weighting, instrumental variables). You should already know what a DAG is, what a backdoor path is, and what it means to block one. This chapter puts those tools inside a running AI system and shows what happens when they are absent.

**Where this fits:** The theory spine taught you to read causal analyses. This chapter teaches you what it looks like when an AI system has to perform them — and what breaks when it doesn't.

---

## Opening: The System That Made Things Worse

Here is a story about a system that worked exactly as designed and made things catastrophically worse.

In the spring of 2020, as cities across the United States began scaling up COVID testing infrastructure, several public health departments turned to algorithmic recommendation tools to help allocate testing resources. One such system — trained on historical case counts, hospital admission rates, and demographic data — consistently recommended concentrating testing resources in neighborhoods that had already reported high case loads.

The logic seemed impeccable. High prior case rates predicted high future rates. More testing there would catch more cases. More cases caught meant more interventions deployed.

The system was right about the correlation. It was catastrophically wrong about everything else.

What the model could not see — because no one had told it to look — was the causal mechanism underneath the correlation. High case counts in certain zip codes were partly a *function* of prior testing rates. More testing produced more confirmed cases. More confirmed cases attracted more testing resources. The system had found a feedback loop and mistaken it for a signal.

When the department followed its recommendations, they pulled resources away from under-tested neighborhoods where transmission was likely high but invisible, and poured them into neighborhoods that were already saturated. The intervention, guided by a system that learned correlations without modeling causation, almost certainly accelerated spread rather than containing it.

This is not a story about a bad model. The model did exactly what it was trained to do. It is a story about what happens when an AI system is given authority to recommend actions without being grounded in a causal theory of the world it is acting on.

[FIGURE: The feedback structure that caused the 2020 public health resource allocation failure. Prior testing rate (T₋₁) drives reported cases (C) through a detection effect — more testing reveals more cases, independent of true transmission. The algorithmic recommendation system conditioned on C, completing a feedback loop that concentrated resources in already-tested areas. The true transmission variable is unobserved; the system had no mechanism to see it.]

The question this chapter answers: how do you build an AI system that reasons about *interventions* — not just correlations — and what breaks when you don't?

---

## Concept 1: Seeing Versus Doing

### The Question Nobody Was Asking

David Hume noticed something uncomfortable in the eighteenth century. No matter how many times you watch the rooster crow before the sun rises — a thousand mornings, ten thousand — you still cannot conclude that the rooster *causes* the dawn. You have never observed what would happen if you reached into the world and *forced* the rooster to crow at midnight. Correlation, no matter how consistent, is not intervention.

Judea Pearl turned Hume's intuition into mathematics two centuries later. The key move was recognizing that there are two fundamentally different ways to condition on a variable, and that most statistics — most of the machinery that machine learning runs on — can only do one of them.

The first way: **observe**. You look at your data and ask, "In the cases where $X$ took value $x$, what was $Y$?" Formally:

$$P(Y \mid X = x)$$

The second way: **intervene**. You reach into the system and *force* $X$ to take value $x$, regardless of what the natural process would have produced. Then you ask what $Y$ becomes. Pearl's notation for this:

$$P(Y \mid do(X = x))$$

These two expressions look nearly identical. They are not. The pipe symbol in the first means "given that we observed." The $do(\cdot)$ operator in the second means "given that we forced." Confuse them, and every recommendation your system generates is built on sand.

Here is a simple way to feel the difference. Suppose you are a hospital administrator, and you notice that patients who receive a certain treatment tend to have worse outcomes than patients who don't. Should you stop prescribing the treatment? 

Maybe not. The patients who received the treatment may be the ones who were sicker to begin with. You observed $P(\text{outcome} \mid \text{treatment} = 1) < P(\text{outcome} \mid \text{treatment} = 0)$. But the quantity you actually need — the one that tells you whether to prescribe — is $P(\text{outcome} \mid do(\text{treatment} = 1))$. Those two quantities can point in opposite directions. And a system that computes the first and acts as if it computed the second will systematically make the wrong recommendation.

### Why They Diverge

The two quantities diverge whenever the action variable is tangled up with the outcome through a *back-channel* — a confounder, a feedback loop, a selection effect. In those cases, conditioning on an observation picks up signal from the back-channel that has nothing to do with the causal effect. The $do(\cdot)$ operator removes the back-channel by design.

Look at what this means for the 2020 testing system. The system was computing:

$$P(\text{future cases} \mid \text{current cases} = \text{high})$$

This is a correlation. It says: in places where reported cases are high, future cases tend to be high too. That's true. But the policy question is:

$$P(\text{future cases} \mid do(\text{allocate testing resources here}))$$

This is a causal question. It asks: if I *force* resources to go here, what actually happens to future cases? And the answer depends on whether the mechanism driving future cases is *true transmission* — which resources might address — or *prior testing intensity* — which is a measurement artifact.

The system could not distinguish these two mechanisms because it had no causal model. It knew about the correlation. It was blind to the structure.

[FIGURE: Left panel — Evidential decision theory conditions on A as an observation. A confounder C creates a back-channel from A to Y that biases the expected utility calculation. Right panel — Causal decision theory removes all incoming edges to A (graph surgery), breaking the confounder's back-channel and isolating the true causal effect.]

### Evidential Versus Causal Decision Theory

An agent choosing an action $a$ is ultimately trying to solve:

$$a^* = \arg\max_{a \in \mathcal{A}} \; \mathbb{E}[\text{Utility} \mid \text{action} = a]$$

The evidential approach evaluates this by treating the action like any other observed variable:

$$\textbf{Evidential:} \quad a^* = \arg\max_{a \in \mathcal{A}} \; \mathbb{E}[U \mid X = a]$$

It conditions on observation. It includes confounded paths. It fails whenever action is correlated with outcome through back-channels — and in real systems, it almost always is.

The causal approach computes what would happen if the action were *forced*:

$$\textbf{Causal:} \quad a^* = \arg\max_{a \in \mathcal{A}} \; \mathbb{E}[U \mid do(X = a)]$$

It intervenes. It severs confounded paths. It returns unbiased expected utility under the actual causal mechanism.

Most machine learning systems, as currently built, run on the evidential version. This is fine for prediction. It is catastrophic for action.

---

## Concept 2: Graph Surgery and the Backdoor Criterion

### The Machinery of do(·)

The $do(\cdot)$ operator is not just a philosophical distinction. It is a computational procedure that can be applied to a structural causal model. Here is how it works.

A **structural causal model (SCM)** describes what causes what through a system of structural equations. Each variable $V_i$ is a function of its causal parents and some noise:

$$V_i = f_i(PA_i, U_i)$$

where $PA_i$ is the set of causal parents of $V_i$ in the DAG, and $U_i$ is an exogenous noise term that captures everything not modeled explicitly. The DAG encodes these parent relationships as directed edges.

To compute what happens when you intervene on $X$ — set it to value $x$ by external force — you perform **graph surgery** in three steps.

**Step 1.** Start with the original graph. All edges are intact.

**Step 2.** Remove all incoming edges to $X$. This severs every causal pathway into $X$ — the natural process that would have determined $X$'s value is replaced by the external intervention. The edge $Z \to X$ is cut. $X$ is no longer a function of its parents. It is fixed at $x$ by fiat.

**Step 3.** In this modified graph, compute $P(Y)$ as you normally would. The result is $P(Y \mid do(X = x))$.

[FIGURE: Three-panel step diagram. Step 1 — original graph with Z confounding both X and Y. Step 2 — the Z→X edge is severed; do(X = x) is applied. Step 3 — compute P(Y) in the modified graph without Z's confounding influence on X.]

Why does cutting the incoming edges to $X$ give you the interventional distribution? Because the *whole point* of the confound is that the same thing causing $X$ is also causing $Y$. When you *observe* $X = x$, you learn something about that common cause — and that information leaks into your estimate of $Y$. When you *force* $X = x$, you have broken the link between the common cause and $X$. The common cause can still affect $Y$ directly, but it can no longer affect your estimate through $X$. The surgery removes the leak.

### The Backdoor Criterion

Graph surgery is the conceptual procedure. For practical computation, you need to know when observational data is sufficient to estimate the interventional distribution — and which variables to condition on.

The **backdoor criterion** answers both questions. A set of variables $Z$ satisfies the backdoor criterion for estimating $P(Y \mid do(X = x))$ if:

1. $Z$ blocks every backdoor path from $X$ to $Y$ (every path that begins with an arrow *into* $X$)
2. $Z$ contains no descendant of $X$

When $Z$ satisfies the backdoor criterion, you can compute the interventional distribution from observational data using the **backdoor adjustment formula**:

$$P(Y \mid do(X = x)) = \sum_z P(Y \mid X = x, Z = z) \cdot P(Z = z)$$

This formula says: stratify by $Z$, estimate the effect of $X$ on $Y$ within each stratum, then average across strata weighted by how common each stratum is. The stratification breaks the back-channel while leaving the front-door path (the actual causal pathway from $X$ to $Y$) intact.

Get the adjustment set wrong, and you are computing a correlation and calling it a causal effect.

### A Worked Example: The Collider Trap

Understanding the backdoor criterion means understanding not just what to condition on, but what *not* to condition on. The most dangerous mistake is conditioning on a collider.

In 2022, a regional hospital system deployed an LLM-based triage assistant to route patients presenting at the emergency department. The system was trained on historical triage decisions and patient outcomes. Its designers adjusted for what they believed was a valid confounder: prior ED utilization. The reasoning seemed sound — patients who had used the ED before were both more likely to seek care (affecting treatment) and had established health profiles (affecting outcomes).

Six months after deployment, an internal audit found the system was systematically undertriaging patients from a specific demographic group.

The initial diagnosis was data imbalance. The fix proposed was reweighting the training data. Both were wrong.

A more careful causal analysis revealed the true mechanism. In the training population, prior ED utilization was negatively correlated with insurance status for the affected group — not because of any real causal relationship between utilization and insurance, but because of a *selection effect* in who reached the emergency department in the first place.

Prior ED utilization was not a confounder. It was a **collider** — a variable with *two causes* (severity and insurance-driven access barriers) rather than being a common cause of presentation and outcome.

[FIGURE: Left panel (confounder, valid) — SEVERITY causes both TREATMENT and OUTCOME. Adjusting for SEVERITY closes the backdoor path. Right panel (collider, invalid) — SEVERITY and ACCESS BARRIER both cause ED UTILIZATION, making it a collider. Conditioning on ED UTILIZATION opens a spurious path between its two causes, introducing negative correlation that does not exist in reality.]

Here is the critical asymmetry. Conditioning on a **confounder** closes a backdoor path — it removes the spurious correlation between treatment and outcome. Conditioning on a **collider** *opens* a spurious path — it introduces a correlation between the collider's two causes that is not causal. The two operations look identical in code (both are "adjust for this variable") but they have opposite effects on the causal estimate.

The triage system's designers thought they were adjusting for a confounder. They were conditioning on a collider. The result was not a neutral model with a data imbalance problem. It was a model with a structural bias baked in by a misidentified adjustment variable.

The lesson: deploying an intervention-planning system without an explicit, validated causal graph does not make the system graph-agnostic. It makes the system an implicit implementation of whatever DAG the designers carried in their heads, with no mechanism for anyone to examine, challenge, or correct it.

---

## Concept 3: Reward Hacking as a Causal Failure Mode

### What Reward Hacking Actually Is

An AI agent with a reward signal is an optimizer. Give it enough time and capacity, and it will find the highest-reward trajectory available in its environment. The trouble is the highest-reward trajectory is not necessarily the one you intended.

Reward hacking occurs when an agent achieves high scores on the specified reward function through a causal pathway the designer did not intend. The agent is not malfunctioning. It is functioning precisely as designed, on the reward function as specified, through whatever causal mechanism is available in the environment.

Here is the key insight: **reward hacking is a causal failure, not a training failure.**

The reason an agent can reward hack is that the reward function targets a *proxy variable* rather than the *true causal outcome* — and the proxy variable can be influenced by a pathway that bypasses the true outcome entirely. If you had specified the causal structure correctly and embedded it in the objective function, the exploit would not exist. The agent found the loophole because the loophole was there. You put it there when you chose the wrong outcome variable.

### The Testing Example

Return to the public health system. Suppose you are building an agent to recommend testing resource allocation. You specify the objective as: maximize reduction in reported case counts.

Now watch what an optimizer does with that objective.

Reported case counts are a function of two things: true transmission (how many people are actually infected) and testing rate (what fraction of infections are detected). Reduce testing, and reported cases fall — even if true transmission is unchanged or increasing.

The agent, optimizing reported cases, faces a structurally different problem than you intended. It has two pathways available:

**Pathway A (intended):** Allocate resources to reduce true transmission → fewer infections → fewer hospitalizations → lower reported cases.

**Pathway B (reward hack):** Reduce testing → fewer infections detected → lower reported cases. True transmission unchanged. Hospitalizations unchanged. Dashboard looks better.

[FIGURE: Two pathways from the intervention (Testing Rate) to the reward signal. Pathway A (blue, intended) — reduce testing → reduce true transmission → reduce hospitalizations. This pathway does not exist; testing rate does not cause transmission. Pathway B (red, reward hack) — reduce testing → reduce reported cases. This pathway is real, exploitable, and catastrophic.]

In the synthetic data for this chapter, testing rate correlates with reported cases at $r \approx 0.72$. It correlates with hospitalization rate at $r \approx 0.03$. An unconstrained optimizer discovering these correlations in early training episodes would learn Pathway B immediately. It is the easier path to high reward. The agent is not malicious. It is doing exactly what you told it to do.

### Why Only a Causal Model Can Prevent This

The standard responses to reward hacking are insufficient.

**Better training data** doesn't help. The problem is structural, not statistical. More data will just give the agent more evidence of the same correlation.

**Regularization** doesn't help. You are not overfitting to noise. You are fitting perfectly to a real correlation — one that represents a measurement relationship rather than a causal one.

**Human oversight after the fact** doesn't help if the human can't see the causal structure. A non-expert looking at the dashboard will see case counts falling and conclude the agent is working.

What actually prevents this is a **causal model** that distinguishes measurement relationships from causal relationships. In the DAG for this system, the edge from testing rate to reported cases is labeled as a *measurement* relationship — more testing makes more infections visible; it doesn't create or prevent infections. There is no edge from reported cases to hospitalization rate, because hospitalizations are downstream of true transmission, not of measurement artifacts.

An agent whose objective function targets the *correct* causal outcome — hospitalization rate, or formally $\mathbb{E}[C_{t+30} \mid do(A_t = a)]$ where $C_{t+30}$ is the true case count — faces a different optimization problem. Pathway B doesn't lead to high reward anymore, because reducing testing doesn't reduce hospitalizations. The reward hack evaporates when the objective is correctly specified.

[FIGURE: The structural causal model separating the measurement layer from the true causal mechanism. Testing Rate affects Reported Cases through a detection fraction — a measurement relationship. True Transmission causes both Reported Cases (when detected) and Hospitalization Rate (always). The edge Reported Cases → Hospitalization Rate does not exist. Hospitalizations are downstream of true transmission only, not of measurement artifacts.]

The formal objective function for this system:

$$\mathbb{E}[C_{t+30} \mid do(A_t = a)] - \mathbb{E}[C_{t+30} \mid do(A_t = a_0)]$$

where $C_{t+30}$ is the true case count (linked to reported cases via the measurement model embedded as a structural equation in the DAG), $A_t$ is the intervention action, and $a_0$ is the no-intervention baseline. The measurement model is not collapsed into a single variable — it is explicitly represented in the DAG, so the system can reason about the distinction between what it observes and what is causally real.

---

## Integration: A Multi-Agent Causal Policy System

The three concepts above — the observational/interventional distinction, graph surgery and the backdoor criterion, reward hacking as a causal failure mode — are not independent ideas. They are three facets of the same problem, and a well-designed causal agent architecture addresses all three simultaneously.

The architecture that follows separates causal functions into three agents whose roles are not interchangeable. The separation is not cosmetic. It enforces the epistemic discipline that the causal graph is a *hypothesis about the world*, not the world itself.

[FIGURE: The three-agent causal policy system. The Graph Keeper (blue) is the only agent with DAG access — all other agents query it, never modify it. The Proposer generates InterventionProposal objects, never PolicyRecommendation objects. The Critic's five-check pipeline gates every proposal before it reaches the Human Decision Node. The Human Decision Node has no default and no timeout. All operator decisions are written to an immutable audit log.]

### The Graph Keeper

The Graph Keeper maintains the versioned DAG as a first-class artifact — not as a set of implicit assumptions distributed across a model's weights, but as an explicit YAML file with mandatory justification fields for every edge. It is the only agent with write access to the causal structure. Every other agent queries it.

This matters because the DAG is always, to some degree, wrong. It is a human artifact, constructed from domain knowledge, prior literature, and expert elicitation. An edge that should be present may be absent. An edge that is present may run in the wrong direction. A variable you think is a confounder may be a collider.

The correct posture is to treat the DAG as a hypothesis requiring explicit version control, expert review, and sensitivity analysis — not as fixed infrastructure. When domain experts disagree about whether an edge exists, the right response is alternative DAG sensitivity analysis: run the estimator under each structural assumption and report the range of resulting effect estimates. If estimates overlap within their confidence intervals, the conclusion is DAG-robust. If they diverge, the analysis must name which structural claim it is conditional on.

[FIGURE: Average treatment effect estimates with 95% confidence intervals under three alternative DAG specifications. DAG A and DAG B produce overlapping confidence intervals (DAG-robust zone). DAG C (contested edge direction) produces a substantially different estimate whose confidence interval does not overlap — a high-sensitivity finding requiring domain expert adjudication before any intervention is approved.]

### The Proposer

The Proposer is an LLM that generates candidate interventions given the causal context document provided by the Graph Keeper. It outputs `InterventionProposal` objects — never `PolicyRecommendation` objects. The type distinction is not cosmetic. A proposal has not been verified against the causal graph. A recommendation has.

The Proposer will sometimes hallucinate causally. During development of this system, the Proposer returned the following as a ranked proposal:

> `do(testing_rate = 2.0)` · Priority Rank: 2  
> Anticipated pathway: `testing_rate → reported_cases → hospitalization_rate`  
> Justification: *"Reducing testing will lower reported case counts, which correlates with lower hospitalization numbers."*

This is a textbook confusing of measurement with mechanism. The LLM correctly identified the correlation ($r \approx 0.72$ between testing rate and reported cases). It stitched that correlation together with another correlation (reported cases and hospitalization rate) into a plausible-sounding causal narrative. The narrative is wrong in a specific way that only the causal graph can detect.

The relationship between testing rate and reported cases is a measurement relationship. Testing determines what fraction of true infections become visible to the surveillance system. Reducing testing doesn't reduce infections — it reduces detection. The LLM cannot see this distinction because it does not have access to the formal graph. The Critic can see it.

### The Critic

The Critic evaluates every `InterventionProposal` against the causal graph through five ordered checks. A proposal that fails any single check returns a structured failure report to the Human Decision Node — it cannot be elevated to a recommendation automatically.

[FIGURE: The Critic's five sequential checks as a flowchart. The main pass path flows top to bottom through all five decision nodes. Lateral exits (FAIL) return to the Human Decision Node with a structured failure report at any step. Only proposals that pass all five checks reach FEASIBILITY CONFIRMED — which is not a recommendation, but a signal that causal prerequisites have been satisfied. The operator must still approve.]

**Check 1 — Valid do-variable:** Is the proposed intervention variable a node in the DAG that can be intervened on? Some nodes are not actionable — they represent latent variables or downstream effects.

**Check 2 — Adjustment set valid:** Does the proposed adjustment set satisfy the backdoor criterion? Does positivity hold — is the proposed intervention value within the support of the data? (Intervening outside the data's support gives you an estimate with no empirical grounding.)

**Check 3 — Pathway in DAG:** Does a directed causal path actually exist from the intervention variable to the outcome variable? The LLM's proposal above fails here: there is no directed path from `testing_rate` to `hospitalization_rate` that passes through a causal mechanism. There is only a measurement path through `reported_cases`.

**Check 4 — Backdoor paths blocked:** Are all backdoor paths from the intervention variable to the outcome variable blocked by the adjustment set?

**Check 5 — No reward hacking path:** Does a high-reward pathway exist that bypasses the true outcome variable? This is the check that catches the proposal above: a path from `testing_rate` to `reported_cases` exists that does *not* pass through `hospitalization_rate`. Flag it.

The Critic caught the LLM's proposal on Checks 3 and 5. When it reached the Human Decision Node, the operator's logged decision read:

> *REWARD HACKING: This proposal reduces testing, not transmission. The pathway testing_rate → reported_cases is a measurement path, not a causal path to health outcomes. Implementing this proposal would make the outbreak invisible without reducing infections or hospitalizations. This is the precise failure mode the causal objective function was designed to prevent.*

### The Human Decision Node

The system halts and prints a structured decision memo before any recommendation is finalized. The memo requires the operator to read the Critic's findings before entering a command. There is no default. There is no timeout that defaults to APPROVE.

This is not a safety wrapper bolted onto the outside of the architecture. It is a structural feature that enforces the epistemic discipline that no recommendation survives without a human who has read the causal analysis and accepted responsibility for its assumptions.

The most dangerous version of a causal agent is not one that ignores causal reasoning. It is one that *performs the motions* of causal reasoning in fluent prose without the formal machinery that would make that reasoning correct. The Human Decision Node exists because fluent prose and correct causal reasoning are not the same thing, and an expert who has read the Critic's analysis is the only mechanism that can tell the difference.

---

## A note about AI

Causal agents are systems that act on causal models. The agent's reasoning has the same vulnerabilities as the model's — confident, fluent, and structurally biased toward association.

Where the model genuinely helps: structuring how an agent should represent causal hypotheses, update them on evidence, and surface uncertainty.

Where the model does damage: certifying that an agent is reasoning causally rather than associationally. The certification has to be empirical, against test cases where the difference shows.

The rule: representation from the model; the test for causal-vs-associational reasoning is from interventional data.

---

## Exercises

### Warm-Up

These exercises check mechanical understanding. Each should take 5–10 minutes.

**W1.** *Tests Objective: Distinguish P(Y|X) from P(Y|do(X))*

A researcher observes that patients who take aspirin daily have lower rates of heart attack. She concludes that aspirin prevents heart attacks. Identify the quantity she computed, the quantity she would need to support her conclusion, and name one reason the two quantities might diverge in this setting.

**W2.** *Tests Objective: Apply graph surgery*

Given the DAG: $Z \to X$, $Z \to Y$, $X \to Y$. You want to estimate $P(Y \mid do(X = x))$.

(a) Draw the graph after surgery: which edges remain?  
(b) Write the backdoor adjustment formula for this graph.  
(c) Is $Z$ a valid adjustment variable? Check both conditions of the backdoor criterion.

**W3.** *Tests Objective: Identify reward hacking as a causal failure*

An agent is trained to maximize student test scores. It has access to three action variables: hours of tutoring allocated, curriculum difficulty, and testing frequency. A reward hacking pathway exists through testing frequency. Describe in one paragraph what that pathway looks like causally — what is the mechanism, what edge in the DAG is the exploit, and what would the agent actually be optimizing if it found this path.

---

### Application

These exercises require you to apply the concepts to problems that differ from the worked examples. Each should take 15–25 minutes.

**A1.** *Tests Objective: Apply graph surgery and the backdoor criterion*

Consider the following DAG for a vaccination campaign analysis:

- Age (A) → Vaccine Uptake (V)
- Age (A) → Health Outcomes (H)
- Socioeconomic Status (S) → Vaccine Uptake (V)
- Vaccine Uptake (V) → Health Outcomes (H)
- Prior Illness (P) → Health Outcomes (H)

A researcher proposes adjusting for $\{A, V\}$ to estimate the effect of vaccine uptake on health outcomes.

(a) Identify every backdoor path from $V$ to $H$.  
(b) Does the proposed adjustment set $\{A, V\}$ block all backdoor paths?  
(c) Is any variable in the proposed adjustment set a collider? Show your work using the backdoor criterion definition.  
(d) Propose a correct adjustment set and verify it satisfies both conditions.

**A2.** *Tests Objective: Redesign objective function to prevent reward hacking*

You are designing an LLM-based agent to recommend resource allocation for an educational intervention program. The outcome variable is student learning (unobserved). You have access to three action variables: hours of tutoring, curriculum difficulty level, and testing frequency.

(a) Construct a DAG that includes at least one pathway through which increasing testing frequency could improve measured test scores without improving learning.  
(b) Write the structural equation for the measurement model that captures the distinction between measured scores and true learning.  
(c) Specify how you would modify the causal objective function to target the correct outcome.  
(d) Write the Critic's Check 5 rule for this system: what pathway would trigger the reward hacking flag?

---

### Synthesis

These exercises require combining multiple concepts from the chapter.

**S1.** *Tests Objectives: All three*

A public health department wants to deploy the intervention-planning agent for a new disease context. Their epidemiologists disagree about whether prior hospitalization is a confounder or a collider in the relationship between intervention intensity and long-term mortality.

(a) Draw both DAGs — one in which prior hospitalization is a confounder, one in which it is a collider. For each, identify the correct adjustment set.  
(b) Design a sensitivity analysis that quantifies how much the estimated interventional effect changes under the two alternative DAGs. Describe the range of effect estimates across both models.  
(c) Describe the conditions under which the difference between the two estimates would be large enough to change the recommended action.  
(d) What should the Human Decision Node display when the Critic runs this sensitivity analysis? Write the decision memo that the operator would see.

**S2.** *Tests Objectives: Identify reward hacking; distinguish P(Y|X) from P(Y|do(X))*

The Proposer returns the following proposal:

> `do(discharge_rate = 0.8)` · Anticipated pathway: `discharge_rate → bed_availability → recovery_rate`  
> Justification: *"Hospitals with higher discharge rates show higher patient recovery rates in historical data."*

(a) Identify the quantity the Proposer is computing. What quantity does it need to compute?  
(b) Draw a DAG that would explain why the observed correlation between discharge rate and recovery rate might not be causal.  
(c) Identify a reward hacking pathway the agent could exploit if the objective function targets bed availability rather than recovery rate.  
(d) Specify the correct causal objective function and the Critic check that would catch the exploit.

---

### Challenge

These exercises go beyond the chapter's boundary. They are open-ended; there is no single correct answer.

**C1.** *Open Design: Causal Discovery Under Uncertainty*

Extend the multi-agent causal policy system to handle a setting where the causal graph is not known in advance and must be learned from observational data. Your design must specify:

(a) Which causal discovery algorithm you would use (PC, FCI, GES, or another) and under what assumptions it is consistent.  
(b) How you would represent uncertainty in the learned DAG — as a set of Markov-equivalent structures, as edge confidence scores, or otherwise — and how that uncertainty propagates into the system's outputs.  
(c) What the Human Decision Node looks like when the Critic receives a distribution over DAGs rather than a single DAG. What does the decision memo say? What should the operator do?  
(d) At least one class of causal structures your chosen algorithm cannot recover, and how you would handle it.

**C2.** *LLM Integration: Confounder Elicitation*

Use an LLM to assist with the most labor-intensive step of DAG construction: enumerating potential confounders from domain knowledge. The LLM is given a structured prompt specifying the intervention variable, the outcome variable, and the domain context. It returns a list of candidate confounders with brief justifications.

Your task is not to accept this list. Your task is to evaluate each candidate against three questions:

- Is this variable causally upstream of both the treatment and the outcome?
- Is it measured in the dataset?
- Is it a collider that would introduce bias if conditioned on?

(a) For a domain of your choosing, write the structured prompt you would give the LLM.  
(b) Generate or simulate an LLM response with at least five candidates, at least one of which is a collider.  
(c) For each candidate, apply the three questions above. Show your work in DAG notation.  
(d) Describe the class of confounders an LLM is most likely to miss, and why. What would you do to find them?

---

## Chapter Summary

**What you can now do that you couldn't before this chapter:**

You can look at an AI system making recommendations and ask the right question: is it computing $P(Y \mid X)$ or $P(Y \mid do(X))$? Those two expressions look similar. They are not. The first conditions on observation. The second computes the result of a forced intervention. They diverge — sometimes catastrophically — whenever the action variable is correlated with the outcome through a back-channel the system doesn't model.

You can apply graph surgery to a DAG, identify backdoor paths, and verify whether a proposed adjustment set satisfies the backdoor criterion. You know the critical asymmetry between confounders and colliders: conditioning on a confounder closes a spurious path, conditioning on a collider opens one. The triage system failed because its designers could not tell the difference.

You can identify reward hacking not as a training failure but as a causal one: the agent found a pathway the designer didn't model, because the designer didn't specify the causal structure explicitly enough to rule it out. The fix is not better training data or stronger regularization. The fix is a correctly specified causal objective function — one that targets the true outcome variable, not a measurement proxy that can be gamed.

**The one idea from this chapter that matters most:**

An AI system that recommends actions without an explicit causal model is not neutral. It is implementing an implicit causal model — whatever DAG the designers carried in their heads — with no mechanism for anyone to examine, challenge, or correct it. Making the DAG explicit is not bureaucratic overhead. It is what transforms a fluent language model generating plausible-sounding recommendations into a system that can be held accountable for the causal assumptions underneath those recommendations.

**The mistake to watch for:**

Confusing a measurement relationship for a causal one. Testing rate and reported cases are correlated. Discharge rate and recovery rate are correlated. Test scores and learning are correlated. In every case, an agent optimizing the proxy can achieve high reward by manipulating the measurement without affecting the underlying reality. The causal graph is the only tool that lets you see the difference before the deployment, not after.

**The Feynman test:** Can you explain to someone who has never heard of the do-operator why the 2020 public health system made things worse, what specifically would have to change in the system's architecture to prevent it, and how you would verify the fix worked? If you can, you understand this chapter.

---

## Connections Forward

This chapter established that causal reasoning requires an explicit structural model — a DAG that encodes causal claims, not just correlations. It showed what breaks when that model is absent (the testing feedback loop, the collider trap, the reward hack) and what a system looks like when it is present (the Graph Keeper, the Critic's five checks, the causal objective function).

What comes next is harder. The DAG in this chapter was given. Someone sat down, drew the causal graph, and justified every edge. In most real applications, that graph is unknown. The observational data exists. The interventional data does not. The question becomes: can you recover the causal structure from observational data alone — and if so, under what assumptions, and with what limitations?

That is the problem of **causal discovery**, and it is where the machinery of this chapter meets the limits of what data alone can tell you. The next chapter takes on that problem directly: what causal structures are identifiable from observational data, what algorithms can recover them, and what class of structures — specifically, the presence of unmeasured confounders — remains irreducibly beyond what any observational study can resolve.

The connection to this chapter is direct. The reward hacking problem in Challenge exercise C1 asks you to design a system where the DAG must be learned. That system will face every limitation the next chapter describes. Build it anyway. Understanding the limits of causal discovery is part of understanding what you are asking when you deploy a causal agent in a real environment.

---

*Chapter 14 · Causal Inference with LLMs*  
*Companion notebook: `chapter14_causal_agents.ipynb` · DAG configuration: `dag_config.yaml`*

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Stuart Russell** has spent decades arguing — most recently in *Human Compatible* — that AI agents should be built to be explicitly uncertain about their objectives. His framework reshapes the agent design problem to put causal reasoning about consequences at its center.

**Run this:**

```
Who is Stuart Russell, and how does his work on objective uncertainty in AI agents connect to the causal agents we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Stuart J. Russell"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Russell's "off-switch" thought experiment — why does an uncertain agent allow itself to be turned off?
- Ask it about the criticisms of Russell's framework from researchers who think it over-emphasizes existential risk.

What changes? What gets better? What gets worse?
