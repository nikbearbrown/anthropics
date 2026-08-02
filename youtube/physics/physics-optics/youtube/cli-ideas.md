# Physics +1 (Optics) — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Double-Slit Interference Pattern Simulator with Claude

- Source: physics-optics/chapters/05-interference.md
- Lane: BUILD (Claude Code)
- Hook: LIGO measures a displacement of one-thousandth of a proton's diameter using this exact physics. Two waves, one phase difference — and either you get brightness or total darkness. Change the slit spacing by one nanometer and every fringe shifts.
- The artifact: A D3 animation of the two-slit intensity pattern I(y) = 4I₁ cos²(πd y / λL), drawing in real time as three sliders move: wavelength λ (400–700 nm, colored by visible light), slit separation d (0.1–1.0 mm), and screen distance L (0.5–5 m). The pattern animates its fringe spacing changing live. A second panel shows the two wavefronts radiating from the slits, with path-length-difference contours.
- Prompt seed: `claude "Build a D3 v7 single-file HTML double-slit interference simulator. X-axis: screen position y (-30 to +30 mm). Y-axis: intensity I/I_max. Draw I(y) = 4·cos²(π·d·y/(λ·L)) using sliders for λ (400–700 nm), slit separation d (0.1–1 mm), screen distance L (0.5–5 m). Color the curve by the wavelength's visible color. Second panel: animate wavefronts from two point sources with path-difference contours. Verify: fringe spacing Δy = λL/d; at λ=633nm, d=0.5mm, L=2m → Δy=2.53mm."`
- Read / check: Fringe spacing Δy = λL/d. At λ=633 nm, d=0.5 mm, L=2 m: Δy = 633×10⁻⁹ × 2 / 5×10⁻⁴ = 2.532 mm. Central max at y=0. First dark fringe at y = λL/(2d) = 1.266 mm. Verify that intensity oscillates 0–4I₁ (not 0–2I₁), confirming constructive interference is super-additive.
- Human supplies: Nothing — fully synthetic. All geometry analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add a coherence-length slider that applies a Gaussian envelope to the fringes — making the pattern fade out at large y as the path-length difference exceeds the coherence length. This shows why ordinary light (coherence length ~1 µm) cannot produce stable fringes without a laser.
- Teardown angle: Intensity does NOT add — amplitudes add and then you square. That non-linearity is the entire source of interference, and its consequence is that two beams can produce zero light at a specific location.
- Exclusions: Single-slit envelope modulation derivation, thin-film interference, polarization effects on coherence.
- Score: 9/10

---

## Candidate 02 — Simulate Snell's Law and Total Internal Reflection with Claude

- Source: physics-optics/chapters/02-reflection-refraction.md
- Lane: BUILD (Claude Code)
- Hook: Fiber-optic cable carries your internet across ocean floors using one inequality and one law. Below the critical angle, your data leaks into the cladding. Above it, every single photon bounces back. Compute the critical angle for any pair of materials and watch light route through glass.
- The artifact: A D3 ray-tracing animation: an incident ray (orange) hits a glass-air interface at a user-controlled angle. The reflected ray (blue) and refracted ray (green) draw from Snell's law n₁sinθ₁ = n₂sinθ₂. As the angle slider crosses the critical angle, the refracted ray swings to 90° and disappears — total internal reflection. A real-time readout shows θ_critical = arcsin(n₂/n₁) and whether TIR is active. A second "fiber" view shows a zig-zagging ray bouncing down a bent fiber.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Snell's law and TIR simulator. Show: incident ray (orange), reflected ray (blue), refracted ray (green) at a flat interface. Sliders: incident angle (0–89°), n1 (1.0–2.0), n2 (1.0–2.0). Compute refracted angle via Snell's law; when TIR occurs, show only reflection. Display critical angle θ_c = arcsin(n2/n1) when n1>n2. Second panel: ray bouncing in a fiber (TIR mode). Verify: glass-air (n1=1.5, n2=1.0) → θ_c = 41.8°."`
- Read / check: θ_c = arcsin(1.0/1.5) = arcsin(0.667) = 41.81°. Above this, no refracted ray, full reflection. Snell's law check: at θ₁=30°, n₁=1.5, n₂=1.0: sinθ₂ = 1.5×sin30°/1.0 = 0.75, θ₂ = 48.6°. Refracted ray bends away from normal as expected for n₁>n₂.
- Human supplies: Nothing — fully synthetic. The second "fiber bounce" panel is purely geometric.
- Output medium: d3 (animated, single HTML file)
- The change: Add Brewster's angle: a second readout shows θ_B = arctan(n₂/n₁) and marks the angle at which the reflected ray is fully polarized, with the reflected intensity bar split into s- and p-polarization components (Fresnel equations).
- Teardown angle: Total internal reflection is not reflection "happening more" — it is Snell's law having no real solution for θ₂ when sinθ₂ would exceed 1. The boundary condition fails and the entire wave reflects. It is a constraint violation, not a physical force.
- Exclusions: Evanescent waves, frustrated TIR, fiber attenuation dB/km.
- Score: 9/10

