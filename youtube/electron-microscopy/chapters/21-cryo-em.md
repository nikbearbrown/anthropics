# Chapter 21 — Cryo-EM: Vitrification, Cryo-Imaging, and Single-Particle Basics


## TL;DR

- Water has a preferred state below zero degrees Celsius: crystalline ice.
- The chapter moves through The plunge, Why vitreous ice, not liquid nitrogen, Imaging the vitrified specimen, How single-particle analysis builds a 3D structure, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Water wants to crystallize. Cryo-EM is the art of outpacing that instinct — freezing a biological specimen so fast that the molecules never get the news.*

---

> **Scope note:** This chapter teaches cryo-EM as a method extension of biological TEM prep and low-dose imaging. Single-particle analysis appears only as introductory framing — enough to read an SPA paper, not to run one.

---

Water has a preferred state below zero degrees Celsius: crystalline ice. The transition is thermodynamically favorable, and given enough time, water will take it. The problem for biology is that crystallization is violent at the molecular scale. Growing ice crystals push through membranes, crush protein complexes, strip hydration shells, and rearrange everything in the process. A cell that has been through ice-crystal formation looks nothing like a cell that was alive. The structural information is destroyed.

Conventional electron microscopy handles this by removing the water entirely — fixation, dehydration, resin embedding — and accepting that the dried, cross-linked structure is a reasonable stand-in for the hydrated original. For many questions, it is. For questions about the conformations of membrane proteins, the internal architecture of ribosomes mid-translocation, or the exact structural state of a drug-target complex, it is not. Chemical fixation locks whatever conformation happens to be prevalent when the fixative diffuses in, which is not necessarily the native state.

Cryo-EM takes a different approach. Instead of removing the water, it freezes the water so fast that crystals cannot form. If you can cool the specimen from room temperature to below the glass-transition temperature — roughly −140 °C — faster than ice nuclei can form and grow, the water arrests in an amorphous glass: the same random liquid-like arrangement it had at room temperature, locked solid. The biological structures dispersed in that glass are preserved in whatever conformation they occupied at the moment of freezing. They have never been heated. They have never been fixed. They are as close to native state as a sample outside a living cell can be.

The cooling rate required is fast: roughly $10^4$ °C per second or above `[verify]`. For a film of buffer 50–100 nm thick, plunging into liquid ethane at −180 °C achieves cooling rates in excess of $10^5$ °C/s `[verify]` — well above the threshold. The buffer vitrifies. The particles in it, frozen mid-rotation in random orientations, are ready to be imaged.

![Schematic cross-section of the thin buffer film during](images/21-cryo-em-fig-01.png)
*Figure 21.1 — Schematic cross-section of the thin buffer film during*

## The plunge

The physical act of vitrification is almost anticlimactically simple. You apply a few microliters of purified specimen suspension to a TEM grid — typically a holey-carbon grid, glow-discharged to make it hydrophilic. You blot the grid with filter paper for a few seconds, drawing away most of the liquid and leaving a film 50–100 nm thick across the grid holes. Then you plunge the grid into a small cup of liquid ethane held near −180 °C. The plunge takes about 200 milliseconds. The buffer vitrifies.

The challenge is everything surrounding that 200 milliseconds. The blotting step is finicky: too much blotting and the ice is too thin for particles to sit in; too little blotting and the ice is too thick for the beam to penetrate. The specimen concentration has to be right — too dilute and you waste beam time searching empty holes; too concentrated and particles overlap and can't be picked individually. The grid surface chemistry has to be right — many proteins prefer to sit at the air-water interface at the top and bottom of the thin film, rather than distributing randomly through the volume. When particles cluster at the interface, they all adopt the same preferred orientation, which catastrophically biases the 3D reconstruction later.

Modern automated plungers — the Vitrobot is one common instrument — handle the humidity control, the blot timing, and the plunge mechanics reproducibly. But the conditions that produce good ice for a given specimen still require empirical optimization. In practice, a new cryo-EM project typically spends weeks or months of grid-prep iterations before acquiring useful data.

