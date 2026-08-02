# Module M-08 — Eigenvalues and Diagonalization
*Why every measurement outcome in quantum mechanics is a real number — and why that is a theorem, not an assumption.*

The observable postulate of quantum mechanics states that physical measurement outcomes are real numbers. Most introductions declare this as a postulate, then separately state that observables are Hermitian operators. The second statement implies the first — real eigenvalues are a consequence of Hermiticity, and the proof fits in four lines. This module establishes that result as a derivation.

---

## The Eigenvalue Problem: Invariant Directions of a Linear Map

For a linear operator $A$ (a matrix, or an operator on a function space), an **eigenvector** is a nonzero vector that $A$ merely stretches — it does not change direction:

$$A\mathbf{v} = \lambda\mathbf{v}, \qquad \mathbf{v} \neq \mathbf{0}.$$

The scalar $\lambda$ is the corresponding **eigenvalue**. Most vectors get rotated when $A$ acts; eigenvectors are the invariant directions. The name comes from the German *eigen* ("own" or "characteristic"), introduced into the mathematical language by David Hilbert around 1904 in his work on integral equations. [verify: Hilbert 1904 Göttingen Nachrichten]

![Two-panel figure: general vectors rotated and stretched by an operator, versus eigenvectors scaled in place](../images/08-eigenvalues-and-diagonalization-fig-01.png)
*Figure 8.1 — Eigenvectors as invariant directions: (left) a fan of general vectors rotated and stretched by the operator; (right) two eigenvectors that are only scaled — their direction unchanged — with collinearity ticks and scale brackets.*

---

## The Characteristic Equation

Rearranging the eigenvalue equation:

$$A\mathbf{v} = \lambda\mathbf{v} \implies (A - \lambda I)\mathbf{v} = \mathbf{0}.$$

This is a homogeneous linear system. It always has the trivial solution $\mathbf{v} = \mathbf{0}$, which we exclude. A nonzero solution exists if and only if $A - \lambda I$ is singular — that is, it has a nontrivial nullspace — which happens precisely when its determinant vanishes:

$$\boxed{\det(A - \lambda I) = 0.}$$

This is the **characteristic equation**. Setting the determinant to zero is the literal condition for a nonzero eigenvector to exist: a nonzero vector in the nullspace of $A - \lambda I$ requires that matrix to be non-invertible, which requires its determinant to vanish. The same structure appears in degenerate perturbation theory, expressed as $\det(M - E^{(1)}I) = 0$ for the matrix of perturbation matrix elements.

Expanding the determinant gives the **characteristic polynomial** $p(\lambda) = \det(A - \lambda I)$, degree $n$ for an $n\times n$ matrix. Its $n$ roots (over $\mathbb{C}$, counted with multiplicity) are the eigenvalues. For each eigenvalue $\lambda_j$, solving $(A - \lambda_j I)\mathbf{v} = \mathbf{0}$ gives the eigenvector(s).

---

## Diagonalization

Suppose $A$ has $n$ linearly independent eigenvectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$ with eigenvalues $\lambda_1, \ldots, \lambda_n$. We stack the eigenvectors as columns of a matrix $P = [\mathbf{v}_1\;\cdots\;\mathbf{v}_n]$. Then $AP = PD$ where $D = \text{diag}(\lambda_1, \ldots, \lambda_n)$. Since the eigenvectors are independent, $P$ is invertible:

$$\boxed{A = PDP^{-1}, \qquad D = P^{-1}AP.}$$

The matrix $D$ is $A$ expressed in the eigenbasis — diagonal, with all couplings eliminated. Diagonalization is a change of coordinates that makes the action of $A$ maximally transparent: in the eigenbasis, $A$ multiplies each coordinate independently by the corresponding eigenvalue.

