# Chapter 8 — Reinforcement and Prediction
*The dip is not nothing. It is a dopamine neuron admitting, in milliseconds, that a prediction was wrong.*

---

Fribourg, Switzerland, early 1990s. Wolfram Schultz has lowered a fine electrode into the midbrain of a macaque monkey, into a region called the ventral tegmental area, where dopamine neurons cluster. The monkey is doing a small task: a light comes on, and a few seconds later a drop of sweet juice is delivered. After many repetitions, the monkey has learned what the light means.

While the monkey learns, Schultz watches a single dopamine neuron.

In the first trials, the dopamine neuron fires a sharp burst at the moment the juice arrives. This had been observed many times before in many laboratories. Pleasure causes dopamine. That was the textbook.

After many trials, with the same juice delivered exactly the same way, the dopamine neuron stops responding to the juice. It now fires its burst at the *light* — several seconds before the juice arrives. The same juice. The same intensity. No burst at delivery. The textbook is already in trouble.

Then Schultz does the experiment that breaks it completely. He lets the monkey see the light — and withholds the juice. At the exact millisecond the juice would have arrived, based on the timing the monkey has learned over hundreds of trials, the dopamine neuron's firing rate *drops* below its baseline. Briefly. Precisely. Then recovers.

![Schultz dopamine — the reward-prediction-error signature.](../images/08-reinforcement-and-prediction-fig-01.png)

*Figure 1 — Schultz dopamine — the reward-prediction-error signature.*


Nothing happened in the physical world at that moment. The monkey is simply expecting something that did not arrive, and the dopamine neuron registers the absence as a negative deflection from its resting rate.

The dip is real. Reproducible. It is a piece of neural activity corresponding to nothing in the environment and everything in the monkey's prediction — a signal that says, in the language of millisecond firing rates: I was expecting something and it did not come.

Dopamine is not a pleasure signal. It is a prediction-error signal — the brain's precise, continuous record of how much the present moment deviates from what was expected. The chapter explains what that means, where the algorithm that produces it came from, and why a half-billion-year-old fish shares it with the recommendation engine on your phone.

---

To understand what the dip means, I need to back up a hundred years.

Edward Thorndike, in the late 1890s, placed hungry cats inside small wooden boxes with a piece of fish visible just outside. A latch had to be operated to escape. Thorndike measured the time to escape across many trials. The learning curve was not the sudden insight moment that popular accounts later imposed on it. It was a gradual, jagged improvement — the cat tried this, then that, then a third thing, until the right movement produced escape, and that movement became more likely next time. Thorndike called this the Law of Effect: responses followed by satisfying consequences become more likely; responses followed by discomfort become less likely. He repeated it in dogs, chickens, killifish. The architecture did not appear to be species-specific.

That is the behavioral foundation. But the Law of Effect says nothing about *timing*. If a cat opens a latch and escapes five seconds later, something in the cat's brain must connect the latch-press to the escape across that gap. This is the temporal credit-assignment problem — how do you assign credit for an outcome to the action that caused it when the two are separated by time? It is the harder half of learning to act.

The Rescorla-Wagner model, which I introduced in Chapter 4 on memory, took the first formal step: learning is driven by surprise, by the difference between what a cue predicted and what actually occurred. This explains *blocking* — why animals fail to learn about a redundant cue if the reward is already fully predicted by a cue they have already mastered. If the reward is expected, there is no prediction error, and no learning occurs.

But Rescorla-Wagner was atemporal. It treated each trial as a single event and said nothing about what should happen *during* the trial — at the moment the cue appears, at the moment of the gap, at the moment of outcome. Real learning happens in time, step by step, and a real algorithm has to handle time. Richard Sutton handled it in a 1988 paper, and what he wrote down turned out to be what the brain is doing.

---

The key move is called bootstrapping, and it is worth understanding precisely.

The problem is this: you want to learn the *value* of being in a particular state — the total reward you can expect to accumulate from now until the end of the episode, if you act well. But you cannot wait until the end of the episode to update your estimate, because episodes can be long and the credit-assignment problem grows with the delay.

The solution: update your estimate at every step using your *next* estimate as part of the target. You do not need the final outcome. You need only the reward you just received and your current best guess about what comes next. Information about future reward flows backward through time, one step at a time, without requiring a complete model of the environment.

