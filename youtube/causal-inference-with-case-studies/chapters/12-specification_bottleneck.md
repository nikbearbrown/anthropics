# Chapter 12: The Specification Bottleneck

## TL;DR

- By the end of this chapter, you should be able to:.
- The chapter moves through How to Use an LLM That Can't Reason Causally to Help You Build the Causal Graph You Need, Learning Objectives, Prerequisites, 1 The Hardest Step Nobody Talks About, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

## How to Use an LLM That Can't Reason Causally to Help You Build the Causal Graph You Need

---

## Learning Objectives

By the end of this chapter, you should be able to:

1. **Explain** why DAG specification is the binding constraint in causal inference — not estimation — and trace the path from one misspecified edge to one biased estimate
2. **Conduct** a five-phase Socratic elicitation session using an LLM as a coaching agent, distinguishing what the LLM contributes (structure, completeness, memory) from what it cannot contribute (causal judgment)
3. **Identify** the specific formal property of a DAG that each elicitation phase determines, and predict the downstream consequence of skipping any phase
4. **Apply** the Human Decision Node: audit each extracted edge against the expert's raw statement, and catch the three extraction failure modes — collapsed mediation, direction inference, and scope shift
5. **Evaluate** a causal analysis using real data against the DAG it assumes, identifying the gap between what the adjustment set requires and what the dataset contains
6. **Recognize** the observational horizon problem — variables outside the expert's domain of knowledge that the five-phase method cannot surface — and reason about its implications for any DAG built from a single expert

---

## Prerequisites

This chapter builds directly on two earlier chapters:

- **Chapter 11:** LLMs as causal reasoners — specifically, the finding that LLMs are unreliable when asked to propose or validate causal relationships. Nothing in Chapter 12 contradicts that finding. We are building on it.
- **Chapter 3:** The backdoor criterion — you need to know what a valid adjustment set requires, because the five-phase method is designed to produce the information the backdoor criterion needs.

You should also be comfortable with DAG notation from Chapter 2: nodes, directed edges, paths, colliders, mediators, and what it means for an arrow to assert a causal claim.

**Where this chapter fits:** Every method in this book — matching, weighting, instrumental variables — assumes you have a correctly specified causal graph. This chapter is about how to build that graph. It belongs here, after you understand the methods, because you can only appreciate what the graph needs to provide once you understand how those methods use it.

---

## 12.1 The Hardest Step Nobody Talks About

I want to start with a fire.

In March 2000, a lightning strike caused a fire at a Philips semiconductor plant in Albuquerque, New Mexico. The plant supplied radio frequency chips to two major customers: Nokia and Ericsson. Both companies lost their chip supply overnight.

Nokia had mapped its supply chain dependencies. It knew the Philips plant was a single point of failure. Within days, Nokia activated backup suppliers and secured remaining inventory from other Philips facilities. Ericsson had not mapped its dependencies. The causal structure was simple — single-source supplier → total dependency → catastrophic production halt — and everyone at Ericsson knew it informally. But nobody had documented it in a formal structure that would have triggered a risk mitigation strategy before the fire.

If someone had run even a basic variable discovery exercise — "what are the single points of failure in our supply chain?" — the node *single-source supplier* would have appeared, the edge to *production halt* would have been drawn, and the contingency plan would have existed before it was needed. Instead, Ericsson lost $400 million in revenue and exited the mobile phone handset market within a year.

The failure repeated at scale twenty years later. When COVID-19 disrupted global supply chains in 2020–2021, the naive analysis was direct: demand surges caused port congestion caused delivery delays. That's the edge everyone drew. But the actual causal structure had multiple confounded pathways operating simultaneously. Labor shortages reduced port throughput. Pandemic vessel rerouting created congestion at alternate ports. Inventory depletion forced emergency shipping that further clogged the system. Each pathway contributed to delays, but they were entangled — correlated with demand surges but not caused by them in any simple way. Without a structured elicitation to separate the pathways, the interventions targeted the wrong cause. You cannot fix port labor shortages by telling people to order less.

These are supply chain examples because that is this chapter's domain. But the failure mode is universal. Replace "single-source supplier" with "single funding source" and you have the same vulnerability in nonprofit operations. Replace "confounded port congestion pathways" with "confounded treatment pathways" and you have the same misattribution problem in clinical trials. The structure is always the same: the causal graph was either unknown or undocumented, and the cost was paid in dollars, in delayed treatments, or in policies that addressed the wrong cause.

