# Chapter 10 — Cancer Etiology: Viral and Bacterial Carcinogens

A 34-year-old woman has an abnormal Pap smear. HPV testing detects type 16. A colposcopy finds a high-grade intraepithelial lesion — abnormal cells confined to the surface, not yet invasive. The lesion is removed. She asks her doctor: "Did I catch cancer from someone?"

The honest answer threads a needle. She did not catch cancer. Cancer is not contagious. What she caught — years earlier, probably without symptoms — was a virus. In most people the immune system clears that virus within a year or two. In her, it persisted. And persistence is the whole story. For more than a decade, two viral proteins quietly disabled her cells' most important safety controls, and a clone of cells inched along the road toward malignancy. The screening caught it before the road ended.

The puzzle is worth sitting with: a virus is a small package of genes, not a tumor. How does that package turn a normal epithelial cell into a precancerous one? And why does this take a decade, leaving a long window in which the process can be stopped?

---

## The fraction we can prevent

About one in eight cancers worldwide — roughly 2.2 million new cases per year — is attributable to an infection. This is both a striking and an actionable number. You cannot edit a genetic predisposition out of existence or easily scrub a chemical carcinogen from the environment, but you can vaccinate against a virus, eradicate a bacterium with a week of antibiotics, or cure a chronic viral infection with antivirals that achieve 95% clearance rates.

![Single proportional bar split at zero baseline: about 13% of cancers worldwide are infection-attributable versus 87% from other causes — roughly one in eight, all preventable.](images/10-cancer-etiology-viral-and-bacterial-carcinogens-fig-04.png)
*Figure 10.4 — Infection-attributable cancer fraction*

The International Agency for Research on Cancer classifies seven viruses and one bacterium as Group 1 carcinogens — definitively carcinogenic to humans: HPV, hepatitis B virus (HBV), hepatitis C virus (HCV), Epstein-Barr virus (EBV), Kaposi sarcoma–associated herpesvirus (KSHV), HTLV-1, Merkel cell polyomavirus, and *Helicobacter pylori*. Each causes a specific spectrum of cancers through a distinct mechanism, but they share one feature: **persistent infection**. Infections that resolve do not cause cancer. Infections that the immune system fails to clear, and that therefore persist for years, do.

---

## Four mechanisms, not one

The naive model of a viral carcinogen is a virus that encodes an oncogene — a cancer-driving protein. That model fits some agents perfectly and fails for others. Understanding why requires distinguishing four mechanisms, which are not mutually exclusive.

**Direct viral oncoproteins.** The most direct route: the virus encodes proteins that themselves disable tumor suppressors, drive proliferation, or block apoptosis. HPV's E6 and E7 are the canonical example and are treated in detail below. EBV encodes LMP1, a transmembrane protein that mimics constitutive signaling through the CD40 receptor — activating NF-κB and other proliferative pathways without any actual ligand. KSHV encodes a viral cyclin (which drives cell division without the normal regulatory constraints on cyclin expression) and a viral interleukin-6 homolog. These viruses bring their own oncogenic toolkit; they have evolved it over millions of years of co-evolution with their hosts.

**Insertional mutagenesis.** When a virus integrates its DNA into the host chromosome, the insertion site can activate a nearby oncogene by placing it under viral promoter control, or disrupt a tumor suppressor by inserting into its coding sequence. HBV integrates in most chronic infections; integration near *TERT* (telomerase reverse transcriptase) or cyclin genes is found in hepatocellular carcinoma. In HPV, integration into the host genome during disease progression often disrupts the viral *E2* gene that normally constrains E6 and E7 expression — a double bad luck in which integration both commits the viral DNA to the cell and releases the brake on the oncoproteins.

**Chronic inflammation.** A persistent infection drives a permanent immune response. Inflammatory cells generate reactive oxygen and nitrogen species that damage DNA continuously. The damaged tissue undergoes repeated cycles of injury and regeneration — elevated cell division means elevated replication, which means elevated opportunity for replication errors. Over decades, this background rate of mutagenesis is enough to accumulate the drivers needed for cancer. This is the dominant mechanism for HBV and HCV in liver cancer and for *H. pylori* in gastric cancer. No single viral oncogene is required; the immune response does the mutagenic work.

