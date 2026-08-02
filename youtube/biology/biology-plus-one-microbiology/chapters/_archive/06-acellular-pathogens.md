# Chapter 06 — Acellular Pathogens

*A virus is a piece of code that needs a host to run.*

## The question before the answer

When you ask whether something is alive, the answer for a virus is genuinely "it depends what you mean."

Outside a host cell, an influenza particle is inert. It does not metabolize. It does not move. It does not respond to stimuli. It does not reproduce. You can sit it in a test tube for years and chemically it is doing nothing. You can crystallize it — the tobacco mosaic virus was crystallized in 1935 — and a crystal is a chemistry experiment, not an organism. [^1]

Inside a host cell, the same particle becomes the most aggressive entity in biology. It releases its genome into the cell, hijacks the cell's transcription and translation machinery, makes hundreds or thousands of copies of itself, and bursts the cell open to release them. A single virion can produce ten thousand virions in twelve hours. The next twelve hours are exponential.

The question "is a virus alive" is asking the wrong question. The right question is: what kind of entity needs to be characterized by its interaction with another entity in order to be characterized at all? A virus is not a thing. A virus is a thing-plus-host. And as soon as you accept that, the strangeness goes away and the chapter becomes tractable.

Prions, which we have already met, are even stranger. They are not even a thing-plus-host in the genetic sense. They are a protein shape that propagates by changing other proteins of the same kind into their shape. They have no genome. They are a piece of information stored in conformation rather than sequence.

This chapter is about the things microbiology counts as pathogens but which are not made of cells.

## Learning objectives

By the end of this chapter, you will be able to:

1. Describe the general structure of a virus (capsid, genome, envelope) and explain how each component constrains transmission.
2. Distinguish DNA viruses from RNA viruses and explain why the choice of genetic material affects mutation rate.
3. Distinguish the lytic cycle from the lysogenic cycle in bacteriophages and describe what determines which cycle a phage takes.
4. Describe how the replication of a retrovirus differs from that of a typical RNA virus.
5. Describe viroids and prions and explain why they exist outside the standard infectious-agent framework.

Prerequisites: Chapters 1–5.

## What a virus is

A virus is, at minimum, two things: a genome wrapped in a protein shell.

The genome can be DNA or RNA — never both — and can be single-stranded or double-stranded, linear or circular, segmented or unsegmented, positive-sense or negative-sense. These choices matter. They constrain how the virus replicates and how easily its genome mutates.

The protein shell is called a *capsid*. The capsid is built from one or a small number of protein subunits called *capsomers*, assembled in a regular geometric pattern — usually icosahedral (a 20-sided polyhedron) or helical. Some viruses additionally have a lipid envelope around the capsid, stolen from the host cell membrane when the virus exits, with viral proteins (glycoproteins) embedded in it. Enveloped viruses are typically more fragile in the environment (the envelope dries out) but better at infecting host cells (the envelope fuses with the host membrane).

Sizes range from about 20 nanometers (the smallest viruses, like parvoviruses) to 400 nanometers and up (the giant viruses — mimivirus, pithovirus — whose discoveries in the 2000s blurred the boundary between virus and cell). Most pathogenic viruses are in the 80–300 nm range.

## Tropism — which cell, which species

A virus does not infect every cell. It infects the cells whose surface receptors match the virus's attachment proteins. *Tropism* is the term for this specificity. HIV's envelope protein gp120 binds CD4 plus a coreceptor, both of which are found on certain T cells, macrophages, and dendritic cells. The receptor specificity determines which cells get infected and, indirectly, what disease results.

Tropism is also why a virus has a host range. Influenza A primarily infects birds, with periodic spillovers into pigs and humans. Rabies infects nearly every mammal. SARS-CoV-2 binds the ACE2 receptor, which is conserved enough across mammals that the virus can infect humans, cats, ferrets, mink, white-tailed deer, and a number of other species — and that conservation is part of why the pandemic has been so hard to contain.

Receptor specificity is also why most viruses do not jump species. The receptors a virus uses in its original host may not exist, or may exist in a slightly different form, in another species. When mutations change the virus's attachment protein in ways that allow it to use a different host's receptor, the result is a new viral host range. That is the central event in most pandemic emergences. We will come back to this in Chapter 16.

