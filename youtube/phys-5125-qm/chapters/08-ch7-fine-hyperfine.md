# Chapter 7 — Fine and Hyperfine Structure

*The tiny corrections that pry a single spectral line apart into many.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

If you solve hydrogen with the plain Coulomb Hamiltonian, every line lands exactly where Bohr said it would. Look closer with a good spectrometer and the lines aren't single — they're bundles, split by gaps a thousand times finer than the gross structure. This chapter is about where those gaps come from and, just as important, how to keep track of them.

Two effects do most of the splitting. The hyperfine interaction couples the electron's spin to the proton's spin: $\vec{S}\cdot\vec{I}$. Spin-orbit coupling couples the electron's spin to its own orbital motion: $\vec{L}\cdot\vec{S}$. Both are small dot products of angular momenta sitting on top of a much bigger energy, so first-order perturbation theory is exactly the right tool.

The honest punchline is bookkeeping. A dot product like $\vec{S}\cdot\vec{I}$ is annoying in the uncoupled basis but trivial once you build the total angular momentum $\vec{F} = \vec{S} + \vec{I}$, because $2\vec{S}\cdot\vec{I} = F^2 - S^2 - I^2$ is diagonal. Adding angular momenta — and the Clebsch–Gordan coefficients that translate between bases — is the machinery that turns messy matrices into eigenvalues you can read off. We close with Landau–Zener tunnelling, where the adiabatic theorem is pushed until it yields an exact, non-perturbative answer.

## The hyperfine structure of H

The hyperfine interaction arises from the coupling between the spin of the nuclear proton and the spin of the electron orbiting it. We skip the derivation and simply quote the result,

$$\hat{H}_{hf} = \frac{A}{\hbar^2}\, \vec{S} \cdot \vec{I} \qquad \vec{S}, \vec{I}:\ \text{spin } 1/2$$

with

$$A = \frac{2\mu_0}{3}\, g_e \mu_B g_p \mu_N\, |\psi_{1s}(0)|^2$$

where

$$\mu_B = \frac{e\hbar}{2m_e} \qquad \text{Bohr magneton}$$

$$g_e \approx 2 \qquad \text{gyromagnetic ratio of the electron}$$

$$\mu_N = \frac{e\hbar}{2m_p} \qquad \text{nuclear magneton}$$

$$g_p \approx 5.59 \qquad \text{gyromagnetic ratio of the proton}$$

The spatial and spin parts of the wave function factorize and can be handled independently.

$$\langle r | \psi_{1s} \rangle = \psi_{1s}(r_1, \theta_1, \varphi_1) |\sigma\rangle_e |\sigma_I\rangle$$

The unperturbed Hamiltonian $H_0$ acts only on the spatial part, whereas the hyperfine term acts only on the spin. The perturbation can therefore be analyzed entirely within the space of spin configurations.

We have already encountered the problem of two spins $S = 1/2$. The configurations are $\{|\uparrow\uparrow\rangle; |\uparrow\downarrow\rangle; |\downarrow\uparrow\rangle; |\downarrow\downarrow\rangle\}$ and the Hamiltonian matrix

$$H_{hf} = A \begin{pmatrix} 1/4 & & & \\ & -1/4 & 1/2 & \\ & 1/2 & -1/4 & \\ & & & 1/4 \end{pmatrix}$$

with eigenstates $|\pm\rangle = \frac{1}{\sqrt{2}}\left( |\uparrow\downarrow\rangle \pm |\downarrow\uparrow\rangle \right)$; $|\uparrow\uparrow\rangle$; $|\downarrow\downarrow\rangle$ and energies

$$E_+ = E_{\uparrow\uparrow} = E_{\downarrow\downarrow} = A/4$$
$$E_- = -\frac{3A}{4}$$

Inserting $|\psi_{1s}(0)|^2 = 1/\pi a_0^3$, the ground state splits into its spin eigenstates

[diagram: $1s$ level splits into upper level $A/4$ corresponding to $|\uparrow\uparrow\rangle, |+\rangle, |\downarrow\downarrow\rangle$, and lower level $3/4\,A$ below, corresponding to $|-\rangle$]

