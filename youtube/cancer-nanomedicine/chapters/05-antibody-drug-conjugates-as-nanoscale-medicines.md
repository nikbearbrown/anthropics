# Chapter 5 — Antibody-Drug Conjugates as Nanoscale Medicines
*The Antibody Finds the Cell. Everything Else Decides Whether the Drug Kills It.*

A team is developing an antibody-drug conjugate against a solid tumor. Their antibody binds its target antigen with exquisite specificity — in culture, antigen-positive cells die and antigen-negative cells are untouched. Confident, they load eight drug molecules onto each antibody, reasoning that more payload means more killing. The construct is elegant on paper.

In animals, two things go wrong at once. The heavily loaded conjugate is cleared from blood far faster than the bare antibody, so less of it reaches the tumor. And the animals develop liver and bone-marrow toxicity that the antibody alone never caused — toxicity in tissues that do not express the target antigen at all. The linker holding the payload to the antibody was too unstable in plasma. It leaked the potent cytotoxin into the bloodstream, dosing the whole body with naked chemotherapy. The very feature meant to concentrate killing in the tumor had turned the construct into a poorly aimed cytotoxic drug with an antibody attached.

The team's error was treating the antibody's specificity as the whole story. An ADC is not a targeted antibody. It is a delivery chain with five places to fail, and the linker and loading they had optimized for "more killing" had broken two of them.

---

An **antibody-drug conjugate** is a three-part molecule: a monoclonal antibody, a cytotoxic payload, and a linker connecting the two. Each part has one job.

The **antibody** is the targeting module. It is engineered to bind one specific antigen, typically a protein expressed on the surface of cancer cells. When the antibody finds its antigen, it pulls the whole conjugate to the cell. This is the only step the antibody controls — which cell gets bound. Everything after binding depends on the other two components.

The **payload** is the warhead. ADC payloads are far too toxic to administer as conventional drugs — they kill cells at subnanomolar concentrations, hundreds to thousands of times more potent than standard chemotherapy. Microtubule poisons, DNA-damaging agents, and topoisomerase inhibitors are common choices. The whole rationale for connecting the payload to an antibody is to deliver a dose to cancer cells that would be lethal to the whole organism if given free. The payload provides the killing; the conjugate determines who receives it.

The **linker** is the chemistry tethering payload to antibody, and it is where selectivity actually lives. A linker that releases payload inside the target cell — and only there — concentrates killing where the antibody delivers the conjugate. A linker that releases payload in the bloodstream turns the antibody into a vehicle for dispersing chemotherapy systemically. The opening-case team had an elegant antibody and a potent payload and a linker that was undermining both.

![ADC anatomy with a Y-shaped antibody, linker, and payload warheads, paired with a five-step internalization sequence from antigen binding to payload hitting its intracellular target](images/05-antibody-drug-conjugates-as-nanoscale-medicines-fig-01.png)
*Figure 5.1 — ADC anatomy and internalization sequence*

<!-- → [DIAGRAM: ADC anatomy — Y-shaped antibody with antigen-binding domains at top; multiple payload molecules attached at multiple sites via linkers along the heavy chains; callouts labeling antibody (targeting: which cell), linker (control: when and where payload releases), payload (killing: mechanism of cell death); second panel showing internalization sequence: ADC binds antigen → cell takes up ADC by endocytosis → endosome acidifies and/or lysosomal enzymes cleave linker → payload released into cytoplasm → payload reaches target (DNA, microtubules, topoisomerase)] -->

---

The **drug-to-antibody ratio** — DAR — is the average number of payload molecules attached to each antibody. For most clinical ADCs, DAR sits between 4 and 8. That range is not arbitrary. It reflects a real trade-off that runs in both directions.

A DAR that is too low delivers too little cytotoxin to kill the target cell after internalization. Even if binding and internalization are efficient, the amount of payload released inside the cell must exceed the threshold required to kill it. Low DAR fails here.

