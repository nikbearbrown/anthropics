# Bear's Doodles — Cancer Research Video Ideas

slate cut 

## Candidate 01 — Why a "99% Accurate" Cancer Test Is Wrong Two Times Out of Three
- Source: `books/cancer-research/chapters/01-cancer-screening-finding-it-early-enough-to-cure.md`
- Production mode: Manim visualization
- Hook: A blood test that is 90% sensitive and 99% specific sounds airtight — yet in a healthy population its positive result is real only about one time in three.
- Core idea: Positive predictive value is not a property of the test; it depends on how common the disease actually is. Screen 100,000 people at 0.5% prevalence and the 1% false-positive rate draws from 99,500 healthy people (995 false alarms) while true cancers number only 450 — so PPV is 31%. Move to a 10% prevalence group and the identical test gives 91%.
- Visual object: A field of 100,000 dots; the sick minority lights up, the test flags them, and the flood of false-positive dots visibly swamps the handful of true positives.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: What "positive test result" means; comfort with a percentage.
- Exclusions: Cut sensitivity-vs-specificity definitions beyond what the demo needs; cut the three screening biases (own video); cut Wilson-Jungner criteria; cut the MCED/Galleri policy discussion; cut the opening 58-year-old case narrative. Keep it to one contrast: same test, two populations.
- Score: 9/10

slate cut 

## Candidate 02 — Why the Same Radiation Dose Can Cure or Paralyze
- Source: `books/cancer-research/chapters/08-radiation-oncology-principles-and-biology.md`
- Production mode: Manim visualization
- Hook: 70 Gray in 35 small daily fractions controls the tumor and spares the spinal cord; the identical 70 Gray packed into 10 big fractions would risk permanent paralysis.
- Core idea: Radiation can't tell a tumor cell from a neuron, but tumor and late-responding normal tissue have different α/β ratios. On the linear-quadratic survival curve, small fractions keep tumor (α/β ≈ 10) and spinal cord (α/β ≈ 3) close together; large fractions send the low-α/β normal tissue plunging far below the tumor. Fractionation is engineering a gap out of an indiscriminate weapon.
- Visual object: Two cell-survival curves that ride together at 2 Gy per fraction and tear apart at 7 Gy per fraction.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: Radiation damages DNA; cells can die from that damage.
- Exclusions: Cut the α/β derivation and the SF = exp(−αD − βD²) equation; cut the full five Rs; cut the BED arithmetic (own video); cut direct-vs-indirect damage and the oxygen enhancement ratio. One idea only: fraction size, not total dose, sets the harm.
- Score: 9/10

slate cut 

## Candidate 03 — Why "Tumors Shrank 3x More" Doesn't Mean Patients Lived Longer
- Source: `books/cancer-research/chapters/04-principles-of-cancer-therapy-goals-and-modalities.md`
- Production mode: Mixed
- Hook: A drug tripled the response rate — 60% of tumors shrank versus 20% — and the survival curves came back nearly identical.
- Core idea: Tumor shrinkage (response rate, progression-free survival) is a surrogate — a proxy for what patients actually care about: living longer and better. A surrogate is trustworthy only if moving it reliably moves the hard endpoint. Here the surrogate moved, overall survival stayed flat, and toxicity got worse — so the "breakthrough" dissolves.
- Visual object: Two overlapping overall-survival curves that refuse to separate, sitting under a tumor-shrinkage bar that towers for the new drug.
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: Cancer drugs are tested in trials; "survival" means how long people live.
- Exclusions: Cut the four treatment goals (cure/control/palliation/comfort); cut neoadjuvant/adjuvant/concurrent timing terms; cut pseudoprogression and iRECIST; cut accelerated-approval policy. Anchor on one trial's four numbers and the surrogate-vs-hard split.
- Score: 9/10

slate cut 

