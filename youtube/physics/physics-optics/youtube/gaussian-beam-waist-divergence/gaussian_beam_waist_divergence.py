#!/usr/bin/env python3
"""
gaussian_beam_waist_divergence.py — Gaussian Beam: Waist-Divergence Trade-Off
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/gaussian-beam-waist-divergence
    manim -qh gaussian_beam_waist_divergence.py GaussianBeamScene

Numpy verification (run standalone):
    python3 gaussian_beam_waist_divergence.py --verify

Physics (checkable):
    w(z) = w₀√(1+(z/z_R)²)  where z_R = πw₀²/λ
    Divergence θ_div ≈ λ/(πw₀)
    Product: w₀×θ_div = λ/π (constant)

    P1: w₀=1mm, λ=633nm: z_R = π×(1e-3)²/(6.33e-7) ≈ 4.97m ✓
    P2: w(z_R) = w₀√2 ≈ 1.414×w₀ — universal ratio ✓
"""
import sys
import numpy as np

LAMBDA = 633e-9   # m, HeNe laser


def rayleigh_range(w0_m, lam=LAMBDA):
    """z_R = πw₀²/λ in meters."""
    return np.pi * w0_m ** 2 / lam


def beam_radius(z_arr, w0_m, lam=LAMBDA):
    """w(z) = w₀√(1+(z/z_R)²)"""
    zR = rayleigh_range(w0_m, lam)
    return w0_m * np.sqrt(1 + (z_arr / zR) ** 2)


def divergence_half_angle(w0_m, lam=LAMBDA):
    """θ_div ≈ λ/(πw₀) in radians."""
    return lam / (np.pi * w0_m)


def verify():
    print("=== Gaussian beam waist-divergence verification ===")
    # P1
    w0 = 1e-3  # 1 mm
    zR = rayleigh_range(w0)
    print(f"P1: w₀={w0*1e3:.1f}mm, λ={LAMBDA*1e9:.0f}nm")
    print(f"    z_R = πw₀²/λ = {zR:.3f} m  (should be ≈4.97m)")
    # P2: universal ratio
    w_at_zR = beam_radius(np.array([zR]), w0)[0]
    ratio = w_at_zR / w0
    print(f"P2: w(z_R)/w₀ = {ratio:.4f}  (should be √2 ≈ 1.4142)")
    # Product invariant
    print(f"\nProduct w₀×θ_div = λ/π:")
    for w0_mm in [2.0, 1.0, 0.5, 0.1]:
        w0_m = w0_mm * 1e-3
        zR_m = rayleigh_range(w0_m)
        th = divergence_half_angle(w0_m)
        prod = w0_m * th
        lam_pi = LAMBDA / np.pi
        print(f"  w₀={w0_mm:.1f}mm: z_R={zR_m:.3f}m, θ={th*1e3:.3f}mrad, w₀·θ={prod*1e9:.2f}nm (λ/π={lam_pi*1e9:.2f}nm)")
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


