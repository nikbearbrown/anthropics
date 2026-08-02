# Chapter 4 — Acellular Pathogens

*The most dangerous thing in a cell is sometimes a passenger that never evolved to be there.*

---

Here is a fact that should unsettle you.

The gene that kills children with kidney failure — the one that turns ordinary *E. coli* into *E. coli* O157:H7 — is not in the bacterium. It never was. It arrived inside a virus that infected a harmless gut bacterium somewhere in the recent evolutionary past, slipped its DNA into the chromosome, and brought a toxin gene along as cargo. The bacterium didn't become dangerous by evolving. It became dangerous by being infected.

Same story for cholera. *Vibrio cholerae* without its phage is a mild organism found in brackish coastal water. With the CTXφ phage integrated into its chromosome, it makes cholera toxin — the protein responsible for the rice-water diarrhea that can drain a person's blood volume in hours. Take the phage away and you take the epidemic with it. Add the phage back and you rebuild cholera from scratch.[^4]

Same for diphtheria, which suffocated children in pre-vaccine Europe by the hundreds of thousands. The toxin gene isn't bacterial. It's in a virus that *Corynebacterium diphtheriae* carries integrated in its genome.

Some of the worst infectious diseases in human history are not bacterial diseases. They are viral diseases that bacteria carry on our behalf.

That's where this chapter is going. But to get there, we first have to understand what a virus actually is — which turns out to require thinking carefully about what "alive" even means.

---

## The definition problem

Let me give you a working definition of life, the kind you'd find in a standard textbook. A living organism maintains itself against entropy through metabolism. It responds to its environment. It grows. It reproduces.

A bacterium passes all four. You pass all four. A virus, outside a host cell, passes none.

An influenza virion sitting on a doorknob is a stable chemical object. It doesn't metabolize. It doesn't respond to anything. It doesn't grow. Left to itself, it does nothing at all. In 1935, Wendell Stanley crystallized tobacco mosaic virus — produced it in crystals, the way you crystallize salt, the way you crystallize something that is definitively not alive.[^2]

Now put that same particle into a human airway cell. It binds, enters, releases its genome, and within hours the cell is producing nothing but virus. Ten thousand virions burst out of a single cell. Each finds another cell. The math is exponential and the timescale is brutal.

So: is it alive?

I think the question is malformed. The right question is: *what kind of entity can only be described by its relationship to another entity?* A virus is not a thing in the usual sense. It is genetic information that has outsourced its metabolism to a host. Outside the host it's chemistry. Inside the host it's something that behaves like an organism. The boundary between those states is a cell membrane.

Once you accept that framing, the rest of the chapter becomes tractable. When I say a virus "does" something — binds, replicates, evades — that is shorthand for: the virus's genome, once inside a cell, gets read by the cell's own machinery in a way that produces more virus. The cell is being made to act on the virus's behalf. The virus is not acting. The direction of causality matters.

---

## What a virus actually consists of

A virus at minimum is two things: a nucleic acid genome wrapped in a protein shell called the **capsid**. Some viruses add a third: a lipid membrane, stolen from the host cell on the way out, called the **envelope**. That's the whole inventory. No ribosomes, no mitochondria, no metabolic enzymes. Just information and packaging.

The genome can be DNA or RNA — never both — and within each there are further choices. Single-stranded or double-stranded. One piece or many (influenza has eight separate RNA segments; if a cell is infected with two influenza strains simultaneously, the segments can reassort, producing new combinations — which is one of the main engines of pandemic flu). Positive-sense or negative-sense.

That last distinction matters more than it might seem. A positive-sense RNA genome can be read directly by a ribosome, exactly like messenger RNA. The moment it enters the cell, it starts producing viral proteins. A negative-sense RNA genome is the complement — the reverse — of a readable strand. A ribosome cannot read it. The virus has to carry its own RNA polymerase inside the virion so it can make a readable copy before protein synthesis can even begin. This is why negative-sense RNA viruses (influenza, rabies, Ebola, measles) have to package extra cargo: without the polymerase, the genome is useless on arrival.

