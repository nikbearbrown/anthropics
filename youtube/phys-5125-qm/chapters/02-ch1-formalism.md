# Chapter 1 — The Formalism of Quantum Mechanics

*Linear algebra in a physicist's costume: vectors that are states, matrices that are measurements.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Strip away the physical names and this chapter is plain linear algebra. A quantum state is a vector in a complex inner-product space — a Hilbert space — and Dirac's bra–ket notation is just bookkeeping for column vectors, row vectors, and the inner products between them. Every measurable quantity is a Hermitian operator, i.e. a matrix that equals its own conjugate transpose. The physics enters through a short list of demands placed on this machinery, and the rest follows mechanically.

What does the formalism optimize for? Consistency between two requirements: measurement outcomes must be real numbers, and total probability must stay fixed at one. Hermiticity guarantees real eigenvalues and an orthonormal eigenbasis; unitary evolution preserves the norm. Diagonalize an operator and you simultaneously read off the possible measured values (eigenvalues) and the states that yield them with certainty (eigenvectors).

The trade-off is sharp. Because non-commuting operators share no common eigenbasis, you cannot make every observable definite at once — the uncertainty relation $\sigma_A \sigma_B \geq |\langle[\hat{A},\hat{B}]\rangle/2i|$ is a theorem, not an assumption. The same commutator algebra that constrains position and momentum also generates angular momentum and forces its eigenvalues onto a discrete ladder. The lesson worth holding onto: nearly everything here is one algebraic structure, eigenvalue problems and commutators, wearing physical clothing.

## 1. Review: The Formalism of quantum mechanics

## 1.1 Hilbert spaces and Dirac notation

In cartesian coordinates, any vector is written as a sum of unit vectors that make up an orthogonal basis

$$\vec{v} = v_1 \hat{e}_1 + v_2 \hat{e}_2 + v_3 \hat{e}_3$$

where

$$\hat{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \hat{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \hat{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

The coefficients $v_i$ may in general be real or complex; here we keep them real for the moment. By the definition of the inner ("dot") product, $(\vec{u}, \vec{v}) = \vec{u} \cdot \vec{v} = |u||v| \cos\theta$

$$(\hat{e}_i, \hat{e}_j) = \hat{e}_i \cdot \hat{e}_j = \delta_{ij} \quad \text{(they are orthogonal)}$$

$$(\vec{v}, \hat{e}_i) = \vec{v} \cdot \hat{e}_i = v_i \quad \text{(projection along } \hat{e}_i\text{)}$$

$$(\vec{v}, \vec{v}) = \vec{v} \cdot \vec{v} = \sum_i v_i^2 > 0$$

The norm is defined as $v = \sqrt{|\vec{v}|^2} = \sqrt{(\vec{v}, \vec{v})}$

**Hilbert space:**

- the coefficients are complex numbers
- It can have infinite dimensions / basis vectors

$$(\vec{u}, \vec{v}) = \sum_i u_i^* v_i$$

$$(\vec{v}, \vec{u}) = (\vec{u}, \vec{v})^* \quad \Rightarrow \quad (\vec{u}, \vec{u}) \text{ is real!}$$

$$\Rightarrow \quad |\vec{u}| = \sqrt{(\vec{u}, \vec{u})} \in \mathbb{R} \geq 0$$

**Dirac notation:**

- A system's state is completely specified by its **state vector** $|\psi\rangle \in \mathcal{H}$

- State vectors are acted on, and transformed, by linear operators

$$|\psi\rangle = \sum_i \psi_i |\alpha_i\rangle \quad \Rightarrow \quad |\psi\rangle = \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix}$$

$d$: dimension of $\mathcal{H}$

$$|\alpha_1\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix}; \quad |\alpha_2\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}; \quad \cdots \quad |\alpha_d\rangle = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}$$

$|\alpha_i\rangle$ form an orthonormal basis

**Example:** two-level system $(d = 2)$

$$|1\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}; \quad |2\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

An arbitrary state is then written as

$$|\psi\rangle = \psi_1 |1\rangle + \psi_2 |2\rangle = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$$

with $\psi_1, \psi_2 \in \mathbb{C}$

A Hilbert space is a vector space, so any linear combination of states is again a member of $\mathcal{H}$

$$\alpha |\phi\rangle + \beta |\psi\rangle \in \mathcal{H}$$

**"Dual" Hilbert space**

$$|\psi\rangle = \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix} \quad \rightarrow \quad \langle\psi| = \begin{pmatrix} \psi_1^*, \psi_2^*, \ldots, \psi_d^* \end{pmatrix}$$

Algebraically, $|\psi\rangle$ is a column vector,

while $\langle\psi|$ is the row vector obtained as its conjugate transpose

**Inner product:**

$$\langle\psi|\varphi\rangle = \sum_{i=1}^{d} \psi_i^* \varphi_i = \begin{pmatrix} \psi_1^* \cdots \psi_d^* \end{pmatrix} \begin{pmatrix} \varphi_1 \\ \varphi_2 \\ \vdots \\ \varphi_d \end{pmatrix} \in \mathbb{C}$$

$\langle\psi|$ is the "bra" and $|\varphi\rangle$ is the "ket", $\langle\psi|\varphi\rangle$ is a "braket".

The coefficients $\psi_i$ now have a clear meaning:

$$\langle\alpha_i|\psi\rangle = \langle\alpha_i|\left(\sum_j \psi_j |\alpha_j\rangle\right)$$

$$= \sum_j \psi_j \langle\alpha_i|\alpha_j\rangle = \sum_j \psi_j \delta_{ij} = \psi_i$$

that is, the "projection" of $|\psi\rangle$ onto the "$i$-th direction", equivalently the $i$-th component of $|\psi\rangle$

The norm of $|\psi\rangle$ is $\sqrt{\langle\psi|\psi\rangle} = \sqrt{\sum_i \psi_i^* \psi_i} = \sqrt{\sum_i |\psi_i|^2}$

**Completeness**

$$\sum_{i=1}^{d} |\alpha_i\rangle\langle\alpha_i| = \mathbb{1} \quad \text{(identity operator)}$$

$$\left(\sum_i |\alpha_i\rangle\langle\alpha_i|\right)\left(\underbrace{\sum_j \psi_j |\alpha_j\rangle}_{|\psi\rangle}\right) = \sum_{ij} \psi_j |\alpha_i\rangle \underbrace{\langle\alpha_i|\alpha_j\rangle}_{\delta_{ij}} = |\psi\rangle$$

**Continuous Hilbert spaces**

Now let the index "$i$" run over a continuum, like a coordinate along the $x$-axis. We label the basis by $|x\rangle$ and express a state as

$$|\psi\rangle = \int dx\, \psi(x) |x\rangle$$

The inner product, or braket, becomes

$$\langle\psi|\varphi\rangle = \left(\int dx_1\, \psi^*(x_1) \langle x_1|\right)\left(\int dx_2\, \varphi(x_2) |x_2\rangle\right)$$