**Liquid ethane is hazardous.** It is a cryogen at −180 °C, a cold-burn risk, and it displaces oxygen in a confined space. It is also *flammable*: liquid ethane near an ignition source is a fire hazard. Cryo-EM labs that prepare grids use a fume hood with no ignition sources, face shields, and cryo gloves. The ethane is stored in sealed vials; small spills are allowed to evaporate in the hood; large spills are an emergency. Appendix A covers the full protocol. The combination of burn risk, asphyxiation risk, and fire risk makes ethane the most operationally demanding cryogen in the building.

Once vitrified, the grid cannot be allowed to warm above roughly −140 °C. Above that temperature, the amorphous ice undergoes devitrification — it crystallizes into cubic or hexagonal ice, destroying the specimen. Every subsequent step in the workflow — storage, transfer, insertion into the microscope, imaging — must maintain the cold chain. The grid lives in liquid nitrogen from the moment it leaves the plunger until it reaches the TEM column.

## Why vitreous ice, not liquid nitrogen

A natural question: why not plunge directly into liquid nitrogen? It is colder, widely available, and less hazardous. The answer is the Leidenfrost effect. When a warm grid contacts liquid nitrogen, the surface of the nitrogen adjacent to the grid instantly boils, forming a thin insulating vapor blanket. The grid is effectively surrounded by a warm gas layer that slows the cooling rate — possibly below the vitrification threshold. The specimen goes through crystalline ice anyway.

Liquid ethane, held just above its melting point at −180 °C, does not boil on contact with the warm grid. It remains liquid, and the cooling rate is limited by thermal diffusion through the ethane rather than by an insulating vapor layer. This is why ethane, despite its hazards, has been the standard cryogen for plunge-freezing since the technique was developed in the early 1980s.

![Comparison of grid plunging into LN₂ vs](images/21-cryo-em-fig-02.png)
*Figure 21.2 — Comparison of grid plunging into LN₂ vs*

High-pressure freezing — the technique used for thicker biological specimens like tissue sections (Chapter 20) — uses a different mechanism: at 2,100 bar, the melting point of water shifts below the glass-transition temperature, so ice cannot form regardless of the cooling rate. But high-pressure freezing requires specialized equipment and cannot preserve the thin, freely suspended particles that single-particle work requires. For particles, the plunge is the method.

## Imaging the vitrified specimen

Inside the TEM, the cryo-holder keeps the grid at roughly −175 °C throughout imaging `[verify]`. This is cold enough that the vitreous ice is stable for hours; it is also cold enough that the specimen is about ten times more resistant to radiation damage than a room-temperature specimen `[verify]`. The biological molecules still damage under electron exposure — bond breaking, mass loss, conformational changes — but the dose threshold is higher at low temperature.

That higher threshold is critical because the fundamental limit on cryo-EM imaging is dose. Each electron that hits the specimen carries energy that can break chemical bonds. The useful information from a biological specimen — the coherent elastic scattering that forms the image — is extracted from a total exposure of 30–50 electrons per Å² `[verify]` before the accumulated damage makes the image uninterpretable. Compare this to a materials science TEM session, where the same sample might receive thousands of electrons per Å² with no consequence. Biological cryo-EM is dose-starved: every electron has to count.

Low-dose discipline (Chapter 19) is mandatory. The standard protocol divides the session into three areas on the grid: a search area at very low magnification to find grid squares with good ice, a tracking area offset from the imaging target to focus and correct astigmatism, and the imaging area itself — never pre-exposed, searched only at minimum dose, imaged once and not revisited. The goal is to accumulate the entire dose budget in a single exposure on a fresh area of the grid.

