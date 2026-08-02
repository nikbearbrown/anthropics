# Chapter 43 — Cancer Immunotherapy in Practice: Checkpoint Inhibitors


## TL;DR

- The most important drug class of the past fifteen years works by removing brakes, not by pressing accelerators.
- The chapter moves through The checkpoint inhibitor era in brief, Patient selection: biomarkers and predictive features, When and how to use checkpoint inhibitors, Response patterns and assessment, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The most important drug class of the past fifteen years works by removing brakes, not by pressing accelerators.

Hold the framing. For most of cancer therapy's history, the strategy has been additive — give the patient something that does something to the cancer. Cytotoxic chemotherapy damages cancer cells. Targeted therapy blocks oncogenic signaling. Radiation breaks DNA. Each modality works by *doing* something.

Immune checkpoint inhibitors work differently. They don't kill cancer cells. They don't block any oncogene. They remove the molecular brakes that prevent the patient's own immune system from killing cancer cells. The therapeutic effect comes from the immune system, awakened from its tolerance. The drug just removes the suppression that was keeping the immune cells from doing their job.

This conceptual difference matters for understanding the practice of immunotherapy. The dose-response is different from chemotherapy. The toxicity is different (autoimmune-like rather than cytotoxic). The response patterns are different (pseudoprogression, delayed responses, durable remissions). The patient selection criteria are different. The management requires different expertise.

This chapter — the first of two on cancer immunotherapy in practice — covers the clinical implementation of immune checkpoint inhibitors. The biology was covered in Chapter 16. This chapter focuses on the practical aspects of using these drugs: patient selection, biomarkers, sequencing, response assessment, and the management of immune-related adverse events. The next — 25B — covers cellular therapies (CAR-T, TIL, TCR-T), cancer vaccines, cytokines, and other immune-based therapies in clinical practice.

Hold the question: *given that immune checkpoint inhibitors work by activating immunity, how do we identify the right patients, deliver the treatment, and manage the consequences?*

---

## The checkpoint inhibitor era in brief

Cancer immunotherapy had a long history of disappointment before the checkpoint inhibitor era. IL-2 produced durable responses in a minority of melanoma and renal cell carcinoma patients but at brutal toxicity. Interferons had modest activity. Cancer vaccines mostly failed. Adoptive cell therapy was limited to research settings. By the late 1990s, immune therapy seemed to be a perpetually almost-working approach.

The reframing came from understanding *immune checkpoints* — the molecular brakes that normally prevent autoimmunity. James Allison's work on CTLA-4 (started in the late 1980s, with clinical translation through the 1990s and 2000s) and Tasuku Honjo's on PD-1 (1992 discovery, with translation following) identified specific molecules that tumors exploit to suppress anti-tumor T cells. Blocking these checkpoints with monoclonal antibodies could release the brakes.

The clinical proof came with *ipilimumab* (Yervoy, anti-CTLA-4). The pivotal trial (MDX010-20) in 2010 showed improved overall survival in metastatic melanoma — a disease previously uniformly fatal within months of metastatic diagnosis. FDA approval came in 2011. Response rates were modest (10-15%), but a substantial fraction of responders had durable, multi-year responses. The "tail" of the survival curve suggested that some patients were being effectively cured.

*Anti-PD-1 antibodies* followed. Nivolumab and pembrolizumab were approved in 2014. The response rates in melanoma were higher (40-50%) than ipilimumab, with similar durable response profiles. The drugs were rapidly extended to other cancers — non-small-cell lung cancer (2015), renal cell carcinoma (2015), Hodgkin lymphoma (2016), urothelial carcinoma (2016), head and neck squamous cell carcinoma (2016), Merkel cell carcinoma (2016), and many others.

*Anti-PD-L1 antibodies* (atezolizumab, durvalumab, avelumab) followed similar trajectories.

*Anti-LAG-3 antibody* (relatlimab) was approved in 2022 in combination with nivolumab for melanoma — the first new checkpoint inhibitor target.