## Total spin of the Hydrogen atom

$$\vec{F} = \vec{S} + \vec{I}$$

$$[\hat{F}_x, \hat{F}_y] = [\hat{S}_x + \hat{I}_x,\ \hat{S}_y + \hat{I}_y] = i\hbar(\hat{S}_z + \hat{I}_z) = i\hbar \hat{F}_z$$

$$\hat{F}_\pm = \hat{S}_\pm + \hat{I}_\pm$$

$$\hat{F}^2 = (\vec{S} + \vec{I})^2 = \vec{S}^2 + \vec{I}^2 + 2\vec{S}\cdot\vec{I} \qquad \circledast$$

$$[\hat{F}_i, \hat{F}_z] = 0$$

Because $\vec{F}$ obeys the angular-momentum algebra, we expect to find states $|F, M_F\rangle$ that are simultaneous eigenstates of $\hat{F}^2$ and $\hat{F}_z$. From $\circledast$ we obtain

$$\hat{F}^2 = \frac{3\hbar^2}{4} + \frac{3\hbar^2}{4} + 2\vec{S}\cdot\vec{I} = \frac{3\hbar^2}{2} + 2\vec{S}\cdot\vec{I}$$

which, up to an additive and a multiplicative constant, is just the hyperfine interaction $H_{hf}$.

$$[\hat{F}^2, H_{hf}] = 0$$

so the two operators share a set of eigenvectors

| $|\sigma\rangle$ | $F$ | $M_F$ | |
|---|---|---|---|
| $|-\rangle$ | 0 | 0 | singlet |
| $|\downarrow\downarrow\rangle$ | 1 | $-1$ | triplet |
| $|+\rangle$ | 1 | 0 | triplet |
| $|\uparrow\uparrow\rangle$ | 1 | 1 | triplet |

Hence, combining two spins $1/2$ produces the allowed values $F = S + I = 0, 1$.

The projections of the new states onto the original basis are the "Clebsch–Gordan" coefficients.

| | $|1,-1\rangle$ | $|10\rangle$ | $|11\rangle$ | $|00\rangle$ |
|---|---|---|---|---|
| $|\downarrow\downarrow\rangle$ | 1 | 0 | 0 | 0 |
| $|\uparrow\downarrow\rangle$ | 0 | $1/\sqrt{2}$ | 0 | $1/\sqrt{2}$ |
| $|\downarrow\uparrow\rangle$ | 0 | $+1/\sqrt{2}$ | 0 | $-1/\sqrt{2}$ |
| $|\uparrow\uparrow\rangle$ | 0 | 0 | 1 | 0 |

In the new basis,

$$\hat{H}_{hf} = \frac{A}{2}\left( \hat{F}^2 - \hat{S}^2 - \hat{I}^2 \right)$$

$$H_{hf} = -\frac{3A}{4} + \frac{A}{2}\begin{pmatrix} 0 & & & \\ & 1 & & \\ & & 1 & \\ & & & 1 \end{pmatrix} = A\begin{pmatrix} -3/4 & & & \\ & 1/4 & & \\ & & 1/4 & \\ & & & 1/4 \end{pmatrix}$$

## Addition of generalized angular momenta

Let us build a recipe for generating every eigenstate of the operator $F$ from the ladder operators $L^+, L^-$. For intuition, we revisit the previous example. Begin with the state $|\uparrow\uparrow\rangle$

$$F^+|\uparrow\uparrow\rangle = F^+|11\rangle = \sqrt{2}\hbar |10\rangle$$
$$F^-|10\rangle = \sqrt{2}\hbar |1-1\rangle$$

$$F^-:\quad |11\rangle \rightarrow |10\rangle \rightarrow |1-1\rangle$$

Since $F^-$ only shifts the quantum number $M_F$, it can never reach $|00\rangle$. But note that

$$F^-|11\rangle = (S^- + I^-)|\uparrow\uparrow\rangle = \hbar\left( |\downarrow\uparrow\rangle + |\uparrow\downarrow\rangle \right)$$

So to construct $|00\rangle$ we simply need the state orthogonal to $|10\rangle$, which must be