---

## Candidate 03 — Build a Diffraction Grating Spectrometer Simulator with Claude

- Source: physics-optics/chapters/06-diffraction.md
- Lane: BUILD (Claude Code)
- Hook: The grating equation d sinθ = mλ is the reason we know the composition of the Sun, the recession velocity of galaxies, and the structure of DNA. A few thousand lines per millimeter and every wavelength lands at a different angle — compute the positions and resolving power yourself.
- The artifact: A D3 animation of a diffraction grating: a user-selected light source (white, sodium lamp, hydrogen discharge, or custom wavelengths) illuminates a grating of N slits with spacing d. The principal maxima positions animate on a screen, with each order m labeled. A wavelength selector highlights each line in its visible color. A resolving power readout R = mN updates live. A second panel shows the intensity envelope I(θ) = [sin(Nφ/2)/sin(φ/2)]² × [sinc(πa sinθ/λ)]² drawing in real time.
- Prompt seed: `claude "Build a D3 v7 single-file HTML diffraction grating simulator. Sliders: grating spacing d (1–10 µm), number of slits N (10–1000), wavelength (400–700 nm, or multi-wavelength list for Na doublet at 589.0/589.6 nm, H Balmer at 656/486/434 nm). Show: (1) angular positions of all principal maxima for m=0,±1,±2, colored by wavelength, (2) intensity profile I(θ), (3) resolving power R = mN. Verify: sodium doublet resolved when R = mN > 589/0.6 ≈ 1000."`
- Read / check: For d=2 µm, λ=550 nm: sinθ_m = mλ/d, m=1: sinθ=0.275, θ=15.96°. Resolving power R=mN. Sodium doublet Δλ=0.6 nm at λ=589 nm: need R>589/0.6≈982. At m=1 this requires N>982 slits. Verify the multi-wavelength case produces a clean separation of the two sodium D lines at N=1000.
- Human supplies: Nothing — fully synthetic. The grating intensity formula is analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add the Rayleigh criterion for two barely-resolved wavelengths — animate a pair of lines slowly merging as N decreases until they overlap at R < λ/Δλ. This makes "resolving power" visceral rather than abstract.
- Teardown angle: The grating is not selecting wavelengths — it is exploiting the fact that different wavelengths satisfy the constructive-interference condition at different angles. The physics is identical to two-slit interference, just applied to thousands of slits simultaneously.
- Exclusions: Blazed gratings, echelle spectrometers, reflection vs. transmission gratings.
- Score: 9/10

---

## Candidate 04 — Trace Rays Through a Two-Lens System with Claude

