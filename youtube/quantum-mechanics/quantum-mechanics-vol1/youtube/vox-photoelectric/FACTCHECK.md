# FACTCHECK — vox-photoelectric

## Beat-by-beat verification

**B01** — "A million-watt red spotlight releases zero electrons. A pocket UV penlight releases them instantly."
- VERIFIED. This is the classic framing of the photoelectric effect. Source: chapter 01.

**B02** — "Three facts: threshold frequency; no time delay; KE depends only on frequency."
- VERIFIED. Millikan (1914-1916) established all three. Source: chapter 01, §Photoelectric Effect.

**B04** — "Einstein 1905: light in discrete photon packets, each carrying hν."
- VERIFIED. Einstein, Annalen der Physik 17, 132 (1905). Source: chapter 01.

**B05** — "KE = hν − Φ; below threshold: negative KE, no escape."
- VERIFIED. Standard Einstein photoelectric equation. Source: chapter 01, eq. displayed.

**B06** — "Sodium: Φ = 2.28 eV; green 546 nm = 2.27 eV → zero electrons from 10,000-W lamp; UV 300 nm = 4.13 eV → ejection."
- VERIFIED. Source: chapter 01 worked example. E = 1240/546 ≈ 2.27 eV; 1240/300 ≈ 4.13 eV. Φ(Na) = 2.28 eV (NIST).

**B07** — "Photons cannot pool their energy."
- VERIFIED. This is the essential non-classical property: one photon acts on one electron independently. Source: chapter 01.

**B08** — "Intensity = count per second; frequency = energy per photon. Independent."
- VERIFIED. Standard interpretation. Source: chapter 01.

**B09** — "Millikan confirmed Einstein's equation despite personal disbelief; Einstein Nobel 1921 for photoelectric effect."
- VERIFIED. Millikan, Phys. Rev. 7, 355 (1916): "obtained in spite of my personal conviction." Nobel Prize facts: Einstein 1921, Millikan 1923. Source: chapter 01.

## Exclusions confirmed
- No stopping-potential algebra (V_stop = KE/e not derived)
- No Einstein-equation derivation
- No Compton scattering
- No extended Millikan biography

## VERDICT: PASS

---

## Doodle-pass addendum (2026-07-25)

**B02 doodle beat** — title: "three facts classical waves cannot explain"; caption:
"threshold · instant · frequency sets energy". No new factual claims introduced;
both strings are accurate summaries of the verified beat content. PASS.

**B05 doodle beat** — DoodleChart line: KE = hν − Φ_Na. Computed from
h = 4.136×10⁻¹⁵ eV·s, Φ_Na = 2.28 eV (NIST). Data in data/B05-ke-vs-nu.csv;
matplotlib truth plot at data/B05-reference.png. Frame verified: hockey-stick line,
threshold accented (ν₀ = 5.51×10¹⁴ Hz), caption "KE = h·ν − Φ · slope = h". PASS.

**B06 doodle beat** — DoodleChart bar: E_green = 1240/546 = 2.27 eV,
Φ_Na = 2.28 eV, E_UV = 1240/300 = 4.13 eV. Data in data/B06-sodium-bars.csv;
matplotlib truth plot at data/B06-reference.png. Frame verified: three bars,
UV bar accented red (tallest at 4.13 eV), caption "Φ = 2.28 eV · UV ejects electrons,
green cannot". All values match FACTCHECK.md §B06. PASS.

**B07 doodle beat** — DoodleScene: sparkle cluster (many red photons, left),
medical cross accent (cannot pool, below), circle (1 UV photon, right). Caption:
"photons cannot pool their energy". No new factual claims; visual is correct analogy.
Frame verified. PASS.

**B08 doodle beat** — DoodleScene: arrow (intensity = count, left),
lightning bolt accent (frequency = energy, right). Caption:
"intensity sets count · frequency sets energy". Accurate summary of beat content.
Frame verified. GATE T PASS (arrow + bolt are simple geometric paths, no hachure-blob
false positives). PASS.

**B04** — stays Manim (electron icon missing from library → SHOPPING.md card).

**B09** — stays Manim per doodle style.md (3 categorical series). No change.

## Doodle-pass VERDICT: PASS (all rendered beats verified)
