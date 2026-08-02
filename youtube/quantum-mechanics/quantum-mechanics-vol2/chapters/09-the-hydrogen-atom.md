# Chapter 9 — The Hydrogen Atom
*One formula Balmer had no explanation for. One calculation Schrödinger did over Christmas break. The same number — and only one of them describes what you would see in the lab.*

In 1885, Johann Balmer published a four-page note. He had been studying four visible spectral lines of hydrogen — red, blue-green, violet, deep violet — and he had found a pattern:

$$\lambda = B\cdot\frac{n^2}{n^2 - 4}, \qquad n = 3, 4, 5, 6, \quad B \approx 364.5\,\text{nm}.$$

He had no theory. Just four numbers from a lab notebook and a formula that fit them exactly — not approximately, exactly, to the precision of the measurements. Johannes Rydberg generalized it in 1888 to cover all spectral series:

$$\frac{1}{\lambda} = R_H\!\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right),$$

with $R_H \approx 1.097 \times 10^7\,\text{m}^{-1}$. Lyman series in the ultraviolet. Balmer in the visible. Paschen in the infrared. All from one formula, and still no explanation for twenty-eight more years.

Bohr supplied a partial answer in 1913: assume electrons orbit in circles, but allow only those orbits where angular momentum is a multiple of $\hbar$. This ansatz produced $E_n = -13.6\,\text{eV}/n^2$ and reproduced Rydberg's formula. But why must angular momentum be quantized? Why don't orbiting electrons radiate, as Maxwell's equations demand? Bohr had no answers. The model was a conjecture that happened to produce the right numbers.

Schrödinger, at an Alpine resort over Christmas 1925, wrote down the wave equation for hydrogen and worked it through. The energies fell out again — same $-13.6\,\text{eV}/n^2$, no arbitrary postulates. What also fell out, and what Bohr had absolutely no machinery for, was the complete spatial structure: a probability density $|\psi_{n\ell m}|^2$, a cloud of likelihood distributed through space, not a path. This chapter works through that calculation.

---

## Reducing Two Bodies to One

A hydrogen atom is a proton (mass $m_p$) and an electron (mass $m_e$) interacting via $V = -e^2/(4\pi\epsilon_0|\vec{r}_e - \vec{r}_p|)$. The Hamiltonian has six coordinates. We can always separate a two-body problem into a freely-drifting center of mass and a one-body relative-coordinate problem. Introduce the center-of-mass $\vec{R} = (m_p\vec{r}_p + m_e\vec{r}_e)/(m_p+m_e)$ and the relative coordinate $\vec{r} = \vec{r}_e - \vec{r}_p$. The Hamiltonian separates:

$$\hat{H} = \frac{\hat{P}^2}{2M} + \underbrace{\frac{\hat{p}^2}{2\mu} - \frac{e^2}{4\pi\epsilon_0 r}}_{\hat{H}_\text{rel}},$$

where $M = m_p + m_e$ is the total mass and

$$\mu = \frac{m_p m_e}{m_p + m_e}$$

is the **reduced mass**. The center-of-mass piece is a free particle drifting through space — uninteresting. All the physics is in $\hat{H}_\text{rel}$: a single particle of mass $\mu$ in a Coulomb potential.

Since $m_p \approx 1836\,m_e$, the reduced mass is $\mu \approx m_e(1 - 1/1836)$, within 0.05% of $m_e$. For rough numbers we use $\mu = m_e$. For precision spectroscopy the difference matters: Harold Urey discovered deuterium in 1932 by finding a second copy of every Balmer line, shifted because deuterium's heavier nucleus changes $\mu$. The Balmer $\alpha$ line shifts by about 1.79 Å between hydrogen and deuterium — small, but unmistakable to a careful spectroscopist. A formula built on the reduced mass predicted the shift before the measurement was made.

The equation to solve is:

$$\left[-\frac{\hbar^2}{2\mu}\nabla^2 - \frac{e^2}{4\pi\epsilon_0 r}\right]\psi(\vec{r}) = E\,\psi(\vec{r}).$$

The potential is spherically symmetric. We know exactly what to do.

---

