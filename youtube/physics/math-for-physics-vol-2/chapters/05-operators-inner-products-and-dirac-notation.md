# Operators, Inner Products, and Dirac Notation

*Inner-product spaces, Hermitian and unitary operators, the real spectra of observables, commutators, and bra–ket notation — the linear-algebraic language quantum mechanics is written in.*

---

## 1. Cold open: why a measurement must come out real

A quantum particle is in some state. You measure its energy. The needle settles on a number — a real number, like every reading any apparatus has ever produced. You repeat the preparation and measure again; sometimes you get a different number, but always a real one, and always one of a discrete, reproducible list of allowed values. Measure energy on a stationary state of a hydrogen atom and you get one of the Bohr levels, never a value in between, never a complex number.

Quantum mechanics encodes the state as a vector $|\psi\rangle$ in a complex vector space — complex, because interference and phases are real physics. The observable (energy, position, spin) is encoded as an operator $\hat{A}$ acting on that space, and the measurement's possible outcomes are the *eigenvalues* of $\hat{A}$. But the state space is complex and a general operator's eigenvalues are complex. So how does the theory guarantee that every measurement yields a real number? And why, when you measure the same observable on a state that happens to be one of its eigenvectors, do you get the *same* answer every time with certainty?

The answers are not physics axioms pulled from the air. They are theorems about a particular class of operators — the **Hermitian** operators — and they follow in a line or two from the structure of an inner-product space. Chapter 4 found eigenvalues and eigenvectors of finite matrices. This chapter promotes matrices to operators, equips the space with an inner product, and proves the two facts the cold open demands: Hermitian operators have real eigenvalues, and their eigenvectors are orthogonal. That is *why* observables are Hermitian.

---

## 2. The tool, named

Volume 1 introduced the dot product of arrows and, in its Fourier-series chapter, the idea of expanding a function in an orthogonal family of sines and cosines with coefficients computed by integration. Chapter 4 gave abstract vector spaces and the finite-dimensional spectral theorem. This chapter fuses the two: an abstract vector space with an **inner product**, which gives it lengths, angles, and orthogonality — and so makes the spectral theorem geometric and the language of quantum mechanics possible.

The new objects are: the inner product $\langle \phi | \psi \rangle$, a complex number measuring overlap; **orthonormal bases** and the resolution of the identity; the **adjoint** $\hat{A}^\dagger$ of an operator; the **Hermitian** ($\hat A^\dagger = \hat A$) and **unitary** ($\hat U^\dagger \hat U = \hat I$) operators that carry, respectively, observables and symmetries; the **commutator** $[\hat A, \hat B]$ that measures the failure of two operators to share an answer; and **Dirac's bra–ket notation**, designed so that all of this reads almost without computation.

---

## 3. Development & derivation

### Inner-product spaces

An **inner product** on a complex vector space assigns to each ordered pair of vectors a complex number $\langle \phi | \psi \rangle$ satisfying three axioms. We adopt the **physicist's convention** (conjugate-linear in the *first* slot), and we commit to it for the whole book:

1. **Conjugate symmetry:** $\langle \phi | \psi \rangle = \langle \psi | \phi \rangle^*$.
2. **Linearity in the second argument:** $\langle \phi | (a\psi_1 + b\psi_2) \rangle = a\langle \phi | \psi_1 \rangle + b\langle \phi | \psi_2 \rangle$. (By conjugate symmetry it is then *anti*-linear in the first.)
3. **Positive-definiteness:** $\langle \psi | \psi \rangle \geq 0$, with equality only for $|\psi\rangle = 0$.

The norm is $\| \psi \| = \sqrt{\langle \psi | \psi \rangle}$, and a **unit vector** has $\langle \psi | \psi \rangle = 1$. For column vectors in $\mathbb{C}^n$ the inner product is $\langle \phi | \psi \rangle = \sum_i \phi_i^* \psi_i$ (note the conjugate — without it the norm would not be positive); for functions on an interval it is $\langle \phi | \psi \rangle = \int \phi^*(x)\psi(x)\,dx$. Two vectors are **orthogonal** when $\langle \phi | \psi \rangle = 0$.

