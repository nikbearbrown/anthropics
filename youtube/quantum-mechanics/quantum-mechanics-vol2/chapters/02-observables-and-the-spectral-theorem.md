# Chapter 2 — Observables, Hermiticity, and the Spectral Theorem
*How the requirement that measurements return real numbers forces the entire structure of quantum observables.*

The momentum operator is $\hat{p} = -i\hbar\,\partial_x$. A student coming from wave mechanics, asked why the $i$ belongs there, will often answer that it simply works — it produces the right de Broglie relation, the right commutation relations, the right everything. That answer is true, and it is a fine empirical observation, but it does not explain anything.

Here is the explanation. Without the $i$, the operator $\hat{p}$ would fail to be Hermitian. And once $\hat{p}$ is not Hermitian, its eigenvalues turn imaginary, which would mean that a measurement of momentum returns a complex number. A ruler that reports a complex-valued length is not describing the physical world.

So the $i$ is a necessity, not a stylistic choice. And the principle that demands it — the requirement that any measured outcome be a real number — demands a great deal more than the form of $\hat{p}$ alone. It demands the whole apparatus of Hermitian operators, spectral decompositions, and projectors. In this chapter we build that apparatus starting from one physical requirement, and we see that the Born rule, the spectral theorem, and the structure of quantum measurement all grow out of it.

---

## Why Observables Must Be Hermitian

Let us begin with the smallest possible starting point. An observable is something we can measure, so its values must be real numbers. If $\hat{A}$ represents an observable, then for any state $|\psi\rangle$ the expectation value

$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle$$

has to be real. Not merely for a few special states — for every state we could possibly prepare.

Now take the complex conjugate of $\langle\hat{A}\rangle$. Using the definition of the adjoint, $\langle\phi|\hat{A}\psi\rangle^* = \langle\hat{A}^\dagger\phi|\psi\rangle$, with $|\phi\rangle = |\psi\rangle$, we find:

$$\langle\hat{A}\rangle^* = \langle\psi|\hat{A}|\psi\rangle^* = \langle\psi|\hat{A}^\dagger|\psi\rangle.$$

For $\langle\hat{A}\rangle$ to be real we need $\langle\hat{A}\rangle = \langle\hat{A}\rangle^*$, which gives

$$\langle\psi|\hat{A}|\psi\rangle = \langle\psi|\hat{A}^\dagger|\psi\rangle \quad \text{for all }|\psi\rangle.$$

By the polarization identity — a standard fact from linear algebra — a sesquilinear form that vanishes on the diagonal vanishes everywhere. So the condition above forces $\hat{A} = \hat{A}^\dagger$: the operator is **Hermitian**, also called self-adjoint.

Notice that this is not a postulate handed down by authority. It is a short three-line argument: measurements return real numbers; real expectation values require $\hat{A} = \hat{A}^\dagger$; therefore every observable is Hermitian. The framework is something the physics requires of us, not something we impose on the physics.

The momentum operator makes the point concrete. With $\hat{p} = -i\hbar\,\partial_x$:

$$\langle\phi|\hat{p}\psi\rangle = \int_{-\infty}^\infty\phi^*(x)(-i\hbar)\partial_x\psi(x)\,dx.$$

Integrate by parts; the boundary term vanishes for normalizable states:

$$= \int_{-\infty}^\infty(i\hbar\partial_x\phi^*)\psi\,dx = \int_{-\infty}^\infty(-i\hbar\partial_x\phi)^*\psi\,dx = \langle\hat{p}\phi|\psi\rangle.$$

So $\hat{p}^\dagger = \hat{p}$. Suppose instead we had tried $\hat{p}' = \hbar\partial_x$, with no $i$. The same integration by parts produces $\langle\hat{p}'\phi|\psi\rangle = -\langle\hat{p}'\phi|\psi\rangle$ — anti-Hermitian, with purely imaginary eigenvalues. Momentum is not imaginary, so the $i$ is carrying real weight.