## Separating the Problem

Any spherically symmetric Hamiltonian separates in spherical coordinates. Write $\psi(r,\theta,\phi) = R(r)Y_\ell^m(\theta,\phi)$. The angular part is the spherical harmonics from Chapter 6 — that result is universal, independent of what $V(r)$ turns out to be. The spherical harmonics know nothing about Coulomb; they know only the rotation group.

The radial part is where hydrogen lives. Making the substitution $u(r) = rR(r)$ converts the three-dimensional radial equation into a one-dimensional one that looks like a familiar Schrödinger equation in a single variable. After substituting, the radial equation becomes:

$$-\frac{\hbar^2}{2\mu}\frac{d^2u}{dr^2} + \underbrace{\left[-\frac{e^2}{4\pi\epsilon_0 r} + \frac{\hbar^2\ell(\ell+1)}{2\mu r^2}\right]}_{V_\text{eff}(r)}u(r) = E\,u(r).$$

The effective potential $V_\text{eff}(r)$ has two competing pieces. The Coulomb well $-e^2/(4\pi\epsilon_0 r)$ pulls the electron toward the nucleus. The centrifugal barrier $+\hbar^2\ell(\ell+1)/(2\mu r^2)$ diverges as $r \to 0$ for $\ell \geq 1$ and pushes probability density away from the origin. For $\ell = 0$ (s-states), the barrier vanishes entirely and the wave function can be nonzero at the nucleus — directly relevant for hyperfine coupling between the electron's probability density and the nuclear magnetic moment.

<!-- → [FIGURE: V_eff(r) for ℓ=0, 1, 2 — showing the pure Coulomb well for ℓ=0, the centrifugal barrier modifying the potential for ℓ=1 and ℓ=2, with a minimum at finite r for ℓ≥1; each curve labeled] -->

![V_eff(r) for ℓ=0, 1, 2 — showing the pure Coulomb well for ℓ=0, the centrifugal barrier modifying the potential for ℓ=1 and ℓ=2, with a…](../images/09-the-hydrogen-atom-fig-01.png)
*Figure 9.1 — V_eff(r) for ℓ=0, 1, 2 — showing the pure Coulomb well for ℓ=0, the centrifugal barrier modifying the potential for ℓ=1 and ℓ=2, with a…*

The boundary conditions: $u(0) = 0$ so that $R = u/r$ stays finite at the origin; $u(r) \to 0$ as $r \to \infty$ so the wave function is normalizable. These two requirements quantize the energy.

---

## The Ground State, Worked Through

The cleanest entry into hydrogen is the ground state, where the full calculation can be done without invoking a Frobenius series. Set $\ell = 0$: centrifugal barrier gone. The radial equation reduces to:

$$-\frac{\hbar^2}{2\mu}\frac{d^2u}{dr^2} - \frac{e^2}{4\pi\epsilon_0 r}\,u(r) = E\,u(r).$$

The simplest function that goes to zero at the origin and decays at infinity is:

$$u(r) = Ar\,e^{-r/a},$$

where $a$ is an unknown length. Differentiating twice, substituting, and collecting terms by powers of $r$:

$$\underbrace{\left(\frac{\hbar^2}{\mu a} - \frac{e^2}{4\pi\epsilon_0}\right)}_{\text{constant term}} + \underbrace{\left(E + \frac{\hbar^2}{2\mu a^2}\right)}_{\text{coefficient of }r}\cdot r = 0.$$

For this to hold at every $r$, both groupings must independently vanish. From the constant terms:

$$a = a_0 \equiv \frac{4\pi\epsilon_0\hbar^2}{\mu e^2} \approx 0.529\,\text{Å}.$$

This is the **Bohr radius** — it emerged from the calculation, not put in by hand. From the coefficient of $r$:

$$E = -\frac{\hbar^2}{2\mu a_0^2} \approx -13.6\,\text{eV}.$$

Both the size of the atom and the ground-state energy follow from a single consistency requirement. Normalize: $A = 2/a_0^{3/2}$, giving:

$$\psi_{100}(r) = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}.$$

