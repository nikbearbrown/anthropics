# Chapter 8 — Identical Particles


## TL;DR

- Two electrons in helium are not "electron 1 and electron 2.
- The chapter moves through The exchange operator, The Slater determinant, The exchange correlation: why symmetry affects energy, Helium: where the singlet-triplet splitting comes from, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Two electrons in helium are not "electron 1 and electron 2." Forgetting that throws away the helium spectrum, the periodic table, and the white dwarf.*

---

Here is a question that sounds like it should have a simple answer. You have two electrons in a helium atom. You measure the position of one and find it at $\mathbf{r}_1$. You measure the position of the other and find it at $\mathbf{r}_2$. Now here is the question: which electron did you measure first?

You cannot answer it. Not because you forgot to label them, and not because your measuring apparatus is imprecise. The two electrons are genuinely, irreducibly indistinguishable. There is no physical procedure — no color, no tag, no trajectory you could follow — that separates "electron 1" from "electron 2." The Schrödinger equation for two electrons has the same structure when you swap their labels, and the wave function knows this. A multi-particle wave function that treats the two electrons as distinct particles is, in a precise sense, lying about the physics.

You might think this is a philosophical subtlety with no observable consequences. It is not. Whether the two-electron wave function is symmetric or antisymmetric under particle exchange determines which spin states helium's excited configurations can have, which in turn determines how often the two electrons sit close to each other, which determines the Coulomb energy by hundreds of millielectronvolts. The singlet-triplet splitting in helium — two families of states with measurably different energies, historically called parahelium and orthohelium — is an experimental fact that a theory using labeled particles cannot even express, let alone predict.

And beyond helium: without the antisymmetry constraint, every electron in every atom would pile into the $1s$ orbital. Shell structure would not exist. The periodic table would not exist. Chemistry would not exist. The indistinguishability of electrons is not a technicality. It is the foundation.

---

## The exchange operator

Define the *exchange operator* $\hat{P}_{12}$ on a two-particle wave function by

$$\hat{P}_{12}\,\psi(\mathbf{r}_1, \mathbf{r}_2) = \psi(\mathbf{r}_2, \mathbf{r}_1).$$

Two immediate consequences. First, $\hat{P}_{12}^2 = \hat{1}$ — swap the labels twice and you are back where you started — so $\hat{P}_{12}$ has eigenvalues $\pm 1$ only. Second, if the particles are truly identical, every observable must be unchanged under their exchange. In particular, the Hamiltonian must commute with the exchange operator:

$$[\hat{H}, \hat{P}_{12}] = 0.$$

Operators that commute with $\hat{H}$ can be simultaneously diagonalized with it. So we can choose energy eigenstates that are also eigenstates of $\hat{P}_{12}$ — states that are either *symmetric* ($+1$ eigenvalue) or *antisymmetric* ($-1$ eigenvalue) under exchange.

Nature then makes one more choice that quantum mechanics itself does not derive: it picks one of the two options for each particle species, permanently. Electrons, protons, neutrons, and all other half-integer-spin particles are *fermions* — their multi-particle wave functions are antisymmetric under exchange. Photons, Higgs bosons, and all other integer-spin particles are *bosons* — their wave functions are symmetric. The connection between spin and statistics is not a postulate of non-relativistic quantum mechanics but a theorem — Pauli's spin-statistics theorem, proved in 1940 [Pauli, *Physical Review* 58, 716–722](https://doi.org/10.1103/PhysRev.58.716) — that requires relativistic quantum field theory to derive. Inside non-relativistic QM, the anti/symmetric assignment is postulated. You should know the deeper theorem exists and that it requires tools we have not yet built.

| particle family | spin | exchange symmetry | examples | statistical behavior | key consequence |
| --- | --- | --- | --- | --- | --- |
| Fermions | half-integer | antisymmetric | electron, proton, neutron | Fermi-Dirac | Pauli exclusion and shell structure |
| Bosons | integer | symmetric | photon, Higgs, $^4$He atom | Bose-Einstein | condensation and coherent fields |

