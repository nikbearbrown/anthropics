#!/usr/bin/env python3
"""
qm_gaussian_uncertainty.py — Gaussian Wave Packet: Minimum Uncertainty σ_x σ_p = ℏ/2
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-quantum-mechanics book.

Render:
    cd physics-plus-one-quantum-mechanics/youtube/qm-gaussian-uncertainty
    manim -qh qm_gaussian_uncertainty.py GaussianUncertaintyScene

Physics:
    ψ(x) = (2πa²)^{-1/4} exp(-x²/4a²)   σ_x = a
    φ̃(p) = (a²/2πℏ²)^{1/4} exp(-p²a²/2ℏ²) σ_p = ℏ/(2a)
    σ_x σ_p = a × ℏ/(2a) = ℏ/2  (exact minimum)
    At a = 1 nm: σ_v = σ_p/m = 5.80e4 m/s for electron
    At a = 0.1 nm: σ_v = 580 km/s
"""
import sys
import numpy as np

HBAR   = 1.055e-34
M_ELEC = 9.109e-31


def sigma_p(a):
    return HBAR / (2.0 * a)


def sigma_v(a, m=M_ELEC):
    return sigma_p(a) / m


def uncertainty_product(a):
    return a * sigma_p(a)


if __name__ == "__main__":
    print("=== Gaussian Uncertainty Verification ===")
    for a_nm in [1.0, 0.1]:
        a = a_nm * 1e-9
        sp = sigma_p(a)
        sv = sigma_v(a)
        prod = uncertainty_product(a)
        print(f"a={a_nm} nm: σ_p={sp:.3e} kg·m/s, σ_v={sv/1e3:.1f} km/s, σ_x·σ_p={prod:.4e} J·s")
        # P1: product = ℏ/2 exactly
        assert abs(prod - HBAR/2) / (HBAR/2) < 1e-10, f"P1 FAIL at a={a_nm}nm"
    print("P1: σ_x σ_p = ℏ/2 at all a ✓")
    # P2: at a=0.1nm, σ_v = 580 km/s
    sv_01 = sigma_v(0.1e-9)
    print(f"P2: a=0.1nm σ_v = {sv_01/1e3:.0f} km/s  (expect 580 km/s)")
    assert abs(sv_01 - 580e3) < 5e3, f"P2 FAIL: {sv_01/1e3:.0f}"
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


