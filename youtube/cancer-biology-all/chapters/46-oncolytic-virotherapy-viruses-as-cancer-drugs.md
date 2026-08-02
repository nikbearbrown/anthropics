# Chapter 46 — Oncolytic Virotherapy: Viruses as Cancer Drugs


## TL;DR

- This chapter gives a working overview of Oncolytic Virotherapy: Viruses as Cancer Drugs, focusing on the ideas a reader needs before moving to the next chapter.
- The chapter moves through The principles of oncolytic virotherapy, Talimogene laherparepvec (T-VEC), Other oncolytic virus platforms, Delivery and access, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Viruses can cause cancer. They can also cure it.

Hold the inversion. Chapter 8B covered viruses as causes of cancer — HPV driving cervical cancer, hepatitis B and C driving liver cancer, EBV driving Burkitt lymphoma, KSHV driving Kaposi sarcoma. Persistent viral infections produce mutations, drive proliferation through viral oncoproteins, induce inflammation that accelerates carcinogenesis. About 13% of human cancers are caused by infections.

But viruses can also be turned against cancer. *Oncolytic viruses* selectively replicate in cancer cells, killing them through lysis and stimulating immune responses against tumor antigens released during cell death. The therapeutic principle was suggested by clinical observations dating to the early 20th century — patients with cancer occasionally experiencing remissions during or after viral infections. The mechanism was unclear but the observation was real. Modern oncolytic virotherapy is the deliberate engineering of viruses to exploit this principle systematically.

The field has been slowly productive. Talimogene laherparepvec (T-VEC, Imlygic) was approved by the FDA in 2015 for advanced melanoma — the first FDA-approved oncolytic virus in the United States. Several other oncolytic viruses are in advanced clinical development. The technology has limitations (most useful for accessible tumors that can be injected; systemic delivery remains challenging; pre-existing immunity neutralizes the virus before it reaches the tumor) but also unique advantages (selective cancer cell killing, immune system engagement, ability to be engineered to express therapeutic payloads).

This chapter — the second of two on gene therapy and oncolytic virotherapy — covers the principles of oncolytic virotherapy, the major virus platforms in clinical development, the clinical applications, the integration with other therapies (especially immune checkpoint inhibitors), and the future directions of the field.

Hold the question: *if viruses can both cause and cure cancer, what determines which side they're on?*

---

## The principles of oncolytic virotherapy

Oncolytic viruses are viruses that replicate selectively in cancer cells, lyse them, and spread to neighboring cancer cells in a self-amplifying process. The mechanism produces several therapeutic effects:

*Direct cytolysis*. The virus replicates in the cancer cell, eventually causing the cell to burst and release new viral particles. The cell dies, contributing to tumor reduction.

*Immune activation*. The viral infection and cell death release viral antigens, tumor antigens, and damage-associated molecular patterns (DAMPs) that activate innate and adaptive immunity. The local immune response can extend beyond the directly infected cells and target the broader tumor.

*Abscopal-like effects*. Local oncolytic virus treatment can sometimes produce systemic effects through immune mechanisms — distant lesions regress without direct viral infection. The phenomenon is similar to the abscopal effect from radiation but more reliably observed with oncolytic viruses (though still inconsistent).

*Modulation of the tumor microenvironment*. The viral infection alters the immune cell infiltration and signaling environment of the tumor, potentially making it more receptive to other immunotherapies.

The selectivity for cancer cells comes from several mechanisms:

*Natural tropism*. Some viruses have a natural tendency to replicate better in cancer cells than in normal cells. The replication may depend on factors more abundant in cancer cells (specific surface receptors, active proliferation, defective antiviral responses).

