# Linear Systems and Matrices

*When one equation is not enough: solving for several unknowns at once*

## A pan that will not hold still until you write down two equations

A small pan hangs from a ceiling by two strings of unequal length, tied to two points a fixed distance apart. One string is short and steep; the other is long and shallow. You start dropping coins into the pan, and you want to know which string will snap first, and how much weight it takes to break it.

You already know the physics. The pan is in *static equilibrium*: it does not accelerate, so the forces on it must sum to zero. The two string tensions $T_1$ and $T_2$ pull up and inward at their respective angles; the weight $w$ pulls straight down. Resolve everything into horizontal and vertical components and you get two statements that must both be true at the same instant:

$$T_1 \cos\alpha_1 = T_2 \cos\alpha_2 \qquad (\text{horizontal balance})$$
$$T_1 \sin\alpha_1 + T_2 \sin\alpha_2 = w \qquad (\text{vertical balance})$$

Here is the difficulty, and it is not a physics difficulty. Neither equation can be solved on its own. The first equation has *two* unknowns in it; so does the second. You cannot isolate $T_1$ without knowing $T_2$, and you cannot isolate $T_2$ without knowing $T_1$. The two tensions are locked together. The physics has handed you not a single equation to rearrange — the skill of Chapter 2 — but a *coupled set*, two equations that must hold simultaneously, with the answer hiding in the place where both are satisfied at once.

This is a new kind of problem, and it has its own mathematics. The math is called the theory of **linear systems**, and its bookkeeping device is the **matrix**. That is the subject of this chapter. The pan is just the doorway.

## The tool, named

A **system of linear equations** is a collection of equations, each of which is *linear* in the unknowns — meaning each unknown appears only to the first power, never squared, never inside a sine, never multiplied by another unknown. A solution is a set of values for the unknowns that makes *every* equation true simultaneously.

The pan gives us a $2\times 2$ system: two equations, two unknowns. The leaning ladder later in the chapter gives us a $3\times 3$ system. Our job is threefold:

1. To solve such systems reliably, by hand, with no guessing.
2. To understand *when* a unique solution exists and when it does not.
3. To organize the arithmetic with **matrices** and **determinants**, the compact notation that turns "solve these three equations" into a single mechanical procedure.

We will meet three methods — substitution, elimination, and Cramer's rule — and discover that they are not three tricks but **one act seen from three angles**: the act of eliminating unknowns one at a time until only solvable single-variable equations remain.

## Development: solving a $2\times 2$ system three ways

Take a clean, abstract system so the methods stand naked:

$$a_{11}x + a_{12}y = b_1$$
$$a_{21}x + a_{22}y = b_2$$

The subscripts are deliberate. $a_{ij}$ is the coefficient in equation $i$ multiplying unknown $j$. We will see in a moment why this grid of double-subscripts is exactly a matrix.

### Method 1: Substitution

Solve one equation for one unknown, then push that expression into the other. From the first equation (assume $a_{11}\neq 0$):

$$x = \frac{b_1 - a_{12}y}{a_{11}}$$

Substitute into the second:

$$a_{21}\cdot\frac{b_1 - a_{12}y}{a_{11}} + a_{22}y = b_2$$

Multiply through by $a_{11}$ and collect the $y$ terms:

$$a_{21}b_1 - a_{21}a_{12}y + a_{11}a_{22}y = a_{11}b_2$$
$$(a_{11}a_{22} - a_{12}a_{21})\,y = a_{11}b_2 - a_{21}b_1$$

Solve:

$$y = \frac{a_{11}b_2 - a_{21}b_1}{a_{11}a_{22} - a_{12}a_{21}}$$

The whole problem has collapsed to a single number divided by another single number. Notice the quantity in the denominator: $a_{11}a_{22} - a_{12}a_{21}$. Keep your eye on it — it will reappear as the hero of the chapter.

### Method 2: Elimination

