# Chapter 16 — Cancer Metabolism: Lipids, Amino Acids, and the Tumor Microenvironment


## TL;DR

- A cancer cell is a tiny factory that has chosen its inputs strategically.
- The chapter moves through Lipid metabolism in cancer, Glutamine addiction, Other amino acid dependencies, MTAP deletion and synthetic lethality, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

A cancer cell is a tiny factory that has chosen its inputs strategically.

Hold the framing. Chapter 11A introduced glucose metabolism — the Warburg effect — as cancer's most famous metabolic adaptation. But glucose is only one input. A growing cancer cell also needs *lipids* for membranes and signaling molecules, *amino acids* for proteins and as carbon sources, *nucleotide precursors* for DNA and RNA, and *reducing equivalents* (NADPH, NADH, FADH2) to drive biosynthesis. The cell rewires its lipid synthesis, becomes addicted to specific amino acids (especially glutamine), exports lactate into the surrounding tissue (which has consequences for nearby immune cells), and competes with neighboring cells for nutrients in ways that shape the *tumor microenvironment* — the complex ecosystem of cancer cells, stromal cells, immune cells, blood vessels, and extracellular matrix in which the tumor lives.

The metabolic landscape of a cancer cell, taken together, is one of the most aggressively reprogrammed aspects of its biology. Every major metabolic pathway is altered. And almost every alteration is now a therapeutic target — drugs that block fatty acid synthesis, drugs that interrupt glutamine import, drugs that target the metabolic competition between tumors and immune cells. Some are FDA-approved (IDH inhibitors, asparaginase). Many are in clinical trials.

This is the second of two chapters on cancer metabolism. This one covers the broader landscape beyond glucose — lipids, amino acids, the tumor microenvironment, and the therapeutic frontier of metabolic cancer treatment.

---

## Lipid metabolism in cancer

Lipids are essential for proliferating cells in several ways. Phospholipids and cholesterol are the building blocks of cell membranes — every new cell needs to double its membrane content before dividing. Signaling lipids (phosphatidylinositols, diacylglycerol, ceramide, prostaglandins) regulate intracellular signaling and intercellular communication. Stored lipids (triglycerides in lipid droplets) provide energy reserves. Modified lipids on proteins (myristoylation, palmitoylation, prenylation) regulate protein localization and activity.

Most differentiated cells in the body do not synthesize fatty acids de novo. They take them up from the bloodstream — derived from dietary fat or from the liver's lipogenic capacity. Cancer cells, by contrast, frequently *reactivate de novo fatty acid synthesis*. This is part of the metabolic reprogramming that allows tumor cells to escape dependence on extracellular lipid supply.

The de novo synthesis pathway:

1. *Citrate* is exported from mitochondria to the cytoplasm.
2. *ATP-citrate lyase (ACLY)* cleaves citrate to acetyl-CoA and oxaloacetate.
3. *Acetyl-CoA carboxylase (ACC)* converts acetyl-CoA to malonyl-CoA.
4. *Fatty acid synthase (FASN)* condenses acetyl-CoA and malonyl-CoA units, in cycles, to produce palmitate (16-carbon saturated fatty acid).
5. Palmitate is then modified by *elongases* (adding more carbons) and *desaturases* (especially SCD1, stearoyl-CoA desaturase 1, introducing double bonds) to produce the various fatty acids the cell needs.

FASN is highly expressed in many cancers (breast, prostate, lung, colon, pancreatic) and is often essential for cancer cell survival. FASN expression correlates with prognosis in several cancer types. FASN inhibitors (TVB-2640 and others) are in clinical trials. SCD1 inhibitors and ACLY inhibitors are also in development. ACC inhibitors (firsocostat, others, originally developed for liver disease) are being explored for cancer.

Cholesterol synthesis is similarly upregulated in many cancers. The mevalonate pathway, which produces cholesterol from acetyl-CoA, also produces isoprenoid intermediates that are essential for protein prenylation (modifying Ras and other GTPases for membrane attachment). *Statins* (HMG-CoA reductase inhibitors) — the cholesterol-lowering drugs used by millions for cardiovascular prevention — also affect cancer cell biology by reducing mevalonate flux. Epidemiological studies suggest that statin users have somewhat reduced cancer incidence and improved outcomes, though clinical trial evidence is mixed. The biology is plausible; the clinical effect is real but modest.