David Baltimore formalized all of this into a classification in 1971 — seven classes, each defined by one question: *what does this virus have to do to go from the genome it carries to messenger RNA the host ribosome can read?*[^3]

<!-- → [TABLE: Baltimore classification — seven rows, columns for class number, genome type, example viruses, whether viral polymerase must be packaged in the virion, and a one-line description of the replication trick that defines each class] -->

The Baltimore class predicts the replication strategy. Give me the class and I can tell you what enzymes the virus must encode, whether it brings its own polymerase, how fast it mutates, and which cellular compartment it replicates in. The classification is not taxonomy for its own sake — it is a predictive framework.

The capsid is built from identical protein subunits, called capsomers, arranged in a regular geometric pattern. Icosahedral geometry — 20-sided, like a d20 — gives you the maximum enclosed volume for the minimum protein. Most "spherical" viruses are icosahedral. Helical capsids wind protein around the genome like a screw. And then there are the bacteriophages with complex architecture: an icosahedral head, a tail, a baseplate, tail fibers. The T4 phage looks like a lunar lander, which is essentially what it is — it lands on a bacterium and injects DNA through the cell wall.

The envelope, when present, is a lipid bilayer with viral glycoproteins studded into it — the spike proteins on a COVID diagram, the hemagglutinin on flu. The envelope is a trade-off worth naming precisely.

Enveloped viruses can enter cells by membrane fusion — one lipid bilayer merging with another — which is efficient and keeps the viral contents hidden from the immune system during entry. But envelopes are fragile. They dry out. They dissolve in soap and alcohol. Anything that disrupts a lipid bilayer kills an enveloped virus.

Non-enveloped viruses have no envelope to dissolve. They are environmentally robust. Norovirus — the thing that spreads through cruise ships and daycare centers — survives on hard surfaces for days because there is nothing to disrupt. Rotavirus, also non-enveloped, behaves the same way.

This is why handwashing with soap is so effective against influenza and SARS-CoV-2 (both enveloped) and so much less effective against norovirus (non-enveloped). The mechanism is not "soap kills germs" in some general sense. Soap specifically disrupts lipid bilayers. Non-enveloped viruses laugh at soap.

A common mistake: treating "enveloped" as a proxy for "more dangerous." It is a transmission strategy, not a virulence rating. Rabies is enveloped and kills essentially every infected person who develops symptoms. Norovirus is non-enveloped and kills almost no one. The envelope shapes how a virus gets from host to host. What it does inside the host is a separate question entirely.

---

## The six-step cycle

<!-- → [DIAGRAM: The six-step lytic cycle as a circular flow — attachment → penetration/uncoating → replication & protein synthesis → assembly → release → new virion seeking next host — annotated with approximate timing for a fast bacteriophage (~20 min total) vs. an enveloped animal virus (~8–24 h), and a callout distinguishing lysis vs. budding at the release step] -->

A virus cannot reproduce by growing and dividing — it has no metabolism to power growth. Instead it reproduces by commandeering a host cell's manufacturing infrastructure. The general shape of this process has six steps, and they're the same whether the virus is a bacteriophage landing on *E. coli* or an influenza particle landing on your airway.

**Attachment.** The virus binds a specific receptor on the cell surface. This is not random contact — it is a molecular lock and key. A phage's tail fibers bind a specific sugar in the bacterial cell wall. Influenza's hemagglutinin binds sialic acid residues on the host membrane. HIV's gp120 binds the CD4 receptor on helper T cells. The receptor specificity is why a phage that infects *E. coli* will not infect *Staphylococcus* — wrong receptor, wrong lock. It is also why HIV specifically destroys cellular immunity — the cells it infects are exactly the ones that coordinate the immune response.

**Penetration and uncoating.** The genome has to get inside the cell. Bacteriophages solve this with brute force — the tail contracts, drives a hollow tube through the cell wall, and injects DNA while the capsid stays outside. Animal cells have no cell wall, only a membrane, so animal viruses get in differently: either endocytosis (the cell engulfs the particle in a vesicle, then acid in the vesicle triggers the capsid to break open) or direct fusion of the envelope with the plasma membrane. Either way, the genome arrives in the cytoplasm and the capsid comes apart — uncoating.

