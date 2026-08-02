# Chapter 1 — Electric Charge and Coulomb's Law

*Two flavors of matter, one inverse-square law, and the simulation that makes superposition visible.*

---

In June 1752, Benjamin Franklin flew a kite into a thunderstorm. A wet hemp string. A metal key tied at the bottom. Storm clouds overhead. He reported drawing small sparks from the key to his knuckle — confirming, by his account, that lightning and the static electricity produced by rubbing amber with fur were the same physical phenomenon at vastly different scales.

A year later, in St. Petersburg, the Russian physicist Georg Wilhelm Richmann tried to replicate the experiment. He died.

I want to start there, with Richmann, because it establishes something important: static electricity is not an abstract topic. The force we are about to write down as a clean equation — $F = kq_1 q_2 / r^2$ — is the same force that traveled down Richmann's apparatus and killed him. The equation is a compressed description of something real and, at sufficient magnitude, lethal. Every symbol in it earns its place.

Franklin's contribution was qualitative: lightning and triboelectric effects are the same thing. The quantitative version had to wait thirty-three years, until 1785, when Charles-Augustin de Coulomb published the results of experiments performed with a custom-built **torsion balance** — two charged spheres on opposite ends of a delicate horizontal rod, suspended by a thin silver wire. The wire twisted in proportion to the force between the charges. Coulomb measured how the force depended on charge magnitude and on separation distance. He found two things. First, the force scales linearly with each charge: double one charge, double the force. Second, the force falls off with the inverse square of the distance: double the separation, reduce the force by four.

Those two facts, combined with a proportionality constant $k$, give Coulomb's law:

$$F = \frac{k q_1 q_2}{r^2}$$

The constant $k \approx 8.99 \times 10^9 \text{ N·m}^2/\text{C}^2$ looks arbitrary until you compare it to its gravitational counterpart. For two electrons — one electron-mass gravitational force versus one electron-charge electrical force — the electrical force is roughly $10^{42}$ times stronger. Gravity between elementary particles is so feeble as to be unmeasurable; the electrical force is what actually holds atoms together. That ratio is one of the deep unexplained numbers in physics. We will not explain it here. But you should know it is unexplained, and that honest uncertainty is where the interesting physics lives.

![log-scale comparison of electromagnetic vs. gravitational force for an electron-electron pair at 1 Å — student should see the ~10⁴² ratio viscerally](../images/01-electric-charge-coulombs-law-fig-01.png)
*Figure 1.1 — Coulomb's Torsion Balance*

<!-- → [CHART: log-scale comparison of electromagnetic vs. gravitational force for an electron-electron pair at 1 Å — student should see the ~10⁴² ratio viscerally] -->

---

## Three facts about charge

Before we can apply Coulomb's law, we need to know what $q$ actually is. The answer comes in three empirical facts — things we know from experiment, not from derivation.

**Fact one: two signs.** Matter comes in two electrical flavors. Franklin's convention (still in use) calls one positive and one negative. Like signs repel; opposite signs attract. The labels are arbitrary. What is not arbitrary is the *count*: nature gives us exactly two kinds, not three, not five. We do not know why two. Some grand unified theories connect the count to the gauge structure of the theory; no derivation feels fully satisfying. It is a fact about the world that we accept and work with.

**Fact two: quantization.** All free charges are integer multiples of the elementary charge

$$e = 1.602\,176\,634 \times 10^{-19} \text{ C}$$

Since 2019, this is the exact, defined value of $e$ — the coulomb is now defined in terms of $e$ rather than the other way around. You cannot have half of $e$. You can have $1e$, $2e$, $10^{23}e$ — but always integer multiples. (Quarks carry fractional charges of $\pm e/3$ or $\pm 2e/3$, but no free quark has ever been isolated; they come permanently bound in hadrons whose total charge is always an integer multiple of $e$.)

**Fact three: conservation.** The total charge of an isolated system does not change. When a high-energy photon produces an electron-positron pair — one particle with charge $-e$ and one with charge $+e$ — the total charge remains zero. When that electron and positron annihilate back into photons, the total charge remains zero. Conservation is exact, to the best of our current measurement.

These three facts — two signs, quantization, conservation — are the grammar of electric charge. Coulomb's law is a sentence written in that grammar. If you do not have the grammar, the sentence is noise.

<!-- → [TABLE: three charge facts side-by-side — fact, what it says, and the experiment or observation that established it (triboelectric experiments, Millikan oil-drop, pair production/annihilation)] -->

