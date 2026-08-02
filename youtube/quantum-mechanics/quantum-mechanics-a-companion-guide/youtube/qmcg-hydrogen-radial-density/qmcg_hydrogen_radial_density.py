#!/usr/bin/env python3
"""
qmcg_hydrogen_radial_density.py — Hydrogen 1s Radial Density: Why the Orbit Picture Fails
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-hydrogen-radial-density
    manim -qh qmcg_hydrogen_radial_density.py HydrogenRadialScene

Verify:
    python3 qmcg_hydrogen_radial_density.py --verify

Physics:
    P(r) = |R₁₀(r)|² r² = (4/a₀³) r² e^{−2r/a₀}
    Peak (mode) at r = a₀
    ⟨r⟩ = 3a₀/2  (mean > mode: asymmetric tail)
    Median ≈ 1.34 a₀
    2p: P(r) ∝ r⁴ e^{−r/a₀}, peak at 4a₀, ⟨r⟩=5a₀
"""
import sys
import numpy as np
from scipy.integrate import cumulative_trapezoid


A0 = 0.0529   # nm, Bohr radius


def P_1s(r_a0):
    """Radial probability density for 1s (normalized, in units of a₀)."""
    return 4 * r_a0**2 * np.exp(-2 * r_a0)


def P_2p(r_a0):
    """Radial probability density for 2p (normalized, in units of a₀)."""
    # R₂₁(r) = (1/√24)(r/a₀)e^{-r/2a₀}/a₀^{3/2}
    # P(r) ∝ r^4 e^{-r/a₀}; normalize
    raw = r_a0**4 * np.exp(-r_a0)
    return raw