## How viruses replicate

The general viral replication cycle has six steps. The details differ by virus type, but the framework is universal.

1. **Attachment**. The virus binds host cell surface receptors via specific viral surface proteins.
2. **Penetration**. The virus enters the cell — by direct fusion of envelope with membrane, by endocytosis, or (for bacteriophages) by injecting the genome through the cell wall.
3. **Uncoating**. The capsid disassembles, releasing the viral genome into the cytoplasm or nucleus.
4. **Replication and synthesis**. The viral genome is copied, and viral proteins are synthesized using host ribosomes.
5. **Assembly**. New capsids form and package new copies of the genome.
6. **Release**. New virions exit the cell, either by bursting the cell open (lysis) or by budding through the membrane (acquiring an envelope on the way out).

The details of step 4 — replication and synthesis — depend on the genome type and are where the most interesting variation lies.

### DNA viruses

Most double-stranded DNA viruses replicate in the host nucleus using a combination of viral and host enzymes. Their replication is generally accurate, because they can use the host's DNA proofreading machinery. Examples: herpes simplex virus, varicella-zoster (chickenpox), Epstein-Barr virus, smallpox.

Smallpox is an exception to the "DNA viruses replicate in the nucleus" rule. Poxviruses replicate in the cytoplasm, encoding their own DNA polymerase and replication machinery. This is why they have larger genomes than typical viruses.

### RNA viruses, positive-sense

Single-stranded RNA viruses with positive-sense genomes act as their own messenger RNA. Once the genome is released into the cytoplasm, it is immediately translated by host ribosomes to produce viral proteins, including an RNA-dependent RNA polymerase that copies the genome to make negative-sense templates and then more positive-sense progeny genomes. Examples: poliovirus, hepatitis A, hepatitis C, rhinoviruses, coronaviruses (including SARS-CoV-2), dengue, West Nile, yellow fever, Zika.

RNA-dependent RNA polymerases lack the proofreading capability of DNA polymerases, which is why RNA viruses mutate fast — typically about a million times faster than DNA viruses per nucleotide per replication. This is the main reason RNA viruses are responsible for so many emerging diseases.

### RNA viruses, negative-sense

Single-stranded RNA viruses with negative-sense genomes cannot be translated directly. They must first be copied to a positive-sense intermediate by an RNA-dependent RNA polymerase that is packaged inside the virion itself. Examples: influenza, rabies, Ebola, measles, mumps, RSV.

### Retroviruses

The most strategically interesting class. A retrovirus carries a positive-sense single-stranded RNA genome and the enzyme reverse transcriptase. After entry, reverse transcriptase copies the RNA genome into double-stranded DNA. The viral DNA is then integrated into the host genome by another viral enzyme, integrase, becoming a *provirus*. The provirus is replicated along with the host's DNA whenever the host cell divides. Sometimes it is transcribed by host RNA polymerase II to produce new viral genomes and proteins.

The reason this matters: a retroviral infection cannot be cleared by removing virus particles from the body. The proviral DNA is part of the host's own genome. Every infected cell carries permanent viral DNA, indefinitely. This is why HIV cannot be cured with current antiviral therapy — therapy suppresses replication, but the provirus persists. Eradicating HIV would require destroying every cell carrying integrated provirus, which is biologically and clinically infeasible.

Reverse transcriptase was such a startling discovery (it violated the "DNA → RNA → protein" version of the central dogma that was taken as fixed) that David Baltimore and Howard Temin shared the 1975 Nobel Prize in Physiology or Medicine for it. [^2] Reverse transcriptase is now also a routine reagent in molecular biology — the basis of RT-PCR, which is how we detect RNA viruses in clinical samples. The enzyme has gone from biochemical heresy to laboratory tool in fifty years.

↳ **Dig Deeper — Endogenous retroviruses and the genome you inherited**

*About 8% of the human genome is made up of sequences that came from retroviruses that integrated into our ancestors' DNA millions of years ago. Some of those sequences now do important jobs.*

