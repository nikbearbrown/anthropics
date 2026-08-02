# Units, Dimensions, and Estimation

*The math of quantity itself — what a number must carry before it can mean anything.*

## Cold open: a spacecraft that was in the wrong place

On 23 September 1999, after nine months and 670 million kilometers, the Mars Climate Orbiter fired its engine to slip into orbit around Mars. It came in about 100 kilometers too low, grazed the upper atmosphere at the wrong angle, and broke apart. The mission cost roughly $327 million.

The investigation found no broken hardware and no software crash. One program, built by the spacecraft's manufacturer, reported the small thruster impulses in *pound-force-seconds*. The navigation software at the Jet Propulsion Laboratory read those numbers as *newton-seconds*. A pound-force is about 4.45 newtons, so every impulse was off by a factor of 4.45, and the trajectory drifted, undetected, until Mars was in the way.

No equation was wrong. No arithmetic was wrong. What was missing was the thing a number must carry before it can mean anything at all: its *unit*, and behind the unit, its *dimension*. This chapter is about the mathematics of quantity itself — how to track what a number measures, how to check that an equation could even be true, how to know how much of a number you actually believe, and how to estimate a quantity you cannot measure. None of it is decoration. The Mars Climate Orbiter is the proof.

## The tool, named

A measured quantity is not a pure number. It is a number times a unit, and behind the unit stands a **dimension** — a statement of *what kind* of thing is being measured: a length, a time, a mass, or some product of these. Four distinct mathematical skills live in this chapter, and they are more general than physics:

1. **Dimensional analysis** — treating dimensions as algebraic objects so that an equation's *form* can be checked, and sometimes *derived*, before any number appears.
2. **Significant figures** — a coarse encoding of how precisely a quantity is known.
3. **Uncertainty propagation** — the rule for how the imprecision in inputs flows into the imprecision of a result.
4. **Order-of-magnitude estimation** — building a believable number for a quantity you cannot measure directly.

The deepest of these is the first, so we build it most carefully.

## Development and derivation

### Dimensions as algebra

In mechanics, every quantity's dimension is built from three base dimensions: length $L$, mass $M$, and time $T$. (The full SI system has seven base dimensions, adding temperature, electric current, amount of substance, and luminous intensity, but mechanics needs only three.) We write the dimension of a quantity $q$ with square brackets, $[q]$. Then:

$$[\text{length}] = L, \quad [\text{time}] = T, \quad [\text{mass}] = M,$$

$$[\text{speed}] = \frac{L}{T} = LT^{-1}, \quad [\text{acceleration}] = LT^{-2}, \quad [\text{force}] = MLT^{-2}.$$

That last one comes straight from $F = ma$: $[F] = [m][a] = M \cdot LT^{-2}$. Dimensions multiply and divide like ordinary algebraic symbols, and crucially, **only quantities of the same dimension can be added, subtracted, or set equal.** You cannot add a length to a time any more than you can add three apples to two hours. This is the *principle of dimensional homogeneity*, and it is the engine of everything that follows.

### Dimensional consistency as a constraint on equations

The principle gives us a free error-check. Take a candidate kinematic relation, $s = \tfrac{1}{2}at^2$, where $s$ is a distance, $a$ an acceleration, $t$ a time. Check the dimensions of each side:

$$[s] = L, \qquad \left[\tfrac{1}{2}at^2\right] = [a][t]^2 = LT^{-2} \cdot T^2 = L.$$

Both sides are a length. The equation *could* be true. The factor $\tfrac{1}{2}$ is a pure number and carries no dimension, so dimensional analysis cannot confirm it — but it can never be the source of a dimensional error. Now take a *wrong* candidate, $s = \tfrac{1}{2}at$:

$$\left[\tfrac{1}{2}at\right] = LT^{-2} \cdot T = LT^{-1}.$$

That is a speed, not a length. The equation is *impossible*, and we knew it without solving anything. This is the practical payoff: **a dimensionally inconsistent equation is certainly wrong; a consistent one is merely allowed.** Consistency is a necessary, not a sufficient, condition for truth.

![Side-by-side dimension check of two candidate kinematic equations: s = ½at² is consistent (both sides L) while s = ½at is impossible (right side is a speed, LT⁻¹).](images/01-units-dimensions-and-estimation-fig-01.png)
*Figure 1.1 — A dimensionally inconsistent equation is certainly wrong; consistency is necessary, not sufficient.*

