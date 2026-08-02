# Chapter 18 — Electric Charge and Electric Field

*The force that runs chemistry, holds matter together, and is forty orders of magnitude stronger than gravity.*

---

Here is a number worth pausing on: the Coulomb force between the electron and the proton in a hydrogen atom is about $8.2 \times 10^{-8}$ N. The gravitational force between them, at the same distance, is about $3.6 \times 10^{-47}$ N. The ratio is $2.3 \times 10^{39}$ — call it forty orders of magnitude.

Gravity holds planets in orbit and galaxies together. But at the scale of atoms and molecules, gravity is negligible to an almost absurd degree. Everything that chemistry does — every bond, every reaction, every protein folding, every nerve firing, every thought you are having right now — runs on Coulomb forces. The stuff of everyday life is not held together by gravity. It is held together by electric charges.

This chapter introduces the two central ideas: the law governing forces between charges, and the field concept that organizes what those forces do in space.

---

## What charge is

Tear off two strips of scotch tape, stick them to a smooth desk, and peel them off briskly. Bring them near each other. They repel. Press one strip sticky-side-down onto the other and pull them apart. The two strips now attract. Before any peeling: neutral tape. After: the two pieces have different signs of charge, and their sum is still zero. Charge moved from one strip to the other. None was created; none was destroyed.

This 90-second kitchen experiment contains the essential physics: charge comes in two signs (call them positive and negative), like charges repel and unlike charges attract, and the total charge in a closed system doesn't change. Everything else is putting numbers on it.

**Charge is quantized.** The smallest unit of free charge in nature is the elementary charge:

$$e = 1.602 \times 10^{-19} \text{ C},$$

where the coulomb (C) is the SI unit. An electron carries $-e$; a proton carries $+e$. Every observed free charge is an integer multiple of $e$ — you never find, say, $0.3e$ wandering around loose. (Quarks carry fractional charges, but they have never been isolated.)

**Charge is conserved.** In any closed system, the net electric charge doesn't change. You can move charge around, create positive-negative pairs together, or annihilate pairs together, but the total stays fixed. This is one of the most precisely tested laws in physics.

**Charge and matter.** Everything around you contains enormous amounts of charge — roughly $10^{23}$ electrons and protons per mole of material. The reason we don't notice is that ordinary matter is nearly perfectly charge-neutral: positive and negative charges cancel. The slightest imbalance shows up dramatically (a doorknob spark, a lightning bolt). The doorknob spark transfers about $10^{-9}$ C — roughly $6 \times 10^9$ electrons out of $\sim 10^{23}$ in the fingertip, a fractional imbalance of $10^{-14}$.

<!-- → [TABLE: Charge magnitudes for common situations. Columns: situation, charge transferred (C), number of elementary charges. Rows: doorknob spark (10⁻⁹ C, 6×10⁹ e), rubbed balloon (~10⁻⁸ C, ~6×10¹⁰ e), lightning bolt (~15 C, ~10²⁰ e), electron (-1.6×10⁻¹⁹ C, 1 e), proton (+1.6×10⁻¹⁹ C, 1 e). Caption: Charge transfers in everyday electrostatic events span twelve orders of magnitude. All are integer multiples of e.] -->

![Three panels with material types. Conductor (copper): dense sea of mobile electrons. Insulator (rubber): electrons tightly bound; almost no mobile charge. Semiconductor (silicon): few mobile carriers — number tunable by doping...](../images/18-electric-charge-and-electric-field-fig-04.png)
*Figure 18.4 — Conductor, Insulator, Semiconductor — Charge Mobility Hierarchy*

### Conductors and insulators

Whether charge can flow through a material makes an enormous practical difference.

**Conductors** have charges (electrons) that move freely. Metals are the canonical example. Salt water, ionized gases, and biological tissue are also conductors.

**Insulators** have charges bound in place. Glass, rubber, dry wood, plastic. When you charge an insulator by friction, the charge stays where you put it.