**Immunosuppression.** Some agents cause cancer not by acting on the cancer cell directly but by dismantling the immune surveillance that would otherwise eliminate early malignant cells. HIV is the central example: it depletes CD4+ T cells, allowing KSHV-driven Kaposi sarcoma and EBV-driven lymphomas to develop at frequencies essentially never seen in immunocompetent people. The carcinogen here is the immunosuppressive virus, not the viruses it unleashes.

![Conceptual map of four routes from a central node — direct viral oncoproteins, insertional mutagenesis, chronic inflammation, and immunosuppression — each branching to one cancer outcome.](images/10-cancer-etiology-viral-and-bacterial-carcinogens-fig-02.png)
*Figure 10.2 — Four mechanisms of microbial carcinogenesis*

<!-- → [DIAGRAM: four mechanisms of microbial carcinogenesis — direct oncoproteins / insertional mutagenesis / chronic inflammation / immunosuppression, each with a representative pathogen] -->

The latency between infection and cancer is long — typically 10 to 20 years for HPV and cervical cancer, 20 to 40 for HBV/HCV and liver cancer, 30 to 50 for *H. pylori* and gastric cancer. The long latency is both the price and the opportunity. Cancers appear a generation after exposure, which obscures the causal chain; but the window between infection and cancer is wide enough for multiple effective interventions.

---

## How HPV disables two checkpoints simultaneously

Human papillomaviruses are small DNA viruses that infect epithelial cells. Of roughly 200 types, persistent infection with high-risk types causes essentially all cervical cancers, most anal cancers, and a growing fraction of oropharyngeal cancers; HPV-16 and HPV-18 account for the majority of cervical cancers, but not all of them. The transforming work is done by two viral proteins.

**E6** recruits a cellular ubiquitin ligase — E6AP — and redirects it to target **p53** for proteasomal destruction. With p53 gone, damaged DNA no longer triggers cell-cycle arrest or apoptosis. The genome's guardian is eliminated, quietly, by a protein that contains no mutated DNA and leaves no sequence change behind.

**E7** binds the retinoblastoma protein **Rb** and disrupts the Rb–E2F complex. Normally, Rb sequesters the transcription factor E2F, preventing it from activating S-phase genes until cyclin D–CDK4/6 phosphorylates Rb and releases E2F as a controlled signal that the cell is ready to divide. E7 forces this release regardless of growth signals. The cell enters S phase whether it should or not.

Together, E6 and E7 do to a cell what mutations in *TP53* and *RB1* would do — but acutely, as a consequence of infection rather than through accumulated mutations. The cell loses both its checkpoint guardian and its gate-to-S-phase in a single infectious event. What takes years of somatic mutation in other cancers happens in one step here. And years of persistent E6/E7 expression give the damaged, checkpoint-free cell time to accumulate the further mutations that push it toward invasion.

The progression is gradual precisely because E6 and E7 create permissive conditions rather than executing transformation directly. A cell expressing these proteins does not immediately become cancerous; it becomes a cell in which damage is not repaired and normal growth controls are not enforced, and in which further mutations accumulate at an elevated rate. The cervical intraepithelial neoplasia grading system — CIN1, CIN2, CIN3, carcinoma in situ, invasive carcinoma — is a histological record of that accumulation. The Pap smear and colposcopy detect it during the long CIN phase, before invasion.

![Two-arm mechanism diagram: HPV E6 redirects a ubiquitin ligase to degrade p53 while E7 disrupts the Rb–E2F complex to release E2F and switch on S-phase genes, both converging on one checkpoint-free proliferating cell.](images/10-cancer-etiology-viral-and-bacterial-carcinogens-fig-01.png)
*Figure 10.1 — HPV E6 and E7 disable two checkpoints*

<!-- → [DIAGRAM: HPV E6 → p53 degradation (loss of damage response); HPV E7 → Rb–E2F disruption (uncontrolled S-phase entry); together = two checkpoints down] -->

---

## *H. pylori* and why the "find the oncogene" model fails

Barry Marshall and Robin Warren proposed in the early 1980s that a spiral bacterium found in stomach biopsies — *Helicobacter pylori* — caused gastritis and ulcers and might be linked to gastric cancer. The medical establishment's resistance was fierce: everyone knew peptic ulcers were caused by stress and excess acid. Marshall famously drank a culture of the bacteria to demonstrate its pathogenicity, developed gastritis within days, and treated himself with antibiotics. The 2005 Nobel Prize was the eventual vindication.