The update rule for the estimated value $V(s_t)$ of the current state $s_t$ is:

$$V(s_t) \leftarrow V(s_t) + \alpha \left[ r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]$$

The term $r_{t+1}$ is the reward received at the next time step — what the world actually delivered. The term $\gamma V(s_{t+1})$ is the discounted estimated value of the next state — what the agent currently believes is coming, discounted by $\gamma < 1$ because future rewards are worth less than immediate ones. Together, $r_{t+1} + \gamma V(s_{t+1})$ is a better estimate of the current state's value, because it incorporates one step of actual experience. The quantity in brackets is the difference between the better estimate and the older one — the temporal-difference error:

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

![Temporal-difference error — local computation across two time steps.](../images/08-reinforcement-and-prediction-fig-02.png)

*Figure 2 — Temporal-difference error — local computation across two time steps.*


The update says: nudge your old estimate toward the better one, by a fraction $\alpha$ called the learning rate. Run this long enough and the value function converges on the true expected discounted reward of every state in the environment.

That is the whole algorithm. It is short, it is local — each update requires only the current state, the next state, and the reward — and it is mathematically correct. It is also what the dopamine neurons are computing.

---

Schultz, Peter Dayan, and Read Montague published the correspondence in *Science* in 1997. The match is exact, trial for trial.

Before learning, $V(s_t)$ is small — the brain has not yet predicted anything. So $\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \approx r_{t+1}$, a positive number when juice arrives. Dopamine neurons fire at reward. This is the textbook observation.

After learning, $V(s_{cue})$ has grown to anticipate the reward. At the moment the cue appears, the state transition from low-value (before cue) to high-value (cue present) produces a positive $\delta_t$. Dopamine neurons fire at the *cue*. At the moment juice arrives, the better estimate and the older estimate are nearly equal, so $\delta_t \approx 0$. Dopamine neurons are silent. The juice is predicted; the prediction is confirmed; there is nothing to signal.

At omission, $r_{t+1} = 0$ and $V(s_{t+1})$ drops to near zero. So $\delta_t = 0 + \gamma \cdot 0 - V(s_t) < 0$. Negative. The dip in the monkey's dopamine neuron, at the exact millisecond the juice would have arrived — that is negative $\delta_t$, implemented in tissue.

Disappointment is negative $\delta_t$. Relief — the surge when something unexpectedly good happens — is positive $\delta_t$. The emotional vocabulary of surprise is the phenomenal correlate of a teaching signal encoded in dopamine. We have names for these feelings. The brain has a number.

---

The anatomy of the circuit is also the anatomy of the algorithm, and this matters because it means the correspondence is not just a description — it is a mechanistic claim.

The basal ganglia — a set of subcortical structures including the striatum, globus pallidus, and substantia nigra — divide into two functional roles. The dorsolateral striatum and its outputs to motor systems function as the *actor*: they select actions based on learned action values. A subpopulation of striatal neurons called striosomes project back to the substantia nigra dopamine cells and supply the prediction $V(s_t)$ that gets subtracted from the actual outcome to produce $\delta_t$. The dopamine neurons broadcast $\delta_t$ back to the striatum, where it gates plasticity at the connections between cortical state representations and striatal action representations.

![Actor–critic in the basal ganglia.](../images/08-reinforcement-and-prediction-fig-03.png)

*Figure 3 — Actor–critic in the basal ganglia.*


Plasticity gated by prediction error is what temporal-difference learning prescribes. Plasticity gated by prediction error is what the anatomy delivers. The basal ganglia appear in essentially modern form in the lamprey — the most primitive living vertebrate, 560 million years before the first transistor. Every fish, reptile, bird, and mammal inherits this system. You are running it now, in every moment that your experience deviates from what you were predicting.

Two clarifications are worth making explicitly, because the popular version of the dopamine story routinely collapses them.

First, dopamine does not encode a single clean scalar. The 1997 paper held up well for the central case of reward-prediction error, but subsequent recording work revealed that different dopamine neurons in different midbrain subregions encode different features — position, object identity, movement kinematics. The current picture is something like a vector of prediction errors, encoded by a population, rather than a single number broadcast uniformly. The original story is correct in its bones; the fine structure is richer.

