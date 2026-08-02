# Vector Spaces, Eigenvalues, and Diagonalization

*The linear algebra that quantum mechanics, classical normal modes, and optics all run on — where the characteristic equation comes from, and why a symmetric matrix always diagonalizes.*

---

## 1. Cold open: two carts, two springs

Set two equal masses $m$ on a frictionless track. Anchor each to a wall with a spring of stiffness $k$, and join them to each other with a third spring of stiffness $k$. Pull both carts aside, release, and watch.

What you see is not simple. Each cart's motion looks like a beat — a fast wiggle whose amplitude swells and fades. Neither cart oscillates at a single clean frequency; energy sloshes back and forth between them. Yet the system is perfectly linear and deterministic. Newton's second law for the two displacements $x_1$ and $x_2$ reads

$$
m\ddot{x}_1 = -k x_1 - k(x_1 - x_2), \qquad
m\ddot{x}_2 = -k x_2 - k(x_2 - x_1).
$$

The two equations are *coupled*: $\ddot{x}_1$ depends on $x_2$, and vice versa. You cannot solve one without the other. The motion looks complicated because we are watching it in the wrong coordinates.

There exist two special motions — call them **normal modes** — in which both carts oscillate at a single shared frequency, perfectly in step. In one, the carts move together (the middle spring never stretches); in the other, they move oppositely. Every possible motion of the system is a superposition of just these two. Finding them is not a trick of cleverness. It is an *eigenvalue problem*, and the same problem — dressed in different physical clothing — decides the energy levels of a two-state atom and the polarization an optical wave plate leaves untouched. This chapter builds the machine that solves all three at once.

---

## 2. The tool, named

Volume 1 taught you to solve a linear system $A\mathbf{x} = \mathbf{b}$ — given a matrix and a target, find the input. This chapter asks a different question. Given a linear map $A$, find the special directions it does not turn — the vectors it merely stretches or shrinks:

$$
A\mathbf{v} = \lambda \mathbf{v}, \qquad \mathbf{v} \neq \mathbf{0}.
$$

A nonzero vector $\mathbf{v}$ obeying this is an **eigenvector**; the scaling factor $\lambda$ is its **eigenvalue** (German *eigen*, "own" or "characteristic" — Hilbert popularized the term around 1904 in the theory of integral equations). Most vectors get rotated when $A$ acts; eigenvectors are the axes along which $A$ acts like simple multiplication. If you can find a full set of them, you can change to coordinates in which $A$ is *diagonal* — and a diagonal matrix decouples everything it touches. That is the payoff: diagonalization turns the coupled carts into two independent oscillators.

Before the eigenvalue problem we need the scaffolding: what a vector space is, how a linear map becomes a matrix once a basis is chosen, and how the determinant detects when a system has nontrivial solutions.

### Vector spaces and bases

A **vector space** $V$ over a field $\mathbb{F}$ (for us $\mathbb{R}$ or $\mathbb{C}$) is a set of objects you can add and scale, with the arithmetic behaving as expected: addition is commutative and associative, there is a zero vector, every vector has a negative, and scalar multiplication distributes over both sums. The objects need not be arrows. Column vectors in $\mathbb{C}^n$ qualify; so do polynomials, and so do the wavefunctions of Chapter 5 — which is exactly why the same algebra serves both.

A set of vectors is **linearly independent** if no nontrivial combination of them vanishes: $\sum_i c_i \mathbf{v}_i = \mathbf{0}$ forces every $c_i = 0$. A **basis** is a linearly independent set that spans $V$ — every vector is a *unique* combination of basis vectors. The number of basis vectors is the **dimension** of $V$, and it does not depend on which basis you choose. Choosing a basis is choosing coordinates: it turns abstract vectors into concrete columns of numbers.

### Linear transformations and matrices

A map $T: V \to V$ is **linear** if it respects the structure: $T(a\mathbf{u} + b\mathbf{v}) = a\,T(\mathbf{u}) + b\,T(\mathbf{v})$. Pick a basis $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$. Linearity means $T$ is completely determined by what it does to the basis vectors, because any input is a combination of them. Write each image in the basis:

$$
T(\mathbf{e}_j) = \sum_{i=1}^{n} A_{ij}\,\mathbf{e}_i.
$$

