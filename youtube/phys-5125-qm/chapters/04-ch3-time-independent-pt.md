# Chapter 3 — Time-Independent Perturbation Theory

*Expanding around a problem you can already solve, in powers of a genuinely small parameter.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Most Hamiltonians we care about cannot be solved exactly. The trick of this chapter is to find a nearby one that can, and treat the difference as a small nudge. Write $\hat{H} = \hat{H}_0 + \lambda\hat{V}$, where $\hat{H}_0$ has known eigenstates and $\lambda$ is a dimensionless dial we imagine turning down toward zero. Then expand both the energies and the states as power series in $\lambda$, match terms order by order, and read off the corrections.

The honest caveat: these series rarely converge. What saves us is that the first one or two terms are often astonishingly accurate. First order gives the energy shift as the expectation value of the perturbation in the unperturbed state; second order sums contributions from every other state, weighted by how strongly they couple and how far away they sit in energy.

That last weighting is also the whole story of where the method fails. Each term carries an energy denominator, so when two unperturbed states share an energy, the formula blows up. Degeneracy is the failure mode, and the fix is surgical: inside the degenerate subspace, first rotate to the basis that diagonalizes $\hat{V}$, then the divisions stay finite. We watch this play out concretely in the quadratic Stark shift of hydrogen's ground state and the linear Stark splitting of its first excited level.

## 3 — Time-independent perturbations

## 3.1 — Non-degenerate perturbation theory

We consider a Hamiltonian of the form

$$\hat{H} = \hat{H}_0 + \hat{H}_1$$

where $\hat{H}_0$ is "big" and $\hat{H}_1$ is "small". Here $\hat{H}_0$ is the "unperturbed Hamiltonian," whose solution we take to be known, while $\hat{H}_1$ is the "perturbation" that will "deform" the original solutions of $\hat{H}_0$. For the moment we further assume that the spectrum of $\hat{H}_0$ has no degeneracies.

Saying that $\hat{H}_1$ is "small" compared to $\hat{H}_0$ amounts to writing

$$\hat{H} = \hat{H}_0 + \lambda\hat{V}$$

with $\hat{H}_1 = \lambda\hat{V}$, where $\lambda$ is a dimensionless parameter and the limit of interest is $\lambda \to 0$. We posit that both the eigenstates and the eigenvalues admit a Taylor-like expansion in powers of $\lambda$. These expansions frequently fail to converge, yet the leading corrections already yield remarkably good predictions.

We want to solve

$$\hat{H}|n\rangle = E_n|n\rangle$$

by knowing the solution to

$$\hat{H}_0|n_0\rangle = E_n^{(0)}|n_0\rangle$$

We write

$$|n\rangle = |n_0\rangle + \lambda|n_1\rangle + \lambda^2|n_2\rangle + \cdots$$

$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots$$

Plugging them into the eigenvalue equation we get

$$\left(\hat{H}_0 + \lambda\hat{V}\right)\left(|n_0\rangle + \lambda|n_1\rangle + \lambda^2|n_2\rangle + \cdots\right)$$
$$= \left(E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots\right)\left(|n_0\rangle + \lambda|n_1\rangle + \lambda^2|n_2\rangle + \cdots\right)$$

Equating terms of the same order in $\lambda$ we get

(1) $\quad \hat{H}_0|n_0\rangle = E_n^{(0)}|n_0\rangle$

(2) $\quad \hat{H}_0|n_1\rangle + \hat{V}|n_0\rangle = E_n^{(1)}|n_0\rangle + E_n^{(0)}|n_1\rangle$

(3) $\quad \hat{H}_0|n_2\rangle + \hat{V}|n_1\rangle = E_n^{(2)}|n_0\rangle + E_n^{(1)}|n_1\rangle + E_n^{(0)}|n_2\rangle$

The first equality holds trivially.

### First-order correction

We take the inner product of (2) with $\langle n_0|$ to obtain

