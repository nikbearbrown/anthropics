# Chapter 10 — Pathogenicity and Disease

*A pathogen is not a thing. It is a verb caught in the act.*

---

In the summer of 1993, a child ate a hamburger at a fast-food restaurant in the western United States. The meat was undercooked. Two days later she had cramps. Three days later, bloody diarrhea. Five days later her urine output dropped to almost nothing, her platelet count crashed, and red blood cells started shredding inside her vessels — the smear under the microscope showed fragmented cells, hemoglobin spilling into the plasma. Her kidneys were failing. The clinical name for what was happening is hemolytic uremic syndrome, and in that year's Jack in the Box outbreak, more than 700 people got sick, 178 had lasting injuries, and four children died.[^1]

The bacterium was *Escherichia coli* O157:H7. The same species lives in your gut right now, billions of cells of it, harmless.

The difference was a small genetic cargo: a prophage carrying a gene for a protein called Shiga toxin. The toxin enters intestinal cells, drifts into the bloodstream, finds its way to the kidneys, binds a specific lipid called Gb3 on the surface of endothelial cells, gets endocytosed, and inside the cell does one thing — it shaves a single adenine off the ribosomal RNA. The ribosome stops. The cell dies. The small vessels of the kidney lose their lining. Platelets pile in to repair the damage. Red blood cells, squeezed through the wreckage, shred. Bloody diarrhea, kidney failure, anemia: the full clinical consequence of one small protein doing one specific thing to one specific receptor.

I want you to hold this case because it is the question the whole chapter is built around. What is a pathogen?

The answer is not "a kind of bacterium." The answer is: a bacterium, plus a specific tool, plus a specific host, plus a specific moment. Take away any one of those four and the disease doesn't happen. Most *E. coli* are not O157:H7. Most O157:H7 don't end up in hamburgers. Most contaminated burgers are cooked properly. Most people who eat a contaminated bite never develop HUS. The disease is the rare alignment of all four. Pathogenicity is an outcome, not a property — and that reframing changes everything that follows.

---

## Virulence as a quantity, not a quality

Two words that shouldn't be interchangeable are.

**Pathogenicity** is the capacity of a microbe to cause disease in some host under some conditions. Binary, more or less. *Mycobacterium tuberculosis* is pathogenic. The yogurt bacterium *Lactobacillus acidophilus* is not.

**Virulence** is the degree. How severe is the disease? How few organisms are needed to start it? How often does infection become clinical illness? Virulence is continuous and it is what clinicians actually measure.

A **primary pathogen** causes disease in a healthy host. Find *Yersinia pestis* in a patient and you have an explanation. An **opportunistic pathogen** causes disease only when the host's defenses are compromised — *Pseudomonas aeruginosa* in a burn wound, *Candida albicans* in an immunosuppressed patient. Same bacterium, different host, different outcome. Pathogenicity is interaction.

The numbers that give virulence operational meaning are **ID50** and **LD50** — the dose that infects 50% and kills 50% of exposed hosts, respectively. The variation is enormous, and it predicts how diseases actually move.[^2]

*Shigella dysenteriae* has an ID50 of roughly ten organisms. Hand-to-mouth casual contact will do it — which is why shigellosis spreads easily in daycare settings. *Vibrio cholerae* needs around 10⁸ organisms, because stomach acid kills most of them; cholera requires heavy water-or-food contamination at scale. The ID50 is not just a toxicology number. It is a transmission prediction. A pathogen you can swallow from a doorknob behaves epidemiologically nothing like a pathogen you need to drink by the liter.

---

## The seven-step sequence — and what each step requires

A pathogen does not "cause disease" as a single event. It runs a sequence, and every step in the sequence requires specific molecular tools. Interrupt any step and the disease doesn't happen. The tools that enable each step are **virulence factors** — anything the pathogen uses to make disease more likely.

<!-- → [DIAGRAM: Seven-step infection sequence as a horizontal flow — exposure → adherence → colonization → invasion → evasion → damage → transmission — with one representative virulence factor labeled at each step (P fimbriae, siderophores, capsule, etc.) and one intervention that breaks each step (handwashing, antibiotics, vaccine, etc.)] -->

**Exposure.** The host encounters the pathogen. Mostly statistics. We'll come back to this when we discuss transmission.