## Candidate 04 — Chemo Doesn't Just Kill Fast-Dividing Cells (The Slogan Is Half Wrong)
- Source: `books/cancer-research/chapters/10-chemotherapy-principles-and-major-drug-classes.md`
- Production mode: Doodle
- Hook: If chemotherapy simply killed whatever divides fastest, the bone marrow — which divides faster than many tumors — would die first and the slow tumor would survive. It's often the reverse.
- Core idea: "Fast division = vulnerability" explains the side effects (hair, gut, marrow) but not the cure. The anti-tumor effect tracks vulnerability, not speed: cancer cells carry defects in DNA repair, apoptosis, and checkpoints, so a normal stem cell takes a hit, pauses, and repairs, while the defective tumor cell takes the same hit and dies.
- Visual object: A fast normal stem cell and a slow tumor cell take identical DNA hits — the normal one patches and moves on, the defective one shatters.
- Manim move: reveal
- Short-form fit: Strong
- Prerequisites: Chemotherapy damages DNA; cells divide.
- Exclusions: Cut the five drug classes and their toxicities; cut cell-cycle-phase specificity; cut the Bari harbor origin story; cut combination-regimen rules. Stay on the one correction: why the slogan fails.
- Score: 9/10

slate cut 

## Candidate 05 — A Genetic "Match" Is a Guess. The Tumor Grades It.
- Source: `books/cancer-research/chapters/05-precision-oncology-matching-therapy-to-tumor.md`
- Production mode: Manim visualization
- Hook: Two patients, the same KRAS G12C mutation, the same targeted drug — one shrinks for four months then rebounds, the other never responds at all.
- Core idea: A molecular match says the target is present; it doesn't say the tumor depends on that target, or that it will keep depending on it. One alteration produces three trajectories — durable benefit, transient response then resistance, and primary non-response — because treatment is selection pressure acting on an evolving population, and co-occurring alterations can route around the block from day one.
- Visual object: Three tumor-burden curves starting from one point and diverging — one stays down, one dips and climbs, one never falls.
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: Cancers have mutations; some drugs target specific mutations.
- Exclusions: Cut predictive-vs-prognostic biomarker theory (own video); cut basket/umbrella/platform trial designs; cut the tumor-agnostic approval list; cut the oncogene-addiction survey. One alteration, three fates.
- Score: 8/10

slate cut 

## Candidate 06 — A Cancerous Lymph Node Is a Perfect Signal and a Useless Target
- Source: `books/cancer-research/chapters/06-surgical-oncology-principles-of-cancer-surgery.md`
- Production mode: Mixed
- Hook: For decades a positive lymph node meant "cut out the rest of them." Then trials showed that removing them didn't help patients live longer — it just caused lifelong arm swelling.
- Core idea: Staging value and therapeutic value are separable. A node with cancer truthfully tells you the disease has reached the lymphatics (staging — confirmed). But removing that node and its basin does not extend survival in low-volume disease (MSLT-II in melanoma, Z0011 in breast) — because the cells that determine survival had already seeded before surgery. One finding, two verdicts.
- Visual object: A single glowing positive node that forks into two labeled paths — "staging: confirmed" (holds) and "therapy: refuted" (severed).
- Manim move: split
- Short-form fit: Strong
- Prerequisites: Lymph nodes can contain spreading cancer; surgeons remove them.
- Exclusions: Cut the five surgical principles; cut sentinel-node tracer technique details; cut the margin/R0 discussion (own video); cut the Halsted history (own video). Just the staging-vs-therapy separation and the two trials.
- Score: 8/10

slate cut 

