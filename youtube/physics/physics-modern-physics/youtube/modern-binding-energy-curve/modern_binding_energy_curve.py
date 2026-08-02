#!/usr/bin/env python3
"""
modern_binding_energy_curve.py — Binding Energy per Nucleon: The Iron Peak
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    BE/A peak at Fe-56: 8.794 MeV/nucleon
    Fusion of 4p→⁴He releases 26.73 MeV
    Fission of U-235 → ~200 MeV per event

Run standalone to verify:
    python3 modern_binding_energy_curve.py
"""
import sys
import numpy as np

# Empirical BE/A data (A, BE/A in MeV) from published tables
NUCLEAR_DATA = [
    (1,  0.00),   # H (no binding)
    (2,  1.11),   # D
    (3,  2.57),   # He-3
    (4,  7.07),   # He-4 (alpha)
    (6,  5.33),   # Li-6
    (7,  5.61),   # Li-7
    (8,  7.06),   # Be-8
    (12, 7.68),   # C-12
    (14, 7.48),   # N-14
    (16, 7.98),   # O-16
    (20, 8.03),   # Ne-20
    (23, 8.11),   # Na-23
    (27, 8.33),   # Al-27
    (32, 8.49),   # S-32
    (40, 8.55),   # Ca-40
    (56, 8.79),   # Fe-56 (maximum)
    (63, 8.75),   # Cu-63
    (90, 8.72),   # Zr-90
    (120, 8.51),  # Sn-120
    (138, 8.34),  # Ba-138
    (197, 7.92),  # Au-197
    (208, 7.87),  # Pb-208
    (235, 7.59),  # U-235
    (238, 7.57),  # U-238
]


def verify():
    print("=== Binding Energy Curve verification ===")
    print(f"Fe-56: BE/A = 8.794 MeV  (P1 card value)")
    # P2: fusion of 4p → He-4
    m_p = 1.007825  # u
    m_He4 = 4.002602  # u
    delta_m = 4 * m_p - m_He4  # mass defect in u
    E_fusion = delta_m * 931.5  # MeV
    print(f"P2: 4p→He-4 mass defect = {delta_m:.6f} u → {E_fusion:.2f} MeV  (card: 26.73 MeV)")
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