- Source: physics-optics/chapters/04-lenses.md
- Lane: BUILD (Claude Code)
- Hook: The optometrist who prescribes your glasses and the engineer who designed the Hubble telescope are both using the same three lines of algebra. Build a two-lens ray tracer and watch the image move from real to virtual as the object crosses the focal point.
- The artifact: A D3 interactive ray diagram for a two-lens system: two lenses on a common optical axis, each with a focal length slider (f₁ and f₂, positive or negative), and a draggable object arrow. Three principal rays trace from the object tip through each lens using the thin-lens equation. The image location, magnification, and real/virtual/upright/inverted status updates live. As the object crosses the first focal point, the animation shows the image jump from real (right of lens) to virtual (left).
- Prompt seed: `claude "Build a D3 v7 single-file HTML two-lens ray tracer. Two lenses on an optical axis, each with draggable focal points and sliders for f1 (-200 to +200 mm) and f2 (-200 to +200 mm). Draggable object at any position. Draw the 3 principal rays for each lens. Apply thin-lens equation sequentially: first-lens image becomes second-lens object. Display: d_o, d_i, m for each lens and total m. Label image: real/virtual, upright/inverted. Verify: two lenses f1=f2=50mm, object at d_o=100mm → final image at d_i=100mm (telescope mode), m=+1."`
- Read / check: Thin-lens eq: 1/f = 1/d_o + 1/d_i. Stage 1: f=50mm, d_o=100mm → 1/d_i = 1/50 - 1/100 = 1/100 → d_i=100mm. Stage 2: second lens at d_o = L - 100mm (where L = separation). Verify magnification m = (-d_i/d_o)×(-d_i2/d_o2). Check sign conventions: positive d_i = real image on far side of lens.
- Human supplies: Nothing — fully synthetic. All geometry from thin-lens equations.
- Output medium: d3 (animated, single HTML file)
- The change: Build a third tab: the human eye with corrective lens — model the too-long eyeball (myopia), show the uncorrected image falling in front of the retina, then add a negative corrective lens and show the image snapping onto the retina. Compute the required lens power in diopters.
- Teardown angle: The thin-lens equation is the same for cameras, eyes, and telescopes — what differs is which distances you control and which you solve for. The lensmaker's equation is the hardware constraint; the thin-lens equation is the geometry.
- Exclusions: Lens aberrations (spherical, chromatic) detailed correction, thick lens formulas, mirror equivalents.
- Score: 8/10

---

## Candidate 05 — Build a Single-Photon Double-Slit Dot-by-Dot Simulator with Claude

- Source: physics-optics/chapters/10-capstone-quantum-optics.md
- Lane: BUILD (Claude Code)
- Hook: Lower the light so much that only one photon is in the apparatus at a time. Each photon makes a single dot. After 50,000 dots, you have the interference pattern. No photon "chose" where to land — the distribution is the physics.
- The artifact: A D3 animation that adds dots to a screen one at a time. Each dot's y-position is sampled from the two-slit probability distribution P(y) = 4I₁cos²(πdy/λL). After N dots (slider: 1 to 10,000), the scatter plot gradually reveals the interference pattern. An overlay of the theoretical I(y) curve appears after 1000 dots. A side histogram builds up, progressively matching the analytic curve.
- Prompt seed: `claude "Build a D3 v7 single-file HTML single-photon double-slit simulator. One dot per frame, y-position sampled from P(y) = cos²(π·d·y/(λ·L)) (normalized). Speed slider (dots per second). Accumulate N dots on a dark screen (dots in white). After N>1000, overlay the theoretical intensity curve. Histogram panel shows dot density vs. y updating live. Verify: after 10000 dots the histogram matches the theoretical pattern to within statistical noise. Sliders: λ, d, L."`
- Read / check: The dot distribution should converge to cos²(πdy/λL) as N → ∞. Test: for parameters giving 5 bright fringes across the screen, after 5000 dots the 5 peaks should be visually distinct. Verify the random seed samples from the correct distribution (inverse CDF or rejection sampling of cos² pattern).
- Human supplies: Nothing — fully synthetic. Random sampling from a cos² distribution is straightforward.
- Output medium: d3 (animated, single HTML file)
- The change: Add a "which-way" toggle that places a detector at one slit. When active, the dots lose their interference pattern and become a broad Gaussian. This demonstrates the complementarity principle: knowing which slit destroys the interference.
- Teardown angle: The interference pattern is not built by photons "knowing about each other" — it is the probability distribution of a single photon's wave function. What accumulates over many shots is the shape of |ψ|².
- Exclusions: Full quantum field theory derivation, photon anti-bunching (HBT experiment), entanglement.
- Score: 8/10

---

## Candidate 06 — Animate the Telescope Rayleigh Resolution Limit with Claude

