# Multivariable Calculus and Partial Derivatives in Depth

*Thermodynamics is multivariable calculus with physical names attached — and the famous relations are just the theorem that mixed partials are equal.*

## The cold open: why is heat written with a slash?

Open a thermodynamics book to the first law and you find an asymmetry that the book may not pause to explain. The change in a gas's internal energy is written $dU$, an ordinary differential. But the heat added and the work done are written $\delta Q$ and $\delta W$ — with a slash through the $d$, or a bar, or a different letter entirely. Why the special notation?

The textbook makes it concrete. Take a fixed quantity of ideal gas from a state $A$ to a state $B$ by two different routes. Route one: heat it at constant volume from $300\ \mathrm{K}$ to $400\ \mathrm{K}$, then let it expand at constant pressure. Route two: expand first, then heat. Measure carefully and you find that the change in internal energy is *identical* both ways — say $\Delta U = 4157\ \mathrm{J}$ — but the heat that flowed in is *different*: perhaps $4157\ \mathrm{J}$ along one path and $5822\ \mathrm{J}$ along the other. <!-- FACT-CHECK FLAG: [UNVERIFIED] — see factchecks/02-multivariable-calculus-and-partial-derivatives-assertions.md. Illustrative numbers attributed to the series thermodynamics book; qualitatively correct (ΔU path-independent, Q path-dependent) but the specific joule values are not independently verifiable. --> The internal energy depends only on *where you are* — on the state — while the heat depends on *how you got there* — on the path.

That distinction is the whole reason for the slash, and it is not physics. It is a statement about a class of mathematical objects called differentials: some are *exact* (they integrate to a function of state, independent of path) and some are *inexact* (they do not). $dU$ is exact; $\delta Q$ is inexact. Everything thermodynamics does with energy, entropy, and the free energies rests on this distinction, and on a handful of facts about derivatives of functions of several variables. This chapter builds that machinery and shows that the celebrated Maxwell relations are nothing but the theorem that mixed partial derivatives are equal.

## The tool, named

Volume 1 *introduced* partial derivatives — in the context of the wave equation and Fourier series — as the rate of change of a function of several variables with respect to one of them, the others held fixed. We assume that. What the advanced courses, thermodynamics above all, demand and Volume 1 did not develop is the full apparatus of **multivariable calculus for interdependent, constrained variables**: the total differential, the multivariable chain rule among variables that depend on each other, the precise distinction between **exact and inexact differentials**, the **Maxwell relations** that follow from the equality of mixed partials, the **Jacobian** for changing variables, and the **Legendre transform** that manufactures the thermodynamic potentials from one another. The single most important new habit is reading the subscript: $(\partial U/\partial T)_V$ and $(\partial U/\partial T)_P$ are different numbers, and forgetting which variable is held fixed is the most-documented error in all of thermal physics.

## Development and derivation

### Partial derivatives and the constraint subscript

A function of two variables $f(x,y)$ has two partial derivatives. The partial with respect to $x$,

$$\left(\frac{\partial f}{\partial x}\right)_y = \lim_{h\to 0}\frac{f(x+h,\,y) - f(x,y)}{h},$$

is the rate of change of $f$ as $x$ varies *with $y$ held fixed*. Geometrically, if $z = f(x,y)$ is a surface, this is the slope of the cross-section cut at constant $y$. In pure mathematics one usually writes $\partial f/\partial x$ and leaves the held-fixed variable implicit, because $x$ and $y$ are independent and there is nothing else to hold. In thermodynamics this laziness is fatal, because the variables are *interdependent*: a gas has variables $P, V, T, S, U, \dots$ linked by an equation of state and by the laws of thermodynamics, and you can describe the same state with many different pairs. So we *always* write the held-fixed variable as a subscript. $(\partial U/\partial T)_V$ — energy's response to temperature at fixed volume — is a genuinely different quantity from $(\partial U/\partial T)_P$, at fixed pressure, because in the second case the volume is free to change and carry energy with it.

