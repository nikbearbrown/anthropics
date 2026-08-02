#!/usr/bin/env python3
"""
cm_wave_superposition.py — Superposition: Constructive and Destructive Interference
SILENT SLATE — brownblue dark palette, physics-plus-one-classical-mechanics.

Physics:
    y1 = A*sin(kx - omega*t)
    y2 = A*sin(kx - omega*t + phi)
    y_total = y1 + y2 = 2A*cos(phi/2)*sin(kx - omega*t + phi/2)
    Amplitude = 2A*|cos(phi/2)|

Verify: python3 cm_wave_superposition.py --verify
Render: manim -qh cm_wave_superposition.py CmWaveSuperpositionScene
"""
import sys
import numpy as np

A     = 1.0    # m
LAM   = 2.0    # m
F_HZ  = 1.0    # Hz
K     = 2 * np.pi / LAM
OMEGA = 2 * np.pi * F_HZ

def wave1(x, t, phi=0.0):
    return A * np.sin(K * x - OMEGA * t)

def wave2(x, t, phi):
    return A * np.sin(K * x - OMEGA * t + phi)

def superposition(x, t, phi):
    return wave1(x, t) + wave2(x, t, phi)

def amplitude_sum(phi):
    return 2 * A * abs(np.cos(phi / 2))

def verify():
    print("=== Wave superposition verification ===")
    # P1: phi=pi -> amplitude = 0
    amp_pi = amplitude_sum(np.pi)
    print(f"P1: phi=pi -> amplitude = {amp_pi:.6f}  (expected 0.0) {'✓' if amp_pi < 1e-10 else '✗'}")
    # P2: phi=pi/3 -> amplitude = 2*cos(pi/6) = sqrt(3)
    amp_pi3 = amplitude_sum(np.pi/3)
    expected = 2 * A * np.cos(np.pi/6)
    print(f"P2: phi=pi/3 -> amplitude = {amp_pi3:.4f}  (expected {expected:.4f}) {'✓' if abs(amp_pi3 - expected) < 0.001 else '✗'}")
    # phi=0: constructive (2A), phi=pi/2: sqrt(2)
    print(f"phi=0 (constructive): amplitude = {amplitude_sum(0):.4f}  (expected 2.0)")
    print(f"phi=pi/2: amplitude = {amplitude_sum(np.pi/2):.4f}  (expected {np.sqrt(2):.4f})")
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
GREEN  = "#50C878"

X_MIN = 0.0
X_MAX = 6.0
N_PTS = 300