Lipid droplets are increasingly recognized in cancer biology. The cytoplasmic organelles store triglycerides and cholesterol esters and release them as needed for energy or membrane synthesis. Some cancers (especially clear cell renal cell carcinoma) carry massive lipid droplets — the cytoplasmic appearance is what makes them "clear" on microscopy. Lipid droplet metabolism is an emerging area of cancer biology.

Membrane lipid composition also matters. Different fatty acids and different headgroups produce membranes with different physical properties. Cancer cells often shift their membrane composition toward more saturated, more rigid lipids, which may resist apoptosis (membrane permeabilization during MOMP is affected by lipid composition) and ferroptosis (which depends on peroxidation of polyunsaturated fatty acids in membranes).

---

## Glutamine addiction

Glutamine is the most abundant amino acid in human blood (around 0.5 mM). It is a critical fuel and biosynthetic substrate for proliferating cells, including cancer cells.

The biology: glutamine enters cells through several transporters (SLC1A5/ASCT2, SLC38A2, SLC7A11, others). Once inside, glutaminase converts glutamine to glutamate, releasing one nitrogen as ammonia. Glutamate dehydrogenase (or transaminases) converts glutamate to α-ketoglutarate. α-Ketoglutarate enters the citric acid cycle.

Glutamine thus provides:

- *Carbon for the citric acid cycle* — replacing the carbons that are exported for biosynthesis (citrate to fatty acids, oxaloacetate to aspartate and pyrimidines, α-ketoglutarate to glutamate and proline).
- *Nitrogen for amino acid and nucleotide synthesis* — glutamine donates nitrogen to several biosynthetic reactions.
- *Glutamate for glutathione synthesis* — the major intracellular antioxidant.
- *Substrate for NADPH production* — via the malic enzyme reaction on cycle intermediates.

Many cancers are *glutamine-addicted*: they cannot survive or proliferate without continuous glutamine supply, even when glucose is abundant. The dependency is strongest in MYC-driven cancers (MYC drives glutamine transporter expression and glutaminase activity), in some KRAS-mutant cancers, and in cancers with reductive glutamine carboxylation (where α-ketoglutarate is reductively converted to citrate to feed lipid synthesis).

The therapeutic implications are large. *Glutaminase inhibitors* — CB-839 (telaglenastat) is the lead clinical compound — block the conversion of glutamine to glutamate in cancer cells. Trials in renal cell carcinoma and other cancers have shown modest activity, sometimes in combination with checkpoint inhibitors or with other targeted therapies. *Asparaginase* — a bacterial enzyme that depletes asparagine and glutamine in the bloodstream — has been used in acute lymphoblastic leukemia for decades; ALL cells cannot synthesize asparagine adequately and depend on extracellular supply, so asparagine depletion is lethal. *Glutamine transporter inhibitors* are in earlier development.

The challenges include the wide variation in glutamine dependence across cancers, the body's adaptation responses (other amino acid sources can partially compensate), and the toxicity to normal proliferating cells that also use glutamine.

---

## Other amino acid dependencies

Beyond glutamine, cancer cells exhibit various amino acid addictions or unusual metabolic features.

*Asparagine*. As mentioned, ALL cells cannot synthesize asparagine and depend on extracellular supply. Asparaginase depletion has been a backbone treatment for childhood ALL since the 1960s, contributing to the dramatic improvement in cure rates (now around 90 percent in pediatric ALL). Solid tumors with similar asparagine synthesis defects are being explored.

*Methionine*. Some cancers are addicted to methionine — they cannot grow on methionine-restricted media even when homocysteine (the immediate precursor) is provided. The methionine-dependence is partly due to defects in the methionine salvage pathway (especially in MTAP-deleted cancers — see below). Methionine-restricted diets are being explored in preclinical and early clinical settings.

*Cysteine and glutathione*. Cells synthesize glutathione (the major antioxidant) from glutamate, cysteine, and glycine. The cysteine is often the limiting amino acid; cells take it up as cystine (the oxidized dimer) through the xCT antiporter (SLC7A11) and reduce it intracellularly. The xCT transporter is upregulated in many cancers and is essential for maintaining glutathione levels. xCT inhibitors (sulfasalazine, erastin) are in development. Inducing oxidative stress through cysteine depletion can trigger ferroptosis (Chapter 10A).

