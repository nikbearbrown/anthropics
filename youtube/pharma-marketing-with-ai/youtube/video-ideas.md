# Video Ideas — Pharma Marketing with AI

Scout date: 2026-07-09
Source material: pantry research syntheses (chapters are scaffold placeholders; content drawn from `pantry/pharma-ai-hcp-marketing-synthesis.md`, `pantry/pharma-marketing-evidence-synthesis.md`, `pantry/conversation-summary.md`, `pantry/moe-vs-ensemble-synthesis.md`).

---

## Candidate 01 — The Prescribing Moment: How Pharma Got Inside Your Doctor's EHR

- Source: `pharma-marketing-with-ai/pantry/pharma-ai-hcp-marketing-synthesis.md`
- Topic: PHARMA MARKETING
- Hook: Epic and Oracle Cerner officially prohibit commercial advertising inside their EHR systems. Pharmaceutical ads appear inside those systems anyway — legally, at the exact moment a physician is writing a prescription, in the same visual layer as drug safety warnings.
- Key case: SMART on FHIR — an open interoperability standard designed for clinical decision support apps — is the technical entry point. Doceree's Spark product uses it to embed branded messages inside EHR workflows at 150+ health systems. When a physician enters ICD-10 code Z87.891 (history of nicotine dependence) and navigates to e-prescribing, a smoking cessation drug ad appears. The CDS Hooks mechanism fires the same way a drug-interaction alert would.
- The Question: When a physician sees a message in the same visual layer as a safety warning, and it is actually an ad — at the moment they are writing a prescription — is that clinical decision support or commercial influence?
- Core idea: The SMART on FHIR and CDS Hooks standards were designed to improve clinical care by giving third-party apps access to patient context at key workflow moments. Commercial platforms repurposed these open standards for point-of-care advertising. The standards opened the door; no regulation controls what walks through it. EHR-integrated advertising sits in a regulatory vacuum with no specific FDA OPDP guidance as of 2026.
- Visual object: A timeline of one prescribing workflow — chart opens → diagnosis code entered → [AD FIRES] ← same moment as drug interaction alert → e-prescription written. The ad insertion moment is color-coded differently but shown in the identical interface layer.
- Manim move: trace — follow a single prescribing workflow step by step; the ad appears exactly at the decision node
- Example seed: Walk through the CDS Hooks JSON payload that fires when a physician prescribes metformin — the co-pay card appears. The payload does not transmit the patient's name or record number. The ad server receives only a contextual trigger: this physician, this diagnostic moment. Is that PHI? The legal question has not been formally adjudicated.
- Length band: 3–5 min
- Still lanes: c2v (EHR workflow diagram), raster (physician at computer), geo (health system exterior)
- Prerequisites: Awareness that doctors use electronic records; basic understanding of drug prescribing workflow
- Exclusions: EHR vendor business models, full FHIR technical spec, Epic vs. Cerner competitive dynamics
- Score: 10/10

---

## Candidate 02 — Bid-by-NPI: When Every Doctor Gets Their Own Auction Price

- Source: `pharma-marketing-with-ai/pantry/pharma-ai-hcp-marketing-synthesis.md`
- Topic: PHARMA MARKETING
- Hook: In 2025, pharma advertisers gained the ability to set individual bid prices for reaching a specific doctor — not a specialty, not a geography, but a single National Provider Identifier. The most valuable prescribers now have their own auction price in a real-time exchange.
- Key case: Bid-by-NPI, launched in 2025 by Tap Native/eHealthcare Solutions, is the first programmatic auction model where pharma brands bid for ad impressions at the single prescriber level, pricing each physician's attention based on their predicted prescribing value. The NPI is the data primitive — a permanent, accurate identifier tied to verified prescribing history — unlike a cookie, which expires and can be blocked.
- The Question: When a physician's prescribing history, specialty, and patient panel are used to price their individual attention in a real-time auction — without their knowledge — what does consent mean in this context?
- Core idea: The NPI identity graph connects three legally separate data streams: de-identified pharmacy claims (who prescribed what), AMA Physician Masterfile (who that NPI is), and behavioral signals (digital reads, CME completions, website visits). The combination is legal under HIPAA safe harbor — no step in the chain is prohibited. The result is a complete commercial profile of a specific physician that prices their attention in a market they don't know exists.
- Visual object: A data flow pipeline — Claims Data → De-identified → AMA Masterfile Bridge → NPI Identity Graph → Real-time Auction → Single Physician's Screen. Each step labeled with its legal status (compliant / compliant / compliant / no consent required).
- Manim move: accumulate — data streams flow in from the left, merge at a central graph node, then route out as an auction bid to a single physician endpoint
- Example seed: Dr. Martinez in cardiology switched three patients off Brand X last month. Her IQVIA LAAD prescribing record updated. Her behavioral signals show Brand Y digital engagement trending up. Her CRM score flags her as a high-value conversion target. The bid-by-NPI system sets a premium price for her next ad impression. She has no idea the score is being kept.
- Length band: 3–5 min
- Still lanes: c2v (data pipeline diagram), raster (physician at laptop), geo (data center)
- Prerequisites: Basic understanding of online advertising auctions; familiarity with medical licensing concepts
- Exclusions: Programmatic advertising technical infrastructure in detail, AMA organizational politics, full HIPAA safe harbor provisions
- Score: 9/10

