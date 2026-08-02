# Module M-07 — Vectors, Vector Spaces, and Inner Products

**When you need this:** QM chapters II·1 (Hilbert-space formalism), IV·2 (entanglement and the Schmidt decomposition)

**Condensed from:** *Mathematics for Physics* Vol 1, Ch 4 (concrete 3D vectors) and Vol 2, Chs 4–5 (abstract spaces and inner products)

---

## From Arrows to Abstract Spaces

The Vol. 1 picture is concrete: a vector is a quantity with magnitude and direction, written in components relative to orthonormal unit vectors $\hat\imath, \hat\jmath, \hat k$:

$$\vec A = A_x\hat\imath + A_y\hat\jmath + A_z\hat k, \qquad |\vec A| = \sqrt{A_x^2 + A_y^2 + A_z^2}.$$

Vectors add component-by-component; the dot product gives a number measuring alignment:

$$\vec A\cdot\vec B = A_xB_x + A_yB_y + A_zB_z = |\vec A||\vec B|\cos\varphi.$$

The Vol. 2 picture abstracts this. A **vector space** $V$ over a field $\mathbb{F}$ ($\mathbb{R}$ or $\mathbb{C}$) is any set of objects that can be added and scaled, with the arithmetic obeying the standard rules: commutativity and associativity of addition, a zero vector, additive inverses, distributivity. The elements do not need to be arrows. Column vectors in $\mathbb{C}^n$ qualify. Polynomials qualify. Square-integrable functions on $\mathbb{R}$, with $(f+g)(x) = f(x)+g(x)$ and $(cf)(x) = c\,f(x)$, qualify — and this last example is where quantum mechanics lives.

![Three-panel figure: geometric arrow with component projections, column vector addition, and function addition](../images/07-vectors-vector-spaces-and-inner-products-fig-01.png)
*Figure 7.1 — Three realizations of the same abstract vector space: (left) a geometric arrow in ℝ² with dashed component projections; (middle) column vector addition shown as two stacks plus a sum stack; (right) two smooth functions and their pointwise sum — unified by the same addition and scaling axioms.*

---

## Linear Independence, Basis, Dimension

A set $\{\mathbf v_1,\ldots,\mathbf v_k\}$ is **linearly independent** if $c_1\mathbf v_1 + \cdots + c_k\mathbf v_k = \mathbf 0$ forces all $c_i = 0$. No vector in the set can be built from the others. A **basis** is a linearly independent set that also spans the space — every $\mathbf v \in V$ has a unique expansion $\mathbf v = \sum_i c_i\mathbf e_i$. The number of basis vectors is the **dimension** of $V$, independent of which basis is chosen.

Choosing a basis is choosing coordinates. The same abstract vector looks different in different bases; this is why the matrix representing a linear operator changes when we change basis, even though the operator itself does not.

---

## Inner Products: The Complex Case

An **inner product** on a complex vector space assigns to each ordered pair $(\phi, \psi)$ a complex number $\langle\phi|\psi\rangle$ satisfying three axioms. We use the **physicist's convention** throughout — conjugate-linear in the *first* argument:

1. **Conjugate symmetry:** $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$
2. **Linearity in the second argument:** $\langle\phi\,|\,a\psi_1 + b\psi_2\rangle = a\langle\phi|\psi_1\rangle + b\langle\phi|\psi_2\rangle$
3. **Positive-definiteness:** $\langle\psi|\psi\rangle \geq 0$, with equality only if $|\psi\rangle = 0$

The **norm** is $\|\psi\| = \sqrt{\langle\psi|\psi\rangle}$. Two vectors are **orthogonal** when $\langle\phi|\psi\rangle = 0$.

The two canonical examples:

**Finite-dimensional (**$\mathbb{C}^n$):
$$\langle\phi|\psi\rangle = \sum_{i=1}^n\phi_i^*\,\psi_i.$$
The conjugate is on the first entry. Without it, $\langle\psi|\psi\rangle = \sum\psi_i^2$ need not be real.

**Function space (**$L^2$):
$$\langle\phi|\psi\rangle = \int_{-\infty}^{\infty}\phi^*(x)\,\psi(x)\,dx.$$
This is the continuum analogue. The real 3D dot product is the special case $\mathbb{R}^3$ where no conjugate is needed.

---

## The Cauchy–Schwarz Inequality

For any two vectors in an inner-product space:

$$|\langle\phi|\psi\rangle|^2 \leq \langle\phi|\phi\rangle\,\langle\psi|\psi\rangle.$$

*Proof sketch.* Let $|\chi\rangle = |\phi\rangle - \frac{\langle\psi|\phi\rangle}{\langle\psi|\psi\rangle}|\psi\rangle$ — the part of $\phi$ remaining after subtracting its projection onto $\psi$. Positive-definiteness requires $\langle\chi|\chi\rangle \geq 0$; expanding and clearing denominators yields the inequality. $\blacksquare$