A DAR that is too high creates a different problem. Cytotoxic payloads are small hydrophobic molecules, and attaching many of them to an antibody makes the conjugate progressively more hydrophobic and aggregation-prone. The immune system and the liver clear hydrophobic, aggregated proteins efficiently. A highly loaded conjugate is removed from circulation before it has time to accumulate in the tumor. The opening-case team loaded to DAR 8 on an antibody scaffold and linker chemistry that did not tolerate that load — the conjugate was cleared in hours rather than days, and the leaked payload poisoned tissues along the way `[verify — specific clearance kinetics]`.

The optimum DAR depends on the payload's hydrophobicity, the linker chemistry, and the conjugation site. Newer site-specific conjugation methods, which attach payload at defined positions on the antibody rather than at random surface lysines, claim to push usable DAR higher without the clearance penalty — the conjugate's aggregation behavior improves when every molecule has the same loading at the same position. Whether this genuinely breaks the DAR trade-off or relocates it to other variables is still being worked out `[verify]`.

---

Linkers are classified by how they release their payload. The two broad categories are **cleavable** and **non-cleavable**, and the distinction determines whether a bystander effect is possible.

**Cleavable linkers** are cut by conditions that are elevated inside cells relative to plasma. The endosome and lysosome are more acidic than the bloodstream; lysosomal enzymes like cathepsins cleave peptide sequences that are stable at plasma pH; glutathione concentrations are 100–1000 times higher inside cells than outside. A linker engineered to respond to any of these conditions will release payload only after the ADC is internalized — in principle. In practice, cleavable linkers are not perfectly stable in plasma, and the degree of premature release determines how much off-target toxicity the drug produces. This is the spectrum the opening case sits at the bad end of.

**Non-cleavable linkers** hold payload to the antibody through bonds that resist acid, enzymes, and reductants. Payload is freed only when the antibody itself is fully degraded inside the lysosome, releasing the drug still attached to an amino acid fragment. The released drug-linker fragment is typically charged and hydrophilic, which means it cannot cross cell membranes. It kills the cell it was internalized into. It does not diffuse into neighbors.

That membrane impermeability is both the safety feature and the limitation of non-cleavable linkers. Safety: payload released from premature degradation cannot enter normal cells that never internalized the conjugate. Limitation: the ADC can only kill cells it directly binds and enters, which means its efficacy is strictly bounded by antigen expression.

---

The **bystander effect** is what happens when freed payload can cross cell membranes and enter neighboring cells — including cells that never expressed the target antigen and never bound the ADC.

The mechanism: an ADC binds an antigen-positive cell, is internalized, the linker is cleaved, and a membrane-permeable payload is released into the cytoplasm. Some of that payload diffuses across the plasma membrane into adjacent cells, killing them even though they expressed no antigen.

The clinical consequence of this mechanism was one of the most significant therapeutic advances in breast cancer of the last decade.

**Trastuzumab emtansine (T-DM1)** is an anti-HER2 ADC with a non-cleavable linker and a microtubule-inhibitor payload. The freed payload bears a charged linker fragment and cannot cross membranes `[verify]`. T-DM1 kills cells it directly enters. In HER2-overexpressing breast cancer, where essentially every cancer cell is HER2-positive, this is sufficient — the ADC reaches every cell because every cell displays the antigen. In tumors that are **HER2-low** — expressing HER2 at low, heterogeneous levels — many cancer cells would never bind or internalize the ADC, and T-DM1 leaves them untouched.

**Trastuzumab deruxtecan (T-DXd)** is also built on the trastuzumab antibody but carries a topoisomerase-I-inhibitor payload at high DAR (~8) on a cleavable linker, and the freed payload is membrane-permeable `[verify]`. When T-DXd binds one of the few HER2-expressing cells in a HER2-low tumor, the released drug diffuses into neighbors — HER2-negative, HER2-low, and HER2-positive alike. The bystander effect spreads killing from the cells the antibody found to the cells the antibody could not bind.

This is why T-DXd, not T-DM1, opened HER2-low breast cancer as a treatable disease category. The antibodies are identical. The clinical behaviors are fundamentally different because the linker-payload combination after binding is what controls the outcome. "Anti-HER2" is not a sufficient description of an ADC.

