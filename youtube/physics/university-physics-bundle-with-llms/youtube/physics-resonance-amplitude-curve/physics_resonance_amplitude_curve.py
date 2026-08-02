#!/usr/bin/env python3
"""
physics_resonance_amplitude_curve.py — Resonance Amplitude A(ω_d) Curve
SILENT SLATE — sim-scout candidate, university-physics-bundle-with-llms book.

Physics:
  A(ω_d) = F₀/m / √((ω₀²-ω_d²)² + (bω_d/m)²)
  m=1 kg, k=16 N/m → ω₀=4 rad/s, F₀=1 N
  Low damping:  b=0.5 → A_max = F₀/(bω₀) = 0.5 m,   Q=8
  High damping: b=2.0 → A_max = F₀/(bω₀) = 0.125 m, Q=2

Testable predictions:
  P1: At ω_d=ω₀=4, b=0.5: A=0.500 m; at ω_d=2, A≈0.124 m
  P2: Half-power bandwidth Δω=b/m=0.5 rad/s; crossing at 3.75 and 4.25

Run standalone verification:
  python3 physics_resonance_amplitude_curve.py --verify

Render:
  manim -qh physics_resonance_amplitude_curve.py ResonanceAmplitudeCurveScene
"""
import sys
import numpy as np

M  = 1.0    # kg
K  = 16.0   # N/m
W0 = 4.0    # rad/s
F0 = 1.0    # N

def amplitude(wd, b):
    denom = np.sqrt((W0**2 - wd**2)**2 + (b * wd / M)**2)
    return (F0 / M) / denom

def Q_factor(b):
    return M * W0 / b

def verify():
    print("=== Resonance amplitude verification ===")
    for b, name in [(0.5, "low"), (2.0, "high")]:
        A_res = amplitude(W0, b)
        A_max_theory = F0 / (b * W0)
        Q = Q_factor(b)
        print(f"  b={b} ({name}): A(ω₀)={A_res:.4f} m, A_max_theory={A_max_theory:.4f} m, Q={Q:.2f}")
    # P1
    A_2 = amplitude(2.0, 0.5)
    print(f"  P1: A(ω_d=2, b=0.5) = {A_2:.4f} m  (expect ≈0.124)")
    # P2: half-power bandwidth
    A_half = amplitude(W0, 0.5) / np.sqrt(2)
    w_arr = np.linspace(3.5, 4.5, 1000)
    crossings = np.where(np.diff(np.sign(amplitude(w_arr, 0.5) - A_half)))[0]
    w_cross = [w_arr[i] for i in crossings]
    print(f"  P2: Half-power crossings at ω ≈ {w_cross}  (expect 3.75, 4.25)")
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

WD_MAX = 12.0   # rad/s sweep range
B_LOW  = 0.5
B_HIGH = 2.0


class ResonanceAmplitudeCurveScene(Scene):
    """
    Two resonance curves (low and high damping) tracing across ω axis.
    Peak markers, Q labels, bandwidth annotation.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Resonance Amplitude Curve",
                     font="EB Garamond", font_size=54, color=INK)
        sub   = Text(
            "m=1 kg  k=16 N/m  ω₀=4 rad/s  F₀=1 N",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2  = Text(
            "A(ωd) = F₀/m / √((ω₀²-ωd²)² + (bωd/m)²)",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Axes ───────────────────────────────────────────────────────────
        ax = Axes(
            x_range=[0, WD_MAX, 2.0],
            y_range=[0, 0.65, 0.1],
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.15),
        ).shift(DOWN * 0.2)

        lbl_x = MathTex(r"\omega_d\;(\mathrm{rad/s})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"A\;(\mathrm{m})",            color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP,    buff=0.08)
        # Mark ω₀ on x axis
        wd0_mark = DashedLine(ax.c2p(W0, 0), ax.c2p(W0, 0.62), color=DIM, stroke_width=1.2)
        wd0_lbl  = MathTex(r"\omega_0=4", color=DIM, font_size=20).next_to(ax.c2p(W0, 0), DOWN, buff=0.1)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Create(wd0_mark), Write(wd0_lbl), run_time=1.2)

        wd_arr = np.linspace(0.01, WD_MAX, 800)

        def make_curve(b, color, lw=2.5):
            A_arr = amplitude(wd_arr, b)
            pts   = [ax.c2p(float(w), float(a)) for w, a in zip(wd_arr, A_arr)]
            c = VMobject(color=color, stroke_width=lw)
            c.set_points_smoothly(pts)
            return c

        # Low damping (sharp peak)
        c_low = make_curve(B_LOW, BLUE)
        self.play(Create(c_low), run_time=2.5)

        # Peak marker
        A_peak_low = amplitude(W0, B_LOW)
        dot_low = Dot(ax.c2p(W0, A_peak_low), color=BLUE, radius=0.10)
        lbl_low = MathTex(
            rf"Q={Q_factor(B_LOW):.0f}\quad A_{{max}}={A_peak_low:.3f}\,\mathrm{{m}}",
            color=BLUE, font_size=22,
        ).next_to(dot_low, UP + RIGHT, buff=0.1)
        self.play(FadeIn(dot_low, scale=1.5), Write(lbl_low), run_time=0.9)
        self.wait(0.5)

        # High damping (broad peak)
        c_high = make_curve(B_HIGH, BROWN, lw=2.0)
        self.play(Create(c_high), run_time=2.0)

        A_peak_high = amplitude(W0, B_HIGH)
        dot_high = Dot(ax.c2p(W0, A_peak_high), color=BROWN, radius=0.10)
        lbl_high = MathTex(
            rf"Q={Q_factor(B_HIGH):.0f}\quad A_{{max}}={A_peak_high:.3f}\,\mathrm{{m}}",
            color=BROWN, font_size=22,
        ).next_to(dot_high, RIGHT, buff=0.12)
        self.play(FadeIn(dot_high, scale=1.5), Write(lbl_high), run_time=0.9)
        self.wait(0.6)

        # ── Half-power bandwidth for low damping ───────────────────────────
        A_half = A_peak_low / np.sqrt(2)
        bw_line = DashedLine(
            ax.c2p(W0 - 0.25, A_half),
            ax.c2p(W0 + 0.25, A_half),
            color=GOLD, stroke_width=1.5,
        )
        bw_lbl = MathTex(
            r"\Delta\omega = b/m = 0.5\,\mathrm{rad/s}",
            color=GOLD, font_size=20,
        ).next_to(bw_line, RIGHT, buff=0.1)
        self.play(Create(bw_line), Write(bw_lbl), run_time=0.9)
        self.wait(0.7)

        # ── Key equation ───────────────────────────────────────────────────
        eq = MathTex(
            r"A_{\max} = \frac{F_0}{b\omega_0}\;\;\;\;Q = \frac{m\omega_0}{b}",
            color=INK, font_size=28,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.0)
        self.wait(3.0)