**Adherence.** The pathogen attaches to a host surface. Without attachment, mucus, ciliary clearance, urine flow, and peristalsis flush the microbe away. The tools are **adhesins** — surface molecules that bind specific host receptors. Uropathogenic *E. coli* has P fimbriae that bind a glycolipid on bladder epithelium; cells without P fimbriae get washed out before they can establish. *Streptococcus pyogenes* has M protein. *Neisseria gonorrhoeae* has Type IV pili. The receptor specificity explains **tissue tropism**: the pathogen gets sick where its adhesin finds a matching partner.

**Colonization.** Attached cells multiply. Most pathogens need iron to grow, and the host hides iron in transferrin and ferritin. So the bacterium secretes **siderophores** — small molecules with extraordinary iron-binding affinity that steal iron from host proteins. Some pathogens form **biofilms**, communities embedded in polysaccharide matrix that resist antibiotics and immune attack. Antibiotic concentrations that kill the same cells free-floating are useless inside the matrix — which is why biofilm on a heart valve or catheter is one of the harder problems in clinical microbiology.

**Invasion.** Some pathogens stop at the surface; others push deeper using **invasins** and matrix-degrading enzymes. *Streptococcus pyogenes* makes hyaluronidase to dissolve the connective tissue that holds skin together — the spreading factor of necrotizing fasciitis. *Listeria monocytogenes* makes internalin, which binds E-cadherin and tricks the epithelial cell into engulfing it. Once inside, *Listeria* hijacks the actin cytoskeleton to push itself from cell to cell without ever exposing itself to antibodies.

**Evasion.** The host has an immune system. A **capsule** — the polysaccharide layer outside the cell wall — resists phagocytosis by making the surface too slippery to grip. The capsule of *Streptococcus pneumoniae* is the virulence determinant: encapsulated strains cause pneumonia, unencapsulated strains do not. **Antigenic variation** periodically changes surface proteins so antibodies aimed at last week's version miss this week's. *Trypanosoma brucei* has hundreds of variant surface glycoprotein genes and cycles between them. Influenza accumulates mutations (antigenic drift) and swaps whole gene segments (antigenic shift). **Intracellular hiding** — *Mycobacterium tuberculosis* lives inside the macrophages that are supposed to kill it. Antibodies cannot reach inside host cells. And **IgA proteases** cleave the antibody that patrols mucous surfaces — *N. gonorrhoeae*, *S. pneumoniae*, and *H. influenzae* all make them.

**Damage.** This is the step that produces symptoms. Three broad mechanisms: direct cytotoxicity (toxins), inflammatory damage (the immune response is sometimes more destructive than the microbe), and resource depletion. The toxin story deserves its own section.

**Transmission.** Exit the host and get into the next one. The portal of exit often mirrors the portal of entry. Respiratory pathogens leave in droplets. GI pathogens leave in stool. Some pathogens appear to manipulate host behavior — rabies causing aggression and biting is the classic case. The transmission step closes the cycle that determines whether the disease is a single case or an outbreak.

---

## Toxins — secreted proteins versus structural components

Of all the virulence factors, toxins are the most visible, the most consequential, and the most confused. Two entirely different things wear the word "toxin," and confusing them leads to clinical mistakes.

**Exotoxins** are proteins secreted by living bacteria. They are heat-labile (boiling denatures them), typically made by Gram-positive organisms (though some Gram-negatives make them), and potent to an almost absurd degree. Botulinum toxin has an estimated LD50 around 1 nanogram per kilogram. They are also highly specific — each one has a particular target, a particular enzyme activity, and a particular clinical syndrome.

The standard architecture is the **AB toxin**: a B subunit that binds a specific receptor on the host cell, and an A subunit with an enzymatic activity that does the damage once inside. Diphtheria toxin, cholera toxin, pertussis toxin, anthrax toxin, botulinum toxin, tetanus toxin, and Shiga toxin are all AB toxins. The same modular design, independently evolved many times — separating binding from action is apparently a robust solution for getting an enzyme inside an enemy cell.