This inequality is the engine of the Robertson uncertainty relation (Module M-09).

---

## Orthonormal Bases and the Resolution of the Identity

A basis $\{|n\rangle\}$ is **orthonormal** if $\langle m|n\rangle = \delta_{mn}$. From any independent set, the **Gram–Schmidt** procedure builds an orthonormal one: take vectors in turn, subtract each one's projections onto the already-orthonormalized vectors, then normalize. In an orthonormal basis, expansion coefficients are just inner products: if $|\psi\rangle = \sum_n c_n|n\rangle$ then $c_n = \langle n|\psi\rangle$.

![Three-panel figure showing Gram-Schmidt steps from non-orthogonal pair to orthonormal pair](../images/07-vectors-vector-spaces-and-inner-products-fig-02.png)
*Figure 7.2 — Gram–Schmidt orthonormalization: (left) two non-orthonormal vectors at an acute angle; (middle) first vector normalized with unit-circle arc, projection dashed onto it, and residual arrow perpendicular to it; (right) completed orthonormal pair with right-angle square.*

Substituting back:

$$|\psi\rangle = \sum_n|n\rangle\langle n|\psi\rangle = \left(\sum_n|n\rangle\langle n|\right)|\psi\rangle.$$

Since this holds for every $|\psi\rangle$, the operator in parentheses must be the identity:

$$\boxed{\sum_n|n\rangle\langle n| = \hat I.}$$

This is the **resolution of the identity** — one of the most-used identities in quantum mechanics. Each term $|n\rangle\langle n|$ is the **projector** onto the $n$-th basis direction. The whole sum reconstructs the identity because the projectors tile the space without overlap. Inserting this form of $\hat I$ into any expression is the standard technique for changing basis, computing matrix elements, and deriving the Born rule.

![Vector diagram: two orthonormal basis arrows, state vector with dashed projections, component arrows, and parallelogram closure](../images/07-vectors-vector-spaces-and-inner-products-fig-03.png)
*Figure 7.3 — Resolution of the identity geometrically: a general state vector projected onto two orthonormal basis directions, the two component arrows reconstructing the original state via parallelogram addition.*

---

## Worked Example: Gram–Schmidt in $\mathbb{C}^2$

We start with $|\mathbf u_1\rangle = (1, i)^T$ and $|\mathbf u_2\rangle = (1, 0)^T$.

**Step 1.** Normalize $|\mathbf u_1\rangle$:

$$\langle\mathbf u_1|\mathbf u_1\rangle = 1^*\cdot1 + i^*\cdot i = 1 + (-i)(i) = 2, \qquad |e_1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}.$$

**Step 2.** Subtract the projection of $|\mathbf u_2\rangle$ onto $|e_1\rangle$:

$$\langle e_1|\mathbf u_2\rangle = \frac{1}{\sqrt{2}}(1^*\cdot1 + i^*\cdot0) = \frac{1}{\sqrt{2}}.$$

The residual:

$$|\mathbf u_2\rangle - \langle e_1|\mathbf u_2\rangle\,|e_1\rangle = \begin{pmatrix}1\\0\end{pmatrix} - \frac{1}{\sqrt{2}}\cdot\frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix} = \begin{pmatrix}1/2\\-i/2\end{pmatrix}.$$

Normalizing: $|e_2\rangle = \frac{1}{\sqrt{2}}(1, -i)^T$.

**Check:** $\langle e_1|e_2\rangle = \frac{1}{2}(1 + i^*\cdot(-i)) = \frac{1}{2}(1 + (-i)(-i)) = \frac{1}{2}(1-1) = 0$. Orthogonal. Note that the cross-term required the conjugate on the bra — without it the check gives $\frac{1}{2}(1+1) \neq 0$, a spurious failure.

---

## In the Quantum Series

### Hilbert Space Is an Infinite-Dimensional Inner-Product Space

The state space of quantum mechanics is $L^2(\mathbb{R})$ or a tensor product of copies of it — an **infinite-dimensional** complete inner-product space called a **Hilbert space**. States are unit vectors: $\langle\psi|\psi\rangle = 1$. Everything from this module carries over with one substitution: sums $\sum_n$ over discrete basis indices become integrals $\int dk$ for continuous bases. The resolution of the identity in the position basis reads

$$\int_{-\infty}^{\infty}|x\rangle\langle x|\,dx = \hat I, \qquad \langle x|x'\rangle = \delta(x-x'),$$

where the Kronecker delta has been replaced by the Dirac delta (Module M-06). The wavefunction is the component of the state in the continuous position basis: $\psi(x) = \langle x|\psi\rangle$.

### The Born Rule as a Projection

The expansion $|\psi\rangle = \sum_n c_n|a_n\rangle$ in an eigenbasis, with $c_n = \langle a_n|\psi\rangle$, is the resolution of the identity applied to a state. The Born rule says the probability of measuring eigenvalue $a_n$ is

