# Chapter 2 — Before Brains: The Cognitive Floor

In the year 2000, in a laboratory in Japan, a biologist named Toshiyuki Nakagaki laid a piece of yellow slime at the entrance of a plastic maze, set food at the exit, and waited.

The organism is *Physarum polycephalum*. It is the color of a school bus, can spread to the size of a dinner plate, and has no mouth, no eyes, no neurons, and no brain. It is a single cell — one continuous, pulsing bag of cytoplasm with millions of nuclei sloshing through a network of tubes it builds out of itself. Within hours of being set down, it had crept into every passage of the maze, every dead end, every wrong turn. Then it began to withdraw. Branch by branch, the exploratory tubes thinned and vanished. When the experiment was over, the mold had pulled its entire body into a single thick channel tracing the shortest path between the two food sources. Of nineteen trials, it found the shortest or near-shortest route in fourteen.

No plan. No map. No nervous system. A cell, and a problem solved.

A decade later, in 2010, Atsushi Tero and colleagues ran the experiment at the scale of a country. They placed oat flakes at the geographic positions of the cities around Tokyo, used bright light as a repellent to stand in for mountains and water, and let *Physarum* connect the dots. Over about a day, the network the mold built matched the actual Tokyo rail system in efficiency, in cost, and in fault tolerance — the qualities human engineers had spent a century tuning. The mold reached something close to their answer in roughly twenty-six hours, with no engineers and no engineering.

I start here because of the question this chapter is built around: *what is the minimum a decision requires?* Not a brain. Not a nervous system. Those came later, and the first systems that decided things predate them by billions of years. I want to know what the floor looks like — the smallest thing that counts as a real choice rather than a mere mechanism. If we cannot see the floor, we cannot see what everything built on top of it actually added.

---

A reflex is not a decision. Your knee jerks when the doctor's hammer taps the tendon. Input in, output out, fixed; the input determines the output every time, regardless of what came before. No comparison happens. No past is weighed against a present.

A decision *varies*. The same stimulus can produce different responses depending on what has happened before. That is the line that matters, and it turns out a real decision — not a metaphorical one — requires exactly four things.

**Sensing.** Some access to the world: a way of turning an external state — a chemical concentration, a pressure, a temperature, a wavelength of light — into an internal signal the system can act on. Without sensing there is nothing to decide about.

**Memory.** The ability to compare *now* with *a moment ago*. This matters more than it sounds. A system that knows only the present cannot tell whether things are getting better or worse; it is frozen at a single instant, like a photograph. Memory turns the snapshot into a movie, and only a movie tells you which way you are travelling.

**Integration.** The ability to weigh signals together over time — not just "how much sugar is here right now" but "what has been happening to the sugar over the last few seconds, and what does the trend mean?" Integration is where the comparison becomes a verdict.

**Variable response.** The output has to be able to change. A system that always does the same thing regardless of input is not deciding; it is executing. Variation is what lets the decision bind to the analysis.

Give the four ingredients a name for what they compute together: **valence**. The word is borrowed from chemistry, where it describes combining power; here it means the approach-or-avoid property of a stimulus. Food has positive valence, toxin negative. Valence is not a judgment, and it may or may not involve any feeling. It is simply a sorting — move toward this, away from that — and without it no preference is possible, and without preference no goal. The whole story of cognition, from bacteria to human beings, is the story of making valence faster, richer, more flexible, more accurate. It begins here.

---

Now the precise version, because precision is where understanding lives.

Imagine you are an *E. coli* bacterium. One cell, swimming in a chemical soup that holds amino acids — food — and copper ions that will kill you. You cannot steer. You have no rudder and no fins. What you have is a flagellar motor at your tail, and it spins two ways: counterclockwise gives you a smooth forward run; clockwise flings your filaments apart and tumbles you into a random new direction. Your life is run, tumble, run, tumble. A drunkard's walk.

