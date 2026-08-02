# Chapter 8 — Simulation, Planning, and Regret

A rat is running a small circular track at the University of Minnesota. Four stations are spaced around it, and at each one a chime sounds, holding a single tone for some number of seconds before a pellet of flavored food drops. Cherry at one station. Banana at the next. Chocolate. Plain. The rat has an hour, and one decision to make over and over: wait here for the food, or skip on to the next station and hope for a better deal.

The rats develop preferences, and they are stubborn about them. Each rat has a threshold — the longest wait it will tolerate for each flavor. Cherry might be worth waiting thirty seconds for. Banana, only ten. The thresholds are idiosyncratic, stable, and genuine in the way preferences are genuine. David Redish's lab calls the track Restaurant Row.

In 2014, Adam Steiner and Redish arranged it so they could catch a particular kind of expensive mistake. The rat arrives at the cherry station. The chime offers a wait inside its cherry threshold — a good deal. The rat skips it anyway, gambling on the next station. It arrives at banana, and the chime offers a wait *above* its banana threshold — a bad deal. Reluctantly, hungry, the rat accepts. Good deal declined; worse deal taken instead.

The rat looked back. Mid-wait at the banana station, it turned its head toward the cherry station it had just passed up. And while it looked, neurons in two places lit up — in the **orbitofrontal cortex**, the OFC, a sheet of prefrontal cortex just behind the eyes, and in the **ventral striatum**, the basal-ganglia region we met in the last chapter computing the value of where you are. They fired in the pattern they had previously fired while the rat was *at the cherry station*. The brain was not encoding the disappointing banana the rat was actually stuck with. It was encoding what the rat should have done a few seconds ago. After the look-back, the rats waited longer at the following stations, and rushed through eating the reward they did get — bolting it, the way a person eats when something has gone wrong. Exactly the corrections that regret produces in a human.

A small mammal had just run a counterfactual.

I want to be careful about the claim. I am not saying the rat *felt* regret in any phenomenal sense. We do not know what it is like to be a rat, and this experiment cannot settle it. What I am saying is that the rat's brain carried out the *computation* of regret — it represented an alternative that had been available and not taken, compared its value to the actual outcome, and revised its policy. That computation is what Judea Pearl calls the third rung of the causal ladder: counterfactual reasoning, which asks not what happened but what *would* have happened had something else been done. It had long been taken for a uniquely human operation. Restaurant Row says otherwise.

This chapter is about the architecture under that look-back — the machinery that lets a brain run the world forward in its head before acting, and backward through the past to recover the better option it missed. By the end you should see why a rat at Restaurant Row is doing something related to what a chess engine does, and why neither is quite what a language model produces when it generates a paragraph beginning *"If I had chosen differently…"*

---

Before the rat, the architecture. There are two ways to learn, and they are different in kind.

A rat in a box presses a lever by accident. A pellet drops. It presses again; another pellet. It presses many times, and the value of pressing gets cached: lever-press → reward. This is one way to learn — store what paid off in the past, retrieve it when the same situation comes around again. Call it **model-free** learning.

Now poison the well. The experimenter, outside the box, feeds the rat those pellets to satiety in a way that makes them sickening — the pellets are now linked to nausea, not reward. Return the rat to the box, and it presses the lever anyway. It has to experience the bad outcome again, in the box, before the cache updates. Anthony Dickinson and Bernard Balleine documented this cleanly with the devaluation paradigm. The model-free agent does not *know* that the lever leads to food that is now aversive. It only knows that the lever has historically been rewarded.

A different kind of agent never makes this mistake. It holds a model: the lever leads to pellets; pellets are currently aversive; therefore the lever is currently a bad idea. It can chain those facts together without pressing anything, compute the expected outcome, and decline. This is **model-based** learning, and it is qualitatively different. The model-free agent retrieves a cached number. The model-based agent *simulates* — it runs a rehearsal of what would happen before it commits.

The distinction maps onto Pearl's three rungs cleanly. The first rung is **association**: A and B occur together. The rooster crows; the sun rises. The lever produces food. The model-free cache is a sophisticated association — which actions in which situations have historically paid off. The second rung is **intervention**: what happens if I *do* X? Both systems can answer this, model-free by lookup, model-based by simulation. The third rung is **counterfactual**: what would have happened if I had done otherwise? This one requires holding two world-states in mind at once — the actual and the road not taken — and computing the difference between them. No amount of caching produces it. It needs a world-model and the ability to run that model in a direction the body never went.