By clinical signature, exotoxins sort into subtypes. **Cytotoxins** kill cells directly: *S. aureus* α-toxin punches membrane pores, Shiga toxin shuts down ribosomes, streptolysin O lyses red blood cells. **Neurotoxins** disrupt nerve function in mirror-image ways: botulinum toxin blocks acetylcholine release at neuromuscular junctions, producing **flaccid paralysis** — muscles cannot contract. Tetanospasmin blocks inhibitory neurotransmitters in the spinal cord, producing **spastic paralysis** — muscles cannot relax. Same molecular mechanism (blocking vesicle fusion), opposite neuron type, opposite clinical syndrome. **Enterotoxins** hijack intestinal ion transport to produce watery diarrhea — cholera toxin is the archetype, which I'll trace in a moment. **Superantigens** are a strange class that don't have specific targets: they bridge MHC class II and T-cell receptors nonspecifically, activating up to 20% of all T cells at once, triggering a cytokine storm, fever, hypotension, organ failure — the toxic shock syndrome of 1980.

**Endotoxin** is one thing: **lipopolysaccharide (LPS)**, the outer leaflet of the Gram-negative outer membrane, specifically its lipid anchor, **lipid A**. It differs from exotoxins on every axis.

<!-- → [TABLE: Exotoxins vs. endotoxin — columns for property, exotoxins, endotoxin — rows for source, chemistry, heat stability, mode of release, potency, specificity, antigenicity, clinical syndrome] -->

The endotoxin mechanism is host-driven. Lipid A is recognized by **TLR4** on macrophages. TLR4 activation releases TNF-α, IL-1, IL-6. At low doses this is a useful local response. At high doses — when Gram-negative bacteria are lysing in the bloodstream — the cascade goes systemic: fever, vasodilation, fluid leaking from vessels into tissue, disseminated intravascular coagulation, organ failure. **Septic shock**. The host's own inflammation is doing most of the killing.

The clinical consequence that follows: when a patient has Gram-negative bacteremia and you give an antibiotic that lyses the bacteria, you release more lipid A in the short term. The antibiotic is necessary — without it the bacterial population grows indefinitely. But killing bacteria fast can make the patient look worse before they look better, because more endotoxin is circulating from dead bacterial walls. Supporting the patient with fluids, vasopressors, and oxygen while the antibiotic does its work is not ancillary to treatment. It is treatment.

---

## Cholera toxin, step by step

Pick one toxin and trace it through completely. The general architecture is best understood in one well-worn case, and the therapy that defeats cholera toxin is one of the more elegant pieces of medicine ever devised.

*Vibrio cholerae* reaches the small intestine through contaminated water. It does not invade tissue. It adheres to the brush border of intestinal epithelium using a Type IV pilus, and then it secretes its toxin.

Cholera toxin (CT) is an **AB₅ toxin**: one A subunit plus a ring of five B subunits. Here is what happens:

<!-- → [DIAGRAM: Cholera toxin mechanism — five panels in sequence: (1) B₅ pentamer binding GM1 ganglioside on apical membrane; (2) endocytosis and retrograde trafficking to ER; (3) A subunit translocation into cytosol; (4) ADP-ribosylation of Gαs locking it "on"; (5) cAMP rise → CFTR activation → Cl⁻/Na⁺/water efflux — final panel shows ORT bypass via SGLT1, annotated to show which transporter the toxin never touches] -->

The B₅ pentamer binds **GM1 ganglioside** — a glycolipid in high concentration on the apical membrane of small intestinal cells. The binding is essentially irreversible. This is why cholera hits the gut specifically: the receptor distribution is the map of where the disease can occur.

The AB₅ complex is endocytosed. But instead of going to the lysosome to be destroyed, it traffics *backward* through the secretory pathway — to the Golgi, then to the endoplasmic reticulum. Cholera toxin has evolved a KDEL-like signal that hijacks the host's own retrograde transport machinery.

In the ER, the A subunit is cleaved and translocated into the cytosol. It has one enzymatic activity: it **ADP-ribosylates the α-subunit of the heterotrimeric G-protein Gs** at a specific arginine, using NAD⁺ as the ADP-ribose donor. The modification locks Gαs in its "on" state permanently. It cannot turn itself off.

Gαs locked on → **adenylate cyclase** runs continuously → cyclic AMP rises and stays high. For hours. For days.