Spherically symmetric. Maximum probability density at the nucleus. Exponential decay in every direction. No ring, no orbit.

---

## Two Radii, and Why They Differ

The quantity we want for "where is the electron" is not $|\psi_{100}|^2$, which is just the density at a point. We want the probability of finding the electron between $r$ and $r + dr$, integrated over all angles. This is the **radial probability density**:

$$P(r) = r^2|R_{10}(r)|^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

The factor $r^2$ is not optional: it comes from the spherical volume element $4\pi r^2\,dr$. A thin shell at radius $r$ has volume proportional to $r^2$. Even though $|\psi|^2$ is largest at $r = 0$, the shell at small $r$ is vanishingly thin, and the probability of finding the electron near the nucleus nearly vanishes. Plotting $|R_{10}|^2$ without the $r^2$ factor and claiming it answers the radial question is the single most common error in hydrogen atom calculations.

<!-- → [FIGURE: P(r) = (4/a₀³)r²e^{−2r/a₀} for the 1s state, with r_mp=a₀ and ⟨r⟩=3a₀/2 marked as vertical lines, the right-skewed tail visible, and a caption noting the shaded area beyond r_mp exceeds 50%] -->

![P(r) = (4/a₀³)r²e^{−2r/a₀} for the 1s state, with r_mp=a₀ and ⟨r⟩=3a₀/2 marked as vertical lines, the right-skewed tail visible, and a…](../images/09-the-hydrogen-atom-fig-02.png)
*Figure 9.2 — P(r) = (4/a₀³)r²e^{−2r/a₀} for the 1s state, with r_mp=a₀ and ⟨r⟩=3a₀/2 marked as vertical lines, the right-skewed tail visible, and a…*

**The most-probable radius.** Differentiate $P(r)$ and set to zero:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0.$$

Factor out $2r$: solutions are $r = 0$ (a minimum) and $r = a_0$ (the maximum):

$$r_\text{mp} = a_0.$$

**The mean radius.** Integrate $r \cdot P(r)$ over all $r$:

$$\langle r\rangle = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr = \frac{4}{a_0^3}\cdot\frac{3!}{(2/a_0)^4} = \frac{3}{2}a_0.$$

The most-probable radius is $a_0$. The mean radius is $\tfrac{3}{2}a_0$. Two different numbers for the same distribution.

They differ because $P(r)$ is right-skewed — it has a long tail at large $r$ that pulls the mean to the right of the peak. A classical electron on a circular orbit at fixed $r_0$ would give $r_\text{mp} = \langle r\rangle = r_0$: one radius. The fact that $r_\text{mp} \neq \langle r\rangle$ is a signature of wave mechanics built into the ground state of the simplest atom.

Bohr placed the electron at radius $a_0$. Schrödinger says the peak of the probability distribution is at $a_0$ — same number, different calculation — but the mean is larger, and the electron is found outside $a_0$ on more than half of all measurements. The agreement on $r_\text{mp}$ is a numerical consequence of a symmetry Bohr did not know about. The disagreement on $\langle r\rangle$ is the substance.

---

## The Full Spectrum

The ground state works out cleanly because the Laguerre polynomial at $n=1$ is a constant — the exponential is the complete solution. For general $(n, \ell)$, expand $u(r)$ as a power series, substitute into the radial equation, and demand that the series terminate: if it does not, the wave function diverges at large $r$ and cannot be normalized. Termination forces:

$$E_n = -\frac{13.6\,\text{eV}}{n^2}, \qquad n = 1, 2, 3, \ldots$$

The energy depends only on $n$, not on $\ell$ or $m$. This is the **Coulomb degeneracy** — and it is not generic. More on that below.

The terminated-series solutions are the associated Laguerre polynomials. The full radial wave functions are:

$$R_{n\ell}(r) = \mathcal{N}_{n\ell}\cdot\left(\frac{r}{a_0}\right)^\ell\cdot e^{-r/(na_0)}\cdot L_{n-\ell-1}^{2\ell+1}\!\!\left(\frac{2r}{na_0}\right),$$

