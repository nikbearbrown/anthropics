# CAJAL figure candidates — electron-microscopy (previz track)

Electron microscopy textbook: classical resolution limit → electron optics → SEM → TEM → spectroscopy → tomography → cryo-EM → sample preparation → artifacts → applications. Mechanism and structural figures mined chapter-by-chapter. Blank unannotated vector — no baked text; previz owns every symbol (λ, V, α, d, Z …). Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

> De-confliction: this book owns electron-microscopy instrumentation and technique diagrams; the imaging-in-cancer book owns clinical modality figures (CT, MRI, PET, fluorescence). Overlapping topic — interaction volume — is treated here as instrumentation physics; the cancer book treats it as a clinical method decision.

---

## 1. abbe-resolution-limit  — wavelength sets the floor; shorter wavelength, finer detail  (MC · comparison/two-panel · Critical)
*Source: chapter 02 — "Electron Optics and Resolution"*

**PASTE:** Draw a blank two-panel side-by-side comparison on a white background. Left panel: a simple circular lens outline (representing light optics) above two point sources separated by a gap, with two overlapping bell-shaped intensity humps below that are barely resolved — the humps nearly merge. Right panel: a tighter circular lens outline (representing electron optics) above the same two point sources, with two sharper, more separated bell-shaped humps that are clearly resolved. No internal lens anatomy, no numerical scales. Uniform strokes, flat fills, no shading, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] Rayleigh/Abbe resolution limit; two point objects; wider humps = longer wavelength = unresolved; narrower humps = shorter wavelength = resolved.
- [O] side-by-side; top: lens symbol; middle: two point sources; bottom: intensity hump pair; right panel is the superior case.
- [P] flat vector, Okabe-Ito: lens outlines neutral gray, unresolved humps Orange #E69F00, resolved humps Blue #0072B2. No baked text.
- [E] exclude: formula text, wavelength numerals, ray-tracing geometry, three-panel variants, a photograph.

**NEGATIVE:** formula text, wavelength numbers, Abbe equation, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 2. gun-type-comparison  — thermionic vs Schottky vs cold FEG: brightness staircase  (VG · comparison panels · Important)
*Source: chapter 03 — "Sources, Lenses, Detectors and Components"*

**PASTE:** Draw a blank three-panel vertical stack on a white background. Each panel is a minimal cross-section of one gun type showing only the tip and extraction geometry. Top panel: a hairpin-wire arch tip (thermionic); source glow region wide. Middle panel: a tapered crystal tip on a base (LaB6 / Schottky), glow region narrower. Bottom panel: a sharper needle tip (cold FEG), glow region very small. Represent the emitted-electron cloud below each tip as a tapered cone — wide for thermionic, medium for Schottky, narrow for cold FEG. Uniform strokes, flat fills, no shading, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] thermionic (large source, low brightness); Schottky FEG (intermediate); cold FEG (tiny virtual source, highest brightness). The emission-cone width is the visual proxy for brightness and energy spread.
- [O] three stacked panels, same frame; top = worst, bottom = best; cone width changes are the crux.
- [P] flat vector, Okabe-Ito: tip metal neutral gray, emission cone Orange #E69F00 (thermionic) / Sky Blue #56B4E9 (Schottky) / Blue #0072B2 (cold FEG). No baked text.
- [E] exclude: voltage numbers, extraction-aperture detail, LaB6 crystal atomic structure, brightness values, temperature annotations.

**NEGATIVE:** voltage numbers, temperature labels, brightness values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 3. interaction-volume-teardrop  — accelerating voltage dictates how deep the beam penetrates  (MC · structural schematic · Critical)
*Source: chapter 06 — "Beam-Specimen Interactions"*

**PASTE:** Draw a blank interaction-volume schematic on a white background: a flat horizontal specimen surface (a thick gray band), with a narrow electron beam arrow entering from above straight down into the surface. Below the surface, draw three nested pear/teardrop outlines, each centered on the beam entry point, each progressively larger and deeper into the specimen — small innermost, medium middle, large outermost. All shapes are symmetric and elongated downward. No cross-hatching, no subsurface detail, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] beam enters specimen and generates a pear-shaped interaction volume; at low kV the volume is shallow and narrow (inner teardrop); at moderate kV medium; at high kV deep and wide (outer teardrop). Three nested outlines represent three voltage regimes.
- [O] vertical: surface at top; beam arrow enters from above; teardrops nested concentrically below.
- [P] flat vector, Okabe-Ito: surface band neutral gray, beam arrow Black #000000, inner volume Bluish Green #009E73, middle volume Blue #0072B2, outer volume Orange #E69F00. No baked text.
- [E] exclude: kV numbers, Kanaya-Okayama equation, secondary-electron escape depth marker, BSE signal annotation, material-property labels.