High cAMP activates the **CFTR chloride channel** in the apical membrane. Chloride pours out of the cell into the gut lumen. Sodium follows the chloride. Water follows the sodium. The result is liters of isotonic fluid flooding from the epithelial cells into the intestine faster than the colon can reabsorb it. Severe cholera can lose **20 liters per day**.[^3] Death is death from dehydration, and it can happen in hours.

Now look at the therapy. Cholera toxin attacks one pathway — cAMP-driven chloride secretion through CFTR. It does not affect the **sodium-glucose cotransporter SGLT1** in the same cells. SGLT1 imports glucose and brings sodium with it. Water follows. Give the patient a solution of glucose and sodium in roughly equimolar amounts, and you reactivate water absorption through a transporter the toxin never touched. The patient absorbs fluid by mouth as fast as they lose it from the other end.

This is **oral rehydration therapy**, formulated largely during the 1971 Bangladesh refugee crisis. Cheap. Effective. Estimated to have saved on the order of 50 million lives since.[^4] It exists because someone understood the mechanism well enough to find the part the toxin had not broken.

That is what a deep dive into mechanism gives you — not just "cholera causes diarrhea," but a specific pathway, a specific lesion, a specific bypass, and a therapy that flows directly from the molecular detail.

---

## Scaling up — epidemiology

One infected body is a case. Many infected bodies is an outbreak. The discipline that studies disease at the population level — **epidemiology** — has its own quantitative machinery, and it connects to the cellular story in ways that are not always made explicit.

John Snow's 1854 London cholera investigation is the founding template. More than 600 people died in Soho within days. The dominant theory was miasma — bad air rising from sewers. Snow had argued for years that cholera was waterborne. He mapped the deaths on paper, address by address. The pattern clustered around the **Broad Street pump**. He had the handle removed. The outbreak ended within days.[^5]

Snow had no microscope, no knowledge of *V. cholerae*, no germ theory. He had a map, a hypothesis, and the discipline to test it. That is the founding template: describe the pattern, generate a hypothesis, test by intervening, see if the pattern changes.

Two numbers run the population picture, and confusing them is a common error.

**Prevalence** is the fraction of a population that *has* the disease at a given moment. A snapshot. **Incidence** is the rate at which *new* cases develop over time. A flow. The rough relationship for a stable disease: prevalence ≈ incidence × average duration. A disease that lasts years accumulates prevalence even at modest incidence (HIV before effective therapy). A disease that resolves in days has low prevalence even at high incidence (norovirus). For planning, you need both: prevalence tells you how many people need care now; incidence tells you whether the load is growing.

Patterns across populations run from **sporadic** (occasional scattered cases: tetanus in the developed world) through **endemic** (consistent baseline: malaria across much of sub-Saharan Africa), **epidemic** (sudden rise above baseline: 1854 Broad Street, 2014 Ebola), and **pandemic** (global spread: 1918 influenza, HIV, COVID-19). The boundaries are conventional; the underlying biology is on a continuum.

Transmission routes sort into five broad categories, and naming the route is the first step in naming the intervention.

**Contact** (direct: skin-to-skin, sexual) → barrier methods, hand hygiene. **Indirect contact via fomite** (pathogen on doorknob, phone, surface) → surface disinfection. **Droplet** (large particles, travel less than a meter: influenza, pertussis) → masks, distance. **Airborne** (small aerosols, travel further, stay suspended: measles, tuberculosis) → ventilation, N95 masks, negative-pressure isolation. **Vehicle** (contaminated non-living medium reaching many people: foodborne, waterborne) → source control, water treatment. **Vector** (living carrier: *Anopheles* mosquito carrying *Plasmodium*; *Ixodes* tick carrying *Borrelia burgdorferi*) → insecticides, bed nets.

Removing the Broad Street pump handle broke a waterborne chain. Bed nets break a vector chain. N95 masks break an airborne chain. Every intervention is a cut in a specific link of the transmission sequence. Knowing how the pathogen moves tells you exactly where to cut.

<!-- → [DIAGRAM: Six transmission routes as a visual taxonomy — each route with a representative pathogen and the primary intervention that breaks it] -->

---

## R₀ — the number that tells you whether an outbreak grows