class GaussianBeamScene(Scene):
    """
    Gaussian beam w(z) profile.
    As w₀ decreases: waist narrows, Rayleigh range shrinks, divergence grows.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_equation()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Gaussian Beam", font="EB Garamond", font_size=64, color=INK)
        sub = Text(
            "w(z) = w₀√(1 + (z/z_R)²)  ·  z_R = πw₀²/λ",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "Tighter focus → faster divergence  (w₀ × θ_div = λ/π = const)",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

    def _phase_equation(self):
        eq1 = MathTex(
            r"w(z) = w_0\sqrt{1 + \left(\frac{z}{z_R}\right)^2}",
            r"\qquad z_R = \frac{\pi w_0^2}{\lambda}",
            color=INK, font_size=36,
        )
        eq2 = MathTex(
            r"\theta_{\rm div} \approx \frac{\lambda}{\pi w_0} \qquad \Rightarrow \qquad w_0 \cdot \theta_{\rm div} = \frac{\lambda}{\pi}",
            color=BLUE, font_size=28,
        )
        VGroup(eq1, eq2).arrange(DOWN, buff=0.5).center()
        self.play(Write(eq1), run_time=1.3)
        self.play(Write(eq2), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(eq1, eq2), run_time=0.4)

    def _phase_sweep(self):
        # Display z range ±8m (normalized)
        # Use normalized coords: z/m, w/mm
        w0_vals = [2.0e-3, 1.0e-3, 0.5e-3, 0.1e-3]  # m
        colors = [DIM, BLUE, GOLD, BROWN]

        # Compute z_R for reference (w₀=1mm)
        zR_ref = rayleigh_range(1e-3)  # ≈4.97m

        # Plot axes: z in meters, w in mm
        ax = Axes(
            x_range=[-10, 10, 2],
            y_range=[0, 8.0, 2.0],
            x_length=10.5,
            y_length=5.2,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.14),
            x_axis_config=dict(numbers_to_include=[-8, -4, 0, 4, 8]),
            y_axis_config=dict(numbers_to_include=[0, 2, 4, 6]),
        ).shift(UP * 0.3)

        lbl_x = MathTex(r"z\;(\mathrm{m})", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"w(z)\;(\mathrm{mm})", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # z range for each w0
        z_arr = np.linspace(-10, 10, 1200)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.4)

        # Invariant annotation
        inv_lbl = MathTex(
            r"w_0 \cdot \theta_{\rm div} = \frac{\lambda}{\pi} \approx 201\,\mathrm{nm}",
            color=GOLD, font_size=22,
        ).to_corner(UR, buff=0.3)
        self.play(Write(inv_lbl), run_time=0.7)

        curve_top = None
        curve_bot = None
        live_lbl = None

        for i, w0 in enumerate(w0_vals):
            zR = rayleigh_range(w0)
            w_z = beam_radius(z_arr, w0) * 1e3  # mm

            # Clamp to plot range
            w_top = np.clip(w_z, 0, 7.8)
            w_bot = np.clip(-w_z, -7.8, 0)

            pts_top = [ax.c2p(z, wt) for z, wt in zip(z_arr, w_top)]
            pts_bot = [ax.c2p(z, wb) for z, wb in zip(z_arr, w_bot)]

            new_top = VMobject(color=colors[i], stroke_width=3.5)
            new_top.set_points_smoothly(pts_top)
            new_bot = VMobject(color=colors[i], stroke_width=3.5)
            new_bot.set_points_smoothly(pts_bot)

            theta_div = divergence_half_angle(w0)
            zR_m = rayleigh_range(w0)
            new_lbl = Text(
                f"w₀ = {w0*1e3:.1f} mm  ·  z_R = {zR_m:.2f} m  ·  θ_div = {theta_div*1e3:.2f} mrad",
                font="EB Garamond", font_size=20, color=colors[i],
            ).to_edge(DOWN, buff=0.25)

            if curve_top is None:
                self.play(Create(new_top), Create(new_bot), Write(new_lbl), run_time=2.0)
            else:
                self.play(
                    Transform(curve_top, new_top),
                    Transform(curve_bot, new_bot),
                    FadeOut(live_lbl), Write(new_lbl),
                    run_time=1.6,
                )
            # Rayleigh range markers
            if abs(zR) <= 9.5:
                zR_l = DashedLine(
                    ax.c2p(-zR, 0), ax.c2p(-zR, w0 * 1e3 * np.sqrt(2)),
                    color=colors[i], stroke_width=1.0, dash_length=0.1,
                )
                zR_r = DashedLine(
                    ax.c2p(zR, 0), ax.c2p(zR, w0 * 1e3 * np.sqrt(2)),
                    color=colors[i], stroke_width=1.0, dash_length=0.1,
                )
                self.play(Create(zR_l), Create(zR_r), run_time=0.4)
            self.wait(0.9)
            curve_top, curve_bot = new_top, new_bot
            live_lbl = new_lbl

        # Final payoff
        payoff = MathTex(
            r"w_0 \downarrow \;\Rightarrow\; z_R \propto w_0^2 \downarrow\!\!\downarrow \;\Rightarrow\; \theta_{\rm div} \propto 1/w_0 \uparrow",
            color=INK, font_size=27,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(live_lbl), Write(payoff), run_time=1.2)
        self.wait(3.0)
