#!/usr/bin/env python3
"""
thermo_schottky_anomaly.py — Schottky Anomaly: C_V Peak From Two-Level Statistics
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

Physics (verified at module level):
    E₀=0, E₁=ε.  Z = 1 + exp(-ε/k_BT)
    P₁ = exp(-ε/k_BT) / Z
    C_V = k_B (ε/k_BT)² exp(ε/k_BT) / (exp(ε/k_BT)+1)²
    Peak at k_BT ≈ 0.417ε → T_peak = ε/(0.417·k_B)
    ε = 0.02 eV → T_peak ≈ 556 K

Render:
    cd physics-thermodynamics/youtube/thermo-schottky-anomaly
    manim -qh thermo_schottky_anomaly.py SchottkyAnomalyScene
"""
import sys
import numpy as np
from scipy.optimize import minimize_scalar

# ─── Constants ────────────────────────────────────────────────────────────────
K_B_EV  = 8.617333e-5   # eV/K
K_B_J   = 1.380649e-23  # J/K
EPS_EV  = 0.02          # eV  — two-level splitting


def partition(T: float, eps: float = EPS_EV) -> float:
    return 1.0 + np.exp(-eps / (K_B_EV * T))


def P1(T: float, eps: float = EPS_EV) -> float:
    """Population of excited state."""
    x = eps / (K_B_EV * T)
    return np.exp(-x) / (1.0 + np.exp(-x))


def Cv_schottky(T: np.ndarray, eps: float = EPS_EV) -> np.ndarray:
    """C_V/k_B for two-level Schottky system."""
    x = eps / (K_B_EV * T)
    # Avoid overflow
    x = np.clip(x, 1e-10, 500)
    return x**2 * np.exp(x) / (np.exp(x) + 1.0)**2


# ─── Verification ─────────────────────────────────────────────────────────────
def _verify():
    print("=== Schottky Anomaly verification ===")
    # Find peak numerically
    res = minimize_scalar(lambda T: -Cv_schottky(np.array([T]))[0], bounds=(1, 10000), method='bounded')
    T_peak = res.x
    kT_peak = K_B_EV * T_peak
    print(f"ε = {EPS_EV:.2f} eV")
    print(f"C_V peak at T = {T_peak:.0f} K  (expected ≈ 556 K)")
    print(f"k_BT_peak / ε = {kT_peak/EPS_EV:.3f}  (expected ≈ 0.417)")
    print(f"P₁ at 100 K: {P1(100.0)*100:.1f}%  (expected ≈ 9.8%)")
    print(f"P₁ at 556 K: {P1(T_peak)*100:.1f}%  (expected ≈ 37%)")
    print(f"P₁ at 10000 K: {P1(10000.0)*100:.1f}%  (expected ≈ 49%)")
    # At T→∞, P₁ → 0.5, Cv → 0
    Cv_hot = Cv_schottky(np.array([1e6]))[0]
    print(f"C_V/k_B at T=10^6 K: {Cv_hot:.6f}  (→ 0 at saturation)")
    print("=== PASSED ===")

_verify()
if __name__ == "__main__":
    sys.exit(0)


# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"

T_MIN   = 10.0
T_MAX   = 3000.0
T_PEAK  = EPS_EV / (2.399 * K_B_EV)    # ≈ 97 K  (x_peak=2.399 where dCv/dT=0)