![Three-panel sequence: original oblique basis with full matrix, change-of-basis arc to eigenvectors, and diagonal matrix in eigenbasis](../images/08-eigenvalues-and-diagonalization-fig-02.png)
*Figure 8.2 — Diagonalization as coordinate change: (left) original basis with all four matrix cells filled; (middle) transformation arc to the eigenvector basis; (right) diagonal matrix with only the two diagonal cells filled, off-diagonal cells empty.* A **defective** matrix has fewer than $n$ independent eigenvectors; the simplest example is $\bigl[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr]$, which has only one eigenvector for its repeated eigenvalue $\lambda = 1$. Such matrices reduce only to Jordan form. In quantum mechanics, however, operators that arise as observables are guaranteed never to be defective — the spectral theorem below ensures it.

---

## The Spectral Theorem for Hermitian Matrices

A complex matrix is **Hermitian** if $A^\dagger = A$ (conjugate transpose equals itself). For real matrices the condition is symmetry, $A^T = A$; over $\mathbb{C}$ it must be $A^\dagger = A$. The $\sigma_y$ Pauli matrix is complex but Hermitian; it is not symmetric. Keeping the two conditions distinct is important for complex quantum mechanics.

**Theorem.** Every Hermitian matrix $A$ has: (i) all eigenvalues real; (ii) eigenvectors belonging to distinct eigenvalues are orthogonal (with respect to the inner product $\langle\mathbf{u}|\mathbf{v}\rangle = \mathbf{u}^\dagger\mathbf{v}$); (iii) a complete orthonormal eigenbasis exists — $A$ is diagonalizable by a unitary matrix $U$ ($U^\dagger = U^{-1}$): $A = UDU^\dagger$ with $D$ real diagonal.

**Proof of real eigenvalues.** Let $A\mathbf{v} = \lambda\mathbf{v}$, $\mathbf{v} \neq \mathbf{0}$. Multiplying on the left by $\mathbf{v}^\dagger$:

$$\mathbf{v}^\dagger A\mathbf{v} = \lambda\,\mathbf{v}^\dagger\mathbf{v} = \lambda\|\mathbf{v}\|^2.$$

The scalar $\mathbf{v}^\dagger A\mathbf{v}$ is its own complex conjugate: $(\mathbf{v}^\dagger A\mathbf{v})^* = \mathbf{v}^\dagger A^\dagger\mathbf{v} = \mathbf{v}^\dagger A\mathbf{v}$, using $A^\dagger = A$. A number equal to its own conjugate is real. Since $\|\mathbf{v}\|^2 > 0$, $\lambda = (\mathbf{v}^\dagger A\mathbf{v})/\|\mathbf{v}\|^2$ is real. $\square$

**Proof of orthogonal eigenvectors.** Take distinct real eigenvalues $\lambda_1 \neq \lambda_2$, with $A\mathbf{v}_1 = \lambda_1\mathbf{v}_1$ and $A\mathbf{v}_2 = \lambda_2\mathbf{v}_2$. We compute $\mathbf{v}_2^\dagger A\mathbf{v}_1$ two ways:

Acting right: $\mathbf{v}_2^\dagger A\mathbf{v}_1 = \lambda_1\,\mathbf{v}_2^\dagger\mathbf{v}_1$.

Acting left (using $A^\dagger = A$ to move $A$ onto the bra): $(A\mathbf{v}_2)^\dagger\mathbf{v}_1 = \lambda_2\,\mathbf{v}_2^\dagger\mathbf{v}_1$.

Subtracting: $(\lambda_1 - \lambda_2)\,\mathbf{v}_2^\dagger\mathbf{v}_1 = 0$. Since $\lambda_1 \neq \lambda_2$, we must have $\mathbf{v}_2^\dagger\mathbf{v}_1 = 0$. $\square$

When an eigenvalue is repeated (degenerate), Gram-Schmidt orthonormalizes the eigenspace internally. Degenerate eigenvalues always have full eigenspaces for Hermitian matrices — the algebraic and geometric multiplicities agree — which is why Hermitian matrices are never defective.

---

## The Spectral Decomposition

Once $A$ is diagonalized in an orthonormal eigenbasis $\{|\lambda_n\rangle\}$ with eigenvalues $\{\lambda_n\}$, the resolution of the identity gives the operator its transparent form:

$$A = UDU^\dagger = \sum_n \lambda_n\,|\lambda_n\rangle\langle\lambda_n|.$$

