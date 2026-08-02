# Module M-14 — Combinatorics and Multiplicity

Thermodynamics is often presented as a set of laws. Counting is often presented as a set of formulas. The connection between them is that equilibrium is not a law — it is a counting result. The most probable macrostate is the one with the most microstates. Temperature is a derivative of a logarithm. Entropy is a logarithm of a count. All of this follows from arithmetic, once we are precise about what we are counting.

---

## The Load-Bearing Distinction

Every counting error in physics begins with confusing three terms. Establishing these clearly before any formula will save considerable trouble.

A **microstate** is one fully-specified arrangement — which specific spins are up, which exact qubits are $|0\rangle$, which precise molecules occupy which box.

A **macrostate** is the coarse, measurable summary — the net magnetization, the syndrome measurement result, the total energy.

The **multiplicity** $\Omega$ is the number of microstates that produce a given macrostate.

Many microstates map to one macrostate. The number that map is $\Omega$. Everything below is the arithmetic of $\Omega$.

---

## Permutations and Combinations

A **permutation** counts ordered arrangements. The number of ordered arrangements of $k$ chosen from $n$ is $P(n,k) = n!/(n-k)!$.

A **combination** counts unordered selections. When we choose $k$ from $n$ and the order of the chosen set does not matter, we divide out the $k!$ internal orderings:

$$\boxed{\binom{n}{k} = \frac{n!}{k!\,(n-k)!}.}$$

The single decision that determines which formula to use: *does order matter?* For spin counting — we care which spins are up, not which one we labeled "first" — order does not matter. Use combinations. The binomial coefficient satisfies the Pascal recursion $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ and appears in the binomial theorem $(a+b)^n = \sum_{k=0}^n\binom{n}{k}a^k b^{n-k}$.

Pascal's triangle appears in Yang Hui's 13th-century work and in al-Karaji's earlier Islamic mathematics, centuries before Pascal's 1665 treatise. The Western name is an artifact of citation history, not priority.

---

## Multiplicity of a Two-State System

$N$ labeled objects, each in one of two states (up/down, $|0\rangle$/$|1\rangle$), have multiplicity

$$\Omega(N, N_\uparrow) = \binom{N}{N_\uparrow} = \frac{N!}{N_\uparrow!\,(N-N_\uparrow)!}$$

for the macrostate with exactly $N_\uparrow$ objects up. This peaks at $N_\uparrow = N/2$ and the peak sharpens with increasing $N$. At thermodynamic scale $N\sim10^{23}$, the peak is a needle: the system is overwhelmingly found at the most probable macrostate. Equilibrium is not imposed from outside. It is simply where the microstates are concentrated.

**Stars and bars.** When distributing $q$ *indistinguishable* quanta among $N$ *distinguishable* bins (the Einstein solid), the counting is:

$$\Omega(N,q) = \binom{q+N-1}{q}.$$

This applies when the objects being distributed are identical. It should not be confused with the spin counting above, where the $N$ spins are distinguishable. The formulas address different physical situations.

![Multiplicity peak and Gaussian sharpening for N=6, 20, 100](../images/14-combinatorics-and-multiplicity-fig-01.png)
*Figure 14.1 — Multiplicity peak sharpening: the normalized binomial distribution $\Omega(N, N_\uparrow)/\Omega_\text{max}$ (top) and its Gaussian envelope (bottom) for $N = 6$, $20$, and $100$, showing how the peak at $N_\uparrow/N = 0.5$ narrows dramatically with increasing $N$.*

---

## Stirling's Approximation

For $N\sim10^{23}$, the factorial $N!$ has more digits than atoms in a room and cannot be evaluated directly. More importantly, we need to *differentiate* $\ln\Omega$ with respect to $N$ — and a factorial is not differentiable. We approximate the sum $\ln N! = \sum_{m=1}^N\ln m$ by an integral:

$$\ln N! = \sum_{m=1}^N\ln m \approx \int_1^N\ln x\,dx = [x\ln x - x]_1^N = N\ln N - N + 1.$$

Dropping the negligible $+1$:

$$\boxed{\ln N! \approx N\ln N - N.}$$