**Replication and protein synthesis.** This is where the host's machinery gets hijacked. Host ribosomes translate viral mRNA into viral proteins. Host nucleotides become viral genome copies. In some of the most aggressive phages, the first proteins made shut down all host gene expression completely. The cell stops being a cell and becomes a virus factory.

**Assembly.** Capsid subunits self-assemble around new genome copies. In well-studied phages you can watch this in electron micrographs: a cell that's been infected for ten minutes contains empty capsid heads; fifteen minutes in, those heads are full; twenty minutes in, complete phage particles are visible. Assembly is not guided by enzymes that read a blueprint. The geometry of the subunits simply enforces the final structure.

**Release.** The cell has to open. For bacteriophages, the virus encodes a lysozyme that breaks down the cell wall from inside. The cell bursts and spills hundreds of phages into the environment. For non-enveloped animal viruses, the cell ruptures similarly. For enveloped animal viruses, the situation is different: the capsid pushes through the cell membrane, picks up a lipid wrapping on the way out, and the cell may survive to bud virus for days. Hepatitis B does this — chronic infection is in part a consequence of non-lethal budding.

The burst size, the timing, the whether-or-not-the-cell-survives — all of these are determined by the virus's specific biology. A fast lytic phage goes from infection to cell death in about twenty minutes at body temperature. An enveloped animal virus might take eight to twenty-four hours. The range matters for how you think about the disease.

---

## The lysogenic choice — and why it explains the worst bacterial diseases

Here is the move that makes the opening case make sense.

After injecting its DNA, some bacteriophages don't start the lytic program. Instead, the phage DNA integrates into the bacterial chromosome at a specific site, falls completely silent, and lets the bacterium go on living. The integrated genome is called a **prophage**. The bacterium is now *lysogenic* for that phage. Every time the bacterium divides, the prophage is copied along with the bacterial chromosome. The phage replicates — but as part of the bacterium, without killing it.

This can persist for thousands of generations. Then something stresses the cell: UV radiation, a certain antibiotic, inflammation from the host immune response. The SOS response activates — a bacterial stress program we'll examine in Chapter 12. One consequence of SOS activation is that it cleaves a protein that was keeping the prophage repressed. The prophage detects the cleavage, excises itself from the chromosome, launches the lytic program, and the cell dies producing a burst of phage.

The phage is hedging. When the bacterium is healthy, ride inside it. When the bacterium is stressed — perhaps about to die anyway — switch to lytic and try to escape. This is a rational strategy from the phage's perspective. From the bacterium's perspective, it is a parasite that has been paying rent for centuries and has just decided to burn down the building.

But the hedging strategy is not the clinically important thing. The clinically important thing is what the prophage brings with it.

A prophage is not just inert passenger DNA. It carries genes. Most of those genes encode the phage's own replication proteins. But some prophages carry genes that *change the bacterium's behavior* — that give the bacterium capabilities it would not otherwise have. This is called **lysogenic conversion**, and it is responsible for a list of catastrophic pathogens.

<!-- → [TABLE: Lysogenic conversion examples — columns for bacterium, phage, toxin or virulence factor encoded, and disease caused — rows for C. diphtheriae / corynephage β / diphtheria toxin / diphtheria; V. cholerae / CTXφ / cholera toxin / cholera; E. coli O157:H7 / Stx prophage / Shiga toxin / HUS; S. pyogenes / SPE phage / erythrogenic toxin / scarlet fever; C. botulinum / C1 phage / botulinum toxin / botulism] -->

The implication is stark. When you ask "is this bacterium pathogenic?" the species name is not the answer. The answer is: *which prophages does this strain carry?* Two strains of *E. coli* can share 99.6% of their chromosomes — one causes mild traveler's diarrhea, the other kills children. The difference is a phage genome integrated in one of them.

Lysogenic conversion is also a mechanism for spreading virulence genes between bacteria. A phage that integrates in one bacterium, excises, and infects another carries whatever DNA it picked up. This process — transduction — is one of three major routes by which bacteria acquire new DNA horizontally, including antibiotic-resistance genes. The chapter on horizontal gene transfer will return to this. For now, the point is that phages are not just pathogens. They are a distribution system for the information that makes bacteria pathogenic.

