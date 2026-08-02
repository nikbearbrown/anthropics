# Chapter 15 — Diffraction and Crystallographic Information in TEM


## TL;DR

- Every crystal is a three-dimensional diffraction grating for electrons — and the TEM lets you read the grating directly, from a region 100 nanometers across, in real time.
- The chapter moves through Why electrons diffract from crystals, Three patterns from three kinds of order, From ring radii to d-spacings, Zone axes and single-crystal patterns, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Every crystal is a three-dimensional diffraction grating for electrons — and the TEM lets you read the grating directly, from a region 100 nanometers across, in real time.*

---

Suppose you have a thin film of titanium dioxide and you want to know whether it is the rutile phase or the anatase phase. The two are chemically identical — same formula, same elements — but structurally distinct, with different crystal symmetries and different properties. An X-ray diffractometer would tell you, given enough material and a few minutes. But suppose the film is only 50 nm thick, deposited on a substrate, and you want to know the phase of a specific 200 nm region, not the average over a millimeter-wide beam.

X-ray diffraction cannot do that. The X-ray beam is too large. SEM cannot do it either — SEM tells you about the surface, not the crystal structure inside. The TEM can, because the TEM lets you insert a small aperture around your 200 nm region, switch the intermediate-lens excitation, and read the diffraction pattern directly off the camera.

What you see when you do this is not the real-space image you had before. The screen transforms: concentric bright rings on a dark background, sharp at the inner radii, dimmer toward the outside. Each ring is a family of lattice planes scattering electrons coherently. The radii of the rings encode the plane spacings. Measure the radii, compute the spacings, compare to published tables: the film is rutile, polycrystalline, with no amorphous component. The identification takes a few minutes. It comes from 200 nm of specimen.

That is the capability this chapter is about.

![Polycrystalline TiO₂ — featureless gray BF image (left) and the SAED ring fingerprint of the same area (right).](../images/15-diffraction-in-tem-fig-01.png)

*Figure 1.* Polycrystalline TiO₂ — featureless gray BF image (left) and the SAED ring fingerprint of the same area (right).


## Why electrons diffract from crystals

The physics is Bragg's law, which was derived for X-rays in 1913 and applies equally to any wave:

$$n\lambda = 2d\sin\theta$$

where $\lambda$ is the wavelength of the incident wave, $d$ is the spacing between adjacent parallel lattice planes, $\theta$ is the angle between the incident wave and those planes, and $n$ is the diffraction order. For first-order diffraction, $n = 1$.

The physical picture: a crystal is a stack of atomic planes with regular spacing $d$. When a wave hits the planes, each plane reflects a fraction of the wave. If the path-length difference between waves reflecting from adjacent planes is exactly one wavelength, the reflections add constructively — you get a diffracted beam. If it is not exactly one wavelength, they cancel. The condition for constructive interference is exactly Bragg's law.

Now put in numbers for TEM at 200 kV. The electron wavelength at that voltage is about 2.5 pm — 0.0025 nm. A typical lattice spacing is something like 0.3 nm. So:

$$\sin\theta = \frac{\lambda}{2d} = \frac{0.0025}{2 \times 0.3} \approx 0.004$$

The diffraction angle $\theta$ is about 0.25 degrees. That is tiny — a fraction of a degree. In X-ray diffraction, Bragg angles run from a few degrees to tens of degrees, and the diffracted beams spread wide. In TEM, the diffracted beams emerge nearly parallel to the direct beam. The entire diffraction pattern at the back focal plane sits within a very small angular range around the optical axis.

This near-parallelism is why electron diffraction patterns look the way they do: the direct beam is a bright spot at the center, and the diffracted spots or rings cluster close to it, separated by distances that scale inversely with the lattice spacings. Small rings mean large spacings; large rings mean small spacings. The pattern is a reciprocal map of the lattice.

## Three patterns from three kinds of order

What you see in the diffraction pattern depends on what kind of crystallinity the specimen has within the selected area.

If the selected area contains a single crystallite oriented so that one specific crystal direction is parallel to the beam, the diffraction pattern is an array of discrete bright **spots** on a dark background. Each spot is one specific set of lattice planes satisfying the Bragg condition. The pattern is the projection of the reciprocal lattice onto the camera plane — a two-dimensional slice through a three-dimensional structure.

The arrangement of spots carries information about the crystal symmetry. When the beam is parallel to a low-index crystallographic direction — called a **zone axis** — the pattern has a recognizable symmetry. Silicon viewed along [001] gives a square array of spots; along [011], a rectangular array; along [111], a hexagonal array. These patterns are recognizable at a glance by anyone who has indexed a few of them. They are the crystallographer's Rosetta stone.