Here is what I find striking about this pattern. Open any causal inference textbook — including this one. The estimation chapters are long, detailed, and full of worked examples. The chapter on how to actually build the DAG is short, gestural, and often reduced to a single instruction: "consult domain experts." As if that were a method rather than a wish.

The Ericsson fire was a **variable discovery failure**: the relevant node existed in the world but not in any formal structure. The COVID port crisis was a **confounder separation failure**: the pathways existed but nobody disentangled them from the obvious direct cause. Both would have been caught by the method this chapter teaches.

**The hardest step in causal inference is not estimation. It is specification.** You can have the cleanest doubly robust estimator in the literature, the most elegant inverse probability weights, the tightest confidence intervals. None of it matters if your causal graph is wrong. If you have drawn an arrow from A to B when the world runs from B to A, your adjustment set is wrong, your estimates are biased, and your conclusions are confident in the wrong direction. The math will be beautiful. The answer will be false.

This chapter turns the wish into a method. Not by replacing domain experts with machines — Chapter 11 established that LLMs are unreliable causal reasoners, and nothing here walks that finding back. Instead, by using LLMs for what they are actually good at: running a structured conversation. The LLM does not decide what causes what. It asks the right questions in the right order. The expert provides the causal knowledge. The LLM provides the scaffolding that keeps the conversation complete, documented, and auditable.

---

## 12.2 The Problem with "Consult Domain Experts"

Before I show you the method, I want to be precise about why unstructured expert consultation fails. Because it does fail — consistently, and in predictable ways.

Imagine you are building a DAG for supply chain disruption. You sit down with an operations manager who has eighteen years of experience. You say: "Tell me what causes delivery delays." She talks for an hour. You take notes. You draw a graph.

What did you get? You got whatever she happened to think of, in whatever order she thought of it, shaped by whatever examples were salient that day. You probably got the variables she knows well and missed the variables she has never directly observed. You almost certainly missed the common causes — the confounders that sit upstream of two variables she named separately, without her realizing they share a source. And you got the mechanisms she compressed into single arrows because the intermediate steps were obvious to her, which means the mediators never appeared on your graph.

The unstructured conversation has four systematic failure modes:

**Incompleteness.** If you don't ask about a variable, it won't appear. The expert tells you what she remembers, not what is complete.

**Missing directionality.** "Inventory levels and delivery delays are related" is an association. Your graph needs a direction. Did low inventory cause delays, or did anticipated delays cause managers to hold more inventory? The direction question often goes unasked.

**Collapsed mediation.** When an expert says A causes C, she is often compressing a chain: A causes B, and B causes C. The direct arrow is a shortcut. The intermediate node — B — is usually exactly what you need to include for a correct adjustment set.

**Hidden common causes.** Two variables the expert named as independently important may share an upstream cause she never mentioned, because she thinks about them separately. No one surfaces the fork unless someone explicitly asks for it.

The five-phase method is designed to catch each of these failures systematically. Each phase targets a specific failure mode. Skip a phase, and that failure mode survives into your final graph.

---

## 12.3 The Five-Phase Method

The method is Socratic knowledge elicitation with iterative graph refinement.

Think of it this way. You're trying to draw a map of a city you've never visited. You can't go there, but you can talk to someone who's lived there for twenty years. The question is how to run that conversation so you don't miss neighborhoods, don't draw roads that don't exist, and don't put the hospital on the wrong side of the river.

You could ask "tell me about your city" and hope for the best. Or you could ask in five structured phases, each designed to catch a different kind of error.

![The five-phase loop as a cycle diagram. Each phase labeled with its name, its target failure mode, and an arrow leading to the running...](images/12-specification-bottleneck-fig-01.png)
*Figure 12.1 — five-phase loop as a cycle diagram*

### Phase 1: Variable Discovery

**Target failure mode:** Incompleteness — variables that exist in the world but not in the graph.

**The question:** "What are the main factors that affect delivery delays and shipping costs in your supply chain?"

This phase builds the node set of your DAG. If a variable is not named here, it cannot appear in any adjustment set. Phase 1 does not ask about causation yet — that invites premature closure and anchors the expert on a particular causal story before you've established what is in the system. Just inventory the variables. Get them on the table.

The LLM's role in this phase is completeness checking. After the expert names variables, the LLM prompts: "Are there upstream factors that affect the variables you've named? Are there external factors — macroeconomic, regulatory, or environmental — that I haven't asked about?" The goal is to push the expert to the edges of what she knows.

### Phase 2: Edge Probing

**Target failure mode:** Missing connections between variables already named.

**The question:** "Does geopolitical risk affect supplier reliability? Directly, or through something else?"