---

## HIV in detail: the retrovirus as worked example

Baltimore Class VI is the retroviruses. They carry a positive-sense RNA genome but do not use it as mRNA directly — they first copy it into DNA using an enzyme called **reverse transcriptase**, then integrate that DNA into the host chromosome. The central dogma runs DNA → RNA → protein. Retroviruses run it RNA → DNA → RNA → protein. When Howard Temin and David Baltimore independently described reverse transcriptase in 1970, the response from molecular biology was disbelief, followed by the 1975 Nobel Prize.[^5]

HIV-1 is the canonical retrovirus. Walk through its replication cycle because each step has a drug, and the drugs are the proof that understanding mechanism is the path to treatment.

**Attachment.** HIV's surface protein gp120 binds the CD4 receptor on helper T cells, macrophages, and dendritic cells — those are HIV's targets, and losing them is what eventually destroys cellular immunity. CD4 binding alone isn't sufficient: gp120 also needs a coreceptor, either CCR5 or CXCR4. People who are homozygous for a deletion in CCR5 — the CCR5-Δ32 mutation — are largely resistant to HIV infection. The coreceptor isn't there; the lock has no keyhole.

*Drugs: CCR5 antagonists (maraviroc) block the coreceptor.*

**Fusion.** Coreceptor binding triggers a conformational change in gp41, a second envelope protein. gp41 inserts into the host membrane and pulls the two membranes together until they fuse. The viral interior — capsid, genome, enzymes — empties directly into the cytoplasm.

*Drugs: fusion inhibitors (enfuvirtide) prevent gp41 from completing the conformational change.*

**Reverse transcription.** The capsid partially disassembles. Reverse transcriptase, which was packaged inside the virion, starts copying the RNA genome into DNA. It uses a host tRNA as a primer, makes a single DNA strand from the RNA template, degrades the RNA template, then makes a second strand. The product is double-stranded viral DNA — the central dogma run backward.

Reverse transcriptase has no proofreading. It misreads about one base in ten thousand. The HIV genome is ten thousand bases long. On average, every new copy contains a mutation. Every patient is infected not with a single virus but with a swarm of variants — a *quasispecies*. Within that swarm, by accident, there are usually some members that partially resist any single drug you give. This is why HIV therapy is always a combination of drugs hitting different steps simultaneously. A virus would need to acquire multiple independent resistance mutations to survive the combination, which is orders of magnitude less probable than acquiring one.

*Drugs: nucleoside reverse transcriptase inhibitors (zidovudine, tenofovir) are fake nucleotides that terminate the growing DNA chain; non-nucleoside RTIs (efavirenz) bind the enzyme directly and freeze it. Both have selective toxicity because reverse transcriptase is a viral enzyme — host DNA polymerases mostly ignore these drugs.*

**Integration.** The viral DNA travels to the nucleus. A viral enzyme, **integrase**, cuts the host chromosome and stitches the viral DNA in. From this moment, the viral genome is part of the host's own genome. The integrated form is the **provirus**.

This is the reason HIV cannot currently be cured. Antiretroviral therapy can reduce viral load to undetectable levels in most patients, but it cannot touch the provirus. Every infected CD4 cell carries permanent viral DNA, and that DNA is invisible to drugs. The latent reservoir is stable, copying itself silently every time the cell divides. Cure would require finding and destroying every cell carrying a provirus — a problem no current approach solves.

*Drugs: integrase strand-transfer inhibitors (dolutegravir, bictegravir) now first-line for most patients.*

**Transcription, translation, assembly, and budding.** When the infected T cell is activated by antigen — doing exactly its normal immune job — host RNA polymerase reads the provirus and produces viral mRNA. Host ribosomes translate it. Viral proteins accumulate. Some are made as polyproteins that require cutting by viral **protease** before they're functional. Capsids self-assemble around new genome copies, bud through the cell membrane picking up an envelope, and mature when protease makes its cuts.

*Drugs: protease inhibitors (darunavir, atazanavir) block the cuts; immature virions assemble but cannot become infectious.*

