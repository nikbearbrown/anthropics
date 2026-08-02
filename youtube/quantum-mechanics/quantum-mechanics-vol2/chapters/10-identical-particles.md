# Chapter 10 — Identical Particles

Spectroscopists in the early 1920s catalogued the helium spectrum in fine detail. They found two distinct families of lines — one called parahelium, one called orthohelium — with different transition rates, different selection rules, different fine-structure patterns. The two families looked like spectra of two different elements.

Helium is one element: nuclear charge $+2e$, two electrons, nothing else. Werner Heisenberg resolved this apparent puzzle in 1926, and his resolution required no new force and no new particle. It required asking a question nobody had thought to ask: when you write down a wave function for two electrons, what must it satisfy purely because the electrons are identical?

---

## What Identical Means

In classical mechanics, two identical billiard balls can always be tracked individually. Even without painting a dot on one, you could in principle follow both through every collision — their trajectories are continuous and you never lose track of which is which.

In quantum mechanics this fails completely. The wave function $\psi(\vec{r}_1, \vec{r}_2)$ spreads each electron over a region of space. When those regions overlap and a detector fires at some position, there is no fact in nature — not merely no practical way to determine, but no fact — about which electron triggered it. The labels "1" and "2" we write into the wave function are mathematical bookkeeping. They cannot be verified by any measurement.

The Hamiltonian confirms this. For two electrons:

$$\hat{H}(1,2) = \frac{\hat{p}_1^2}{2m_e} + \frac{\hat{p}_2^2}{2m_e} + V(\vec{r}_1) + V(\vec{r}_2) + \frac{e^2}{4\pi\epsilon_0|\vec{r}_1 - \vec{r}_2|}.$$

Swap the subscripts 1 and 2 everywhere: $\hat{H}(1,2) = \hat{H}(2,1)$. The physics does not distinguish the two labels.

Define the exchange operator $\hat{P}_{12}\,\psi(\vec{r}_1, \vec{r}_2) = \psi(\vec{r}_2, \vec{r}_1)$. Apply it twice: $\hat{P}_{12}^2 = \mathbb{1}$. The eigenvalues $\lambda$ satisfy $\lambda^2 = 1$, giving only $\lambda = +1$ or $\lambda = -1$.

Since $\hat{H}(1,2) = \hat{H}(2,1)$, we have $[\hat{H}, \hat{P}_{12}] = 0$: the exchange operator commutes with the Hamiltonian. Energy eigenstates can be chosen with definite exchange symmetry, and that symmetry is conserved under time evolution.

The empirical postulate — confirmed universally and explained by the spin-statistics theorem of relativistic quantum field theory — is:

**Bosons** have symmetric wave functions ($\hat{P}_{12}\psi = +\psi$): integer spin. Photons, the Higgs, $^4\text{He}$ atoms.

**Fermions** have antisymmetric wave functions ($\hat{P}_{12}\psi = -\psi$): half-integer spin. Electrons, protons, neutrons.

Composite particles inherit their statistics by counting constituent fermions: an even number makes a boson, an odd number makes a fermion. The consequences are dramatic. $^4\text{He}$ has 6 constituent fermions (even) and becomes superfluid at 2.17 K. $^3\text{He}$ has 5 (odd), is a fermion, and becomes superfluid only at 2.5 mK — three orders of magnitude colder, from a single parity count.

<!-- → [TABLE: Statistics of common particles — photon spin-1 boson; electron spin-1/2 fermion; proton spin-1/2 fermion (3 quarks); ⁴He spin-0 boson (6 fermions) superfluid 2.17 K; ³He spin-1/2 fermion (5 fermions) superfluid 2.5 mK; ⁸⁷Rb integer boson first dilute-gas BEC 1995] -->

![Boson and fermion classification by constituent fermion count](../images/10-identical-particles-fig-01.png)
*Figure 10.1 — Taxonomy: particles with an even number of constituent fermions are bosons (left branch, blue) while those with an odd count are fermions (right branch, orange); terminus icons show macroscopic ground-state pile-up for bosons and the Pauli exclusion stack for fermions.*

