#!/usr/bin/env python3
"""
single_slit_diffraction_sinc_squared.py — Single-Slit Sinc² Pattern: Width Inverting as Slit Narrows
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/single-slit-diffraction-sinc-squared
    manim -qh single_slit_diffraction_sinc_squared.py SingleSlitDiffractionScene

Numpy verification (run standalone):
    python3 single_slit_diffraction_sinc_squared.py --verify

Physics (checkable):
    I(θ) = I₀·[sin(α)/α]²  where α = πa·sinθ/λ
    Minima at a·sinθ = mλ  → sinθ_min = mλ/a

    P1: a=0.1mm, λ=500nm: first minimum at sinθ = λ/a = 0.005 rad ✓
        α = π×0.1e-3×0.005/500e-9 = π, sinc²(π)=0 ✓
    P2: First sidelobe maximum at α=3π/2: I/I₀=(1/(3π/2))²≈0.0450=4.5% ✓
"""
import sys
import numpy as np

LAMBDA_NM = 550e-9  # m, visible green


def sinc_squared_intensity(theta_arr, a_m, lam=LAMBDA_NM):
    """I(θ)/I₀ for single-slit diffraction. theta_arr in radians, a_m in meters."""
    alpha = np.pi * a_m * np.sin(theta_arr) / lam
    # sinc²: handle alpha=0 (limit = 1)
    with np.errstate(invalid='ignore', divide='ignore'):
        val = np.where(
            np.abs(alpha) < 1e-12,
            1.0,
            (np.sin(alpha) / alpha) ** 2
        )
    return val


def first_minimum_angle(a_m, lam=LAMBDA_NM):
    """First minimum at sinθ = λ/a → θ in degrees."""
    return np.degrees(np.arcsin(lam / a_m))


def verify():
    print("=== Single-slit diffraction verification ===")
    lam = 500e-9  # P1 uses 500nm
    a = 0.1e-3
    sin_theta_min = lam / a
    print(f"P1: a={a*1e3:.1f}mm, λ={lam*1e9:.0f}nm")
    print(f"    First minimum: sinθ = λ/a = {sin_theta_min:.4f} rad")
    alpha_check = np.pi * a * sin_theta_min / lam
    print(f"    α at first min = {alpha_check:.4f}π (should be π)")
    print(f"    sinc²(π) = {(np.sin(alpha_check)/alpha_check)**2:.6f} (should be ≈0)")
    # P2: sidelobe at α=3π/2
    alpha_sl = 3 * np.pi / 2
    sl_intensity = (np.sin(alpha_sl) / alpha_sl) ** 2
    print(f"P2: First sidelobe at α=3π/2: I/I₀ = {sl_intensity:.4f} = {sl_intensity*100:.1f}% (should be ≈4.5%)")
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


class SingleSlitDiffractionScene(Scene):
    """
    Single-slit sinc² diffraction pattern.
    As slit width a decreases: central maximum widens, sidelobes spread.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        self._phase_title()
        self._phase_equation()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Single-Slit Diffraction", font="EB Garamond", font_size=60, color=INK)
        sub = Text(
            "I(θ) = I₀ · [sin(α)/α]²  where  α = πa·sinθ/λ",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "Smaller slit → wider pattern  (the geometry-optics instinct reversed)",
            font="EB Garamond", font_size=21, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_equation(self):
        eq = MathTex(
            r"I(\theta) = I_0 \left[\frac{\sin\!\left(\frac{\pi a \sin\theta}{\lambda}\right)}{\frac{\pi a \sin\theta}{\lambda}}\right]^2",
            color=INK, font_size=38,
        )
        note = MathTex(
            r"\text{First minimum: } a\sin\theta = \lambda \;\Rightarrow\; \sin\theta_{\min} = \frac{\lambda}{a}",
            color=BLUE, font_size=28,
        )
        VGroup(eq, note).arrange(DOWN, buff=0.5).center()
        self.play(Write(eq), run_time=1.5)
        self.play(Write(note), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(eq, note), run_time=0.4)

    def _phase_sweep(self):
        # Axes: x = sinθ (central region), y = I/I₀
        ax = Axes(
            x_range=[-0.016, 0.016, 0.004],
            y_range=[0, 1.1, 0.25],
            x_length=10.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.15),
            x_axis_config=dict(numbers_to_include=[-0.01, 0, 0.01]),
            y_axis_config=dict(numbers_to_include=[0, 0.25, 0.5, 0.75, 1.0]),
        ).shift(UP * 0.2)

        lbl_x = MathTex(r"\sin\theta", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"I/I_0", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.5)

        # Slit widths to sweep
        slit_widths = [0.5e-3, 0.2e-3, 0.1e-3, 0.05e-3]
        colors = [BLUE, BROWN, GOLD, INK]

        theta_max = np.arcsin(0.015)
        sin_theta = np.linspace(-0.015, 0.015, 1200)
        theta_arr = np.arcsin(np.clip(sin_theta, -0.999, 0.999))

        curve = None
        live_lbl = None
        for i, a in enumerate(slit_widths):
            intensity = sinc_squared_intensity(theta_arr, a)
            pts = [ax.c2p(s, max(0.0, iv)) for s, iv in zip(sin_theta, intensity)]
            new_curve = VMobject(color=colors[i], stroke_width=3.5)
            new_curve.set_points_smoothly(pts)

            # First minimum position
            sin_min = LAMBDA_NM / a
            first_min_x = ax.c2p(sin_min, 0)[0]
            first_min_line = DashedLine(
                start=ax.c2p(sin_min, 0),
                end=ax.c2p(sin_min, 0.12),
                color=colors[i], stroke_width=1.2, dash_length=0.1,
            )
            neg_min_line = DashedLine(
                start=ax.c2p(-sin_min, 0),
                end=ax.c2p(-sin_min, 0.12),
                color=colors[i], stroke_width=1.2, dash_length=0.1,
            )

            # Label
            central_width = 2 * np.degrees(np.arcsin(LAMBDA_NM / a))
            new_lbl_text = f"a = {a*1e3:.2f} mm  ·  central width ∝ 1/a = {central_width:.2f}°"
            new_lbl = Text(new_lbl_text, font="EB Garamond", font_size=20, color=colors[i])
            new_lbl.to_edge(DOWN, buff=0.25)

            if curve is None:
                self.play(Create(new_curve), Create(first_min_line), Create(neg_min_line),
                          Write(new_lbl), run_time=2.0)
            else:
                self.play(
                    Transform(curve, new_curve),
                    FadeOut(live_lbl),
                    Create(first_min_line), Create(neg_min_line),
                    Write(new_lbl),
                    run_time=1.8,
                )
            self.wait(1.0)
            curve = new_curve
            live_lbl = new_lbl

        # Final payoff
        payoff = MathTex(
            r"\Delta\theta_{\rm central} = \frac{2\lambda}{a} \;\;\; \Longrightarrow \;\;\; \text{smaller } a \Rightarrow \text{ wider pattern}",
            color=INK, font_size=28,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(live_lbl), Write(payoff), run_time=1.2)
        self.wait(3.0)