One inequality does enormous work. For any two vectors, the **Cauchy–Schwarz inequality** holds:

$$
|\langle \phi | \psi \rangle|^2 \leq \langle \phi | \phi \rangle\, \langle \psi | \psi \rangle.
$$

*Proof.* If $|\psi\rangle = 0$ both sides vanish. Otherwise consider $|\chi\rangle = |\phi\rangle - \frac{\langle \psi | \phi \rangle}{\langle \psi | \psi \rangle}|\psi\rangle$, the part of $\phi$ left after subtracting its projection onto $\psi$. Positive-definiteness gives $\langle \chi | \chi \rangle \geq 0$; expanding that expression and clearing the denominator yields exactly the inequality. We will need it for the uncertainty relation. $\quad\blacksquare$

### Orthonormal bases and the resolution of the identity

A basis $\{|n\rangle\}$ is **orthonormal** if $\langle m | n \rangle = \delta_{mn}$ (Kronecker delta: $1$ if $m=n$, else $0$). Any orthonormal set can be built from a merely independent one by **Gram–Schmidt** orthonormalization (Schmidt, 1907): take each vector in turn, subtract its projections onto the already-orthonormalized ones, and normalize. In an orthonormal basis the expansion coefficients of any vector are just inner products:

$$
|\psi\rangle = \sum_n c_n |n\rangle, \qquad
c_n = \langle n | \psi \rangle,
$$

because $\langle m | \psi \rangle = \sum_n c_n \langle m | n \rangle = c_m$. Substituting $c_n = \langle n|\psi\rangle$ back gives the single most-used identity in quantum mechanics:

$$
|\psi\rangle = \sum_n |n\rangle\langle n | \psi\rangle
\quad\Longrightarrow\quad
\boxed{\;\sum_n |n\rangle\langle n| = \hat{I}.\;}
$$

This is the **resolution of the identity**. Each term $|n\rangle\langle n|$ is the projector onto the $n$-th basis direction; summed, they reconstruct the whole. You can slip $\hat I$ in this form into any expression to change basis or insert intermediate states — the workhorse move of the formalism.

![A state vector psi resolved into two orthonormal basis directions. Its components are the inner products bra a-one ket psi and bra a-two ket psi, the lengths of its shadows on each axis. A side box gives the Born-rule probabilities as the squared components, which sum to one.](images/05-operators-inner-products-and-dirac-notation-fig-01.png)
*Figure 5.1 — A state's components in an orthonormal basis are the inner products $c_n=\langle a_n|\psi\rangle$; the Born rule reads the squared components as probabilities, with $\sum|c_n|^2=1$.*

### Dirac notation

P. A. M. Dirac introduced bra–ket notation in a 1939 note titled, fittingly, "A new notation for quantum mechanics," motivated by the conviction that "a good notation can be of great assistance." Split the bracket $\langle \phi | \psi \rangle$ into two halves:

- the **ket** $|\psi\rangle$ is a vector in the space $V$;
- the **bra** $\langle \phi |$ is a *linear functional* — a machine that eats a ket and returns the number $\langle \phi | \psi \rangle$. The bras form the **dual space** $V^*$, and the inner product sets up the correspondence $|\phi\rangle \leftrightarrow \langle \phi|$.

The correspondence is **anti-linear**: the bra paired with $a|\phi\rangle$ is $a^* \langle \phi|$. This conjugation is not decoration; forgetting it is the single most common error in the subject, and it produces the telltale symptom of a spuriously complex expectation value. Knowing what *type* each object is — ket, bra, operator, or scalar — prevents most mistakes: $|\psi\rangle\langle\phi|$ is an **operator** (ket times bra), while $\langle\phi|\psi\rangle$ is a **scalar** (bra times ket). The order matters absolutely.