$$= \int dx_1\, dx_2\, \psi^*(x_1)\varphi(x_2) \underbrace{\langle x_1|x_2\rangle}_{\delta(x_1 - x_2)}$$

$$= \int dx\, \psi^*(x)\varphi(x)$$

The identity is now written

$$\int dx\, |x\rangle\langle x| = \mathbb{1}$$

## 1.2 Observables and operators

An operator is a mathematical map that sends one state to another

$$\hat{O}|\psi\rangle = |\varphi\rangle \quad ; \quad |\psi\rangle, |\varphi\rangle \in \mathcal{H}$$

It admits a matrix representation. In the basis $|\alpha\rangle$, the matrix elements of $\hat{O}$ are defined by

$$O_{ij} = \langle\alpha_i|\hat{O}|\alpha_j\rangle$$

$$\rightarrow \quad \langle\alpha_i|\hat{O}|\psi\rangle = \sum_j \langle\alpha_i|\hat{O}|\alpha_j\rangle\langle\alpha_j|\psi\rangle$$

$$= \sum_j O_{ij}\, \psi_j = \langle\alpha_i|\varphi\rangle = \varphi_i$$

$$\rightarrow \quad \begin{pmatrix} \varphi_1 \\ \varphi_2 \\ \vdots \\ \varphi_d \end{pmatrix} = \begin{pmatrix} O_{11} & O_{12} & \cdots & O_{1d} \\ O_{21} & O_{22} & & \vdots \\ \vdots & & \ddots & \\ O_{d1} & \cdots & & O_{dd} \end{pmatrix} \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix}$$

**Example:** two-level system $|1\rangle; |2\rangle$

Define the "occupation operators"

$$\hat{N}_1 = |1\rangle\langle 1| \quad ; \quad \hat{N}_2 = |2\rangle\langle 2|$$

$$\hat{N}_1\left(\psi_1 |1\rangle + \psi_2 |2\rangle\right) = \psi_1 |1\rangle \underbrace{\langle 1|1\rangle}_{=1} + \psi_2 |1\rangle \underbrace{\langle 1|2\rangle}_{=0}$$

$$= \psi_1 |1\rangle$$

Similarly, $\hat{N}_2|\psi\rangle = \psi_2 |2\rangle$

Notice that $\hat{N}_1 + \hat{N}_2 = \mathbb{1}$

**Matrices:** $\langle 1|\hat{N}_1|1\rangle = 1$ ; $\langle 2|\hat{N}_1|2\rangle = 0$
$\langle 1|\hat{N}_1|2\rangle = 0$

$$N_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}; \quad N_2 = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}; \quad N_1 + N_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

**"Transition operators":** $S^+ = |2\rangle\langle 1|$ ; $S^- = |1\rangle\langle 2|$

$$\rightarrow \quad S^+|1\rangle = |2\rangle \quad ; \quad S^+|2\rangle = 0$$

$$S^-|2\rangle = |1\rangle \quad ; \quad S^-|1\rangle = 0$$

$$S^+|\psi\rangle = \psi_1 |2\rangle$$

**Matrices**

$$S^+ = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}; \quad S^- = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$

The same ideas carry over to continuous Hilbert spaces

$$\langle\psi|\hat{O}|\varphi\rangle = \langle\psi|\left(\hat{O}|\varphi\rangle\right) = \int dx\, \psi^*(x)\, \hat{O}\, \varphi(x)$$

**Expectation values:**

Operators stand for physical observables that an instrument can measure. For a state $|\psi\rangle$, the expectation value of $\hat{O}$ is

$$\langle\hat{O}\rangle = \langle\psi|\hat{O}|\psi\rangle =$$

$$= \sum_{ij} \psi_i^* \psi_j \langle\alpha_i|\hat{O}|\alpha_j\rangle$$

$$= \sum_{ij} \psi_i^* \psi_j\, O_{ij}$$

or $\quad \langle\hat{O}\rangle = \int dx\, \psi^*(x)\, O\, \psi(x)$

Because a measurement must yield a real number, we require $\langle O \rangle \in \mathbb{R}$ for every state $|\psi\rangle$. Equivalently:

$$\langle\hat{O}\rangle^* = \langle\psi|\hat{O}|\psi\rangle^* = \langle O\psi|\psi\rangle = \langle O \rangle$$

Operators that satisfy this condition are called **Hermitian**.

An operator $\hat{O}$ is Hermitian when it coincides with its Hermitian conjugate, $\hat{O} = \hat{O}^\dagger$, that is

$$\langle\alpha_i|\hat{O}|\alpha_j\rangle = \langle\alpha_j|\hat{O}|\alpha_i\rangle^*$$

$$\rightarrow \quad O_{ij} = (O_{ji})^* = (O^\dagger)_{ij}$$

**END LECT #1**

**Example:** two-level system

$S^+, S^-$ are **not** Hermitian, so neither can represent an observable.

The combinations $N_1, N_2, (S^+ + S^-), i(S^+ - S^-)$, on the other hand, are.

## 1.3 Change of basis (rotations)

Suppose a state is expressed in a basis $|\alpha\rangle$ as

$$|\psi\rangle = \sum_\alpha \psi_\alpha |\alpha\rangle$$

inserting a resolution of the identity gives

$$|\psi\rangle = \sum_\alpha \psi_\alpha \sum_\beta |\beta\rangle\langle\beta|\alpha\rangle$$

$$= \sum_\beta \left(\sum_\alpha \langle\beta|\alpha\rangle \psi_\alpha\right) |\beta\rangle$$

$$= \sum_\beta \left(\sum_\alpha \langle\beta|\alpha\rangle\langle\alpha|\psi\rangle\right) |\beta\rangle$$

$$= \sum_\beta \langle\beta|\psi\rangle |\beta\rangle = \sum_\beta \psi_\beta |\beta\rangle$$

with $\psi_\beta = \langle\beta|\psi\rangle = \sum_\alpha U_{\alpha\beta}^* \psi_\alpha$, having defined the transformation $U_{\alpha\beta} = \langle\alpha|\beta\rangle$. These are the projections of the $|\alpha\rangle$ states onto the $|\beta\rangle$ basis.

$$\rightarrow \quad \psi_\beta = \langle\beta|\psi\rangle = \sum_\alpha (U^\dagger)_{\beta\alpha} \psi_\alpha; \quad \psi_\alpha = \sum_\beta U_{\alpha\beta} \psi_\beta$$

$U_{\alpha\beta}$ is a unitary transformation

$$U^\dagger U = \mathbb{1} \quad \Rightarrow \quad U^\dagger = U^{-1}$$

**Matrices:**

$$\langle\beta|O|\beta'\rangle = \sum_{\alpha\alpha'} \langle\beta|\alpha\rangle\langle\alpha|O|\alpha'\rangle\langle\alpha'|\beta'\rangle$$