where $\mathcal{N}_{n\ell}$ is the normalization constant and $L_{n-\ell-1}^{2\ell+1}$ is an associated Laguerre polynomial of degree $n - \ell - 1$. The subscript is where the quantum number constraints live.

**Three constraints, three distinct sources:**

- $n \geq 1$: the Frobenius series terminates only for positive integer $n$.
- $\ell \leq n-1$: the Laguerre polynomial has degree $n - \ell - 1$; a polynomial of negative degree does not exist.
- $|m| \leq \ell$: from Chapter 6, the angular momentum algebra, unchanged by the form of $V(r)$.

**Counting states.** For each $n$, sum over all allowed $\ell$:

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2.$$

Each shell $n$ contains $n^2$ orbital states. Including spin ($m_s = \pm\tfrac{1}{2}$ from Chapter 8), each shell holds $2n^2$ states. Shell $n=2$ holds 8; shell $n=3$ holds 18; shell $n=4$ holds 32. These are the row lengths of the periodic table — not numerology, but a structural consequence of the three constraints derived across Chapters 6, 8, and 9.

<!-- → [TABLE: shell structure table — n from 1 to 4, shell label K/L/M/N, n² orbital states, 2n² with spin, corresponding periodic table row lengths] -->

![Shell state counting: 2n² degeneracy and periodic table row lengths](../images/09-the-hydrogen-atom-fig-05.png)
*Figure 9.5 — Stacked bars for shells $n=1$ to $4$ (K–N) subdivided by subshell type ($s$, $p$, $d$, $f$), with total capacities $2, 8, 18, 32$ matching the $2n^2$ formula and the corresponding periodic-table row lengths.*

A node-counting rule ties the structure together. The total number of nodes in $\psi_{n\ell m}$ is $n-1$, partitioned into $n - \ell - 1$ **radial nodes** and $\ell$ **angular nodes**. The 2s state ($\ell=0$) has one radial node and no angular nodes. The 2p states ($\ell=1$) have no radial nodes and one angular node. Both have total nodes equal to 1 and both sit at $E_2 = -3.4$ eV. Same energy, different spatial organization of the same number of oscillations.

The general mean radius formula for any state is:

$$\langle r\rangle_{n\ell} = \frac{a_0}{2}\bigl[3n^2 - \ell(\ell+1)\bigr].$$

For $(1,0)$: $\langle r\rangle = \tfrac{3}{2}a_0$. Check. For $(2,0)$: $6a_0$. For $(2,1)$: $5a_0$. At fixed $n$, increasing $\ell$ moves the mean radius closer to the nucleus — the centrifugal barrier shifts the probability outward at small $r$ but the overall effect is to narrow the distribution.

---

## Complex Orbitals and Real Orbitals

The wave functions $\psi_{n\ell m}$ with $m \neq 0$ are complex: eigenstates of $\hat{L}_z$ with eigenvalue $m\hbar$. They have azimuthal symmetry around the $z$-axis and no preferred direction in the $xy$-plane.

The chemistry textbook $p_x$ and $p_y$ orbitals are real linear combinations:

$$p_x \propto \psi_{21,-1} - \psi_{21,+1} \propto \sin\theta\cos\phi, \qquad p_y \propto i(\psi_{21,-1} + \psi_{21,+1}) \propto \sin\theta\sin\phi.$$

These are the dumbbell shapes pointing along the Cartesian axes — useful for understanding bonding — but they are not eigenstates of $\hat{L}_z$. Both descriptions span the same subspace. Physics prefers the complex eigenstates because they diagonalize $\hat{L}_z$. Chemistry prefers the real combinations because bonding is about directional overlap. Neither is wrong; the choice depends on what you want to make explicit.

---

## The Hidden Symmetry

The Coulomb degeneracy — 2s and 2p sharing $E = -3.4$ eV; 3s, 3p, 3d all at $-1.51$ eV — is not generic. For any central potential, energy depends on both $n$ and $\ell$; the $m$-degeneracy is universal (rotational symmetry), but the $\ell$-degeneracy is special to $V \propto 1/r$.