**Prompt:**
> Describe endogenous retroviruses (ERVs) in the human genome. How did they get there? Approximately what fraction of the genome is ERV-derived? What functions, if any, do they appear to serve in modern human biology — particularly the syncytin proteins, derived from retroviral envelope genes, that are essential for placenta formation? End by discussing whether ERVs have been implicated in any current human diseases.

**What to do with the output:** This is one of the more striking cases of "viral DNA repurposed for host function." Carry it forward to Chapter 10 (chromosome structure) and Chapter 11 (mobile genetic elements).

## Bacteriophages and the lytic/lysogenic switch

Viruses that infect bacteria are called bacteriophages — "phages" for short. They are the most numerous biological entities on Earth, outnumbering bacteria by roughly an order of magnitude. There are estimated to be 10³¹ phage particles on Earth at any moment. [^3]

Phages have a more visually striking structure than most animal viruses. The classic T-even phages (T2, T4, T6) have an icosahedral head, a hollow tail, a baseplate, and tail fibers that bind to specific receptors on the bacterial surface. The phage injects its DNA through the tail like a syringe.

Once the DNA is inside, the phage can take one of two paths.

### Lytic cycle

The phage immediately hijacks the bacterial machinery to produce hundreds of new phage particles. The cell is killed and ruptured (lysed) to release the progeny. This typically takes 20–40 minutes for a fast phage. The host cell dies; the surrounding bacteria are now in a phage-rich environment.

### Lysogenic cycle

The phage DNA integrates into the bacterial chromosome and goes quiet. The integrated phage genome is called a *prophage*. The bacterial cell continues to divide normally; each daughter cell inherits the prophage. The bacterium is now *lysogenic*. Most of the phage genes are silenced.

Under stress — DNA damage from UV light, antibiotics, or starvation — the prophage can be triggered to excise from the bacterial chromosome, switch on its lytic genes, and produce phage particles, killing the cell. The phage is essentially hedging: replicate quietly when the host is doing well, replicate explosively when the host is in trouble.

The lysogenic cycle has a major medical implication. Some bacterial toxins are encoded not by the bacterium's own chromosome but by prophages integrated into it. *Corynebacterium diphtheriae* produces diphtheria toxin only if it is lysogenic for the corynephage β. *Clostridium botulinum* produces botulinum toxin from a lysogenic prophage. *Vibrio cholerae* produces cholera toxin from a phage. Some strains of *E. coli* (like O157:H7) produce Shiga toxin from a prophage. The pathogenicity of these bacteria is essentially imported from a virus.

↳ **Dig Deeper — Phage therapy as a returning idea**

*Phage therapy preceded antibiotics. It was largely abandoned in the West when antibiotics arrived. Antibiotic resistance has revived interest, particularly for resistant infections.*

**Prompt:**
> Trace the history of bacteriophage therapy from d'Hérelle's early work in the 1920s, through its persistence in the Soviet Union, to the current revival as antibiotic resistance limits standard options. What are the main scientific advantages of phage therapy (specificity, evolution-along-with-pathogen) and the main practical disadvantages (narrow host range, immune response to phage, regulatory hurdles)? Discuss two recent high-profile cases of compassionate-use phage therapy for resistant infections.

**What to do with the output:** This is a real clinical option for multidrug-resistant infections that will recur in Chapter 14. The current state of phage therapy in 2025 is somewhere between "experimental" and "specialty therapy."

This is also one of the mechanisms of horizontal gene transfer we met in Chapter 1. The phage carries bacterial DNA from one host to another in a process called *transduction*. Antibiotic resistance genes have been spread between bacterial species this way. We will return to it in Chapter 11.

## Viroids — RNA without a coat

Viroids are smaller than viruses. They are short circular single-stranded RNA molecules — 246 to 401 nucleotides long, with no protein coat at all. They infect plants. The RNA has no protein-coding capacity but folds into characteristic structures that interfere with the plant's RNA processing machinery.

The first viroid identified was the potato spindle tuber viroid in 1971, by Theodor Diener. [^4] More than thirty viroids have been characterized since. They are responsible for significant agricultural disease — coconut cadang-cadang viroid kills coconut palms in the Philippines; citrus exocortis viroid affects citrus trees worldwide.

