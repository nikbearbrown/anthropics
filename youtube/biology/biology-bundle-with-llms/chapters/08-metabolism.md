# Chapter 8 — Metabolism: How Life Stays Improbable
*The accounting trick that keeps cells alive.*

---

Here is something that bothered me for a long time.

The second law of thermodynamics says the universe tends toward disorder. Entropy increases. Things spread out, cool down, randomize. A drop of ink in a glass of water diffuses until the color is uniform. A hot cup of coffee loses heat to the room until both are the same temperature. You cannot reverse either process without doing work — without importing energy from somewhere else.

A living cell is, by this logic, an outrage. It is concentrated. It is organized. Its proteins fold into precise shapes. Its DNA is coiled and sorted. Its ions are pumped into gradients — more sodium outside, more potassium inside — against the natural tendency of things to even out. Everything about a living cell is an offense against the second law.

And yet cells exist. And they do not violate the second law. So what is actually going on?

The answer is that the second law applies to *closed* systems — systems that do not exchange energy with their surroundings. A cell is not a closed system. It is ferociously open. It takes in food, burns it, exports heat and waste, and uses the energy flowing through it to maintain its local improbability. The cell does not cheat entropy. It exports it. The universe's disorder increases — all the waste heat and carbon dioxide the cell breathes out — and the cell stays ordered by making its surroundings more disordered.

<!-- → [IMAGE: Two side-by-side panels — left: a sealed aquarium with no organisms, arrows showing molecules diffusing toward equilibrium, labeled "closed system: trending to maximum entropy"; right: a cell with arrows showing energy/food entering and heat/waste exiting, labeled "open system: exporting entropy, maintaining local order"] -->

Once you see this, everything else about metabolism falls into place. This chapter is about the three mechanisms that make it work: how the cell decides which reactions are allowed, how it pays for the ones that are not, and how it makes the whole thing fast enough to matter.

---

## Which Reactions Are Allowed

Every chemical reaction inside a cell involves moving energy around. Bonds break, bonds form, molecules rearrange. Some of these reactions release energy to the surroundings — burning glucose, breaking down fat. Others require energy from somewhere else — building proteins, copying DNA.

The question is: how do we know which is which?

The physicist Josiah Willard Gibbs worked this out in the 1870s. He was interested in a practical question: given a chemical reaction, can I predict whether it will happen spontaneously? Not how fast. Not how to make it happen. Just: if I leave these molecules alone, will they react?

His answer was a single number. We call it the change in Gibbs free energy, written ΔG. The equation is:

$$\Delta G = \Delta H - T\Delta S$$

Let me unpack each piece.

ΔH is the change in enthalpy — roughly, the total energy change. When bonds break, energy is released. When bonds form, energy is stored. If a reaction releases more energy breaking bonds than it uses forming new ones, ΔH is negative: the reaction gives off energy. If it costs more to form the new bonds than was released, ΔH is positive: the reaction requires energy input.

ΔS is the change in entropy — the change in disorder. If a reaction produces more disorder (one large molecule breaks into many small ones, a crystal dissolves, a concentrated gradient disperses), ΔS is positive. If a reaction creates order (small molecules assemble into a large one, scattered ions gather into a crystal), ΔS is negative.

T is the absolute temperature in Kelvin. It scales how much the entropy term matters.

<!-- → [TABLE: Four-quadrant summary of ΔG outcomes — rows: ΔH negative / ΔH positive; columns: ΔS positive / ΔS negative — each cell showing whether the reaction is always spontaneous, never spontaneous, or temperature-dependent, with a one-line biological example in each quadrant] -->

Now the rule: if ΔG is negative, the reaction is exergonic — it releases usable energy and will happen spontaneously. If ΔG is positive, the reaction is endergonic — it requires an energy input and will not happen on its own.

The equation says something subtle. A reaction can be exothermic (ΔH negative, releasing heat) but still not happen if the entropy change is sufficiently unfavorable. Or a reaction can absorb heat from the surroundings (ΔH positive) and still proceed spontaneously if it creates enough disorder. Temperature shifts the balance: at high enough temperatures, the entropy term dominates and reactions that increase disorder become favorable regardless of their enthalpy.

Here is an example. Dissolving ammonium nitrate in water is endothermic — the flask gets cold. You put energy in. And yet the dissolution is spontaneous (ΔG < 0). Why? Because the entropy increase is enormous. One ionic solid becomes a solution of many freely diffusing ions. The TΔS term overcomes the unfavorable ΔH. At room temperature, the reaction proceeds.