$$|00\rangle = \frac{1}{\sqrt{2}}\left( |\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle \right)$$

[diagram:
$|11\rangle$
$\;\downarrow F^-$
$|10\rangle \overset{\text{orthogonality}}{\longrightarrow} |00\rangle$
$\;\downarrow F^-$
$|1-1\rangle$]

Alternating $F^-$ with orthogonalization in this way generates the complete set of eigenstates of $F$.

The general situation involves two coupled angular momenta

$$\vec{J} = \vec{J}_1 + \vec{J}_2$$

In the "uncoupled" basis, states carry the labels $|j_1 j_2 m_1 m_2\rangle$, while in the coupled basis they read $|j_1 j_2, J, M\rangle$. The uncoupled states are eigenstates of $J_1^2, J_2^2, J_{1z}, J_{2z}$, and the coupled states are eigenstates of $J_1^2, J_2^2, J^2, J_z$. Since $j_1$ and $j_2$ are fixed in any given problem (say, a spin 1 and a spin 1/2), we can drop those labels and just write $|JM\rangle$ for the coupled states.

### Example

| | |
|---|---|
| $|11\rangle$ | $|\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}\rangle$ |
| $|10\rangle$ | $\frac{1}{\sqrt{2}}\left( |\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\rangle + |\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\rangle \right)$ |
| $|1-1\rangle$ | $|\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, -\frac{1}{2}\rangle$ |
| $|00\rangle$ | $\frac{1}{\sqrt{2}}\left( |\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\rangle - |\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\rangle \right)$ |

In general, $J$ runs between the two extremes in unit steps: $J = j_1 + j_2,\ j_1 + j_2 - 1, \cdots, |j_1 - j_2|$

with $M = -J, -J+1, \dots, J-1, J$.

To switch between the two bases we use the Clebsch–Gordan coefficients, which have been tabulated for arbitrary $J$.

$$|JM\rangle = \sum_{m_1 = -j_1}^{j_1} \sum_{m_2 = -j_2}^{j_2} \left( |j_1 j_2 m_1 m_2\rangle \langle j_1 j_2 m_1 m_2| \right) |JM\rangle$$

$$= \sum_{m_1 = -j_1}^{j_1} \sum_{m_2 = -j_2}^{j_2} \langle j_1 j_2 m_1 m_2 | JM\rangle\, |j_1 j_2 m_1 m_2\rangle$$

$$= \sum_{m_1 = -j_1}^{j_1} \sum_{m_2 = -j_2}^{j_2} C^{j_1 j_2 J}_{m_1 m_2 M}\, |j_1 j_2 m_1 m_2\rangle$$

The C–G coefficients are real, so the inverse transformation is just the transpose.

$$|j_1 j_2 m_1 m_2\rangle = \sum_{J = |j_1 - j_2|}^{j_1 + j_2} \sum_{M = -J}^{J} |JM\rangle \langle JM | j_1 j_2 m_1 m_2\rangle$$

$$= \sum_{J = |j_1 - j_2|}^{j_1 + j_2} \sum_{M = -J}^{J} C^{j_1 j_2 J}_{m_1 m_2 M}\, |JM\rangle\, \delta_{M, m_1 + m_2}$$

$$= \sum_{J = |j_1 - j_2|}^{j_1 + j_2} C^{j_1 j_2 J}_{m_1 m_2 M}\, |JM\rangle$$

## Angular momentum and spectroscopic notation

The electron's total angular momentum is usually written $\vec{J}$

$$\vec{J} = \vec{L} + \vec{S}$$

Since the electron carries spin $S = 1/2$, we have

$$j = \ell + \frac{1}{2}\, |\ell + \frac{1}{2} - 1| = \begin{cases} \ell + \frac{1}{2},\ \ell - \frac{1}{2} & \ell \geq 1 \\ 1/2 & \ell = 0 \end{cases}$$

For atoms with more than one electron we sum all orbital and spin angular momenta, $J = L + S$. The atomic state is recorded in "spectroscopic notation"

$$^{2S+1}L_J$$

$$L = 0, 1, 2, 3, 4, 5, 6, 7$$
$$\text{letter} = S, P, D, F, G, H, I, K$$