- Source: physics-optics/chapters/08-optical-instruments.md
- Lane: BUILD (Claude Code)
- Hook: The Hubble Space Telescope can resolve a coin from 500 km. The formula that says so — θ_min = 1.22λ/D — also says you could double the resolution if you doubled the mirror. Build the simulation that makes two stars merge as their separation drops below the limit.
- The artifact: A D3 animation showing two point sources (stars) whose angular separation decreases from 5×θ_min to 0. The Airy disk pattern for each source is computed and summed; the combined image animates from clearly separated to just barely resolved (Rayleigh criterion: first dark ring of one Airy disk at center of other) to merged. A telescope diameter slider D (0.1 m to 8 m) and wavelength slider λ (400–800 nm) update θ_min = 1.22λ/D live. The angular resolution in arcseconds is displayed.
- Prompt seed: `claude "Build a D3 v7 single-file HTML telescope resolution simulator. Two point sources separated by Δθ (slider from 5×Rayleigh to 0). Each source produces an Airy disk pattern: I(r) ∝ [2J₁(πDr/λ)/(πDr/λ)]² computed via Bessel J1 approximation. Sum the two patterns. Sliders: D (0.1–10m), λ (400–800 nm). Display: θ_min = 1.22λ/D in arcseconds. At Rayleigh separation, show the barely-resolved pair. Verify: Hubble (D=2.4m, λ=550nm) → θ_min ≈ 0.058 arcseconds."`
- Read / check: θ_min = 1.22×550×10⁻⁹/2.4 = 2.796×10⁻⁷ rad = 0.0577 arcsec. At Rayleigh criterion: the dip between two Airy disks should be 73.5% of the peak (the classic Rayleigh dip). Verify the Bessel J₁ approximation (or numerically compute) produces the correct first zero at r = 1.22λ/D.
- Human supplies: Nothing — fully synthetic. Airy disk computation is analytic (or numerically approximated via series expansion for J₁).
- Output medium: d3 (animated, single HTML file)
- The change: Add a third source at the center and show a triple star barely resolved — stress-testing the Rayleigh criterion for a more complex scene.
- Teardown angle: The diffraction limit is not a flaw of the optics — it is the uncertainty principle applied to photon momentum. A smaller aperture means less known about the transverse photon momentum, hence a larger diffraction cone.
- Exclusions: Adaptive optics correction, speckle imaging, interferometric aperture synthesis (VLBI).
- Score: 8/10

---

## Candidate 07 — Visualize Jones Calculus for Polarization with Claude

- Source: physics-optics/chapters/07-polarization.md
- Lane: BUILD (Claude Code)
- Hook: The LCD screen you're reading on right now works because a thin slab of crystals rotates polarization by exactly 90°. Jones calculus is the 2×2 matrix system that predicts every pixel state. Build the three-polarizer paradox and watch crossed polarizers transmit light when you insert a 45° sheet between them.
- The artifact: A D3 animation showing the E-field tip tracing its polarization ellipse in real time as Jones matrices are applied in sequence. The user builds a chain of optical elements (polarizer, quarter-wave plate, half-wave plate) by dragging them into a sequence. The output intensity and polarization ellipse update after each element. The three-polarizer paradox is the first demo: H-polarizer → 45° polarizer → V-polarizer, with intensity readout showing non-zero transmission.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Jones calculus visualizer. Show: (1) animated E-field tip tracing polarization ellipse, (2) a drag-and-drop optical element chain (polarizer at angle θ, QWP, HWP), (3) output intensity I/I₀ = |J_out|² after chain. Implement Jones matrices: polarizer P(θ)=[[cos²θ, cosθsinθ],[sinθcosθ,sin²θ]], QWP Q=exp(-iπ/4)[[1,0],[0,i]]. Show: three-polarizer paradox. Verify: H-pol → 45° pol → V-pol → I/I₀ = 0.25."`
- Read / check: Three-polarizer: H-pol Jones vector [1,0]. After 45° polarizer: [1/√2, 1/√2]/√2 = [0.5, 0.5] (amplitude), I = 0.5. After V-pol: [0, 0.5], I = 0.25. So 25% transmitted. Verify QWP converts linear to circular: [1,0] → QWP → [1,i]/√2, then ellipse should be a circle.
- Human supplies: Nothing — fully synthetic. Jones matrix algebra is pure linear algebra.
- Output medium: d3 (animated, single HTML file)
- The change: Add a second demo: the LCD pixel — H-pol → twisted nematic LC (rotates by user-specified angle, implemented as a rotation matrix) → V-pol. Show pixel brightness vs. twist angle. At 0° twist (voltage on): black pixel. At 90° twist: white pixel.
- Teardown angle: The three-polarizer paradox is not a paradox — it is the result of measuring in an intermediate basis. The second polarizer does not "let more light through" — it creates a new component along the V direction that wasn't present before.
- Exclusions: Mueller matrices (for partially polarized light), birefringence derivation from Maxwell's equations, crystal optics.
- Score: 8/10

