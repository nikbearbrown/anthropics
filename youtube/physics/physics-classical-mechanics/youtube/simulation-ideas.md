# Physics: Classical Mechanics — Simulation Ideas

## Candidate 01 — Animate "Rolling Race: Moment of Inertia Determines the Finish Line"
- Source: `physics-classical-mechanics/chapters/13-rotational-motion-and-angular-momentum.md`
- Topic: Moment of Inertia and Rolling Motion
- Lane: MANIM (directed animation)
- Hook: Four objects start at the same height. The heavier ones don't win — the shape does. A hollow hoop always finishes last, no matter what it's made of.
- The rule: Energy conservation on a ramp: mgh = ½mv²_cm + ½Iω², with ω = v_cm/R. Using I = βMR² (β = 0 for sliding, 1/3 for solid sphere, 1/2 for disk, 1 for hoop): v_cm = √(2gh/(1+β)). Finish order depends only on β.
- Concrete numbers: Ramp h = 1.0 m, g = 9.8 m/s². Sliding block: v = 4.43 m/s (β=0). Solid sphere: v = 3.74 m/s (β=2/5). Disk: v = 3.62 m/s (β=1/2). Hoop: v = 3.13 m/s (β=1). Time differences: sphere reaches bottom in t = 0.535 s, hoop in t = 0.639 s — hoop loses by 104 ms.
- The artifact / what moves: Four objects (block, sphere, disk, hoop) released simultaneously at the top of a ramp; a ghost label showing "β = 0 / 2/5 / 1/2 / 1" travels with each. Objects roll in real time, separating visibly, block coasting ahead, hoop falling behind. At the bottom, a velocity readout snaps into place for each. A second beat strips the ramp away and redraws the same four objects at equal mass and equal radius — finish order unchanged. A KE bar chart fills simultaneously: translational vs rotational fraction visible for each.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At h = 1.0 m, sphere bottom speed is 3.742 m/s (exactly √(10gh/7)); hoop is 3.130 m/s (exactly √(gh)); ratio = 1.195. P2: Rotational fraction of total KE for the disk is exactly 1/3 (since β/(1+β) = (1/2)/(3/2) = 1/3); for the hoop it is exactly 1/2.
- The change: Replace the ramp with a curved bowl. All rolling objects still reach the same height, but the time structure changes — reveals that period of oscillation in the bowl also depends on β, not just mass.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all masses equal, radii equal, geometry is the only variable.
- Teardown angle: Races aren't about weight — they're about how much of the energy gets warehoused in spin. The hoop pays the highest rotational tax every meter; the solid sphere pays the least. Geometry is destiny on a ramp.
- Exclusions: Derivation of I from scratch; friction coefficient analysis; real material properties; bouncing or deformation.
- Sim slug: classical-rolling-race
- Score: 9/10

## Candidate 02 — Animate "Figure Skater: Angular Momentum Conserved, Kinetic Energy Is Not"
- Source: `physics-classical-mechanics/chapters/13-rotational-motion-and-angular-momentum.md`
- Topic: Conservation of Angular Momentum
- Lane: MANIM (directed animation)
- Hook: The skater pulls her arms in and spins four times faster. But her kinetic energy quadruples. Where did that energy come from? Her muscles — and the simulation proves it with numbers.
- The rule: L = Iω is conserved when no external torque acts. I_f ω_f = I_i ω_i. KE = L²/(2I) — so halving I doubles ω and quadruples KE. The work done by the skater against centrifugal pseudo-force equals ΔKE = KE_f − KE_i.
- Concrete numbers: I_i = 4.0 kg·m², ω_i = 1.5 rev/s (9.42 rad/s). Arms pulled in: I_f = 1.0 kg·m², ω_f = 6.0 rev/s (37.7 rad/s). KE_i = ½(4.0)(9.42)² = 177 J. KE_f = ½(1.0)(37.7)² = 710 J. Muscle work = 533 J. L = 37.7 kg·m²/s throughout.
- The artifact / what moves: A top-down view of a figure skater as a rigid body with two arm segments. Arms start fully extended (high I); spin is slow. Arms draw in toward the body in 1.5 s of animation — angular velocity visibly increases as I decreases. Two real-time gauges: an L (angular momentum) needle stays pinned; a KE bar climbs 4×. At the end, a muscle-work annotation (+533 J) appears. A second pass: arms extend again — ω drops to 1.5 rev/s, KE returns to 177 J, L unchanged.
- Output medium: Manim (mp4)
- Two testable predictions: P1: ω_f/ω_i = I_i/I_f = 4.0/1.0 = 4.00 exactly; simulation readout must show 6.00 rev/s when I drops to 1.0 kg·m². P2: KE_f/KE_i = (I_i/I_f)² × (I_f/I_i) = I_i/I_f = 4.0 — kinetic energy scales as the inverse of I for fixed L, so a 4× I drop gives 4× KE; numerical check: 710/177 = 4.01 (rounding).
- The change: Replace the arms with a mass on a string that reels in. Same I → L → ω algebra, but now the tension doing work is explicit — visualized as a force arrow on the string — closing the energy accounting without ambiguity.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; moment of inertia treated as a lumped parameter, no detailed anatomy required.
- Teardown angle: Conservation of angular momentum is free. The energy boost is not — it costs muscle work every time. Nature conserves L, not KE, and that distinction is exactly what makes spinning in place feel like exercise.
- Exclusions: Detailed anatomy of the skater's body shape; friction at the blade; derivation of I for complex body shapes; gyroscopic precession.
- Sim slug: classical-angular-momentum-skater
- Score: 9/10