This is the **spectral decomposition**: the operator is the sum of each eigenvalue times the projector onto the corresponding eigenstate. It carries every fact about $A$ without coordinates.

![Single panel: full operator matrix equals sum of eigenvalue-scaled rank-1 projector matrices, with geometric lobe interpretation](../images/08-eigenvalues-and-diagonalization-fig-03.png)
*Figure 8.3 — Spectral decomposition: the full operator (left, all cells filled) equals eigenvalue-scale marker times first projector (one filled cell) plus eigenvalue-scale marker times second projector (other filled cell); geometrically, two perpendicular eigenvector arrows each with a projector lobe scaled by the corresponding eigenvalue.*

---

## Functions of Operators

The spectral decomposition makes it straightforward to apply any function to an operator: we apply the function to each eigenvalue separately.

$$f(A) = \sum_n f(\lambda_n)\,|\lambda_n\rangle\langle\lambda_n|.$$

The time-evolution operator in quantum mechanics is defined exactly this way:

$$\hat{U}(t) = e^{-i\hat{H}t/\hbar} = \sum_n e^{-iE_n t/\hbar}|E_n\rangle\langle E_n|.$$

Computing $e^{\hat{H}}$ by brute-force power series is laborious; in the eigenbasis it reduces to exponentiating each eigenvalue separately. The same works for $\sin(\hat{A})$, $\ln(\hat{A})$, or any analytic function: spectral decomposition reduces $f(A)$ to applying $f$ to a list of numbers. This is why energy eigenvalue problems are so central in quantum mechanics: knowing the eigenbasis of $\hat{H}$ is the prerequisite for computing the time evolution of any state.

---

## Simultaneous Diagonalization

Two Hermitian operators $\hat{A}$ and $\hat{B}$ share a common orthonormal eigenbasis if and only if they commute:

$$[\hat{A},\hat{B}] \equiv \hat{A}\hat{B} - \hat{B}\hat{A} = 0 \;\Longleftrightarrow\; \hat{A}\text{ and }\hat{B}\text{ are simultaneously diagonalizable.}$$

When they commute, each eigenvector of $\hat{A}$ is also an eigenvector of $\hat{B}$, and states can be labeled simultaneously by both eigenvalues. This is the mathematical basis of quantum numbers: the hydrogen atom's states can be labeled by $(n, \ell, m_\ell, m_s)$ because $\hat{H}$, $\hat{L}^2$, $\hat{L}_z$, and $\hat{S}_z$ all mutually commute.

---

## The Continuous Spectrum

The finite-dimensional spectral theorem assumes $n$ eigenvalues and $n$ eigenvectors. Quantum mechanics routinely involves operators whose spectrum is not discrete. The position operator $\hat{x}|x'\rangle = x'|x'\rangle$ and the momentum operator $\hat{p}|p\rangle = p|p\rangle$ have purely continuous spectra: every real number is an eigenvalue, and the corresponding "eigenstates" $|x'\rangle = \delta(x - x')$ and $|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$ are not square-integrable — they lie outside $L^2(\mathbb{R})$.

The correct framework is the **rigged Hilbert space**: a chain $\Phi\subset\mathcal{H}\subset\Phi^*$ where $\Phi$ is a space of well-behaved (rapidly decaying, smooth) functions, $\mathcal{H} = L^2$, and $\Phi^*$ is the space of continuous linear functionals on $\Phi$ (which includes the Dirac delta). Generalized eigenvectors live in $\Phi^*$, not in $\mathcal{H}$. The spectral theorem extends to this setting (the nuclear spectral theorem, due to Gelfand and collaborators in the 1950s), with the resolution of the identity becoming:

$$\hat{I} = \int_{-\infty}^\infty|x\rangle\langle x|\,dx, \qquad \langle x|x'\rangle = \delta(x-x').$$

In practice, whenever we write $\int|x\rangle\langle x|\,dx = \hat{I}$ or $\langle p|p'\rangle = \delta(p-p')$, we are using the generalized spectral theorem. The Dirac delta replaces the Kronecker delta; probability becomes probability density; no individual eigenstate is normalizable, but superpositions (wave packets) are.

