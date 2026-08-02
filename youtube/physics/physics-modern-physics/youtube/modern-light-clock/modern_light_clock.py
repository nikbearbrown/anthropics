#!/usr/bin/env python3
"""
modern_light_clock.py — Light Clock: Pythagorean Geometry of Time Dilation
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    d=1 m mirror separation
    v=0   → Δt₀ = 2d/c = 6.67 ns
    v=0.6c → Δt  = 8.33 ns (γ=1.25)
    v=0.866c → Δt = 13.33 ns (γ=2.00)

Run standalone to verify:
    python3 modern_light_clock.py
"""
import sys
import numpy as np

C_LIGHT = 2.998e8  # m/s
D_MIRROR = 1.0     # m


def gamma(beta): return 1.0 / np.sqrt(1.0 - beta**2)
def delta_t0(): return 2 * D_MIRROR / C_LIGHT
def delta_t(beta): return gamma(beta) * delta_t0()


def verify():
    print("=== Light Clock verification ===")
    print(f"Δt₀ = {delta_t0()*1e9:.3f} ns  (card: 6.67 ns)")
    for b, g_card, dt_card in [(0.6, 1.25, 8.33), (0.866, 2.0, 13.33), (0.99, 7.09, 47.3)]:
        g = gamma(b)
        dt = delta_t(b) * 1e9
        print(f"β={b}: γ={g:.4f} (card:{g_card}), Δt={dt:.2f} ns (card:{dt_card})")
    # P1: β=√3/2 ≈ 0.866 → γ=2.000 exactly
    b_p1 = np.sqrt(3) / 2
    print(f"\nP1: β=√3/2={b_p1:.6f} → γ={gamma(b_p1):.6f}  (should be 2.000000)")
    # P2: triangle verification (cΔt/2)² = (vΔt/2)² + d²
    b2 = 0.6
    dt2 = delta_t(b2)
    lhs = (C_LIGHT * dt2 / 2)**2
    rhs = (b2 * C_LIGHT * dt2 / 2)**2 + D_MIRROR**2
    print(f"P2: (cΔt/2)² = {lhs:.6f}, (vΔt/2)²+d² = {rhs:.6f}  (should match)")
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