The mechanism question for cancer is instructive. The first instinct is to search for a bacterial oncogene — something like E6 or E7. *H. pylori* does inject a protein, **CagA**, into gastric epithelial cells via a type IV secretion system, where it disrupts intracellular signaling. CagA-positive strains carry higher cancer risk than CagA-negative ones. But CagA is not a classical transforming oncoprotein. It does not degrade p53 or constitutively release E2F. And most people carry *H. pylori* for their entire lives without developing gastric cancer. The "find the oncogene" approach does not close.

The correct mechanism is chronic inflammation. *H. pylori* colonizes the gastric mucosa and persists indefinitely unless eradicated. The immune response to it is continuous: infiltrating neutrophils and macrophages generate reactive oxygen and nitrogen species, damaging the DNA of gastric epithelial cells. The repeated injury drives compensatory regeneration — elevated cell division — which multiplies opportunities for replication errors. Over 30 to 50 years, the stomach progresses through a stereotyped sequence: chronic active gastritis → atrophic gastritis → intestinal metaplasia → dysplasia → adenocarcinoma. The Correa cascade, as it is called, is the slow geological sedimentation of a mutagenic environment acting on a proliferating epithelium.

![Horizontal timeline over decades of inflammation: gastritis, atrophy, metaplasia, dysplasia, adenocarcinoma — a stereotyped progression driven by persistent injury with no single bacterial oncogene.](images/10-cancer-etiology-viral-and-bacterial-carcinogens-fig-03.png)
*Figure 10.3 — Chronic inflammation and the Correa cascade*

Because the driver is the *persistent infection*, removing it interrupts the chain. Eradication therapy — a proton-pump inhibitor plus two antibiotics for one to two weeks — clears the bacterium in 80 to 95% of patients. Long-term follow-up data show roughly a 35% reduction in gastric cancer incidence in eradicated versus non-eradicated patients, with the benefit largest in patients treated before precancerous changes have already established. Once atrophic gastritis or intestinal metaplasia is present, eradication still helps but the accumulated mutagenic damage is harder to undo.

The same logic that wrongly demanded an oncogene from *H. pylori* would have prevented the discovery of the intervention. Getting the mechanism right — inflammation, not direct transformation — led directly to antibiotics as cancer prevention.

---

## Prevention as mechanism-based intervention

The mechanistic clarity of infectious carcinogenesis makes it uniquely amenable to prevention. Each step in the causal chain from infection to cancer is a potential intervention point.

The **HPV vaccine** immunizes against the viral capsid protein L1, generating antibodies that block infection before it establishes. Gardasil 9, protecting against nine HPV types, prevents roughly 90% of cervical cancers. In populations with high vaccination coverage — several high-income countries — cervical cancer incidence is already falling sharply among vaccinated cohorts. This is not a 20-year projections; the signal is visible now.

The **hepatitis B vaccine** prevents HBV infection and has substantially reduced liver cancer incidence in countries where childhood vaccination was introduced in the 1980s and 1990s. A generation of children vaccinated against HBV is becoming a generation of adults with lower hepatocellular carcinoma rates.

**HCV** was transformed from a chronic, cancer-predisposing infection into a curable disease in 2014 with direct-acting antivirals. Cure rates above 95% are now routine. Curing HCV eliminates the ongoing inflammatory driver; the liver cancer risk falls substantially, though not to baseline in patients who already have cirrhosis.

*H. pylori* **eradication** is gastric cancer prevention — a fact that was controversial when Marshall and Warren first proposed the connection and is now the basis of population-level eradication programs in high-incidence countries.

The conceptual point deserves stating directly: infectious-disease prevention and cancer prevention are the same enterprise here. The HPV vaccine is an anti-cancer vaccine. The HBV vaccine is anti-cancer. HCV antivirals are anti-cancer treatment. Framing them as separate fields obscures the opportunity — and helps explain why cervical cancer mortality in sub-Saharan Africa is roughly ten times that in high-income countries, where vaccination, screening, and treatment are accessible.

---

## Necessary but not sufficient

