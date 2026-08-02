# Chapter 6 — The Variational Method

*Bounding the ground state by guessing its shape — and watching the chemical bond fall out of the arithmetic.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Perturbation theory needs a small knob to turn. When there is no such knob — when the interaction is the whole problem, as it is for the electrons in helium or the binding of two protons — we need a different move. The variational method is that move, and it rests on one honest fact: for *any* normalized trial state you write down, the expectation value $\langle H \rangle$ can never sit below the true ground-state energy. It can only equal it or overshoot. So the recipe is almost cheeky in its simplicity. Guess the shape of the answer, leave a few parameters free, compute $\langle H \rangle$, and slide those parameters until the energy is as low as you can drive it. The lowest you reach is your best upper bound; the shape that reaches it is your best wave function.

The art is entirely in the guess. A Gaussian nails the harmonic oscillator exactly because the oscillator's ground state *is* a Gaussian. A hydrogenic orbital with an adjustable effective charge captures how each helium electron partly screens the nucleus from the other. And a sum of two atomic orbitals, $|A\rangle \pm |B\rangle$, gives you bonding and antibonding molecular orbitals — the chemical bond emerging from a two-term variational ansatz. We close by promoting the parameters to coefficients in a basis, which turns minimization into a generalized eigenvalue problem with an overlap matrix.

## 6 — The variational method

Notice that the correction to the energy of the He atom due to the interactions is

$$\delta E = \langle 1s1s | V | 1s1s \rangle$$

and the resulting estimate of the ground state energy is just the expectation value

$$E_{1s1s} = \langle 1s1s | H_0 | 1s1s \rangle + \langle 1s1s | V | 1s1s \rangle =$$

$$= \langle 1s1s | H | 1s1s \rangle$$

This is a first example of a "variational" calculation. The strategy is to write down a candidate ground-state wave-function controlled by a collection of tunable parameters $\{\alpha_1, \alpha_2, \dots \alpha_n\} = \{\vec{\alpha}\}$. The variational energy is then estimated as

$$E_V = \langle \psi(\{\vec{\alpha}\}) | H | \psi(\{\vec{\alpha}\}) \rangle$$

One can show that this quantity never falls below the true ground-state energy

$$E_V \geq E_0$$

The argument is short. Expand $|\psi(\{\vec{\alpha}\})\rangle$ in the eigenbasis of $\hat{H}$

$$|\psi\rangle = \sum_n \psi_n |n\rangle$$

The variational energy becomes

$$E_V = \langle \psi | \hat{H} | \psi \rangle = \sum_n |\psi_n|^2 \langle n | \hat{H} | n \rangle = \sum_n |\psi_n|^2 E_n$$

$$\rightarrow E_V \geq E_0$$

The whole game is to find a trial function flexible enough to capture the physics, so that tuning $\{\vec{\alpha}\}$ brings us as near the ground state as possible. We achieve this by minimizing $E_V$ over the $\alpha$'s. In practice, then, we look for solutions of the system

$$\frac{\partial E_V}{\partial \alpha_i} = \langle \frac{\partial \psi}{\partial \alpha_i} | H | \psi \rangle + \langle \psi | H | \frac{\partial \psi}{\partial \alpha_i} \rangle = 0$$

### Example: Ground-state of the 1d harmonic oscillator

$$\hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + \frac{1}{2} m \omega^2 x^2$$

For a "trial" function we take a Gaussian

$$\psi(x) = A e^{-bx^2}$$

The normalization constant $A$ follows from

$$1 = \int_{-\infty}^{\infty} |\psi(x)|^2 \, dx = |A|^2 \int_{-\infty}^{\infty} e^{-2bx^2} \, dx = |A|^2 \sqrt{\frac{\pi}{2b}}$$

$$\rightarrow A = \left(\frac{2b}{\pi}\right)^{1/4}$$

Now, $\langle H \rangle = \langle T \rangle + \langle V \rangle$

