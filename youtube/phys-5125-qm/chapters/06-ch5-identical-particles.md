# Chapter 5 — Identical Particles

*When particles become truly interchangeable, indistinguishability forces the wave function into strict symmetry — and exchange turns into a real energy with no classical shadow.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Here is the puzzle that drives this whole chapter. Take two electrons. Not "two electrons that look alike" — two electrons that are genuinely, perfectly the same. There is no sticker, no serial number, nothing in principle that tells one from the other. Now swap them. Nothing observable can change, because nothing distinguished them to begin with.

That single fact does almost all the work. If swapping two particles must leave every measurable prediction alone, the state can only pick up a sign: $+1$ or $-1$. Bosons take the plus and pile into symmetric states; fermions take the minus and live in antisymmetric ones. From the minus sign alone you get the Pauli exclusion principle — two fermions cannot share a state, because the antisymmetric combination of identical things is just zero.

The payoff is the part with no classical analogue. When you compute the energy of two interacting particles, the (anti)symmetry splits one interaction integral into two pieces: an ordinary "direct" term you could have guessed classically, and an "exchange" term that exists purely because the particles are indistinguishable. That exchange piece is what separates singlet from triplet, powers Hund's rule, and sets the singlet–triplet splitting in helium. Spin never appears in the Hamiltonian, yet it controls the energy. Keep that thread in mind as we build it up.

## 5 — Identical particles

## 5.1 Intrinsic angular momentum: spin

In quantum mechanics, the spin $\vec{S}$ is a basic attribute of elementary particles with no classical counterpart. It stands on the same footing as mass or charge: an intrinsic property that cannot be altered.

Spin obeys the same algebra as angular momentum:

$$\hat{S} = (\hat{S}^x, \hat{S}^y, \hat{S}^z), \quad \text{with}$$

$$[\hat{S}^x, \hat{S}^y] = i\hbar \hat{S}^z, \quad [\hat{S}^y, \hat{S}^z] = i\hbar \hat{S}^x, \quad [\hat{S}^z, \hat{S}^x] = i\hbar \hat{S}^y$$

We write $|s, m\rangle$ for the joint eigenstates of $\hat{S}^2$ and $\hat{S}^z$

$$\hat{S}^2 |s, m\rangle = \hbar^2 s(s+1)|s, m\rangle$$

$$\hat{S}^z |s, m\rangle = \hbar m |s, m\rangle$$

with $m = -s, -s+1, \cdots, s-1, s$.

The raising and lowering operators are defined by

$$\hat{S}^\pm |s, m\rangle = \hbar \sqrt{s(s+1) - m(m\pm 1)}\, |s, m\pm 1\rangle$$

with $\hat{S}^\pm = \hat{S}^x \pm i\hat{S}^y$.

Unlike orbital angular momentum, the states $|s, m\rangle$ have no representation in real space.

### The spin of the elementary particles

**Fermions:** half-integer value of $s$
electrons, quarks, protons, neutrons are fermions with spin $s = \tfrac{1}{2}$

**Bosons:** integer value of $s$
photons are bosons with $s = 1$,
the Higgs has $s = 0$

## 5.2 Theory of spin-$\tfrac{1}{2}$

$$s = \tfrac{1}{2} \rightarrow m = \pm\tfrac{1}{2}$$

They are two-level systems!

$$\hat{S}^2 |\tfrac{1}{2}, m\rangle = \hbar^2 \tfrac{1}{2}\left(\tfrac{1}{2}+1\right)|\tfrac{1}{2}, m\rangle = \hbar^2\tfrac{3}{4}|\tfrac{1}{2}, m\rangle$$

$$\hat{S}^z |\tfrac{1}{2}, m\rangle = \hbar m |\tfrac{1}{2}, m\rangle$$

From here on we can drop the index $s$ and label the states $|+\rangle, |-\rangle$; $|1\rangle, |2\rangle$ or $|\uparrow\rangle, |\downarrow\rangle$.

As noted earlier, an arbitrary state in this basis reads