But the drunkard is not stumbling at random. In 1972, Howard Berg built a microscope that could track a single bacterium through three-dimensional space, and watching for hours he saw the pattern: the runs were *longer* when the cell happened to be heading toward food. The drunk was finding his way to the bar — not by knowing where it was, but by walking longer in the right direction whenever he stumbled onto it.

![A jagged path crossing a faint left-to-right food gradient from a low-food start toward a high-food source, made of straight runs punctuated by sharp tumble reorientations; one long run climbing toward the source is drawn in red and labeled "run extended," and the path as a whole drifts uphill despite never aiming directly at the source.](images/02-before-brains-cognitive-floor-fig-01.png)

*Figure 2.1 — The run-and-tumble walk net-drifts up a gradient the cell cannot perceive directionally, simply by extending runs (red) whenever conditions are improving.*

This is **chemotaxis** — from *chemo*, chemical, and *taxis*, directed movement: motion guided by a chemical gradient.

The mechanism begins at the cell surface, studded with receptor proteins called methyl-accepting chemotaxis proteins, or MCPs. When an attractant binds, the receptor changes shape, and that shift propagates inward and inhibits a kinase called CheA. A kinase's job is to hang a phosphate group onto a target; CheA's target is a small messenger protein, CheY. Phosphorylated CheY — CheY-P — drifts to the flagellar motors and pushes them toward clockwise rotation. Clockwise means tumble. So: more attractant, receptor activated, CheA inhibited, less CheY-P, less tumbling, longer runs.

That part is clean, and it supplies two of the four ingredients — sensing, in the receptor that reads the world, and variable response, in the motor that switches as a function of the signal. But this cascade alone responds only to the *current* concentration. A cell that read only the present level would tumble just as happily sitting in the middle of a rich food patch as at its edge, because the level is high in both. It would have no way to know whether it was surrounded by food or merely approaching it. It would lose all sense of direction. The cascade alone does not navigate. To navigate, the cell needs memory.

The memory lives in two more enzymes: **CheR** and **CheB**. CheR adds methyl groups to the MCP receptors; CheB removes them. Methylation changes the receptor's sensitivity, and — this is the trick — these two enzymes work on a *slower* timescale than the binding cascade. So the receptor's current sensitivity is a record of the recent average concentration. When the present level rises above that baseline — things getting better — the cell runs. When it drops below — things getting worse — CheA fires, CheY-P climbs, and the cell tumbles. This is **methylation memory**: a slow chemical mark on a protein that holds the running average of recent inputs. It is memory in the same functional sense your hippocampus is, only shorter and smaller.

In 1986, Segall, Block, and Berg measured the exact window by pulsing bacteria with attractant. The cell weighs its chemical experience over the past four seconds, with the most recent second weighted positively and the prior three weighted negatively. Which is to say: the cell computes a derivative. It responds to the *change* in concentration over time, not the level. It is doing differential calculus with two enzymes and a methylation rate.

![A step plot of weight against time before the present, divided into four one-second bins; the most recent second carries a positive bar drawn in red and the three earlier seconds carry progressively smaller negative bars below the zero line, so the kernel subtracts the recent past from the present and yields a trend rather than a level.](images/02-before-brains-cognitive-floor-fig-02.png)

*Figure 2.2 — The cell weights the most recent second positively (red) and the prior three negatively, computing the change in concentration — a derivative — rather than its absolute level.*

The four-second window is not arbitrary. It is matched to how far the cell can swim in a single run before Brownian buffeting randomizes its heading. A longer memory would be memory of a self that no longer exists — the cell would be comparing its present to a position it can no longer point back toward. The window is tuned to the physics of the bacterium's world.

This is what makes it a decision and not a reflex. The reflex responds to a *level*. The decision responds to a *trend*. The reflex cannot tell which way things are going; the decision can.

