# Chapter 9 — Cancer Etiology: Chemical and Radiation Carcinogens


## TL;DR

- A carcinogen is a molecule that finds your DNA and changes one of its letters.
- The chapter moves through The carcinogen classification system, Initiation, promotion, progression, Tobacco carcinogens, Other chemical carcinogens, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A carcinogen is a molecule that finds your DNA and changes one of its letters.

That is the whole story for chemical and radiation carcinogenesis, at the cellular level. The mechanisms are diverse — covalent adducts, ionization-driven breaks, oxidative damage, replication errors — but the endpoint is the same. Something binds DNA or breaks DNA or distorts DNA in a way that introduces a mutation. If the mutation lands in the wrong gene in the wrong cell, a clonal lineage acquires a small selective advantage, and the slow march toward cancer begins.

Chapter 3 introduced the major risk factors at the population level. This chapter goes deeper at the mechanistic level. *How* does benzo[a]pyrene from cigarette smoke mutate a DNA base? *How* does a UV photon cause a thymine dimer? *How* does ionizing radiation generate the specific kinds of damage that drive specific kinds of cancer? *How* did epidemiology and toxicology converge on the carcinogen classification system that now governs occupational safety and consumer regulation worldwide? These are questions about mechanism, and the mechanism is interesting because it ties the population-level statistics of Chapter 3 to the cellular biology of Chapter 4.

This chapter — the first of two on cancer etiology — covers the non-biological carcinogens: chemical and radiation. The next — 8B — covers the biological ones: viruses, bacteria, and the multifactorial framework that integrates all the causes. The split is principled. Non-biological carcinogens damage DNA directly through chemistry or physics. Biological carcinogens damage DNA indirectly, usually by introducing viral genes that drive proliferation, induce chronic inflammation that generates DNA-damaging by-products, or alter the cellular state in ways that promote mutation accumulation.

Hold the question: *given a specific carcinogen, what specific mutations does it produce, in what specific cells, and how do those mutations lead to cancer?*

---

## The carcinogen classification system

In 1965, the World Health Organization created the International Agency for Research on Cancer (IARC), headquartered in Lyon, France. One of IARC's central functions is the *Monographs Programme* — a systematic review of agents (chemicals, mixtures, exposures, infections, behaviors) for carcinogenicity. The program publishes monographs that classify agents into one of five groups:

- **Group 1**: Carcinogenic to humans (sufficient evidence in humans).
- **Group 2A**: Probably carcinogenic to humans (sufficient evidence in animals plus suggestive evidence in humans).
- **Group 2B**: Possibly carcinogenic to humans (limited evidence in either humans or animals).
- **Group 3**: Not classifiable as to carcinogenicity (inadequate evidence).
- **Group 4**: Probably not carcinogenic to humans (reserved for agents with strong evidence of *non*-carcinogenicity; very few agents have ever been placed here).

The system matters because it governs what gets regulated and how strongly. As of 2026, IARC has classified around 130 agents as Group 1, around 90 as Group 2A, several hundred as Group 2B, and the rest as Group 3 or 4. Group 1 classification typically triggers occupational exposure limits, product warnings, or outright bans depending on the agent and the jurisdiction.

The classification is based on three lines of evidence. *Human epidemiology*: do exposed populations have higher cancer rates? *Animal studies*: do exposed animals develop tumors? *Mechanistic evidence*: is there a plausible biological mechanism by which the agent could cause cancer? Strong evidence on all three pushes an agent to Group 1. Strong animal evidence with weak human evidence pushes to Group 2A. The system has been criticized for both excessive caution (classifying things like processed meat or aloe vera extract as Group 1 or 2B) and excessive permissiveness (some critics argue specific industrial chemicals deserve harder classifications than they have received). The system is not perfect, but it is the most systematic global framework for assessing carcinogenicity.

Two general principles emerge from decades of IARC analysis.

First, *dose matters*. Most carcinogens produce cancer in a dose-dependent way. Heavy exposure produces more cancer than light exposure. But for genotoxic carcinogens — those that directly damage DNA — there is no clean *threshold* below which exposure is safe; the model is generally one of linear dose-response with no threshold, though the absolute risk at very low doses may be vanishingly small.

Second, *latency is long*. Most cancers caused by a specific exposure take decades to manifest. Lung cancer from smoking typically appears 20-40 years after sustained heavy smoking begins. Mesothelioma from asbestos appears 30-40 years after exposure. The latency is one reason regulating new exposures is hard — by the time you see the cancers, the exposed population has been carrying the burden for a generation.