Viroids are interesting biologically because they are pure information — a self-replicating piece of RNA with no protein, dependent on host enzymes for everything. They are a working example of what an "RNA world" precursor to life might have looked like. If life passed through a stage where RNA molecules self-replicated using whatever enzymes were available, viroids may be a vestige of that stage that has survived by parasitizing modern plants.

There are no known viroids of animals.

## Prions — protein without RNA

A prion is even more reduced. It is a protein with no genome at all.

The discovery story is worth telling. Scrapie, a fatal neurological disease in sheep, had been recognized for centuries. By the 1960s it was clear that something infectious caused it. The infectious agent was passable from sheep to sheep and from sheep to other animals. But every attempt to find a virus or bacterium responsible failed. The agent survived treatments that should have destroyed any nucleic acid — ionizing radiation, UV light, nucleases, formalin. It seemed to behave like a protein but to transmit like an infection.

In 1982, Stanley Prusiner proposed that the infectious agent of scrapie was a protein. Just a protein. He coined the term *prion* — for *pro*teinaceous *in*fectious particle — and proposed a mechanism: a normal cellular protein, present in healthy brain tissue, was being converted to a misfolded form that aggregated into damaging fibrils, and the misfolded form was somehow inducing the normal form to also misfold. [^5]

The response from the field was that this was impossible. Proteins do not propagate. The genetic information that determines protein structure is in DNA, not in protein conformation. A protein that templated its own misfolding would be a self-replicating piece of structural information, which violated everything biology thought it knew about heredity.

It took fifteen years. The mechanism has been worked out in considerable detail. There is a normal cellular prion protein, PrP^C, present in healthy nerve cells. It can adopt an alternative misfolded conformation, PrP^Sc, that is rich in beta-sheets where the normal form is rich in alpha-helices. The misfolded form induces other PrP^C molecules to refold into the misfolded form on contact. The misfolded forms aggregate into amyloid fibrils that damage neurons. The disease propagates through the brain, killing neurons, producing the characteristic spongiform appearance (vacuoles in brain tissue) and inevitably killing the patient.

Prusiner won the Nobel Prize in 1997.

Prion diseases include:

- **Creutzfeldt-Jakob disease** (CJD) — Cora's diagnosis from Chapter 1. About 1 in a million per year worldwide. Most cases are sporadic; a small fraction are inherited; a smaller fraction are acquired (from contaminated medical instruments, growth hormone preparations, corneal transplants).
- **Variant CJD** — the human form acquired from cattle infected with bovine spongiform encephalopathy (BSE, "mad cow disease"). About 230 cases worldwide, mostly in the UK, in the 1990s and 2000s.
- **Kuru** — discovered in the 1950s in the Fore people of Papua New Guinea, transmitted by ritual cannibalism of deceased family members. Disappeared when the practice ended. Daniel Carleton Gajdusek shared the 1976 Nobel for this work, which was the first identification of prion disease as transmissible. [^6]
- **Fatal familial insomnia** — an inherited prion disease causing progressive insomnia and death within roughly a year of onset. Extraordinarily rare.

Why does a normal protein exist that can be hijacked into a self-propagating misfolded form? PrP^C is found in many tissues, including the immune system and the nervous system, but its normal function is not fully understood. Mice with the PrP gene knocked out are mostly normal — they show some subtle neurological defects with age. There may be a role in copper binding, in synapse maintenance, in myelin sheath integrity. The picture is incomplete. What we know is that the protein exists, that it can misfold, that the misfolded form propagates, and that the cumulative misfolding eventually destroys the brain.

There is some evidence that other neurodegenerative diseases — Alzheimer's, Parkinson's, Huntington's, ALS — involve protein-aggregation mechanisms with some prion-like features. The protein in each case is different. The mechanism — a misfolded protein inducing nearby copies to misfold — is similar enough that some researchers now refer to the broader category as "prion-like." Whether these diseases are transmissible from person to person in the way classical prion diseases are is still being investigated, but the evidence so far is that they are not, under normal circumstances. The transmission is across cells within a single patient, not across patients.

↳ **Dig Deeper — The "prion-like" hypothesis for Alzheimer's transmissibility**