$$= \sum_{\alpha\alpha'} U_{\alpha\beta}^*\, U_{\alpha'\beta'}\, O_{\alpha\alpha'}$$

$$O' = U^\dagger O U \quad ; \quad O = U O' U^\dagger$$

**Example:** 2-level system

$$|\pm\rangle = \frac{1}{\sqrt{2}}\left[|1\rangle \pm |2\rangle\right] \rightarrow \begin{cases} |+\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle) \\ |-\rangle = \frac{1}{\sqrt{2}}(|1\rangle - |2\rangle) \end{cases}$$

$$U_{+1} = \frac{1}{\sqrt{2}}, \quad U_{+2} = \frac{1}{\sqrt{2}}, \quad U_{-1} = \frac{1}{\sqrt{2}}, \quad U_{-2} = -\frac{1}{\sqrt{2}}$$

$$\rightarrow \quad U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \qquad \psi = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}$$

$$\rightarrow \quad \psi' = \frac{1}{\sqrt{2}} \begin{pmatrix} \psi_1 + \psi_2 \\ \psi_1 - \psi_2 \end{pmatrix}$$

or, $|\psi\rangle = \psi_1 |1\rangle + \psi_2 |2\rangle = \frac{1}{\sqrt{2}}\left\{\psi_1(|+\rangle + |-\rangle) + \psi_2(|+\rangle - |-\rangle)\right\}$

$$= \frac{1}{\sqrt{2}}(\psi_1 + \psi_2)|+\rangle + \frac{1}{\sqrt{2}}(\psi_1 - \psi_2)|-\rangle = \psi_+ |+\rangle + \psi_- |-\rangle$$

## 1.4 The eigenvalue problem

Given an operator $\hat{O}$, its eigenstates are the states that $\hat{O}$ leaves unchanged apart from an overall scaling:

$$\hat{O}|\psi\rangle = \lambda |\psi\rangle \quad ; \quad \lambda \text{ is a scalar}$$

$|\psi\rangle$: eigenstate ; $\lambda$ is the associated eigenvalue

Rearranging this gives

$$(\hat{O} - \lambda \mathbb{1})|\psi\rangle = 0$$

In matrix form this reads

$$\begin{pmatrix} O_{11} - \lambda & O_{12} & O_{13} & \cdots & O_{1d} \\ O_{21} & O_{22} - \lambda & O_{23} & \cdots & O_{2d} \\ \vdots & O_{32} & \ddots & & \\ O_{d1} & \cdots & & & O_{dd} - \lambda \end{pmatrix} \begin{pmatrix} \psi_1 \\ \psi_2 \\ \vdots \\ \psi_d \end{pmatrix} = 0$$

A non-trivial solution exists only if

$$\det(O - \lambda \mathbb{1}) = 0$$

This secular equation for $\lambda$ produces a set of solutions $\lambda_i$. With the eigenvalues in hand, the matching eigenvectors (eigenstates) follow.

**Eigenvalues of Hermitian operators:**

(i) The eigenvalues of Hermitian operators are **real**

$$\hat{O}|\psi\rangle = \lambda |\psi\rangle$$

$$\rightarrow \quad \langle\psi|\hat{O}\psi\rangle = \lambda \langle\psi|\psi\rangle$$

$$\langle O\psi|\psi\rangle = \lambda^* \langle\psi|\psi\rangle$$

But $\langle\psi|O\psi\rangle = \langle O\psi|\psi\rangle \Rightarrow \lambda = \lambda^* \in \mathbb{R}$

(ii) Two eigenstates $|\psi_1\rangle; |\psi_2\rangle$ associated to different eigenvalues $\lambda_1 \neq \lambda_2$ are **orthogonal**

$$\hat{O}|\psi_1\rangle = \lambda_1 |\psi_1\rangle \quad ; \quad \hat{O}|\psi_2\rangle = \lambda_2 |\psi_2\rangle$$

$$\langle\psi_2|\hat{O}|\psi_1\rangle = \lambda_1 \langle\psi_2|\psi_1\rangle; \quad \langle\psi_1|\hat{O}|\psi_2\rangle = \lambda_2 \langle\psi_1|\psi_2\rangle \quad (1)$$

$$\langle\psi_1|\hat{O}|\psi_2\rangle^* = \lambda_1 \langle\psi_1|\psi_2\rangle^*$$

$$\rightarrow \quad \langle\psi_1|\hat{O}|\psi_2\rangle = \lambda_1 \langle\psi_1|\psi_2\rangle \quad (2)$$

From (1) and (2) ; $\lambda_1 \langle\psi_1|\psi_2\rangle = \lambda_2 \langle\psi_1|\psi_2\rangle$

Since $\lambda_1 \neq \lambda_2 \rightarrow \langle\psi_1|\psi_2\rangle = 0$

And if $\lambda_1 = \lambda_2$ (degeneracy)? Within that subspace one can always choose a set of mutually orthogonal eigenvectors.

(iii) The eigenvectors of a Hermitian operator span the complete Hilbert space and form an orthogonal basis.

$$\hat{O}|\psi_i\rangle = \lambda_i |\psi_i\rangle \quad i = 1, 2, \ldots, d$$

**The eigenvalue problem in quantum mechanics**

When a system is prepared in an eigenstate of an operator $\hat{O}$, measuring $\hat{O}$ always returns the same value

$$\langle\psi|\hat{O}|\psi\rangle = \lambda \langle\psi|\psi\rangle$$

**Example:** two-level system

Take the operator $S^+ + S^- = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

$$\det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 \rightarrow \boxed{\lambda_\pm = \pm 1}$$

$\lambda = 1)$

$$\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} \psi_{+1} \\ \psi_{+2} \end{pmatrix} = 0 \rightarrow -\psi_{+1} + \psi_{+2} = 0$$

or $\psi_{+1} = \psi_{+2}$

$$\rightarrow \quad |\psi_+\rangle = \psi_{+1}|1\rangle + \psi_{+1}|2\rangle = \psi_{+1}(|1\rangle + |2\rangle)$$

Imposing the normalization condition $\langle\psi_+|\psi_+\rangle = 1$

$$\rightarrow \quad \langle\psi_+|\psi_+\rangle = |\psi_{+1}|^2 \cdot 2 = 1 \rightarrow \psi_{+1} = \frac{1}{\sqrt{2}}$$

so that $|\psi_+\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle)$

$\lambda = -1)$

$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} \psi_{-1} \\ \psi_{-2} \end{pmatrix} = 0 \rightarrow \psi_{-1} = -\psi_{-2}$$

$$\rightarrow \quad |\psi_-\rangle = \frac{1}{\sqrt{2}}(|1\rangle - |2\rangle)$$

Notice that $\langle\psi_+|\psi_-\rangle = 0$

## 1.5 Statistical interpretation

Measuring a physical observable $O$, represented by a Hermitian operator $\hat{O}$, on a state $|\psi\rangle$ yields an eigenvalue $\lambda_i$ with probability:

$$P(\lambda_i) = |\langle\psi_i|\psi\rangle|^2 = |\psi_i|^2$$

When that outcome occurs, the post-measurement state of the system is $|\psi_i\rangle$

$$\hat{O}|\psi\rangle \;\overset{\text{collapse}}{\longrightarrow}\; |\psi_i\rangle \qquad (O = \lambda_i)$$

The squared coefficients $|\psi_i|^2$ are thus the probabilities of finding the system in each eigenstate

$$\langle O \rangle = \langle\psi|\hat{O}|\psi\rangle = \sum_{ij} \psi_i^* \psi_j \langle\psi_i|\hat{O}|\psi_j\rangle$$

$$= \sum_{ij} \psi_i^* \psi_j\, \lambda_j \langle\psi_i|\psi_j\rangle = \sum_i \lambda_i |\psi_i|^2$$

$$= \sum_i \lambda_i\, P(\lambda_i) \qquad \text{with } \sum_i P(\lambda_i) = 1$$

In the continuum

$$|\psi\rangle = \int dx\, \psi(x) |x\rangle$$

Measuring the position operator gives

$$\hat{x}|\psi\rangle = \int dx\, \psi(x)\, \hat{x}|x\rangle = \int dx\, x\, \psi(x) |x\rangle$$

$$\hat{x}|x\rangle = x|x\rangle$$

$$\langle\psi|\hat{x}|\psi\rangle = \int dx\, dx'\, x\, \psi^*(x')\, \psi(x) \underbrace{\langle x'|x\rangle}_{\delta(x - x')}$$

$$= \int dx\, x\, \underbrace{|\psi(x)|^2}_{P(x)} = \int dx\, x\, P(x)$$

$$\rightarrow \quad P(x) = |\psi(x)|^2$$

The probability of locating the particle within $[x, x+dx]$ is

$$P(x)\, dx = |\psi(x)|^2\, dx$$

## 1.6 The generalized uncertainty principle

Measure the observable $O$ repeatedly and the outcomes spread across a histogram. The spread, and hence the precision, is captured by the standard deviation

$$\sigma_O^2 = \langle(\hat{O} - \langle O \rangle)^2\rangle = \langle\psi|(\hat{O} - \langle O \rangle)^2|\psi\rangle$$

$$= \langle(\hat{O} - \langle O \rangle)\psi\,|\,(\hat{O} - \langle O \rangle)\psi\rangle$$

Now take two observables $\hat{A}$ and $\hat{B}$. Applying the Schwartz inequality yields

$$\sigma_A^2 \sigma_B^2 = \langle(\hat{A} - \langle A \rangle)\psi\,|\,(\hat{A} - \langle A \rangle)\psi\rangle \langle(\hat{B} - \langle B \rangle)\psi\,|\,(\hat{B} - \langle B \rangle)\psi\rangle$$

$$\geq |\langle(\hat{A} - \langle A \rangle)\psi\,|\,(\hat{B} - \langle B \rangle)\psi\rangle|^2$$

A few steps of algebra then lead to the inequality

$$\sigma_A \sigma_B \geq \left|\frac{1}{2i}\langle[\hat{A}, \hat{B}]\rangle\right| \qquad \text{(Townsend 3.5)}$$

with $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$

**END LECTURE #2**

This is a derived result of the theory, not a postulate. It sets the fundamental limit on how precisely two quantities, such as position and momentum, can be measured at once:

$$[\hat{x}, \hat{p}]\,\psi(x) = \left[x, -i\hbar\frac{d}{dx}\right]\psi(x) = -i\hbar\left[x\frac{d}{dx} - \frac{d}{dx}x\right]\psi(x)$$

$$= -i\hbar\left(x\frac{d\psi}{dx} - \psi(x) - x\frac{d\psi}{dx}\right) = i\hbar\,\psi(x)$$

$$\Rightarrow \quad [\hat{x}, \hat{p}] = i\hbar \quad \rightarrow \quad \sigma_x \sigma_p \geq \frac{\hbar}{2}$$

The same relation applies to any pair of non-commuting operators, $[\hat{A}, \hat{B}] \neq 0$

**Operators that commute**

When $[\hat{A}, \hat{B}] = 0$, both can be measured simultaneously to arbitrary precision. They also share a common set of eigenvectors, so one can find eigenvectors of $\hat{A}$ that are simultaneously eigenvectors of $\hat{B}$. This is enormously useful, especially for exploiting symmetries to solve the Schrödinger equation.

**Example:** Two level system

Introduce the following operators

$$\hat{S}_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \frac{\hbar}{2}\left(\hat{S}^+ + \hat{S}^-\right)$$

$$\hat{S}_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \frac{\hbar}{2i}\left(\hat{S}^+ - \hat{S}^-\right)$$

$$\hat{S}_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \frac{\hbar}{2}\left(\hat{N}_1 + \hat{N}_0\right)$$

$$\left[\hat{S}_x, \hat{S}_z\right] = \frac{\hbar^2}{4}\begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} = -i\hbar\,\hat{S}_y \neq 0$$

$$\rightarrow \sigma_x \sigma_y \geq \left|\frac{1}{2i}\langle -i\hbar\,\hat{S}_y\rangle\right| = \frac{\hbar}{2}\left|\langle \hat{S}_y\rangle\right|$$

So the lower bound itself depends on the quantum state. In particular, if $\langle \hat{S}_y\rangle = 0$ the bound vanishes. One such state is, for example

$$|\psi\rangle = \frac{1}{\sqrt{2}}\left(|y+\rangle + |y-\rangle\right)$$

where $|y\pm\rangle$ satisfy $\hat{S}_y |\pm\rangle = \pm\frac{\hbar}{2}|\pm\rangle$

$$\langle \psi | \hat{S}_y | \psi\rangle = \frac{1}{2}\left(\langle +| + \langle -|\right)\hat{S}_y\left(|+\rangle + |-\rangle\right)$$

$$= \frac{1}{2}\left(\langle +|\hat{S}_y|+\rangle + \langle -|\hat{S}_y|-\rangle\right)$$

$$= \frac{1}{2}\left(\frac{\hbar}{2} - \frac{\hbar}{2}\right) = 0$$

## 1.7 The Schrödinger equation

Introduce the time-evolution operator, which advances a state forward in time

$$\hat{U}(t)|\psi(0)\rangle = |\psi(t)\rangle$$

To conserve probability, the evolution must preserve the norm of the state

$$\langle \psi(t)|\psi(t)\rangle = \langle U\psi(0)|U\psi(0)\rangle$$

$$= \langle \psi(0)|U^\dagger(t)U(t)|\psi(0)\rangle$$

$$= \langle \psi(0)|\psi(0)\rangle = 1$$

$$\rightarrow U^\dagger(t)U(t) = \mathbb{I} \rightarrow U(t) \text{ must be } \underline{\text{unitary}}$$

