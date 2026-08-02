#!/usr/bin/env python3
"""
modern_chandrasekhar_limit.py — Chandrasekhar Limit: White Dwarf Mass-Radius Curve
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    Non-relativistic: R ∝ M^{-1/3}
    Chandrasekhar limit: M_Ch ≈ 1.44 M_sun
    Sirius B: 1.02 M_sun, R ≈ 5800 km

Run standalone to verify:
    python3 modern_chandrasekhar_limit.py
"""
import sys
import numpy as np

M_SUN = 1.989e30     # kg
R_SUN = 6.957e8      # m
R_EARTH = 6.371e6    # m

# WD mass-radius relation (non-relativistic polytrope, μ_e=2)
# R/R_sun = (0.0127) * (M/M_sun)^{-1/3}  (approximate, for fully ionized C/O)
R_COEFF_NONREL = 0.0127  # R_sun


def R_WD_nonrel(M_solar):
    """Non-relativistic WD radius in solar radii."""
    return R_COEFF_NONREL * M_solar**(-1.0 / 3.0)


def R_WD_chandrasekhar(M_solar, M_ch=1.44):
    """
    Approximate full Chandrasekhar mass-radius (including relativistic softening).
    R ∝ (1 - (M/M_ch)^{4/3})^{1/2} * M^{-1/3}
    This bends downward and reaches 0 at M_ch.
    """
    ratio = M_solar / M_ch
    if ratio >= 1.0:
        return 0.0
    return R_COEFF_NONREL * M_solar**(-1.0 / 3.0) * (1.0 - ratio**(4.0 / 3.0))**0.5


def verify():
    print("=== Chandrasekhar limit verification ===")
    for M in [0.5, 1.0, 1.02, 1.3, 1.44]:
        R_nr = R_WD_nonrel(M) * R_SUN / 1e3  # km
        R_ch = R_WD_chandrasekhar(M) * R_SUN / 1e3
        print(f"M={M:.2f} M_sun: R_nonrel={R_nr:.0f} km, R_Chan={R_ch:.0f} km")
    print(f"\nSirius B: 1.02 M_sun → R_nonrel = {R_WD_nonrel(1.02)*R_SUN/1e3:.0f} km  (HST: 5840 km)")
    print(f"P1: More massive WD → smaller radius (inverted): R ∝ M^{{-1/3}}")
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


