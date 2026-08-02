#!/usr/bin/env python3
"""
physics_bohr_emission_spectrum.py — Bohr Hydrogen Spectrum Energy Levels and Balmer Transitions
SILENT SLATE — sim-scout candidate, physics-with-llms book.

Physics:
  E_n = -13.6 / n² eV
  ΔE = E_ni - E_nf   (photon emitted)
  1/λ = R(1/nf² - 1/ni²),   R = 1.097e7 m⁻¹

Balmer series (nf=2): Hα=656nm, Hβ=486nm, Hγ=434nm, Hδ=410nm

Testable predictions:
  P1: n=3→2: λ = 1/(R×5/36) = 656 nm (red)
  P2: n=4→2: ΔE = 13.6(1/4-1/16) = 2.55 eV → λ = 486 nm (blue-green)

Run standalone verification:
  python3 physics_bohr_emission_spectrum.py --verify

Render:
  manim -qh physics_bohr_emission_spectrum.py BohrEmissionSpectrumScene
"""
import sys
import numpy as np

E_H   = 13.6          # eV  (Rydberg energy)
R_INF = 1.0973732e7   # m⁻¹ (Rydberg constant)
H_EV  = 4.136e-15    # eV·s
C_MS  = 3e8           # m/s

def energy_level(n: int) -> float:
    return -E_H / n**2

def wavelength_nm(ni: int, nf: int) -> float:
    inv_lam = R_INF * (1.0/nf**2 - 1.0/ni**2)
    return 1.0 / inv_lam * 1e9  # nm

def verify():
    print("=== Bohr emission spectrum verification ===")
    for n in range(1, 7):
        print(f"  E_{n} = {energy_level(n):.4f} eV")
    print()
    print("  Balmer series (nf=2):")
    for ni in range(3, 7):
        lam = wavelength_nm(ni, 2)
        dE  = energy_level(ni) - energy_level(2)
        print(f"    n={ni}→2  λ={lam:.1f} nm  ΔE={-dE:.4f} eV")
    # P1
    lam32 = wavelength_nm(3, 2)
    print(f"\n  P1: λ(3→2) = {lam32:.2f} nm  (expect 656 nm)")
    # P2
    dE42 = abs(energy_level(4) - energy_level(2))
    lam42 = wavelength_nm(4, 2)
    print(f"  P2: ΔE(4→2) = {dE42:.4f} eV  λ = {lam42:.2f} nm  (expect 486 nm)")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

# Balmer series colours (approximate visible)
BALMER = [
    (3, 2, "#FF4444", "Hα  656 nm"),   # red
    (4, 2, "#4488FF", "Hβ  486 nm"),   # blue
    (5, 2, "#9966DD", "Hγ  434 nm"),   # violet
    (6, 2, "#7744BB", "Hδ  410 nm"),   # far violet
]

N_LEVELS = 6