### From checking to deriving: the count of dimensionless groups

Dimensional analysis does something stronger than catch errors — it can hand you the *form* of an answer before you do any physics. The precise statement is the **Buckingham $\Pi$-theorem** (Buckingham, 1914; the result predates him — more on that below): *any physically meaningful relation among $n$ dimensioned variables, built from $k$ independent base dimensions, can be rewritten as a relation among exactly $n - k$ dimensionless products.* [verify — Buckingham 1914]

The theorem is, underneath, a fact of linear algebra. Write each variable's dimensions as a column of exponents over the base dimensions; the dimensionless products are the null space of the resulting matrix, and $n-k$ is its nullity. We will not prove the general theorem, but we can execute its elementary form — Rayleigh's "method of dimensions" — by hand.

**Worked derivation: the period of a pendulum.** What sets the period $T_p$ of a swinging pendulum? Plausibly the length $\ell$, the gravitational acceleration $g$, and the bob's mass $m$. Assume the period is a product of powers:

$$T_p = C\,\ell^{a}\, g^{b}\, m^{c},$$

where $C$ is a dimensionless constant. Now demand dimensional consistency. The left side has dimension $T$. The right side:

$$[\ell^a g^b m^c] = L^{a}\,(LT^{-2})^{b}\, M^{c} = L^{a+b}\, T^{-2b}\, M^{c}.$$

Match the exponent of each base dimension on both sides:

- Mass: $c = 0$ — *the mass does not matter.*
- Time: $-2b = 1 \Rightarrow b = -\tfrac{1}{2}$.
- Length: $a + b = 0 \Rightarrow a = \tfrac{1}{2}$.

So

$$T_p = C\,\ell^{1/2}\, g^{-1/2} = C\sqrt{\frac{\ell}{g}}.$$

![Exponent-matching derivation of the pendulum period: assuming Tp = C·ℓᵃgᵇmᶜ and matching the L, M, T exponents gives c=0, b=−½, a=½, so Tp = C√(ℓ/g).](images/01-units-dimensions-and-estimation-fig-02.png)
*Figure 1.2 — Matching the exponent of each base dimension fixes the form of the pendulum period; only the pure number C is left to the physics.*

We have derived that the period grows as the square root of the length and shrinks as the square root of $g$, and that it is independent of mass — without writing a single equation of motion. The one thing dimensions cannot give us is the pure number $C$; the full theory (Chapter 11) will show $C = 2\pi$. Notice what was *not* mechanical: deciding that $\ell$, $g$, and $m$ were the relevant variables. That choice is physical judgment. The theorem tells you how many groups exist *once you have chosen the variables*; choosing them well is the irreducibly human part.

### Significant figures, honestly

A measurement carries a number *and* a statement of how well that number is known. Significant figures are the crude, built-in version of that statement. When you write $1.50$ m, you are claiming to know the length to the hundredths place — three significant figures. When you write $1.5$ m, you are claiming only two. The trailing zero in $1.50$ is *significant*: it is a promise, not a placeholder.