$$\langle n_0|\hat{H}_0|n_1\rangle + \langle n_0|\hat{V}|n_0\rangle = E_n^{(0)}\langle n_0|n_1\rangle + E_n^{(1)}\langle n_0|n_0\rangle$$

$\underbrace{E_n^{(0)}\langle n_0|n_1\rangle}_{0}$ on the left, $\underbrace{\phantom{0}}_{0}$ term cancels:

$$\longrightarrow \quad \boxed{E_n^{(1)} = \langle n_0|\hat{V}|n_0\rangle}$$

Taking the inner product with $\langle k_0|$ ; $k\neq n$

$$\langle k_0|\hat{H}_0|n_1\rangle + \langle k_0|\hat{V}|n_0\rangle = E_n^{(0)}\langle k_0|n_1\rangle$$

$$\longrightarrow \quad \langle k_0|n_1\rangle = \frac{\langle k_0|\hat{V}|n_0\rangle}{E_n^{(0)} - E_k^{(0)}}$$

Then, to first order in $\lambda$, we get

$$\boxed{\,|n\rangle = |n_0\rangle + \lambda|n_1\rangle = |n_0\rangle + \lambda\sum_k \frac{\langle k_0|\hat{V}|n_0\rangle}{E_n^{(0)} - E_k^{(0)}}|k_0\rangle\,}$$

### Second-order energy correction

We take the product of $\langle n_0|$ in (3) to obtain

$$\underbrace{\langle n_0|\hat{H}_0|n_2\rangle}_{0} + \langle n_0|\hat{V}|n_1\rangle = E_n^{(0)}\langle n_0|n_2\rangle + \underbrace{E_n^{(1)}\langle n_0|n_1\rangle}_{0} + E_n^{(2)}\langle n_0|n_0\rangle$$

What about $\langle n_0|n_1\rangle$ ?

We found that $|n\rangle = |n_0\rangle + \lambda|n_1\rangle + \mathcal{O}(\lambda^2)$. These states must be normalized

$$\langle n|n\rangle = \underbrace{\langle n_0|n_0\rangle}_{1} + \lambda\left(\langle n_0|n_1\rangle + \langle n_1|n_0\rangle\right) + \mathcal{O}(\lambda^2)$$

$$\longrightarrow \langle n_0|n_1\rangle + \langle n_1|n_0\rangle = 0 \longrightarrow \langle n_0|n_1\rangle \text{ is pure imaginary}$$

$$\longrightarrow |n\rangle = |n_0\rangle + \lambda|n_1\rangle = |n_0\rangle + \lambda\,(ia)|n_0\rangle + \lambda\underbrace{\sum_{k\neq 0}\langle k_0|n_1\rangle|k_0\rangle}_{\perp\,|n_0\rangle}$$

$$= e^{i\alpha}|n_0\rangle + \lambda\,(\text{contributions} \perp |n_0\rangle)$$

We are free to redefine the phase of $|n\rangle$, for example

by setting $a=0$. With that choice the first order correction has no projection onto $|n_0\rangle$

$$\langle n_0|n_1\rangle = 0$$

$$\longrightarrow E_n^{(2)} = \langle n_0|\hat{V}|n_1\rangle = \langle n_0|\hat{V}\sum_{k\neq n}|k_0\rangle\frac{\langle k_0|\hat{V}|n_0\rangle}{E_n^{(0)} - E_k^{(0)}}$$

$$\boxed{\,E_n^{(2)} = \sum_{k\neq n}\frac{\left|\langle k_0|\hat{V}|n_0\rangle\right|^2}{E_n^{(0)} - E_k^{(0)}}\,}$$

### Observations

- The second order correction to the ground-state energy is always negative, because $E_n^{(0)} - E_k^{(0)} < 0$ while the numerator is a square.

- Treating the perturbation as a small correction is only justified when the matrix elements between "neighboring" states are small relative to the spacing of the unperturbed energy levels.