Consider an infinitesimal time step

$$\hat{U}(dt) = 1 - \frac{i}{\hbar}\hat{H}\,dt$$

where $\hat{H}$ generates "time translations". Unitarity forces $\hat{H}$ to be Hermitian.

One can show that $\hat{U}$ obeys a first-order differential equation in time

$$\hat{U}(t+dt) = \hat{U}(dt)\hat{U}(t) = \left(1 - \frac{i}{\hbar}\hat{H}\,dt\right)\hat{U}(t)$$

$$\rightarrow \hat{U}(t+dt) - \hat{U}(t) = \left(-\frac{i}{\hbar}\hat{H}\,dt\right)\hat{U}(t)$$

$$\rightarrow i\hbar\frac{d\hat{U}}{dt} = \hat{H}\hat{U}(t)$$

$$\rightarrow i\hbar\frac{d}{dt}\hat{U}(t)|\psi(0)\rangle = \hat{H}\hat{U}(t)|\psi(0)\rangle$$

$$\boxed{i\hbar\frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle}$$

*Schrödinger equation*

For a time-independent $\hat{H}$ we may expand

$$\hat{U}(t) = \lim_{N\to\infty}\left[1 - \frac{i}{\hbar}\hat{H}\left(t/N\right)\right]^N = e^{-i\hat{H}t/\hbar}$$

and $$|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle$$

$\hat{H}$ has units of energy. Moreover, if $\hat{H}$ is time independent:

$$\langle \psi|\hat{H}|\psi\rangle = \text{const.}$$

which points to energy conservation. Indeed, $\hat{H}$ is the Hamiltonian, the "energy operator". Hence

$$E = \langle\hat{H}\rangle = \langle\psi|\hat{H}|\psi\rangle$$

The eigenstates of the Hamiltonian satisfy

$$\hat{H}|\psi\rangle = E|\psi\rangle$$

and $$e^{-i\hat{H}t/\hbar}|E\rangle = e^{-iEt/\hbar}|E\rangle$$

Therefore, if the system starts in an energy eigenstate,

$$|\psi(t)\rangle = e^{-iEt/\hbar}|E\rangle = e^{-iEt/\hbar}|\psi(0)\rangle$$

The state merely acquires an overall phase. Physically nothing changes with time; this is a "stationary state".

## 1.8 Time-dependence of expectation values

Take an observable and track how its expectation value evolves in time

$$\frac{d}{dt}\langle\hat{O}\rangle = \frac{d}{dt}\langle\psi(t)|\hat{O}|\psi(t)\rangle$$

$$= \left(\frac{d}{dt}\langle\psi(t)|\right)\hat{O}|\psi(t)\rangle + \langle\psi(t)|\hat{O}\left(\frac{d}{dt}|\psi(t)\rangle\right)$$

$$\quad + \langle\psi(t)|\frac{d\hat{O}}{dt}|\psi(t)\rangle$$

$$= \frac{-1}{i\hbar}\langle\psi(t)|\hat{H}\hat{O}|\psi(t)\rangle + \frac{1}{i\hbar}\langle\psi(t)|\hat{O}\hat{H}|\psi(t)\rangle$$

$$\quad + \langle\psi(t)|\frac{d\hat{O}}{dt}|\psi(t)\rangle$$

$$= \frac{i}{\hbar}\langle\psi(t)|[\hat{H},\hat{O}]|\psi(t)\rangle + \langle\psi(t)|\frac{d\hat{O}}{dt}|\psi(t)\rangle$$

*"Generalized Ehrenfest theorem"*

If $\hat{O} \neq \hat{O}(t)$ has no explicit time dependence

$$\rightarrow \frac{d}{dt}\langle\hat{O}\rangle = \frac{i}{\hbar}\langle[\hat{H},\hat{O}]\rangle$$

**Example:**

$$\frac{d}{dt}\langle\hat{x}\rangle = \frac{i}{\hbar}\langle[\hat{H},\hat{x}]\rangle = \left\langle\frac{\hat{p}}{m}\right\rangle$$

$$\rightarrow m\frac{d}{dt}\langle\hat{x}\rangle = \langle\hat{p}\rangle$$

If the observable commutes with $\hat{H}$, i.e. $[\hat{H},\hat{O}]=0$

$$\rightarrow \frac{d}{dt}\langle\hat{O}\rangle = 0$$

$$\rightarrow \hat{O} \text{ is a constant of motion.}$$

**Example:** two-level system (Townsend Ex.4.2)

Take the Hamiltonian

$$\hat{H} = \omega_0\,\hat{S}_x$$

with initial state $|\psi(0)\rangle = |1\rangle$. Find how the state evolves in time.

**Solution:** $\hat{U}(t) = e^{-i\omega_0\hat{S}_x t/\hbar}$

First express $|\psi(0)\rangle$ in the

eigenbasis of $\hat{S}_x$.

Recall $|x+\rangle = \frac{1}{\sqrt{2}}\left(|1\rangle + |2\rangle\right)$

$$|x-\rangle = \frac{1}{\sqrt{2}}\left(|1\rangle - |2\rangle\right)$$

Inverting,

$$|1\rangle = \frac{1}{\sqrt{2}}\left(|x+\rangle + |x-\rangle\right)$$

$$|2\rangle = \frac{1}{\sqrt{2}}\left(|x+\rangle - |x-\rangle\right)$$

Applying the evolution operator to $|\psi(0)\rangle$,

$$|\psi(t)\rangle = e^{-i\omega_0\hat{S}_x t/\hbar}|1\rangle = \frac{e^{-i\frac{\omega_0 t}{2}}}{\sqrt{2}}|x+\rangle + \frac{e^{i\frac{\omega_0 t}{2}}}{\sqrt{2}}|x-\rangle$$

Transforming back to the original basis,

$$|\psi(t)\rangle = \frac{e^{-i\frac{\omega_0 t}{2}}}{2}\left(|1\rangle + |2\rangle\right) + \frac{e^{i\frac{\omega_0 t}{2}}}{2}\left(|1\rangle - |2\rangle\right)$$

$$= \cos\frac{\omega_0 t}{2}|1\rangle - i\sin\frac{\omega_0 t}{2}|2\rangle$$

From this we can compute $\langle S^z(t)\rangle$

$$\langle S^z(t)\rangle = \cos^2\frac{\omega_0 t}{2}\left(\frac{\hbar}{2}\right) + \sin^2\frac{\omega_0 t}{2}\left(-\frac{\hbar}{2}\right)$$

$$= \frac{\hbar}{2}\left(\cos^2\frac{\omega_0 t}{2} - \sin^2\frac{\omega_0 t}{2}\right) = \frac{\hbar}{2}\cos\omega_0 t$$

More generally, when the initial state is not an eigenstate

$$e^{-i\hat{H}t/\hbar}|\psi(0)\rangle = e^{-i\hat{H}t/\hbar}\sum_n \langle n|\psi(0)\rangle|n\rangle$$

