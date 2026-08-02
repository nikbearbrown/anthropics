# Chapter 1 — Electric Charge and Coulomb's Law

*Two flavors of matter, one inverse-square law, and the simulation that makes superposition visible.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the empirical facts about electric charge — two signs, quantization, conservation — and identify which were known before Coulomb and which came later.
2. **(Apply)** Use Coulomb's law in vector form to compute the force between two point charges given their charges and positions.
3. **(Apply)** Apply the superposition principle to compute the net force on a charge from an arrangement of two or more other charges.
4. **(Analyze)** Identify in a given problem statement whether Coulomb's law applies directly, whether superposition suffices, or whether a continuous integration is required.
5. **(Apply)** Build a multi-charge force simulator that visualizes individual and net force vectors.

---

## Opening case: a kite, a key, and a Russian basement

In June 1752, somewhere in or near Philadelphia, Benjamin Franklin flew a kite into a thunderstorm. A wet hemp string ran from kite to ground. At the bottom end, a metal key was tied. As storm clouds passed, Franklin reported drawing small sparks from the key to his knuckle — confirming, by his account, that lightning and the static electricity produced by rubbing amber with fur were the same physical phenomenon at vastly different scales.

A year later, in St. Petersburg, the Russian physicist Georg Wilhelm Richmann tried to replicate the experiment. He died, struck through his apparatus by lightning. Static electricity is not an abstract topic.

What Franklin's connection established — that lightning and "tribo-electric" effects share one underlying physics — was qualitative. The quantitative version came in 1785 when Charles-Augustin de Coulomb published the results of experiments performed with a custom-built **torsion balance**: two charged spheres on opposite ends of a delicate horizontal rod, suspended by a thin silver wire. The wire twisted in proportion to the force between the charges. Coulomb measured how the force depended on charge magnitude and on separation distance.

He found two things. First, the force scales linearly with each charge: $F \propto q_1 q_2$. Second, the force falls off with the inverse square of the distance: $F \propto 1/r^2$. Together, with a proportionality constant $k$:

$$F = \frac{k q_1 q_2}{r^2}$$

The same mathematical structure as Newton's gravitational law — but with charges in two signs (so the force can repel as well as attract), and a constant $k \approx 8.99 \times 10^9 \text{ N·m}^2/\text{C}^2$ that is roughly $10^{40}$ times stronger than its gravitational counterpart for an electron-electron pair.

This chapter is the quantitative law and its first applications. Chapter 2 reformulates it as a field. Chapter 3 reformulates it again as a flux. The book builds outward from Coulomb's law for the next six chapters; understanding it deeply now pays off through Maxwell.

---

## Core concept

### Three facts about charge

**Sign.** Matter comes in two electrical flavors. Franklin's convention (which we still use) calls one positive and one negative. Like signs repel; opposite signs attract. The labels are arbitrary, but the *count* is empirical: nature gives us exactly two kinds, not three.

**Quantization.** All free charges are integer multiples of the elementary charge

$$e = 1.602\,176\,634 \times 10^{-19} \text{ C}$$

Since 2019, this is the *exact, defined* value of e — the coulomb is now defined as the charge of exactly 1/e ≈ 6.241 × 10¹⁸ elementary charges. (Quarks carry fractional charges of ±e/3 or ±2e/3, but no free quark has ever been observed; quarks always come bound in hadrons whose total charge is integer.)

**Conservation.** The total charge of an isolated system is constant in time. Local creation: when a high-energy photon produces an electron-positron pair, total charge is still zero. Local destruction: when an electron and positron annihilate, total charge is still zero. Conservation is exact at the level of Standard Model physics.

### Conductors and insulators

Materials differ in how freely their charges move:

- **Conductors** (metals, electrolyte solutions, plasmas) have charges that move freely under an applied field. Excess charge spreads over the surface in microseconds.
- **Insulators** (glass, plastic, dry air, vacuum) have charges bound to fixed positions. Excess charge stays where you put it.
- **Semiconductors** (silicon, germanium, doped variants) sit between, with a few mobile carriers at room temperature. They're the basis of every transistor; we return to them in Chapter 11.

Three practical mechanisms by which charge moves:
- **Friction** (the triboelectric effect): rubbing materials transfers electrons. Walk across a wool rug, become net-negative; touch a doorknob, get a small spark.
- **Conduction**: bring a charged object in contact with a conductor; charge flows until potentials match.
- **Induction**: bring a charged object *near* (not touching) a conductor; charges in the conductor rearrange, then ground the conductor to drain off the unwanted sign.