### Examples:

ground-state of H : $^2S_{1/2}$

carbon has $L = 1, S = 0, J = 0$ : $^3P_0$

## Spin-orbit coupling

To see where spin-orbit coupling comes from, step into the electron's rest frame. From there, the electron sits at the origin and the proton sweeps around it like a current loop, generating a magnetic field. That field then couples to the electron's own spin magnetic moment.

[diagram: a loop with magnetic field $\vec{B}$ pointing up at center, electron $e^-$ at center, proton orbiting at radius $\vec{r}$]

At the center of the loop the magnetic field is

$$B = \frac{\mu_0 I}{2r}$$

The proton's speed in the electron frame equals the electron's speed in the proton frame

$$L = mvr \quad ; \quad v = \frac{L}{mr}$$

Writing the current as $I = \frac{e}{T}$ with period $T = 2\pi r/v$, we get

$$B = \frac{\mu_0}{2r}\frac{e}{T} = \frac{\mu_0}{2r}\frac{ev}{2\pi r} = \frac{\mu_0}{2r}\frac{eL}{2\pi r m r}$$

$$\Rightarrow \vec{B} = \frac{e\vec{L}}{4\pi \varepsilon_0 m c^2 r^3}$$

The interaction energy of a magnetic dipole in a magnetic field is

$$E = -\vec{\mu}\cdot\vec{B} \qquad \text{with}\quad \vec{\mu} = -\frac{e}{m}\vec{S}$$

$$\Rightarrow \hat{H}_{SO} = \frac{e^2}{4\pi\varepsilon_0 m^2 c^2 r^3}\, \hat{\vec{L}}\cdot\hat{\vec{S}}$$

It is convenient to switch to the total angular momentum basis

$$\vec{J} = \vec{L} + \vec{S}$$

$$J^2 = L^2 + S^2 - 2\vec{L}\cdot\vec{S}$$

$$\Rightarrow \vec{L}\cdot\vec{S} = \frac{1}{2}\left( J^2 - L^2 - S^2 \right)$$

The states are labeled by their quantum numbers

$$|n, \ell, s, j, m_j\rangle$$

with $j = \ell + s,\ \ell + s - 1,\ \dots,\ |\ell - s|$

The first-order energy correction from spin-orbit coupling is fixed by the matrix elements

$$\left\langle n\ell s j, m_j \left| \frac{\vec{L}\cdot\vec{S}}{r^3} \right| n\ell s j, m_j \right\rangle$$

$$= \left\langle \frac{1}{r^3} \right\rangle_{n\ell} \langle \ell s j, m_j | \vec{L}\cdot\vec{S} | \ell s j, m_j \rangle$$

$$= \frac{1}{2}\left\langle \frac{1}{r^3} \right\rangle_{n\ell} \langle \ell s j, m_j | J^2 - L^2 - S^2 | \ell s j, m_j \rangle$$

$$= \frac{1}{2}\left\langle \frac{1}{r^3} \right\rangle_{n\ell} \hbar^2 \left[ j(j+1) - \ell(\ell+1) - s(s+1) \right]$$

The radial expectation value works out to

$$\left\langle \frac{1}{r^3} \right\rangle_{n\ell} = \frac{1}{a_0^3\, n^3\, \ell(\ell + \frac{1}{2})(\ell+1)}$$

Putting the pieces together, we arrive at

$$\boxed{ E_{SO}^{(1)} = \frac{1}{4}\, \alpha mc^2\, \frac{j(j+1) - \ell(\ell+1) - 3/4}{n^3\, \ell(\ell + \frac{1}{2})(\ell+1)} }$$

This expression looks troublesome if we

consider $\ell = 0$, since numerator and denominator both vanish. But we can set the worry aside on physical grounds: when $\ell = 0$ there is no spin-orbit coupling at all, because the orbital angular momentum is zero. The formula thus applies only to $\ell \neq 0$.

[diagram: $n=2$ level splits into three levels — $2P_{3/2}$ (top), $2S_{1/2}$ (middle), $2P_{1/2}$ (bottom)]

## Fine structure of the H atom

