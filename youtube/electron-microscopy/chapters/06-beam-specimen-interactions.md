# Chapter 6 — Electron Beam–Specimen Interactions in SEM


## TL;DR

- A 1 nm probe enters the specimen and becomes a micrometer-wide cloud — and every image you take is a sample from that cloud, not from the probe.
- The chapter moves through What happens when the beam enters the solid, How deep the beam goes, Backscattered electrons: the depth signal, Secondary electrons: the surface signal, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A 1 nm probe enters the specimen and becomes a micrometer-wide cloud — and every image you take is a sample from that cloud, not from the probe.*

---

Here is an experiment you can do with a block of PMMA — the same plastic in safety goggles and contact lenses — and a scanning electron microscope. Park the beam on a single point at 20 keV for a few seconds. Remove the specimen. Drop it in a beaker of methyl isobutyl ketone, which selectively dissolves polymer chains that have been broken by radiation. Wait a minute. Pull it out and look at the surface under an optical microscope.

There is a crater. Not a dimple, not a mark — a teardrop-shaped cavity, open at the top, dropping nearly a micrometer below the entry point, swelling into a bulb wider than the beam ever was. The beam was 1 nm across. The crater is several hundred nanometers wide and a micrometer deep. The beam did not do what you aimed at. It spread.

What you are looking at is the **interaction volume** — the three-dimensional region of the specimen that the beam actually touches once it enters the solid. The etch reveals it because the beam broke polymer chains everywhere it deposited energy, not just at the surface. The contours of the crater are contours of dose. And dose spread out in a teardrop because inside the solid, the beam electron does not travel in a straight line. It scatters — sideways, downward, sometimes backward — until after many collisions it has deposited all its kinetic energy and stopped.

Every signal you collect from an SEM detector comes from somewhere inside that teardrop. Secondary electrons, backscattered electrons, characteristic X-rays: each one originates at a specific depth range within the volume, and the image you read from each signal is not a picture of the beam impact point. It is a depth-averaged, lateral-averaged sample from a cloud whose size depends on the voltage you set, the elements in your specimen, and the angle at which the beam meets the surface. Understanding this is understanding what the SEM is actually measuring.

![Etched PMMA crater (left) and a Monte Carlo simulation of trajectories at 20 keV in PMMA (right). Two independent measurements of the same physics.](../images/06-beam-specimen-interactions-fig-01.png)

*Figure 1.* Etched PMMA crater (left) and a Monte Carlo simulation of trajectories at 20 keV in PMMA (right). Two independent measurements of the same physics.

## What happens when the beam enters the solid

There are two physically distinct things the beam electron can do when it encounters an atom.

The first is **elastic scattering**. The electron interacts with the electrostatic field of the nucleus — a heavy, positively charged object that barely recoils — and the electron's direction changes without its speed changing. The kinetic energy before equals the kinetic energy after. The word elastic, from the Greek for "able to spring back," means the collision conserves kinetic energy. What it does not conserve is direction. A strong elastic scatter can deflect the electron by tens of degrees. Many such events, and the trajectory becomes a random walk.

The cross-section for elastic scattering scales roughly as $Z^2 / E^2$ — proportional to the square of the atomic number and inversely proportional to the square of the electron energy. High-Z elements scatter strongly; high-energy electrons scatter weakly. Both relations matter for the shape of the interaction volume.

The second is **inelastic scattering**. The electron interacts with bound electrons in the specimen, transferring energy to ionize or excite them. Kinetic energy is not conserved; some of it goes into changing the internal state of the target atom. Each such collision takes a bite of a few tens to a few hundred electron volts from the incident electron's kinetic energy. After many inelastic events, the beam electron has lost all its energy and stops.

Inelastic scattering is what kills the beam and produces the signals. Secondary electrons appear when a loosely bound specimen electron receives a few eV and escapes the surface. Characteristic X-rays appear when a tightly bound inner-shell electron is ejected and an outer-shell electron drops to fill the vacancy, releasing a photon with an energy that identifies the element. The beam slows down via inelastic scattering; it spreads sideways via elastic scattering. The combined effect is the random walk that produces the teardrop.