### The total differential

If both variables change a little, the function changes by a sum of the two contributions. For a smooth $f(x,y)$, the **total differential** is

$$df = \left(\frac{\partial f}{\partial x}\right)_y dx + \left(\frac{\partial f}{\partial y}\right)_x dy.$$

This is the linear approximation to the change in $f$ for small displacements $dx, dy$, and it is the central object of the chapter. Read it as a bookkeeping statement: the total change in $f$ is the rate-times-displacement in the $x$-direction plus the rate-times-displacement in the $y$-direction.

![An oblique sketch of a surface z = f(x,y) with one marked point P. A cross-section curve at constant y has slope partial f by partial x; a cross-section at constant x has slope partial f by partial y; a side box gives the total differential as the sum of each slope times its displacement.](images/02-multivariable-calculus-and-partial-derivatives-fig-01.png)
*Figure 2.1 — A partial derivative is the slope of one cross-section of the surface; the total differential adds the two slope-times-displacement contributions.*

### The multivariable chain rule

Suppose $x$ and $y$ are themselves functions of a parameter $t$ (a path through the plane). Then $f$ varies with $t$ through both, and dividing the total differential by $dt$ gives the **chain rule**:

$$\frac{df}{dt} = \left(\frac{\partial f}{\partial x}\right)_y\frac{dx}{dt} + \left(\frac{\partial f}{\partial y}\right)_x\frac{dy}{dt}.$$

A consequence we will need repeatedly: the **triple product rule**. Take three variables $x, y, z$ constrained by one relation, so any one is a function of the other two. Holding $f$ — equivalently, moving along a curve of constant $z$ — one can show (by setting $dz = 0$ in $dz = (\partial z/\partial x)_y dx + (\partial z/\partial y)_x dy$ and rearranging) that

$$\left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial z}\right)_x\left(\frac{\partial z}{\partial x}\right)_y = -1.$$

The minus sign surprises people; it is real, and it is the tool for converting a partial derivative you cannot measure into a product of ones you can.

### Exact and inexact differentials — the heart of the chapter

Not every expression of the form $M(x,y)\,dx + N(x,y)\,dy$ is the total differential of some function. When it *is* — when there exists $f$ with $df = M\,dx + N\,dy$ — we call the differential **exact**, and $f$ a *state function* (its value depends only on the point $(x,y)$, not on how you arrived). When no such $f$ exists, the differential is **inexact**, and its integral $\int M\,dx + N\,dy$ along a path depends on the path.

When does $f$ exist? If $df = M\,dx + N\,dy$ is exact, then by matching to the total differential, $M = (\partial f/\partial x)_y$ and $N = (\partial f/\partial y)_x$. Differentiate $M$ with respect to $y$ and $N$ with respect to $x$:

$$\left(\frac{\partial M}{\partial y}\right)_x = \frac{\partial^2 f}{\partial y\,\partial x}, \qquad \left(\frac{\partial N}{\partial x}\right)_y = \frac{\partial^2 f}{\partial x\,\partial y}.$$

For a function with continuous second derivatives, the order of partial differentiation does not matter — the **equality of mixed partials**, variously credited to Clairaut, Schwarz, and Young:

$$\frac{\partial^2 f}{\partial y\,\partial x} = \frac{\partial^2 f}{\partial x\,\partial y}.$$

Therefore exactness *forces*

$$\boxed{\;\left(\frac{\partial M}{\partial y}\right)_x = \left(\frac{\partial N}{\partial x}\right)_y.\;}$$

This is the **exactness test**, and (on a simply connected domain) it works in reverse too: if the cross-derivatives are equal, a state function $f$ exists. The whole edifice of state functions versus path functions reduces to checking whether two mixed partials agree.