$$P(a_n) = |c_n|^2 = |\langle a_n|\psi\rangle|^2.$$

This is the squared projection of the state onto the eigenstate — a geometric statement about inner-product spaces. Normalization ensures $\sum_n|c_n|^2 = 1$, which is the Pythagorean theorem in Hilbert space.

### Entanglement and the Tensor-Product Inner Product

For a two-particle system, the state space is the **tensor product** $\mathcal H_A \otimes \mathcal H_B$. If $\{|a_m\rangle\}$ and $\{|b_n\rangle\}$ are orthonormal bases for $\mathcal H_A$ and $\mathcal H_B$ respectively, then $\{|a_m\rangle\otimes|b_n\rangle\}$ is an orthonormal basis for $\mathcal H_A\otimes\mathcal H_B$, with inner product

$$\langle a_m\otimes b_n\,|\,a_{m'}\otimes b_{n'}\rangle = \langle a_m|a_{m'}\rangle\,\langle b_n|b_{n'}\rangle = \delta_{mm'}\delta_{nn'}.$$

A general state $|\Psi\rangle = \sum_{m,n}c_{mn}|a_m\rangle\otimes|b_n\rangle$ is **entangled** if it cannot be written as a single product $|\alpha\rangle\otimes|\beta\rangle$. The **Schmidt decomposition** — a singular-value decomposition applied to the coefficient matrix $c_{mn}$ — identifies this: a state is entangled if and only if its Schmidt rank exceeds one. The concepts of bases, orthonormality, and expansion coefficients are essential to give entanglement any mathematical content.

---

## Conventions and Pitfalls

**Physicist vs. mathematician convention.** Physicists put the conjugate on the *first* slot: $\langle\phi|\psi\rangle = \sum\phi_i^*\psi_i$. Mathematicians often put it on the second. The quantum series uses the physicist's convention exclusively.

**Forgetting the conjugate.** Writing $\langle a\phi|\psi\rangle = a\langle\phi|\psi\rangle$ instead of $a^*\langle\phi|\psi\rangle$ is the most common error. Scalars pulled out of the bra (first slot) get conjugated; pulled out of the ket, they are unchanged.

**Real vs. complex orthogonality.** For real vectors, $\langle\phi|\psi\rangle = 0$ corresponds to geometric perpendicularity. For complex vectors, it is an algebraic condition without a simple visual interpretation. We should not try to picture it as perpendicular arrows.

**Infinite dimension.** Finite-dimensional basis intuition generalizes, but completeness requires careful treatment of limits. $L^2(\mathbb{R})$ is complete; not every inner-product space is. The distinction matters when we want to guarantee that a Cauchy sequence of states converges to a state.

---

## Quick Practice

1. Let $|\phi\rangle = (1,i)^T/\sqrt{2}$ and $|\psi\rangle = (1,-i)^T/\sqrt{2}$ in $\mathbb{C}^2$. Compute $\langle\phi|\psi\rangle$ and $\langle\psi|\phi\rangle$. Verify $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$ and check that both vectors are normalized.

2. A normalized state $|\psi\rangle = \frac{3}{5}|0\rangle + \frac{4i}{5}|1\rangle$ in an orthonormal basis $\{|0\rangle,|1\rangle\}$. Use the resolution of the identity to find $\langle0|\psi\rangle$ and $\langle1|\psi\rangle$, then verify $|\langle0|\psi\rangle|^2 + |\langle1|\psi\rangle|^2 = 1$.

3. Show that $|\alpha\rangle = (1,0,i)^T/\sqrt{2}$ and $|\beta\rangle = (0,1,0)^T$ are orthonormal in $\mathbb{C}^3$. Find a third vector $|\gamma\rangle$ orthonormal to both. (*Hint: apply Gram–Schmidt to* $(i,0,1)^T$, *then normalize.*)

---

## Go Deeper

For the full development of concrete 3D vectors including the dot product derivation and cross product: **Vol. 1, Ch. 4**.

For abstract vector spaces, linear independence, basis, dimension, and the spectral theorem: **Vol. 2, Ch. 4**.

For inner-product axioms, Gram–Schmidt, the resolution of the identity, and Dirac notation in full: **Vol. 2, Ch. 5**.

For rigorous infinite-dimensional Hilbert spaces and completeness: von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1955); Reed and Simon, *Methods of Modern Mathematical Physics, Vol. I* (Academic Press, 1972).

---

## References

- Dirac, P.A.M. *The Principles of Quantum Mechanics*, 4th ed. Oxford University Press, 1958. [verify]
- von Neumann, J. *Mathematische Grundlagen der Quantenmechanik*. Springer, 1932. English translation: Princeton University Press, 1955. [verify]
- Hilbert, D. "Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen." *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, 1904. [verify]
- Wilson, E.B. *Vector Analysis*. Yale University Press, 1901. [verify]
