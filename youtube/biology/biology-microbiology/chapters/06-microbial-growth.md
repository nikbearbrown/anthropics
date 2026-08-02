# Chapter 6 — Microbial Growth


## TL;DR

- How a phone call turned a safe piece of meat into a dangerous one — and why the math behind it is the same math behind septic shock.
- The chapter moves through The equation, and what it means, The four-phase growth curve, Measuring the population, Worked example — from a blood culture to a treatment decision, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*How a phone call turned a safe piece of meat into a dangerous one — and why the math behind it is the same math behind septic shock.*

---

A culinary student sets a pound of ground beef on the counter at 22 °C while she takes a phone call. The call runs four hours. When she comes back, the meat looks the same. Smells the same. She rinses it and starts cooking.

Let me show you what happened while she was on the phone.

Ground beef leaving the grinder carries a small but reliable population of bacteria — somewhere between 10 and 100 colony-forming units per gram. Call it 10 cells per gram for round numbers. The dominant organisms are mesophiles: they prefer body temperature but grow respectably at room temperature. Call the doubling time at 22 °C twenty minutes.

Four hours is 240 minutes. Twenty minutes per doubling means twelve doublings in four hours. After *n* doublings:

$$N = N_0 \cdot 2^n$$

Plug in *N₀ = 10* and *n = 12*:

$$N = 10 \cdot 2^{12} = 10 \cdot 4{,}096 \approx 41{,}000 \text{ cells/gram}$$

Now extend the same call to six hours. Eighteen doublings:

$$N = 10 \cdot 2^{18} = 10 \cdot 262{,}144 \approx 2.6 \times 10^6 \text{ cells/gram}$$

A pound of meat is 454 grams. Total bacterial load: somewhere over a billion cells. Nothing to see. Nothing to smell. A billion bacteria.

Now consider a different scene. A patient arrives in the emergency department with chills. Their blood culture shows *E. coli* at 100 CFU/mL. There are five liters of blood in a human adult, so the total bloodstream burden is about half a million cells. The attending physician orders antibiotics. The lab will call back in 18 to 48 hours with the organism's identity and drug sensitivities.

Here is what happens during those 48 hours if the antibiotics are wrong or arrive late. In a bloodstream with a generous doubling time of one hour — the immune system is fighting, so it is slower than broth — six hours gives six doublings:

$$N = 100 \cdot 2^6 \approx 6{,}400 \text{ CFU/mL}$$

That is the difference between a patient who is starting to feel cold and a patient in septic shock. By the time the lab calls with the culture result, the population has, on the doubling-time clock, become unrecognizable.

![Exponential growth comparison ](images/06-microbial-growth-fig-01.png)
*Figure 6.1 — Exponential growth comparison *

This chapter is about the mathematics, machinery, and environmental switches behind that arithmetic. The math is simple. What it implies is not.

---

## The equation, and what it means

Bacteria reproduce by **binary fission**. One cell becomes two. The mechanism: duplicate the chromosome, elongate, build a wall across the middle, split. Parent and daughters are genetically identical. No aging cell is left behind — the parent doesn't survive to watch; it becomes the offspring.

Three things about this matter for everything that follows.

First, it is *symmetric*. The parent does not produce offspring while persisting. It becomes them. There is no clock ticking on a separate parent cell, getting older while its children divide.

Second, it is *exponential*. Every cell capable of dividing contributes to the next round. The population multiplies rather than adds. This is why bacterial growth surprises people — our intuitions are calibrated for additive processes. Income adds. Bacteria multiply. The math of compound interest and the math of bacterial growth are the same math.

Third, it is *fast when conditions are favorable*. *E. coli* in warm broth divides every 20 minutes. *Vibrio natriegens*, the fastest known bacterium, divides every 10 minutes. *Mycobacterium tuberculosis* divides every 18 to 24 hours. That range — 10 minutes to 24 hours — covers six orders of magnitude in daily growth rate. The doubling time of a pathogen is not a number to report and move on; it is the timescale on which the infection evolves.