The **basic reproduction number R₀** ("R-naught") is the average number of new infections produced by one infected person in a fully susceptible population. It depends on the pathogen and the population together — transmission efficiency, contact rates, duration of infectiousness all contribute.

R₀ > 1 → epidemic grows. R₀ < 1 → epidemic dies out. R₀ = 1 → endemic steady state.

Approximate values, acknowledging that estimates vary by population and study conditions:

- Measles: 12–18
- Pertussis: 12–17
- Smallpox: 5–7
- COVID-19 (original strain): 2–3 (later variants higher)
- Ebola: 1.5–2.5
- Seasonal influenza: 1.5–2

Measles is the contagion benchmark. One case in a fully susceptible group infects 12 to 18 others on average. That single number explains why measles requires near-universal vaccination, and why even modest coverage drops allow it to return.

<!-- → [CHART: R₀ values for major pathogens on a horizontal bar chart, ordered by R₀, annotated with the herd immunity threshold each one implies — student should see how rapidly p* approaches 1 as R₀ increases beyond 5] -->

### The herd immunity threshold — a napkin calculation

If a fraction *p* of the population is immune, an infected person who would have caused R₀ new infections in a fully susceptible population now causes only R₀ × (1 − *p*) new infections — because R₀ × *p* of their contacts are immune dead ends.

The epidemic dies out when each case produces less than one new case:

$$R_0 \times (1 - p) < 1$$

Solving for *p*, the **herd immunity threshold** is:

$$p^* = 1 - \frac{1}{R_0}$$

Plug in measles at R₀ = 12: *p** = 1 − 1/12 ≈ **91.7%**.
At R₀ = 15: *p** ≈ 93.3%.
At R₀ = 18: *p** ≈ 94.4%.
Seasonal flu at R₀ = 2: *p** = 50%.

Now watch what one coverage drop does. Suppose a community has 95% measles vaccination — above threshold, outbreak dies out. Coverage falls to 85%. With R₀ = 15 and *p* = 0.85:

$$R_\text{eff} = R_0 \times (1 - p) = 15 \times 0.15 = 2.25$$

Each case produces 2.25 new cases. The epidemic grows. A 10-percentage-point drop in vaccination coverage is enough to flip a community from "protected" to "outbreak country." The measles outbreaks at Disneyland in 2014, in Brooklyn in 2019, in Samoa in 2019 — all are this calculation running itself out in different populations.

One thing the formula does not say: the threshold protects the community on average. It does not protect the individual unvaccinated person who encounters a case before the chain is extinguished. And below threshold, the disease reaches the people who *cannot* be vaccinated — infants too young, immunocompromised patients, people on chemotherapy — first and hardest, because they have no individual protection and rely entirely on the community's coverage. Herd immunity is a population property. It is not a personal shield.

### The overdispersion problem — why R₀ is incomplete

R₀ is an average. Real transmission is often wildly **overdispersed**: most infected people infect nobody, and a small fraction infect many. SARS-CoV-1 was a dramatic example. Most chains died out immediately. A handful of superspreader events drove most of the global spread. Lloyd-Smith et al. estimated that 20% of cases were responsible for 80% of transmission in that outbreak — the classic Pareto skew applied to disease.

This means R₀ = 2 can hide a world where 80% of cases are dead ends and 20% launch outbreaks. Control strategies that target the overdispersed tail — ventilation in crowded indoor spaces, limiting large gatherings, identifying and isolating superspreader settings — can be more effective than uniform blanket measures, because they cut at the right part of the distribution. An R₀-centered pandemic model that assumes homogeneous mixing will systematically underestimate how much can be achieved by targeting high-transmission events, and overestimate how much is needed through universal restrictions.

R₀ is the headline number. The dispersion is the story underneath.

---

## The honest limits

The cellular framework in this chapter — seven stages, specific virulence factors, molecular mechanisms — works well for primary pathogens and for asking which tool at which step produces which syndrome. It is less satisfying for the aftermath.

Rheumatic heart disease after streptococcal infection. Post-COVID syndromes. Post-Lyme symptoms. In each case the pathogen has been cleared and the patient is still sick. The inflammatory aftermath — the host's own immune response continuing after the trigger is gone — may matter more in the long run than what the bacteria did during active infection. Naming that limit honestly is part of doing the method right.