The refined form is $N!\approx\sqrt{2\pi N}(N/e)^N$, giving $\ln N!\approx N\ln N - N + \tfrac{1}{2}\ln(2\pi N)$.

**Why dropping the** $\tfrac{1}{2}\ln(2\pi N)$ **term is valid at thermodynamic scale.** For $N = 10^{23}$: the kept term $N\ln N\approx5\times10^{24}$; the dropped term $\approx27$. The relative error is one part in $10^{23}$. No experiment could resolve it. For small $N$ — a 5-qubit code — the error matters; use the refined form or exact factorials.

**Stirling applied to the binomial coefficient.** Using $\ln\Omega = \ln N! - \ln N_\uparrow! - \ln(N-N_\uparrow)!$ and applying the leading Stirling form to each factorial:

$$\ln\Omega = N\ln N - N_\uparrow\ln N_\uparrow - (N-N_\uparrow)\ln(N-N_\uparrow).$$

This is the fundamental formula: a smooth, differentiable function of $N_\uparrow$ that can be maximized analytically and differentiated with respect to energy.

![Stirling approximation relative error vs N](../images/14-combinatorics-and-multiplicity-fig-03.png)
*Figure 14.3 — Stirling approximation accuracy: the relative error of the leading form $N\ln N - N$ (solid) drops from roughly 40% at $N = 6$ to negligible above $N \approx 30$; the refined form with $\tfrac{1}{2}\ln(2\pi N)$ (dashed) converges faster.*

---

## From Multiplicity to Entropy: $S = k\ln\Omega$

Two interlocking arguments explain why entropy is the logarithm of the count.

**Multiplicities multiply; entropy must add.** If system $A$ has $\Omega_A$ microstates and system $B$ has $\Omega_B$, the combined system has $\Omega_A\Omega_B$ microstates. Thermodynamic entropy is extensive — it adds when we combine systems. The only function that converts multiplication to addition is the logarithm:

$$\ln(\Omega_A\Omega_B) = \ln\Omega_A + \ln\Omega_B.$$

So if entropy is a function of multiplicity and must be additive, it must be proportional to $\ln\Omega$.

**Temperature follows by differentiating.** With $S = k\ln\Omega$ a differentiable function of energy (Stirling makes this possible), we define temperature through

$$\frac{1}{T} \equiv \frac{\partial S}{\partial E}.$$

Maximizing $\Omega$ subject to fixed total energy is equivalent to requiring $\partial S_A/\partial E = \partial S_B/\partial E$ — the statement that both systems share a common temperature. The entire equilibrium condition is a calculus exercise on a counting formula.

One notation note: Boltzmann wrote $S = k\log W$ with $W$ for Wahrscheinlichkeit (probability/multiplicity) — same object, different letter. The form $S = k\ln\Omega$ with the natural logarithm is the convention used throughout this series. Shannon entropy uses $\log_2$ with the result in bits; von Neumann entropy $S = -\text{Tr}(\rho\log\rho)$ uses $\ln$. The physics is identical; only the proportionality constant changes.

---

## Identical Particles: When Counting Changes

The distinction between bosons and fermions in Chapter 10 is, at its mathematical root, a counting distinction. Placing two quantum particles into two available single-particle states gives:

| Statistics | Rule | Distinct microstates |
|---|---|:---:|
| Maxwell-Boltzmann (distinguishable) | any occupancy | 4 |
| Bose-Einstein (identical bosons) | any occupancy per state | 3 |
| Fermi-Dirac (identical fermions) | at most 1 per state (Pauli) | 1 |

![Three statistics microstate enumeration for 2 particles in 2 states](../images/14-combinatorics-and-multiplicity-fig-02.png)
*Figure 14.2 — Three statistics compared: Maxwell-Boltzmann (4 microstates, distinguishable particles), Bose-Einstein (3 microstates, identical bosons), and Fermi-Dirac (1 microstate, identical fermions) for two particles occupying two single-particle states.*

The Fermi-Dirac count is 1 because the only allowed configuration for two identical fermions in two states is "one in each state." The wavefunction antisymmetry enforces exactly this: a Slater determinant

$$|\psi\rangle = \frac{1}{\sqrt{2}}\bigl(\phi_a(1)\phi_b(2) - \phi_b(1)\phi_a(2)\bigr)$$