![A pressure–volume state plane with states A and B joined by two routes. A results box reports that the integral of the exact differential dU is the same on both routes (path independent, equal to delta U), while the integral of the inexact differential delta Q differs between routes (path dependent), with the slash on delta marking the warning.](images/02-multivariable-calculus-and-partial-derivatives-fig-02.png)
*Figure 2.2 — Exact vs inexact: $\int dU$ is the same along both routes from A to B, but $\int\delta Q$ depends on the path — which is why heat wears a slash.* An inexact differential fails this test; sometimes it can be repaired by an **integrating factor** — a function $\mu$ such that $\mu(M\,dx + N\,dy)$ *is* exact even though $M\,dx + N\,dy$ is not. The deepest example in physics is that $\delta Q$ is inexact but $\delta Q/T$ is exact: temperature is the integrating factor that turns heat into entropy. (Carathéodory built the second law on exactly this fact in 1909, though the full Pfaffian-form argument is beyond what we need here.)

### The fundamental relation and the Maxwell relations

Thermodynamics gives us one exact differential to start from. The first law, combined with $\delta Q = T\,dS$ for a reversible process and $\delta W = P\,dV$, yields the **fundamental relation** for the internal energy of a simple gas:

$$dU = T\,dS - P\,dV.$$

Notice what this tells us. $U$ is naturally a function of $S$ and $V$ — its "natural variables" — and comparing to the total differential $dU = (\partial U/\partial S)_V\,dS + (\partial U/\partial V)_S\,dV$ we read off

$$T = \left(\frac{\partial U}{\partial S}\right)_V, \qquad -P = \left(\frac{\partial U}{\partial V}\right)_S.$$

Now apply the exactness test. Because $dU$ is exact, $\partial M/\partial y = \partial N/\partial x$ with $M = T$, $N = -P$, $x = S$, $y = V$:

$$\left(\frac{\partial T}{\partial V}\right)_S = \left(\frac{\partial (-P)}{\partial S}\right)_V \;\Longrightarrow\; \boxed{\;\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V.\;}$$

This is a **Maxwell relation** — one of four — and Maxwell published it in his *Theory of Heat* (1871): it is the equality of mixed partials, with physics quantities in the slots. <!-- FACT-CHECK FLAG: [UNVERIFIED] — see factchecks/02-multivariable-calculus-and-partial-derivatives-assertions.md. The relations are genuinely Maxwell's (1871) and equivalent to the mixed-partials statement, but historically Maxwell reached them via a geometric Carnot-cycle argument, not the exact-differential derivation shown here. --> There is nothing more to it. The relation connects two derivatives that look unrelated, and it is *true* purely because $U$ is a state function. The other three relations come from the same move applied to three other state functions, which we now build.

### The Legendre transform and the other potentials

We have one potential, $U(S,V)$, with natural variables entropy and volume. But $S$ has no meter — you cannot dial entropy in a lab — whereas temperature does. We would like a potential whose natural variable is $T$ instead of $S$. The device that performs this trade is the **Legendre transform**, introduced by Legendre in 1787 for differential equations and later borrowed for thermodynamics (by Massieu in 1869, then systematized by Gibbs) and for mechanics (Chapter 11).

Here is the transform in the abstract. Given a (convex) function $f(x)$, define the conjugate variable $p = df/dx$ — the slope. The Legendre transform replaces $f$ as a function of $x$ by a new function of $p$:

$$g(p) = f(x) - p\,x \qquad \text{(with $x$ eliminated in favor of $p$).}$$

Why this combination? Differentiate: $dg = df - p\,dx - x\,dp = (p\,dx) - p\,dx - x\,dp = -x\,dp$. The $dx$ terms cancel by the very definition $p = df/dx$, leaving $dg = -x\,dp$ — so $g$ is genuinely a clean function of $p$, with $x = -dg/dp$. The transform has swapped the roles of the variable and its conjugate slope, losing no information: from $g(p)$ you can recover $f(x)$ by transforming back. Geometrically, $g$ encodes $f$ by its family of tangent lines (slope $p$, intercept related to $g$) rather than by its points.