$$|\psi\rangle = c_+ |+\rangle + c_2 |-\rangle$$

The eigenvectors of $\hat{S}^x$ are

$$|+_x\rangle = \tfrac{1}{\sqrt{2}}\big[|+\rangle + |-\rangle\big] \quad;\quad |-_x\rangle = \tfrac{1}{\sqrt{2}}\big[|+\rangle - |-\rangle\big]$$

$$\rightarrow |\psi\rangle = \frac{c_+ + c_-}{\sqrt{2}}|+_x\rangle + \frac{c_+ - c_-}{\sqrt{2}}|-_x\rangle$$

Hence the probability of finding the spin pointing one way or the other along $x$ is

$$P(s^x = \hbar/2) = \left|\frac{c_+ + c_-}{\sqrt{2}}\right|^2 \quad;\quad P(s^x = -\tfrac{\hbar}{2}) = \left|\frac{c_+ - c_-}{\sqrt{2}}\right|^2$$

## 5.3 — Addition of spins $s = \tfrac{1}{2}$

Take a system of two particles in definite states $|s_1, m_1\rangle$ and $|s_2, m_2\rangle$. We write the state of the system as

$$|s_1, s_2, m_1, m_2\rangle = |s_1, m_1\rangle \otimes |s_2, m_2\rangle$$

The state is "separable"

$$\hat{S}_1^2 |s_1 s_2, m_1 m_2\rangle = s_1(s_1+1)\hbar^2 |s_1 s_2, m_1, m_2\rangle$$

$$\hat{S}_2^2 |s_1 s_2, m_1 m_2\rangle = s_2(s_2+1)\hbar^2 |s_1 s_2, m_1 m_2\rangle$$

$$\hat{S}_1^z |s_1 s_2 m_1 m_2\rangle = \hbar m_1 |s_1 s_2 m_1 m_2\rangle$$

$$\hat{S}_2^z |s_1 s_2 m_1 m_2\rangle = \hbar m_2 |s_1 s_2 m_1 m_2\rangle$$

We now want the **total** spin of the system. One readily checks that

$$\hat{S}^z |s_1 s_2 m_1 m_2\rangle = \hat{S}_1^z + \hat{S}_2^z |s_1 s_2 m_1 m_2\rangle =$$

$$= \hbar (m_1 + m_2) |s_1 s_2 m_1 m_2\rangle$$

However, the states $|s_1 s_2 m_1 m_2\rangle$ are not eigenstates of $\hat{S}^2 = (\hat{S}_1 + \hat{S}_2)^2$!

Let us solve this for two $s = \tfrac{1}{2}$ particles. There are 4 possible combinations of $m_1 + m_2$

$$|++\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}\rangle \qquad (m = 1)$$

$$|+-\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}\rangle \qquad (m = 0)$$

$$|-+\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}, \tfrac{1}{2}\rangle \qquad (m = 0)$$

$$|--\rangle \equiv |\tfrac{1}{2}, \tfrac{1}{2}, -\tfrac{1}{2}, -\tfrac{1}{2}\rangle \qquad (m = -1)$$

How can there be two $m = 0$ states? To settle this we invoke the identity

$$\hat{S}^2 = (\hat{S}_1 + \hat{S}_2)^2 = \hat{S}_1^2 + \hat{S}_2^2 + 2\hat{S}_1 \cdot \hat{S}_2$$

$$= \hat{S}_1^2 + \hat{S}_2^2 + \hat{S}_1^+ \hat{S}_2^- + \hat{S}_1^- \hat{S}_2^+ + 2\hat{S}_1^z \hat{S}_2^z$$

This lets us readily build the matrix representation of the operator in this basis

$$\hat{S}^2 = \frac{\hbar^2}{2}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 2 & 0 \\ 0 & 2 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} + \frac{3}{2}\hbar^2\, \mathbb{I}$$

We see at once that $|++\rangle$ and $|--\rangle$ are eigenvectors of $\hat{S}^2$ with eigenvalues $2\hbar^2$, so they carry quantum number $s = 1$, since $1(1+1) = 2$.