---

## Candidate 03 — The Verification Gap: Every Script Lift Number Is Vendor-Generated

- Source: `pharma-marketing-with-ai/pantry/pharma-ai-hcp-marketing-synthesis.md`
- Topic: PHARMA MARKETING
- Hook: Point-of-care pharmaceutical advertising is a billion-dollar industry claiming 19–44% script lift. Every single one of those numbers comes from the platform selling the product. There are no independent academic validations. The most invasive form of medical influence has the weakest evidence base.
- Key case: OptimizeRx claims its DAAP platform produced 3x the return in half the time vs. traditional trigger-based targeting in a 2024 major depressive disorder campaign. Doceree reports average script lifts of 19–25% from EHR programs based on NPI-level analysis. The methodology: the same data infrastructure used for targeting (NPI prescribing history) is used to measure the outcome. The platform that sells the targeting also runs the attribution. There is no independent audit.
- The Question: If the only evidence that EHR-integrated pharma advertising works comes from the companies selling EHR-integrated pharma advertising — and those companies use the same proprietary data for targeting AND measurement — what does "19% script lift" actually prove?
- Core idea: Attribution methodology in point-of-care advertising is structurally circular: the NPI-level link between ad exposure and subsequent prescribing requires access to the same claims data used for targeting. The platform knows which physicians saw the ad (they served it) and which subsequently prescribed (they have the prescribing data). Comparing exposed vs. unexposed HCPs requires constructing a valid counterfactual from observational data — a methodological problem the platforms do not describe in detail and academic researchers have not independently assessed.
- Visual object: A closed loop diagram — [Pharma Brand] → [Platform Targets Dr. X] → [Dr. X Prescribes] → [Platform Claims Credit] → [Pharma Brand Pays] → back to start. An "Independent Auditor" node shown outside the loop with no connecting arrows.
- Manim move: rotate — the closed attribution loop spins continuously; the external auditor node stays still with no connection
- Example seed: Contrast this with TV advertising measurement — Nielsen panels, independent viewership data, academic marketing studies that pharmaceutical advertisers can't manipulate. Now contrast with EHR advertising: only the platform knows who saw what; only the platform has the prescribing data; only the platform runs the analysis. The industry has self-certified its own effectiveness at billion-dollar scale.
- Length band: 2–3 min
- Still lanes: c2v (circular loop diagram), raster (data analyst, pharmaceutical executive)
- Prerequisites: Basic understanding of how advertising effectiveness is typically measured
- Exclusions: Full statistical methods for causal inference, individual platform technical specifications, FDA measurement standards
- Score: 9/10

---

## Candidate 04 — The Black Box Susceptibility Problem: AI That Profiles Physicians Without Naming What It Learns