*Branched-chain amino acids* (leucine, isoleucine, valine) are essential amino acids required for protein synthesis and as signaling molecules (leucine activates mTORC1). Some cancers have altered branched-chain amino acid metabolism, including overexpression of BCAT1 (branched-chain aminotransferase 1) in some leukemias.

*Tryptophan*. The amino acid tryptophan is degraded by indoleamine 2,3-dioxygenase (IDO) to kynurenine. IDO is upregulated in many cancers and creates a local tryptophan-depleted microenvironment that suppresses T-cell function (T cells require tryptophan for proliferation and effector function). IDO inhibitors (epacadostat and others) were heavily pursued as immune-enhancing cancer therapies; clinical results have been mixed.

*Arginine*. Some cancers (notably hepatocellular carcinoma and some melanomas) lack arginine biosynthesis and depend on extracellular arginine. Arginine deiminase (ADI) — a bacterial enzyme that depletes arginine — is being explored therapeutically.

The pattern across amino acids is consistent. Cancer cells adapt their amino acid metabolism to maximize biosynthesis under nutrient-limiting conditions, and the adaptations create dependencies that selective therapies can exploit.

---

## MTAP deletion and synthetic lethality

A particularly elegant amino acid-related cancer biology story involves MTAP and PRMT5.

*MTAP* (methylthioadenosine phosphorylase) is an enzyme in the methionine salvage pathway. Its substrate, methylthioadenosine (MTA), is a by-product of polyamine synthesis. MTAP cleaves MTA into adenine (which can be salvaged for nucleotide synthesis) and methylthioribose-1-phosphate (which can be salvaged back to methionine). MTAP is essential for efficient nucleotide and methionine salvage.

The *MTAP* gene is located on chromosome 9p21, immediately adjacent to *CDKN2A* (encoding p16). The *CDKN2A* locus is deleted in roughly 30 percent of all cancers; in many of these deletions, *MTAP* is co-deleted as a passenger. Approximately 15 percent of all human cancers are *MTAP-deleted*.

MTAP-deleted cells accumulate MTA — the substrate that can no longer be salvaged. The accumulated MTA is structurally similar to S-adenosylmethionine (SAM), the methyl donor for methyltransferases. MTA acts as a competitive inhibitor of *PRMT5*, an arginine methyltransferase that methylates histone H4 and various non-histone substrates.

The consequence: MTAP-deleted cells have partially inhibited PRMT5, and they are uniquely sensitive to *additional* PRMT5 inhibition. Normal cells have full PRMT5 activity and are not sensitive to PRMT5 inhibitor concentrations that kill MTAP-deleted cells.

The principle is *synthetic lethality* — the deleted gene (MTAP) and the inhibited gene (PRMT5) are both individually tolerable but together lethal. MTAP-deleted cells are already partially compromised by accumulated MTA; PRMT5 inhibitors push them over the edge.

PRMT5 inhibitors (MRTX1719, AMG-193, AG-270, and others) are in clinical trials specifically for MTAP-deleted cancers. Early results suggest selective activity in the deletion-positive population. The strategy is one of the cleaner examples of metabolism-informed precision oncology, identifying a deletion that occurs in 15 percent of cancers and providing a selective therapy for those cancers.

---

## The tumor microenvironment

A tumor is not just a clump of cancer cells. It is an ecosystem — cancer cells plus stromal cells (fibroblasts, immune cells, endothelial cells, pericytes, adipocytes) plus extracellular matrix plus blood vessels plus extracellular fluid and signaling molecules. The metabolic state of this ecosystem differs dramatically from normal tissue and shapes everything that happens inside it.

*Hypoxia and acidosis*. Solid tumors typically outgrow their blood supply, creating regions of low oxygen (hypoxia) and accumulated metabolic byproducts (acidosis from lactate excretion). The pH inside tumors is often 6.5 to 6.8, compared to 7.4 in normal tissue. Hypoxia and acidosis affect everything — cancer cell behavior, immune cell function, drug penetration, response to radiation (hypoxic tumors are more radioresistant because radiation damage requires oxygen for full effect).

*Nutrient depletion*. Cancer cells consume nutrients voraciously, and the local supply often runs short. Glucose levels in tumor interstitial fluid can be 5-fold lower than in serum. Glutamine, arginine, and other amino acids can be depleted. Vitamin levels (especially vitamins involved in one-carbon metabolism) can be reduced. The cells that share the microenvironment compete for what is left.