Two modes of control, three rungs of reasoning. The model-free cache lives on rungs one and two. Reaching rung three takes genuine simulation — and the rat at the banana station, looking back at cherry, is on rung three.

---

In 1948, Edward Tolman published a paper describing something he had watched rats do at T-junctions. A rat approaches the fork, pauses, and swings its head left, then right, then left again. Tolman called this *vicarious trial and error* — VTE — and argued the rat was trying the alternatives out in its head before committing. His behaviorist colleagues were unconvinced. VTE could be nothing but an indecisive head-wobble with no thought behind it. The argument could not be settled with the neurophysiology of 1948.

Sixty years on, the electrodes were fine enough to settle it.

The hippocampus — which the last chapter established as the seat of the spatial map — turns out to be a trajectory generator. The place cells that fire when the rat occupies a particular location *also* fire, in rapid sequence, when the rat is sitting still, during brief high-frequency bursts called **sharp-wave ripples** in the CA1 and CA3 subfields of the hippocampus. A ripple is a burst of synchronous activity lasting roughly fifty to a hundred milliseconds. During each one, populations of place cells fire in sequences that re-create routes through the map.

Brad Pfeiffer and David Foster, recording from many place cells at once in 2013, caught the forward version. Just before a rat began moving toward a remembered goal, a quick sweep of place-cell firing — beginning at the rat's current position, ending at the goal, traversing the path between — ran off in about a hundred milliseconds, far faster than the rat could physically run it. And the sweep predicted which route the rat then took. Sometimes it predicted the route better than the rat's prior behavior would have, as though the simulation had evaluated the options and picked the better one. The hippocampus was pre-experiencing the trajectory before the body took a step.

This is **forward replay** — the map running a fast simulation of a candidate future on the same neural substrate that encodes the real path during movement. The sweep is the simulation made visible, a sequence of place-cell activations for locations the animal is not in, running at roughly fifteen to twenty times physical speed.

Foster and Matthew Wilson, in 2006, documented the mirror image. After a rat ran a path and reached reward, the place cells fired in *reverse* order — from the reward location backward through the path just taken. **Reverse replay**, also during sharp-wave ripples, immediately after reward. Its function is credit assignment: propagating the reward signal backward through the trajectory so each step that helped reach the reward has its value updated.

Pause on that, because it closes a loop from two chapters back. The temporal-difference error — the gap between expected and received reward, the quantity the dopamine cell fires for — needs a way to reach the states that *led* to the reward, not just the moment of reward itself. Reverse replay is that delivery mechanism. The dopamine burst fires at the reward. The hippocampus, in a ripple, re-traverses the just-completed path backward. Each state on the path flickers briefly back to life, and the value-updating machinery receives a coincident signal — *this state was on the road to the reward* — so the cached value of that state climbs a notch. One physical trajectory; dozens of value updates, propagated through the whole chain in a single ripple lasting under a tenth of a second.

Together the two forms give the hippocampus its role as a planning organ. Forward replay evaluates candidate futures. Reverse replay assigns credit to the past. The animal can sit still and do the mental work of navigation — weighing paths, updating values — at fifteen or twenty times the speed of physical experience, in the gaps between actual movements.

And Tolman's VTE is, on this account, the behavioral surface of forward replay. When the sweep runs down one candidate arm and then the other, the rat's head follows the simulated trajectory, turning toward each option as the simulation visits it. What looked like hesitation was the body partly executing the routes the hippocampus was projecting forward. The 1948 observation and the 2013 recording are looking at the same thing from opposite sides of the skull.

---

Let me trace one decision cycle end to end, because the forward and reverse halves are easy to describe apart and easy to lose together.

A rat arrives at a junction it has visited many times. To the left is a food location it has reached before. To the right is a novel arm it has never explored. It pauses.

During the pause, sharp-wave ripples fire. Place cells sweep left along the familiar arm, projecting the trajectory toward the known food, reading off the cached reward value at the end. Then the sweep runs right along the novel arm — where the place cells are weak from inexperience, and the sweep peters out without reaching a high-value endpoint. The comparison favors the left. The rat turns left. That is forward replay used as a policy evaluator: the model-based system running candidate futures through the spatial model and choosing the one whose simulated outcome is best.

The rat runs left. As it moves, place cells fire in the order of actual locations. No replay during locomotion — the system is executing, not simulating.