**NEGATIVE:** kV numbers, depth markers, SE/BSE labels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 4. sem-detector-geometry  — Everhart-Thornley detector position determines signal type collected  (VG · structural schematic · Important)
*Source: chapter 07 — "SEM Detectors and Image Formation"*

**PASTE:** Draw a blank SEM chamber cross-section on a white background: a vertical electron beam arrow entering from the top center striking a specimen surface (horizontal band). On the right side of the chamber, show one small rectangular detector housing with a Faraday cage grid in front of it (the ET detector). Above the objective lens, show one small circular detector aperture (the in-lens detector position). Draw a few short curved arrows from the specimen surface — some pointing broadly toward the ET detector (secondary electrons), a few pointing steeply upward toward the in-lens aperture (backscattered). No labels, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] ET (Everhart-Thornley) detector positioned to side with bias grid; in-lens detector positioned on axis above objective; secondary electrons curve toward ET due to grid bias; backscattered travel steeply upward.
- [O] vertical beam; specimen at center base; ET detector to right; in-lens marker at top; electron trajectory arrows diverge from specimen.
- [P] flat vector, Okabe-Ito: beam Black #000000, specimen band neutral gray, ET detector Orange #E69F00, in-lens detector Blue #0072B2, SE trajectory arrows Bluish Green #009E73, BSE trajectory arrows Sky Blue #56B4E9. No baked text.
- [E] exclude: numerical bias voltages, scintillator/PMT internal anatomy, exact geometry dimensions, BSE detector ring, cathodoluminescence hardware.

**NEGATIVE:** bias voltage numbers, internal PMT anatomy, numerical dimensions, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 5. eds-xray-generation  — inner-shell ionization → characteristic X-ray or Auger electron  (MC · mechanism cross-section · Critical)
*Source: chapter 09 — "Energy Dispersive Spectroscopy"*

**PASTE:** Draw a blank atomic X-ray emission mechanism on a white background: two concentric circles representing K and L electron shells around a central nucleus dot. On the left, show an incoming electron arrow striking and ejecting one electron from the inner (K) shell (the ejected electron is shown as a dot leaving the atom). Then show a filling arrow from the L shell to the vacancy in the K shell, accompanied by a wavy arrow representing the emitted X-ray photon leaving to the right. All elements minimal — only nucleus dot, two shell circles, one ejected electron dot, one fill arrow, one wavy photon arrow. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] incident electron knocks out K-shell electron (ionization); L-shell electron fills vacancy; energy difference released as characteristic K-alpha X-ray. This is the origin of EDS peaks.
- [O] left-to-right sequence: incoming beam → ionization → vacancy fill → X-ray emission; two-shell atom centered.
- [P] flat vector, Okabe-Ito: nucleus neutral gray filled circle, K shell Blue #0072B2 circle, L shell Sky Blue #56B4E9 circle, incident electron Black #000000 arrow, ejected electron Vermillion #D55E00 dot with arrow, fill arrow Bluish Green #009E73, X-ray wavy arrow Orange #E69F00. No baked text.
- [E] exclude: M/N shells, Auger electron path, characteristic energy numbers, atomic number labels, detector geometry.

**NEGATIVE:** shell labels, energy numbers, atomic number, Auger path, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 6. cpd-phase-diagram  — critical-point drying avoids the liquid-vapor boundary  (MC · cycle/path · Important)
*Source: chapter 08 — "SEM Sample Preparation"*