---

## Candidate 08 — Simulate a Michelson Interferometer and Measure Wavelength with Claude

- Source: physics-optics/chapters/05-interference.md, chapters/09-coherence-lasers.md
- Lane: BUILD (Claude Code)
- Hook: LIGO uses a Michelson interferometer to measure arm-length differences of 10⁻¹⁸ m. The same instrument in 1887 found nothing — and that null result overthrew classical physics. Build the interferometer, drag one mirror, and watch the fringe pattern shift to measure wavelength.
- The artifact: A D3 animation of a Michelson interferometer: a beamsplitter, two mirrors (one fixed, one moveable via slider), two return beams recombining. The path-length difference Δ = 2Δx is computed live. The output intensity I = I₀(1 + cosφ) where φ = 2π·Δ/λ updates live. A fringe counter in the center shows how many fringes have passed as the mirror moves — from which λ = 2Δx/N is computed. This is the actual method used to define the meter from 1889 to 1960.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Michelson interferometer simulator. Show: (1) optical path diagram with beamsplitter and two mirrors, (2) mirror-2 position slider (0–2 µm travel), (3) output intensity I = I₀·(1+cos(2π·2Δx/λ)) plotted vs. mirror position (circular fringe pattern and/or 1D oscillation), (4) fringe counter N and computed wavelength λ_meas = 2Δx/N. Sliders: λ (400–700 nm), initial alignment. Verify: for λ=633nm, one full fringe cycle = 316.5 nm mirror travel."`
- Read / check: One fringe = one path-length change of λ (i.e., mirror moves λ/2). For λ=633 nm: mirror moves 316.5 nm per fringe. At Δx=1 µm travel: N = 2×10⁻⁶/633×10⁻⁹ = 3.16 fringes. Verify counter increments at correct mirror positions. Computed λ_meas should match input λ within numerical precision.
- Human supplies: Nothing — fully synthetic. All geometry analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add a second arm-length comparison scenario: the Michelson-Morley experiment setup. Both arm lengths equal, but the ether-wind speed slider changes expected phase difference. Output: predicted fringe shift (classical ether theory) vs. observed shift = 0 (null result). This recreates the experiment that ended classical physics.
- Teardown angle: The Michelson interferometer converts path-length differences into intensity changes with a sensitivity limited only by the coherence length of the source. LIGO's 10⁻¹⁸ m sensitivity is this same principle with 4 km arms, 100 kW laser, and squeezed-light enhancement.
- Exclusions: Finesse, Fabry-Perot etalon, heterodyne detection.
- Score: 7/10

---

## Candidate 09 — Simulate the Lensmaker's Equation: Design a Prescription Lens with Claude