The numbers $A_{ij}$ are the entries of the **matrix** of $T$ in this basis; the image of $\mathbf{e}_j$ is the $j$-th column. (Arthur Cayley, in his 1858 "Memoir on the Theory of Matrices," was the first to treat such an array as a single algebraic object with its own multiplication — initially regarded as a mere convenient notation for linear transformations.) Crucially, the *same* linear map has *different* matrices in different bases. The whole game of diagonalization is to find the basis in which the matrix is as simple as possible.

### Determinants and singularity

The **determinant** $\det A$ is a single number computed from $A$'s entries that vanishes exactly when $A$ is singular — when its columns are linearly dependent, equivalently when $A$ maps some nonzero vector to zero. We take the cofactor expansion from Volume 1 as known. The one fact we will lean on relentlessly:

$$
A\mathbf{v} = \mathbf{0} \text{ has a nonzero solution } \mathbf{v}
\iff \det A = 0.
$$

A square system has a nontrivial nullspace if and only if its determinant is zero. Everything about eigenvalues flows from this single equivalence.

---

## 3. Development & derivation

### Where the characteristic equation comes from

Rewrite the eigenvalue equation by moving everything to one side:

$$
A\mathbf{v} = \lambda \mathbf{v}
\;\Longrightarrow\;
A\mathbf{v} - \lambda \mathbf{v} = \mathbf{0}
\;\Longrightarrow\;
(A - \lambda I)\,\mathbf{v} = \mathbf{0},
$$

where $I$ is the identity matrix (we insert it so that $\lambda$ subtracts from $A$ as a matrix, not a scalar). This is a homogeneous linear system for the unknown vector $\mathbf{v}$. It *always* has the trivial solution $\mathbf{v} = \mathbf{0}$ — which we forbade. So the question becomes: for which values of $\lambda$ does $(A - \lambda I)\mathbf{v} = \mathbf{0}$ have a *nonzero* solution?

By the singularity fact, that happens precisely when the matrix $A - \lambda I$ is singular:

$$
\boxed{\;\det(A - \lambda I) = 0.\;}
$$

This is the **characteristic equation**, and this derivation is the answer to a question students often cannot answer: *why* set the determinant to zero? Because a nonzero eigenvector is, by definition, a nonzero vector in the nullspace of $A - \lambda I$ — and a matrix has a nontrivial nullspace exactly when its determinant vanishes. Setting $\det(A-\lambda I)=0$ is not a recipe; it is the literal condition for an eigenvector to exist.

Expanding the determinant gives a polynomial in $\lambda$ of degree $n$ (for an $n \times n$ matrix), the **characteristic polynomial** $p(\lambda) = \det(A - \lambda I)$. Its roots are the eigenvalues. Over $\mathbb{C}$ a degree-$n$ polynomial always has $n$ roots counted with multiplicity (the fundamental theorem of algebra, Volume 1), so an $n \times n$ complex matrix always has $n$ eigenvalues — though some may coincide, and some may be complex even when $A$ is real. For each eigenvalue, solving $(A - \lambda I)\mathbf{v} = \mathbf{0}$ recovers the eigenvector(s).

### Diagonalization

Suppose $A$ ($n \times n$) has $n$ linearly independent eigenvectors $\mathbf{v}_1, \dots, \mathbf{v}_n$ with eigenvalues $\lambda_1, \dots, \lambda_n$. Stack the eigenvectors as the columns of a matrix $P = [\,\mathbf{v}_1 \;\cdots\; \mathbf{v}_n\,]$. Then $A$ acting on each column gives $A\mathbf{v}_j = \lambda_j \mathbf{v}_j$, so

$$
AP = [\,\lambda_1 \mathbf{v}_1 \;\cdots\; \lambda_n \mathbf{v}_n\,] = P D,
\qquad
D = \operatorname{diag}(\lambda_1, \dots, \lambda_n).
$$

Because the eigenvectors are independent, $P$ is invertible, and we may write

$$
\boxed{\;A = P D P^{-1}, \qquad D = P^{-1} A P.\;}
$$

The matrix $P^{-1}AP$ is $A$ *expressed in the eigenbasis*, and there it is diagonal. The off-diagonal entries — the couplings — are gone. This is exactly what we need for the carts: in the eigenbasis the equations of motion decouple into independent oscillators.