![A convex curve f(x) with a single tangent line drawn at a point P. The tangent's slope is the conjugate variable p equal to df by dx, and its intercept on the vertical axis is minus g of p. A side box gives the transform g(p) = f − p x and the thermodynamic instance A = U − TS, which trades entropy for temperature.](images/02-multivariable-calculus-and-partial-derivatives-fig-03.png)
*Figure 2.3 — The Legendre transform encodes a convex $f(x)$ by its tangent lines: slope $p=df/dx$, intercept $-g(p)$ — the move that turns $U$ into the Helmholtz free energy $A=U-TS$.*

Apply this to $U(S,V)$. To trade $S$ for its conjugate slope $T = (\partial U/\partial S)_V$, subtract $TS$:

$$A = U - TS, \qquad dA = dU - T\,dS - S\,dT = (T\,dS - P\,dV) - T\,dS - S\,dT = -S\,dT - P\,dV.$$

The $T\,dS$ cancels exactly as the abstract transform promised, and we are left with the **Helmholtz free energy** $A$, naturally a function of $T$ and $V$ — temperature instead of entropy, just as wanted. To trade $V$ for its conjugate $P$ instead, add $PV$ to $U$ (the sign chosen so the $P\,dV$ cancels):

$$H = U + PV, \qquad dH = T\,dS + V\,dP,$$

the **enthalpy**, naturally a function of $S$ and $P$. (The series thermodynamics book introduces $H = U + PV$ and notes it "is a state function since $U, P, V$ are"; what we have shown is that it is specifically a *Legendre transform* of $U$.) Trade both, $S\to T$ and $V\to P$, to get the **Gibbs free energy**:

$$G = U - TS + PV, \qquad dG = -S\,dT + V\,dP,$$

naturally a function of $T$ and $P$ — the two most controllable laboratory variables, which is why $G$ governs chemistry and phase transitions. Four potentials, *not* four unrelated definitions to memorize, but one function $U$ and three Legendre transforms of it.

Each potential, being an exact differential, yields a Maxwell relation by the equality of mixed partials. From $dA = -S\,dT - P\,dV$:

$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V.$$

This is the *workhorse* relation, and the next worked example shows why. The remaining two come from $dH$ and $dG$ identically. All four:

$$\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V,\quad \left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P,\quad \left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V,\quad \left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P.$$

Memorize the *derivation*, not the table. Given any potential and its natural variables, you can reconstruct its Maxwell relation in ten seconds by equating mixed partials.

### Jacobians for changing variables

When you must convert a derivative taken at one set of fixed variables into derivatives at another set, the **Jacobian** determinant is the systematic tool. For two functions $u(x,y), v(x,y)$,

$$\frac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} (\partial u/\partial x)_y & (\partial u/\partial y)_x \\ (\partial v/\partial x)_y & (\partial v/\partial y)_x \end{vmatrix}.$$

Two facts make it useful: a partial derivative is a Jacobian, $(\partial u/\partial x)_y = \partial(u,y)/\partial(x,y)$, and Jacobians chain and invert like fractions, $\partial(u,v)/\partial(x,y) = [\partial(u,v)/\partial(r,s)]\,[\partial(r,s)/\partial(x,y)]$. Together these turn the manipulation of constrained partials — and the triple product rule, which is just a statement about a Jacobian — into routine determinant algebra. The same Jacobian governs the volume element in a change of variables in multivariable integration, the form in which it appears in statistical mechanics' phase-space integrals.

## Worked examples

### Example 1 — Measuring the unmeasurable with a Maxwell relation

Entropy has no meter. How, then, does one find $(\partial S/\partial V)_T$ — how entropy changes when a gas expands at fixed temperature? The workhorse Maxwell relation answers it without ever measuring entropy:

$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V.$$

The right-hand side is built entirely from $P$, $V$, $T$ — quantities with gauges. For an ideal gas $PV = nRT$, so $P = nRT/V$ and $(\partial P/\partial T)_V = nR/V$; hence $(\partial S/\partial V)_T = nR/V > 0$: an ideal gas gains entropy on isothermal expansion, and we computed it from a pressure gauge and a thermometer. This is the Maxwell relation earning its keep: it converts an unmeasurable response into a measurable one.