class GaussianUncertaintyScene(Scene):
    """Two-panel: position Gaussian + momentum Gaussian with slider a."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_static()
        self._phase_slider()

    def _phase_title(self):
        title = Text("Heisenberg Uncertainty Principle", font="EB Garamond",
                     font_size=50, color=INK)
        sub = MathTex(r"\sigma_x\,\sigma_p=\frac{\hbar}{2}\quad\text{(Gaussian: minimum)}",
                      color=BLUE, font_size=30)
        sub2 = Text("Tighten x → momentum spreads by the same factor",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_static(self):
        a0 = 1.0    # normalized units
        x_arr = np.linspace(-4, 4, 400)
        p_arr = np.linspace(-4, 4, 400)

        psi2_x = np.exp(-x_arr**2 / (2 * a0**2))    # ∝ |ψ|²
        psi2_p = np.exp(-p_arr**2 * a0**2 / 2)       # ∝ |φ̃|²

        ax_x = Axes(x_range=[-4, 4, 2], y_range=[0, 1.2, 0.5],
                    x_length=4.5, y_length=3.5,
                    axis_config=dict(color=INK, stroke_width=1.5,
                                     include_ticks=False, tip_length=0.18),
                    ).shift(LEFT * 3.0)
        ax_p = Axes(x_range=[-4, 4, 2], y_range=[0, 1.2, 0.5],
                    x_length=4.5, y_length=3.5,
                    axis_config=dict(color=INK, stroke_width=1.5,
                                     include_ticks=False, tip_length=0.18),
                    ).shift(RIGHT * 3.0)

        lx = MathTex(r"x\;(\sigma_0)", color=INK, font_size=20).next_to(
            ax_x.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"|\psi|^2", color=INK, font_size=20).next_to(
            ax_x.y_axis.get_end(), UP, buff=0.06)
        lp = MathTex(r"p\;(\hbar/\sigma_0)", color=INK, font_size=20).next_to(
            ax_p.x_axis.get_end(), RIGHT, buff=0.06)
        lpy = MathTex(r"|\tilde{\phi}|^2", color=INK, font_size=20).next_to(
            ax_p.y_axis.get_end(), UP, buff=0.06)

        pts_x = [ax_x.c2p(x, y) for x, y in zip(x_arr, psi2_x)]
        pts_p = [ax_p.c2p(p, y) for p, y in zip(p_arr, psi2_p)]
        curve_x = VMobject(color=BLUE, stroke_width=2.8)
        curve_x.set_points_smoothly(pts_x)
        curve_p = VMobject(color=GOLD, stroke_width=2.8)
        curve_p.set_points_smoothly(pts_p)

        sigma_x_lbl = MathTex(r"\sigma_x=a", color=BLUE, font_size=22
                               ).next_to(ax_x, DOWN, buff=0.2)
        sigma_p_lbl = MathTex(r"\sigma_p=\hbar/2a", color=GOLD, font_size=22
                               ).next_to(ax_p, DOWN, buff=0.2)
        prod_lbl = MathTex(r"\sigma_x\sigma_p=\frac{\hbar}{2}", color=INK, font_size=26
                           ).to_edge(DOWN, buff=0.25)

        hdr = Text("a = 1 (normalized units)", font="EB Garamond",
                   font_size=22, color=INK).to_edge(UP, buff=0.22)
        self.play(Create(ax_x), Create(ax_p), Write(lx), Write(ly),
                  Write(lp), Write(lpy), Write(hdr), run_time=1.5)
        self.play(Create(curve_x), Create(curve_p), run_time=1.5)
        self.play(Write(sigma_x_lbl), Write(sigma_p_lbl), Write(prod_lbl), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(hdr, curve_x, curve_p, sigma_x_lbl, sigma_p_lbl,
                          prod_lbl, ax_x, ax_p, lx, ly, lp, lpy), run_time=0.5)

    def _phase_slider(self):
        a_track = ValueTracker(2.0)

        ax_x = Axes(x_range=[-6, 6, 2], y_range=[0, 1.2, 0.5],
                    x_length=4.5, y_length=3.5,
                    axis_config=dict(color=INK, stroke_width=1.5,
                                     include_ticks=False, tip_length=0.18),
                    ).shift(LEFT * 3.0)
        ax_p = Axes(x_range=[-6, 6, 2], y_range=[0, 1.2, 0.5],
                    x_length=4.5, y_length=3.5,
                    axis_config=dict(color=INK, stroke_width=1.5,
                                     include_ticks=False, tip_length=0.18),
                    ).shift(RIGHT * 3.0)
        self.add(ax_x, ax_p)

        def _cx():
            a = a_track.get_value()
            x_arr = np.linspace(-6, 6, 300)
            y = np.exp(-x_arr**2 / (2 * a**2))
            pts = [ax_x.c2p(x, yy) for x, yy in zip(x_arr, y)]
            m = VMobject(color=BLUE, stroke_width=2.8)
            m.set_points_smoothly(pts)
            return m

        def _cp():
            a = a_track.get_value()
            sp = 1.0 / (2 * a)    # σ_p in normalized units
            p_arr = np.linspace(-6, 6, 300)
            y = np.exp(-p_arr**2 / (2 * sp**2))
            pts = [ax_p.c2p(p, yy) for p, yy in zip(p_arr, y)]
            m = VMobject(color=GOLD, stroke_width=2.8)
            m.set_points_smoothly(pts)
            return m

        dyn_cx = always_redraw(_cx)
        dyn_cp = always_redraw(_cp)
        self.add(dyn_cx, dyn_cp)

        a_lbl = MathTex(r"a = ", color=DIM, font_size=30)
        a_num = DecimalNumber(2.0, num_decimal_places=2, color=DIM, font_size=30)
        a_num.add_updater(lambda m: m.set_value(a_track.get_value()))
        a_row = VGroup(a_lbl, a_num).arrange(RIGHT, buff=0.08).to_edge(DOWN, buff=0.28)

        prod_lbl = MathTex(r"\sigma_x\sigma_p=\hbar/2\;\text{always}",
                           color=INK, font_size=24).next_to(a_row, UP, buff=0.15)

        hdr = Text("Narrow x → wide p — same factor, inverse",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.18)
        self.play(Write(hdr), FadeIn(a_row), Write(prod_lbl), run_time=0.8)
        self.play(a_track.animate.set_value(0.3), run_time=4.0, rate_func=smooth)
        self.wait(1.0)
        self.play(a_track.animate.set_value(3.0), run_time=4.0, rate_func=smooth)
        self.wait(1.5)
        final = Text("The Gaussian is the only state that saturates σ_xσ_p = ℏ/2",
                     font="EB Garamond", font_size=22, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(a_row, prod_lbl), Write(final), run_time=1.2)
        self.wait(2.5)
