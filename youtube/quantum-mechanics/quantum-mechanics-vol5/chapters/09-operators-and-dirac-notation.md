# Module M-09 — Operators and Dirac Notation
*When you need this: QM chapters II·1 (state space and formalism), II·2 (observables and measurement), II·3 (time evolution and the Schrödinger equation)*

Dirac introduced the bra-ket notation in a 1939 note in the *Proceedings of the Cambridge Philosophical Society*, with the stated motivation that "a good notation can be of great assistance." The insight was to split the inner product bracket $\langle\phi|\psi\rangle$ into two independently meaningful objects. Tracking what each object is — its type — eliminates most common algebraic errors.

---

## Bra–Ket Notation

The **ket** $|\psi\rangle$ is a vector in the Hilbert space $V$. The **bra** $\langle\phi|$ is a linear functional — an element of the dual space $V^*$ — that accepts a ket and returns the number $\langle\phi|\psi\rangle$. The inner product sets up a correspondence $|\phi\rangle \leftrightarrow \langle\phi|$ that is **anti-linear**: the bra corresponding to $a|\phi\rangle$ is $a^*\langle\phi|$. This conjugation is essential. Omitting it leads to spuriously complex expectation values and is the single most common error in the subject.

Type discipline — knowing what each expression is — prevents most algebraic mistakes:

| Expression | Type |
|---|---|
| $\langle\phi|\psi\rangle$ | Scalar (complex number) |
| $|\psi\rangle\langle\phi|$ | Operator (maps $|\chi\rangle\mapsto\langle\phi|\chi\rangle|\psi\rangle$) |
| $\hat A|\psi\rangle$ | Ket |
| $\langle\phi|\hat A$ | Bra |

The order matters: $\langle\phi|\psi\rangle$ is a number; $|\psi\rangle\langle\phi|$ is an operator.

![Two-row diagram: bra-ket inner product yielding a scalar versus ket-bra outer product yielding an operator](../images/09-operators-and-dirac-notation-fig-01.png)
*Figure 9.1 — Bra–ket type grammar: (top row) bra⟩⟨ket with open ends facing each other collapses to a scalar; (bottom row) ket⟩⟨bra with open ends facing outward produces an operator that maps kets to kets.*

---

## The Adjoint

The adjoint $\hat A^\dagger$ of an operator $\hat A$ is defined by:

$$\langle\phi\,|\,\hat A\psi\rangle = \langle\hat A^\dagger\phi\,|\,\psi\rangle \qquad \text{for all } |\phi\rangle, |\psi\rangle.$$

For matrices, $(\hat A^\dagger)_{ij} = A_{ji}^*$ — the conjugate transpose. Three rules that matter:

$$(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger \qquad \text{(reverses order)},$$
$$(c\hat A)^\dagger = c^*\hat A^\dagger,$$
$$(|\psi\rangle\langle\phi|)^\dagger = |\phi\rangle\langle\psi|.$$

The order-reversal rule is the analogue of the transpose rule for products. Writing $(\hat A\hat B)^\dagger = \hat A^\dagger\hat B^\dagger$ by analogy with scalars is incorrect for operators that do not commute.

![Diagram showing the adjoint flip: operator moving from ket side to bra side with dagger marker, plus three manipulation rule panels](../images/09-operators-and-dirac-notation-fig-02.png)
*Figure 9.2 — The adjoint as a flip across the inner product: (main) an operator on the ket side transfers to the bra side with a dagger marker; (lower strip) three rules — order reversal (AB)† = B†A†, scalar conjugation (cA)† = c*A†, and ket-bra adjoint swap.*

---

## Hermitian Operators

An operator is Hermitian (self-adjoint) if $\hat A^\dagger = \hat A$, equivalently:

$$\langle\phi\,|\,\hat A\psi\rangle = \langle\hat A\phi\,|\,\psi\rangle \qquad \text{for all }|\phi\rangle, |\psi\rangle.$$

A Hermitian operator can be moved freely from the right to the left of an inner product without changing the value — except for the conjugation that cancels in expectation values.

**Real eigenvalues — two-line proof.** Let $\hat A|a\rangle = a|a\rangle$. Sandwiching $\hat A$ between the eigenstate:

$$\langle a\,|\,\hat A\,|\,a\rangle = a\langle a|a\rangle.$$

The left side equals its own complex conjugate: $(\langle a|\hat A|a\rangle)^* = \langle a|\hat A^\dagger|a\rangle = \langle a|\hat A|a\rangle$, since $\hat A^\dagger = \hat A$. Therefore $a\langle a|a\rangle$ is real. Since $\langle a|a\rangle > 0$, $a$ must be real. $\square$

**Orthogonal eigenvectors — two-line proof.** Take $\hat A|a\rangle = a|a\rangle$ and $\hat A|b\rangle = b|b\rangle$ with $a \neq b$. We evaluate $\langle b|\hat A|a\rangle$ two ways:

- Acting right: $\langle b|\hat A|a\rangle = a\langle b|a\rangle$.
- Acting left: $\langle b|\hat A|a\rangle = \langle\hat A b|a\rangle = b\langle b|a\rangle$ (since $b$ is real).

Subtracting: $(a - b)\langle b|a\rangle = 0$. Since $a \neq b$: $\langle b|a\rangle = 0$. $\square$

These two results are central to the formalism: measurements yield real numbers because observables are Hermitian, and distinct outcomes are perfectly distinguishable because their eigenstates are orthogonal.

---

## Unitary Operators

An operator is unitary if $\hat U^\dagger\hat U = \hat I$ (equivalently $\hat U^\dagger = \hat U^{-1}$). Unitary operators preserve inner products:

$$\langle\hat U\phi\,|\,\hat U\psi\rangle = \langle\phi\,|\,\hat U^\dagger\hat U\,|\,\psi\rangle = \langle\phi|\psi\rangle.$$

Since probabilities are squared norms, unitary operators preserve probabilities. This is why time evolution and symmetry operations in quantum mechanics are unitary.

---

## The Resolution of the Identity

In an orthonormal basis $\{|n\rangle\}$:

$$\hat I = \sum_n |n\rangle\langle n|.$$

Each term $|n\rangle\langle n|$ is the projector onto the $n$-th basis direction. **Inserting** $\hat I$ **in this form** is the standard technique for: extracting components ($\langle n|\psi\rangle = c_n$), changing basis (insert between two operators), deriving the Born rule ($P(a_n) = |\langle a_n|\psi\rangle|^2$), and computing matrix elements ($A_{mn} = \langle m|\hat A|n\rangle$).

---

## The Spectral Decomposition

From the eigenbasis $\{\hat A|a_n\rangle = a_n|a_n\rangle\}$ of a Hermitian operator, the resolution of the identity gives:

$$\hat A = \sum_n a_n|a_n\rangle\langle a_n|.$$

The operator is the sum of (eigenvalue) $\times$ (projector onto eigenstate). Applying it to any $|\psi\rangle$ scales each eigen-component $\langle a_n|\psi\rangle$ by $a_n$.

---

## Expectation Values and the Born Rule

We expand a normalized state in the eigenbasis of $\hat A$: $|\psi\rangle = \sum_n c_n|a_n\rangle$, $c_n = \langle a_n|\psi\rangle$. The Born rule assigns probability $|c_n|^2$ to outcome $a_n$. The expectation value:

$$\langle\hat A\rangle \equiv \langle\psi\,|\,\hat A\,|\,\psi\rangle = \sum_{m,n} c_m^* c_n \langle a_m|\hat A|a_n\rangle = \sum_n a_n|c_n|^2,$$

which is exactly "sum of (outcome) $\times$ (probability)." Because $\hat A$ is Hermitian, $\langle\hat A\rangle$ is guaranteed real. A complex expectation value for a Hermitian operator indicates a dropped conjugate when forming the bra — use this as a reflex diagnostic.

---

## Commutators

The commutator of two operators is $[\hat A, \hat B] = \hat A\hat B - \hat B\hat A$. Properties:

$[\hat A, \hat B] = -[\hat B, \hat A]$ (antisymmetric). $[\hat A, \hat B\hat C] = [\hat A,\hat B]\hat C + \hat B[\hat A,\hat C]$ (Leibniz rule). $[\hat A, \hat B] = 0 \iff \hat A$ and $\hat B$ share a common eigenbasis $\iff$ both can be measured simultaneously with arbitrary sharpness.

**The canonical commutator** in one dimension:

$$[\hat x, \hat p] = i\hbar.$$

We derive it by letting both sides act on a test function $\psi(x)$:

$$[\hat x, \hat p]\psi = x(-i\hbar\,\partial_x\psi) - (-i\hbar)\,\partial_x(x\psi)
= -i\hbar x\psi' + i\hbar(\psi + x\psi') = i\hbar\psi.$$

