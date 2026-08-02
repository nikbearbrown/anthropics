# Chapter 2 — The Hydrogen Atom

*The last atom we can solve in closed form — the benchmark every approximation answers to.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Here is the remarkable thing about hydrogen: one electron, one proton, a $1/r$ pull between them, and the whole spectrum drops out exactly. No perturbation series, no variational guess — just a differential equation and the demand that the wavefunction stay finite. That demand is the entire trick. We separate the angular part (already handled by the central-potential machinery) from the radial part, then squeeze the radial equation between two boundary conditions: it cannot blow up at infinity, and it cannot blow up at the origin. Each condition fixes the form of the solution at one end. What survives in the middle is a power series — and that series only stays a polynomial, only stays normalizable, for a discrete set of energies. Quantization is not imposed; it is forced.

The payoff is the spectrum $E_n = -\mu Z^2 e^4/2\hbar^2 n^2$, energies depending on $n$ alone. The angular momentum $\ell$ drops out entirely, which is strange — the $m$-degeneracy comes from rotational symmetry, but the $\ell$-degeneracy demands a deeper reason. That reason is the Laplace–Runge–Lenz vector, a conserved quantity special to $1/r$ potentials. Its algebra is powerful enough that Pauli extracted the full spectrum from it before Schrödinger wrote his equation. Hydrogen is the last atom we solve cleanly; everything heavier is measured against it.

## 2.1 The hydrogen atom

The hydrogen atom is a nucleus of charge $+Ze$ with an electron bound to it by the attractive Coulomb force. With only one electron, we drop spin from the picture. Exactly as in the classical two-body problem, we work in the center-of-mass frame and let the reduced mass stand in for the electron mass in the Hamiltonian

$$\hat{H} = \frac{\hat{p}_e^2}{2\mu} - \frac{Ze^2}{|\vec{r}|}$$

$$\mu = \frac{m_e m_p}{m_e + m_p} \quad ; \quad m_p \approx 1836\,m_e \to \mu \approx m_e$$

$$Z = 1 \quad \text{for hydrogen}$$

In spherical coordinates

$$\hat{H} = \frac{\hat{p}_r^2}{2\mu} + \frac{\hbar^2\hat{L}^2}{2\mu r^2} - \frac{Ze^2}{r} = \frac{\hat{p}_r^2}{2\mu} + \frac{\hbar^2\ell(\ell+1)}{2\mu r^2} - \frac{Ze^2}{r}$$

As before, the task reduces to solving the radial eigenvalue problem at fixed $\ell$

$$\frac{d^2\chi}{dr^2} + \left[\frac{2\mu E}{\hbar^2} + \frac{2\mu Ze^2}{\hbar^2 r} - \frac{\ell(\ell+1)}{r^2}\right]\chi = 0$$

It pays to switch to dimensionless variables

$$\rho = \frac{\sqrt{8\mu|E|}}{\hbar}\,r \quad ; \quad \rho_0 = \sqrt{\frac{\mu}{2|E|}}\,\frac{Ze^2}{\hbar}$$

$$\longrightarrow \quad \frac{d^2\chi}{d\rho^2} - \left[\frac{1}{4} - \frac{\rho_0}{\rho} + \frac{\ell(\ell+1)}{\rho^2}\right]\chi = 0$$

For $\rho \gg 1$:

$$\frac{d^2\chi}{d\rho^2} - \frac{1}{4}\chi = 0 \quad \longrightarrow \quad \chi \sim e^{\pm\rho/2}$$

Since the solution must not diverge, we keep only the decaying exponential.

For $\rho \to 0$:

We try $\rho^s$ in the differential equation

$$s(s-1)\rho^{s-2} + \rho_0\rho^{s-1} - \frac{1}{4}\rho^s - \ell(\ell+1)\rho^{s-2} = 0$$

In the limit $\rho \to 0$ the $\rho^{s-2}$ terms dominate.

Killing the singularity requires

$$-s(s-1) + \ell(\ell+1) = 0$$

$\longrightarrow s = \ell+1$, or $s = -\ell$. We throw out $\rho^{-\ell}$ because:
- For $\ell \geq 1$, $\chi$ diverges.
- For $\ell = 0$, $R \sim \dfrac{1}{r}$, also diverges.