---

## Initiation, promotion, progression

The dominant framework for chemical carcinogenesis dates from work in the 1940s-1960s on mouse skin painting experiments. The framework holds that carcinogenesis proceeds in three stages.

*Initiation* is the irreversible step in which a carcinogen induces a mutation in a target cell. Initiation alone may produce no visible cancer; the initiated cell sits in the tissue carrying its altered DNA, indistinguishable from its neighbors.

*Promotion* is the (typically reversible) step in which non-mutagenic factors — chronic inflammation, hormonal stimulation, wound healing, certain non-genotoxic chemicals — cause the initiated cell to proliferate selectively. Tumor promoters are not themselves mutagenic, but they expand the initiated clone.

*Progression* is the further accumulation of mutations and clonal selection that produces frank malignancy — invasion, metastasis, the full hallmarks.

The framework was demonstrated experimentally with mouse skin. Apply a single dose of a genotoxic carcinogen (like dimethylbenzanthracene, DMBA) — no tumors develop. Then apply a non-mutagenic tumor promoter (like TPA, phorbol 12-myristate 13-acetate) repeatedly — tumors develop. Apply TPA without prior DMBA — no tumors. The initiator-promoter sequence is required; the order matters; the promoter does its work only on cells that have already been initiated.

The model has limitations. Real carcinogenesis is rarely so clean — most carcinogens have both initiating and promoting activities, and many cancers involve multiple initiating events. But the conceptual framework is still useful. It tells you that some exposures cause cancer by introducing mutations; others cause cancer by selecting for cells that already carry mutations. Public health interventions can target either stage. Eliminating initiators (banning carcinogens) and eliminating promoters (treating chronic inflammation, reducing obesity, addressing hormonal exposures) both reduce cancer incidence.

---

## Tobacco carcinogens

Tobacco smoke is the most thoroughly characterized human carcinogen mixture. Each puff of a cigarette delivers thousands of compounds, more than 70 of which are known or suspected carcinogens. The major classes:

*Polycyclic aromatic hydrocarbons (PAHs)*. Benzo[a]pyrene is the canonical example. PAHs are formed by incomplete combustion of organic material — tobacco, of course, but also charred meat, coal tar, diesel exhaust, soot. PAHs are themselves not directly carcinogenic; they require metabolic activation by cytochrome P450 enzymes (particularly CYP1A1, CYP1B1) to be converted into reactive epoxides. The benzo[a]pyrene diol epoxide (BPDE) is the ultimate carcinogen — a reactive molecule that binds covalently to guanine residues in DNA, forming a bulky adduct. The adduct, if unrepaired, causes G-to-T transversions during replication.

The signature of tobacco-smoke mutagenesis is in the *TP53* mutations of lung cancers. In smokers' lung cancers, the *TP53* mutations show a striking excess of G-to-T transversions at specific codons — codons 157, 248, 249, 273 — that are known to be targets of BPDE binding. In non-smokers' lung cancers, the *TP53* mutations are mostly G-to-A transitions, which is a different mutational signature reflecting a different etiology. The fingerprint of the carcinogen is readable in the genome of the tumor it produced, decades after the exposure.

*N-Nitrosamines*. Tobacco-specific nitrosamines (TSNAs) such as NNK and NNN are formed during tobacco curing. They are alkylating agents — molecules that transfer methyl or ethyl groups to DNA. The major DNA lesions are O6-methylguanine and 7-methylguanine. O6-methylguanine mispairs with thymine during replication, producing G-to-A transitions. NNK specifically induces lung adenocarcinoma in laboratory animals, and its DNA adducts are detectable in human smokers' lungs.

*Aromatic amines*. 4-Aminobiphenyl, 2-naphthylamine, and other aromatic amines were used historically in the dye and rubber industries and are also present in tobacco smoke. They are metabolically activated by N-hydroxylation, followed by O-acetylation, to produce reactive nitrenium ions that bind DNA. The signature mutation is at certain bladder cancer codons, and aromatic-amine-related bladder cancer was the canonical occupational cancer of the 19th and 20th century textile and dye industries.

*Acetaldehyde, formaldehyde, acrolein*. Small reactive aldehydes that bind DNA and cause crosslinks. Acetaldehyde is also produced endogenously from ethanol metabolism, which is part of why alcohol contributes to cancer risk in the upper aerodigestive tract.