### Coulomb's law in vector form

Two point charges $q_1$ and $q_2$ at positions $\vec{r}_1$ and $\vec{r}_2$. The force on $q_2$ due to $q_1$ is

$$\vec{F}_{12} = \frac{k q_1 q_2}{|\vec{r}_2 - \vec{r}_1|^3}(\vec{r}_2 - \vec{r}_1)$$

The vector $(\vec{r}_2 - \vec{r}_1)$ points from $q_1$ to $q_2$. If both charges have the same sign, $q_1 q_2 > 0$ and the force on $q_2$ points away from $q_1$ — repulsion. If opposite signs, $q_1 q_2 < 0$ and the force on $q_2$ points toward $q_1$ — attraction.

By Newton's third law, $\vec{F}_{21} = -\vec{F}_{12}$.

The constant $k$ is often written

$$k = \frac{1}{4\pi\varepsilon_0}, \qquad \varepsilon_0 = 8.854 \times 10^{-12} \frac{\text{C}^2}{\text{N·m}^2}$$

where $\varepsilon_0$ is the **permittivity of free space**. The $4\pi$ in the denominator looks ugly; it pays for itself in Gauss's law (Chapter 3), where the $4\pi$ cancels against the surface area of a sphere.

### The superposition principle

The net force on a charge from an arrangement of other charges is the **vector sum** of the pairwise Coulomb forces:

$$\vec{F}_{\text{net on } j} = \sum_{i \neq j} \frac{k q_i q_j}{|\vec{r}_j - \vec{r}_i|^3}(\vec{r}_j - \vec{r}_i)$$

Superposition is a separate empirical fact. Coulomb's law tells you the force between two charges; superposition tells you that adding a third charge does not change the force between the first two. The total is the vector sum. Anywhere in this book that you compute "the force from many charges," you are using superposition.

Superposition holds because Maxwell's equations are *linear* in charge and field — a fact this chapter cannot derive but you should know.

---

## Worked example: three charges in a line

Three charges on the x-axis: $q_1 = +1\,\mu\text{C}$ at $x = 0$, $q_2 = +1\,\mu\text{C}$ at $x = +4\,\text{cm}$, and $q_3 = +1\,\mu\text{C}$ at $x = +6\,\text{cm}$. Find the net force on $q_3$.

**Step 1.** Compute the force on $q_3$ from $q_1$. Distance: $r_{13} = 0.06\,\text{m}$. Both positive, so force on $q_3$ is in the $+x$ direction (away from $q_1$).
$$F_{13} = \frac{(8.99 \times 10^9)(10^{-6})(10^{-6})}{(0.06)^2} = 2.50\,\text{N}$$
$\vec{F}_{13} = +2.50\,\hat{x}$ N.

**Step 2.** Compute the force on $q_3$ from $q_2$. Distance: $r_{23} = 0.02\,\text{m}$. Both positive, force in $+x$.
$$F_{23} = \frac{(8.99 \times 10^9)(10^{-6})(10^{-6})}{(0.02)^2} = 22.5\,\text{N}$$
$\vec{F}_{23} = +22.5\,\hat{x}$ N.

**Step 3.** Superpose: $\vec{F}_{\text{net}} = \vec{F}_{13} + \vec{F}_{23} = +25.0\,\hat{x}$ N.

**The lesson.** Even though $q_1$ and $q_2$ have the same magnitude, $q_2$ dominates the force on $q_3$ by a factor of 9 — the inverse-square law amplifies the closer charge. In any superposition problem, identify the dominant pair first; the rest are corrections.

**The limit.** This works for point charges. For *extended* charge distributions — a charged rod, a sphere of charge — you replace the sum with an integral: $\vec{F} = \int k\,dq\,\hat{r}/r^2$, integrated over the distribution. The integration is what Chapter 2 spends most of its time on.

---

## Common misconceptions

**"Positive charge means more charge, negative means less."** No. Positive and negative are *labels for two distinct flavors of charge*, not amounts. A 5 µC positive charge and a 5 µC negative charge are equal in magnitude; they just push on each other in opposite ways.

