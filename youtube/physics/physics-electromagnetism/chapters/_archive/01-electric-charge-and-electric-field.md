# Chapter 1 — Electric Charge and Electric Field

**Suggested titles**

1. Electric Charge and Electric Field
2. Coulomb, Faraday, and the Geometry of Electric Force
3. Why Two Electrons Repel Across a Vacuum

**TL;DR.** Electric charge is a fundamental property of matter, conserved and quantized in units of the elementary charge $e = 1.602 \times 10^{-19}$ C. Two charges interact via Coulomb's law $F = kq_1q_2/r^2$ — the same inverse-square structure as gravity, but with a force constant about $10^{40}$ times stronger. To organize many-charge problems, we replace forces with **fields**: a charge creates an electric field $\vec{E}$ in space, and another charge feels force $\vec{F} = q\vec{E}$. By the end of this chapter you can compute forces and fields for any small assembly of point charges and reason qualitatively about field lines and conductors.

---

## A 1752 Pennsylvania thunderstorm and a kite string

In June 1752, in or near Philadelphia, Benjamin Franklin flew a kite into a thunderstorm. The story has been simplified, dramatized, and probably partly invented, but the experimental claim is real: Franklin connected lightning to static electricity, the same phenomenon that produces a small spark when you walk across a wool carpet and touch a doorknob. He did this by observing that the wet hemp string of his kite, with a metal key tied to its lower end, drew small sparks to his knuckle when storm clouds passed overhead.

The dangerous part is real too. A Russian scientist named Georg Wilhelm Richmann, attempting to replicate Franklin's experiment in St. Petersburg in 1753, was killed by a direct lightning strike through his apparatus. Richmann is the only person known to have died doing physics in this particular way, and the historical lesson is that taking lightning seriously matters.

What Franklin established — *that lightning and static electricity are the same physical phenomenon at vastly different scales* — was the connection that launched modern electrostatics. The amber-rubbed-with-fur attraction known to the ancient Greeks (the word *electric* comes from the Greek *elektron*, meaning amber) and the Megavolt discharge between cloud and ground were now one subject. It would take Charles Augustin de Coulomb, in 1785, to put the inverse-square law on the force between charges, and it would take Michael Faraday, in the 1830s, to invent the concept of the *field* that lets us reason about charges that do not touch. This chapter walks through that arc.

**Learning objectives.** By the end of this chapter you should be able to:

1. State the conservation of charge, the quantization of charge ($e = 1.602 \times 10^{-19}$ C), and the two signs.
2. Distinguish conductors from insulators and explain charging by friction, conduction, and induction.
3. State and apply Coulomb's law: $F = k|q_1q_2|/r^2$ with $k = 8.99 \times 10^9$ N·m²/C².
4. Compute the net Coulomb force on a charge from multiple other charges using vector superposition.
5. Compute the electric field of a point charge: $E = kq/r^2$, and compute the force on a test charge from a known field: $F = qE$.
6. Draw qualitatively correct electric field lines for a single point charge, a dipole, and parallel plate configurations.

