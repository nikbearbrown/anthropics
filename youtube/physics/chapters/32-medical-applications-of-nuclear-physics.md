# Chapter 32 — Medical Applications of Nuclear Physics

*The same physics that diagnoses disease can cure it. The dose makes the difference.*

---

George de Hevesy is twenty-eight years old, a chemist in Vienna, and he suspects his landlady is recycling last week's leftovers. In 1913 he has no way to prove it — except that he has recently been working with radium-D, what we now call lead-210, a beta emitter with a conveniently long half-life. He sprinkles a small amount onto his hash one Sunday, leaves the rest on the plate, and asks her to take it back.

Wednesday evening, she serves him hash again. He brings out an electroscope. It discharges.

The radium-D is in the new dish.

De Hevesy catches his landlady — but he also notices something larger: a radioactive isotope behaves chemically like its stable partners and follows the same biological pathways, but its presence and concentration can be detected anywhere with a radiation counter. Tag a substance with a radioactive isotope and you can track it through any chemical or biological process you like, in a living organism, in real time, without disturbing it.

He spent the rest of his career working out what that meant. The 1943 Nobel Prize in Chemistry. The foundation of nuclear medicine. By the 1960s, doctors could image organs by injecting tagged compounds and detecting emitted gamma rays. By the 1980s, PET scans could map metabolic activity at millimeter resolution. By the 2010s, targeted radioisotope therapies were curing cancers that surgery and chemotherapy couldn't reach.

This chapter is about how nuclear physics — alpha, beta, gamma, half-life, binding energy from Chapter 31 — gets put to work inside the human body. And about the units that quantify what radiation does when it arrives.

---

## Imaging: what each tool sees

A patient receives an injection of technetium-99m bound to a bone-seeking compound. The Tc-99m has a half-life of 6.0 hours and emits a 140-keV gamma ray — energetic enough to escape the body but not so energetic it deposits excessive dose. The compound concentrates in regions of active bone metabolism: fracture sites, tumors, infection.

A few hours later, a gamma camera records each gamma arrival and its position. The image, accumulated over minutes, shows the patient's skeleton highlighted where the tracer has concentrated. A radiologist can spot fractures invisible to X-ray, metastatic cancer in bone, deep infections.

Now compare this to a chest X-ray. The X-ray is a transmission image: an external source sends X-rays through the body, and differential absorption by tissues of different density casts a 2D shadow. Bone absorbs more than soft tissue, which absorbs more than air. The image reveals structure — broken ribs, dense tumors, foreign objects.

![Patient injected with positron-emitting tracer (FDG, ¹⁸F). Positron annihilates with nearby electron, producing two 511 keV gamma photons traveling at exactly 180°. Ring of detectors records coincident pairs; tomographic...](../images/32-medical-applications-of-nuclear-physics-fig-01.png)
*Figure 32.1 — PET — Positron Annihilates Electron, Two 511 keV Gammas Fly Back-to-Back*

Now compare both to PET. The patient receives $^{18}$F-fluorodeoxyglucose (FDG) — glucose with a fluorine-18 label ($t_{1/2}$ = 110 min). Cells that consume glucose preferentially (most cancers, active brain regions) accumulate the FDG. Fluorine-18 decays by positron emission; each positron travels a few millimeters and annihilates with an electron, releasing two 511-keV gamma rays traveling in exactly opposite directions. A ring of detectors records coincident gamma pairs and reconstructs the 3D distribution of glucose consumption. The image shows function — where the body is metabolically active — not structure.

Three tools, three physical signals, three completely different windows. Choosing the right one for the clinical question is half the art of medical imaging.

<!-- → [TABLE: major medical imaging modalities — columns: modality, physical signal detected, what it reveals, typical effective dose; rows: chest X-ray (differential X-ray absorption, structure/density, 0.1 mSv), CT (differential X-ray absorption, 3D structure, 7–10 mSv), MRI (RF response of nuclear spin precession, soft tissue detail and some function, no ionizing dose), gamma camera/SPECT (gammas from injected radiotracer, organ function and perfusion, 5–10 mSv), PET (coincident gamma pairs from positron annihilation, metabolic function, 7–10 mSv), PET-CT (both, anatomy + function fused, 14 mSv); student should see that each modality detects a different physical signal and is good for different clinical questions] -->

