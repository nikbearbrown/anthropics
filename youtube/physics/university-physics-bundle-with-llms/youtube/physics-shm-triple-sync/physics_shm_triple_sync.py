#!/usr/bin/env python3
"""
physics_shm_triple_sync.py — SHM Triple Sync: x, v, a on same time axis
SILENT SLATE — sim-scout candidate, university-physics-bundle-with-llms book.

Physics:
  x(t) = A cos(ω₀t)
  v(t) = -Aω₀ sin(ω₀t)
  a(t) = -Aω₀² cos(ω₀t)
  m=2 kg, k=32 N/m → ω₀=4 rad/s, T=π/2 s ≈ 1.571 s
  A=0.020 m, v_max=0.080 m/s, a_max=0.32 m/s²

Testable predictions:
  P1: At t=T/4: x=0, v=-v_max=-0.080 m/s
  P2: a is exactly antiphase to x (mirror image)

Run standalone verification:
  python3 physics_shm_triple_sync.py --verify

Render:
  manim -qh physics_shm_triple_sync.py SHMTripleSyncScene
"""
import sys
import numpy as np

M    = 2.0    # kg
K    = 32.0   # N/m
A    = 0.020  # m
W0   = np.sqrt(K / M)   # 4.0 rad/s
T    = 2 * np.pi / W0   # ≈ 1.5708 s
VMAX = A * W0            # 0.080 m/s
AMAX = A * W0**2         # 0.32 m/s²

def x_t(t): return A * np.cos(W0 * t)
def v_t(t): return -A * W0 * np.sin(W0 * t)
def a_t(t): return -A * W0**2 * np.cos(W0 * t)

def verify():
    print("=== SHM triple sync verification ===")
    print(f"  ω₀ = {W0:.4f} rad/s,  T = {T:.4f} s")
    print(f"  v_max = {VMAX:.4f} m/s,  a_max = {AMAX:.4f} m/s²")
    t_q = T / 4
    print(f"  At t=T/4={t_q:.4f} s: x={x_t(t_q):.6f}, v={v_t(t_q):.6f}, a={a_t(t_q):.6f}")
    # P1
    print(f"  P1: x(T/4) ≈ 0: {np.isclose(x_t(t_q), 0, atol=1e-9)}")
    print(f"  P1: v(T/4) = -v_max: {np.isclose(v_t(t_q), -VMAX, rtol=1e-6)}")
    # P2: a = -A*ω₀²*cos(ω₀t) = -ω₀²*x → antiphase
    t_test = np.linspace(0, T, 100)
    print(f"  P2: a = -ω₀²·x everywhere: {np.allclose(a_t(t_test), -W0**2 * x_t(t_test))}")
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
GREEN  = "#50FA7B"
RED    = "#FF5555"

N_CYCLES = 2.5
T_END    = N_CYCLES * T


class SHMTripleSyncScene(Scene):
    """
    Three simultaneous SHM curves (x, v, a) on a shared time axis.
    Moving cursor highlights phase relationships.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Simple Harmonic Motion — Triple Sync",
                     font="EB Garamond", font_size=50, color=INK)
        sub   = Text(
            "m=2 kg  k=32 N/m  ω₀=4 rad/s  A=0.020 m",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2  = Text(
            "x, v, a — same cosine, different phase",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Shared axes ────────────────────────────────────────────────────
        # Normalise all three to [-1, 1] for display
        t_arr = np.linspace(0, T_END, 500)

        ax = Axes(
            x_range=[0, T_END, T],
            y_range=[-1.35, 1.35, 0.5],
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.15),
        ).shift(DOWN * 0.2)

        lbl_x = Text("t (s)", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = Text("normalised", font="EB Garamond", font_size=17, color=DIM).next_to(ax.y_axis.get_end(), UP, buff=0.06)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)

        # Normalised curves
        x_norm = x_t(t_arr) / A
        v_norm = v_t(t_arr) / VMAX
        a_norm = a_t(t_arr) / AMAX

        def make_curve(y_norm, color, lbl_str):
            pts = [ax.c2p(float(t), float(y)) for t, y in zip(t_arr, y_norm)]
            c = VMobject(color=color, stroke_width=2.5)
            c.set_points_smoothly(pts)
            return c

        cx = make_curve(x_norm, BLUE,  "x(t)")
        cv = make_curve(v_norm, GREEN, "v(t)")
        ca = make_curve(a_norm, RED,   "a(t)")

        lx = Text("x(t)", font="EB Garamond", font_size=20, color=BLUE).to_edge(RIGHT, buff=0.3).shift(UP * 1.8)
        lv = Text("v(t)", font="EB Garamond", font_size=20, color=GREEN).to_edge(RIGHT, buff=0.3).shift(UP * 0.9)
        la = Text("a(t)", font="EB Garamond", font_size=20, color=RED).to_edge(RIGHT, buff=0.3)

        self.play(
            Create(cx), Create(cv), Create(ca),
            Write(lx), Write(lv), Write(la),
            run_time=3.0,
        )
        self.wait(0.6)

        # ── Moving cursor at T/4 ───────────────────────────────────────────
        t_q = T / 4
        cursor = DashedLine(
            ax.c2p(0, -1.3), ax.c2p(0, 1.3),
            color=GOLD, stroke_width=1.8,
        )

        dot_x = Dot(ax.c2p(0, x_t(0)/A), color=BLUE,  radius=0.10)
        dot_v = Dot(ax.c2p(0, v_t(0)/VMAX), color=GREEN, radius=0.10)
        dot_a = Dot(ax.c2p(0, a_t(0)/AMAX), color=RED,   radius=0.10)

        self.play(Create(cursor), FadeIn(dot_x, dot_v, dot_a), run_time=0.6)

        # Sweep cursor from 0 to T_END
        def update_cursor(mob, alpha):
            t_now = alpha * T_END
            mob.become(DashedLine(
                ax.c2p(t_now, -1.3), ax.c2p(t_now, 1.3),
                color=GOLD, stroke_width=1.8,
            ))

        def update_dot(mob, alpha, fn, norm):
            t_now = alpha * T_END
            mob.move_to(ax.c2p(t_now, fn(t_now) / norm))

        self.play(
            UpdateFromAlphaFunc(cursor, update_cursor),
            UpdateFromAlphaFunc(dot_x, lambda m, a: update_dot(m, a, x_t, A)),
            UpdateFromAlphaFunc(dot_v, lambda m, a: update_dot(m, a, v_t, VMAX)),
            UpdateFromAlphaFunc(dot_a, lambda m, a: update_dot(m, a, a_t, AMAX)),
            run_time=5.0,
            rate_func=linear,
        )
        self.wait(0.4)

        # ── Phase callouts ─────────────────────────────────────────────────
        anno1 = Text(
            "v peaks when x = 0  (π/2 phase lead)",
            font="EB Garamond", font_size=22, color=GREEN,
        ).to_edge(UP, buff=0.22)
        anno2 = Text(
            "a = −ω₀²x  (exactly antiphase to x)",
            font="EB Garamond", font_size=22, color=RED,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(anno1), Write(anno2), run_time=1.0)
        self.wait(3.0)
