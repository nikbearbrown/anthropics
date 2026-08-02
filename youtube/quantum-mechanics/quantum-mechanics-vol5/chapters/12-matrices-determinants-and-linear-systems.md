# Module M-12 — Matrices, Determinants, and Linear Systems
*When you need this: QM chapters II·7 (Spin-½), IV·1 (Density Matrices), IV·4 (Quantum Gates)*

Spin-½ is the simplest non-trivial quantum system, and all of Chapter II·7 is $2\times 2$ matrix algebra. The Pauli matrices are the spin operators (up to $\hbar/2$); states are two-component column vectors; measurements are eigenvalue computations; time evolution is matrix exponentiation. Chapter IV·1 adds the trace and the concept of a mixed state. Chapter IV·4 adds unitary matrices and the tensor product for multi-qubit systems.

The *Mathematics for Physics* Vol 1 foundation covers real matrices with classical mechanics examples. This module extends those foundations into the complex matrix language that quantum mechanics requires: the Hermitian conjugate, Hermitian and unitary matrices, and the Pauli matrices as a concrete worked system.

---

## What a Matrix Is and What It Does

A matrix is a rectangular array of numbers (real or complex). An $m\times n$ matrix $A$ has $m$ rows and $n$ columns; the entry in row $i$ and column $j$ is $A_{ij}$. A column vector with $n$ entries is an $n\times 1$ matrix.

Matrix multiplication: $(AB)_{ij} = \sum_k A_{ik}B_{kj}$. The product $AB$ requires the number of columns of $A$ to equal the number of rows of $B$. Matrix multiplication is **not commutative** in general: $AB \neq BA$.

The **commutator** of two matrices is $[A, B] = AB - BA$. If $[A, B] = 0$, the matrices commute and share a common set of eigenvectors. In QM, the commutator $[\hat A, \hat B] = i\hbar\hat C$ encodes the uncertainty principle; for the Pauli matrices, $[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk}\sigma_k$ is the algebra of angular momentum.

A **linear system** $A\mathbf{x} = \mathbf{b}$ asks: find the vector $\mathbf{x}$ such that $A$ applied to it gives $\mathbf{b}$. In QM the system is often: given an operator (matrix) and an eigenvalue condition, find the eigenstates.

---

## The Determinant

For a $2\times 2$ matrix:

$$\det A = a_{11}a_{22} - a_{12}a_{21}.$$

The geometric meaning: the signed area of the parallelogram spanned by the two row vectors. Zero determinant means the rows are linearly dependent — the matrix is singular and $A\mathbf{x} = \mathbf{b}$ has either no solution or infinitely many.

For a $3\times 3$ matrix, cofactor expansion along the top row:

$$\det A = a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33}\end{vmatrix} - a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33}\end{vmatrix} + a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32}\end{vmatrix}.$$

Key properties: $\det(AB) = \det(A)\det(B)$; $\det(A^\dagger) = (\det A)^*$; $\det A = 0 \Leftrightarrow A$ is singular; $\det(\alpha A) = \alpha^n\det(A)$ for an $n\times n$ matrix (not $\alpha\det A$ — a frequent error).

**Solvability.** The system $A\mathbf{x} = \mathbf{b}$ has a unique solution when $\det A \neq 0$. Cramer's rule: $x_j = \det A_j / \det A$, where $A_j$ is $A$ with column $j$ replaced by $\mathbf{b}$. For $n > 3$, use Gaussian elimination.

---

## Complex Matrices: The Hermitian Conjugate

QM requires matrices with complex entries. Three operations are important:

**Complex conjugate** $A^*$: replace each entry $A_{ij}$ with $A_{ij}^*$.

**Transpose** $A^T$: reflect entries across the diagonal, $(A^T)_{ij} = A_{ji}$.

**Hermitian conjugate (adjoint)** $A^\dagger$: conjugate and transpose simultaneously, $(A^\dagger)_{ij} = A_{ji}^*$.

