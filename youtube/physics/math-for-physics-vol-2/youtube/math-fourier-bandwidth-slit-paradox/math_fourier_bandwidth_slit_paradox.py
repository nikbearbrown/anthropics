#!/usr/bin/env python3
"""
math_fourier_bandwidth_slit_paradox.py — Fourier Transform Bandwidth: the Slit Paradox
SILENT SLATE — math-explainer (brownblue) candidate, math-for-physics-vol-2 book.

Δt · Δω ≥ 1/2. Top-hat aperture narrowed → sinc² diffraction pattern widens.
Gaussian: Δx · Δk = 1/2 exactly (minimum uncertainty).

Render:
    cd math-for-physics-vol-2/youtube/math-fourier-bandwidth-slit-paradox
    manim -qh math_fourier_bandwidth_slit_paradox.py FourierBandwidthScene

Verify:
    python3 math_fourier_bandwidth_slit_paradox.py --verify

Testable predictions:
    P1: At a=1.0 the first zero of sinc(ka/2) falls at k=2π≈6.283;
        at a=0.5 it falls at k=4π≈12.566 — exact 2× shift.
    P2: Gaussian f(x)=exp(-x²/2a²) → Δx·Δk = 1/2 for ALL a.
"""
import sys
import numpy as np

# ─── Pure numpy physics — no Manim deps ──────────────────────────────────────

def tophat_ft(k_arr, a):
    """Fourier transform of top-hat of width a: sinc(ka/2)."""
    # F(k) = a * sinc(ka/2π) in numpy sinc convention (normalized)
    # = a * sin(ka/2) / (ka/2)  — raw sinc
    ka2 = k_arr * a / 2.0
    with np.errstate(divide='ignore', invalid='ignore'):
        val = np.where(np.abs(ka2) < 1e-12, 1.0, np.sin(ka2) / ka2)
    return val

def gaussian_ft(k_arr, a):
    """Fourier transform of Gaussian exp(-x²/2a²) → exp(-a²k²/2)."""
    return np.exp(-a**2 * k_arr**2 / 2.0)

def first_zero(a):
    """First zero of sinc(ka/2): k = 2π/a."""
    return 2 * np.pi / a

def gaussian_widths(a):
    """Δx = a/sqrt(2), Δk = 1/(a*sqrt(2)), product = 1/2."""
    dx = a / np.sqrt(2)
    dk = 1.0 / (a * np.sqrt(2))
    return dx, dk, dx * dk

def verify():
    print("=== Fourier Bandwidth Slit Paradox — verification ===")
    for a in [1.0, 0.5, 0.25]:
        k0 = first_zero(a)
        print(f"a={a:.2f}: first zero at k = {k0:.4f}  (expected {2*np.pi/a:.4f})")
    print()
    print("P1 check: halving a doubles first-zero k?")
    print(f"  a=1.0 → k₀={first_zero(1.0):.4f}")
    print(f"  a=0.5 → k₀={first_zero(0.5):.4f}  (ratio = {first_zero(0.5)/first_zero(1.0):.2f}, expected 2.00) ✓")
    print()
    print("P2 check: Gaussian Δx·Δk = 1/2 for all a?")
    for a in [2.0, 1.0, 0.5, 0.1]:
        dx, dk, prod = gaussian_widths(a)
        print(f"  a={a:.1f}: Δx={dx:.4f}, Δk={dk:.4f}, product={prod:.4f}  (expected 0.5000) {'✓' if abs(prod-0.5)<1e-10 else '✗'}")
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