*Polonium-210*. A radioactive isotope present in tobacco leaves (taken up from soil). Polonium-210 emits alpha particles, which deposit large amounts of energy in small volumes of tissue and produce double-strand DNA breaks. The contribution of polonium-210 to lung cancer in smokers is real but smaller than the chemical carcinogens.

*Metals (cadmium, nickel, chromium, arsenic)*. Multiple mechanisms — oxidative damage, displacement of zinc in DNA repair proteins, interference with epigenetic regulation. Trace presence in tobacco smoke contributes to cancer risk.

The dose-response is clean and steep. A heavy smoker (more than 20 cigarettes per day for more than 30 years) has a roughly 20-fold elevated lung cancer risk relative to a never-smoker. The relative risk scales with both intensity (cigarettes per day) and duration (years smoked); pack-years (a measure that multiplies the two) is a reasonable single number. Quitting reduces risk, slowly. Risk approaches but never quite returns to never-smoker baseline.

What is striking is the breadth of cancers tobacco causes. The original epidemiological focus was lung cancer (Doll and Hill 1950, Wynder and Graham 1950). Subsequent work added oral cavity, larynx, pharynx, esophagus, stomach, pancreas, kidney, bladder, cervix, and acute myeloid leukemia. The breadth makes sense mechanistically: the carcinogens in tobacco smoke distribute throughout the body and damage DNA wherever cells are dividing. Tissues in direct contact (lung, oral cavity) get the heaviest exposure, but the metabolites travel.

---

## Other chemical carcinogens

*Aflatoxin B1*. A mycotoxin produced by *Aspergillus flavus* and *Aspergillus parasiticus*, fungi that contaminate stored grains and peanuts in humid tropical climates. Aflatoxin is metabolized by cytochrome P450 to an epoxide that binds DNA, producing specifically a G-to-T transversion at codon 249 of *TP53* — one of the most specific mutational signatures known. Liver cancer rates in sub-Saharan Africa and parts of East Asia, where aflatoxin contamination of stored grains is common and where hepatitis B is endemic, are dramatically elevated; the combination of aflatoxin (initiator) and hepatitis B chronic infection (promoter, through chronic inflammation) is the carcinogenic synergy.

*Vinyl chloride*. The monomer for PVC plastic. Workers exposed to high levels (particularly in the polymerization step) developed angiosarcoma of the liver — a rare cancer that became unexplainably common in vinyl chloride workers in the 1960s and 70s. The mechanism is metabolic activation to a reactive epoxide that damages DNA. Recognition of the link led to dramatic reduction in occupational exposure limits.

*Benzene*. An aromatic hydrocarbon used historically as an industrial solvent and present in gasoline. Workers in petroleum refineries, chemical plants, and (historically) shoemaking developed acute myeloid leukemia at elevated rates. The mechanism is metabolic activation to reactive intermediates (benzoquinone, muconaldehyde) that damage hematopoietic stem cell DNA. Benzene is now classified as Group 1 and is regulated strictly in occupational settings.

*Asbestos*. A family of naturally occurring fibrous minerals (chrysotile, amosite, crocidolite, others) used extensively in the twentieth century for insulation, shipbuilding, automobile brake pads, and many other applications. Asbestos fibers, when inhaled, lodge in the pleura (the lining of the lungs) and cause persistent local inflammation. The signature cancer is mesothelioma — a rare cancer of the pleural lining with latency of 30-40 years after exposure. Asbestos also causes lung cancer (synergistically with smoking) and several other cancers. Most uses were banned in developed countries by the 1980s-90s, but mesothelioma cases continue to appear in workers exposed decades earlier.

*Chromium VI*. Hexavalent chromium, used historically in chrome plating, leather tanning, and pigment manufacture. Inhalation exposure causes lung cancer. The mechanism involves intracellular reduction to chromium III with generation of reactive oxygen species and DNA-protein crosslinks. Regulated as Group 1.

*Arsenic*. Naturally occurring in groundwater in some regions (Bangladesh, West Bengal, parts of the southwestern United States, parts of South America). Chronic ingestion causes skin, lung, bladder, and liver cancers. The mechanism involves oxidative damage, interference with DNA repair, and epigenetic modification. Public health interventions to provide arsenic-free water in affected regions are among the most cost-effective cancer prevention measures in the world.

*Cadmium, nickel, beryllium, formaldehyde, ethylene oxide*. Other Group 1 chemical carcinogens, each with its own mechanism and characteristic cancers.