By 2026, checkpoint inhibitors are approved for more than 20 cancer types and have multiple indications across early-stage, locally advanced, and metastatic settings. They are among the most prescribed cancer drugs.

The clinical impact has been substantial. In melanoma, the five-year survival rate for metastatic disease has risen from under 10% (pre-immunotherapy) to over 50% (with combination ipilimumab/nivolumab). Similar dramatic improvements have occurred in some other cancers. The immune therapy era has reshaped cancer outcomes in ways that targeted therapy alone could not.

---

## Patient selection: biomarkers and predictive features

Not all cancers respond to checkpoint inhibitors. Identifying who will respond — and who won't — is central to good practice.

The major predictive biomarkers:

*PD-L1 expression*. The most commonly used biomarker. Measured by immunohistochemistry on tumor cells, immune cells, or both. The clinical thresholds and reporting vary:
- *Tumor Proportion Score (TPS)* in lung cancer: the percentage of tumor cells expressing PD-L1. Cutoffs of ≥1%, ≥50%, etc.
- *Combined Positive Score (CPS)*: in head and neck cancer, gastric cancer, etc. Includes both tumor and immune cells.
- *IC score*: in urothelial cancer. The percentage of tumor area occupied by PD-L1-positive immune cells.

The performance of PD-L1 as a biomarker is imperfect. Some PD-L1-positive tumors don't respond; some PD-L1-negative tumors respond well. The biology is more complex than a simple expression cutoff.

*Microsatellite instability (MSI) status*. MSI-high tumors (typically from Lynch syndrome or sporadic MLH1 hypermethylation) have very high mutation burden and respond extremely well to anti-PD-1 therapy. Response rates of 30-50% across MSI-H cancers, regardless of tissue of origin. Pembrolizumab has tumor-agnostic FDA approval for MSI-H tumors (2017) — the first tumor-agnostic approval.

*Tumor mutational burden (TMB)*. Higher TMB (more mutations, more potential neoantigens) generally predicts better immunotherapy response. Pembrolizumab is approved for TMB-high (≥10 mut/Mb) tumors regardless of tissue type.

*Mismatch repair deficiency (dMMR)*. Detected by IHC for MLH1, MSH2, MSH6, PMS2. Equivalent to MSI-H by a different testing approach. Either test is acceptable for clinical decision-making.

*EBV positivity*. EBV-positive gastric cancers and EBV-positive lymphomas often respond to immunotherapy.

*Specific tumor types*. Some cancers (Hodgkin lymphoma, Merkel cell carcinoma, cutaneous squamous cell carcinoma) respond very well to checkpoint inhibitors regardless of other biomarkers.

*Specific molecular features that predict non-response*. EGFR-mutated and ALK-rearranged lung cancers respond poorly to immunotherapy (probably due to low TMB and other immunological features). Microsatellite-stable (non-MSI-H) colorectal cancer responds poorly to single-agent checkpoint inhibitors. KRAS G12C-mutant lung cancer responds variably.

The biomarker landscape continues to evolve. Composite biomarkers integrating PD-L1, TMB, MSI, gene expression signatures, and clinical features are being developed. Multi-omic approaches may eventually provide more accurate prediction.

---

## When and how to use checkpoint inhibitors

The clinical applications of checkpoint inhibitors span multiple settings:

*First-line metastatic disease*. Many cancers use checkpoint inhibitors first-line, either alone or in combination:
- *NSCLC*. Pembrolizumab alone for PD-L1 ≥50%; pembrolizumab + chemotherapy for lower PD-L1; ipilimumab + nivolumab combinations.
- *Melanoma*. Anti-PD-1 alone for some; ipilimumab + nivolumab for others.
- *Renal cell carcinoma*. Pembrolizumab + axitinib, nivolumab + cabozantinib, or ipilimumab + nivolumab.
- *Hepatocellular carcinoma*. Atezolizumab + bevacizumab, durvalumab + tremelimumab.
- *Gastric/GEJ cancer*. Nivolumab + chemotherapy for PD-L1-positive disease.
- *Head and neck squamous cell carcinoma*. Pembrolizumab alone or with chemotherapy depending on PD-L1.
- *Urothelial carcinoma*. Pembrolizumab + enfortumab vedotin (a recent combination).
- *Triple-negative breast cancer*. Pembrolizumab + chemotherapy for PD-L1-positive disease.