**PASTE:** Draw a blank CO2-like phase diagram on a white background: two curved boundary lines meeting at a single point (the critical point, marked with a small filled circle) — one boundary representing solid-liquid, one representing liquid-vapor. Show two paths from a lower-left starting point to the upper-right gaseous region. Path A: a dashed arrow that crosses the liquid-vapor boundary directly (the "wrong" path — direct evaporation). Path B: a solid arrow that curves around above and to the right of the critical point without crossing any phase boundary (the CPD path). No region labels, no axis text, no phase-name annotations.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] CO2 P-T phase diagram; critical point at top of liquid-vapor coexistence curve; direct evaporation crosses the boundary (wrong); CPD path goes supercritical, avoids the boundary (correct).
- [O] implicit T-axis (horizontal), implicit P-axis (vertical); boundary curves center-frame; critical point dot; two paths diverge from starting point.
- [P] flat vector, Okabe-Ito: phase boundary curves neutral gray, critical point dot Black #000000 filled, wrong path (direct evaporation) Vermillion #D55E00 dashed arrow, CPD path Blue #0072B2 solid arrow. No baked text.
- [E] exclude: axis tick marks, temperature or pressure values, phase-region fill, chemical formula, text annotations.

**NEGATIVE:** temperature numbers, pressure values, text region labels, chemical formulas, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 7. tem-column-schematic  — from gun to camera: the relay chain of lenses  (VG · structural schematic · Critical)
*Source: chapter 13 — "TEM Instrument Design and Operation"*

**PASTE:** Draw a blank TEM column cross-section on a white background: a tall vertical rectangle representing the column. Stack from top to bottom, evenly spaced, six labeled zones — represented only as narrow horizontal bands of different fill: gun zone (top), condenser-1 lens band, condenser-2 lens band, specimen slot (slightly wider gap), objective lens band, projector lenses band (one band representing the group), camera/detector plane (bottom rectangle). Draw a single vertical beam line running through all zones. No text, no anatomical detail inside each band.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] TEM column as a six-zone vertical stack: electron gun → two condenser lenses → specimen → objective lens → projector system → detector/camera. The relay chain concept.
- [O] top-to-bottom; beam runs through center; bands represent major functional zones; widths uniform.
- [P] flat vector, Okabe-Ito: column outline neutral gray, beam line Black #000000, gun zone Orange #E69F00, condenser bands Sky Blue #56B4E9, specimen slot Reddish Purple #CC79A7, objective band Blue #0072B2, projector band Bluish Green #009E73, camera band Yellow #F0E442. No baked text.
- [E] exclude: polepiece geometry, coil windings, vacuum pump connections, crossover positions, magnification numerals.

**NEGATIVE:** coil detail, vacuum anatomy, magnification numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 8. tem-bf-df-aperture  — aperture position in the back focal plane determines bright-field vs dark-field  (MC · comparison panels · Critical)
*Source: chapter 14 — "Image Formation in TEM"*

**PASTE:** Draw a blank two-panel comparison on a white background. Each panel shows a schematic objective lens (a horizontal oval) with a specimen strip above it and an aperture disk below. In the back focal plane below the lens, show three spots in a horizontal row representing the diffraction pattern: one central spot (direct beam) and one spot on each side (diffracted beams). Left panel (bright-field): the aperture circle surrounds only the central spot. Right panel (dark-field): the aperture circle is shifted to surround one of the off-axis diffracted spots. No image planes shown, no ray-tracing lines. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] objective aperture placed at the back focal plane selects which beams form the image; centered aperture → bright-field (direct beam only); off-axis aperture → dark-field (one diffracted beam only).
- [O] two side-by-side panels; aperture ring shifts laterally between panels; diffraction spots remain fixed.
- [P] flat vector, Okabe-Ito: lens body neutral gray oval, specimen band neutral gray, direct-beam spot Blue #0072B2, diffracted spots Sky Blue #56B4E9, aperture ring Orange #E69F00. No baked text.
- [E] exclude: intermediate lenses, image-plane representation, interference fringe formation, aperture-size numbers, specimen detail.

**NEGATIVE:** intermediate lenses, image plane, fringe formation, aperture size numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 9. diffraction-three-patterns  — single crystal spots, polycrystalline rings, amorphous halo  (VG · comparison panels · Important)
*Source: chapter 15 — "Diffraction in TEM"*

