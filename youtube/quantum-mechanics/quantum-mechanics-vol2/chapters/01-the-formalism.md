# Chapter 1 — The Formalism: Hilbert Space, Dirac Notation, and Operators

The wave function $\psi(x)$ gives the probability amplitude for finding a particle at position $x$. Its Fourier transform $\tilde{\psi}(p)$ gives the probability amplitude for finding that same particle with momentum $p$. Both functions carry exactly the same physical information — each is a complete description of the quantum state — and yet they can look entirely different from one another. One might be sharply peaked while the other spreads out and oscillates. A Gaussian in position stays Gaussian in momentum, but a step function in position becomes a sinc function in momentum.

Neither representation deserves to be called "the state" in any privileged sense. The wave function $\psi(x)$ is not the state itself. It is what the state looks like when we describe it in one particular basis. The Fourier transform $\tilde{\psi}(p)$ is what that same state looks like in a different basis. The state — the genuine physical object — sits above both descriptions at once. Compare it to a vector in ordinary three-dimensional space: its numerical coordinates differ between Cartesian and spherical systems, but the vector itself does not budge when we switch coordinate systems.

So far, every calculation in wave mechanics has been carried out in a single basis, usually position. The formalism we develop in this chapter lets us write the physics once, in basis-free language, and then evaluate it in whatever basis happens to be convenient.

![State vector projecting onto three distinct bases: position-space wave function, momentum-space wave function, and energy-basis coefficients](../images/01-the-formalism-fig-01.png)
*Figure 1.1 — A single abstract state vector projects onto three different bases, yielding three different-looking but informationally equivalent representations.*

---

## The Arena

A **Hilbert space** $\mathcal{H}$ is a complete complex inner-product space. The two words that carry the weight are *complex* and *inner product*. In such a space we can add vectors, scale them by complex numbers, and compute inner products. That is the whole structure, and we will not need more.

The word *complex* is doing real work. We can multiply a state by any $c \in \mathbb{C}$ and it remains a valid state. The inner product is **sesquilinear**, which means it is linear in the second argument but conjugate-linear in the first:

$$\langle(a|\phi_1\rangle + b|\phi_2\rangle)|\psi\rangle = a^*\langle\phi_1|\psi\rangle + b^*\langle\phi_2|\psi\rangle.$$

It is also conjugate-symmetric rather than symmetric:

$$\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*.$$

Exchanging the bra and the ket conjugates the answer. In a real vector space the inner product is symmetric and we may swap the two factors freely; in a Hilbert space we cannot. That conjugate sign is the quiet source of countless errors in adjoint calculations and confused steps in Hermiticity proofs, so it pays to learn it thoroughly.

The dimension can be finite or infinite. A qubit lives in $\mathbb{C}^2$. The states of a particle moving along a line live in $L^2(\mathbb{R})$, the space of square-integrable complex functions. The same abstract framework covers both cases without any change.

---

## Kets, Bras, and What They Are

Dirac's notation has the useful property of keeping the different categories of object plainly visible.

A **ket** $|\psi\rangle$ is a vector in $\mathcal{H}$. It is helpful to picture it as a column vector.

A **bra** $\langle\phi|$ is a linear functional on $\mathcal{H}$ — a rule that sends any ket to a complex number. Each ket $|\phi\rangle$ comes paired with a bra $\langle\phi|$, defined by $\langle\phi|: |\psi\rangle \mapsto \langle\phi|\psi\rangle$. It is helpful to picture this as a row vector, the conjugate transpose of the column.

The bra paired with $c|\phi\rangle$ is $c^*\langle\phi|$. That complex conjugate is not an extra rule we have to remember; it follows directly from the definition of the inner product.

The bracket $\langle\phi|\psi\rangle$ is a **scalar**, an ordinary complex number. Written in the opposite order, $|\psi\rangle\langle\phi|$ is an **operator** — the rule that sends any $|\chi\rangle$ to $\langle\phi|\chi\rangle\,|\psi\rangle$. Inner product gives a scalar; outer product gives an operator. These belong to genuinely different categories, and an expression that confuses one for the other is wrong in two ways at the same time.

---

## Three Identities

Choose an orthonormal basis $\{|n\rangle\}$ for $\mathcal{H}$. Three identities then carry us through nearly everything.

**Completeness:**
$$\sum_n |n\rangle\langle n| = \hat{I}.$$

This is nothing more than the number 1, dressed up as an operator. In the continuous position basis it becomes an integral: $\int |x\rangle\langle x|\,dx = \hat{I}$.

**Orthonormality:**
$$\langle m|n\rangle = \delta_{mn}.$$

In the position basis: $\langle x|x'\rangle = \delta(x-x')$.

**Expansion:**
$$|\psi\rangle = \sum_n c_n|n\rangle, \qquad c_n = \langle n|\psi\rangle.$$