$$\langle T \rangle = -\frac{\hbar^2}{2m} |A|^2 \int_{-\infty}^{\infty} e^{-bx^2} \frac{d^2}{dx^2}\left(e^{-bx^2}\right) = \frac{\hbar^2 b}{2m}$$

$$\langle V \rangle = \frac{1}{2} m \omega^2 |A|^2 \int_{-\infty}^{\infty} e^{-bx^2} x^2 \, dx = \frac{m\omega^2}{8b}$$

$$\langle H \rangle = \frac{\hbar^2 b}{2m} + \frac{m\omega^2}{8b}$$

We minimize $\langle H \rangle$:

$$\frac{d}{db}\langle H \rangle = \frac{\hbar^2}{2m} - \frac{m\omega^2}{8b^2} = 0 \rightarrow b = \frac{m\omega}{2\hbar}$$

$$\rightarrow E_V = \frac{1}{2} \hbar \omega$$

The result is exact here for a simple reason: the actual ground state happens to be a Gaussian. Gaussians are favorites precisely because they are so convenient to integrate.

### Example: Delta function potential

$$H = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} - \alpha \delta(x)$$

We keep the same trial function. The kinetic energy was already computed in the previous example

$$\langle V \rangle = -\alpha |A|^2 \int_{-\infty}^{\infty} e^{-2bx^2} \delta(x) \, dx = -\alpha \sqrt{\frac{2b}{\pi}}$$

$$\rightarrow \langle H \rangle = \frac{\hbar^2 b}{2m} - \alpha \sqrt{\frac{2b}{\pi}}$$

$$\frac{d\langle H\rangle}{db} = \frac{\hbar^2}{2m} - \frac{\alpha}{\sqrt{2\pi b}} = 0 \rightarrow b = \frac{2m^2 \alpha^2}{\pi \hbar^4} \rightarrow E_V = -\frac{m\alpha^2}{\pi \hbar^2}$$

$$E_V > E_{gs} = -m\alpha^2 / 2\hbar^2$$

### Example: Ground state of Helium

We choose $|\psi\rangle = |100(\tilde{z})\rangle \, |100(\tilde{z})\rangle$, with

$$\psi(\vec{r}) = \langle \vec{r} | 100(\tilde{z}) \rangle = \frac{1}{\sqrt{\pi}} \left(\frac{\tilde{z}}{a_0}\right)^{3/2} e^{-\tilde{z} r / a_0}$$

Evaluating $\langle H \rangle$ is simpler once we regroup the Hamiltonian

$$\hat{H} = \frac{\hat{p}_1^2}{2m} + \frac{\hat{p}_2^2}{2m} - \frac{Ze^2}{|\vec{r}_1|} - \frac{Ze^2}{|\vec{r}_2|} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|} =$$

$$= \left[ \frac{\hat{p}_1^2}{2m} - \frac{\tilde{z}e^2}{|\vec{r}_1|} + \frac{\hat{p}_2^2}{2m} - \frac{\tilde{z}e^2}{|\vec{r}_2|} \right] + \frac{(\tilde{z}-Z)e^2}{|\vec{r}_1|} + \frac{(\tilde{z}-Z)e^2}{|\vec{r}_2|} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

The expectation value is now straightforward to obtain

$$\langle H \rangle = \frac{1}{2} m_e c^2 \alpha^2 \left( -2\tilde{z}^2 + 4\tilde{z}(\tilde{z}-Z) + \frac{5}{4}\tilde{z} \right)$$

$$= \frac{1}{2} m_e c^2 \alpha^2 \left( 2\tilde{z}^2 - 4Z\tilde{z} + \frac{5}{4}\tilde{z} \right)$$

Minimizing

$$\frac{\partial \langle H \rangle}{\partial \tilde{z}} = 0 \rightarrow \tilde{z} = Z - \frac{5}{16}$$