**PASTE:** Draw a blank three-panel side-by-side comparison on a white background. Each panel is a square frame representing a diffraction pattern screen. Left panel: several bright spots arranged in a symmetric grid pattern (single crystal). Middle panel: concentric rings with no individual spots (polycrystalline aggregate). Right panel: one broad diffuse ring with fuzzy edges (amorphous material). All panels same size. Central spot implied but not dominant. Uniform strokes, no shading, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] three specimen types produce three diffraction pattern morphologies: single-crystal → spot array; polycrystal → Debye-Scherrer rings; amorphous → diffuse halo. The pattern shape diagnoses the specimen order.
- [O] three equal-width panels, left to right in order of decreasing crystalline order; central beam spot implied; rings replace spots as order decreases.
- [P] flat vector, Okabe-Ito: background white, spots Blue #0072B2 (left), rings Sky Blue #56B4E9 (middle), halo Reddish Purple #CC79A7 (right). Panel borders neutral gray. No baked text.
- [E] exclude: d-spacing numbers, Miller indices, scale bar, camera-length annotation, specimen photographs.

**NEGATIVE:** d-spacing values, Miller indices, scale bar, camera length numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 10. tem-contrast-mechanisms  — mass-thickness vs diffraction contrast: different rules, different specimens  (VG · comparison panels · Critical)
*Source: chapter 16 — "TEM Contrast Mechanisms"*

**PASTE:** Draw a blank two-panel comparison on a white background. Each panel shows a cross-section of a thin specimen above an aperture, with a transmitted-beam arrow below. Left panel (mass-thickness contrast): the specimen has two regions of different thickness or density shown as differing shades of gray fill — a thicker/denser dark region and a thinner/lighter region; the beam arrow beneath the dark region is thinner (less intensity transmitted). Right panel (diffraction contrast): the specimen is uniform thickness but shows one grain tilted (its outline slightly angled) relative to a neighboring grain; beneath the tilted grain the beam arrow is thinner (diffracted away). No labels, no ray lines, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] mass-thickness contrast: heavy or thick regions scatter more → appear dark in bright-field (left). Diffraction contrast: a crystalline grain at Bragg condition diffracts strongly → also appears dark in bright-field, but mechanism is diffraction not mass (right).
- [O] two side-by-side panels; each shows specimen cross-section + transmitted-beam proxy; contrast origin differs between them.
- [P] flat vector, Okabe-Ito: specimen neutral gray, dense/thick region Blue #0072B2 (left panel), tilted grain Orange #E69F00 (right panel), beam arrows Black #000000 with width indicating intensity. No baked text.
- [E] exclude: formula text, extinction-length values, weak-beam dark-field setup, phase contrast / HRTEM, Z-contrast (HAADF).

**NEGATIVE:** formula text, extinction length, weak-beam detail, HRTEM lattice fringes, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 11. stem-detector-zones  — one probe scan, three concentric detector rings, three simultaneous images  (MC · structural schematic · Critical)
*Source: chapter 17 — "Advanced TEM Imaging Modes: HRTEM, STEM, and HAADF"*

**PASTE:** Draw a blank STEM detector geometry diagram on a white background: a thin horizontal specimen strip, below it a vertical gap, then three concentric ring/disk shapes centered on the beam axis. The innermost shape is a filled circle (bright-field detector, collecting the direct beam). Around it a hollow ring (annular dark-field, ADF, at moderate angles). Around that a wider hollow ring (high-angle annular dark-field, HAADF, at large angles). A small dot above the specimen represents the focused probe position. Three arrows from different electron trajectories reach the three different detector zones. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] STEM geometry: focused probe scans specimen; electrons scattered at different angles are collected by three nested detector zones simultaneously — on-axis BF, moderate-angle ADF, large-angle HAADF. Each produces a different contrast image.
- [O] top: probe dot on specimen; center: gap; bottom: three concentric detector shapes; trajectory arrows connect scattering angles to detector zones.
- [P] flat vector, Okabe-Ito: specimen neutral gray, probe dot Black #000000, BF detector Blue #0072B2, ADF ring Sky Blue #56B4E9, HAADF ring Orange #E69F00, trajectory arrows Bluish Green #009E73 (BF), Reddish Purple #CC79A7 (ADF), Vermillion #D55E00 (HAADF). No baked text.
- [E] exclude: Z-dependence formula, collection angle numbers, convergence angle annotation, lens above specimen, EELS spectrometer below.