To find the values of $s$ in the $|+-\rangle$, $|-+\rangle$ ($m = 0$) subspace we must solve

$$\det\begin{pmatrix} -1-\lambda & 2 \\ 2 & -1-\lambda \end{pmatrix} = (-1-\lambda)^2 - 4 = 0 \rightarrow \lambda = 1, -3$$

or $s = \dfrac{\hbar^2}{2}\lambda + \dfrac{3}{2}\hbar^2 = 0, 2\hbar^2$

So one eigenvector belongs to $s = 0$ and the other to $s = 1$. Solving for the eigenvectors gives:

$$|1, 0\rangle = \tfrac{1}{\sqrt{2}}\big[|+-\rangle + |-+\rangle\big] \qquad (s = 1, m = 0)$$

$$|0, 0\rangle = \tfrac{1}{\sqrt{2}}\big[|+-\rangle - |-+\rangle\big] \qquad (s = 0, m = 0)$$

We therefore end up with three states having $s = 1$, $m = -1, 0, 1$; and one with $s = 0$, $m = 0$.

## 5.4 Pairs of indistinguishable particles

Let us ask which states are permitted for two particles. In general a two-particle state is specified by

$$|ab\rangle = |a\rangle_1 \otimes |b\rangle_2$$

where $|a\rangle_1$ is the state of particle 1 and $|b\rangle_2$ that of particle 2. We introduce the "exchange operator", or permutation operator, which acts as

$$\hat{P}_{12}|ab\rangle = |ba\rangle$$

or

$$\hat{P}_{12}\left(|a\rangle_1 \otimes |b\rangle_2\right) = |b\rangle_1 \otimes |a\rangle_2$$

Because the particles are indistinguishable, we have no way of telling whether the exchange operator has acted: the "exchanged" state must equal the original one up to a phase

$$\hat{P}_{12}|\psi\rangle = e^{i\delta}|\psi\rangle = \lambda |\psi\rangle$$

Applying $\hat{P}_{12}$ twice returns the identity. Hence

$$\hat{P}_{12}^2 |\psi\rangle = \lambda^2 |\psi\rangle = |\psi\rangle \rightarrow \lambda = \pm 1$$

Plainly, if both particles are in state $a$

$$\hat{P}_{12}|aa\rangle = |aa\rangle$$

$\rightarrow |aa\rangle$ is a "symmetric" state under exchange.

If $b \neq a$ we must find the eigenstates of $\hat{P}_{12}$

$$\hat{P}_{12} = \begin{pmatrix} \langle ab|\hat{P}_{12}|ab\rangle & \langle ab|\hat{P}_{12}|ba\rangle \\ \langle ba|\hat{P}_{12}|ab\rangle & \langle ba|\hat{P}_{12}|ba\rangle \end{pmatrix}$$

$$= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

The eigenvalues are, naturally, $\lambda = \pm 1$. The eigenstates are:

$$|+\rangle = \tfrac{1}{\sqrt{2}}\big(|ab\rangle + |ba\rangle\big) \qquad \lambda = 1$$

$$|-\rangle = \tfrac{1}{\sqrt{2}}\big(|ab\rangle - |ba\rangle\big) \qquad \lambda = -1$$

Notice that two particles **must** sit in either the $|+\rangle$ or the $|-\rangle$ state and cannot occupy a linear superposition of the two. They are forced to

"make a choice" between them. Fortunately, Nature settles it for them:

**Bosons:** appear only in symmetric states

**Fermions:** appear only in antisymmetric states

### Pauli's exclusion principle:

We noted that two particles in the same state are necessarily symmetric under exchange. Since a fermionic state is antisymmetric, two fermions can never occupy the same state.

**Example:** two spin $s = \tfrac{1}{2}$ particles.

We found that two spins $s = \tfrac{1}{2}$ can occupy the states

$$|1, 0\rangle = \tfrac{1}{\sqrt{2}}\big(|+-\rangle + |-+\rangle\big)$$