*Lactate accumulation*. Cancer cells excrete lactate from Warburg metabolism. The lactate accumulates in the microenvironment, contributing to acidosis. Lactate also has direct immunosuppressive effects — it inhibits T cell and NK cell function, polarizes macrophages toward the tumor-promoting M2 phenotype, and supports regulatory T cell (Treg) function.

*Immunometabolic competition*. T cells, like cancer cells, are proliferating cells that need glucose, glutamine, and other nutrients to function. Cancer cells outcompete T cells for these nutrients in the tumor microenvironment, contributing to T cell exhaustion and immune escape. This *metabolic immune suppression* is one mechanism by which tumors evade the immune system.

*Cancer-associated fibroblasts (CAFs)*. The stromal fibroblasts in tumors are not passive bystanders. They are metabolically active, often secreting metabolites and signaling molecules that support tumor growth. Some CAFs secrete lactate that cancer cells can take up and oxidize (the "reverse Warburg effect"). Others provide amino acids, growth factors, or extracellular matrix components.

*Adipocytes in tumor microenvironment*. In breast cancer, ovarian cancer, and others, adipocytes (fat cells) in the tumor microenvironment release fatty acids that cancer cells take up and use. The metabolic exchange between adipocytes and cancer cells is part of why obesity is associated with several cancers.

*Vasculature and perfusion*. Tumor blood vessels are typically chaotic — branched abnormally, leaky, sometimes blind-ended. The disorganized vasculature contributes to hypoxia, drug penetration problems, and the difficulty of delivering immunotherapies. Anti-angiogenic therapy (Chapter 12) is partly about reshaping this vasculature.

The picture that emerges is of a metabolically distinctive ecosystem where cancer cells, stromal cells, and immune cells all interact through metabolic exchange and competition. Therapeutic strategies are increasingly targeting this ecosystem rather than just the cancer cells alone.

---

## Therapeutic metabolic targeting

Drugs that target cancer metabolism span several categories.

*Direct enzyme inhibitors*. Compounds that inhibit specific metabolic enzymes in cancer cells. Examples: IDH1/IDH2 inhibitors (ivosidenib, enasidenib), MAT2A inhibitors for MTAP-deleted cancers, FASN inhibitors, glutaminase inhibitors (CB-839), PHGDH inhibitors, IDO inhibitors, ACLY inhibitors. The drugs work by selectively impairing a metabolic activity that the cancer depends on.

*Nutrient depletion*. Drugs or enzymes that deplete specific nutrients from the bloodstream. Asparaginase for ALL is the classical case. Arginine deiminase for arginine-auxotrophic cancers is in development. Glutamine depletion strategies are being explored.

*Antifolates*. Methotrexate, pemetrexed, and related drugs block folate-dependent one-carbon metabolism. They have been backbone agents since the 1940s and remain widely used.

*Hypomethylating agents*. Azacitidine and decitabine target DNA methyltransferases, indirectly modulating one-carbon metabolism by depleting cellular SAM pools as a side effect. The drugs are approved for myelodysplastic syndrome and AML.

*Synthetic lethal approaches*. PRMT5 inhibitors for MTAP-deleted cancers. MTH1 inhibitors for cancers with high oxidative stress. Others in development.

*Combinations with immunotherapy*. The understanding that the tumor microenvironment metabolism suppresses immune function has led to combination trials. Glutaminase inhibitors with PD-1 inhibitors. Lactate transport inhibitors with checkpoint blockade. IDO inhibitors with checkpoint inhibitors (though the early IDO trials were disappointing). The conceptual rationale is to remove the metabolic suppression so that immune therapy can work.

*Dietary interventions*. Caloric restriction. Ketogenic diets (which deplete glucose). Methionine-restricted diets. Specific amino acid restrictions. The preclinical evidence for dietary modulation of cancer is significant; the clinical translation is much harder because long-term dietary adherence is difficult and the effects in human trials are modest.

*Repurposed metabolic drugs*. Metformin (mild complex I inhibitor) has been associated with reduced cancer incidence in epidemiology. Statins (mevalonate pathway inhibitors) similarly. Aspirin (which affects prostaglandin metabolism and likely has multiple mechanisms) has clinical evidence for reduced colorectal cancer mortality. The repurposing approach is attractive because the safety profiles are well-established, but the effect sizes have generally been modest.

