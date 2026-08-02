#!/usr/bin/env python3
"""
physics_de_broglie_wavelength_scale.py — de Broglie Wavelength: 35-Decade Span
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    λ = h/p = h/(mv) for non-relativistic
    λ_electron(100 eV) = h/sqrt(2 m_e eV)
    λ_bowling = h/(m v)

Render:
    cd physics/youtube/physics-de-broglie-wavelength-scale
    manim -qh physics_de_broglie_wavelength_scale.py deBroglieScene
"""
import sys
import numpy as np

H    = 6.626e-34   # J·s
ME   = 9.11e-31    # kg electron mass
E_EV = 1.6e-19     # J per eV


def lambda_electron_eV(eV):
    KE = eV * E_EV
    p  = np.sqrt(2 * ME * KE)
    return H / p


def lambda_classical(mass_kg, speed_ms):
    return H / (mass_kg * speed_ms)


def verify():
    print("=== de Broglie Wavelength verification ===")
    lam100 = lambda_electron_eV(100)
    print(f"  Electron at 100 eV: λ = {lam100:.4e} m = {lam100*1e10:.4f} Å")
    lam54 = lambda_electron_eV(54)
    print(f"  Electron at 54 eV (Davisson-Germer): λ = {lam54:.4e} m = {lam54*1e10:.4f} Å")
    print(f"  Ni lattice spacing ≈ 2.15 Å  (ratio λ/d = {lam54*1e10/2.15:.3f})")
    # P1: λ at 54 eV → 1.67 Å
    assert abs(lam54*1e10 - 1.67) < 0.02, f"P1: {lam54*1e10}"
    # Bowling ball
    lam_bowl = lambda_classical(3.0, 10.0)
    print(f"  Bowling ball (3 kg, 10 m/s): λ = {lam_bowl:.4e} m")
    # P2: ratio
    ratio = lam_bowl / lambda_electron_eV(100)
    print(f"  Ratio λ_bowl / λ_e(100eV) = {ratio:.4e}  (≈ 5.6e-25)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class deBroglieScene(Scene):
    """Log-scale axis: marker slides from electron to bowling ball."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._logscale_axis()

    def _title(self):
        t1 = Text("de Broglie Wavelength", font="EB Garamond", font_size=58, color=INK)
        t2 = Text("35 orders of magnitude — why bowling balls don't diffract",
                  font="EB Garamond", font_size=23, color=DIM)
        t3 = MathTex(r"\lambda = \frac{h}{p} = \frac{h}{mv}", color=BLUE, font_size=38)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _logscale_axis(self):
        # Log10(λ) axis from -35 to 0
        ax = NumberLine(
            x_range=[-35, 1, 5],
            length=12,
            color=INK,
            include_tip=True,
            tip_length=0.2,
        ).shift(DOWN*0.5)
        self.play(Create(ax), run_time=1.0)
        lx = Text("log₁₀(λ / m)", font="EB Garamond", font_size=22, color=INK).next_to(ax, DOWN, buff=0.35)
        self.play(Write(lx), run_time=0.4)

        # Reference lines
        refs = [
            (-10, "atomic spacing (0.1 nm)", BLUE),
            (-7,  "visible light (100–700 nm)", GOLD),
        ]
        for log_val, label, col in refs:
            d = DashedLine(ax.n2p(log_val)+DOWN*0.4, ax.n2p(log_val)+UP*0.4,
                           color=col, stroke_width=1.5, dash_length=0.12)
            lbl = Text(label, font="EB Garamond", font_size=15, color=col)
            lbl.next_to(ax.n2p(log_val), UP, buff=0.5)
            self.play(Create(d), Write(lbl), run_time=0.5)

        # Objects
        objects = [
            ("Electron\n100 eV", lambda_electron_eV(100), BLUE),
            ("Electron\n54 eV (Davisson-Germer)", lambda_electron_eV(54), BLUE),
            ("Proton\n100 eV", H/np.sqrt(2*1.67e-27*100*E_EV), BROWN),
            ("Protein\n70 kDa, 10 m/s", lambda_classical(70e3/6.022e23, 10), DIM),
            ("Human\n70 kg, 1.5 m/s", lambda_classical(70, 1.5), DIM),
            ("Bowling\nball 3 kg, 10 m/s", lambda_classical(3.0, 10.0), BROWN),
        ]

        dots_lbls = []
        for name, lam, col in objects:
            log_lam = np.log10(lam)
            pos = ax.n2p(log_lam)
            d = Dot(pos, color=col, radius=0.12)
            lbl = Text(name, font="EB Garamond", font_size=14, color=col)
            lbl.next_to(d, UP, buff=0.35)
            self.play(FadeIn(d), Write(lbl), run_time=0.7)
            dots_lbls.append((d, lbl))

        # Key annotation
        ann = Text(
            "Electron λ ≈ atomic spacing → diffraction possible\nBowling ball λ → 20 decades smaller than any aperture",
            font="EB Garamond", font_size=19, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(ann), run_time=1.0)
        self.wait(3.0)