![Left, the inner product bra phi ket psi shown as the overlap of two vectors, its magnitude given by the cosine of the angle between them. Right, a grammar table: bra times ket gives a scalar number, ket times bra gives an operator, and summed projectors give the resolution of the identity.](images/05-operators-inner-products-and-dirac-notation-fig-03.png)
*Figure 5.3 — Bra–ket grammar: $\langle\phi|\psi\rangle$ is an overlap (a scalar), $|\psi\rangle\langle\phi|$ is an operator — the order decides the type.*

### The adjoint, and Hermitian and unitary operators

An operator $\hat A$ maps kets to kets. Its **adjoint** $\hat A^\dagger$ is defined by how it moves across the inner product:

$$
\langle \phi | \hat A \psi \rangle = \langle \hat A^\dagger \phi | \psi \rangle
\quad\text{for all } |\phi\rangle, |\psi\rangle.
$$

For matrices the adjoint is the conjugate transpose, $(\hat A^\dagger)_{ij} = A_{ji}^*$. Taking the dagger reverses order and conjugates: $(\hat A \hat B)^\dagger = \hat B^\dagger \hat A^\dagger$, and $(c\hat A)^\dagger = c^* \hat A^\dagger$. Two special classes:

- **Hermitian (self-adjoint):** $\hat A^\dagger = \hat A$. These carry observables. They are the operators that can be moved freely from one side of an inner product to the other: $\langle \phi | \hat A \psi \rangle = \langle \hat A \phi | \psi \rangle$.
- **Unitary:** $\hat U^\dagger \hat U = \hat I$, equivalently $\hat U^\dagger = \hat U^{-1}$. These preserve inner products: $\langle \hat U\phi | \hat U\psi \rangle = \langle \phi | \hat U^\dagger \hat U | \psi \rangle = \langle \phi | \psi \rangle$. Because they preserve norms, they preserve probabilities — which is why time evolution and symmetries are unitary.

> **A caveat for infinite dimensions.** In finite dimensions "Hermitian" (symmetric: $\langle\phi|\hat A\psi\rangle=\langle\hat A\phi|\psi\rangle$ on all vectors) and "self-adjoint" coincide exactly. In infinite dimensions they can come apart: an operator may be symmetric on its natural domain yet *fail* to be self-adjoint, because of subtleties about which functions it is allowed to act on and whether boundary terms vanish. The canonical trap is the momentum operator on a half-line, which is symmetric but not self-adjoint. The full account (domains, deficiency indices) belongs to functional analysis — see Reed and Simon. For this book we work where the distinction is harmless and flag it where it is not; the real-spectrum theorem below holds for genuinely self-adjoint operators.

### Hermitian ⟹ real eigenvalues and orthogonal eigenvectors

This is the central derivation, and it is the cold open's answer. Let $\hat A$ be Hermitian with $\hat A|a\rangle = a|a\rangle$, $|a\rangle \neq 0$.

**Real eigenvalues.** Sandwich $\hat A$ in the eigenstate:

$$
\langle a | \hat A | a \rangle = a \langle a | a \rangle.
$$

Now take the complex conjugate of the left side. By conjugate symmetry, $\langle a|\hat A|a\rangle^* = \langle a | \hat A^\dagger | a\rangle$ — but $\hat A^\dagger = \hat A$, so the conjugate equals $\langle a|\hat A|a\rangle$ itself. The number $\langle a|\hat A|a\rangle$ is its own conjugate, hence real. Since $\langle a | a \rangle > 0$ is real and positive,

$$
a = \frac{\langle a | \hat A | a \rangle}{\langle a | a \rangle} \in \mathbb{R}.
$$

Every eigenvalue of a Hermitian operator is real. Measurements come out real because observables are Hermitian.

![The complex plane with the real axis marked. A general operator's eigenvalues could lie off-axis (shown crossed out as forbidden), but a Hermitian operator's eigenvalues all fall on the real axis as discrete levels E-one, E-two, E-three. A side box gives the two-line proof that the eigenvalue equals its own conjugate.](images/05-operators-inner-products-and-dirac-notation-fig-02.png)
*Figure 5.2 — A Hermitian operator's eigenvalues are pinned to the real axis: because $\hat A^\dagger=\hat A$, the expectation $\langle a|\hat A|a\rangle$ equals its own conjugate, so $a$ is real — which is why measurements never read off a complex number.*