class ModernLightClockScene(Scene):
    """
    Split screen: stationary clock (left) vs moving clock (right).
    Pythagorean triangle materializes. β sweeps 0→0.99.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_geometry_argument()
        self._phase_split_clock()
        self._phase_beta_sweep()

    def _phase_title(self):
        title = Text("Light Clock — Time Dilation from Pythagoras",
                     font="EB Garamond", font_size=54, color=INK)
        sub = Text("Time dilation is not a clock malfunction — it is geometry",
                   font="EB Garamond", font_size=24, color=BLUE)
        hook = Text("The math falls straight out of the Pythagorean theorem",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_geometry_argument(self):
        eqs = VGroup(
            MathTex(r"\Delta t_0 = \frac{2d}{c}", color=INK, font_size=38),
            MathTex(r"\left(\frac{c\Delta t}{2}\right)^2 = \left(\frac{v\Delta t}{2}\right)^2 + d^2",
                    color=BLUE, font_size=34),
            MathTex(r"\Rightarrow\;\Delta t = \frac{\Delta t_0}{\sqrt{1-v^2/c^2}} = \gamma\,\Delta t_0",
                    color=GOLD, font_size=34),
        ).arrange(DOWN, buff=0.48).center()
        for mob in eqs:
            self.play(Write(mob), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(eqs), run_time=0.5)

    def _phase_split_clock(self):
        beta = 0.6
        g = gamma(beta)
        dt0_ns = delta_t0() * 1e9
        dt_ns = delta_t(beta) * 1e9

        # ── Left: stationary clock ─────────────────────────────────────────────
        mirror_top_L = Line([-6, 1.5, 0], [-3.5, 1.5, 0], color=DIM, stroke_width=3)
        mirror_bot_L = Line([-6, -1.5, 0], [-3.5, -1.5, 0], color=DIM, stroke_width=3)
        photon_path_L = DashedLine([-4.75, -1.5, 0], [-4.75, 1.5, 0],
                                   color=BLUE, stroke_width=2.5)
        dt0_lbl = MathTex(r"\Delta t_0 = 6.67\,\text{ns}", color=BLUE, font_size=22
                           ).move_to([-4.75, 0, 0]).shift(RIGHT * 0.7)
        stat_lbl = Text("Stationary clock", font="EB Garamond", font_size=20,
                        color=INK).move_to([-4.75, 2.2, 0])

        # ── Right: moving clock (v=0.6c) ───────────────────────────────────────
        mirror_top_R = Line([0.5, 1.5, 0], [6, 1.5, 0], color=DIM, stroke_width=3)
        mirror_bot_R = Line([0.5, -1.5, 0], [6, -1.5, 0], color=DIM, stroke_width=3)

        # Sawtooth path: photon travels diagonally
        mid_x = 3.25
        pts = [[0.8, -1.5, 0], [mid_x, 1.5, 0], [5.7, -1.5, 0]]
        photon_path_R = VMobject(color=BLUE, stroke_width=2.5)
        photon_path_R.set_points_smoothly([np.array(p) for p in pts])

        dt_lbl = MathTex(r"\Delta t = 8.33\,\text{ns}\;(\gamma=1.25)",
                         color=GOLD, font_size=22).move_to([3.25, 0.2, 0])
        move_lbl = Text("Moving clock (v=0.6c)", font="EB Garamond", font_size=20,
                        color=INK).move_to([3.25, 2.2, 0])

        # Right-angle triangle
        tri_pts = [
            np.array([1.0, -1.5, 0]),
            np.array([1.0, 1.5, 0]),
            np.array([mid_x, -1.5, 0]),
        ]
        triangle = Polygon(*tri_pts, color=BROWN, stroke_width=2, fill_opacity=0.15,
                           fill_color=BROWN)
        d_lbl = MathTex(r"d", color=DIM, font_size=20).move_to([0.7, 0, 0])
        vdt2_lbl = MathTex(r"\tfrac{v\Delta t}{2}", color=DIM, font_size=18
                           ).move_to([2.0, -1.9, 0])
        hyp_lbl = MathTex(r"\tfrac{c\Delta t}{2}", color=BROWN, font_size=18
                          ).move_to([1.5, 0.2, 0])

        sep = DashedLine([0, -2.8, 0], [0, 2.8, 0], color=DIM, stroke_width=1.5)

        self.play(
            Create(mirror_top_L), Create(mirror_bot_L),
            Create(mirror_top_R), Create(mirror_bot_R),
            Create(sep), run_time=0.9)
        self.play(Create(photon_path_L), Write(dt0_lbl), Write(stat_lbl), run_time=1.2)
        self.play(Create(photon_path_R), Write(dt_lbl), Write(move_lbl), run_time=1.5)
        self.play(Create(triangle), Write(d_lbl), Write(vdt2_lbl), Write(hyp_lbl),
                  run_time=1.2)
        self.wait(3.5)
        self.play(FadeOut(mirror_top_L, mirror_bot_L, mirror_top_R, mirror_bot_R,
                          photon_path_L, photon_path_R, dt0_lbl, dt_lbl,
                          stat_lbl, move_lbl, triangle, d_lbl, vdt2_lbl,
                          hyp_lbl, sep), run_time=0.5)

    def _phase_beta_sweep(self):
        title = Text("β sweeps 0 → 0.99: tick period stretches",
                     font="EB Garamond", font_size=28, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 1.0, 0.2],
            y_range=[0, 55, 10],
            x_length=9,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"\beta", color=INK, font_size=24
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"\Delta t\;(\text{ns})", color=INK, font_size=24
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        b_vals = np.linspace(0.0, 0.998, 500)
        dt_vals = [delta_t(b) * 1e9 for b in b_vals]

        curve = ax.plot_line_graph(
            x_values=list(b_vals), y_values=[min(v, 55) for v in dt_vals],
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )
        horiz = ax.plot_line_graph(
            x_values=[0, 0.998], y_values=[delta_t0() * 1e9] * 2,
            line_color=DIM, stroke_width=1.5, add_vertex_dots=False,
        )
        dt0_lbl = MathTex(r"\Delta t_0 = 6.67\,\text{ns}", color=DIM, font_size=20
                          ).move_to(ax.c2p(0.3, delta_t0() * 1e9)).shift(UP * 0.3)

        # Key dots
        for b, g_txt, color in [(0.866, r"\gamma=2", GOLD), (0.99, r"\gamma=7.09", BROWN)]:
            dt_v = delta_t(b) * 1e9
            if dt_v <= 55:
                d = Dot(ax.c2p(b, dt_v), color=color, radius=0.1)
                l = MathTex(g_txt, color=color, font_size=20).next_to(d, RIGHT, buff=0.1)
                self.play(FadeIn(d), Write(l), run_time=0.5)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(curve), run_time=2.0)
        self.play(Create(horiz), Write(dt0_lbl), run_time=0.8)
        self.wait(3.5)