---

## Worked Example: Diagonalizing $\sigma_y$

Let $\sigma_y = \bigl[\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr]$. First we check Hermiticity: $(\sigma_y^\dagger)_{ij} = (\sigma_y^*)_{ji}$, so $(\sigma_y^\dagger)_{12} = (\sigma_y^*)_{21} = (i)^* = -i = (\sigma_y)_{12}$. Hermitian.

**Characteristic equation:**

$$\det(\sigma_y - \lambda I) = \det\begin{pmatrix}-\lambda & -i \\ i & -\lambda\end{pmatrix} = \lambda^2 - (-i)(i) = \lambda^2 - 1 = 0 \implies \lambda = \pm1.$$

Real eigenvalues despite complex entries — the spectral theorem applied.

**Eigenvectors.** For $\lambda = +1$: from $(\sigma_y - I)\mathbf{v} = 0$, the first row gives $-v_1 - iv_2 = 0$, so $v_1 = -iv_2$. Taking $v_2 = 1$ and normalizing:

$$|\lambda = +1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}-i\\1\end{pmatrix}.$$

For $\lambda = -1$: similarly, $v_1 = iv_2$:

$$|\lambda = -1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}i\\1\end{pmatrix}.$$

**Orthogonality check.** Using the complex inner product (conjugate on the first factor):

$$\langle\lambda{=}{-1}|\lambda{=}{+1}\rangle = \frac{1}{2}\bigl[(i)^*(-i) + (1)^*(1)\bigr] = \frac{1}{2}\bigl[(-i)(-i) + 1\bigr] = \frac{1}{2}[-1+1] = 0. \checkmark$$

These are the $\text{spin-}\frac{1}{2}$ eigenstates along the $\pm y$ direction. The physical content: a particle whose spin is measured along $y$ will return $+\hbar/2$ in the state $|\lambda = +1\rangle$ and $-\hbar/2$ in the state $|\lambda = -1\rangle$, with certainty.

**Spectral decomposition.** $\sigma_y = (+1)|\lambda{=}+1\rangle\langle\lambda{=}+1| + (-1)|\lambda{=}-1\rangle\langle\lambda{=}-1|$. One verifies this reconstructs $\bigl[\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr]$ by expanding the outer products.

---

## Where This Appears in the Quantum Series

**QM II·2 — Observables and the spectral decomposition.** Every observable is a Hermitian operator. The spectral theorem guarantees real eigenvalues (measurement outcomes are real), orthogonal eigenstates (distinct outcomes are distinguishable), and completeness (the Born rule can assign probabilities to all outcomes). These are not postulates — they follow from Hermiticity.