vanishes identically when $\phi_a = \phi_b$ — two fermions in the same state give zero amplitude. Pauli exclusion is the algebraic statement that $\Omega_\text{FD} = 0$ for doubly-occupied single-particle states. The determinant structure is the counting rule made antisymmetric.

A parallel issue arises in classical statistical mechanics. For $N$ identical classical particles, the naive multiplicity must be divided by $N!$ to avoid counting permutations of identical molecules as distinct microstates — the Gibbs paradox. Quantum mechanics handles this automatically via symmetrization. If you are working with a classical gas of identical molecules and your entropy is non-extensive, the $N!$ factor has been omitted.

<!-- → [TABLE: three-row comparison of Maxwell-Boltzmann, Bose-Einstein, and Fermi-Dirac counting for 2 particles in 2 states — showing all allowed configurations explicitly for each statistics, with the microstates listed and the count; this makes the counting difference visceral before any wavefunctions are introduced] -->

---

## Quantum Error Correction: Syndrome as Macrostate

An $[[n,k,d]]$ quantum error-correcting code encodes $k$ logical qubits in $n$ physical qubits and can correct any error on up to $t = \lfloor(d-1)/2\rfloor$ physical qubits. The combinatorics enters directly.

**Counting errors.** The number of distinct $\text{weight-}t$ Pauli errors on $n$ qubits (errors affecting exactly $t$ sites) is

$$\binom{n}{t}\times3^t,$$

since there are $\binom{n}{t}$ ways to choose which $t$ sites are affected and $3^t$ choices of Pauli operator ($X$, $Y$, or $Z$) at each affected site.

**The Hamming bound.** For a code to correct all $\text{weight-}\leq t$ errors, the correctable error cosets must fit in the syndrome space without overlapping:

$$\sum_{j=0}^t\binom{n}{j}3^j \leq 2^{n-k}.$$

The left side counts how many distinguishable error syndromes the code must accommodate; the right side is the size of the syndrome space. This is a pure combinatorial constraint.

**Syndrome = macrostate.** A syndrome measurement projects the physical system onto a coset of the stabilizer group. Multiple distinct Pauli error patterns (microstates) produce the same syndrome (macrostate) — exactly the structure of $\Omega > 1$. The decoder infers which microstate caused the observed macrostate and applies the corresponding correction. When two or more distinct errors give the same syndrome, the code is degenerate, and the syndrome multiplicity is exactly $\Omega > 1$.

**Fault-tolerance threshold.** The probability that at least $t+1$ errors occur among $n$ gate operations, each with error rate $p$, is bounded by the binomial tail:

$$P(\text{failure}) \leq \binom{n}{t+1}p^{t+1}.$$

Below the threshold error rate $p_\text{th}$, this is exponentially suppressed by concatenation — each level replaces $p$ by $\sim p^2/p_\text{th}$. The binomial coefficient counts the ways failure can occur.

---

## Worked Example: Counting Microstates for a Small System

**A system has** $N = 6$ **distinguishable spins. How many microstates have exactly** $N_\uparrow = 2$ **spins up?**

Order doesn't matter (which two are up, not which-first):

$$\Omega(6,2) = \binom{6}{2} = \frac{6\times5}{2} = 15.$$

Total microstates: $2^6 = 64$. Fraction: $15/64 \approx 23.4\%$.

The peak macrostate is $N_\uparrow = 3$: $\binom{6}{3} = 20$, giving $20/64\approx31.3\%$. The peak is not yet dominant at $N = 6$; at $N = 10^{23}$ it is a knife-edge.

**Stirling check at small** $N$. Exact: $\ln15\approx2.71$. Stirling: $6\ln6 - 6 - (2\ln2 - 2) - (4\ln4 - 4)\approx3.81$. A 40% error. Stirling is inaccurate for small $N$ and becomes reliable only in the thermodynamic limit. Note which regime you are in before applying it.

---

## Quick Practice

1. **Enumerate, then formula.** A system has $N = 4$ labeled spins. List all microstates with $N_\uparrow = 2$ by hand. Confirm with $\binom{4}{2}$. Compute $\Omega(4,2)/2^4$ — what fraction of all microstates have exactly two spins up?