Since this holds for all $\psi$, $[\hat x, \hat p] = i\hbar$. The factor $i\hbar$ follows from the definition $\hat p = -i\hbar\partial_x$ acting on functions.

---

## The Robertson Uncertainty Relation

For any two observables $\hat A$ and $\hat B$ in state $|\psi\rangle$, we define the variance $\sigma_A^2 = \langle(\hat A - \langle\hat A\rangle)^2\rangle$ and the shifted operators $\delta\hat A = \hat A - \langle\hat A\rangle$ (still Hermitian, since $\langle\hat A\rangle$ is real). Then $\sigma_A^2 = \|\delta\hat A\,\psi\|^2$. Setting $|f\rangle = \delta\hat A|\psi\rangle$ and $|g\rangle = \delta\hat B|\psi\rangle$, Cauchy–Schwarz gives $\|f\|^2\|g\|^2 \geq |\langle f|g\rangle|^2$. The imaginary part of $\langle f|g\rangle = \langle\psi|\delta\hat A\,\delta\hat B|\psi\rangle$ equals $\frac{1}{2i}\langle[\hat A,\hat B]\rangle$ (the commutator shifts cancel). Using $|\langle f|g\rangle|^2 \geq (\operatorname{Im}\langle f|g\rangle)^2$:

$$\boxed{\sigma_A\,\sigma_B \geq \tfrac{1}{2}\,|\langle[\hat A,\hat B]\rangle|.}$$

Robertson's uncertainty relation (1929). Applied to $[\hat x,\hat p] = i\hbar$: $\sigma_x\sigma_p \geq \hbar/2$.

![Four-stage vertical flowchart: Cauchy-Schwarz geometry → squared-norm inequality → real/imaginary decomposition → Robertson bound](../images/09-operators-and-dirac-notation-fig-03.png)
*Figure 9.3 — Robertson uncertainty from Cauchy–Schwarz: four-stage logical chain from the geometric overlap of two vectors through the squared inner product inequality, decomposition into real and imaginary parts with the commutator in the imaginary sub-box, to the final σ_A σ_B ≥ ½|⟨[Â,B̂]⟩| bound.*