To see that memory is doing all the work, take it out. Knock out CheR and CheB — delete the two methylation enzymes — and the cell is still alive, still swimming, still responding to attractant; the CheA–CheY-P cascade still runs. Drop the mutant into a gradient and it will still bias its flagella where the concentration is high. But it cannot navigate. Its random walk stays random. It runs longer in rich zones, but it cannot tell *whether* things are improving, so it does not preferentially run toward the source. The drunkard in the rich zone is now just a drunkard who does not want to leave. Three of the four ingredients are intact — it senses, it responds, it integrates in a limited way — and the one that is missing, memory, the comparison of present to past, is the one that makes directed behavior possible. This is the **knockout test**, and the book will use it again and again: if you want to argue an ingredient is necessary, remove it and watch what breaks.

---

Now the same logic in a wholly different material.

*Physarum*, the slime mold, runs the same four-ingredient computation through a body that is a web of cytoplasmic tubes rather than a single swimming cell. The logic is architectural instead of molecular. Cytoplasm sloshes back and forth through the tubes in rhythmic pulses, and the rule is simple: tubes carrying high, sustained flow grow thicker; tubes carrying low flow thin and disappear. When food is detected at a node, local oscillations shift their phase, flow toward the food increases, that channel is reinforced, and the network reorganizes around it. This — strengthening high-flow channels, pruning low-flow ones — is **flow-based network pruning**, and the same idea returns later in this book when we reach the pruning of synapses in nervous systems.

The maze solution falls straight out of that one rule. Every route gets explored; the mold fills the maze. Dead-end branches carry no net flow, because there is no food at the end of them, so they thin and retract. The shortest path carries the most sustained flow, because it links the two food sources with the least detour, so it is the last tube standing. No planning, no map — just the physics of flow and reinforcement.

Nakagaki, describing his result, was careful with the word *intelligence*; he tended to prefer *smart*, a term Western reporters did not object to in the way they objected to *intelligence*. (Treat that as the gist of his public stance rather than a verbatim quotation.) The slime mold computes. Whether the computing amounts to intelligence depends on what you decide intelligence means — the problem of Chapter 1, met again. The mechanism, at least, is not in doubt.

The mold's memory is worth pausing on, because some of it sits outside the body. Part is internal: the flow channels themselves record which routes have paid off — thick tubes mean recent high flow, thin tubes recent low flow, the body its own ledger. But *Physarum* also lays down a trail of extracellular slime wherever it has already been, and it tends to avoid that slime on later forays. Reid and colleagues demonstrated this in 2012: a mold whose own trail was hidden from it took far longer to escape a trap than one that could read where it had already searched. The memory is not molecular; it is written into the environment. This is an ancient trick that turns out to be universal — encode past behavior in a physical mark that future behavior can read. Ants do it with pheromones. Beavers do it with dams. Humans do it with cities and books. *Physarum* did it before any animal.

External memory scales with the size of the explored space, not the size of the body, which is its great advantage. But it is public: anything in the environment can read it. A trail is information your competitors can use against you. Internal memory is private; external memory is broadcast. Every memory system pays that trade somewhere.

What I want you to see is not just that two organisms solve similar problems, but that they solve them with the *same logical structure* built from completely different materials. The bacterium runs its memory in methylation reactions on membrane proteins; the slime mold runs its memory in cytoplasmic flow and a trail of slime. The computation — sense, remember, integrate, respond variably — is identical. The substrate is not. This is **substrate independence**: the function is the thing, the substrate merely the medium. The brain, when we get to it, is not running some unique kind of computation. It is running these same ancient computations faster, with more parameters, in a different material.

---

One more case, because it shows a mechanism you will meet again in a very different setting.

The Venus flytrap, *Dionaea muscipula*, has a sharp problem to solve: close on insects, but not on rain. Closing is expensive, and a trap that snapped at every raindrop would exhaust itself and starve. The solution is a counting rule. Inside the trap, fine trigger hairs each fire an electrical pulse — an action potential — when bent. One pulse does nothing. Two action potentials within roughly thirty seconds snap the trap shut. And the trap keeps counting: around five action potentials, generated as a trapped insect struggles, switch on the genes for digestive glands and sodium uptake. The plant, in a real sense, counts to five.