The basic formula:

$$N = N_0 \cdot 2^{n}$$

where *n* is the number of generations elapsed. Since *n = t/g* (elapsed time divided by generation time):

$$N = N_0 \cdot 2^{t/g}$$

To compute generation time from measurements, rearrange with logarithms:

$$g = \frac{t \cdot \log_{10}(2)}{\log_{10}(N/N_0)} \approx \frac{0.301 \cdot t}{\log_{10}(N/N_0)}$$

We will use this formula in the worked example. It is the one calculation in this chapter worth putting in your notes.

![Generation-time formula derivation in three steps ](images/06-microbial-growth-fig-02.png)
*Figure 6.2 — Generation-time formula derivation in three steps *

---

## The four-phase growth curve

Put a small number of cells into a sealed flask of broth, hold temperature constant, and watch the population. You always get the same shape. It has four phases. The shape is robust enough that you can use deviations from it as a diagnostic — something is unusual if the curve does not look like this.

![Four-phase bacterial growth curve ](images/06-microbial-growth-fig-03.png)
*Figure 6.3 — Four-phase bacterial growth curve *

**Lag.** After inoculation, the cell count does not rise. The cells are alive. They are not dormant. They are synthesizing the enzymes they need for the current medium, repairing damage accumulated in the previous environment, and rebuilding ribosome pools that were let go during nutrient deprivation. They are getting ready to divide. They have not started.

The length of lag depends on how different the new conditions are from the old. Cells moved from one log-phase culture to another in the same medium often have no measurable lag. Cells from a long-stationary culture transferred to fresh broth may lag for hours. Cells coming out of a freezer vial may lag overnight. The clinical analogue: a bacterium inoculated into a wound from a skin reservoir spends time adapting before it begins replicating. The lag is the window during which prompt cleaning and prophylactic antibiotics are most effective.

**Log (exponential) phase.** The cells begin dividing at the maximum rate the conditions permit. Cell number doubles every *g* minutes. On a log-scale y-axis, the population versus time is a straight line. That is what "exponential" looks like in the language of graphs: a straight line on a log scale.

This phase is where microbiologists do their work. Log-phase cells are metabolically vigorous, reproductively reliable, and behaviorally reproducible. It is also the phase where antibiotics work best — because almost every antibiotic targets a process that only happens in actively dividing cells. Beta-lactams target cell wall synthesis. Fluoroquinolones target DNA replication. Macrolides and aminoglycosides target the ribosome during active translation. A cell that is not synthesizing wall, replicating DNA, or actively translating is much harder to kill. This is important enough that I will say it again in the misconceptions section.

**Stationary.** The line flattens. The population reaches a density at which the rate of new cell production equals the rate of cell death. Total count stays roughly constant. The reasons are usually some combination of nutrient depletion, waste accumulation (acid from fermentation, alcohols, organic acids), and quorum-sensing-mediated gene-expression changes that down-regulate growth and up-regulate stress responses.

For *E. coli* in standard broth, stationary phase typically peaks around 10⁹ cells per milliliter. That number is approximate and medium-dependent, but it is the right order of magnitude.

Stationary is not metabolically silent. Cells are still respiring, synthesizing, maintaining themselves. Some are still dividing — balanced by other cells dying. The misconception that "stationary" means "stopped" is one of the most common in introductory microbiology, and it matters: a patient's bloodstream is not a batch flask, and cells in stationary phase are still doing things.

**Death.** Eventually the death rate exceeds the birth rate. The viable population declines. The decline is typically exponential too — a straight line on a log scale, now sloping down. Some bacteria form dormant structures (spores, persisters) that can survive for days to decades. Many simply die. The population can collapse to a tiny fraction of its peak.

---

## Measuring the population

To plot a growth curve you need to count cells. There is no single right way. There are four standard methods, each measuring something slightly different — and confusing them produces wrong answers with high confidence.