A matrix is **Hermitian** if $A^\dagger = A$ — each entry equals the complex conjugate of its mirror. Hermitian matrices have real eigenvalues and orthogonal eigenvectors; they represent observables in QM.

A matrix is **unitary** if $U^\dagger U = UU^\dagger = I$. Unitary matrices preserve inner products and norms; they represent time evolution, rotations, and quantum gates.

These three operations are distinct. For real matrices, $A^\dagger = A^T$. For a real symmetric matrix, $A^\dagger = A$, so it is automatically Hermitian. For $\sigma_y$: the $(1,2)$ entry is $-i$; its conjugate is $+i$; the $(1,2)$ entry of $A^\dagger$ (which is the $(2,1)$ entry of $A^*$) is $+i$, and indeed $\sigma_y^\dagger = \sigma_y$.

![Three conjugate operations on a complex matrix](../images/12-matrices-determinants-and-linear-systems-fig-01.png)
*Figure 12.1 — Three conjugate operations: complex conjugate $A^*$ (same positions, conjugated entries), transpose $A^T$ (swapped off-diagonal positions), and Hermitian conjugate $A^\dagger$ (both operations combined), which is the primary operation in quantum mechanics.*

---

## The Trace

The trace of an $n\times n$ matrix is the sum of the diagonal entries: $\operatorname{tr}(A) = \sum_i A_{ii}$.

Key properties: $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ — cyclic invariance, more generally $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$; $\operatorname{tr}(A+B) = \operatorname{tr}(A) + \operatorname{tr}(B)$; $\operatorname{tr}(A^\dagger) = (\operatorname{tr}A)^*$; the trace is basis-independent ($\operatorname{tr}(S^{-1}AS) = \operatorname{tr}(A)$); for a $2\times 2$ matrix, $\operatorname{tr}(A) = \lambda_1 + \lambda_2$ and $\det(A) = \lambda_1\lambda_2$ where $\lambda_i$ are eigenvalues.

The trace is not the determinant. $\det(A+B) \neq \det(A) + \det(B)$ and $\operatorname{tr}(AB) \neq \operatorname{tr}(A)\operatorname{tr}(B)$. These are among the most common algebraic errors.

In QM: the expectation value of observable $\hat A$ in state $\rho$ is $\langle\hat A\rangle = \operatorname{tr}(\rho\hat A)$; normalization of the density matrix is $\operatorname{tr}(\rho) = 1$; purity is $\operatorname{tr}(\rho^2) \leq 1$; and the probability of outcome $a_i$ is $\operatorname{tr}(\Pi_i\,\rho)$ where $\Pi_i = |a_i\rangle\langle a_i|$.

---

## Eigenvalues and the Characteristic Polynomial

The eigenvalue equation is $A\mathbf{v} = \lambda\mathbf{v}$: the vector $\mathbf{v}$ (eigenvector) changes only by the scalar $\lambda$ (eigenvalue). Rearranging: $(A - \lambda I)\mathbf{v} = \mathbf{0}$. For a non-trivial solution, the matrix $(A - \lambda I)$ must be singular:

$$\det(A - \lambda I) = 0.$$

For a $2\times 2$ matrix this gives $\lambda^2 - \operatorname{tr}(A)\,\lambda + \det(A) = 0$ — a degree-2 polynomial whose coefficients encode the trace and determinant directly.

For Hermitian $A$: all eigenvalues are real. If $\lambda_1 \neq \lambda_2$, the corresponding eigenvectors are orthogonal. The **spectral decomposition** is:

$$A = \sum_i \lambda_i\,|v_i\rangle\langle v_i|,$$

where $\{|v_i\rangle\}$ is the orthonormal eigenbasis. In QM, measurement of observable $A$ yields eigenvalue $\lambda_i$ with probability $|\langle v_i|\psi\rangle|^2$, and collapses the state to $|v_i\rangle$.

---

## The Pauli Matrices and Spin-½

The Pauli matrices are the three traceless Hermitian $2\times 2$ matrices:

$$\sigma_x = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}.$$