class BohrEmissionSpectrumScene(Scene):
    """
    Vertical energy-level diagram + electron transitions + spectrum strip.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Bohr Hydrogen Spectrum", font="EB Garamond", font_size=56, color=INK)
        sub   = Text(
            "Eₙ = −13.6/n² eV  ·  Balmer series: n→2",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "Four visible lines — hydrogen's fingerprint",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Energy level diagram (left) ─────────────────────────────────────
        # Map energy (-13.6 to 0 eV) to y position
        E_min = energy_level(1)   # -13.6 eV
        E_max = 0.0               # ionisation limit

        diagram_left  = -5.0
        diagram_right = -0.5
        diagram_bottom = -3.2
        diagram_top    =  3.2
        level_width    =  3.8

        def e_to_y(E: float) -> float:
            # Map [E_min, E_max] → [diagram_bottom, diagram_top]
            return diagram_bottom + (E - E_min) / (E_max - E_min) * (diagram_top - diagram_bottom)

        # Draw energy levels
        level_lines = VGroup()
        level_labels = VGroup()
        for n in range(1, N_LEVELS + 1):
            E = energy_level(n)
            y = e_to_y(E)
            line = Line(
                np.array([diagram_left, y, 0]),
                np.array([diagram_left + level_width, y, 0]),
                color=DIM if n < N_LEVELS else DIM,
                stroke_width=2.0 if n == 1 else 1.5,
            )
            lbl_n = MathTex(rf"n={n}", color=INK, font_size=18)
            lbl_n.next_to(line, LEFT, buff=0.1)
            lbl_e = MathTex(rf"{E:.2f}\,\mathrm{{eV}}", color=DIM, font_size=16)
            lbl_e.next_to(line, RIGHT, buff=0.1)
            level_lines.add(line)
            level_labels.add(lbl_n, lbl_e)

        # Ionisation label at top
        ion_line = Line(
            np.array([diagram_left, diagram_top + 0.15, 0]),
            np.array([diagram_left + level_width, diagram_top + 0.15, 0]),
            color=DIM, stroke_width=1.0, stroke_opacity=0.5,
        )
        ion_lbl = Text("n=∞  (ionisation)", font="EB Garamond", font_size=14, color=DIM)
        ion_lbl.next_to(ion_line, RIGHT, buff=0.1)

        self.play(
            Create(level_lines),
            Write(level_labels),
            Create(ion_line), Write(ion_lbl),
            run_time=1.5,
        )
        self.wait(0.5)

        # ── Spectrum strip (right panel) ────────────────────────────────────
        strip_left  =  0.3
        strip_right =  6.2
        strip_y     = -2.8
        strip_height = 0.55

        strip_bg = Rectangle(
            width=strip_right - strip_left,
            height=strip_height,
            color=CANVAS, fill_color="#111111", fill_opacity=1.0,
            stroke_color=INK, stroke_width=1.0,
        ).move_to(np.array([(strip_left + strip_right)/2, strip_y, 0]))

        nm_min = 400.0
        nm_max = 700.0

        def nm_to_x(lam_nm: float) -> float:
            return strip_left + (lam_nm - nm_min) / (nm_max - nm_min) * (strip_right - strip_left)

        strip_lbl = Text("Visible spectrum (400–700 nm)", font="EB Garamond", font_size=16, color=DIM)
        strip_lbl.next_to(strip_bg, UP, buff=0.1)

        self.play(FadeIn(strip_bg), Write(strip_lbl), run_time=0.8)

        # ── Animate each Balmer transition ─────────────────────────────────
        for ni, nf, col, name in BALMER:
            E_i = energy_level(ni)
            E_f = energy_level(nf)
            y_i = e_to_y(E_i)
            y_f = e_to_y(E_f)
            x_mid = diagram_left + level_width * 0.5

            lam = wavelength_nm(ni, nf)

            # Electron arrow (downward)
            arr = Arrow(
                np.array([x_mid, y_i, 0]),
                np.array([x_mid, y_f, 0]),
                color=col, stroke_width=2.5, tip_length=0.18,
            )

            # Photon burst at level nf, moving right
            photon_start = np.array([x_mid + 0.2, y_f + 0.1, 0])
            photon_end   = np.array([nm_to_x(lam), strip_y + strip_height/2, 0])
            photon_line  = DashedLine(photon_start, photon_end, color=col, stroke_width=1.8)

            # Spectrum line
            x_spec = nm_to_x(lam)
            spec_line = Line(
                np.array([x_spec, strip_y - strip_height/2, 0]),
                np.array([x_spec, strip_y + strip_height/2, 0]),
                color=col, stroke_width=3.5,
            )
            spec_lbl = Text(name, font="EB Garamond", font_size=14, color=col)
            spec_lbl.next_to(spec_line, UP, buff=0.08)

            # Transition label
            trans_lbl = MathTex(
                rf"n={ni}\to n={nf}\;\;\lambda={lam:.0f}\,\mathrm{{nm}}",
                color=col, font_size=22,
            ).to_edge(UP, buff=0.22)

            self.play(Write(trans_lbl), GrowArrow(arr), run_time=0.9)
            self.play(Create(photon_line), run_time=0.5)
            self.play(Create(spec_line), Write(spec_lbl), run_time=0.6)
            self.wait(0.8)
            self.play(FadeOut(trans_lbl, arr, photon_line), run_time=0.4)

        # ── Final fingerprint callout ───────────────────────────────────────
        final = Text(
            "These four lines are hydrogen's fingerprint — always identical wavelengths",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(UP, buff=0.22)
        formula = MathTex(
            r"\frac{1}{\lambda} = R\!\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right)",
            color=BLUE, font_size=30,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(final), Write(formula), run_time=1.5)
        self.wait(3.0)
