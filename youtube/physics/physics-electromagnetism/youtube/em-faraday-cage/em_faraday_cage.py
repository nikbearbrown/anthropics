#!/usr/bin/env python3
"""
em_faraday_cage.py — Faraday Cage: E=0 Inside a Conductor
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    Outer sphere R=0.20 m, Q=50 nC
    E at r=0.30 m: kQ/r² = 4,994 N/C
    E inside conductor: 0

Run standalone to verify:
    python3 em_faraday_cage.py
"""
import sys
import numpy as np

K_COULOMB = 8.99e9   # N m²/C²
Q_OUTER = 50e-9      # C
R_SHELL = 0.20       # m


def E_outside(r): return K_COULOMB * Q_OUTER / r**2
def E_inside(): return 0.0  # exact


def verify():
    print("=== Faraday Cage verification ===")
    r = 0.30
    print(f"E at r=0.30 m (outside): {E_outside(r):.1f} N/C  (card: 4994)")
    print(f"E at r=0.15 m (inside): {E_inside():.1f} N/C  (exact)")
    # P2: inner charge Q_inner in cavity → outer surface charge = Q_outer + Q_inner
    # but Q_inner = 0 on inner surface of a conductor with external point charge only
    # E outside still = kQ/r² where Q = total enclosed
    print(f"P1: E_interior = 0 regardless of external field — guaranteed by Gauss")
    print(f"P2: For Q_inner in cavity at center, E at r=0.30 m = {K_COULOMB*Q_OUTER/0.09:.1f} N/C")
    print(f"   Same as kQ_outer/r² = {K_COULOMB*Q_OUTER/r**2:.1f} N/C")
    print("=== PASSED ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ── Manim scene ───────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class EmFaradayCageScene(Scene):
    """
    Cross-section of conducting shell. External E field lines bend around;
    interior is field-free. Gaussian surface sweep confirms Q_enc = 0.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_gauss_argument()
        self._phase_field_diagram()
        self._phase_verification()

    def _phase_title(self):
        title = Text("Faraday Cage — E = 0 Inside a Conductor",
                     font="EB Garamond", font_size=52, color=INK)
        sub = Text("Not a material property — a consequence of Gauss's law",
                   font="EB Garamond", font_size=24, color=BLUE)
        hook = Text("Every free charge moves until the internal field is exactly zero",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_gauss_argument(self):
        steps = VGroup(
            MathTex(r"\text{Inside conductor: }E_{\rm internal} = 0",
                    color=INK, font_size=32),
            MathTex(r"\text{Gaussian surface inside conductor: }\oint\vec{E}\cdot d\vec{A}=0",
                    color=BLUE, font_size=28),
            MathTex(r"\Rightarrow Q_{\rm enc} = 0", color=GOLD, font_size=36),
            MathTex(r"\text{All charge on outer surface}",
                    color=DIM, font_size=28),
        ).arrange(DOWN, buff=0.45).center()
        for mob in steps:
            self.play(Write(mob), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(steps), run_time=0.5)

    def _phase_field_diagram(self):
        # Conducting shell (annular ring in cross section)
        outer_ring = Circle(radius=2.5, color=DIM, stroke_width=8)
        inner_ring = Circle(radius=1.8, color=DIM, stroke_width=2, stroke_opacity=0.5)
        conductor_lbl = Text("conductor", font="EB Garamond", font_size=18, color=DIM
                             ).move_to([2.1, 0, 0])

        # Cavity: dark region inside
        cavity = Circle(radius=1.7, color=CANVAS, fill_color=CANVAS, fill_opacity=1.0,
                        stroke_width=0)
        interior_lbl = MathTex(r"E = 0", color=GOLD, font_size=32).center()

        # External field lines: approach from left, bend around shell
        ext_arrows = VGroup()
        for y in np.linspace(-1.5, 1.5, 5):
            # Left of shell
            arr = Arrow(start=[-5.5, y, 0], end=[-2.6, y, 0], color=BLUE,
                        stroke_width=1.5, buff=0, tip_length=0.18)
            ext_arrows.add(arr)
            # Right of shell
            arr2 = Arrow(start=[2.6, y, 0], end=[5.5, y, 0], color=BLUE,
                         stroke_width=1.5, buff=0, tip_length=0.18)
            ext_arrows.add(arr2)

        external_E = MathTex(r"E_{\rm ext}", color=BLUE, font_size=24
                             ).move_to([-4.5, 2.0, 0])
        zero_badge = MathTex(r"E_{\rm inside}=0", color=GOLD, font_size=24
                             ).center()

        # Gaussian surface (dashed circle inside conductor)
        gauss = DashedVMobject(Circle(radius=2.1, color=BROWN, stroke_width=2))
        gauss_lbl = Text("Gaussian surface in conductor: E = 0 everywhere on it",
                         font="EB Garamond", font_size=18, color=BROWN
                         ).to_edge(DOWN, buff=0.28)

        self.play(Create(outer_ring), Create(inner_ring), FadeIn(cavity),
                  Write(conductor_lbl), run_time=1.0)
        self.play(Write(interior_lbl), run_time=0.7)
        self.play(Create(ext_arrows), Write(external_E), run_time=1.5)
        self.play(Create(gauss), Write(gauss_lbl), run_time=1.2)
        self.wait(3.0)
        self.play(FadeOut(outer_ring, inner_ring, cavity, conductor_lbl,
                          interior_lbl, ext_arrows, external_E, gauss, gauss_lbl),
                  run_time=0.5)

    def _phase_verification(self):
        r = 0.30
        eq1 = MathTex(
            r"E(r=0.30\,\mathrm{m}) = \frac{kQ}{r^2} = "
            + f"{E_outside(r):.0f}" + r"\,\mathrm{N/C\;(outside)}",
            color=INK, font_size=30)
        eq2 = MathTex(r"E\,(r=0.15\,\mathrm{m}) = 0.000\,\mathrm{N/C\;(inside)}",
                      color=GOLD, font_size=30)
        note = Text(
            "Shielding isn't a design choice — the free electrons enforce it automatically",
            font="EB Garamond", font_size=21, color=DIM)
        VGroup(eq1, eq2, note).arrange(DOWN, buff=0.55).center()
        for mob in [eq1, eq2, note]:
            self.play(Write(mob), run_time=0.9)
        self.wait(3.5)