## Candidate 07 — The "Cleaner" Radiation Beam That Doesn't Help Where It Hurts
- Source: `books/cancer-research/chapters/09-modern-radiation-therapy-technology-toxicity-and-integration.md`
- Production mode: Manim visualization
- Hook: Proton beams really do stop dead at the tumor with no exit dose — and for prostate cancer that elegance buys the patient almost nothing.
- Core idea: The proton's Bragg peak spares tissue beyond the tumor. But prostate side effects — rectal bleeding, urinary and sexual dysfunction — come from structures beside the prostate, not beyond it, and modern IMRT already protects those. Dosimetric superiority is necessary but not sufficient for clinical benefit: you have to ask whether the tissue you're saving is the tissue driving the patient's outcome.
- Visual object: A depth-dose curve drawing itself into tissue — the photon trailing an exit tail, the proton spiking at the Bragg peak and vanishing — with the "feared toxicity" zone highlighted beside, not beyond, the target.
- Manim move: drawon
- Short-form fit: Strong
- Prerequisites: Radiation is aimed through the body at a tumor; nearby organs get hit.
- Exclusions: Cut IMRT/VMAT/IGRT machinery; cut the pediatric and chordoma cases where protons DO win (mention in one line only); cut chemoradiation and PACIFIC; cut oligometastatic SABR. One question: is the spared tissue the tissue that matters?
- Score: 8/10

slate cut 

## Candidate 08 — How to "Double" Survival Without Anyone Living a Day Longer
- Source: `books/cancer-research/chapters/01-cancer-screening-finding-it-early-enough-to-cure.md`
- Production mode: Doodle
- Hook: Find the cancer at 50 instead of 55, and "five-year survival" can double — even if the patient dies at 60 either way.
- Core idea: Lead-time bias. Survival is measured from the date of diagnosis. Move the diagnosis earlier and the measured survival stretches, while the actual age at death never budges. This is why screening programs can advertise dramatic survival gains while changing nothing about when people die — and why the only honest endpoint is disease-specific mortality.
- Visual object: A single lifespan bar with a fixed death marker; slide the diagnosis marker leftward and watch the "survival" span balloon while death stays pinned.
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: "Five-year survival" is a common cancer statistic.
- Exclusions: Cut length-time bias and overdiagnosis (fold to one closing line, or separate videos); cut PPV/prevalence (own video); cut Wilson-Jungner; cut the NLST mortality result beyond one sentence. One bias, one sliding marker.
- Score: 8/10

slate cut 

## Candidate 09 — The Blood-Test Mutation That Never Came From the Tumor
- Source: `books/cancer-research/chapters/03-molecular-diagnostics-staging-and-the-liquid-biopsy.md`
- Production mode: Mixed
- Hook: A liquid biopsy on a lung-cancer patient flags a DNMT3A mutation — a signal that most likely came from his aging blood cells, not his tumor at all.
- Core idea: Plasma cell-free DNA is a pool fed by two sources — dying tumor cells and the patient's own aging white blood cells (clonal hematopoiesis, common in everyone over 60). Once the fragments mix, the assay can't tell which source a mutation came from. Acting on a clonal-hematopoiesis mutation as if it were tumor sends the patient down a pointless, frightening workup.
- Visual object: Two streams of DNA fragments — tumor and white-cell — pouring into one plasma pool where a flagged mutation floats with no traceable origin.
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: Blood carries DNA fragments; tests can read mutations.
- Exclusions: Cut the three-validity hierarchy; cut TNM staging; cut the DYNAMIC/MRD trial; cut low-shedding sensitivity limits. Just: two sources, one indistinguishable pool.
- Score: 8/10

slate cut 

## Candidate 10 — The Surgery That Healed Faster and Let the Cancer Come Back
- Source: `books/cancer-research/chapters/07-modern-surgical-oncology-minimally-invasive-and-reconstructive-approaches.md`
- Production mode: Mixed
- Hook: Keyhole surgery for cervical cancer gave smaller scars, less blood loss, faster recovery — and a several-fold higher recurrence rate that got the trial stopped early.
- Core idea: A surgery produces two outcomes on two clocks. Recovery and morbidity show up in days to weeks; cancer control takes years. Minimally invasive radical hysterectomy won the fast clock and lost the slow one (the LACC trial), and because equivalence had been assumed from other operations, thousands were done before anyone measured the survival cost. Oncologic equivalence must be proven per operation.
- Visual object: A dual timeline — the recovery track peaks green in weeks while the oncologic track stays flat, then bends downward years later.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: Surgery removes tumors; "recurrence" means the cancer comes back.
- Exclusions: Cut the list of operations where MIS proved equivalent (one line); cut the three candidate mechanisms for LACC harm; cut robotic-surgery cost debate; cut reconstruction. One lesson: two clocks, and the assumption that skipped the second.
- Score: 8/10