$$\rightarrow E_V = -\frac{1}{2} m_e c^2 \alpha^2 \left[ 2\left(Z - \frac{5}{16}\right)^2 \right] = -77.4 \text{ eV}$$

which sits much nearer the measured value of $-78.8$ eV. We set $Z=2$ in this expression. The point is that the wave function builds in the fact that each electron sees an effective nuclear charge partly shielded by the other electron.

### Excited states

Note that if we pick a trial wave function orthogonal to the ground state

$$\langle \psi | \psi_{gs} \rangle = 0$$

then $E_V \geq E_1$, so we can estimate the first excited state as well. One way to enforce this is to place the trial state in a different symmetry sector (for instance, using different values of $n$ in the helium case).

## 6.2 The Hydrogen molecule ion

The $H_2^+$ molecule has the shape of a dumbbell. We work in the rotating frame and pin the nuclei at fixed positions separated by a distance $R$. We also neglect nuclear vibrations, since the nuclei move far more sluggishly than the electrons. This is the well-known "Born-Oppenheimer" approximation. Treating $R$ as a variational parameter lets us extract both the molecule's size and its energy.

This is a one-electron problem. When the atoms are far apart, $R \to \infty$, the electron sits on either atom 1 or atom 2. Bringing them together lets the wave function spread out. A natural trial function is a linear combination of hydrogenic 1s states, one centered on each nucleus

$$\langle r | A \rangle = \frac{1}{\sqrt{\pi a_0^3}} e^{-|\vec{r} - \vec{R}/2| / a_0}$$

$$\langle r | B \rangle = \frac{1}{\sqrt{\pi a_0^3}} e^{-|\vec{r} + \vec{R}/2| / a_0}$$

$$\hat{H} = \frac{\hat{p}^2}{2m_e} - \frac{e^2}{|\vec{r} - \vec{R}/2|} - \frac{e^2}{|\vec{r} + \vec{R}/2|} + \frac{e^2}{R} \quad \text{(proton-proton)}$$

$$H_{AA} = \langle A | H | A \rangle = \langle A | \frac{\hat{p}^2}{2m_e} - \frac{e^2}{|\vec{r} - \vec{R}/2|} | A \rangle - \langle A | \frac{e^2}{|\vec{r} + \vec{R}/2|} | A \rangle + \frac{e^2}{R}$$

$$= E_1 - \int d^3 r \, \frac{e^2}{|\vec{r} + \vec{R}/2|} |\langle r | A \rangle|^2 + \frac{e^2}{R}$$

Symmetry alone tells us, with no further computation, that $H_{BB} = H_{AA}$

$$H_{AB} = \langle A | H | B \rangle = \langle A | \frac{p^2}{2m_e} - \frac{e^2}{|\vec{r} - \vec{R}/2|} | B \rangle - \langle A | \frac{e^2}{|\vec{r} + \vec{R}/2|} | B \rangle + \frac{e^2}{R} \langle A | B \rangle$$

$$= E_1 \langle A | B \rangle - \langle A | \frac{e^2}{|\vec{r} + \vec{R}/2|} | B \rangle + \frac{e^2}{R} \langle A | B \rangle$$

where $\langle A | B \rangle = S_{AB}$ is known as the "overlap integral".

The molecule's reflection symmetry about the origin suggests a variational solution, much as the permutation operator did earlier. The ground state ought to be unchanged under a reflection, equivalently under exchanging the indices 1,2.

$$R | \psi \rangle = e^{i\delta} | \psi \rangle$$

But $R^2 \equiv \mathbb{1} \rightarrow e^{i\delta} = \pm 1$

So there are two candidate solutions:

$$|\pm\rangle = \frac{1}{\sqrt{2 \pm 2 S_{AB}}} \left[ |A\rangle \pm |B\rangle \right]$$

where the extra piece in the normalization comes from $|1\rangle$ and $|2\rangle$ not being orthogonal.

The expectation values work out to

$$E_\pm = \frac{1}{1 \pm S_{AB}} \left( H_{AA} \pm H_{AB} \right)$$