**"Coulomb's law works for any pair of objects."** It is exact only for *point charges* — sources with no extent. For two charged spheres, Coulomb's law gives the right answer between their centers *because* the spherical symmetry forces it (a result we'll prove in Chapter 3). For irregular distributions or close approach where the charges' extent matters, you must integrate. Many textbook problems implicitly assume point-charge approximation; the assumption deserves to be named.

**"The force on a test charge comes from the field, not from the source charges."** Both framings are correct and equivalent. The field is a bookkeeping device — a way to describe what each source charge does to space, which any subsequent charge then responds to. Chapter 2 makes the field formulation explicit; for now, either picture works.

**"$q_1$ and $q_2$ in the formula refer to total charge, so for two electrons I should plug in $-e$ for each."** Correct. The force between two electrons is then $F = ke^2/r^2 > 0$ — repulsive. Students sometimes drop the signs and lose the direction. Vector form $\vec{F}_{12}$ keeps track for you; the *direction* of $\vec{F}$ comes from $q_1 q_2$ (sign) and $(\vec{r}_2 - \vec{r}_1)$ together.

---

## Exercises

**Warm-up (Understand).** State the three facts about electric charge in one sentence each. Then state Coulomb's law in vector form and identify each symbol.

**Apply.** Two point charges, $q_1 = +2\,\mu\text{C}$ at the origin and $q_2 = -3\,\mu\text{C}$ at $(3,0)$ cm, both in vacuum. Compute the force on $q_2$ in vector form. Repeat for a third charge $q_3 = +1\,\mu\text{C}$ added at $(0, 4)$ cm — find the net force on $q_3$.

**Apply + Analyze.** Two equal positive charges of magnitude $q$ are at $(\pm a, 0)$. A third positive charge $Q$ is placed on the $y$-axis at $(0, y)$. (a) Find the net force on $Q$. (b) Show that for $y > 0$, the force points in $+\hat{y}$. (c) What happens at $y = 0$ exactly? Is this equilibrium *stable*? (Hint: think about what happens if $Q$ drifts slightly off-axis.)

**Apply.** An equilibrium problem. Three charges sit on a line. $q_1 = +q$ at $x = 0$ and $q_2 = +q$ at $x = L$. Find the position $x_3$ where a third positive charge $q_3$ can be placed so that the net force on it is zero. (Answer: $x_3 = L/2$ by symmetry.) Now: is this an equilibrium? Test it by displacing $q_3$ slightly along the $x$-axis and computing whether the restoring force is positive or negative.

**Challenge (Analyze).** A uniformly charged rod of length $L$ and total charge $Q$ lies along the $x$-axis from $0$ to $L$. Find the force on a test charge $q$ at position $(L + d, 0)$. (Hint: divide the rod into elements $dq = (Q/L)\,dx$, integrate $dF$ from each element.)

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

The central claim of this chapter — Coulomb's law in the form $F = k q_1 q_2 / r^2$ — has survived every test at intermediate distances (atomic to laboratory scale, $10^{-10}$ m to ~$10^4$ m) to spectacular precision. The exponent of $r$ in the denominator has been measured to be 2 to within a part in $10^{16}$ at laboratory scales (tests of inverse-square law via Coulomb-balance and capacitor experiments). At very short distances (sub-femtometer, inside the nucleus), the strong and weak forces dominate; Coulomb's law remains but is no longer the dominant interaction. At cosmic distances and very weak fields, some quantum-gravity proposals predict deviations; none has been confirmed. A reproducible measurement of a non-integer exponent at any scale where Coulomb's law currently holds would force the rewriting of this chapter and the next ten.

## Still puzzling

- *Why two signs and not three?* Empirical fact, not derivation. Some grand unified theories link the count to gauge structure, but no closed-form "why exactly two."
- *Why is $k$ so much larger than the gravitational constant $G$?* The ratio $ke^2 / Gm_e^2 \approx 4 \times 10^{42}$ is one of the famous unexplained large numbers in physics. The hierarchy problem in particle physics is a more sophisticated version of the same question.
- *What is charge, ontologically?* The classical answer is "the quantity that satisfies Coulomb's law and is conserved." A deeper quantum-field-theoretic answer is "the eigenvalue under a U(1) gauge transformation." Neither answer feels satisfying to most students. Honest uncertainty.

---

**Tags:** electric charge, Coulomb's law, superposition, permittivity, conductors, insulators, torsion balance, Franklin

