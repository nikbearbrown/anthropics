#!/usr/bin/env python3
"""
astro_planck_temperature_sweep.py — Planck Curves: Temperature Sweep, Wien Shift, Stefan-Boltzmann
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-planck-temperature-sweep
    manim -qh astro_planck_temperature_sweep.py PlanckTemperatureSweepScene

Verify:
    python3 astro_planck_temperature_sweep.py

Physics:
    Planck: B_λ = (2hc²/λ⁵) / (exp(hc/λkT) - 1)
    Wien: λ_peak = b/T, b = 2.898e-3 m·K
    L ∝ T⁴ (Stefan-Boltzmann at fixed R)
    Stars: M-dwarf 3000K, Sun 5778K, Sirius 9940K, Rigel 12100K
"""
import sys
import numpy as np

H_PLANCK = 6.62607e-34   # J·s
K_BOLTZ  = 1.38065e-23   # J/K
C_LIGHT  = 2.99792e8     # m/s
B_WIEN   = 2.897771e-3   # m·K


def planck_B_lambda(lam_nm: np.ndarray, T: float) -> np.ndarray:
    """Spectral radiance B_λ (W/sr/m²/m) vs wavelength in nm."""
    lam = lam_nm * 1e-9
    exponent = H_PLANCK * C_LIGHT / (lam * K_BOLTZ * T)
    # Clip to avoid overflow
    exponent = np.clip(exponent, 0, 700)
    return (2.0 * H_PLANCK * C_LIGHT**2 / lam**5) / (np.exp(exponent) - 1.0)


def wien_peak(T: float) -> float:
    """λ_peak in nm."""
    return B_WIEN / T * 1e9


def stefan_ratio(T: float, T_ref: float) -> float:
    """L(T)/L(T_ref) at fixed radius."""
    return (T / T_ref) ** 4


def verify():
    print("=== Planck temperature sweep verification ===")
    stars = [
        ("M-dwarf", 3000), ("Sun", 5778), ("Sirius A", 9940), ("Rigel", 12100),
    ]
    for name, T in stars:
        lam = wien_peak(T)
        print(f"  {name} T={T}K → λ_peak = {lam:.1f} nm")

    # P1: Wien law
    lam_sun = wien_peak(5778)
    print(f"\nP1: Sun λ_peak = {lam_sun:.1f} nm  (card says 502 nm)")

    # P2: L∝T⁴ — doubling T from 3000→6000 K gives 16×
    ratio = stefan_ratio(6000, 3000)
    print(f"P2: L(6000K)/L(3000K) = {ratio:.1f}  (should be 16)")

    # Rigel vs Sun
    ratio_rs = stefan_ratio(12100, 5778)
    print(f"L(Rigel)/L(Sun) at fixed R = {ratio_rs:.1f}  (card says 19.3×)")
    print("=== PASSED ===" if abs(ratio - 16.0) < 1e-6 else "=== CHECK ===")


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