**NEGATIVE:** Z-formula, angle numbers, convergence annotation, lens detail, EELS spectrometer, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 12. eels-spectrum-regions  — zero-loss, plasmon, and core-loss edges in one spectrum  (VG · structural schematic · Important)
*Source: chapter 18 — "EELS"*

**PASTE:** Draw a blank EELS spectrum schematic on a white background: a horizontal axis (energy loss increases left to right) and a vertical axis (signal intensity). Draw one spectrum as a continuous curve: at the leftmost position a tall sharp peak (zero-loss peak, ZLP); to its right a smaller broader bump (plasmon peak, low-loss region); then a long declining baseline followed by two distinct step-up edges with sawtooth profile, separated by a gap (core-loss edges from two different elements). The curve must be a single continuous path. No axis labels, no tick marks, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] EELS spectrum: three distinct regions — zero-loss peak (elastically scattered electrons), low-loss region (plasmon, phonon ~5–50 eV), core-loss edges (element-specific ionization thresholds, hundreds to thousands eV). Each region encodes different specimen properties.
- [O] left-to-right energy axis; intensity on vertical; single-line curve transitions through all three regions; the two core-loss edge steps are prominent features.
- [P] flat vector, Okabe-Ito: curve Black #000000; zero-loss peak fill Blue #0072B2; plasmon region fill Sky Blue #56B4E9; core-loss edges Bluish Green #009E73 step fills; baseline region white. No baked text.
- [E] exclude: energy-scale numbers, element identification labels, background-subtraction overlay, monochromator hardware, EFTEM description.

**NEGATIVE:** energy numbers, element labels, background-subtraction curves, hardware diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 13. tomography-tilt-series  — tilt → projections → back-projection → 3D volume  (MC · process flowchart · Important)
*Source: chapter 19 — "Tomography and Low-Dose Imaging"*

**PASTE:** Draw a blank four-stage horizontal process chain on a white background. Stage 1: a small 3D-implied box (specimen) with a beam arrow, tilted slightly — show three different tilt angles as overlaid rectangles at slightly different orientations. Stage 2: three projection silhouette strips side by side (each strip is a 2D rectangular projection image, representing one tilt). Stage 3: a circular "reconstruction" symbol with radiating lines inward representing back-projection. Stage 4: a 3D-implied cube or volume icon representing the reconstructed 3D model. Right-pointing arrows connect each stage. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] electron tomography workflow: specimen tilted to many angles → 2D projection image recorded at each tilt → projections combined by weighted back-projection algorithm → 3D density volume reconstructed.
- [O] four-stage left-to-right chain; connecting arrows; each stage a distinct visual icon.
- [P] flat vector, Okabe-Ito: specimen box Orange #E69F00, projection strips Sky Blue #56B4E9, back-projection disc Blue #0072B2 with radiating spokes, 3D volume Bluish Green #009E73, stage arrows Black #000000. No baked text.
- [E] exclude: tilt angle numbers, back-projection mathematics, sinogram representation, Radon transform, missing-wedge artifact depiction.

**NEGATIVE:** tilt angle numbers, sinogram, Radon transform formulas, missing-wedge, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 14. cryo-em-vitrification  — plunge into liquid ethane beats ice crystal formation  (MC · process flowchart · Critical)
*Source: chapter 21 — "Cryo-EM"*

**PASTE:** Draw a blank four-stage vitrification sequence on a white background. Stage 1: a small circle representing a droplet of aqueous sample on a TEM grid (holey carbon film shown as a flat strip with small holes). Stage 2: blotting paper shapes on either side of the grid, compressing the droplet to a thin film — shown as narrowing of the droplet between two flat rectangles. Stage 3: a downward plunge arrow into a small container (the liquid ethane bath — shown as a shallow cup below). Stage 4: the grid now embedded in a uniform light-blue layer (vitreous ice, amorphous), contrasted with a small crossed-out hexagonal ice crystal to the side. Right-pointing arrows and one downward arrow connect the stages. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] cryo-EM specimen preparation: apply sample to holey-carbon grid → blot to thin film → plunge rapidly into liquid ethane → vitreous (amorphous) ice forms instantly, trapping sample in near-native hydrated state. Key: fast cooling avoids crystalline ice formation.
- [O] four stages, left-to-right with one downward plunge arrow at stage 3; crossed-out hexagon icon marks the avoided crystalline-ice outcome.
- [P] flat vector, Okabe-Ito: grid neutral gray, droplet Blue #0072B2, blotting paper Yellow #F0E442, plunge arrow Black #000000, liquid-ethane cup Orange #E69F00, vitreous-ice layer Sky Blue #56B4E9 (semi-transparent), crossed-out crystal Vermillion #D55E00. No baked text.
- [E] exclude: cooling rate numbers, ethane temperature annotations, cryo-holder anatomy, vitrification window calculations, single-particle analysis workflow.