---

## Conductors and insulators

There is one more piece of background before we can use the law in any practical problem: materials differ enormously in how freely their charges move.

**Conductors** — metals, electrolyte solutions, plasmas — have charges that move freely under an applied field. Put excess charge on a copper sphere; it spreads over the surface in microseconds. **Insulators** — glass, dry plastic, vacuum — have charges bound in place. Put excess charge on a glass rod; it stays where you put it, which is why you can charge a glass rod by rubbing it. **Semiconductors** sit between, with a small number of mobile carriers at room temperature; they are the basis of every transistor and microprocessor, and we return to them in Chapter 11.

Three mechanisms transfer charge between objects. **Friction** (the triboelectric effect): rubbing two materials together moves electrons from one to the other. Walk across a wool carpet; you become net-negative. Touch a metal doorknob; the charge discharges through a small spark. **Conduction**: bring a charged conductor into contact with another conductor; charge flows until their electrical potentials equalize. **Induction**: bring a charged object *near* (not touching) a conductor; charges in the conductor rearrange in response, and if you then momentarily connect the conductor to ground, you drain off the repelled sign and leave a net charge of the other sign.

The reason I am telling you this before the math: every problem where you apply Coulomb's law has an implicit assumption about whether charge can move. If the charges are on insulators, or if we treat them as fixed point charges, the law applies directly. If charges are free to move — if we are near conductors — the situation is more complicated, and we will return to that complication in Chapter 4.

<!-- → [TABLE: conductors vs. insulators vs. semiconductors — columns: material class, example materials, charge mobility, timescale for charge redistribution, where it appears in this book] -->

![three-step diagram of charge transfer by induction — (1) charged rod brought near neutral conductor, (2) charges separate inside conductor, (3) conductor grounded and disconnected, leaving net charge — each step shows...](../images/01-electric-charge-coulombs-law-fig-02.png)
*Figure 1.2 — Coulomb's Law in Vector Form*

<!-- → [INFOGRAPHIC: three-step diagram of charge transfer by induction — (1) charged rod brought near neutral conductor, (2) charges separate inside conductor, (3) conductor grounded and disconnected, leaving net charge — each step shows the charge distribution schematically] -->

---

## Coulomb's law in vector form

The scalar form $F = kq_1 q_2 / r^2$ tells you the magnitude. It does not tell you the direction. In a problem with more than two charges, direction is everything. Here is the vector form.

Two point charges $q_1$ at position $\vec{r}_1$ and $q_2$ at position $\vec{r}_2$. The force on $q_2$ due to $q_1$ is:

$$\vec{F}_{12} = \frac{k q_1 q_2}{|\vec{r}_2 - \vec{r}_1|^3}\left(\vec{r}_2 - \vec{r}_1\right)$$

The vector $(\vec{r}_2 - \vec{r}_1)$ points from $q_1$ toward $q_2$. If $q_1 q_2 > 0$ — same sign — then $\vec{F}_{12}$ points in the same direction as $(\vec{r}_2 - \vec{r}_1)$, which means *away* from $q_1$. Repulsion. If $q_1 q_2 < 0$ — opposite signs — then $\vec{F}_{12}$ points opposite to $(\vec{r}_2 - \vec{r}_1)$, which means *toward* $q_1$. Attraction. The algebra of signs handles the direction automatically, which is why you should always work in vector form once you are past the simplest one-dimensional case.

By Newton's third law, $\vec{F}_{21} = -\vec{F}_{12}$: the force on $q_1$ from $q_2$ is equal in magnitude and opposite in direction.

The constant $k$ is frequently written in an equivalent form that will look less arbitrary after Chapter 3:

$$k = \frac{1}{4\pi\varepsilon_0}, \qquad \varepsilon_0 = 8.854 \times 10^{-12} \frac{\text{C}^2}{\text{N·m}^2}$$

$\varepsilon_0$ is the **permittivity of free space**. The $4\pi$ in the denominator looks like it complicates things. It pays for itself in Gauss's law, where the $4\pi$ from the surface area of a sphere cancels it and the result is clean. For now, treat $k$ and $1/4\pi\varepsilon_0$ as interchangeable.

![two charges with position vectors r₁ and r₂, the separation vector (r₂ − r₁), and the force arrows — one for same-sign (repulsion) and one for opposite-sign (attraction), labeled clearly](../images/01-electric-charge-coulombs-law-fig-03.png)
*Figure 1.3 — Three Charges in a Line*