This is a statement about **state preparation** — how narrowly concentrated a single quantum state can simultaneously be in two incompatible observables — derived from Cauchy–Schwarz and Hermiticity. It says nothing about what happens to a particle when it is measured. The disturbance version (Heisenberg's microscope) is a separate and weaker result, formalized by Ozawa in 2003. Conflating them is a well-documented error in physics education.

---

## Worked Example: Hermiticity of $\hat p = -i\hbar\partial_x$

The factor of $-i$ in the momentum operator is precisely what makes it Hermitian. We verify this by integration by parts on $L^2(\mathbb{R})$:

$$\langle\phi\,|\,\hat p\,\psi\rangle = \int_{-\infty}^{\infty}\phi^*(x)(-i\hbar)\,\partial_x\psi(x)\,dx.$$

Integrating by parts with $u = \phi^*$ and $dv = \partial_x\psi\,dx$:

$$= \bigl[-i\hbar\,\phi^*(x)\psi(x)\bigr]_{-\infty}^{\infty} + \int_{-\infty}^{\infty}(i\hbar\,\partial_x\phi^*)\psi\,dx = \int_{-\infty}^{\infty}(-i\hbar\,\partial_x\phi)^*\psi\,dx = \langle\hat p\,\phi\,|\,\psi\rangle.$$

The boundary term vanishes because square-integrable states decay at infinity. The conjugation $(-i)^* = +i$ flips the sign that integration by parts introduced, leaving $\hat p$ self-adjoint. Without the $-i$, the operator $\partial_x$ is anti-Hermitian ($\hat A^\dagger = -\hat A$) and its eigenvalues would be purely imaginary — unusable as measurement outcomes.

---

## Where These Methods Appear in the Quantum Series

**The full formalism in one place (QM II·1).** The correspondences are direct: states are kets up to overall phase; observables are Hermitian operators with real eigenvalues; measurement outcomes are eigenvalues of the spectral decomposition; the probability of outcome $a_n$ is $|\langle a_n|\psi\rangle|^2$; the wavefunction $\psi(x) = \langle x|\psi\rangle$ is the component in the continuous position basis; time evolution preserves probability because $\hat U(t) = e^{-i\hat Ht/\hbar}$ is unitary.

**The continuous-spectrum subtlety and rigged Hilbert space.** The formalism of this module is developed for discrete spectra. Position and momentum operators have continuous spectra: every real number is an eigenvalue, and the "eigenstates" $|x\rangle$ and $|p\rangle$ are not elements of $L^2(\mathbb{R})$. They are generalized eigenstates in the sense of the rigged Hilbert space (Gelfand triple $\Phi \subset L^2 \subset \Phi^*$), with orthonormality relations $\langle x|x'\rangle = \delta(x-x')$ and $\langle p|p'\rangle = \delta(p-p')$. In practice: use these formally (insert $\int|x\rangle\langle x|\,dx = \hat I$, use $\delta(x-x')$ to evaluate inner products) and interpret $|\langle x|\psi\rangle|^2\,dx = |\psi(x)|^2\,dx$ as a probability density, not a probability. Treating generalized eigenstates as formal limits of normalizable wave packets is adequate for all calculations in the QM series.

The connection to Module M-06: the overlap $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$ is the kernel of the Fourier transform. The change of basis from position to momentum representation is the Fourier transform:

$$\tilde\psi(p) = \langle p|\psi\rangle = \int\langle p|x\rangle\langle x|\psi\rangle\,dx = \int\frac{e^{-ipx/\hbar}}{\sqrt{2\pi\hbar}}\,\psi(x)\,dx.$$

**Compatible observables and quantum numbers (QM II·2).** $[\hat A, \hat B] = 0$ if and only if $\hat A$ and $\hat B$ share a common orthonormal eigenbasis — both observables can be simultaneously sharp, and a state can be labeled by both eigenvalues simultaneously. In hydrogen, $[\hat H, \hat L^2] = [\hat H, \hat L_z] = [\hat L^2, \hat L_z] = 0$, which is why states can be labeled by $(n, \ell, m)$. A **complete set of commuting observables (CSCO)** is a maximal set of mutually commuting Hermitian operators whose simultaneous eigenstates are nondegenerate — the minimal labeling that fully specifies a state. The quantum numbers of any system are the eigenvalues of its CSCO.

**Time evolution and the Schrödinger equation (QM II·3).** The Schrödinger equation $i\hbar\,\partial_t|\psi\rangle = \hat H|\psi\rangle$ has the formal solution $|\psi(t)\rangle = e^{-i\hat Ht/\hbar}|\psi(0)\rangle$. The operator $\hat U(t) = e^{-i\hat Ht/\hbar}$ is unitary when $\hat H$ is Hermitian (because $\hat U^\dagger = e^{+i\hat H^\dagger t/\hbar} = e^{+i\hat Ht/\hbar} = \hat U^{-1}$). In the energy eigenbasis:

$$|\psi(t)\rangle = \sum_n c_n\,e^{-iE_nt/\hbar}\,|E_n\rangle.$$

Each energy eigenstate oscillates at its own frequency $\omega_n = E_n/\hbar$ — the quantum analogue of normal modes.

**Beyond the source: superoperators and the Lindblad equation (QM IV·6).** When a quantum system interacts with an environment, the state requires a density matrix $\hat\rho$ — a Hermitian positive-semidefinite operator with $\operatorname{tr}\hat\rho = 1$. The dynamics under Markovian dissipation is the Lindblad equation:

$$\frac{d\hat\rho}{dt} = -\frac{i}{\hbar}[\hat H,\hat\rho] + \sum_k\left(\hat L_k\hat\rho\hat L_k^\dagger - \frac{1}{2}\hat L_k^\dagger\hat L_k\hat\rho - \frac{1}{2}\hat\rho\hat L_k^\dagger\hat L_k\right),$$

where $\hat L_k$ are the Lindblad operators encoding the dissipation channels. The right-hand side is a **superoperator** — a linear map from operators to operators. Finding steady states of the Lindblad equation is an eigenvalue problem in the space of operators. Every piece of superoperator algebra is built from the adjoint, commutator, and inner-product structure developed in this module.

---

## Conventions and Pitfalls

**Anti-linearity of the bra.** The bra dual to $a|\phi\rangle$ is $a^*\langle\phi|$. The symptom of forgetting this: a complex expectation value $\langle\hat A\rangle$ for a Hermitian $\hat A$. Since $\langle\hat A\rangle = \langle\hat A\rangle^*$ for any Hermitian operator, a complex result is a guaranteed error indicator.

**Order is not optional.** $|\psi\rangle\langle\phi|$ is an operator and $\langle\phi|\psi\rangle$ is a scalar. Most errors in Dirac notation come from accidentally swapping this order.

**Adjoint reverses order.** $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger$. Writing it the other way is the operator-algebra analogue of $(AB)^T = B^TA^T$ for matrices.

**Hermitian vs. self-adjoint in infinite dimensions.** In finite dimensions these coincide exactly. In infinite dimensions they can come apart: an operator may satisfy $\langle\phi|\hat A\psi\rangle = \langle\hat A\phi|\psi\rangle$ on its natural dense domain (symmetric) yet fail to be self-adjoint because the domain of $\hat A$ and the domain of $\hat A^\dagger$ differ. The canonical example: $\hat p = -i\hbar\partial_x$ on the half-line $[0,\infty)$ — the boundary term $[-i\hbar\phi^*\psi]_0^\infty$ no longer vanishes, and self-adjoint extensions require specifying a boundary condition at $x=0$. Different boundary conditions give different self-adjoint extensions with different spectra. For the full-line problem with decaying states, the boundary term vanishes and the distinction does not arise.

**Robertson vs. measurement disturbance.** Robertson's inequality says nothing about what happens to a particle when it is measured. It is a statement about any single quantum state — about how sharply any one state can be simultaneously concentrated in two non-commuting observables. Conflating this with Heisenberg's microscope argument is a persistent error.

---

## Quick Practice

1. Show that $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger$ directly from the defining relation $\langle\phi|\hat A\psi\rangle = \langle\hat A^\dagger\phi|\psi\rangle$. Then verify the specific case $\hat A = \sigma_x$, $\hat B = \sigma_z$ in $\mathbb{C}^2$.

2. Compute the commutator $[\hat x, \hat p^2]$ using $[\hat x, \hat p] = i\hbar$ and the Leibniz identity $[\hat A,\hat B\hat C] = [\hat A,\hat B]\hat C + \hat B[\hat A,\hat C]$. What physical consequence follows from $[\hat x, \hat p^2] \neq 0$?

3. A normalized state is $|\psi\rangle = \frac{1}{\sqrt{3}}|+\rangle + \sqrt{\frac{2}{3}}|-\rangle$, where $|\pm\rangle$ are the eigenstates of $\hat S_z$ with eigenvalues $\pm\hbar/2$. Compute $\langle\hat S_z\rangle$ and $\sigma_{S_z}^2 = \langle\hat S_z^2\rangle - \langle\hat S_z\rangle^2$ using the spectral decomposition $\hat S_z = \frac{\hbar}{2}|+\rangle\langle+| - \frac{\hbar}{2}|-\rangle\langle-|$.

---

## Go Deeper

Full derivations of all results in this module: *Mathematics for Physics*, Vol. 2, Ch. 5 (inner-product axioms, Cauchy–Schwarz, Gram–Schmidt, resolution of the identity, Dirac notation, adjoint, Hermitian and unitary operators, Robertson derivation, worked examples).

For Hermitian vs. self-adjoint in infinite dimensions, self-adjoint extensions, and the rigorous spectral theorem for unbounded operators: Reed, M., and Simon, B. *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness.* Academic Press, 1975.

For the rigged Hilbert space and generalized eigenfunctions: Gel'fand, I. M., and Vilenkin, N. Ya. *Generalized Functions, Vol. 4.* Academic Press, 1964. An accessible physics treatment: Ballentine, L. E. *Quantum Mechanics: A Modern Development.* World Scientific, 1998, Ch. 1.

---

## References

Dirac, P. A. M. (1939). A new notation for quantum mechanics. *Mathematical Proceedings of the Cambridge Philosophical Society*, 35, 416–418.

Dirac, P. A. M. (1930, 4th ed. 1958). *The Principles of Quantum Mechanics*. Oxford University Press.

von Neumann, J. (1932/1955). *Mathematical Foundations of Quantum Mechanics*. Princeton University Press.

Robertson, H. P. (1929). The uncertainty principle. *Physical Review*, 34, 163–164.

Ozawa, M. (2003). Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement. *Physical Review A*, 67, 042105.

Lindblad, G. (1976). On the generators of quantum dynamical semigroups. *Communications in Mathematical Physics*, 48, 119–130.

Reed, M., & Simon, B. (1975). *Methods of Modern Mathematical Physics, Vol. II*. Academic Press.

Gel'fand, I. M., & Vilenkin, N. Ya. (1964). *Generalized Functions, Vol. 4*. Academic Press.

Shankar, R. (1994). *Principles of Quantum Mechanics* (2nd ed.). Plenum.

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*. Wiley.