**Orthogonal eigenvectors.** Take two eigenstates with distinct eigenvalues, $\hat A|a\rangle = a|a\rangle$ and $\hat A|b\rangle = b|b\rangle$, $a \neq b$ (both real now). Evaluate $\langle b | \hat A | a \rangle$ two ways. Acting right: $\langle b|\hat A|a\rangle = a\langle b | a\rangle$. Acting left, using Hermiticity to move $\hat A$ onto the bra, where it returns the (real) eigenvalue $b$: $\langle b|\hat A|a\rangle = b \langle b | a \rangle$. Subtract:

$$
(a - b)\langle b | a \rangle = 0.
$$

Since $a \neq b$, we conclude $\langle b | a \rangle = 0$: **eigenvectors of distinct eigenvalues are orthogonal.** Distinct measurement outcomes correspond to perfectly distinguishable states. (Degenerate eigenvalues share an eigenspace, which Gram–Schmidt renders orthonormal.) The eigenstates of a Hermitian operator thus form an orthonormal basis — the **spectral decomposition**:

$$
\hat A = \sum_n a_n |a_n\rangle\langle a_n|.
$$

The operator is literally the sum of its eigenvalues times the projectors onto its eigenstates. Apply it to any $|\psi\rangle$ and you read off what it does: scale each eigen-component $\langle a_n|\psi\rangle$ by $a_n$.

### Expectation values and the Born rule

Expand a normalized state in an observable's eigenbasis, $|\psi\rangle = \sum_n c_n |a_n\rangle$ with $c_n = \langle a_n|\psi\rangle$. The Born rule says a measurement of $\hat A$ yields outcome $a_n$ with probability $|c_n|^2 = |\langle a_n | \psi\rangle|^2$ — the squared overlap, a geometric projection. The **expectation value** is the average outcome, and Dirac notation computes it in one line:

$$
\langle \hat A \rangle = \langle \psi | \hat A | \psi \rangle
= \sum_{m,n} c_m^* c_n \langle a_m | \hat A | a_n \rangle
= \sum_{m,n} c_m^* c_n\, a_n \delta_{mn}
= \sum_n a_n |c_n|^2,
$$

precisely $\sum_n (\text{outcome})\times(\text{probability})$. And because $\hat A$ is Hermitian, $\langle\hat A\rangle$ is guaranteed real — if your computation returns a complex number, you dropped a conjugate when forming the bra. That is a reflex worth building.

### Commutators and the uncertainty structure

Operators need not commute: in general $\hat A \hat B \neq \hat B \hat A$. The **commutator**

$$
[\hat A, \hat B] = \hat A\hat B - \hat B\hat A
$$

measures the failure. If $[\hat A,\hat B] = 0$, the two operators share a common eigenbasis and *can* be measured simultaneously to arbitrary sharpness; if not, they cannot. The canonical example is position and momentum, $[\hat x, \hat p] = i\hbar$.

How much sharpness must be sacrificed is **Robertson's uncertainty relation** (1929). Define the spread of $\hat A$ in state $|\psi\rangle$ as $\sigma_A^2 = \langle (\hat A - \langle \hat A\rangle)^2\rangle$, and let $\delta\hat A = \hat A - \langle\hat A\rangle$ (Hermitian, since $\langle\hat A\rangle$ is real). Then $\sigma_A^2 = \langle\psi|\delta\hat A^2|\psi\rangle = \langle\, \delta\hat A\psi | \delta\hat A\psi\rangle = \|\delta\hat A\,\psi\|^2$, using Hermiticity. Apply Cauchy–Schwarz to the vectors $|f\rangle = \delta\hat A|\psi\rangle$ and $|g\rangle = \delta\hat B|\psi\rangle$:

$$
\sigma_A^2\,\sigma_B^2 = \|f\|^2\,\|g\|^2 \geq |\langle f | g\rangle|^2.
$$