This is not a trick. This is the equation working as intended.

Now apply it to a cell. Building a protein is endergonic — ΔG is positive. Joining amino acids into a chain creates order, decreases entropy, and requires energy. The reaction will not happen on its own. Breaking down glucose is exergonic — ΔG is strongly negative. Burning a sugar molecule to carbon dioxide and water creates disorder, releases energy. This will happen.

The cell's entire strategy is to link these two facts together. Use the exergonic reactions to power the endergonic ones. But how, exactly? The energy released by burning glucose does not teleport across the cell to where a protein is being assembled. There has to be a mechanism.

That mechanism is ATP.

---

## The Energy Coupon

ATP stands for adenosine triphosphate. It is a nucleotide — one of the building blocks of RNA — but the cell has recruited it for a second job: energy currency.

The molecule has three phosphate groups chained together. The bonds between the phosphate groups are high-energy. When you break the bond between the second and third phosphate, releasing one phosphate group (this is called hydrolysis), you get a significant release of free energy:

$$\text{ATP} + \text{H}_2\text{O} \rightarrow \text{ADP} + \text{P}_i + \text{energy}$$

Under cellular conditions, this releases about 14 kilocalories per mole. ΔG is negative. ATP hydrolysis is exergonic.

<!-- → [IMAGE: Structural diagram of ATP showing adenosine, ribose, and the three phosphate groups in a chain — the bond between the second and third phosphate highlighted and labeled "high-energy bond, ~14 kcal/mol released on hydrolysis"; ADP and Pi shown as the hydrolysis products] -->

So here is the trick. The cell takes that exergonic reaction — ATP hydrolysis — and mechanically couples it to an endergonic reaction. The two reactions share an intermediate. The energy released by one directly drives the other. This is not a metaphor. It is a molecular mechanism. The phosphate group does not float off and release energy into the medium. It transfers to another molecule, changing that molecule's energy state, enabling a reaction that would not otherwise happen.

The clearest example I know of is the sodium-potassium pump.

Every cell in your body maintains a gradient: more sodium ions outside the cell than inside, more potassium ions inside than outside. This gradient is essential — nerve cells use it to fire, muscle cells use it to contract, and the existence of the gradient across the membrane drives many other transport processes. But maintaining a gradient costs energy. Ions want to diffuse down their concentration gradients, from high concentration to low. Pumping them the other way is endergonic.

The pump is a protein that sits in the cell membrane. In each cycle, it pushes three sodium ions out and pulls two potassium ions in. To do this, it uses one ATP molecule.

Here is how the coupling works. The ATP approaches the pump. The pump hydrolyzes the ATP, but instead of releasing the phosphate freely, the phosphate attaches to the pump itself — the pump gets phosphorylated. This changes the pump's shape. The new shape binds three sodium ions from inside the cell and positions them to be ejected outward. The sodium ions are released outside. Then the pump binds two potassium ions from outside. The phosphate detaches. The pump returns to its original shape. The potassium ions are released inside.

One ATP. Three sodium out, two potassium in. The pump is reset and ready for another cycle.

<!-- → [INFOGRAPHIC: Five-step cycle diagram of the sodium-potassium pump — step 1: ATP binds and phosphorylates the pump; step 2: pump changes shape, binds 3 Na+ from cytoplasm; step 3: Na+ ejected outside; step 4: pump binds 2 K+ from outside; step 5: phosphate released, pump returns to original shape, K+ released inside — each step labeled with the conformational change and the ion movement, with the net result (3 Na+ out, 2 K+ in, 1 ATP spent) shown as a summary] -->

The accounting: ATP hydrolysis releases ~14 kcal/mol. Pumping the three sodium ions against their gradient costs ~6 kcal/mol. Net ΔG is negative. The reaction is exergonic overall. It proceeds.

This is what "coupling" means. The exergonic reaction and the endergonic reaction share a physical intermediate — the phosphorylated pump — so the energy does not get lost. The thermodynamics of the whole coupled system is what matters, and the whole is favorable.

The cell does this everywhere. Every time it needs to drive an unfavorable reaction, it couples it to ATP hydrolysis. Building a protein: ATP couples to each peptide bond formation. Replicating DNA: ATP drives the assembly of nucleotides. Moving a flagellum: ATP-powered motor proteins convert chemical energy to mechanical rotation.