$$\lambda\langle m|\hat{V}|n\rangle \ll \left|E_n^{(0)} - E_m^{(0)}\right| \qquad m\neq n$$

## 3.2 Quadratic Stark effect

When an atom sits in an E-field, the electrons and the nucleus are tugged in opposite directions, producing an electric dipole. We treat a Hydrogen atom subject to the perturbation.

$$\hat{V} = eEz = eEr\cos\theta$$

At first glance the heavy degeneracy of the H atom seems to rule out our method. In fact, this is a situation where "selection rules" eliminate nearly all matrix elements, leaving a problem that non-degenerate perturbation theory can handle.

With the perturbation directed along the $z$ axis, the Hamiltonian remains invariant under rotations about $z$ $\rightarrow [\hat{H}, \hat{L}_z] = 0$

Consequently the $m$ quantum number stays conserved, and the perturbation does not mix states of different $m$.

$$\langle n, \ell, m' | \hat{z} | n, \ell, m \rangle = 0 \quad m \neq m'$$

So the only corrections to $|1,0,0\rangle$ arise from $|n, \ell, 0\rangle$. Furthermore, one can show that only the $n \neq 1$, $\ell = 1$ terms contribute.

The first order correction to the energy will be

$$E_1^{(1)} = \langle 100 | eEz | 100 \rangle$$

Since $\psi_{100}(\vec{r}) \sim e^{-r/a_0}$ this matrix element is

$$\langle 100 | z | 100 \rangle = \int \psi_{100}^{*}\, r\cos\theta\, \psi_{100}\, r^2 \, dr\, \sin\theta\, d\theta\, d\varphi = 0$$

The second order term is

$$E_1^{(2)} = \sum_{n \neq 1} \frac{|\langle n10 | eEz | 100 \rangle|^2}{E_n - E_1}$$

This is not easy to evaluate, but we can obtain an upper bound by observing that

$$|E_1 - E_n| \geq |E_1 - E_2|$$

$$\rightarrow |E_1^{(2)}| < \frac{1}{E_2 - E_1} \sum_{n \neq 1} |\langle n10 | eEz | 100 \rangle|^2$$

$$= \frac{e^2 E^2}{E_2 - E_1} \sum_{\substack{n \neq 1 \\ \ell m}} \langle 100 | z | n\ell m \rangle \langle n\ell m | z | 100 \rangle \quad \text{(We used selection rules)}$$

Reinserting a complete set of eigenstates lets us invoke the identity

$$\sum_{n\ell m} |n\ell m\rangle\langle n\ell m| = \mathbb{1}$$

and we may now include $n=1$ since the denominator has been altered. Hence,

$$|E_1^{(2)}| < \frac{1}{E_2 - E_1} \langle 100 | e^2 E^2 z^2 | 100 \rangle$$

For the ground state of H, $\langle 100 | z^2 | 100 \rangle = \dfrac{a_0^2}{3}$

$E_1 = -e^2/2a_0$ ; $E_2 = E_1/4$

$$\rightarrow |E_1^{(2)}| < \frac{8}{3} E^2 a_0^3$$

Moreover, since every term in the series for $E^{(2)}$ is negative, we can also pin down a lower bound

$$|E_1^{(2)}| > \frac{|\langle 210 | eEz | 100 \rangle|^2}{E_2 - E_1} = 0.55 \times \frac{8}{3} E^2 a_0^3$$

As it happens, this problem can be solved exactly, giving $E_1^{(2)} = \dfrac{9}{4} E^2 a_0^3$

**Example:** Harmonic oscillator in an electric field.

$$\hat{H}_0 = \frac{\hat{p}^2}{2m} + \frac{1}{2} m\omega^2 \hat{x}^2$$

$$\hat{V} = -qE\hat{x}$$

**Solution:**

$$E_n^{(0)} = \hbar\omega \left( n + \tfrac{1}{2} \right)$$

We use $\hat{x} = \sqrt{\dfrac{\hbar}{2m\omega}} \, (a + a^\dagger)$