The overlap $\langle f|g\rangle = \langle\psi|\delta\hat A\,\delta\hat B|\psi\rangle$ is a complex number; its imaginary part is $\frac{1}{2i}\langle\psi|[\delta\hat A,\delta\hat B]|\psi\rangle = \frac{1}{2i}\langle[\hat A,\hat B]\rangle$ (the constant shifts drop out of the commutator). Since $|\langle f|g\rangle|^2 \geq (\operatorname{Im}\langle f|g\rangle)^2$,

$$
\sigma_A^2\,\sigma_B^2 \geq \left(\frac{1}{2i}\langle[\hat A,\hat B]\rangle\right)^2,
\qquad\text{so}\qquad
\boxed{\;\sigma_A\,\sigma_B \geq \tfrac12\,\big|\langle [\hat A,\hat B]\rangle\big|.\;}
$$

This is a statement about *state preparation* — about how concentrated a single state can be in two observables at once — derived purely from Cauchy–Schwarz and Hermiticity. It is **not** a story about a clumsy measurement disturbing the system (that is Heisenberg's heuristic microscope, and the disturbance version was formalized separately by Ozawa in 2003). The Robertson bound is a geometric fact about vectors in an inner-product space.

---

## 4. Worked examples

### Example 1 — Spin along $x$, the same object three ways

Take the Pauli operator $\hat S_x \propto \sigma_x = \left[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right]$ in the basis $\{|0\rangle, |1\rangle\}$ (spin up/down along $z$). It is Hermitian. Its eigenvalues are $\pm 1$ (solve $\det(\sigma_x - \lambda I)=\lambda^2-1=0$), with eigenstates $|\pm\rangle = (|0\rangle \pm |1\rangle)/\sqrt 2$ — real, as required, and orthogonal: $\langle +|-\rangle = \frac12(1 - 1) = 0$. Prepare the state $|0\rangle$. The probability of measuring $+1$ is $|\langle + | 0\rangle|^2 = |1/\sqrt2|^2 = 1/2$, and likewise for $-1$. The expectation value is $\langle 0|\sigma_x|0\rangle = 0$: averaged over many runs the result is zero, even though no single run ever yields zero. The same calculation in three notations — abstract bracket $\langle 0|\hat S_x|0\rangle$, matrix product $(1\ 0)\sigma_x(1\ 0)^T$, and a position-style integral if these were wavefunctions — gives the same number; learning to translate among them fluently is the practical skill the chapter trains.

### Example 2 — Why the $-i$ in $\hat p$ is load-bearing

The momentum operator is $\hat p = -i\hbar\,\partial_x$. The factor of $-i$ is exactly what makes it Hermitian on the $L^2$ inner product $\langle\phi|\psi\rangle = \int_{-\infty}^{\infty}\phi^*\psi\,dx$. Check by integration by parts:

$$
\langle \phi | \hat p\,\psi\rangle = \int \phi^* (-i\hbar)\,\partial_x\psi\,dx
= \underbrace{[-i\hbar\,\phi^*\psi]_{-\infty}^{\infty}}_{=\,0} + \int (-i\hbar\,\partial_x\phi)^* \psi\,dx
= \langle \hat p\,\phi | \psi\rangle,
$$

where the boundary term vanishes because square-integrable states decay at infinity. The conjugation $(-i)^* = +i$ in moving the operator onto the bra flips the sign that integration by parts introduced, leaving $\hat p$ self-adjoint. A bare derivative $\partial_x$ alone is *anti*-Hermitian; the $-i$ rotates it into a genuine observable. (This is precisely where the half-line caveat bites: cut the domain to $[0,\infty)$ and the boundary term need not vanish, and $\hat p$ stops being self-adjoint.)

### Example 3 — The canonical commutator and $\sigma_x\sigma_p \geq \hbar/2$

Compute $[\hat x, \hat p]$ by letting it act on a test function $\psi(x)$:

$$
[\hat x, \hat p]\psi = x(-i\hbar\,\psi') - (-i\hbar)\,\partial_x(x\psi)
= -i\hbar x\psi' + i\hbar(\psi + x\psi') = i\hbar\,\psi.
$$

Since this holds for all $\psi$, $[\hat x,\hat p] = i\hbar$. Feed this into Robertson:

$$
\sigma_x\,\sigma_p \geq \tfrac12|\langle[\hat x,\hat p]\rangle| = \tfrac12|i\hbar| = \frac{\hbar}{2}.
$$

The Heisenberg relation $\sigma_x\sigma_p \geq \hbar/2$ is not a separate postulate — it is Robertson's theorem evaluated on the canonical commutator. It says no state can be sharply localized in both position and momentum at once; the Gaussian wave packet of Chapter 6 saturates it.

---

## 5. Return to the cold open

Why must a measured energy be real, and why does measuring an eigenstate give the same answer with certainty? Both follow from the two-line theorem. The energy observable is the Hamiltonian $\hat H$, taken Hermitian. Therefore (real-eigenvalue theorem) every possible measured energy $E_n$ — every eigenvalue of $\hat H$ — is a real number; that is why no apparatus has ever read off a complex energy. And if the system is *in* an eigenstate $|E_n\rangle$, then expanding it in the energy eigenbasis gives a single nonzero coefficient, so the Born probability of outcome $E_n$ is $|\langle E_n|E_n\rangle|^2 = 1$: the result is certain, and repeats. Distinct energy levels give orthogonal states (orthogonality theorem), so the levels are perfectly distinguishable — exactly the discrete, reproducible spectrum the cold open described. The physics postulate "observables are Hermitian" is doing the work of guaranteeing real, reproducible, distinguishable outcomes, and the guarantee is a theorem, not a hope.

The framework also tells you what *can* be measured together. Energy and angular momentum can be simultaneously definite in hydrogen precisely because $[\hat H, \hat L^2] = [\hat H, \hat L_z] = 0$ — commuting Hermitian operators share an eigenbasis, the foundation of the quantum numbers $(n, \ell, m)$ we will derive in Chapter 7.

---

## 6. Where it generalizes

- **Unitary time evolution.** Conservation of probability, $\langle\psi(t)|\psi(t)\rangle = 1$ for all $t$, forces the evolution operator $\hat U(t) = e^{-i\hat H t/\hbar}$ to be unitary — and $\hat U$ is built from the Hermitian $\hat H$ exactly so that it is. Spin precession and qubit gates are unitary $2\times2$ operators.
- **Compatible observables.** $[\hat A,\hat B]=0 \iff$ simultaneous eigenbasis $\iff$ both sharp at once. Complete sets of commuting observables (e.g. $\{\hat H, \hat L^2, \hat L_z\}$) label states uniquely.
- **The infinite-dimensional sequel.** Promote the index $n$ to a continuous label and the sum $\sum_n |n\rangle\langle n|$ becomes an integral $\int |x\rangle\langle x|\,dx = \hat I$, with $\langle x|x'\rangle = \delta(x-x')$. The Dirac delta and continuous bases — gestured at here — are developed properly in Chapter 6, where the change of basis $\langle x|p\rangle$ turns out to be the Fourier transform.
- **Sturm–Liouville theory.** When the operator is a differential operator and the vectors are functions, "Hermitian operator with real eigenvalues and orthogonal eigenfunctions" becomes the statement that Legendre, Hermite, and Bessel functions form orthogonal complete bases (Chapter 7). The two-line theorem of this chapter is the engine of all of it.