If the selected area contains many small crystallites oriented randomly, no single orientation dominates. Each crystallite produces its own spot pattern, but in a different orientation. Superimpose hundreds of spot patterns at random orientations, and the spots smear into concentric **rings**. A ring of radius $R$ corresponds to the lattice spacing $d$ that satisfies the Bragg condition at that angle. The ring pattern tells you the material is polycrystalline — and the ring radii tell you the d-spacings, and therefore the phase.

If the material has no long-range order — glass, an amorphous polymer, an oxide deposited without annealing — the diffraction signal becomes broad **diffuse halos**. Individual atoms still have characteristic nearest-neighbor distances (atoms cannot overlap), so there is some residual signal at the radii corresponding to those distances. But the sharp rings of a crystalline material are absent. Diffuse halos signal: amorphous.

The three patterns — spots, rings, halos — are as distinct as three different states of matter, because they are.

## From ring radii to d-spacings

The relationship between what you measure on the camera and the actual lattice spacing in the specimen is:

$$R \cdot d = L \cdot \lambda$$

where $R$ is the radius of the ring (or the distance from the center to a spot) measured on the camera screen, $d$ is the lattice spacing in the specimen, $L$ is the **camera length** — the effective distance from the specimen to the camera plane — and $\lambda$ is the electron wavelength.

The camera length is a property of how the projector lenses are set. Typically 50–500 mm for routine selected-area diffraction. It is not a physical distance in the column; it is an effective optical distance, controlled by the intermediate and projector lens excitations, calibrated against a specimen of known d-spacings.

The calibration is the step students most often skip and most often regret. You need to run a standard — polycrystalline gold or aluminum, whose d-spacings are published to high precision — and record the ring radii at the same camera-length setting you will use for your unknowns. Then $L\lambda = R_{\text{standard}} \times d_{\text{standard}}$, and you have the product $L\lambda$ needed to compute d-spacings from every subsequent measurement.

Without calibration, camera length is uncertain enough that d-spacing errors of 5–15% are easy to accumulate — enough to confuse rutile with anatase, or iron oxide with iron carbide.

Worked through for the rutile film: at $L = 200$ mm and $\lambda = 0.00251$ nm, a ring at radius 1.55 mm on the camera gives $d = L\lambda/R = 200 \times 0.00251 / 1.55 = 0.324$ nm. The published rutile (110) spacing is 0.325 nm. The match is within measurement precision. Work through the other rings in the same way and if they all match rutile spacings and none match anatase spacings, the identification is secure. One spacing is not enough — the coincidence is possible with other phases. Three or four spacings all consistent with one phase and inconsistent with others is a solid identification.

## Zone axes and single-crystal patterns

When the selected area contains a single grain large enough to fill the aperture, the diffraction pattern is a spot array. Reading that array — assigning Miller indices to the spots and figuring out which crystal direction is parallel to the beam — is the process called indexing.

The key concept is the zone axis. A zone axis is the crystal direction parallel to the beam. All lattice planes that contain that direction satisfy the zone law: $hu + kv + lw = 0$ for a zone axis $[uvw]$ and plane $(hkl)$. These planes, and only these planes, can scatter electrons in the geometry where the beam is parallel to $[uvw]$.

The practical consequence: when you tilt the specimen to align a zone axis with the beam, the diffraction pattern takes on the symmetry of that zone axis. Cubic crystals along $[001]$ show a square spot pattern with four-fold symmetry. Along $[111]$, a pattern with three-fold or six-fold symmetry. Along $[011]$, a rectangular pattern. The symmetry is immediately recognizable, and identifying the zone axis gives you the crystal's orientation relative to the beam.

Getting to a zone axis requires tilting the specimen with the TEM's double-tilt holder. You start in diffraction mode, watch the spot pattern as you tilt in small increments, and navigate by the rule that spots move in symmetric trajectories around zone axes as you tilt. When the pattern snaps into a recognizable symmetric arrangement, you are on or near a zone axis. Fine-tune by tilting both axes to maximize the symmetry and bring the pattern to its ideal form. Once there, the crystal is aligned for high-resolution imaging — you can switch to imaging mode and see lattice fringes from the planes whose spots you just identified.

The combination is essential for HRTEM work (Chapter 17): you need to know which crystal planes will produce visible fringes before you can interpret the high-resolution image. The diffraction pattern is the map; the HRTEM image is the territory.

## What SAED is good for and where it stops

Selected-area electron diffraction is the right tool for three classes of questions.

The first is **phase identification** of a small region. When you have a 50–200 nm particle, grain, or feature and want to know its crystal phase, SAED gives you d-spacings that you compare to published tables. The spatial selectivity is what sets this apart from bulk X-ray diffraction — you are measuring a single particle, not a powder average.