Direct-electron-detection cameras transformed this calculation. Before about 2013, cryo-EM images were recorded on slow scintillator-CCD cameras with relatively low detective quantum efficiency — a significant fraction of the information per electron was wasted. Direct-detection cameras sense electrons without an intermediate scintillator layer, recovering that lost efficiency. More importantly, they read out fast enough to record a multi-second exposure as 30–50 individual frames. Each frame has a tiny fraction of the total dose. The frames are then computationally aligned and summed, correcting for **beam-induced motion** — a wobble of the specimen that occurs in the first second of exposure as the beam heats and charges the ice. Motion correction, applied frame by frame, was what pushed cryo-EM from ~1 nm resolution into the sub-3 Å regime `[verify]`.

![Schematic of the DED frame-stack concept ](images/21-cryo-em-fig-03.png)
*Figure 21.3 — Schematic of the DED frame-stack concept *

## How single-particle analysis builds a 3D structure

A typical cryo-EM micrograph shows hundreds to thousands of individual copies of the same molecule — say, ribosomes — embedded in vitreous ice. Each ribosome is a single molecule in a unique orientation, frozen mid-rotation at the moment of vitrification. Each one is a different 2D projection of the same 3D object, viewed from a different angle.

This is exactly what you need for a 3D reconstruction, if you have enough copies. The logic is tomographic: if you can collect projections of the same object from many angles, you can reconstruct the 3D object that produced them. In conventional tomography (Chapter 19), you tilt a single specimen and collect projections at each tilt angle. In single-particle analysis, the tilting is done by the molecules themselves — thousands of copies, each at a different orientation, collectively spanning all angles.

The reconstruction algorithm assigns each particle image to an orientation based on how similar it looks to computed projections of a 3D model, then uses those angle-assigned images to refine the model iteratively. The cycle converges when the model's projections match the data. What comes out is a 3D electron-density map at whatever resolution the data support.

Why does averaging improve resolution? Each individual particle image has terrible signal-to-noise ratio — a few hundred electrons per Å² on a molecule a few nanometers across. Most pixels are dominated by noise. But the noise is uncorrelated between particles, and the signal is correlated — every copy of the ribosome has the same underlying structure. Averaging $N$ particles reduces the noise relative to the signal by $\sqrt{N}$. Average 100,000 particles and the noise drops by a factor of 316. This is the fundamental reason cryo-EM SPA works despite the dose constraint: you cannot increase the dose per particle without damaging the specimen, but you can average over more particles indefinitely.

![Illustration of the averaging principle ](images/21-cryo-em-fig-04.png)
*Figure 21.4 — Illustration of the averaging principle *

The bottleneck is data collection and computation, not physics. A modern cryo-EM session produces 1,000–10,000 micrographs, each containing hundreds of particles, over 24–72 hours of automated acquisition. The data volume is terabytes. The computational pipeline — particle picking, CTF correction, 2D classification, 3D reconstruction, refinement — runs on GPU clusters for days or weeks.

## What resolution numbers mean

When a cryo-EM paper reports "2.8 Å resolution," what does that mean in practice?

The standard metric is the Fourier Shell Correlation (FSC) at the 0.143 cutoff `[verify]`. The dataset is split into two halves; each half produces an independent 3D reconstruction; the FSC measures how well the two reconstructions agree as a function of spatial frequency. The resolution is defined as the spatial frequency at which the FSC drops to 0.143. This is a global number — it describes the average resolution across the entire structure.

What you can see at a given resolution: at 12 Å, you have the overall shape, nothing more. At 7 Å, secondary structure elements — alpha helices appear as cylinders, beta sheets as flat planes — are visible. At 4 Å, the backbone trace of the protein becomes clear. At 2.5–3 Å, side chains of most amino acids are visible, and an atomic model can be fit. Below 2 Å, individual atoms begin to be resolved.

The 2020 Nobel Prize in Chemistry `[verify]` recognized the cryo-EM revolution — specifically the contributions of Jacques Dubochet (vitrification), Joachim Frank (image processing and SPA reconstruction), and Richard Henderson (high-resolution protein structure by electron microscopy). The prize was awarded in 2017 `[verify]`. Ribosome structures, membrane protein structures, and entire viral capsids are now routinely solved at 2–4 Å by groups with standard access to modern instruments. Structures that spent decades resisting crystallization for X-ray diffraction are yielding to cryo-EM.