The full arc: mechanism understood in the 1980s and 1990s, drugs developed targeting each mechanistically-understood step, patients on combination therapy now largely living normal lifespans, cure blocked by the one step — integration — that is irreversible. The mechanism led to the drugs. The step that lacks a drug is the step that is hardest to reverse.

<!-- → [INFOGRAPHIC: HIV replication cycle as a linear pathway — six steps with drug class annotations at each step, plus the "integration = no cure" callout for step 4] -->

---

## When even the genome disappears: viroids and prions

A virus is a genome plus a capsid. What if you take away the capsid? You get a **viroid** — a naked, circular, single-stranded RNA molecule, 246 to 401 nucleotides, too small to encode any protein. No protein at all. Viroids infect plants, replicate using the plant's own RNA polymerases, and cause real agricultural disease — potato spindle tuber, coconut cadang-cadang. Theodor Diener identified the first one in 1971.[^6]

Why only plants? Likely because plant RNA polymerases happen to copy viroid RNAs as a byproduct of their normal function. But "happen to" is the kind of phrase that usually marks an explanation that isn't finished. Viroids also look like they might be relics of an RNA world — self-replicating information that predates proteins. That is speculative, but it's the kind of speculation that might be right.

Now take away the genome entirely.

A **prion** is a misfolded protein that propagates by inducing normally-folded copies of the same protein to misfold. No DNA. No RNA. No nucleic acid of any kind. Just structural information passed from one protein molecule to another by physical contact.

Scrapie — a fatal neurological disease of sheep — had been known for centuries. By the 1960s it was clearly transmissible, passable from sheep to sheep and from sheep to mice. But the infectious agent survived everything that should have destroyed it: ionizing radiation, UV, nucleases, formalin. Nothing that damages nucleic acid touched it. It behaved like an infectious protein.

Stanley Prusiner proposed in 1982 that it *was* a protein, and only a protein.[^7] The field's response was that this was impossible. Proteins don't replicate. Their structure is determined by genes. A self-propagating protein fold would mean inheritance without nucleic acid, which violated the central dogma.

Prusiner won the 1997 Nobel.

The current picture: there is a normal neuronal protein, **PrP^C**, that can adopt an alternative beta-sheet-rich conformation, **PrP^Sc**. PrP^Sc, on contact with PrP^C, templates the normal form into the misfolded form. The misfolded forms aggregate into fibrils, damage neurons, and kill the patient. The disease spreads through the brain like a line of falling dominoes: one misfolded protein touches its neighbor, which touches its neighbor, and the front advances until the brain is riddled with vacuoles.

Human prion diseases: sporadic Creutzfeldt-Jakob disease (about one in a million per year), variant CJD acquired from BSE-infected beef, kuru transmitted by ritual cannibalism among the Fore people of Papua New Guinea, fatal familial insomnia. Animal prion diseases include scrapie, BSE, and chronic wasting disease in deer and elk — the last of which is spreading through North American cervid populations and deserves more public-health attention than it receives. `[verify: current CWD prevalence figures as of 2026]`

Two clinical facts about prions that cannot be overstated.

First: no nucleic acid, so no nuclease, no UV radiation, no formaldehyde touches them.

Second: unusually resistant to heat. Standard autoclave — 121°C for 15 minutes, the protocol that reliably kills bacterial endospores — does not reliably inactivate prions. Special protocols are required: 134°C for 18 minutes plus sodium hydroxide treatment. Neurosurgical instruments used on a CJD patient, processed through standard sterilization, have transmitted disease to subsequent patients. Some such instruments have to be incinerated. Iatrogenic CJD from pooled cadaveric growth hormone — pituitary extracts drawn from unscreened donors in the 1980s — caused over 200 deaths.[^8]

A misfolded protein cannot be killed. There is nothing alive to begin with.

---

## Two misconceptions worth burning down

**"Antibiotics kill viruses."** They don't. Antibiotics target structures that bacteria have and human cells don't: peptidoglycan in the cell wall (penicillins), bacterial 70S ribosomes (tetracyclines, aminoglycosides), bacterial DNA gyrase (fluoroquinolones). A virus has none of these. It has no cell wall, no ribosomes of its own, no metabolic enzymes. It uses *your* ribosomes and *your* nucleotides. An antibiotic has nothing to bind.