$$\rightarrow E_n^{(1)} = \langle n | \hat{V} | n \rangle = -qE\sqrt{\frac{\hbar}{2m\omega}} \langle n | a + a^\dagger | n \rangle = 0$$

The second order correction will be

$$E_n^{(2)} = \sum_{k \neq n} \frac{|\langle k | V | n \rangle|^2}{\hbar\omega\left(n + \tfrac{1}{2}\right) - \hbar\omega\left(k + \tfrac{1}{2}\right)}$$

The perturbation only mixes states with $k = n \pm 1$

$$(a + a^\dagger)|n\rangle = \sqrt{n+1}\,|n+1\rangle + \sqrt{n}\,|n-1\rangle$$

$$\rightarrow E_n^{(2)} = \frac{q^2 E^2 \hbar}{2m\omega} \left( \frac{n+1}{-\hbar\omega} + \frac{n}{\hbar\omega} \right) = -\frac{q^2 E^2}{2m\omega^2}$$

**Example:** Non-linear oscillator

$$H_0 = \frac{\hat{p}^2}{2m} + \frac{m\omega^2 \hat{x}^2}{2}$$

$$V = \lambda \frac{\hat{x}^4}{4}$$

**Solution:**

It is convenient to recast these expressions in terms of bosonic operators

$$V = \frac{\lambda \hbar^2}{16 m^2\omega^2} \left( (a^\dagger)^4 + 4(a^\dagger)^3 a + 6\left(a^\dagger a\right)^2 + a^4 + 6(a^\dagger)^2 + 6a^2 + 6a^\dagger a + 3 \right)$$

$$E_n^{(1)} = \lambda \langle n | \hat{V} | n \rangle = \frac{\lambda \hbar^2}{16 m^2\omega^2} \langle n | 6n^2 + 6n + 3 | n \rangle$$

$$= \frac{3\lambda \hbar^2}{8 m^2\omega^2} \left( n^2 + n + \tfrac{1}{2} \right) = \frac{3\lambda}{8 m^2\omega^4} \frac{n^2 + n + \tfrac{1}{2}}{(n + \tfrac{1}{2})^2} \left( E_n^{(0)} \right)^2$$

with $E_n^{(0)} = \hbar\omega\left( n + \tfrac{1}{2} \right)$

## 3.3 Degenerate perturbation theory

The formalism above breaks down once degeneracies appear, because of the difference $E_n^{(0)} - E_m^{(0)}$ sitting in the denominator.

**Example:** 2D harmonic oscillator

$$H_0 = \frac{\hat{p}_x^2 + \hat{p}_y^2}{2m} + \frac{1}{2} m\omega^2 (\hat{x}^2 + \hat{y}^2)$$

$$= \hat{H}_{0x} + \hat{H}_{0y}$$

$\rightarrow$ The eigenstates are products

$$|n_x, n_y\rangle = |n_x\rangle \otimes |n_y\rangle$$

With energies

$$E_{n_x n_y} = E_{n_x} + E_{n_y} = \hbar\omega\left( n_x + n_y + 1 \right)$$

Suppose we introduce a small perturbation

$$\hat{V} = \alpha m\omega^2 \hat{x}\hat{y}$$

where $\alpha$ is a small parameter

Notice that

$$\hat{V} = \alpha m\omega^2 \frac{\hbar}{2m\omega} (a_x + a_x^\dagger)(a_y + a_y^\dagger)$$

Hence, the first order correction

$$E_{n_x n_y}^{(1)} = \langle n_x n_y | V | n_x n_y \rangle = 0$$

Going to second order, the theory falls apart

$$E_{10}^{(0)} = E_{01}^{(0)}$$

And yet we know this tiny perturbation cannot "destroy" the oscillator. By combining the $x^2 + y^2$ term with the $xy$ perturbation we complete the square, obtaining an oscillator whose equipotential surfaces are ellipses.