| Resolution | What is visible in the density map |
|---|---|
| **12+ Å** | Overall molecular shape only — envelope of the particle |
| **7–12 Å** | Secondary structure: α-helices visible as cylinders, β-sheets as planes |
| **4–7 Å** | Protein backbone trace visible; can begin docking known structures |
| **2.5–4 Å** | Side chains visible; an atomic model can be fit and refined |
| **< 2.5 Å** | Individual atoms resolved; near-X-ray-quality model — bound waters, ion coordination, alternate side-chain rotamers |

*The resolution number is meaningless without this calibration. A 4 Å map and an 8 Å map answer different questions.*

## The limitations you carry honestly

Cryo-EM SPA has real limitations, and reading a paper critically requires knowing what they are.

**Preferred orientation** is the most common and most insidious. Proteins at the air-water interface of the thin ice film do not orient randomly — many proteins have asymmetric surfaces and preferentially expose one face to the interface. If all particles are oriented the same way, the reconstruction has anisotropic resolution: good in some directions, bad in others. The maps may look impressive in the preferred-orientation plane but be blurred in the orthogonal direction. Detection: the angular distribution plot in the methods section should show coverage across all orientations. Mitigation: detergent additives to break interface preference, or tilted-grid acquisition.

**Specimen heterogeneity** means the dataset is a mixture of different conformational states. SPA classification separates them — sometimes cleanly, sometimes not. A reported structure is one class from that mixture, which is scientifically interesting if the classes are real and scientifically misleading if the classification is overfitted to noise.

**Local resolution variation** means the global FSC number does not represent the whole structure equally. A ribosome structure at "3.0 Å global resolution" may have a core at 2.5 Å and flexible peripheral elements at 5 Å. The paper should report local-resolution maps, not just the global number.

**The optimization overhead is invisible in the final paper.** A published cryo-EM structure represents months or years of grid-prep optimization, software pipeline tuning, and data curation. What looks like a straightforward method in the methods section may have required hundreds of failed grids to achieve. This is not dishonesty; it is the nature of publishing results rather than process.

## Where cryo-EM fits

Cryo-EM is the right technique when the question requires high-resolution 3D structure of a biological macromolecule in near-native state — particularly when the molecule resists crystallization (many membrane proteins), is large and flexible (ribosomes, viral capsids, large complexes), or needs to be characterized in multiple conformational states simultaneously.

It is the wrong technique when surface morphology of bulk material is the question (SEM), when elemental composition is the question (EDS), when live-cell dynamics are the question (fluorescence microscopy), or when the specimen is a hard inorganic material that requires FIB milling rather than thin-film blotting to prepare (Chapter 22).

For nanomedicine applications — lipid nanoparticles for mRNA delivery, polymer micelles, protein-drug conjugates — cryo-EM has become essential. Cryo-tomography on individual particles (Chapter 19) gives 3D internal structure; SPA on populations gives high-resolution ensemble averages. The combination answers questions that no other technique can: what does this 200 nm LNP actually look like inside, at molecular resolution, in buffer?

The wonder, stated plainly: by cooling a thin buffer film from room temperature to −175 °C in 200 milliseconds, it is possible to preserve the three-dimensional structure of protein complexes with sufficient fidelity to reconstruct them at near-atomic resolution from the images of 100,000 individual copies. The cooling front moves at millimeters per second; the molecular events frozen are happening on picosecond timescales. The technique bridges twelve orders of magnitude in time — and it works.

---

## Exercises

### Warm-up

**21.1** Explain in one sentence why plunge-freezing into liquid nitrogen fails to vitrify a TEM specimen, while plunge-freezing into liquid ethane at −180 °C succeeds. Your answer should name the physical phenomenon responsible. *(Tests: Leidenfrost effect and its consequence for cooling rate)*

**21.2** A cryo-EM micrograph shows discrete sharp diffraction rings overlaid on the specimen region. What has gone wrong, and what does it tell you about the ice? *(Tests: crystalline ice artifact recognition)*

