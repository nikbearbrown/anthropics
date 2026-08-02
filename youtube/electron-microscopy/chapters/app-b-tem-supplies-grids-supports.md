# Appendix B — TEM Supplies, Grids, Supports, Stains, and Holders

> **Reference appendix.** Use as the comprehensive consumables guide for TEM work. Cross-referenced from Chapters 20 (biological prep) and 22 (inorganic prep).

## B.1 Why this appendix exists

A working TEM lab uses dozens of consumables: grids in many sizes and materials, support films of various types, stains and fixatives, tweezers, grid boxes, holders, storage. The choice among them is not arbitrary — each consumable affects image quality, contamination resistance, charging behavior, contrast, or specimen stability.

This appendix is the working reference for those choices, organized to support both biological (Ch. 20) and inorganic (Ch. 22) workflows.

---

## B.2 TEM grids: materials and mesh

A TEM grid is a 3 mm diameter disc with a regular pattern of holes that supports the specimen while allowing electron transmission. The standard parameters:

| Material | Z | Notes |
|---|---|---|
| Copper (Cu) | 29 | most common; magnetic-immune; cheap |
| Nickel (Ni) | 28 | for samples that interact poorly with Cu |
| Gold (Au) | 79 | corrosion-resistant; for biological work |
| Molybdenum (Mo) | 42 | high-temperature stable; for high-T in-situ |
| Aluminum (Al) | 13 | rare; for low-Z imaging |
| Titanium (Ti) | 22 | for biological and chemical compatibility |

Mesh size = number of squares per inch (1 inch = 25.4 mm):

| Mesh | Squares per side | Open area % | Use |
|---|---|---|---|
| 100 | 100 | ~70% | very large open area; coarse specimens |
| 150 | 150 | ~65% | coarse specimens |
| 200 | 200 | ~55-60% | standard for routine work |
| 300 | 300 | ~50-55% | standard for biological work |
| 400 | 400 | ~45-50% | finer mesh; smaller specimens |
| 600 | 600 | ~35-40% | fine mesh; smaller specimens |
| 1000 | 1000 | ~20-30% | very fine mesh; small specimens |

Smaller mesh = more support but smaller imaging area per square.

---

## B.3 Support films

Most TEM specimens cannot rest directly on the grid; they need a support film across the grid holes. Common supports:

**Continuous carbon film.** A uniform amorphous carbon film (typically 5-30 nm thick) deposited across the grid. Provides full coverage; sometimes thicker than ideal for HRTEM.

**Holey carbon film.** Carbon film with regular holes (typically 1-5 μm in diameter). Specimens can sit either over the carbon (if using carbon as support) or over the holes (for cryo-TEM single-particle work where vitreous ice fills the hole).

**Lacey carbon film.** Carbon film with irregular holes (the "lacey" pattern). Open area per cm² ranges from ~50% (most lacey) to ~30% (less open). Used for nanoparticles where multiple particles per field of view are wanted.

**Formvar film.** Polymer support film (polyvinyl formal). Thinner than carbon (~5 nm typical). More fragile but allows imaging of specimens placed directly on the film.

**Lacey + carbon hybrid.** A lacey carbon film with a continuous thin carbon (e.g., a few nm of additional carbon) for additional support of nanoparticles.

**Quick reference for support choice:**

| Specimen | Support |
|---|---|
| Particles in suspension (small) | continuous carbon or formvar |
| Particles in suspension (medium) | lacey carbon or holey carbon |
| Cryo-EM single-particle | holey carbon (e.g., Quantifoil R 1.2/1.3 [verify]) |
| Cryo-EM tomography | lacey or holey |
| Sectioned biological | none (sections sit directly on grid) |
| FIB lamella | special grids with notch cutouts |
| Nanoparticles in suspension | lacey carbon |
| Powders | lacey or holey carbon |

[verify all]

---

## B.4 Glow discharge

Carbon support films are hydrophobic; aqueous specimens applied directly bead up rather than spreading. **Glow discharge** treatment hydrophilizes the surface:

- Brief exposure (5-30 seconds) to a low-pressure plasma (often air or H₂/O₂).
- Result: negative charge accumulates on the surface; aqueous solutions wet evenly.
- Optional: positive-charge plasma treatment (e.g., amino-functional silane) for selective adsorption.

Standard equipment: a small glow-discharge instrument (Pelco easiGlow or similar [verify]) that handles 12-24 grids at a time.

Glow discharge is a common bottleneck in EM workflows; treatments expire after hours-to-days, so grids are typically glow-discharged immediately before specimen application.

---

## B.5 Tweezers

Grid handling requires precision tweezers:

| Type | Use |
|---|---|
| Self-closing tweezers (PELCO Pro) | hands-free grid holding during transfer |
| Reverse-action tweezers | open-by-default; close on press |
| Standard fine-tip tweezers | direct grid pickup |
| Anti-magnetic tweezers | for magnetic specimens or near magnetic detectors |

Practice grid handling with sacrificial grids before committing to expensive specimens. A dropped grid is unrecoverable; a flipped grid can be re-flipped with care.

---

## B.6 Stains and fixatives

For biological TEM (Ch. 20):

| Reagent | Typical concentration | Purpose |
|---|---|---|
| Glutaraldehyde | 2.0-2.5% in buffer | primary fixation; protein crosslinking |
| Paraformaldehyde | 2-4% in buffer | secondary fixation; faster penetration |
| Osmium tetroxide (OsO₄) | 1-2% in buffer | post-fixation; lipid stabilization; contrast |
| Uranyl acetate | 1-2% (negative); 2% (positive) | TEM staining |
| Lead citrate | 0.04% (CO₂-free water) | post-staining contrast |
| Phosphotungstic acid (PTA) | 1-2% | negative staining (alternative to UA) |
| Cacodylate buffer | 0.1 M, pH 7.2-7.4 | fixation buffer (toxic; cross-ref App A) |
| Phosphate buffer | 0.1 M, pH 7.2-7.4 | fixation buffer (less toxic) |
| HMDS | pure | drying alternative to CPD |
| Tannic acid | 0.5-1% | en-bloc enhancement of contrast |

For inorganic TEM (Ch. 22), most specimens do not require stains; the heavy elements provide contrast directly. Exceptions:

- **Ion-mill cleanup pass** at low kV to reduce amorphization.
- **Carbon coating** on insulating samples for charge dissipation.
- **Pt deposition** in FIB protective layers.

---

## B.7 Grid storage and handling

After preparation, grids must be stored protected from contamination:

| Storage | Use |
|---|---|
| Grid boxes (3-100 slots) | routine storage |
| Cryo-grid boxes (LN₂-storage) | cryo-EM grids at LN₂ |
| Diamond-cut wooden boxes | high-quality storage of master grids |
| Single-use individual cassettes | shipping or special-handling |

**Best practice:**
- Label grid boxes with date, specimen, and operator.
- Store at room temperature in a desiccator if possible.
- Cryo grids: never warm above the vitrification limit (~−140 °C).
- Avoid magnetic environments for ferritic-steel-grid storage.
- Document grid usage in a lab log.

---

## B.8 Specimen holders

Standard TEM holders:

| Holder type | Use |
|---|---|
| Single-tilt holder | routine imaging; up to ±60° tilt |
| Double-tilt holder | orientation-dependent imaging; ±60°/±60° |
| Cryo holder (LN₂) | cryo-EM, cryo-tomography |
| High-tilt holder (±70-75°) | tomography |
| Heating holder | in-situ heating up to ~1500 °C [verify] |
| Cooling holder (LN₂) | LN₂-cold imaging |
| Cryo-helium holder | He-cold imaging (~4 K) |
| Straining holder | mechanical loading in-situ |
| FIB lift-out grid | for FIB-prepared lamellae |

Holders are instrument-specific; not interchangeable between manufacturers without adapters.

---

## B.9 Vacuum-compatible material handling

A general rule: nothing goes into the TEM column that hasn't been clean-handled:

| Material | Handling |
|---|---|
| Grids | gloved hands; designated tweezers |
| Stainless tools | clean before use; isopropanol rinse if needed |
| Tweezers | wipe clean; isolated storage |
| Resins | plasma-cleaned grids only |
| Solvents | filtered; volatile-free |