The pattern is consistent: the carcinogens enter the cell, are activated by metabolism (often by cytochrome P450 enzymes that normally detoxify), produce reactive intermediates that bind DNA, generate specific mutations in characteristic patterns, and eventually lead to cancer. The mutational signatures are now detectable in tumor genome sequencing. A 2013 paper from the Sanger Institute (Alexandrov et al., *Nature*) cataloged about 30 mutational signatures across cancer types; many of them are recognizable as the fingerprints of specific carcinogens.

---

## Ionizing radiation

Ionizing radiation — X-rays, gamma rays, alpha particles, beta particles, neutrons — has enough energy to displace electrons from atoms, breaking chemical bonds. In biological tissue, the primary damage is to DNA, both directly (ionization of DNA atoms) and indirectly (ionization of water producing reactive oxygen species that diffuse to DNA).

The damage spectrum is characteristic. Ionizing radiation produces *single-strand breaks*, *double-strand breaks*, *base modifications*, and *crosslinks*. Double-strand breaks are the most consequential — they are dangerous to the cell because misrepair produces chromosomal abnormalities, and they require the homologous recombination or non-homologous end joining pathways introduced in Chapter 4.

The cancers ionizing radiation causes are diverse but follow patterns. *Leukemia* is one of the most radiation-sensitive cancers; the bone marrow's actively dividing hematopoietic cells are particularly vulnerable. *Thyroid cancer* is highly sensitive, especially in children — the thyroid concentrates iodine and is dosed heavily by radioactive iodine isotopes. *Breast cancer* in women exposed in adolescence is elevated. *Lung cancer*, *stomach cancer*, *colon cancer*, *bladder cancer*, and others all show dose-response relationships with radiation.

The evidence comes from several human populations.

*Atomic bomb survivors*. The Life Span Study, following roughly 120,000 survivors of Hiroshima and Nagasaki since 1950, is the foundational dataset. Excess cancers (especially leukemia in the first decade and solid tumors over longer follow-up) appeared in a dose-dependent pattern. The dose-response relationship has been used to extrapolate risks at lower doses for radiation safety standards.

*Nuclear workers*. Cohort studies of nuclear-industry workers in the US, UK, France, and elsewhere have produced dose-response relationships consistent with the atomic bomb data, with some refinement for chronic low-dose exposure.

*Medical radiation*. Patients receiving therapeutic radiation for one cancer have elevated risks of second primaries in the irradiated field decades later. Diagnostic CT scans, particularly in children, are associated with small but detectable increases in cancer risk.

*Radon-exposed miners*. Uranium miners and other underground miners inhaling radon daughter products (alpha-emitters) develop lung cancer at elevated rates. Residential radon (from natural radon emanating from soil and rock) is the second leading cause of lung cancer after smoking in the United States.

The dose-response model used for radiation safety is the *linear-no-threshold* (LNT) model: cancer risk increases linearly with dose, with no threshold below which exposure is safe. The LNT model is conservative; at very low doses, the data are noisy and some studies suggest possible hormetic effects (low-dose radiation may even have protective effects in some contexts). But for regulatory purposes, LNT is the default — it provides a clear framework and errs toward caution.

A typical chest X-ray delivers about 0.1 millisievert. A head CT delivers about 2 mSv. A chest CT delivers 5-10 mSv. A whole-body PET-CT delivers 25 mSv or more. The natural background radiation in most places is 2-3 mSv per year. The legal occupational exposure limit in most countries is 20 mSv per year averaged over 5 years (with no single year over 50 mSv). The radiation effective dose during a single transatlantic flight is about 0.05 mSv. For context: a single 100 mSv exposure increases lifetime cancer risk by approximately 0.5 percent above baseline.

---

## Ultraviolet radiation

Ultraviolet radiation is non-ionizing (it does not have enough energy to ionize atoms) but is energetic enough to cause specific kinds of DNA damage. The main lesion is the *cyclobutane pyrimidine dimer* — when UV-B (280-315 nm) hits adjacent pyrimidines (especially adjacent thymines), it covalently links them into a structure that DNA polymerase cannot read past. The *6-4 photoproduct* is a related lesion. Both lesions, if unrepaired, cause C-to-T transitions at dipyrimidine sites — the signature mutation of UV exposure.

The cancers caused by UV are mostly cutaneous. *Basal cell carcinoma* and *squamous cell carcinoma* are the most common — both are highly UV-driven, with the tumor genomes carrying massive C-to-T mutational burdens at dipyrimidine sites. *Melanoma* is the more lethal UV-related cancer; melanoma genomes show high mutational burden including the UV signature, though some melanomas (acral, mucosal) arise in non-sun-exposed sites and have different etiology.