*[Plot: two wave functions over the interval; $|+\rangle$ (peaked/cusped at both $-R/2$ and $R/2$, even) above, $|-\rangle$ (odd, antisymmetric about origin) below, with markers at $-R/2$ and $R/2$.]*

Only the even-parity function $|+\rangle$ has a minimum, occurring at a separation of 1.3 Å. For this reason $|+\rangle$ is called the "bonding" orbital and $|-\rangle$ the "anti-bonding" one. Such "molecular orbitals" are linear combinations of atomic orbitals — the so-called "LCAO" technique.

*[Plot: $E$(eV) vs $R$(Å). Curve $E_-$ approaches $2E_1$ from above (no minimum, antibonding). Curve $E_+$ has a minimum below (bonding). Both approach the asymptote $2E_1$ at large $R$.]*

## 6.3 The Hydrogen molecule

As before, we write the Hamiltonian

$$\hat{H} = \frac{\hat{p}_1^2}{2m_e} - \frac{e^2}{|\vec{r}_1 - \vec{R}/2|} - \frac{e^2}{|\vec{r}_1 + \vec{R}/2|} + \frac{\hat{p}_2^2}{2m_e} - \frac{e^2}{|\vec{r}_2 - \vec{R}/2|} - \frac{e^2}{|\vec{r}_2 + \vec{R}/2|}$$

$$+ \frac{e^2}{R} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

where the final term $V(|\vec{r}_1 - \vec{r}_2|) = \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$ captures the electron-electron interaction

### Molecular orbitals

A first attempt reuses the MO's obtained for $H_2^+$

$$|\pm\rangle = \frac{1}{\sqrt{2(1 \pm S)}} \left( |A\rangle \pm |B\rangle \right)$$

We begin by building Slater determinants from these MO's, now including spin. Take the singlet state, for example. Since $|+\rangle$ came out lower in energy for $H_2^+$, we use

$$|\psi\rangle = \frac{1}{\sqrt{2}} |+\rangle_1 |+\rangle_2 \left( |\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle \right)$$

The variational energy is then

$$\langle \psi | \hat{H} | \psi \rangle = \langle \psi | \hat{H}_1 | \psi \rangle + \langle \psi | \hat{H}_2 | \psi \rangle + \langle \psi | \hat{V} | \psi \rangle + \frac{e^2}{R}$$

$$= \mathcal{E}_0 + \mathcal{E}_0 + J_{AO} + \frac{e^2}{R}$$

### Valence bond picture

Now expand $|\psi\rangle$ over the AO's

$$|\psi\rangle = \frac{1}{2(1+S)} \left( |A\rangle_1 + |B\rangle_1 \right) \left( |A\rangle_2 + |B\rangle_2 \right) |\chi_S\rangle$$

$$= \frac{1}{2(1+S)} \left( |A\rangle_1 |A\rangle_2 + |A\rangle_1 |B\rangle_2 + |A\rangle_2 |B\rangle_1 + |B\rangle_1 |B\rangle_2 \right) |\chi_S\rangle$$

The 2nd and 3rd terms are the "covalent" configurations, the ones that produce the chemical bond. The first and last are the "ionic" configurations, with both electrons in the same orbital. These ionic pieces carry higher energy because of the strong Coulomb repulsion of two electrons sharing one AO. Ideally we would like to adjust the relative weights of these contributions!

The valence bond picture simply drops the ionic configurations.

$$|\psi\rangle = \frac{1}{\sqrt{2(1+S^2)}} \left( |A\rangle_1 |B\rangle_2 + |A\rangle_2 |B\rangle_1 \right) |\chi_S\rangle$$

(Verify the normalization as exercise)

The energy of this state is then

$$\langle \psi | \hat{H} | \psi \rangle = 2 \langle \psi | \hat{H}_1 | \psi \rangle + \langle \psi | \hat{V} | \psi \rangle + \frac{e^2}{R}$$