*Engineered selectivity*. Viruses can be genetically modified to delete genes essential for replication in normal cells but dispensable in cancer cells. For instance:
- *ICP34.5 deletion* in herpes simplex virus (used in T-VEC). ICP34.5 counteracts host antiviral responses; cells with intact antiviral signaling (normal cells) shut down infection without ICP34.5. Cancer cells with defective antiviral signaling allow the deleted virus to replicate.
- *E1B-55 deletion* in adenovirus. E1B-55 inactivates p53. In cells with intact p53 (normal cells), the virus without E1B-55 cannot replicate. In cancer cells with mutated p53, the virus replicates freely.
- *Various other engineering* targeting specific cancer-associated defects.

*Tumor-specific promoters*. Viral genes essential for replication can be placed under control of tumor-specific promoters (PSA promoter for prostate cancer, AFP promoter for hepatocellular carcinoma, telomerase promoter for many cancers). The virus replicates only in cells where the promoter is active.

*Defective antiviral responses in cancer cells*. Cancer cells often have impaired interferon signaling and other antiviral defenses. This makes them more susceptible to viral infection than normal cells with intact defenses.

The combination of these mechanisms allows oncolytic viruses to preferentially replicate in cancer cells while sparing normal tissue.

---

## Talimogene laherparepvec (T-VEC)

T-VEC is the first FDA-approved oncolytic virus and the most clinically established. It is an engineered herpes simplex virus type 1 (HSV-1) with specific modifications:

*ICP34.5 deletion*. Removes the gene that counteracts host antiviral responses. The virus cannot replicate effectively in cells with intact antiviral signaling. Cancer cells with defective signaling allow replication.

*ICP47 deletion*. ICP47 normally blocks MHC class I-mediated antigen presentation in HSV-infected cells (helping the virus evade immunity). Deleting it allows the infected cancer cells to present viral and tumor antigens to T cells, enhancing immune recognition.

*GM-CSF insertion*. The deletion creates space for inserting a therapeutic gene. T-VEC encodes human GM-CSF (granulocyte-macrophage colony-stimulating factor) under control of the CMV promoter. The infected cells produce GM-CSF, which recruits and matures dendritic cells locally, enhancing immune responses against the released tumor antigens.

The clinical use:
- T-VEC is injected directly into accessible cutaneous, subcutaneous, or nodal melanoma lesions.
- Multiple injections over time (typically every 2 weeks for at least 6 months).
- Local lesion regression occurs in most patients.
- Some systemic responses occur (regression of non-injected lesions), reflecting the immune mechanism.

The pivotal OPTiM trial (T-VEC vs. GM-CSF alone in unresectable stage IIIB-IV melanoma) showed:
- Durable response rate (lasting ≥6 months) of 16% with T-VEC vs. 2% with GM-CSF alone.
- Overall response rate of about 26%.
- Modest overall survival benefit.

T-VEC was approved in 2015. Use has been substantial but bounded by the requirement for accessible, injectable lesions and the substantial logistic requirements of repeated intratumoral injections.

T-VEC has been combined with immune checkpoint inhibitors:
- *T-VEC + ipilimumab*. Improved response rates compared to either alone in melanoma.
- *T-VEC + pembrolizumab*. Showed promise in early trials, though the phase 3 MASTERKEY-265 trial in melanoma did not show significant benefit over pembrolizumab alone — a disappointing result that has tempered enthusiasm for some combinations.

The T-VEC experience illustrates both the promise (real clinical activity, immune mechanism) and the limitations (modest absolute benefit, intratumoral injection requirement) of current oncolytic virotherapy.

---

## Other oncolytic virus platforms

Multiple virus platforms are being developed for oncolytic applications. Each has its own advantages and limitations.

*Herpes simplex virus (HSV)*. T-VEC is the prototype. Other HSV-based oncolytics:
- *Nivolumab combined with HSV variants*. Multiple combinations in development.
- *NSC-CRAd-S-pK7*. A different HSV variant.
- *Various engineered HSV with additional therapeutic genes*.

The HSV platform has the advantages of large cargo capacity (allowing insertion of multiple therapeutic genes) and clinical experience with T-VEC. Limitations include pre-existing immunity in many patients and challenges with systemic delivery.