&nbsp;&nbsp;&nbsp;&nbsp;unperturbed &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;perturbed

*(Figure: left — concentric circles centered on origin with cross axes; right — concentric ellipses tilted along a diagonal axis.)*

*end lecture*

In the original problem, rotational symmetry lets us orient the $x$-$y$ axes however we like. In the new one it pays to align them with the axes of symmetry. In that representation the corrections to the unperturbed eigenstates come out small.

**Solution:** choose a basis set in a degenerate subspace such that the perturbation is diagonal in this representation!

For the problem above, the solution can in fact be found exactly

$$\frac{1}{2} m\omega^2 (x^2 + y^2) + \alpha m\omega^2 xy$$

$$= \frac{1}{2} m\omega^2 \left[ (1 + \alpha)\left( \frac{\hat{x} + \hat{y}}{\sqrt{2}} \right)^2 + (1 - \alpha)\left( \frac{\hat{x} - \hat{y}}{\sqrt{2}} \right)^2 \right]$$

$$\hbar\omega \rightarrow \hbar\omega\sqrt{1 \pm \alpha} \approx \hbar\omega\left( 1 \pm \frac{\alpha}{2} \right)$$

Let us make these ideas precise. Suppose the unperturbed eigenstates $|n^{(0)}\rangle$; $n = 1, \dots, g$ carry energies $E_n^{(0)}$ that are equal or nearly so.

*(Figure: Energy level diagram. Left side — before perturbation: a level $E_1^{(0)}$ labeled "$g$-fold degenerate before perturbation," and a higher level $E_{g+1}^{(0)}$. Right side — after perturbation: the $g$-fold level splits into $g$ separate levels labeled $E_1', \dots, E_g$, "$g$ values"; the $E_{g+1}^{(0)}$ level remains above.)*

The cure is to build a new basis out of the eigenstates of $V$. We will see that adding the corresponding eigenvalues to the unperturbed energies produces the first order correction. Label these new states as

$$|\tilde{n}\rangle = \sum_{i=1}^{g} C_{ni} |i\rangle$$

that satisfy $V|\tilde{n}\rangle = V_n |\tilde{n}\rangle$

Together with the complementary collection of non-degenerate states $\{|m^{(0)}\rangle\,;\, m > g\}$ they make up a new orthonormal basis

$$\left\{ |\tilde{1}\rangle, |\tilde{2}\rangle, \dots, |\tilde{g}\rangle, |g+1^{(0)}\rangle, |g+2^{(0)}\rangle, \dots \right\}$$

the matrix $V$ in this basis looks like

$$V = \begin{pmatrix} V_{1}V_{2} & 0 & V_{1,g+1} & \cdots \\ 0 & V_g & V_{g,g+1} & \cdots \\ \hline V_{g+1,1} \cdots V_{g+1,g} & & & \\ \vdots & \vdots & & \end{pmatrix}$$

We now show that the diagonal elements are the first order corrections to $E_n^{(0)}$. The Schrödinger eq for the total Hamiltonian is

$$\hat{H}|n\rangle = (\hat{H}_0 + \hat{V})|n\rangle = E_n |n\rangle$$

We now substitute

$$|n\rangle = |\tilde{n}\rangle$$
$$E_n = E_n^{(0)} + E_n^{(1)} \quad\Big\}\quad n \leq g$$

$$\hat{H}_0 |\tilde{n}\rangle + \hat{V}|\tilde{n}\rangle = E_n^{(0)}|\tilde{n}\rangle + E_n^{(1)}|\tilde{n}\rangle$$

$$\rightarrow V|\tilde{n}\rangle = E_n^{(1)}|\tilde{n}\rangle$$

because $H_0|\tilde{n}\rangle = E_n^{(0)}|\tilde{n}\rangle$; the $|\tilde{n}\rangle$ are linear combinations of degenerate eigenstates of $H_0$, and are therefore themselves degenerate eigenstates of $H_0$.

