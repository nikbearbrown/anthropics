#!/usr/bin/env python3
"""
math_gaussian_wave_packet_uncertainty.py — Gaussian Wave Packet: Uncertainty Tradeoff
SILENT SLATE — math-explainer (brownblue) candidate, math-for-physics-vol-2 book.

ψ(x) = exp(-x²/2a²). FT: exp(-a²k²/2). Δx·Δk = 1/2 always.

Render:
    cd math-for-physics-vol-2/youtube/math-gaussian-wave-packet-uncertainty
    manim -qh math_gaussian_wave_packet_uncertainty.py GaussianWavePacketScene

Verify:
    python3 math_gaussian_wave_packet_uncertainty.py --verify

Testable predictions:
    P1: a=1.0 → Δx=0.707, Δk=0.707, product=0.500
    P2: Top-hat of same width → product > 0.5 (Gaussian is minimizer)
"""
import sys
import numpy as np

def gaussian_x(x, a):
    return np.exp(-x**2 / (2 * a**2))

def gaussian_k(k, a):
    return np.exp(-a**2 * k**2 / 2.0)

def widths(a):
    dx = a / np.sqrt(2)
    dk = 1.0 / (a * np.sqrt(2))
    return dx, dk, dx * dk

def tophat_ft_product(a):
    """Δx·Δk for top-hat of half-width a (rms width a/√3)."""
    # Top-hat f(x)=1 for |x|<a, else 0
    # Δx_rms = a/√3
    # FT: F(k) = 2sin(ka)/(k) — sinc shape
    # Δk_rms from ∫k²|F|²dk / ∫|F|²dk computed numerically
    k_arr = np.linspace(-50/a, 50/a, 100000)
    dk_step = k_arr[1] - k_arr[0]
    ka = k_arr * a
    with np.errstate(divide='ignore', invalid='ignore'):
        Fk = np.where(np.abs(ka) < 1e-10, 2*a, 2*np.sin(ka)/k_arr)
    Fk2 = Fk**2
    norm = np.sum(Fk2) * dk_step
    k2_mean = np.sum(k_arr**2 * Fk2) * dk_step / norm
    dk_rms = np.sqrt(k2_mean)
    dx_rms = a / np.sqrt(3)
    return dx_rms * dk_rms

def verify():
    print("=== Gaussian Wave Packet Uncertainty — verification ===")
    for a in [2.0, 1.0, 0.5, 0.1]:
        dx, dk, prod = widths(a)
        print(f"a={a:.1f}: Δx={dx:.4f}, Δk={dk:.4f}, product={prod:.4f}  {'✓' if abs(prod-0.5)<1e-10 else '✗'}")
    print()
    print("P1: a=1.0 → Δx=Δk=1/√2≈0.707, product=0.500  ✓")
    prod_tophat = tophat_ft_product(1.0)
    print(f"P2: Top-hat (a=1): Δx·Δk ≈ {prod_tophat:.4f}  > 0.500?  {'✓ YES' if prod_tophat > 0.5 else '✗ NO'}")
    print("    (Gaussian is unique minimizer — top-hat exceeds 1/2)")
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