$$= \sum_n \langle n|\psi(0)\rangle\,e^{-iE_n t/\hbar}|n\rangle$$

so computing the time evolution amounts to finding the eigenvalues and eigenvectors of $\hat{H}$.

## 1.9 From wavefunctions to kets (bras)

Every wave function $\psi(\vec{r})$ corresponds to a ket $|\psi\rangle$. What remains is to spell out how scalar products and matrix elements are computed.

The scalar product must reduce to the usual overlap of wave functions

$$\langle\psi|\varphi\rangle = \int d^3 r\,\psi^*(\vec{r})\,\varphi(\vec{r})$$

For the matrix elements, introduce the "$r$-representation", built on the continuous basis

$$|\vec{r}\rangle \Leftrightarrow \delta(\vec{r}-\vec{r}_0)$$

It satisfies

- $\langle\vec{r}_0|\vec{r}_0'\rangle = \int d^3 r\,\delta(\vec{r}-\vec{r}_0)\,\delta(\vec{r}-\vec{r}_0') = \delta(\vec{r}_0 - \vec{r}_0')$

- Closure: $\int d^3 r_0\,|\vec{r}_0\rangle\langle\vec{r}_0| = \mathbb{I}$

From these we obtain:

**END LECTURE #3**

**a) Components of a ket:**

$$|\psi\rangle = \int d^3 r_0\,|\vec{r}_0\rangle\langle\vec{r}_0|\psi\rangle$$

$$= \int d^3 r_0\,|\vec{r}_0\rangle\left(\int d^3 r\,\delta(\vec{r}_0-\vec{r})\,\psi(\vec{r})\right)$$

$$= \int d^3 r_0\,\psi(\vec{r}_0)\,|\vec{r}_0\rangle$$

$$\rightarrow \langle\vec{r}_0|\psi\rangle = \psi(\vec{r}_0)$$

**b) Matrix elements:**

$$\langle\varphi|\hat{O}|\psi\rangle = \int d^3 r_0\,d^3 r_0'\,\langle\varphi|\vec{r}_0\rangle\langle\vec{r}_0|\hat{O}|\vec{r}_0'\rangle\langle\vec{r}_0'|\psi\rangle$$