*Adenovirus*. The first virus explored for oncolytic applications. Various engineered adenoviruses are in development:
- *ONYX-015* and *H101* (delta-24 adenovirus variants). ONYX-015 was widely tested in head and neck cancer with some efficacy but not approved in the US. H101 was approved in China in 2005 (Oncorine) for head and neck cancer.
- *DNX-2401* and others. Engineered adenoviruses in clinical trials for glioblastoma, sarcoma, and other cancers.
- *AdV-tk*. Adenovirus expressing HSV-tk for ganciclovir-based suicide gene therapy.

The adenovirus platform has advantages of high infectivity and ease of engineering, plus extensive clinical experience. Limitations include strong immune responses that prevent repeat dosing and rapid clearance from the bloodstream.

*Vesicular stomatitis virus (VSV)*. A negative-sense RNA virus with natural sensitivity to interferon (which is absent or impaired in many cancer cells). VSV-based oncolytics are in clinical trials.

*Newcastle disease virus*. A bird virus that doesn't typically infect humans. Various Newcastle disease virus oncolytics in development.

*Measles virus*. Engineered to lack the disease-causing features. *MV-NIS* (modified measles virus expressing sodium iodide symporter) has been tested in various cancers; the SIS gene allows imaging of viral distribution and concentration of iodine isotopes for combined therapy.

*Vaccinia virus*. A poxvirus used as smallpox vaccine. Engineered for oncolytic applications. *Pexa-Vec (JX-594)* was a vaccinia-based oncolytic that showed some activity in hepatocellular carcinoma but its phase 3 trial was negative.

*Reovirus*. A double-stranded RNA virus. *Reolysin (pelareorep)* is a wild-type reovirus tested in many cancers, particularly those with activated Ras signaling (where reovirus replicates preferentially).

*Coxsackievirus*. *CVA21* (Cavatak) and other variants in clinical trials.

*Parvovirus*. *H-1PV* and others.

*Seneca Valley Virus*. A picornavirus with selective tropism for some cancer types.

*Polio virus* (recombinant, attenuated). *PVS-RIPO* (recombinant polio virus with rhinovirus IRES) tested in glioblastoma. Granted breakthrough therapy designation by FDA in 2016, though full approval has not yet been achieved.

The diversity of platforms reflects the recognition that different viruses have different properties relevant for different cancer applications. The choice of virus involves consideration of tumor type, target tissue accessibility, pre-existing immunity, manufacturing considerations, and the specific engineering needed.

---

## Delivery and access

Oncolytic viruses must reach cancer cells to work. The major delivery routes:

*Intratumoral injection*. The dominant approach. Direct injection into accessible cutaneous, subcutaneous, lymph node, intracranial, or intrahepatic tumors. The virus concentrates locally, replicates, and may spread to adjacent regions or systemically through immune mechanisms.

Advantages: high local concentration, less systemic exposure, less immune clearance of the virus.

Limitations: requires accessible tumors. Many tumors (lung, pancreas, peritoneal disease) are difficult to inject reliably. Multiple injections are typically needed.

*Intravenous administration*. Systemic delivery aimed at reaching all metastatic sites.

Advantages: reaches widespread disease.

Limitations: pre-existing immunity often neutralizes the virus rapidly in circulation; the virus is cleared by the liver and spleen before reaching tumors; small fractions reach the tumor.

*Intracavitary delivery*. Intraperitoneal for ovarian and other intraperitoneal cancers; intrathecal for CNS disease; intravesical for bladder cancer (where BCG, technically an attenuated bacterium, has been the standard for decades). The cavities provide a confined space for the virus to act with reduced systemic clearance.

*Loco-regional delivery*. Hepatic arterial infusion for liver tumors; isolated limb perfusion for limb sarcomas; intrathecal for CNS disease.