$$\longrightarrow \quad \chi \to \rho^{\ell+1} \quad \text{for } \rho \to 0$$

With both limits in hand, we write a general trial solution

$$\chi(\rho) = \rho^{\ell+1} \, e^{-\rho/2} \, P(\rho)$$

Inserting this into the radial equation gives

$$\frac{d^2 P}{d\rho^2} + \left(\frac{2\ell+2}{\rho} - 1\right)\frac{dP}{d\rho} + \left(\frac{\rho_0 + \ell + 1}{\rho}\right)P = 0$$

Take $P(\rho) = \displaystyle\sum_{k=0}^{\infty} c_k \rho^k$ with $c_0 \neq 0$

$$\longrightarrow \sum_{k=2}^{\infty} k(k-1)c_k\rho^{k-2} + \sum_{k=1}^{\infty}(2\ell+2)k\,c_k\rho^{k-2} + \sum_{k=0}^{\infty}\left(-k+\rho_0-(\ell+1)\right)c_k\rho^{k-1} = 0$$

which rearranges to

$$\sum_{k=0}^{\infty}\left\{k(k+1) + (2\ell+2)(k+1)\,c_{k+1} + \left(-k+\rho_0-(\ell+1)\right)c_k\right\}\rho^{k-1} = 0$$

$$\longrightarrow \quad \frac{c_{k+1}}{c_k} = \frac{k+\ell+1-\rho_0}{(k+1)(k+2\ell+2)}$$

Note that $\dfrac{c_{k+1}}{c_k} \overset{k\to\infty}{\longrightarrow} \dfrac{1}{k}$, so the unterminated series grows like $e^\rho$. The series must therefore cut off

$$\rho_0 = 1+\ell+k_{\max}, \quad \text{with } k_{\max} = 0,1,2,\ldots$$

The solution is then a polynomial of degree $n$. Quantizing $\rho_0$ this way yields

$$E = -\frac{\mu Z^2 e^4}{2\hbar^2(1+\ell+k_{\max})^2}$$

With $k_{\max}$ and $\ell$ both non-negative integers, we set $n = 1+\ell+k_{\max}$

$$\boxed{\,E_n = -\frac{\mu Z^2 e^4}{2\hbar^2 n^2}\,} \qquad n = 1,2,3,\ldots$$

$$E_n = -\frac{Z^2}{2n^2}\,E_h$$

With $E_h = \dfrac{\mu e^4}{\hbar^2} \approx 4.36\times10^{-18}\,\text{J} \approx 27.2\,\text{eV} = 1\,\text{Hartree}$

The ground state corresponds to $n=1$, $Z=1$:

$$E_1 = 0.5\,\text{Hartree} = -1\,\text{Ry} \quad (\text{Rydberg})$$

The polynomials appearing in the solution are the "Laguerre polynomials".

### Hydrogenic wave functions

$$\psi_{n\ell m}(r,\theta,\varphi) = R_{n\ell}(r)\,Y_\ell^m(\theta,\varphi) = \frac{\chi_{n\ell}(r)}{r}\,Y_\ell^m(\theta,\varphi)$$

Written in the dimensionless variable $\rho$

$$\rho = \sqrt{\frac{8\mu|E|}{\hbar^2}}\,r = \frac{2Z}{n}\frac{r}{a_0}$$

with $a_0 = \dfrac{\hbar}{\mu c\alpha}$ ; $\alpha = \dfrac{e^2}{\hbar c} \sim \dfrac{1}{137}$ (fine-structure constant)

$a_0$ is the Bohr radius $a_0 \sim 0.529\,\text{Å}$

$$R_{10} = 2\left(\frac{Z}{a_0}\right)^{3/2} e^{-Zr/a_0}$$

$$R_{20} = 2\left(\frac{Z}{2a_0}\right)^{3/2}\left(1 - \frac{Zr}{2a_0}\right)e^{-Zr/2a_0}$$

$$R_{21} = \frac{1}{\sqrt{3}}\left(\frac{Z}{2a_0}\right)^{3/2}\frac{Zr}{a_0}\,e^{-Zr/2a_0}$$

**Example:** An electron in the Coulomb field of a proton is in the state

