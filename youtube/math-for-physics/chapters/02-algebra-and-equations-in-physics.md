# Algebra and Equations in Physics

*Solving for the symbol before the number — and reading what the symbol tells you.*

## Cold open: two blocks, one rope, and a question the number cannot answer

Two blocks hang over a frictionless pulley on a single rope — the classic Atwood machine. One block has mass $m_1$, the other $m_2$. Released, the system accelerates: the heavier block falls, the lighter rises. The exam question gives you numbers — $m_1 = 3$ kg, $m_2 = 5$ kg — and asks for the acceleration. You could plug in and grind out a number. Most students do.

But suppose the real question is the one that matters: *what happens when the two masses are equal?* Or *what happens when one mass is enormous compared to the other?* A number cannot answer that. Only the symbolic solution — $a$ written in terms of $m_1$ and $m_2$, before any numbers are substituted — can be *read* for its meaning. And here is the unsettling research finding that frames this whole chapter: intro-physics students reliably do *worse* on the symbolic version of a problem than on a numerically identical one. The gap is not arithmetic. It is a misunderstanding of what a variable *is*. This chapter is about the most undervalued skill in all of physics: solving for the symbol, and then reading it.

## The tool, named

The tool is **algebra used as reasoning about relations among quantities**, with three disciplines layered on top:

1. **Symbolic manipulation** — isolating an unknown in a multi-term relation by operating identically on both sides of an equation, *before* substituting numbers.
2. **Reading the symbolic result** — extracting meaning from the answer by checking limits, units, and proportionalities.
3. **Proportional and scaling reasoning** — recognizing when one quantity varies as a power of another, and reasoning multiplicatively rather than additively.

The word *algebra* itself comes from the Arabic *al-jabr* — "restoring" or "balancing" — from al-Khwarizmi's ninth-century treatise. The image is exact: an equation is a balance, and you may do anything to it so long as you do the same thing to both sides.

## Development and derivation

### The equals sign is a balance, not a button

The first and most stubborn misconception is reading "$=$" as "compute the answer" — the calculator-button meaning — rather than as "is equivalent to." If $=$ means "equivalent," then the legitimate moves are obvious: whatever you do to the left, do to the right, and equivalence is preserved. Add the same term to both sides. Multiply both sides by the same nonzero quantity. Take the same function of both sides. That is the entire mechanical content of equation-solving, and it is al-Khwarizmi's *al-jabr* — balancing — made into a rule.

### Isolating a variable in a multi-term relation

Solving for an unknown means peeling away everything attached to it, in reverse order, by inverse operations. Consider the kinematic relation $v^2 = v_0^2 + 2as$, and suppose we want $a$:

$$v^2 = v_0^2 + 2as \;\Rightarrow\; v^2 - v_0^2 = 2as \;\Rightarrow\; a = \frac{v^2 - v_0^2}{2s}.$$

Each arrow is one balanced move: subtract $v_0^2$ from both sides, then divide both sides by $2s$. The result is *general* — it holds for every $v$, $v_0$, $s$ — which is exactly what makes it more valuable than any single number.

### The central derivation: the Atwood machine, symbolically

Two masses, $m_1$ and $m_2$, connected by a rope of negligible mass over a frictionless, massless pulley. Take $m_2 > m_1$, so $m_2$ falls and $m_1$ rises, both with the same magnitude of acceleration $a$ (the rope is inextensible), and the same rope tension $T$ throughout.

Apply Newton's second law to each block, choosing the positive direction along the direction each will actually move:

$$\text{Falling block } m_2:\quad m_2 g - T = m_2 a,$$
$$\text{Rising block } m_1:\quad T - m_1 g = m_1 a.$$

Two equations, two unknowns ($a$ and $T$). The cleanest move is to *add* them, which eliminates the tension:

$$(m_2 g - T) + (T - m_1 g) = m_2 a + m_1 a$$
$$m_2 g - m_1 g = (m_1 + m_2)a$$
$$\boxed{\,a = \frac{(m_2 - m_1)\,g}{m_1 + m_2}\,.}$$

Now — and this is the whole point of the chapter — we *read* it.

**Limiting case 1: equal masses.** Set $m_1 = m_2$. The numerator vanishes, so $a = 0$. Equal masses balance; nothing accelerates. The symbol told us this instantly. A number never could.

**Limiting case 2: one mass vanishes.** Let $m_1 \to 0$. Then $a \to m_2 g / m_2 = g$. With nothing on the other end, $m_2$ simply free-falls at $g$. Correct, and reassuring — the formula reduces to known physics at its edges.

**Units check.** The numerator $(m_2 - m_1)g$ has dimension $M \cdot LT^{-2}$ (a force); the denominator $m_1 + m_2$ has dimension $M$. The ratio has dimension $LT^{-2}$ — an acceleration. The answer survives a dimensional check, which it could not have if we had botched the algebra.