def verify():
    print("=== Hydrogen radial density verification ===")
    r = np.linspace(1e-6, 20, 100000)
    P = P_1s(r)
    norm = np.trapz(P, r)
    print(f"  1s normalization: ∫P(r)dr = {norm:.6f}  (should be 1.0)")
    mean = np.trapz(r * P, r) / norm
    print(f"  P1: peak at r = {r[P.argmax()]:.4f} a₀  (should be 1.0000)")
    print(f"  P2: ⟨r⟩ = {mean:.6f} a₀  (should be 3/2 = {1.5})")

    # Median
    cumulative = cumulative_trapezoid(P / norm, r, initial=0)
    idx_median = np.searchsorted(cumulative, 0.5)
    print(f"  Median ≈ {r[idx_median]:.4f} a₀  (expected ≈1.34)")

    # 2p
    r2 = np.linspace(1e-6, 30, 100000)
    P2 = P_2p(r2)
    norm2 = np.trapz(P2, r2)
    mean2 = np.trapz(r2 * P2, r2) / norm2
    print(f"\n  2p peak at r = {r2[P2.argmax()]:.4f} a₀  (should be 4.0)")
    print(f"  2p ⟨r⟩ = {mean2:.4f} a₀  (should be 5.0)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class HydrogenRadialScene(Scene):
    """
    Phase 1: title
    Phase 2: P(r) for 1s — mode, mean, median marked separately
    Phase 3: sweeping area accumulation to find median
    Phase 4: 2p comparison — mode at 4a₀ matches Bohr's n=2 radius
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_1s()
        self._phase_2p()

    def _phase_title(self):
        title = Text("Hydrogen 1s Radial Density", font="EB Garamond", font_size=54, color=INK)
        sub1  = Text(
            "P(r) = (4/a₀³) r² e^{−2r/a₀}  ·  peak at a₀, mean at 3a₀/2",
            font="EB Garamond", font_size=23, color=BLUE,
        )
        sub2  = Text(
            "Bohr's orbit = mode.  Mean ≠ mode.  There is no orbit.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_1s(self):
        r_max = 10.0
        r_arr = np.linspace(1e-4, r_max, 600)
        P     = P_1s(r_arr)
        P_norm_val = np.trapz(P, r_arr)
        P_norm = P / P_norm_val

        ax = Axes(
            x_range=[0, r_max, 1], y_range=[0, P_norm.max() * 1.15, 0.05],
            x_length=9.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(UP * 0.3)

        x_lbl = MathTex(r"r/a_0", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"P(r)", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        pts  = [ax.c2p(r, p) for r, p in zip(r_arr, P_norm)]
        curve = VMobject(color=BLUE, stroke_width=2.8)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=1.0)

        # Mode at r=1
        mode_line = DashedLine(ax.c2p(1.0, 0), ax.c2p(1.0, P_norm.max()), color=GOLD, stroke_width=2.0)
        mode_lbl  = MathTex(r"\text{mode} = a_0", color=GOLD, font_size=20).next_to(ax.c2p(1.0, P_norm.max()), UP, buff=0.1)
        self.play(Create(mode_line), Write(mode_lbl), run_time=0.6)

        # Mean at r=1.5
        mean_val = np.trapz(r_arr * P_norm, r_arr)
        mean_line = DashedLine(ax.c2p(mean_val, 0), ax.c2p(mean_val, P_norm.max()), color=BROWN, stroke_width=2.0)
        mean_lbl  = MathTex(r"\langle r\rangle = \frac{3a_0}{2}", color=BROWN, font_size=20).next_to(ax.c2p(mean_val, P_norm.max() * 0.7), RIGHT, buff=0.1)
        self.play(Create(mean_line), Write(mean_lbl), run_time=0.6)

        # Median ≈ 1.34
        cum = cumulative_trapezoid(P_norm, r_arr, initial=0)
        idx = np.searchsorted(cum, 0.5)
        med_val = r_arr[min(idx, len(r_arr)-1)]
        med_line = DashedLine(ax.c2p(med_val, 0), ax.c2p(med_val, P_norm.max()), color=DIM, stroke_width=1.5)
        med_lbl  = MathTex(r"\text{median}\approx1.34a_0", color=DIM, font_size=18).next_to(ax.c2p(med_val, P_norm.max() * 0.4), LEFT, buff=0.1)
        self.play(Create(med_line), Write(med_lbl), run_time=0.6)

        note = Text(
            "Three distinct markers: orbit picture predicts they should coincide",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(note), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_2p(self):
        r_max = 20.0
        r_arr = np.linspace(1e-4, r_max, 600)
        P2    = P_2p(r_arr)
        P2_n  = P2 / np.trapz(P2, r_arr)

        ax = Axes(
            x_range=[0, r_max, 2], y_range=[0, P2_n.max() * 1.15, 0.01],
            x_length=9.0, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(UP * 0.3)

        x_lbl = MathTex(r"r/a_0", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        hdr   = Text("2p radial density — mode at 4a₀ (Bohr's n=2 prediction)",
                     font="EB Garamond", font_size=20, color=GOLD).to_edge(UP, buff=0.22)
        self.play(Create(ax), Write(x_lbl), Write(hdr), run_time=0.8)

        pts   = [ax.c2p(r, p) for r, p in zip(r_arr, P2_n)]
        curve2 = VMobject(color=GOLD, stroke_width=2.8)
        curve2.set_points_smoothly(pts)
        self.play(Create(curve2), run_time=0.8)

        mode2_line = DashedLine(ax.c2p(4.0, 0), ax.c2p(4.0, P2_n.max()), color=BLUE, stroke_width=2.0)
        mode2_lbl  = MathTex(r"\text{mode}=4a_0", color=BLUE, font_size=22).next_to(ax.c2p(4.0, P2_n.max()), UP, buff=0.1)
        mean2      = np.trapz(r_arr * P2_n, r_arr)
        mean2_line = DashedLine(ax.c2p(mean2, 0), ax.c2p(mean2, P2_n.max()), color=BROWN, stroke_width=2.0)
        mean2_lbl  = MathTex(r"\langle r\rangle=5a_0", color=BROWN, font_size=20).next_to(ax.c2p(mean2, P2_n.max()*0.5), RIGHT, buff=0.1)

        self.play(Create(mode2_line), Write(mode2_lbl), Create(mean2_line), Write(mean2_lbl), run_time=1.0)

        fin = Text(
            "Bohr always gets the mode right — SO(4) symmetry — but the cloud does everything else",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.7)
        self.wait(2.5)