No real cancer has a single cause, and infection is no exception to the multifactorial rule. Most people who carry *H. pylori* for life never develop gastric cancer. Over 90% of adults carry EBV; most never develop EBV-associated lymphoma or nasopharyngeal carcinoma. The majority of people who acquire HPV clear it without consequences.

Infection is typically **necessary but not sufficient**. Endemic Burkitt lymphoma requires EBV *plus* holoendemic malaria, which drives the sustained B-cell proliferation that amplifies the risk of EBV-associated transformation. Nasopharyngeal carcinoma involves EBV plus dietary and genetic cofactors specific to the populations where it is concentrated. Hepatocellular carcinoma in some regions involves HBV or HCV plus aflatoxin from contaminated grain, where the two exposures together exceed either alone — a multiplicative interaction, not additive.

The multifactorial reality does not weaken the causal claim for infection. It contextualizes it. Removing the infection removes a necessary contributor, even if not the only one, and the intervention data — vaccination, eradication, antivirals — demonstrate the reduction in cancer incidence that follows. The mechanism and the intervention both confirm the causal role.

---

## What would change this picture

The central claim is that specific persistent infections cause specific cancers through known mechanisms, and that interrupting the infection prevents the cancer. This is now intervention-level evidence, not just association. HPV vaccination is driving cervical cancer incidence toward elimination in high-coverage populations. HBV vaccination has produced measurable reductions in childhood liver cancer rates. *H. pylori* eradication lowers gastric cancer incidence in randomized follow-up.

The finding that would force revision: long-term, well-controlled vaccination or eradication programs, with high uptake and adequate follow-up, showing no reduction in the corresponding cancer relative to comparable control populations. If mature HPV-vaccinated cohorts showed cervical cancer rates indistinguishable from unvaccinated cohorts, or if *H. pylori* eradication trials showed no gastric-cancer benefit even in patients treated before precancerous change, the causal claim would require fundamental re-examination. A demonstration that the association was confounded — that some third factor drove both infection and cancer — would similarly force revision. Neither has happened.

---

## Still open

Why only a minority of persistently infected people develop cancer is not fully understood. Half the world carries *H. pylori*; over 90% of adults carry EBV; HPV infection is near-universal among sexually active adults. The host genetic factors, bacterial or viral strain differences, and environmental cofactors that determine progression in the minority and resolution in the majority are actively studied and incompletely mapped. The answer matters for targeting screening and eradication toward those most at risk.

There is no licensed EBV vaccine as of 2026, despite EBV's role in Burkitt lymphoma, Hodgkin lymphoma, nasopharyngeal carcinoma, and gastric cancer, and despite EBV's near-universal prevalence. An effective vaccine would have a large global cancer prevention impact; why this gap exists — technical, commercial, or regulatory — is itself a question worth asking.

The broader microbial community — the microbiome rather than named pathogens — may modulate cancer risk and therapy response in ways that the single-pathogen framework does not capture. How much of the currently unexplained variation in cancer incidence and treatment response is attributable to microbial communities rather than host genetics or named carcinogens is genuinely open.

---

## LLM Exercises

1. **(Four mechanisms)** List the four mechanisms by which microbes cause cancer, give one representative pathogen for each, and explain why the four are not interchangeable — what feature of the pathogen's biology determines which mechanism applies. For the inflammation mechanism, write a sentence-level causal chain from persistent infection to cancer.

2. **(E6/E7 checkpoint logic)** Explain at the molecular level how HPV E6 and E7 together achieve what would otherwise require two separate somatic mutations in *TP53* and *RB1*. Then predict: in a cell already expressing E6 and E7, what would an additional loss-of-function mutation in *TP53* add, if anything? Justify your answer.

3. **(Mechanism failure)** The "find the oncogene" model works for HPV but fails for *H. pylori*. Construct the argument that someone using only the direct-oncoprotein framework would make about *H. pylori*, explain precisely where that argument goes wrong, and identify what experimental observation would have forced a shift to the inflammation model.

4. **(Prevention chain)** Cervical cancer mortality in sub-Saharan Africa is roughly ten times that in high-income countries. Identify at least three distinct links in the prevention chain from HPV exposure to death, and for each, estimate its relative contribution to the gap. Which single intervention would yield the largest mortality reduction per dollar? Justify with mechanistic and epidemiological reasoning.