Prescribing antibiotics for viral respiratory infections — which is most of them — does nothing to the virus and selects for resistance in the bacterial flora of the patient. The harm shows up months and years later, in someone else's infection.

Antiviral drugs exist precisely because they target viral-specific enzymes: reverse transcriptase, integrase, protease, neuraminidase. The target has no host equivalent. The drug works because the virus does something the host doesn't.

**"Viruses are always harmful."** The catalog of named viruses is biased toward pathogens because we discovered most of them by looking for causes of disease. The actual population of viruses on Earth is something like 10^31 particles, mostly bacteriophages in the oceans.[^9] Most have no human host. Phages kill marine bacteria continuously, cycling carbon and nutrients at planetary scale. The ocean's productivity is partly a function of viral death rates.

Phages are also being developed as therapeutics against antibiotic-resistant bacterial infections — an idea that predates antibiotics themselves, was abandoned when penicillin arrived, and is being reconsidered seriously as resistance makes antibiotics less reliable. `[verify: current FDA status of phage therapy approvals as of 2026]`

---

## Still puzzling

Giant viruses — Mimivirus, Pandoravirus, Pithovirus, discovered in the 2000s — have genomes larger than some bacteria and encode their own translation factors. Are they pushing the alive/not-alive line, or are they reduced cells that gradually shed their cellular architecture and converged on virus-like form? I don't have a clean answer, and the field doesn't either.

I'm also unsettled by how rare prion diseases are. The misfolding mechanism should, on its face, be more common than it is. The normal PrP^C protein is expressed in healthy neurons throughout life. The conversion reaction is thermodynamically accessible. And yet sporadic CJD affects one in a million people per year. Something is strongly suppressing spontaneous conversion in the vast majority of individuals, and the nature of that suppression is not well understood.

And the plant-only distribution of viroids remains suspicious. The RNA-polymerase hypothesis explains it descriptively. It does not explain why no comparable parasitic RNA has ever established itself stably in animal cells, given billions of years of opportunity.

---

## LLM Exercise — Building the Viral Replication Simulator

**Project:** `simulations/04-viral-replication.html`
**Tool:** Claude, ChatGPT, or Gemini — the exercise is the same.
**Framework:** Show / Say / Constrain / Verify.

### Show

```
Here is a description of what I'm trying to build:

A single-file HTML simulator showing a viral replication cycle.
Stack: vanilla HTML + CSS + JavaScript, no external libraries.

User interface:
- Two selectors at top: virus type (bacteriophage / non-enveloped
  animal / enveloped animal / retrovirus) and cycle (lytic / lysogenic;
  lysogenic only enabled for bacteriophage).
- Central panel: a stylized host cell with the virus visible.
- The cycle plays as an animation. At each step, a text label
  describes what is happening at that step.
- Step counter (1–6 for lytic; more for retroviral; branch for lysogenic).
- For lytic: a simulation clock showing approximate time to lysis.
- For lysogenic: a "prophage integrated" state, a "stress applied"
  button that triggers excision and switches into lytic mode.
- Comparison mode: side-by-side panels running lytic vs. lysogenic
  on the same phage, time-synced.

Educational goal: a student who watches this should understand
(a) the universal six-step cycle, (b) how lysogenic differs by
quietly integrating until induced, (c) what's different about
retroviruses (reverse transcription + integration as extra steps).
```

### Say

```
Generate the simulator as a single self-contained HTML file.
Inline CSS and JavaScript. No build step, no npm, no CDN.

Stylize the host cell and virus as simple SVG or CSS shapes
(not realistic — abstract, like a teaching diagram). Use
clear colors that distinguish: viral genome, viral protein,
host membrane, host cytoplasm, host nucleus (for animal viruses).

The animation should be slow enough to read. Roughly 2–3 seconds
per step is right. Include a "next step" button so a student can
also step through manually.

For each step, the on-screen label should be one sentence in plain
English (not jargon). Example for attachment: "The virus binds a
specific receptor on the cell surface — only certain cells qualify."

For the side-by-side comparison view, the two panels run the same
phage in parallel. The lytic panel produces ~100 progeny phages
in ~20 simulated minutes. The lysogenic panel sits dormant the
whole time. A "stress" button in the lysogenic panel triggers
induction and the panel catches up in ~2 simulated minutes.
```