![A commuting square. Across the top, the matrix A acts in the original basis where it couples the coordinates. Down the left, P inverse changes into the eigenbasis; across the bottom the diagonal matrix D simply scales each coordinate; up the right, P changes back. Both routes agree, which is A equals P D P inverse.](images/04-vector-spaces-eigenvalues-and-diagonalization-fig-03.png)
*Figure 4.3 — Diagonalization as a change of basis: in the eigenbasis the coupled map $A$ becomes the diagonal $D$, and $A = PDP^{-1}$ is the round trip.*

Not every matrix diagonalizes. A matrix with fewer than $n$ independent eigenvectors is **defective** (the simplest example is $\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$, whose only eigenvalue $1$ yields a single eigenvector direction); such matrices reduce only to Jordan form, which we do not develop here. The reassuring fact for physics is the spectral theorem below: the symmetric and Hermitian matrices that physics actually produces are *never* defective.

### Why a symmetric matrix always diagonalizes (the spectral theorem)

A real matrix is **symmetric** if $A^T = A$. Cauchy showed already in 1829, in the language of quadratic forms and the "secular equation" of celestial mechanics, that such matrices have entirely real eigenvalues and mutually perpendicular principal axes. Here is the modern argument, and it is short.

**Real eigenvalues.** Take an eigenpair $A\mathbf{v} = \lambda\mathbf{v}$, allowing complex entries for the moment. Let $\mathbf{v}^\dagger$ denote the conjugate transpose. Multiply on the left by $\mathbf{v}^\dagger$:

$$
\mathbf{v}^\dagger A \mathbf{v} = \lambda\, \mathbf{v}^\dagger \mathbf{v} = \lambda\,\|\mathbf{v}\|^2 .
$$

Now take the conjugate transpose of the whole scalar $\mathbf{v}^\dagger A \mathbf{v}$. Since it is a number, conjugating equals taking the dagger: $(\mathbf{v}^\dagger A \mathbf{v})^\dagger = \mathbf{v}^\dagger A^\dagger \mathbf{v}$. For a *real symmetric* matrix $A^\dagger = A^T = A$, so this equals $\mathbf{v}^\dagger A \mathbf{v}$ again — the quantity is its own conjugate, hence real. Therefore $\lambda \|\mathbf{v}\|^2$ is real, and since $\|\mathbf{v}\|^2 > 0$, the eigenvalue $\lambda$ is real. (The identical argument with $A^\dagger = A$ proves real eigenvalues for complex *Hermitian* matrices; Chapter 5 leans on exactly this.)

**Orthogonal eigenvectors.** Take two eigenpairs with *distinct* eigenvalues, $A\mathbf{v}_1 = \lambda_1\mathbf{v}_1$ and $A\mathbf{v}_2 = \lambda_2 \mathbf{v}_2$, $\lambda_1 \neq \lambda_2$, eigenvalues now known real. Compute $\mathbf{v}_2^T A \mathbf{v}_1$ two ways. Acting right: $\mathbf{v}_2^T A \mathbf{v}_1 = \lambda_1 \mathbf{v}_2^T \mathbf{v}_1$. Acting left, using $A^T = A$ so that $\mathbf{v}_2^T A = (A\mathbf{v}_2)^T = \lambda_2 \mathbf{v}_2^T$: the same quantity equals $\lambda_2 \mathbf{v}_2^T \mathbf{v}_1$. Subtract:

$$
(\lambda_1 - \lambda_2)\,\mathbf{v}_2^T \mathbf{v}_1 = 0.
$$

Since $\lambda_1 \neq \lambda_2$, we must have $\mathbf{v}_2^T \mathbf{v}_1 = 0$: the eigenvectors are **orthogonal**. (When an eigenvalue is repeated, its eigenspace can be made orthonormal internally by Gram–Schmidt, Chapter 5.) Normalizing each eigenvector to unit length makes $P$ an **orthogonal** matrix, $P^T = P^{-1}$, and the diagonalization becomes $A = PDP^T$. A real symmetric matrix is therefore always diagonalizable by a rotation of axes, with real eigenvalues — the finite-dimensional **spectral theorem**. This is the result that makes the physics safe.

---

## 4. Worked examples

### Example 1 — A 2×2 symmetric matrix, diagonalized

Let

$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.
$$

Characteristic equation:

$$
\det(A - \lambda I) = \det\begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix}
= (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0,
$$

so $(\lambda - 1)(\lambda - 3) = 0$ and $\lambda = 1, 3$ — real, as the spectral theorem guarantees. For $\lambda = 3$, solve $(A - 3I)\mathbf{v} = \mathbf{0}$: $\left[\begin{smallmatrix}-1 & 1\\ 1 & -1\end{smallmatrix}\right]\mathbf{v}=\mathbf 0$ gives $v_1 = v_2$, so $\mathbf{v} = (1,1)^T/\sqrt{2}$. For $\lambda = 1$: $\left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]\mathbf v=\mathbf 0$ gives $v_1 = -v_2$, so $\mathbf{v} = (1,-1)^T/\sqrt{2}$. The two eigenvectors are orthogonal, as promised. With $P = \frac{1}{\sqrt 2}\left[\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right]$ we get $P^T A P = \operatorname{diag}(3, 1)$.

![A grid of vectors before and after applying the matrix with entries two, one, one, two. A generic vector is rotated by the map, but the two eigenvectors along the lines y equals x and y equals minus x keep their direction and are merely scaled, by three and by one respectively.](images/04-vector-spaces-eigenvalues-and-diagonalization-fig-01.png)
*Figure 4.1 — Eigenvectors are the directions $A$ only scales: a generic vector is turned, but $(1,1)$ stretches by $\lambda=3$ and $(1,-1)$ by $\lambda=1$, each keeping its direction.*

### Example 2 — The Pauli matrix, where Hermitian beats symmetric

Quantum mechanics builds two-state systems on the Pauli matrices. Take

$$
\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}.
$$

This is *not* symmetric ($\sigma_y^T \neq \sigma_y$), but it is **Hermitian**: $\sigma_y^\dagger = (\sigma_y^T)^* = \sigma_y$. The Hermitian version of the theorem still forces real eigenvalues. Characteristic equation:

$$
\det\begin{pmatrix} -\lambda & -i \\ i & -\lambda \end{pmatrix}
= \lambda^2 - (-i)(i) = \lambda^2 - 1 = 0
\;\Longrightarrow\; \lambda = \pm 1.
$$

Real, despite the imaginary entries — exactly what an observable's eigenvalues must be. The eigenvector for $\lambda = +1$ solves $-v_1 - i v_2 = 0$, giving $\mathbf{v}_+ = (1, i)^T/\sqrt{2}$; for $\lambda = -1$, $\mathbf{v}_- = (1, -i)^T/\sqrt{2}$. These are the two spin states polarized along $\pm y$. Note that "symmetric" is the wrong condition over $\mathbb{C}$; **Hermitian** ($A^\dagger = A$) is the right one, and it is the protagonist of the next chapter.

### Example 3 — Jones calculus: the polarization a wave plate leaves alone

In R. C. Jones's 1941 calculus for optical systems, a polarization state is a vector in $\mathbb{C}^2$ and each optical element is a $2 \times 2$ matrix. A quarter-wave plate with fast axis horizontal is (up to an overall phase)

$$
W = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}.
$$

It is already diagonal, so its **eigenpolarizations** are the basis states $(1,0)^T$ (horizontal) and $(0,1)^T$ (vertical), with eigenvalues $1$ and $i$. Physically: light polarized along either axis emerges with the same polarization, merely phase-shifted — the eigenvalue is the phase factor. Feed in light at $45^\circ$, a *combination* of the two eigenstates, and the relative phase $i$ between them converts it to circular polarization. The eigenvectors are precisely the states the device cannot scramble; everything else is a superposition that the device reshapes. Same equation $A\mathbf{v}=\lambda\mathbf{v}$, third physical costume.

---

## 5. Return to the cold open: normal modes as an eigenvalue problem

Return to the two carts. Look for a motion in which both oscillate at one frequency $\omega$: set $x_j(t) = a_j \cos\omega t$, so $\ddot{x}_j = -\omega^2 x_j$. The equations of motion

$$
m\ddot{x}_1 = -2k x_1 + k x_2, \qquad
m\ddot{x}_2 = k x_1 - 2k x_2
$$

become, in matrix form with $\mathbf{a} = (a_1, a_2)^T$,

$$
-\omega^2 m\, \mathbf{a} = -K\mathbf{a}, \qquad
K = \begin{pmatrix} 2k & -k \\ -k & 2k \end{pmatrix},
$$

where $K$ is the **stiffness matrix**. Rearranged, $K\mathbf{a} = \omega^2 m\, \mathbf{a}$.