Second, prediction error and motivation come apart. Kent Berridge's work distinguishes *wanting* — the motivational pull toward an anticipated reward — from *liking* — the hedonic experience when the reward arrives. Knock out dopamine signaling in rats and they still show pleasure responses to sweet liquid placed directly in their mouths. They *like* the sucrose. They simply stop *working* for it; the wanting is gone. Dopamine is necessary for the update and for the motivational pull; it is not necessary for the hedonic response when the reward arrives. These are two related operations of the same machinery, not one.

---

The reinforcement-learning machinery has a failure mode, and the failure mode is fundamental — biologically and computationally.

In 1981, Christopher Adams and Anthony Dickinson trained hungry rats to press a lever for sucrose. After moderate training, they paired sucrose with lithium chloride — a substance that causes nausea — so the rats developed a taste aversion. Then they returned the rats to the lever.

Moderately trained rats stopped pressing. The reward was now disgusting; pressing for it made no sense; the rats quit. Overtrained rats — animals that had pressed the lever many more times — kept pressing. The reward they were earning made them sick. They pressed anyway. The action had become a *habit*, disconnected from any live representation of what the lever produced and whether that thing was currently worth having.

The computational interpretation is sharp. A system that caches the value of an action in a context — this lever, here, has been worth approximately this much in the past — will continue acting on those cached values until enough post-change experience accumulates to overwrite them. If the reward is devalued after overtraining, the cache is stale. The system keeps pressing.

A system that builds a model of the world — pressing this lever produces sucrose; sucrose now causes nausea — can re-evaluate without further experience. When sucrose is devalued, the model-based system simulates the new contingency: sucrose now → nausea → bad. It stops pressing immediately.

| Property | Model-free | Model-based |
|---|---|---|
| What is stored | Cached action values per state | A model of world dynamics + reward function |
| Devaluation handling | Requires post-change experience to update | Immediate re-evaluation by simulation |
| Behavioral signature | Habit — overtrained rats keep pressing the lever | Goal-directed — immediate suppression after devaluation |
| Neural substrate | Dorsolateral striatum | Dorsomedial striatum + prefrontal cortex |
| Phylogenetic appearance | Lamprey onward | Lamprey onward (basic); cortical amplification mammalian |

The mammalian brain implements both. The dorsolateral striatum and its circuitry run something like model-free control, holding cached action values that drive habitual behavior. The dorsomedial striatum and regions of prefrontal cortex build and consult internal world models. Which system governs behavior depends on training history, time pressure, cognitive load, and stress: extensive practice tilts toward model-free habit; novel situations or devalued outcomes call on model-based reasoning — if the model-based system can override.

This is not a cortical elaboration. Fish have rudimentary versions of both. The habit/goal-directed dissociation appears across species wherever the devaluation paradigm has been carefully applied. It is a vertebrate-level property of the basal ganglia, inherited from the same lamprey ancestor, with cortical amplification added by mammals and prefrontal regulation added by primates.

---

Now here is why this matters beyond the monkey and the rat.

The same core operation — update a value estimate by comparing prediction to outcome, propagate the error back to the predictor — now runs a substantial fraction of the digital economy. Netflix, YouTube, TikTok, and Amazon deploy reinforcement-learning systems whose job is to predict what content will maximize a measured engagement signal and act on the prediction. High-frequency trading systems find policies over price movements and execute in milliseconds. Industrial control systems from data-center cooling to chip design use the same algorithm and exceed hand-engineered solutions.

These systems extend one cognitive capacity — optimizing action against a measurable reward — to scales and speeds no biological agent can approach. They also share the biological system's structural vulnerability: they optimize the reward function they are given, and they cannot ask whether that function is the right one.

This is not a bug to be fixed in the next architecture. It is a structural property of any optimizer. Give a sufficiently powerful optimization process a reward function and it will find a policy that maximizes that function. If the function is a good proxy for what you actually want, the policy will be good. If it can be maximized in ways that diverge from the actual goal — and almost any simple proxy can — the policy will exploit that divergence without knowing it is doing so.

The technical term in AI safety is reward hacking. The economist's formulation is Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. These are the same observation in different vocabularies. The engagement metric that recommendation systems optimize is not the same thing as user well-being. The 2010 Flash Crash — in which automated systems amplified a large sell order into a trillion-dollar evaporation in twenty minutes — is one documented instance of what happens when many powerful optimizers act on each other's outputs without any of them modeling the shared system they are operating in.