*Combined with carrier cells*. The virus is loaded into carrier cells (often mesenchymal stem cells or T cells) that home to the tumor and deliver the virus locally. This approach is in early clinical development.

The delivery challenges are one of the major limitations of oncolytic virotherapy. Solutions are being developed but remain imperfect.

---

## Combining oncolytic viruses with other therapies

The most promising direction in oncolytic virotherapy is combination with other anti-cancer modalities. The biological rationale is strong:

*Oncolytic virus + immune checkpoint inhibitor*. The virus releases tumor antigens, primes immune responses, and modulates the tumor microenvironment. Checkpoint inhibitors prevent shutdown of the resulting immune responses. The combination should be synergistic.

The clinical experience has been mixed:
- *T-VEC + ipilimumab* in melanoma. Improved response rates over ipilimumab alone.
- *T-VEC + pembrolizumab* in melanoma. The MASTERKEY-265 phase 3 trial did not show benefit over pembrolizumab alone. Disappointing but informative.

The mixed results suggest that the synergy is real but not consistent across all contexts. Optimizing the combination (timing, dosing, virus selection, patient selection) is an active research area.

*Oncolytic virus + chemotherapy*. The virus and chemotherapy may have complementary mechanisms (virus targets cancer cells through replication-dependent killing; chemotherapy targets through DNA damage and other mechanisms). Various combinations in clinical trials.

*Oncolytic virus + targeted therapy*. Specific combinations are being explored where the biology suggests synergy.

*Oncolytic virus + radiation*. Radiation may enhance viral replication in cells (through DNA damage response effects) and may produce immunogenic cell death that complements the viral immune effects. Combinations in clinical trials.

*Oncolytic virus + CAR-T or other cellular therapy*. The virus may modulate the tumor microenvironment to make cellular therapy more effective. Preclinical work suggests potential synergy; clinical trials are in development.

*Oncolytic virus engineered with immune therapy genes*. The virus itself can be engineered to deliver immune therapies. T-VEC's GM-CSF is an example. Newer oncolytic viruses are being engineered with:
- *Cytokines* (IL-12, IL-15, IL-18, IFN, others).
- *Checkpoint inhibitor genes* (anti-PD-1, anti-PD-L1 antibodies expressed by the virus).
- *Bispecific T cell engagers* (BiTEs delivered by the virus).
- *Costimulatory molecules* (CD40 ligand, GITRL, 4-1BBL).
- *Tumor antigens* (vaccine-like effect from viral antigen expression).