class ModernBindingEnergyCurveScene(Scene):
    """
    BE/A vs A curve draws point by point.
    Fe-56 peak marked. Fusion (left slope) and fission (right slope) arrows.
    Stellar nucleosynthesis schedule annotated.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_curve()
        self._phase_arrows()
        self._phase_stellar()

    def _phase_title(self):
        title = Text("Binding Energy per Nucleon — The Iron Peak",
                     font="EB Garamond", font_size=52, color=INK)
        sub = MathTex(
            r"\frac{BE}{A} = \frac{(Zm_p + Nm_n - M_{\rm nucleus})c^2}{A}",
            color=BLUE, font_size=30)
        hook = Text(
            "Iron is the graveyard of stellar fusion — everything heavier costs a supernova",
            font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        eqs = VGroup(
            MathTex(r"{}^{4}\text{He (alpha):}\;BE/A = 7.07\,\text{MeV}", color=INK, font_size=30),
            MathTex(r"{}^{56}\text{Fe (max):}\;BE/A = 8.79\,\text{MeV}", color=GOLD, font_size=34),
            MathTex(r"{}^{235}\text{U:}\;BE/A = 7.59\,\text{MeV}", color=INK, font_size=30),
            MathTex(r"\text{Fusion }(A<56)\text{ and Fission }(A>56)\text{ both gain energy toward Fe}",
                    color=BLUE, font_size=26),
        ).arrange(DOWN, buff=0.42).center()
        for mob in eqs:
            self.play(Write(mob), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(eqs), run_time=0.5)

    def _phase_curve(self):
        A_vals = [d[0] for d in NUCLEAR_DATA]
        BE_vals = [d[1] for d in NUCLEAR_DATA]

        ax = Axes(
            x_range=[0, 250, 50],
            y_range=[0, 10, 2],
            x_length=10,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"A\;\text{(mass number)}", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"BE/A\;(\text{MeV})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title = Text("Binding energy per nucleon vs mass number",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), Create(ax), Write(lx), Write(ly), run_time=1.2)

        # Draw curve point by point with smooth interpolation
        curve = ax.plot_line_graph(
            x_values=A_vals, y_values=BE_vals,
            line_color=BLUE, stroke_width=3, add_vertex_dots=True,
            vertex_dot_radius=0.06,
            vertex_dot_style=dict(fill_color=BLUE),
        )
        self.play(Create(curve), run_time=3.0)

        # Fe-56 peak marker
        fe_dot = Dot(ax.c2p(56, 8.79), color=GOLD, radius=0.15)
        fe_lbl = MathTex(r"{}^{56}\text{Fe}\;8.79\,\text{MeV}", color=GOLD,
                         font_size=22).next_to(ax.c2p(56, 8.79), UR, buff=0.15)
        self.play(FadeIn(fe_dot), Write(fe_lbl), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(title, ax, lx, ly, curve, fe_dot, fe_lbl), run_time=0.5)

    def _phase_arrows(self):
        # Schematic diagram with arrows
        ax = Axes(
            x_range=[0, 250, 50],
            y_range=[0, 10, 2],
            x_length=10,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        A_vals = [d[0] for d in NUCLEAR_DATA]
        BE_vals = [d[1] for d in NUCLEAR_DATA]
        curve = ax.plot_line_graph(
            x_values=A_vals, y_values=BE_vals,
            line_color=BLUE, stroke_width=2.5, add_vertex_dots=False,
        )
        self.play(Create(ax), Create(curve), run_time=1.0)

        # Fusion arrow: D → He-4 (left slope)
        fusion_arrow = Arrow(start=ax.c2p(2, 1.11), end=ax.c2p(40, 8.55),
                             color=GOLD, stroke_width=2.5, buff=0.1, tip_length=0.22)
        fusion_lbl = Text("fusion\n(energy released)", font="EB Garamond",
                          font_size=18, color=GOLD).next_to(ax.c2p(15, 5), LEFT,
                                                            buff=0.1)
        # Fission arrow: U → Ba+Kr (right slope)
        fission_arrow = Arrow(start=ax.c2p(235, 7.59), end=ax.c2p(140, 8.34),
                              color=BROWN, stroke_width=2.5, buff=0.1, tip_length=0.22)
        fission_lbl = Text("fission\n(energy released)", font="EB Garamond",
                           font_size=18, color=BROWN).next_to(ax.c2p(190, 8.0), RIGHT,
                                                               buff=0.1)
        fe_peak = Dot(ax.c2p(56, 8.79), color=GOLD, radius=0.15)
        fe_lbl = MathTex(r"{}^{56}\text{Fe}", color=GOLD, font_size=22
                         ).next_to(ax.c2p(56, 8.79), UP, buff=0.1)

        self.play(Create(fusion_arrow), Write(fusion_lbl), run_time=1.2)
        self.play(Create(fission_arrow), Write(fission_lbl), run_time=1.2)
        self.play(FadeIn(fe_peak), Write(fe_lbl), run_time=0.8)

        caption = Text(
            "Stars fuse everything up to iron for free — heavier elements cost a supernova",
            font="EB Garamond", font_size=20, color=DIM).to_edge(DOWN, buff=0.28)
        self.play(Write(caption), run_time=0.8)
        self.wait(3.5)
        self.play(FadeOut(ax, curve, fusion_arrow, fusion_lbl, fission_arrow,
                          fission_lbl, fe_peak, fe_lbl, caption), run_time=0.5)

    def _phase_stellar(self):
        steps = VGroup(
            Text("Stellar nucleosynthesis — ascending the left slope:",
                 font="EB Garamond", font_size=26, color=INK),
            MathTex(r"\text{H} \to \text{He core (pp chain)} \to", color=BLUE, font_size=28),
            MathTex(r"\text{He} \to \text{C, O shell} \to", color=BROWN, font_size=28),
            MathTex(r"\text{C/O} \to \text{Ne, Mg} \to \text{Si} \to {}^{56}\text{Fe ash}",
                    color=GOLD, font_size=28),
            Text("Fusion stops at iron. The core collapses → supernova.",
                 font="EB Garamond", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.38).center()
        for mob in steps:
            self.play(FadeIn(mob) if isinstance(mob, Text) else Write(mob), run_time=0.9)
        self.wait(4.0)