The full set of energy corrections also contains relativistic pieces that we will not pursue here, among them terms arising from Dirac's equation $\rightarrow$ "Darwin" term.

## Landau–Zener tunnelling

Take a spin-$\frac{1}{2}$ subject to a $B$-field along the $x$-direction

$$H_0 = -\mu_B B_1 \tau_x = V\tau_x$$

Now turn on a time-dependent $B$-field along $z$ that ramps up linearly in time

$$H_1(t) = \alpha t\, \tau_z$$

(where $\alpha$ has the proper units)

The total Hamiltonian becomes

$$H(t) = \begin{pmatrix} \alpha t & V \\ V & -\alpha t \end{pmatrix} = \alpha t\, \tau_z + V\tau_x$$

Note that $H_1$ is not a small perturbation, since $|\alpha t|$ can grow large. Here $\alpha$ plays the role of a rate of change of $B_z$. The instantaneous energy eigenvalues are

$$E_\pm = \pm \sqrt{(\alpha t)^2 + V^2}$$

with eigenfunctions $|+\rangle = \begin{pmatrix} \sin\frac{\Theta(t)}{2} \\ \sin\frac{\Theta(t)}{2} \end{pmatrix}$; $|-\rangle = \begin{pmatrix} \sin\frac{\Theta(t)}{2} \\ \cos\frac{\Theta(t)}{2} \end{pmatrix}$

[diagram: avoided crossing of energy levels vs. time. Upper branch labeled $|+\rangle = |\uparrow\rangle$ on the left going to $|+\rangle = |\downarrow\rangle$ on the right (slope $\alpha t$); lower branch labeled $|-\rangle = |\downarrow\rangle$ on the left going to $|-\rangle = |\uparrow\rangle = -\alpha t$ on the right. The gap at the crossing is $2\,T_\alpha$ wide and $2V$ tall, with $T_\alpha = \frac{V}{\alpha}$.]

$\Theta(t)$ is a time-dependent function still to be determined.

It is worth noting that

$$\hat{H}(t) = \vec{n}(t)\cdot\vec{\tau} \qquad \text{with}\quad \vec{n} = (V, 0, \alpha t)$$

and

$$\Theta(t) = \tan^{-1}\left( \frac{V}{\alpha t} \right) \qquad E_\pm(t) = \pm |\vec{n}|$$

Unpacking the meaning of this would require the theory of spin rotations, which lies outside this discussion.

### Landau–Zener Solution

We take $\alpha V \gg \alpha$ so that the formulas derived for the

adiabatic theorem apply — suppose we begin in $|-\rangle$ and start ramping the field

$$\dot{C}_+(t) = -C_-(t)\, e^{i\theta_+^-(t)} \left\langle +\left|\frac{d}{dt}\right|-\right\rangle$$

with

$$\theta_+^-(t) = -\frac{1}{\hbar}\int_{-\infty}^{t}\left(E_-(t') - E_+(t')\right)dt'$$

Now examine the matrix elements:

$$\begin{cases}
\dfrac{d}{dt}|+\rangle = -\dfrac{d\theta}{dt}\dfrac{1}{2}\begin{pmatrix}\sin\theta/2 \\ -\cos\theta/2\end{pmatrix} = -\dfrac{d\theta}{dt}\,|-\rangle \\[2mm]
\dfrac{d}{dt}|-\rangle = \dfrac{d\theta}{dt}\dfrac{1}{2}\begin{pmatrix}\cos\theta/2 \\ \sin\theta/2\end{pmatrix} = \dfrac{1}{2}\dfrac{d\theta}{dt}\,|+\rangle
\end{cases}$$

$$\Rightarrow \begin{cases}
\left\langle -\left|\dfrac{d}{dt}\right|-\right\rangle = \left\langle +\left|\dfrac{d}{dt}\right|+\right\rangle = 0 \\[2mm]
\left\langle +\left|\dfrac{d}{dt}\right|-\right\rangle = \dfrac{1}{2}\dot{\theta} \\[2mm]
\left\langle -\left|\dfrac{d}{dt}\right|+\right\rangle = -\dfrac{1}{2}\dot{\theta}
\end{cases}$$