The rat reaches the food and eats. The dopamine system fires its burst — the prediction-error signal. Immediately, ripples fire again, sweeping backward from the food through each place field on the path, back to the junction. The prediction-error signal is propagated backward, nudging up the cached value of each place field that helped reach the reward.

What the two accomplish together: the forward replay evaluated the options without the rat physically trying both. The reverse replay updated the values from a single experience, without the dozens of repetitions a pure model-free learner would need. Together they let the model-based system behave adaptively after a handful of real experiences — padding real experience with simulated experience, prospective and retrospective, in the gaps between steps.

![A T-maze decision diagram: at the junction the rat pauses while forward place-cell sweeps (dashed) project down the familiar left arm toward known food and down the novel right arm where the sweep peters out; after the rat runs left and reaches reward, a red reverse-replay sweep runs backward along the taken path to assign credit.](images/08-simulation-planning-regret-fig-02.png)

*Figure 8.2 — In one decision cycle the hippocampus sweeps forward down each candidate arm to choose (dashed), then replays the taken path backward (red) to propagate the reward signal and update each step's value.*

---

Now back to the rat looking at the cherry station, and to a distinction that does a great deal of work.

*Disappointment* is a worse-than-expected signal. The outcome fell below prediction. It is a pure prediction error — the negative dopamine signal. Disappointment needs no representation of any alternative action. It needs only a representation of what was expected and what arrived.

*Regret* is more specific. The outcome is worse not merely because it fell below expectation but because *a better option was available and was not taken*. Regret requires the agent to represent the counterfactual — the option it could have chosen — and to compare its value with the actual outcome. Strip out the counterfactual and there is no regret. There is only disappointment.

Steiner and Redish built their analysis to pull the two apart, and the comparison turns on two kinds of bad outcome.

On a **regret-eligible** trial, the rat reaches the cherry station, which chimes a wait inside its cherry threshold — a good deal — and skips it. It arrives at the banana station, which chimes a wait above its banana threshold — a bad deal — and, stuck, accepts. Mid-wait at banana, the OFC and ventral-striatal neurons fire in the pattern they previously fired *at cherry*. The rat turns its head back toward cherry. On the trials that follow, it accepts longer waits than usual — threshold elevated, as if correcting the error — and it bolts the food it does get.

On a **disappointment** trial, the structure is different in the one way that matters. The rat reaches the chocolate station, which chimes a wait *above* its chocolate threshold — a bad deal — and correctly skips it. It arrives at the plain station, which also chimes above threshold — another bad deal — and accepts under duress. Mid-wait at plain, the neurons encoding chocolate do *not* fire above baseline. The rat does not look back. Its subsequent behavior shows no threshold elevation.

Both trial types end in a below-expectation outcome. Both produce a negative prediction-error signal the moment the rat realizes it is stuck with a bad deal. But only one — only the regret-eligible trial, the one where a genuinely *better* option was passed up — produces the look-back, the reactivation of the missed alternative in OFC and ventral striatum, and the policy update. On the disappointment trial, no better option was ever on the table. There is nothing to count as the road not taken, and the brain does not encode one.

So the OFC and the ventral striatum are not encoding *any* bad outcome. They are encoding the specific case where a better option was passed up. That joint reactivation is the neural signature of a counterfactual representation, distributed across a cortical region and a basal-ganglia region rather than localized to one spot — which is what you would expect of something that has to bind *where the rat could have been* to *how valuable that would have been*. The look-back is the behavioral signature. The elevated threshold on later trials is the policy update the counterfactual reasoning produced. Regret, in a rodent, is Pearl's third rung implemented in a circuit. The same dissociation has been reported in macaques. The capacity does not begin with us.

![A two-row comparison: in the regret-eligible trial the rat skips a good cherry deal, takes a bad banana deal, then a red look-back arrow shows OFC and ventral striatum replaying the cherry station, raising its threshold on later trials; in the disappointment trial the rat correctly skips a bad chocolate deal, takes a bad plain deal, and shows no look-back and no reactivation.](images/08-simulation-planning-regret-fig-01.png)

*Figure 8.1 — Only when a genuinely better option was passed up (top) does the rat look back and reactivate the missed station in red — the counterfactual that distinguishes regret from mere disappointment (bottom).*

And the limit, stated plainly: we still do not know whether rats *experience* regret or merely *compute* it. The OFC-and-striatum reactivation in the cherry pattern tells us the computation is running. It does not tell us what the computation feels like, or whether it feels like anything at all. I think it is more honest to say that and stop than to assume the rat has a rich inner life, or to assume it has none.