It helps to see significant figures for what they actually are — a coarse encoding of **relative uncertainty**. A number written to three significant figures is known to roughly one part in a few hundred, i.e. to about $\pm 0.5\%$. This is why the rituals you may have memorized work: when you multiply or divide, the result keeps the *fewest* significant figures of any input, because relative uncertainties combine, and the sloppiest input dominates. Treat significant figures as a shorthand for "how much of this do I believe," not as a bureaucratic rule, and the rules stop being arbitrary. (Whether to teach significant figures at all, versus always stating an explicit $\pm$, is genuinely contested among metrology educators `[contested — see pantry]`; this book's position is that significant figures are a useful shorthand precisely *because* they encode relative uncertainty, and should be taught as such.)

### Propagating uncertainty through products and powers

Now the real rule, derived. Suppose a result $q$ is computed from measured quantities, each with a small uncertainty. We want the uncertainty in $q$. The key idea: for a quantity built by multiplication, division, and powers, **relative uncertainties combine**, weighted by exponents.

Take the most useful case, a product of powers:

$$q = A^{m} B^{n}.$$

Take the natural logarithm of both sides — this is the trick that turns products into sums:

$$\ln q = m \ln A + n \ln B.$$

Now take the differential of each side (the differential $d$ tracks a small change):

$$\frac{dq}{q} = m\,\frac{dA}{A} + n\,\frac{dB}{B}.$$

Reading $dq/q$ as the relative uncertainty in $q$, this says: **the relative uncertainty in a product of powers is the sum of the input relative uncertainties, each multiplied by its exponent.** A power of $n$ multiplies the relative uncertainty by $|n|$. That single fact is the whole rule.

A subtlety: this linear sum is the *worst case*, assuming the errors conspire. If the errors in $A$ and $B$ are *independent* — which is common — they partly cancel on average, and the right combination is the square root of the sum of squares (combination "in quadrature"):

$$\frac{\delta q}{q} = \sqrt{\left(m\,\frac{\delta A}{A}\right)^2 + \left(n\,\frac{\delta B}{B}\right)^2}.$$

Both the linear (worst-case) and the quadrature (statistical) combinations are used; which is correct depends on whether the errors are independent `[contested — see pantry]`. We will use the simpler linear sum for hand estimates and note where quadrature would soften the result.

### Order-of-magnitude estimation

Sometimes you cannot measure a quantity, and an exact formula does not exist or is not worth the trouble. The mathematical skill is to *decompose* the unknown into factors you can each estimate to within a factor of ten, estimate each, and recombine. The art is in the decomposition; the arithmetic is trivial. A useful tool when you have a low bound $x_{\text{lo}}$ and a high bound $x_{\text{hi}}$ is the **geometric mean**, $\sqrt{x_{\text{lo}}\,x_{\text{hi}}}$ — the natural "middle" on a logarithmic scale, where order-of-magnitude reasoning lives.

## Worked examples

### Example 1 — Converting and checking a density

The density of aluminum is given as $2.7\ \text{g/cm}^3$. Convert to SI ($\text{kg/m}^3$) by multiplying by conversion factors arranged so the unwanted units cancel:

$$2.7\,\frac{\text{g}}{\text{cm}^3} \times \frac{1\ \text{kg}}{1000\ \text{g}} \times \frac{10^6\ \text{cm}^3}{1\ \text{m}^3} = 2700\,\frac{\text{kg}}{\text{m}^3}.$$

(The $10^6$ comes from $1\ \text{m}^3 = (100\ \text{cm})^3 = 10^6\ \text{cm}^3$ — a place students routinely lose a factor of 100, because they cube the length conversion but forget to cube it everywhere.) The dimension is $M/L^3$ on both sides. Consistent.

### Example 2 — Uncertainty in a volume from a measured diameter

You measure a sphere's diameter as $d = 5.2 \pm 0.1$ cm and want its volume, $V = \tfrac{\pi}{6}d^3$. The volume depends on $d$ to the *third* power, so by the rule above the relative uncertainty in $V$ is three times the relative uncertainty in $d$:

$$\frac{\delta d}{d} = \frac{0.1}{5.2} = 1.9\%, \qquad \frac{\delta V}{V} = 3 \times 1.9\% = 5.8\%.$$

The central value is $V = \tfrac{\pi}{6}(5.2)^3 = 73.6\ \text{cm}^3$, so $\delta V = 0.058 \times 73.6 = 4.3\ \text{cm}^3$, and you report $V = 73.6 \pm 4.3\ \text{cm}^3$. The lesson is the factor of 3: a cube *amplifies* the imprecision of its input threefold.

![Bar chart comparing a 1.9% relative uncertainty in a measured diameter to the resulting 5.8% relative uncertainty in the volume, which depends on the cube of the diameter — a factor-of-3 amplification.](images/01-units-dimensions-and-estimation-fig-03.png)
*Figure 1.3 — A power of 3 multiplies the relative uncertainty by 3: the exponent, not the arithmetic, sets the imprecision.* If the volume came instead from independently measured length, width, and height, you would combine three relative uncertainties — in quadrature if they were independent.

### Example 3 — A Fermi estimate

Enrico Fermi, at the first nuclear test in July 1945, dropped scraps of paper as the blast wave passed and estimated the yield from how far they blew — landing on roughly 10 kilotons, the right order of magnitude. (The exact figure he cited varies across retellings; treat it as approximate `[verify]`.) The method is the lesson. Estimate the number of air molecules in a typical room ($\sim 4\ \text{m} \times 4\ \text{m} \times 3\ \text{m} \approx 50\ \text{m}^3$). At room conditions a mole of gas occupies about $0.024\ \text{m}^3$, so the room holds about $50/0.024 \approx 2 \times 10^3$ moles, and at $6 \times 10^{23}$ molecules per mole that is about $1 \times 10^{27}$ molecules. We claim only the exponent; the leading digit is not to be believed, and saying so *is* the discipline.

## Return to the cold open

The Mars Climate Orbiter was a units failure, and units failures are exactly what dimensional bookkeeping prevents. The thruster impulse has dimension $[F][t] = MLT^{-2}\cdot T = MLT^{-1}$, an impulse. Both pound-force-seconds and newton-seconds have that dimension — which is precisely why a pure dimensional check would *not* have caught this error. Dimensions were consistent; only the *numerical scale of the unit* differed, by the factor $1\ \text{lbf} = 4.45\ \text{N}$.

This sharpens the chapter's central distinction. Dimensional analysis guarantees you are adding lengths to lengths; it does not guarantee you are using the *same* length unit. The fix is the second discipline of this chapter: carry the unit explicitly through every line, as an algebraic factor, so that the conversion $\times\,4.45$ is forced to appear or its absence becomes visible. Had the impulses been carried as "$x\ \text{lbf·s}$" and the navigation code demanded "$y\ \text{N·s}$," the missing conversion factor would have been a syntactic gap, not a silent factor of 4.45. The $327 million lesson: a dimension tells you *what kind* of quantity; a unit tells you *which yardstick*; you must track both.

## Where it generalizes

The $\Pi$-theorem is not a physics fact — it is linear algebra, the null space of an exponent matrix, and it works identically wherever quantities have dimensions. Biologists use it for allometric scaling (why metabolic rate scales as roughly the $3/4$ power of body mass); engineers use it to design scale models (the Reynolds number is a dimensionless $\Pi$ group); machine-learning researchers "non-dimensionalize" a loss function to compare runs at different scales. The skill of *deciding which variables matter* — the human step the theorem cannot supply — is the same skill everywhere. Uncertainty propagation is the foundation of all experimental science and of metrology (see the GUM, the international Guide to the Expression of Uncertainty in Measurement). And the square-root scaling we pulled from the pendulum is your first encounter with a **scaling law** — the subject of the next chapter, where proportional reasoning becomes a tool in its own right, and a preview of simple harmonic motion in Chapter 11.

A note on provenance, because it is a clean lesson: the "$\Pi$-theorem" is named for Buckingham (1914), but Joseph Bertrand proved special cases in 1878 and Aimé Vaschy gave a general statement in 1892. The result is named for the popularizer, not the originator — a pattern you will meet again. `[contested — see pantry]`

## Exercises

1. **(Check)** Is $v^2 = 2as$ dimensionally consistent, where $v$ is a speed, $a$ an acceleration, $s$ a distance? Show each side's dimension.

2. **(Convert)** A car travels at 65 miles per hour. Express this in m/s, carrying units as algebraic factors so each cancellation is visible. (Use $1\ \text{mile} = 1609\ \text{m}$.)

3. **(Derivation)** A mass $m$ on a spring of stiffness $k$ (units N/m) oscillates with period $T$. Using only dimensional analysis, derive how $T$ depends on $m$ and $k$. (You should find $T \propto \sqrt{m/k}$.) State explicitly which variable, if any, you judged irrelevant and why.

4. **(Uncertainty)** You measure the side of a square as $s = 5.3 \pm 0.2$ cm. Find the area and its uncertainty using the relative-uncertainty rule, and state the result as $A \pm \delta A$.

5. **(Estimate)** Estimate the number of piano tuners in a city of one million people. Lay out your decomposition into factors explicitly, and state which factor you are least sure of.

## Sources

- Edgar Buckingham, "On Physically Similar Systems; Illustrations of the Use of Dimensional Equations," *Physical Review* 4, 345 (1914).
- Lord Rayleigh (J. W. Strutt), *The Theory of Sound* (1877); and his "method of dimensions."
- A. Vaschy (1892); Joseph Bertrand (1878) — priority of the $\Pi$-theorem (via standard histories of dimensional analysis). `[verify]`
- BIPM, *The International System of Units (SI)*, 9th edition (2019); NIST Special Publication 330 (2019).
- B. N. Taylor & C. E. Kuyatt, NIST Technical Note 1297 (1994); JCGM 100:2008, *Guide to the Expression of Uncertainty in Measurement* (GUM).
- NASA, *Mars Climate Orbiter Mishap Investigation Board Phase I Report* (1999).
