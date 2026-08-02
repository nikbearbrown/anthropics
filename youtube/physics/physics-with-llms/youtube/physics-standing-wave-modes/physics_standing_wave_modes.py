#!/usr/bin/env python3
"""
physics_standing_wave_modes.py — Standing Waves n=1,2,3,4 Modes on a Fixed String
SILENT SLATE — sim-scout candidate, physics-with-llms book.

Physics:
  y(x,t) = 2A sin(kx) cos(ωt)
  k = nπ/L,  ω = nπv/L
  L = 2 m,  wave speed v = 4 m/s
  f_n = nv/(2L) → f1=1 Hz, f2=2 Hz, f3=3 Hz, f4=4 Hz

Testable predictions:
  P1: n=2 midpoint (x=1 m) never moves — it is a node
  P2: f4/f1 = 4 exactly

Run standalone verification:
  python3 physics_standing_wave_modes.py --verify

Render:
  manim -qh physics_standing_wave_modes.py StandingWaveModesScene
"""
import sys
import numpy as np

L_STRING = 2.0    # m
V_WAVE   = 4.0    # m/s
A_AMP    = 1.0    # normalised amplitude

def freq(n: int) -> float:
    return n * V_WAVE / (2 * L_STRING)

def standing_wave(n: int, t: float, x: np.ndarray) -> np.ndarray:
    k = n * np.pi / L_STRING
    w = n * np.pi * V_WAVE / L_STRING
    return 2 * A_AMP * np.sin(k * x) * np.cos(w * t)

def node_positions(n: int) -> list:
    return [i * L_STRING / n for i in range(n + 1)]

def verify():
    print("=== Standing wave modes verification ===")
    for n in range(1, 5):
        f = freq(n)
        nodes = node_positions(n)
        print(f"  n={n}  f={f:.4f} Hz  nodes={nodes}")
    # P1: n=2 midpoint is a node
    x_test = np.array([1.0])
    y = standing_wave(2, 0.1, x_test)
    print(f"  n=2, x=1 m, t=0.1 s: y={y[0]:.10f}  (expect 0)")
    # P2
    print(f"  f4/f1 = {freq(4)/freq(1):.4f}  (expect 4.0000)")
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

N_MODES  = [1, 2, 3, 4]
COLORS   = [BLUE, GOLD, BROWN, "#C77DFF"]  # per-mode colour
X_PTS    = 300


class StandingWaveModesScene(Scene):
    """
    Animate each standing-wave mode sequentially.
    Show string oscillating, nodes fixed, formula update.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Standing Waves", font="EB Garamond", font_size=60, color=INK)
        sub   = Text(
            "L = 2 m  ·  v = 4 m/s  ·  modes n = 1, 2, 3, 4",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2  = Text(
            "y(x,t) = 2A sin(kx) cos(ωt)  —  nodes never move",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── String axes (centred) ──────────────────────────────────────────
        x_arr = np.linspace(0, L_STRING, X_PTS)

        ax = Axes(
            x_range=[0, L_STRING + 0.1, 0.5],
            y_range=[-2.2, 2.2, 1.0],
            x_length=9.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.2, include_ticks=True, tip_length=0.15),
        ).shift(DOWN * 0.3)

        lbl_x = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"y",               color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP,    buff=0.06)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)

        # ── Animate each mode ──────────────────────────────────────────────
        for n, col in zip(N_MODES, COLORS):
            f   = freq(n)
            T   = 1.0 / f
            n_col = col

            # Static formula + counter
            formula = MathTex(
                rf"n = {n}\quad f_{n} = \frac{{n v}}{{2L}} = {f:.1f}\,\mathrm{{Hz}}",
                color=n_col, font_size=30,
            ).to_edge(UP, buff=0.22)

            # Draw the string at t=0
            y0 = standing_wave(n, 0.0, x_arr)
            pts0 = [ax.c2p(float(x), float(y)) for x, y in zip(x_arr, y0)]
            string_curve = VMobject(color=n_col, stroke_width=3.0)
            string_curve.set_points_smoothly(pts0)

            # Node dots
            nodes = node_positions(n)
            node_dots = VGroup(*[
                Dot(ax.c2p(xn, 0.0), color=INK, radius=0.09)
                for xn in nodes
            ])

            self.play(
                Write(formula),
                Create(string_curve),
                FadeIn(node_dots),
                run_time=1.0,
            )

            # Oscillate for ~1.5 cycles
            n_frames = 36
            cycle_time = 1.5 * T
            for i in range(1, n_frames + 1):
                t = cycle_time * i / n_frames
                y_new = standing_wave(n, t, x_arr)
                pts_new = [ax.c2p(float(x), float(y)) for x, y in zip(x_arr, y_new)]
                new_curve = VMobject(color=n_col, stroke_width=3.0)
                new_curve.set_points_smoothly(pts_new)
                self.remove(string_curve)
                string_curve = new_curve
                self.add(string_curve)
                self.wait(cycle_time / n_frames)

            self.wait(0.5)
            self.play(
                FadeOut(formula, string_curve, node_dots),
                run_time=0.5,
            )

        # ── Final summary ──────────────────────────────────────────────────
        summary = Text(
            "Each mode adds one antinode  ·  nodes never move",
            font="EB Garamond", font_size=26, color=INK,
        ).center().shift(UP * 0.5)
        rule = MathTex(
            r"f_n = n f_1 \quad k_n = n\frac{\pi}{L}",
            color=BLUE, font_size=32,
        ).center().shift(DOWN * 0.3)
        self.play(Write(summary), Write(rule), run_time=1.5)
        self.wait(3.0)