This shows that the eigenvalues of $V$ supply the first order energy corrections for $n \leq g$, with $E_n^{(1)} = V_n$

In this new basis the ambiguities caused by the degeneracy of $H_0$ disappear, and we can carry on with the machinery built for non-degenerate perturbation theory:

$$|n\rangle = |\tilde{n}\rangle + \lambda|\tilde{n}^{(1)}\rangle + \lambda^2|\tilde{n}^{(2)}\rangle + \cdots \quad (n \leq g)$$
$$|n\rangle = |n^{(0)}\rangle + \lambda|n^{(1)}\rangle + \lambda^2|n^{(2)}\rangle + \cdots \quad (n > g)$$

$$E_n = E_n^{(0)} + \lambda V_n + \lambda^2 E_n^{(2)} \quad (n \leq g)$$
$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} \quad (n > g)$$

with $V_n = \langle \tilde{n} | V | \tilde{n} \rangle$

$$E_n^{(1)} = \langle n^{(0)} | V | n^{(0)} \rangle$$

**Example:** two-level system

$$\hat{H} = \begin{pmatrix} E_0 & V \\ V & E_1 \end{pmatrix} = \begin{pmatrix} E_0 & 0 \\ 0 & E_1 \end{pmatrix} + \begin{pmatrix} 0 & V \\ V & 0 \end{pmatrix}$$

we may regard $E_0$ and $E_1$ as the unperturbed energies and $V$ as the perturbation that couples the two states. In the language of spin operators, this becomes

$$\hat{H} = \frac{(E_0 + E_1)}{2} \hat{\mathbb{1}} + (E_0 - E_1)\hat{S}^z + 2V\hat{S}^x$$

The eigenvalues of this $2\times2$ problem can be easily obtained

$$E_\pm = \frac{1}{2}(E_0 + E_1) \pm \frac{1}{2}\sqrt{(E_0 - E_1)^2 + 4V^2}$$

Rather than write out the exact eigenstates, consider the limit $|E_0 - E_1| \gg V$

$$\pm \frac{1}{2}\sqrt{(E_0 - E_1)^2 + 4V^2} \approx \pm\frac{1}{2}(E_0 - E_1) + \frac{V^2}{E_0 - E_1}$$

$$\rightarrow E_+ = E_0 + \frac{V^2}{E_0 - E_1} \;;\; E_- = E_1 + \frac{V^2}{E_1 - E_0}$$

This matches non-degenerate perturbation theory. The corresponding eigenstates are:

$$|+\rangle = |0\rangle - \frac{V}{E_1 - E_0}|1\rangle$$

$$|-\rangle = |1\rangle - \frac{V}{E_1 - E_0}|0\rangle$$

The case $E_0 = E_1$ is known as a resonance.

The eigenenergies and eigenstates are

$$E_+ = E_0 + V \;;\; |+\rangle = \frac{1}{\sqrt{2}}\left( |0\rangle + |1\rangle \right)$$

$$E_- = E_0 - V \;;\; |-\rangle = \frac{1}{\sqrt{2}}\left( |0\rangle - |1\rangle \right)$$

*(Figure: Energy vs $E_0 - E_1$. Two solid curves: an upper branch labeled $E_+$ that comes from $E_1$ on the left and approaches $E_0$ on the right, and a lower branch labeled $E_-$ that comes from $E_0$ on the left and approaches $E_1$ on the right. Dashed diagonal lines (the unperturbed levels) cross at the origin; the solid curves show an avoided crossing.)*

The perturbation opens a gap: an __avoided level crossing__. A genuine crossing is possible only when the matrix elements between the two states vanish, which usually signals an underlying symmetry. With no symmetry present we instead see __level repulsion__, so the energy levels refuse to cross as a parameter in the Hamiltonian is tuned.

**Example:** 2d-harmonic oscillator

$$\hat{H}_0 = \hat{H}_{0x} + \hat{H}_{0y}$$

$$\hat{V} = \alpha m\omega^2 \hat{x}\hat{y}$$