### Example 2 — The energy equation and why ideal-gas energy depends only on temperature

How does internal energy depend on volume at fixed temperature, $(\partial U/\partial V)_T$? Start from $dU = T\,dS - P\,dV$ and differentiate with respect to $V$ at constant $T$:

$$\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial S}{\partial V}\right)_T - P.$$

Now use the workhorse Maxwell relation to replace the entropy derivative:

$$\boxed{\;\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_V - P.\;}$$

This is the **energy equation**, and again the right side is all measurable. For an ideal gas, $(\partial P/\partial T)_V = nR/V = P/T$, so

$$\left(\frac{\partial U}{\partial V}\right)_T = T\cdot\frac{P}{T} - P = 0.$$

The internal energy of an ideal gas does not change with volume at fixed temperature — it depends on temperature alone, a result usually asserted in introductory courses and here *derived* from the fundamental relation and a Maxwell relation. For a van der Waals gas, where $P = nRT/(V-nb) - a n^2/V^2$, the same formula gives $(\partial U/\partial V)_T = a n^2/V^2 \neq 0$: a real gas does change its energy on expansion, which is why it cools when it expands freely (the Joule effect). The mathematics distinguishes the ideal gas from the real one cleanly.

### Example 3 — A chain-rule payoff: heat capacities and exact-versus-inexact

Heat capacity is the heat required per degree, but heat is path-dependent, so we must specify the path: $C_V = (\partial U/\partial T)_V$ at constant volume, and $C_P = (\partial H/\partial T)_P$ at constant pressure, using the natural potential for each constraint. They differ, and the chain rule among constrained variables produces the relation between them. For an ideal gas the result is **Mayer's relation** $C_P - C_V = nR$. <!-- FACT-CHECK FLAG: [CONFIRMED] — see factchecks/02-multivariable-calculus-and-partial-derivatives-assertions.md (C_P − C_V = nR for an ideal gas, = R per mole; standard, derivation verified) --> The cleanest route writes $H = U + PV = U + nRT$ for an ideal gas, so $C_P = (\partial H/\partial T)_P = (\partial U/\partial T)_P + nR$; and since ideal-gas $U$ depends only on $T$ (Example 2), $(\partial U/\partial T)_P = (\partial U/\partial T)_V = C_V$, giving $C_P = C_V + nR$. The example also illustrates the cold open's lesson: $C_P > C_V$ precisely because at constant pressure some of the heat goes into the path-dependent work of expansion, $\delta W = P\,dV$, an inexact differential, while at constant volume no work is done and all the heat raises $U$.

## Return to the cold open: $\delta Q$ is inexact, $dU$ is not

We can now say exactly why heat wears a slash. Internal energy is a state function: $dU$ is an exact differential, $dU = T\,dS - P\,dV$, and its integral from $A$ to $B$ depends only on the endpoints — which is why the two-path experiment gave the *same* $\Delta U = 4157\ \mathrm{J}$ both ways. Heat is not a state function. The first law reads $\delta Q = dU + \delta W = dU + P\,dV$, and while $dU$ is exact, $P\,dV$ is not the differential of any state function (there is no "work content" of a gas), so $\delta Q$ inherits that inexactness. Its integral $\int \delta Q$ — the total heat — depends on the path, which is why the two routes gave $4157\ \mathrm{J}$ and $5822\ \mathrm{J}$. The slash is a flag: it warns that you may not integrate this differential without knowing the path, and that there is no function "$Q$" of the state whose change you are computing.

You can verify the inexactness with the exactness test. Along a path in the $(V,T)$ plane, write $\delta Q = C_V\,dT + [\text{something}]\,dV$; the cross-derivatives do not match in general, so no state function $Q(V,T)$ exists. But divide by $T$ and the cross-derivatives *do* match — that repaired differential, $\delta Q/T = dS$, integrates to the entropy, a genuine state function. Temperature is the integrating factor, and the existence of entropy is the statement that one exists. The cold open's odd notation is, in the end, the exact/inexact distinction of multivariable calculus, dressed in physical clothes. Thermodynamics *is* this mathematics; learn the differentials and the relations stop being a list to memorize and become things you can derive.