Surface contamination on the holder, the grid, or the specimen produces hydrocarbon contamination during imaging — recognized as dark squares developing where the beam imaged at high kV (Ch. 5). Mitigation includes plasma cleaning before insertion.

---

## B.10 Quick-reference: grid + support + treatment for common specimens

For common specimens, the standard combination:

| Specimen | Grid | Support | Treatment |
|---|---|---|---|
| Routine bacteria (negative stain) | 200-300 mesh Cu | continuous carbon | glow discharge |
| Routine sectioned biology | 200-mesh Cu or Au | continuous carbon | none beyond glow |
| Cryo-EM single-particle work | 200 or 300 mesh Cu | holey carbon (R 1.2/1.3) | glow discharge |
| Cryo-EM membrane proteins | 300 mesh Au | holey carbon + thin carbon | glow discharge |
| Nanoparticles in suspension | 200 mesh Cu | lacey carbon | direct deposit, dry |
| Powdered solid materials | 100-200 mesh Cu | lacey or holey carbon | direct |
| Polished metal disc + ion mill | none (discs themselves) | n/a | n/a |
| FIB lamella | Cu Omniprobe grid | none | FIB welding |

[verify all]

---

## B.11 Disposal of TEM consumables

| Item | Disposal |
|---|---|
| Used Cu grids (no biohazard) | regular waste |
| Cu grids with biological specimens | hazardous waste (biological) |
| Au or Mo grids | metal recycling |
| OsO₄-stained grids | hazardous waste (chemical) |
| Uranyl-acetate-stained grids | hazardous waste (radioactive) |
| Used carbon paint | regular waste (after solvent evaporation) |
| Polishing slurries | hazardous waste; specific by chemistry |
| Cryogenic dewars | return for recycling |

---

## B.12 Where to source consumables

Common suppliers (selection; not exhaustive [verify]):

| Supplier | Typical products |
|---|---|
| Ted Pella | grids, support films, knives, tweezers, stains |
| Electron Microscopy Sciences | grids, fixatives, stains, resins, support films |
| Quantifoil | holey carbon grids, R 1.2/1.3 specifically |
| Bal-Tec / EMS / Leica | cryo prep equipment, microtomes |
| Gatan | cameras, holders |
| EMS / Pelco | tweezers, grid boxes |
| Diatome | diamond knives |

Suppliers vary by region and institution; the lab manager will have the standard suppliers list.

---

## B.13 Summary

This appendix is the working reference for TEM consumables. The key disciplines:

1. **Match grid material and mesh to specimen type and question.**
2. **Choose support film by what the specimen needs (continuous, holey, lacey).**
3. **Glow-discharge before applying aqueous specimens.**
4. **Use precision tweezers and document grid handling.**
5. **Match stain choice to imaging mode (BF, DF, HRTEM, etc.).**
6. **Store grids appropriately by specimen type.**
7. **Choose holder by imaging requirements (tilt range, temperature).**
8. **Handle clean and document.**

The discipline is comprehensive. The goal: routine TEM specimen preparation that produces good science with minimal contamination and consistent results.

---

**What would change my mind:** the practical experience of a working TEM lab where specific consumables are chosen with material-by-material rationale; this appendix is general guidance, but specific patterns require local tailoring.

**Tags:** `TEM-consumables`, `grids`, `support-films`, `stains`, `holders`, `reference`

---

### Note to the professor

This appendix is reference material drawn from week-12 (biological prep, stains), week-13 (inorganic prep, grids), and standard TEM-supply reference content. Specific manufacturers and brand names ([verify] markers throughout) should be checked against current Northeastern lab procurement and TEM equipment specifications.

`[verify]` markers are extensive throughout because consumable specifications vary across institutions and over time.

Length ~2,400 words. Within the 2,000-4,000 word emma appendix range.

Voice anchoring: anchored, but appendix-style: section-and-table-heavy rather than narrative. Cross-references to Chapters 20 and 22 are explicit per book.md authoring rules.