---

## Antisymmetry Built In

For two fermions in single-particle states $\phi_a$ and $\phi_b$, the antisymmetric wave function is:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_a(1)\phi_b(2) - \phi_b(1)\phi_a(2)\bigr].$$

John Slater noticed in 1929 that this is a $2\times2$ determinant:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\det\begin{pmatrix}\phi_a(1) & \phi_b(1) \\ \phi_a(2) & \phi_b(2)\end{pmatrix}.$$

Swapping particles swaps rows. Swapping rows flips the sign of a determinant. Antisymmetry is now a property of matrix structure, enforced automatically by the algebra.

![2×2 Slater determinant row-swap and sign flip](../images/10-identical-particles-fig-02.png)
*Figure 10.2 — Swapping the two particle labels (rows) in a $2\times2$ Slater determinant flips the sign (center panel); when both rows are identical, the determinant is identically zero — the Pauli exclusion principle as a theorem about determinants.*

The construction extends to $N$ fermions. Build the $N\times N$ matrix where entry $(i,j)$ is the $i$-th single-particle orbital evaluated at the $j$-th particle's coordinates. The **Slater determinant** is:

$$\psi(1,\ldots,N) = \frac{1}{\sqrt{N!}}\det\begin{pmatrix}\phi_1(1)&\phi_2(1)&\cdots&\phi_N(1)\\\phi_1(2)&\phi_2(2)&\cdots&\phi_N(2)\\\vdots&&\ddots&\vdots\\\phi_1(N)&\phi_2(N)&\cdots&\phi_N(N)\end{pmatrix}.$$

Swapping any two particles swaps two rows, flipping the sign. The $1/\sqrt{N!}$ is the normalization — all $N!$ terms in the expansion are orthogonal when the $\phi_i$ are orthonormal.

This is the wave function ansatz on which all of computational quantum chemistry is built. Hartree-Fock theory minimizes $\langle\psi|\hat{H}|\psi\rangle$ over the choice of single-particle orbitals $\{\phi_i\}$, with the $N$-electron state constrained to a single Slater determinant. Configuration interaction, coupled-cluster theory, and many density-functional approaches are corrections to or extensions of this starting point.

![N×N Slater determinant structure](../images/10-identical-particles-fig-03.png)
*Figure 10.3 — The $N\times N$ Slater determinant: diagonal cells (particle $i$ in orbital $i$, highlighted) and off-diagonal cells; any row swap flips the sign, and two identical columns produce an identically zero determinant.*

---

## Pauli Exclusion as a Theorem

Now suppose two of the single-particle orbitals are identical: $\phi_i = \phi_j$ for some $i \neq j$. Two columns of the Slater determinant are identical. A determinant with two identical columns is exactly zero — not approximately zero, not zero in some limit, identically zero everywhere in configuration space.

A wave function that is identically zero cannot be normalized. It is not a state. Two fermions cannot occupy the same single-particle orbital.

This is the **Pauli exclusion principle**. Pauli stated it in 1925 as an empirical rule — no two electrons in an atom can share the same quantum numbers $(n, \ell, m_\ell, m_s)$ — because it explained the periodic table and he could not find a reason to reject it. He received the Nobel Prize in 1945 partly for it. But as he stated it, the rule was a phenomenological postulate with no derivation. Slater showed four years later that it is a theorem about determinants, not an independent assumption.

The determinant form matters because it generalizes. The quantum numbers $(n, \ell, m_\ell, m_s)$ are labels specific to atomic orbitals. In a solid-state system the relevant labels are band indices and crystal momenta — different labels, same physics. The antisymmetry argument survives unchanged in both contexts.

---

## Worked Example — Building the Antisymmetric Two-Electron State

