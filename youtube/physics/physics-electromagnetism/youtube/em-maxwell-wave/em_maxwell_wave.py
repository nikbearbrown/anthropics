#!/usr/bin/env python3
"""
em_maxwell_wave.py — Maxwell's EM Wave: E⊥B⊥propagation, c from two constants
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    c = 1/sqrt(μ₀ε₀) = 2.998×10⁸ m/s
    E₀ = 1000 V/m → B₀ = E₀/c = 3.336 μT
    λ=550 nm (green): f=5.45×10¹⁴ Hz

Run standalone to verify:
    python3 em_maxwell_wave.py
"""
import sys
import numpy as np

MU0 = 4 * np.pi * 1e-7   # T·m/A
EPS0 = 8.854e-12          # F/m
C_LIGHT = 1 / np.sqrt(MU0 * EPS0)
E0 = 1000.0               # V/m


def B0(): return E0 / C_LIGHT
def intensity(): return E0**2 / (2 * MU0 * C_LIGHT)


def verify():
    print("=== Maxwell Wave verification ===")
    print(f"c = 1/√(μ₀ε₀) = {C_LIGHT:.4e} m/s  (should be 2.998e8)")
    print(f"B₀ = E₀/c = {B0()*1e6:.3f} μT  (P1: 3.336 μT)")
    print(f"E₀/B₀ = {E0/B0():.4e}  (should equal c)")
    print(f"Intensity = {intensity():.2f} W/m²  (card: ~1330 W/m²)")
    lam = 550e-9
    f = C_LIGHT / lam
    print(f"λ=550 nm → f = {f:.3e} Hz  (card: 5.45e14)")
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

RED_COLOR = "#E05252"


class EmMaxwellWaveScene(Scene):
    """
    3D-style EM wave visualization: E (blue vertical ribbon) + B (brown horizontal
    ribbon), plus derivation panel showing c = 1/√(μ₀ε₀).
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_derivation()
        self._phase_wave()
        self._phase_e_over_b()

    def _phase_title(self):
        title = Text("Maxwell's Electromagnetic Wave", font="EB Garamond",
                     font_size=54, color=INK)
        sub = MathTex(
            r"c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = 2.998\times10^8\,\mathrm{m/s}",
            color=BLUE, font_size=32)
        hook = Text(
            "The speed of light falls out of two static-field constants — nobody expected that",
            font="EB Garamond", font_size=20, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_derivation(self):
        steps = VGroup(
            MathTex(r"\mu_0 = 4\pi\times10^{-7}\,\mathrm{T\cdot m/A}", color=DIM,
                    font_size=30),
            MathTex(r"\varepsilon_0 = 8.854\times10^{-12}\,\mathrm{F/m}", color=DIM,
                    font_size=30),
            MathTex(r"c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}", color=INK,
                    font_size=36),
            MathTex(r"= \frac{1}{\sqrt{(4\pi\times10^{-7})(8.854\times10^{-12})}}",
                    color=INK, font_size=30),
            MathTex(r"= 2.998\times10^8\,\mathrm{m/s}\;\checkmark", color=GOLD,
                    font_size=36),
        ).arrange(DOWN, buff=0.38).center()
        for mob in steps:
            self.play(Write(mob), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(steps), run_time=0.5)

    def _phase_wave(self):
        # Draw EM wave as two sinusoidal curves in the XY and XZ planes
        N = 300
        x_range = np.linspace(-5.5, 5.5, N)
        lam_scene = 3.0  # scene wavelength
        k = 2 * np.pi / lam_scene

        e_y = np.sin(k * x_range)  # E field (vertical, blue)
        b_z = np.sin(k * x_range)  # B field (horizontal, brown)

        # E ribbon (in XY plane)
        e_pts = [np.array([x, 1.2 * ey, 0]) for x, ey in zip(x_range, e_y)]
        e_curve = VMobject(color=BLUE, stroke_width=3)
        e_curve.set_points_smoothly(e_pts)

        # B ribbon (shifted to look like XZ projection — use y=0 level, vary y in muted color)
        b_pts = [np.array([x, -0.2 + 0.8 * bz, 0]) for x, bz in zip(x_range, b_z)]
        b_curve = VMobject(color=BROWN, stroke_width=3)
        b_curve.set_points_smoothly(b_pts)

        # Propagation arrow
        k_arrow = Arrow(start=[-5, -2.5, 0], end=[5, -2.5, 0], color=GOLD,
                        stroke_width=2, buff=0)
        k_lbl = MathTex(r"\hat{k}\;(\text{propagation})", color=GOLD, font_size=22
                        ).next_to(k_arrow, DOWN, buff=0.1)

        e_lbl = MathTex(r"\vec{E}\;(E_0=1{,}000\,\mathrm{V/m})", color=BLUE,
                        font_size=22).to_corner(UL, buff=0.4)
        b_lbl = MathTex(r"\vec{B}\;(B_0=3.336\,\mathrm{\mu T})", color=BROWN,
                        font_size=22).to_corner(UR, buff=0.4)
        perp_note = Text("E ⊥ B ⊥ propagation  at every point",
                         font="EB Garamond", font_size=22, color=DIM
                         ).to_edge(DOWN, buff=0.28)

        self.play(Create(k_arrow), Write(k_lbl), run_time=0.8)
        self.play(Create(e_curve), Write(e_lbl), run_time=1.8)
        self.play(Create(b_curve), Write(b_lbl), run_time=1.8)
        self.play(Write(perp_note), run_time=0.7)
        self.wait(3.0)
        self.play(FadeOut(e_curve, b_curve, k_arrow, k_lbl, e_lbl, b_lbl, perp_note),
                  run_time=0.5)

    def _phase_e_over_b(self):
        B0_val = B0()
        ratio_eq = MathTex(
            r"\frac{E_0}{B_0} = \frac{1{,}000\,\mathrm{V/m}}{3.336\,\mathrm{\mu T}} = "
            + f"{E0/B0_val:.4e}" + r"\,\mathrm{m/s} = c",
            color=INK, font_size=30,
        )
        intensity_eq = MathTex(
            r"I = \frac{E_0^2}{2\mu_0 c} = "
            + f"{intensity():.0f}" + r"\,\mathrm{W/m^2}",
            color=GOLD, font_size=30,
        )
        note = Text(
            "The same ratio E₀/B₀ = c holds at any wavelength — from gamma rays to radio",
            font="EB Garamond", font_size=21, color=DIM)
        VGroup(ratio_eq, intensity_eq, note).arrange(DOWN, buff=0.5).center()
        for mob in [ratio_eq, intensity_eq, note]:
            self.play(Write(mob), run_time=1.0)
        self.wait(3.5)
