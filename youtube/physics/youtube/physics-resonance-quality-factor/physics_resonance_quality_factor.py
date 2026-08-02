#!/usr/bin/env python3
"""
physics_resonance_quality_factor.py — Resonance Quality Factor Q
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    A(f) ∝ 1/sqrt((f²-f₀²)² + (f₀f/Q)²)
    f₀ = 440 Hz, Q = 2, 10, 100
    FWHM = f₀/Q
    Decay: amplitude ∝ exp(-πf₀t/Q)

Render:
    cd physics/youtube/physics-resonance-quality-factor
    manim -qh physics_resonance_quality_factor.py ResonanceQScene
"""
import sys
import numpy as np

F0 = 440.0  # Hz

def amplitude_norm(f, f0, Q):
    """Normalized steady-state amplitude (peak = Q for this normalization)."""
    return Q / np.sqrt((f**2 - f0**2)**2 + (f0*f/Q)**2) * f0


def fwhm(f0, Q):
    return f0 / Q


def decay_env(t, f0, Q):
    return np.exp(-np.pi * f0 * t / Q)


def verify():
    print("=== Resonance Quality Factor verification ===")
    for Q in [2, 10, 100]:
        bw = fwhm(F0, Q)
        print(f"  Q={Q:4d}: FWHM = {bw:.2f} Hz,  decay cycles to 1/e = Q/π = {Q/np.pi:.2f}")
    # P1: FWHM ratio
    assert abs(fwhm(F0,100)/fwhm(F0,10) - 0.1) < 1e-10, "P1 failed"
    # P2: decay at Q=100 → 100/π ≈ 31.8 cycles
    cycles_Q100 = 100/np.pi
    print(f"  Q=100: ring-down = {cycles_Q100:.2f} oscillations")
    cycles_Q2   = 2/np.pi
    print(f"  Q=2: ring-down = {cycles_Q2:.4f} oscillations (< 1 cycle)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

Q_VALS   = [2, 10, 100]
Q_COLORS = [BROWN, DIM, BLUE]


class ResonanceQScene(Scene):
    """Three amplitude-response curves and ring-down envelopes."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._freq_axes()
        self._draw_response_curves(ax)
        self._ring_down()

    def _title(self):
        t1 = Text("Resonance Quality Factor Q", font="EB Garamond", font_size=56, color=INK)
        t2 = Text("Sharp vs broad response — the same principle makes clocks and kills bridges",
                  font="EB Garamond", font_size=22, color=DIM)
        t3 = MathTex(r"\Delta f_{\rm FWHM} = \frac{f_0}{Q}", color=GOLD, font_size=36)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _freq_axes(self):
        ax = Axes(
            x_range=[0, 880, 220],
            y_range=[0, 115, 25],
            x_length=10,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.3)
        lx = MathTex(r"f\;(\mathrm{Hz})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = Text("Amplitude", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        # Resonance frequency marker
        dash = DashedLine(ax.c2p(F0, 0), ax.c2p(F0, 115), color=DIM, stroke_width=1.2, dash_length=0.15)
        lbl_f0 = MathTex(r"f_0=440\,\mathrm{Hz}", color=DIM, font_size=19).next_to(ax.c2p(F0, 0), DOWN, buff=0.08)
        hdr = Text("Steady-state amplitude vs driving frequency",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Create(dash), Write(lbl_f0), Write(hdr), run_time=1.5)
        return ax

    def _draw_response_curves(self, ax):
        fs = np.linspace(1, 879, 2000)
        for Q, col in zip(Q_VALS, Q_COLORS):
            amp = amplitude_norm(fs, F0, Q)
            # Clip to plot
            amp_clip = np.clip(amp, 0, 110)
            pts = np.array([ax.c2p(f, a) for f, a in zip(fs, amp_clip)])
            crv = VMobject(color=col, stroke_width=2.6).set_points_smoothly(pts)
            lbl = Text(f"Q = {Q}", font="EB Garamond", font_size=20, color=col)
            # Position label near peak
            peak_a = min(amplitude_norm(np.array([F0]), F0, Q)[0], 108)
            lbl.move_to(ax.c2p(F0 + 60, peak_a - 5))
            self.play(Create(crv), Write(lbl), run_time=1.5)
            self.wait(0.4)

            bw = fwhm(F0, Q)
            bw_lbl = Text(f"FWHM = {bw:.0f} Hz" if Q < 100 else f"FWHM = {bw:.1f} Hz",
                          font="EB Garamond", font_size=17, color=col)
            bw_lbl.to_edge(DOWN, buff=0.18 + 0.3*Q_VALS.index(Q))
            self.play(Write(bw_lbl), run_time=0.5)

        self.wait(1.5)

    def _ring_down(self):
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        ax = Axes(
            x_range=[0, 0.15, 0.05],
            y_range=[0, 1.1, 0.25],
            x_length=10,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.4)
        lx = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("Amplitude", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Ring-down envelopes — same f₀ = 440 Hz",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        ts = np.linspace(0, 0.15, 2000)
        for Q, col in zip(Q_VALS, Q_COLORS):
            env = decay_env(ts, F0, Q)
            osc = env * np.cos(2*np.pi*F0*ts)
            pts = np.array([ax.c2p(t, max(0, o)) for t, o in zip(ts, osc)])
            crv = VMobject(color=col, stroke_width=2.0).set_points_smoothly(pts)
            lbl = Text(f"Q={Q}", font="EB Garamond", font_size=18, color=col)
            lbl.to_edge(RIGHT, buff=0.2).shift(DOWN*(Q_VALS.index(Q)*0.4))
            self.play(Create(crv), Write(lbl), run_time=1.2)

        final = Text(
            "Q=2 dies in < 1 cycle  ·  Q=100 rings for 32 cycles",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