$\hat{H}_0$ is degenerate in pairs $(nm)$. Let us consider the case $n=0$; $m=1$

$$V = \begin{pmatrix} \langle 01 | V | 01 \rangle & \langle 01 | V | 10 \rangle \\ \langle 10 | V | 01 \rangle & \langle 10 | V | 10 \rangle \end{pmatrix}$$

We recall the identity:

$$\hat{V} = \frac{\alpha\omega\hbar}{2} (a_x + a_x^\dagger)(a_y + a_y^\dagger)$$

that allows us to obtain the matrix elements

$$\langle 01 | V | 01 \rangle = \langle 10 | V | 10 \rangle = 0 \;;\; \langle 01 | V | 10 \rangle = \frac{\alpha\omega\hbar}{2}$$

$$\rightarrow V = \begin{pmatrix} 0 & \dfrac{\alpha\omega\hbar}{2} \\ \dfrac{\alpha\omega\hbar}{2} & 0 \end{pmatrix}$$

which has eigenvalues

$$V_\pm = \pm \frac{\alpha\omega\hbar}{2}$$

*(Figure: level $E_{10}$ splits into $E_+ = E_{10} + \dfrac{\alpha\omega\hbar}{2}$ and $E_- = E_{10} - \dfrac{\alpha\omega\hbar}{2}$.)*

the corresponding wave functions are

$$|10_\pm\rangle = \frac{1}{\sqrt{2}}\left( |10\rangle \pm |01\rangle \right)$$

We now recall the exact eigenvalues

$$\hbar\omega \rightarrow \hbar\omega\sqrt{1 \pm \alpha} \approx \hbar\omega\left( 1 \pm \frac{\alpha}{2} \right)$$

## 3.4 Linear Stark effect

Let us turn to the first excited states of Hydrogen $|2,0,0\rangle$, $|2,1,-1\rangle$, $|2,1,0\rangle$, $|2,1,1\rangle$. This manifold is four-fold degenerate, so we must diagonalize a $4\times4$ matrix. As noted before, only matrix elements between states sharing the same quantum number $m$ survive. Here only a single such term exists:

$$\langle 210 | z | 200 \rangle = \int_0^\infty r^2\, dr \int_0^\pi \sin\theta\, d\theta \int_0^{2\pi} d\varphi\; \psi_{210}^{*}\, r\cos\theta\, \psi_{200}$$

$$= -3a_0$$

Therefore, the $4\times4$ matrix is

$$\begin{pmatrix} 0 & -3eEa_0 & 0 & 0 \\ -3eEa_0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

Its eigenvalues can be readily obtained as

$$E_2^{(1)} = 0,\; 0,\; 3eEa_0,\; -3eEa_0$$

with eigenstates

$$|2,1,1\rangle,\; |2,1,-1\rangle,\; \frac{1}{\sqrt{2}}\left( |210\rangle - |200\rangle \right),\; \frac{1}{\sqrt{2}}\left( |200\rangle + |210\rangle \right)$$

The first two states stay unshifted thanks to the rotational symmetry in the $x$-$y$ plane. Note that, in contrast to the quadratic shift of the ground state, here the shift is linear.

*(Figure: the degenerate level splits into three: top — $\frac{1}{\sqrt{2}}(|210\rangle - |200\rangle)$ shifted up by $3eEa_0$; middle (unshifted) — $|211\rangle$, $|21-1\rangle$; bottom — $\frac{1}{\sqrt{2}}(|210\rangle + |200\rangle)$ shifted down by $3eEa_0$.)*


---

## References and Further Reading

*Editorial addition mapping the notes to their source text.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 11 (Time-Independent Perturbations) — non-degenerate and degenerate perturbation theory and the Stark effect.

**Further reading.** Sakurai & Napolitano, the "Approximation Methods" chapter; Griffiths & Schroeter, the "Time-Independent Perturbation Theory" chapter; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XI.