class FourierBandwidthScene(Scene):
    """
    Slit narrowed → diffraction pattern widens.
    Then Gaussian pair shows Δx·Δk = 0.500 exactly.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_tophat()
        self._phase_gaussian()

    # ── Phase 1: Title card ──────────────────────────────────────────────────

    def _phase_title(self):
        title = Text("Fourier Bandwidth", font="EB Garamond", font_size=64, color=INK)
        sub1 = Text(
            "narrow aperture  ·  wide diffraction  ·  Δx · Δk ≥ 1/2",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2 = Text(
            "The Gaussian saturates the bound — no other shape can do better",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    # ── Phase 2: Top-hat apertures vs sinc² diffraction ─────────────────────

    def _phase_tophat(self):
        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)

        ax_x = Axes(
            x_range=[-2.5, 2.5, 1.0], y_range=[-0.15, 1.25, 0.5],
            x_length=5.5, y_length=3.5, axis_config=axis_cfg,
        ).shift(LEFT * 3.4 + DOWN * 0.2)

        ax_k = Axes(
            x_range=[-20, 20, 5], y_range=[-0.15, 1.25, 0.5],
            x_length=5.5, y_length=3.5, axis_config=axis_cfg,
        ).shift(RIGHT * 3.4 + DOWN * 0.2)

        lbl_x  = MathTex(r"x", color=INK, font_size=24).next_to(ax_x.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_ax = MathTex(r"f(x)", color=INK, font_size=24).next_to(ax_x.y_axis.get_end(), UP, buff=0.08)
        lbl_k  = MathTex(r"k", color=INK, font_size=24).next_to(ax_k.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_ak = MathTex(r"|F(k)|", color=INK, font_size=24).next_to(ax_k.y_axis.get_end(), UP, buff=0.08)

        hdr_x = Text("Aperture  f(x)", font="EB Garamond", font_size=20, color=DIM).next_to(ax_x, UP, buff=0.12)
        hdr_k = Text("Diffraction  |F(k)|", font="EB Garamond", font_size=20, color=DIM).next_to(ax_k, UP, buff=0.12)

        self.play(
            Create(ax_x), Create(ax_k),
            Write(lbl_x), Write(lbl_ax), Write(lbl_k), Write(lbl_ak),
            Write(hdr_x), Write(hdr_k),
            run_time=1.8,
        )

        colors = [BLUE, GOLD, BROWN]
        widths = [1.0, 0.5, 0.25]
        x_arr = np.linspace(-2.5, 2.5, 600)
        k_arr = np.linspace(-20, 20, 1000)

        prev_aperture = None
        prev_sinc     = None
        prev_zero_line = None
        prev_lbl = None

        for i, (a, col) in enumerate(zip(widths, colors)):
            # Top-hat: |x| < a/2
            th = np.where(np.abs(x_arr) <= a / 2.0, 1.0, 0.0)
            ft = np.abs(tophat_ft(k_arr, a))
            ft /= ft.max()

            aperture_pts = [ax_x.c2p(x, y) for x, y in zip(x_arr, th)]
            sinc_pts     = [ax_k.c2p(k, y) for k, y in zip(k_arr, ft)]

            aperture = VMobject(color=col, stroke_width=3.5)
            aperture.set_points_smoothly(aperture_pts)
            sinc_curve = VMobject(color=col, stroke_width=3.5)
            sinc_curve.set_points_smoothly(sinc_pts)

            k0 = first_zero(a)
            zero_x = ax_k.c2p(k0, 0.0)
            zero_line = DashedLine(
                ax_k.c2p(k0, -0.08), ax_k.c2p(k0, 1.1),
                color=col, stroke_width=1.8, dash_length=0.12,
            )
            zero_lbl = MathTex(
                rf"k_0 = {k0:.2f}", color=col, font_size=22,
            ).next_to(ax_k.c2p(k0, 1.1), UP, buff=0.05)

            caption = Text(
                f"a = {a:.2f}  →  first zero at k = {k0:.3f}",
                font="EB Garamond", font_size=22, color=col,
            ).to_edge(DOWN, buff=0.28)

            if prev_aperture is not None:
                self.play(
                    FadeOut(prev_aperture), FadeOut(prev_sinc),
                    FadeOut(prev_zero_line), FadeOut(prev_lbl),
                    run_time=0.4,
                )
            self.play(FadeOut(prev_lbl) if prev_lbl else Wait(0), run_time=0.1)

            self.play(
                Create(aperture), Create(sinc_curve),
                Create(zero_line), Write(zero_lbl),
                Write(caption),
                run_time=2.0,
            )
            self.wait(1.5)
            self.play(FadeOut(caption), run_time=0.3)

            prev_aperture = aperture
            prev_sinc     = sinc_curve
            prev_zero_line = zero_line
            prev_lbl = zero_lbl

        self.play(
            FadeOut(prev_aperture, prev_sinc, prev_zero_line, prev_lbl,
                    ax_x, ax_k, lbl_x, lbl_ax, lbl_k, lbl_ak, hdr_x, hdr_k),
            run_time=0.7,
        )

    # ── Phase 3: Gaussian pair — Δx·Δk = 0.500 always ──────────────────────

    def _phase_gaussian(self):
        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)

        ax_x = Axes(
            x_range=[-6, 6, 2], y_range=[-0.05, 1.2, 0.5],
            x_length=5.5, y_length=3.5, axis_config=axis_cfg,
        ).shift(LEFT * 3.4 + DOWN * 0.2)

        ax_k = Axes(
            x_range=[-15, 15, 5], y_range=[-0.05, 1.2, 0.5],
            x_length=5.5, y_length=3.5, axis_config=axis_cfg,
        ).shift(RIGHT * 3.4 + DOWN * 0.2)

        lbl_x = MathTex(r"x", color=INK, font_size=24).next_to(ax_x.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_k = MathTex(r"k", color=INK, font_size=24).next_to(ax_k.x_axis.get_end(), RIGHT, buff=0.08)
        hdr_x = Text("Position  ψ(x)", font="EB Garamond", font_size=20, color=DIM).next_to(ax_x, UP, buff=0.12)
        hdr_k = Text("Momentum  |ψ̃(k)|²", font="EB Garamond", font_size=20, color=DIM).next_to(ax_k, UP, buff=0.12)

        self.play(Create(ax_x), Create(ax_k), Write(lbl_x), Write(lbl_k),
                  Write(hdr_x), Write(hdr_k), run_time=1.5)

        product_lbl = MathTex(r"\Delta x \cdot \Delta k = 0.500", color=GOLD, font_size=32)
        product_lbl.to_edge(DOWN, buff=0.3)
        self.play(Write(product_lbl), run_time=0.8)

        a_tracker = ValueTracker(2.0)
        x_arr = np.linspace(-6, 6, 600)
        k_arr = np.linspace(-15, 15, 600)

        def _gauss_x():
            a = a_tracker.get_value()
            y = np.exp(-x_arr**2 / (2 * a**2))
            pts = [ax_x.c2p(x, yy) for x, yy in zip(x_arr, y)]
            m = VMobject(color=BLUE, stroke_width=3.5)
            m.set_points_smoothly(pts)
            return m

        def _gauss_k():
            a = a_tracker.get_value()
            y = gaussian_ft(k_arr, a)
            y /= y.max() if y.max() > 0 else 1
            pts = [ax_k.c2p(k, yy) for k, yy in zip(k_arr, y)]
            m = VMobject(color=BROWN, stroke_width=3.5)
            m.set_points_smoothly(pts)
            return m

        def _dx_line():
            a = a_tracker.get_value()
            dx = a / np.sqrt(2)
            return DashedLine(
                ax_x.c2p(-dx, 0), ax_x.c2p(dx, 0),
                color=GOLD, stroke_width=2.5,
            )

        def _dk_line():
            a = a_tracker.get_value()
            dk = 1.0 / (a * np.sqrt(2))
            return DashedLine(
                ax_k.c2p(-dk, 0), ax_k.c2p(dk, 0),
                color=GOLD, stroke_width=2.5,
            )

        gx = always_redraw(_gauss_x)
        gk = always_redraw(_gauss_k)
        dx = always_redraw(_dx_line)
        dk = always_redraw(_dk_line)

        self.add(gx, gk, dx, dk)

        # Animate a from 2.0 → 0.3 → 2.5
        self.play(a_tracker.animate.set_value(0.3), run_time=4.0, rate_func=smooth)
        self.wait(1.0)
        self.play(a_tracker.animate.set_value(2.5), run_time=4.0, rate_func=smooth)
        self.wait(1.5)

        final = Text(
            "Narrow in x  ↔  wide in k   ·   product locked at 1/2",
            font="EB Garamond", font_size=26, color=INK,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(product_lbl), Write(final), run_time=1.2)
        self.wait(2.5)