Now do not solve for anything yet. Instead, scale the equations so that one unknown's coefficient is identical in both, then subtract to annihilate it. Multiply the first equation by $a_{21}$ and the second by $a_{11}$:

$$a_{21}a_{11}x + a_{21}a_{12}y = a_{21}b_1$$
$$a_{11}a_{21}x + a_{11}a_{22}y = a_{11}b_2$$

The $x$ coefficients now match. Subtract the first from the second:

$$(a_{11}a_{22} - a_{21}a_{12})\,y = a_{11}b_2 - a_{21}b_1$$

This is *the same equation for $y$* that substitution produced. Elimination and substitution are not different methods. They are the same elimination of an unknown, done with slightly different hand motions. This is the oldest mathematics in the chapter: the Chinese *Nine Chapters on the Mathematical Art* (c. 150 BCE) solved exactly such systems by arranging counting rods in a grid and reducing the columns by subtraction — Gaussian elimination two millennia before Gauss [verify].

### The determinant appears

That recurring denominator $a_{11}a_{22} - a_{12}a_{21}$ deserves a name and a notation. We write the coefficients as a square array — a **matrix** —

$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}$$

and define its **determinant** as

$$\det A = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22}\end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}.$$

The word *matrix* — Latin for "womb" — was coined by James Joseph Sylvester in 1850 for the array "out of which" determinants are born [verify]. The determinant itself is older: Seki Takakazu in Japan (1683) and Leibniz in Europe (1693) introduced it independently, as the single number that tells you whether a linear system can be solved [verify].

Why does the determinant decide solvability? Look at what we derived:

$$y = \frac{a_{11}b_2 - a_{21}b_1}{\det A}.$$

If $\det A = 0$, that fraction is undefined — there is no unique value of $y$. Geometrically, each equation $a_{i1}x + a_{i2}y = b_i$ is a straight line in the $(x,y)$ plane, and the solution is their crossing point. A nonzero determinant means the lines cross at exactly one point: one solution. A zero determinant means the lines are *parallel* — either they never meet (no solution) or they are the same line (infinitely many solutions). The determinant is the number that asks: *do these lines actually cross?*

![A 2×2 linear system drawn as two intersecting lines, with the solution at their crossing point.](images/10-linear-systems-and-matrices-fig-01.png)
*Figure 10.1 — Two equations are two lines; the simultaneous solution is the single point where they cross.*

![Two panels: a nonzero determinant spans a parallelogram of positive area and the lines cross once; a zero determinant collapses the parallelogram and the lines are parallel.](images/10-linear-systems-and-matrices-fig-02.png)
*Figure 10.2 — The determinant as signed area: nonzero area means one crossing (unique solution); zero area means parallel lines (no unique solution).*

### Method 3: Cramer's rule

We can package the answer for *both* unknowns in determinant form. Repeating the algebra for $x$ gives the symmetric result

$$x = \frac{b_1 a_{22} - b_2 a_{12}}{\det A}, \qquad y = \frac{a_{11}b_2 - a_{21}b_1}{\det A}.$$

These numerators are themselves determinants — of the matrix $A$ with one column replaced by the right-hand side $(b_1, b_2)$:

$$x = \frac{\begin{vmatrix} b_1 & a_{12} \\ b_2 & a_{22}\end{vmatrix}}{\det A}, \qquad
y = \frac{\begin{vmatrix} a_{11} & b_1 \\ a_{21} & b_2\end{vmatrix}}{\det A}.$$

This is **Cramer's rule**: each unknown is a ratio of determinants, with the system's determinant on the bottom and a column-replaced determinant on top. Gabriel Cramer published it in 1750 for the general $n\times n$ case, though Colin Maclaurin had special cases a couple of years earlier — a contested priority worth naming honestly [contested — see pantry]. Cramer's rule is beautiful and exact. It is also slow: for large systems, elimination is far more efficient. Treat it as the *conceptual* tool — the closed-form proof that the determinant runs the show — not the everyday workhorse.

### The $3\times 3$ determinant