$$|0, 0\rangle = \tfrac{1}{\sqrt{2}}\big(|+-\rangle - |-+\rangle\big)$$

We recognize these as symmetric and anti-symmetric under exchange.

*end of lecture.*

This is simple to explain once we notice the following identity:

$$\hat{S}^2 = \hbar^2 \hat{S}_1^z \hat{S}_2^z + \tfrac{3}{2}\hbar^2\, \mathbb{I} + \hbar^2 \hat{P}_{12}$$

$$\rightarrow [\hat{P}_{12}, \hat{S}^2] = 0$$

$\rightarrow$ eigenstates of $\hat{S}^2$ must also be eigenstates of $\hat{P}_{12}$.

## 5.5 Many-particle systems

For a system of $N$ identical particles, the Hamiltonian must stay invariant under any permutation of two particles or coordinates. For identical particles the exchange sign must be the same for every pair, or else the particles would be distinguishable. The $N$-particle wave function is therefore odd under the exchange of any pair of fermions, and even for bosons

$$\psi(x_1, \ldots x_n, \ldots x_m, \ldots x_N) = \pm\, \psi(x_1, \ldots x_m, \ldots x_n, \ldots x_N)$$

Consider a system of $N$ non-interacting particles with Hamiltonian

$$\hat{H} = \hat{H}_1 + \hat{H}_2 + \cdots \hat{H}_N$$

with, for instance $\hat{H}_i = \frac{\hat{p}_i^2}{2m} + V(\vec{x}_i)$

The general $N$-particle wave function for the energy

$$E_i = E_{i_1} + E_{i_2} + \cdots E_{i_N}$$

can be written as

$$|\psi(x_1, \ldots x_N)\rangle = \sum_{\{\sigma\} \in S} C_{\sigma_1, \sigma_2, \ldots \sigma_N} |\psi_{\sigma_1}(x_1)\rangle \cdots |\psi_{\sigma_N}(x_N)\rangle$$

where $\{\sigma\}$ runs over all permutations of the indices $\{i_1, i_2, \ldots i_N\}$. The coefficients $C_{\sigma_1 \ldots \sigma_N}$ are invariant under permutations for bosons, and change sign under an odd number of permutations for fermions. They must also be normalized

$$\sum_{\{\sigma\} \in S} |C_{\sigma_1 \ldots \sigma_N}|^2 = 1$$

**Fermions:** By anti-symmetry, all indices must differ. One checks that the wave function, up to an overall phase, is proportional to the so-called "Slater determinant":

$$\psi(x_1, x_2, \ldots x_N) = \frac{1}{\sqrt{N!}}\begin{vmatrix} \psi_{i_1}(x_1) & \psi_{i_2}(x_1) & \cdots & \psi_{i_N}(x_1) \\ \psi_{i_1}(x_2) & \psi_{i_2}(x_2) & & \psi_{i_N}(x_2) \\ \vdots & \vdots & & \vdots \\ \psi_{i_1}(x_N) & \psi_{i_2}(x_N) & \cdots & \psi_{i_N}(x_N) \end{vmatrix}$$

The antisymmetry follows from the $(-1)$ picked up when two columns are exchanged. Written out:

### Example: three-particle system

$$\psi(x_1 x_2 x_3) = \frac{1}{\sqrt{6}}\begin{vmatrix} \psi_a(x_1) & \psi_b(x_1) & \psi_c(x_1) \\ \psi_a(x_2) & \psi_b(x_2) & \psi_c(x_2) \\ \psi_a(x_3) & \psi_b(x_3) & \psi_c(x_3) \end{vmatrix}$$

$$= \frac{1}{\sqrt{6}}\Big(\psi_a(x_1)\psi_b(x_2)\psi_c(x_3) - \psi_a(x_1)\psi_c(x_2)\psi_b(x_3)$$

$$- \psi_b(x_1)\psi_a(x_2)\psi_c(x_3) + \psi_b(x_1)\psi_c(x_2)\psi_a(x_3)$$

$$+ \psi_c(x_1)\psi_a(x_2)\psi_b(x_3) - \psi_c(x_1)\psi_b(x_2)\psi_a(x_3)\Big)$$