The coefficient $c_n$ is the projection of the abstract vector onto the $n$-th basis direction. Switch to a different basis and the numbers change, but the vector itself stays put.

Completeness is the workhorse of the three. Slipping the identity $\hat{I}$ between any two expressions turns abstract inner products into concrete sums or integrals:

$$\langle\phi|\psi\rangle = \langle\phi|\hat{I}|\psi\rangle = \sum_n \langle\phi|n\rangle\langle n|\psi\rangle = \sum_n \phi_n^* \psi_n.$$

In the position basis this reads $\int\phi^*(x)\psi(x)\,dx$. So the abstract inner product and the familiar wave-function overlap integral are simply two faces of the same quantity.

![Three-stage diagram: abstract inner product with a gap, the identity operator inserted as a sum of projectors, and the resulting chain of paired inner products](../images/01-the-formalism-fig-02.png)
*Figure 1.2 — The completeness insertion technique: inserting the identity as a sum of projectors converts an abstract inner product into a concrete sum of overlap amplitudes.*

---

## The Fourier Transform Is a Basis Change

The quantum state of a particle on a line is a unit vector $|\psi\rangle$ in $L^2(\mathbb{R})$. Two convenient bases are the position eigenstates $\{|x\rangle\}$ and the momentum eigenstates $\{|p\rangle\}$.

The position-space wave function is $\psi(x) = \langle x|\psi\rangle$.

The momentum-space wave function is $\tilde{\psi}(p) = \langle p|\psi\rangle$.

These are two representations of one and the same vector — a single state seen in two different bases.

Now insert the position completeness relation into $\tilde{\psi}(p)$:

$$\tilde{\psi}(p) = \langle p|\psi\rangle = \int\langle p|x\rangle\langle x|\psi\rangle\,dx = \int\langle p|x\rangle\,\psi(x)\,dx.$$

All that remains is to identify $\langle p|x\rangle$. The momentum eigenstate, written in position space, obeys $\hat{p}|p\rangle = p|p\rangle$, that is, $-i\hbar\,\partial_x\langle x|p\rangle = p\langle x|p\rangle$, which gives $\langle x|p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$. Hence $\langle p|x\rangle = e^{-ipx/\hbar}/\sqrt{2\pi\hbar}$, and:

$$\tilde{\psi}(p) = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx.$$

This is the Fourier transform. We did not have to borrow it from analysis; it dropped out of the completeness relation together with one differential equation. Whenever a Fourier transform shows up in quantum mechanics, what we are really watching is a change of basis.

The position and momentum representations hold exactly the same physics. Neither one is more fundamental than the other. We simply work in whichever one makes the calculation easier.

---

## Operators: Abstract Maps, Not Matrices

A **linear operator** $\hat{A}$ is a linear map $\mathcal{H} \to \mathcal{H}$. It exists on its own, with no reference to any basis.

Once we pick a basis $\{|n\rangle\}$, the operator acquires a matrix representation:

$$A_{mn} = \langle m|\hat{A}|n\rangle.$$

A different basis yields a different matrix, but the operator is the same operator. This is the central distinction of the chapter.

The position operator $\hat{x}$ makes the point cleanly. In the position basis, $\hat{x}$ acts by multiplication, so its matrix is diagonal. In the energy basis of the harmonic oscillator, the very same operator $\hat{x}$ has tridiagonal matrix elements involving $\sqrt{n}$. One operator, two matrices that look nothing alike. The matrices are byproducts of the basis we chose; the operator is not.

![Central operator object connected by branch arrows to a diagonal matrix (position basis) on the left and a tridiagonal matrix (energy basis) on the right, with a bidirectional arc connecting the two matrices](../images/01-the-formalism-fig-03.png)
*Figure 1.3 — The same operator yields a diagonal matrix in one basis and a tridiagonal matrix in another; the operator itself is basis-independent.*

The **adjoint** $\hat{A}^\dagger$ is defined by:

$$\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle \quad \text{for all }|\psi\rangle, |\phi\rangle.$$

In matrix form, $(A^\dagger)_{mn} = A_{nm}^*$ — the conjugate transpose. An operator is **Hermitian** when $\hat{A}^\dagger = \hat{A}$, that is, when $A_{mn} = A_{nm}^*$. A worthwhile example to keep in mind is $\sigma_y = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$. Its plain transpose is $\bigl(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\bigr) = -\sigma_y$, which is antisymmetric. But its conjugate transpose is $+\sigma_y$, which is Hermitian. The factor of $i$ is what makes the difference. A matrix can carry complex off-diagonal entries and still be Hermitian, provided $A_{12} = A_{21}^*$. The slogan "Hermitian means symmetric" is a habit carried over from real linear algebra, and in the complex case it simply does not hold.