- Source: `pharma-marketing-with-ai/pantry/conversation-summary.md`
- Topic: PHARMA MARKETING
- Hook: Pharmaceutical AI targeting systems can learn which physicians are psychologically susceptible to which relationship stimuli — without any discriminatory variable being named, without any single party making a discriminatory decision, distributed across four commercial relationships with no point of accountability.
- Key case: The data exists: Open Payments (public) records which physicians accept meals and from whom. NPI prescribing data shows whether prescribing shifted after payment activity. CRM records link each physician to each rep relationship. Computer vision can proxy rep demographic characteristics from photos. A model trained on "which pairings preceded prescribing increases" learns the pattern without labels. The output is: "assign rep ID 4471 to NPI 1234567890." The reason lives in 50 million parameters.
- The Question: When an AI system learns that certain physician profiles respond to certain rep characteristics — and optimizes accordingly — who is responsible for the discrimination that emerges, and who is harmed?
- Core idea: Three parties bear costs from a susceptibility targeting model no one explicitly built. The rep is sorted by physical characteristics through "neutral optimization" — less conventionally attractive reps get worse territories, managed out, cause unnamed. The physician is profiled for psychological susceptibility without consent or knowledge, matched to the relationship stimulus most likely to produce desired prescribing behavior. The patient receives a prescription shaped not by clinical evidence but by a targeting model that identified their doctor as susceptible to a specific stimulus. Current US regulation addresses none of these three harms.
- Visual object: A three-node harm diagram — Rep (top), Physician (middle), Patient (bottom). Arrows show how the optimization model flows harm downward through each layer. A separate "Regulatory Coverage" overlay shows what each existing regime covers (FDA: content; Sunshine Act: disclosure; HIPAA: patient data) — none of the nodes are covered.
- Manim move: spread — a single model output branches out and touches all three victim nodes simultaneously, while regulation markers appear and miss each node
- Example seed: Describe the mechanism without naming anyone: a pharma brand trains a next-best-action model on three years of rep-physician interaction data and downstream prescribing outcomes. The model recommends rep assignments. The brand's territory manager acts on the recommendations. No one reviewed what the model learned. No one asked. The EU AI Act would require this system to be audited as high-risk AI in healthcare. No US equivalent applies.
- Length band: 3–5 min
- Still lanes: c2v (harm diagram, regulatory coverage overlay), raster (physician-rep interaction)
- Prerequisites: Basic understanding of machine learning / recommendation systems; awareness of pharmaceutical sales practices
- Exclusions: Specific company names, individual case studies, EU AI Act technical compliance requirements in detail
- Score: 9/10

---

## Candidate 05 — The Market Failure at the Center: Why Nobody Funds the AI That Would Help Patients

- Source: `pharma-marketing-with-ai/pantry/pharma-ai-hcp-marketing-synthesis.md`
- Topic: PHARMA MARKETING
- Hook: The same SMART on FHIR standard that delivers branded pharmaceutical ads at the prescribing moment could, in principle, deliver comparative effectiveness data and generic substitution prompts at the same moment. The technology is identical. Nobody pays for the second version at scale.
- Key case: Healthcare AI investment in pharma commercial operations is projected to grow from $1.9 billion in 2025 to over $16 billion by 2034 — funded entirely by pharma commercial interest. The VA academic detailing program, NPS MedicineWise in Australia, and the Therapeutics Initiative in British Columbia are the largest functioning alternatives. None operates at the scale or with the investment level of the commercial stack. The infrastructure being built — NPI identity graphs, real-time EHR integration, AI audience modeling — exists because pharma brands pay for it.
- The Question: The parties who benefit most from unbiased prescribing are patients and payers. Why are they the least organized to fund the counter-infrastructure?
- Core idea: The funding asymmetry is not a technology problem or an ethics problem — it is a collective action problem. Pharma brands capture the benefit of commercial AI targeting specifically, immediately, and measurably (script lift per campaign). Patients and payers would capture the benefit of evidence-based prescribing AI diffusely, over long time horizons, and unattributably. The economics run against the patient-centered alternative even when the technology to build it already exists and is already deployed commercially.
- Visual object: A split investment comparison — left column shows commercial pharma AI stack (labeled investments, $16B projected) built on SMART on FHIR. Right column shows patient-centered AI alternative (VA program, NPS MedicineWise — same technology, labeled as underfunded fragments). The SMART on FHIR layer is shown as shared infrastructure at the base of both columns.
- Manim move: duplicate — the same technology stack duplicates; one copy accumulates investment labels, the other remains sparse
- Example seed: A physician opens a patient chart. The SMART on FHIR layer fires. In the commercial version: a co-pay card for a brand-name drug appears. In the hypothetical patient-centered version: comparative effectiveness data appears, including generic alternatives and cost-to-patient estimates. Both are technically feasible today. One is funded at billion-dollar scale. Describe exactly what the unfunded version would show.
- Length band: 3–5 min
- Still lanes: c2v (investment comparison diagram), raster (physician at EHR), geo (VA facility)
- Prerequisites: Basic awareness of how pharmaceutical marketing works; understanding that EHR software is used to prescribe drugs
- Exclusions: Specific policy prescriptions, legislative proposals, detailed health economics modeling
- Score: 10/10