The second is **orientation determination**. A zone-axis pattern gives the crystal orientation directly. If you need to know whether adjacent grains are misoriented by 5 degrees or 45 degrees — important for understanding grain boundary character and mechanical behavior — SAED spot patterns from each grain give you the answer.

The third is **distinguishing crystalline from amorphous**. A material that looks featureless in bright-field can be shown to be crystalline (sharp rings), nanocrystalline (broad rings), or amorphous (halos) from the diffraction pattern. This is information you cannot extract from the image alone.

Where SAED stops: trace phases below about 10 volume percent. If a secondary phase makes up less than 10% of the selected area, its diffraction signal is too weak to see reliably above background. For trace-phase identification, you need more selective techniques — convergent-beam electron diffraction (CBED) from a focused probe, or energy-filtered diffraction that suppresses inelastic background.

SAED also cannot easily identify amorphous phases chemically. The diffuse halos tell you the material is amorphous; they do not tell you whether it is amorphous silica, amorphous carbon, or amorphous polymer. For that, you need EELS (Chapter 18) or EDS (Chapter 9) alongside the diffraction.

## The pattern in the workflow

A real TEM session on a crystalline specimen uses diffraction and imaging together, iteratively.

You start in bright-field imaging mode and find the region of interest. You insert the selected-area aperture — a physical aperture in the image plane of the objective lens, which limits the beam to the region you want to examine — and center it on the feature. You switch the intermediate lens to diffraction mode. The image disappears; the diffraction pattern appears.

If the pattern shows rings, you are looking at a polycrystalline or nanocrystalline region. Measure the rings; identify the phase. If you want to image only one phase, switch back to imaging mode and tilt the objective aperture onto the ring of interest, blocking all other beams. What you get is a dark-field image showing only the material that scattered into that ring — the spatial distribution of that phase, one crystallographic family at a time.

If the pattern shows spots, you may be on a single grain or a few. Tilt to a zone axis; record the pattern; identify the orientation. Switch back to imaging mode; find the lattice fringes that correspond to the spots you indexed. The fringes confirm the identification and show you where individual atomic planes lie.

If the pattern shows halos, the material is amorphous in this region. That is itself useful information — it distinguishes amorphous from crystalline regions of the same specimen.

The iteration between diffraction and imaging is what makes TEM so information-dense. Other characterization techniques give you one kind of information: XRD gives bulk crystal structure, SEM gives surface morphology, EDS gives elemental composition. TEM gives all of these from the same 100 nm region in one session — image, diffraction pattern, elemental spectrum — and each one is site-specific.

## The numbers that anchor this

The precision of SAED is worth understanding concretely.

At 200 kV, $\lambda = 0.0025$ nm. Camera length 200 mm. Ring radius 1.55 mm. From $d = L\lambda/R$: $d = 200 \times 0.0025 / 1.55 = 0.323$ nm. The rutile (110) spacing is 0.325 nm. The agreement is within 0.002 nm — 2 pm. The diameter of a hydrogen atom is about 0.1 nm; we are measuring lattice spacings to 2% of that.

What limits the precision? Camera-length calibration, primarily. If the calibration is off by 2%, the d-spacing measurement is off by 2%. For most phase identification that is fine — the spacings of different phases differ by at least a few percent, so the ambiguity between rutile and anatase (whose closest spacings differ by about 5–10%) is resolved easily. For distinguishing two phases with nearly identical structures — different polytypes, or phases with similar unit cells — more careful calibration or higher-precision diffraction (CBED) is needed.

The angular precision of zone-axis orientation is about 0.1–0.5 degrees, limited by the tilt accuracy of the stage. This is fine for most HRTEM work, where you need to be within one or two degrees of the zone axis to see clear lattice fringes.

The spatial selectivity of the selected-area aperture is typically 50–500 nm equivalent diameter in the specimen plane, depending on the aperture size and lens settings. For a 200 nm aperture on a specimen with 50 nm grain size, you are averaging over a few grains. For a 50 nm aperture on a specimen with 5 nm grain size, you might be averaging over hundreds. The aperture size is a choice, and it has to match the grain size of the specimen.

---

*What would change my mind:* evidence that SAED can routinely identify trace phases below 5 volume percent in a thin specimen without convergent-beam or energy-filtered methods. Current practice requires roughly 10 volume percent or more before the secondary diffraction signal is reliably distinguishable from background in a conventional SAED pattern.

*Still puzzling:* the transition from SAED pattern recognition to confident phase identification remains more art than algorithm in difficult cases — overlapping phases, strong texture, beam-sensitive specimens that change under the dose required to acquire a clean pattern. Software-based pattern matching helps but does not replace the operator's judgment about which candidate phases are chemically plausible.

