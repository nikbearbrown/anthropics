# Combinatorics, Multiplicity, and Stirling's Approximation

*Permutations and combinations, the binomial coefficient, microstate counting, factorials and Stirling's approximation, and the bridge from counting to entropy — the discrete mathematics that statistical mechanics runs on.*

---

## 1. Cold open: a hundred tiny magnets

Take a row of atoms, each carrying a tiny magnetic moment — a spin that, in a magnetic field, can point only one of two ways: *up* (aligned, low energy) or *down* (anti-aligned, high energy). This is a **two-state paramagnet**, and it is the simplest system in all of thermal physics. Suppose you have $N = 100$ of them.

Here is the question the thermodynamics book asks, and the question this chapter exists to answer. You can *measure* the total magnetization, which depends only on $N_\uparrow$, the number pointing up. That measurable quantity is the **macrostate**. But for a given magnetization there are many, many specific patterns of up and down spins that produce it — spin 1 up, spin 2 down, spin 3 up… — and each such pattern is a **microstate**. The thermodynamics book makes a single, audacious postulate: *every accessible microstate is equally likely*. From that one assumption, the entire edifice of equilibrium, temperature, and entropy follows — *if* you can count microstates.

So: how many microstates have exactly $N_\uparrow$ spins up? With $N=100$ and $N_\uparrow = 50$ the answer is a number with 29 digits. The book then claims that the system, left alone, overwhelmingly sits near $N_\uparrow = 50$ — the most probable macrostate — and that the logarithm of this microstate count *is the entropy*. Two things need explaining. First, how do we count those 29-digit numbers, and how do we handle the factorials of $N \sim 10^{23}$ that real systems demand? Second, why should the *logarithm* of a count be entropy? This chapter answers both. The counting is combinatorics; the taming of the factorials is Stirling's approximation; and the bridge from count to entropy is the most consequential single equation in statistical mechanics, $S = k\ln\Omega$.

---

## 2. The tool, named

Volume 1 introduced factorials and the binomial theorem at the level of "here is how to expand $(a+b)^n$." Volume 2 picks up exactly where the numbers get physical: at $N \sim 10^{23}$, where exact factorials are not just tedious but *uncomputable*, and where the only way forward is to replace $N!$ with a smooth, differentiable function of $N$. That replacement — **Stirling's approximation** — is what lets us write entropy as a function we can differentiate, and differentiating it is what gives temperature. The chain is:
$$
\text{count microstates } \Omega \;\longrightarrow\; S = k\ln\Omega \;\longrightarrow\; \frac{1}{T} = \frac{\partial S}{\partial E}.
$$
Every link in that chain needs combinatorics and Stirling. We build them now.

Before any formula, internalize one distinction, because students conflate it more than any other: a **microstate** is one specific, fully-detailed arrangement (this exact spin pattern); a **macrostate** is the coarse, measurable summary (the net magnetization). Many microstates map to one macrostate. The number that map to a given macrostate is its **multiplicity** $\Omega$. Everything below is the arithmetic of $\Omega$.

---

## 3. Development and derivation

### 3.1 Permutations and combinations

Start small and concrete — the research on how students actually learn this is unambiguous: *enumerate before you reach for a formula.*

A **permutation** counts ordered arrangements. The number of ways to arrange $n$ distinct objects in a row is
$$
n! = n\cdot(n-1)\cdot(n-2)\cdots 2\cdot 1,
$$
because there are $n$ choices for the first slot, $n-1$ for the second, and so on. The number of ordered arrangements of $k$ objects chosen from $n$ is
$$
P(n,k) = \frac{n!}{(n-k)!}.
$$
A **combination** counts *unordered* selections — when order does not matter. Choosing $k$ objects from $n$, then dividing out the $k!$ orderings of the chosen set that we just over-counted, gives the **binomial coefficient**:
$$
\boxed{\;\binom{n}{k} = \frac{n!}{k!\,(n-k)!}.\;}
$$
The single decision that determines which formula you need is: *does order matter?* For our spins, the microstate is "which specific spins are up," and the up-spins are interchangeable as a set — order does not matter — so the count is a combination.

The binomial coefficient is the entry in **Pascal's triangle**, which obeys the recursion
$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$
(to pick $k$ from $n$, either the last object is in your selection — leaving $\binom{n-1}{k-1}$ ways for the rest — or it is not, leaving $\binom{n-1}{k}$). The triangle is old: it appears in Yang Hui's work in 13th-century China — "Yang Hui's triangle" — and in the Islamic tradition with al-Karaji, centuries before Pascal's 1665 treatise gave it the name it carries in the West. And the coefficient earns its name from the **binomial theorem**:
$$
(a+b)^n = \sum_{k=0}^{n}\binom{n}{k} a^k b^{n-k},
$$
where $\binom{n}{k}$ counts the number of terms that produce $a^k b^{n-k}$ when you multiply out $n$ factors.