With the node set established, Phase 2 asks about connections. For every pair of variables that the expert might plausibly link, the LLM generates a direct probe. The "directly, or through something else?" clause is load-bearing — it primes the expert to think about mediators rather than collapsing chains into single arrows.

The LLM's role is to ensure that every named variable has been probed against every other, not just the pairs the expert mentions spontaneously. This catches the missing edges that unstructured conversation leaves behind.

### Phase 3: Mechanism Questioning

**Target failure mode:** False edges and collapsed mediation.

**The question:** "You said fuel prices affect delivery delays. Walk me through the mechanism. What's the chain of events?"

This is the most valuable phase in the method. When someone says A causes C, mechanism questioning often reveals that A causes B and B causes C — and the direct arrow is a compression. It also, critically, catches arrows that should not exist at all.

Here is a concrete example from the case study this chapter develops. The expert initially described fuel prices as affecting delivery delays. That sounds plausible. Every supply chain dataset shows fuel costs and delivery timing co-moving. But when Phase 3 asked for the mechanism — "what actually happens when fuel gets expensive, step by step?" — the expert's answer was immediate: "Carriers charge more. They don't slow down." Fuel prices affect *costs*, not *timing*. The direct edge from fuel prices to delivery delays was not a simplification. It was wrong. Phase 3 killed it in one sentence.

I want to be precise about what it would have cost to keep that edge. Section 12.4 traces this in detail. For now: one surviving false edge corrupts the adjustment set, which corrupts every downstream estimate that uses that adjustment set. Phase 3 exists to force the mechanism conversation before the graph is finalized.

### Phase 4: Confounder Probing

**Target failure mode:** Hidden common causes — the forks that create spurious association.

**The question:** "Is there something that might be driving both fuel prices and shipping costs at the same time?"

This phase explicitly hunts for the confounders that Phase 2 misses. When an expert names two variables as independently important, she is thinking about them separately. She may not spontaneously connect them to a shared upstream cause. Phase 4 makes that connection the explicit subject of a question.

The LLM generates confounder probes for every pair of variables that share no directed path in the current running graph. The question structure — "is there something driving both X and Y?" — invokes the fork pattern from Chapter 2. The expert can often identify common causes when asked directly, even if she would never have named them spontaneously.

### Phase 5: Checkpoint Validation

**Target failure mode:** Translation errors between what the expert said and what the graph encodes.

**The question:** "Here's the graph we've built so far. Does this match your understanding?"

After the first four phases, the LLM presents the current graph — the nodes, the directed edges, and the claimed mechanisms — and asks the expert to review it. This is the error-correction phase. It catches cases where the expert said one thing and the analyst heard another, where a directional claim was made implicitly and encoded explicitly in the wrong direction, and where the expert's overall model of the system doesn't match the formal graph that emerged from the conversation.

Phase 5 does not substitute for the Human Decision Node (described in Section 12.5). The expert validates the content; the analyst validates the structure.

---

## 12.4 What One Skipped Phase Actually Costs

A method that feels rigorous is not the same as a method that is rigorous. Let me trace a specific path from one skipped question to one biased estimate, because the causal chain here is as traceable as any in the supply chain DAG.

Suppose Phase 3 is omitted. Nobody asks "how does expensive fuel slow down a delivery?" The edge $\text{fuel\_prices} \rightarrow \text{delivery\_delays}$ survives because it sounds plausible. Fuel and delays co-occur in every supply chain dataset where both are measured.

Now the analyst asks: what is the causal effect of port congestion on delivery delays? The backdoor criterion computes the adjustment set from the graph. With the false edge in the graph, $\text{fuel\_prices}$ appears as a candidate in that set — it looks like a variable that shares causal ancestry with both the treatment and the outcome. The analyst adjusts for it.

Here is the damage. Fuel prices are entangled with $\text{geopolitical\_risk}$, which is a real confounder for the port congestion estimate. Geopolitical instability drives both port disruptions (through trade route interference) and delivery delays (through supplier failures and insurance costs). This is a fork: $\text{geopolitical\_risk} \rightarrow \text{port\_congestion}$ and $\text{geopolitical\_risk} \rightarrow \text{delivery\_delays}$. Correctly conditioning on geopolitical risk is necessary to identify the effect of port congestion on delays.

When the analyst conditions on fuel prices instead — because the false edge made fuel prices look relevant — she partially absorbs the variation in geopolitical risk. The adjustment is both wrong (adjusting for something causally unrelated to timing) and incomplete (not fully adjusting for the actual confounder). The correct doubly robust estimate for port congestion's effect on delivery delays, computed from the correct DAG, is 0.45. With fuel prices incorrectly in the adjustment set, that number shifts — not because of sampling noise, but because the adjustment set is structurally wrong.