<!-- → [IMAGE: diagram showing two charges with position vectors r₁ and r₂, the separation vector (r₂ − r₁), and the force arrows — one for same-sign (repulsion) and one for opposite-sign (attraction), labeled clearly] -->

---

## The superposition principle

Now suppose there are three charges, or thirty. The net force on any one charge from all the others is the **vector sum** of the individual Coulomb forces:

$$\vec{F}_{\text{net on } j} = \sum_{i \neq j} \frac{k q_i q_j}{|\vec{r}_j - \vec{r}_i|^3}\left(\vec{r}_j - \vec{r}_i\right)$$

This is called **superposition**. It is a separate empirical fact from Coulomb's law itself. Coulomb's law tells you the force between any two charges. Superposition tells you that adding a third charge does not alter the force between the original two — the total is simply the vector sum of all pairwise contributions.

Superposition holds because Maxwell's equations are *linear* in charge and field. We cannot derive that linearity from first principles here — it is a fact about how the equations of electromagnetism happen to be structured. But it is important to name it explicitly, because in other areas of physics (gravity in general relativity, for instance) superposition fails. Here it holds, and that makes calculation vastly simpler.

A concrete check: place two positive charges near each other. They repel. Now place a negative charge nearby. Does the negative charge change the repulsion between the first two? No. It adds its own attractive pull on each, but the repulsion between the original pair is unmodified. If you ever doubt superposition, that is the experiment you would run.

![three-charge diagram showing (left) two positive charges with repulsion arrow between them, then (right) same two charges with a negative charge added nearby — the pairwise repulsion arrow between the original pair is...](../images/01-electric-charge-coulombs-law-fig-04.png)
*Figure 1.4 — Three Materials, One Variable*

<!-- → [IMAGE: three-charge diagram showing (left) two positive charges with repulsion arrow between them, then (right) same two charges with a negative charge added nearby — the pairwise repulsion arrow between the original pair is identical in both panels; only new force vectors are added, not modified] -->

---

## Worked example: three charges on a line

Three charges on the $x$-axis: $q_1 = +1\,\mu\text{C}$ at $x = 0$, $q_2 = +1\,\mu\text{C}$ at $x = +4\,\text{cm}$, $q_3 = +1\,\mu\text{C}$ at $x = +6\,\text{cm}$. What is the net force on $q_3$?

**What we know.** $q_3$ has two neighbors, both positive. Both will push it in the $+x$ direction. The question is: by how much?

**Force from $q_1$ on $q_3$.** Distance $r_{13} = 0.06\,\text{m}$.

$$F_{13} = \frac{(8.99 \times 10^9)(10^{-6})(10^{-6})}{(0.06)^2} = \frac{8.99 \times 10^{-3}}{3.6 \times 10^{-3}} = 2.50\,\text{N}$$

Direction: $+\hat{x}$ (repulsion pushes $q_3$ away from $q_1$, which is to its left).

**Force from $q_2$ on $q_3$.** Distance $r_{23} = 0.02\,\text{m}$.

$$F_{23} = \frac{(8.99 \times 10^9)(10^{-6})(10^{-6})}{(0.02)^2} = \frac{8.99 \times 10^{-3}}{4 \times 10^{-4}} = 22.5\,\text{N}$$

Direction: $+\hat{x}$.

**Superpose:** $\vec{F}_{\text{net}} = 2.50\,\hat{x} + 22.5\,\hat{x} = 25.0\,\hat{x}$ N.

**What this reveals.** $q_2$ is three times closer to $q_3$ than $q_1$ is. The inverse-square law makes that a factor of nine in force — $q_2$ contributes nine times more than $q_1$ even though both charges are identical. In any superposition problem, identify the dominant pair first. The remaining terms are corrections, often small ones.

**Where this breaks.** This calculation assumes all three charges are point charges sitting still. For extended charge distributions — a uniformly charged rod, a sphere of charge — you replace the discrete sum with an integral: $\vec{F} = \int k\,dq\,\hat{r}/r^2$ over the distribution. One such integral appears at the end of this chapter; the systematic treatment of continuous distributions begins in Chapter 2.

<!-- → [IMAGE: x-axis diagram showing q₁, q₂, q₃ at their positions with labeled distances r₁₃ = 6 cm and r₂₃ = 2 cm, and force arrows showing F₁₃ (small) and F₂₃ (large) on q₃ — student should see the asymmetry visually before computing] -->