Classically, this property shows up as the non-precession of Kepler orbits: an ellipse in a $1/r$ potential closes perfectly on itself. For any other power law the orbit precesses. The quantity that stays constant precisely because of non-precession is the **Laplace–Runge–Lenz vector**, pointing along the major axis. In quantum mechanics, the three angular-momentum operators and three Runge–Lenz operators — six in total — form the Lie algebra $\mathfrak{so}(4)$: rotations in four dimensions. Wolfgang Pauli used this algebra to solve hydrogen algebraically in 1926, before Schrödinger published the wave-mechanical solution.

The moment the potential departs from $1/r$, the $\mathfrak{so}(4)$ symmetry breaks and the $\ell$-degeneracy splits. In sodium, ten inner electrons partially screen the nuclear charge and the effective potential felt by the valence electron is no longer Coulomb. The 3s level falls below 3p, which falls below 3d. The bright yellow sodium D lines at 589 nm are the $3p \to 3s$ transitions, and they exist precisely because sodium's effective potential is not $1/r$. Those two lines are spectroscopic evidence of broken $\mathfrak{so}(4)$ symmetry.

<!-- → [FIGURE: energy level diagram comparing hydrogen (all ℓ degenerate at each n) vs. sodium (levels split by ℓ at n=3), illustrating the $\ell$-degeneracy breaking; sodium D line marked] -->

![energy level diagram comparing hydrogen (all ℓ degenerate at each n) vs. sodium (levels split by ℓ at n=3), illustrating the…](../images/09-the-hydrogen-atom-fig-03.png)
*Figure 9.3 — energy level diagram comparing hydrogen (all ℓ degenerate at each n) vs. sodium (levels split by ℓ at n=3), illustrating the…*

---

## Transitions and Selection Rules

Two levels separated by $\Delta E$ can be connected by emitting a photon of frequency $\omega = \Delta E/\hbar$. The Balmer $\alpha$ line — $n=3 \to n=2$ — sits at:

$$\lambda = \frac{hc}{\Delta E} = \frac{1240\,\text{eV·nm}}{13.6\times(1/4 - 1/9)\,\text{eV}} \approx 656.3\,\text{nm}.$$

The experimental value is 656.281 nm. Agreement to 0.003%. This is what Balmer's formula was missing: a derivation.

Not every transition is allowed. A photon carries angular momentum 1, and angular momentum conservation during emission requires the electron's orbital angular momentum to change by $\pm 1$. The electric-dipole selection rules — derived by computing $\langle\psi_f|\hat{\vec{r}}|\psi_i\rangle$ and requiring it to be nonzero — are:

$$\Delta\ell = \pm 1, \qquad \Delta m = 0, \pm 1.$$

The $2s \to 1s$ transition has $\Delta\ell = 0$ and is electric-dipole forbidden. It occurs via two-photon emission with lifetime $\approx 0.12$ s — eight orders of magnitude slower than allowed transitions. This is not a curiosity; it is what makes the 2s state metastable enough to interrogate with exquisite precision. The $1S\text{-}2S$ two-photon transition in hydrogen has been measured to fifteen significant figures using optical frequency combs. The ALPHA collaboration at CERN has measured the same transition in antihydrogen and found agreement with ordinary hydrogen at parts-per-trillion precision — a direct test of CPT symmetry.

<!-- → [FIGURE: hydrogen energy level diagram for n=1 through 5, with allowed electric-dipole transitions (Δℓ=±1) as solid arrows grouped into Lyman, Balmer, Paschen series, and the forbidden 2s→1s as a dashed arrow labeled "two-photon, τ≈0.12s"] -->

![hydrogen energy level diagram for n=1 through 5, with allowed electric-dipole transitions (Δℓ=±1) as solid arrows grouped into Lyman,…](../images/09-the-hydrogen-atom-fig-04.png)
*Figure 9.4 — hydrogen energy level diagram for n=1 through 5, with allowed electric-dipole transitions (Δℓ=±1) as solid arrows grouped into Lyman,…*

---

## What the Orbital Is Not

Three points worth being precise about.