Three ways to charge an object: by **friction** (rubbing transfers electrons between materials — the scotch-tape experiment), by **conduction** (a charged object touches a neutral one and charges flow until equilibrium), and by **induction** (a charged object brought near a conductor redistributes the conductor's free charges without touching it; the conductor can be left with a net charge by grounding and disconnecting while the inducing charge is still nearby).

<!-- → [FIGURE: Three-panel diagram showing the three charging methods. Panel 1 (Friction): wool cloth rubbing glass rod, electron transfer arrows from glass to cloth, rod ends up +, cloth ends up -. Panel 2 (Conduction): charged rod (marked +) touching neutral metal sphere, charge flow arrows, sphere ends up + after contact. Panel 3 (Induction): charged rod (marked -) held near metal sphere without touching, charge redistribution shown (+ near rod, - far side), ground wire attached draining - charge, rod removed leaving sphere +. Caption: Three mechanisms for charging objects. Friction transfers electrons between different materials. Conduction shares charge by contact. Induction redistributes existing charge without transfer, leaving an opposite charge after grounding.] -->

---

## Coulomb's law

![Schematic of Coulomb's apparatus: a thin fiber suspends a horizontal rod with a charged ball at one end and a counterweight at the other. A second charged ball is brought close; the repulsive force twists the fiber by an angle...](../images/18-electric-charge-and-electric-field-fig-01.png)
*Figure 18.1 — Coulomb's Torsion Balance (1785) — Twist Measures Inverse-Square Force*

In 1785, Charles Coulomb used a torsion balance in Paris to measure the force between charged spheres as a function of their separation and their charge magnitudes. He found:

$$F = k\frac{|q_1 q_2|}{r^2},$$

where $k = 8.99 \times 10^9 \text{ N·m}^2/\text{C}^2$. The force is along the line joining the charges — repulsive if the charges have the same sign, attractive if opposite.

Coulomb didn't guess the inverse-square form; he measured it. The exponent is now known to be 2 to within one part in $10^{16}$ — among the most precisely tested quantitative claims in all of science.

![Two panels. Left: like charges (+/+) — forces point apart, repulsion. Right: unlike charges (+/−) — forces point toward each other, attraction. Same magnitude F = k|q₁q₂|/r² in both. Newton's third law holds — equal and opposite.](../images/18-electric-charge-and-electric-field-fig-02.png)
*Figure 18.2 — Coulomb's Law Vector Form — Sign of q₁q₂ Sets the Direction*

**Compare to gravity.** Coulomb's law looks exactly like Newton's law of gravitation:

$$F_\text{gravity} = G\frac{m_1 m_2}{r^2}, \quad F_\text{Coulomb} = k\frac{|q_1 q_2|}{r^2}.$$

Same structure: inverse-square distance dependence, proportional to the product of source quantities, with a constant of proportionality. But the scale is completely different. For an electron and proton in hydrogen, the Coulomb force is $\sim 10^{40}$ times larger than the gravitational force. This is why gravity, the force you're most aware of in daily life, plays no role whatsoever in chemistry, and why Coulomb forces, which you're mostly unaware of, run everything at the molecular scale.

<!-- → [TABLE: Coulomb vs. gravity comparison. Rows: force law (F = k|q₁q₂|/r² vs F = Gm₁m₂/r²), constant (k = 8.99×10⁹ N·m²/C² vs G = 6.67×10⁻¹¹ N·m²/kg²), source quantity (electric charge vs mass), signs (two signs: attractive and repulsive vs one sign: always attractive), force between e⁻ and p⁺ in H atom (8.2×10⁻⁸ N vs 3.6×10⁻⁴⁷ N), ratio (F_C/F_G = 2.3×10³⁹). Caption: Coulomb and gravitational forces have identical mathematical structure but differ in strength by 39 orders of magnitude for atomic particles. This is why chemistry runs on electrostatics, not gravity.] -->

The difference also explains why macroscopic objects have to be nearly neutral. If a gram of iron had even a small charge imbalance — say, one extra electron per billion atoms — the repulsive Coulomb force between two such grams one meter apart would be enormous. The universe enforces near-perfect charge balance at macroscopic scales precisely because the slightest imbalance produces forces that quickly restore neutrality.

![Three charges in a triangle: target charge q₀ feels forces from q₁ (close, large) and q₂ (far, small). Vector sum gives the net force. The closer charge dominates because of the inverse-square law.](../images/18-electric-charge-and-electric-field-fig-03.png)
*Figure 18.3 — Three-Charge Superposition — Add Force Vectors, Dominant Pair Wins*

**Superposition.** When multiple charges act on a single charge, the forces add as vectors:

$$\vec{F}_\text{net} = \vec{F}_1 + \vec{F}_2 + \vec{F}_3 + \cdots$$

Each pairwise Coulomb force is computed separately, then added geometrically. Charges don't "block" each other; every pair interacts directly.

**A worked example.** Three charges on the x-axis: $q_1 = +2.0\,\mu\text{C}$ at $x = 0$, $q_2 = -3.0\,\mu\text{C}$ at $x = 0.10$ m, $q_3 = +5.0\,\mu\text{C}$ at $x = 0.30$ m. Net force on $q_2$?

Force from $q_1$ on $q_2$ (separation 0.10 m):

$$F_{12} = (8.99\times10^9)\frac{(2\times10^{-6})(3\times10^{-6})}{(0.10)^2} = 5.39 \text{ N.}$$

The product $q_1 q_2$ is negative (opposite signs), so the force is attractive: $q_2$ is pulled toward $q_1$, in the $-x$ direction. $\vec{F}_{12} = -5.39\hat{x}$ N.

Force from $q_3$ on $q_2$ (separation 0.20 m):

$$F_{23} = (8.99\times10^9)\frac{(3\times10^{-6})(5\times10^{-6})}{(0.20)^2} = 3.37 \text{ N.}$$

Again opposite signs, so attractive: $q_2$ pulled toward $q_3$, in the $+x$ direction. $\vec{F}_{23} = +3.37\hat{x}$ N.

Net: $\vec{F} = (-5.39 + 3.37)\hat{x} = -2.02\hat{x}$ N. About 2 N in the $-x$ direction — dominated by the closer positive charge.

<!-- → [FIGURE: Three point charges on x-axis. q₁ = +2μC at x=0 (red, +), q₂ = -3μC at x=0.10 m (blue, -), q₃ = +5μC at x=0.30 m (red, +). Force arrows on q₂: F₁₂ pointing left (5.39 N), F₂₃ pointing right (3.37 N), F_net pointing left (2.02 N). Distance labels 0.10 m and 0.20 m shown. Caption: Coulomb superposition for three charges. Each pairwise force computed separately, then added as vectors. The sign of each product determines direction; distance squared determines magnitude.] -->

---

## The electric field

Here is a question that seems pedantic but isn't: when charge $q_1$ pushes on charge $q_2$, *how does $q_1$ communicate the push across the gap between them*?

Newton's gravitational law had the same problem. Gravity acts "instantaneously" across empty space — action at a distance — which Newton himself found philosophically troubling but couldn't resolve. For gravity in slow, static situations, the action-at-a-distance picture works fine. For electromagnetic phenomena that change in time — radio waves, light — it fails completely. Maxwell's equations, which we will reach in Chapter 24, describe electric and magnetic fields propagating through space at the speed of light. For that description to work, the field must be a real physical thing, not just a bookkeeping device.

That is what Michael Faraday proposed in the 1830s, working at the Royal Institution in London. Faraday came to physics from a bookbinder's apprenticeship, without the formal mathematics that dominated his contemporaries. What he had was a visual, physical imagination — and he pictured charges not as directly pushing on each other but as *sourcing a field that fills space*, which then acts on any other charge that enters the space.

**Definition.** Place a small positive test charge $q_\text{test}$ at some point. The force it feels is:

$$\vec{F} = q_\text{test}\,\vec{E}.$$

![Linear plot of |E| vs r for a point charge. Field drops as 1/r². Markers at r = 1, 2, 3, 4 show that doubling the distance quarters the field. On log-log axes (inset), slope is −2.](../images/18-electric-charge-and-electric-field-fig-06.png)
*Figure 18.6 — |E| ∝ 1/r² — Field Falls Off Steeply with Distance*

The electric field $\vec{E}$ at that point is defined as $\vec{F}/q_\text{test}$ — force per unit positive charge. Units: N/C, equivalently V/m.

For a single point charge $Q$:

$$\vec{E} = \frac{kQ}{r^2}\hat{r},$$

pointing outward from positive $Q$, inward toward negative $Q$. This is just Coulomb's law divided by the test charge.

For multiple sources, fields superpose vectorially:

$$\vec{E}_\text{total} = \vec{E}_1 + \vec{E}_2 + \cdots$$

**The payoff.** With the field concept, you do the work once — compute $\vec{E}$ at every point in space from the source charges — and then any charge that enters the region feels force $q\vec{E}$ without needing to "know" where all the sources are. For a complex source distribution (a charged protein, an antenna, a thundercloud), this is enormously more tractable than recomputing Coulomb sums for every new test charge.

**A worked example.** Two charges form a dipole: $+q$ at $(0, +a)$ and $-q$ at $(0, -a)$. What is the field at the origin?

From $+q$ (distance $a$, pointing away from $+q$, which is downward at the origin): $E_+ = kq/a^2$, in the $-y$ direction.

From $-q$ (distance $a$, pointing toward $-q$, which is also downward): $E_- = kq/a^2$, in the $-y$ direction.

They add:

$$E_\text{net} = \frac{2kq}{a^2}, \quad \text{in the} -y \text{ direction.}$$

At the midpoint between the two charges, both contributions point the same way and reinforce. This is why the field between the poles of a dipole is strong — and it's the basic geometry of many molecular electric effects.

<!-- → [FIGURE: Dipole geometry. +q at (0, +a) and -q at (0, -a) on y-axis. Point P at origin. Two electric field vectors shown at P: E₊ pointing away from +q (downward, -y direction) and E₋ pointing toward -q (also -y direction). Resultant E_net = 2kq/a² shown in -y direction. Caption: Both field contributions from the dipole point in the same direction at the midpoint. The net field at the midpoint is 2kq/a², directed from + to -.] -->

---

## Field lines: the visual vocabulary

Faraday's greatest contribution may be the *picture* of the field. He literally drew the field lines — curves that, at every point, are tangent to the field vector. Iron filings around a magnet trace these lines. Charge distributions in electrostatics do too. The rules:

Field lines emerge from positive charges and terminate on negative charges. The number of lines emerging from a charge is proportional to its magnitude. Lines never cross (the field has a unique direction at every point). The density of lines — lines per unit perpendicular area — is proportional to the field strength.

<!-- → [FIGURE: Three field-line diagrams side by side. Left: isolated positive charge — lines radiate outward uniformly in all directions. Center: electric dipole (+q left, -q right) — lines curve from + to -, with characteristic hourglass pattern. Right: parallel plates (+ top, - bottom) — uniform parallel lines pointing from + to - in the gap, fringing at edges. Caption: Field lines for the three most important geometries: point charge, dipole, and parallel plates. Line density encodes field strength; direction encodes field direction.] -->

![Three field-line diagrams. Single +q: radial outward lines. Dipole (+/−): lines from + to −, characteristic loops. Two equal +q: lines push apart, null point appears at midpoint (where forces cancel).](../images/18-electric-charge-and-electric-field-fig-05.png)
*Figure 18.5 — Field-Line Atlas — Single Charge, Dipole, Two Equal Charges*

Some key field-line facts. For a single positive charge, the lines radiate outward — more dense near the charge (where $E \propto 1/r^2$ is large), less dense far away. For a dipole, lines curve from positive to negative; the pattern looks like Faraday's iron filings around a bar magnet. For two large parallel plates carrying equal and opposite charge, the field between them is uniform — lines are straight, parallel, equally spaced — with fringing at the edges. This is the geometry of a capacitor.

One more fact, which follows from charge being unable to accumulate in a conductor's interior in equilibrium: **inside a conductor in electrostatic equilibrium, the field is exactly zero.** Any nonzero field would push the free electrons until they redistribute on the surface and cancel the field. The charges arrange themselves on the surface precisely to produce zero net field inside. Consequence: a conducting enclosure shields its interior from external electric fields — the Faraday cage. Cars protect their occupants from lightning not because tires insulate (they don't, at megavolt potentials) but because the conducting metal body routes the charge around the interior, with zero field inside.

<!-- → [FIGURE: Faraday cage diagram. Rectangular conducting enclosure with external electric field lines shown (parallel arrows) approaching from outside. Field lines bend around and along the conductor surface. Inside the enclosure: no field lines — empty, labeled E = 0. Surface charge distribution shown (+ and - labels on conductor surfaces facing field). Caption: A conducting enclosure in an external field develops surface charges that exactly cancel the external field inside. The interior is shielded. This is the Faraday cage effect.] -->

---

## The structure of the chapter's physics

Putting it together: charges source fields ($\vec{E} = kq/r^2$ for a point charge), fields exert forces on charges ($\vec{F} = q\vec{E}$), and superposition lets you add contributions from many sources.

The conceptual arc: we started with direct action at a distance (Coulomb's law, force between two specific charges), then introduced the field as an intermediate — the source charge creates a field, the field tells other charges what to do. For static problems the two pictures give identical numbers. For dynamic problems — changing currents, propagating radiation — only the field picture works. We'll need it fully in Chapter 24.

The scale claim bears repeating. The Coulomb constant $k \approx 9 \times 10^9$ and the gravitational constant $G \approx 6.7 \times 10^{-11}$: these differ by twenty orders of magnitude in SI units, and when you account for the difference in source quantities (kilograms vs. coulombs), the force ratio for electron-proton reaches $10^{39}$. The universe gives us gravity to organize large aggregates of neutral matter, and electrostatics to organize everything inside the matter. Same inverse-square structure. Forty orders of magnitude apart in strength.

---

## Exercises

### Warm-up

**18.1** *(LO 1)* How many electrons are in 1 nC of charge? In 1 mC?

**18.2** *(LO 3)* Two $+2.0\,\mu\text{C}$ charges are 5 cm apart. Magnitude of the Coulomb force?

**18.3** *(LO 5)* Electric field magnitude at 10 cm from a $+5.0\,\mu\text{C}$ point charge?

**18.4** *(LO 5)* A $+1.0\times10^{-6}$ C test charge sits where the field is 300 N/C in the $+y$ direction. Force on it?

### Application

**18.5** *(LO 3, 4)* Charges $+3\,\mu\text{C}$ at $x=0$ and $-2\,\mu\text{C}$ at $x=0.20$ m. Net force on $+1\,\mu\text{C}$ placed at $x=0.10$ m?

**18.6** *(LO 5, 6)* Charges $+q$ at $(0, +a)$ and $-q$ at $(0, -a)$. (a) Field at the origin. (b) Field at $(d, 0)$ for $d \gg a$. (c) Sketch the field lines.

**18.7** *(LO 2)* Describe what happens when a charged glass rod is brought near (not touching) a long metal rod on an insulating stand. Use the words *induction*, *polarization*, *grounding*, and *charge separation*.

**18.8** *(LO 3)* Compute the ratio of the Coulomb to gravitational force between an electron and proton at the Bohr radius ($5.29\times10^{-11}$ m).

### Synthesis

**18.9** *(LO 3, 5)* Field inside a parallel-plate capacitor is 1000 N/C. Force on an electron. If the electron starts at rest, its acceleration?

**18.10** *(LO 4, 5)* Three identical charges $+q$ at the corners of an equilateral triangle of side $a$. Net force on one of them, in terms of $k, q, a$?

**18.11** *(LO 6)* Without math, explain why the field inside a hollow charged conducting sphere is zero, but outside is the same as if all charge were at the center.

### Challenge

**18.12** *(beyond chapter)* Estimate the Coulomb force per base pair in DNA, given adjacent base-pair separation ~0.34 nm and each phosphate carrying charge $-e$. Compare to typical chemical bond strengths (~10⁻⁹ N).

**18.13** *(beyond chapter)* If charge were continuous rather than quantized, describe one observable physical phenomenon that would be different. Defend your answer.

---

## LLM Exercise — Chapter 18: Electric Charge in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** Identification of one electrical or electrostatic component of your anchor phenomenon, with computed charge, force, or field.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 18 (Electric Charge and Field), I want to identify ONE electrostatic component of my phenomenon.

Please:

1. Identify the electrostatic element. Examples:
   - Bike commute: static buildup on the bike frame from rolling friction; static shock when touching a metal door after walking inside.
   - Coffee maker: the ions in tap water that conduct current.
   - Marathon: the ions across a runner's neuron membrane (action potential).
   - Espresso machine: static cling between coffee grounds and grinder.
   - Basketball: triboelectric charging when the ball strikes the court.

2. Estimate the charges involved (in coulombs or in number of elementary charges).

3. If two charges interact, compute the Coulomb force using F = kq₁q₂/r².

4. If a region has a known field, compute the force on a test charge.

5. State your input numbers and uncertainty.

6. Sanity check by comparing to a published number (e.g., typical static-discharge voltages, neuron action potential ~70 mV).

7. Connect to Chapter 19 (Electric Potential), where we'll add energy to this picture.

Save the output as logbook/chapter-18-electric-charge.md.
```

### What this produces

Your eighteenth Logbook entry — an electrostatic component computed quantitatively.

### How to adapt this prompt

- *For phenomena with no obvious electrical element*: every solid object has billions of charges held in place by Coulomb forces — use this to estimate, e.g., the force holding a small piece of your phenomenon together.
- *For Claude Code:* Compute Coulomb sums for a small lattice (say, 10×10 grid of alternating charges) and watch for cancellations.

### Connection to previous chapters

Builds on Chapters 4 (Newton's laws) and 6 (gravitational inverse-square law) by introducing a structurally similar electric force.

### Preview of next chapter

Chapter 19 introduces electric potential and the energy stored in electric fields. The Chapter 19 LLM Exercise will compute energies and voltages for the same component you analyzed here.

---

**Tags:** electric-charge, Coulomb-law, electric-field, electrostatics, conductors-insulators