**Colony-forming units (CFU) on a plate.** Dilute the culture serially, spread a known volume on agar, incubate, count colonies. Each colony came from one viable cell. Multiply by dilution factor to get CFU per milliliter. This is the gold standard for clinical work — when a urine culture reports 10⁵ CFU/mL as the threshold for a UTI diagnosis, that number came from this method. The advantage: it counts only cells capable of growing. The disadvantage: it counts only cells capable of growing on this medium under these conditions. Anaerobes don't grow on aerobic plates. Fastidious organisms don't grow on standard media. Environmental samples typically contain 100 to 1,000 times more cells visible by microscopy than will form colonies. Most environmental bacteria are unculturable. Speed: slow. Most clinical pathogens take 18–48 hours; *Mycobacterium* takes weeks.

**Turbidity (OD600).** Shine 600 nm light through the culture. The cloudier the culture, the more light it scatters, the higher the optical density the spectrophotometer reports. For *E. coli* in rich broth, OD600 of 1.0 corresponds to roughly 8 × 10⁸ cells/mL. Fast — seconds per reading. The disadvantage: it does not distinguish live from dead. Cellular debris scatters light. Dead cells scatter light. A culture killed by a bactericidal antibiotic may show no change in OD for hours after the cells have lost viability. OD measures *biomass*, not *viability*.

**Direct microscopic count.** Load a known volume into a counting chamber etched with a grid of squares of known dimensions, count cells under the microscope. Fast. Measures all cells — live, dead, and intermediate. The right method when you want total cell load regardless of viability. Tedious at low densities.

**Most probable number (MPN).** A statistical method used in water quality testing when the cells of interest may be rare. Replicate dilutions are scored as growth or no growth; a probability table converts the pattern into an estimated density. Slow, but designed for large volumes with sparse target cells.