Together with the identity $I$, they form a basis for all $2\times 2$ Hermitian matrices: any Hermitian $2\times 2$ matrix $A$ decomposes as $A = a_0 I + \mathbf{a}\cdot\boldsymbol{\sigma}$ with real $a_0$ and $\mathbf{a}$.

**Properties.** Each Pauli matrix is Hermitian ($\sigma_i^\dagger = \sigma_i$), squares to the identity ($\sigma_i^2 = I$), has eigenvalues $\pm 1$, and is traceless with $\det(\sigma_i) = -1$.

**Commutation relations** (the algebra of SU(2), hence of angular momentum):

$$[\sigma_i, \sigma_j] = 2i\,\varepsilon_{ijk}\,\sigma_k.$$

Explicitly: $[\sigma_x, \sigma_y] = 2i\sigma_z$, $[\sigma_y, \sigma_z] = 2i\sigma_x$, $[\sigma_z, \sigma_x] = 2i\sigma_y$.

![Pauli matrix commutation cycle](../images/12-matrices-determinants-and-linear-systems-fig-03.png)
*Figure 12.3 — Pauli matrix commutation cycle: the three Pauli operators form a closed clockwise cycle under the commutation relation $[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk}\sigma_k$, reflecting the SU(2) algebra of angular momentum.*

**Anticommutation:** $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$.

Combined: $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$.

The spin-½ angular momentum operators are $\hat S_i = (\hbar/2)\sigma_i$. The eigenstates:

$$|{\uparrow}\rangle = \begin{pmatrix}1\\0\end{pmatrix},\quad |{\downarrow}\rangle = \begin{pmatrix}0\\1\end{pmatrix} \quad(\sigma_z\text{ eigenstates, eigenvalues }+1,\,-1).$$

$$|{+x}\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix},\quad |{-x}\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix} \quad(\sigma_x\text{ eigenstates, eigenvalues }+1,\,-1).$$

$$|{+y}\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix},\quad |{-y}\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix} \quad(\sigma_y\text{ eigenstates, eigenvalues }+1,\,-1).$$

$\text{Spin-}\hat n$ **component.** For any unit vector $\hat n = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$, the operator $\hat n\cdot\boldsymbol{\sigma}$ has eigenvalues $\pm 1$ and eigenstates:

$$|{+\hat n}\rangle = \begin{pmatrix}\cos(\theta/2) \\ e^{i\phi}\sin(\theta/2)\end{pmatrix}, \qquad |{-\hat n}\rangle = \begin{pmatrix}-e^{-i\phi}\sin(\theta/2) \\ \cos(\theta/2)\end{pmatrix}.$$

**Rotation of spinors.** A rotation by angle $\alpha$ about axis $\hat n$ acts on the spinor as:

$$U = e^{-i\alpha\hat n\cdot\boldsymbol{\sigma}/2} = \cos(\alpha/2)\,I - i\sin(\alpha/2)\,(\hat n\cdot\boldsymbol{\sigma}).$$

This uses $(\hat n\cdot\boldsymbol{\sigma})^2 = I$. The factor $1/2$ means a $2\pi$ rotation gives $U = -I$, not $+I$: a spinor picks up a phase of $-1$ under a full rotation. This is the mathematical signature of spin-½ and has no classical analogue.

---

## The Density Matrix

A pure state $|\psi\rangle$ defines a density matrix $\rho = |\psi\rangle\langle\psi|$ — a rank-1 Hermitian positive semi-definite matrix with $\operatorname{tr}(\rho) = 1$ and $\rho^2 = \rho$.

A mixed state is a statistical mixture: $\rho = \sum_i p_i|\psi_i\rangle\langle\psi_i|$ with $p_i \geq 0$ and $\sum_i p_i = 1$. For a single qubit:

$$\rho = \frac{1}{2}(I + \mathbf{r}\cdot\boldsymbol{\sigma}), \qquad |\mathbf{r}| \leq 1.$$