2. **Stirling at work.** Use the leading Stirling approximation to compute $\ln\binom{20}{10}$ analytically. The exact value is $\binom{20}{10} = 184756$; report the relative error. At what $N$ does the relative error become negligible for thermodynamic purposes?

3. **Syndrome counting.** A $[[5,1,3]]$ code encodes 1 logical qubit in 5 physical qubits and corrects all weight-1 errors. (a) How many distinct weight-1 Pauli errors are there? (b) How many distinct weight-0 errors? (c) Does the Hamming bound $\sum_{j=0}^1\binom{5}{j}3^j\leq2^{5-1}$ hold? (d) What does saturation mean physically?

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the microstate / macrostate / multiplicity distinction.*
   A system consists of 3 distinguishable coins, each heads or tails. (a) List all 8 microstates explicitly. (b) Group them by macrostate (number of heads) and compute $\Omega$ for each macrostate. (c) Verify that $\sum_\text{macrostates}\Omega = 8$. (d) Which macrostate is most probable if each microstate is equally likely, and why is this the "equilibrium" macrostate?
   *Tests: the three core concepts before any formula appears; seeing that equilibrium is a counting result.*

2. *Difficulty: Warm-up — tests permutations vs. combinations.*
   Five students compete for three prizes. (a) In how many ways can the gold, silver, and bronze prizes be awarded to three distinct students (order matters)? (b) In how many ways can a committee of three be chosen from the five (order does not matter)? (c) For the spin problem: you have 5 labeled spins and want to know how many configurations have exactly 3 up. Which formula applies, and why?
   *Tests: the order-matters decision as the key step; connecting to the spin counting problem.*

3. *Difficulty: Warm-up — tests the Stirling approximation.*
   (a) Compute $\ln(10!)$ exactly (use $10! = 3628800$). (b) Compute the leading Stirling approximation $N\ln N - N$ for $N = 10$. (c) Compute the refined Stirling $N\ln N - N + \tfrac{1}{2}\ln(2\pi N)$ for $N = 10$. (d) Which approximation is closer to the exact value, and by how much?
   *Tests: direct comparison of exact factorial, leading Stirling, and refined Stirling at small N.*

**Application**

4. *Difficulty: Application — multiplicity and entropy.*
   A two-state paramagnet has $N = 100$ spins and total energy $E = -B\mu(N_\uparrow - N_\downarrow)\hbar$ where $B$ is the applied field. (a) Express $N_\uparrow$ in terms of $N$ and $E$. (b) Use the leading Stirling approximation to write $\ln\Omega(N,N_\uparrow)$ as a function of $N$ and $N_\uparrow$. (c) Show that $\ln\Omega$ is maximized at $N_\uparrow = N/2$ by taking $d(\ln\Omega)/dN_\uparrow = 0$. (d) Compute $S/k = \ln\Omega$ at the maximum and verify it equals $N\ln2$.
   *Tests: connecting* $\Omega$ *to energy, differentiating to find the maximum, connecting to entropy.*

5. *Difficulty: Application — Hamming bound for quantum codes.*
   A $[[7,1,3]]$ code encodes 1 logical qubit in 7 physical qubits and corrects all weight-1 errors ($t = 1$). (a) How many distinct weight-0 and weight-1 Pauli errors are there? Compute the total $\sum_{j=0}^1\binom{7}{j}3^j$. (b) The syndrome space has size $2^{7-1} = 64$. Does the Hamming bound hold? (c) Is the bound saturated? If not, how much slack is there? (d) What does non-saturation tell you about whether a code with these parameters is "optimal"?
   *Tests: applying the Hamming bound to a real code; comparing left and right sides; interpreting saturation.*

6. *Difficulty: Application — temperature from entropy.*
   An Einstein solid with $N = 3$ oscillators and total energy $q\hbar\omega$ has multiplicity $\Omega(N,q) = \binom{q+N-1}{q}$. (a) Compute $\Omega$ for $q = 0, 1, 2, 3, 4$. (b) Compute $S(q) = k\ln\Omega(q)$ for each value. (c) Define the temperature via $1/T = \partial S/\partial E = (1/\hbar\omega)\partial S/\partial q$ and estimate $T$ at $q = 2$ by the finite difference $(S(3)-S(1))/(2\hbar\omega)$. (d) Does $T$ increase or decrease as $q$ increases? What does this mean physically?
   *Tests: direct computation of multiplicity, entropy, and temperature for a small quantum system; seeing temperature emerge from counting.*