One note on what this postulate applies to: it is not limited to electrons that are nearby. Two electrons at opposite ends of the galaxy are still identical, and in principle the wave function across all electrons in the universe is antisymmetric under the exchange of any pair. In practice, exchange effects between electrons in distant atoms are negligible because the overlap integral between their localized orbitals is exponentially small with distance. The antisymmetry holds globally; it only *matters* locally.

And one note for completeness: in two spatial dimensions, the argument breaks down. When two particles exchange positions in 2D, the path of exchange can wind around the relative-position singularity in topologically distinct ways, and the exchange phase is not restricted to $\pm 1$ — it can be any complex number $e^{i\theta}$. Particles with such intermediate statistics are *anyons*, and they have been observed in the fractional quantum Hall effect [Bartolomei et al. 2020, *Science* 368, 173–177](https://doi.org/10.1126/science.aaz5601). The $\pm 1$ dichotomy is a property of three spatial dimensions, not of quantum mechanics in general.

---

## The Slater determinant

For $N$ identical fermions, there is a clean way to write the antisymmetric multi-particle wave function. Label the single-particle *spin-orbitals* (spatial wave function times spin state) as $\phi_1, \phi_2, \ldots, \phi_N$, and label the particles as $1, 2, \ldots, N$. The antisymmetric state is

$$\psi(1, 2, \ldots, N) = \frac{1}{\sqrt{N!}} \begin{vmatrix} \phi_1(1) & \phi_1(2) & \cdots & \phi_1(N) \\ \phi_2(1) & \phi_2(2) & \cdots & \phi_2(N) \\ \vdots & \vdots & \ddots & \vdots \\ \phi_N(1) & \phi_N(2) & \cdots & \phi_N(N) \end{vmatrix}.$$

Slater introduced this in 1929 [*Physical Review* 34, 1293–1322](https://doi.org/10.1103/PhysRev.34.1293). The determinant structure does two things automatically.

![N=3 Slater determinant ](../images/08-identical-particles-fig-01.png)
*Figure 8.1 — N=3 Slater determinant *

First, antisymmetry is built in. Swap two particle labels — that is, swap two columns of the determinant — and the determinant changes sign. That is what determinants do when you transpose two columns. No extra work needed; the algebra enforces the postulate.

Second, and this is the one that matters most for atomic physics: if two of the spin-orbitals are identical — two rows of the determinant are the same — the determinant is zero. The wave function vanishes identically. You cannot put two identical fermions in the same single-particle state, not because of a rule you learned about quantum numbers, but because the antisymmetric wave function constructed from two identical orbitals is zero. This is Pauli exclusion as a property of determinants.

For $N=2$, the Slater determinant is

$$\psi(1,2) = \frac{1}{\sqrt{2}}\left[\phi_a(1)\phi_b(2) - \phi_a(2)\phi_b(1)\right].$$

For $N=3$, with spin-orbitals $\phi_a, \phi_b, \phi_c$, the determinant expands into $3! = 6$ terms with alternating signs — every permutation of the three particles among the three orbitals, weighted by the sign of the permutation. The general $N$-particle case has $N!$ terms.

The Slater determinant is also the foundation of Hartree–Fock theory — the workhorse of computational quantum chemistry. The approximation is: assume the $N$-electron ground state is a single Slater determinant, then minimize $\langle\psi|\hat{H}|\psi\rangle$ over the choice of single-particle orbitals. Everything in computational chemistry beyond Hartree–Fock — configuration interaction, coupled cluster, density-functional theory — is a correction to the single-determinant ansatz. This is not a computational detail; it is the direct consequence of the antisymmetry postulate applied to atoms.

---

## The exchange correlation: why symmetry affects energy

Before helium, a simple example. Two non-interacting identical particles in a 1D infinite well. Particle A is in orbital $\psi_1(x)$; particle B is in orbital $\psi_2(x)$. For distinguishable particles, the joint wave function is just $\psi_1(x_1)\psi_2(x_2)$ and the joint probability density is $|\psi_1(x_1)|^2|\psi_2(x_2)|^2$.

For identical fermions with symmetric spin (both spin-up, so the spin state is symmetric), the spatial wave function must be antisymmetric:

$$\psi_A(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_1(x_1)\psi_2(x_2) - \psi_1(x_2)\psi_2(x_1)\right].$$

For identical bosons, the symmetric spatial wave function is

$$\psi_S(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_1(x_1)\psi_2(x_2) + \psi_1(x_2)\psi_2(x_1)\right].$$

Now evaluate $\langle(x_1-x_2)^2\rangle$ for each case. Expanding the squared wave functions and integrating, the cross terms produce an *exchange integral* that adds to the fermion average separation and subtracts from the boson one. The result (Griffiths §5.1.2 carries this calculation):

$$\langle(x_1-x_2)^2\rangle_\text{fermion} > \langle(x_1-x_2)^2\rangle_\text{distinguishable} > \langle(x_1-x_2)^2\rangle_\text{boson}.$$

No interaction term in the Hamiltonian has been turned on. The particles are non-interacting. The difference in average separation comes entirely from the symmetry of the spatial wave function. Fermions are statistically further apart than distinguishable particles would be; bosons are statistically closer. This is the *exchange correlation* — call it that, not an "exchange force." There is no extra term in the Hamiltonian. There is only the Coulomb force and the antisymmetry constraint on the wave function. The antisymmetry dictates how often the two electrons sit close enough for the Coulomb repulsion to matter. That is the entire mechanism behind the helium spectrum.

![No interaction. No force. Just the symmetry of the wave function.](../images/08-identical-particles-fig-02.png)
*Figure 8.2 — Three plots of |ψ(x₁, x₂)|² as a 2D*

---

## Helium: where the singlet-triplet splitting comes from

For two spin-1/2 particles, the spin states decompose into a *singlet* (antisymmetric under exchange, total spin $S=0$) and a *triplet* (symmetric under exchange, total spin $S=1$):

$$|\text{singlet}\rangle = \frac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle), \qquad |\text{triplet}\rangle \in \left\{|\!\uparrow\uparrow\rangle,\; \tfrac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle),\; |\!\downarrow\downarrow\rangle\right\}.$$