*Adjuvant therapy*. Increasingly approved as adjuvant therapy after curative-intent treatment:
- *Melanoma*. Pembrolizumab, nivolumab, or ipilimumab + nivolumab as adjuvant for stage III-IV resected disease.
- *NSCLC*. Atezolizumab as adjuvant for resected stage II-IIIA PD-L1 ≥1%; pembrolizumab as adjuvant for resected stage IB-IIIA.
- *Renal cell carcinoma*. Pembrolizumab as adjuvant for high-risk resected disease.
- *Urothelial carcinoma*. Nivolumab as adjuvant for high-risk resected disease.
- *Triple-negative breast cancer*. Pembrolizumab as adjuvant in combination with chemotherapy.

*Neoadjuvant therapy*. Before surgery to potentially improve response and identify responders:
- *Melanoma*. Neoadjuvant checkpoint inhibitors increasingly used.
- *Lung cancer*. Nivolumab + chemotherapy approved for resectable NSCLC.
- *Triple-negative breast cancer*. Pembrolizumab + chemotherapy as neoadjuvant.

*Consolidation therapy*. After definitive chemoradiation:
- *NSCLC*. Durvalumab consolidation after concurrent chemoradiation for stage III disease.
- *Esophageal cancer*. Nivolumab as adjuvant after concurrent chemoradiation.

*Maintenance therapy*. Continued treatment after initial response.

The expansion of indications reflects the breadth of checkpoint inhibitor activity across cancer types and disease stages.

---

## Response patterns and assessment

Immune checkpoint inhibitor responses can differ from chemotherapy responses in ways that affect assessment:

*Pseudoprogression*. Initial increase in tumor size before subsequent regression. Caused by immune cell infiltration of the tumor, which transiently increases the radiographic size. Eventually the immune attack causes tumor regression. Pseudoprogression is uncommon (probably 5-10% of patients) but real.

*Hyperprogression*. Accelerated tumor growth after starting immunotherapy. Reported in some studies (especially elderly patients or specific molecular subtypes), though the exact frequency and biological basis remain debated.

*Delayed response*. Some patients show stable disease for months before tumors begin regressing. The initial assessment underestimates the eventual response.

*Durable response*. Patients who respond to immunotherapy often have remarkably durable responses — sometimes lasting years after stopping treatment. This is unprecedented in metastatic disease and represents one of the most exciting features of immunotherapy.

*Mixed response*. Some lesions respond while others progress. Common in metastatic disease.

The standard RECIST criteria can mislead in these settings. Modified criteria have been developed:

*iRECIST (immune-related RECIST)*. Allows for unconfirmed progression. If initial scan shows progression, confirmation is needed on subsequent imaging 4-8 weeks later. If the apparent progression is pseudoprogression, the subsequent scan shows regression. Treatment can be continued.

*imRECIST (immune-modified RECIST)*. Similar concept with some technical differences.

*irRC (immune-related response criteria)*. An earlier framework.

The practical implication is that progression on imaging shortly after initiating immunotherapy doesn't necessarily mean treatment failure. Clinical correlation, repeat imaging, and consideration of pseudoprogression are needed before discontinuing therapy.

*Treatment duration*. How long to continue checkpoint inhibitors in responders is one of the open clinical questions. Standard durations are 1-2 years in most settings. Some patients stop treatment and remain in remission for years (suggesting durable immune memory). Others may benefit from continued therapy. The optimal duration is being studied.