The bystander effect is double-edged. The same membrane permeability that enables spreading tumor cell killing also means that payload released anywhere — including from premature linker cleavage in plasma — can enter normal cells in the vicinity. T-DXd carries a known risk of **interstitial lung disease and pneumonitis**, a potentially serious toxicity that requires monitoring and has been fatal in some cases `[verify — current label and incidence data]`. The width of the bystander effect's reach is essentially the same whether the payload is released in a tumor or in the lung parenchyma.

![Two-panel comparison over a HER2-expression gradient: T-DM1's contained payload killing only the cell it entered versus T-DXd's permeable payload spreading to antigen-negative neighbors](images/05-antibody-drug-conjugates-as-nanoscale-medicines-fig-02.png)
*Figure 5.2 — Bystander effect: T-DM1 vs T-DXd*

<!-- → [DIAGRAM: bystander effect panel — left: T-DM1 with non-cleavable linker, payload released inside antigen-positive cell, charged fragment stays inside, antigen-negative neighboring cell survives; right: T-DXd with cleavable linker, membrane-permeable payload crosses into antigen-negative neighbor and kills it; antigen expression level shown as gradient from high to low across cells] -->

---

For a payload molecule to kill a cancer cell, the ADC must clear five sequential steps. The antibody controls one of them.

**Step one: circulation.** The ADC must survive in blood long enough to reach the tumor. Linker stability in plasma governs loss here. An unstable linker releases payload in circulation; each release event both wastes a warhead and introduces free cytotoxin into the bloodstream. The opening-case team's conjugate failed primarily here — and the freed payload then committed step-five toxicity everywhere.

**Step two: antigen binding.** The ADC must bind its target antigen on the cancer cell surface. Antibody affinity, antigen expression level, and tumor perfusion govern this step. This is where targeting ligands operate — and only here. High antigen expression helps; heterogeneous expression (some cells high, others low or absent) limits it.

**Step three: internalization.** The bound ADC must be pulled into the cell, typically by receptor-mediated endocytosis. Not all antigen-antibody pairs trigger efficient internalization. An ADC whose target antigen does not cycle efficiently into endosomes will sit on the cell surface and be cleared without delivering payload. Some evidence suggests extracellular linker cleavage in the acidic tumor microenvironment contributes for certain constructs, but intracellular delivery remains the primary intended route `[verify]`.

**Step four: linker cleavage.** Inside the endosome or lysosome, the linker must be cleaved under conditions that are specific to that compartment. The cleavage triggers payload release. Non-cleavable linkers require full antibody degradation before the payload is freed. Cleavable linkers respond to pH, enzyme activity, or reductant concentration. The design question is: how stable in plasma, how labile in the lysosome?

**Step five: payload escape and action.** The freed drug must reach its intracellular target. A membrane-impermeable payload stays in the lysosome and may be pumped out by efflux transporters before it reaches DNA or microtubules. A membrane-permeable payload escapes into the cytoplasm and, in some cases, into neighboring cells. Drug-resistance mechanisms that upregulate efflux transporters affect this step. P-glycoprotein and MDR1 are the classic culprits; some ADC payloads are substrates and some are not — the choice of payload class affects step-five loss.

![Narrowing funnel of five ADC dose-loss steps from injected dose to payload action, with a terminal branch splitting into bystander benefit and normal-tissue toxicity](images/05-antibody-drug-conjugates-as-nanoscale-medicines-fig-03.png)
*Figure 5.3 — ADC five-step dose-loss funnel with bystander branch*

<!-- → [DIAGRAM: dose-loss funnel — vertical funnel from "injected dose" at top to "payload molecules acting at intracellular target" at bottom; five constriction bands labeled with the step name and the engineering parameter controlling loss at that step; side branch off step five showing membrane-permeable payload diffusing into neighboring cell (bystander) and into normal cell (toxicity); opening-case failure points marked at steps one and five with annotation of the mechanism] -->

Adding a targeting ligand addresses step two. It does not improve linker stability, internalization efficiency, lysosomal cleavage, or payload efflux resistance. The claim that "the antibody targets the tumor" is technically true at step two and silent about the other four steps — and in most ADC programs that fail, step two was not the limiting problem.

---

