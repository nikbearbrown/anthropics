#!/usr/bin/env python3
"""
modern_time_dilation.py — Time Dilation: The Light Clock and the Pythagorean Derivation
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-modern-physics book.

Render:
    cd physics-plus-one-modern-physics/youtube/modern-time-dilation
    manim -qh modern_time_dilation.py TimeDilationScene

Physics:
    γ = 1/sqrt(1 - v²/c²)
    Muon: v = 0.9994c → γ = 28.87, Δt = 63.5 μs (rest = 2.2 μs)
    Classical prediction: d = 0.9994c × 2.2 μs = 659 m ≈ 0.66 km
    Relativistic: d = 0.9994c × 63.5 μs ≈ 19 km (survives to sea level)
"""
import sys
import numpy as np

C_LIGHT = 3.0e8    # m/s


def gamma(beta):
    return 1.0 / np.sqrt(1.0 - beta**2)


MUON_BETA   = 0.9994
MUON_TAU0   = 2.2e-6      # s  (rest lifetime)
MUON_GAMMA  = gamma(MUON_BETA)
MUON_DT     = MUON_GAMMA * MUON_TAU0
MUON_D_REL  = MUON_BETA * C_LIGHT * MUON_DT
MUON_D_CLAS = MUON_BETA * C_LIGHT * MUON_TAU0


if __name__ == "__main__":
    print("=== Time Dilation Verification ===")
    print(f"γ(0.9994) = {MUON_GAMMA:.2f}  (expect 28.9)")
    print(f"Δt dilated = {MUON_DT*1e6:.1f} μs  (expect 63.5 μs)")
    print(f"Relativistic distance = {MUON_D_REL/1e3:.1f} km  (expect ~19 km)")
    print(f"Classical distance = {MUON_D_CLAS/1e3:.2f} km  (expect 0.66 km)")
    # P1: γ check
    assert abs(MUON_GAMMA - 28.9) < 0.5, f"P1 FAIL: γ={MUON_GAMMA:.2f}"
    # P2: at v=0, γ=1
    assert abs(gamma(0.0) - 1.0) < 1e-10, "P2 FAIL"
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