In matrix language, the Hermitian condition $\hat{A} = \hat{A}^\dagger$ reads $A_{mn} = A_{nm}^*$: the matrix equals its own conjugate transpose. The diagonal entries must then be real, since $A_{nn} = A_{nn}^*$, and the off-diagonal entries come in conjugate pairs. A matrix can hold complex entries and still be Hermitian, as long as that pattern is honored. The Pauli matrix $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$ is the example to keep in mind: its entries are complex, yet $(\sigma_y)_{12} = -i = (i)^* = (\sigma_y)_{21}^*$, so it is Hermitian. The right diagnostic question is never "are the entries real?" but rather "does $A_{mn} = A_{nm}^*$ hold?"

![Two 3×3 matrix grids side by side: diagonal cells in orange, off-diagonal conjugate pairs color-matched across the two grids, with an equals sign indicating the Hermitian condition A = A†](../images/02-observables-and-the-spectral-theorem-fig-03.png)
*Figure 2.3 — The Hermitian condition in matrix form: diagonal entries are real (self-conjugate) and off-diagonal entries come in conjugate pairs mirrored across the diagonal.*

<!-- → [TABLE: summary of Hermitian vs. anti-Hermitian vs. unitary — showing the defining condition, the constraint on diagonal entries, the constraint on eigenvalues, and a $2\times 2$ example for each; this makes the distinctions among the three operator types visually immediate] -->

---

## Eigenvalues Are Real

**Theorem.** If $\hat{A}$ is Hermitian and $\hat{A}|a\rangle = a|a\rangle$, then $a\in\mathbb{R}$.

**Proof.** We compute $\langle a|\hat{A}|a\rangle$ in two different ways.

First, let $\hat{A}$ act on the ket: $\langle a|\hat{A}|a\rangle = a\langle a|a\rangle = a$.

Second, let $\hat{A}$ act on the bra, using Hermiticity. Since $\hat{A}|a\rangle = a|a\rangle$, taking the bra of both sides gives $\langle a|\hat{A} = a^*\langle a|$. Therefore $\langle a|\hat{A}|a\rangle = a^*\langle a|a\rangle = a^*$.

Setting the two equal: $a = a^*$, so $a\in\mathbb{R}$. $\square$

The proof runs four lines, and its structure is worth committing to memory: evaluate the same sandwich $\langle a|\hat{A}|a\rangle$ once by acting on the ket and once by acting on the bra; Hermiticity makes the bra-side calculation produce the conjugate; equating the two forces the eigenvalue to equal its own conjugate.

It is instructive to see what breaks without Hermiticity. In the second step, the bra of $\hat{A}|a\rangle = a|a\rangle$ would give $\langle a|\hat{A}^\dagger = \bar{a}^*\langle a|$, where $\bar{a}$ is the eigenvalue of $\hat{A}^\dagger$ — in general not equal to $a$. The two computations of the sandwich then disagree, and no conclusion follows. The matrix $\bigl(\begin{smallmatrix}0&i\\i&0\end{smallmatrix}\bigr)$ is not Hermitian (check: $(A)_{12} = i$ but $A_{21}^* = i^* = -i \neq i$), and its eigenvalues are $\pm i$ — purely imaginary, exactly as the theorem predicts they may be once Hermiticity is gone.

![Two panels: left shows three eigenvalue markers on a real number line (Hermitian case); right shows three markers scattered in the complex plane with nonzero imaginary parts (non-Hermitian case)](../images/02-observables-and-the-spectral-theorem-fig-04.png)
*Figure 2.4 — Hermitian operators have all eigenvalues on the real line (left); non-Hermitian operators can have eigenvalues anywhere in the complex plane (right).*

---

## Eigenstates Are Orthogonal

**Theorem.** If $\hat{A}$ is Hermitian with eigenstates $\hat{A}|a\rangle = a|a\rangle$ and $\hat{A}|a'\rangle = a'|a'\rangle$, and $a \neq a'$, then $\langle a|a'\rangle = 0$.

**Proof.** We compute $\langle a|\hat{A}|a'\rangle$ in two ways.

First: $\langle a|\hat{A}|a'\rangle = a'\langle a|a'\rangle$.

Second: since $a$ is real (just established), $\langle a|\hat{A} = a\langle a|$, so $\langle a|\hat{A}|a'\rangle = a\langle a|a'\rangle$.