The combination approach addresses both the limitations of oncolytic viruses (modest single-agent activity) and the limitations of other modalities (cold tumors that don't respond to checkpoint inhibitors). The future of the field likely lies in well-designed combinations.

---

## Specific cancer applications

Oncolytic virotherapy is being tested in many cancer types. Some specific areas of active development:

*Melanoma*. T-VEC is FDA-approved. Many other oncolytic virus trials, often in combination with checkpoint inhibitors.

*Glioblastoma*. A particularly active area because glioblastoma is universally fatal and accessible to local viral injection during neurosurgery. Multiple oncolytic viruses (PVS-RIPO, DNX-2401, others) in clinical trials. Some encouraging early results but no approvals yet.

*Hepatocellular carcinoma*. The liver is accessible to local viral injection and can be targeted by hepatic arterial delivery. Pexa-Vec was tested extensively; phase 3 trial was negative. Other oncolytic viruses in development.

*Ovarian cancer*. Intraperitoneal delivery is feasible. Several oncolytic viruses in clinical trials.

*Bladder cancer*. Intravesical delivery is straightforward. Oncolytic viruses being tested as alternatives or additions to BCG.

*Head and neck cancer*. Intratumoral injection of accessible lesions. Multiple trials.

*Pancreatic cancer*. A particularly challenging cancer with few effective treatments. Some oncolytic viruses (RP1, others) showing early promise in trials.

*Lung cancer*. Bronchoscopic and CT-guided injection approaches. Various trials.

*Sarcoma*. Local injection of accessible lesions.

*Pediatric cancers*. Various trials.

The pattern is that oncolytic viruses are most useful for accessible tumors and for cancers where conventional approaches have limited success. The integration with immune therapy is increasingly the standard approach.

---

## Safety considerations

Oncolytic viruses are biological agents that replicate in patients. Safety considerations include:

*Vector shedding*. The replicating virus may be shed in body fluids (saliva, urine, etc.). Patients are typically told to avoid contact with immunocompromised individuals, pregnant women, and infants for some period after treatment.

*Immune compromise risk*. Patients on immunosuppression may be at higher risk of disseminated infection from oncolytic virus.

*Pre-existing immunity*. Many patients have antibodies against common viruses (HSV, adenovirus, others). The pre-existing immunity rapidly neutralizes the virus in circulation but does not prevent intratumoral replication. The implication is that intratumoral injection works better than IV delivery for these viruses.

*Cross-species considerations*. Some oncolytic viruses are engineered from animal viruses (e.g., Newcastle disease virus from chickens; reovirus). The cross-species use has theoretical concerns about pathogenicity changes but has been largely safe in clinical experience.

*Off-target tissue infection*. Despite engineering for cancer selectivity, viruses may infect normal tissues at low levels. Most current oncolytic viruses have acceptable safety profiles, but vigilance is needed.

*Tumor lysis syndrome*. Massive cancer cell death can release intracellular contents (potassium, phosphate, uric acid, nucleic acids) that overwhelm renal clearance. Less common with oncolytic viruses than with highly cytotoxic chemotherapy but possible.

*Cytokine release syndrome*. Less common than with CAR-T but possible. Managed similarly.

The safety experience with FDA-approved T-VEC has been generally favorable. Newer oncolytic viruses must demonstrate similar safety to gain approval.

---

## The future of oncolytic virotherapy

The field has been slow to produce major clinical advances despite decades of research, but several trends suggest progress is accelerating:

*Better viral engineering*. Modern oncolytic viruses are engineered with multiple modifications — cancer selectivity, immune evasion (where useful), expression of therapeutic payloads, controlled replication. The engineering toolkit continues to expand.

*Combination strategies*. The recognition that oncolytic viruses work best in combination has shifted the field. The optimization of combinations is the major direction.

*Local delivery improvements*. Better intratumoral injection technologies, image-guided delivery, intracavitary approaches.

*Systemic delivery innovations*. Carrier cells, encapsulation, shielding from pre-existing immunity, alternative viruses with less pre-existing immunity.

*Imaging-guided treatment*. Visualizing viral biodistribution and replication using engineered reporter genes (NIS gene, fluorescent reporters).

*Personalized approaches*. Choosing the right virus for the right patient based on tumor characteristics and immune profile.

*Off-the-shelf cellular delivery*. Engineered cells (mesenchymal stem cells, T cells, NK cells) that home to tumors and release oncolytic virus locally.

*Self-amplifying RNA*. Some emerging approaches use self-amplifying RNA delivered by lipid nanoparticles, providing some of the benefits of viruses without the immune neutralization issues.

The next decade may finally bring the broader clinical success that the field has long anticipated. The combination with checkpoint inhibitors has been the most important conceptual advance; engineering and delivery innovations may be the most important technical advances.

---

## What this chapter gives you

Oncolytic virotherapy uses viruses that selectively replicate in cancer cells, lysing them and stimulating immune responses against released tumor antigens. The selectivity comes from natural tropism, engineered deletions of genes needed in normal cells, tumor-specific promoters, and defective antiviral responses in cancer cells.

Talimogene laherparepvec (T-VEC, Imlygic) was the first FDA-approved oncolytic virus (2015) for advanced melanoma. It's an engineered HSV-1 with ICP34.5 deletion (for cancer selectivity), ICP47 deletion (for immune recognition), and GM-CSF insertion (for immune stimulation). Intratumoral injection produces local responses and some systemic effects through immune mechanisms.

Other oncolytic virus platforms in clinical development include adenovirus, vesicular stomatitis virus, Newcastle disease virus, measles virus, vaccinia, reovirus, coxsackievirus, parvovirus, polio virus (PVS-RIPO for glioblastoma), and others. Each platform has specific advantages and limitations.

Delivery is dominated by intratumoral injection, with intracavitary and loco-regional delivery for specific cancers. Systemic IV delivery is challenged by pre-existing immunity and clearance. New delivery approaches (carrier cells, shielding) are being explored.

Combinations with other therapies — particularly immune checkpoint inhibitors — are the most promising direction. The biology supports synergy (oncolytic virus releases antigens, primes immunity; checkpoint inhibitor sustains responses), though clinical results have been mixed (T-VEC + ipilimumab works; T-VEC + pembrolizumab in MASTERKEY-265 did not show benefit).

Specific cancer applications are being explored across cancer types, with melanoma, glioblastoma, hepatocellular carcinoma, ovarian cancer, head and neck cancer, and others as particular areas of activity.

Safety considerations include vector shedding, immune compromise risk, pre-existing immunity, cross-species considerations, off-target infection, and rare cases of tumor lysis or cytokine release syndromes. The safety experience with T-VEC has been favorable.

The future of oncolytic virotherapy lies in better viral engineering, combination strategies, improved delivery, imaging-guided treatment, personalized approaches, off-the-shelf cellular delivery, and emerging technologies like self-amplifying RNA.

This concludes Chapter 26 and the systemic therapy modalities. Chapter 27 turns to specific cancer types and their integrated management, applying the principles covered throughout this section to specific clinical contexts.

---

## LLM exercises

1. Ask your LLM to walk through the engineering of T-VEC from wild-type HSV-1 to the approved oncolytic. What specific genetic modifications were made (ICP34.5 deletion, ICP47 deletion, GM-CSF insertion), what does each modification achieve, and how was the final product validated clinically? Identify what this engineering pattern represents for the broader oncolytic virus field.

2. Have your LLM compare the MASTERKEY-265 (T-VEC + pembrolizumab in melanoma) and KEYNOTE-006 (pembrolizumab alone in melanoma) trial designs and outcomes. What did MASTERKEY-265 not show, and what does this tell us about oncolytic virus + checkpoint inhibitor combinations? Identify the implications for future trial design.

3. Use your LLM to construct a clinical scenario where you would consider oncolytic virotherapy as the primary or adjunctive treatment. What are the patient and tumor characteristics that favor oncolytic virus use, what would be the expected response rate, and what are the limitations to discuss with the patient?

4. Ask your LLM to compare the advantages and disadvantages of different oncolytic virus platforms (HSV, adenovirus, vaccinia, reovirus, measles, others). For each: the cargo capacity, the cancer types most relevant, the delivery considerations, and the manufacturing complexity. Identify which platform you would choose for a hypothetical oncolytic virotherapy for ovarian cancer.

5. Have your LLM survey the strategies for overcoming pre-existing immunity to oncolytic viruses. What approaches are being explored (alternative viruses, carrier cells, immune evasion engineering, polymer coating, shielding), and what is the level of evidence for each? Identify the most promising direction for systemic delivery of oncolytic viruses.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Robert Martuza** engineered the first oncolytic herpes simplex virus in 1991 — modifying the virus to replicate only in tumor cells. The work led directly to talimogene laherparepvec (T-VEC), the first FDA-approved oncolytic virus.

**Run this:**

```
Who is Robert Martuza, and how does his work on oncolytic herpesviruses connect to the virotherapy we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Robert L. Martuza"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Martuza's modifications to HSV restrict viral replication to dividing tumor cells.
- Ask it to compare oncolytic virus therapy with checkpoint inhibitors — when do clinicians combine them, and why?

What changes? What gets better? What gets worse?