A solver computes adjoints, checks Hermiticity, and diagonalizes. It does not know that the $-i$ in $\hat p$ is what makes momentum measurable, that a complex expectation value means you dropped a dagger, that the Robertson bound is about state preparation rather than clumsy measurement, or that $[\hat A,\hat B]=0$ is *why* two quantities can be simultaneously definite. Those reflexes are what turn formal symbol-pushing into understanding.

---

## Exercises

1. **(Adjoints.)** For operators $\hat A, \hat B$ and scalar $c$, prove $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger$ and $(c\hat A)^\dagger = c^*\hat A^\dagger$ directly from the defining relation $\langle\phi|\hat A\psi\rangle = \langle\hat A^\dagger\phi|\psi\rangle$. Deduce that $\hat A\hat A^\dagger$ and $\hat A + \hat A^\dagger$ are Hermitian for any $\hat A$.

2. **(Derivation — required.)** Prove that a Hermitian operator has real eigenvalues, and that eigenvectors belonging to distinct eigenvalues are orthogonal. State precisely where each step uses $\hat A^\dagger = \hat A$.

3. **(Hermitian ≠ symmetric.)** Show $\sigma_y = \left[\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\right]$ is Hermitian but not symmetric, find its eigenvalues and eigenvectors, and verify the eigenvectors are orthogonal. Explain why, over $\mathbb{C}$, the relevant condition for a real spectrum is Hermiticity, not symmetry.