### Constrain

```
Constraints (non-negotiable):

1. No external dependencies. No CDN, no React, no library. Vanilla.
2. Single file. Drop it in a folder and double-click to run.
3. Mobile-friendly: the layout reflows on narrow viewports.
4. Labels must be biologically accurate. Use the chapter's terms
   (attachment, penetration, uncoating, replication, assembly,
   release; plus reverse transcription and integration for
   retroviruses; prophage and induction for lysogenic).
5. Don't invent steps that aren't in the chapter. If you think
   something is missing, surface the question rather than guessing.
6. Approximate timings only — label them as approximate. This is
   a teaching simulation, not a kinetic model.

If you cannot meet any of these, say which one and propose an
alternative before writing any code.
```

### Verify

After the LLM generates the file, open it and check every option. Specifically:

1. Does the lytic bacteriophage cycle have exactly six labeled steps in order?
2. Does the lysogenic mode actually pause and stay paused until you click "stress"?
3. Does the retrovirus mode add reverse transcription and integration?
4. Does the comparison mode run two panels in parallel time?
5. Are the labels grammatical and accurate?
6. Open the file with the network disabled. Does it still work? If it tries to load a CDN, constraint 1 was violated.

When something fails, give the LLM the specific failure — not a request for a rewrite. "The reverse transcription step is missing from the retrovirus mode" is more effective than "fix the retrovirus part."

### Extension exercise — bridge to Chapter 5

Once the simulator works, run this:

```
For each step in my HIV replication simulator, identify which
host cell biochemical pathway the virus is hijacking. Specifically:

- Translation: which host machinery is making viral proteins?
- Nucleotide synthesis: where do the building blocks for the
  viral DNA copy come from?
- Membrane lipids: where does the viral envelope come from?
- ATP and energy: which step of viral replication is most
  energy-expensive, and where does the ATP come from?

Be specific. Name the host pathway (glycolysis, oxidative
phosphorylation, lipid biogenesis, etc.) and the host molecule.

End with: which of these host pathways, if disrupted, would
also kill the host cell — and which could in principle be
selectively inhibited?
```

This conversation is the bridge into Chapter 5, where the actual biochemistry of the host pathways gets taught from the ground up. You are previewing the dependency.

---

## Exercises

### Warm-up

1. **The minimum virus.** Describe the minimum components of a virus in your own words. Then explain what an envelope adds and what it costs — name the specific structural property that makes enveloped viruses vulnerable to soap and non-enveloped viruses resistant to it.

2. **Baltimore classification.** A newly discovered virus has a single-stranded RNA genome that the host ribosome can read directly without any additional copying step. State its Baltimore class, explain the reasoning, and predict whether it must package a polymerase inside its virion. Repeat the exercise for a negative-sense RNA virus.

3. **Lytic vs. lysogenic in one paragraph.** Without using the words "lytic" or "lysogenic," describe in plain English the two strategies a bacteriophage can take after injecting its DNA, why each strategy makes sense from the phage's perspective, and what triggers the switch from one to the other.

### Application

4. **The soap question.** A hospital wants to select a hand sanitizer for use on a pediatric ward where both influenza and norovirus are circulating. The two candidates are alcohol-based gel and bleach solution. Using only the structural principles in this chapter, predict which pathogens each product will inactivate effectively and which it will not — and explain the mechanism in each case. Would your recommendation differ for a ward where rotavirus is the primary concern?

5. **Lysogenic conversion in the kitchen.** A food microbiology lab identifies two strains of *Vibrio cholerae* in oysters from the same harvest. Strain A produces cholera toxin. Strain B does not. Whole-genome sequencing shows they share 99.4% of their core chromosomes. Using the lysogenic conversion framework, explain the most likely source of the toxin-production difference, design a single experiment to test your hypothesis, and describe what result would confirm it and what result would refute it.