Two anti-HER2 ADCs, same targeting antibody, same clinical context: a breast tumor that is HER2-low.

T-DM1: non-cleavable linker, membrane-impermeable payload after release, DAR approximately 3.5. T-DXd: cleavable linker, membrane-permeable payload, DAR approximately 8.

The first instinct is that both should underperform equally in a HER2-low tumor — antigen is scarce, so little ADC binds, so little drug is delivered. Pick whichever is better tolerated.

That reasoning treats the antibody as the whole mechanism. It ignores what happens downstream of binding. T-DM1 kills only cells it directly binds and internalizes. In a HER2-low tumor where antigen-positive cells are sparse and interspersed with antigen-negative cells, the cells T-DM1 reaches are surrounded by cells it cannot reach. The antigen-negative majority survives. T-DXd, with its membrane-permeable payload, kills the HER2-positive cell it internalized into and the HER2-negative cells around it. From a small number of entry points, the drug spreads through the patch.

T-DXd is the correct choice for HER2-low disease, and the decisive variable is the linker-payload combination enabling the bystander effect. The antibodies are identical. The clinical outcomes are not.

The limit: in a uniformly HER2-high tumor, the calculation shifts. The bystander effect matters less when every cell is antigen-positive — T-DM1 can reach essentially all of them directly. Other factors now drive the comparison: payload class and potency, DAR and its clearance implications, and the toxicity profiles — specifically, T-DXd's pneumonitis risk, which requires active monitoring and dose interruption in a way T-DM1's toxicity does not.

---

The most successful ADC in oncology by any measure is T-DXd, and understanding why requires holding five things at once: the antibody that targets HER2, the high DAR that loads enough payload per molecule, the cleavable linker that releases it in the lysosome, the membrane-permeable payload that enables bystander killing, and the pneumonitis risk that membrane permeability also creates. Remove any one of those five and you get a different drug with different clinical behavior. The antibody is the part that gets named in the drug's name. It is not the part that explains its activity in HER2-low disease.

This is the discipline the chapter asks for: when evaluating an ADC — or any claim that targeting solves delivery — trace the delivery chain. Ask which step the design improvement actually addresses. Ask which normal tissue shares a dependency with the target tissue at any step where payload escapes. Ask whether the bystander effect is a feature or a liability in the specific tumor architecture being treated.

The antibody finds the cell. Everything else decides whether the drug kills it.

---

## Exercises

**Warm-up**

1. *[Recall — moderate]* Label the three structural parts of an ADC and state in one sentence each what each part determines about the drug's behavior. Then name which single part the opening-case team chose badly and describe the symptom in the animals that revealed it — connecting the symptom to the mechanism of failure.
*What this tests: whether you can connect each structural component to its specific function in the delivery chain, and trace a toxicity observation back to a design failure.*

2. *[Recall — moderate]* Explain why DAR is an optimum rather than a maximum. Name the specific consequence of DAR that is too low and the specific consequence of DAR that is too high, identifying the delivery-chain step where each failure occurs.
*What this tests: the DAR trade-off and its mechanistic basis — whether you understand why the problem runs in both directions.*

3. *[Recall — moderate]* Define the bystander effect, name the payload property that enables it, and explain why T-DXd — but not T-DM1 — produces it despite both carrying the same targeting antibody.
*What this tests: the mechanistic difference between non-cleavable and cleavable linkers and the role of membrane permeability in bystander killing — the pivot of the T-DM1 versus T-DXd comparison.*

**Application**

4. *[Apply — moderate-hard]* A new ADC has DAR 10, a plasma-stable cleavable linker, and a non-membrane-permeable payload, targeting an antigen uniformly expressed at high levels across the tumor. Predict whether it will show a bystander effect, assess whether its DAR is a concern, and identify in which tumor architecture — uniformly antigen-high versus antigen-heterogeneous — its lack of bystander effect matters least. Justify each prediction by naming the delivery-chain step involved.
*What this tests: applying the three design parameters (DAR, linker stability, payload permeability) to a new construct; using tumor architecture to determine which properties matter most.*