## Where it generalizes

The exactness test is not confined to thermodynamics. In electromagnetism, a force field $\mathbf{F}$ is *conservative* — derivable from a potential — exactly when its differential is exact, which for $\mathbf{F} = (F_x, F_y)$ is the condition $(\partial F_x/\partial y) = (\partial F_y/\partial x)$, the same cross-derivative equality. In Chapter 3 this becomes the statement $\nabla \times \mathbf{F} = 0$: the curl is the field-theoretic form of the exactness test, and "conservative $\Leftrightarrow$ curl-free $\Leftrightarrow$ has a potential" is "exact $\Leftrightarrow$ state function exists" in vector-calculus language. The Legendre transform travels even further: the very same operation that traded entropy for temperature trades the velocity $\dot q$ for the momentum $p$ in passing from the Lagrangian $L(q,\dot q)$ to the Hamiltonian $H(q,p)$ in Chapter 11 — one mathematical device building both the thermodynamic potentials and the foundation of analytical mechanics and quantum theory. And the Jacobian that converts between $(S,V)$ and $(T,P)$ descriptions is the same Jacobian that governs phase-space volume in Liouville's theorem at the foundation of statistical mechanics. One body of multivariable calculus, every field that has more than one variable to vary.

## Exercises

1. **(Constraint subscript.)** For one mole of ideal gas, $U = \tfrac{3}{2}RT$. Compute $(\partial U/\partial T)_V$ and $(\partial U/\partial T)_P$ and confirm they are equal *for this gas*. Then explain in one sentence why they need not be equal for a gas whose energy depends on volume.

2. **(Exactness test.)** Determine whether each differential is exact. For the exact one, find the state function $f$. (a) $df = y\,dx + x\,dy$. (b) $\delta g = y\,dx - x\,dy$. Show your cross-derivative check in each case.

3. **(Derivation — required.)** Starting from the fundamental relation $dU = T\,dS - P\,dV$ and the definition $A = U - TS$, carry out the Legendre transform explicitly to obtain $dA = -S\,dT - P\,dV$. Then derive the Maxwell relation $(\partial S/\partial V)_T = (\partial P/\partial T)_V$ from it by equating mixed partials, stating clearly which theorem you are using.

4. **(Energy equation.)** Use the energy equation $(\partial U/\partial V)_T = T(\partial P/\partial T)_V - P$ to evaluate $(\partial U/\partial V)_T$ for a van der Waals gas with $P = RT/(V-b) - a/V^2$ (one mole). Interpret the sign of your result physically.

5. **(Triple product rule.)** Verify the triple product rule $(\partial P/\partial V)_T(\partial V/\partial T)_P(\partial T/\partial P)_V = -1$ for one mole of ideal gas $PV = RT$ by computing all three partial derivatives explicitly and multiplying.

## Sources

- James Clerk Maxwell, *Theory of Heat* (London: Longmans, Green, 1871).
- J. Willard Gibbs, "On the Equilibrium of Heterogeneous Substances," *Transactions of the Connecticut Academy of Arts and Sciences* 3 (1875–78), pp. 108–248 and 343–524.
- François Massieu, "Sur les fonctions caractéristiques des divers fluides," *Comptes rendus de l'Académie des sciences* 69 (1869), pp. 858–862 and (Addition) pp. 1057–1061. [pagination confirmed 2026-05-30]
- Constantin Carathéodory, "Untersuchungen über die Grundlagen der Thermodynamik," *Mathematische Annalen* 67 (1909), pp. 355–386.
- Adrien-Marie Legendre, *Mémoire sur l'intégration de quelques équations aux différences partielles* (Mémoires de l'Académie des sciences, 1787).