**Bosons:** Here the determinant is replaced by the permanent, defined just like the determinant but with every sign positive.

### Example: three-particle system.

Different orbitals $a \neq b \neq c$

$$\psi(x_1 x_2 x_3) = \frac{1}{\sqrt{6}}\,\text{perm}\begin{pmatrix} \psi_a(x_1) & \psi_b(x_1) & \psi_c(x_1) \\ \psi_a(x_2) & \psi_b(x_2) & \psi_c(x_2) \\ \psi_a(x_3) & \psi_b(x_3) & \psi_c(x_3) \end{pmatrix}$$

$$= \frac{1}{\sqrt{6}}\Big(\psi_a(x_1)\psi_b(x_2)\psi_c(x_3) + \psi_a(x_1)\psi_c(x_2)\psi_b(x_3)$$

$$+ \psi_b(x_1)\psi_a(x_2)\psi_c(x_3) + \psi_b(x_1)\psi_c(x_2)\psi_a(x_3)$$

$$+ \psi_c(x_1)\psi_a(x_2)\psi_b(x_3) + \psi_c(x_1)\psi_b(x_2)\psi_a(x_3)\Big)$$

Two identical orbitals $a = b \neq c$

$$\psi(x_1 x_2 x_3) = \frac{1}{\sqrt{3}}\frac{1}{2!}\,\text{perm}\begin{pmatrix} \psi_a(x_1) & \psi_a(x_1) & \psi_c(x_1) \\ \psi_a(x_2) & \psi_a(x_2) & \psi_c(x_2) \\ \psi_a(x_3) & \psi_a(x_3) & \psi_c(x_3) \end{pmatrix}$$

$$= \frac{1}{\sqrt{3}}\Big(\psi_a(x_1)\psi_a(x_2)\psi_c(x_3) + \psi_a(x_1)\psi_a(x_3)\psi_c(x_2)$$

$$+ \psi_a(x_1)\psi_a(x_3)\psi_c(x_2)\Big)$$

One can show that the normalization carries an extra $\sqrt{n_a!}$, where $n_a$ is the number of times the orbital $\psi_a$ is occupied.

### Example: Two particles with spin

Consider two particles that may occupy two orbitals $\psi_1(r), \psi_2(r)$ and carry spin $\uparrow\downarrow$. We can build the following Slater determinants:

$$\psi_{1\uparrow 2\uparrow}(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}\begin{vmatrix} \psi_{1\uparrow}(\vec{r}_1) & \psi_{2\uparrow}(\vec{r}_1) \\ \psi_{1\uparrow}(\vec{r}_2) & \psi_{2\uparrow}(\vec{r}_2) \end{vmatrix} = \frac{1}{\sqrt{2}}\left(\psi_{1\uparrow}(\vec{r}_1)\psi_{2\uparrow}(\vec{r}_2) - \psi_{1\uparrow}(\vec{r}_2)\psi_{2\uparrow}(\vec{r}_1)\right)$$

$$\psi_{1\downarrow 2\downarrow}(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}\begin{vmatrix} \psi_{1\downarrow}(\vec{r}_1) & \psi_{2\downarrow}(\vec{r}_1) \\ \psi_{1\downarrow}(\vec{r}_2) & \psi_{2\downarrow}(\vec{r}_2) \end{vmatrix} = \frac{1}{\sqrt{2}}\left(\psi_{1\downarrow}(\vec{r}_1)\psi_{2\downarrow}(\vec{r}_2) - \psi_{1\downarrow}(\vec{r}_2)\psi_{2\downarrow}(\vec{r}_1)\right)$$