6. **Why combination therapy.** Explain, from the mechanism of reverse transcriptase, why treating HIV with a single antiretroviral drug reliably fails within months while treating it with three drugs targeting different steps does not. Your answer must include: what property of reverse transcriptase generates the standing population of variants, why a single drug creates selection pressure that a pre-existing variant can exploit, and why acquiring three simultaneous resistance mutations is statistically different from acquiring one.

### Synthesis

7. **The prion sterilization problem.** A neurosurgery unit discovers that a patient who underwent a brain biopsy last year has just been diagnosed with sporadic CJD. The instruments used were processed through standard autoclave (121°C, 15 minutes) between uses and have since been used on three other patients. Explain why the standard protocol was insufficient, what property of prions makes conventional sterilization fail, and what the unit should do now — both for the affected instruments and for the three subsequent patients. Reference the specific mechanism of prion propagation.

8. **Trace the disease chain.** A four-year-old eats undercooked beef containing *E. coli* O157:H7 and develops hemolytic uremic syndrome five days later. Trace the complete causal chain from the first ingestion to kidney failure. At each link, identify whether the agent responsible is the bacterium itself, the prophage, or the toxin — and name one point in the chain where an intervention could have broken it. Write your answer as a numbered sequence of no more than eight steps.

### Challenge

9. **The alive/not-alive question, operationalized.** The chapter argues the question "is a virus alive?" is malformed and proposes a better framing. Evaluate that framing: does it actually resolve the question, or does it relocate it? State explicitly what definition of life you're working with, apply it to a viroid (no protein, no capsid — just RNA), and then apply it to a prion (no nucleic acid — just protein). For each, state whether your definition classifies it as alive, not alive, or requires extension of the definition. End with: what observation, in principle, would force you to revise your definition?

---

## Tags

`acellular-pathogens` `virus-structure` `lytic-lysogenic-cycle` `HIV-replication` `prions` `lysogenic-conversion` `Baltimore-classification` `antiviral-drugs` `microbiology`

---

**What would change my mind:** If careful experiments showed that synthetic recombinant prion preparations, made from pure protein with no nucleic acid contamination, were reproducibly non-infectious, the protein-only hypothesis would need significant revision and the prion-as-category-unto-itself framing would have to soften.

**Still puzzling:** Why giant viruses look like reduced cells, why prion disease is so rare given how often the normal protein is expressed, and why viroids have never established in animal hosts despite billions of years of opportunity.

---

[^2]: Stanley, W.M. "Isolation of a crystalline protein possessing the properties of tobacco-mosaic virus." *Science* 81, no. 2113 (1935): 644–645. doi:10.1126/science.81.2113.644.
[^3]: Baltimore, D. "Expression of animal virus genomes." *Bacteriological Reviews* 35, no. 3 (1971): 235–241.
[^4]: Waldor, M.K., and Mekalanos, J.J. "Lysogenic conversion by a filamentous phage encoding cholera toxin." *Science* 272, no. 5270 (1996): 1910–1914. doi:10.1126/science.272.5270.1910.
[^5]: Royal Swedish Academy of Sciences. "The Nobel Prize in Physiology or Medicine 1975." https://www.nobelprize.org/prizes/medicine/1975/summary/
[^6]: Diener, T.O. "Potato spindle tuber 'virus.' IV. A replicating, low molecular weight RNA." *Virology* 45, no. 2 (1971): 411–428. doi:10.1016/0042-6822(71)90342-4.
[^7]: Prusiner, S.B. "Novel proteinaceous infectious particles cause scrapie." *Science* 216, no. 4542 (1982): 136–144. doi:10.1126/science.6801762.
[^8]: Brown, P., et al. "Iatrogenic Creutzfeldt-Jakob disease, final assessment." *Emerging Infectious Diseases* 18, no. 6 (2012): 901–907. doi:10.3201/eid1806.120116.
[^9]: Mushegian, A.R. "Are there 10^31 virus particles on Earth, or more, or fewer?" *Journal of Bacteriology* 202, no. 9 (2020): e00052-20. doi:10.1128/JB.00052-20.