4. **(Commutators and compatibility.)** Compute $[\hat x, \hat p^2]$ using $[\hat x,\hat p]=i\hbar$ and the identity $[\hat A,\hat B\hat C]=[\hat A,\hat B]\hat C+\hat B[\hat A,\hat C]$. What does a nonzero result say about measuring position and kinetic energy simultaneously?

5. **(Unitarity preserves probability.)** Show that if $\hat U$ is unitary then $\|\hat U\psi\| = \|\psi\|$ for every state. Then show that $\hat U = e^{-i\hat H t/\hbar}$ is unitary whenever $\hat H$ is Hermitian, and explain why this is exactly the requirement that total probability be conserved in time.

---

## Sources

- Dirac, P. A. M. "A new notation for quantum mechanics." *Mathematical Proceedings of the Cambridge Philosophical Society* **35**, 416–418 (1939). DOI 10.1017/S0305004100021162. [Origin of bra–ket notation; the notation became standard with the 3rd edition (1947) of *Principles*.]
- Dirac, P. A. M. *The Principles of Quantum Mechanics* (Oxford, 1st ed. 1930; 3rd ed. 1947). [State vectors, observables as operators, the spectral picture.]
- von Neumann, J. *Mathematische Grundlagen der Quantenmechanik* (Springer, 1932); English: *Mathematical Foundations of Quantum Mechanics* (Princeton, 1955). [The rigorous Hilbert-space, self-adjoint-operator formulation; criticized Dirac's delta as mathematically improper.]
- Robertson, H. P. "The Uncertainty Principle." *Physical Review* **34**, 163–164 (1929). [The state-based uncertainty relation $\sigma_A\sigma_B \geq \frac12|\langle[\hat A,\hat B]\rangle|$ from Cauchy–Schwarz.]
- Schmidt, E. Work on orthonormalization of function systems (1907), after Gram (1883). [The Gram–Schmidt procedure for orthonormal bases.]
- Hilbert, D., and collaborators. Integral-equation and inner-product-space theory (1904–1910). [Where Hilbert spaces and the spectral idea were forged, two decades before quantum mechanics. *verify specific venues.*] <!-- FACT-CHECK FLAG: UNVERIFIED — the 1904 "Grundzüge…" is confirmed (see Ch.4), but the full 1904–1910 span / specific venues are not individually confirmed. See factchecks/05-operators-inner-products-and-dirac-notation-assertions.md -->
- Reed, M., and B. Simon. *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975). [The honest account of Hermitian vs. self-adjoint in infinite dimensions: domains, boundary terms, deficiency indices.]
- Ozawa, M. "Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement." *Physical Review A* **67**, 042105 (2003). [The separate measurement-disturbance relation, distinct from the Robertson state bound.]
- Singh, C., and E. Marshman. "Investigating student difficulties with Dirac notation." arXiv:1510.01296 (2015); and related PER (arXiv:1509.04084, 1701.01409, 1701.01411). [Documents the translation, conjugation, and expectation-value difficulties this chapter is designed around.]
- Stanford Encyclopedia of Philosophy, "Quantum Theory: von Neumann vs. Dirac." [On the productive tension between usable formalism and full rigor.]