The framework is also incomplete for polymicrobial disease. Koch's postulates, and everything that follows from them, assume one organism causing one disease. Inflammatory bowel disease, periodontal disease, bacterial vaginosis — community-level shifts in microbiome composition that don't pin on a single agent. What causal language means at the community scale is still being worked out, and the seven-step single-pathogen model cannot stretch to cover it. It is a very good model for what it was designed for, and it was not designed for everything.

---

## Still puzzling

Why are AB toxins so convergently evolved? Diphtheria, cholera, pertussis, anthrax, botulinum, tetanus, and Shiga toxins are all AB-architecture, produced by bacteria that are not closely related. Is the modular A-B separation a structural necessity for delivering an enzyme into a host cell, or is it a contingent fact of how toxin genes shuffle between lineages via phages and plasmids? Different answers point at completely different evolutionary stories, and I haven't seen a satisfying treatment.

Why is overdispersion so common in respiratory pathogen transmission, and why has standard pandemic planning been so slow to incorporate it? The SARS-CoV-1 data made the point in 2003. COVID-19 confirmed it. R₀-centered models still dominate the public conversation. Part of this is a communication problem. Part of it, I suspect, is how the field trains its quantitative intuition — we build on well-mixed models that are tractable, and tractability has a gravitational pull that outlasts its usefulness.

---

## LLM Exercise — Chapter 10: Building the Epidemic Simulator

**Project:** `10-epidemic-simulator.html` — an interactive SIR-model epidemic simulator.
**Tool:** Claude Code (recommended) or any LLM with file-writing.

### What you're building

A single-file HTML page that simulates a basic SIR epidemic model with these controls:

- **R₀ slider** (range 1.0 to 15.0, step 0.1)
- **Initial infected** (integer, 1 to 100)
- **Vaccination rate** (slider, 0% to 100%)
- **Population size** (slider or input, 500 to 10,000)
- **Recovery rate** (slider, days; default 7)
- **Run / Reset** buttons

The visualization:

- **Animated population grid** — each cell colored by state: gray (susceptible), red (infected), green (recovered), blue (vaccinated)
- **S/I/R time-series curves** — three lines, animated as time advances
- **A computed herd immunity threshold line** drawn against the vaccination slider, labeled with the current *p** value
- **Output panel** — peak day, peak infected count, total epidemic size, and a one-line verdict ("Outbreak contained" vs. "Epidemic occurred")

### The Show / Say / Constrain / Verify prompt

```
SHOW:
I'm working on a microbiology textbook exercise. I want a single
HTML file (10-epidemic-simulator.html) that simulates a basic SIR
epidemic model with interactive controls. The student should be
able to drag R0 between 1 and 15 (covering flu through measles),
adjust vaccination rate from 0% to 100%, set initial infected and
population size, and see what happens.

SAY:
The educational goal is for the student to see — physically, in
the animated grid and the curves — three things:
  1. Why R0 determines whether an outbreak burns through or fades.
  2. Why the herd immunity threshold p* = 1 - 1/R0 is the right
     formula (and why crossing it changes everything).
  3. Why even small drops in vaccination above threshold can flip
     a community into outbreak mode.

CONSTRAIN:
- Single file, no external dependencies (no CDN, no npm).
- Vanilla HTML / CSS / JavaScript only.
- Use Canvas for the population grid and SVG or Canvas for the
  S/I/R curves.
- Standard discrete-time SIR update:
    new_infections = beta * S * I / N
    new_recoveries = gamma * I
  where beta = R0 * gamma, gamma = 1/recovery_days
- Vaccinated individuals are removed from S at simulation start
  (move them directly to a separate "vaccinated" pool).
- Display the herd immunity threshold formula visibly on the
  page: p* = 1 - 1/R0, with the current value computed live.
- Population grid: at minimum 30x30 cells (900 individuals) up to
  100x100 (10,000). Pick a reasonable rendering speed.
- Time step: roughly 30 frames per simulated day; total simulation
  caps at 365 days or when I = 0 (whichever comes first).
- One-page UI: controls at top, grid on left, curves on right,
  output panel below.

VERIFY:
After running:
  1. Set R0 = 15, vaccination = 0%. Expect: nearly the entire
     population is infected before the epidemic burns out. Total
     epidemic size should be close to 100%.
  2. Set R0 = 15, vaccination = 95% (above p* = 93%). Expect:
     the few initial cases fade out without sustained spread.
  3. Set R0 = 15, vaccination = 85% (below p*). Expect: a slower
     but still substantial outbreak.
  4. Set R0 = 2, vaccination = 60% (above p* = 50%). Expect:
     contained.
  5. The herd immunity threshold displayed on the page should
     update live as you move R0, and should match p* = 1 - 1/R0
     to two decimal places.

If any of those fail, fix the model and explain what was wrong.
```