One skipped question. One surviving false edge. One corrupted adjustment set. One biased estimate. The domain expert in the case study killed this edge in one sentence during Phase 3: "Carriers charge more when fuel is expensive. They don't slow down." That sentence is Phase 3's entire purpose.

---

## 12.5 How the LLM Actually Operates

Chapter 11 established that LLMs cannot reliably propose or validate causal relationships. I am not building a causal oracle. I am building a coaching agent, and the distinction matters.

The LLM — in this implementation, Claude via the Anthropic API — operates as an agent called **ProfY**. ProfY talks to the analyst, not to the domain expert directly. ProfY generates the next Socratic prompt for each phase. The analyst relays it to the expert. The analyst relays the expert's answer back. ProfY extracts structured variable-edge pairs from the conversation. At no point does ProfY propose a causal relationship on its own authority.

What ProfY contributes is **facilitation, not reasoning**: it keeps the conversation on track, asks from multiple angles across five phases, translates free-form expert knowledge into structured variable-edge pairs, and maintains state across a long session that a human would handle inconsistently. Think of it as a court reporter who also knows which questions to ask next — but who has no opinion about the testimony.

The system runs in two modes. **Replay mode** reads from saved transcripts and requires no API key — it is suitable for students running the notebook from the repository. **Live mode** calls the Anthropic API in real time and supports actual elicitation sessions.

The API call structure for each phase prompt looks like this:

```python
import anthropic

client = anthropic.Anthropic()

def run_phase(phase_number, phase_prompt, conversation_history):
    """
    Run one elicitation phase. Returns extracted edges as structured pairs.
    phase_prompt: the system instructions for this specific phase
    conversation_history: accumulated context from all prior phases
    """
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=phase_prompt,
        messages=conversation_history
    )
    
    # Extract structured edges from the response
    # ProfY returns variable-edge pairs in a parseable format
    content = response.content[0].text
    return parse_edges(content)  # returns list of (source, target) tuples
```

Each phase uses a different system prompt, tuned to the specific failure mode that phase targets. The Phase 3 prompt explicitly instructs ProfY to ask for mechanisms before accepting any proposed edge. The Phase 4 prompt explicitly instructs ProfY to ask whether any pair of variables shares an upstream cause. The prompts are not interchangeable — each embeds the causal reasoning the analyst needs from that phase.

### The Human Decision Node

After elicitation completes, every proposed edge is presented as commented-out Python code:

```python
# Phase 3 extraction — review each edge before uncommenting
# Expert statement: "When fuel is expensive, carriers charge more but don't slow down"
# Extracted: fuel_prices → shipping_cost (ACCEPTED)
# Extracted: fuel_prices → delivery_delays (REVIEW — mechanism does not support timing effect)

edges = [
    # ("fuel_prices", "shipping_cost"),      # uncomment to accept
    # ("fuel_prices", "delivery_delays"),    # uncomment to accept — see note above
    # ("port_congestion", "delivery_delays"), # uncomment to accept
]
```

The notebook will not proceed until this cell is edited. Every rejection is logged with the analyst's reasoning. This is not a soft suggestion — the code literally stops. Passive acceptance is eliminated by design, because passive acceptance is where false edges survive into the final graph.

The Human Decision Node is the architectural acknowledgment that the LLM cannot be trusted to validate causal claims. The analyst must look at every proposed edge and ask: does the expert's stated mechanism actually support this arrow? The ProfY system preserves the full transcript alongside extracted edges precisely so this comparison is easy to make.

---

## 12.6 Three Extraction Failure Modes

The Human Decision Node catches causally wrong edges. But there is a quieter failure mode: edges that don't faithfully represent what the expert said. This is distinct from causal wrongness. These edges may be causally defensible while still misrepresenting the causal structure the expert actually described.

Three extraction errors recur:

**Collapsed mediation.** The expert describes a causal chain; the LLM extracts a direct edge. During Phase 3 of the case study, the expert said: "When geopolitical instability hits, it disrupts suppliers, and that makes raw materials harder to get." That is a mediated pathway:

$$\text{geopolitical\_risk} \rightarrow \text{supplier\_reliability} \rightarrow \text{raw\_material\_availability}$$

ProfY extracted one edge: $\text{geopolitical\_risk} \rightarrow \text{raw\_material\_availability}$. Not wrong about the endpoint — geopolitical risk does ultimately affect raw material availability. But the mediator ($\text{supplier\_reliability}$) is gone. And the mediator matters: it is a node through which interventions could operate. If you want to ask "what is the direct effect of geopolitical risk on raw material availability, net of its effect on supplier reliability?", you need the mediator in the graph. The collapsed extraction makes that question unaskable.