**Prerequisites.** Chapter 4 (Newton's laws, vectors), Chapter 6 (gravitational inverse-square law for analogy). Algebra and basic vector arithmetic.

**Why this chapter matters.** Almost every technology in your life — phones, cars, lights, computers, MRI machines, electric motors — runs on electrical phenomena governed by what you learn here. The chemistry of the cell membrane, the molecular structure of DNA, and the binding of every atom in your body all rely on Coulomb forces between charges. This is the foundation chapter for everything in chapters 19–24.

---

## Concept 1 — Charge: signs, quantization, conservation

### A scotch tape experiment, 90 seconds

Tear off two strips of clear scotch tape about 30 cm long. Stick them firmly to a smooth desk surface, then peel them off briskly. Bring them near each other (held by their non-sticky ends). They repel — visibly springing apart. This is static electricity, manufactured in your kitchen. Both pieces of tape acquired the same kind of charge when peeled, and like charges repel.

Now stick one strip on top of the other (sticky-to-paper-side) and pull the pair apart. The two strips, separated, attract — opposite charges. The peeling process transferred charge from one strip to the other. Total charge before peeling: zero. Total charge after: zero (one strip positive, one negative). Charge isn't created or destroyed; it's redistributed.

This is the entire conceptual content of charge in 90 seconds and one piece of tape. Two signs. Like repels like. Total charge is conserved. The rest of the chapter is putting numbers on it.

### The mechanism — what charge is

**Electric charge** is a fundamental property of matter, like mass. It comes in two signs that Franklin (somewhat arbitrarily) labeled positive and negative. Like charges repel; opposite charges attract.

Charge is **quantized**: the smallest free charge in nature is the elementary charge

$$e = 1.602 \times 10^{-19} \text{ C},$$

where the SI unit of charge is the **coulomb** (C). An electron carries charge $-e$; a proton carries $+e$; a neutron carries 0. Every observed free charge is an integer multiple of $e$. (Quarks carry fractional charges, $\pm e/3$ and $\pm 2e/3$, but they are confined inside hadrons and have never been isolated.)

A coulomb is a *lot* of charge. One coulomb of separated electrons would contain $1/e \approx 6.24 \times 10^{18}$ of them. A typical static-charged object — a comb after running through dry hair, a balloon rubbed on a sweater — carries on the order of $10^{-9}$ C (a nanocoulomb). A lightning bolt transfers roughly 15 C in milliseconds, which is why it does so much damage.

Charge is **conserved**: in any closed system, the total electric charge does not change. A charge can be moved from one place to another (the scotch-tape experiment); a positive-negative pair can be created together (electron-positron pair production in high-energy physics); positive-negative pairs can annihilate. But the *net* charge is fixed.

### Conductors and insulators

The classification matters because it determines how charges move:

**Conductors** are materials with charges (typically electrons) that can move freely. Metals are the canonical examples — copper, silver, aluminum. Salt water, ionized gases, and human tissue (mostly water with dissolved ions) are also conductors.

**Insulators** are materials in which charges are bound and cannot move freely. Glass, plastic, dry wood, dry air, rubber, ceramics. When you charge an insulator (by friction), the charge stays where you put it.

**Semiconductors** sit in between (silicon, germanium); their conductivity can be controlled by doping. The whole digital revolution rests on this controllability — but we will save semiconductors for a later course.

There are three basic ways to charge an object:

**Friction** (triboelectric): rubbing two materials transfers electrons from one to the other. The scotch-tape experiment is friction.

**Conduction** (contact): a charged object touches a neutral one; charges flow until they reach equilibrium.

**Induction** (no contact): a charged object brought near a conductor causes the conductor's free charges to redistribute. If you ground the conductor while the charged object is near, free charges flow to or from ground; remove the ground and then the inducing object, and the conductor is left with a net charge of opposite sign.

### The trade-off

Defining charge as a fundamental property of matter trades **deeper explanation for predictive simplicity.** We do not, in this chapter, ask *why* there are charges or *why* there are exactly two signs. We accept their existence and observed behavior, then derive consequences. The "what is charge?" question, like "what is mass?", is genuinely open at the deepest level — quantum field theory has answers, but they are postgraduate.

### Worked example — how many electrons in a static-electric spark?

A typical doorknob spark transfers about 1 nC of charge. How many electrons is that?

$$N = \frac{Q}{e} = \frac{10^{-9}}{1.602 \times 10^{-19}} \approx 6.2 \times 10^9.$$

About 6 billion electrons. From a sample of $\sim 10^{23}$ atoms in your fingertip, that is $\sim 10^{-13}$ — a tiny fraction. We are aware of static electricity through the spark and the small shock, but the underlying redistribution is barely perceptible at the atomic level.

### Common misconceptions

- *"A charged object is one with extra positive charges."* It might have extra positive charges (deficit of electrons) or extra negative charges (surplus electrons). The sign tells you which.
- *"Insulators don't have charge."* They are full of charges — every atom has electrons and a nucleus. Insulators just don't allow the charges to *move*.
- *"Charging by induction means the inducing object loses charge."* No — induction redistributes the conductor's existing charges. The inducing object is unchanged.

↳ **Dig Deeper — Why is charge quantized?**

*The quantization of charge is one of the deepest empirical facts in physics. Every observed free charge is an integer multiple of $e$. There is no theoretical proof that this must be true — quantum electrodynamics is consistent with charge taking continuous values — but Dirac noted in 1931 that the existence of even a single magnetic monopole anywhere in the universe would force charge quantization. None has been observed. The fact remains an unexplained empirical regularity at the deepest level.*

**Prompt:**
> Explain Dirac's 1931 argument that the existence of a single magnetic monopole would imply quantization of electric charge. Walk me through the angular momentum quantization condition for a charge orbiting a monopole, and show how requiring this to be a half-integer multiple of $\hbar$ forces $eg = n\hbar c/2$. End with one sentence on why no monopole has been observed despite extensive searches, and what that means for our understanding of why electric charge is nevertheless quantized.

**What to do with the output:** Save it. The Dirac monopole argument is one of the most elegant results in theoretical physics and it returns when you study quantum mechanics formally.

---

## Concept 2 — Coulomb's law

### Charles Coulomb's torsion balance, 1785

In 1785, Charles Augustin de Coulomb built a delicate apparatus in Paris: a horizontal bar suspended by a thin silver wire, with a small charged sphere on one end. He brought another charged sphere near it, observed how much the suspended bar twisted, and used the wire's known torsional spring constant to back out the force on the sphere.

By varying the distance between the spheres and the magnitudes of their charges (which he calibrated by touching neutral spheres of the same size to the original — by symmetry, charge would split equally), Coulomb established that the electrostatic force between two point charges $q_1$ and $q_2$, separated by distance $r$, has magnitude

$$F = k \frac{|q_1 q_2|}{r^2},$$

where $k = 8.99 \times 10^9 \text{ N} \cdot \text{m}^2/\text{C}^2$ is the **Coulomb constant**. The force is along the line joining the charges, repulsive if the charges have the same sign, attractive if opposite.

Coulomb did not just guess the inverse-square form. He measured it. The exponent is now known to be 2 to within experimental uncertainty of about one part in $10^{16}$ — one of the most precisely tested mathematical claims in physics.

### The mechanism — Coulomb in detail

Coulomb's law is the electrostatic analog of Newton's law of gravity. Both have:

- An inverse-square dependence on distance.
- A force proportional to the product of two scalar source quantities (mass for gravity, charge for electrostatics).
- A prefactor constant of nature.

But the differences are dramatic. Gravity is always attractive; Coulomb has both signs. The Coulomb constant $k$ is enormous compared to the gravitational constant $G$ when scaled by the relevant source quantities. To see how big the difference is, compare the Coulomb and gravitational forces between an electron and a proton in a hydrogen atom (separated by the Bohr radius, $r = 5.29 \times 10^{-11}$ m):

**Coulomb:** $F_C = k e^2/r^2 = (8.99 \times 10^9)(1.602 \times 10^{-19})^2 / (5.29 \times 10^{-11})^2 \approx 8.24 \times 10^{-8}$ N.

**Gravity:** $F_G = G m_e m_p / r^2 = (6.67 \times 10^{-11})(9.11 \times 10^{-31})(1.67 \times 10^{-27})/(5.29 \times 10^{-11})^2 \approx 3.61 \times 10^{-47}$ N.

Ratio: $F_C / F_G \approx 2.3 \times 10^{39}$. Electrostatic force is forty orders of magnitude stronger than gravity at atomic scales. This is why chemistry runs on electrostatics and not gravity, why every solid object you touch resists compression by Coulomb forces between molecular electrons, and why gravity needs *enormous* aggregate mass (a planet, a star) to be noticeable while electrostatics shows up between two strips of scotch tape.

### Vector form and superposition

Coulomb's law is fundamentally a vector law. The force on charge $q_1$ from charge $q_2$ is

$$\vec{F}_{12} = k \frac{q_1 q_2}{r^2} \hat{r}_{12},$$

where $\hat{r}_{12}$ is the unit vector from $q_2$ to $q_1$. The sign of the product $q_1 q_2$ encodes whether the force is attractive or repulsive: positive product means same-sign charges, force points away from the other charge (repulsive); negative product means opposite signs, force points toward the other charge (attractive).

For multiple charges, the **principle of superposition** says: the total force on a charge equals the vector sum of the Coulomb forces from every other charge taken pairwise. This is a strong claim — it means Coulomb interactions don't "interfere" with each other in the sense waves do. It has been tested rigorously and never failed.

### The trade-off

Coulomb's law trades **simplicity for the assumption of point charges and electrostatic equilibrium.** The formula is exact for point charges or spherically symmetric charge distributions in equilibrium. For extended distributions and time-varying situations, you need integration or full Maxwell's equations (Chapter 24). For introductory problems, Coulomb's law for point charges is the workhorse.

### Worked example — three charges in a row

Three point charges sit on the x-axis: $q_1 = +2.0 \mu \text{C}$ at $x = 0$, $q_2 = -3.0 \mu \text{C}$ at $x = 0.10$ m, $q_3 = +5.0 \mu \text{C}$ at $x = 0.30$ m. What is the net force on $q_2$?

**Reasoning.** Force on $q_2$ from $q_1$ (separated by 0.10 m):

$$F_{12} = k \frac{|q_1 q_2|}{r_{12}^2} = (8.99 \times 10^9) \frac{(2 \times 10^{-6})(3 \times 10^{-6})}{(0.10)^2} = 5.39 \text{ N}.$$

The product $q_1 q_2 < 0$, so the force is attractive — $q_2$ is pulled *toward* $q_1$, i.e., in the $-x$ direction. So $\vec{F}_{12} = -5.39 \hat{x}$ N.

Force on $q_2$ from $q_3$ (separated by 0.20 m):

$$F_{23} = (8.99 \times 10^9) \frac{(3 \times 10^{-6})(5 \times 10^{-6})}{(0.20)^2} = 3.37 \text{ N}.$$

Again $q_2 q_3 < 0$, so attractive — $q_2$ is pulled toward $q_3$, in the $+x$ direction. So $\vec{F}_{23} = +3.37 \hat{x}$ N.

Superposition:

$$\vec{F}_\text{net} = \vec{F}_{12} + \vec{F}_{23} = (-5.39 + 3.37) \hat{x} = -2.02 \hat{x} \text{ N}.$$

About 2 N in the $-x$ direction. The negative charge $q_2$ is pulled net leftward, dominated by the closer positive charge $q_1$.

### Common misconceptions

- *"Coulomb's law works for any charge distribution."* It works exactly only for point charges. For extended distributions, you integrate over Coulomb's law.
- *"The force is the same on both charges."* By Newton's third law, yes — equal magnitude, opposite direction. But the *acceleration* depends on each charge's mass.
- *"Charges affect each other instantly."* No — electromagnetic effects propagate at the speed of light. For introductory electrostatics we treat the propagation as instantaneous, but Chapter 24 will correct this.

↳ **Dig Deeper — Why the inverse-square law and not some other power**

*Coulomb's $1/r^2$ law is one of the most precisely tested forms in physics — the exponent is known to be 2 to within $10^{-16}$. The $1/r^2$ form is not arbitrary; it follows from the geometric fact that field lines from a point source spread out over a sphere of area $4\pi r^2$. Any deviation from $1/r^2$ would mean photons have nonzero rest mass — and the experimental upper bound on photon mass comes from precisely these tests of Coulomb's law.*

**Prompt:**
> Walk me through why the inverse-square dependence in Coulomb's law (and Newton's gravity) follows from the geometry of three-dimensional space — specifically, that field lines from a point source spread over a sphere of area $4\pi r^2$. Then explain how Cavendish, Maxwell, and modern experiments have tested the exponent for any deviation from 2 (Cavendish: $\pm 0.02$; Maxwell: $\pm 5 \times 10^{-5}$; modern: $\pm 10^{-16}$). End with one sentence on what a deviation from $1/r^2$ would imply about photon mass.