Put both electrons in the 1s spatial orbital of helium, with spin-orbitals $\phi_A = \psi_{100}\chi_\uparrow$ and $\phi_B = \psi_{100}\chi_\downarrow$.

**The Slater determinant:**

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_A(1)\phi_B(2) - \phi_B(1)\phi_A(2)\bigr] = \psi_{100}(\vec{r}_1)\psi_{100}(\vec{r}_2)\cdot\frac{1}{\sqrt{2}}\bigl[\chi_\uparrow(m_{s1})\chi_\downarrow(m_{s2}) - \chi_\downarrow(m_{s1})\chi_\uparrow(m_{s2})\bigr].$$

The spatial part is symmetric; the spin part is antisymmetric — the spin singlet $|S=0, M_S=0\rangle$. Total: symmetric $\times$ antisymmetric = antisymmetric. ✓

**Attempt to put both electrons in the same spin-orbital**, say $\phi_A = \phi_B = \psi_{100}\chi_\uparrow$:

$$\psi_-(1,2) = \frac{1}{\sqrt{2}}\bigl[\phi_A(1)\phi_A(2) - \phi_A(1)\phi_A(2)\bigr] = 0.$$

Identically zero. Two electrons in the 1s orbital must have opposite spins — not by postulate, but because the determinant with two identical columns is zero.

---

## Helium and the Exchange Integral

Helium's Hamiltonian is

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla_1^2 - \frac{\hbar^2}{2m_e}\nabla_2^2 - \frac{2e^2}{4\pi\epsilon_0 r_1} - \frac{2e^2}{4\pi\epsilon_0 r_2} + \underbrace{\frac{e^2}{4\pi\epsilon_0|\vec{r}_1-\vec{r}_2|}}_{V_{12}}.$$

The electron-electron repulsion $V_{12}$ makes this analytically insoluble. We treat it as a perturbation on the exactly-solved two-electron hydrogenic problem.

The total wave function must be antisymmetric. From Chapter 8, two-spin states split into a singlet (antisymmetric, $S = 0$) and a triplet (symmetric, $S = 1$). Pairing with spatial parts:

**Parahelium**: symmetric spatial $\times$ singlet spin. $S = 0$.

**Orthohelium**: antisymmetric spatial $\times$ triplet spin. $S = 1$.

Both total wave functions are antisymmetric. Both are physical. And the helium ground state is necessarily parahelium: the only $1s^2$ spatial wave function is $\phi_{1s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)$, which is symmetric, so the spin must be the singlet. The antisymmetric spatial combination $\phi_{1s}(\vec{r}_1)\phi_{1s}(\vec{r}_2) - \phi_{1s}(\vec{r}_2)\phi_{1s}(\vec{r}_1) = 0$ vanishes by Pauli — no $1s^2$ orthohelium ground state exists.

For the 1s2s excited configuration, the two antisymmetric states are:

$$\psi_\pm = \frac{1}{\sqrt{2}}\bigl[\phi_{1s}(\vec{r}_1)\phi_{2s}(\vec{r}_2) \pm \phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\bigr]\times\begin{cases}\chi_\text{singlet} & (+)\\\chi_\text{triplet} & (-)\end{cases}.$$

First-order perturbation theory gives the Coulomb correction:

$$\langle V_{12}\rangle_\pm = J \pm K,$$

where

$$J = \iint |\phi_{1s}(\vec{r}_1)|^2\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}|\phi_{2s}(\vec{r}_2)|^2\,d^3r_1\,d^3r_2$$

is the **direct integral** — the classical Coulomb energy between the two charge densities $|\phi_{1s}|^2$ and $|\phi_{2s}|^2$. A classical physicist could write this down.

$$K = \iint \phi_{1s}^*(\vec{r}_1)\phi_{2s}^*(\vec{r}_2)\frac{e^2/(4\pi\epsilon_0)}{|\vec{r}_1-\vec{r}_2|}\phi_{2s}(\vec{r}_1)\phi_{1s}(\vec{r}_2)\,d^3r_1\,d^3r_2$$