5. **(Necessary but not sufficient)** A patient from a region with both high *H. pylori* prevalence and high aflatoxin exposure develops hepatocellular carcinoma. Explain why the two exposures together might produce cancer at higher rates than either alone, using the initiation–promotion framework. Then explain why eradicating *H. pylori* in this patient's community would reduce but not eliminate liver cancer risk, and name the second intervention required.

---

## References

- NCI, HPV and Cancer. https://www.cancer.gov/about-cancer/causes-prevention/risk/infectious-agents/hpv-and-cancer
- NCI, Risk Factors: Infectious Agents. https://www.cancer.gov/about-cancer/causes-prevention/risk/infectious-agents
- NCI, *H. pylori* and Cancer. https://www.cancer.gov/about-cancer/causes-prevention/risk/infectious-agents/h-pylori-fact-sheet
- IARC, Global cancer burden 2022. https://www.iarc.who.int/news-events/new-report-on-global-cancer-burden-in-2022-by-world-region-and-human-development-level/
- Hanahan, D. (2022). Hallmarks of Cancer: New Dimensions. *Cancer Discovery*, 12(1), 31–46. https://aacrjournals.org/cancerdiscovery/article/12/1/31/675608/
- American Cancer Society, Cancer Facts & Figures 2026. https://www.cancer.org/research/cancer-facts-statistics/all-cancer-facts-figures/2026-cancer-facts-figures.html

---

## Prompts

### Figure 10.1 — HPV E6 and E7 disable two checkpoints
Build a node-edge systems diagram with two parallel arms converging on one terminal node. Upper arm: E6 oncoprotein → ubiquitin ligase → p53 degraded. Lower arm: E7 oncoprotein → Rb–E2F complex (block edge) → E2F released → S-phase genes on. Both arms feed directed arrows into a single shared node: checkpoint-free proliferating cell. Use arrowheads for activating edges and a distinct blunt/bar terminator for inhibitory edges (E7 blocking Rb, ligase degrading p53). Color the two oncoproteins blue (dominant drivers), the degraded/disrupted guardians (p53, Rb–E2F) sky-blue (anchors being attacked), and draw inhibitory edges in vermillion (blocking). Lay arms as two horizontal tracks merging at the right. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 10.2 — Four mechanisms of microbial carcinogenesis
Build a node-edge conceptual map: one central root node, "Microbial carcinogenesis," with four arrows radiating to four leaf nodes — direct oncoproteins switch off host control; insertional mutagenesis activates or disrupts a gene; chronic inflammation, reactive species hit DNA; immunosuppression lets a second pathogen pass. Arrange as a central hub with four spokes (radial or four-quadrant layout), each spoke a single directed arrow. Color the root sky-blue (anchor), the direct-oncoprotein and immunosuppression leaves vermillion (negative/aggressive routes), the inflammation leaf a transitional tone, and the insertional-mutagenesis leaf neutral gray. No numeric data, no axes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 10.3 — Chronic inflammation and the Correa cascade
Build a horizontal timeline with a single left-to-right axis labeled "Decades of inflammation" and five evenly spaced markers, each a labeled node with a one-line subtitle. Order: Gastritis (persistent bacterium, reactive species); Atrophy (epithelium thins); Metaplasia (tissue reorganizes); Dysplasia (architecture disordered); Adenocarcinoma (invasive endpoint). Sort strictly left-to-right in progression order; categorical time axis, no zero baseline. Color the first marker (Gastritis) a transitional tone to signal the inflammatory engine, the final marker (Adenocarcinoma) vermillion (negative endpoint), and intermediate markers neutral gray. No numeric data. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.

### Figure 10.4 — Infection-attributable cancer fraction
Build a single vertical bar chart (or one stacked/split bar) on a y-axis from a zero baseline, unit "% of cancers worldwide," showing two proportional segments: infection-attributable = 13 (highlighted) and other causes = 87. Keep ink proportional to value; zero baseline mandatory. Highlight the infection-attributable segment in blue (dominant focus) and render the other-causes segment in neutral gray. Add a direct data label on the highlighted segment ("~13%, roughly one in eight") and a short caption noting it equals about 2.2 million cases a year from seven viruses plus one bacterium. No legend needed if segments are directly labeled. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, Okabe-Ito colorblind-safe palette via CSS variables.