The field is rapidly developing. Cancer metabolism research has moved from descriptive (cataloging what's different in tumor cells) to mechanistic (understanding why) to therapeutic (drugging the mechanisms). The IDH inhibitor success has demonstrated the feasibility of metabolic targeting. The PRMT5/MTAP synthetic lethal approach shows the power of metabolism-informed precision oncology. More approvals are expected in coming years.

---

## What this chapter gives you

Cancer metabolism extends far beyond the Warburg effect of glucose. Lipid metabolism is upregulated to support membrane biosynthesis, with FASN, ACLY, and SCD1 as actively targeted enzymes. Many cancers are addicted to specific amino acids — glutamine in MYC-driven cancers, asparagine in ALL, arginine in some hepatocellular carcinomas, methionine in some tumors. The amino acid addictions create dependencies that selective therapies (asparaginase, glutaminase inhibitors, arginine deiminase) can exploit.

The MTAP-PRMT5 synthetic lethal axis exemplifies how metabolic dependencies created by recurrent gene deletions can be turned into therapeutic vulnerabilities. The mechanism — accumulated MTA inhibiting PRMT5 in MTAP-deleted cells — illustrates the elegant logic of synthetic lethality applied to metabolism.

The tumor microenvironment is a metabolically distinctive ecosystem characterized by hypoxia, acidosis, nutrient depletion, lactate accumulation, and metabolic immune suppression. Cancer cells, stromal cells, and immune cells compete and exchange metabolites in ways that shape tumor progression and therapeutic response. Targeting the metabolic microenvironment is becoming a key strategy in combination with traditional anti-cancer approaches.

Therapeutic metabolic targeting includes direct enzyme inhibitors (IDH inhibitors, FASN inhibitors, glutaminase inhibitors), nutrient depletion (asparaginase, ADI), antifolates, hypomethylating agents, synthetic lethal approaches, and combinations with immunotherapy. The pipeline is broad and active, and several drug classes are expected to gain FDA approval in coming years.

Chapter 12 turns to angiogenesis — the process by which tumors recruit blood vessels to supply their growth, and the antiangiogenic therapies that have become standard care in several cancers. The metabolic story of this chapter intersects with the angiogenesis story directly: hypoxia drives both HIF-mediated metabolic reprogramming and VEGF-driven angiogenesis, and the same tumor that needs new blood vessels needs them in part because of its metabolic demands.

---

## LLM exercises

1. Ask your LLM to walk through the de novo fatty acid synthesis pathway in cancer cells from citrate to palmitate. What are the key regulatory enzymes (ACLY, ACC, FASN, SCD1), which are upregulated in which cancers, and which are being targeted therapeutically? Identify the lead clinical candidates and their development status.

2. Have your LLM explain glutamine addiction in MYC-driven cancers. What does MYC do to upregulate glutamine uptake and utilization, and why are these cancers particularly vulnerable to glutaminase inhibitors? Cross-check the clinical trial data on CB-839 (telaglenastat) and assess whether the biology has translated to clinical benefit.

3. Use your LLM to construct the synthetic lethality logic between MTAP deletion and PRMT5 inhibition. Walk through the metabolic intermediate (MTA), its inhibition of PRMT5 in MTAP-deleted cells, and the resulting vulnerability. Then identify three other examples of metabolism-driven synthetic lethality in current preclinical or clinical development.

4. Ask your LLM to describe the metabolic features of the tumor microenvironment and how they suppress immune function. What are the specific mechanisms by which lactate, hypoxia, and nutrient depletion impair T cell activity? Then probe: what current combination therapies (metabolic drug + immune checkpoint inhibitor) are being tested, and what is the early evidence?

5. Have your LLM survey the evidence for repurposed metabolic drugs in cancer — metformin, statins, aspirin. For each, summarize the epidemiological evidence, the proposed mechanism, and the clinical trial results. Where is the evidence strongest, where is it weakest, and what would convince you to recommend (or not recommend) each for cancer prevention?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Karen Vousden** has spent decades showing that p53 — long known as a tumor suppressor — also reroutes cancer metabolism through serine, glutamine, and antioxidant pathways. Her work bridged classical tumor biology and modern metabolic oncology.

**Run this:**

```
Who is Karen Vousden, and how does her work on p53 and cancer metabolism connect to the lipid and amino-acid metabolism we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Karen Vousden"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of p53's non-canonical metabolic functions — the serine pathway, for example.
- Ask it to compare the textbook p53 story (apoptosis, cell cycle arrest) with the modern picture that includes metabolism and stress response.

What changes? What gets better? What gets worse?