*Several lines of evidence — accidental cases of amyloid-beta pathology from contaminated growth hormone, animal model transmission experiments — have raised the question of whether Alzheimer's can be transmitted between humans. The consensus is that ordinary contact does not transmit it. The picture at the edges is less clear.*

**Prompt:**
> Describe the evidence for and against the "prion-like" hypothesis of Alzheimer's disease transmissibility. Cover: animal model experiments showing that brain extracts can seed amyloid pathology; the 2015 Jaunmuktane et al. *Nature* paper on cadaveric growth hormone recipients with amyloid deposits; the (now-banned) practice of cadaveric pituitary growth hormone; what these findings do and do not imply about person-to-person transmission under normal circumstances.

**What to do with the output:** This is one of the more consequential open questions in neurology. The clinical implications would be enormous if Alzheimer's turned out to be transmissible under any normal circumstance. As of now, the consensus is that it is not — but the door is not entirely closed.

## What the chapter is really about

A virus is a piece of code that needs a host to run. A viroid is a piece of code with no protein. A prion is a piece of structural information with no code at all.

Each of these expands the working definition of what an infectious agent can be. Until 1898, "infectious agent" meant bacterium. The discovery of viruses (tobacco mosaic virus, Beijerinck and Ivanovsky) added a category — agents too small to be cultured on standard media, that pass through filters that retain bacteria. The discovery of viroids in 1971 added another category — agents made of RNA with no protein. The discovery of prions in 1982 added another — agents made of protein with no genome.

This is the same pattern we saw in Chapter 1. Each new category was resisted. Each was confirmed. Each forced an expansion of what microbiology counted as its subject.

I do not think the expansion is finished. There are infectious agents that have not yet been characterized and possibly categories of agent that we do not have the tools to detect. If you read about an emerging disease and the lab cannot identify the pathogen, do not assume the lab is incompetent. Assume that the agent might not fit any current category, and that the case might be the first of a category we will name in twenty years.

## Still puzzling

I do not understand why prion diseases are so rare. The mechanism — a normal protein that can misfold and template further misfolding — should, on the face of it, produce more disease than it does. The prion protein is expressed in many tissues across most mammals. Misfolding events presumably happen occasionally just by thermal fluctuation. The fact that sporadic CJD strikes only 1 in a million people per year suggests there is a robust quality-control mechanism that disposes of misfolded prion proteins almost all the time, and only rarely fails. I have not seen a satisfying account of what that mechanism is.

## What would change my mind

The classification of prion diseases as exclusively diseases of conformation, not sequence, would need revision if a true prion infectious agent were found to contain even minor nucleic acid contamination that is required for transmission. The infectivity of purified prion preparations has been demonstrated repeatedly, but the field has periodically had to argue against claims of residual nucleic acid. As of this writing, the protein-only hypothesis is the consensus, and synthetic prions made entirely from recombinant protein have demonstrated transmissibility, which strongly supports the model. `[verify: status of any 2025-26 challenges to the protein-only hypothesis]`

## LLM exercises

1. **A virus you have never met.** Ask the LLM to describe a viral genus you have never heard of, including its genome type, host range, and replication strategy. Use the chapter's framework (genome type, capsid, envelope, replication mechanism) to predict what the virus should look like and behave like. Compare to the LLM's description.
2. **Engineering a phage therapy.** If you wanted to use bacteriophages to treat an antibiotic-resistant bacterial infection, what features would you want in your phage? What features would you want to engineer out? Have the LLM walk through the design considerations. Compare to actual phage therapy work.
3. **Why are RNA viruses so successful?** Ask the LLM why RNA viruses are responsible for so many emerging diseases. Identify three reasons in the answer and rate each on biological plausibility. The chapter mentions mutation rate; the LLM should be able to identify additional factors.
4. **The prion conformation conversion.** Ask the LLM to describe the molecular mechanism by which PrP^Sc converts PrP^C to its misfolded form. Press the LLM on what is known mechanistically versus what is inferred. Where does the explanation become hand-wavy, and what would be needed to make it rigorous?
5. **The category boundary.** Have a conversation with the LLM about whether viruses, viroids, and prions should be considered "alive." Insist on operational definitions rather than philosophical handwaving. The point of the exercise is to make the disagreement productive: what experiment, in principle, would settle it?

## References