| method | what it counts | speed | when to use |
| --- | --- | --- | --- |
| CFU (viable cells | 1–14 days | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| OD600 (total biomass | seconds | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| direct microscopic count (all cells | minutes | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |
| MPN (viable cells statistical | 1–7 days | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

The most expensive mistake: treating OD600 and CFU as interchangeable. They measure different things. When you need to know how many live cells remain after antibiotic treatment, OD is wrong. When you need to monitor an actively growing culture in real time, CFU is slow and OD is fine. The method is part of the answer.

---

## Worked example — from a blood culture to a treatment decision

A clinical lab receives a blood sample drawn at 14:00. At 16:00, an aliquot is plated for CFU: the count is 3,200 CFU/mL. At 20:00, another aliquot is plated: the count is 100,000 CFU/mL.

**Question 1.** What is the generation time of this organism in the bloodstream culture?

$$g = \frac{0.301 \cdot t}{\log_{10}(N/N_0)}$$

- *t* = 4 hours = 240 minutes
- *N/N₀* = 100,000 / 3,200 = 31.25
- log₁₀(31.25) ≈ 1.495

$$g = \frac{0.301 \times 240}{1.495} = \frac{72.24}{1.495} \approx 48 \text{ minutes}$$

Sanity check: 240 minutes ÷ 48 minutes per generation = 5 generations. 3,200 × 2⁵ = 3,200 × 32 = 102,400 ≈ 10⁵. The arithmetic is self-consistent.

**Question 2.** A second patient arrives with the same organism at 50 CFU/mL. Fever typically begins when bloodstream bacterial load crosses roughly 10⁴ CFU/mL — the point at which bacterial products circulating at that density trigger a detectable systemic immune response. At the generation time we just calculated, how long until this patient becomes febrile?

Solve *N = N₀ · 2^(t/g)* for *t*:

$$t = g \cdot \log_2\!\left(\frac{N}{N_0}\right) = 48 \cdot \log_2\!\left(\frac{10^4}{50}\right) = 48 \cdot \log_2(200)$$

log₂(200) = log₁₀(200) / log₁₀(2) = 2.301 / 0.301 ≈ 7.64

$$t \approx 48 \times 7.64 \approx 367 \text{ minutes} \approx 6.1 \text{ hours}$$

About six hours.

**The clinical implication.** Conventional blood culture results take 18 to 48 hours to complete — time for the bottle to flag positive, the subculture to grow, the organism to be identified, susceptibility testing to finish. By the time the lab calls, the patient's bloodstream bacterial load has gone through 22 to 60 doublings. Waiting for the culture result before starting treatment is not a conservative choice. It is an arithmetic choice with known consequences.

This is why severe sepsis is treated empirically: a broad-spectrum antibiotic is given immediately on clinical suspicion, before the lab has identified anything. Empiric therapy is sometimes wrong about the specific organism. It gets adjusted when the result returns. The adjustment is reasonable. The alternative — waiting six to twelve hours for a definitive result while the population doubles every 48 minutes — is not.

!["The culture result arrives too late" ](images/06-microbial-growth-fig-04.png)
*Figure 6.4 — "The culture result arrives too late" *

**The limit.** The exponential math is a useful prediction for the first several hours of an untreated infection. It is not a prediction for what happens twelve hours in. The bacterium eventually hits stationary phase — the bloodstream is not a flask, but it is a finite environment with finite glucose and amino acids. The immune system is killing cells throughout. And at some bloodstream density, the body's response — vascular collapse, organ failure — ends the experiment before any carrying capacity is reached. The four phases are real; the log phase does not run forever.

---

## The four environmental switches

A bacterium grows within an envelope of physical and chemical conditions. Outside that envelope, the growth rate drops toward zero. Four variables define the envelope: temperature, pH, oxygen, and water activity.

**Temperature.** Microbes are sorted by the temperature range they tolerate:

*Psychrophiles* prefer below 15 °C — polar oceans, deep sea, your refrigerator if you are unlucky. Their membrane lipids are enriched in unsaturated fatty acids that stay fluid near freezing. *Psychrotrophs* grow at 4 °C but prefer warmer temperatures — *Listeria monocytogenes* is the clinical example, and it is why listeriosis is associated with refrigerated deli meats. *Mesophiles* prefer 25–45 °C; essentially every clinical pathogen is a mesophile with an optimum at or near 37 °C, which is not a coincidence. *Thermophiles* prefer above 45 °C. *Hyperthermophiles* — mostly archaea — top out above 80 °C, with the current record at 122 °C held by *Methanopyrus kandleri* strain 116. [verify: current temperature record]

The clinical implication of the temperature distribution: most pathogens grow fastest at the temperature inside you. Fever — raising body temperature one to three degrees — is not just inflammation. It is the immune system nudging the thermometer away from the pathogen's optimum. The fever response is the host using temperature as a growth-rate switch.

**pH.** Most bacteria prefer pH between 6 and 8. *Acidophiles* thrive below 5 — *Lactobacillus* prefers pH 4–5, which is why healthy vaginal and gut microbiomes are protective against pathogens: the acid environment those organisms create falls outside most pathogen envelopes. *Helicobacter pylori* survives at the pH of stomach contents (1.5–4.0) by producing urease, which generates ammonia and locally neutralizes acid around the cell — a beautiful trick, because the urea substrate is supplied by normal host physiology. *Neutrophiles* — the large clinical middle — prefer pH 6–8. Food preservation by pickling, fermenting, and adding vinegar works by pushing pH below the neutrophile floor.

**Oxygen.** This dimension has the most categories because oxygen is simultaneously a valuable substrate (for aerobic respiration) and a toxic one (it generates reactive oxygen species). The categories that matter clinically:

*Obligate aerobes* require oxygen — *Mycobacterium tuberculosis*, most fungi, *Pseudomonas aeruginosa*. *Obligate anaerobes* cannot tolerate oxygen — *Clostridium*, *Bacteroides*. They live in the large intestine, anaerobic abscesses, and deep wounds. *Facultative anaerobes* use oxygen when available but switch to fermentation when it is not — *E. coli*, most enterobacteria, *Saccharomyces*. This metabolic flexibility is part of why these organisms dominate clinical infection. *Microaerophiles* need oxygen but only at low concentrations — *Helicobacter pylori*, *Campylobacter*. *Aerotolerant anaerobes* ferment regardless and merely survive in oxygen — *Lactobacillus*, *Streptococcus*.

The diagnostic consequence: anaerobes do not grow on aerobic culture plates. When a patient has an abdominal abscess, a deep wound, or a dental infection, the lab must be specifically requested to set up anaerobic cultures. Otherwise *Bacteroides* from the abscess will not appear in the report and the clinician will treat for the wrong organism.

![Oxygen requirement spectrum ](images/06-microbial-growth-fig-05.png)
*Figure 6.5 — Oxygen requirement spectrum *

**Water activity.** Microbes need water — but at what solute concentration? The technical measure is *water activity* (*a_w*): the ratio of the vapor pressure of water in the substrate to pure water. Pure water = 1.0. Adding solute lowers *a_w*. Fresh meat is around 0.99. Dried fruit around 0.70. Honey around 0.60. Most pathogens require *a_w* > 0.91. *Staphylococcus aureus* tolerates down to 0.86, which is unusually low and explains its association with salted and cured foods. Yeasts and molds tolerate lower still. Food preservation by drying, salting, sugaring, and concentrating all work by pushing *a_w* below the organism's floor.

| organism | temp optimum (°C) | temp floor | ceiling | pH optimum |
| --- | --- | --- | --- | --- |
| E. coli, S. aureus, Clostridium perfringens, Listeria monocytogenes, Mycobacterium tuberculosis, Helicobacter pylori. Student should return to this table after the simulator exercise and check whether the simulator's parameters match. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## Biofilms — where the growth-curve model breaks down

If you imagine a bacterium, you probably imagine a single cell swimming freely through liquid. Most bacteria in nature are not doing that.

A **biofilm** is a structured, surface-attached community of cells embedded in a self-produced matrix of polysaccharides, proteins, and extracellular DNA. The matrix glues cells to a surface and to each other. The community develops three-dimensional architecture — cells in different layers experience different oxygen levels, different nutrient concentrations, different waste accumulation. They specialize accordingly. The result is not a collection of independent cells that happen to be touching. It is a community with division of labor.

Biofilm formation is the dominant lifestyle for most environmental bacteria. And it is the failure mode for a large fraction of clinical infections. Costerton and colleagues estimated in 1999 that more than 65% of human infections involve biofilm communities. [verify]

Biofilm cells are 10 to 1,000 times more resistant to antibiotics than the same bacteria growing in planktonic culture. Four reasons:

The matrix slows antibiotic diffusion. Drugs reach deep cells at reduced concentrations. Cells deep in the biofilm grow slowly because nutrients are limited there — and antibiotics that target dividing cells (most antibiotics, especially beta-lactams) are less effective on slow-growing cells. A subset of cells called *persisters* enter dormant metabolic states that virtually no antibiotic can touch. And the close cell-cell contact inside a biofilm accelerates horizontal gene transfer of resistance genes.

![Cross-section diagram of a mature biofilm on a](images/06-microbial-growth-fig-06.png)
*Figure 6.6 — Cross-section diagram of a mature biofilm on a*

The clinical picture: any indwelling medical device is a biofilm risk. Urinary catheters, central venous lines, prosthetic heart valves, prosthetic joints — anything that sits in the body with a colonizable surface. Once a biofilm establishes, antibiotic therapy alone rarely clears it. The standard recommendation is surgical: remove the device, debride the tissue, replace the prosthesis.

The growth curve we have been drawing is a *planktonic* growth curve — for cells swimming freely in liquid. A biofilm community generates a completely different curve, with different kinetics and different antibiotic susceptibility. The four-phase model we have been building is accurate and useful for planktonic cells. It is the wrong model for biofilm infections, and the wrong model is what makes device-associated infections so hard to treat.

---

## Three misconceptions worth naming explicitly

**"Log phase is the most dangerous phase clinically."** This is precisely backwards. Log phase is the most antibiotic-susceptible phase. Cells in log phase are actively synthesizing cell wall, replicating DNA, translating proteins. Most antibiotics target one of those processes. A cell that is not doing them is harder to kill. The clinical paradox is that the patient feels worst when the bacterial load is highest — late log, early stationary — but the drugs work best when the population is still in early log. Start therapy early. This is the arithmetic reason behind "don't wait for the culture result."

**"Stationary phase means no metabolism."** No. Stationary means the rate of cell production equals the rate of cell death. The total count is flat; the turnover is not zero. Cells in stationary are actively respiring, synthesizing (different proteins than log-phase cells — stress-response regulons, in *E. coli* controlled by the sigma factor RpoS), repairing damage, and in some species entering persister states. The curve looks flat because births and deaths balance. Plenty is happening; it is balanced out.

**"OD600 and CFU measure the same thing."** They do not. OD600 measures light scattering from everything in the culture — live cells, dead cells, debris. CFU counts only cells capable of growing on that plate under those conditions. A culture treated with a bactericidal antibiotic may show no OD change for hours after the cells have lost viability. When the question is "how many live cells are there?", OD is wrong. When the question is "is this culture actively growing?", OD is fast and fine.

---

## LLM Exercise — Extend your simulator

This exercise extends `00-growth-curve.html` from Chapter 0. You should have that file running. If you don't, go back to Chapter 0 first.

**Output file:** `06-growth-simulator.html`
**Tool:** Cowork, or Claude.ai, or any LLM that produces a single-file D3 v7 build.

### The four-move prompt

**Show.** *"Read CLAUDE.md and DESIGN.md from this project. Also read `00-growth-curve.html` — the new file extends it. Conform to all three."*

**Say.**

```
Build 06-growth-simulator.html — a bacterial growth-curve simulator
with environmental controls. Start from the logistic-growth-with-lag-
and-death core of 00-growth-curve.html and add the following.

Sliders:
- Temperature (0 to 80°C, default 37). Each organism has an optimum
  temperature and a tolerance window; outside the window, effective r
  drops smoothly toward zero (Gaussian or piecewise-linear — comment
  which is used).
- pH (4.0 to 10.0, default 7.0). Same logic.

Selectors:
- Oxygen atmosphere: aerobic / microaerobic / anaerobic.
- Organism — four choices:
    E. coli (facultative anaerobe; T opt 37, pH opt 7, td 20 min)
    S. aureus (facultative anaerobe; T opt 37, pH opt 7, td 30 min,
               grows at a_w down to 0.86)
    C. perfringens (obligate anaerobe; T opt 43, pH opt 6.5,
                    td 8 min under ideal anaerobic conditions)
    L. acidophilus (aerotolerant anaerobe; T opt 37, pH opt 5.5,
                    td 90 min)

Toggle:
- Biofilm mode — when enabled: curve flattens at a lower K, lag
  phase lengthens, and a separate "antibiotic susceptibility"
  indicator (0–100%) drops by roughly 100-fold relative to
  planktonic.

Display: growth curve animates in real time as sliders move. Readout
shows current effective td and effective r. A banner reads "optimal
conditions" (green) when all four environmental knobs are inside the
organism's preferred window, and shows "most limiting factor" (amber)
when any knob is outside.
```

**Constrain.**

```
Use Euler integration, dt = 0.1 min, log y-axis, 0 to 8 hours —
same as 00-growth-curve.html. Temperature and pH fall-off functions
must produce r → 0 at the edges of the slider range so the curve
actually flattens. Biofilm toggle must change both the displayed
curve and the antibiotic-susceptibility readout. Use the existing
color palette from DESIGN.md. Single self-contained HTML, D3 v7
from CDN, no other dependencies.
```

**Verify.**

```
Biology check — three falsifiable claims the simulator must satisfy:

1. Setting organism to C. perfringens under aerobic atmosphere must
   produce r = 0 (flat curve).
2. Setting organism to L. acidophilus at pH 5.5, temperature 37,
   anaerobic atmosphere must produce td within 10% of 90 minutes.
3. Enabling biofilm mode must reduce antibiotic susceptibility by
   at least 100-fold compared to planktonic mode for the same
   organism and atmosphere.

After every parameter change, print to the console: organism,
temperature, pH, oxygen, biofilm state, effective r, effective td,
susceptibility percent. Add a comment at the top of the script:

// CLAIM: Effective growth rate is the product of intrinsic r and
// the fitness multipliers from temperature, pH, and oxygen.
// Biofilm mode reduces both growth rate and antibiotic
// susceptibility relative to planktonic.
```

### Exploration tasks

Once it runs, work through these.

1. **The pathogen sweep.** For each of the four organisms, find the combination of temperature, pH, and oxygen that produces the fastest doubling time the simulator allows. Are the optimal conditions different for each? Map your answers against the chapter. Where the simulator disagrees with the textbook — it will — articulate the disagreement. The disagreement is a feature, not a bug.

2. **The refrigerator test.** Set organism to *Listeria monocytogenes*... you will notice it is not in the dropdown. Add it. (Extend the prompt: "Add *Listeria monocytogenes* — psychrotroph, temperature optimum 30 °C but grows down to 4 °C, pH optimum 7.0, facultative anaerobe, doubling time 60 min at optimum.") Set temperature to 4 °C and watch the curve. How long does it take to go from 10² to 10⁵ CFU/g? What is the food-safety implication?

3. **The biofilm comparison.** Add *Pseudomonas aeruginosa* (temperature optimum 37, pH optimum 7, obligate aerobe, generation time 30 min). Run two simulations side by side: planktonic and biofilm. Where do they diverge? Does the divergence point match what you would predict from the matrix-diffusion explanation above?

### Extension to Chapter 7

Chapter 7 turns to the genome: DNA replication, transcription, translation. The connection to growth is direct — every binary fission requires a complete copy of the genome. Doubling times shorter than the time required to replicate the genome require a trick: initiating new rounds of replication before the old ones finish. That trick has consequences for genome biology. The extension prompt for the next chapter will add a **genome replication clock** to the simulator: every doubling triggers a replication event of stated duration, and you will be able to see when the replication clock starts running before the previous round finished.

Get the environmental controls and biofilm toggle working first. Sweep the parameters. The simulator's value is not faithful reproduction of any specific organism — it is the ability to see the *shape* of how environmental constraints control growth, and to carry that intuition into clinical contexts where the constraints matter.

---

**What would change my mind.** If single-cell techniques applied to a representative panel of clinical isolates *in vivo* showed that infections rarely traverse anything resembling the four canonical phases — instead exhibiting continuous low-grade replication with no identifiable lag, log, stationary, or death structure — the four-phase framework would need to be demoted from "model of microbial growth" to "model of microbial growth in batch culture," and the chapter would need a new spine for in-vivo dynamics. [verify: state of single-cell microbial growth dynamics literature as of 2026]

**Still puzzling.** I do not fully understand why a clonal population — genetically identical cells in identical medium — produces persister cells at the rates it does. Stochastic gene expression is part of the answer. But the rate is reproducible across experiments even though the individual events appear stochastic. The reproducibility of a stochastic process is itself a puzzle.

---

*Binary fission copies the chromosome once per division. That sounds simple, but the genome has to be fully replicated before the cell can split, and at the fastest doubling times — 20 minutes for *E. coli* — the chromosome takes longer than 20 minutes to copy. How the cell handles that contradiction is Chapter 7.*

---

## Exercises

### Warm-up

**1.** A culture of *Pseudomonas aeruginosa* is plated for CFU at two time points: *t = 0* gives 2.0 × 10⁴ CFU/mL; *t = 2 hours* gives 3.2 × 10⁵ CFU/mL. Calculate the generation time. Show your work using the formula in the chapter. *(Tests: generation-time calculation.)*

**2.** For each food item below, predict whether *Staphylococcus aureus* will grow, grow slowly, or fail to grow, and name the single most limiting factor: (a) country ham, *a_w* = 0.87, 15 °C, aerobic; (b) fresh chicken breast, *a_w* = 0.99, 37 °C, aerobic; (c) honey, *a_w* = 0.60, 25 °C, aerobic. *(Tests: water activity and temperature as growth switches.)*

**3.** A microbiologist monitors a culture by OD600 over four hours and reports a smooth upward curve with no plateau. She concludes the culture is still in log phase throughout. A lab partner runs CFU plates at the two-hour and four-hour marks and finds the viable count is unchanged between them. How do you reconcile these two observations? What is the most likely explanation? *(Tests: OD vs. CFU, what each measures.)*

### Application

**4.** A patient with a prosthetic knee develops a *Staphylococcus epidermidis* infection. The organism is reported susceptible to vancomycin on the antibiogram (MIC 1 µg/mL). The patient completes six weeks of intravenous vancomycin at therapeutic serum levels. The infection recurs within a month of stopping therapy. Using the concepts in this chapter, explain the most likely mechanism of treatment failure. Why does the antibiogram mislead in this context? What is the standard-of-care recommendation? *(Tests: biofilm resistance mechanisms, distinction between susceptibility testing on planktonic cells vs. biofilm behavior.)*

**5.** A blood culture drawn at 08:00 shows 200 CFU/mL. A second culture from the same patient drawn at 12:00 shows 5,000 CFU/mL. (a) Calculate the generation time. (b) The clinical team wants to know when the patient's bacteremia likely reached 10³ CFU/mL — the level at which early fever typically begins. Working backward from the 08:00 measurement, estimate when that threshold was crossed. (c) The patient reports that symptoms started "last night around 10 pm." Is your calculated onset time consistent with that history? What assumptions is your answer resting on? *(Tests: generation-time formula, backward projection, honest acknowledgment of model limits.)*

**6.** *Clostridium perfringens* has the fastest known doubling time of any clinical pathogen: approximately 8 minutes under optimal conditions. Starting from 10² CFU/g in a cooked roast left at 43 °C (its optimal temperature) for 3 hours: (a) how many generations elapse? (b) What is the final CFU/g? (c) The standard infectious dose for *C. perfringens* food poisoning is approximately 10⁶ to 10⁷ CFU/g. Does three hours at optimal temperature produce a dangerous load from a 100 CFU/g starting point? *(Tests: exponential growth arithmetic on a high-stakes clinical pathogen.)*

### Synthesis

**7.** A clinician argues: "We should wait for the blood culture sensitivity result before starting antibiotics — that way we know we're using the right drug." A colleague argues: "We should start broad-spectrum empiric therapy immediately and adjust when the result comes back." Using the growth-curve arithmetic from the worked example, construct the mathematical argument for the second position. What assumptions does your argument rest on, and under what clinical circumstances might the first position be justified? *(Tests: worked-example reasoning applied to a clinical decision, honest acknowledgment of limits.)*

**8.** The chapter describes four mechanisms by which biofilm cells resist antibiotics: matrix diffusion limitation, slow growth, persister dormancy, and horizontal gene transfer. Rank these four mechanisms from most to least important for a *Pseudomonas aeruginosa* biofilm on a ventilator tube, and justify your ranking. Note: the ranking is contested in the literature — your justification matters more than the order. *(Tests: integrating biofilm mechanisms, constructing an evidence-based argument.)*

### Challenge

**9.** The chapter states that the lag phase "is the window during which prompt cleaning and prophylactic antibiotics are most effective." Construct a quantitative argument for this claim using the growth-curve framework. Specifically: if a wound is contaminated with 10³ cells at time zero and the organism has a 30-minute generation time, how much does a 2-hour lag (representing clinical response time) change the viable count the antibiotic must clear versus immediate treatment? Then: name one factor the model ignores that would make the real situation better than the model predicts, and one that would make it worse. *(Tests: integration of lag-phase biology with exponential arithmetic, model critique.)*