**21.3** If averaging $N$ particles improves signal-to-noise ratio by $\sqrt{N}$, how many particles must be averaged to achieve a 100-fold improvement over a single particle? Why can't the same SNR improvement be achieved by simply increasing the beam dose on a single particle? *(Tests: the averaging argument and the dose constraint)*

### Application

**21.4** A graduate student prepares cryo-EM grids of a 300 kDa membrane protein complex and finds that all particles in the micrographs appear as identical round disks — no variation in shape between particles. What artifact does this suggest, and what two experimental approaches could address it? *(Tests: preferred orientation recognition and mitigation)*

**21.5** A published cryo-EM paper reports "3.2 Å global resolution" for a 250 kDa enzyme. The authors also show a local-resolution map where the catalytic core reaches 2.8 Å but a flexible regulatory domain is at 6.5 Å. What does this tell you about the limitation of the global FSC number, and what biological interpretation can you draw about the regulatory domain? `[verify]` *(Tests: local vs. global resolution, FSC interpretation, and connecting resolution to structural flexibility)*

**21.6** You are setting up a cryo-EM session on a new purified protein. Your first grids show thick ice (low contrast, particles barely visible) in some holes and empty holes (no ice film, just holey carbon) in others. Name the blotting parameter most likely responsible for each problem and how you would adjust it. *(Tests: blotting optimization and ice-thickness troubleshooting)*

**21.7** Explain why direct-electron-detection cameras improved cryo-EM resolution compared to scintillator-CCD cameras, using the concepts of detective quantum efficiency and beam-induced motion correction. *(Tests: DED mechanism and its connection to the resolution jump post-2013)*

### Synthesis

**21.8** A structural biology lab wants to characterize a 500 kDa protein complex that is known to exist in three distinct conformational states during its catalytic cycle. Design a cryo-EM SPA workflow that could resolve all three states. Specify: specimen preparation considerations, approximate particle number needed, which computational step separates the three states, and one potential artifact that could falsely create apparent conformational states that don't exist biologically. *(Tests: integrating vitrification, particle count/averaging, 3D classification, and heterogeneity artifact awareness as a connected workflow)*

**21.9** A nanomedicine lab has 150 nm lipid nanoparticles loaded with mRNA and wants to determine whether the mRNA is in the aqueous core or associated with the lipid bilayer. Compare what conventional TEM (after negative staining), cryo-TEM single-particle imaging, and cryo-electron tomography each can and cannot tell them about this question, and recommend which to use first and why. *(Tests: technique selection across conventional TEM, cryo-TEM, and cryo-ET for a nanomedicine question that directly connects to multiple chapters)*

### Challenge

**21.10** A cryo-EM paper reports a membrane protein structure at 3.5 Å resolution using 80,000 particles. A reviewer notes that the angular distribution plot shows strong preferred orientation — 90% of particles are in two orientations. Using the concepts in this chapter, explain quantitatively why preferred orientation compromises the reconstruction quality even if the global FSC reports 3.5 Å, and propose what the authors should do to address the reviewer's concern. `[verify: FSC and angular distribution interplay]` *(Tests: connecting preferred orientation, angular coverage, reconstruction anisotropy, and critical reading of resolution claims — requires synthesizing the limitations section with the FSC/resolution section in a specific critique)*

---

*What would change my mind:* evidence that chemical fixation can reliably preserve membrane-protein conformations with the same fidelity as cryo-EM. The empirical record consistently favors cryo-EM for native-state preservation. The resolution gap, since direct-detection cameras became standard, is also large enough that cryo-EM is the obvious choice for high-resolution structural work on biological macromolecules.

*Still puzzling:* the factors that predict whether a cryo-EM project will succeed — good particle distribution, no preferred orientation, adequate ice thickness — are largely empirical and project-specific. The optimization loop from "first grid" to "usable data" varies from days to years and is not well-predicted by biochemical characterization of the specimen. A theory of grid-prep optimization would be valuable.