## Candidate 03 — Animate "Pendulum Period: Mass Cancels, Only Length and g Survive"
- Source: `physics-classical-mechanics/chapters/18-oscillatory-motion-and-waves.md`
- Topic: Simple Harmonic Motion — Pendulum
- Lane: MANIM (directed animation)
- Hook: Drop a steel ball and a ping-pong ball on the same pendulum arm. They swing in perfect unison. Mass cancels algebraically — but the animation lets you see WHY: both accelerating forces are proportional to mass, so the ratio doesn't care.
- The rule: Restoring torque: τ = −mgL sinθ ≈ −mgLθ (small angle). Moment of inertia: I = mL². Angular equation: θ̈ = −(g/L)θ. Period T = 2π√(L/g) — mass m drops out identically. For large angles, T increases: T ≈ T₀(1 + θ₀²/16 + ...).
- Concrete numbers: L = 1.00 m, g = 9.80 m/s² → T = 2.007 s. Moon (g = 1.62 m/s²): T = 4.93 s. L = 0.25 m (Earth): T = 1.003 s. Large-angle correction: at θ₀ = 30° (π/6), T ≈ 1.017 × T₀ — 1.7% longer than small-angle formula predicts.
- The artifact / what moves: Side-by-side pendulums: one heavy ball, one light, same L = 1.0 m. Released together from 10°. They stay in phase for 10 full swings — period readout identical at 2.007 s. Second panel: single pendulum, L slides from 1.0 m to 0.25 m in real time. T-clock halves as L quarters — exactly 4× faster because T ∝ √L. Third panel: Earth pendulum vs Moon pendulum, same L = 1.0 m, released simultaneously; Moon lags behind by 2.9 s per cycle.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Quadrupling L increases T by exactly √4 = 2.000; at L = 1.0 m, T = 2.007 s; at L = 4.0 m, T = 4.014 s. Simulation must display this ratio. P2: On the Moon (g = 1.62 m/s²) a 1.0 m pendulum has T = 4.934 s; ratio T_moon/T_earth = √(9.80/1.62) = 2.459; after 5 Earth periods (10.03 s) the Moon pendulum has completed only 2.03 cycles — it is already half a period behind.
- The change: Add the large-angle correction: at θ₀ = 45° the period is ≈1.04 T₀ (4% late). Animate a clock calibrated for small-angle SHM drifting vs the true pendulum — shows where the approximation breaks.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; no measured data required.
- Teardown angle: A pendulum clock on the Moon runs 59% slow. Not because gravity is weaker in some vague way — because the period scales as √(1/g) and that square root is exact. The formula is a precision instrument; the Moon just changes one input.
- Exclusions: Derivation via Lagrangian; air resistance and damping; coupled pendulums; Foucault rotation; chaos at large amplitudes.
- Sim slug: classical-pendulum-period-mass-cancels
- Score: 9/10