$$\Rightarrow C_+(t) = -\int_{-\infty}^{t} dt'\; C_-(t')\, e^{i\theta_+^-(t')} \left\langle +\left|\frac{d}{dt}\right|-\right\rangle$$

$$\boxed{C_-(t)\approx 1}$$

$$\approx \frac{1}{2}\int_{-\infty}^{t} dt'\;\dot{\theta}\; e^{\frac{2i}{\hbar}\int_{-\infty}^{t'}\sqrt{(\alpha t'')^2 + V^2}\,dt''}$$

We can evaluate $\dfrac{d\theta}{dt} = -\dfrac{V\alpha}{(\alpha t)^2 + V^2}$

Finally,

$$\boxed{\; C_+(\infty) \approx \frac{1}{2}\int_{-\infty}^{\infty} dt\; \frac{V\alpha}{(\alpha t)^2 + V^2}\; e^{\frac{2i}{\hbar}\int_{-\infty}^{t}\sqrt{(\alpha t')^2 + V^2}\,dt'}\;}$$

This integral can in fact be done exactly, giving

$$C_+(\infty) \approx \frac{\pi}{3}\, e^{-\pi V^2/\alpha}$$

or

$$P_+(\infty) = \frac{\pi^2}{9}\, e^{-\pi V^2/\alpha}$$

The exact answer to the problem is

$$P_+(\infty) = e^{-\pi V^2/\alpha}$$

This result is valid for any $\alpha$, not only $\alpha \to 0$. So as $\alpha$ increases, the system grows more likely to end up in $|+\rangle$ and the spin to **not flip**.

Observe that $\alpha/V^2 \ll 1$ ($V^2\!/\alpha \gg 1$) is exactly the condition for adiabatic evolution. And because $|\alpha t|$ can be made arbitrarily large, this solution is non-perturbative — it is inaccessible to perturbation theory.

**Large $\alpha$** — Landau–Zener tunnelling

*(Avoided-crossing diagram of energy levels vs. time. Two diabatic states cross as straight dashed diagonal lines; the adiabatic eigenstates are the solid curved branches that avoid each other, separated by a gap labeled $2V$.)*

- Upper-left branch: $|+\rangle = |\uparrow\rangle$
- Upper-right branch: $|+\rangle = |\downarrow\rangle$, with $\alpha\nearrow$ (large slope)
- Lower-left branch: $|-\rangle = |\downarrow\rangle$
- Lower-right branch: $|-\rangle = |\uparrow\rangle$
- Gap between branches: $2V$
- Horizontal axis: time ($t$)

*(Arrows trace the trajectory tunnelling across the gap — for large $\alpha$ the system follows the diabatic line and the spin does not flip.)*

**Small $\alpha$** — Adiabatic behavior

*(Same avoided-crossing diagram. For small $\alpha$ the system follows the lower adiabatic branch smoothly through the avoided crossing.)*

- Upper-left branch: $|+\rangle = |\uparrow\rangle$
- Upper-right branch: $|+\rangle = |\downarrow\rangle$, with $\alpha\searrow$ (small slope)
- Lower-left branch: $|-\rangle = |\downarrow\rangle$
- Lower-right branch: $|-\rangle = |\uparrow\rangle$
- Gap between branches: $2V$
- Horizontal axis: time ($t$)

*(Arrows trace the trajectory following the lower adiabatic branch across the avoided crossing — the system stays on the same energy surface and the spin flips.)*


---

## References and Further Reading

*Editorial addition mapping the notes to their source texts.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 11 (Time-Independent Perturbations) for fine structure and spin–orbit coupling; Ch. 3 and Ch. 5 for the addition of angular momenta. The Landau–Zener problem extends the adiabatic theorem of Chapter 4.

**Further reading.** Griffiths & Schroeter, the "Time-Independent Perturbation Theory" chapter (fine structure, the Zeeman effect, and hyperfine splitting of hydrogen); Sakurai & Napolitano, the "Approximation Methods" chapter; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XII. Original papers: L. D. Landau, *Phys. Z. Sowjetunion* **2**, 46 (1932); C. Zener, *Proc. R. Soc. Lond. A* **137**, 696 (1932).