Three independent confirmations — two limits and a units check — and not one of them required a number. That is what "solve symbolically first" buys you: an answer you can interrogate.

![Atwood machine diagram with two masses over a pulley and the boxed symbolic acceleration a = (m₂−m₁)g/(m₁+m₂), read at its limits: equal masses give a=0, a vanishing mass gives a→g, and the acceleration is always less than g.](images/02-algebra-and-equations-in-physics-fig-01.png)
*Figure 2.1 — The symbolic solution answers questions about the machine — equal masses, a vanishing mass, the ceiling at g — that no single number could.*

### Proportionality and scaling laws

The simplest nontrivial relation between two quantities is *proportionality*, $y = kx$: double $x$, double $y$. The general power-law form is $y = kx^n$. The reasoning these demand is **multiplicative**, and this is where students most often go wrong. Asked "if 3 items cost \$12, what do 5 cost?", many *add* (\$12 + \$2) instead of *scaling* ($\$12 \times \tfrac{5}{3}$). The additive instinct is the single most documented error in proportional reasoning. The fix is to always ask: *by what factor did the input change, and to what power does the output respond?*

**Worked derivation: the spring period.** A mass on a spring oscillates with period $T = 2\pi\sqrt{m/k}$ (derived in Chapter 11; take it as given here). Read it as a scaling law. Quadruple the mass:

$$T(4m) = 2\pi\sqrt{\frac{4m}{k}} = 2\sqrt{\,}\cdot 2\pi\sqrt{\frac{m}{k}} = 2\,T(m).$$

Because $T \propto \sqrt{m}$, multiplying the mass by 4 multiplies the period by $\sqrt{4} = 2$. No number was needed; the *exponent* $\tfrac{1}{2}$ did the work.

### Galileo's square–cube law: scaling as a physical argument

The oldest and cleanest scaling argument predates calculus. Galileo (*Two New Sciences*, 1638) asked why nature cannot build a giant simply by scaling an animal up uniformly. For a shape scaled by a linear factor $L$, geometry forces:

$$\text{area} \propto L^2, \qquad \text{volume} \propto L^3.$$

A bone's *strength* is set by its cross-sectional area, so strength $\propto L^2$. The animal's *weight* is set by its volume, so weight $\propto L^3$. The stress the bones must bear is weight divided by cross-section:

$$\text{stress} = \frac{\text{weight}}{\text{cross-section}} \propto \frac{L^3}{L^2} = L.$$

Stress grows in direct proportion to size. Double an animal's linear dimensions and its bones must bear twice the stress; they will fail unless they grow disproportionately thick. This is *why* an elephant cannot have a gazelle's slender legs — and the entire argument is three lines of proportional algebra, no calculus, no numbers.