**Direction inference.** The expert states an association; the LLM infers a direction. When the expert says "inventory levels and delivery delays are related," that is an observation, not a causal claim. The LLM may extract $\text{inventory\_levels} \rightarrow \text{delivery\_delays}$ because that is the more common causal story. But the actual direction in this expert's model might be the reverse: anticipated delays cause managers to hold higher inventory as a buffer. A reversed direction changes which variables are confounders and which are mediators — with direct consequences for the adjustment set.

**Scope shift.** The expert makes a conditional claim; the LLM extracts it as unconditional. "In high-demand seasons, port congestion causes delays" is a conditional statement. Extracting it as $\text{port\_congestion} \rightarrow \text{delivery\_delays}$ without the demand seasonality condition misses the interaction structure. The edge may belong in the graph, but its strength and conditions are part of the causal claim.

| Expert's raw statement | LLM's extraction | Faithful extraction |
|---|---|---|
| "Geopolitical instability disrupts suppliers, which makes raw materials harder to get." | $\text{geopolitical\_risk} \rightarrow \text{raw\_material\_availability}$ | $\text{geopolitical\_risk} \rightarrow \text{supplier\_reliability} \rightarrow \text{raw\_material\_availability}$ |
| "Inventory levels and delivery delays are related." | $\text{inventory\_levels} \rightarrow \text{delivery\_delays}$ | Association only — direction requires domain judgment |
| "In high-demand seasons, port congestion causes delays." | $\text{port\_congestion} \rightarrow \text{delivery\_delays}$ | Conditional edge — demand volatility may be a moderator |

The practice: before the Human Decision Node, read each raw expert statement next to its extracted edge and ask three questions. Did this compress a mediated pathway? Did the extraction infer a direction the expert never stated? Did it generalize a conditional claim into an unconditional edge? These three questions are the audit. The system preserves the full transcript to make the audit possible. It cannot make the analyst do it.

---

## 12.7 The Case Study