is the **exchange integral** — the cross-term generated by antisymmetrization, swapping which electron is "in 1s" and which is "in 2s." It has no classical analog whatsoever. For real orbitals and the positive Coulomb kernel $1/r_{12} > 0$, the integrand of $K$ is non-negative everywhere, so $K > 0$.

Result: parahelium 1s2s has energy $E^{(0)} + J + K$; orthohelium 1s2s has $E^{(0)} + J - K$. Since $K > 0$, orthohelium lies lower by $2K \approx 0.80$ eV — a large, observable splitting.

![Para/ortho helium energy splitting: J and K integrals](../images/10-identical-particles-fig-04.png)
*Figure 10.4 — Energy-level diagram for the helium 1s2s configuration: the parahelium singlet (orange, higher) lies above the orthohelium triplet (green, lower) by $2K \approx 0.80$ eV; brackets indicate the direct integral $J$ and exchange integral $K$ contributions.*

The mechanism, stated precisely:

$S = 1$ (triplet) requires antisymmetric spatial wave function. The antisymmetric $\psi_-$ vanishes when $\vec{r}_1 = \vec{r}_2$. Electrons in $\psi_-$ stay farther apart on average. Farther apart means less Coulomb repulsion. Lower energy.

Spin determines which spatial symmetry class is required. The spatial wave function determines how close the electrons approach. Proximity determines Coulomb repulsion. No spin-dependent force appears anywhere in this chain. What looked like two spectral families from a spin-spin interaction is entirely a consequence of the antisymmetry requirement and the geometry of wave functions.

![Spatial symmetry to Coulomb energy: three-step mechanism](../images/10-identical-particles-fig-05.png)
*Figure 10.5 — Three-step causal chain: symmetric spatial wave function (top track, orange) has high joint probability at $\vec{r}_1=\vec{r}_2$, high Coulomb repulsion, and higher energy; antisymmetric spatial (bottom track, green) has a Pauli node at coincidence, low repulsion, and lower energy.*

---

## Hund's First Rule

In 1925 Friedrich Hund catalogued an empirical regularity: for a given electron configuration in a partially filled subshell, the term with highest total spin has the lowest energy. This is Hund's first rule.

It is not a separate postulate. The mechanism is the exchange integral. Higher $S$ requires a more antisymmetric spatial wave function, which keeps electrons farther apart on average, which reduces Coulomb repulsion. The rule is a corollary of antisymmetry applied to multi-electron atoms.

Oxygen ($1s^2\,2s^2\,2p^4$): the three $2p$ orbitals hold four electrons. Hund's rule says fill each orbital with one electron (parallel spins) before pairing. The ground state has $S = 1$, two unpaired electrons, and is paramagnetic. The $S = 1$ configuration is lower in energy because its antisymmetric spatial wave function keeps the four electrons farther apart. That is why oxygen is a magnet.

---

## The Periodic Table

Three facts combine to produce the structure of the periodic table.

**Screening breaks hydrogenic degeneracy.** In a multi-electron atom, inner electrons partially shield the nuclear charge from outer electrons. Orbitals with low $\ell$ penetrate closer to the nucleus and are less effectively screened; at fixed $n$, $\text{low-}\ell$ states lie below $\text{high-}\ell$ states. The $n^2$-fold Coulomb degeneracy of hydrogen breaks. The 2s lies below 2p in lithium; the 3d lies above 4s in potassium.

**Pauli exclusion limits occupancy.** Each spin-orbital holds exactly one electron. Each spatial orbital holds at most two — one spin-up, one spin-down — and only with opposite spins. Without this, every electron in every atom would collapse to the 1s orbital. There would be no chemistry.

**Hund's rule fills partially occupied subshells.** Within a subshell, different $m_\ell$ orbitals fill with parallel spins before pairing. The exchange energy stabilizes the $\text{high-}S$ configuration.