MRI deserves a special note because it is the one major imaging modality that is *not* based on ionizing radiation and not based on nuclear decay. It works on the spin of hydrogen nuclei — protons in water molecules — precessing in a strong external magnetic field. Apply a radio-frequency pulse at the Larmor frequency ($f = \gamma B_0 / 2\pi$, with $\gamma/(2\pi) = 42.58$ MHz/T for protons), tip the spins out of alignment, and the relaxation back to equilibrium emits a measurable RF signal. The relaxation times $T_1$ and $T_2$ depend sensitively on the chemical environment — different in white matter vs. gray matter, different in tumor vs. healthy tissue, different in inflamed vs. normal muscle. That dependence is what gives MRI its extraordinary soft-tissue contrast. No radiation. No radioactive tracer. Just quantum mechanics applied to nuclear spin in a strong magnetic field.

The limitations are real: MRI is slow, expensive, and excludes patients with certain metallic implants. For soft-tissue and brain imaging it is unmatched. For rapid triage of suspected fractures, a plain X-ray is still faster and cheaper. The tools are not interchangeable.

---

## Dose: quantifying what radiation does

A radiation worker at a nuclear medicine clinic wears a small badge — film, thermoluminescent crystals, or a chip-based dosimeter. Once a month it is read. If their annual accumulated dose exceeds 50 mSv, they are pulled from radiation work for the rest of the year.

That number, 50 mSv, is an *equivalent dose* in millisieverts. To understand what it means — to compare it to a chest X-ray, to natural background, to a cancer therapy — you need the chain of three units that converts raw radioactive decays to biological damage.

**Activity** is how many decays per unit time. One **becquerel** (Bq) is one decay per second. One **curie** (Ci) is $3.7 \times 10^{10}$ Bq, originally defined as the activity of one gram of radium-226.

**Absorbed dose** is energy deposited per unit mass of tissue. One **gray** (Gy) = 1 J/kg. (The older unit, the rad, is 0.01 Gy and still appears in clinical settings.) A given activity over a given time deposits a dose that depends on the geometry, the stopping power of tissue, and what fraction of the emitted energy is absorbed.

![Two panels of damage tracks through tissue. Alpha (high LET): dense ionization along a short straight track, w_R = 20. Gamma (low LET): sparse, scattered ionization over a long range, w_R = 1. Same dose in Gy, 20× difference...](../images/32-medical-applications-of-nuclear-physics-fig-02.png)
*Figure 32.2 — α vs γ — Same Energy, Very Different Damage Track*

**Equivalent dose** is absorbed dose weighted by the biological effectiveness of the radiation type. One gray of alpha particles damages tissue far more than one gray of gamma rays, because alphas — heavy, slow, highly charged — deposit their energy in dense tracks that create clustered DNA double-strand breaks. Gamma photons create sparse, isolated ionizations that cells can usually repair. The *radiation weighting factor* $w_R$ captures this:

| Radiation | $w_R$ |
|---|---|
| X-rays, gamma rays, beta particles | 1 |
| Thermal neutrons | 5–10 |
| Fast neutrons | 10–20 |
| Alpha particles, heavy nuclei | 20 |

One **sievert** (Sv) = 1 Gy $\times$ $w_R$. The older unit, the rem, equals 0.01 Sv. So 0.5 Gy of gammas = 0.5 Sv, while 0.5 Gy of alphas = 10 Sv — twenty times the biological damage from the same deposited energy.

Some reference doses to anchor the scale:

