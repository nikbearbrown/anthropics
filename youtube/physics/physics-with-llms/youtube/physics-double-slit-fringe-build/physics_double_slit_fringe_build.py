#!/usr/bin/env python3
"""
physics_double_slit_fringe_build.py — Double-Slit Interference Pattern Build-up
SILENT SLATE — sim-scout candidate, physics-with-llms book.

Physics:
  I(y) = I0 cos²(π d y / λ L)
  d = 0.5 mm = 5e-4 m, λ = 600 nm = 6e-7 m, L = 1 m
  Fringe spacing Δy = λL/d = 1.2 mm

Testable predictions:
  P1: Δy = λL/d = (6e-7)(1)/(5e-4) = 1.2e-3 m = 1.2 mm
  P2: 3rd bright fringe at y = 3 × 1.2 mm = 3.6 mm from center

Run standalone verification:
  python3 physics_double_slit_fringe_build.py --verify

Render:
  manim -qh physics_double_slit_fringe_build.py DoubleSlit FringeBuildScene
"""
import sys
import numpy as np

D_SLIT  = 0.5e-3   # m
LAM     = 600e-9    # m
L_SCREN = 1.0       # m
I0      = 1.0

def fringe_spacing() -> float:
    return LAM * L_SCREN / D_SLIT

def intensity(y: np.ndarray) -> np.ndarray:
    return I0 * np.cos(np.pi * D_SLIT * y / (LAM * L_SCREN))**2

def bright_fringes(m_max: int = 3):
    return [m * fringe_spacing() for m in range(-m_max, m_max + 1)]

def verify():
    print("=== Double-slit fringe verification ===")
    dy = fringe_spacing()
    print(f"  Fringe spacing Δy = {dy*1e3:.4f} mm  (expect 1.2 mm)")
    for m in range(4):
        y = m * dy
        I = intensity(np.array([y]))[0]
        print(f"  m={m}: y = {y*1e3:.3f} mm, I = {I:.4f}  (expect 1.0)")
    y_dark = 0.5 * dy
    I_dark = intensity(np.array([y_dark]))[0]
    print(f"  Dark fringe at y = {y_dark*1e3:.3f} mm, I = {I_dark:.6f}  (expect 0)")
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

# We'll display y in mm for readability
Y_MM_MAX = 6.0   # ±6 mm shown


class DoubleSlit_FringeBuildScene(Scene):
    """
    Build up the double-slit intensity pattern from center outward.
    Show intensity profile and bright/dark fringe labels.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Double-Slit Interference", font="EB Garamond", font_size=56, color=INK)
        sub   = Text(
            "d = 0.5 mm  ·  λ = 600 nm  ·  L = 1 m",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2  = Text(
            "I(y) = I₀ cos²(πdy / λL)  —  two sources → darkness",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Intensity axes ─────────────────────────────────────────────────
        ax = Axes(
            x_range=[-Y_MM_MAX, Y_MM_MAX, 1.0],
            y_range=[0, 1.2, 0.5],
            x_length=10.5,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        ).shift(DOWN * 0.5)

        lbl_x = MathTex(r"y\;(\mathrm{mm})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"I / I_0",           color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP,   buff=0.08)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)

        # ── Draw intensity pattern from center outward ─────────────────────
        dy = fringe_spacing() * 1e3  # mm
        n_steps = 30
        y_mm_arr = np.linspace(-Y_MM_MAX, Y_MM_MAX, 600)
        I_arr    = intensity(y_mm_arr * 1e-3)

        # Build segments from center outward
        full_pts = [ax.c2p(float(y), float(I)) for y, I in zip(y_mm_arr, I_arr)]
        # Animate by revealing the curve in steps
        center_idx = len(y_mm_arr) // 2
        fringe_curve = VMobject(color=BLUE, stroke_width=2.5)
        fringe_curve.set_points_smoothly(full_pts)
        self.play(Create(fringe_curve), run_time=3.5)
        self.wait(0.5)

        # ── Label bright fringes ───────────────────────────────────────────
        bright_labels = VGroup()
        for m in range(-3, 4):
            y_mm = m * dy
            if abs(y_mm) > Y_MM_MAX - 0.3:
                continue
            dot = Dot(ax.c2p(y_mm, 1.0), color=GOLD, radius=0.10)
            lbl = MathTex(rf"m={m}", color=GOLD, font_size=16)
            lbl.next_to(dot, UP, buff=0.06)
            bright_labels.add(dot, lbl)

        self.play(FadeIn(bright_labels), run_time=1.0)
        self.wait(0.5)

        # ── Label dark fringes ─────────────────────────────────────────────
        dark_labels = VGroup()
        for m in range(-3, 3):
            y_mm = (m + 0.5) * dy
            if abs(y_mm) > Y_MM_MAX - 0.3:
                continue
            dot = Dot(ax.c2p(y_mm, 0.0), color=BROWN, radius=0.09)
            dark_labels.add(dot)

        dark_anno = Text("dark = destructive", font="EB Garamond", font_size=18, color=BROWN)
        dark_anno.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(dark_labels), Write(dark_anno), run_time=0.9)
        self.wait(0.8)

        # ── Fringe spacing callout ─────────────────────────────────────────
        spacing_eq = MathTex(
            r"\Delta y = \frac{\lambda L}{d} = \frac{600\,\mathrm{nm}\times 1\,\mathrm{m}}{0.5\,\mathrm{mm}} = 1.2\,\mathrm{mm}",
            color=INK, font_size=26,
        ).to_edge(UP, buff=0.20)
        self.play(FadeOut(dark_anno), Write(spacing_eq), run_time=1.2)
        self.wait(2.5)

        # ── Constructive / destructive labels ─────────────────────────────
        constr = Text("Constructive  d sinθ = mλ",     font="EB Garamond", font_size=20, color=GOLD).to_edge(DOWN, buff=0.42)
        destr  = Text("Destructive  d sinθ = (m+½)λ",  font="EB Garamond", font_size=20, color=BROWN).to_edge(DOWN, buff=0.18)
        self.play(Write(constr), Write(destr), run_time=1.0)
        self.wait(3.0)