$$\psi_{1\uparrow 2\downarrow}(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}\begin{vmatrix} \psi_{1\uparrow}(\vec{r}_1) & \psi_{2\downarrow}(\vec{r}_1) \\ \psi_{1\uparrow}(\vec{r}_2) & \psi_{2\downarrow}(\vec{r}_2) \end{vmatrix} = \frac{1}{\sqrt{2}}\left(\psi_{1\uparrow}(\vec{r}_1)\psi_{2\downarrow}(\vec{r}_2) - \psi_{1\uparrow}(\vec{r}_2)\psi_{2\downarrow}(\vec{r}_1)\right)$$

Same for $\psi_{1\downarrow 2\uparrow}$

Notice that $\psi_{1\uparrow 1\downarrow}$ and $\psi_{2\uparrow 2\downarrow}$ are allowed, but $\psi_{1\uparrow 1\uparrow}$ or $\psi_{2\uparrow 2\uparrow}$ are not.

Moreover, as we shall see next, these states are neither singlets nor triplets.

### Two particles with spin: space and spin wave functions

The total wave function for two particles with spin is a simultaneous eigenfunction of $\hat{H}$, $\hat{S}^2$ and $\hat{S}^z$, and takes the form

$$\Psi_{\sigma_1 \sigma_2}(\vec{r}_1, \vec{r}_2) = \psi(\vec{r}_1, \vec{r}_2)\,\chi(\sigma_1, \sigma_2)$$

where $\sigma_1, \sigma_2$ now stand in for $m$ to denote $\uparrow, \downarrow$ or $\uparrow, \downarrow$.

$\Psi$ must be anti-symmetric. Consequently a pair of electrons in a $|0,0\rangle$ (singlet) state must carry a symmetric spatial wave function $\psi(\vec{r}_2, \vec{r}_1) = \psi(\vec{r}_1, \vec{r}_2)$, while in the triplet states the spatial wave function must be anti-symmetric.

### Example: Hydrogen ($H_2$) gas

Here the spin of the protons proves crucial. With parallel spins the molecule is "orthohydrogen"; in the singlet state it is "parahydrogen". Both are very stable, and transitions between them may take weeks.

The actual interaction energy between the protons is entirely negligible. The rotational energy of the molecule, however, matters a great deal. A state with angular momentum $\ell$ has parity $(-1)^\ell$. Parahydrogen, with its antisymmetric spin wave function, therefore needs a symmetric proton space wave function and admits only even values of $\ell$. By the same reasoning, orthohydrogen admits only odd $\ell$. The rotational energy of a state with angular momentum $\ell$ is

$$E_\ell^{\text{rot}} = \frac{\hbar^2 \ell(\ell+1)}{I}$$

so the two species of hydrogen gas carry different rotational energies.

## 5.6 Particles with interactions and exchange

Now the general eigenstate is written as a linear combination of Slater determinants (fermions) or permanents (bosons).

Take two fermions and two orbitals, 1 and 2. The combinations with the correct antisymmetry are

$$\Psi_S(x_1, s_1, x_2, s_2) = \frac{1}{\sqrt{2}}\left(\psi_1(x_1)\psi_2(x_2) + \psi_1(x_2)\psi_2(x_1)\right)\chi_0(s_1, s_2)$$

$$\Psi_t(x_1, s_1, x_2, s_2) = \frac{1}{\sqrt{2}}\left(\psi_1(x_1)\psi_2(x_2) - \psi_1(x_2)\psi_2(x_1)\right)\chi_1(s_1, s_2)$$

where $s, t$ refer to the singlet and triplet states

$$\chi_0(s_1, s_2) = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right)$$

$$\chi_1(s_1, s_2) = \left\{|\uparrow\uparrow\rangle\,;\;\frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle\right)\,;\;|\downarrow\downarrow\rangle\right\}$$

Now switch on a small interaction $V(x_1, x_2)$ and treat it perturbatively

$$\delta E = \int dx_1 \int dx_2 \sum_{s_1, s_2} |\psi(x_1, s_1, x_2, s_2)|^2\, V(x_1 x_2)$$

For the singlet and triplet states we obtain

$$\delta E_S = \int dx_1 \int dx_2\, |\psi_1(x_1)|^2 |\psi_2(x_2)|^2\, V(x_1, x_2)$$