The Aufbau principle combines all three: fill orbitals in order of increasing energy (lowest $n + \ell$ first, ties broken by lowest $n$), two electrons per orbital, parallel spins first within a subshell. The sequence is $1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, \ldots$ Row lengths $2, 8, 8, 18, 18, 32$ follow from $2(2\ell + 1)$ summed over the subshells in each period — twice the orbital degeneracy, the factor of 2 from spin.

About twenty atoms violate the Madelung energy ordering. Chromium ($3d^5\,4s^1$ rather than $3d^4\,4s^2$) and copper ($3d^{10}\,4s^1$ rather than $3d^9\,4s^2$) are the standard examples: exchange-energy stabilization of a half-filled or completely-filled 3d subshell wins against the small 3d-4s energy gap. These are not anomalies; they are cases where Hund's exchange stabilization barely beats the Madelung ordering.

The periodic table is not a catalogue of patterns. It is a theorem about antisymmetric wave functions, screened Coulomb potentials, and first-order perturbation theory.

---

## Bosons, Briefly

Bosons have symmetric wave functions. Nothing prevents any number of them from occupying the same single-particle state. At low temperature and high density, a macroscopic fraction can pile into the lowest-energy state — Bose-Einstein condensation. Cornell and Wieman achieved the first dilute-gas BEC in $^{87}\text{Rb}$ at JILA in 1995, cooling the atoms to roughly 170 nK. Nobel Prize 2001.

One misconception worth clarifying: bosons are not attracted to each other and fermions are not repelled by each other in the sense of forces. There is no term in the Hamiltonian encoding exchange statistics. What exists is a correlation in the joint probability density $|\psi(\vec{r}_1, \vec{r}_2)|^2$ from the symmetrization: fermions have a Pauli node at $\vec{r}_1 = \vec{r}_2$ (the antisymmetric wave function vanishes there); bosons have enhanced probability at $\vec{r}_1 = \vec{r}_2$ (the symmetric wave function peaks on the diagonal). The single-particle marginal density $\int|\psi|^2\,d^3r_2$ is identical for bosons, fermions, and distinguishable particles in the same pair of single-particle states. A single-particle detector cannot distinguish them.

![Joint probability density: boson, fermion, and distinguishable particles](../images/10-identical-particles-fig-06.png)
*Figure 10.6 — Three panels of $|\psi(x_1,x_2)|^2$ for two particles in a 1D well: bosons (diagonal enhancement), fermions (Pauli node along $x_1=x_2$), and distinguishable particles (no diagonal feature); the marginal density (bottom strip) is identical in all three cases.*

The fermion node also holds up dead stars. Electrons in a white dwarf cannot share single-particle states; as the star contracts, electrons are forced into higher-energy states, generating an outward degeneracy pressure with no thermal origin. Chandrasekhar showed in 1931 that this pressure has a relativistic limit at approximately $1.4\,M_\odot$ — above which no equilibrium exists and gravitational collapse is inevitable. He did this calculation at age 19 on a steamship from India to England. Nobel Prize 1983.

---

## References

- Pauli, W. (1925). "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren." *Zeitschrift für Physik*, 31, 765–783.
- Slater, J.C. (1929). "The Theory of Complex Spectra." *Physical Review*, 34, 1293–1322.
- Heisenberg, W. (1926). "Mehrköperproblem und Resonanz in der Quantenmechanik." *Zeitschrift für Physik*, 38, 411–426.
- Pauli, W. (1940). "The Connection Between Spin and Statistics." *Physical Review*, 58, 716–722.
- Chandrasekhar, S. (1931). "The Maximum Mass of Ideal White Dwarfs." *Astrophysical Journal*, 74, 81–82.
- Anderson, M.H. et al. (1995). "Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor." *Science*, 269, 198–201.
- Griffiths, D.J. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 5.
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Chapter 11.
- Sakurai, J.J. and Napolitano, J. (2021). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Chapter 7.