The total wave function — spatial times spin — must be antisymmetric for electrons (fermions). So:

- Spin singlet (antisymmetric) pairs with spatial symmetric: *parahelium*.
- Spin triplet (symmetric) pairs with spatial antisymmetric: *orthohelium*.

The helium ground state has both electrons in the $1s$ orbital. The only spatial wave function available from two copies of $\psi_{1s}$ is the symmetric product $\psi_{1s}(\mathbf{r}_1)\psi_{1s}(\mathbf{r}_2)$ — it is automatically symmetric, because there is only one spatial orbital. This forces the spin to be singlet. The ground state of helium is necessarily $S=0$ parahelium with no other option.

The first excited state is more interesting: one electron in $1s$ and one in $2s$. Now the spatial wave function can be either symmetric or antisymmetric:

$$\psi_\pm(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}}\left[\psi_{1s}(\mathbf{r}_1)\psi_{2s}(\mathbf{r}_2) \pm \psi_{1s}(\mathbf{r}_2)\psi_{2s}(\mathbf{r}_1)\right].$$

The $+$ combination (symmetric) pairs with spin singlet to give parahelium. The $-$ combination (antisymmetric) pairs with spin triplet to give orthohelium. Both have the same zeroth-order energy — one electron in $1s$, one in $2s$. The Coulomb repulsion $e^2/(4\pi\varepsilon_0 r_{12})$ splits them.

Compute $\langle V_{ee}\rangle$ on the two spatial states. Expanding $|\psi_\pm|^2$, the diagonal terms give the *direct (Coulomb) integral*

$$J = \int\!\!\int |\psi_{1s}(\mathbf{r}_1)|^2\,|\psi_{2s}(\mathbf{r}_2)|^2\,\frac{e^2}{4\pi\varepsilon_0 r_{12}}\,d^3r_1\,d^3r_2,$$