$$= 2 \frac{\left( \mathcal{E}_0 + S \langle A | \hat{H}_1 | B \rangle \right)}{(1 + S^2)} + \frac{J + k}{(1 + S^2)} + \frac{e^2}{R}$$

*[Plot: $E$ vs $R$. Dashed curve labeled MO (higher minimum), dotted/solid curves labeled VB and exact (lower minima). Arrow indicates "Extra pot. energy from ionic configs." between the MO and VB/exact curves.]*

## 6.4 Generalized eigenvalue problem

Often the trial wave function is built as a linear combination of basis states, as we just did for $H_2^+$. In that case

$$|\psi\rangle = \sum_n \psi_n |n\rangle$$

Here we may regard the coefficients $\psi_n$ as the variational parameters, with the basis covering only part of the Hilbert space.

$$\langle H \rangle = \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle} = \frac{\sum_{nm} \psi_n^* \psi_m \langle n | H | m \rangle}{\sum_{nm} \psi_n^* \psi_m S_{nm}} = \frac{\sum_{nm} \psi_n^* \psi_m H_{nm}}{\sum_{nm} \psi_n^* \psi_m S_{nm}}$$

where $S_{nm} = \langle n | m \rangle$. The best solution comes from solving the equations

$$\frac{\partial \langle H \rangle}{\partial \psi_n^*} = \frac{\sum_m \psi_m \left[ H_{nm} \left( \sum_{n'm'} \psi_{n'}^* \psi_{m'} S_{n'm'} \right) - S_{nm} \left( \sum_{n'm'} \psi_{n'}^* \psi_{m'} H_{n'm'} \right) \right]}{\left( \sum_{nm} \psi_n^* \psi_m S_{nm} \right)^2}$$

Collecting terms gives

$$\frac{\sum_m \psi_m H_{nm} - E \sum_m \psi_m S_{nm}}{\sum_{nm} \psi_n^* \psi_m S_{nm}} = 0$$

which requires the numerator to vanish

$$\sum_m^N \left( H_{nm} - E S_{nm} \right) \psi_m = 0 \qquad n = 1, \dots, N$$

This is a generalized eigenvalue problem:

$$\bar{\bar{H}} \vec{\psi} = E \bar{\bar{S}} \vec{\psi}$$

with $\bar{\bar{H}}$ the Hamiltonian matrix and $\bar{\bar{S}}$ the "overlap matrix". What sets it apart from an ordinary eigenvalue problem is the appearance of $\bar{\bar{S}}$. We solve it by locating the roots of the secular determinant

$$\begin{vmatrix} H_{11} - E S_{11} & H_{12} - E S_{12} & \cdots & H_{1n} - E S_{1n} \\ H_{21} - E S_{21} & H_{22} - E S_{22} & \cdots & H_{2n} - E S_{2n} \\ \vdots & \vdots & & \vdots \\ H_{N1} - E S_{N1} & H_{N2} - E S_{N2} & \cdots & H_{nn} - E S_{nn} \end{vmatrix} = 0$$

When the basis is orthonormal, $S_{nm} = \delta_{nm}$ and the usual eigenvalue problem returns.

It is fair to ask: are we then solving the problem exactly? Only if the basis set is complete. In practice we want the basis as small as we can manage, to keep the calculation tractable.

### Example: The infinite potential well

$$V(x) = \begin{cases} \infty & \text{for } |x| > a \\ 0 & \text{for } |x| \leq a \end{cases}$$

The solutions must therefore vanish at $x = \pm a$. We set $a=1$ and adopt natural units with $\hbar / 2m = 1$

A convenient choice is a polynomial basis

$$\psi_n(x) = x^n (x-1)(x+1) \quad ; \quad n = 0, 1, 2, \dots$$

The overlap matrix is computed without difficulty

$$S_{nm} = \int_{-1}^{1} \psi_n(x) \psi_m(x) \, dx = \frac{2}{m+n+5} - \frac{4}{m+n+3} + \frac{2}{n+m+1}$$