The vector $\mathbf{r}$ is the Bloch vector; its coordinates are the spin expectation values: $r_i = \operatorname{tr}(\rho\sigma_i)$. Pure states live on the Bloch sphere ($|\mathbf{r}| = 1$); mixed states live inside it.

Properties encoded in the density matrix: $\operatorname{tr}(\rho) = 1$ (normalization); $\rho^\dagger = \rho$ (Hermiticity — $\mathbf{r}$ must be real); $\rho \geq 0$ (positive semi-definite — equivalent to $|\mathbf{r}| \leq 1$); $\operatorname{tr}(\rho^2) = (1 + |\mathbf{r}|^2)/2$ (equals 1 iff pure).

![Bloch sphere cross-section showing pure and mixed states](../images/12-matrices-determinants-and-linear-systems-fig-02.png)
*Figure 12.2 — Bloch sphere: pure states live on the surface ($|\mathbf{r}| = 1$), mixed states occupy the interior ($|\mathbf{r}| < 1$), and the maximally mixed state $\rho = I/2$ sits at the center.*

The expectation value of any observable $\hat A$:

$$\langle\hat A\rangle = \operatorname{tr}(\rho\,\hat A).$$

This is the fundamental formula for computing predictions from a density matrix, including when the state is mixed and no single wavefunction describes it.

---

## Quantum Gates: Unitary Matrices

A quantum gate on a single qubit is a $2\times 2$ unitary matrix $U$ ($UU^\dagger = I$). Gates are applied by matrix-vector multiplication: $|\psi'\rangle = U|\psi\rangle$. Sequential gates compose by matrix multiplication: applying $V$ then $U$ gives $UV|\psi\rangle$.

Standard single-qubit gates. The Pauli gates are each their own inverse (Hermitian and unitary). The Hadamard gate:

$$H = \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}.$$

$H^2 = I$ (self-inverse). $H|0\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ — the Hadamard creates equal superposition and rotates between the $z$-eigenbasis and the $x$-eigenbasis. The phase gate $S = \operatorname{diag}(1, i)$ and $T$-gate $T = \operatorname{diag}(1, e^{i\pi/4})$ add phases without changing populations.

---

## The Kronecker Product for Composite Systems

A two-qubit system lives in $\mathbb{C}^2 \otimes \mathbb{C}^2 \cong \mathbb{C}^4$. The Kronecker product (matrix tensor product) $A \otimes B$ encodes operators on composite systems:

$$A \otimes B = \begin{pmatrix}a_{11}B & a_{12}B \\ a_{21}B & a_{22}B\end{pmatrix}.$$

The CNOT gate (controlled-NOT, the key two-qubit gate):

$$\text{CNOT} = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$$

in the basis $|00\rangle, |01\rangle, |10\rangle, |11\rangle$. It flips qubit 2 if and only if qubit 1 is $|1\rangle$. CNOT is not a tensor product of single-qubit gates — it is an entangling gate.

A single-qubit gate $U$ acting on qubit 1 of a two-qubit system is $U \otimes I_{2\times 2}$ — a $4\times 4$ matrix. Writing just $U$ in a two-qubit calculation is a dimension error. The rule: $n$ qubits require $2^n\times 2^n$ matrices.

---

## Worked Example: Eigenvalues and Eigenvectors of $\sigma_x$

**Problem.** Find the eigenvalues and eigenvectors of $\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ and interpret the result as a spin measurement.

**Step 1 — characteristic polynomial:**

$$\det(\sigma_x - \lambda I) = \det\begin{pmatrix}-\lambda & 1 \\ 1 & -\lambda\end{pmatrix} = \lambda^2 - 1 = 0.$$

Eigenvalues: $\lambda_\pm = \pm 1$. Check: $\operatorname{tr}(\sigma_x) = 0 = \lambda_+ + \lambda_-$ ✓; $\det(\sigma_x) = -1 = \lambda_+\lambda_-$ ✓.

**Step 2 — eigenvectors:**