$$|\psi\rangle = \frac{1}{\sqrt{2}}|1,0,0\rangle + \frac{1}{\sqrt{2}}|2,1,1\rangle$$

a) What is $|\psi(t)\rangle$ ?

b) Calculate $\langle E\rangle$, $\langle L^2\rangle$, $\langle L_x\rangle$, $\langle L_y\rangle$, $\langle L_z\rangle$

**Solution**

a) $$|\psi(t)\rangle = \frac{e^{-iE_1 t/\hbar}}{\sqrt{2}}|1,0,0\rangle + \frac{e^{-iE_2 t/\hbar}}{\sqrt{2}}|2,1,1\rangle$$

b) $$\langle E\rangle = \langle\psi(t)|H|\psi(t)\rangle = \frac{1}{2}E_1 + \frac{1}{2}E_2$$

$$\langle L^2\rangle = \frac{1(1+1)\hbar^2}{2} = \hbar^2$$

$$\langle L_z\rangle = \frac{\hbar}{2}$$

$$\langle L_x\rangle = \frac{1}{2}\langle L_+ + L_-\rangle =$$
$$= \frac{1}{2}\left(\frac{e^{iE_1 t/\hbar}}{\sqrt{2}}\langle 1,0,0| + \frac{e^{iE_2 t/\hbar}}{\sqrt{2}}\langle 2,1,1|\right)\hbar\,e^{-iE_2 t/\hbar}|2,1,0\rangle = 0$$

(same for $\langle L_y\rangle = 0$)

### Degeneracy

For a given $n$, the permitted values of $\ell$ are

$$\ell = 0, \ldots, n-1$$

For a given $\ell$, the permitted values of $m$ are

$$m = -\ell, -\ell+1, \ldots, \ell-1, \ell$$

Summing over both, the total degeneracy at fixed $n$ is

$$\sum_{\ell=0}^{n-1}(2\ell+1) = \frac{2(n-1)n}{2} + n = n^2$$

(Energy level diagram: vertical axis $E$, horizontal axis $\ell$. Levels shown at $n=1$ (lowest), $n=2$, $n=3$, $n=4$. Columns labeled $\ell=0$ (s), $\ell=1$ (p), $\ell=2$ (d), $\ell=3$ (f), with increasing numbers of states across rows.)

*end lecture*

That the energy ignores $\ell$ is far from obvious — the $m$-degeneracy follows plainly from rotational symmetry, but this one does not.

The extra degeneracy springs from a "hidden symmetry" present whenever the central potential takes the form $V(r) = -k/r$ (Kepler problems). Classically, this shows up as an additional conserved quantity:

$$\vec{A} = \vec{p}\times\vec{L} - \mu k\frac{\vec{r}}{r} \qquad \text{"Laplace-Runge-Lenz vector"}$$

The quantum counterpart is defined as

$$\hat{\vec{A}} = \hat{\vec{p}}\times\hat{\vec{L}} - \mu Ze^2\frac{\hat{\vec{r}}}{r}$$

One can verify that $[\hat{H}, \hat{A}] = 0$.

Strikingly, this conservation law and the algebra it generates let Pauli derive the hydrogen spectrum in 1926 *before* the Schrödinger equation existed !!!

**Exercise:** $[\hat{H}, \hat{A}_\alpha] = 0$ ; $[\hat{A}_\alpha, \hat{L}_\beta] = i\hbar\epsilon_{\alpha\beta\gamma}\hat{A}_\gamma$

$$[\hat{A}_\alpha, \hat{A}_\beta] = i\hbar\epsilon_{\alpha\beta\gamma}(-2m\hat{H})\hat{L}_\gamma$$


---

## References and Further Reading

*Editorial addition mapping the notes to their source text.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 9 (Translational and Rotational Symmetry in the Two-Body Problem) and Ch. 10 (Bound States of Central Potentials — the hydrogen atom).

**Further reading.** Griffiths & Schroeter, *Introduction to Quantum Mechanics*, the "Quantum Mechanics in Three Dimensions" chapter (the hydrogen atom); Sakurai & Napolitano, the central-potential sections; Shankar, *Principles of Quantum Mechanics*, Ch. 12–13.