**What to do with the output:** Save it. The geometric argument for inverse-square laws applies to gravity, electrostatics, light intensity, and sound intensity — all of which spread spherically.

---

## Concept 3 — The electric field

### Faraday at the Royal Institution, 1830s

In the 1830s at the Royal Institution in London, Michael Faraday — bookbinder's apprentice turned the most important experimental physicist of his century — was sprinkling iron filings around bar magnets and watching them organize themselves into curving lines. He was working out the visual representation of magnetic fields, but the *idea* he developed became the central organizing concept for all of electromagnetism: *the field*.

A field, in Faraday's conception, is a property of space itself. Around a charged object, every point in space has an electric field — a vector telling you what force a unit positive test charge would feel if you put it there. The charge sources the field. The field tells other charges what to do.

This sounds like a relabeling, but it isn't. It is a profound reorganization. Instead of "every charge directly affects every other charge through action at a distance," the new picture is "every charge sources a field that fills space, and any other charge feels the local field where it sits." For static problems the two pictures give identical answers. For dynamic problems — radio, light, antennas — the field picture is the *only* one that works, because fields propagate at finite speed and carry energy and momentum on their own.

### The mechanism — defining the electric field

The **electric field** $\vec{E}$ at a point is defined operationally: place a small positive test charge $q$ at the point; the force it feels is $\vec{F} = q\vec{E}$. The field has units N/C (newtons per coulomb), or equivalently V/m (volts per meter, used more commonly).