---

## Combination immunotherapy

Single-agent checkpoint inhibitors are effective in some cancers but limited in others. Combinations are increasingly the standard:

*Anti-CTLA-4 + anti-PD-1*. The classic combination. Ipilimumab + nivolumab in melanoma produces response rates around 60% with higher rates of durable response. Approved in melanoma, renal cell carcinoma, MSI-H colorectal cancer, hepatocellular carcinoma, malignant pleural mesothelioma, and others. Toxicity is substantially higher than either drug alone (about 55% grade 3-4 immune-related adverse events).

*Anti-PD-1 + chemotherapy*. Multiple approvals. The mechanism: chemotherapy releases tumor antigens through cell death, modulates the immune microenvironment, and may sensitize tumors to immune attack. Pembrolizumab + chemotherapy in NSCLC, head and neck cancer, gastric cancer, breast cancer, and others.

*Anti-PD-1/L1 + anti-angiogenic therapy*. Multiple approvals. Mechanism: anti-angiogenic therapy normalizes the immunosuppressive tumor microenvironment. Discussed in Chapter 12B.

*Anti-PD-1 + targeted therapy*. Mixed results. Some combinations are synergistic (BRAF/MEK inhibitors + anti-PD-1 in melanoma, with some restrictions). Others have shown unexpected toxicity (some EGFR inhibitor combinations).

*Anti-LAG-3 + anti-PD-1*. Relatlimab + nivolumab in melanoma (RELATIVITY-047 trial) improved PFS over nivolumab alone, with FDA approval in 2022. The first non-CTLA-4 immune checkpoint combination approved.

*Anti-TIGIT + anti-PD-L1*. Has shown mixed results in trials. Tiragolumab in some combinations has shown benefit; others haven't.

*Newer checkpoint targets*. Anti-TIM-3, anti-VISTA, anti-BTLA, and others in clinical development. The combination space continues to expand.

The combination logic — hitting multiple immunosuppressive mechanisms simultaneously — addresses the redundancy in tumor immune evasion. The cost is increased toxicity. Patient selection for combination versus monotherapy is one of the key clinical decisions.

---

## Immune-related adverse events

Immune-related adverse events (irAEs) are the inherent cost of releasing immune brakes. The same mechanisms that allow anti-tumor immunity can produce autoimmune-like reactions against normal tissues.

The irAEs span essentially every organ system:

*Skin*. Rash, pruritus, vitiligo. The most common irAE category. Usually mild and manageable with topical steroids.

*GI*. Colitis, hepatitis. Diarrhea is common (and may indicate colitis); severe colitis can cause perforation and death if not promptly recognized and treated. Hepatitis presents with elevated transaminases.

*Endocrine*. Thyroiditis (hyperthyroidism → hypothyroidism, often), hypophysitis (hypopituitarism), adrenal insufficiency, type 1 diabetes. Endocrine irAEs often produce permanent organ damage requiring lifelong hormone replacement.

*Pulmonary*. Pneumonitis. Range from asymptomatic radiographic findings to fatal respiratory failure.

*Cardiac*. Myocarditis. Rare (about 1% of patients) but often fatal when severe. Particularly seen with anti-CTLA-4 + anti-PD-1 combinations.

*Renal*. Nephritis, acute kidney injury.

*Neurologic*. Encephalitis, myasthenia gravis-like syndromes, Guillain-Barré-like syndromes, neuropathy. Rare but serious.

*Musculoskeletal*. Arthritis, myositis. The myositis can cause severe muscle weakness and respiratory compromise.

*Hematologic*. Cytopenias (rare).

*Ocular*. Uveitis, conjunctivitis.

*Other*. Pancreatitis, sarcoidosis-like reactions, various other rare presentations.