class CmWaveSuperpositionScene(Scene):
    """
    Three-panel: wave1 (blue), wave2 (brown, phase shifted), sum (gold).
    Phi slider sweeps 0 -> 2pi. Amplitude panel shows 2A|cos(phi/2)|.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._static_cases()
        self._slider_phase()
        self._amplitude_plot()
        self._finale()

    def _title(self):
        t = Text("Superposition: Constructive and Destructive Interference",
                 font="EB Garamond", font_size=44, color=INK)
        s = Text(
            "y₁ + y₂ = 2A cos(φ/2) sin(kx − ωt + φ/2)\n"
            "At φ = 0: amplitude doubles.  At φ = π: amplitude = 0.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _make_axes_triple(self):
        """Three stacked horizontal axes."""
        axes = []
        offsets = [2.2, 0.0, -2.2]
        labels = ["Wave 1", "Wave 2", "Sum"]
        colors = [BLUE, BROWN, GOLD]
        for y_off, lbl, col in zip(offsets, labels, colors):
            ax = Axes(
                x_range=[X_MIN, X_MAX, 1.0],
                y_range=[-2.2, 2.2, 1.0],
                x_length=9,
                y_length=1.5,
                axis_config=dict(color=DIM, stroke_width=0.8,
                                 include_ticks=False, tip_length=0.1),
            ).shift(UP * y_off + LEFT * 0.5)
            lbl_mob = Text(lbl, font="EB Garamond", font_size=18, color=col)
            lbl_mob.next_to(ax.y_axis.get_end(), UL, buff=0.05)
            axes.append((ax, lbl_mob, col))
        return axes

    def _static_cases(self):
        x = np.linspace(X_MIN, X_MAX, N_PTS)

        for phi_deg, label, col_phase in [
            (0,   "φ = 0  (constructive)", GOLD),
            (180, "φ = π  (destructive)",  BROWN),
        ]:
            phi = np.radians(phi_deg)
            t_snap = 0.0

            axes_triple = self._make_axes_triple()
            all_mobs = [ax for ax, _, _ in axes_triple] + [lbl for _, lbl, _ in axes_triple]
            self.play(*[Create(ax) for ax, _, _ in axes_triple],
                      *[Write(lbl) for _, lbl, _ in axes_triple], run_time=0.8)

            y1 = wave1(x, t_snap)
            y2 = wave2(x, t_snap, phi)
            yt = superposition(x, t_snap, phi)

            ax1, _, _ = axes_triple[0]
            ax2, _, _ = axes_triple[1]
            ax3, _, _ = axes_triple[2]

            for ax, y_data, col in [(ax1, y1, BLUE), (ax2, y2, BROWN), (ax3, yt, GOLD)]:
                pts = np.array([ax.c2p(xi, yi) for xi, yi in zip(x, y_data)])
                m = VMobject(color=col, stroke_width=2.5)
                m.set_points_smoothly(pts)
                all_mobs.append(m)
                self.play(Create(m), run_time=0.7)

            amp = amplitude_sum(phi)
            cap = Text(
                f"{label}  —  amplitude = {amp:.2f} m",
                font="EB Garamond", font_size=22, color=col_phase,
            ).to_edge(DOWN, buff=0.2)
            self.play(Write(cap), run_time=0.7)
            self.wait(2.0)
            self.play(*[FadeOut(m) for m in all_mobs], FadeOut(cap), run_time=0.4)

    def _slider_phase(self):
        phi_tracker = ValueTracker(0.0)
        x = np.linspace(X_MIN, X_MAX, N_PTS)

        # Three stacked axes (persistent)
        axes_triple = self._make_axes_triple()
        self.play(*[Create(ax) for ax, _, _ in axes_triple],
                  *[Write(lbl) for _, lbl, _ in axes_triple], run_time=0.8)
        ax1, _, _ = axes_triple[0]
        ax2, _, _ = axes_triple[1]
        ax3, _, _ = axes_triple[2]

        def _make_wave(ax, phi_shift, col, t_snap=0.0):
            def _fn():
                phi = phi_tracker.get_value()
                if phi_shift == 0:
                    y = wave1(x, t_snap)
                elif phi_shift == 1:
                    y = wave2(x, t_snap, phi)
                else:
                    y = superposition(x, t_snap, phi)
                y_clip = np.clip(y, -2.1, 2.1)
                pts = np.array([ax.c2p(xi, yi) for xi, yi in zip(x, y_clip)])
                m = VMobject(color=col, stroke_width=2.5)
                m.set_points_smoothly(pts)
                return m
            return _fn

        dyn1 = always_redraw(_make_wave(ax1, 0, BLUE))
        dyn2 = always_redraw(_make_wave(ax2, 1, BROWN))
        dyn3 = always_redraw(_make_wave(ax3, 2, GOLD))
        self.add(dyn1, dyn2, dyn3)

        phi_lbl = MathTex(r"\phi = ", color=INK, font_size=28)
        phi_num = DecimalNumber(0.0, num_decimal_places=2, color=GOLD, font_size=28)
        pi_unit = MathTex(r"\times\pi", color=INK, font_size=28)
        phi_num.add_updater(lambda m: m.set_value(phi_tracker.get_value() / np.pi))
        phi_row = VGroup(phi_lbl, phi_num, pi_unit).arrange(RIGHT, buff=0.1).to_corner(UR, buff=0.3)

        amp_lbl = MathTex(r"|A_{\rm sum}| = ", color=DIM, font_size=24)
        amp_num = DecimalNumber(2.0, num_decimal_places=3, color=GOLD, font_size=24)
        amp_m   = MathTex(r"\,\mathrm{m}", color=DIM, font_size=24)
        amp_num.add_updater(lambda m: m.set_value(amplitude_sum(phi_tracker.get_value())))
        amp_row = VGroup(amp_lbl, amp_num, amp_m).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.25)

        self.play(Write(phi_row), Write(amp_row), run_time=0.8)
        # Sweep phi 0 -> 2pi
        self.play(phi_tracker.animate.set_value(2 * np.pi), run_time=6.0, rate_func=linear)
        self.wait(1.0)
        self.play(FadeOut(phi_row, amp_row, dyn1, dyn2, dyn3,
                          *[ax for ax, _, _ in axes_triple],
                          *[lbl for _, lbl, _ in axes_triple]), run_time=0.4)

    def _amplitude_plot(self):
        ax = Axes(
            x_range=[0, 2 * np.pi + 0.1, np.pi/2],
            y_range=[0, 2.1, 0.5],
            x_length=8,
            y_length=3.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).center()
        lx = MathTex(r"\phi", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"|A_{\rm sum}|", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        phi_vals = np.linspace(0, 2 * np.pi, 400)
        amp_vals = amplitude_sum(phi_vals)
        pts = np.array([ax.c2p(p, a) for p, a in zip(phi_vals, amp_vals)])
        amp_curve = VMobject(color=GOLD, stroke_width=3)
        amp_curve.set_points_smoothly(pts)

        # Tick labels at 0, pi, 2pi
        for phi_val, lbl_str in [(0, "0"), (np.pi, r"\pi"), (2*np.pi, r"2\pi")]:
            lbl = MathTex(lbl_str, color=DIM, font_size=20)
            lbl.next_to(ax.c2p(phi_val, 0), DOWN, buff=0.1)
            self.add(lbl)
        # Markers at constructive/destructive
        for phi_val, ann, col in [(0, "max 2A", BLUE), (np.pi, "0", BROWN), (2*np.pi, "max 2A", BLUE)]:
            d = Dot(ax.c2p(phi_val, amplitude_sum(phi_val + 1e-9)), color=col, radius=0.1)
            self.add(d)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(amp_curve), run_time=1.8)
        eq = MathTex(r"|A_{\rm sum}| = 2A\left|\cos\frac{\phi}{2}\right|",
                     color=INK, font_size=28).to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.0)
        self.wait(2.5)

    def _finale(self):
        eq = MathTex(
            r"y_{\rm total} = 2A\cos\!\tfrac{\phi}{2}\sin\!\left(kx - \omega t + \tfrac{\phi}{2}\right)",
            color=INK, font_size=30,
        ).center().shift(DOWN * 2.8)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