Jennifer Böhm, Sönke Scherzer, and Rainer Hedrich's group traced the mechanism to calcium. Each action potential drives a spike of calcium inside the trap's cells. Calcium decays over time as pumps clear it, but it does not fall all the way back before the window closes, so a second spike adds to the residue of the first. Only when the summed calcium crosses a threshold does the trap fire. The calcium concentration *is* the short-term memory; the threshold *is* the decision rule. The trap counts by exploiting the fact that calcium decays more slowly than the interval between the twitches of struggling prey.

This kind of mechanism — a signal that climbs with each event and leaks away between them — is a **leaky integrator**. *Integrator* because it sums incoming events; *leaky* because the running total decays in the gaps. The leaky version is more useful than a perfect one because it forgets old events on its own. Leaky integrators run all through neuroscience, where they describe how some neurons pile up evidence before firing a decision. The flytrap is doing the same thing, in ionic calcium, with no neurons at all.

And its integration window, like the bacterium's four seconds, is calibrated to the statistics of the signal it must catch. Insects move in irregular, rapid jerks — two contacts in thirty seconds is the signature of struggling prey. Rain falls more evenly and rarely lands twice on the same hair inside the window. The physics of the problem sets the memory. This is always true: the right timescale for memory is the one that matches the structure of the signal you need to read. We will meet that principle again when we ask how long working memory should run in a primate, or how long a context window should be in a language model.

---

I need to be honest about the frontier of this literature, because some of its most-cited claims have not held up.

Two famous demonstrations of plant cognition are now in dispute. Monica Gagliano's 2014 study reported that *Mimosa pudica*, the sensitive plant, habituated to repeated drops and held the habit for a month; Robert Biegler argued the data could be explained by ordinary sensory adaptation or motor fatigue, and the disagreement was never settled by clean independent replication. Gagliano's 2016 study claimed pea plants learned to associate the direction of a fan with the direction of light — classical conditioning — but Kasey Markel's blinded replication in 2020 found no effect.

The responsible position: habituation is well demonstrated in *Physarum*, and not yet well demonstrated in plants. The flytrap's calcium counting is a real mechanism. The rest needs more work before I will assert it. The pattern of overreach here is worth naming, because it recurs throughout the study of minds. There is always a careful claim — *the organism produces a behavior characteristic of X* — and an inflated one — *the organism experiences X the way we do*. The careful claim is often supported. The inflated one is almost never established, and stating it as fact is not scientific boldness; it is a failure to tell evidence from enthusiasm. I will try to hold that line through the whole book, and you should hold me to it.

---

Everything described so far is *functional* cognition. It says nothing about whether the bacterium feels anything. When I say the bacterium *decides*, I mean only that its output depends on a comparison of present state to remembered state — not that there is something it is like to be an *E. coli* computing a derivative. The question of inner experience is real, and it returns in Chapter 5 when we reach valence and affect in animals with nervous systems. Here it is set aside. The four-ingredient floor is a claim about computation, not about consciousness.

It is also a claim that could be wrong, and I want to say how. The framework would fail if some substantial class of organisms reliably reached environmental goals while genuinely lacking one of the four ingredients — say, an organism that climbed a gradient with no internal state held across time at all, pure stimulus-response with the comparator experimentally ruled out, yet measurable drift uphill. The bacterial knockout experiments are the strongest current evidence the other way: delete the memory enzymes and gradient navigation cleanly disappears. If a careful study found brainless navigation with memory ruled out, I would downgrade the model from *architectural minimum* to *one common implementation among others*. I also do not yet know how cleanly the four ingredients separate when the substrate fuses them — in *Physarum*, sensing and memory may live in the same flow network with no line between them. The clean strip-and-test that works in *E. coli* may not apply when the parts are materially welded together. That is part of what the next chapter, on the worm, lets us test.

---

There is a human-built version of this floor on the wall of nearly every house, and it is worth ending on, because it shows how rare the full architecture still is.