slate cut 

## Candidate 11 — She Got the Exact Right Dose. It Was a Massive Overdose.
- Source: `books/cancer-research/chapters/11-chemotherapy-pharmacology-resistance-and-toxicity-management.md`
- Production mode: Mixed
- Hook: Five days into standard-dose chemo she's in the ER with near-zero white cells — having received precisely the milligrams the protocol specified.
- Core idea: A dose is a property of the drug and the body it enters. The enzyme DPD (gene DPYD) clears about 80% of fluoropyrimidine chemo. In the 3–5% of people carrying loss-of-function variants, the "normal" dose isn't cleared — it accumulates to a functional overdose. The error wasn't arithmetic; it was treating the milligram as fixed instead of testing the enzyme first.
- Visual object: Two identical pills entering two bodies; in the normal metabolizer the drug level rises and drains, in the variant carrier the drain is blocked and the level climbs into the toxic zone.
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: Drugs are broken down and cleared by the body; genes vary between people.
- Exclusions: Cut the full ADME walkthrough; cut UGT1A1 and TPMT (name them in one line); cut the resistance section (own video); cut the supportive-care calendar. One gene, one drug, one overdose.
- Score: 8/10

slate cut 

## Candidate 12 — A Negative Biopsy Doesn't Mean No Cancer
- Source: `books/cancer-research/chapters/02-cancer-diagnosis-imaging-and-the-tissue-sample.md`
- Production mode: Manim visualization
- Hook: The scan screams cancer, the biopsy comes back benign — and there's still a better-than-one-in-three chance the tumor is there and the needle simply missed it.
- Core idea: Biopsy results are asymmetric: a positive is reliable (cancer cells were seen), a negative is not (maybe absent, maybe missed). With a high pretest probability (say 80%) and an imperfect biopsy sensitivity (~85%), a benign result only drags the probability of cancer down to about 39% — not zero. In dense pancreatic tumors the needle can pass through stroma and pull back reassuring, wrong tissue.
- Visual object: A probability bar that starts at 80% and, when the negative biopsy lands, drains only partway — stopping at 39%, far above the "stop looking" line.
- Manim move: drain
- Short-form fit: Strong
- Prerequisites: Biopsies sample tissue with a needle; tests aren't perfect.
- Exclusions: Cut the imaging-modality tour (CT/MRI/US/PET); cut FFPE/H&E/IHC pathology; cut FNA-vs-core comparison; cut the full likelihood-ratio math (show the two numbers only). One asymmetry, one partial drain.
- Score: 7/10

slate cut 

## Candidate 13 — Why 36 Grays Can Hit Harder Than 60
- Source: `books/cancer-research/chapters/08-radiation-oncology-principles-and-biology.md`
- Production mode: Manim visualization
- Hook: For prostate cancer, 36 Gy delivered in 5 big fractions is biologically a bigger dose than 60 Gy in 30 small ones.
- Core idea: Physical Grays aren't biological effect. Biologically effective dose depends on fraction size and the tissue's α/β. Prostate tumor has an unusually low α/β (~1.5), so large fractions land on the steep part of its survival curve: 36.25 Gy in 5 fractions ≈ 211 Gy BED versus 60 Gy in 30 fractions ≈ 140 Gy BED. Comparing raw Grays is like comparing a bullet's mass to its velocity and calling it energy.
- Visual object: Two dose bars — 60 and 36 — that flip their heights when the BED formula is applied, the small physical dose morphing into the larger biological one.
- Manim move: morph
- Short-form fit: Medium
- Prerequisites: Radiation dose is measured in Grays; ideally watch Candidate 02 first.
- Exclusions: Cut the LQ-model derivation; cut the five Rs; cut the rectal-wall safety calculation (mention in one line); cut the SBRT-model-breakdown caveat. One counterintuitive flip, powered by one formula.
- Score: 7/10