The cloud is not a hypothesis. Monte Carlo simulation — named for the casino, because the algorithm uses random numbers to approximate what are in principle deterministic collisions — tracks tens of thousands of simulated trajectories through the solid, each one sampling elastic and inelastic cross-sections at every step. The ensemble of trajectories produces a density map that matches the etched PMMA craters. Two independent measurements of the same physics, agreeing. The cloud is real.

![Monte Carlo trajectory plot showing ~100 electron paths](images/06-beam-specimen-interactions-fig-01.png)
*Figure 6.1 — Monte Carlo trajectory plot showing ~100 electron paths*

## How deep the beam goes

The size of the interaction volume can be estimated without a Monte Carlo run. The most widely used approximation is the **Kanaya–Okayama range**:

$$R_{\text{KO}} \text{ [μm]} = \frac{0.0276 \, A \, E_0^{1.67}}{\rho \, Z^{0.889}}$$

where $E_0$ is the beam energy in keV, $A$ is the atomic weight in g/mol, $\rho$ is the density in g/cm³, and $Z$ is the atomic number. The formula is empirical — fitted to measured ranges — but the exponents encode real physics. The $E_0^{1.67}$ scaling reflects how energy loss per unit path length changes as the electron slows down: the beam spends more and more time per unit length as it decelerates, depositing energy more densely near the end of its range. The $Z^{0.889}$ in the denominator reflects that high-Z materials scatter electrons back sooner, reducing effective penetration.

Work through an example. At 20 keV in copper ($A = 63.55$, $\rho = 8.96$ g/cm³, $Z = 29$):

$$R_{\text{KO}} = \frac{0.0276 \times 63.55 \times 20^{1.67}}{8.96 \times 29^{0.889}} = \frac{0.0276 \times 63.55 \times 142.0}{8.96 \times 19.8} \approx \frac{249}{177} \approx 1.4 \text{ μm}.$$

Textbooks quote 1–2 μm for copper at 20 keV. The estimate is good.

Now drop the voltage to 5 keV. The range scales as $E_0^{1.67}$, so the ratio is $(5/20)^{1.67} = (0.25)^{1.67} \approx 0.10$. The interaction volume shrinks by a factor of ten — from 1.4 μm to about 140 nm. At 1 keV, another factor of roughly eight smaller: tens of nanometers. **kV is the dominant control over interaction volume size.** Nothing else the operator adjusts changes the depth by as much as kV does.

The shape of the cloud changes too. In a low-Z material like carbon or biological tissue, elastic scattering is weak — the beam travels nearly straight down for a while before scattering becomes significant, then eventually spreads. The cloud is a narrow-waisted teardrop: a slim neck near the surface, a wider bulb at depth. In a high-Z material like gold or tungsten, the strong $Z^2$ elastic cross-section bends trajectories immediately, broadening the cloud near the surface. The teardrop becomes a hemisphere. The practical consequence: for surface-sensitive work, high-Z specimens at a given kV are "worse" — the beam spreads sooner, closer to the surface, blurring whatever surface feature you are trying to image.

The mental model I want you to carry: at 20 keV in a metal, you are sampling roughly a micrometer of material. At 5 keV, roughly a hundred nanometers. At 1 keV, tens of nanometers. These are not precise numbers, but they are the right order of magnitude, and they are the numbers you need to check before trusting that your image is telling you what you think it is.

![Interaction volume cross-sections for copper at 1, 5,](images/06-beam-specimen-interactions-fig-02.png)
*Figure 6.2 — Interaction volume cross-sections for copper at 1, 5,*

## Backscattered electrons: the depth signal

A **backscattered electron** is a beam electron that has undergone enough elastic deflections to reverse its net direction and exit the specimen back through the entrance surface. It did not bounce off the surface like a billiard ball — its path inside the solid was tortuous, a long random walk that happened, by accumulation of deflections, to turn around before the electron lost all its energy. Because elastic scattering conserves kinetic energy, BSEs exit with a large fraction of the beam energy: the energy distribution peaks somewhere between $0.7\,E_0$ and $0.9\,E_0$, and BSEs carry enough energy to reach detectors millimeters away without assistance.