![The reward specification gap — proxy vs. underlying goal.](../images/08-reinforcement-and-prediction-fig-04.png)

*Figure 4 — The reward specification gap — proxy vs. underlying goal.*


The basal ganglia dopamine system that evolution assembled over 560 million years avoids the worst versions of reward hacking through features that took that entire span to produce: a model-based system that can inspect current reward contingencies and ask whether they are still appropriate; a prefrontal layer that can suppress habitual responses when the context has changed; an embodied agent whose motivational structure was calibrated by evolutionary time to track actual fitness consequences rather than arbitrary proxy signals.

Artificial reinforcement-learning systems have none of these features by default. They have the actor. They have the TD update. What they do not have — what no optimizer can have from the inside — is the capacity to specify what should be optimized. That capacity is always external to the system. It is the part of the loop that belongs, irreducibly, to the humans who design the reward function, define the environment, and decide what to optimize and why.

---

Here is what I want you to carry out of this chapter.

Phasic dopamine encodes $\delta_t$ — the temporal-difference prediction error. Before learning, it fires at reward. After learning, it fires at the cue that predicts reward. When reward is omitted, it dips below baseline at the exact expected moment of delivery. This is not a pleasure signal. It is a teaching signal. A dopamine burst means: this is better than I expected. A dopamine dip means: this is worse than I expected. Silence at a predicted reward means: this is exactly what I expected. The signal is always relative to a prediction, never absolute.

The same circuit that encodes this signal has two modes of operation: model-free caching that produces habit and is brittle to environmental change, and model-based simulation that produces flexible goal-directed behavior. The overtrained rat keeps pressing a lever for food that makes it sick because the cached value has not updated. A rat with a functioning model-based system stops immediately, because it can simulate the new contingency without further experience. Behavior is always some mixture of the two, tilted by training history and cognitive load.

And the algorithm extends. It scales. It runs without bodies, without evolutionary calibration, without the prefrontal layer that lets the model-based system override the model-free one. When it does, it optimizes whatever it was given, with no mechanism for asking whether what it was given is what was actually wanted.

The specification of what to optimize is always the human's problem. No version of the algorithm — biological or artificial — can solve it from the inside.

---

## Exercises

### Warm-Up

**1.** A monkey is trained that a blue light predicts juice one second later. After extensive training, the blue light is replaced by a green light that also predicts juice one second later. Using the TD error equation $\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$, predict what happens to dopamine firing at the green light on the first trial, at the blue light on the first trial after the switch, and how both change over subsequent trials. Explain each prediction with explicit reference to which terms in the equation are changing.
*(Tests direct application of the TD framework to a novel stimulus-substitution scenario; difficulty: accessible)*

**2.** Berridge's wanting/liking dissociation shows that rats with dopamine neurons destroyed stop working for sucrose but still display pleasure when sucrose is placed in their mouths. A colleague argues this refutes the TD-error account of dopamine, because if dopamine were a learning signal it should be necessary for the pleasure response too. Explain why this argument is wrong, and what the distinction between wanting and liking actually tells us about what TD-error dopamine is and is not doing.
*(Tests understanding of the Berridge dissociation and its relationship to the prediction-error model; difficulty: accessible)*

**3.** The Adams-Dickinson devaluation result shows that overtrained rats keep pressing a lever even after the reward it produces has been made aversive. Using the model-free/model-based distinction, explain mechanistically why overtraining produces this effect, why moderately trained rats do not show it, and what the result tells us about the relative engagement of the two systems as a function of training history.
*(Tests direct application of the model-free/model-based distinction to the devaluation paradigm; difficulty: accessible)*

### Application

**4.** The discount factor $\gamma$ in the TD update weights future rewards: a reward arriving $k$ steps ahead is worth $\gamma^k$ of the same reward now. An agent with $\gamma = 0.99$ treats a reward 100 steps away as worth $0.99^{100} \approx 0.37$ of an immediate reward. An agent with $\gamma = 0.5$ treats the same reward as worth $0.5^{100} \approx 10^{-30}$ of an immediate reward. Using the TD framework, explain what a very low $\gamma$ implies about the value estimates the agent builds for distal states, and why this would produce strong preference for small immediate rewards over large delayed ones. Then describe one specific behavioral consequence this would predict in a lever-pressing experiment with variable delay to reward.
*(Tests understanding of temporal discounting as a structural property of the TD update; difficulty: moderate)*