$$+ \int dx_1 \int dx_2\, \psi_1^*(x_1)\psi_2^*(x_2)\, V(x_1, x_2)\,\psi_1(x_2)\psi_2(x_1)$$

$$\delta E_t = \int dx_1 \int dx_2\, |\psi_1(x_1)|^2 |\psi_2(x_2)|^2\, V(x_1, x_2)$$

$$- \int dx_1 \int dx_2\, \psi_1^*(x_1)\psi_2^*(x_2)\, V(x_1, x_2)\,\psi_1(x_1)\psi_2(x_2)$$

The first terms in both expressions are equal and go by the name "Hartree" term. It is readily recognized as a density-density interaction between the single-particle densities $|\psi_1(x_1)|^2$ and $|\psi_2(x_2)|^2$, blind to the spin state. The second term, the "Fock" or "exchange" term, has no classical interpretation. When the wave functions are real and positive and the interaction is repulsive, $V(x_1 x_2) > 0$, the triplet lies below the singlet in energy. In general, though, this need not hold.

*end of lecture*

### Example: Hund's rule

We saw that even though spin never enters the Hamiltonian explicitly, the energy of the eigenstates still depends on the spin orientation. The source is the electrostatic repulsion between electrons. In the spatially antisymmetric wave function the electrons have zero probability of coinciding and are, on average, farther apart than in the spatially symmetric state. Electrostatic repulsion therefore pushes the spatially symmetric state above its counterpart. The lowest-energy state thus has its spins aligned (in practice, a high-spin state). This gives Hund's rule for the magnetization of partially filled atomic shells in transition metals and rare earths: for shells half filled or less, all spins point the same way. It is a first step toward understanding ferromagnetism.

## 5.7 The Helium atom

This is a case where every consideration above comes into play.

$$\hat{H} = \hat{H}_1 + \hat{H}_2 + V(\vec{r}_1, \vec{r}_2)$$

$$= \frac{\hat{p}_1^2}{2m} + \frac{\hat{p}_2^2}{2m} - \frac{Ze^2}{|\vec{r}_1|} - \frac{Ze^2}{|\vec{r}_2|} + \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

with $Z = 2$. We drop the kinetic energy of the nucleus and hold the atomic positions fixed; the proton interaction is then constant. Although $V$ can be sizable, we treat it as a perturbation to begin with. The eigenstates of the unperturbed Hamiltonian are taken to be hydrogenic wave functions

$$|n_1, \ell_1, m_1\rangle_1 \otimes |n_2, \ell_2, m_2\rangle_2$$

### The ground state

We begin with $|100\rangle_1 \otimes |100\rangle_2$

We still need the spin state of the electrons. The only possibility is

$$\frac{1}{\sqrt{2}}\left[|+\rangle_1|-\rangle_2 - |-\rangle_1|+\rangle_2\right]$$

which is antisymmetric under spin exchange.

The ground state is then

$$|1s,1s\rangle = |100\rangle_1 |100\rangle_2 \, \frac{1}{\sqrt{2}} \left[ |+-\rangle - |-+\rangle \right]$$

The energy of the unperturbed state reads

$$E^{(0)}_{1s1s} = E^{(0)}_{1s} + E^{(0)}_{1s} = 2\left(-\frac{1}{2} m_e c^2 Z^2 \alpha^2\right) = -108.8 \text{ eV}$$

The first-order correction is

$$E^{(1)}_{1s1s} = \langle 1s\,1s | \frac{e^2}{|\vec{r}_1 - \vec{r}_2|} | 1s\,1s \rangle$$

Following the previous section, we get

$$E^{(1)}_{1s1s} = \int d\vec{r}_1 \int d\vec{r}_2 \; |\psi_{1s}(\vec{r}_1)|^2 \, |\psi_{1s}(\vec{r}_2)|^2 \, \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

which has the form

$$\int d^3 r_1 \int d^3 r_2 \; \frac{\rho(\vec{r}_1)\,\rho(\vec{r}_2)}{|\vec{r}_1 - \vec{r}_2|}$$