![Logarithmic ladder of equivalent dose (Sv). 5 μSv dental X-ray, 100 μSv chest X-ray, 2 mSv annual background, 10 mSv abdominal CT, 50 mSv annual occupational limit, 1 Sv acute illness threshold, 4 Sv LD50 (50% mortality...](../images/32-medical-applications-of-nuclear-physics-fig-03.png)
*Figure 32.3 — Radiation Dose Ladder — Dental X-Ray to Acute Lethal*

Annual U.S. background radiation averages about 3.0 mSv — dominated by radon from soil (~2 mSv) and cosmic rays (~0.3 mSv, more at altitude). A chest X-ray is ~0.1 mSv. A chest CT is ~7 mSv, about two years of background. A whole-body PET-CT is ~14 mSv. The acute lethal dose (LD50, no treatment) is ~4–5 Sv — five thousand times a chest CT. The occupational annual limit for U.S. radiation workers is 50 mSv.

<!-- → [CHART: radiation dose comparison on a log scale — horizontal bar chart with doses on a log axis from 0.001 mSv to 10,000 mSv (10 Sv); bars for: dental X-ray (0.005 mSv), chest X-ray (0.1 mSv), mammogram (0.4 mSv), chest CT (7 mSv), whole-body PET-CT (14 mSv), annual U.S. background (3 mSv, shown as vertical reference line), annual occupational limit (50 mSv), acute lethal dose LD50 (4,000–5,000 mSv); color-code bars by risk category (green for below background, yellow for 1–50 mSv, red above 100 mSv); student should see the 7-order-of-magnitude span from dental X-ray to lethal dose and where each medical procedure falls relative to natural background] -->

![Comparison table of five major modalities: X-ray (ionizing, 0.1 mSv, 0.2 mm), CT (ionizing, 10 mSv, 0.3 mm), MRI (non-ionizing magnetic, 0 mSv, 0.5 mm), SPECT (gamma tracer, 5 mSv, 5 mm), PET (positron tracer, 7 mSv, 4 mm).](../images/32-medical-applications-of-nuclear-physics-fig-05.png)
*Figure 32.5 — Medical Imaging Modalities — Signal, Dose, Resolution Compared*

The risk model used to regulate medical imaging is the **linear no-threshold** (LNT) model: cancer risk is assumed proportional to dose, with no safe floor. Above ~100 mSv the data (primarily from Hiroshima and Nagasaki survivor cohorts) are reasonably clear. Below that, the data are sparse and the model is an extrapolation. The LNT model gives a rough risk coefficient of $\sim 5 \times 10^{-5}$ per mSv — one additional cancer per 20,000 mSv of total population dose. A single 10-mSv CT scan carries an estimated $\sim 0.05\%$ additional lifetime cancer risk, against a baseline U.S. cancer risk of ~40%. For a genuine clinical indication, the benefit of the information vastly outweighs the risk. For routine screening of asymptomatic patients — especially children, whose longer remaining lifespan and growing tissues increase sensitivity — the calculus is harder.

Worked example: a worker accidentally inhales an alpha emitter. The alpha particles deposit an absorbed dose of $0.50 \text{ Gy}$ to the lung. What is the equivalent dose?

$$H = D \times w_R = 0.50 \text{ Gy} \times 20 = 10 \text{ Sv}.$$

Ten sieverts is catastrophic — 200 times the annual occupational limit, well into the range of severe acute radiation syndrome. Alpha emitters in the lung are precisely this dangerous because they're stopped by only a few cell layers, depositing all their energy locally. This is why radon in basements — an alpha emitter that lodges in lung tissue when inhaled — is the second leading cause of lung cancer in the United States after smoking.

---

## Therapy: the same physics, a million times the dose

A brain-tumor patient is fitted with a metal halo bolted to the skull for sub-millimeter positioning. They lie inside a *Leksell Gamma Knife* — a hemispherical helmet containing 192 cobalt-60 sources. Each $^{60}$Co source emits 1.17 and 1.33 MeV gammas when it decays. Each individual beam is too weak to cause tissue damage alone. But all 192 beams converge on a single point — the tumor — where the combined dose is high enough to destroy it.

The patient walks out the same day. No incision. Sub-millimeter precision.

This is radiation therapy: using ionizing radiation to kill cancer. The same ionizing radiation that diagnoses bone metastases, at a dose millions of times higher, focused with geometry to deliver a lethal dose to the tumor while sparing surrounding tissue. The ratio of tumor-cell kill to normal-cell kill is the *therapeutic ratio*, and every technique in radiation therapy is engineered to maximize it.

**External beam radiation therapy (EBRT)** uses a beam of X-rays or charged particles aimed at the tumor from outside. To spare normal tissue, the beam is rotated through many angles (intensity-modulated radiation therapy, IMRT), so the tumor accumulates dose from every angle while any single normal-tissue point receives a fraction of the total. Modern LINAC machines produce 6–25 MV X-rays from electrons accelerated into tungsten targets.

**Brachytherapy** implants radioactive seeds directly inside or adjacent to the tumor — high local dose, minimal distant dose. Prostate cancer: $^{125}$I or $^{103}$Pd seeds implanted permanently, decaying slowly over weeks to months. Cervical cancer: $^{192}$Ir sources loaded into an applicator, delivering their dose, then removed.

**Targeted radiopharmaceuticals** chemically attach a radioactive isotope to a molecule that selectively binds to cancer cells. Thyroid cancer: $^{131}$I, because thyroid cells selectively take up iodine. The beta particles from $^{131}$I have range ~1–2 mm in tissue — they kill the cells that absorbed the iodine without significantly damaging the surrounding structure. Bone-metastatic prostate cancer: $^{223}$Ra, a calcium analog that deposits in bone. Newer antibody-conjugated agents target specific tumor surface receptors.

![Dose deposition vs depth in tissue. X-ray: high at surface, falls exponentially. Protons: low at surface, peaks sharply at the end of range (Bragg peak), then nothing beyond. Tumor placed at peak gets maximum dose; healthy...](../images/32-medical-applications-of-nuclear-physics-fig-04.png)
*Figure 32.4 — Bragg Peak — Proton Therapy Deposits Dose at a Chosen Depth, Then Stops*

**Proton and charged-particle therapy** exploit the *Bragg peak* — the depth at which a charged particle deposits maximum energy. A fast proton moving through tissue gradually loses energy via ionizations; as it slows, the rate of energy loss increases (because slower particles spend more time in any given region). Just before the proton stops, there is a sharp peak of dose deposition. Beyond it: essentially nothing. By tuning the initial energy, the therapist places the Bragg peak exactly at the tumor depth.

Compare this to a megavoltage X-ray beam, which deposits maximum dose near the patient's surface and falls off exponentially with depth. To treat a deep tumor with X-rays, you unavoidably overdose the tissue in front of it. With protons, you don't — or much less so. This physical advantage is why proton therapy is increasingly used for pediatric cancers and tumors adjacent to critical structures.

<!-- → [INFOGRAPHIC: depth-dose curves for a megavoltage X-ray beam and a proton beam — x-axis is depth in tissue (0–30 cm), y-axis is relative dose (0–100%); the X-ray curve starts high near the surface (~80%), has a brief buildup, then falls roughly exponentially; the proton curve is low near the surface (~30%), rises, then has a sharp Bragg peak (~100%) at the target depth (e.g., 15 cm), followed by a sharp falloff to near zero; shade the tumor region at the target depth and annotate that the proton beam delivers full dose at the tumor while the X-ray beam deposits significant dose in front of and beyond the tumor] -->

A standard prostate-cancer radiotherapy course delivers 200 cGy (2 Gy) per fraction, five days per week for eight weeks:

$$D_\text{total} = 2 \text{ Gy} \times 5 \times 8 = 80 \text{ Gy}.$$

The whole-body acute lethal dose is ~5 Gy. Eighty grays to the prostate is survivable because it is *geometrically localized* — surrounding normal tissue receives much less. The therapeutic ratio is what makes the treatment possible.

---

## Tracing, imaging, and treating: the same idea

Pull back to de Hevesy's table in 1913. He had noticed that you could track a substance through a biological system by tagging it with a radioactive isotope. The radioactivity is detectable anywhere. The chemistry is identical to the untagged version.

That single observation is the conceptual foundation of nuclear medicine.

Diagnostic: inject a tiny amount of a tagged compound. The tracer follows the same metabolic pathways as the untagged molecule, but it announces its location by emitting radiation. The gamma camera, SPECT, and PET scanner are just detectors that record where the signal comes from. The dose is small — a few millisieverts, comparable to natural background for a year.

Therapeutic: the same idea, scaled up. Use a beta or alpha emitter instead of a gamma emitter, so the energy is deposited locally rather than escaping. Use a molecule that concentrates in the tumor rather than distributing throughout the body. The target tissue absorbs a lethal dose. The dose elsewhere is limited by the specificity of the targeting molecule.

A thyroid cancer patient walks through this full arc. First, a $^{99m}$Tc scan shows the thyroid's anatomy and identifies suspicious nodules. Then a $^{18}$F-FDG PET-CT maps metabolic activity and looks for metastases. Then surgery removes the thyroid. Then $^{131}$I is given at therapeutic doses — 100–200 mCi, thousands of times more than a diagnostic dose — targeting any residual thyroid tissue (including cancer cells that take up iodine) with beta particles that travel only a millimeter or two. The patient is temporarily isolated in a shielded hospital room because the $^{131}$I's gamma rays would expose visitors and family. The 5-year survival rate for differentiated thyroid cancer with this approach exceeds 95%.

Same physics — radioactive decay, charged particles depositing energy in tissue — applied at diagnostic doses for detection, therapeutic doses for cure. The units (Bq, Gy, Sv) exist to make this range navigable. A 10-mSv PET scan and an 80-Gy prostate treatment are both applications of the same decay physics, separated by five orders of magnitude in delivered dose.

The dose makes the difference. That is the central fact of this chapter.

---

## Exercises

### Warm-up

**32.1** *(LO 1)* Match each imaging modality to the physical signal it detects and one clinical question it answers well: (a) CT scan, (b) MRI, (c) PET with $^{18}$F-FDG, (d) bone scan with $^{99m}$Tc, (e) chest X-ray. Signals: differential X-ray absorption; gamma emission from injected tracer; coincident gamma pairs from positron annihilation; RF response from nuclear spin precession.

**32.2** *(LO 2)* Convert: (a) $8.5 \text{ mCi}$ to Bq; (b) $3.0 \text{ Gy}$ to rad; (c) $25 \text{ mSv}$ to rem; (d) $0.20 \text{ Gy}$ of fast neutrons ($w_R = 15$) to Sv.

**32.3** *(LO 3)* Why is $^{99m}$Tc the most widely used radiopharmaceutical isotope? Address at least three of: half-life, gamma energy, decay mode, production method, availability of technetium chemistry.

**32.4** *(LO 4)* A prostate cancer patient receives $2.0 \text{ Gy}$ per fraction, five days per week, for nine weeks of external-beam radiotherapy. (a) What is the total dose? (b) The whole-body acute lethal dose is ~5 Gy. Why doesn't this treatment kill the patient?

### Application

**32.5** *(LO 2, 5)* A radiologist receives the occupational dose limit of $50 \text{ mSv}$ in one year. (a) Estimate the increased lifetime cancer risk using the LNT coefficient $5 \times 10^{-5}$ per mSv. (b) Compare to the U.S. baseline lifetime cancer risk (~40%). (c) Over a 30-year career at this limit, what is the cumulative dose and the estimated total additional risk?

**32.6** *(LO 2)* An alpha-emitting radon daughter deposits $0.030 \text{ Gy}$ of absorbed dose to the lung. (a) What is the equivalent dose? (b) An X-ray exam of the same lung deposits $0.50 \text{ Gy}$. What is the equivalent dose from the X-ray? (c) Which is more biologically damaging, and by what factor?

**32.7** *(LO 3)* $^{131}$I (iodine-131, $t_{1/2} = 8.0 \text{ d}$) is given at a therapeutic activity of $150 \text{ mCi}$ to treat thyroid cancer. (a) Convert the initial activity to Bq. (b) How long until the activity has fallen to $1\%$ of the starting value? (c) Why is the patient isolated during this period?

**32.8** *(LO 4)* Explain the physical principle of the Bragg peak in proton therapy in your own words. (a) Why does a proton deposit more energy per unit length as it slows down? (b) Why is there essentially no dose beyond the Bragg peak? (c) For a tumor at 12 cm depth, what happens to tissue at 8 cm and at 15 cm compared to a megavoltage X-ray treatment?

### Synthesis

**32.9** *(LO 2, 5)* A patient undergoes three imaging procedures in one year: a chest CT (7 mSv), an abdominal CT (10 mSv), and a whole-body PET-CT for cancer staging (14 mSv). (a) What is the total effective dose? (b) How does this compare to annual U.S. background? (c) Estimate the additional lifetime cancer risk. (d) Under what clinical circumstances would this total dose be justified?

**32.10** *(LO 3, 4)* Compare the use of $^{123}$I ($t_{1/2} = 13 \text{ h}$, pure gamma) and $^{131}$I ($t_{1/2} = 8.0 \text{ d}$, beta + gamma) in thyroid medicine. (a) Which would you use for a diagnostic thyroid scan, and why? (b) Which would you use for ablation of residual thyroid cancer, and why? (c) Why would $^{123}$I be a poor choice for therapy, and why would $^{131}$I be a poor choice for pure diagnosis?

**32.11** *(LO 1, 2, 4)* A patient with a 3-cm brain tumor receives Gamma Knife radiosurgery with 192 cobalt-60 sources ($t_{1/2} = 5.27 \text{ yr}$, each emitting gammas at 1.17 and 1.33 MeV). The prescription dose to the tumor is 20 Gy. (a) Why use 192 beams rather than one stronger beam? (b) The cobalt sources are replaced periodically. How long before each source decays to half its initial activity? (c) If the sources are $3.5 \text{ yr}$ old, by what factor has the activity (and therefore dose rate per source) changed?

### Challenge

**32.12** *(LO 5, beyond chapter)* The LNT model assumes a proportional risk down to zero dose. Consider a community living at 3,000 m altitude (extra cosmic-ray dose ~1 mSv/yr above sea level). (a) Using LNT, what additional cancer risk does this represent per year? Per lifetime (75 yr)? (b) In practice, mountain communities do not have elevated cancer rates. What does this suggest about LNT at very low doses? (c) Why do regulators continue to use LNT despite this observation?

**32.13** *(LO 3, 4, beyond chapter)* Lutetium-177 ($^{177}$Lu) is a beta emitter ($t_{1/2} = 6.7 \text{ d}$, max beta energy 0.50 MeV) that is being used as a targeted radiotherapy agent for neuroendocrine tumors and prostate cancer when attached to specific tumor-targeting peptides. (a) Why is a beta emitter (rather than a gamma or alpha emitter) often preferred for targeted therapy? (b) The beta particle has range ~1 mm in tissue. What does this imply about the minimum tumor size that can be treated effectively? (c) A tumor receives $80 \text{ Gy}$ of absorbed dose from the beta particles, while the adjacent normal organ receives $8 \text{ Gy}$. What is the therapeutic ratio, and why is even a ratio of 10 valuable for cancer treatment?

---



By the end of this chapter you should be able to:

1. Identify the principal medical-imaging modalities and describe what physical signal each detects.
2. Define activity (Bq, Ci), absorbed dose (Gy), and equivalent dose (Sv), apply the radiation weighting factor $w_R$, and convert between units.
3. Explain how radioactive tracers are chosen for specific diagnostic applications (half-life, gamma energy, biological pathway) and why $^{99m}$Tc and $^{18}$F are so widely used.
4. Describe external-beam, brachytherapy, and targeted-radiopharmaceutical radiation therapy and explain the therapeutic ratio and the Bragg peak advantage of proton therapy.
5. Estimate equivalent dose for an exposure scenario and connect it to cancer risk using the linear no-threshold model.

**Prerequisites.** Chapter 31 (radioactivity, decay modes, half-life). Chapter 30 (X-ray production). Chapter 22 (magnetic fields, for MRI context).

**Why this chapter matters.** Nearly every modern medical workup involves a nuclear-physics-based procedure. CT scans account for ~70 million procedures per year in the U.S. alone. PET-CT has transformed cancer staging. Targeted radiotherapy now cures many cancers that were fatal a generation ago. Understanding both the power and the dose risk of these tools is part of being a literate participant in a modern medical system.

---

## ↳ Dig Deeper — How MRI works at the level of nuclear spin

*MRI is the one major imaging modality not based on ionizing radiation. The physics is quantum mechanics applied to proton spin in a strong magnetic field — Larmor precession, RF excitation, and relaxation times that encode chemical environment.*

**Prompt:**
> Explain how MRI works at the level of nuclear spin. (a) Alignment of hydrogen-1 nuclear spins in a strong external field $B_0$ (typically 1.5–3 T). (b) Larmor precession at $f = \gamma B_0/(2\pi)$ with $\gamma/(2\pi) = 42.58$ MHz/T for protons. (c) How an RF pulse at the Larmor frequency tips the spins out of alignment, and how relaxation back to equilibrium ($T_1$, $T_2$) emits a measurable signal. (d) How magnetic-field gradients encode spatial position into the precession frequency. End with one sentence on why different soft tissues have distinctive $T_1$ and $T_2$ values and why this gives MRI its soft-tissue contrast advantage over CT.

**What to do with the output:** Save it. MRI is one of the most beautiful applications of quantum mechanics in clinical medicine, and a perfect example of how an arcane physical effect becomes routine practice.

---

## ↳ Dig Deeper — The linear no-threshold model and its critics

*The chapter uses LNT implicitly. Below ~100 mSv, the epidemiological data are too sparse to confirm or refute linearity. The debate has real consequences for radiation regulation, pediatric CT policy, and occupational limits.*

**Prompt:**
> Explain the LNT model and its critics. (a) State the assumption: cancer risk is linearly proportional to dose, with no threshold. (b) Summarize the evidence for it (Hiroshima/Nagasaki data above ~50–100 mSv). (c) Summarize the main challenges: hormesis (very low doses may be beneficial), threshold models, and DNA-repair arguments. (d) Explain why LNT is still used in regulation (precautionary principle, absence of strong contradictory data at clinically relevant doses). End with one sentence on why this matters for pediatric imaging protocols and occupational exposure limits.

**What to do with the output:** Save it. The LNT debate is one of the few places where nuclear physics, epidemiology, and public-health policy directly intersect — and where the underlying science is genuinely uncertain.

---

## ↳ Dig Deeper — The Bragg peak and the case for proton therapy

*The physical advantage of protons over X-rays — a sharp dose peak at controllable depth, near-zero dose beyond — is clear. Whether that translates to clinical benefit for most adult cancers is actively debated.*

**Prompt:**
> Explain the physics of the Bragg peak in proton therapy. (a) Describe the Bethe-Bloch energy-loss formula: $-dE/dx \propto Z^2/v^2$. Explain why slowing particles deposit more energy per unit length. (b) Compare the depth-dose curve of protons (sharp Bragg peak, near-zero dose beyond) to megavoltage X-rays (buildup near surface, exponential falloff). (c) The case for proton therapy: pediatric cancers, brain tumors near critical structures, cases where sparing distal tissue is critical. (d) The controversy: $100M+ facility cost, limited evidence of clinical benefit over advanced X-ray techniques (IMRT, VMAT) for many adult cancers. End with one sentence on the current clinical trajectory of proton therapy in oncology.

**What to do with the output:** Save it. Proton therapy is an active frontier in radiation oncology and a good case study in how a clear physics advantage does not automatically translate into proportionate clinical benefit.

---

## LLM Exercise — Chapter 32: Medical Nuclear Physics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry connecting your phenomenon to medical imaging or therapy via radiation dose.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 32, I want to apply medical-nuclear-physics — imaging, dose, therapy — to my phenomenon.

Please:

1. Identify ONE medical-nuclear connection. Examples:
   - Bike commute: the X-ray for a wrist fracture from a fall; the bone scan for a stress injury.
   - Coffee maker: the annual background dose to any person who operates it; the X-ray used to diagnose occupational injuries.
   - Basketball shot: X-ray for a sprained finger or knee, MRI for ligament damage, bone scan for stress fracture.
   - Marathon: X-ray or MRI for stress fractures or tendinitis; DEXA scan for bone density monitoring in older runners.

2. Apply ONE chapter equation. Compute equivalent dose from absorbed dose × $w_R$, or estimate cancer risk from a specific procedure using the LNT model ($\sim 5 \times 10^{-5}$ per mSv).

3. Specify input numbers (look up the typical effective dose for the procedure).

4. Run the calculation. Report value with units.

5. One sanity check: does the dose match published reference values?

6. One sentence connecting to Chapter 33 (particle physics) — many of the same physics ideas underlie particle therapy.

Save the output as logbook/chapter-32-medical-nuclear.md.
```

### What this produces

A Logbook entry computing a radiation dose relevant to your phenomenon, with a cancer-risk context from the LNT model.

### How to adapt this prompt

- *If you've personally had imaging procedures:* compute your own cumulative dose in mSv, with appropriate uncertainty.
- *For Claude Code:* if you have a list of imaging procedures with doses, sum them and compare to background and occupational limits.

### Connection to previous chapters

Builds on Chapter 31 (radioactivity, decay modes, half-life) and Chapter 30 (X-ray production from atomic transitions). Chapter 22's magnetic fields underlie MRI.

### Preview of next chapter

Chapter 33 (particle physics) descends below the nucleus — to quarks and the Standard Model. Relativistic charged-particle beams, the same physics used in proton therapy, also underlie particle accelerators at high energy.

---

## What would change my mind

The chapter argues that medical nuclear techniques are well-validated and that their benefits in appropriately selected situations outweigh radiation risks. The argument would need revision if large-scale epidemiological studies found cancer risks from diagnostic-level doses significantly higher than LNT predicts, or if a non-ionizing modality achieved equivalent diagnostic performance for current PET/CT applications. Both are active research areas.

## Still puzzling

The deepest unresolved question this chapter raises: *what is the actual cancer risk from diagnostic-level radiation doses (1–50 mSv)?* Above ~100 mSv, atomic-bomb survivor data are fairly clear. Below that, the LNT extrapolation is the best available tool, but it is an extrapolation, not a measurement. The answer matters for whether routine pediatric CT screening is wise, whether repeated PET-CT monitoring increases population cancer rates, and how strict occupational limits should be. The uncertainty is not academic — it drives billions of dollars of medical-practice decisions each year.

---

## AI Wayback Machine

**Irène Joliot-Curie** discovered artificial radioactivity in 1934 with her husband Frédéric — and the Nobel Prize they shared the following year made possible the artificial radioisotopes used in modern PET and SPECT imaging.

![Irène Joliot-Curie](../images/irene-joliot-curie-v1p.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Irène Joliot-Curie, and how does her work on artificial radioactivity connect to the medical applications of nuclear physics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Irène Joliot-Curie"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how bombardment of aluminum with alpha particles produced the first artificial radioisotope.
- Ask it about her parallel career as a French government minister for scientific research, and what happened to that role.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 33 (particle physics) descends below the nucleon — to quarks, gluons, and the Standard Model. Relativistic charged-particle beams and particle accelerators, the same hardware used in proton therapy, also probe sub-nuclear structure at much higher energies. Chapter 34 (frontiers) considers dark matter, gravitational waves, and open questions in fundamental physics — many of the detection techniques used there have common roots with the radiation-detection physics in this chapter.

---

**Tags:** medical-nuclear-physics, radiation-dose, PET-imaging, radiotherapy, dosimetry