## Candidate 04 — Animate "Elastic Collision: The Mass-Ratio Spectrum from Stop to Bounce"
- Source: `physics-classical-mechanics/chapters/08-linear-momentum-and-collisions.md`
- Topic: Elastic Collisions and Momentum Transfer
- Lane: MANIM (directed animation)
- Hook: Shoot a bullet at a wall of equal mass: the bullet stops cold. Make the wall ten times heavier: the bullet bounces back with nearly its original speed. Make the wall ten times lighter: the wall flies off at twice the bullet's speed. One equation, three completely different outcomes — and a continuous morph between them.
- The rule: 1D elastic collision: v₁f = (m₁−m₂)/(m₁+m₂)v₁; v₂f = 2m₁/(m₁+m₂)v₁. Mass ratio r = m₂/m₁. Three limits: r = 1 (v₁f = 0, v₂f = v₁); r → ∞ (v₁f → −v₁, v₂f → 0); r → 0 (v₁f → +v₁, v₂f → 2v₁).
- Concrete numbers: m₁ = 1.0 kg, v₁ = 5.0 m/s. r = 1: v₁f = 0, v₂f = 5.0 m/s. r = 10: v₁f = −4.09 m/s (81.8% reversal), v₂f = 0.91 m/s. r = 0.1: v₁f = +4.09 m/s, v₂f = 9.09 m/s. r = 3 (neutron moderation): v₁f = −1.25 m/s, v₂f = 3.75 m/s — target gets 56% of KE, ideal for slowing neutrons with hydrogen (r ≈ 1) vs graphite (r ≈ 12).
- The artifact / what moves: Ball 1 (projectile) slides right at v₁ = 5 m/s. Ball 2 (target) sits still. Collision fires; both velocities update with velocity vectors. A mass-ratio slider morphs r continuously from 0.01 to 100: the post-collision vectors animate in real time. Key tick marks animate with a frame: r = 1 shows a full stop; r = ∞ shows a perfect bounce; r = 0 shows target flying off at 2v₁. Below, a "fraction of KE transferred" curve plots as r sweeps — peaks at r = 1 with 100% transfer.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At r = 1, post-collision KE of projectile is exactly 0 J; target KE is exactly 12.5 J (= ½ × 1.0 × 5²), conservation confirmed by simulation readout. P2: The fraction of KE transferred to the target, f = 4r/(1+r)², peaks at f = 1.000 when r = 1 and falls to f = 4r for r ≪ 1; at r = 10, f = 4×10/(11²) = 0.331 — the sim KE bars must match this to 3 significant figures.
- The change: Chain three collisions: a heavy ball hits a medium ball hits a light ball (Newton's Cradle). Optimal mass ratio for maximum energy transfer at each stage — engineering a multi-stage shock cascade.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; 1D elastic mechanics, exact formulas.
- Teardown angle: Nuclear reactor moderators pick their material by mass ratio. Hydrogen (r ≈ 1) slows a neutron in one hit. Carbon (r ≈ 12) needs ten hits. The peak of the KE-transfer curve at r = 1 is the engineering design criterion — expressed as a physics formula.
- Exclusions: Inelastic collisions; coefficient of restitution; center-of-mass frame derivation; 2D collisions; relativistic corrections.
- Sim slug: classical-elastic-collision-mass-ratio
- Score: 9/10

## Candidate 05 — Animate "Pulsar Spin-Up: Stellar Collapse and the Conservation of Angular Momentum"
- Source: `physics-classical-mechanics/chapters/13-rotational-motion-and-angular-momentum.md`
- Topic: Conservation of Angular Momentum — Astrophysical Scale
- Lane: MANIM (directed animation)
- Hook: A star collapses from the size of the Sun to the size of a city. Angular momentum is conserved. The spin rate goes from once a month to thirty times a second. The math is middle-school algebra once you accept L = Iω.
- The rule: L = Iω conserved; I = (2/5)MR² for a uniform solid sphere. ω_f = ω_i × (R_i/R_f)². For a solar-mass collapse from R_i ≈ 7×10⁸ m to R_f ≈ 10⁴ m (neutron star radius ≈ 10 km): ratio = (7×10⁸ / 10⁴)² = (7×10⁴)² = 4.9×10⁹. Starting period ≈ 25 days → final period ≈ 25 days / (4.9×10⁹) ≈ 440 µs.
- Concrete numbers: Pre-collapse: R_i = 7×10⁸ m, P_i = 25 days = 2.16×10⁶ s, ω_i = 2.9×10⁻⁶ rad/s. Neutron star: R_f = 1.0×10⁴ m, ω_f = ω_i × (R_i/R_f)² = 2.9×10⁻⁶ × 4.9×10⁹ = 14,210 rad/s → P_f = 0.44 ms. Crab Pulsar (observed): P = 33 ms, ω = 190 rad/s — a partially spun-up example. If it began at P_i ≈ 10 ms (supernova remnant age of 1,000 yr confirms spin-down rate).
- The artifact / what moves: A large glowing sphere (the Sun, to scale) rotating slowly — one tick every 25 days, sped up. A collapse animation: radius shrinks by a factor of 70,000 over 3 seconds of screen time. As radius falls, a real-time ω gauge climbs exponentially. The final neutron star flashes at 33 ms (Crab Pulsar rate) with a lighthouse-beam sweep. Below, an L meter stays flat throughout — angular momentum unchanged despite the factor-of-10⁹ change in I.
- Output medium: Manim (mp4)
- Two testable predictions: P1: Final ω scales as (R_i/R_f)², so a 10× smaller radius gives 100× faster spin — verifiable: shrink to 7×10⁷ m (10× smaller than Sun) → P_f = 25 days / 100 = 6 hours. P2: The Crab Pulsar period of 33 ms corresponds to an implied radius compression ratio of √(2.16×10⁶ s / 0.033 s) = √(6.5×10⁷) = 8,100 — meaning the progenitor star's angular velocity compressed by a factor of 6.6×10⁷ at the current measured period, consistent with known remnant age and spin-down.
- The change: Add a magnetar: same mass, same collapse, but a pre-collapse magnetic field compressed into a tiny volume. Show the magnetic field lines (B ∝ 1/R²) intensifying by the same (R_i/R_f)² factor. A magnetar's B ≈ 10¹¹ T emerges from a solar B ≈ 10⁻⁴ T input.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; stellar and neutron star parameters are published standard values.
- Teardown angle: Pulsars are the universe's most precise clocks because their moment of inertia is nearly constant once formed. The spin-up is a one-time angular momentum dividend from the collapse; after that, L slowly drains away via magnetic braking. The math is the same algebra a figure skater uses.
- Exclusions: Relativistic corrections to neutron star interior; equation of state; gravitational wave emission; full supernova mechanism.
- Sim slug: classical-pulsar-spinup
- Score: 9/10

## Candidate 06 — Animate "SHM Energy Exchange: KE and PE Sum to a Constant"
- Source: `physics-classical-mechanics/chapters/18-oscillatory-motion-and-waves.md`
- Topic: Simple Harmonic Motion — Energy
- Lane: MANIM (directed animation)
- Hook: The spring compresses — all kinetic energy vanishes into the coil. It releases — all potential energy reappears as motion. The sum never moves. Watch conservation of energy happen in real time, not just as a formula.
- The rule: x(t) = A cos(ωt), v(t) = −Aω sin(ωt). KE = ½mv² = ½mA²ω²sin²(ωt) = ½kA²sin²(ωt). PE = ½kx² = ½kA²cos²(ωt). E_total = ½kA² (constant). Energy flows from PE to KE and back with frequency 2ω.
- Concrete numbers: m = 0.5 kg, k = 50 N/m, A = 0.20 m. ω = √(50/0.5) = 10 rad/s, T = 0.628 s. E_total = ½(50)(0.04) = 1.00 J. At x = A: KE = 0, PE = 1.00 J. At x = 0: KE = 1.00 J, PE = 0. At x = A/√2: KE = PE = 0.50 J. Max v = Aω = 2.0 m/s at x = 0. Quartz crystal: ω = 2π × 32,768 Hz — same formula, vastly different numbers.
- The artifact / what moves: A horizontal mass-spring system oscillates. Below it, two overlapping sine-squared curves fill in real time — KE in orange, PE in blue, their sum a flat white line at 1.00 J. A vertical cursor tracks the oscillation position; at each x the bar heights shift exactly as expected. The curves are updated continuously so the viewer watches energy slosh between the two modes. A phase readout shows: "At x = 0: all KE. At x = A: all PE."
- Output medium: Manim (mp4)
- Two testable predictions: P1: The crossover point (KE = PE) occurs at x = ±A/√2 = ±0.141 m; at that point v = ±Aω/√2 = ±1.414 m/s; both must read exactly 0.500 J on the simulation bars. P2: Energy oscillates at frequency 2ω = 20 rad/s, so the KE curve completes two full peaks for every one oscillation cycle; the simulation time-axis must show two orange humps per blue hump per period T = 0.628 s.
- The change: Add a damping coefficient b. Show the energy envelope decaying as E(t) = E₀e^(−bt/m). The sum curve tilts downward; the oscillation amplitude shrinks; the system reaches equilibrium at E = 0 as all energy converts to heat.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; spring constants and masses are the only inputs.
- Teardown angle: The sum being constant isn't a coincidence — it's a proof that no energy leaks out of a conservative system. When the damping is added and the sum starts to fall, it shows exactly where the energy goes. Flat-line conservation is the diagnostic.
- Exclusions: Derivation of the SHM equation from Newton's second law; nonlinear spring corrections; quantum oscillator energy levels; acoustic resonance.
- Sim slug: classical-shm-energy-exchange
- Score: 8/10

## Candidate 07 — Animate "Impulse and the Airbag: Same Δp, Longer Δt, Smaller Force"
- Source: `physics-classical-mechanics/chapters/08-linear-momentum-and-collisions.md`
- Topic: Impulse-Momentum Theorem
- Lane: MANIM (directed animation)
- Hook: A car stops in 0.01 s — the dashboard exerts 1,000 N. The airbag fires and stops the same person in 0.15 s — the force drops to 67 N. Same change in momentum. Fifteen times longer contact time. Fifteen times smaller force. That is the entire physics of crash safety.
- The rule: J = FΔt = Δp. For a fixed Δp, F = Δp/Δt — force is inversely proportional to contact time. Area under the F-t graph is conserved (= Δp) even as the peak force and shape change.
- Concrete numbers: m = 75 kg (driver), v₀ = 15 m/s (54 km/h), v_f = 0. Δp = 1,125 N·s. Dashboard (Δt = 0.01 s): F_avg = 112,500 N = 11,500 kg force ≈ 153 g — fatal. Steering wheel with seatbelt (Δt = 0.08 s): F_avg = 14,063 N ≈ 19 g — survivable. Airbag (Δt = 0.15 s): F_avg = 7,500 N ≈ 10 g — safe. Threshold for rib fracture: ~35 g at chest.
- The artifact / what moves: Three collision scenarios play as side-by-side F-t graph panels. Left: dashboard (sharp spike, tiny area). Middle: seatbelt (broader curve, same area). Right: airbag (wide plateau, same area). The body-deceleration readout displays g-force in real time. A horizontal red line marks the injury threshold. Spike pierces it; seatbelt barely touches it; airbag stays comfortably below. The F-t curve area (= Δp) is numerically identical in all three cases — a running integral displayed below each.
- Output medium: Manim (mp4)
- Two testable predictions: P1: The integral ∫F dt must equal 1,125 N·s in all three panels — any deviation in the simulation reveals a coding error in the force model. P2: The peak airbag force at Δt = 0.15 s is F_avg = 7,500 N = 10.2 g; at Δt = 0.08 s the peak is exactly 14,063 N = 19.1 g; ratio must be 15/8 = 1.875, matching the inverse Δt ratio.
- The change: Show a crumple zone as a variable-Δt parameter. Sweep Δt from 0.005 s to 0.300 s and plot the resulting peak force — a hyperbola. Mark the threshold and shade the "safe zone" Δt ≥ 0.11 s, directly translating to crumple depth ≈ v₀ × Δt_min / 2 = 0.83 m minimum.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; crash biomechanics thresholds are published NHTSA/FMVSS values.
- Teardown angle: An airbag isn't a cushion — it's a timer. Its only job is to buy 150 ms of contact time. The momentum change is physics; the force is engineering. Every millimeter of crumple zone exists to extend Δt. The F-t area is inviolable; only the peak is negotiable.
- Exclusions: Detailed biomechanics of rib cage response; airbag chemistry (sodium azide); 2D crash direction effects; seat belt pre-tensioner.
- Sim slug: classical-impulse-airbag
- Score: 8/10

## Candidate 08 — Animate "Work-Energy Theorem: Area Under the F-x Curve Is the KE Gain"
- Source: `physics-classical-mechanics/chapters/09-work-energy-and-energy-resources.md`
- Topic: Work and the Work-Energy Theorem
- Lane: MANIM (directed animation)
- Hook: A variable force acts on a block. The force changes moment to moment, but the area under the force-displacement graph is exact kinetic energy gained. Watch the area fill in as the block speeds up — the measurement is built into the geometry.
- The rule: W_net = ∫F·dx = ΔKE = ½mv_f² − ½mv_i². For constant force: W = Fd cosθ. For a spring: W = ½kx² (triangle area). Work by gravity: W = mgh regardless of path — conservative force.
- Concrete numbers: Block m = 2.0 kg, starts at rest. F(x) = 10 + 5x N over x = 0 to 4.0 m. W = ∫₀⁴(10+5x)dx = [10x + 2.5x²]₀⁴ = 40 + 40 = 80 J. v_f = √(2W/m) = √(80) = 8.94 m/s. Spring compress: k = 200 N/m, x = 0.30 m. W = ½(200)(0.09) = 9.0 J → v = √(2×9.0/2.0) = 3.0 m/s.
- The artifact / what moves: A block on a frictionless track, pushed by a force arrow that varies as F(x) = 10 + 5x. Below the track, an F-x graph draws in real time as the block moves — the area under the curve fills with color. A KE gauge on the right climbs in lockstep with the accumulated area. At x = 4.0 m, both read 80 J. Second scene: replace the variable force with a spring. The curved triangular area fills as the spring compresses; KE gauge matches ½kx².
- Output medium: Manim (mp4)
- Two testable predictions: P1: At x = 2.0 m (halfway), ∫₀²(10+5x)dx = 20+10 = 30 J; v = √(2×30/2.0) = 5.48 m/s; the simulation KE bar must read 30 J exactly at that position. P2: For the spring at x = 0.30 m, W = ½(200)(0.09) = 9.00 J; v = 3.00 m/s; KE bar must match to three significant figures.
- The change: Add friction with a constant friction force f = 5.0 N. Now W_net = ∫F dx − f × d. The filled area splits: shaded "friction-loss" region vs net KE gain. The block stops sooner; the theorem still holds for W_net, but total area no longer equals final KE.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; all forces and masses are chosen parameters.
- Teardown angle: Calculus hides inside the area. You don't need to integrate by hand — you need to see that the geometry IS the energy. Every change in force shape changes the block's final speed, and the F-x graph is a direct physical accounting, not an abstraction.
- Exclusions: Derivation of the work-energy theorem from Newton's second law; potential energy and conservative force derivation; thermodynamics connection.
- Sim slug: classical-work-energy-area
- Score: 8/10

## Candidate 09 — Animate "Projectile Range Curve: The 45° Maximum and the Complementary-Angle Tie"
- Source: `physics-classical-mechanics/chapters/04-projectile-motion.md`
- Topic: Projectile Motion and Range
- Lane: MANIM (directed animation)
- Hook: Every artillery gunner knows to aim at 45°. But 30° and 60° reach the same target. So do 20° and 70°. One formula, an infinite family of complementary pairs — and the 45° peak is the only angle that stands alone.
- The rule: Range R = v₀² sin(2θ)/g. Maximum at θ = 45° (sin 90° = 1). Complementary angles: sin(2θ) = sin(2(90°−θ)), so R is identical at θ and (90°−θ). Time of flight: T = 2v₀sinθ/g. Peak height: H = v₀²sin²θ/(2g).
- Concrete numbers: v₀ = 30.0 m/s, g = 9.80 m/s². R_max at 45°: R = (30)²/9.80 = 91.8 m. At 30°: R = (30)²sin60°/9.80 = 79.5 m. At 60°: R = (30)²sin120°/9.80 = 79.5 m — same. At 20° and 70°: R = 58.8 m each. At 15° and 75°: R = 44.4 m each. Olympic long jump (θ ≈ 22°): actual v₀ ≈ 9.8 m/s → R ≈ 7.6 m — complementary angle 68° would reach the same distance but at impractical height.
- The artifact / what moves: A polar-style range plot sweeps from 0° to 90°: as the angle marker rotates, the projectile arc draws in the upper panel and the corresponding R value plots on the lower curve. The curve rises, peaks at 45°, falls symmetrically. When the angle hits 60°, a ghost arc from 30° reappears and overlaps exactly — same R, different trajectory shape. Complementary pairs are highlighted: 30°/60°, 20°/70°, 15°/75°. The 45° arc is widest in every dimension.
- Output medium: Manim (mp4)
- Two testable predictions: P1: At θ = 45°, R = v₀²/g = 900/9.80 = 91.84 m; at θ = 44° and 46°, R = v₀²sin(88°)/g = 91.77 m — less by 0.07 m; the simulation must resolve this ≈0.08% drop. P2: The pair 30°/60° both give R = v₀²sin(60°)/g = 79.53 m; their trajectories must overlap at the landing point with pixel precision; peak heights are H(30°) = 11.48 m vs H(60°) = 34.44 m — a 3:1 ratio the simulation arc heights must reflect.
- The change: Add air resistance (drag ∝ v²). The range curve shifts: optimal angle drops below 45° (≈33–38° for a baseball), the symmetry of complementary pairs breaks. The two panels — ideal vs drag — play side by side.
- Human supplies (Claude can't): Nothing — fully synthetic/analytic for ideal projectile; drag coefficient is a standard published value for a sports ball.
- Teardown angle: The 45° rule is an ideal-world fact that crumbles the moment air exists. Every ballistic engineer, every golfer, every shot-putter targets an angle below 45° because drag is real. The simulation is the gap between the textbook answer and the field.
- Exclusions: Coriolis effect; range over elevated targets; full aerodynamic coefficient tables; spin effects on trajectory.
- Sim slug: classical-projectile-range-curve
- Score: 8/10

## Candidate 10 — Animate "Gravitational Orbits: Orbital Speed and Kepler's T² ∝ r³"
- Source: `physics-classical-mechanics/chapters/12-uniform-circular-motion-and-gravitation.md`
- Topic: Orbital Mechanics and Kepler's Third Law
- Lane: MANIM (directed animation)
- Hook: Double the orbital radius and you expect the year to double. It doesn't — it nearly triples. T scales as r^(3/2), and that extra half-power is the hidden signature of inverse-square gravity.
- The rule: Orbital speed v = √(GM/r); centripetal condition: mv²/r = GMm/r². Period T = 2πr/v = 2πr^(3/2)/√(GM). Kepler's Third Law: T² ∝ r³, or T²/r³ = 4π²/(GM) = constant. For solar system: T in years, r in AU → T² = r³.
- Concrete numbers: Earth: r = 1 AU = 1.496×10¹¹ m, T = 1.00 yr, v = 29.8 km/s. Mars: r = 1.524 AU, T = 1.524^(3/2) = 1.881 yr, v = 24.1 km/s. Jupiter: r = 5.204 AU, T = 5.204^(3/2) = 11.87 yr, v = 13.1 km/s. ISS at r = 6.778×10⁶ m: v = 7,670 m/s, T = 92.3 min. Geostationary: r = 42,164 km, T = 24.0 hr, v = 3.07 km/s.
- The artifact / what moves: Top-down solar system view (inner planets + Jupiter, not to absolute scale but log-radius). Each planet traces its orbit at its actual T ratio. A log-log T vs r axis fills in as each planet's point drops onto the line T² ∝ r³. The slope is labeled 3/2. A "year counter" shows Earth lapping Mercury (Mercury: 0.241 yr) and Jupiter barely moving (11.87 yr) in the same screen time. A third panel: v vs r curve — v = √(GM/r) draws from Mercury to Jupiter; every planet's v drops off exactly as 1/√r.
- Output medium: Manim (mp4)
- Two testable predictions: P1: T²/r³ = constant = 1.00 yr²/AU³ for all planets; Jupiter's T² = 11.87² = 140.9 yr², r³ = 5.204³ = 140.8 AU³ — ratio 1.001; simulation must verify this ratio for all four planets shown to within 1%. P2: Halving the orbital radius increases orbital speed by √2 = 1.414 and decreases period by (1/2)^(3/2) = 0.354; a hypothetical planet at 0.5 AU orbits in 0.354 yr at v = 42.1 km/s; these must match the simulation's animated readout.
- The change: Replace circular with elliptical orbits (Kepler's first law). Show that the 3/2 log-log slope still holds when r is the semi-major axis. Animate conservation of angular momentum: the planet speeds up at perihelion and slows at aphelion — the area swept per unit time stays constant (Kepler's second law as a visible arc-sector fill).
- Human supplies (Claude can't): Nothing — fully synthetic/analytic; planetary data are textbook standard values.
- Teardown angle: The 3/2 exponent isn't geometry — it's proof that gravity falls as 1/r². Any other force law gives a different Kepler exponent. Newton worked backward: observed 3/2 → deduced inverse-square law. The log-log plot is the fingerprint.
- Exclusions: General relativistic precession; tidal locking; three-body problem; derivation of Kepler's laws from first principles.
- Sim slug: classical-kepler-third-law
- Score: 9/10