For three equations in three unknowns we need the determinant of a $3\times 3$ matrix. It is built by **cofactor expansion** along the top row — each top entry times the $2\times 2$ determinant left over when you delete its row and column, with alternating signs:

$$\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{vmatrix}
= a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33}\end{vmatrix}
- a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33}\end{vmatrix}
+ a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32}\end{vmatrix}.$$

The geometric reading carries over: a $2\times 2$ determinant is the signed *area* of the parallelogram spanned by its rows; a $3\times 3$ determinant is the signed *volume* of the parallelepiped spanned by its three rows. Zero volume means the three rows are coplanar — the equations are not independent, and no unique solution exists.

For solving an actual $3\times 3$ system by hand, elimination is usually cleaner than Cramer's rule: eliminate one unknown from two of the equations to get a $2\times 2$ system, solve that, then back-substitute. We do exactly this for the ladder below.

## Worked examples

### Example 1 — The two-string pan, solved three ways

Return to the cold open with concrete geometry. The short string makes the steeper angle; from the string lengths (5 cm and 10 cm) and their ceiling separation, the geometry works out to

$$\sin\alpha_1 = \tfrac{2}{\sqrt5},\ \cos\alpha_1 = \tfrac{1}{\sqrt5}; \qquad \sin\alpha_2 = \tfrac{1}{\sqrt5},\ \cos\alpha_2 = \tfrac{2}{\sqrt5}.$$

The equilibrium system is

$$\tfrac{1}{\sqrt5}T_1 - \tfrac{2}{\sqrt5}T_2 = 0 \qquad (\Sigma F_x = 0)$$
$$\tfrac{2}{\sqrt5}T_1 + \tfrac{1}{\sqrt5}T_2 = w \qquad (\Sigma F_y = 0)$$

**By substitution.** The first equation gives $T_1 = 2T_2$. Substitute into the second:
$$\tfrac{2}{\sqrt5}(2T_2) + \tfrac{1}{\sqrt5}T_2 = w \;\Rightarrow\; \tfrac{5}{\sqrt5}T_2 = w \;\Rightarrow\; T_2 = \tfrac{w}{\sqrt5}, \quad T_1 = \tfrac{2w}{\sqrt5}.$$

**By elimination.** Multiply the first equation by 2 and add to the second to kill $T_2$: $\tfrac{2}{\sqrt5}T_1 - \tfrac{4}{\sqrt5}T_2 = 0$ added to $\tfrac{2}{\sqrt5}T_1 + \tfrac{1}{\sqrt5}T_2 = w$... instead multiply the first by 1 and the second by 2 and subtract to confirm — either route returns the identical $T_1 = 2T_2$, hence the same answer.

**By Cramer's rule.** The coefficient matrix and its determinant:
$$A = \frac{1}{\sqrt5}\begin{pmatrix} 1 & -2 \\ 2 & 1\end{pmatrix}, \qquad
\det A = \frac{1}{5}\bigl(1\cdot 1 - (-2)\cdot 2\bigr) = \frac{5}{5} = 1.$$
Then
$$T_1 = \frac{1}{\det A}\begin{vmatrix} 0 & -2/\sqrt5 \\ w & 1/\sqrt5\end{vmatrix} = \frac{2w}{\sqrt5}, \qquad
T_2 = \frac{1}{\det A}\begin{vmatrix} 1/\sqrt5 & 0 \\ 2/\sqrt5 & w\end{vmatrix} = \frac{w}{\sqrt5}.$$

All three methods agree: $T_1 = 2T_2$. The short, steep string carries twice the tension and **snaps first**. Setting $T_1$ to the breaking tension $2.80$ N gives $w = \tfrac{\sqrt5}{2}(2.80) \approx 3.13$ N, so the total hanging mass at failure is $w/g \approx 0.319$ kg. Subtracting the 42 g pan, about **277 g** of coins breaks it. Three methods, one answer — the surest sign they are one method in disguise.

### Example 2 — The leaning ladder: a genuine $3\times 3$ system