ATP is the cell's universal energy coupon. It is not the energy source — glucose is the energy source. ATP is the transfer mechanism. Energy extracted from glucose breakdown is captured as ATP. ATP is then spent, wherever needed, to drive endergonic processes.

One detail worth sitting with: ATP is unstable. Left alone in water, it spontaneously hydrolyzes. The very exergonicity that makes it useful also makes it a ticking clock. Cells do not stockpile ATP. They regenerate it continuously, on demand, using the energy from food. This is why you cannot stop eating. The moment you stop supplying glucose and oxygen, ATP regeneration slows, and the cell's ability to drive endergonic processes collapses. That is what cell death is, at one level: the ATP budget running to zero.

---

## Why It Needs to Be Fast

Here is a fact that seems, at first, to wreck everything I just said.

The combustion of glucose is exergonic. ΔG is strongly negative — around -686 kilocalories per mole. By everything the Gibbs equation says, glucose should burn. Spontaneously. In your cells, at body temperature.

It does not. You can put glucose powder in water at 37°C and nothing happens. It sits there for years.

The Gibbs free energy equation tells you whether a reaction will happen. It does not tell you how fast. A reaction can be thermodynamically favorable — ΔG < 0 — and still be uselessly slow if the molecules cannot get over the energy barrier required to begin reacting.

That barrier is called the activation energy.

Think of it this way. You have a boulder sitting in a small depression at the top of a hill. The bottom of the hill is lower in energy — it is where the boulder wants to be, thermodynamically. But to get there, the boulder first has to be lifted slightly out of the depression, over a small lip. The final destination is downhill. But the first step is uphill. Without enough energy to clear that lip, the boulder stays put, metastably, for a long time.

Glucose is the boulder. The activation energy is the lip. The cell needs to get glucose over that barrier, quickly, at 37°C, in water, without combustion.

The cell's solution is enzymes.

An enzyme is a protein that catalyzes a chemical reaction. What it does, precisely: it lowers the activation energy. It finds a lower-energy path to the transition state — the intermediate configuration the molecules must pass through. The final destination is the same. The starting point is the same. ΔG is unchanged. The thermodynamic verdict does not change. But the energy required to get there drops dramatically, and reactions that would take years without a catalyst happen in milliseconds.

<!-- → [CHART: Reaction energy diagram — x-axis: reaction progress; y-axis: free energy — two curves on the same axes: one tall activation energy peak (no enzyme), one shorter peak (with enzyme); both curves have the same starting energy and ending energy, and the same ΔG (shown as the drop from start to finish); the difference between the two peaks is labeled "activation energy lowered by enzyme"] -->

How does an enzyme lower activation energy? By providing an environment that stabilizes the transition state.

An enzyme has an active site — a pocket, usually deep inside the protein, shaped precisely for its substrate. When the substrate molecule approaches, the enzyme does not just mechanically clamp onto it. The enzyme changes shape slightly. The substrate changes shape slightly. The induced fit model — developed by Daniel Koshland in the 1950s — describes how both the enzyme and substrate are subtly deformed to achieve maximum complementarity at the transition state. The enzyme's active site is not shaped for the substrate; it is shaped for the substrate halfway through the reaction, at the highest-energy intermediate.

<!-- → [IMAGE: Side-by-side comparison of lock-and-key model (rigid enzyme active site, substrate snaps in unchanged) vs. induced fit model (enzyme and substrate both deform slightly toward each other, achieving better complementarity at the transition state) — labeled to show that induced fit is the evidence-supported model] -->

The amino acids lining the active site are arranged to weaken exactly the bonds that need to break. Some of them are acidic and donate protons; others are basic and accept them. Some create a locally hydrophobic environment; others provide electrostatic stabilization. The active site is a precisely engineered microenvironment for catalysis.

This specificity has a consequence: each enzyme works on a narrow range of substrates. An enzyme that cuts a specific peptide bond will not cut a different one. An enzyme that adds a phosphate to glucose will not add it to galactose. The cell runs hundreds of metabolic pathways simultaneously — glycolysis, the citric acid cycle, fatty acid synthesis, amino acid biosynthesis — and they do not interfere with each other because each enzyme recognizes only its specific substrate.