**NEGATIVE:** cooling rate numbers, temperature values, cryo-holder anatomy, SPA workflow boxes, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 15. sem-biological-prep-pipeline  — fix → dehydrate → CPD → mount → coat → image  (MC · process flowchart · Important)
*Source: chapter 08 — "SEM Sample Preparation"*

**PASTE:** Draw a blank six-stage linear process flowchart on a white background. Each stage is a small square icon connected by right-pointing arrows. Stage 1: a blob shape with internal crosslinks (chemical fixation). Stage 2: a series of six small containers in decreasing water-blue fill representing the graded ethanol series. Stage 3: a pressure vessel icon with CO2 label avoided — show only a sealed cylinder. Stage 4: a circular SEM stub icon with the specimen rectangle on top. Stage 5: a spray/sputter coating icon (a target disk with downward arrows). Stage 6: an electron beam arrow hitting a specimen (imaging). Six stages, five arrows, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] biological SEM specimen preparation: chemical fixation (glutaraldehyde + osmium) → graded ethanol dehydration → critical-point drying → mounting on stub → sputter coating (Pt/Au) → SEM imaging. Each stage solves one physical problem (crosslinking, water removal, surface-tension avoidance, conductivity).
- [O] left-to-right six-stage linear chain; each stage a distinct icon; arrows connect; no branching.
- [P] flat vector, Okabe-Ito: stage icons cycle through Orange #E69F00, Sky Blue #56B4E9, Blue #0072B2, Bluish Green #009E73, Reddish Purple #CC79A7, Yellow #F0E442. Arrows Black #000000. No baked text.
- [E] exclude: glutaraldehyde/osmium chemical formulas, ethanol percentages, CPD temperature/pressure values, coating thickness numbers, SEM parameter settings.

**NEGATIVE:** chemical formulas, percentage numbers, temperature values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 16. tem-biological-prep-pipeline  — fix → dehydrate → embed → section → stain → image  (MC · process flowchart · Important)
*Source: chapter 20 — "TEM Sample Preparation for Biological Materials"*

**PASTE:** Draw a blank six-stage linear process flowchart on a white background. Each stage is a small icon connected by right-pointing arrows. Stage 1: a tissue block with crosslink lines (fixation). Stage 2: a row of graded containers (dehydration). Stage 3: a rectangular mold block (resin infiltration and embedding). Stage 4: a diamond knife cross-section with a thin ribbon floating off it (ultramicrotomy). Stage 5: a TEM grid circle with a thin square section on it, with small droplet icons (staining). Stage 6: an electron beam entering a TEM column icon (imaging). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] biological TEM preparation: glutaraldehyde + osmium fixation → graded ethanol dehydration → resin infiltration and embedding → ultramicrotome sections (70 nm) → heavy-metal staining (uranyl/lead) → TEM imaging. Each stage builds on the previous.
- [O] left-to-right six-stage chain; each stage distinct; the ultramicrotome section is the critical thin-slice step.
- [P] flat vector, Okabe-Ito: icons cycle Orange #E69F00, Sky Blue #56B4E9, Blue #0072B2, Bluish Green #009E73, Reddish Purple #CC79A7, Yellow #F0E442. Arrows Black #000000. No baked text.
- [E] exclude: chemical names, section thickness numbers, staining times, osmium tetroxide toxicity annotation, cryo alternative path.

**NEGATIVE:** chemical names, thickness numbers, staining protocols, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 17. inorganic-tem-prep-four-stages  — bulk → disc → dimple → ion-mill → electron-transparent  (MC · process flowchart · Supplementary)
*Source: chapter 22 — "TEM Sample Preparation for Inorganic and Materials Science Specimens"*

