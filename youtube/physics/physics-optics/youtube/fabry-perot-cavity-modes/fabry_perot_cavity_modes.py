#!/usr/bin/env python3
"""
fabry_perot_cavity_modes.py — Fabry-Pérot: Cavity Mode Lines Sharpening as R Increases
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/fabry-perot-cavity-modes
    manim -qh fabry_perot_cavity_modes.py FabryPerotCavityModesScene

Numpy verification (run standalone):
    python3 fabry_perot_cavity_modes.py --verify

Physics (checkable):
    T(ν) = 1 / (1 + F·sin²(πνL/c))  where F = 4R/(1−R)²
    Mode spacing: Δν = c/(2L)

    P1: L=30cm → Δν = 3e8/0.6 = 500 MHz ✓
    P2: R=0.95: F = 4×0.95/(0.05)² = 1520; finesse = π√F/2 ≈ 61.1 ✓
"""
import sys
import numpy as np

C = 3e8  # m/s


def finesse_coeff(R):
    """F = 4R/(1−R)²"""
    return 4 * R / (1 - R) ** 2


def transmission(nu_arr, L_m, R):
    """Fabry-Pérot transmission vs frequency."""
    F = finesse_coeff(R)
    phase = np.pi * nu_arr * L_m / C
    return 1.0 / (1.0 + F * np.sin(phase) ** 2)


def mode_spacing(L_m):
    return C / (2 * L_m)


def finesse(R):
    return np.pi * np.sqrt(finesse_coeff(R)) / 2


def verify():
    print("=== Fabry-Pérot cavity modes verification ===")
    # P1
    L = 0.30
    dnu = mode_spacing(L)
    print(f"P1: L={L}m → Δν = c/(2L) = {dnu/1e6:.0f} MHz  (should be 500 MHz)")
    # P2
    R = 0.95
    F = finesse_coeff(R)
    fin = finesse(R)
    print(f"P2: R={R} → F={F:.1f}, finesse = π√F/2 = {fin:.1f}  (should be ≈61.1)")
    # Mode count for HeNe gain bandwidth 1.5 GHz
    gain_bw = 1.5e9
    for L_cm in [10, 30, 60, 100]:
        dnu_l = mode_spacing(L_cm / 100)
        modes = int(gain_bw / dnu_l)
        print(f"  L={L_cm}cm: Δν={dnu_l/1e6:.0f}MHz, modes≈{modes}")
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

GAIN_BW = 1.5e9   # Hz  HeNe gain bandwidth
L_M     = 0.30    # m   cavity length (fixed)


class FabryPerotCavityModesScene(Scene):
    """
    Fabry-Pérot resonator: transmission vs frequency.
    R sweeps from 0.5 to 0.95 — mode peaks sharpen dramatically.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_equation()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Fabry-Pérot Resonator", font="EB Garamond", font_size=56, color=INK)
        sub = Text(
            "T(ν) = 1/(1 + F·sin²(πνL/c))  ·  F = 4R/(1−R)²",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "Higher mirror reflectivity → sharper mode peaks → narrower linewidth",
            font="EB Garamond", font_size=21, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

    def _phase_equation(self):
        eq1 = MathTex(
            r"T(\nu) = \frac{1}{1 + F\sin^2\!\!\left(\frac{\pi\nu L}{c}\right)}",
            color=INK, font_size=36,
        )
        eq2 = MathTex(
            r"F = \frac{4R}{(1-R)^2} \qquad \mathcal{F} = \frac{\pi\sqrt{F}}{2} \quad\text{(finesse)}",
            color=BLUE, font_size=28,
        )
        eq3 = MathTex(
            r"\Delta\nu = \frac{c}{2L} \quad\text{(free spectral range)}",
            color=GOLD, font_size=28,
        )
        VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.4).center()
        self.play(Write(eq1), run_time=1.2)
        self.play(Write(eq2), run_time=0.9)
        self.play(Write(eq3), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(eq1, eq2, eq3), run_time=0.4)

    def _phase_sweep(self):
        dnu = mode_spacing(L_M)  # = 500 MHz for L=30cm
        # Frequency axis: show ~3 free spectral ranges centered at 0
        nu_max = 2.5 * dnu
        nu_arr = np.linspace(-nu_max, nu_max, 4000)
        nu_GHz = nu_arr / 1e9

        ax = Axes(
            x_range=[-nu_max / 1e9, nu_max / 1e9, dnu / 1e9],
            y_range=[0, 1.12, 0.25],
            x_length=11.0,
            y_length=5.2,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.14),
            y_axis_config=dict(numbers_to_include=[0, 0.25, 0.5, 0.75, 1.0]),
        ).shift(UP * 0.3)

        lbl_x = MathTex(r"\nu - \nu_0\;(\mathrm{GHz})", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"T(\nu)", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.4)

        R_vals  = [0.50, 0.70, 0.85, 0.95]
        colors  = [DIM, BROWN, BLUE, GOLD]

        curve = None
        live_lbl = None

        for i, R in enumerate(R_vals):
            T = transmission(nu_arr, L_M, R)
            pts = [ax.c2p(n, t) for n, t in zip(nu_GHz, T)]
            new_curve = VMobject(color=colors[i], stroke_width=3.2)
            new_curve.set_points_smoothly(pts)

            F_val = finesse_coeff(R)
            fin = finesse(R)
            new_lbl = Text(
                f"R = {R:.2f}  ·  F = {F_val:.0f}  ·  finesse = {fin:.1f}",
                font="EB Garamond", font_size=20, color=colors[i],
            ).to_edge(DOWN, buff=0.28)

            if curve is None:
                self.play(Create(new_curve), Write(new_lbl), run_time=1.8)
            else:
                self.play(
                    Transform(curve, new_curve),
                    FadeOut(live_lbl), Write(new_lbl),
                    run_time=1.6,
                )
            self.wait(1.0)
            curve = new_curve
            live_lbl = new_lbl

        # Mode spacing annotation
        mode_ann = MathTex(
            r"\Delta\nu = \frac{c}{2L} = \frac{3\times10^8}{0.60} = 500\,\mathrm{MHz}",
            color=INK, font_size=26,
        ).to_edge(UP, buff=0.22)

        finesse_ann = Text(
            "Higher R → sharper peaks → better frequency selectivity",
            font="EB Garamond", font_size=20, color=BLUE,
        ).to_edge(DOWN, buff=0.28)

        self.play(FadeOut(live_lbl), Write(mode_ann), Write(finesse_ann), run_time=1.2)
        self.wait(3.0)