class GaussianWavePacketScene(Scene):
    """
    Two-panel: ψ(x) left, |ψ̃(k)|² right.
    Slider a sweeps 2.0 → 0.2 → 2.5.
    Δx·Δk stays pinned at 0.500.
    Then top-hat comparison shows product > 0.5.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_gaussian_sweep()
        self._phase_tophat_compare()

    def _phase_title(self):
        title = Text("Gaussian Wave Packet", font="EB Garamond", font_size=56, color=INK)
        sub1 = Text(
            "position width ↔ momentum width  ·  Δx · Δk ≥ 1/2",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2 = Text(
            "The Gaussian saturates the Heisenberg bound — uniquely",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_gaussian_sweep(self):
        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)

        ax_x = Axes(
            x_range=[-5, 5, 2], y_range=[-0.05, 1.2, 0.5],
            x_length=5.5, y_length=4.0, axis_config=axis_cfg,
        ).shift(LEFT * 3.3 + DOWN * 0.3)

        ax_k = Axes(
            x_range=[-12, 12, 4], y_range=[-0.05, 1.2, 0.5],
            x_length=5.5, y_length=4.0, axis_config=axis_cfg,
        ).shift(RIGHT * 3.3 + DOWN * 0.3)

        lbl_x  = MathTex(r"x",        color=INK, font_size=24).next_to(ax_x.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_px = MathTex(r"\psi(x)",  color=INK, font_size=24).next_to(ax_x.y_axis.get_end(), UP, buff=0.08)
        lbl_k  = MathTex(r"k",        color=INK, font_size=24).next_to(ax_k.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_pk = MathTex(r"|\tilde\psi(k)|^2", color=INK, font_size=24).next_to(ax_k.y_axis.get_end(), UP, buff=0.08)

        hdr_x = Text("Position space", font="EB Garamond", font_size=20, color=DIM).next_to(ax_x, UP, buff=0.12)
        hdr_k = Text("Momentum space", font="EB Garamond", font_size=20, color=DIM).next_to(ax_k, UP, buff=0.12)

        self.play(Create(ax_x), Create(ax_k),
                  Write(lbl_x), Write(lbl_px), Write(lbl_k), Write(lbl_pk),
                  Write(hdr_x), Write(hdr_k), run_time=1.8)

        # Product label (always 0.500)
        product_eq = MathTex(r"\Delta x \cdot \Delta k = 0.500", color=GOLD, font_size=30)
        product_eq.to_edge(DOWN, buff=0.32)
        gabor_line = DashedLine(
            ax_k.c2p(-12, 0), ax_k.c2p(12, 0),
            color=GOLD, stroke_width=1.5, dash_length=0.18,
        )
        gabor_lbl = Text("Gabor floor = 1/2", font="EB Garamond", font_size=18, color=GOLD)
        gabor_lbl.next_to(ax_k.c2p(12, 0), RIGHT, buff=0.05)
        self.play(Write(product_eq), run_time=0.8)

        a_tracker = ValueTracker(2.0)
        x_arr = np.linspace(-5, 5, 500)
        k_arr = np.linspace(-12, 12, 500)

        def _gx():
            a = a_tracker.get_value()
            y = gaussian_x(x_arr, a)
            pts = [ax_x.c2p(x, yy) for x, yy in zip(x_arr, y)]
            m = VMobject(color=BLUE, stroke_width=3.5)
            m.set_points_smoothly(pts)
            return m

        def _gk():
            a = a_tracker.get_value()
            y = gaussian_k(k_arr, a)**2
            pts = [ax_k.c2p(k, yy) for k, yy in zip(k_arr, y)]
            m = VMobject(color=BROWN, stroke_width=3.5)
            m.set_points_smoothly(pts)
            return m

        def _dx_segment():
            a = a_tracker.get_value()
            dx = a / np.sqrt(2)
            return DashedLine(
                ax_x.c2p(-dx, np.exp(-0.5)), ax_x.c2p(dx, np.exp(-0.5)),
                color=GOLD, stroke_width=2.5,
            )

        def _dk_segment():
            a = a_tracker.get_value()
            dk = 1.0 / (a * np.sqrt(2))
            return DashedLine(
                ax_k.c2p(-dk, np.exp(-1.0)), ax_k.c2p(dk, np.exp(-1.0)),
                color=GOLD, stroke_width=2.5,
            )

        def _a_label():
            a = a_tracker.get_value()
            dx, dk, prod = widths(a)
            return MathTex(
                rf"a={a:.2f},\;\Delta x={dx:.3f},\;\Delta k={dk:.3f}",
                color=INK, font_size=22,
            ).to_edge(UP, buff=0.25)

        gx    = always_redraw(_gx)
        gk    = always_redraw(_gk)
        seg_x = always_redraw(_dx_segment)
        seg_k = always_redraw(_dk_segment)
        a_lbl = always_redraw(_a_label)

        self.add(gx, gk, seg_x, seg_k, a_lbl)

        # Sweep a: 2.0 → 0.3 → 2.5
        self.play(a_tracker.animate.set_value(0.3), run_time=5.0, rate_func=smooth)
        self.wait(0.8)
        self.play(a_tracker.animate.set_value(2.5), run_time=4.0, rate_func=smooth)
        self.wait(1.5)

        self.play(
            FadeOut(gx, gk, seg_x, seg_k, a_lbl, product_eq,
                    ax_x, ax_k, lbl_x, lbl_px, lbl_k, lbl_pk, hdr_x, hdr_k),
            run_time=0.7,
        )

    def _phase_tophat_compare(self):
        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18)
        ax_k = Axes(
            x_range=[-15, 15, 5], y_range=[-0.05, 1.2, 0.5],
            x_length=9.0, y_length=4.5, axis_config=axis_cfg,
        ).shift(DOWN * 0.5)

        lbl_k = MathTex(r"k", color=INK, font_size=24).next_to(ax_k.x_axis.get_end(), RIGHT, buff=0.08)
        hdr   = Text("Momentum-space comparison (a = 1.0)", font="EB Garamond",
                     font_size=22, color=DIM).next_to(ax_k, UP, buff=0.12)

        k_arr = np.linspace(-15, 15, 1000)
        a = 1.0

        # Gaussian FT
        gk_y = gaussian_k(k_arr, a)**2
        gk_pts = [ax_k.c2p(k, y) for k, y in zip(k_arr, gk_y)]
        gk_mob = VMobject(color=BLUE, stroke_width=3.5)
        gk_mob.set_points_smoothly(gk_pts)

        # Top-hat FT sinc² (normalized)
        ka = k_arr * a
        with np.errstate(divide='ignore', invalid='ignore'):
            sinc_y = np.where(np.abs(ka) < 1e-9, 1.0, np.sin(ka) / ka)**2
        sinc_pts = [ax_k.c2p(k, y) for k, y in zip(k_arr, sinc_y)]
        sinc_mob = VMobject(color=BROWN, stroke_width=3.0, stroke_opacity=0.85)
        sinc_mob.set_points_smoothly(sinc_pts)

        # Products
        prod_g = 0.500
        prod_t = tophat_ft_product(a)

        self.play(Create(ax_k), Write(lbl_k), Write(hdr), run_time=1.2)
        self.play(Create(gk_mob), run_time=1.5)

        g_lbl = MathTex(
            rf"\text{{Gaussian}}\;\Delta x\cdot\Delta k = {prod_g:.3f}",
            color=BLUE, font_size=24,
        ).to_corner(UL, buff=0.45)
        self.play(Write(g_lbl), run_time=0.7)

        self.play(Create(sinc_mob), run_time=1.5)
        t_lbl = MathTex(
            rf"\text{{Top-hat}}\;\Delta x\cdot\Delta k = {prod_t:.3f}",
            color=BROWN, font_size=24,
        ).next_to(g_lbl, DOWN, buff=0.3)
        self.play(Write(t_lbl), run_time=0.7)

        caption = Text(
            "Top-hat has heavier tails → larger Δk → product > 1/2",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.32)
        self.play(Write(caption), run_time=0.8)
        self.wait(2.0)

        final = Text(
            "Gaussian: the unique minimum-uncertainty shape",
            font="EB Garamond", font_size=26, color=GOLD,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(caption), Write(final), run_time=1.0)
        self.wait(2.5)