slate cut 

## Candidate 14 — Same Mutation, Same Drug, Opposite Result — Because of the Neighborhood
- Source: `books/cancer-research/chapters/05-precision-oncology-matching-therapy-to-tumor.md`
- Production mode: Doodle
- Hook: BRAF V600E melanoma melts away on BRAF-blocking drugs (response over 60%); the identical mutation in colon cancer barely flinches.
- Core idea: The tissue that's supposed to be "incidental" in a tumor-agnostic mutation isn't. Colorectal cells carry abundant EGFR signaling; block BRAF and feedback reactivates EGFR, restoring the very signal the drug just cut — a bypass route melanoma doesn't have. Same target, same drug, different wiring, so colon cancer needs an added anti-EGFR antibody to respond at all.
- Visual object: A signaling pathway with the BRAF node blocked; in melanoma the line goes dark, in colon cancer a hidden EGFR bypass lights up and reroutes around the block.
- Manim move: reveal
- Short-form fit: Strong
- Prerequisites: Drugs can block a specific step in a cell's growth signal.
- Exclusions: Cut predictive-vs-prognostic theory; cut trial designs; cut the KRAS resistance story (Candidate 05); cut the tumor-agnostic approval list. One pathway, one bypass, two tissues.
- Score: 7/10

slate cut 

## Candidate 15 — Why "Block the Pump" Failed: A Cancer Cell Has Six Doors
- Source: `books/cancer-research/chapters/11-chemotherapy-pharmacology-resistance-and-toxicity-management.md`
- Production mode: Doodle
- Hook: Cancer cells pump chemo back out, so the obvious fix was to jam the pump — and in trial after trial it did nothing.
- Core idea: Resistance in real tumors isn't one leak, it's a system. A resistant cell can reduce drug uptake, pump drug out, inactivate it, mutate the target, ramp up DNA repair, and evade apoptosis — often several at once. Block the efflux pump and the drug still gets neutralized, repaired around, or its death signal ignored. Single-target reversal fails because the defenses run in parallel.
- Visual object: One tumor cell with a drug molecule trying to reach its target and getting stopped at six different points; sealing the pump just reroutes the failure to the next door.
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: Chemo has to get inside a cell and hit a target to work.
- Exclusions: Cut intrinsic-vs-acquired framing; cut named genes (ABCB1, MGMT, ERCC1) beyond one example; cut the clonal-evolution timeline; cut pharmacogenomics (own video). Show the six defenses and why one lock doesn't matter.
- Score: 7/10

slate cut 

## Candidate 16 — Eighty Years of Bigger Surgery That Never Saved More Lives
- Source: `books/cancer-research/chapters/06-surgical-oncology-principles-of-cancer-surgery.md`
- Production mode: Mixed
- Hook: The radical mastectomy removed the breast, the muscles, and every axillary node for eighty years — and a trial showed a simple lumpectomy plus radiation gave the same survival.
- Core idea: Intuition says more complete removal must mean more certain cure. Randomized trials (Fisher's NSABP B-06) repeatedly refuted it: survival is set by micrometastatic cells that left the primary before any operation began, so extending the local operation adds morbidity without adding life. Surgery should be as limited as the evidence supports, not as radical as fear suggests.
- Visual object: The Halsted resection field shrinking step by step down to a lumpectomy, while the survival curve beside it never moves.
- Manim move: collapse
- Short-form fit: Medium
- Prerequisites: Surgery removes tumors; cancer can spread microscopically before surgery.
- Exclusions: Cut the five surgical principles; cut margins/R0 detail; cut sentinel-node and the staging-vs-therapy trials (Candidate 06); cut the pancreatic/bladder/neck examples (one line). One historical reversal and why biology, not the knife, sets the ceiling.
- Score: 7/10