for $n+m$ even, zero otherwise

The Hamiltonian matrix elements are

$$H_{nm} = \langle n | \hat{P}^2 | m \rangle = \int_{-1}^{1} \psi_n(x) \left( -\frac{d^2}{dx^2} \right) \psi_m(x)\, dx$$

$$= -8 \left[ \frac{1 - m - n - 2mn}{(n+m+3)(n+m+1)(n+m-1)} \right]$$

for $m+n$ even, zero otherwise.

The problem then has to be solved numerically, with accuracy gained by retaining more basis states.

For illustration, let us keep only two states, $n = 0, 1$.

$$S_{00} = \frac{2}{5} - \frac{4}{3} + 2 = \frac{16}{15} \quad ; \quad H_{00} = \frac{8}{3}$$

$$S_{11} = \frac{2}{7} - \frac{4}{5} + \frac{2}{3} = \frac{16}{105} \quad ; \quad H_{11} = \frac{-8(-3)}{5 \cdot 3 \cdot 1} = \frac{8}{5} \quad ; \quad S_{01} = H_{01} = 0$$

$$\begin{vmatrix} \dfrac{8}{3} - \dfrac{16}{5}E & 0 \\[2mm] 0 & \dfrac{8}{5} - \dfrac{16}{105}E \end{vmatrix} = 0 \;\Rightarrow\; \frac{8}{3} - \frac{16}{15}E = 0 \;\Rightarrow\; E = \frac{15}{16} \cdot \frac{8}{3} = \frac{5}{2}$$

$$E_{\text{exact}} = \frac{\pi^2}{4} \approx 2.46$$

### Example: Hydrogen atom with Gaussians

It helps to work in "standard units"

- unit of distance : $a_0$
- unit of mass : $m_e$
- unit of energy : $m_e c^2 \alpha^2$ (Hartree)

The Schrödinger eq. then reads

$$\left[ -\frac{1}{2}\nabla^2 - \frac{1}{r} \right] \psi(x) = E\psi(x)$$

We want the ground state. Take a Gaussian basis

$$\chi_p(r) = e^{-\alpha_p r^2}$$

with

$$\alpha_1 = 13.00773$$
$$\alpha_2 = 1.962079$$
$$\alpha_3 = 0.444529$$
$$\alpha_4 = 0.1219492$$

The matrix elements are

$$S_{pq} = \int d^3r\; e^{-\alpha_p r^2} e^{-\alpha_q r^2} = \left( \frac{\pi}{\alpha_p + \alpha_q} \right)^{3/2}$$

$$T_{pq} = \int d^3r\; e^{-\alpha_p r^2} \nabla^2 e^{-\alpha_q r^2} = 3\, \frac{\alpha_p \alpha_q \pi^{3/2}}{(\alpha_p + \alpha_q)^{5/2}}$$

$$V_{pq} = \int d^3r\; e^{-\alpha_p r^2} \frac{1}{r} e^{-\alpha_q r^2} = -\frac{2\pi}{(\alpha_p + \alpha_q)}$$

With these, the problem is solved numerically to give

$$E_v = -0.499278\; E_H$$

The exact result is

$$E_{\text{exact}} = -\frac{1}{2} E_H$$

[blank page]

[blank page]

[blank page]


---

## References and Further Reading

*Editorial addition. The variational treatment of helium and of the hydrogen molecules is developed most fully in the companion texts below.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., introduces the approximation methods in Ch. 11 (Time-Independent Perturbations).

**Further reading.** Griffiths & Schroeter, *Introduction to Quantum Mechanics*, the "Variational Principle" chapter (the ground state of helium and the hydrogen-molecule ion H₂⁺); Sakurai & Napolitano, the variational-method section of the "Approximation Methods" chapter; Shankar, *Principles of Quantum Mechanics*, Ch. 16; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Complement E_XI.