Setting them equal: $(a' - a)\langle a|a'\rangle = 0$. Since $a' \neq a$, we conclude $\langle a|a'\rangle = 0$. $\square$

This proof relies on $a$ being real, so the two theorems are linked in a chain. Without the first, the second step cannot proceed: $\langle a|\hat{A} = a\langle a|$ requires $a = a^*$, which is precisely what the first theorem gives us.

**Degeneracy breaks the argument.** When $a = a'$, the factor $(a' - a) = 0$ and the equation $(0)\langle a|a'\rangle = 0$ tells us nothing at all. Two linearly independent eigenstates that share an eigenvalue need not be orthogonal. The identity operator $\hat{I}$ shows this at once: every vector is an eigenvector with eigenvalue 1, and arbitrary vectors are generally not orthogonal.

The cure is Gram-Schmidt orthogonalization: within the degenerate subspace, build an orthonormal basis by the standard procedure. The spectral theorem assures us this can always be done — a degenerate subspace always has a complete orthonormal eigenbasis, though not a unique one. The freedom in choosing a basis inside the subspace is a genuine extra degree of freedom, and in practice we pin it down by finding a second observable that commutes with $\hat{A}$ and tells the degenerate states apart.

Degeneracy is never an accident. It is always the fingerprint of a symmetry: some transformation that leaves the Hamiltonian alone while mixing the degenerate states among themselves. The hydrogen atom's energy levels are degenerate in $\ell$ and $m_\ell$ because the Hamiltonian commutes with the angular momentum operators — that is, because of rotational symmetry. The additional quantum numbers labeling the degenerate states are the eigenvalues of those symmetry generators. We will meet this same pattern again and again throughout the course.

---

## The Spectral Theorem

Putting together real eigenvalues, orthogonal eigenstates, and the completeness of the eigenbasis, we arrive at the central result:

> Every Hermitian operator $\hat{A}$ can be written in its **spectral decomposition**:
$$\hat{A} = \sum_n a_n\,|a_n\rangle\langle a_n|.$$

Each term $\hat{P}_n = |a_n\rangle\langle a_n|$ is a **projector** onto the $n$-th eigenspace. These projectors obey four properties, all of which follow straight from the orthonormality of the eigenstates:

$$\hat{P}_n^2 = \hat{P}_n \qquad \text{(idempotent: projecting twice is the same as once)}$$
$$\hat{P}_n^\dagger = \hat{P}_n \qquad \text{(Hermitian: projectors are themselves observables)}$$
$$\sum_n\hat{P}_n = \hat{I} \qquad \text{(completeness: the projectors partition the identity)}$$
$$\hat{P}_m\hat{P}_n = \delta_{mn}\hat{P}_n \qquad \text{(orthogonality: projectors onto different eigenspaces commute to zero)}$$

The spectral decomposition is the operator version of writing a vector in its own eigenbasis: in that basis the operator becomes diagonal, with eigenvalues $a_n$ along the diagonal. What the decomposition says, in words, is that $\hat{A}$ acts on any state by projecting it onto each eigenspace and then scaling that piece by the matching eigenvalue.

For a degenerate eigenvalue $a_n$ with multiplicity $d > 1$, the projector is $\hat{P}_n = \sum_{k=1}^d|a_n,k\rangle\langle a_n,k|$ — a sum over the orthonormal basis we chose for the degenerate subspace. The spectral decomposition still holds; the projector simply has rank $d > 1$.

<!-- → [FIGURE: geometric diagram in a 2D Hilbert space — showing a state vector |ψ⟩, the two eigenstates |a₁⟩ and |a₂⟩ as an orthonormal basis, and the projections P̂₁|ψ⟩ and P̂₂|ψ⟩ as components; the goal is to make the Born rule visually obvious as "squared length of the projection"] -->

![geometric diagram in a 2D Hilbert space — showing a state vector |ψ⟩, the two eigenstates |a₁⟩ and |a₂⟩ as an orthonormal basis, and the…](../images/02-observables-and-the-spectral-theorem-fig-01.png)
*Figure 2.1 — geometric diagram in a 2D Hilbert space — showing a state vector |ψ⟩, the two eigenstates |a₁⟩ and |a₂⟩ as an orthonormal basis, and the…*