The selectivity comes from shape and charge. A substrate must fit the active site in three dimensions, with the right complementary charge distribution. Change one functional group on the substrate and the affinity drops drastically. This is why a molecule of the wrong chirality — the mirror-image version — will often not work at all with the same enzyme, even though its molecular formula is identical. The enzyme reads the shape, not the formula.

---

## The Thermostat

Now the cell has a problem on the other end. It can run metabolic reactions fast. ATP is available. Glucose is being burned. But how does the cell avoid burning all its glucose at once? How does it avoid building up enormous amounts of ATP that then spontaneously hydrolyze uselessly?

The answer is feedback inhibition, and it is one of the most elegant mechanisms I know.

Glycolysis is the metabolic pathway that breaks glucose down into pyruvate, producing ATP in the process. It involves about ten steps, each catalyzed by a different enzyme. One of the early enzymes — the third step — is called phosphofructokinase, or PFK. PFK catalyzes the conversion of fructose-6-phosphate to fructose-1,6-bisphosphate. This is the committed step: after PFK acts, the molecule is committed to going all the way through glycolysis.

PFK has a second binding site, separate from its active site. This is an allosteric site — a site that, when occupied, changes the enzyme's shape and alters its activity without blocking the substrate directly. And what binds to this allosteric site? ATP.

When ATP concentrations in the cell are high, ATP binds to PFK's allosteric site. This changes PFK's shape in a way that reduces its affinity for fructose-6-phosphate. PFK slows down. Glycolysis slows down. The cell stops producing more ATP — because it already has enough.

When ATP concentrations are low and ADP concentrations are high (because ATP has been spent), ADP binds to PFK's allosteric site instead and acts as an activator. PFK speeds up. Glycolysis accelerates. More ATP is produced.

The product of the pathway inhibits an enzyme at the beginning of the pathway. This is feedback inhibition: the end product reaching back and tapping the brakes on its own production. It is a biological thermostat. When the house is warm enough, the heater shuts off. When it gets cold, the heater turns back on.

<!-- → [INFOGRAPHIC: Glycolysis shown as a vertical cascade of reaction boxes (steps 1–10) with ATP produced at the bottom — a curved arrow from the ATP product looping back to step 3 (PFK), labeled "feedback inhibition: high ATP slows PFK"; a second arrow from ADP looping to step 3, labeled "activation: low ATP / high ADP speeds PFK" — student should see that the pathway regulates itself without a central controller] -->

What I find remarkable is that no central controller is needed. There is no cell-wide energy monitor that surveys ATP levels and sends signals. The regulation is local and automatic. PFK sits in the cytoplasm, surrounded by ATP and ADP. When ATP is high, it binds and slows. When ATP is low, ADP binds and speeds. The system is self-regulating, driven purely by the concentrations of molecules the pathway itself produces.

<!-- → [IMAGE: Side-by-side comparison of competitive inhibition (inhibitor molecule blocks the active site directly, competing with substrate) vs. allosteric inhibition (inhibitor binds a separate site, induces a conformational change that distorts the active site) — labeled to show that ATP inhibits PFK allosterically, not competitively] -->

This principle — allosteric regulation, feedback inhibition, local self-correction — repeats throughout metabolism. Almost every pathway has a committed step, and almost every committed step is allosterically regulated by the pathway's products. It is not a coincidence. It is an engineering solution that evolution converged on independently multiple times.

---

## Putting It Together

Return to the puzzle I started with. A living cell is locally improbable — ordered, concentrated, gradient-maintaining — in a universe that tends toward disorder. How?

Here is the complete picture.

The cell is an open system. It imports high-energy molecules — glucose, fats — that were built using energy from the sun. It breaks those molecules down in exergonic reactions, reactions where ΔG is strongly negative. The energy released is not wasted as heat. It is captured in ATP.

ATP is the coupler. It takes the exergonic and links it to the endergonic. Building proteins, pumping ions, copying DNA — all these are endergonic processes that the cell must run. ATP hydrolysis, coupled mechanically to these processes, provides the energy. The total ΔG of each coupled reaction is negative. Each coupled reaction proceeds.

Enzymes make everything fast enough to be useful. Without enzymes, the activation energies are too high and the reactions are too slow. Enzymes lower those barriers. They do not change the thermodynamic verdict. They just make the thermodynamically favorable reactions happen on biological timescales.