---

Consider a bird.

The western scrub-jay earns part of its living by caching food and recovering it later. Nicola Clayton and Anthony Dickinson, in a 1998 paper in *Nature*, established the memory component. Jays were given both wax-moth larvae — preferred when fresh, inedible once they have rotted — and peanuts, which keep but are less prized. After a short delay, the jays preferentially recovered the larvae; the fresh ones were still good. After a longer delay, they switched to the peanuts; the larvae had spoiled. The jays were integrating *what* they had cached, *where*, and *when*, and using all three together to decide what to dig up. Episodic-like memory, the first behavioral demonstration of it in any non-human animal.

The future-planning result followed, in Raby, Alexis, Dickinson, and Clayton's 2007 study, also in *Nature*. Jays were given experience that in one compartment of their housing, breakfast reliably failed to appear the next morning, while in another it reliably did. Then, one evening, *while sated* — with no current hunger to drive them — they were given food to cache freely. They cached more of it in the no-breakfast compartment. They were provisioning for a hunger they did not feel, in the place where they had learned that hunger would strike.

This mattered because of a hypothesis it broke. The *Bischof–Köhler hypothesis* held that non-human animals cannot plan for a motivational state different from their current one — that a sated animal cannot act for the benefit of a future hungry self, because it cannot represent that future state from the inside. The hypothesis was popular partly because it drew a clean line between human and non-human minds. The jays cached for a hunger they did not feel. The line, wherever it runs, does not run through this capacity.

Later work went further: jays re-cache their food in private after they have been *observed* caching, as though modeling what a watching thief now knows and acting to defeat that knowledge by moving the stash. The bird is representing what another agent knows about the bird's own past actions, and planning against that representation. We return to it in the next chapter.

Here is the theoretical weight for *this* chapter. The jay has no mammalian hippocampus in the anatomical sense, and no six-layered neocortex at all. What it has, in its forebrain, is a dorsal pallium whose subregions comparative neuroanatomy has matched to mammalian cortical areas by their connectivity and molecular markers. Two anatomically distinct neural systems. The same computation. Independent evolutionary origins in lineages that split more than three hundred million years ago.

That convergence is the most important theoretical result in the chapter. It tells us simulation is a *function*, not a *structure*. The mammalian hippocampal–prefrontal system and the corvid hippocampal-formation–nidopallium reached the same computational solution from different starting materials, because the function is valuable enough to be worth reaching twice. Any nervous system that needs to evaluate options not yet taken, plan for states not yet reached, and learn from alternatives not selected will be driven toward the same solution. The substrate is the variable. The function is the constraint.

---

An organism that can only learn from physical experience must meet every situation that matters at full biological cost and risk. It cannot adjust to a poisoned food source until it has been poisoned. It cannot evaluate an untried route until it has run it. It cannot recover from a missed opportunity until the missing has done enough harm to drag a value update through model-free retraining. That is the model-free ceiling.

An organism that can simulate can rehearse situations it has never been in, weigh options it has not tried, and adapt to a changed world without failing repeatedly first. The gain is qualitative, not incremental: a simulating agent can behave adaptively in environments it has never physically entered. That is what the rat does when it sweeps forward down an arm it has not yet run. That is what the jay does when it caches for a hunger it does not feel. That is what is happening when OFC and ventral-striatal neurons fire in the pattern of a station the rat has already left.

What simulation does not buy is the ability to simulate well *outside* the domain the machinery was built for. The corvid capacity has been documented most thoroughly in food caching — the high-stakes planning problem the species evolved to solve. Whether it generalizes to arbitrary planning is far less clear. The mammalian model-based system, sitting in a more anatomically generalized prefrontal–hippocampal network, appears to generalize more broadly. The depth and reach of simulation scale with the anatomical generality of the planning network, not merely with its presence.

And simulation can miscalibrate. Regret well-calibrated is genuinely useful: flagging the cases where a better option was available and the policy needs updating is exactly the feedback a model-based learner wants. But the same machinery that makes adaptive counterfactual reasoning possible makes pathological rumination possible. The rat's look-back is brief and produces an immediate correction; it does not linger. Human regret can persist far past the point where any policy update would still help. The difference lies partly in how the prefrontal cortex regulates *when* a simulation is shut down — a problem I only flag here.