With the spectral decomposition in hand, we can also define functions of operators directly:

$$f(\hat{A}) = \sum_n f(a_n)\,|a_n\rangle\langle a_n|.$$

The time-evolution operator $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ is built in exactly this way:

$$\hat{U}(t) = \sum_n e^{-iE_n t/\hbar}|E_n\rangle\langle E_n|.$$

Any initial state decomposes into energy eigenstates, and each one rotates at its own frequency $E_n/\hbar$. The full time evolution is a superposition of these rotations. We do not have to assume this — it follows from the spectral theorem applied to $\hat{H}$, which is Hermitian.

---

## The Born Rule as Geometry

The spectral decomposition turns the Born rule into a statement about geometry. Expand any state in the eigenbasis of $\hat{A}$:

$$|\psi\rangle = \sum_n c_n|a_n\rangle, \qquad c_n = \langle a_n|\psi\rangle.$$

The probability of obtaining the outcome $a_n$ is

$$P(a_n) = |\langle a_n|\psi\rangle|^2 = |c_n|^2 = \langle\psi|\hat{P}_n|\psi\rangle = \|\hat{P}_n|\psi\rangle\|^2.$$

This is the squared length of the projection of $|\psi\rangle$ onto the eigenspace of $a_n$. Probability is not a separate postulate bolted onto the formalism — it is the squared norm of a component, a geometric quantity that already lives in the structure of the Hilbert space.

The expectation value follows right away:

$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle = \langle\psi|\left(\sum_n a_n\hat{P}_n\right)|\psi\rangle = \sum_n a_n|c_n|^2 = \sum_n a_n P(a_n).$$

The expectation value is the probability-weighted average of the eigenvalues — which is precisely the definition of expected value from ordinary probability theory. The spectral theorem makes that connection exact and derivable rather than merely suggestive.

One distinction deserves to be stated twice. The quantity $\langle a_n|\psi\rangle = c_n$ is a complex amplitude. The probability is $|c_n|^2$, its squared modulus. The two differ by the act of taking the modulus squared, which discards the phase $e^{i\theta_n}$. That phase disappears when we compute a single measurement probability, but it returns in interference terms whenever two amplitudes feed the same outcome. Writing "the probability is $\langle a_n|\psi\rangle$" and ending up with a complex number is the single most common error in quantum mechanics, because it confuses two genuinely different objects: an amplitude (complex, living in the Hilbert space) and a probability (real, non-negative, a frequency of outcomes).

![State vector inside a unit circle, projected onto two orthogonal eigenstate axes with dashed perpendicular lines; probability squares beside each axis are proportional to the squared projection lengths](../images/02-observables-and-the-spectral-theorem-fig-02.png)
*Figure 2.2 — The Born rule as geometry: the probability of each measurement outcome equals the squared length of the state vector's projection onto the corresponding eigenstate direction.*

<!-- → [INFOGRAPHIC: "amplitude vs. probability" — showing the same state decomposed in two different bases; in each case, the amplitude c_n is a complex vector, the probability |c_n|² is its squared length; the diagram should make clear that the phase θ_n disappears in |c_n|² but survives if you add two amplitudes before squaring] -->

---

## A Worked Example: Diagonalizing a $2\times 2$ Observable

Consider the operator

$$\hat{B} = \begin{pmatrix}2 & 1+i \\ 1-i & 0\end{pmatrix}.$$

We will work through it step by step, and each step illustrates one of the ideas above.

**Hermiticity check.** Is $B_{12} = B_{21}^*$? We have $B_{12} = 1+i$ and $B_{21} = 1-i = (1+i)^* = B_{12}^*$. Good. The diagonal entries are 2 and 0, both real. Good. So $\hat{B}$ is Hermitian.

**Eigenvalues.** The secular equation $\det(\hat{B} - \lambda\hat{I}) = 0$ reads:

$$-\lambda(2-\lambda) - (1+i)(1-i) = 0.$$

Noting $(1+i)(1-i) = |1+i|^2 = 2$:

$$\lambda^2 - 2\lambda - 2 = 0 \implies \lambda = 1 \pm\sqrt{3}.$$

Both real, as the theorem requires. Sum check: $\lambda_+ + \lambda_- = 2 = \text{Tr}(\hat{B})$. Product check: $\lambda_+\lambda_- = 1-3 = -2 = \det(\hat{B})$. Both pass.

**Eigenvectors.** For $\lambda_+= 1+\sqrt{3}$, substitute into $(\hat{B} - \lambda_+\hat{I})|b_+\rangle = 0$. The first row gives $(1-\sqrt{3})x + (1+i)y = 0$, so $x = \frac{1+i}{\sqrt{3}-1}y$. Rationalizing: $x = \frac{(1+i)(\sqrt{3}+1)}{2}y$. Normalize using $|x|^2 + |y|^2 = 1$; since $|1+i|^2 = 2$ and $(\sqrt{3}+1)^2 = 4 + 2\sqrt{3}$, one finds $|y|^2 = 1/(3+\sqrt{3})$.

A tempting shortcut to avoid: trying to read the eigenvectors directly off the matrix without solving the system. That only works for matrices that are already diagonal. For any non-diagonal $\hat{B}$, we have to substitute the eigenvalue and solve the homogeneous system.

For $\lambda_-$, the same procedure yields $|b_-\rangle$ orthogonal to $|b_+\rangle$ — which you can confirm by computing $\langle b_+|b_-\rangle = 0$.

**Spectral decomposition.**

$$\hat{B} = \lambda_+|b_+\rangle\langle b_+| + \lambda_-|b_-\rangle\langle b_-|.$$

To verify: $\hat{B}|b_+\rangle = \lambda_+|b_+\rangle$ and $\hat{B}|b_-\rangle = \lambda_-|b_-\rangle$ by construction. Cross-check: $\lambda_+|b_+\rangle\langle b_+|b_+\rangle + \lambda_-|b_-\rangle\langle b_-|b_+\rangle = \lambda_+|b_+\rangle$. The completeness check: $|b_+\rangle\langle b_+| + |b_-\rangle\langle b_-| = \hat{I}$.

**Born rule.** For $|\psi\rangle = (|1\rangle + |2\rangle)/\sqrt{2}$ (using the original basis $\{|1\rangle, |2\rangle\}$):

$$\langle\hat{B}\rangle = \frac{1}{2}\bigl(\langle 1| + \langle 2|\bigr)\begin{pmatrix}2&1+i\\1-i&0\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix} = \frac{1}{2}\bigl((2+1+i)+(1-i+0)\bigr) = \frac{1}{2}(4) = 2.$$

This should equal $\lambda_+ P(\lambda_+) + \lambda_- P(\lambda_-)$, and indeed both computations give 2 — the spectral formula and the direct matrix calculation agree.

The lesson is that the spectral decomposition of $\hat{B}$ holds everything we could want to know about the observable: the possible outcomes $\lambda_\pm$, the states $|b_\pm\rangle$ that produce each outcome with certainty, and the probability of each outcome from any input state through the inner product. Diagonalizing $\hat{B}$ is just finding the basis in which the measurement becomes transparent.

A boundary on the method: for a $10\times 10$ Hermitian matrix, the secular equation is a degree-10 polynomial, which has no general closed-form solution. In practice we diagonalize numerically. The spectral theorem guarantees that eigenvalues exist, that they are real, and that the eigenvectors span the space — but it does not hand us a formula for them. Even so, that guarantee is enough to build the physics.

---

## What the Commutator Will Say

The spectral theorem settles the question of a single observable completely: which outcomes are possible, which states produce each one with certainty, how probabilities are computed. The next question concerns two observables: can we measure both at once and obtain definite values for each?