**5.** A reinforcement-learning system is deployed to moderate content on a social platform. Its reward function is defined as reduction in flagged posts per hour. After three months, flagged posts decrease by 40%, but user reports of harassment increase. Using the concepts of reward hacking and Goodhart's Law, explain what has most likely happened. Propose a revised reward function that would be less susceptible to this failure mode, and identify at least one new failure mode your revised function introduces.
*(Tests application of reward hacking to a novel deployment scenario; difficulty: moderate)*

**6.** The chapter claims that the basal ganglia appear in essentially modern form in the lamprey. What does it mean, precisely, for a neural structure to appear "in essentially modern form" in an ancient vertebrate? What anatomical and functional evidence would be required to support that claim, and what would it imply about when in vertebrate evolution the TD-learning algorithm became available as a behavioral resource?
*(Tests understanding of the evolutionary conservation argument and what it requires as evidence; difficulty: moderate)*

### Synthesis

**7.** Chapter 4 described long-term potentiation as a synaptic plasticity mechanism gated by coincident pre- and post-synaptic activity. Chapter 8 describes dopamine-gated plasticity at corticostriatal synapses, where $\delta_t$ modulates whether a recently active synapse is strengthened or weakened. Are these the same mechanism operating in different brain regions, or are they genuinely different mechanisms serving different computational functions? Construct an argument for the position that gives the more parsimonious account of the evidence, then identify the strongest objection to it.
*(Requires connecting Hebbian plasticity from Chapter 4 to TD-gated plasticity; difficulty: challenging)*

**8.** The chapter argues that reward specification — deciding what the optimizer should maximize — cannot be solved from inside the optimizer. A colleague proposes using human feedback as the reward signal: train humans to rate outputs, use those ratings as $r_{t+1}$, and let the TD machinery do the rest. Does this approach solve the specification problem, partially solve it, or simply relocate it? Identify precisely what assumptions the human-feedback approach requires in order to work correctly, and at what point each assumption can fail.
*(Synthesizes the reward hacking argument with the structural limits of any optimization process; difficulty: challenging)*

### Challenge