The 90% isosurface images in chemistry textbooks — dumbbells, cloverleaves, lobes — are not containing walls. The electron does not orbit inside the dumbbell. The surface encloses the region where there is 90% probability of finding the electron on a single position measurement; on 10% of measurements the electron is found outside it. The $r_\text{mp} \neq \langle r\rangle$ calculation is the direct evidence: a path has one radius; a probability distribution has a peak and a mean that need not coincide.

The Bohr model gets $E_n = -13.6\,\text{eV}/n^2$ right because hydrogen's $\mathfrak{so}(4)$ symmetry makes the energy depend on a single quantum number, and Bohr's condition $L = n\hbar$ counts that quantum number correctly for circular orbits. But Bohr requires $\ell = n$ always — maximum angular momentum — while Schrödinger says $\ell = 0, 1, \ldots, n-1$. The 2s state ($\ell=0$, no angular momentum) is utterly forbidden in Bohr's model, yet perfectly physical and spectroscopically accessible in Schrödinger's. The Bohr model is a numerical accident. This chapter buries it.

$|\psi|^2$ is not a smeared charge distribution sitting continuously in space. It is the distribution of outcomes over many repeated position measurements on identically prepared atoms. The electron remains a point particle; fire electrons at hydrogen, measure where they scatter, and the histogram of scattering events converges to $|\psi|^2$ over many trials. The cloud shows where measurements land.

---

## Exercises

**Warm-up**

1. *[Reduced mass and its consequences]* The reduced mass of ordinary hydrogen is $\mu = m_pm_e/(m_p+m_e)$, $m_p \approx 1836\,m_e$. (a) Compute $\mu$ to four significant figures in units of $m_e$. (b) By what fractional amount does using exact $\mu$ rather than $m_e$ change $a_0$? (c) A muonic hydrogen atom replaces the electron with a muon ($m_\mu \approx 207\,m_e$). Compute the muonic Bohr radius $a_0^\mu$ and ground-state energy $E_1^\mu$.
*What this tests: following the reduced-mass calculation through to observable consequences, including the isotope shift and muonic hydrogen.*

2. *[Normalization and the Jacobian]* Verify $\psi_{100}(r) = (\pi a_0^3)^{-1/2}e^{-r/a_0}$ is normalized. Write the radial probability density $P(r) = r^2|R_{10}(r)|^2$ and verify $\int_0^\infty P(r)\,dr = 1$. Confirm $P(0) = 0$ and explain in one sentence why this does not contradict $|\psi_{100}(0)|^2 \neq 0$.
*What this tests: the Jacobian is compulsory, not optional — and* $P(0)=0$ *is a geometric fact about shell volume, not a property of the wave function.*

3. *[Quantum number counting]* List all allowed $(n,\ell,m)$ combinations for $n=3$. Verify the count gives $n^2 = 9$ orbital states and $2n^2 = 18$ with spin. For each of the three constraints on quantum numbers, write one sentence stating its mathematical origin.
*What this tests: the three constraints come from three separate sources, and conflating them is a persistent error.*

**Application**

4. *[The 2s state]* The 2s radial wave function is $R_{20}(r) = (8a_0^3)^{-1/2}(2 - r/a_0)e^{-r/(2a_0)}$. (a) Find the radial node. (b) Find $r_\text{mp}$ by maximizing $P(r) = r^2|R_{20}|^2$. (c) Compute $\langle r\rangle_{2s}$ using $\int_0^\infty r^n e^{-r/b}\,dr = n!\,b^{n+1}$. Do $r_\text{mp}$ and $\langle r\rangle$ still differ?
*What this tests: the* $r_\text{mp} \neq \langle r\rangle$ *discrepancy is not a ground-state peculiarity but a general feature of skewed distributions.*

5. *[Spectral series and the isotope shift]* (a) Compute the Lyman $\alpha$ wavelength ($n=2 \to n=1$) and confirm it is ultraviolet. (b) Compute the Paschen $\alpha$ wavelength ($n=4 \to n=3$) and confirm it is near-infrared. (c) Estimate the isotope shift at Balmer $\alpha$ between hydrogen ($m_p \approx 1836\,m_e$) and deuterium ($m_d \approx 3672\,m_e$), and explain why Urey could detect it in 1932.
*What this tests: the reduced mass is not a correction but a physical quantity with measurable spectroscopic consequences.*