- Source: physics-optics/chapters/04-lenses.md
- Lane: BUILD (Claude Code)
- Hook: An optometrist writes −2.50 D on your prescription and orders a lens ground to specific radii of curvature. The lensmaker's equation connects those radii to the focal power you need. Build the design tool and find the glass curves that correct 5 diopters of myopia.
- The artifact: A D3 interactive showing a lens cross-section with two curved surfaces (R₁ and R₂ sliders, positive or negative). The lensmaker's equation 1/f = (n−1)[1/R₁ − 1/R₂] computes the focal length live. A power readout in diopters P = 1/f (with f in meters) updates. The viewer can also set a target power (e.g., −2.5 D) and watch which combinations of R₁, R₂ satisfy it — a curve in the (R₁, R₂) design space is plotted.
- Prompt seed: `claude "Build a D3 v7 single-file HTML lensmaker's equation calculator. Sliders: R1 (-500 to +500 mm, center of curvature direction), R2 (-500 to +500 mm), n (1.4–1.9 for glass). Compute: 1/f = (n-1)*(1/R1 - 1/R2). Display: f in mm, P in diopters = 1000/f. Cross-section drawing of the lens shape (arc-of-circle approximation for each surface). Second panel: the (R1,R2) curve satisfying 1/f = target power for a given n. Verify: n=1.5, R1=100mm, R2=-100mm → f=100mm (equiconvex, P=10D)."`
- Read / check: For n=1.5, equiconvex (R₁=100, R₂=−100): 1/f = 0.5×(1/100 − 1/(−100)) = 0.5×(0.01 + 0.01) = 0.01 mm⁻¹, f=100 mm, P=10 D. For plano-convex (R₁=100, R₂=∞): 1/f = 0.5×(1/100 − 0) = 0.005, f=200 mm, P=5 D. Check shape renders correctly (concave vs. convex for each sign).
- Human supplies: Nothing — fully synthetic. Lensmaker's equation is analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add dispersion: the refractive index varies with wavelength via Cauchy's equation n(λ) = A + B/λ². Show how the focal length differs for red (700 nm) and blue (400 nm) — this is chromatic aberration — and compute the achromatic doublet condition for two glasses.
- Teardown angle: The lensmaker's equation encodes the fact that a lens works by refracting at two surfaces, not one. The "focusing power" of each surface adds. The equation is just Snell's law applied twice at the paraxial limit.
- Exclusions: Thick lens formula, aspheric lens design, Seidel aberration coefficients.
- Score: 7/10

---

## Candidate 10 — Build a Gaussian Beam and Laser Cavity Mode Visualizer with Claude

- Source: physics-optics/chapters/09-coherence-lasers.md
- Lane: BUILD (Claude Code)
- Hook: A laser beam is not a cylinder of light — it is a Gaussian beam that focuses to a waist, then diverges with an angle determined by its wavelength and waist size. The Rayleigh range tells you how far the beam stays collimated. Build the visualizer and find the parameters that collimate a HeNe laser over 1 km.
- The artifact: A D3 animation of a Gaussian beam profile: the beam width w(z) = w₀√(1 + (z/z_R)²) plotted as the beam expands from a waist w₀ at z=0. Sliders for w₀ (0.1–10 mm) and λ (400–1000 nm) update z_R = πw₀²/λ and the divergence half-angle θ = λ/(πw₀). A second panel shows the laser cavity: two mirrors separated by L, with the Gaussian mode bouncing between them, and mode spacing Δν = c/(2L) computed.
- Prompt seed: `claude "Build a D3 v7 single-file HTML Gaussian beam visualizer. Show: (1) beam width w(z) = w₀√(1+(z/z_R)²) from z=-5z_R to +5z_R, with the waist region shaded, (2) sliders for w₀ (0.1–10mm) and λ (400–1000nm), (3) readout of z_R = π·w₀²/λ (Rayleigh range), far-field divergence θ = λ/(π·w₀) in mrad. Second panel: laser cavity of length L (slider), cavity mode spacing Δν = c/(2L) in MHz. Verify: HeNe λ=633nm, w₀=1mm → z_R = π×10⁻⁶/633×10⁻⁹ = 4.97m, θ = 0.633/π mrad = 0.201 mrad."`
- Read / check: z_R = π×(10⁻³)²/(633×10⁻⁹) = π×10⁻⁶/6.33×10⁻⁷ = 4.97 m. θ = 633×10⁻⁹/(π×10⁻³) = 2.015×10⁻⁴ rad = 0.201 mrad. At z = z_R, w = √2 × w₀. Cavity: L=0.3m → Δν = 3×10⁸/(2×0.3) = 500 MHz. Verify the beam width formula is symmetric around z=0.
- Human supplies: Nothing — fully synthetic. Gaussian beam formula is analytic.
- Output medium: d3 (animated, single HTML file)
- The change: Add a focusing element: a thin lens placed at z=d from the waist. Compute the new waist location and size using the Gaussian beam transformation through a lens. Show how a collimating lens placed at z=z_R makes the divergence much smaller.
- Teardown angle: The Gaussian beam is the fundamental solution to the paraxial wave equation — the best-collimated beam any laser can produce. The product w₀ × θ = λ/π is the diffraction-limited beam parameter product; you cannot beat it with any optics.
- Exclusions: Higher-order transverse modes (Hermite-Gauss, Laguerre-Gauss), ABCD ray matrix formalism, nonlinear optics.
- Score: 7/10