The **backscatter coefficient** $\eta = i_{\text{BSE}} / i_B$ — the fraction of beam electrons that backscatter — rises monotonically with atomic number. Carbon ($Z = 6$) gives $\eta \approx 0.05$; gold ($Z = 79$) gives $\eta \approx 0.48$. The relationship is nearly monotonic across the periodic table, which makes it useful: if two phases in a specimen differ in average $Z$, they will differ in $\eta$, and in a BSE image the heavier phase will appear brighter than the lighter phase. This is **atomic number contrast**, or Z-contrast, and it is the BSE image's distinctive contribution to SEM analysis.

The monotonic $\eta$-vs-$Z$ curve is steep at low $Z$ and flattens at high $Z$. Distinguishing carbon from silicon by BSE contrast is easy; distinguishing tantalum from tungsten is hard. And within the SEM voltage range — 5 to 30 keV — $\eta$ depends only weakly on $E_0$. You can change kV to adjust the interaction volume size without scrambling the gray-level scale of your BSE image. That is a useful operational fact: BSE compositional contrast is robust to kV changes, while spatial resolution and depth sampling are not.

![Plot of backscatter coefficient η vs atomic number](images/06-beam-specimen-interactions-fig-03.png)
*Figure 6.3 — Plot of backscatter coefficient η vs atomic number*

BSEs sample a substantial depth of the interaction volume — up to about half the Kanaya–Okayama range in low-Z materials, somewhat less in high-Z materials where the strong elastic cross-section reflects the beam back sooner. At 20 keV in a metal, BSE signal can come from 500 nm below the surface. This is why BSE imaging is the right tool for detecting buried features — inclusions, precipitates, second phases hidden beneath a polished surface — and the wrong tool if you want to know about only the top few nanometers.

## Secondary electrons: the surface signal

A **secondary electron** is defined operationally as a specimen electron with kinetic energy below 50 eV. Most SEs are below 10 eV; the energy distribution peaks at 2–5 eV. These are loosely bound outer-shell electrons that received a small energy transfer in an inelastic collision with the beam, just enough to escape the surface if the collision happened close enough to it.

The key word is *close enough*. A 5 eV electron in a solid loses energy to further inelastic events at an extraordinary rate; after traveling a few nanometers, it has dropped below the work function and can no longer escape. The **escape depth** of a secondary electron is on the order of 2–5 nm in metals, somewhat larger in low-density organic materials. Compare to BSEs, which carry kilo-electron-volts of energy and escape from hundreds of nanometers. SE and BSE sample completely different layers of the same interaction volume.

This surface sensitivity is why SE images look like photographs: the signal is dominated by the geometry of the topmost nanometers of the specimen surface, and the image reads the way a light-and-shadow photograph reads. The SE coefficient $\delta = n_{\text{SE}}/n_B$ rises with specimen tilt — surfaces canted toward the beam emit more SEs because the beam travels through more near-surface material per unit depth — so a raised feature facing the beam looks bright, a slope facing away looks dark, an edge looks brightest of all. The brain interprets this as a three-dimensional surface, and it is nearly right.

There is a subtlety in the SE signal that matters for anyone doing high-resolution work. Not all secondary electrons are equally informative. Three populations are worth distinguishing.

**SE1** electrons are generated directly at the beam impact point, in a footprint comparable to the focused probe diameter. They carry the lateral resolution of the beam. This is the signal you want.

**SE2** electrons are generated where backscattered electrons exit the specimen. Because BSEs can exit over a wide lateral area — hundreds of nanometers from the beam impact point — SE2 is a BSE-modulated signal spread over a much larger footprint than the probe. It blurs the apparent SE resolution and introduces Z-contrast into what looks like a topographic image.

**SE3** electrons are generated where BSEs strike the objective lens polepiece or chamber walls. They have no spatial connection to the beam impact point. They add a roughly uniform background to the image — or, worse, a directional artifact if the geometry is asymmetric.