Feedback inhibition prevents the system from running out of control. When ATP is abundant, the pathways that make ATP slow down automatically. When ATP is scarce, they speed up. The cell regulates its own energy metabolism without a master controller.

<!-- → [INFOGRAPHIC: Full synthesis diagram — glucose entering on the left; glycolysis cascade in the center producing ATP; ATP feeding out to three labeled processes (protein synthesis, ion pumping, DNA replication) each shown with an endergonic arrow made favorable by ATP coupling; feedback inhibition arrow from ATP back to PFK; waste products (CO2, heat) exiting to the right — the whole diagram enclosed in a cell boundary with "open system" labeled, entropy arrows pointing outward] -->

The cell does not defeat entropy. It exploits it. It funnels entropy outward — exhaling CO₂, excreting waste, radiating heat — and uses the energy flowing through it to stay organized. The universe's entropy increases. The cell's entropy stays low. The second law is satisfied. Life continues.

When I first worked through this carefully, what struck me was not the complexity. It was the economy. Three mechanisms — thermodynamic favorability, ATP coupling, enzyme catalysis — are enough to explain how an open system can maintain improbability indefinitely. Everything else in metabolism is elaboration on those three principles.

The cell is not magic. It is physics, run very cleverly, at very small scales, very fast.

---

## Exercises

**Warm-up**

1. A reaction has ΔH = −50 kJ/mol and ΔS = +100 J/(mol·K). At 300 K, calculate ΔG and determine whether the reaction is exergonic or endergonic. Show your work. *Tests: applying the Gibbs equation.*

2. Explain in your own words why a reaction can be thermodynamically favorable (ΔG < 0) yet not occur at room temperature. What determines whether it actually happens? *Tests: distinguishing thermodynamic favorability from kinetics.*

3. ATP hydrolysis releases ~14 kcal/mol under cellular conditions. If the sodium-potassium pump spends one ATP per cycle and pumping three sodium ions costs ~6 kcal/mol, what happens to the remaining energy? Where does it go? *Tests: energy accounting in coupled reactions.*

**Application**

4. Protein synthesis requires forming peptide bonds between amino acids — an endergonic reaction. Describe, using the Gibbs free energy framework, how ATP coupling makes this possible. What is the physical intermediate that links the two reactions? *Tests: applying coupling logic to a new context.*

5. An inhibitor drug blocks the active site of PFK directly, competing with fructose-6-phosphate for binding. A second drug binds to PFK's allosteric site and freezes the enzyme in a low-activity conformation. Both drugs slow glycolysis. What is the mechanistic difference between them? How would you distinguish their effects experimentally? *Tests: competitive vs. allosteric inhibition.*

6. Cells maintain a roughly constant ratio of ATP to ADP. During intense exercise, this ratio drops sharply. Using what you know about feedback inhibition of PFK, predict what happens to glycolysis during exercise. Then predict what happens in the minutes after exercise stops. *Tests: applying feedback regulation to a physiological scenario.*

**Synthesis**

7. A cell in a closed system would reach chemical equilibrium and die. A living cell in an open system stays far from equilibrium. Use the concept of entropy and the second law of thermodynamics to explain why both statements are true simultaneously, and why they are not contradictory. *Tests: integrating thermodynamics and the open-system logic of life.*

8. Design an alternative energy currency for cells. It must be transferable, portable, capable of coupling exergonic to endergonic reactions, and regenerable. What molecular properties would it need? What would it trade off compared to ATP? *Tests: reasoning from principles rather than memorized facts.*

**Challenge**

9. ATP is unstable — it spontaneously hydrolyzes in water. This seems like a design flaw. Argue that it is actually a feature. What would go wrong if ATP were highly stable and resisted hydrolysis? *Tests: reasoning about the functional consequences of molecular properties.*

10. Feedback inhibition of glycolysis by ATP is allosteric: ATP binds away from the active site and induces a conformational change. Why might evolution have favored allosteric regulation over simple competitive inhibition (where ATP would block the active site directly)? What does the allosteric mechanism allow that competitive inhibition would not? *Tests: open-ended reasoning about evolutionary design logic.*

---

## LLM Exercises

The following exercises are designed for use with a large language model. Paste the prompt into any capable model and examine the response critically — not for correctness alone, but for whether the reasoning is mechanistic or merely verbal.