with $\rho(\vec{r}) = e\,|\psi_{1s}(\vec{r})|^2$.

This integral can be done exactly to give (see Townsend 12.31)

$$E^{(1)}_{1s,1s} = \frac{5}{8} Z \, m_e c^2 \alpha^2 = 34 \text{ eV}$$

Adding the two contributions, we obtain to first order

$$E_{1s,1s} \approx E^{(0)}_{1s,1s} + E^{(1)}_{1s,1s} = -74.8 \text{ eV}$$

The experimental value is $E_{\exp} = -78.8 \text{ eV}$.

### Excited states:

Consider now a state $|100\rangle \otimes |2\ell m\rangle$.

We can form 16 antisymmetric states

$$\frac{1}{\sqrt{2}} \left( |100\rangle_1 |2\ell m\rangle_2 - |2\ell m\rangle_1 |100\rangle_2 \right) \chi_1(s_1 s_2)$$

$$\frac{1}{\sqrt{2}} \left( |100\rangle_1 |2\ell m\rangle_2 + |2\ell m\rangle_1 |100\rangle_2 \right) \chi_0(s_1 s_2)$$

The unperturbed energy is

$$E_{1s,\,2s\,\text{or}\,2p} = E_{1s} + E_{2s\,\text{or}\,2p} =$$

$$= -\frac{1}{2} m_e c^2 Z^2 \alpha^2 \left(1 + \frac{1}{2^2}\right) = -68.0 \text{ eV}$$

Since this is a degenerate manifold, we must use degenerate perturbation theory.

Recall first that $[\hat{H}, \hat{S}^2] = [\hat{H}, \hat{S}^z] = 0$. The Hamiltonian therefore does not mix states with different $S^2$ or $S^z$. These four states are thus already eigenstates of the perturbation, whose matrix is diagonal

$$E^{(1)} = \frac{1}{2} \left( \langle 100| \langle 2\ell m| \pm \langle 2\ell m| \langle 100| \right) \frac{e^2}{|\vec{r}_1 - \vec{r}_2|}$$

$$\left( |100\rangle_1 |2\ell m\rangle_2 \pm |2\ell m\rangle_1 |100\rangle_2 \right)$$

$$= J \pm k$$

Here $J$ is the Hartree term, always positive, while $k$ is the Fock term, or exchange energy. By the earlier argument, the triplet of $S=1$ states is shifted by $J-k$, and the $S=0$ state by $J+k$.

*end of lecture*

Evaluating these integrals gives

$$E^{(1)}_{1s,2s} = J_{1s,2s} \pm k_{1s,2s} = 11.4 \text{ eV} \pm 1.2 \text{ eV}$$

$$E^{(1)}_{1s,2p} = J_{1s,2p} \pm k_{1s,2p} = 13.2 \text{ eV} \pm 0.9 \text{ eV}$$

$$\rightarrow E_{1s,2s} \approx -56.6 \text{ eV} \pm 1.2 \text{ eV}$$

$$E_{1s,2p} \approx -54.8 \text{ eV} \pm 0.9 \text{ eV}$$

*[Energy level diagram: from $E_0$ ($E_{1s2s}$), splitting into:*
- *$E_0 + J_{1s2s}$, further split by $2k_{1s2s}$ into singlet $E_0 + J + k$ (top) and triplet $E_0 + J - k$ (bottom)*
- *upper branch shows $2k_{1s2p}$ splitting]*

*[Lower diagram: spectroscopic levels with arrows — $^1P$, $^3P$, $^1S$, $^3S$]*


---

## References and Further Reading

*Editorial addition mapping the notes to their source text. The helium electron–electron repulsion integral is cited in the text as Townsend §12.31.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 5 (A System of Two Spin-½ Particles — addition of spins, the singlet and triplet states) and Ch. 12 (Identical Particles — exchange symmetry, the helium atom, §12.31).

**Further reading.** Sakurai & Napolitano, the "Identical Particles" chapter; Griffiths & Schroeter, the "Identical Particles" chapter; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XIV.