![Rows zero through six of Pascal's triangle of binomial coefficients, with the n equals 4 row 1 4 6 4 1 highlighted in red and arrows showing that the entry 10 equals 4 plus 6](images/09-combinatorics-multiplicity-and-stirling-fig-01.png)
*Figure 9.1 — Pascal's triangle: each entry C(n, k) is the sum of the two above it, and row n = 4 (1, 4, 6, 4, 1) counts the four-spin states by number pointing up.*

### 3.2 Multiplicity of the two-state system

Now the payoff. A microstate of the paramagnet is a specific assignment of up/down to each of the $N$ labeled spins. A macrostate is fixed by $N_\uparrow$ alone. The number of microstates with exactly $N_\uparrow$ up — the **multiplicity** — is the number of ways to *choose which* $N_\uparrow$ of the $N$ spins are up:
$$
\Omega(N, N_\uparrow) = \binom{N}{N_\uparrow} = \frac{N!}{N_\uparrow!\,(N-N_\uparrow)!}.
$$
For small $N$ you can list them. With $N=4$: there is $\Omega=1$ way to have all four up ($\uparrow\uparrow\uparrow\uparrow$), $\Omega=4$ ways to have three up, $\Omega=6$ ways to have two up, $\Omega=4$ ways for one, $\Omega=1$ for none — the row $1,4,6,4,1$ of Pascal's triangle, summing to $2^4 = 16$ total microstates. The multiplicity peaks sharply in the middle, at $N_\uparrow = N/2$. As $N$ grows that peak gets *relatively* sharper and sharper: this is the mathematical content of "the system sits at the most probable macrostate." Equilibrium is not a law imposed from outside; it is just where the microstates are overwhelmingly concentrated.

![Two multiplicity curves normalized to peak height one, plotted against the fraction of spins pointing up; the N equals 10 curve is broad and the N equals 50 curve in red is much narrower, both peaking at one half](images/09-combinatorics-multiplicity-and-stirling-fig-02.png)
*Figure 9.2 — Multiplicity Ω(N, N↑) peaks at N↑ = N/2 and sharpens as N grows: at N ~ 10²³ the peak is a needle, which is what "equilibrium" means.*

### 3.3 Stirling's approximation — taming the factorial

For $N = 100$, $\binom{100}{50}$ is computable but unpleasant. For $N = 10^{23}$, $N!$ has more digits than there are atoms in the room, and no calculator will touch it. Worse, we want to *differentiate* $\ln\Omega$ with respect to $N$ — and a factorial is not a differentiable function. We need a smooth approximation.

Take the logarithm of the factorial and turn the sum into an integral:
$$
\ln N! = \sum_{m=1}^{N}\ln m \approx \int_{1}^{N}\ln x\,dx.
$$
The integral is elementary (by parts):
$$
\int_1^N \ln x\,dx = \big[x\ln x - x\big]_1^N = N\ln N - N + 1.
$$
Dropping the negligible $+1$ for large $N$ gives the leading-order **Stirling approximation**:
$$
\boxed{\;\ln N! \approx N\ln N - N.\;}
$$
A more careful asymptotic analysis (Euler–Maclaurin, or the saddle-point evaluation of $N! = \int_0^\infty x^N e^{-x}dx$) supplies the next term and the constant:
$$
\ln N! \approx N\ln N - N + \tfrac12\ln(2\pi N), \qquad\text{i.e.}\qquad N! \approx \sqrt{2\pi N}\left(\frac{N}{e}\right)^{N}.
$$
The constant $\sqrt{2\pi}$ is the historically interesting part. De Moivre, in his 1730 *Miscellanea Analytica*, had the form $N! \approx C\,N^{N+1/2}e^{-N}$ but could not pin down $C$; James Stirling, in the *Methodus Differentialis* of the same year, identified $C = \sqrt{2\pi}$. It is properly a de Moivre–Stirling result — and it is the same de Moivre, in the same decade, whose binomial-limit work gave us the Gaussian in Chapter 8. The $\sqrt{2\pi}$ that normalizes the bell curve and the $\sqrt{2\pi N}$ in Stirling are not a coincidence; they are the same Gaussian integral seen from two sides.

![The exact natural log of N factorial as plotted points, the leading Stirling curve N ln N minus N in brown lying below at small N, and the refined Stirling curve including one half log of two pi N in red essentially coincident with the exact values by N around ten](images/09-combinatorics-multiplicity-and-stirling-fig-03.png)
*Figure 9.3 — Stirling's approximation converging to the exact ln N!: the leading form trails at small N, but the refined form overlaps the exact value by N ≈ 10.*

**Why is dropping the $\tfrac12\ln(2\pi N)$ term allowed?** This is the question students rightly distrust, so settle it with numbers. For $N = 10^{23}$:
$$
N\ln N \approx 10^{23}\times 53 \approx 5\times 10^{24}, \qquad \tfrac12\ln(2\pi N) \approx \tfrac12\ln(6\times 10^{23}) \approx 27.
$$
The term we keep is of order $10^{24}$; the term we drop is of order $10^1$. Discarding it is an error of one part in $10^{23}$. At thermodynamic scale the leading Stirling form is not an approximation in any practical sense — it is exact to a precision no experiment could ever resolve. *That* is why the cheating feels like cheating but isn't.

### 3.4 From multiplicity to entropy: $S = k\ln\Omega$

We have a count $\Omega$. We want entropy. Why the logarithm?

Two arguments, one mathematical and one physical. **Mathematically**, multiplicities *multiply*: if system A has $\Omega_A$ microstates and system B has $\Omega_B$, the combined system has $\Omega_A\Omega_B$ (every microstate of A paired with every microstate of B). But entropy, as thermodynamics defines it through heat, is *extensive* — it should *add* when you combine systems. The only function that turns multiplication into addition is the logarithm: $\ln(\Omega_A\Omega_B) = \ln\Omega_A + \ln\Omega_B$. So if entropy is to be a function of multiplicity and to be additive, it must be proportional to $\ln\Omega$:
$$
\boxed{\;S = k\ln\Omega.\;}
$$
**Physically**, Boltzmann argued in his 1877 combinatorial paper that the equilibrium macrostate is the one of maximum multiplicity, and that the thermodynamic entropy — the quantity that only increases — tracks $\ln\Omega$. The constant of proportionality $k$ (the Boltzmann constant) was actually named, and the equation first written in this compact form, by Planck around 1900–1906; the form $S = k\log W$ carved on Boltzmann's Vienna tombstone is Planck's typography. Boltzmann supplied the physics and the logarithmic relation; Planck supplied the constant and the engraving.

Now the smoothness pays off. With $S = k\ln\Omega$ a differentiable function of energy, the thermodynamics book *defines* temperature as
$$
\frac{1}{T} = \frac{\partial S}{\partial E},
$$
and the entire structure of equilibrium thermodynamics — temperature, the approach to equilibrium, the second law as a statement that systems move toward higher multiplicity — falls out of counting. The second law is, at bottom, a counting argument: a system evolves toward the macrostate with the most microstates simply because there are vastly more ways to be there.

### 3.5 The Boltzmann distribution, derived by counting

Chapter 8 introduced the Boltzmann factor $e^{-E/k_BT}$ as a distribution to be used. Here we *derive* it — closing the loop the previous chapter opened.

Put a small system in thermal contact with a large reservoir, the two sharing a fixed total energy $E_{\text{tot}}$. By the equal-probability postulate, the probability that the small system sits in a *specific* state of energy $E_i$ is proportional to the number of reservoir microstates compatible with it, namely $\Omega_R(E_{\text{tot}} - E_i)$:
$$
P_i \propto \Omega_R(E_{\text{tot}} - E_i) = \exp\!\big[\ln\Omega_R(E_{\text{tot}} - E_i)\big].
$$
Because the reservoir is enormous, $E_i \ll E_{\text{tot}}$, so expand $\ln\Omega_R$ to first order in $E_i$:
$$
\ln\Omega_R(E_{\text{tot}} - E_i) \approx \ln\Omega_R(E_{\text{tot}}) - E_i\,\frac{\partial \ln\Omega_R}{\partial E}.
$$
But $\partial \ln\Omega_R/\partial E = \frac{1}{k}\,\partial S/\partial E = 1/(kT)$ by §3.4. Substituting,
$$
P_i \propto e^{\ln\Omega_R(E_{\text{tot}})}\,e^{-E_i/kT} \;\propto\; e^{-E_i/kT}.
$$
Normalizing by $Z = \sum_i e^{-E_i/kT}$ gives the **Boltzmann distribution** $P_i = e^{-E_i/kT}/Z$. The master distribution of all of thermal physics is a first-order Taylor expansion of the *logarithm of a microstate count*. That is the deepest payoff of learning to count.

---

## 4. Worked examples

### Example 1 — Two coupled Einstein solids reach equilibrium

An **Einstein solid** models a crystal as $N$ independent oscillators sharing $q$ quanta of energy. The number of ways to distribute $q$ indistinguishable quanta among $N$ distinguishable oscillators is a "stars and bars" count — arrange $q$ stars (quanta) and $N-1$ bars (dividers) in a row:
$$
\Omega(N,q) = \binom{q+N-1}{q}.
$$
Now put two such solids, A and B, in thermal contact, free to exchange a fixed total of $q_{\text{tot}}$ quanta. The total multiplicity for a split $(q_A, q_B = q_{\text{tot}}-q_A)$ is the product $\Omega_A(q_A)\,\Omega_B(q_B)$. Evaluating this product across all splits, you find it is sharply peaked at one particular division — and that peak gets dramatically sharper as $N$ grows. The most probable split *is* thermal equilibrium, and the condition that the product be maximal,
$$
\frac{\partial \ln\Omega_A}{\partial q_A} = \frac{\partial \ln\Omega_B}{\partial q_B},
$$
is exactly the statement that the two solids have come to a *common temperature* ($\partial S/\partial E$ equal on both sides). Equilibrium and temperature both emerge from multiplying two combinatorial counts and finding the peak.

### Example 2 — Free expansion and the entropy of mixing

Let an ideal gas of $N$ molecules double its volume by expanding freely into vacuum. Each molecule now has twice as many accessible position-states, so the total multiplicity is multiplied by $2^N$:
$$
\Delta S = k\ln(2^N\Omega) - k\ln\Omega = kN\ln 2.
$$
For one mole, $N = N_A$, and $k N_A = R$, so $\Delta S = R\ln 2 \approx 5.76\ \mathrm{J/K}$. This is *exactly* the value the Clausius heat-integral $\int dQ_{\text{rev}}/T$ gives for the same process. The counting definition of entropy and the heat-engine definition agree to the last decimal — the cleanest demonstration that $S = k\ln\Omega$ is the same entropy that thermodynamics had all along.

### Example 3 — Counting changes when particles are identical (quantum statistics)

How many microstates exist depends on whether the particles are distinguishable. Put 2 particles into 2 states:
- **Distinguishable (Maxwell–Boltzmann):** $2^2 = 4$ microstates — particle labels matter.
- **Identical bosons (Bose–Einstein):** the particles are interchangeable and any number may share a state; the distinct configurations are {both in 1}, {both in 2}, {one in each} — only **3**.
- **Identical fermions (Fermi–Dirac):** interchangeable *and* no two may occupy the same state (Pauli exclusion); only {one in each} survives — just **1**.

The entire difference between classical and quantum statistics is a *counting* difference: what you are allowed to call a distinct microstate. The vanishing of the Slater determinant for two fermions in the same state is Pauli exclusion expressed as an algebraic fact about counting. (The full Bose–Einstein and Fermi–Dirac distributions belong to the quantum and thermal books; the *combinatorics* of the difference lives here.)

> **An honest sidebar — the Gibbs paradox.** For classical *identical* particles you must divide the naive count by $N!$ to avoid over-counting permutations of indistinguishable molecules; skip this and the entropy comes out non-extensive (the "Gibbs paradox"). Whether that $N!$ is a quantum fact or a classical bookkeeping convention is a genuine, still-discussed foundational question. For our purposes: divide by $N!$, and note that the cleanest justification for *why* is quantum indistinguishability.

---

## 5. Return to the cold open

The hundred tiny magnets are now fully under control. The number of microstates with $N_\uparrow$ up is $\binom{100}{N_\uparrow}$; it peaks at $N_\uparrow = 50$ with that 29-digit value, and the peak is so sharp that the system, exploring its equally-likely microstates, is overwhelmingly found near zero net magnetization. To turn the count into thermodynamics we take its logarithm — $S = k\ln\binom{N}{N_\uparrow}$ — and to evaluate that for real $N \sim 10^{23}$ we apply Stirling, $\ln N! \approx N\ln N - N$, which converts the intractable factorial into a smooth function of $N_\uparrow$ that we can differentiate. Differentiating $\ln\Omega$ with respect to energy gives $1/T$; the most probable macrostate gives equilibrium; and the same machinery, applied to a system in contact with a reservoir, hands us the Boltzmann distribution that Chapter 8 took on faith.

The postulate the thermodynamics book made — all microstates equally likely — combined with the arithmetic of $\binom{N}{N_\uparrow}$ and the smoothing of Stirling, *is* statistical mechanics. There was no extra physics smuggled in. There was only counting, a logarithm, and a derivative.

---

## 6. Where it generalizes

The one move — *count the microstates, take the logarithm* — generates entropy, temperature, and the Boltzmann distribution. It reaches much further:

- **Information theory.** Shannon's entropy $H = -\sum_i p_i \log p_i$ is the same logarithm-of-a-count, generalized to non-uniform probabilities; in the equal-probability case it reduces to $\log\Omega$. Entropy as "missing information" and entropy as "log of microstate count" are one idea.
- **Black-hole thermodynamics.** The Bekenstein–Hawking entropy assigns a black hole an entropy proportional to its horizon area in Planck units — a microstate count for gravity, and one of the deepest open problems in physics is *what* those microstates are.
- **The de Moivre connection.** The sharply-peaked multiplicity of §3.2, expanded near its maximum, *is* a Gaussian — which is precisely the de Moivre–Laplace argument of Chapter 8 seen from the counting side. The bell curve of measurement error and the peak of equilibrium are the same mathematics.

The judgment no symbolic engine can supply is the modeling step: **deciding what counts as a microstate.** Is the spin pattern the microstate and the magnetization the macrostate? Are the particles distinguishable? The entire physical content lives in that choice. A computer will evaluate $\binom{n}{k}$ flawlessly; it will not tell you *what to count*.

---

## Exercises

1. **(Enumerate, then formula.)** A system has 5 distinguishable boxes and you place 3 identical balls so that no box holds more than one. List all the arrangements by hand, then confirm your count equals $\binom{5}{3}$. Now repeat allowing any number of balls per box (stars and bars) and compare.

2. **(The key derivation.)** Derive $\ln N! \approx N\ln N - N$ by approximating $\sum_{m=1}^N \ln m$ with $\int_1^N \ln x\,dx$ and integrating by parts. Then, for $N = 60$, compare your approximation to the exact $\ln 60!$ and report the relative error. Explain why the error shrinks as $N$ grows.

3. **(Multiplicity and its peak.)** For the two-state paramagnet with $N = 20$, compute $\Omega(N, N_\uparrow)$ for $N_\uparrow = 10$ and for $N_\uparrow = 15$. By what factor is the central macrostate more probable than the off-center one? Argue qualitatively how this ratio behaves as $N\to 10^{23}$.

4. **(Counting to a distribution.)** Reproduce the derivation of the Boltzmann factor in §3.5 in your own words, justifying each step. Identify precisely where the first-order Taylor expansion is used and why $\partial\ln\Omega_R/\partial E$ may be treated as constant.

5. **(Conceptual.)** A student says "entropy is disorder." Replace this with the counting definition and explain, using free expansion ($\Delta S = R\ln 2$), why "the number of accessible microstates increased" is both more precise and more useful than "the gas got more disordered."

---

## Sources

- J. Stirling, *Methodus Differentialis* (1730) — the asymptotic factorial series and the constant $\sqrt{2\pi}$.
- A. de Moivre, *Miscellanea Analytica* (1730) — the form $N! \approx C\,N^{N+1/2}e^{-N}$ prior to Stirling's identification of $C$.
- L. Boltzmann, "Über die Beziehung zwischen dem zweiten Hauptsatze… und der Wahrscheinlichkeitsrechnung," *Wiener Berichte* 76:373–435 (1877) — microstate counting and $S \propto \ln W$. (English translation, *Entropy* (MDPI), 2015. [verify])
- M. Planck, *Vorlesungen über die Theorie der Wärmestrahlung* (1906) — the constant $k$ named for Boltzmann and the form $S = k\log W$.
- J. W. Gibbs, *Elementary Principles in Statistical Mechanics* (1902) — ensemble counting and the entropy–probability relation.
- B. Pascal, *Traité du triangle arithmétique* (1665, posthumous), and the Pascal–Fermat correspondence (1654) — the binomial coefficient and the triangle. Earlier appearances: Yang Hui (c. 1238–1298), Jia Xian (~1100), and al-Karaji in the Islamic tradition.
- D. V. Schroeder, *An Introduction to Thermal Physics* — the standard modern treatment of the two-state paramagnet and the Einstein solid (paramagnet, Einstein-solid, and free-expansion examples). [verify edition/pages]
- In-series: *Physics — Thermodynamics* ch. 07 (free expansion; the two definitions of entropy agreeing at $R\ln 2$) and ch. 08 (microstates/macrostates, the fundamental postulate, the Boltzmann distribution by counting); *Physics — Quantum Mechanics* ch. 08 (Slater determinant, Pauli exclusion as a counting corollary, composite-particle parity).