$$= \int d^3 r_0\,d^3 r_0'\,\varphi^*(\vec{r}_0)\,\hat{O}(\vec{r}_0,\vec{r}_0')\,\psi(\vec{r}_0')$$

**Example:** $\hat{x}$-operator: $\hat{x}|x\rangle = x|x\rangle$

$$\rightarrow \langle x|\hat{x}|x'\rangle = x\langle x|x'\rangle = x\,\delta(x-x')$$

$$\rightarrow \langle\varphi|\hat{x}|\psi\rangle = \int dx\,dx'\,\delta(x-x')\,\varphi^*(x)\,x\,\psi(x')$$

$$= \int dx\,\varphi^*(x)\,x\,\psi(x)$$

## 1.10 Momentum operator

The momentum operator is defined through its action on a state of definite momentum $P$ (a 1d example, for simplicity)

$$\hat{P}|P\rangle = P|P\rangle\;;\quad \langle x|P\rangle = \frac{e^{iPx/\hbar}}{\sqrt{2\pi\hbar}}$$

therefore

$$\langle x|\hat{P}|\psi\rangle = \int dP\,\langle x|P\rangle\langle P|\hat{P}|\psi\rangle =$$

$$= \int dP\,P\,\langle x|P\rangle\langle P|\psi\rangle =$$

$$= \frac{1}{\sqrt{2\pi\hbar}}\int dP\,e^{iPx/\hbar}\,P\,\psi(P)$$

This is the Fourier transform of $P\psi(P)$, namely $-i\hbar\frac{\partial}{\partial x}\psi(x)$

$$\rightarrow \langle x|\hat{P}|\psi\rangle = -i\hbar\frac{\partial}{\partial x}\psi(x)$$

$$\rightarrow \langle\varphi|\hat{P}|\psi\rangle = \int dx\,\langle\varphi|x\rangle\langle x|\hat{P}|\psi\rangle =$$

$$= \int dx\,\varphi^*(x)\left[-i\hbar\frac{\partial}{\partial x}\right]\psi(x)$$

The momentum operator is Hermitian:

$$\langle\varphi|\hat{P}\psi\rangle = \int_{-\infty}^{\infty} dx\,\varphi^*(x)\left(-i\hbar\frac{d}{dx}\psi(x)\right)$$

$$\overset{\text{by parts}}{=} -i\hbar\,\varphi^*(x)\psi(x)\Big|_{-\infty}^{\infty} + i\hbar\int_{-\infty}^{\infty} dx\,\psi(x)\frac{d\varphi^*(x)}{dx}$$

Normalizable wave functions must vanish at infinity, so the boundary term drops out and

$$\langle\varphi|\hat{P}\psi\rangle = \langle\hat{P}\varphi|\psi\rangle$$

## 1.11 Angular momentum

$$\hat{P}_x = \frac{\hbar}{i}\frac{\partial}{\partial x}\;;\quad \hat{P}_y = \frac{\hbar}{i}\frac{\partial}{\partial y}\;;\quad \hat{P}_z = \frac{\hbar}{i}\frac{\partial}{\partial z}$$

$$\hat{\vec{P}} = \frac{\hbar}{i}\vec{\nabla}\;;\quad [\hat{r}_i,\hat{P}_j] = i\hbar\,\delta_{ij}$$

$$\boxed{\hat{\vec{L}} = \hat{\vec{r}}\times\hat{\vec{P}}}$$

$$[\hat{L}_x,\hat{L}_y] = i\hbar\hat{L}_z \rightarrow \sigma_x\sigma_y \geq \frac{\hbar}{2}|\langle L_z\rangle|$$

We may also form the square of $\vec{L}$:

$$\hat{L}^2 = \hat{\vec{L}}\cdot\hat{\vec{L}} = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$$

$$[\hat{L}^2,L_x] = [\hat{L}^2,L_y] = [\hat{L}^2,L_z] = 0$$

If the Hamiltonian is rotationally invariant

$$[\hat{H},\hat{L}^2] = [\hat{H},\hat{L}_z] = 0$$

The eigenstates of $H$ are then simultaneously eigenstates of $\hat{L}^2$ and $\hat{L}_z$.

The choice of $L_z$ is conventional; $L_x$ or $L_y$ would serve equally well, with nothing special about $L_z$.

To find the eigenstates it helps to introduce the operators

$$\hat{L}_+ = \hat{L}_x + i\hat{L}_y\;;\quad \hat{L}_- = \hat{L}_+^\dagger = \hat{L}_x - i\hat{L}_y$$

$$\rightarrow \hat{L}_x = \frac{1}{2}\left(\hat{L}_+ + \hat{L}_-\right)\;;\quad \hat{L}_y = \frac{1}{2i}\left(\hat{L}_+ - \hat{L}_-\right)$$

$\hat{L}_+$ and $\hat{L}_-$ are not Hermitian and satisfy

$$[\hat{L}_+,\hat{L}_-] = 2\hbar\hat{L}_z,\quad [\hat{L}_z,\hat{L}_+] = \hbar\hat{L}_+,\quad [\hat{L}_z,\hat{L}_-] = -\hbar\hat{L}_-$$

One can check that

$$\hat{L}^2 = \frac{1}{2}\left(\hat{L}_+\hat{L}_- + \hat{L}_-\hat{L}_+\right) + \hat{L}_z^2$$

$$= \hat{L}_+\hat{L}_- + \hat{L}_z^2 - \hbar\hat{L}_z$$

$$= \hat{L}_-\hat{L}_+ + \hat{L}_z^2 + \hbar\hat{L}_z$$

These relations tightly constrain the allowed eigenvalues of $\hat{L}_z$ and $\hat{L}^2$.

Suppose we know one eigenvalue of $\hat{L}_z$, written as $\hbar m$ (the factor $\hbar$ makes $m$ dimensionless). Here $L_+$ and $L_-$ act as "ladder" operators

$$\hat{L}_z\hat{L}_+|m\rangle = \left(\hat{L}_+\hat{L}_z + \hbar\hat{L}_+\right)|m\rangle = \hbar(m+1)\hat{L}_+|m\rangle$$

$$\rightarrow \hat{L}_+|m\rangle = \hbar C_m|m+1\rangle$$

Similarly $$L_-|m\rangle = \hbar C_m'|m-1\rangle$$

The constants $C_m, C_m'$ follow from $L_+ = L_-^\dagger$

$$\langle m+1|\hat{L}_+|m\rangle = \hbar C_m = \hbar C_{m+1}'^* \rightarrow C_m' = C_{m-1}^*$$

Absorbing the phase into the state makes the constants real $\rightarrow C_m' = C_{m-1}$

Now consider the operator

$$\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2 = \frac{1}{2}\left(\hat{L}_+\hat{L}_- + \hat{L}_-\hat{L}_+\right)$$

Being a sum of squares of Hermitian operators, it has non-negative expectation value. Hence, for a fixed eigenvalue $\ell$ of $L^2$, the $L_z$ spectrum is confined to $[-\ell, \ell]$.

$$\rightarrow C_\ell = C_{-\ell}' = C_{-\ell} = 0$$

Equivalently, there exist eigenstates with

$$\hat{L}_-|\ell,-\ell\rangle = \hat{L}_+|\ell,\ell\rangle = 0$$

Because repeated application of $L_\pm$ connects the states $|\ell,m\rangle$ from $m=-\ell$ up to $m=\ell$, the quantity $2\ell$ must be an integer, so $m$ takes integer or half-integer values

Now apply $L^2$ to $|\ell,\ell\rangle$

$$\hat{L}^2|\ell,\ell\rangle = \hat{L}_-\hat{L}_+|\ell,\ell\rangle + \hat{L}_z^2|\ell,\ell\rangle + \hbar\hat{L}_z|\ell,\ell\rangle$$

$$= \left(0 + \hbar^2\ell^2 + \hbar^2\ell\right)|\ell,\ell\rangle$$

$$= \hbar^2\ell(\ell+1)|\ell,\ell\rangle$$

This departs from the classical answer. For a particle circulating in the $x$-$y$ plane one would have $L_x = L_y = 0$; $L_z = \ell$; $L^2 = \ell^2$. The discrepancy comes from quantum fluctuations of the transverse components: although $\langle L_x\rangle = \langle L_y\rangle = 0$, their fluctuations do not vanish!

$$\langle\ell,\ell|\hat{L}_x^2|\ell,\ell\rangle = \langle\ell,\ell|\hat{L}_y^2|\ell,\ell\rangle = \hbar^2\ell/2$$

$$\rightarrow \sigma_{Lx} = \sigma_{Ly} = \hbar\sqrt{\ell/2}$$

Were $L_x = L_y = 0$ exactly, we would have perfect certainty on both components, in conflict with Heisenberg's uncertainty principle!

Finally, we determine the constants $C_m$

$$\hat{L}_+\hat{L}_-|\ell,-\ell\rangle = \left(\hat{L}_-\hat{L}_+ + 2\hbar\hat{L}_z\right)|\ell,-\ell\rangle$$

$$= \left(\hbar^2 C_\ell^2 - 2\hbar^2\ell\right)|\ell,-\ell\rangle$$

$$\rightarrow C_\ell = \sqrt{2\ell}$$

Repeating with $|\ell,-\ell+1\rangle \rightarrow C_{\ell+1} = \sqrt{(2\ell-1)2}$

Continuing in this way gives the general result

$$C_m = \sqrt{(\ell-m)(\ell+m+1)}$$

**Summarizing:**

$$\hat{L}_z|\ell,m\rangle = \hbar m|\ell,m\rangle$$

$$\hat{L}^2|\ell,m\rangle = \hbar^2\ell(\ell+1)|\ell,m\rangle$$

with $\ell$ integer or half-integer, and $m = -\ell, \ldots, \ell$.

$$\hat{L}_+|\ell,m\rangle = \hbar\sqrt{(\ell+m+1)(\ell-m)}\,|\ell,m+1\rangle$$

$$\hat{L}_-|\ell,m\rangle = \hbar\sqrt{(\ell+m)(\ell+1-m)}\,|\ell,m-1\rangle$$

$$\langle\ell,m|\hat{L}_x|\ell,m-1\rangle = \langle\ell,m-1|\hat{L}_x|\ell,m\rangle = \frac{\hbar}{2}\sqrt{(\ell+m)(\ell+1-m)}$$

$$\langle\ell,m|\hat{L}_y|\ell,m-1\rangle = \langle\ell,m-1|\hat{L}_y|\ell,m\rangle = -\frac{\hbar}{2}\sqrt{(\ell+m)(\ell+1-m)}$$

**Example:** $L=1$

Basis: $|\ell,m\rangle = \{|1,-1\rangle;\ |1,0\rangle;\ |1,1\rangle\}$

$$\hat{L}_+|1,-1\rangle = \hbar\sqrt{2}|1,0\rangle$$

$$\hat{L}_+|1,0\rangle = \hbar\sqrt{2}|1,1\rangle$$

$$\rightarrow L_- = \sqrt{2}\hbar\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

Similarly

$$L_+ = \sqrt{2}\hbar\begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} = (L_-)^\dagger$$

### Angular momentum in coordinate representation

Working in spherical coordinates

$$x = r\sin\theta\cos\varphi\;;\quad y = r\sin\theta\sin\varphi\;;\quad z = r\cos\theta$$

$$\rightarrow \hat{L}_z = -i\hbar\frac{\partial}{\partial\varphi}$$

$$\hat{L}_\pm = \pm\hbar e^{\pm i\varphi}\left(\frac{\partial}{\partial\theta} \pm i\cot\theta\frac{\partial}{\partial\varphi}\right)$$

$$\hat{L}^2 = -\hbar^2\left[\frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2} + \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)\right]$$