For a single point charge $Q$ at the origin, the field at distance $r$ is

$$\vec{E} = \frac{kQ}{r^2} \hat{r},$$

pointing outward if $Q > 0$ and inward if $Q < 0$. Notice this is just Coulomb's law per unit test charge: divide $\vec{F} = kQq/r^2 \hat{r}$ by $q$ and you get $\vec{E}$.

For multiple sources, fields superpose vectorially:

$$\vec{E}_\text{total} = \vec{E}_1 + \vec{E}_2 + \vec{E}_3 + \dots$$

Then the force on a charge $q$ at that point is $\vec{F} = q\vec{E}_\text{total}$.

### Electric field lines

Field lines are a visual tool. Rules:

1. Lines start on positive charges, end on negative charges.
2. The number of lines emerging from a charge is proportional to the magnitude of the charge.
3. Lines never cross (the field has a unique direction at every point).
4. The density of lines (lines per unit perpendicular area) is proportional to the field strength.
5. Lines are perpendicular to conductor surfaces in equilibrium (because charges in a conductor would otherwise rearrange).

For a single positive point charge, lines radiate outward in all directions. For a single negative charge, they converge inward. For a *dipole* (positive and negative charge separated), lines curve from positive to negative — the famous bar-magnet-like pattern Faraday's iron filings traced. For two *parallel plates* of opposite charge, lines run uniformly straight from positive to negative plate (this is the geometry of a capacitor, Chapter 19).