Three characters: **Ally** (data modeler and analyst, uses ProfY as copilot), **Nora** (domain expert, operations manager with eighteen years of experience), and **ProfY** (Ally's coaching agent — talks to Ally, not to Nora directly).

The domain is supply chain disruption. The target outcomes are delivery delays and shipping costs. The ground truth DAG has 12 nodes and 19 edges. Three exogenous roots — $\text{geopolitical\_risk}$, $\text{labor\_shortages}$, $\text{demand\_volatility}$ — drive the system. Every edge in the reference graph is cited from published supply chain literature: Chopra and Sodhi (2004), Ho et al. (2015), Tang (2006).

![The ground truth supply chain DAG with 12 nodes and 19 edges. Exogenous roots on the left, target outcomes on the right. Edges grouped...](images/12-specification-bottleneck-fig-02.png)
*Figure 12.2 — ground truth supply chain DAG with 12 nodes and 19 edges*

**Structural Hamming Distance (SHD)** is the evaluation metric: it counts mistakes on the map. You drew a road that doesn't exist? That's one. Missed a road that does? That's one. Drew it going the wrong way? That's one. SHD adds them up. Secondary metrics — precision, recall, F1 over edges — decompose this further.

### The Ideal Run

With all five phases executed correctly and Nora's full knowledge engaged: 12 variables surfaced, 19 edges proposed, SHD = 0, Precision = 1.0, Recall = 1.0, F1 = 1.0. A perfect map.

This is not the interesting result.

### The Imperfect DAG

Four deliberate mistakes were introduced to demonstrate what specification errors cost downstream:

- **Two missing edges:** $\text{fuel\_prices} \rightarrow \text{production\_capacity}$ and $\text{supplier\_reliability} \rightarrow \text{order\_lead\_time}$ — variables the expert knows about but didn't mention because nobody asked directly
- **One hallucinated edge:** $\text{fuel\_prices} \rightarrow \text{delivery\_delays}$ — the edge Phase 3 would have killed, surviving because Phase 3 was skipped
- **One reversed edge:** $\text{order\_lead\_time} \rightarrow \text{demand\_volatility}$ — drawn backwards, like saying the long line at the coffee shop caused everyone to want coffee

Result: SHD = 4, F1 = 0.865. Four mistakes that propagate into every downstream estimate.

### What the Estimates Show

With the correct DAG, the backdoor criterion computes adjustment sets and doubly robust estimation runs on the validated graph.

**Port congestion → delivery delays.**

- Naive difference: 0.95
- Doubly robust estimate, adjusting for $\text{geopolitical\_risk}$ and $\text{labor\_shortages}$: **0.45**

Nearly half of what looked like port congestion was actually geopolitical instability and labor shortages driving both congestion and delays simultaneously. The fork structure — $\text{geopolitical\_risk} \rightarrow \text{port\_congestion}$ and $\text{geopolitical\_risk} \rightarrow \text{delivery\_delays}$ — is why the naive number is so inflated. The unadjusted estimate absorbs the common cause.

**Fuel prices → shipping cost.**

- Naive difference: 0.98
- Doubly robust ATE: **0.51**

Geopolitical risk was inflating the naive estimate through route disruptions, insurance premiums, and port delays — all of which raise costs through mechanisms other than fuel. Think of it like rain and traffic. The naive comparison says traffic is 0.98 worse when it rains. The adjusted estimate says rain itself accounts for 0.51. The rest is more cars on the road — a confounder correlated with rain but with its own separate effect on traffic.

### Sensitivity Analysis

**Remove one edge** ($\text{fuel\_prices} \rightarrow \text{production\_capacity}$): SHD increases by 1, F1 drops to 0.973. A minor structural error, but the adjustment set is now incomplete for any estimate involving production capacity as a treatment or outcome.

**Reverse one edge** ($\text{inventory\_levels} \rightarrow \text{delivery\_delays}$ reversed to $\text{delivery\_delays} \rightarrow \text{inventory\_levels}$): SHD increases by 1, F1 drops to 0.947. A direction error changes which variables are confounders and which are mediators. Condition on a mediator and you block the causal pathway you are trying to measure. The math still runs. The answer is wrong in a way that is invisible without the correct graph.

### The Real Data Test

The system was applied to the DataCo Smart Supply Chain dataset — 180,000 real orders with shipping mode, delivery status, order characteristics, and cost data.

Late delivery rates by shipping mode: Standard Class at 38%, First Class at 95%. First Class shipping is late almost every time, which likely reflects how "late" is defined relative to promised delivery windows and the types of orders routed to premium shipping — an endogeneity problem built into the data structure.

The doubly robust estimate barely moved from the naive difference. The propensity model achieved only 0.60 accuracy — barely better than a coin flip. The real confounders that the DAG requires for a valid adjustment — inventory levels, order urgency, cost pressure from upstream disruptions — are not in the dataset.

This is the lesson simulated data cannot teach. A well-built DAG does not just tell you what to control for. It tells you what you are missing. The gap between what the DAG's adjustment set requires and what the data contains is where bias lives. No estimator, however sophisticated, can adjust for variables that were never measured. The DAG is the diagnostic that tells you to stop.

> **When the estimate barely moves after doubly robust adjustment, that is not evidence of robustness. It is often evidence that the adjustment variables are not in the data.**

---

## 12.8 The Limitation the Five Phases Cannot Fix

The five-phase method reduces specification error systematically. It does not eliminate it. There is a formal bound on what it can do.

All five phases depend on the expert being able to name every causally relevant variable. But some confounders operate in domains the expert never observes.

Consider credit terms — the financial agreements a procurement department negotiates with shipping carriers. Credit terms affect which carriers accept a company's business (constraining shipping mode availability) and how quickly carriers prioritize shipments (affecting delivery timing). Credit terms are a common cause of both shipping mode and delivery delays. They belong in the DAG.

But Nora is an operations manager. She has never seen a carrier contract. No amount of Socratic questioning surfaces a variable the expert doesn't know exists. Phase 1 won't catch it. Phase 4 won't catch it. All five phases can run perfectly and the adjustment set will still be wrong.

This is the **observational horizon problem**: the backdoor criterion computes correct adjustment sets given the graph you provide. It cannot tell you the graph is missing a node. The five-phase method is bounded by the expert's domain of observation, not by the method's structure.

This is also why Chapter 13 matters. Data-driven structure learning algorithms can sometimes detect that the data is inconsistent with the assumed graph — a signal that something is missing. The expert builds the map from knowledge. The algorithm checks it against the terrain. Neither is complete alone.

---

## Chapter Summary

The specification bottleneck is real, and this chapter gave you a method for addressing it.

**You can now conduct a five-phase elicitation.** Each phase targets a specific failure mode: Phase 1 catches missing variables, Phase 2 catches missing edges, Phase 3 catches false edges and collapsed mediation, Phase 4 catches hidden common causes, Phase 5 catches translation errors. Skip any phase and a specific formal property of the DAG is compromised in a predictable way.

**You understand what the LLM contributes and what it cannot.** ProfY facilitates — it maintains state, generates structured prompts, translates free-form knowledge into graph structure. It does not reason causally. The Human Decision Node enforces this boundary architecturally: the code stops until every proposed edge is explicitly accepted or rejected.

**You can audit extraction fidelity.** Three failure modes — collapsed mediation, direction inference, scope shift — produce edges that misrepresent the expert's stated structure even when they are causally defensible. The comparison between raw expert statement and extracted edge is the audit. The system makes it possible. The analyst has to do it.

**You know what the real data test reveals.** A DAG that requires variables the dataset doesn't contain produces estimates that cannot be trusted. The gap between what the adjustment set needs and what the data has is where bias lives. A well-built DAG turns that gap visible.

**The one idea that matters most:** Specification errors are not random noise. They are structural. A false edge corrupts a specific adjustment set. A reversed edge turns a confounder into a mediator. A missing mediator makes a class of causal questions unaskable. The five-phase method catches each of these in a specific phase because each failure mode has a specific origin.

**The common mistake to watch for:** Treating the elicitation as complete when the conversation feels complete. The conversation feels complete when the expert stops generating new variables. But silence is not completeness — it is the observational horizon. Phase 4's explicit confounder probes push past the horizon as far as the expert's knowledge allows. They cannot push past the edge of what she has ever observed.

**The Feynman test for this chapter:** Explain to someone why skipping Phase 3 produced a biased estimate in Section 12.4. Walk them through the path: no mechanism question → false edge survives → edge corrupts adjustment set → wrong variable absorbs confounder variance → estimate shifts. If you can trace that chain, you understand this chapter. If you can only say "Phase 3 is important," you have memorized the method without understanding it.

---

## Connections Forward

**Chapter 13 (Data-Driven Structure Learning)** adds the algorithmic check to the expert-elicited graph. Given the DAG Ally and Nora built together, and given the DataCo dataset, can structure learning algorithms test whether the data's conditional independence patterns are consistent with the assumed graph? Can they suggest edges the expert missed? The expert's knowledge and the data's patterns are two independent sources of structural information. Chapter 13 shows how to use both.

The deeper question Chapter 13 addresses is the one Chapter 12 leaves open: what happens when the expert's observational horizon excludes a causally important variable, and the data has the right variables to detect the inconsistency? The answer is not "the algorithm finds the right graph automatically." It is more specific and more limited than that — and more useful.

---

## Exercises

### Warm-Up

**Exercise 12.1** — *Tests Learning Objective 2 | Difficulty: Low*

For each of the five phases, write one sentence stating: (a) the failure mode the phase targets, and (b) the formal property of the DAG the phase determines (node set, edge set, directionality, common causes, translation accuracy).

**Exercise 12.2** — *Tests Learning Objective 1 | Difficulty: Low*

The chapter traces the path: skipped Phase 3 → false edge $\text{fuel\_prices} \rightarrow \text{delivery\_delays}$ → corrupted adjustment set → biased estimate. Draw this as a causal chain with five nodes. Then identify: which node in this chain is the one that the Human Decision Node is designed to interrupt?

### Application

**Exercise 12.3** — *Tests Learning Objectives 3 and 4 | Difficulty: Medium*

A student conducts a five-phase elicitation for a DAG about employee turnover. During Phase 3, the expert says: "When managers give bad reviews, it hurts morale, and low morale is what actually makes people quit."

(a) What is the faithful extraction of this statement as a graph structure?  
(b) What would the collapsed extraction look like?  
(c) For the causal question "what is the direct effect of manager reviews on turnover, net of its effect on morale?", explain what you can and cannot estimate under each extraction.

**Exercise 12.4** — *Tests Learning Objectives 2, 3, and 6 | Difficulty: Medium*

You are designing a five-phase elicitation for a DAG about patient readmission rates after hospital discharge. Your domain expert is a hospital floor nurse with ten years of experience.

(a) Write specific Phase 1 and Phase 4 prompts for this domain.  
(b) Identify two variables that are likely inside the nurse's observational horizon and two variables likely outside it.  
(c) For one of the variables outside her horizon, name the structural role it would play in the DAG (confounder, mediator, collider) and explain what estimate would be biased by its absence.

**Exercise 12.5** — *Tests Learning Objective 5 | Difficulty: Medium*

The DataCo analysis produced a propensity model with 0.60 accuracy. The doubly robust estimate barely moved from the naive difference.

(a) Is this evidence that the causal effect estimate is reliable? Explain using the concept of adjustment set requirements.  
(b) What would you need to add to the dataset before trusting the doubly robust estimate?  
(c) Name one variable the DAG requires for adjustment that the DataCo dataset plausibly doesn't contain, and explain why its absence biases the estimate in a specific direction.

### Synthesis

**Exercise 12.6** — *Tests all Learning Objectives | Difficulty: High*

**Student Deliverable: DAG Diagnostic Report**

Complete the chapter's notebook elicitation exercise. Then write a report with three components:

**Component 1 — Phase-to-formalism mapping.** For each of the five phases, identify: (a) what formal property of the DAG that phase determined, and (b) whether that property is complete in your elicited graph. If it is not complete, identify the specific gap and which phase should have caught it.

**Component 2 — Measurability audit.** Pick one causal question from your elicited DAG. Compute the backdoor adjustment set. For each variable in that set, state whether it is measurable in the available dataset. For any unmeasured variable, write one sentence explaining what bias its absence introduces and in which direction.

**Component 3 — Latent confounder analysis.** Name one plausible latent confounder not in your DAG. Explain why the five-phase elicitation would not have caught it — reasoning specifically about the boundaries of your expert's observational horizon, not just saying "we didn't ask." What structural role would this variable play, and how would its absence affect the specific adjustment set from Component 2?

*Grading criteria: Component 1 is graded on whether the phase-to-formalism mapping is technically correct. Component 2 is graded on whether the measurability audit is specific (names variables, states direction of bias) rather than vague (says "bias may exist"). Component 3 is graded on whether the proposed confounder is genuinely outside the expert's domain of observation — not just a variable you forgot to ask about.*

### Challenge

**Exercise 12.7** — *Tests Learning Objectives 1, 4, and 6 | Difficulty: High*

The chapter claims that a reversed edge "turns a confounder into a mediator." Construct a minimal three-node DAG that demonstrates this claim — show a configuration in which variable $M$ is a confounder for the effect of $X$ on $Y$, and then show how reversing one edge in the graph makes $M$ a mediator instead.

(a) For each DAG, apply the backdoor criterion and state the correct adjustment set.  
(b) Show that conditioning on $M$ produces different estimates under each DAG — not just because the adjustment set changes, but because the causal question has changed.  
(c) Connect this back to the reversed edge in the case study's imperfect DAG. What specific estimate was affected, and in which direction?

---

### LLM Integration Activity: Run the Elicitation

Using the chapter's notebook (Replay mode requires no API key), run all five phases of the elicitation with the saved Nora transcript. After elicitation completes:

1. Before the Human Decision Node, read each extracted edge next to Nora's raw statement. Identify at least one instance of each of the three extraction failure modes: collapsed mediation, direction inference, and scope shift.

2. At the Human Decision Node, make explicit accept/reject decisions for every proposed edge. For each rejection, write one sentence of reasoning — not "this seems wrong" but a specific mechanistic argument for why the edge does not belong.

3. Compute the SHD between your final accepted graph and the reference DAG. For each mistake (missed edge, false edge, reversed edge), identify which phase should have caught it and why it didn't.

---

*End of Chapter 12*

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Edward Leamer** wrote "Let's Take the Con Out of Econometrics" in 1983 — arguing that empirical economics was effectively a search over many specifications, with researchers reporting only their favorites. His work made specification sensitivity a serious methodological issue.

**Run this:**

```
Who is Edward Leamer, and how does his work on specification sensitivity connect to the specification bottleneck we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Edward Leamer"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Leamer's extreme-bounds analysis on a specific applied question.
- Ask it about the credibility revolution in economics that Leamer's critique helped launch.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 12.1 — five-phase loop as a cycle diagram

Create a standalone D3 v7 HTML figure for "five-phase loop as a cycle diagram". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes and arrow connectors. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/12-specification-bottleneck-fig-01.html`

---

### Figure 12.2 — ground truth supply chain DAG with 12 nodes and 19 edges

Create a standalone D3 v7 HTML figure for "ground truth supply chain DAG with 12 nodes and 19 edges". Use a horizontal process diagram with 4 to 5 ordered stages with directed connectors. Marks: rectangular stage nodes and arrow connectors. Channels: position for sequence or category, length for quantitative emphasis when bars are used, color for the primary highlighted item only, and direct text labels for accessibility. Use a zero baseline for quantitative bars. Include title, desc, role="img", aria-labelledby, ResizeObserver redraw, dark mode CSS variables, and reduced-motion safeguards. Deliver as one HTML file with inline CSS and the D3 7.9.0 CDN.

> Reference implementation: `d3/12-specification-bottleneck-fig-02.html`