**QM III·2 — Degenerate perturbation theory.** Fine structure in hydrogen lifts the degeneracy within levels of fixed $n$. The method: restrict the perturbation $H' = H_\text{SO} + H_\text{rel}$ to the degenerate subspace, build the matrix $M_{ij} = \langle n,i\,|H'|\,n,j\rangle$, and diagonalize. The first-order energy corrections are the eigenvalues of $M$; the "good states" (the ones that diagonalize $H'$) are the eigenvectors. This is the $2\times2$ or $4\times4$ Hermitian diagonalization of this module applied to a subspace.

**QM IV·6 — Density matrices and open systems.** The density matrix $\hat\rho$ is Hermitian, positive-semidefinite (all eigenvalues $\geq 0$), and $\text{Tr}\hat\rho = 1$. Diagonalizing it:

$$\hat\rho = \sum_n p_n|\psi_n\rangle\langle\psi_n|, \qquad p_n \geq 0, \quad \sum_n p_n = 1.$$

The eigenvalues $p_n$ are the classical probabilities of the pure states $|\psi_n\rangle$ in the ensemble.

---

## Quick Practice

1. Find the eigenvalues and orthonormal eigenvectors of $A = \bigl[\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\bigr]$. Write the spectral decomposition $A = \sum_n\lambda_n|\lambda_n\rangle\langle\lambda_n|$ and verify by multiplying out.

2. Using the spectral decomposition from Exercise 1, compute $e^A$ and $e^{iA}$ via the formula $f(A) = \sum f(\lambda_n)|\lambda_n\rangle\langle\lambda_n|$. Check that $e^{iA}$ is unitary ($U^\dagger U = I$).

3. For $\hat{A} = \sigma_z = \bigl[\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr]$ and $\hat{B} = \sigma_x = \bigl[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr]$, compute $[\hat{A},\hat{B}]$. Do they share an eigenbasis? Find the eigenbases of each and exhibit a state that is an eigenstate of $\hat{A}$ but not of $\hat{B}$.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the characteristic equation.*
   For the matrix $B = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$: (a) write the characteristic equation $\det(B - \lambda I) = 0$ and expand it; (b) find the eigenvalues; (c) explain in one sentence why you set the determinant to zero rather than, say, the trace or the norm.
   *Tests: the reasoning behind the characteristic equation, not just the recipe.*

2. *Difficulty: Warm-up — tests Hermitian vs. symmetric.*
   Which of the following matrices is Hermitian? For each, check $A^\dagger = A$ explicitly. (a) $\bigl[\begin{smallmatrix}2&i\\-i&3\end{smallmatrix}\bigr]$; (b) $\bigl[\begin{smallmatrix}2&i\\i&3\end{smallmatrix}\bigr]$; (c) $\bigl[\begin{smallmatrix}1&1+i\\1-i&2\end{smallmatrix}\bigr]$. For the Hermitian case(s), compute the eigenvalues and verify they are real.
   *Tests: the Hermitian condition* $A^\dagger = A$ *vs. symmetry* $A^T = A$; *real eigenvalues as a consequence.*

3. *Difficulty: Warm-up — tests orthogonality with the complex inner product.*
   Verify that $|\lambda{=}{+1}\rangle = \tfrac{1}{\sqrt{2}}\bigl(\begin{smallmatrix}-i\\1\end{smallmatrix}\bigr)$ and $|\lambda{=}{-1}\rangle = \tfrac{1}{\sqrt{2}}\bigl(\begin{smallmatrix}i\\1\end{smallmatrix}\bigr)$ (the $\sigma_y$ eigenvectors from the worked example) are orthogonal using the complex inner product $\langle u|v\rangle = \mathbf{u}^\dagger\mathbf{v}$. Then attempt the same computation using the real dot product $\mathbf{u}^T\mathbf{v}$. What do you get, and why does it differ?
   *Tests: the necessity of the conjugate inner product; a concrete failure if conjugation is omitted.*

**Application**

4. *Difficulty: Application — full diagonalization.*
   Diagonalize $\sigma_x = \bigl[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr]$: find its eigenvalues, orthonormal eigenvectors, the diagonalizing matrix $U$, and the spectral decomposition. Verify $\sigma_x = UDU^\dagger$ by multiplying out.
   *Tests: complete diagonalization procedure for a Pauli matrix; verification of the spectral decomposition.*

5. *Difficulty: Application — function of an operator.*
   Using the spectral decomposition of $\sigma_z = \bigl[\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr]$ (already diagonal): (a) compute $e^{i\theta\sigma_z}$ for real $\theta$; (b) verify the result is a unitary matrix; (c) interpret the result geometrically as a rotation of the Bloch sphere — what axis does it rotate about, and by what angle?
   *Tests: computing a matrix function via spectral decomposition for a diagonal matrix; connecting to physical rotation.*

6. *Difficulty: Application — commutator and simultaneous eigenbasis.*
   Compute $[\sigma_x, \sigma_z]$ explicitly. (a) Is it zero? (b) Find the eigenbases of $\sigma_x$ and $\sigma_z$ separately. (c) Exhibit a state $|\psi\rangle$ that is an eigenstate of $\sigma_x$ with eigenvalue $+1$; write it in the $\sigma_z$ eigenbasis and confirm it is not an eigenstate of $\sigma_z$. (d) What does the nonzero commutator say about simultaneously measuring spin along $x$ and $z$?
   *Tests: commutator as the obstruction to simultaneous diagonalization; physical interpretation in terms of quantum measurement.*

**Synthesis**

7. *Difficulty: Synthesis — degenerate perturbation theory as a diagonalization.*
   In the hydrogen $n = 2$ level, the spin-orbit perturbation $H_\text{SO}$ is block-diagonal in the $|n, \ell, j, m_j\rangle$ basis but has off-diagonal elements in the $|n, \ell, m_\ell, m_s\rangle$ basis. Consider a $2\times2$ block of $H_\text{SO}$ in the degenerate subspace:

   $$M = \begin{pmatrix}0 & \delta \\ \delta & 0\end{pmatrix}$$

   for some real $\delta > 0$. (a) Find the eigenvalues of $M$ (these are the first-order energy corrections). (b) Find the eigenvectors (the "good states"). (c) The original degenerate states are mixed by the perturbation; the good states are specific combinations. Explain in one sentence why working in the unperturbed basis $\{|1\rangle, |2\rangle\}$ would fail to give the correct first-order corrections.
   *Tests: diagonalization as the mathematical content of degenerate perturbation theory; understanding why the eigenbasis is the physically correct starting point.*

8. *Difficulty: Synthesis — density matrix diagonalization.*
   A density matrix for a two-level system is $\hat\rho = \bigl[\begin{smallmatrix}0.7 & 0.2i \\ -0.2i & 0.3\end{smallmatrix}\bigr]$. (a) Verify $\hat\rho^\dagger = \hat\rho$ and $\text{Tr}\hat\rho = 1$. (b) Diagonalize $\hat\rho$ to find its eigenvalues $p_1$ and $p_2$. (c) Verify $p_1 + p_2 = 1$ and $p_1, p_2 \geq 0$. (d) Compute the purity $\text{Tr}(\hat\rho^2) = p_1^2 + p_2^2$ and determine whether this state is pure ($\text{Tr}\hat\rho^2 = 1$) or mixed ($\text{Tr}\hat\rho^2 < 1$).
   *Tests: complete diagonalization of a density matrix; purity as a diagnostic for pure vs. mixed state.*

**Challenge**

9. *Difficulty: Challenge — the continuous spectrum and the generalized spectral theorem.*
   The position operator $\hat{x}$ on $L^2(\mathbb{R})$ has eigenvalue equation $\hat{x}|x'\rangle = x'|x'\rangle$ with formal eigenstates $\langle x|x'\rangle = \delta(x - x')$. (a) Show directly that $\delta(x - x')$ is not in $L^2(\mathbb{R})$ by computing $\int|\delta(x-x')|^2\,dx$ and identifying the divergence. (b) Despite this, the resolution of the identity $\hat{I} = \int_{-\infty}^\infty|x'\rangle\langle x'|\,dx'$ is valid in the sense that $\langle\psi|\hat{I}|\phi\rangle = \langle\psi|\phi\rangle$ for all $|\psi\rangle, |\phi\rangle\in L^2(\mathbb{R})$. Verify this by computing $\int\langle\psi|x'\rangle\langle x'|\phi\rangle\,dx'$ and showing it equals $\langle\psi|\phi\rangle = \int\psi^*(x)\phi(x)\,dx$. (c) State in one sentence what the difference is between the discrete spectral theorem (eigenvalues, eigenvectors in $\mathcal{H}$, Kronecker delta orthonormality) and the continuous generalization (continuous spectrum, generalized eigenvectors outside $\mathcal{H}$, Dirac delta orthonormality).
   *Tests: the failure of square-integrability for position eigenstates; the Dirac delta as a distribution; connecting the abstract statement to the physics of position measurements.*

---

## References

Cayley, A. (1858). A memoir on the theory of matrices. *Philosophical Transactions of the Royal Society of London*, 148, 17–37.

Cauchy, A.-L. (1829). *Exercices de mathématiques*, Vol. 4, pp. 174–195.

Hilbert, D. (1904). Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*.

Shankar, R. (1994). *Principles of Quantum Mechanics* (2nd ed.). Plenum. Chapter 1.

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*, Vol. 1. Wiley. Complement $\text{B}_\text{III}$.

Reed, M., & Simon, B. (1975). *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness*. Academic Press.