In a standard Everhart-Thornley detector at 20 kV on a polished metal, SE2 and SE3 together can account for more than half the collected signal. The high-resolution SE1 fraction is buried. Through-the-lens detectors — Chapter 7 — work precisely because the strong magnetic field of an immersion objective captures SE1 and SE2 preferentially while excluding SE3, which lacks enough energy to spiral through the lens field against the voltage gradient. The difference in image quality between a standard E-T image and a TTL image at the same beam conditions can be dramatic, and the physics of why is all in the SE1/SE2/SE3 distinction.

![Cross-section schematic of the interaction volume showing SE1](images/06-beam-specimen-interactions-fig-04.png)
*Figure 6.4 — Cross-section schematic of the interaction volume showing SE1*

One more consequence of SE physics worth carrying: the SE coefficient $\delta$ rises as kV drops. At 1–2 keV, $\delta$ often exceeds 1 for many materials — meaning the specimen emits more electrons than it receives. A non-conducting specimen at this condition actually charges *positively*, not negatively, which self-limits further charging. This is why imaging polymers and biological specimens at around 1.5 kV often eliminates the charging artifacts that plague higher-voltage work, and why this trick works better on insulators than conductors: for insulators, the surface charges until the secondary yield balances the beam current; for conductors, charge dissipates before that balance matters.

## Matching signal to question

The beam enters at a point. Inside the solid, it spreads into a teardrop whose horizontal width at the widest point may be comparable to its depth — or smaller, depending on Z and kV. Different signals exit from different depths of this teardrop:

Auger electrons come from the top 2 nm or less — surface chemistry, rarely used in standard SEM. SE1 from the top few nanometers — high-resolution surface morphology. SE2 from the same thin layer, but emerging over the full BSE footprint — blurred, composition-tinged morphology. BSE from tens to hundreds of nanometers — Z-contrast, buried features. Characteristic X-rays from the full interaction volume — elemental composition, at the cost of the interaction volume's lateral blur.

These are not arbitrary detector labels. They are four different windows onto four different spatial regions of the same teardrop. The question you want to answer determines which window to open.

Want to know the surface topography of a biological cell? SE at low kV — minimize the interaction volume, use a TTL detector if available to isolate SE1, keep kV low enough that the escape depth dominates over the BSE-modulated SE2 contribution. Want to know whether a bright region in a polished alloy is a heavy-element phase or a geometric artifact? BSE — if the brightness is Z-contrast, it survives a stage rotation; if it is geometric, it rotates with the stage. Want to find a tungsten inclusion buried under 300 nm of aluminum matrix? BSE at high kV — the interaction volume must reach the inclusion, and the $\eta$ contrast between W and Al is about 0.4, which is enormous.

The coupling that catches students: changing kV to improve surface sensitivity also changes the SE coefficient, changes the BSE sampling depth, changes the characteristic X-ray excitation range, and potentially changes the charging behavior of the specimen — all at once. There is no knob that changes only one thing. Every operating-condition choice is a trade across the whole signal budget.

The other failure mode worth naming is the one the PMMA experiment illustrates directly: assuming the image is a picture of the surface. A 1 nm probe at 20 keV in a biological specimen produces an interaction volume several micrometers wide and deep. The image you take at that condition is not a surface image. It is a projection through a micrometer of material, averaged laterally over the interaction volume width. If you need the surface — really need the top few nanometers — you need low kV, probably TTL detection, and an awareness that the SE2 contribution is never completely gone.

The interaction volume is not a complication or an artifact. It is the physics. The beam is a point; the signal is a teardrop. Everything else in SEM practice is about deciding which layer of the teardrop answers your question, and then choosing operating conditions that make that layer dominant.

---

## Exercises

### Warm-up

**6.1** Classify each of the following as primarily a product of elastic scattering, inelastic scattering, or both: (a) backscattered electrons, (b) characteristic X-rays, (c) secondary electrons, (d) the trajectory deflection that produces the teardrop shape. Give a one-sentence physical reason for each. *(Tests: elastic vs. inelastic scattering and their respective consequences)*