A uniform ladder of weight $w$ leans against a frictionless wall on a rough floor. Three forces are unknown: the wall's horizontal normal force $F_w$, the floor's vertical normal force $N$, and the floor's friction $f$. The physics gives three equations — two force balances and one torque balance (taking the torque about the foot of the ladder, where $N$ and $f$ contribute nothing):

$$\begin{aligned}
\Sigma F_x = 0:&\quad f - F_w = 0 \\
\Sigma F_y = 0:&\quad N - w = 0 \\
\Sigma \tau = 0:&\quad F_w (L\sin\beta) - w\bigl(\tfrac{L}{2}\sin\beta\bigr) = 0
\end{aligned}$$

This is the moment to notice *why three equations are needed*: three unknowns demand three independent constraints. With only the two force equations we would be one equation short — the system would be underdetermined, the determinant of any $2\times 3$ block meaningless. The torque equation supplies the missing relation. In matrix form, with unknown vector $(F_w, N, f)$:

$$\begin{pmatrix} -1 & 0 & 1 \\ 0 & 1 & 0 \\ L\sin\beta & 0 & 0\end{pmatrix}
\begin{pmatrix} F_w \\ N \\ f\end{pmatrix}
= \begin{pmatrix} 0 \\ w \\ \tfrac{wL}{2}\sin\beta\end{pmatrix}.$$

The third equation alone gives $F_w = \tfrac{w}{2}$ — the torque equation decoupled cleanly because of the smart pivot choice. Back-substitution then gives $f = F_w = \tfrac{w}{2}$ and $N = w$. The ladder is safe only while the floor can supply that much friction: $f \le \mu_s N$, i.e. $\tfrac{w}{2}\le \mu_s w$, which fails when $\mu_s < \tfrac12$ at a steep-enough lean. A clever pivot turned a $3\times 3$ solve into one division — the modeling judgment a solver cannot make for you.

### Example 3 — A collision as a linear system, and where the linear toolkit stops

Two pucks collide head-on on frictionless ice and **stick together** (perfectly inelastic). Momentum is conserved:

$$m_1 v_1 + m_2 v_2 = (m_1 + m_2)\,v_f.$$

With the masses and incoming velocities known, this is a single *linear* equation in the one unknown $v_f$ — solved instantly: $v_f = (m_1 v_1 + m_2 v_2)/(m_1+m_2)$. For the hockey pucks of the source material ($m_1 = 0.12$ kg at $-2.5$ m/s into $m_2 = 0.15$ kg at rest): $v_f = -0.30/0.27 \approx -1.11$ m/s. Linear; clean.

Now make the collision **elastic**. Momentum is still linear, but kinetic-energy conservation adds a *quadratic* equation:

$$m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2' \qquad (\text{linear})$$
$$\tfrac12 m_1 v_1^2 + \tfrac12 m_2 v_2^2 = \tfrac12 m_1 v_1'^2 + \tfrac12 m_2 v_2'^2 \qquad (\text{quadratic})$$

This is no longer a linear system — the squared velocities put it beyond the reach of matrices and determinants. That boundary is worth feeling: the moment a conservation law involves a square, the elegant linear machinery stops, and you fall back on substitution-into-a-quadratic (Chapter 2) or the algebraic identities special to elastic collisions. Knowing *where the linear toolkit ends* is itself part of the toolkit.

## Back to the pan

The pan that "would not hold still" was never a physics mystery — it was a request to solve a $2\times 2$ linear system. The two equilibrium equations were two lines in the $(T_1, T_2)$ plane; the tensions were the coordinates of their single crossing point. Substitution, elimination, and Cramer's rule all walked to that crossing by the same route, eliminating one tension to expose the other. The determinant ($\det A = 1$, comfortably nonzero) guaranteed the lines actually crossed — that the structure was rigid and the problem had one answer.