The frequency depends on the drug and combination:
- *Anti-PD-1/PD-L1 monotherapy*. About 20% of patients have grade 3-4 irAEs.
- *Anti-CTLA-4 monotherapy*. About 30-40%.
- *Anti-CTLA-4 + anti-PD-1*. About 55-60%.

The timing varies. Some irAEs occur early (days to weeks); some occur late (months after starting, or even after stopping treatment). The variability complicates monitoring.

The management framework:

*Grade 1-2 irAEs*. Often managed with continued therapy and symptomatic treatment. Topical steroids for skin. Antidiarrheals for mild diarrhea (with caution).

*Grade 3-4 irAEs*. Generally require holding immunotherapy and starting systemic corticosteroids (typically prednisone 1-2 mg/kg/day or equivalent). The steroid course is gradually tapered over weeks to months.

*Steroid-refractory irAEs*. Additional immunosuppression is needed. Options include infliximab (anti-TNF), mycophenolate, tacrolimus, vedolizumab (gut-selective anti-integrin), and others, depending on the affected organ. Multidisciplinary management involving the relevant organ specialist is essential.

*Permanent discontinuation*. Generally required for severe irAEs, especially involving heart, brain, or causing significant permanent damage.

*Rechallenge*. After resolution of grade 2-3 irAEs, immunotherapy may sometimes be resumed at lower intensity. Decisions are individualized.

The expertise required to manage irAEs is real. Many academic centers have specialized immune-related toxicity clinics. The expertise is less available in community settings, creating quality concerns.

Importantly, irAEs are *mechanistically linked to anti-tumor response*. Patients who develop irAEs often have better tumor responses. The autoimmunity and the anti-tumor activity reflect the same underlying mechanism — overcoming peripheral tolerance.

---

## Practical considerations

Several practical aspects of checkpoint inhibitor use:

*Dosing schedules*. Most checkpoint inhibitors are given every 3 weeks (some every 2 weeks, some every 4 weeks, some every 6 weeks). Some products have approved alternate-week dosing for patient convenience.

*Infusion characteristics*. Generally 30-60 minute infusions. Hypersensitivity reactions are uncommon. No premedication usually required.

*Bridging with steroids*. Patients on chronic high-dose steroids may have reduced response to checkpoint inhibitors (because steroids suppress the immune system that the drugs are trying to activate). Discontinuing steroids before initiating immunotherapy is preferred when possible.

*Vaccines during immunotherapy*. Live vaccines are generally avoided. Inactivated vaccines (influenza, COVID-19) are usually given.

*Pregnancy*. Checkpoint inhibitors should generally be avoided in pregnancy due to potential effects on fetal development and immune tolerance.

*Patient counseling*. Patients should be educated about irAE symptoms and instructed to report them promptly. Many patients delay reporting symptoms, sometimes with severe consequences. Symptom awareness materials and contact information for prompt evaluation are part of standard care.

*Special populations*. Older patients tolerate immunotherapy generally well. Patients with prior autoimmune disease are at increased risk of irAEs but can sometimes be treated with careful monitoring. Patients with HIV (well-controlled) and prior transplants are treated cautiously.

---

## Cost and access

Checkpoint inhibitors are expensive. Typical annual costs in the US range from $150,000 to $250,000+. The high costs create access barriers:

*Insurance variability*. Coverage varies by insurance and indication. Prior authorization is often required.

*International access*. Many low- and middle-income countries have limited access to checkpoint inhibitors. The drugs are largely unavailable in much of sub-Saharan Africa, South Asia, and parts of Latin America.

*Biosimilars*. As patents begin to expire, biosimilar versions of checkpoint inhibitors are being developed. Increased competition may eventually reduce costs.

*Cost-effectiveness debates*. The high costs combined with the substantial benefits create complex cost-effectiveness considerations. Different countries have made different decisions about coverage.

The economic dimensions of immunotherapy continue to be a major topic in oncology policy.

---

## What this chapter gives you

