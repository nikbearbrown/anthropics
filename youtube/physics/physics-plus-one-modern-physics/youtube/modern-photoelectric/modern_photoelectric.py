#!/usr/bin/env python3
"""
modern_photoelectric.py — Photoelectric Effect: KE_max = hf − BE
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-modern-physics book.

Render:
    cd physics-plus-one-modern-physics/youtube/modern-photoelectric
    manim -qh modern_photoelectric.py PhotoelectricScene

Physics:
    KE_max = hf − BE  (work function = binding energy)
    h = 4.136e-15 eV·s
    Calcium BE = 2.71 eV, f_thresh = BE/h = 6.55e14 Hz (λ = 458 nm)
    At f = 8e14 Hz: KE = 4.136e-15 × 8e14 − 2.71 = 3.309 − 2.71 = 0.599 eV
    Slope of KE vs f = h (universal), x-intercept = BE/h (metal-specific)
"""
import sys
import numpy as np

H_EV = 4.136e-15     # eV·s

METALS = [
    ("Calcium",   2.71),
    ("Aluminum",  4.08),
    ("Gold",      5.10),
]


def ke_max(f, BE):
    """Max KE in eV at frequency f Hz for metal with work function BE eV."""
    ke = H_EV * f - BE
    return np.maximum(ke, 0.0)


def f_threshold(BE):
    return BE / H_EV


if __name__ == "__main__":
    print("=== Photoelectric Effect Verification ===")
    # P1: Calcium threshold
    f_thresh_Ca = f_threshold(2.71)
    lam_thresh  = 3.0e8 / f_thresh_Ca
    print(f"Ca threshold: f={f_thresh_Ca:.3e} Hz, λ={lam_thresh*1e9:.0f} nm  (expect 458 nm)")
    assert abs(f_thresh_Ca - 6.55e14) < 0.05e14, f"P1 FAIL: {f_thresh_Ca:.3e}"
    # P2: slope is universal — use raw (unclamped) KE = hf - BE to verify slope = h
    f_test = np.array([7e14, 8e14, 9e14, 10e14, 11e14])
    ke1_raw = H_EV * f_test - 2.71   # Ca — all above threshold at these frequencies
    ke2_raw = H_EV * f_test - 4.08   # Al — all above threshold at these frequencies
    slope1 = np.polyfit(f_test, ke1_raw, 1)[0]
    slope2 = np.polyfit(f_test, ke2_raw, 1)[0]
    print(f"Slope (Ca) = {slope1:.4e} eV·s,  Slope (Al) = {slope2:.4e} eV·s  (expect h={H_EV:.4e})")
    assert abs(slope1 - H_EV) / H_EV < 0.01, "P2 FAIL: slope"
    assert abs(slope2 - H_EV) / H_EV < 0.01, "P2 FAIL: slope"
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

F_MIN = 4e14
F_MAX = 12e14
COLORS = [BLUE, GOLD, BROWN]


class PhotoelectricScene(Scene):
    """KE_max vs f for three metals — same slope h, different thresholds."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_lines(ax)
        self._phase_classical_fail()

    def _phase_title(self):
        title = Text("The Photoelectric Effect", font="EB Garamond",
                     font_size=54, color=INK)
        sub = Text("KE_max = hf − BE — the slope is Planck's constant",
                   font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[F_MIN, F_MAX, 2e14],
            y_range=[-3.5, 3.5, 1],
            x_length=9.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.1)
        x_lbl = MathTex(r"f\;(\mathrm{Hz})", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"KE_{\rm max}\;(\mathrm{eV})", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        # KE = 0 line
        zero_line = DashedLine(ax.c2p(F_MIN, 0), ax.c2p(F_MAX, 0),
                               color=DIM, stroke_width=1.0)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), Create(zero_line), run_time=1.5)
        return ax

    def _phase_lines(self, ax):
        f_arr = np.linspace(F_MIN, F_MAX, 400)

        hdr = Text("Three metals — same slope h, different thresholds",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.5)

        lines = []
        for (name, BE), col in zip(METALS, COLORS):
            ke = H_EV * f_arr - BE
            # Plot only above-threshold region but draw full line
            ke_clip = np.where(ke < 0, ke, ke)
            pts = [ax.c2p(f, k) for f, k in zip(f_arr, ke_clip)
                   if ax.y_range[0] <= k <= ax.y_range[1]]
            if pts:
                line = VMobject(color=col, stroke_width=2.5)
                line.set_points_smoothly(pts)
            else:
                line = VMobject()

            ft = f_threshold(BE)
            lbl = Text(f"{name}  BE={BE} eV", font="EB Garamond",
                       font_size=17, color=col).next_to(
                ax.c2p(ft + 0.5e14, 0.2), UP, buff=0.05)
            thresh_line = DashedLine(
                ax.c2p(ft, ax.y_range[0]), ax.c2p(ft, 0.05),
                color=col, stroke_width=1.2)
            self.play(Create(line), Create(thresh_line), Write(lbl), run_time=1.0)
            lines.append((line, thresh_line, lbl))

        slope_eq = MathTex(
            r"\text{slope} = h = 4.136\times10^{-15}\,\mathrm{eV\cdot s}\;"
            r"(\text{same for all metals})",
            color=GOLD, font_size=22).to_edge(DOWN, buff=0.28)
        self.play(Write(slope_eq), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(hdr, slope_eq, *[m for tup in lines for m in tup]), run_time=0.5)

    def _phase_classical_fail(self):
        hdr = Text("Classical wave theory predicts: intensity → KE, no threshold",
                   font="EB Garamond", font_size=20, color=BROWN).to_edge(UP, buff=0.22)
        col1 = Text("Quantum:  threshold at f = BE/h  regardless of intensity",
                    font="EB Garamond", font_size=22, color=BLUE).shift(UP * 0.8)
        col2 = Text("Classical: no threshold — bright enough light always ejects electrons",
                    font="EB Garamond", font_size=22, color=BROWN).shift(DOWN * 0.2)
        col3 = Text("Experiment agrees with quantum — classical is wrong",
                    font="EB Garamond", font_size=22, color=GOLD).shift(DOWN * 1.2)
        self.play(Write(hdr), run_time=0.5)
        self.play(Write(col1), run_time=0.9)
        self.play(Write(col2), run_time=0.9)
        self.play(Write(col3), run_time=0.9)
        self.wait(2.5)
        final = MathTex(
            r"KE_{\rm max}=hf-BE\quad(\text{Einstein 1905, Nobel 1921})",
            color=INK, font_size=30).to_edge(DOWN, buff=0.28)
        self.play(Write(final), run_time=1.2)
        self.wait(2.5)