6. *[Selection rules]* For each transition, state allowed or forbidden and give the reason: (a) $3p \to 1s$; (b) $3d \to 1s$; (c) $3p \to 2p$; (d) $3d \to 2p$; (e) $2s \to 1s$. For each forbidden transition, name one process by which it can still occur.
*What this tests:* $\Delta\ell = \pm 1$ *is the electric-dipole selection rule; forbidden transitions do occur, just slowly.*

7. *[Mean radius formula]* The general formula is $\langle r\rangle_{n\ell} = (a_0/2)[3n^2 - \ell(\ell+1)]$. (a) Verify for $(1,0)$ and $(2,0)$. (b) For fixed $n$, does increasing $\ell$ increase or decrease $\langle r\rangle$? Use the centrifugal-barrier picture. (c) For $(3,2)$, compute $\langle r\rangle$ and compare to $r_\text{mp} \approx n^2 a_0$.
*What this tests: the mean-radius formula is derived from the algebra of the Laguerre polynomials, and its dependence on* $\ell$ *has a physical interpretation.*

**Synthesis**

8. [*Broken* $\mathfrak{so}(4)$ *symmetry in sodium]* Hydrogen's $\ell$-degeneracy is a signature of the $1/r$ potential. In sodium, the 3s level sits at $-5.14$ eV and 3p at $-3.04$ eV. (a) What observable could distinguish 2s from 2p in hydrogen without measuring energy? (b) Compute the wavelength of the sodium $3p \to 3s$ transition. (c) The sodium D line is a doublet at 589.0 nm and 589.6 nm. What interaction splits the 3p level into two?
*What this tests: connecting the abstract symmetry argument to a real spectroscopic observable, and identifying spin-orbit coupling as the source of the fine-structure doublet.*

9. *[Oscillating dipole]* The superposition $\Psi = (1/\sqrt{2})[\psi_{100}e^{-iE_1 t/\hbar} + \psi_{210}e^{-iE_2 t/\hbar}]$. (a) Show $|\Psi|^2$ contains a cross-term oscillating at $\omega_{12} = (E_2-E_1)/\hbar$. Compute $\omega_{12}$ in rad/s and the period in femtoseconds. (b) Compute $\langle z\rangle(t)$ and show it oscillates at $\omega_{12}$. (c) Explain in two sentences why the oscillating dipole represents the atom in the act of emitting a photon, rather than sitting in either stationary state.
*What this tests: connecting the time-dependent superposition to the classical-radiation picture — the oscillating charge distribution is what drives photon emission.*

**Challenge**

10. [$n^2$ *degeneracy and what makes Coulomb special]* The identity $\sum_{\ell=0}^{n-1}(2\ell+1) = n^2$ underlies the shell structure. Prove it by induction or by pairing terms. Then: in a hypothetical atom where energy depends on $n_r + \ell + 1$ (with $n_r = n - \ell - 1$ radial nodes), how many orbital states share energy level $N = n_r + \ell + 1$? Compare to hydrogen and explain in one sentence why Coulomb degeneracy requires $\mathfrak{so}(4)$ symmetry and not just $\mathfrak{so}(3)$.
*What this tests: seeing the counting argument from the inside, and understanding that the* $n^2$ *degeneracy is not a generic feature of central potentials but a special property of the* $1/r$ *interaction.*

---

## References

Balmer, J. J. (1885). Notiz über die Spectrallinien des Wasserstoffs. *Annalen der Physik*, 25, 80.

Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine*, 26, 1–25.

Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Annalen der Physik*, 79, 361–376.

Pauli, W. (1926). Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik. *Zeitschrift für Physik*, 36, 336–363. (Algebraic solution via the Runge–Lenz vector.)

Urey, H. C., Brickwedde, F. G., & Murphy, G. M. (1932). A hydrogen isotope of mass 2. *Physical Review*, 39, 164.

ALPHA Collaboration (2017). Measurement of the 1S–2S transition frequency in antihydrogen. *Nature*, 541, 506–510.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. Chapter 4.

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. Chapter 10.

