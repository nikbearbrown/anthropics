#!/usr/bin/env python3
"""
physics_damped_oscillator_regimes.py — Damped Oscillator: Under/Critical/Overdamped
SILENT SLATE — sim-scout candidate, university-physics-bundle-with-llms book.

Physics:
  x'' + 2γx' + ω₀²x = 0
  m=1 kg, k=16 N/m → ω₀=4 rad/s
  Underdamped:  b=2 N·s/m → γ=1,  ω=√15≈3.873 rad/s,  τ=1 s
  Critically:   b=8 N·s/m → γ=4=ω₀  (b_c=2√(mk)=8)
  Overdamped:   b=16 N·s/m → γ=8 > ω₀

Testable predictions:
  P1: Underdamped amplitude at t=1 s is e⁻¹ ≈ 0.368 A₀
  P2: Critically damped reaches equilibrium fastest

Run standalone verification:
  python3 physics_damped_oscillator_regimes.py --verify

Render:
  manim -qh physics_damped_oscillator_regimes.py DampedOscillatorRegimesScene
"""
import sys
import numpy as np

M  = 1.0    # kg
K  = 16.0   # N/m
W0 = 4.0    # rad/s (= √(K/M))
A0 = 1.0    # initial displacement

# Damping coefficients for three regimes
B_UNDER = 2.0   # underdamped
B_CRIT  = 8.0   # critically damped (b_c = 2√(mk) = 2×4 = 8)
B_OVER  = 16.0  # overdamped

def gamma(b): return b / (2 * M)

def x_underdamped(t, b=B_UNDER):
    gam = gamma(b)
    wd  = np.sqrt(max(W0**2 - gam**2, 1e-20))
    return A0 * np.exp(-gam * t) * np.cos(wd * t)

def x_critical(t, b=B_CRIT):
    gam = gamma(b)
    return A0 * (1 + gam * t) * np.exp(-gam * t)

def x_overdamped(t, b=B_OVER):
    gam = gamma(b)
    r1  = -gam + np.sqrt(gam**2 - W0**2)
    r2  = -gam - np.sqrt(gam**2 - W0**2)
    # ICs: x(0)=A0, v(0)=0 → coefficients
    C2  = (r1 * A0) / (r1 - r2)
    C1  = A0 - C2
    return C1 * np.exp(r1 * t) + C2 * np.exp(r2 * t)

def verify():
    print("=== Damped oscillator verification ===")
    print(f"  ω₀={W0}, b_c={B_CRIT}, γ_c={gamma(B_CRIT)}")
    t_arr = np.linspace(0, 5, 1000)
    # P1: underdamped at t=1 s
    x1 = x_underdamped(1.0)
    print(f"  P1: x_under(t=1) = {x1:.6f}  (expect A₀/e = {A0/np.e:.6f})")
    print(f"  P1 passes: {np.isclose(x1, A0*np.exp(-gamma(B_UNDER)*1.0)*np.cos(np.sqrt(W0**2-gamma(B_UNDER)**2)))}")
    # P2: which regime returns to x=0.01 first?
    threshold = 0.01
    for name, fn in [("under", x_underdamped), ("crit", x_critical), ("over", x_overdamped)]:
        idx = np.argmax(np.abs(fn(t_arr)) < threshold)
        print(f"  {name} first crosses x<0.01 at t≈{t_arr[idx]:.3f} s")
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

T_MAX = 5.0


class DampedOscillatorRegimesScene(Scene):
    """
    Three regimes on one plot. Envelope for underdamped. Side annotations.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Damped Oscillator — Three Regimes",
                     font="EB Garamond", font_size=52, color=INK)
        sub   = Text(
            "m=1 kg  k=16 N/m  ω₀=4 rad/s",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2  = Text(
            "x'' + 2γx' + ω₀²x = 0  —  one equation, three futures",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Axes ───────────────────────────────────────────────────────────
        ax = Axes(
            x_range=[0, T_MAX, 1.0],
            y_range=[-1.1, 1.2, 0.5],
            x_length=10.0,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.15),
        ).shift(DOWN * 0.3)

        lbl_x = Text("t (s)",     font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"x(t)", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)

        t_arr = np.linspace(0, T_MAX, 600)

        def make_curve(fn, color, lw=2.5):
            pts = [ax.c2p(float(t), float(fn(t))) for t in t_arr]
            c = VMobject(color=color, stroke_width=lw)
            c.set_points_smoothly(pts)
            return c

        # Envelope for underdamped
        env_pos = A0 * np.exp(-gamma(B_UNDER) * t_arr)
        env_neg = -env_pos
        env_pts_pos = [ax.c2p(float(t), float(e)) for t, e in zip(t_arr, env_pos)]
        env_pts_neg = [ax.c2p(float(t), float(e)) for t, e in zip(t_arr, env_neg)]
        env_p = VMobject(color=BLUE, stroke_width=1.2, stroke_opacity=0.5)
        env_p.set_points_smoothly(env_pts_pos)
        env_n = VMobject(color=BLUE, stroke_width=1.2, stroke_opacity=0.5)
        env_n.set_points_smoothly(env_pts_neg)

        c_under = make_curve(x_underdamped, BLUE)
        c_crit  = make_curve(x_critical,    GOLD, lw=3.0)
        c_over  = make_curve(x_overdamped,  BROWN)

        # Color-coded b-values only — purely numeric MathTex, no text modes
        lbl_u = MathTex(r"b=2",  font_size=26, color=BLUE).move_to(ax.c2p(0.4, 0.9))
        lbl_c = MathTex(r"b_c",  font_size=26, color=GOLD).move_to(ax.c2p(1.0, 0.68))
        lbl_o = MathTex(r"b=16", font_size=26, color=BROWN).move_to(ax.c2p(2.5, 0.55))

        self.play(
            Create(env_p), Create(env_n),
            Create(c_under), Write(lbl_u),
            run_time=2.0,
        )
        self.wait(0.4)
        self.play(Create(c_crit), Write(lbl_c), run_time=1.5)
        self.wait(0.4)
        self.play(Create(c_over), Write(lbl_o), run_time=1.5)
        self.wait(0.5)

        # ── e-folding annotation ───────────────────────────────────────────
        t_tau = 1.0  # τ=1 s for underdamped
        dot_env = Dot(ax.c2p(t_tau, np.exp(-1)), color=BLUE, radius=0.10)
        arr_env = Arrow(
            ax.c2p(t_tau + 0.4, np.exp(-1) + 0.2),
            ax.c2p(t_tau, np.exp(-1)),
            color=INK, stroke_width=1.5, tip_length=0.15,
        )
        env_lbl = MathTex(r"A_0 e^{-1}\;\mathrm{at}\;t=\tau=1\,\mathrm{s}",
                          color=BLUE, font_size=20)
        env_lbl.next_to(arr_env.get_start(), RIGHT, buff=0.05)

        self.play(FadeIn(dot_env), GrowArrow(arr_env), Write(env_lbl), run_time=1.0)
        self.wait(0.8)

        # ── Critical damping rule ──────────────────────────────────────────
        rule = Text(
            "Critical damping: fastest return without oscillation  b_c = 2√(mk) = 8",
            font="EB Garamond", font_size=20, color=GOLD,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(rule), run_time=1.0)
        self.wait(3.0)