### The trade-off

The field concept trades **conceptual abstraction for computational and physical power.** A field is harder to picture than a force between two specific charges, but it lets you reason about systems with many charges, lets you see how electromagnetism propagates in space, and turns out to carry real energy and momentum (a fact you will use in Chapter 24). The cost: you have to learn to think about properties of empty space.

### Worked example — field at the midpoint of a dipole

Two charges sit on the x-axis: $+q$ at $x = -a$, $-q$ at $x = +a$. What is the electric field at the midpoint $x = 0$?

**Reasoning.** At $x = 0$, the field from $+q$ points in the $+x$ direction (away from $+q$). Magnitude: $E_+ = kq/a^2$.

The field from $-q$ also points in the $+x$ direction (toward the negative charge). Magnitude: $E_- = kq/a^2$.

The two add:

$$E_\text{net} = E_+ + E_- = \frac{2kq}{a^2}, \quad \text{in the } +x \text{ direction}.$$

At the midpoint, the contributions reinforce. Off-axis, they don't, and the dipole field is more complex (and is the famous "field lines from positive looping to negative" pattern).

### Common misconceptions

- *"A field requires a charge to detect it."* The field exists regardless. The detector charge is just how we measure it. Gravity has the same character.
- *"Electric field lines are physical things you could touch."* They are a visualization tool. The field itself is a vector at every point in space — continuous, not made of discrete lines.
- *"The field of multiple charges is the average of the individual fields."* No — the *vector sum*. For two equal and opposite charges symmetrically placed, the average is zero, but the actual field is not zero everywhere.

↳ **Dig Deeper — Conductors in equilibrium and the electric field inside**

*A subtle and powerful fact: in electrostatic equilibrium, the electric field inside a conductor is zero. This isn't a postulate — it follows from the fact that any nonzero field would push the conductor's free electrons until equilibrium was restored. The consequence is the Faraday cage: a conducting enclosure shields its interior from external electric fields.*

**Prompt:**
> Walk me through why the electric field inside a conductor in electrostatic equilibrium must be zero. Use the argument that any nonzero internal field would accelerate free electrons until they redistribute on the surface to cancel the field. Then explain the Faraday cage effect: an external static field is canceled inside a conducting enclosure by induced surface charges. Cite one practical example (cars during lightning strikes, sensitive electronics inside metal enclosures, MRI rooms) and explain why the cage works for static fields but only partially for time-varying ones. End with one sentence on what changes when fields oscillate at very high frequencies.