**PASTE:** Draw a blank four-stage reduction diagram on a white background: four cross-section views of the same disc specimen at different stages of thinning. Stage 1: a thick flat rectangle (bulk disc, full thickness). Stage 2: the same disc but thinner with a slight concave dimple at the center (dimple grinding). Stage 3: the disc even thinner with the center showing a perforation — a small hole at the center (ion milling almost complete). Stage 4: the disc with a clear hole at center and a very thin annular region around the hole (electron-transparent area, shown in lighter fill). Right-pointing arrows connect the four stages. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] inorganic TEM specimen goes through mechanical thinning → dimple grinding → ion-milling to perforation → the annular region around the hole is electron-transparent (sub-100 nm). Five-orders-of-magnitude thickness reduction represented in four visual stages.
- [O] left-to-right four stages; cross-section view; the perforation/hole appears and grows; the thin annular region is the final imaging area.
- [P] flat vector, Okabe-Ito: bulk disc neutral gray, dimple darker Blue #0072B2 fill, ion-milled region Sky Blue #56B4E9, electron-transparent region Bluish Green #009E73 very light fill, perforation hole white with outline. Arrows Black #000000. No baked text.
- [E] exclude: thickness numbers, milling-rate values, argon-ion beam angle, FIB alternative path, electropolishing variant.

**NEGATIVE:** thickness numbers, milling rates, argon angle, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 18. fib-sem-dual-beam-geometry  — ion column + electron column at 52° meet at the eucentric point  (VG · structural schematic · Important)
*Source: chapter 10 — "Advanced SEM: FIB-SEM, Dual Beam Systems, and Variable Pressure SEM"*

**PASTE:** Draw a blank dual-beam FIB-SEM geometry diagram on a white background: a horizontal specimen surface (flat rectangle). Above and to the left, a vertical electron-column tube pointing straight down to the specimen. Above and to the right, an angled ion-column tube pointing at the same spot on the specimen from a 52° angle relative to the specimen normal. Show a single dot at the intersection point on the specimen surface (the eucentric coincidence point). Draw a small arc at the specimen to indicate the 52° angle between the two beams. Beam arrows travel from each column to the specimen dot. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] dual-beam FIB-SEM: electron column is vertical (SEM mode, imaging); ion column is angled at 52° from specimen normal (FIB mode, milling); both beams converge at the same eucentric point on the specimen; simultaneous mill-and-image is possible from this geometry.
- [O] two column tubes converging to one point on the specimen; 52° angle arc at the convergence; specimen surface horizontal.
- [P] flat vector, Okabe-Ito: electron column Blue #0072B2, e-beam arrow Black #000000, ion column Orange #E69F00, ion-beam arrow Vermillion #D55E00, specimen surface neutral gray, eucentric point dot Black #000000, angle arc Sky Blue #56B4E9. No baked text.
- [E] exclude: gas injection needles, micromanipulator arm, platinum deposition nozzle, chamber anatomy, FIB milling steps.

**NEGATIVE:** gas injection hardware, micromanipulator, platinum nozzle, chamber interior, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 19. artifact-recognition-comparison  — charging, contamination, astigmatism, beam damage: four bad images  (VG · comparison panels · Critical)
*Source: chapter 23 — "Artifact Recognition"*

**PASTE:** Draw a blank four-panel grid on a white background (2×2 arrangement). Each panel is a square frame containing a minimal schematic representing one artifact morphology. Panel A: streaky bright regions and dark patches (charging artifact — irregular bright patches and dark spots). Panel B: a growing dark deposit accumulating around the scan field edge (contamination — dark frame-within-frame). Panel C: oval-stretched blurred central object instead of a round one (astigmatism — an ellipse where a circle should be). Panel D: a specimen outline with the center appearing degraded/mottled compared to the edges (beam damage — central brightening and structural degradation). No text, no labels.
- [S] double-column 178mm, 300 DPI, vector, white bg, square (2×2).
- [C] four common SEM/TEM artifacts with distinct visual signatures: charging (bright/dark patches and streaks), contamination (carbon deposit ring), astigmatism (directional blur / elongated features), beam damage (dose-dependent structural degradation).
- [O] 2×2 grid; each cell one artifact type; visual signature must be iconic and distinct for diagnosis.
- [P] flat vector, Okabe-Ito: charging panel Orange #E69F00 patches, contamination panel Blue #0072B2 frame ring, astigmatism panel Reddish Purple #CC79A7 ellipse, beam-damage panel Vermillion #D55E00 mottled center. Panel borders neutral gray. No baked text.
- [E] exclude: FIB-specific artifacts (curtaining, redeposition), EDS peak artifacts, VP-SEM skirt artifacts, numerical diagnoses, remediation steps.