That last point is the physical payoff of the determinant. Had it come out zero, it would not have been an arithmetic accident: a zero determinant would mean the two strings pulled along the *same* line, unable to balance a sideways load — a structure that is a mechanism, not a rigid support. The mathematics flags the failure before the pan ever falls.

## Where it generalizes

Linear systems are everywhere that several quantities constrain each other at once. The same matrix machinery solves the currents in a resistor network (Kirchhoff's node and loop equations are a linear system), the member forces in a bridge truss (two force equations per pin joint, a network of coupled systems), the balanced amounts in a chemical equation, the equilibrium prices in an economy, and the pixel transformations in computer graphics. Whenever you write "set up the equations and solve," and there is more than one of them, you are solving a linear system — and a computer doing it in microseconds with `numpy.linalg.solve` is running the very elimination the *Nine Chapters* did with bamboo rods.

What it cannot do for you is the modeling: drawing the free-body diagram, choosing the axes, deciding which forces are unknown, and writing the *correct* coefficient matrix. The solver inverts the matrix; you have to build it. The deeper structure of matrices — eigenvalues and eigenvectors, the natural axes along which a matrix merely stretches without rotating, which govern coupled oscillations and stability — is the subject of **Volume 2**. Here we have the essential first move: when one equation is not enough, write them all and solve them together.

## Exercises

1. **Solve and verify.** Solve the system $3x + 2y = 12,\ \ x - y = 1$ by (a) substitution and (b) elimination, and confirm both give the same $(x,y)$. Then compute $\det A$ for the coefficient matrix and use Cramer's rule as a third check.

2. **Two support cables.** A sign of weight $W$ hangs from two cables meeting at a point, one at $30^\circ$ above horizontal to the left, the other at $45^\circ$ above horizontal to the right. Write the two equilibrium equations $\Sigma F_x = 0,\ \Sigma F_y = 0$ as a linear system in the tensions $T_1, T_2$, and solve for both in terms of $W$.

3. **When does it fail? (derivation).** Consider the system $a_{11}x + a_{12}y = b_1,\ a_{21}x + a_{22}y = b_2$. Derive, from the elimination steps, the condition on the coefficients under which the system has (a) exactly one solution, (b) no solution, (c) infinitely many. Express each case in terms of $\det A$ and the right-hand sides, and sketch the corresponding pair of lines.

4. **A $3\times 3$ by elimination.** Solve
$$x + y + z = 6,\quad 2x - y + z = 3,\quad x + 2y - z = 2$$
by eliminating $z$ from two pairs to reduce to a $2\times 2$ system, then back-substitute. Verify your answer by computing $\det A$ and checking it is nonzero.

5. **The boundary of linearity.** Two equal masses collide elastically in one dimension, one initially at rest. Write down the momentum equation (linear) and the kinetic-energy equation (quadratic). Explain in one paragraph why the pair cannot be solved by matrices alone, and identify exactly which equation breaks the linear structure.

## Sources

- *Jiuzhang Suanshu* (The Nine Chapters on the Mathematical Art), Chapter 8 (*Fangcheng*), c. 150 BCE; with commentary by Liu Hui, 3rd c. CE — array-based elimination of simultaneous linear equations. [verify]
- Gabriel Cramer, *Introduction à l'analyse des lignes courbes algébriques* (1750) — the determinant rule for $n\times n$ systems; Maclaurin priority discussed in Kosinski, "Cramer's Rule Is Due to Cramer" (2001). [contested — see pantry]
- Seki Takakazu (1683) and G. W. Leibniz (1693) — independent introduction of determinants as a solvability test. [verify]
- James Joseph Sylvester (1850) — coinage of the term "matrix." [verify]
- Arthur Cayley, "A Memoir on the Theory of Matrices," *Philosophical Transactions of the Royal Society* 148 (1858), pp. 17–46 — matrix algebra as such.
- Source physics: *Static Equilibrium and Elasticity* (two-string pan, leaning ladder) and *Linear Momentum and Collisions* (inelastic/elastic collisions), retained physics chapters 13 and 10.