which is the classical Coulomb repulsion between the two charge distributions. The cross term gives the *exchange integral*

$$K = \int\!\!\int \psi_{1s}^{*}(\mathbf{r}_1)\psi_{2s}^{*}(\mathbf{r}_2)\,\frac{e^2}{4\pi\varepsilon_0 r_{12}}\,\psi_{1s}(\mathbf{r}_2)\psi_{2s}(\mathbf{r}_1)\,d^3r_1\,d^3r_2.$$

$K$ has no classical analog. It exists because the wave function is antisymmetrized — the cross term in $|\psi_\pm|^2$ is present only because of the $\pm$ structure. For real $1s$ and $2s$ orbitals, $K > 0$. The energy corrections are:

$$\langle V_{ee}\rangle_\pm = J \pm K.$$

Parahelium (symmetric spatial, $S=0$) has energy $E_0 + J + K$. Orthohelium (antisymmetric spatial, $S=1$) has energy $E_0 + J - K$. Orthohelium lies *lower* by $2K$.

Empirically: the orthohelium $1s2s$ state sits at $-59.2$ eV, the parahelium at $-58.4$ eV, a splitting of about 0.8 eV [NIST Atomic Spectra Database](https://www.nist.gov/pml/atomic-spectra-database). Orthohelium is lower, as the calculation predicts.

![Helium energy level diagram ](../images/08-identical-particles-fig-03.png)
*Figure 8.3 — Helium energy level diagram *

Notice what happened here. The spins did not interact directly — there is no $\hat{S}_1 \cdot \hat{S}_2$ term in the Hamiltonian at this order. What happened is that the spin state *forced the symmetry of the spatial wave function*, which forced how often the electrons sit near each other, which changed the Coulomb energy. The triplet has antisymmetric spatial: the electrons stay further apart, the Coulomb repulsion is reduced, the energy is lower. The spin label is a marker for the spatial symmetry sector. The Coulomb force is doing the work; the antisymmetry is channeling it.

This generalizes to *Hund's first rule*: for a given electron configuration, the term with maximum total spin lies lowest in energy. More parallel spins force more antisymmetric pieces of the spatial wave function, which keeps electrons further apart, which reduces the Coulomb repulsion. The rule is exchange physics, applied configuration by configuration. [Hund 1925, *Zeitschrift für Physik* 33, 345–371](https://doi.org/10.1007/BF01328319).

---

## The periodic table as antisymmetry plus screening

With Pauli exclusion from antisymmetry established, the architecture of the periodic table follows from three ingredients: the approximate hydrogenic energy ordering modified by electron screening, the requirement that each spin-orbital hold at most one electron, and Hund's rule for partially filled subshells.

The *Aufbau* principle is the filling recipe. The *Madelung rule* encodes the empirical filling order: fill orbitals in sequence of increasing $n + \ell$, and for equal $n + \ell$ fill in order of increasing $n$:

$$1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p, \ldots$$

The physical content is screening. An outer electron in a high-$\ell$ orbital is more effectively screened from the nucleus by the inner shells than an electron in a low-$\ell$ orbital at the same $n$, because low-$\ell$ orbitals penetrate the inner shells more deeply and experience a larger effective nuclear charge. This is why $4s$ sits below $3d$ in energy for light atoms — the $4s$ electron, despite its larger principal quantum number, penetrates the core more effectively than the $3d$ electron and is less screened.

![The Madelung diagonal-filling diagram ](../images/08-identical-particles-fig-04.png)
*Figure 8.4 — The Madelung diagonal-filling diagram *

Madelung's rule is not exact. Chromium's observed ground configuration is $[\text{Ar}]\,3d^5 4s^1$, not the predicted $3d^4 4s^2$. The half-filled $3d^5$ subshell is stabilized by exchange — five parallel spins, one per $d$-orbital, maximize the spin multiplicity and minimize the intra-subshell Coulomb energy through Hund's rule — and the $4s$–$3d$ energy gap is small enough that the exchange stabilization wins. Copper is $3d^{10} 4s^1$ for the analogous reason. There are roughly twenty such exceptions across the periodic table, concentrated in the $d$- and $f$-blocks where orbital energies become near-degenerate. The exceptions are not failures of quantum mechanics; they are places where the Madelung heuristic's approximations break down and the actual energy competition has to be computed.

Take carbon as the worked case. $Z=6$: configuration $1s^2\,2s^2\,2p^2$. The filled $1s$ and $2s$ subshells contribute nothing interesting — Pauli requires paired opposite spins and there is no choice. The $2p$ subshell has two electrons in three available orbitals ($m_\ell = -1, 0, +1$). By Hund's first rule, the two electrons go into *distinct* $m_\ell$ orbitals with *parallel* spins, total $S = 1$, spatial wave function antisymmetric in those two orbitals. The orbital angular momentum picks up $M_L = m_{\ell,1} + m_{\ell,2}$, and by Hund's second rule (maximum $L$ consistent with maximum $S$ and Pauli), the total orbital angular momentum is $L=1$. By Hund's third rule (for a less-than-half-filled subshell, minimum $J$ is the ground state), $J = |L - S| = 0$. The ground term is ${}^3P_0$. The NIST Atomic Spectra Database lists carbon's ground term as ${}^3P_0$ [NIST: C I](https://physics.nist.gov/PhysRefData/ASD/levels_form.html), with ${}^3P_1$ at $16.4\,\text{cm}^{-1}$ and ${}^3P_2$ at $43.4\,\text{cm}^{-1}$ above — fine-structure splittings of a few meV, consistent with spin-orbit coupling as a small perturbation on the much larger exchange splitting that established $S=1$ at the bottom.

The same procedure predicts the ground term of the entire first row. H: ${}^2S_{1/2}$. He: ${}^1S_0$. Li: ${}^2S_{1/2}$. Be: ${}^1S_0$. B: ${}^2P_{1/2}$. C: ${}^3P_0$. N: ${}^4S_{3/2}$. O: ${}^3P_2$. F: ${}^2P_{3/2}$. Ne: ${}^1S_0$. Every prediction checks against NIST.

---

## What the statistics look like at large scale

The antisymmetric structure of fermion wave functions has consequences far beyond atomic physics. When many fermions fill a band of single-particle states, they stack from the bottom up — each state takes at most one fermion — and at low temperature the distribution approaches a sharp step at the Fermi energy. The resulting *Fermi–Dirac distribution* is

$$\langle n_i\rangle_\text{FD} = \frac{1}{e^{(E_i - \mu)/k_BT} + 1}.$$

For bosons, the symmetric wave function allows unlimited occupation of any single state. At low temperature, bosons cascade into the ground state. The *Bose–Einstein distribution* is

$$\langle n_i\rangle_\text{BE} = \frac{1}{e^{(E_i - \mu)/k_BT} - 1}.$$

The sign in the denominator is the entire story. At high temperature and low density, the two distributions converge to the classical Maxwell–Boltzmann form. At low temperature, they diverge: bosons condense, fermions refuse to.

![One sign difference in the denominator. Two different universes at low temperature.](../images/08-identical-particles-fig-05.png)
*Figure 8.5 — Plot of ⟨n_i⟩ vs (E_i − μ)/k_BT for*

Bose–Einstein condensation in dilute gases was first observed in rubidium-87 at 170 nK by Cornell and Wieman's group at Boulder [Anderson et al. 1995, *Science* 269, 198–201](https://doi.org/10.1126/science.269.5221.198), and days later in sodium at MIT by Ketterle's group [Davis et al. 1995, *Physical Review Letters* 75, 3969](https://doi.org/10.1103/PhysRevLett.75.3969). Nobel Prize 2001.

On the fermion side: Chandrasekhar showed in 1931 [*Astrophysical Journal* 74, 81–82](https://doi.org/10.1086/143324) that the *degeneracy pressure* from a Fermi sea of electrons supports white dwarfs against gravitational collapse, up to a limiting mass of $\approx 1.4\,M_\odot$ — the Chandrasekhar limit. Above that mass, electron degeneracy pressure cannot hold, and the star collapses to a neutron star or black hole. The same antisymmetry that governs the helium spectrum governs the fate of stellar remnants.

---

## What would change my mind

The VIP and VIP-2 collaborations at Gran Sasso have searched for Pauli-violating atomic transitions in copper — transitions that would be forbidden if the antisymmetry postulate held exactly. They have placed limits on the probability of such violations at the part-per-$10^{29}$ level [Curceanu et al. 2017, *Acta Physica Polonica B* 48, 1741; verify most recent VIP-2 bound, likely 2023–2024 *Physics Letters B* or *Physical Review Letters*][verify]. A positive signal at any level would force the central postulate of this chapter to be revised. None has appeared. Separately, an integer-spin fundamental particle that behaved as a fermion would force a revision of the spin-statistics theorem and therefore of relativistic QFT. No such particle has been observed.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-identical-particles-assertions.md -->

---

## Still puzzling

**Why is the spin-statistics connection exact?** Pauli's 1940 proof runs through relativistic causality — operators at spacelike separation must commute or anticommute, depending on spin, so that measurements outside each other's light cone don't interfere. Both causality and Lorentz invariance are ingredients. Inside QFT these are non-negotiable, so the theorem is non-negotiable inside QFT. Whether QFT itself is the whole story is the harder question.

**What is happening in two dimensions?** Anyons exist because the topology of 2D particle exchange admits more than two equivalence classes of paths. The $\pm 1$ postulate is a statement about 3D topology, not about quantum mechanics. The cleanest exposition is in Wilczek's 1990 *Fractional Statistics and Anyon Superconductivity*. Whether anyon-based topological quantum computation becomes practical is a hardware question open at the time of writing.

**Why does Madelung's rule have exceptions?** The honest answer is that the exchange stabilization of half-filled and full-filled shells competes with orbital energy ordering, and there is no closed-form rule for when one wins. Computational quantum chemistry handles this by computing, not by applying a rule. The Madelung heuristic is a good first-order organizer; it is not derivable from first principles without the calculation.

**Is the universe one large antisymmetric electron wave function?** In principle, yes. In practice, the overlap between localized orbitals at macroscopic separations is exponentially small, and the exchange effects are correspondingly negligible. The global antisymmetry holds; it produces no measurable consequence outside the atomic scale. Whether it is worth thinking about cosmologically is a thought experiment rather than a physics question.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Pauli, W. "The Connection Between Spin and Statistics." *Physical Review* 58, 716–722 (1940). https://doi.org/10.1103/PhysRev.58.716
2. Slater, J. C. "The Theory of Complex Spectra." *Physical Review* 34, 1293–1322 (1929). https://doi.org/10.1103/PhysRev.34.1293
3. Bartolomei, H. et al. "Fractional statistics in anyon collisions." *Science* 368, 173–177 (2020). https://doi.org/10.1126/science.aaz5601
4. Hund, F. "Zur Deutung verwickelter Spektren..." *Zeitschrift für Physik* 33, 345–371 (1925). https://doi.org/10.1007/BF01328319
5. Anderson, M. H. et al. "Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor." *Science* 269, 198–201 (1995). https://doi.org/10.1126/science.269.5221.198
6. Davis, K. B. et al. "Bose-Einstein Condensation in a Gas of Sodium Atoms." *Physical Review Letters* 75, 3969–3973 (1995). https://doi.org/10.1103/PhysRevLett.75.3969
7. Chandrasekhar, S. "The Maximum Mass of Ideal White Dwarfs." *Astrophysical Journal* 74, 81–82 (1931). https://doi.org/10.1086/143324
8. NIST Atomic Spectra Database. https://physics.nist.gov/PhysRefData/ASD/levels_form.html