**What to do with the output:** Save it. Faraday cage logic underlies practical electromagnetic shielding everywhere in engineering.

---

## Synthesis — charges, force, field

Step back. Three concepts:

1. **Charge.** Fundamental property of matter, two signs, conserved, quantized in units of $e$.

2. **Coulomb's law.** $F = kq_1q_2/r^2$ along the line between point charges. Inverse-square, like gravity, but vastly stronger at atomic scales.

3. **Electric field.** $\vec{E} = \vec{F}/q$, sourced by charges, fills space, lets us reason about many-charge systems and (eventually) about radiation.

The architecture: charges create fields; fields exert forces on other charges. The field carries the information about the source's location and magnitude through space.

### A worked example combining all three concepts — a chloride ion in saltwater

A Cl⁻ ion in 1 M NaCl solution is surrounded by Na⁺ and Cl⁻ ions in the surrounding water. Why doesn't the chloride ion fly off into space, and what holds it in place?

**Charge.** Cl⁻ carries charge $-e = -1.602 \times 10^{-19}$ C. Surrounding water molecules are polar — neutral overall but with a dipole structure (slightly positive H side, slightly negative O side).

**Coulomb force from one nearby Na⁺.** A Na⁺ ion at distance $r = 0.5$ nm $= 5 \times 10^{-10}$ m exerts attractive force

$$F = k \frac{e^2}{r^2} = (8.99 \times 10^9) \frac{(1.602 \times 10^{-19})^2}{(5 \times 10^{-10})^2} \approx 9.2 \times 10^{-10} \text{ N}.$$

**Field perspective.** The Cl⁻ feels the *vector sum* of the fields from every nearby Na⁺ and Cl⁻ ion. In equilibrium, the time-averaged field is roughly zero (the Cl⁻ is surrounded by oppositely charged Na⁺ ions, balanced by other Cl⁻ ions further away). The water molecules' dipoles align around the ion to *screen* its charge — a phenomenon called solvation, central to all biological chemistry.

**Scale shift.** The same Coulomb forces, scaled up to $10^{23}$ ions, produce the macroscopic conductivity of salt water (Chapter 20), the electrochemistry that runs every battery (Chapter 19), and the membrane potentials that fire neurons in your brain.

The chemistry of life is electrostatics. Once you have Coulomb's law and the field concept, you have the foundation for biochemistry, electronics, and electromagnetic radiation in one stroke.

---

## Exercises

### Warm-up

**18.1** *(LO 1)* How many electrons are in 1 nC of charge? In 1 mC of charge?

**18.2** *(LO 3)* Two point charges, each $+2.0 \mu \text{C}$, are 5 cm apart. What is the magnitude of the Coulomb force between them?

**18.3** *(LO 5)* What is the magnitude of the electric field at distance 10 cm from a point charge of $+5.0 \mu \text{C}$?

**18.4** *(LO 5)* A test charge of $+1.0 \times 10^{-6}$ C is placed at a point where the electric field is $300$ N/C in the $+y$ direction. What force does it feel?

### Application

**18.5** *(LO 3, 4)* Two charges, $+3 \mu\text{C}$ at $x = 0$ and $-2 \mu\text{C}$ at $x = 0.20$ m, lie on the x-axis. Compute the net force on a third charge $+1 \mu\text{C}$ placed at $x = 0.10$ m.

**18.6** *(LO 5, 6)* Two charges, $+q$ and $-q$, are placed at $(0, +a)$ and $(0, -a)$. (a) Find the electric field at the origin. (b) Find the electric field at $(d, 0)$ for $d \gg a$. (c) Sketch the field lines.

**18.7** *(LO 2)* Describe in detail what happens when a charged glass rod is brought near (but not touching) one end of a long metal rod resting on an insulating stand. Use the words *induction*, *polarization*, *grounding*, and *charge separation*.

**18.8** *(LO 3)* Compare the electrostatic force between an electron and a proton at the Bohr radius ($5.29 \times 10^{-11}$ m) to the gravitational force between them. Express the ratio.

### Synthesis