For $\lambda = +1$: $(\sigma_x - I)\mathbf{v} = \mathbf{0}$ gives $\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\mathbf{v} = \mathbf{0}$, so $v_1 = v_2$. Normalized: $|{+x}\rangle = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$.

For $\lambda = -1$: $(\sigma_x + I)\mathbf{v} = \mathbf{0}$ gives $\begin{pmatrix}1&1\\1&1\end{pmatrix}\mathbf{v} = \mathbf{0}$, so $v_1 = -v_2$. Normalized: $|{-x}\rangle = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}$.

**Step 3 — orthogonality check:**

$$\langle{+x}|{-x}\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\end{pmatrix}\cdot\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix} = \frac{1}{2}(1-1) = 0. \checkmark$$

**Step 4 — QM interpretation.** $\sigma_x$ is a Hermitian observable. Its eigenvalues $\pm 1$ (equivalently $S_x = \pm\hbar/2$) are the only possible outcomes of an $x$-spin measurement. After measuring $S_x = +\hbar/2$, the state collapses to $|{+x}\rangle$, a superposition of $|{\uparrow}\rangle$ and $|{\downarrow}\rangle$ in equal proportions.

**Step 5 — verify Hadamard diagonalizes** $\sigma_x$. Since $H|{+x}\rangle = |{\uparrow}\rangle$ and $H|{-x}\rangle = |{\downarrow}\rangle$, the Hadamard gate rotates between the $z$-eigenbasis and the $x$-eigenbasis. Verify by matrix multiplication: $H\,\sigma_x\,H^\dagger = \sigma_z$.

---

## Where These Methods Appear in the Quantum Series

**QM II·7 — Spin-½.** The entire chapter is $2\times 2$ matrix algebra. Key computations: finding eigenvalues of $\hat S_n = \hat{\mathbf{S}}\cdot\hat n$ for any direction $\hat n$ by the characteristic polynomial; computing rotation of spinors using $U = e^{-i\alpha\hat n\cdot\boldsymbol{\sigma}/2}$; evaluating $\langle S_x\rangle$, $\langle S_y\rangle$, $\langle S_z\rangle$ for a given spinor using $\langle S_i\rangle = (\hbar/2)\langle\psi|\sigma_i|\psi\rangle$. The non-commutativity of Pauli matrices $[\sigma_x, \sigma_y] = 2i\sigma_z$ directly encodes the non-commutativity of spin measurements.

**QM IV·1 — Density Matrix.** The density matrix is Hermitian, positive semi-definite, and has unit trace. For a single qubit the Bloch-sphere parametrization $\rho = (I + \mathbf{r}\cdot\boldsymbol{\sigma})/2$ encodes all physical information. The trace formula $\langle A\rangle = \operatorname{tr}(\rho A)$ is the central computational tool. Purity $\operatorname{tr}(\rho^2)$: compute $\rho^2$ by matrix multiplication, then trace the result. For the Bloch parametrization: $\rho^2 = (I + \mathbf{r}\cdot\boldsymbol{\sigma})^2/4$, so $\operatorname{tr}(\rho^2) = (1 + |\mathbf{r}|^2)/2$.

**QM IV·4 — Quantum Gates.** Every single-qubit gate is a $2\times 2$ unitary matrix. Gate composition is matrix multiplication; the inverse of a unitary gate is its Hermitian conjugate. Two-qubit gates are $4\times 4$ unitary matrices, constructed as Kronecker products for separable operations or directly (as the CNOT) for entangling operations.

A simple circuit to verify by hand: $H\,X\,H = Z$. Computing step by step:

$$X\,H = \begin{pmatrix}0&1\\1&0\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1&-1\\1&1\end{pmatrix},$$

$$H\,(XH) = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1&-1\\1&1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2&0\\0&-2\end{pmatrix} = Z. \checkmark$$

---

## Conventions and Pitfalls

$A^\dagger$ **vs.** $A^T$ **vs.** $A^*$. These are three different operations. $A^\dagger = (A^*)^T$ — conjugate each entry AND transpose. Never write $A^*$ when you mean $A^\dagger$: getting the order of operations wrong gives the wrong matrix.