### After the file works — exploration

1. **Find the cliff.** Set R₀ = 12. Slowly decrease vaccination rate from 100%. At what coverage does the outbreak start to take off? Compare to the computed *p** = 1 − 1/12.
2. **Compare pathogens.** Run R₀ = 2 (flu-like), R₀ = 3 (COVID-like), R₀ = 7 (smallpox), R₀ = 15 (measles), each at 70% vaccination. Which contain? Which don't?
3. **Vary recovery time.** Hold R₀ fixed. What happens to the epidemic curve as recovery time goes from 3 days to 14 days? Why does R₀ alone not predict the *shape* of the outbreak?
4. **Initial seed sensitivity.** With R₀ = 4 and 50% vaccination, run the simulation 10 times with one initial case. How many runs lead to large outbreaks and how many die out? What does this tell you about extinction probability in real outbreaks?

### Extension toward Chapter 11

The SIR model treats "recovery" as a black box. Chapter 11 (Innate Immunity) pries it open. Two specific bridges:

1. The simulator assumes recovered individuals are permanently immune. Real immunity wanes (flu, pertussis) or fails entirely (no lasting immunity against gonorrhea). Modify the model so recovered individuals lose immunity after a random duration and return to the susceptible pool. This is the **SIRS** model, and it is the foundation for understanding why some pathogens cycle endemically rather than disappearing.

2. The simulator assumes infected individuals are immediately infectious. Real infections have an incubation period: infected but not yet shedding. Add an **E** (exposed) compartment between S and I. This gives you **SEIR**, the workhorse of pandemic modeling for most respiratory pathogens. Compare the epidemic curve shape with and without the E compartment.

In both cases, what you are doing is building a slightly better model of what the host's immune response is actually doing — which is what Chapter 11 will teach at the cellular level.

---

## Exercises

### Warm-up

1. **Pathogenicity vs. virulence.** *Escherichia coli* is a normal gut commensal and also the cause of several distinct diseases. Use this one organism to illustrate the difference between pathogenicity and virulence, and to explain why "dangerous bacterium" is a less useful category than "bacterium carrying specific virulence factors in a specific host context."

2. **ID50 as transmission prediction.** *Shigella dysenteriae* has an ID50 of roughly 10 organisms. *Vibrio cholerae* has an ID50 of roughly 10⁸. Without looking anything up, predict which pathogen is more likely to spread through direct person-to-person contact in a childcare setting, and which is more likely to cause large waterborne outbreaks. Explain the mechanistic link between ID50 and transmission route.

3. **Botulinum vs. tetanus.** Both botulinum toxin and tetanospasmin block neurotransmitter release by cleaving SNARE proteins at the presynaptic membrane. Yet one causes flaccid paralysis and the other causes spastic paralysis. Explain the paradox. Your answer must name the specific type of synapse each toxin acts on and why blocking it produces opposite motor effects.

### Application

4. **The seven steps in a clinical case.** A 34-year-old woman develops a urinary tract infection. Trace the infecting *E. coli* through as many of the seven stages as apply, naming the specific virulence factor required at each step. Then identify one stage where an intervention — catheter removal, antibiotic, cranberry extract, vaccine (hypothetical or real) — could plausibly break the chain, and explain the mechanism of that intervention.

5. **Endotoxin and the antibiotic paradox.** A patient with Gram-negative bacteremia is started on a bactericidal antibiotic. Three hours later, her blood pressure drops further and her lactate rises — she appears to be getting worse, not better. The blood culture drawn at hour zero is now growing *Klebsiella pneumoniae*. Explain the molecular mechanism responsible for this apparent worsening. Should the antibiotic be stopped? What should be done instead, and why?