**Synthesis**

7. *Difficulty: Synthesis — comparing classical and quantum counting.*
   Two distinguishable particles $A$ and $B$ are placed in two boxes (box 1 and box 2). (a) List all 4 classical (Maxwell-Boltzmann) microstates. (b) Now treat them as identical bosons. List all distinct quantum microstates (remembering that $|A\text{ in 1},B\text{ in 2}\rangle$ and $|B\text{ in 1},A\text{ in 2}\rangle$ are the same state for identical particles). (c) Now treat them as identical fermions: how many distinct microstates are there? (d) Compute the probability that both particles are in box 1 for each statistics. Explain how this changes qualitatively in each case and what physical phenomenon each reflects (bunching for bosons, exclusion for fermions).
   *Tests: all three statistics in a minimal example; connecting the count to the physical phenomena of bunching and Pauli exclusion.*

8. *Difficulty: Synthesis — entropy additivity and the Gibbs paradox.*
   Two systems $A$ and $B$ each have $N$ distinguishable particles with multiplicities $\Omega_A$ and $\Omega_B$. (a) Show that the combined multiplicity is $\Omega_{AB} = \Omega_A\Omega_B$ and hence $S_{AB} = S_A + S_B$ (entropy is extensive). (b) Now suppose the $N$ particles in each system are identical and indistinguishable. For a classical gas occupying the same volume $V$ at the same temperature: if you divide $\Omega$ by $N!$, show that the Sackur-Tetrode entropy is extensive. (c) If you forgot the $N!$ and mixed two identical gases at the same pressure and temperature, compute the apparent entropy of mixing and show it is nonzero — the Gibbs paradox. (d) Explain in one sentence why quantum mechanics resolves this paradox automatically.
   *Tests: additivity of entropy from multiplicities; the Gibbs* $N!$ *factor; the Gibbs paradox and its quantum resolution.*

**Challenge**

9. *Difficulty: Challenge — the peak sharpens as a Gaussian.*
   For a two-state paramagnet with $N$ spins, the multiplicity $\Omega(N,N_\uparrow) = \binom{N}{N_\uparrow}$ is maximized at $N_\uparrow = N/2$. (a) Write $N_\uparrow = N/2 + s$ where $s$ is the deviation from the peak. Show that $\ln\Omega(N,N/2+s) \approx N\ln2 - 2s^2/N$ for $|s|\ll N/2$ by Taylor-expanding $\ln\Omega$ around $s = 0$ to second order using the Stirling approximation. (b) The probability of macrostate $s$ relative to the peak is $P(s) \propto e^{-2s^2/N}$ — a Gaussian. Identify the standard deviation $\sigma$ of this distribution. (c) The fractional width of the peak is $\sigma/N = 1/\sqrt{2N}$: show this → 0 as $N\to\infty$ and compute $\sigma/N$ for $N = 10^{23}$. (d) Interpret: at thermodynamic scale, what does the vanishing of $\sigma/N$ imply about the reliability of macroscopic thermodynamics?
   *Tests: Taylor expansion of ln Ω; the Gaussian peak as the central limit theorem in disguise; the connection between peak sharpness and thermodynamic certainty.*

---

## References

Boltzmann, L. (1877). Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung. *Wiener Berichte*, 76, 373–435.

Planck, M. (1906). *Vorlesungen über die Theorie der Wärmestrahlung*.

Stirling, J. (1730). *Methodus Differentialis*.

Calderbank, A. R., & Shor, P. W. (1996). Good quantum error-correcting codes exist. *Physical Review A*, 54, 1098–1105.

Gottesman, D. (1997). Stabilizer codes and quantum error correction. Ph.D. thesis, California Institute of Technology.

Schroeder, D. V. *An Introduction to Thermal Physics*. Addison-Wesley.