---

## Common misconceptions

**"Positive charge means more charge, negative means less."** No. Positive and negative are labels for two distinct flavors — like north and south poles of a magnet. A $+5\,\mu\text{C}$ charge and a $-5\,\mu\text{C}$ charge are equal in magnitude; they push on each other in opposite directions. There is no sense in which one "has more charge" than the other.

**"Coulomb's law works for any pair of objects."** It is exact only for **point charges** — sources with no spatial extent. For two uniformly charged spheres, Coulomb's law happens to give the exact answer between their centers, but that is a theorem we prove in Chapter 3, not a general rule. For irregular or nearby extended distributions, you must integrate.

**"Two electrons: I should drop the negative sign and just use magnitudes."** The vector form handles signs automatically. The force between two electrons: $q_1 q_2 = (-e)(-e) = e^2 > 0$, so $\vec{F}_{12}$ points away from $q_1$ — repulsion, as it should be. Drop the signs and you lose the direction. Work in vector form.

---

## Exercises

**Warm-up 1.** *(Fact recall — tests: two signs, quantization, conservation)* State the three empirical facts about electric charge in one sentence each. For each, name the experiment or phenomenon that most directly establishes it.

**Warm-up 2.** *(Scalar Coulomb's law — tests: direct application of $F = kq_1q_2/r^2$)* Two point charges, $q_1 = +4\,\mu\text{C}$ and $q_2 = +4\,\mu\text{C}$, are separated by $r = 0.10\,\text{m}$ in vacuum. Compute the magnitude of the force between them. Is it attractive or repulsive? Now double the separation. What is the new force? Express your answer as a ratio to the original.

**Warm-up 3.** *(Vector form — tests: direction tracking with signs)* Two charges: $q_1 = +2\,\mu\text{C}$ at the origin and $q_2 = -5\,\mu\text{C}$ at $(0.04, 0)$ m. Write out $\vec{F}_{12}$ (the force on $q_2$ due to $q_1$) fully in vector form, including sign. Verify the direction makes physical sense.

**Application 1.** *(Superposition in 1D — tests: vector sum of pairwise forces)* Three charges on the $x$-axis: $q_1 = +3\,\mu\text{C}$ at $x = 0$, $q_2 = -3\,\mu\text{C}$ at $x = 0.03\,\text{m}$, $q_3 = +3\,\mu\text{C}$ at $x = 0.06\,\text{m}$. Find the net force on $q_2$. Note: $q_1$ and $q_3$ are both at 3 cm from $q_2$ — does symmetry simplify the problem, or does the sign of $q_2$ complicate it?

**Application 2.** *(Superposition in 2D — tests: vector components before summing)* $q_1 = +1\,\mu\text{C}$ at $(0, 0)$, $q_2 = +1\,\mu\text{C}$ at $(0.03, 0)$ m, $q_3 = +1\,\mu\text{C}$ at $(0, 0.04)$ m. Find the net force on $q_3$ in vector component form. Verify by checking that the direction makes intuitive sense: both $q_1$ and $q_2$ should push $q_3$ away from them.

**Application 3.** *(Conductor/insulator reasoning — tests: knowing when Coulomb's law applies directly)* A charged glass rod (charge $+Q$, insulator) is held near a grounded copper sphere. Describe qualitatively what happens to the charge distribution on the copper sphere. Does Coulomb's law between the rod and sphere simplify to $F = kQq/r^2$ for some total charge $q$ on the sphere? Why or why not?

**Synthesis 1.** *(Equilibrium — tests: superposition + force balance)* Two equal positive charges $+q$ are fixed at $x = -a$ and $x = +a$. A third charge $Q$ (sign unknown) is placed at the origin. (a) For what sign of $Q$ is the origin an equilibrium position? (b) For that sign, is the equilibrium stable against displacement along the $x$-axis? Along the $y$-axis? (These have different answers — explain why.)

**Synthesis 2.** *(Inverse-square dominance — tests: recognizing when close charges dominate)* A charge $q = +1\,\mu\text{C}$ is placed at $x = 1.00\,\text{m}$. Two other charges $+1\,\mu\text{C}$ are at $x = 0$ and $x = 0.99\,\text{m}$. Without computing, rank the three pairwise forces on the charge at $x = 1.00\,\text{m}$. Then compute and verify your ranking. What fraction of the total force comes from the closer neighbor?

**Challenge.** *(Continuous distribution — points toward Chapter 2)* A uniformly charged rod of length $L$ and total charge $Q$ lies along the $x$-axis from $x = 0$ to $x = L$. A point charge $q$ sits at $x = L + d$. Divide the rod into infinitesimal elements $dq = (Q/L)\,dx$, write the Coulomb force $d\vec{F}$ from each element on $q$, and integrate to find the total force. Show that in the limit $d \gg L$, the result reduces to Coulomb's law for two point charges $Q$ and $q$ separated by distance $d + L/2$ — the rod looks like a point charge from far away.

---

## LLM Exercises

### Build the Coulomb force simulator (`01-coulombs-law.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** Coulomb's law in vector form: $\vec{F}_{ji} = k q_i q_j (\vec{r}_j - \vec{r}_i) / |\vec{r}_j - \vec{r}_i|^3$.
>
> **Say.** Build an interactive multi-charge Coulomb force simulator. Users can drag charges onto a canvas, set magnitudes via sliders, and see force vectors on each.
>
> **Constrain.** D3 v7. Up to 6 charges supported. Each charge: red (positive) or blue (negative) circle, with magnitude shown next to it. Force vectors: red for repulsive, blue for attractive, length scaled by log(1+|F|). Show both individual pairwise force vectors (light gray) and net force (heavy black) on each charge. Drag-and-drop interaction. Slider beside each charge for q. Filename: `01-coulombs-law.html`.
>
> **Verify.** (a) Two equal positive charges: forces on each are equal in magnitude and point apart. (b) Equal opposite charges: forces equal and point together. (c) Adding a third charge does not change the original two charges' pairwise force; it adds a third vector to each (superposition visible).

### Exploration

- Place three equal positive charges at the vertices of an equilateral triangle. Net force on each? (Answer: outward along the symmetry axis from the triangle's center. Check this.)
- Place four charges in a square (alternating signs). Sketch the net force on each before running the simulation.
- Find a configuration where the net force on one charge is zero. Does such a configuration exist for three charges in a plane?

### Extension prompt (chapter bridge)

> **Show.** I've computed forces between charges. Now I want to see the *electric field* at every point in space — the force a unit test charge would feel.
>
> **Say.** Modify the simulator to add a 2D vector-field background showing $\vec{E}$ at a grid of points.
>
> **Constrain.** 20×15 grid of arrows. Arrow direction = $\vec{E}$ direction at that grid point; arrow length proportional to log(1+|$\vec{E}$|). Color map: blue (weak) to red (strong). Keep the existing charges and force-vector overlay.
>
> **Verify.** Field arrows should point away from positive charges and toward negative charges. The field magnitude near a single charge should fall as 1/r² — verify by hovering at points 1× and 2× the radius and comparing.

Save as `01b-electric-field-preview.html`. This is the lead-in to Chapter 2.

---

## What would change my mind

The central claim — $F = kq_1 q_2 / r^2$ with the exponent exactly 2 — has survived every test at intermediate distances (atomic to laboratory scale, $10^{-10}$ m to roughly $10^4$ m) to spectacular precision. The exponent has been measured to be 2 to within a part in $10^{16}$ at laboratory scales. At very short distances (sub-femtometer, inside the nucleus), the strong and weak forces dominate; Coulomb's law remains valid but is no longer the dominant interaction. At cosmic distances and very weak fields, some quantum-gravity proposals predict deviations; none has been confirmed. A reproducible measurement of a non-integer exponent at any scale where the law currently holds would force the rewriting of this chapter and the next ten.

## Still puzzling

*Why two signs and not three?* Empirical fact, not derivation. Some grand unified theories link the count to gauge structure, but no closed-form "why exactly two."

*Why is $k$ so much larger than the gravitational constant $G$?* The ratio $ke^2 / Gm_e^2 \approx 4 \times 10^{42}$ is one of the famous unexplained large numbers in physics — the hierarchy problem in particle physics is a more sophisticated version of the same question.

*What is charge, ontologically?* The classical answer: "the quantity that satisfies Coulomb's law and is conserved." A deeper quantum-field-theoretic answer: "the eigenvalue under a U(1) gauge transformation." Neither feels satisfying. Honest uncertainty.

---

**Tags:** electric charge, Coulomb's law, superposition, permittivity, conductors, insulators, torsion balance, Franklin