6. **Herd immunity under partial vaccine efficacy.** A respiratory pathogen has R₀ = 6. A vaccine with 85% efficacy is available (meaning a vaccinated person has 85% lower probability of infection than an unvaccinated one). What fraction of the population must be vaccinated to achieve effective herd immunity? Show the derivation. If a second, more transmissible variant emerges with R₀ = 9, what vaccination fraction is now required with the same vaccine? Discuss what this implies for booster campaigns.

### Synthesis

7. **The ORT insight.** Oral rehydration therapy for cholera was developed in the early 1970s, decades after the cholera toxin mechanism was first described. Yet the key insight — that the SGLT1 transporter is unaffected by the toxin — follows directly from the molecular mechanism. Explain, step by step, the chain of mechanistic reasoning that leads from "cholera toxin locks Gαs permanently on" to "giving glucose and sodium by mouth should restore fluid absorption." Then generalize: what is the design principle for a therapy derived from a toxin mechanism, and give one other toxin-disease pair where an analogous bypass might be imagined?

8. **Overdispersion and control strategy.** Two pathogens both have R₀ = 3 in the same population. Pathogen A has homogeneous transmission: each infected person infects close to 3 others. Pathogen B is highly overdispersed: 80% of cases infect no one, and 20% each infect about 15. A health authority has resources for one of two interventions: (a) universal masking reducing transmission by 40% for everyone, or (b) targeted ventilation improvements in high-density indoor venues, estimated to reduce the superspreading 20% by 75%. Analyze which intervention is more effective against each pathogen, and explain why the same intervention can be optimal for one pathogen and inefficient for the other.

### Challenge

9. **Design a virulence-factor vaccine.** The chapter describes five broad evasion strategies: capsules, antigenic variation, intracellular hiding, IgA proteases, and molecular mimicry. For each strategy, evaluate whether a vaccine targeting that virulence factor is (a) mechanistically feasible, (b) likely to confer broad protection across strains, and (c) at risk of driving immune evasion evolution. For the strategy you consider most promising as a vaccine target, describe what a first-generation vaccine would look like and what its principal failure mode would be.

---

## Tags

`pathogenicity` `virulence` `toxins` `endotoxin` `epidemiology` `R-nought` `herd-immunity` `cholera-toxin` `LPS` `microbiology`

---

**What would change my mind:** If genomic and multi-omic surveillance of a major primary pathogen like *S. pneumoniae* or *S. aureus* consistently showed that host immune-state and microbiome composition explain more virulence variation across patients than pathogen genotype does, the "pathogen brings the tools" framing would need to give substantial ground to "host context selects the syndrome." Some of this is already established for opportunistic pathogens. The question is how far it generalizes.

**Still puzzling:** Why AB toxins are so convergently evolved across unrelated organisms, whether this reflects a structural constraint or a plasmid-and-phage distribution artifact. Why overdispersion is so common in respiratory transmission but has been so slow to enter standard pandemic planning. And how much of the long-term clinical signature of an infection is the microbe's doing versus the immune response's aftermath — post-streptococcal disease, post-COVID syndrome, post-Lyme symptoms — where the pathogen is gone and the patient is still sick.

---

[^1]: Bell, B.P. et al. "A multistate outbreak of *Escherichia coli* O157:H7-associated bloody diarrhea and hemolytic uremic syndrome from hamburgers." *JAMA* 272, no. 17 (1994): 1349–1353. doi:10.1001/jama.1994.03520170059036.
[^2]: Schmid-Hempel, P. and Frank, S.A. "Pathogenesis, virulence, and infective dose." *PLoS Pathogens* 3, no. 10 (2007): e147. doi:10.1371/journal.ppat.0030147.
[^3]: Sack, D.A. et al. "Cholera." *The Lancet* 363, no. 9404 (2004): 223–233. doi:10.1016/S0140-6736(03)15328-7.
[^4]: Ruxin, J.N. "Magic bullet: the history of oral rehydration therapy." *Medical History* 38, no. 4 (1994): 363–397. doi:10.1017/s0025727300036905.
[^5]: Snow, J. *On the Mode of Communication of Cholera*, 2nd ed. London: John Churchill, 1855. https://www.ph.ucla.edu/epi/snow/snowbook.html
