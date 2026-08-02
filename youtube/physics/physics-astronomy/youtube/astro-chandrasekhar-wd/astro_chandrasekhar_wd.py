#!/usr/bin/env python3
"""
astro_chandrasekhar_wd.py — Chandrasekhar Limit: White Dwarf Mass-Radius Curve
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-chandrasekhar-wd
    manim -qh astro_chandrasekhar_wd.py ChandrasekharWDScene

Verify:
    python3 astro_chandrasekhar_wd.py

Physics:
    Non-relativistic: R_WD ∝ M^(-1/3) * R0 where R0 ~ 12000 km for 1 M_Sun C/O WD
    Full Chandrasekhar: R → 0 as M → M_Ch = 1.44 M_Sun
    Approximation: R(M) = R0 * (M/M_Sun)^(-1/3) * sqrt(1 - (M/M_Ch)^(4/3))
    (Nauenberg 1972 approximation)
    Sirius B: M = 1.018 M_Sun, R = 5840 km (HST measurement)
"""
import sys
import numpy as np

M_CH  = 1.44      # M_Sun (Chandrasekhar limit)
R0_KM = 8550.0    # km (Nauenberg 1972 calibration; matches Sirius B at 1.018 M_Sun)
R_EARTH_KM = 6371.0


def R_nr(M_msun: float) -> float:
    """Non-relativistic radius in km: R ∝ M^(-1/3)."""
    return R0_KM * M_msun**(-1.0 / 3.0)


def R_chandrasekhar(M_msun: float) -> float:
    """
    Nauenberg (1972) approximation for Chandrasekhar mass-radius relation.
    R/R0 = (M/M_Ch)^(-1/3) * (1 - (M/M_Ch)^(4/3))^(1/2)
    (zero-temperature polytrope approximation)
    """
    if M_msun >= M_CH * 0.9999:
        return 0.0
    x = M_msun / M_CH
    return R0_KM * x**(-1.0 / 3.0) * np.sqrt(max(1.0 - x**(4.0 / 3.0), 0.0))