There are two limits worth naming before the close. The whole regret argument leans on the claim that OFC and ventral striatum encode the *missed alternative* specifically. If a more careful re-analysis showed that reactivation tracking a perceptual feature of the previous station rather than its value, or showed it appearing on trials where no genuinely better option was passed up, the case for Pearl's third rung in the rat would weaken, and the argument would need rebuilding from a smaller base. And the forward-replay-causes-the-choice claim is, in the critical sense, correlational: the sweep predicts the route, but whether *removing* the sweep — by optogenetically disrupting the ripples at exactly the right instant — would change which route the rat picks is the intervention that would settle it. Disrupting awake ripples does impair memory-guided decisions in related work, but the clean experiment for *this* claim is technically hard, and not yet definitive.

---

This is where the human tool arrives. A pilot trainee climbs into a flight simulator and crashes an aircraft into a mountain — and walks away, because the aircraft and the mountain are a model, run forward in software at the trainee's command. The weather service runs an atmospheric model forward and tells you it will rain on Thursday, having flown a thousand simulated Thursdays it will never have to live through. An engineer runs a structural model of a bridge through a magnitude-eight earthquake that has not happened and may never happen, and learns whether the bridge would stand. In every case the move is the rat's move at the junction: run the world forward in a representation, read off the outcome, and act on the result without paying the cost of the real thing.

What the tool extends is forward replay — the candidate future evaluated before the body commits — pushed out of the skull and onto silicon, where the simulation can be faster, longer, and shared. The pilot's simulator is not faster than the rat's hippocampus by a factor of fifteen. It is faster by whatever a data center can manage, and it does not forget, and a thousand trainees can fly the same crash. The capacity is the same capacity. What changed is the scale and the substrate.

But the simulator inherits the rat's limit too, sharpened. A model is only as good as what it represents, and it will run confidently forward into outcomes its representation never captured. The flight simulator that omits a failure mode will train pilots to handle every emergency but that one. The forecast that misjudges the model will tell you Thursday with great precision and be wrong. The rat ruminating past the point of usefulness, the forecast confident past the point of accuracy — these are the same failure, which is the failure of any system that mistakes the richness of its simulation for the completeness of its model of the world. The capacity to run the world forward in your head is among the most powerful any nervous system ever evolved. It is powerful exactly to the degree that the model inside it is true, and it is silent about the difference.

---

## Sources

- Steiner, A. P., & Redish, A. D. (2014). "Behavioral and neurophysiological correlates of regret in rat decision-making on a neuroeconomic task." *Nature Neuroscience* 17: 995–1002.
- Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect.* Basic Books.
- Balleine, B. W., & Dickinson, A. (1998). "Goal-directed instrumental action: contingency and incentive learning and their cortical substrates." *Neuropharmacology* 37: 407–419.
- Adams, C. D., & Dickinson, A. (1981). "Instrumental responding following reinforcer devaluation." *Quarterly Journal of Experimental Psychology* 33B: 109–121.
- Tolman, E. C. (1948). "Cognitive maps in rats and men." *Psychological Review* 55: 189–208.
- Pfeiffer, B. E., & Foster, D. J. (2013). "Hippocampal place-cell sequences depict future paths to remembered goals." *Nature* 497: 74–79.
- Foster, D. J., & Wilson, M. A. (2006). "Reverse replay of behavioural sequences in hippocampal place cells during the awake state." *Nature* 440: 680–683.
- Ambrose, R. E., Pfeiffer, B. E., & Foster, D. J. (2016). "Reverse replay of hippocampal place cells is uniquely modulated by changing reward." *Neuron* 91: 1124–1136.
- Jadhav, S. P., Kemere, C., German, P. W., & Frank, L. M. (2012). "Awake hippocampal sharp-wave ripples support spatial memory." *Science* 336: 1454–1458.
- Clayton, N. S., & Dickinson, A. (1998). "Episodic-like memory during cache recovery by scrub jays." *Nature* 395: 272–274.
- Raby, C. R., Alexis, D. M., Dickinson, A., & Clayton, N. S. (2007). "Planning for the future by western scrub-jays." *Nature* 445: 919–921.
- Emery, N. J., & Clayton, N. S. (2001). "Effects of experience and social context on prospective caching strategies by scrub jays." *Nature* 414: 443–446.
- Abe, H., & Lee, D. (2011). "Distributed coding of actual and hypothetical outcomes in the orbital and dorsolateral prefrontal cortex." *Neuron* 70: 731–741.