class TimeDilationScene(Scene):
    """Light clock derivation + muon example + γ curve."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_light_clock()
        self._phase_derivation()
        self._phase_muon()
        self._phase_gamma_curve()

    def _phase_title(self):
        title = Text("Time Dilation", font="EB Garamond", font_size=60, color=INK)
        sub = Text("A light clock moving at v runs slower — by exactly γ",
                   font="EB Garamond", font_size=23, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_light_clock(self):
        # Left: stationary clock
        L = 2.0
        lx = LEFT * 3.5
        mirror_bot = Dot(lx + DOWN * L / 2, color=BLUE, radius=0.12)
        mirror_top = Dot(lx + UP   * L / 2, color=BLUE, radius=0.12)
        photon     = Dot(lx + DOWN * L / 2, color=GOLD, radius=0.1)
        clock_lbl  = Text("Stationary", font="EB Garamond",
                          font_size=19, color=DIM).next_to(lx + DOWN * L / 2, DOWN, buff=0.2)
        L_lbl = MathTex(r"L", color=DIM, font_size=22).next_to(lx, LEFT, buff=0.2)

        # Right: moving clock
        rx = RIGHT * 2.5
        mirror_bot_m = Dot(rx + DOWN * L / 2, color=BLUE, radius=0.12)
        mirror_top_m = Dot(rx + UP   * L / 2, color=BLUE, radius=0.12)
        clock_lbl_m  = Text("Moving at v", font="EB Garamond",
                             font_size=19, color=DIM).next_to(rx + DOWN * L / 2, DOWN, buff=0.2)

        # Pythagorean triangle on right
        tri_base = rx + DOWN * L / 2 + RIGHT * 1.2
        tri_top  = rx + UP   * L / 2
        tri_hyp  = rx + DOWN * L / 2

        hdr = Text("The Light Clock", font="EB Garamond",
                   font_size=24, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.5)
        self.play(
            FadeIn(mirror_bot, mirror_top, clock_lbl, L_lbl),
            FadeIn(mirror_bot_m, mirror_top_m, clock_lbl_m),
            run_time=1.0)
        self.play(FadeIn(photon), run_time=0.3)
        # Bounce stationary photon
        for _ in range(2):
            self.play(photon.animate.move_to(lx + UP   * L / 2), run_time=0.5)
            self.play(photon.animate.move_to(lx + DOWN * L / 2), run_time=0.5)

        # Draw diagonal on moving clock
        diag = Line(tri_hyp, tri_top, color=GOLD, stroke_width=2.5)
        horiz = DashedLine(tri_hyp, tri_base, color=BROWN, stroke_width=1.8)
        vert  = Line(tri_base, tri_top, color=BLUE, stroke_width=2.0)
        vleg_lbl  = MathTex(r"L=c\Delta t_0/2", color=BLUE, font_size=17).next_to(
            tri_base, RIGHT, buff=0.08)
        hleg_lbl  = MathTex(r"v\Delta t/2",     color=BROWN, font_size=17).next_to(
            (tri_hyp + tri_base) / 2, DOWN, buff=0.08)
        hyp_lbl   = MathTex(r"c\Delta t/2",     color=GOLD, font_size=17).next_to(
            (tri_hyp + tri_top) / 2, LEFT, buff=0.08)

        self.play(Create(diag), Create(horiz), Create(vert), run_time=1.2)
        self.play(Write(vleg_lbl), Write(hleg_lbl), Write(hyp_lbl), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(hdr, mirror_bot, mirror_top, photon, clock_lbl, L_lbl,
                          mirror_bot_m, mirror_top_m, clock_lbl_m,
                          diag, horiz, vert, vleg_lbl, hleg_lbl, hyp_lbl), run_time=0.5)

    def _phase_derivation(self):
        steps = [
            MathTex(r"(c\tfrac{\Delta t}{2})^2=(v\tfrac{\Delta t}{2})^2+(L)^2",
                    color=BLUE, font_size=30),
            MathTex(r"L=\frac{c\,\Delta t_0}{2}\;\Rightarrow\;"
                    r"c^2\Delta t^2=v^2\Delta t^2+c^2\Delta t_0^2",
                    color=GOLD, font_size=28),
            MathTex(r"\Delta t=\frac{\Delta t_0}{\sqrt{1-v^2/c^2}}=\gamma\,\Delta t_0",
                    color=INK, font_size=36),
        ]
        VGroup(*steps).arrange(DOWN, buff=0.55).center()
        for step in steps:
            self.play(Write(step), run_time=1.1)
            self.wait(0.6)
        self.wait(1.5)
        self.play(FadeOut(*steps), run_time=0.5)

    def _phase_muon(self):
        hdr = Text("Muon: v = 0.9994c, rest lifetime 2.2 μs",
                   font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.22)

        rows = [
            MathTex(r"\gamma=\frac{1}{\sqrt{1-0.9994^2}}=28.9",
                    color=BLUE, font_size=30),
            MathTex(r"\Delta t=28.9\times2.2\,\mu\mathrm{s}=63.5\,\mu\mathrm{s}",
                    color=GOLD, font_size=30),
            MathTex(r"d_{\rm rel}=0.9994c\times63.5\,\mu\mathrm{s}\approx19\,\mathrm{km}\;\checkmark",
                    color=INK, font_size=28),
            MathTex(r"d_{\rm classical}=0.9994c\times2.2\,\mu\mathrm{s}\approx0.66\,\mathrm{km}\;\times",
                    color=BROWN, font_size=26),
        ]
        VGroup(*rows).arrange(DOWN, buff=0.42).center()
        self.play(Write(hdr), run_time=0.5)
        for r in rows:
            self.play(Write(r), run_time=0.9)
            self.wait(0.4)
        self.wait(2.0)
        self.play(FadeOut(hdr, *rows), run_time=0.5)

    def _phase_gamma_curve(self):
        ax = Axes(
            x_range=[0, 1.0, 0.2],
            y_range=[1, 12, 2],
            x_length=8.5,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3)
        x_lbl = MathTex(r"\beta = v/c", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"\gamma", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.2)

        beta = np.linspace(0, 0.995, 600)
        gam  = gamma(beta)
        gam_c = np.clip(gam, 1, 11.5)
        pts = [ax.c2p(b, g) for b, g in zip(beta, gam_c)]
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)

        # Muon point
        muon_pt = Dot(ax.c2p(MUON_BETA, min(MUON_GAMMA, 11.5)), color=GOLD, radius=0.12)
        muon_lbl = Text("Muon  γ = 28.9", font="EB Garamond",
                        font_size=18, color=GOLD).next_to(muon_pt, UP, buff=0.08)

        # γ = 1 dashed line
        newtonian = DashedLine(ax.c2p(0, 1), ax.c2p(0.995, 1),
                               color=DIM, stroke_width=1.2)
        newton_lbl = MathTex(r"\gamma=1\;\text{(Newtonian)}", color=DIM, font_size=18
                              ).next_to(ax.c2p(0.5, 1), DOWN, buff=0.1)

        self.play(Create(curve), run_time=2.5)
        self.play(Create(newtonian), Write(newton_lbl), run_time=0.8)
        self.play(FadeIn(muon_pt), Write(muon_lbl), run_time=0.8)
        asym = Text("v → c  →  γ → ∞  →  infinite energy required",
                    font="EB Garamond", font_size=22, color=INK).to_edge(DOWN, buff=0.28)
        self.play(Write(asym), run_time=1.0)
        self.wait(2.5)