Because $\hat{L}_z$ takes such a simple form, its eigenstates follow at once:

$$-i\hbar\frac{\partial}{\partial\varphi}\Psi_m(\varphi) = \hbar m\Psi_m(\varphi)$$

$$\rightarrow \Psi_m(\varphi) = \frac{1}{\sqrt{2\pi}}e^{im\varphi}\quad m = 0, \pm 1, \pm 2, \ldots$$

Since $\psi(\varphi+2\pi) = \psi(\varphi)$, $m$ must be an integer.

The joint eigenstates of $\hat{L}^2$ and $\hat{L}^z$ are the "spherical harmonics". For $m=\ell$

$$Y_\ell^\ell(\theta,\varphi) = \frac{(-1)^\ell}{2^\ell\ell!}\sqrt{\frac{(2\ell+1)!}{4\pi}}\sin^\ell(\theta)\,e^{i\ell\varphi}$$

The solutions for $m<\ell$ are generated by applying $\hat{L}_-$

$$Y_\ell^m(\theta,\varphi) = (-1)^m\sqrt{\frac{(2\ell+1)(\ell-m)!}{4\pi\,(\ell+m)!}}\,P_{\ell m}(\cos\theta)\,e^{im\varphi},$$

where $P_{\ell m}$ are generalized Legendre polynomials

$$P_\ell^m(x) = (1-x^2)^{|m|/2}\left(\frac{d}{dx}\right)^{|m|}P_\ell(x)$$

$$P_\ell(x) = \frac{1}{2^\ell\ell!}\left(\frac{d}{dx}\right)^\ell(x^2-1)^\ell.$$

The $Y_\ell^m$ constitute a complete, orthogonal basis

$$\int_0^{2\pi} d\varphi \int_0^{\pi} d\theta \, \sin\theta \, Y_\ell^m(\theta,\varphi)^* \, Y_{\ell'}^{m'}(\theta,\varphi) = \delta_{\ell\ell'} \, \delta_{mm'}$$

and, by construction, they satisfy

$$\hat{L}^2 \, Y_\ell^m(\theta,\varphi) = \hbar^2 \ell(\ell+1) \, Y_\ell^m(\theta,\varphi)$$

$$\hat{L}_z \, Y_\ell^m(\theta,\varphi) = \hbar m \, Y_\ell^m(\theta,\varphi)$$

## 2 — A particle in a spherically symmetric potential

We aim to solve

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi$$

with the Hamiltonian

$$\hat{H} = \frac{\hat{p}^2}{2m} + V(r)$$

$$\longrightarrow \quad i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi$$

with $\nabla^2 = \dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2} + \dfrac{\partial^2}{\partial z^2}$

Because the potential carries no time dependence

$$\Psi_n(\vec{r},t) = \psi_n(\vec{r}) \, e^{-iE_n t/\hbar}$$

where the spatial part $\psi_n$ obeys the time-independent Schrödinger equation

$$\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi$$

The general solution of the time-dependent Schrödinger equation then takes the form

$$\Psi(\vec{r},t) = \sum_n c_n \, \psi_n(\vec{r}) \, e^{-iE_n t/\hbar}$$

where the coefficients $c_n$ are fixed by the initial conditions.

For a spherically symmetric potential, we first note that

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\left(\frac{\partial^2}{\partial\varphi^2}\right)$$

Therefore

$$\frac{\hat{p}^2}{2m} = -\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{\hat{L}^2}{2mr^2}$$

Where the first term contains

$$\hat{p}_r^2 = -\hbar^2 \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) = -\hbar^2\frac{\partial^2}{\partial r^2} - \hbar^2\frac{2}{r}\frac{\partial}{\partial r}$$

As in the classical case, the Hamiltonian of a particle in a spherically symmetric potential reads:

$$H = \frac{\hat{p}_r^2}{2m} + \frac{\hat{L}^2}{2mr^2} + V(r)$$

### Separation of variables:

For a particle in a central potential,

$$[\hat{H}, \hat{L}^2] = [\hat{H}, \hat{L}_z] = 0$$

so we can seek solutions of the Schrödinger equation that are simultaneously eigenfunctions of $\hat{H}$, $\hat{L}^2$ and $\hat{L}_z$

$$\hat{H}\,\psi_{n\ell m}(r,\theta,\varphi) = E_n \, \psi_{n\ell m}(r,\theta,\varphi)$$

$$\hat{L}^2 \, \psi_{n\ell m}(r,\theta,\varphi) = \hbar^2\ell(\ell+1) \, \psi_{n\ell m}(r,\theta,\varphi)$$

$$\hat{L}_z \, \psi_{n\ell m}(r,\theta,\varphi) = \hbar m \, \psi_{n\ell m}(r,\theta,\varphi)$$

Since these eigenfunctions are also angular momentum eigenstates, we write them as

$$\psi(r,\theta,\varphi) = R(r) \, Y_\ell^m(\theta,\varphi)$$

Substituting this into the Schrödinger equation yields the eigenvalue equation for the radial part

$$-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{d}{dr}\right) - \frac{\ell(\ell+1)}{r^2} + V(r)\right]R(r) = ER(r)$$

Setting $\chi(r) = r R(r)$, we obtain

$$\left[-\frac{\hbar^2}{2m}\frac{d^2}{dr^2} + V_{\text{eff}}\right]\chi(r) = E\chi(r)$$

$$V_{\text{eff}}(r) = V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2} \qquad r > 0$$

*end lecture*

a one-dimensional Schrödinger equation for $\chi(r)$. For each $\ell$, the radial equation must be solved subject to $\chi(0) = 0$, equivalent to an infinite barrier at the origin and ensuring $\chi = 0$ for $r < 0$. The eigenvalues are independent of $L_z$ or $m$, giving a $2\ell+1$-fold degeneracy for each value of $\ell$.


---

## References and Further Reading

*The references below are an editorial addition. Prof. Feiguin's lecture notes follow John S. Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed. (University Science Books, 2012); the generalized uncertainty relation is cited in the text as Townsend §3.5.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 1 (Stern–Gerlach Experiments), Ch. 2 (Rotation of Basis States and Matrix Mechanics), Ch. 3 (Angular Momentum — the generalized uncertainty principle, §3.5), Ch. 4 (Time Evolution). Wave mechanics and the momentum operator: Ch. 6.

**Further reading.** Sakurai & Napolitano, *Modern Quantum Mechanics*, the "Fundamental Concepts" and "Quantum Dynamics" chapters; Shankar, *Principles of Quantum Mechanics*, Ch. 1, 4; Cohen-Tannoudji, Diu & Laloë, *Quantum Mechanics*, Vol. I, Ch. II–III.