[^1]: Stanley, W.M. "Isolation of a crystalline protein possessing the properties of tobacco-mosaic virus." *Science* 81, no. 2113 (1935): 644–645. doi:10.1126/science.81.2113.644.
[^2]: Royal Swedish Academy of Sciences. "The Nobel Prize in Physiology or Medicine 1975: Tumour Viruses and Genetic Material of the Cell." https://www.nobelprize.org/prizes/medicine/1975/summary/
[^3]: Mushegian, A.R. "Are there 10^31 virus particles on Earth, or more, or fewer?" *Journal of Bacteriology* 202, no. 9 (2020): e00052-20. doi:10.1128/JB.00052-20.
[^4]: Diener, T.O. "Potato spindle tuber 'virus.' IV. A replicating, low molecular weight RNA." *Virology* 45, no. 2 (1971): 411–428. doi:10.1016/0042-6822(71)90342-4.
[^5]: Prusiner, S.B. "Novel proteinaceous infectious particles cause scrapie." *Science* 216, no. 4542 (1982): 136–144. doi:10.1126/science.6801762.
[^6]: Gajdusek, D.C. "Unconventional viruses and the origin and disappearance of kuru." *Science* 197, no. 4307 (1977): 943–960. doi:10.1126/science.142303.
---

## LLM Exercise — Chapter 6: Acellular Pathogens (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this chapter:** 4-5 viral entries + virus-specific schema fields.
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 6 of my Microbe Database project. Chapter 6 covered
acellular pathogens: viruses (DNA vs. RNA, single-strand vs.
double-strand, enveloped vs. naked, Baltimore classification);
viroids; prions.

Schema additions for viruses:
- **Genome_type**: dsDNA / ssDNA / dsRNA / +ssRNA / -ssRNA / RT-RNA
  / RT-DNA (Baltimore classification).
- **Envelope**: enveloped / naked (matters for transmissibility
  and disinfection — naked viruses are more environmentally stable).
- **Replication_site**: nucleus / cytoplasm.
- **Host_range**: humans, animals, plants, bacteria, archaea.

Add 4-5 viral entries:

1. **Influenza A virus** — ssRNA(-), enveloped, segmented genome
   (8 segments → antigenic shift and drift); seasonal flu pandemics.
2. **HIV-1** — ssRNA(+) retrovirus, enveloped, integrates into
   host genome; AIDS pathogen.
3. **Hepatitis B virus** — dsDNA-RT (Baltimore Group VII), enveloped;
   chronic liver disease; only DNA virus with reverse transcriptase.
4. **Rabies virus** — ssRNA(-), enveloped, bullet-shaped capsid;
   neurotropic; 99% fatality once symptoms appear.
5. *(optional)* **SARS-CoV-2** — ssRNA(+), enveloped, coronavirus;
   COVID-19; spike protein well-characterized.

For each entry, populate all schema fields + the new virus-specific
ones. Body section: replication strategy, transmission, vaccination
status, treatment.

End with: in your database, which viruses share the most fields
in common, and what does that tell you about classification by
function (Baltimore) vs. classification by clinical impact?
```

---

**What this produces:** 4-5 viral entries + virus-specific fields. Database now ~22-26 entries — almost half of the eventual ~40-60.

**How to adapt this prompt:**

- *For your own project:* If pandemic-preparedness focus, ensure SARS-CoV-2 and Ebola are in. If oncology focus, HPV and HBV/HCV.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Bulk INSERT with virus fields.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Schema flexibility tested again — viral entries need DIFFERENT fields than bacterial ones, but the database should accommodate.

**Preview of next chapter:** Chapter 7 covers microbial biochemistry — molecular building blocks. Adds biochemistry-related fields and 1-2 organism entries (notable for unusual biochemistry).


---

## AI Wayback Machine

**Martinus Beijerinck** was discovered the first virus — tobacco mosaic virus — in 1898 by showing the agent was a "contagium vivum fluidum".

**Run this:**

```
Who is Martinus Beijerinck, and how does their work connect to viruses and acellular pathogens we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Martinus Beijerinck"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Martinus Beijerinck's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Martinus Beijerinck's framework."

What changes? What gets better? What gets worse?