Immune checkpoint inhibitors have transformed cancer therapy across more than 20 cancer types. Anti-CTLA-4 (ipilimumab), anti-PD-1 (nivolumab, pembrolizumab, cemiplimab, dostarlimab, others), anti-PD-L1 (atezolizumab, durvalumab, avelumab), and anti-LAG-3 (relatlimab) provide options across many indications.

Patient selection uses biomarkers including PD-L1 expression, microsatellite instability/dMMR status, and tumor mutational burden. The biomarkers are imperfect; some PD-L1-negative tumors respond well and some PD-L1-high tumors don't respond. Better biomarker development continues.

Clinical applications span first-line metastatic disease, adjuvant therapy, neoadjuvant therapy, consolidation, and maintenance. Indications continue to expand.

Response assessment uses modified criteria (iRECIST, imRECIST) that allow for pseudoprogression and delayed responses. The unique features of immunotherapy responses (pseudoprogression, durable remissions, mixed responses) require careful interpretation.

Combination immunotherapy includes anti-CTLA-4 + anti-PD-1 (more active but more toxic), anti-PD-1 + chemotherapy, anti-PD-1 + anti-angiogenic therapy, anti-PD-1 + targeted therapy, and anti-LAG-3 + anti-PD-1. Newer combinations with TIGIT, TIM-3, and other targets are in development.

Immune-related adverse events span essentially every organ system. Management involves a grading system, with grade 3-4 events generally requiring treatment hold and systemic corticosteroids. Severe events may require permanent discontinuation. The expertise to manage irAEs is increasingly important.

Practical considerations include dosing schedules, infusion characteristics, patient counseling about symptom reporting, and special populations.

Cost and access remain significant issues, with substantial barriers in lower-resource settings and ongoing cost-effectiveness debates.

Chapter 25B turns to other immunotherapy approaches in clinical practice — CAR-T cells, TIL therapy, TCR-T, cancer vaccines, and cytokines. These complement checkpoint inhibitors with different mechanisms and applications.

---

## LLM exercises

1. Ask your LLM to walk through the pivotal trial of ipilimumab in metastatic melanoma (MDX010-20) that led to FDA approval in 2011. What was the trial design, what were the outcomes, and what did the survival curve suggest about the unique features of immunotherapy? Identify what this trial established as the foundation of modern immunotherapy.

2. Have your LLM compare the major biomarkers for checkpoint inhibitor response — PD-L1 expression, microsatellite instability, tumor mutational burden, and gene expression signatures. For each: how is it measured, what cancers is it relevant in, and what is its predictive accuracy? Identify the biomarker most likely to be displaced or improved upon.

3. Use your LLM to explain pseudoprogression with immune checkpoint inhibitors. What is the biological mechanism, how frequent is it, and how do iRECIST criteria account for it? Construct a clinical scenario showing how managing apparent progression on imaging requires considering pseudoprogression.

4. Ask your LLM to walk through the management of severe immune-mediated colitis. What are the typical symptoms, what is the workup, what is the role of corticosteroids and infliximab, and what is the long-term management plan? Identify the key decision points in escalating treatment.

5. Have your LLM analyze the cost-effectiveness debate around checkpoint inhibitors. What are the typical costs, what are the survival benefits in major indications, and how do cost per QALY analyses come out? Compare with regulatory and reimbursement decisions in different countries.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Tasuku Honjo** discovered PD-1 in 1992 — a T-cell inhibitory receptor whose blockade lets the immune system attack tumors. The work won him the 2018 Nobel Prize with James Allison and produced the most-used immunotherapy class in modern oncology.

![Tasuku Honjo](../images/tasuku-honjo-112.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Tasuku Honjo, and how does his discovery of PD-1 connect to the checkpoint immunotherapy we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Tasuku Honjo"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through what PD-1 does in healthy T cells — and why tumors exploit it.
- Ask it to compare the clinical responses to anti-CTLA-4 versus anti-PD-1 therapies in melanoma.

What changes? What gets better? What gets worse?