**NEGATIVE:** FIB curtaining, redeposition, EDS artifacts, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## 20. multimodal-technique-selection  — characterization question maps to one technique's physics  (VG · conceptual map · Important)
*Source: chapter 24 — "Choosing the Right Technique" and chapter 25 — "Applications"*

**PASTE:** Draw a blank radial conceptual map on a white background: a central circle representing the specimen. Radiating from it, six equal-length arms ending in rounded icon boxes (not text) — representing six characterization goals. Top: a size-distribution bar-chart icon (population statistics → SEM). Upper-right: a cross-section of concentric rings (internal structure → TEM). Right: a 3D cube icon (3D reconstruction → tomography). Lower-right: a spectrum-peak icon (elemental composition → EDS/EELS). Bottom: a grid of spots (crystal phase → diffraction). Upper-left: an atomic-column dot icon (atomic resolution → HAADF-STEM). Six arms, six goal icons, one central specimen circle. No text.
- [S] double-column 178mm, 300 DPI, vector, white bg, square.
- [C] the technique-selection logic: each characterization question (population, internal structure, 3D, elemental, crystal, atomic) maps to one technique whose physics uniquely enables it. No technique answers all questions; together they close the argument.
- [O] radial from center; six arms at even angular spacing; central circle = specimen; outer icon = technique/goal proxy.
- [P] flat vector, Okabe-Ito: central circle Black #000000 filled, arms neutral gray, icons cycling Orange #E69F00, Sky Blue #56B4E9, Blue #0072B2, Bluish Green #009E73, Reddish Purple #CC79A7, Yellow #F0E442. No baked text.
- [E] exclude: technique name text, table reproduction, cost/time annotations, specific instrument brands, numerical resolution limits.

**NEGATIVE:** technique name text, cost or time data, brand names, resolution numbers, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, watermarks, red-green color combinations, 3D perspective distortion

---

## Zero-candidate chapters

- **ch01 — Introduction to EM**: contextual history/motivation chapter; concepts introduced conceptually before any diagrammable mechanism is defined. Figures here would duplicate ch02 (resolution limit).
- **ch05 — SEM Modes of Operation**: the core diagrammable content (interaction volume vs kV, probe-size/current trade) is fully covered by candidate 3 (interaction-volume-teardrop). Remaining content is parameter tables and operational decisions unsuitable for CAJAL flat-vector figures.
- **ch11 — Designing SEM Experiments**: synthesis/case-study chapter; no novel mechanisms to diagram. Concepts are combinations of prior-chapter physics already covered by candidates 3, 4, and 15.
- **ch26 — Designing, Reporting, Critiquing**: methods and documentation chapter; content is procedural guidance rather than visual mechanisms. No CAJAL candidates.
- **app-a — Lab Practice and Safety**: safety protocols; no mechanism figures.
- **app-b — TEM Supplies, Grids, Supports**: materials reference; tabular, not diagrammatic.

---

## Video candidates

FIGURE abbe-resolution-limit — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE gun-type-comparison — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE interaction-volume-teardrop — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE sem-detector-geometry — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE eds-xray-generation — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE cpd-phase-diagram — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE tem-column-schematic — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE tem-bf-df-aperture — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE diffraction-three-patterns — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE tem-contrast-mechanisms — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE stem-detector-zones — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE eels-spectrum-regions — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE tomography-tilt-series — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE cryo-em-vitrification — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE sem-biological-prep-pipeline — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE tem-biological-prep-pipeline — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE inorganic-tem-prep-four-stages — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE fib-sem-dual-beam-geometry — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE artifact-recognition-comparison — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE multimodal-technique-selection — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** **cryo-em-vitrification** — highest-priority candidate (criterion 2); if produced, **tomography-tilt-series**, **sem-biological-prep-pipeline**, **tem-biological-prep-pipeline**, **inorganic-tem-prep-four-stages** could fold in as supporting beats rather than separate videos.