The dose-response is intricate. Sunburn (acute high-dose UV) appears to be the dominant risk factor for melanoma — a history of severe blistering sunburns in childhood or adolescence dramatically elevates melanoma risk. Chronic moderate UV exposure (sun-exposed faces and hands of farmers, sailors, outdoor workers) drives the keratinocyte cancers more than melanoma. The biology may reflect different cells of origin — melanocytes versus keratinocytes — with different damage tolerance and different repair kinetics.

*Xeroderma pigmentosum (XP)* is the inherited disease that demonstrates the role of UV damage and nucleotide excision repair (NER, Chapter 4) in skin cancer prevention. XP patients carry biallelic mutations in NER genes (XPA through XPG, plus a few others) and cannot repair UV-induced thymine dimers. They develop hundreds of skin cancers before adolescence and rarely live past their twenties without strict sun avoidance. XP is the proof that the entire NER pathway exists, in normal people, primarily to protect against UV-induced cancer.

Prevention is straightforward in principle: sun avoidance during peak UV hours, protective clothing, broad-spectrum sunscreen (SPF 30 or higher), avoidance of tanning beds (which deliver intense UV-A and UV-B and are classified as Group 1 carcinogens). The execution is harder because UV exposure is also the primary source of vitamin D, and complete sun avoidance creates other health problems. The trade-offs are real and individual.

---

## What this chapter gives you

Chemical and radiation carcinogens damage DNA directly. Chemical carcinogens generally require metabolic activation by cellular enzymes, producing reactive intermediates that form covalent adducts with DNA. Different carcinogens leave different mutational fingerprints — tobacco-smoke G-to-T transversions at specific *TP53* codons, aflatoxin G-to-T at codon 249, UV C-to-T at dipyrimidine sites — that are now readable in tumor genomes.

Ionizing radiation acts directly through ionization, producing single- and double-strand breaks, base modifications, and crosslinks. The dose-response is approximately linear, with no clean safe threshold, and informs occupational and medical radiation standards. UV radiation acts through pyrimidine dimer formation and is the dominant cause of skin cancers.

The carcinogen classification system (IARC) provides the global framework for assessing carcinogenicity and informs occupational and consumer regulation. The system is imperfect but principled, and the population-level interventions it has supported — bans on asbestos, occupational exposure limits, smoking restrictions — have measurably reduced cancer incidence in countries that have implemented them.

Chapter 8B picks up with the biological carcinogens — viruses, bacteria, and the multifactorial integration that ties the various etiologies together.

---

## LLM exercises

1. Ask your LLM to walk through the metabolic activation of benzo[a]pyrene from cigarette smoke into BPDE and the formation of DNA adducts. What is the resulting mutational signature, and how is it detectable in lung cancer genomes? Cross-check the LLM's explanation with the COSMIC mutational signatures database.

2. Have your LLM compare the carcinogenicity classifications of three controversial agents in the IARC system — for instance, glyphosate, processed meat, mobile-phone radiofrequency emissions. For each: what group is it in, what is the underlying evidence, and what are the strongest counterarguments? Probe the LLM on whether the classification is being properly communicated to the public.

3. Use your LLM to generate a table comparing five major chemical carcinogens (tobacco PAHs, aflatoxin B1, benzene, vinyl chloride, asbestos) by mechanism, primary target cancer, latency, dose-response, and public health interventions. Identify any gaps in the LLM's information.

4. Ask your LLM to explain the linear-no-threshold (LNT) model for radiation carcinogenesis. What evidence supports it, what evidence challenges it, and how do regulatory agencies use it? Then probe: should LNT be revised in light of more recent data, or should it remain the conservative default?

5. Have your LLM design a public-health prevention campaign for residential radon exposure in your country. What is the prevalence of elevated indoor radon, what testing and remediation are recommended, and what are the cost-effectiveness numbers? Compare the LLM's recommendations with the actual EPA (or equivalent agency) guidance.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Bruce Ames** developed the Ames test in 1973 — a quick bacterial assay for chemical mutagenicity — that became the standard screen for carcinogens. He also developed the controversial view that endogenous oxidative damage matters more than synthetic chemicals for most cancers.

**Run this:**

```
Who is Bruce Ames, and how does the Ames test connect to the chemical and radiation carcinogens we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Bruce Ames"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the Salmonella reversion assay at the heart of the Ames test.
- Ask it about Ames's contested later thesis — that 99.9% of dietary carcinogens are natural, not synthetic.

What changes? What gets better? What gets worse?