A word of honesty about the general structure. With *unequal* masses this is a **generalized eigenvalue problem** $K\mathbf{a} = \omega^2 M \mathbf{a}$, with $M$ the (diagonal) mass matrix — not quite the $A\mathbf{v}=\lambda\mathbf{v}$ we solved. The clean way to reduce it: substitute $\mathbf{a} = M^{-1/2}\mathbf{u}$ and multiply through by $M^{-1/2}$, giving the *ordinary* symmetric eigenproblem

$$
\big(M^{-1/2} K M^{-1/2}\big)\,\mathbf{u} = \omega^2 \mathbf{u}.
$$

This mass-weighting is why a heavy mass on one spring shifts the mode shapes; the symmetric matrix $M^{-1/2}KM^{-1/2}$ is what actually diagonalizes. For our equal masses $M = mI$, the weighting is trivial and we may divide by $m$ directly. The eigenvalues are $\omega^2$:

$$
\det(K - m\omega^2 I) = \det\begin{pmatrix} 2k - m\omega^2 & -k \\ -k & 2k - m\omega^2 \end{pmatrix}
= (2k - m\omega^2)^2 - k^2 = 0.
$$

So $2k - m\omega^2 = \pm k$, giving the two normal-mode frequencies

$$
\omega_1^2 = \frac{k}{m}, \qquad \omega_2^2 = \frac{3k}{m}.
$$

The eigenvectors are the **mode shapes**. For $\omega_1^2 = k/m$: $(2k - k)a_1 - k a_2 = 0 \Rightarrow a_1 = a_2$ — both carts move *together*, the middle spring never stretches, so it cannot raise the frequency above $\sqrt{k/m}$. For $\omega_2^2 = 3k/m$: $a_1 = -a_2$ — the carts move *oppositely*, stretching the middle spring hard, raising the frequency.

![Two stacked schematics of two equal masses on springs between walls. In mode one the carts are displaced the same way, the middle spring unstretched, at frequency squared k over m. In mode two they are displaced oppositely, stretching the middle spring hard, at frequency squared three k over m.](images/04-vector-spaces-eigenvalues-and-diagonalization-fig-02.png)
*Figure 4.2 — The two normal modes are the eigenvectors of the stiffness matrix: the in-phase mode $(1,1)$ at $\omega^2=k/m$ and the out-of-phase mode $(1,-1)$ at $\omega^2=3k/m$.* Every motion of the system is a superposition $\mathbf{x}(t) = c_1 \mathbf{v}_1 \cos\omega_1 t + c_2 \mathbf{v}_2 \cos\omega_2 t$. The beats we saw at the start are just two pure tones of slightly different frequency interfering. Diagonalizing $K$ *is* the change to normal coordinates that makes the carts independent — the eigenvectors are the coordinates in which the physics is simple.

---

## 6. Where it generalizes

The same three steps — write the matrix, solve $\det(A - \lambda I) = 0$, find the eigenvectors — recur across upper-division physics, and the deep point is that they are *one* problem wearing different clothes:

- **Quantum mechanics.** The time-independent Schrödinger equation $\hat{H}|\psi\rangle = E|\psi\rangle$ is an eigenvalue problem: energies are eigenvalues, stationary states are eigenvectors. A two-state atom is the $2 \times 2$ Hermitian case of Example 2 verbatim; avoided crossings (the ammonia maser, neutrino oscillations) are eigenvalue repulsion of a $2\times2$ Hermitian matrix. Chapter 5 promotes the matrices to operators on infinite-dimensional spaces, but the algebra survives intact.
- **Classical mechanics.** The moment-of-inertia tensor is real symmetric; diagonalizing it yields the principal axes (eigenvectors) and principal moments (eigenvalues) — a body spins cleanly only about a principal axis. The Hessian of a potential decides the stability of an equilibrium through the signs of its eigenvalues.
- **Optics.** Jones eigenpolarizations (Example 3) generalize to any sequence of optical elements multiplied together; the system's eigenpolarizations are the states it transmits unchanged up to phase.
- **The infinite-dimensional sequel.** When the "vectors" are functions and the "matrix" is a differential operator, the eigenvalue problem becomes Sturm–Liouville theory (Chapter 7), and the orthogonality of eigenvectors for distinct eigenvalues — which we proved here in two lines — becomes the orthogonality of Legendre polynomials, spherical harmonics, and Bessel functions. The finite-dimensional spectral theorem of this chapter is the warm-up for all of it.