5. *[Apply — moderate-hard]* Compare T-DM1 and T-DXd for a patient whose tumor is **uniformly HER2-high**. Explain what changes in the bystander-effect argument when antigen-negative neighbors are rare, and identify what factors — payload class, DAR, toxicity profile — now drive the comparison. Your answer should reach a different emphasis than the HER2-low comparison and explain why.
*What this tests: recognizing when the bystander effect is and is not the decisive variable; adjusting the analysis when tumor architecture changes.*

6. *[Apply — hard]* A press release claims a new ADC is "exquisitely tumor-selective because of its high-affinity antibody." Write three specific questions you would ask before accepting the selectivity claim. At least one must concern linker plasma stability, one must concern payload membrane permeability, and one must concern a normal tissue that might share the relevant antigen or delivery vulnerability at any step in the chain.
*What this tests: applying the five-step delivery chain as a critical evaluation framework; identifying the three steps the antibody affinity claim says nothing about.*

**Synthesis**

7. *[Synthesis — hard]* Draw a dose-loss funnel for an ADC, from injected dose to payload molecules acting at the intracellular target. Mark all five delivery-chain steps, label each with the engineering parameter that controls loss there, and add a bystander-diffusion branch off step five. Then annotate the funnel twice: once for the opening-case team's high-DAR, unstable-linker design (marking where the most dose is lost), and once for T-DXd in a HER2-low tumor (marking where the bystander effect recovers killing that would otherwise be lost). Write two sentences summarizing what the two annotations reveal about what "delivery efficiency" means for these two constructs.
*What this tests: integrating all five steps into a spatial and quantitative model; using the funnel to compare two constructs with different failure modes.*

8. *[Synthesis — hard]* An ADC against a novel solid-tumor antigen has excellent in vitro killing of antigen-positive cells but disappointing in vivo activity. Propose three distinct hypotheses — each at a different delivery-chain step — that could explain the gap, and for each hypothesis: name the step, describe the specific failure mechanism, identify the experiment that would confirm or rule it out, and name the design modification that would address it if confirmed.
*What this tests: using the five-step framework as a diagnostic tool for translational failure; connecting each hypothesis to a mechanistic test and a design solution.*

**Challenge**

9. *[Challenge — very hard]* The "Still Puzzling" section notes that the bystander effect's spatial reach — how far membrane-permeable payload travels from a releasing cell into surrounding tissue — is not quantified in a way that lets engineers tune it predictably. This same reach governs both therapeutic spread in the tumor and off-tumor toxicity in normal tissue. Design a quantitative study — specifying the in vitro model, imaging modality, mathematical model, and in vivo validation approach — that would characterize the payload diffusion radius as a function of payload hydrophobicity and membrane permeability. Then explain how you would use the resulting data to set a payload permeability specification for a new ADC program targeting an antigen expressed at low levels in both tumor and a normal tissue of concern — specifically, how you would define the permeability window that maximizes bystander killing in the tumor while staying below the toxicity threshold in the normal tissue.
*What this tests: translating a mechanistic gap into a quantitative experimental design; applying physical chemistry reasoning to a therapeutic index optimization problem.*

---

## What Would Change My Mind

The central claim of this chapter is that an ADC's selectivity and clinical behavior are governed downstream of antibody binding — by linker stability, DAR, and payload membrane permeability — so that the antibody alone does not determine the outcome. The cleanest finding that would revise this: a head-to-head clinical comparison of ADCs identical in antibody, linker, and payload but differing only in DAR, showing that efficacy and toxicity track DAR negligibly across a wide range, while a separate comparison of ADCs differing only in antibody affinity showed affinity dominating outcome. That pattern would invert the chapter's emphasis. To date the evidence runs the other way: same-antibody ADCs (T-DM1 vs. T-DXd) behave very differently because of their linkers and payloads. I would also revise if rigorous data showed the bystander effect explanation for T-DXd's HER2-low activity is an artifact and the activity is fully explained by direct antigen-positive cell killing `[contested — see pantry flag]`.

## Still Puzzling