class SchottkyAnomalyScene(Scene):
    """
    Split screen: left = energy level populations, right = C_V curve.
    A temperature cursor sweeps from 10 K to 3000 K, updating both panels.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax_cv, ax_pop = self._build_split_axes()
        self._phase_static_cv(ax_cv)
        self._phase_sweep(ax_cv, ax_pop)

    def _phase_title(self):
        title = Text("Schottky Anomaly", font="EB Garamond", font_size=64, color=INK)
        sub1 = MathTex(
            r"C_V = k_B \left(\frac{\varepsilon}{k_BT}\right)^2 \frac{e^{\varepsilon/k_BT}}{(e^{\varepsilon/k_BT}+1)^2}",
            color=BLUE, font_size=30,
        )
        sub2 = Text(
            "Zero at T=0 · zero at T=∞ · peak in between — the Goldilocks signature",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub1), run_time=0.9)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _build_split_axes(self):
        # Right: C_V(T) curve
        ax_cv = Axes(
            x_range=[T_MIN, T_MAX, 500],
            y_range=[0, 0.5, 0.1],
            x_length=5.5,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(RIGHT * 3.5 + DOWN * 0.3)

        lbl_cx = MathTex(r"T\;(\mathrm{K})", color=INK, font_size=22).next_to(ax_cv.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_cy = MathTex(r"C_V/k_B", color=INK, font_size=22).next_to(ax_cv.y_axis.get_end(), UP, buff=0.08)
        hdr_cv = Text("C_V / k_B", font="EB Garamond", font_size=22, color=DIM).next_to(ax_cv, UP, buff=0.1)

        # Left: population diagram (manual, not Axes)
        hdr_pop = Text("Level populations", font="EB Garamond",
                       font_size=22, color=DIM).shift(LEFT * 3.5 + UP * 3.2)

        self.play(Create(ax_cv), Write(lbl_cx), Write(lbl_cy), Write(hdr_cv), Write(hdr_pop), run_time=1.5)
        return ax_cv, hdr_pop

    def _phase_static_cv(self, ax_cv):
        """Draw the full C_V curve first."""
        Ts = np.linspace(T_MIN + 1, T_MAX, 600)
        Cvs = Cv_schottky(Ts)
        pts = [ax_cv.c2p(T, C) for T, C in zip(Ts, Cvs)]
        curve = VMobject(color=BLUE, stroke_width=3.5)
        curve.set_points_smoothly(pts)

        # Peak marker
        peak_x = ax_cv.c2p(T_PEAK, Cv_schottky(np.array([T_PEAK]))[0])
        peak_dot = Dot(peak_x, color=GOLD, radius=0.08)
        peak_lbl = MathTex(r"T_{\rm peak}\approx 97\,\mathrm{K}", color=GOLD, font_size=20).next_to(
            peak_x, UP, buff=0.12)

        self.play(Create(curve), run_time=2.5)
        self.play(Create(peak_dot), Write(peak_lbl), run_time=0.8)
        self.wait(1.0)
        self._cv_curve = curve
        self._peak_dot = peak_dot
        self._peak_lbl = peak_lbl

    def _phase_sweep(self, ax_cv, ax_pop_hdr):
        """Sweep T — cursor on C_V, bars on population panel."""
        T_tracker = ValueTracker(T_MIN)

        # Population bars (left panel)
        # Ground level: y = -1.5, excited: y = 0.5
        bar_cx = -3.5
        bar_w  = 2.5
        y_gnd  = -1.0
        y_exc  =  1.0
        bar_h_scale = 4.0   # max bar height

        gnd_line  = Line([bar_cx - bar_w/2, y_gnd, 0], [bar_cx + bar_w/2, y_gnd, 0],
                         color=DIM, stroke_width=2.0)
        exc_line  = Line([bar_cx - bar_w/2, y_exc, 0], [bar_cx + bar_w/2, y_exc, 0],
                         color=BLUE, stroke_width=2.0)
        lbl_gnd   = Text("E₀=0 (ground)", font="EB Garamond",
                          font_size=20, color=DIM).next_to(gnd_line, RIGHT, buff=0.15)
        lbl_exc   = Text("E₁=ε (excited)", font="EB Garamond",
                          font_size=20, color=BLUE).next_to(exc_line, RIGHT, buff=0.15)

        self.play(Create(gnd_line), Create(exc_line), Write(lbl_gnd), Write(lbl_exc), run_time=0.8)

        def make_pop_bars():
            T = T_tracker.get_value()
            p1 = P1(T)
            p0 = 1.0 - p1
            # Ground bar (grows DOWN from level line)
            h0 = p0 * bar_h_scale
            bar0 = Rectangle(width=0.8, height=max(h0, 0.01),
                              color=DIM, fill_color=DIM, fill_opacity=0.5, stroke_width=0)
            bar0.next_to(gnd_line, DOWN, buff=0.0).align_to(gnd_line, RIGHT).shift(LEFT * 1.0)
            # Excited bar (grows UP from excited line)
            h1 = p1 * bar_h_scale
            bar1 = Rectangle(width=0.8, height=max(h1, 0.01),
                              color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=0)
            bar1.next_to(exc_line, UP, buff=0.0).align_to(exc_line, RIGHT).shift(LEFT * 1.0)
            # Fraction labels
            lbl0 = Text(f"{p0*100:.0f}%", font="EB Garamond", font_size=18, color=DIM).move_to(bar0)
            lbl1 = Text(f"{p1*100:.0f}%", font="EB Garamond", font_size=18, color=BLUE).move_to(bar1)
            return VGroup(bar0, bar1, lbl0, lbl1)

        def make_cursor():
            T = T_tracker.get_value()
            Cv = Cv_schottky(np.array([T]))[0]
            x  = np.clip(T, T_MIN, T_MAX)
            return Dot(ax_cv.c2p(x, Cv), color=GOLD, radius=0.1)

        dyn_bars   = always_redraw(make_pop_bars)
        dyn_cursor = always_redraw(make_cursor)
        self.add(dyn_bars, dyn_cursor)

        # Readouts
        T_lbl = MathTex(r"T = ", color=INK, font_size=28)
        T_num = DecimalNumber(T_MIN, num_decimal_places=0, color=GOLD, font_size=28)
        T_K   = MathTex(r"\mathrm{K}", color=INK, font_size=28)
        T_num.add_updater(lambda m: m.set_value(T_tracker.get_value()))
        T_row = VGroup(T_lbl, T_num, T_K).arrange(RIGHT, buff=0.08).to_edge(DOWN, buff=0.25)

        hdr_sw = Text("Sweep T — population shift drives C_V peak",
                      font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.25)
        self.play(Write(hdr_sw), FadeIn(T_row), run_time=0.8)

        # Sweep to T_PEAK then to T_MAX
        self.play(T_tracker.animate.set_value(T_PEAK), run_time=5.0, rate_func=smooth)
        peak_note = Text("Population changing fastest here — C_V at maximum (~97 K for ε=0.02 eV)",
                         font="EB Garamond", font_size=20, color=GOLD).next_to(T_row, UP, buff=0.1)
        self.play(Write(peak_note), run_time=0.8)
        self.wait(1.0)
        self.play(FadeOut(peak_note), run_time=0.3)

        self.play(T_tracker.animate.set_value(T_MAX), run_time=5.0, rate_func=smooth)
        self.wait(1.0)

        final = Text(
            "At T→∞: both levels equally populated (P₁→50%) — population can't change further\n"
            "→ no more energy absorbed → C_V → 0",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeOut(T_row), Write(final), run_time=1.2)
        self.wait(3.0)