Consider first the things that fall short. In 1909, the chemist Søren Sørensen, working at the Carlsberg Laboratory on the chemistry of fermentation, gave us a way to put a number on acidity — the pH scale. Dip a strip, read a color, compare to a card: a single-point measurement of valence, this batch is fine or too sour, approach or adjust. It says nothing about whether the acidity is rising or falling, nothing about the trend. The modern pH electrode does better, turning hydrogen-ion concentration into a continuous voltage — but still no trend, still no comparison to the recent past. A sensor without a decision. The smoke detector on your ceiling is the same shape: an excellent one-step sensor with a reliable threshold, and it saves lives, but it would tumble at random in a chemical gradient, because it has no memory of whether the particle level is rising. That is exactly why it shrieks when you make toast. It reads the absolute level, not the trend.

Now the thing that completes the loop. A blood-glucose monitor logs history and can plot a trend on your phone — but the trend is for *you* to act on; the monitor itself closes no loop on the world. A closed-loop insulin pump does close it: it senses glucose, holds a history, computes a delivery rate, and acts. That device runs all four ingredients. It is, in its algorithmic shape, doing what *E. coli* has done for billions of years, on the same logic, with very different stakes.

| System | Sensing | Memory | Integration | Variable response |
| --- | --- | --- | --- | --- |
| Litmus paper | yes | no | no | no |
| pH electrode | yes | no | no | no |
| Smoke detector | yes | no | partial (threshold) | yes (alarm) |
| Blood-glucose monitor | yes | yes (logged) | partial (trend display) | no (reports only) |
| Closed-loop insulin pump | yes | yes | yes | yes |
| *E. coli* chemotaxis | yes | yes (methylation) | yes (derivative) | yes (run/tumble) |

The step that turns a sensor into a decision-maker is the **temporal derivative**: not "what is the level of X" but "how is the level of X changing relative to recent experience." Most instruments still stop one step short. The bacterium took that step billions of years ago, with two enzymes, in a picogram of cytoplasm — and the same logic now hangs on the wall as a thermostat, the cheapest decision-maker most of us own. The thermostat senses temperature, holds a set-point, compares the room to that remembered target, and acts to close the gap. Sense, remember, compare, respond. It is the control loop in its plainest form, the bacterium's trick rendered in a bimetallic strip and a switch — and it sits there in the hallway, deciding, hundreds of times a day, in a way the smoke detector beside it never quite manages to.

---

## Sources

- Nakagaki, T., Yamada, H. & Tóth, Á. (2000). "Maze-solving by an amoeboid organism." *Nature* 407:470.
- Tero, A. et al. (2010). "Rules for Biologically Inspired Adaptive Network Design." *Science* 327(5964):439–442. (Tokyo rail comparison; ~26 h network formation.)
- Berg, H. C. & Brown, D. A. (1972). "Chemotaxis in *Escherichia coli* analysed by three-dimensional tracking." *Nature* 239:500–504.
- Segall, J. E., Block, S. M. & Berg, H. C. (1986). "Temporal comparisons in bacterial chemotaxis." *PNAS* 83:8987–8991. (The ~4-second weighting window.)
- Reid, C. R., Latty, T., Dussutour, A. & Beekman, M. (2012). "Slime mold uses an externalized spatial 'memory' to navigate in complex environments." *PNAS* 109:17490–17494.
- Böhm, J., Scherzer, S. et al. (2016). "The Venus Flytrap *Dionaea muscipula* Counts Prey-Induced Action Potentials to Induce Sodium Uptake." *Current Biology* 26(3):286–295. (Two APs close the trap; ~5 trigger digestion.)
- Hedrich, R. & Neher, E. (2018). "Venus Flytrap: How an Excitable, Carnivorous Plant Works." *Trends in Plant Science* 23(3):220–234.
- Gagliano, M. et al. (2014). *Oecologia* 175:63–72 (*Mimosa* habituation); Biegler, R. (2018), *Oecologia* (critique).
- Gagliano, M. et al. (2016). *Scientific Reports* (pea-plant conditioning); Markel, K. (2020). "Lack of evidence for associative learning in pea plants." *eLife* 9:e57614.
- Sørensen, S. P. L. (1909). Introduction of the pH scale, Carlsberg Laboratory.