The answer hinges on whether the two operators commute. If $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A} = 0$, the operators share a common eigenbasis and simultaneous sharp values are possible. If $[\hat{A}, \hat{B}] \neq 0$, they share no basis and simultaneous sharp values are impossible — the uncertainty principle is the quantitative form of this impossibility, derived from the commutator algebra rather than from any story about a measurement disturbing the system. That is the subject of the next chapter, and it grows directly out of the spectral theorem we have developed here.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the Hermitian condition on* $2\times 2$ *matrices.*
   For each matrix below, determine whether it is Hermitian, anti-Hermitian ($\hat{A}^\dagger = -\hat{A}$), or neither. (a) $\bigl(\begin{smallmatrix}1&2i\\-2i&3\end{smallmatrix}\bigr)$, (b) $\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr)$, (c) $\bigl(\begin{smallmatrix}1&1+i\\1-i&-1\end{smallmatrix}\bigr)$. For each Hermitian case, verify that the diagonal entries are real. Correct a common error: explain why checking "symmetric" (i.e., $A_{mn} = A_{nm}$) rather than "conjugate-symmetric" ($A_{mn} = A_{nm}^*$) gives wrong answers for complex matrices.
   *Tests: ability to apply* $A_{mn} = A_{nm}^*$ *and distinguish from plain transpose symmetry.*

2. *Difficulty: Warm-up — tests the real-eigenvalue proof.*
   Prove in four lines: if $\hat{A}$ is Hermitian and $\hat{A}|a\rangle = a|a\rangle$, then $a\in\mathbb{R}$. Then exhibit a non-Hermitian $2\times 2$ matrix with a purely imaginary eigenvalue and identify exactly which step of the proof fails for it.
   *Tests: ability to reproduce and articulate the proof; locates the role of Hermiticity.*

3. *Difficulty: Warm-up — tests the amplitude-vs-probability distinction.*
   The state $|\psi\rangle = (3/5)|0\rangle + (4i/5)|1\rangle$ is measured in the $\sigma_z$ eigenbasis. (a) Compute the amplitudes $\langle 0|\psi\rangle$ and $\langle 1|\psi\rangle$. (b) Compute the probabilities $P(+1)$ and $P(-1)$ and verify they sum to 1. (c) Compute $\langle\sigma_z\rangle$ using the spectral sum $\sum_n a_n P(a_n)$ and verify by direct calculation $\langle\psi|\sigma_z|\psi\rangle$.
   *Tests: whether the student correctly squares the modulus rather than the amplitude; applies the spectral expectation formula.*

**Application**

4. *Difficulty: Application — full diagonalization.*
   Diagonalize $\hat{A} = \bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$. (a) Find eigenvalues from the secular equation $\lambda^2 - \text{Tr}(\hat{A})\lambda + \det(\hat{A}) = 0$. (b) Find and normalize the eigenvectors. (c) Write the spectral decomposition $\hat{A} = \lambda_1|a_1\rangle\langle a_1| + \lambda_2|a_2\rangle\langle a_2|$ and verify by expanding the outer products. (d) Verify $\hat{P}_1^2 = \hat{P}_1$ and $\hat{P}_1\hat{P}_2 = 0$.
   *Tests: complete execution of the diagonalization procedure and the projector properties.*

5. *Difficulty: Application — phase parameter in a Hermitian observable.*
   The operator $\hat{M} = \bigl(\begin{smallmatrix}0&e^{i\phi}\\e^{-i\phi}&0\end{smallmatrix}\bigr)$ for real $\phi$. (a) Verify Hermiticity. (b) Find the eigenvalues — they should be independent of $\phi$. (c) Find the eigenstates and show they depend on $\phi$. (d) Compute $\langle\hat{M}\rangle$ when the state is $|0\rangle$ and when it is $(|0\rangle + |1\rangle)/\sqrt{2}$. Explain physically why the eigenvalues are $\phi$-independent while the eigenstates are not.
   *Tests: diagonalization with a phase parameter; separates the role of eigenvalues from eigenstates.*

6. *Difficulty: Application — functions of operators via the spectral decomposition.*
   The Hamiltonian is $\hat{H} = E_0\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$. (a) Write the spectral decomposition of $\hat{H}$. (b) Use it to construct $e^{-i\hat{H}t/\hbar}$ explicitly as a $2\times 2$ matrix. (c) Evolve the initial state $|\psi(0)\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ to $|\psi(t)\rangle$. (d) Compute $\langle\hat{H}\rangle$ at time $t$ and verify it is constant.
   *Tests: construction of functions of operators via spectral decomposition; energy conservation.*