A computer algebra system will hand you eigenvalues and eigenvectors in a heartbeat. What it will not do is recognize that the coupled carts and the two-state atom are the *same* eigenvalue problem, choose the basis that makes the physics transparent, or use "this matrix is Hermitian, so its eigenvalues must be real" as a check on its own arithmetic. That judgment is the chapter's real content.

---

## Exercises

1. **(Computation.)** Find the eigenvalues and normalized eigenvectors of $A = \left[\begin{smallmatrix} 3 & 1 \\ 1 & 3 \end{smallmatrix}\right]$. Verify the eigenvectors are orthogonal and that $\det A$ equals the product of the eigenvalues.

2. **(Complex eigenvalues.)** Show that the rotation matrix $R(\theta) = \left[\begin{smallmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{smallmatrix}\right]$ has eigenvalues $e^{\pm i\theta}$ and no real eigenvectors for $0 < \theta < \pi$. Explain geometrically why a rotation has no real invariant direction, and why this does not contradict the spectral theorem.

3. **(Derivation — required.)** Prove that the eigenvectors of a real symmetric matrix belonging to two *distinct* eigenvalues are orthogonal, computing $\mathbf{v}_2^T A \mathbf{v}_1$ two ways. Then state precisely where the argument uses $A^T = A$ and where it uses $\lambda_1 \neq \lambda_2$.

4. **(Normal modes.)** Three equal masses are connected in a line by four identical springs (the outer two anchored to walls). Write the $3\times3$ stiffness matrix $K$, find the three normal-mode frequencies, and sketch the three mode shapes. Which mode has the lowest frequency, and why?

5. **(Hermitian vs. symmetric.)** Show that $\sigma_y$ in Example 2 is Hermitian but not symmetric, and that its eigenvalues are nonetheless real. Construct a complex symmetric matrix whose eigenvalues are *not* real, demonstrating that over $\mathbb{C}$ it is Hermiticity, not symmetry, that guarantees a real spectrum.

---

## Sources

- Cayley, A. "A Memoir on the Theory of Matrices." *Philosophical Transactions of the Royal Society of London* **148**, 17–37 (1858). [The founding paper of matrix algebra; states the Cayley–Hamilton theorem, proved generally only later.]
- Cauchy, A.-L. *Exercices de mathématiques* **4** (1829), pp. 174–195. [Real eigenvalues and orthogonal principal axes of symmetric quadratic forms — the seed of the spectral theorem, via the "secular equation" of celestial mechanics. Pagination confirmed (Hawkins, "Cauchy and the spectral theory of matrices," *Hist. Math.* 2, 1975).]
- Sylvester, J. J. Papers on matrices and invariants (1850s). [Coined "matrix"; the law of inertia for quadratic forms.] See Higham, N. J., "Cayley, Sylvester, and Early Matrix Theory," *Linear Algebra and its Applications* **428**, 39–43 (2008).
- Jones, R. C. "A New Calculus for the Treatment of Optical Systems." *Journal of the Optical Society of America* **31**, 488–493 (1941). [First paper of the Jones-calculus series; polarization states as $\mathbb{C}^2$ vectors, optical elements as $2\times2$ matrices.]
- Rayleigh, Lord (J. W. Strutt). *The Theory of Sound*, Vol. 1 (Macmillan, 1877). [Small oscillations of coupled systems as the classical origin of normal modes as a (generalized) eigenvalue problem.]
- Hilbert, D. "Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen" (1904), where "eigenvalue" terminology (*Eigenwert*, *Eigenfunktion*) was introduced and popularized. [CONFIRMED — terms appear in Hilbert's first 1904 communication on integral equations and were rapidly adopted in the German literature.]
- Serbin, K., and M. Wawro. "Student interpretations of eigenequations in linear algebra and quantum mechanics." *International Journal of Research in Undergraduate Mathematics Education* (2024). [Documents that students treat $A\mathbf v=\lambda\mathbf v$ and $\hat H|\psi\rangle=E|\psi\rangle$ as unrelated — the cross-context blindness this chapter is built to attack. *verify volume/pages.*] <!-- FACT-CHECK FLAG: UNVERIFIED — volume/pages not confirmed via authoritative venue. See factchecks/04-vector-spaces-eigenvalues-and-diagonalization-assertions.md -->