The adjoint reverses the order of a product: $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger\hat{A}^\dagger$. The proof is a single line from the definition, but the rule is essential whenever we manipulate products of operators.

Changing basis from $\{|a_n\rangle\}$ to $\{|b_m\rangle\}$ is carried out by the unitary matrix $U_{mn} = \langle a_m|b_n\rangle$, which transforms operator matrices as $O' = U^\dagger O U$. The eigenvalues of $O'$ match those of $O$ exactly. The physics is basis-independent. The matrix is the observer's description; the operator is the thing being described.

---

## Worked Example — A State in the Energy Basis

Suppose a particle sits in an infinite square well of width $L$, prepared in the state

$$\psi(x) = \sqrt{\frac{30}{L^5}}\,x(L-x), \qquad 0 < x < L.$$

The energy eigenstates are $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ with eigenvalues $E_n = n^2 E_1$, where $E_1 = \pi^2\hbar^2/(2mL^2)$. We will compute $\langle\hat{H}\rangle$ by two different routes and watch them agree.

**Energy basis route.** The expansion coefficients are $c_n = \langle E_n|\psi\rangle = \int_0^L\psi_n^*(x)\psi(x)\,dx$. Using the standard integral $\int_0^L x(L-x)\sin(n\pi x/L)\,dx = 2L^3/(n^3\pi^3)\cdot[1-(-1)^n]$, which vanishes for even $n$:

$$c_n = \frac{4\sqrt{60}}{n^3\pi^3} \quad (n \text{ odd}), \qquad c_n = 0 \quad (n \text{ even}).$$

Check normalization: $\sum_{n\,\text{odd}}|c_n|^2 = 960/\pi^6 \cdot \sum_{n\,\text{odd}}1/n^6$. The sum $\sum_{n\,\text{odd}}1/n^6 = \pi^6/960$, so $\sum|c_n|^2 = 1$.

![Bar chart with bars at odd quantum numbers n = 1, 3, 5, 7, 9; the n=1 bar nearly reaches probability 1 while all others are negligible stubs](../images/01-the-formalism-fig-04.png)
*Figure 1.4 — Energy-basis probability distribution for the parabolic state: the ground state carries essentially all the probability, with higher odd modes contributing negligibly.*

In the energy basis $\hat{H}$ is diagonal, so:

$$\langle\hat{H}\rangle = \sum_{n\,\text{odd}}|c_n|^2 E_n = \frac{960 E_1}{\pi^6}\sum_{n\,\text{odd}}\frac{1}{n^4} = \frac{960 E_1}{\pi^6}\cdot\frac{\pi^4}{96} = \frac{10 E_1}{\pi^2} = \frac{5\hbar^2}{mL^2}.$$

**Position basis route.** With $\hat{H} = -(\hbar^2/2m)\partial_x^2$ and $\partial_x^2\psi = -2\sqrt{30/L^5}$:

$$\langle\hat{H}\rangle = \frac{\hbar^2}{m}\sqrt{\frac{30}{L^5}}\int_0^L x(L-x)\,dx\cdot\sqrt{\frac{30}{L^5}} = \frac{60\hbar^2}{mL^5}\cdot\frac{L^3}{6} = \frac{10\hbar^2}{mL^2}\cdot\frac{1}{2} = \frac{5\hbar^2}{mL^2}.$$

The two routes give the same number, as they must: the expectation value does not depend on the basis. In the energy basis the work is a weighted discrete sum; in the position basis it is two derivatives and an integral. Both arrive at the same answer, and that is exactly what it means for the operator to exist independently of any basis.

One limitation is worth naming. This calculation leaned on knowing the eigenstates $\psi_n(x)$ in closed form. For a more complicated potential, where the eigenstates cannot be written down analytically, the energy-basis route is no longer available to us. The abstract formalism remains exact; whether we can actually compute with it depends on whether we have a usable basis in hand.

---

## References

- Dirac, P.A.M. *The Principles of Quantum Mechanics*, 4th ed. Oxford University Press, 1958.
- von Neumann, J. *Mathematical Foundations of Quantum Mechanics*. Princeton University Press, 1955.
- Townsend, J.S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012, §§1.1–1.5.
- Sakurai, J.J. and Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2021, §§1.2–1.3.
- Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. Springer, 1994, Ch. 1.
- Griffiths, D.J. and Schroeter, D.F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018, §3.1.
- Cataloglu, E. and Robinett, R.W. "Testing the development of student conceptual and visualization understanding in quantum mechanics." *American Journal of Physics* 70, 238 (2002). https://doi.org/10.1119/1.1430386
- Singh, C. and Marshman, E. "Review of student difficulties in upper-level quantum mechanics." *Physical Review Special Topics — Physics Education Research* 11, 020117 (2015). https://doi.org/10.1103/PhysRevSTPER.11.020117