**18.9** *(LO 3, 5)* The electric field inside a parallel-plate capacitor (which we will study formally in Chapter 19) is approximately uniform. If the field strength is $1000$ N/C, compute the force on an electron in the field. If the electron starts at rest, what is its acceleration?

**18.10** *(LO 4, 5)* Three identical charges $+q$ sit at the corners of an equilateral triangle of side $a$. Compute the net force on one of them. Express the result in terms of $k, q, a$.

**18.11** *(LO 6)* Without doing math, explain why the electric field inside a hollow charged conducting sphere is zero, but the field outside is the same as if all the charge were concentrated at the center. (You can quote the result; the proof is in your textbook.)

### Challenge

**18.12** *(beyond chapter)* The DNA double helix is held together largely by the Coulomb attraction between the negatively charged phosphate groups on opposite strands and the positive ions in solution that bridge them. Estimate the Coulomb force per base pair, given that adjacent bases are about 0.34 nm apart and each phosphate carries charge $-e$. Compare this to typical bond strengths in chemistry (~10⁻⁹ N).

**18.13** *(beyond chapter)* If charge were continuous rather than quantized (i.e., if we could have any tiny fractional value of $e$), describe one observable physical phenomenon that would be different. Defend your answer.

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

3. If two charges interact, compute the Coulomb force using $F = kq_1q_2/r^2$.

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

## Chapter summary

Charge is a fundamental property of matter, conserved and quantized. Coulomb's law gives the force between point charges, and the electric field organizes the description of many-charge systems. Three commitments:

1. **Charge has two signs, is conserved, and is quantized** in units of $e = 1.602 \times 10^{-19}$ C.

2. **Coulomb's law $F = k|q_1q_2|/r^2$** describes the force between point charges, and superposition gives the net force on a charge from many sources.

3. **The electric field $\vec{E} = \vec{F}/q$** is the more general organizing concept. A charge sources a field; another charge feels force $\vec{F} = q\vec{E}$. The field formalism is essential for time-varying problems (radiation, light) we will meet later.

The one idea that matters most: **Coulomb's law has the same inverse-square form as gravity, but $\sim 10^{40}$ times stronger at atomic scales.** This is why chemistry runs on electrostatics, why static-electric phenomena are everywhere, and why electromagnetism dominates the engineering world.

The common mistake to watch for: **forgetting that Coulomb's law is a vector law.** The force points along the line between charges, with sign determined by the charges' signs. Treat magnitudes and directions separately.

---

## What would change my mind

The chapter argues that charge quantization in units of $e$ is universal for all observable charges. The argument would need revision if a free fractionally charged particle (a stray quark, a magnetic monopole's electromagnetic dual) were observed in any experiment. None has been so far, despite decades of searching, but the question is open.

## Still puzzling

The deepest puzzle this chapter raises and does not resolve: *why is electric charge quantized at all?* Quantum field theory is mathematically consistent with continuous charge values; the universe just doesn't seem to use them. Dirac in 1931 showed that a single magnetic monopole anywhere would force quantization, but no monopole has been seen. The empirical fact stands; the theoretical reason is genuinely open.

---

## Connections forward

Chapter 19 introduces **electric potential** and the energy stored in electric fields — the bridge between forces (this chapter) and circuits (Chapter 20). Chapter 22 introduces magnetism, which is the relativistic complement of electric fields. Chapter 23 unifies the two via electromagnetic induction. Chapter 24 reveals that electromagnetic *fields* propagate as waves (light), at the universal speed $c$. Every later chapter on electricity, magnetism, light, and atomic physics rests on the foundations you installed here.

---

**Tags:** electric-charge, Coulomb-law, electric-field, electrostatics, conductors-insulators

---

## AI Wayback Machine

**Michael Faraday** developed the concept of fields in the 1830s — proposing that electric and magnetic forces act through space rather than at a distance. His field-line drawings became the visual vocabulary of electromagnetism. He was largely self-taught and apprenticed as a bookbinder.

**Run this:**

```
Who was Michael Faraday, and how does his field concept connect to the electric field we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Michael Faraday"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to draw the field lines for a specific charge configuration the way Faraday would have.
- Ask it about Faraday's parallel work on chemistry and the founding of the Royal Institution Christmas Lectures.

What changes? What gets better? What gets worse?