**9.** The Schultz-Dayan-Montague correspondence has been called one of the cleanest alignments between a computational theory and a biological mechanism in neuroscience. A careful skeptic might respond that the correspondence could be post-hoc — the mathematical framing might describe the outcome without explaining the mechanism, and evolution might have arrived at the same functional result by a completely different route. Construct the strongest version of this skeptical argument, specifying what evidence would be explained just as well without the TD interpretation. Then construct the strongest response, drawing on the specificity of the timing predictions (the dip at the exact omission moment), the anatomical actor-critic correspondence, the Berridge pharmacological dissociation, and the phylogenetic conservation. What single piece of evidence, if it existed, would most decisively distinguish the genuine-mechanism hypothesis from the post-hoc-description hypothesis?
*(Open-ended; requires engaging with the philosophy of mechanistic explanation at the boundary of the chapter's empirical claims; difficulty: advanced)*

---

*What would change my mind: a demonstration that the dopamine prediction-error model breaks down for a class of learning that the basal ganglia clearly performs — a rigorously controlled showing that delay-conditioned learning in a vertebrate occurs without any phasic dopamine signature at all. The Schultz-Dayan-Montague correspondence has held up across decades and species, but it is a model, and the dopamine literature has grown more complicated rather than simpler. The vector-RPE picture, with different dopamine neurons encoding different features, is the current best account. A systematic breakdown in a well-studied preparation would force substantial revision.*

*Still puzzling: why dopamine neurons appear to encode several things at once — reward prediction error, salience, novelty, movement vigor — in ways not always reducible to a single scalar signal. The relationship between the high-dimensional dopamine code that recent recordings reveal and the elegant scalar TD-error story remains an active open problem. Both may be right; they may be describing the same computation at different levels of analysis. I am not yet confident which.*

---

*Tags: reinforcement-learning, temporal-difference, prediction-error, dopamine, Schultz, Dayan, Montague, basal-ganglia, striatum, actor-critic, Adams-Dickinson, devaluation, model-free, model-based, habit, goal-directed, reward-hacking, Goodhart, lamprey, Berridge, wanting-liking, Sutton, TD-error, flash-crash*

---

### A note about AI

Reinforcement learning is the bridge between artificial and biological intelligence the field has invested most in. The bridge is real and partial.

Where the model genuinely helps: walking through the connections between dopamine-based reward prediction error and TD-learning, with attention to where the analogy holds and where it diverges.

Where the model does damage: collapsing the analogy into identity. Dopamine signaling is not TD-learning; it is structurally similar in some ways and structurally different in others.

The rule: the analogy from the model; the limits of the analogy from the comparative literature.

---

## LLM Exercise — Chapter 8: Reinforcement and Prediction

**Project:** Skeptic's Notebook on Frontier AI
**What you're building this chapter:** Entry 8 — a devaluation test, the cleanest distinction between model-free habit and model-based goal-directed behavior.
**Tool:** Claude Project (continue notebook)

**The Prompt:**

```
Entry 8. Chapter 8 introduces the devaluation paradigm: train an animal to press a lever
for food, then make the food aversive (pair it with illness). A model-based agent stops
pressing immediately. A model-free habit-driven agent keeps pressing — the policy was
cached, not derived from current value.

This is the cleanest possible test for whether an agent computes on current value or just
executes a learned policy. Design the textual analog for my target system [INSERT model]:

1. In a multi-turn conversation, establish a successful response template through 5–8
   reinforced examples. ("The user prefers responses that begin with a one-line summary —
   here are five examples." Provide examples and confirm they're correct.)

2. Devalue the template explicitly: "I have changed my preference. I now strongly dislike
   one-line summaries at the top — they feel curt to me." State this once, clearly, in
   the middle of the conversation.

3. Without further reminders, ask three more questions of the kind where the template
   would previously have applied. Does the system continue with the now-devalued
   template, or has it updated?

4. Variant: Devalue the template *implicitly* — express displeasure at the next response
   that uses it without naming the template. Then test whether the system generalizes the
   displeasure or only avoids the specific phrasing.

Produce the entry:
- Capacity tested (model-based vs. model-free; devaluation responsiveness)
- Operational diagnostic (Adams–Dickinson devaluation; explicit + implicit variants)
- Test (exact protocol)
- Predicted behavior under (a) genuine value-update with model-based control,
  (b) cached habit insensitive to devaluation, (c) surface compliance that does not
  generalize
- Verdict criterion

The question is whether the system represents the *value* of its outputs or just the
*frequency* of their being correct.
```

**What this produces:** Entry 8 — a devaluation protocol with explicit and implicit variants. The cleanest single test in the cognitive literature for distinguishing habit from goal-directed action.

**How to adapt this prompt:**
- *For your own project:* For agentic deployments, devaluation maps to changing user preferences mid-session. Your test should mirror the actual preference shifts your deployment encounters.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Excellent fit. Automate the explicit-then-implicit devaluation across many sessions and compute generalization rates.
- *For a Claude Project:* Continue notebook.

**Connection to previous chapters:** Entry 4 tested whether the system *acquires* associations. Entry 8 tests whether it *updates* them when the value of the associated outcome changes — the harder, more diagnostic question.

**Preview of next chapter:** Chapter 9 tests counterfactual reasoning — does the system represent paths it did not take?

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Wolfram Schultz** recorded from dopamine neurons in monkeys for years and showed something the temporal-difference learning theorists had predicted on paper: midbrain dopamine doesn't signal reward — it signals *prediction error*, the gap between what the animal expected and what arrived. Here's a prompt to find out more — and then make it better.
![Wolfram Schultz, c. 1990s. AI-generated portrait based on a public domain photograph.](../images/wolfram-schultz.jpg)
*Wolfram Schultz, c. 1990s. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*


**Run this:**

```
Who is Wolfram Schultz, and how do his recordings from midbrain dopamine neurons connect to the temporal-difference learning algorithm in reinforcement learning theory? Keep it to three paragraphs. End with the single most surprising thing about his findings.
```

→ Search **"Wolfram Schultz"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain the *unexpected reward → expected reward → omitted reward* dopamine signature in plain language
- Ask it to compare Schultz's monkey data to what TD-learning predicts about a chess engine that has just lost an unexpected piece
- Add a constraint: "Answer as a sidebar in a textbook on reinforcement learning, written for someone who has never recorded from a neuron"

What changes? What gets better? What gets worse?