- **How much payload actually reaches the tumor?** As with all nanomedicines, the injected-dose-to-tumor fraction for ADCs is poorly characterized in patients, and the delivery-chain framing would be far sharper with real biodistribution numbers per step `[verify]`.
- **Why do some ADCs work without obvious internalization?** Extracellular linker cleavage in the acidic tumor microenvironment may contribute for some constructs, but the relative weight of intracellular versus extracellular release is unsettled `[verify]`.
- **What sets the ceiling on the bystander effect?** Membrane-permeable payloads enable bystander killing, but how far the freed drug travels — and how that distance trades against off-tumor toxicity — is not quantified in a way that lets engineers tune it predictably.
- **Is there a principled upper limit on DAR?** Newer site-specific conjugation chemistries claim to push DAR higher without the clearance penalty. Whether this genuinely breaks the DAR trade-off or relocates it remains open `[verify]`.

## References

- NCI. *Targeted Therapy for Cancer.* https://www.cancer.gov/about-cancer/treatment/types/targeted-therapies
- NCI. *Cancer and Nanotechnology.* https://www.cancer.gov/sites/ocnr/cancer-nanotechnology
- Matsumura, Y., & Maeda, H. (1986). A new concept for macromolecular therapeutics in cancer chemotherapy. *Cancer Research*, 46(12 Pt 1), 6387–6392.
- Wilhelm, S., et al. (2016). Analysis of nanoparticle delivery to tumours. *Nature Reviews Materials*, 1, 16014.

---

## Prompts

### Figure 5.1 — ADC anatomy and internalization sequence
Build a two-panel figure. Panel A (anatomy schematic): a Y-shaped antibody with antigen-binding domains, a linker tethering payload warheads along the heavy chains; callouts labeling antibody (targeting: which cell), linker (control: when/where payload releases), payload (the kill). Render the antibody in sky-blue (anchor), the linker in reddish-purple, the payload warheads in vermillion. Panel B (horizontal internalization process, left to right): Antigen binding at cell surface → Endocytic engulfment into vesicle → Endosome acidifies, linker cleaved → Payload released to cytoplasm → Payload hits DNA/microtubule target; connect the five stages with rightward arrows. Encode Stage 1 (binding) as the sky-blue anchor, Stage 3 (cleavage) as a transitional hue, Stage 4 (release) in dominant blue, Stage 5 (target hit) in green (positive). Direct-label each stage. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned via CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.2 — Bystander effect: T-DM1 vs T-DXd
Build a two-panel comparison over a shared cell field whose antigen expression runs as a gradient from high to low (HER2-high to HER2-low/negative cells). Left panel "T-DM1 (non-cleavable, impermeable)": payload freed inside one antigen-positive cell stays confined; antigen-negative neighbors survive intact; kills only the cell it entered; HER2-low tumors untreatable. Right panel "T-DXd (cleavable, permeable)": freed payload crosses the membrane and diffuses out; antigen-negative neighbors die; bystander killing spreads across the patch; opens HER2-low tumors as treatable. Use the same cell-field layout in both panels so the only difference is payload fate. Encode contained/surviving-neighbor outcomes (T-DM1's untreatable HER2-low) in vermillion (blocking/negative); encode bystander spread and "opens HER2-low as treatable" in green (positive). Annotate the shared axis "Payload fate after entering one antigen-positive cell". Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned via CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 5.3 — ADC five-step dose-loss funnel with bystander branch
Build a left-to-right narrowing funnel of six stages tracing ADC dose to action, with a terminal fork. Stages: Injected dose; Circulation survival / linker stability; Antigen binding; Internalization; Linker cleavage; Payload escape / action. Each stage is a segment narrowing monotonically left to right; connect with rightward arrows. At the terminal stage, split into a two-way branch: diffusion to a neighboring tumor cell (bystander benefit) versus to a normal cell (toxicity). Encode the first stage (Injected dose) in dominant blue; the four intermediate loss stages (circulation, binding, internalization, cleavage) in vermillion (blocking/negative); the terminal payload-action stage in green (positive). At the fork, color the bystander-benefit arm green and the normal-tissue-toxicity arm vermillion. Direct-label each stage and both fork arms. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned via CDN, Okabe-Ito colorblind-safe palette via CSS variables.