class PlanckTemperatureSweepScene(Scene):
    """
    Planck curve sweeps T from 3000K to 12000K.
    Peak marker moves left (Wien shift). Area explodes (Stefan-Boltzmann).
    Key stars labeled as dots.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_planck_sweep()
        self._phase_wien_law()

    def _phase_title(self):
        title = Text("Planck Blackbody Curves", font="EB Garamond", font_size=58, color=INK)
        sub1 = Text(
            "Double the temperature → 16× more luminosity; half the peak wavelength.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"\lambda_{\rm peak} = \frac{b}{T},\quad L \propto T^4",
                       color=BLUE, font_size=30)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_planck_sweep(self):
        lam_arr = np.linspace(100, 2000, 400)
        T_ref  = 5778.0  # Sun — normalise to 1

        # Normalise all curves to Sun's peak
        B_sun = planck_B_lambda(lam_arr, T_ref)
        B_max = B_sun.max()

        ax = Axes(
            x_range=[100, 2000, 400],
            y_range=[0, 22.0, 5.0],
            x_length=9.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.4)
        lbl_x = MathTex(r"\lambda\;(\mathrm{nm})", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"B_\lambda / B_{\rm Sun,max}", color=INK, font_size=20
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Visible band shading
        vis_left  = ax.c2p(380, 0)
        vis_right = ax.c2p(700, 4.5 * ax.y_length / 22.0 * 22)
        vis_rect  = Rectangle(
            width=ax.c2p(700,0)[0] - ax.c2p(380,0)[0],
            height=ax.c2p(0,5)[1] - ax.c2p(0,0)[1],
            color=BLUE, fill_color=BLUE, fill_opacity=0.07, stroke_width=0,
        )
        vis_rect.move_to([(ax.c2p(380,0)[0]+ax.c2p(700,0)[0])/2, ax.c2p(0,2.5)[1], 0])
        vis_lbl = Text("visible", font="EB Garamond", font_size=14, color=BLUE
                       ).move_to([(ax.c2p(380,0)[0]+ax.c2p(700,0)[0])/2, ax.c2p(0,0.25)[1], 0])

        hdr = Text("Blackbody spectrum — temperature sweep 3000 K → 12 000 K",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr),
                  FadeIn(vis_rect), Write(vis_lbl), run_time=1.5)

        stars = [
            (3000,  DIM,   "M-dwarf 3000 K"),
            (5778,  BLUE,  "Sun 5778 K"),
            (9940,  GOLD,  "Sirius 9940 K"),
            (12100, BROWN, "Rigel 12100 K"),
        ]

        prev_curve = None
        for T, color, lbl_str in stars:
            B = planck_B_lambda(lam_arr, T) / B_max
            new_curve = VMobject(color=color, stroke_width=3.0)
            new_curve.set_points_smoothly([ax.c2p(lam, b) for lam, b in zip(lam_arr, B)])

            lam_peak = wien_peak(T)
            pk_dot = Dot(ax.c2p(lam_peak, planck_B_lambda(np.array([lam_peak]), T)[0] / B_max),
                         radius=0.09, color=color)
            pk_lbl = Text(lbl_str, font="EB Garamond", font_size=16, color=color
                          ).next_to(pk_dot, UR, buff=0.04)
            caption = Text(f"λ_peak = {lam_peak:.0f} nm",
                           font="EB Garamond", font_size=19, color=color
                           ).to_edge(DOWN, buff=0.28)

            if prev_curve is None:
                self.play(Create(new_curve), FadeIn(pk_dot), Write(pk_lbl),
                          Write(caption), run_time=1.2)
            else:
                self.play(Create(new_curve), FadeIn(pk_dot), Write(pk_lbl),
                          Transform(self._cap, caption), run_time=1.0)
            prev_curve = new_curve
            self._cap = caption

        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_wien_law(self):
        T_arr = np.linspace(3000, 12000, 300)
        lam_arr = B_WIEN / T_arr * 1e9

        ax = Axes(
            x_range=[3000, 12000, 2000],
            y_range=[0, 1100, 200],
            x_length=8.5,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.5)
        lbl_x = MathTex(r"T\;(\mathrm{K})", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"\lambda_{\rm peak}\;(\mathrm{nm})", color=INK, font_size=20
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Wien displacement law: λ_peak = b/T",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)

        c_wien = VMobject(color=BLUE, stroke_width=3.5)
        c_wien.set_points_smoothly([ax.c2p(T, lam) for T, lam in zip(T_arr, lam_arr)])

        star_dots = {
            "Sun": (5778, GOLD), "Sirius": (9940, BROWN), "M-dwarf": (3000, DIM),
        }

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.1)
        self.play(Create(c_wien), run_time=1.4)
        for name, (T, color) in star_dots.items():
            lam = wien_peak(T)
            d = Dot(ax.c2p(T, lam), radius=0.1, color=color)
            lbl = Text(name, font="EB Garamond", font_size=17, color=color).next_to(d, UR, buff=0.05)
            self.play(FadeIn(d), Write(lbl), run_time=0.6)

        cap = MathTex(
            r"b = 2.898 \times 10^{-3}\;\mathrm{m\cdot K}",
            color=INK, font_size=26,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(cap), run_time=0.9)
        self.wait(3.0)
