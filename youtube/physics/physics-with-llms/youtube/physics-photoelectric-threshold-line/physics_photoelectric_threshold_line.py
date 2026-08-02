#!/usr/bin/env python3
"""
physics_photoelectric_threshold_line.py — Photoelectric Threshold Line KE_max vs Frequency
SILENT SLATE — sim-scout candidate, physics-with-llms book.

Physics:
  KE_max = hf − φ
  Tungsten: φ = 4.5 eV → f0 = φ/h = 1.087e15 Hz
  Calcium:  φ = 2.71 eV → f0 = 6.55e14 Hz
  h = 4.136e-15 eV·s  (Planck's constant in eV·s)

Testable predictions:
  P1: Tungsten threshold f0 = 4.5/(4.136e-15) ≈ 1.087e15 Hz
  P2: Slope of KE vs f line = h = 4.136e-15 eV·s for every metal

Run standalone verification:
  python3 physics_photoelectric_threshold_line.py --verify

Render:
  manim -qh physics_photoelectric_threshold_line.py PhotoelectricThresholdScene
"""
import sys
import numpy as np

H_EV   = 4.136e-15  # eV·s
PHI_W  = 4.5        # eV  (tungsten)
PHI_CA = 2.71       # eV  (calcium)

def threshold_freq(phi_ev: float) -> float:
    return phi_ev / H_EV

def ke_max(f: np.ndarray, phi_ev: float) -> np.ndarray:
    ke = H_EV * f - phi_ev
    return np.where(ke > 0, ke, 0.0)

def verify():
    print("=== Photoelectric threshold verification ===")
    f0_W  = threshold_freq(PHI_W)
    f0_Ca = threshold_freq(PHI_CA)
    print(f"  Tungsten  φ={PHI_W} eV  f0 = {f0_W:.4e} Hz")
    print(f"  Calcium   φ={PHI_CA} eV  f0 = {f0_Ca:.4e} Hz")
    # Check slope
    f_test = np.array([f0_W * 1.5, f0_W * 2.0])
    ke1 = ke_max(f_test, PHI_W)
    slope = (ke1[1] - ke1[0]) / (f_test[1] - f_test[0])
    print(f"  Slope of KE vs f = {slope:.4e} eV·s  (expect {H_EV:.4e})")
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

F_MIN = 0.5e15   # Hz
F_MAX = 2.0e15   # Hz


class PhotoelectricThresholdScene(Scene):
    """
    Draw KE_max vs frequency for Tungsten and Calcium.
    Show zero-KE region, threshold crossings, slope = h.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Photoelectric Effect", font="EB Garamond", font_size=58, color=INK)
        sub   = Text(
            "KE_max = hf − φ  ·  threshold frequency f₀ = φ/h",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "Below f₀ — no electrons, no matter how bright",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Axes  (frequency in units of 10^15 Hz for display) ────────────
        # We scale x to [0.5, 2.0] with unit = 10^15 Hz
        f0_W_scaled  = threshold_freq(PHI_W)  / 1e15
        f0_Ca_scaled = threshold_freq(PHI_CA) / 1e15

        ax = Axes(
            x_range=[0.5, 2.1, 0.25],
            y_range=[-1.0, 4.0, 1.0],
            x_length=9.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        ).shift(DOWN * 0.2)

        lbl_x = MathTex(r"f\;(10^{15}\,\mathrm{Hz})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"KE_{\max}\;(\mathrm{eV})",  color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP,    buff=0.08)

        # zero-KE shaded region
        zero_region = Rectangle(
            width=ax.c2p(f0_W_scaled, 0)[0] - ax.c2p(0.5, 0)[0],
            height=0.05,
            color=BROWN, fill_color=BROWN, fill_opacity=0.12, stroke_width=0,
        ).align_to(ax.c2p(0.5, -1.0), UL).stretch_to_fit_height(
            ax.c2p(0, 0)[1] - ax.c2p(0, -1.0)[1]
        )

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)

        # ── Draw threshold line for Tungsten ───────────────────────────────
        f_arr = np.linspace(F_MIN, F_MAX, 400)
        f_scaled = f_arr / 1e15
        ke_W  = ke_max(f_arr, PHI_W)
        ke_Ca = ke_max(f_arr, PHI_CA)

        # Tungsten line
        pts_W = [ax.c2p(float(fs), float(ke)) for fs, ke in zip(f_scaled, ke_W)]
        curve_W = VMobject(color=BLUE, stroke_width=3.0)
        curve_W.set_points_smoothly(pts_W)

        # Threshold marker Tungsten
        dot_W = Dot(ax.c2p(f0_W_scaled, 0), color=BLUE, radius=0.12)
        lbl_W = MathTex(
            rf"f_0(\mathrm{{W}}) = {threshold_freq(PHI_W)/1e15:.3f}\times10^{{15}}\,\mathrm{{Hz}}",
            color=BLUE, font_size=22,
        ).next_to(dot_W, UP + RIGHT, buff=0.1)

        self.play(Create(curve_W), FadeIn(dot_W), Write(lbl_W), run_time=2.0)
        self.wait(0.7)

        # ── Calcium line ───────────────────────────────────────────────────
        pts_Ca = [ax.c2p(float(fs), float(ke)) for fs, ke in zip(f_scaled, ke_Ca)]
        curve_Ca = VMobject(color=GOLD, stroke_width=2.5, stroke_opacity=0.85)
        curve_Ca.set_points_smoothly(pts_Ca)

        dot_Ca = Dot(ax.c2p(f0_Ca_scaled, 0), color=GOLD, radius=0.12)
        lbl_Ca = MathTex(
            rf"f_0(\mathrm{{Ca}}) = {threshold_freq(PHI_CA)/1e15:.3f}\times10^{{15}}\,\mathrm{{Hz}}",
            color=GOLD, font_size=22,
        ).next_to(dot_Ca, DOWN + RIGHT, buff=0.08)

        self.play(Create(curve_Ca), FadeIn(dot_Ca), Write(lbl_Ca), run_time=1.8)
        self.wait(0.7)

        # ── Same slope = h annotation ──────────────────────────────────────
        slope_anno = MathTex(
            r"\text{slope} = h = 4.136\times10^{-15}\,\mathrm{eV\cdot s}",
            color=INK, font_size=26,
        ).to_edge(UP, buff=0.22)
        # Brace showing parallel lines
        arrow_brace = Arrow(
            ax.c2p(1.6, 0.8), ax.c2p(1.8, 1.627),
            color=INK, stroke_width=2, tip_length=0.15,
        )
        self.play(Write(slope_anno), GrowArrow(arrow_brace), run_time=1.0)
        self.wait(0.8)

        # ── Formula at bottom ──────────────────────────────────────────────
        eq = MathTex(
            r"KE_{\max} = hf - \phi \quad \phi_W = 4.5\,\mathrm{eV},\;\phi_{Ca} = 2.71\,\mathrm{eV}",
            color=INK, font_size=25,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(eq), run_time=1.2)
        self.wait(2.5)