**Synthesis**

7. *Difficulty: Synthesis — degeneracy and Gram-Schmidt.*
   The observable
   $\hat{G} = \bigl(\begin{smallmatrix}2&0&0\\0&0&1\\0&1&0\end{smallmatrix}\bigr)$
   on a 3D Hilbert space. (a) Find all three eigenvalues. (b) Identify the degenerate eigenvalue and apply Gram-Schmidt to the degenerate subspace to produce two orthonormal eigenstates. (c) Write the full spectral decomposition, expressing the degenerate projector as a sum of two rank-1 outer products. (d) Compute $\langle\hat{G}\rangle$ for the state $|\psi\rangle = (|1\rangle + |2\rangle + |3\rangle)/\sqrt{3}$ by both the spectral sum $\sum_n a_n P(a_n)$ and the direct matrix product $\langle\psi|\hat{G}|\psi\rangle$.
   *Tests: handling the degenerate case; Gram-Schmidt within a subspace; spectral expectation in 3D.*

8. *Difficulty: Synthesis — projectors as observables.*
   Let $\hat{P} = |a\rangle\langle a|$ be a rank-1 projector. (a) Prove $\hat{P}^2 = \hat{P}$, $\hat{P}^\dagger = \hat{P}$, $\text{Tr}(\hat{P}) = 1$, and that the eigenvalues of $\hat{P}$ are 0 and 1. (b) Interpret each property physically: which says "projecting twice is the same as projecting once"? Which says "the projector is itself a Hermitian observable"? Which says "the projector has rank 1"? Which says "the measurement outcome is always 0 or 1"? (c) Explain why a projector valued observable corresponds to a yes/no measurement (does the system have property $a_n$?) and how $P(a_n) = \langle\psi|\hat{P}_n|\psi\rangle$ follows from treating $\hat{P}_n$ as an observable in the standard Born rule.
   *Tests: algebraic proof of projector properties, physical interpretation of each, and connection to the Born rule as a special case.*

**Challenge**

9. *Difficulty: Challenge — the polarization identity and its role in the Hermiticity argument.*
   The step "if $\langle\psi|(\hat{A} - \hat{A}^\dagger)|\psi\rangle = 0$ for all $|\psi\rangle$, then $\hat{A} = \hat{A}^\dagger$" is not obvious. Let $\hat{C} = \hat{A} - \hat{A}^\dagger$ and suppose $\langle\psi|\hat{C}|\psi\rangle = 0$ for all $|\psi\rangle$. (a) Use the substitution $|\psi\rangle = |\phi\rangle + |\chi\rangle$ to show $\langle\phi|\hat{C}|\chi\rangle + \langle\chi|\hat{C}|\phi\rangle = 0$. (b) Use $|\psi\rangle = |\phi\rangle + i|\chi\rangle$ to show $\langle\phi|\hat{C}|\chi\rangle - \langle\chi|\hat{C}|\phi\rangle = 0$. (c) Combining (a) and (b), show $\langle\phi|\hat{C}|\chi\rangle = 0$ for all $|\phi\rangle, |\chi\rangle$, and conclude $\hat{C} = 0$. This is the polarization identity. (d) Identify where in the argument you used the fact that the Hilbert space is over $\mathbb{C}$ rather than $\mathbb{R}$ — what goes wrong if the field is real?
   *Tests: ability to carry out the polarization identity argument; understands why complex scalars are essential to the conclusion.*

---

## References

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §§1.2–1.5.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. §§1.3–1.4.

Shankar, R. (1994). *Principles of Quantum Mechanics* (2nd ed.). Springer. §1.5.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §3.3.

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*, Vol. I. Wiley.

Reed, M., & Simon, B. (1972). *Methods of Modern Mathematical Physics*, Vol. I. Academic Press. (Rigorous treatment of self-adjoint operators and the spectral theorem in infinite dimensions.)

Marshman, E., & Singh, C. (2017). Investigating and improving student understanding of the probability distributions for measuring physical observables in quantum mechanics. *European Journal of Physics*, 38, 025705.