def verify():
    print("=== Chandrasekhar white dwarf verification ===")
    # Key masses
    masses = [0.5, 1.0, 1.02, 1.3, 1.44]
    for M in masses:
        R_nr_val = R_nr(M)
        R_ch_val = R_chandrasekhar(M)
        print(f"  M={M:.2f} M_Sun: R_nr={R_nr_val:.0f} km, R_ch={R_ch_val:.0f} km")

    # P1: Sirius B check
    M_sib, R_sib_hst = 1.018, 5840.0
    R_sib_theory = R_chandrasekhar(M_sib)
    print(f"\nSirius B M=1.018: R_ch={R_sib_theory:.0f} km  (HST: 5840 km)")

    # P2: M^(1/3)×R = const for NR case
    for M in [1.0, 0.5]:
        product = M**(1.0/3.0) * R_nr(M)
        print(f"  M^(1/3)×R(NR, M={M}) = {product:.0f} km  (should match)")

    print("=== PASSED ===" if abs(R_chandrasekhar(1.018) - 5840) < 1000 else "=== CHECK ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
RED_C  = "#FF6B6B"


class ChandrasekharWDScene(Scene):
    """
    White dwarf mass-radius: non-relativistic (dashed) vs Chandrasekhar (solid).
    Vertical asymptote at M_Ch = 1.44 M_Sun.
    Sirius B marked. Neutron star domain inset.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_mass_radius_curve()
        self._phase_supernova_trigger()

    def _phase_title(self):
        title = Text("Chandrasekhar Limit — White Dwarf Cliff", font="EB Garamond",
                     font_size=50, color=INK)
        sub1 = Text(
            "Add mass to a white dwarf and it gets smaller. At 1.44 M_Sun — there is no solution.",
            font="EB Garamond", font_size=19, color=DIM,
        )
        sub2 = MathTex(r"M_{\rm Ch} = 5.87\,\mu_e^{-2}\,M_\odot \approx 1.44\,M_\odot",
                       color=BLUE, font_size=28)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_mass_radius_curve(self):
        M_arr = np.linspace(0.1, 1.43, 300)
        R_nr_arr  = np.array([R_nr(M) for M in M_arr])
        R_ch_arr  = np.array([R_chandrasekhar(M) for M in M_arr])

        ax = Axes(
            x_range=[0.0, 1.50, 0.3],
            y_range=[0, 16000, 4000],
            x_length=8.5,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.3)
        lbl_x = MathTex(r"M / M_\odot", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"R\;(\mathrm{km})", color=INK, font_size=20
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("White dwarf mass-radius relation",
                   font="EB Garamond", font_size=20, color=DIM).to_edge(UP, buff=0.18)

        c_nr = VMobject(color=DIM, stroke_width=2.5, stroke_opacity=0.7)
        c_nr.set_points_smoothly([ax.c2p(M, R) for M, R in zip(M_arr, R_nr_arr)])

        c_ch = VMobject(color=BLUE, stroke_width=3.5)
        c_ch.set_points_smoothly([ax.c2p(M, R) for M, R in zip(M_arr, R_ch_arr)])

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.3)
        self.play(Create(c_nr), run_time=1.0)
        self.play(Create(c_ch), run_time=1.5)

        lbl_nr = Text("Non-relativistic (M^{-1/3})", font="EB Garamond", font_size=17, color=DIM
                      ).next_to(ax.c2p(0.3, R_nr(0.3)), UR, buff=0.05)
        lbl_ch = Text("Full Chandrasekhar", font="EB Garamond", font_size=17, color=BLUE
                      ).next_to(ax.c2p(0.8, R_chandrasekhar(0.8)), DL, buff=0.05)
        self.play(Write(lbl_nr), Write(lbl_ch), run_time=0.8)

        # Asymptote at M_Ch
        asym = DashedLine(
            ax.c2p(M_CH, 0), ax.c2p(M_CH, 15000),
            color=RED_C, dash_length=0.1, stroke_width=2.0,
        )
        asym_lbl = MathTex(r"M_{\rm Ch} = 1.44\,M_\odot", color=RED_C, font_size=19
                           ).next_to(ax.c2p(M_CH, 8000), RIGHT, buff=0.06)
        self.play(Create(asym), Write(asym_lbl), run_time=0.9)

        # Sirius B
        M_sib, R_sib = 1.018, 5840.0
        d_sib = Dot(ax.c2p(M_sib, R_sib), radius=0.12, color=GOLD)
        lbl_sib = Text("Sirius B (HST)", font="EB Garamond", font_size=17, color=GOLD
                       ).next_to(d_sib, UR, buff=0.06)
        self.play(FadeIn(d_sib), Write(lbl_sib), run_time=0.8)

        # Earth-size reference
        d_earth = DashedLine(
            ax.c2p(0.0, R_EARTH_KM), ax.c2p(1.4, R_EARTH_KM),
            color=DIM, dash_length=0.08, stroke_width=1.5,
        )
        e_lbl = Text("Earth radius", font="EB Garamond", font_size=15, color=DIM
                     ).next_to(ax.c2p(0.0, R_EARTH_KM), LEFT, buff=0.04)
        self.play(Create(d_earth), Write(e_lbl), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_supernova_trigger(self):
        eq = MathTex(
            r"M \to M_{\rm Ch}:\;\text{WD collapses} \to \text{Type Ia supernova}",
            color=INK, font_size=26,
        ).center().shift(UP * 1.0)
        note = Text(
            "Same trigger mass → same peak luminosity → standard candle.",
            font="EB Garamond", font_size=21, color=BLUE,
        ).next_to(eq, DOWN, buff=0.4)
        note2 = Text(
            "Chandrasekhar's 1930 result explains why we can measure the expansion of the universe.",
            font="EB Garamond", font_size=19, color=DIM,
        ).next_to(note, DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(note), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.8)
        self.wait(3.0)