**6.2** Without computing a number, predict whether the Kanaya–Okayama range is larger in aluminum ($Z=13$, $\rho = 2.70$ g/cm³) or in gold ($Z=79$, $\rho = 19.3$ g/cm³) at the same beam energy. Identify which factor in the formula dominates your prediction — Z or density — and explain why. *(Tests: qualitative reading of the KO formula)*

**6.3** Order the following from shallowest to deepest sampling depth: SE1, BSE, characteristic X-ray, Auger electron. *(Tests: signal depth hierarchy)*

### Application

**6.4** A 10 keV beam strikes a specimen of pure iron ($A = 55.85$, $\rho = 7.87$ g/cm³, $Z = 26$). Calculate the Kanaya–Okayama range. Then predict the range at 20 keV without a full recalculation — use the $E_0^{1.67}$ scaling directly. *(Tests: KO calculation and scaling intuition)*

**6.5** You are imaging a polished alloy cross-section containing an aluminum-rich phase and a nickel-rich phase. At 20 kV with a BSE detector, the Ni-rich phase appears bright. You rotate the specimen stage by 90° and the contrast pattern stays fixed relative to the phase boundaries. What does this confirm, and why would the conclusion be different if the bright region had rotated with the stage? *(Tests: distinguishing Z-contrast from geometric/topographic BSE contrast)*

**6.6** A student wants to image 20 nm silicon dioxide particles on a carbon substrate at the highest possible surface sensitivity. She has a choice of 1 kV, 5 kV, or 20 kV. Which kV should she choose, and why? Name one artifact she should watch for at that kV. *(Tests: kV selection for surface-sensitive SE imaging and associated trade-offs)*

**6.7** A BSE image at 25 kV shows a bright dot embedded in a dark matrix. When the operator drops to 5 kV, the bright dot disappears. Propose an explanation for what the bright dot represents and why it vanishes at low kV. *(Tests: BSE depth sampling and buried-feature detection)*

### Synthesis

**6.8** A materials scientist is characterizing a polished steel sample that contains iron carbide precipitates (~100 nm diameter, $Z_{\text{av}} \approx 16$) embedded in an iron matrix ($Z = 26$). She wants to (a) confirm the precipitate locations, (b) measure whether any precipitates are subsurface, and (c) image the grain boundary structure at the surface. For each goal, specify the signal (SE or BSE), the kV, and explain in one sentence how the interaction-volume physics drives the choice. *(Tests: integrating depth sampling, Z-contrast, and surface sensitivity as a simultaneous design problem)*

**6.9** The SE coefficient $\delta$ for a polymer exceeds 1 at 1.5 kV. Explain why this means the specimen charges positively rather than negatively at that voltage, and why this self-limits further charging. Then explain why the same effect does not help a metallic specimen. *(Tests: SE crossover energy, charging physics, and the role of conductivity — requires connecting SE yield, charge balance, and specimen properties)*

### Challenge

**6.10** You are specifying the imaging conditions for a cryo-SEM experiment on a hydrated biological cell (~90% water by volume, average $Z \approx 7$, density ≈ 1.0 g/cm³). Your goal is to image the cell membrane (thickness ~8 nm) without significant contribution from cytoplasmic content below it. Estimate the Kanaya–Okayama range at 1 kV and at 3 kV for this material. Based on your estimates, propose a kV and justify whether SE or BSE is the appropriate signal. Identify the two most likely artifacts at your chosen condition and propose a mitigation for each. *(Tests: applying KO estimation to a soft-matter low-Z specimen, signal selection, and artifact awareness as a unified imaging design problem)*

---

*What would change my mind:* evidence that the Kanaya–Okayama scaling significantly overestimates or underestimates interaction volume depth for common SEM materials across the 5–30 keV operating range. Modified parameterizations exist and differ by tens of percent in specific cases; a systematic deviation across the full range would revise the mental model here.

*Still puzzling:* the 50 eV cutoff between SE and BSE is operationally useful but physically arbitrary. The energy distribution of inelastically scattered electrons is continuous; the line is a calibration convention, not a physical break. Whether a 48 eV electron is "secondary" or "backscattered" is a matter of definition, not physics.
