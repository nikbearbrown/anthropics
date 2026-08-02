#!/usr/bin/env python3
"""
modern_gravitational_redshift.py — Gravitational Redshift: λ_∞/λ_r = 1/√(1 − R_S/r)
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-modern-physics book.

Render:
    cd physics-plus-one-modern-physics/youtube/modern-gravitational-redshift
    manim -qh modern_gravitational_redshift.py GravRedshiftScene

Physics:
    R_S = 2GM/c² (Schwarzschild radius)
    10 M_sun black hole: R_S = 2×6.674e-11×10×1.989e30/(3e8)² = 29.54 km
    At r=2R_S: λ_∞/λ_r = 1/sqrt(0.5) = sqrt(2) = 1.414
    At r=1.1R_S: λ_∞/λ_r = 1/sqrt(1-1/1.1) = 1/sqrt(0.0909) = 3.317
    Pound-Rebka: Δf/f = gh/c² = 9.80×22.5/(3e8)² = 2.45e-15
"""
import sys
import numpy as np

G_GRAV = 6.674e-11
C_LIGHT = 3.0e8
M_SUN   = 1.989e30
M_BH    = 10 * M_SUN


def schwarzschild_radius(M):
    return 2.0 * G_GRAV * M / C_LIGHT**2


def redshift_factor(r, RS):
    """λ_∞/λ_r = 1/sqrt(1 - R_S/r)."""
    return 1.0 / np.sqrt(1.0 - RS / r)


def pound_rebka(g=9.80, h=22.5):
    return g * h / C_LIGHT**2


if __name__ == "__main__":
    print("=== Gravitational Redshift Verification ===")
    RS = schwarzschild_radius(M_BH)
    print(f"10 M_sun BH: R_S = {RS/1e3:.2f} km  (expect 29.5 km)")
    assert abs(RS - 29.5e3) < 0.2e3, f"RS FAIL: {RS/1e3:.2f} km"
    # P1: at r = 2R_S
    z1 = redshift_factor(2 * RS, RS)
    print(f"P1: at r=2R_S: λ_∞/λ_r = {z1:.4f}  (expect sqrt(2)={np.sqrt(2):.4f})")
    assert abs(z1 - np.sqrt(2)) < 1e-4, "P1 FAIL"
    # P2: Pound-Rebka
    pr = pound_rebka()
    print(f"P2: Pound-Rebka Δf/f = {pr:.3e}  (expect 2.45e-15)")
    assert abs(pr - 2.45e-15) < 0.05e-15, f"P2 FAIL: {pr:.3e}"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class GravRedshiftScene(Scene):
    """Gravitational redshift curve + Pound-Rebka inset."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_curve(ax)
        self._phase_pound_rebka()

    def _phase_title(self):
        title = Text("Gravitational Redshift", font="EB Garamond",
                     font_size=54, color=INK)
        sub = MathTex(
            r"\lambda_\infty/\lambda_r = 1/\sqrt{1-R_S/r}",
            color=BLUE, font_size=32)
        sub2 = Text("Light climbing out of a gravity well stretches",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[1.0, 8.0, 1.0],
            y_range=[1.0, 5.0, 1.0],
            x_length=8.5,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.2)
        x_lbl = MathTex(r"r/R_S", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"\lambda_\infty/\lambda_r", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        # R_S marker
        rs_line = DashedLine(ax.c2p(1.0, 1.0), ax.c2p(1.0, 4.8),
                             color=BROWN, stroke_width=1.5)
        rs_lbl  = MathTex(r"r=R_S\;(\text{singularity})", color=BROWN, font_size=18
                          ).next_to(ax.c2p(1.0, 4.8), UP, buff=0.05)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl),
                  Create(rs_line), Write(rs_lbl), run_time=1.5)
        return ax

    def _phase_curve(self, ax):
        RS = schwarzschild_radius(M_BH)
        r_over_RS = np.linspace(1.01, 8.0, 600)
        z = redshift_factor(r_over_RS * RS, RS)
        z_c = np.clip(z, 1.0, 4.8)

        pts = [ax.c2p(r, z_) for r, z_ in zip(r_over_RS, z_c)]
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)

        # Key points
        pt_2RS  = Dot(ax.c2p(2.0, np.sqrt(2)), color=GOLD, radius=0.1)
        lbl_2RS = MathTex(r"r=2R_S:\;\sqrt{2}=1.414", color=GOLD, font_size=20
                          ).next_to(ax.c2p(2.0, np.sqrt(2)), RIGHT, buff=0.1)

        # Infinity reference: z → 1 as r → ∞
        inf_line = DashedLine(ax.c2p(1.0, 1.0), ax.c2p(8.0, 1.0),
                              color=DIM, stroke_width=1.0)
        inf_lbl = MathTex(r"r\to\infty:\;\lambda_\infty/\lambda_r\to1", color=DIM, font_size=18
                          ).next_to(ax.c2p(5.0, 1.0), DOWN, buff=0.1)

        hdr = Text("10 M_sun black hole — R_S = 29.5 km", font="EB Garamond",
                   font_size=20, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), Create(inf_line), Write(inf_lbl), run_time=0.8)
        self.play(Create(curve), run_time=2.5)
        self.play(FadeIn(pt_2RS), Write(lbl_2RS), run_time=0.8)
        cap = MathTex(
            r"\frac{\lambda_\infty}{\lambda_r}=\frac{1}{\sqrt{1-R_S/r}}"
            r"\xrightarrow{r\to R_S}\infty",
            color=INK, font_size=26).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(hdr, curve, pt_2RS, lbl_2RS, inf_line, inf_lbl, cap), run_time=0.5)

    def _phase_pound_rebka(self):
        hdr = Text("Pound-Rebka 1959 — Measured in an elevator shaft",
                   font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.22)

        pr = pound_rebka()
        rows = [
            MathTex(r"\frac{\Delta f}{f}=\frac{gh}{c^2}",
                    color=BLUE, font_size=34),
            MathTex(
                r"=\frac{9.80\,\mathrm{m/s^2}\times22.5\,\mathrm{m}}{(3\times10^8)^2}",
                color=GOLD, font_size=28),
            MathTex(r"=2.46\times10^{-15}\quad\text{(measured 1959 at 1\% precision)}",
                    color=INK, font_size=24),
        ]
        VGroup(*rows).arrange(DOWN, buff=0.45).center()
        self.play(Write(hdr), run_time=0.5)
        for r in rows:
            self.play(Write(r), run_time=1.0)
            self.wait(0.5)
        self.wait(1.5)
        gps = Text("GPS correction: +38.4 μs/day (without it: 10 km drift/day)",
                   font="EB Garamond", font_size=20, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(Write(gps), run_time=1.0)
        self.wait(2.5)