**Exercise 1 — Why ATP, not ADP or AMP**
Prompt a model: *"ATP is the universal energy currency. Why is the third phosphate bond — the one hydrolyzed to release energy — particularly suited to this role? Engage with the electrostatic repulsion between adjacent phosphate groups, the resonance stabilization of the released phosphate, and the favorable hydration of the products. Then explain why cells sometimes use GTP instead and what the energetic cost of switching currencies is."*

Evaluate whether the model engages with the actual chemistry (phosphate-phosphate repulsion, resonance, hydration) rather than vaguely citing "high-energy bonds." The phrase "high-energy bond" is a teaching shortcut — the energy comes from the products' stability, not from the bond's intrinsic energy.

**Exercise 2 — Coupled reactions, on the page**
Prompt: *"The reaction glucose + Pᵢ → glucose-6-phosphate has a positive ΔG of about +13.8 kJ/mol — it is energetically unfavorable. Yet cells perform it routinely. Walk me through how coupling this reaction to ATP hydrolysis (ΔG ≈ -30.5 kJ/mol) makes the combined reaction favorable, and explain why the coupling requires the same enzyme molecule (hexokinase) rather than two separate enzymes acting in sequence. What is the kinetic significance of having the two reactions occur on the same active site?"*

Evaluate whether the model correctly computes the net ΔG of approximately -16.7 kJ/mol and engages with the enzymatic coupling — both reactions must occur in a single active site to ensure the released energy is captured rather than dissipated as heat.

**Exercise 3 — Enzymes and the activation-energy gap**
Prompt: *"An uncatalyzed reaction has an activation energy of 60 kJ/mol. An enzyme reduces it to 25 kJ/mol. Estimate, using the Arrhenius equation [Ea/RT scaling], the order-of-magnitude speedup the enzyme provides at body temperature (310 K). Then identify three distinct mechanisms by which enzymes lower activation energy: substrate orientation, transition-state stabilization, and induced fit. Which of these is most consequential for most enzymes?"*

Evaluate whether the model correctly applies the Arrhenius scaling (the speedup is approximately e^((60-25)×1000/(8.314×310)) ≈ e^13.6 ≈ 800,000-fold — the LLM may approximate; check the order of magnitude) and whether it distinguishes the three mechanisms rather than collapsing them into "lowering the energy barrier."

**Exercise 4 — Allosteric regulation as feedback control**
Prompt: *"In glycolysis, the enzyme phosphofructokinase-1 (PFK-1) is allosterically inhibited by ATP and citrate, and activated by AMP and fructose-2,6-bisphosphate. Trace the logic: why does each of these regulators make sense as a control input? Specifically, what does each signal tell PFK-1 about the cell's energy state, and how does the regulatory architecture prevent the cell from running glycolysis when energy supplies are already adequate?"*

Evaluate whether the model correctly identifies ATP as a signal of energy abundance (inhibitor), AMP as a signal of energy depletion (activator), and citrate as a signal that the citric acid cycle is saturated (inhibitor). Push for engagement with the rationale: regulation at PFK-1 is the committed step of glycolysis, so regulating here prevents wasted downstream investment.

**Exercise 5 — The thermodynamic case for catabolism**
Prompt: *"Cellular respiration releases approximately 686 kcal of free energy per mole of glucose oxidized [verify]. Cells capture roughly 30-32 ATP per glucose, with each ATP equivalent to about 7.3 kcal/mol — meaning the cell captures roughly 220-235 kcal of the 686 kcal as usable energy. Walk me through where the rest goes (heat, primarily), and why the second law of thermodynamics requires that some energy be lost. Could a cell ever achieve 100% efficiency? Why or why not?"*

Evaluate whether the model correctly computes the efficiency (approximately 32-34%, comparable to a modern internal combustion engine) and engages with the second-law argument: any spontaneous reaction must increase the universe's entropy, which requires that some energy be released as heat.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Gerty Cori** and her husband Carl worked out the Cori cycle — how muscle lactate becomes liver glucose — and were jointly awarded the 1947 Nobel Prize. She was the first American woman to win a Nobel in science.

**Run this:**

```
Who was Gerty Cori, and how does the Cori cycle connect to the metabolism we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Gerty Cori"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to trace one molecule of lactate through the Cori cycle from working muscle to liver and back to muscle.
- Add a constraint: "Answer including the institutional resistance the Coris faced because Gerty was a woman — and how it shaped where they worked."

What changes? What gets better? What gets worse?