**Row vs. column vectors.** In QM, $|\psi\rangle$ is a column vector; $\langle\psi|$ is its Hermitian conjugate, a row vector. The inner product $\langle\phi|\psi\rangle$ is (row) times (column) = scalar. The outer product $|\psi\rangle\langle\phi|$ is (column) times (row) = matrix. Reversing these produces scalars where matrices are needed and vice versa.

**Determinant is not additive.** $\det(A+B) \neq \det(A) + \det(B)$. Also: $\det(\alpha A) = \alpha^n\det(A)$, not $\alpha\det(A)$, for an $n\times n$ matrix.

**Trace cyclicity requires valid multiplication.** $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$ — cyclic, not arbitrary permutation. $\operatorname{tr}(ABC) \neq \operatorname{tr}(ACB)$ in general.

**Pauli matrix convention.** The standard physics convention is $[\sigma_x, \sigma_y] = 2i\sigma_z$. Some sources use $\sigma_i/2$ as generators (giving $[\sigma_i/2, \sigma_j/2] = i\varepsilon_{ijk}\sigma_k/2$). Mixing conventions gives wrong commutators. Verify any convention by checking whether $[\sigma_x, \sigma_y]$ gives $2i\sigma_z$ or $i\sigma_z$.

**Two-qubit dimensions.** A single qubit is $\mathbb{C}^2$; a two-qubit system is $\mathbb{C}^4$. To apply $\sigma_x$ to qubit 1 of a two-qubit system, the operator is $\sigma_x \otimes I_{2\times 2}$ — a $4\times 4$ matrix. Writing just $\sigma_x$ in a two-qubit calculation is a dimension error. The rule: $n$ qubits require $2^n\times 2^n$ matrices.

---

## Quick Practice

1. **Eigenvalues of** $\sigma_z$. Compute $\det(\sigma_z - \lambda I) = 0$ explicitly, find the eigenvalues, and verify $\operatorname{tr}(\sigma_z) = \lambda_1 + \lambda_2$ and $\det(\sigma_z) = \lambda_1\lambda_2$. Write the eigenvectors and confirm they are orthogonal.

2. **Density matrix.** Compute $\rho = |{+x}\rangle\langle{+x}|$ for $|{+x}\rangle = (1,1)^T/\sqrt{2}$. Verify: (a) $\operatorname{tr}(\rho) = 1$, (b) $\rho^2 = \rho$ (pure state), (c) $\langle\sigma_x\rangle = \operatorname{tr}(\rho\sigma_x) = 1$.

3. **Gate composition.** Verify by matrix multiplication that $H\,Z\,H = X$. Then compute the action of the circuit on $|{\uparrow}\rangle = (1,0)^T$: apply $H$, then $Z$, then $H$, and confirm the result equals $X|{\uparrow}\rangle = |{\downarrow}\rangle = (0,1)^T$.

---

## Go Deeper

The real-matrix foundations — linear systems, determinants, Cramer's rule, Gaussian elimination — are in *Mathematics for Physics* Vol 1, Ch 10. The QM-critical extensions in this module (complex matrices, Hermitian conjugate, Pauli matrices, trace, Kronecker product) go beyond that source.

For the spectral theorem and diagonalization, see Module M-08 and *Mathematics for Physics* Vol 2, Ch 4. For the tensor product and composite Hilbert spaces, see Module M-17.

---

## References

Cayley, A. (1858). A memoir on the theory of matrices. *Philosophical Transactions of the Royal Society*, 148, 17–46.

Pauli, W. (1927). Zur Quantenmechanik des magnetischen Elektrons. *Zeitschrift für Physik*, 43, 601–623. Introduction of the Pauli matrices as spin operators.

Dirac, P. A. M. (1958). *The Principles of Quantum Mechanics* (4th ed.). Oxford University Press. Chapter XI (spin).

Nielsen, M. A., & Chuang, I. L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. Chapter 2.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. Chapter 4.4.