![Square-cube scaling: doubling a cube's side multiplies cross-sectional area by 4 and volume (weight) by 8, so stress = weight/cross-section scales as L³/L² = L, doubling.](images/02-algebra-and-equations-in-physics-fig-02.png)
*Figure 2.2 — Area scales as L², volume as L³, so stress grows in direct proportion to size — why nature cannot simply scale an animal up.*

## Worked examples

### Example 1 — Block on an incline, solved symbolically

A block on a ramp inclined at angle $\theta$, with coefficient of kinetic friction $\mu$, slides down. Resolving forces along the slope (the trigonometry of this decomposition is the subject of Chapter 3; here we use the result), Newton's second law gives:

$$mg\sin\theta - \mu m g\cos\theta = ma.$$

The mass $m$ appears in every term — so divide it out, and watch it vanish:

$$a = g(\sin\theta - \mu\cos\theta).$$

**Read it.** The mass cancelled: the acceleration of a sliding block does not depend on how heavy it is — a result worth pausing on. And the *condition for sliding at all* drops out directly: the block accelerates only if $a > 0$, i.e. $\sin\theta > \mu\cos\theta$, i.e.

$$\tan\theta > \mu.$$

The block slips once the slope's tangent exceeds the friction coefficient. That clean criterion is invisible in any numerical answer; it is *given* by the symbolic one.

![Block on an incline at angle θ with the driving component mg sinθ and resisting friction μmg cosθ; an inset shows the slip threshold tanθ > μ and the critical angle θ_c = arctan μ.](images/02-algebra-and-equations-in-physics-fig-03.png)
*Figure 2.3 — Dividing out the mass leaves a = g(sinθ − μcosθ); the block slips precisely when tanθ exceeds μ.*

### Example 2 — The additive bug, caught

A recipe for 4 people needs 600 g of flour; you are cooking for 6. The additive (wrong) reasoning: "6 is 2 more than 4, so add 2 people's worth." But you do not know "a person's worth" independently — that *is* the ratio you are trying to use. The multiplicative (correct) reasoning: the scale factor is $6/4 = 1.5$, so flour $= 600 \times 1.5 = 900$ g. The discipline is to identify the factor first and apply it to the whole quantity.

### Example 3 — Static equilibrium as two equations in two unknowns

A static problem — a beam, a ladder, a hanging pan — gives you two independent constraints: the forces sum to zero ($\sum \vec{F} = 0$) and the torques sum to zero ($\sum \tau = 0$). Consider a pan of weight $w$ hanging from two strings at different angles, with tensions $T_1$ and $T_2$. Horizontal and vertical force balance give two linear equations:

$$T_1\sin\theta_1 = T_2\sin\theta_2, \qquad T_1\cos\theta_1 + T_2\cos\theta_2 = w.$$

From the first, $T_2 = T_1\sin\theta_1/\sin\theta_2$; substitute into the second and isolate $T_1$:

$$T_1\cos\theta_1 + T_1\frac{\sin\theta_1}{\sin\theta_2}\cos\theta_2 = w \;\Rightarrow\; T_1 = \frac{w}{\cos\theta_1 + \sin\theta_1\cot\theta_2}.$$

Once $T_1$ is known, back-substitute for $T_2$. This *substitution-and-back-substitution* method is exactly how you solve any small system of linear equations by hand — and it is the seed of the matrix methods in Chapter 10, which mechanize it for systems too large to juggle this way.

## Return to the cold open

The Atwood machine's symbolic solution, $a = (m_2 - m_1)g/(m_1+m_2)$, answered the questions the number could not. Equal masses: $a = 0$. One mass vanishing: $a \to g$. And we can now read a third feature for free: the acceleration can never exceed $g$, because $(m_2 - m_1) < (m_1 + m_2)$ always, so the fraction is always less than one. The system is *always* gentler than free fall. A student who plugged in $m_1 = 3$, $m_2 = 5$ and reported $a = 2.45\ \text{m/s}^2$ has a number; a student who derived and read the symbol has *understood the machine* — and could answer any question about it, for any masses, forever. That is the difference the education research measures, and it is the difference this book exists to teach.

## Where it generalizes

Reading a relation by taking its limits and checking its proportionalities is a universal move. In chemistry, the same skill reads a rate law to see which reactant controls the speed. In finance, it reads a compound-interest formula to see what dominates over long horizons. In any field, the symbolic answer is the one you can interrogate; the numerical answer is the one you can only report. A modern solver — Wolfram Alpha, a large language model — will happily hand you $a = (m_2-m_1)g/(m_1+m_2)$. What it will not do for you is *notice that equal masses give zero*, or *choose which limit is the one that matters for your problem*. That interpretive reading is the human skill, and it is exactly what the symbol-pushing tools do not supply.

The scaling laws point forward in two directions: to log–log plots and power-law exponents in Chapter 5 (where scaling becomes a graphical tool), and outward to D'Arcy Thompson's *On Growth and Form*, where the same algebra of proportionality governs bone thickness, metabolic rate, and the strength of a beam. The two-equations-in-two-unknowns method points forward to Chapter 10, where matrices turn it into a systematic procedure. (One honest caveat: some research argues that *numbers* scaffold meaning for novices and that symbolic fluency should be built gradually rather than demanded up front `[contested — see pantry]`. This book takes the symbol-first side, but the goal is the *reading* of the symbol, not symbol-pushing for its own sake.)

## Exercises

1. **(Isolate)** Solve $v = v_0 + at$ for $t$, then for $a$. State each balancing move.

2. **(Read a symbol)** From the incline result $a = g(\sin\theta - \mu\cos\theta)$, find the angle at which a block is on the verge of sliding, in terms of $\mu$. What is this angle called?

3. **(Derivation)** Derive the Atwood acceleration $a = (m_2-m_1)g/(m_1+m_2)$ from the two force equations, then verify it in *both* limiting cases and by a dimensional check. Show every step.

4. **(Scaling)** Kinetic energy is $KE = \tfrac{1}{2}mv^2$. By what factor does the stopping distance (proportional to $KE$ for constant braking force) change if a car's speed triples? Reason multiplicatively and state the exponent you used.

5. **(Square–cube)** A cube of side $L$ is scaled to side $2L$. By what factor does its surface area change? Its volume? Use these to explain why small animals lose body heat faster than large ones.

## Sources

- Muhammad ibn Musa al-Khwarizmi, *al-Kitab al-mukhtasar fi hisab al-jabr wa'l-muqabala* (c. 820); etymology of "algebra" from *al-jabr*.
- Galileo Galilei, *Dialogues Concerning Two New Sciences* (1638) — the square–cube law.
- M. A. Peterson, "Galileo's Discovery of Scaling Laws," *American Journal of Physics* 70, 575 (2002). `[verify]`
- E. T. Torigoe & G. E. Gladding, "Symbols are not numbers" / "How numbers help students solve physics problems," (2011). `[verify]`
- F. Tourniaire & S. Pulos, "Proportional reasoning: A review of the literature," *Educational Studies in Mathematics* 16 (1985).
- D'Arcy Wentworth Thompson, *On Growth and Form* (1917).