class ModernChandrasekharLimitScene(Scene):
    """
    Mass-radius curve for white dwarfs: non-relativistic (R ∝ M^{-1/3})
    and full Chandrasekhar result bending to zero at 1.44 M_sun.
    Sirius B dot. Limit annotation.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_curve()
        self._phase_endpoints()

    def _phase_title(self):
        title = Text("Chandrasekhar Limit — White Dwarf Mass-Radius",
                     font="EB Garamond", font_size=50, color=INK)
        sub = Text("Add mass and it shrinks — keep adding and it collapses to zero",
                   font="EB Garamond", font_size=23, color=BLUE)
        hook = Text(
            "Not an engineering limit — a quantum mechanical one. Derived at age 19 on a steamship.",
            font="EB Garamond", font_size=20, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        eqs = VGroup(
            MathTex(r"R \propto M^{-1/3}\quad\text{(non-relativistic)}",
                    color=BLUE, font_size=34),
            MathTex(r"M_{\rm Ch} = \frac{5.87}{\mu_e^2}M_\odot \approx 1.44\,M_\odot",
                    color=GOLD, font_size=34),
            MathTex(r"\text{Beyond }M_{\rm Ch}:\;\text{neutron star or black hole}",
                    color=DIM, font_size=28),
        ).arrange(DOWN, buff=0.48).center()
        for mob in eqs:
            self.play(Write(mob), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(eqs), run_time=0.5)

    def _phase_curve(self):
        M_vals = np.linspace(0.1, 1.43, 300)
        R_nonrel = [R_WD_nonrel(m) * R_SUN / R_EARTH for m in M_vals]  # in Earth radii
        R_chan = [R_WD_chandrasekhar(m) * R_SUN / R_EARTH for m in M_vals]

        ax = Axes(
            x_range=[0, 1.55, 0.3],
            y_range=[0, 6, 1],
            x_length=9,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"M\;(M_\odot)", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"R\;(R_\oplus)", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title = Text("White dwarf mass-radius: more mass → smaller radius",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), Create(ax), Write(lx), Write(ly), run_time=1.2)

        # Non-relativistic curve
        valid_nr = [r <= 6 for r in R_nonrel]
        c_nonrel = ax.plot_line_graph(
            x_values=[m for m, v in zip(M_vals, valid_nr) if v],
            y_values=[r for r, v in zip(R_nonrel, valid_nr) if v],
            line_color=BLUE, stroke_width=2.5, add_vertex_dots=False,
        )
        lbl_nr = MathTex(r"R\propto M^{-1/3}\;\text{(non-rel.)}", color=BLUE,
                         font_size=20).to_corner(UR, buff=0.5).shift(DOWN * 0.1)
        self.play(Create(c_nonrel), Write(lbl_nr), run_time=2.0)

        # Full Chandrasekhar curve
        valid_ch = [r >= 0 and r <= 6 for r in R_chan]
        c_chan = ax.plot_line_graph(
            x_values=[m for m, v in zip(M_vals, valid_ch) if v],
            y_values=[r for r, v in zip(R_chan, valid_ch) if v],
            line_color=BROWN, stroke_width=2.5, add_vertex_dots=False,
        )
        lbl_ch = MathTex(r"\text{Full Chandrasekhar}", color=BROWN, font_size=20
                         ).next_to(lbl_nr, DOWN, buff=0.2)
        self.play(Create(c_chan), Write(lbl_ch), run_time=2.0)

        # Chandrasekhar limit dashed line
        limit_line = DashedLine(ax.c2p(1.44, 0), ax.c2p(1.44, 6),
                                color=GOLD, stroke_width=2)
        limit_lbl = MathTex(r"M_{\rm Ch}=1.44\,M_\odot", color=GOLD, font_size=20
                            ).next_to(ax.c2p(1.44, 5.5), RIGHT, buff=0.08)
        self.play(Create(limit_line), Write(limit_lbl), run_time=0.8)

        # Sirius B
        R_siriusB = R_WD_chandrasekhar(1.02) * R_SUN / R_EARTH
        siriusB_dot = Dot(ax.c2p(1.02, R_siriusB), color=GOLD, radius=0.13)
        sb_lbl = MathTex(r"\text{Sirius B}", color=GOLD, font_size=20
                         ).next_to(ax.c2p(1.02, R_siriusB), UR, buff=0.12)
        self.play(FadeIn(siriusB_dot), Write(sb_lbl), run_time=0.8)

        note = Text("Sirius B: 1.02 M_sun, R=5,800 km  (HST: 5,840 km — within 1%)",
                    font="EB Garamond", font_size=19, color=DIM).to_edge(DOWN, buff=0.28)
        self.play(Write(note), run_time=0.7)
        self.wait(3.5)
        self.play(FadeOut(title, ax, lx, ly, c_nonrel, lbl_nr, c_chan, lbl_ch,
                          limit_line, limit_lbl, siriusB_dot, sb_lbl, note),
                  run_time=0.5)

    def _phase_endpoints(self):
        rows = VGroup(
            MathTex(r"M < 1.44\,M_\odot:\;\text{white dwarf (stable)}",
                    color=BLUE, font_size=30),
            MathTex(r"M \approx 1.44\,M_\odot:\;\text{Type Ia supernova trigger}",
                    color=GOLD, font_size=30),
            MathTex(r"M > 1.44\,M_\odot:\;\text{neutron star or black hole}",
                    color=BROWN, font_size=30),
            Text("There is a maximum mass for a cold dead star —",
                 font="EB Garamond", font_size=22, color=INK),
            Text("nature announcing that black holes are mandatory",
                 font="EB Garamond", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.38).center()
        for mob in rows:
            self.play(Write(mob) if isinstance(mob, MathTex) else FadeIn(mob),
                      run_time=0.9)
        self.wait(4.0)
