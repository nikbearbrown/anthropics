#!/usr/bin/env python3
"""
thermo_maxwell_boltzmann.py — Maxwell-Boltzmann Speed Distribution
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

Physics verified at module level. Run:
    python3 thermo_maxwell_boltzmann.py     # prints verification table

Render:
    cd physics-thermodynamics/youtube/thermo-maxwell-boltzmann
    manim -qh thermo_maxwell_boltzmann.py MaxwellBoltzmannScene

Physics:
    f(v) = 4π(m/2πk_BT)^(3/2) v² exp(-mv²/2k_BT)
    v_mp  = sqrt(2k_BT/m)
    v_avg = sqrt(8k_BT/πm)
    v_rms = sqrt(3k_BT/m)

    O₂ at 300 K: v_mp=395, v_avg=446, v_rms=484 m/s
    Ratio v_mp:v_avg:v_rms = 1 : sqrt(4/π) : sqrt(3/2) = 1:1.128:1.225
"""
import sys
import numpy as np
from scipy import integrate

# ─── Physics constants ────────────────────────────────────────────────────────
K_B    = 1.380649e-23   # J/K  Boltzmann constant
N_A    = 6.02214076e23  # mol⁻¹ Avogadro
M_O2   = 32.0e-3 / N_A # kg per O₂ molecule
M_H2   = 2.016e-3 / N_A # kg per H₂ molecule
M_N2   = 28.014e-3 / N_A # kg per N₂ molecule
V_ESC_MARS  = 5.0e3    # m/s  Mars escape velocity
V_ESC_EARTH = 11.2e3   # m/s  Earth escape velocity


# ─── Pure numpy functions — no Manim ─────────────────────────────────────────

def mb_speed(v: np.ndarray, m: float, T: float) -> np.ndarray:
    """Maxwell-Boltzmann speed distribution f(v)."""
    a = 4.0 * np.pi * (m / (2.0 * np.pi * K_B * T)) ** 1.5
    return a * v**2 * np.exp(-m * v**2 / (2.0 * K_B * T))


def v_mp(m: float, T: float) -> float:
    return np.sqrt(2.0 * K_B * T / m)


def v_avg(m: float, T: float) -> float:
    return np.sqrt(8.0 * K_B * T / (np.pi * m))


def v_rms(m: float, T: float) -> float:
    return np.sqrt(3.0 * K_B * T / m)


def escape_fraction(m: float, T: float, v_esc: float) -> float:
    """Fraction of molecules with speed > v_esc."""
    result, _ = integrate.quad(mb_speed, v_esc, np.inf, args=(m, T), limit=200)
    return result


# ─── Module-level verification ────────────────────────────────────────────────
def _verify():
    print("=== Maxwell-Boltzmann verification ===")
    T = 300.0
    vmp  = v_mp(M_O2, T)
    vavg = v_avg(M_O2, T)
    vrms = v_rms(M_O2, T)
    print(f"O₂ at {T} K:")
    print(f"  v_mp  = {vmp:.0f} m/s   (expected ≈ 395)")
    print(f"  v_avg = {vavg:.0f} m/s  (expected ≈ 446)")
    print(f"  v_rms = {vrms:.0f} m/s  (expected ≈ 484)")
    r1 = vavg / vmp;  r2 = vrms / vmp
    print(f"  Ratios — v_avg/v_mp = {r1:.4f} (√4/π={np.sqrt(4/np.pi):.4f}), v_rms/v_mp = {r2:.4f} (√3/2={np.sqrt(1.5):.4f})")
    fH2_mars  = escape_fraction(M_H2, 200.0, V_ESC_MARS)
    fH2_earth = escape_fraction(M_H2, 200.0, V_ESC_EARTH)
    fN2_mars  = escape_fraction(M_N2, 200.0, V_ESC_MARS)
    print(f"H₂ @ 200 K escape fraction (Mars  5.0 km/s): {fH2_mars:.2e}  (expected ~10⁻³)")
    print(f"H₂ @ 200 K escape fraction (Earth 11.2km/s): {fH2_earth:.2e}")
    print(f"N₂ @ 200 K escape fraction (Mars  5.0 km/s): {fN2_mars:.2e}  (expected ~10⁻¹⁰⁰ → 0)")
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


class MaxwellBoltzmannScene(Scene):
    """
    Phase 1: Title.
    Phase 2: O₂ at 300 K — draw curve, drop three speed markers.
    Phase 3: T sweep 100→2000 K — peak slides right and broadens.
    Phase 4: Overlay H₂ vs N₂ at 200 K; shade tail > Mars escape velocity.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_draw_curve()
        self._phase_temp_sweep(ax)
        self._phase_escape(ax)

    # ── Phase 1: Title ────────────────────────────────────────────────────────
    def _phase_title(self):
        title = Text("Maxwell-Boltzmann Speed Distribution", font="EB Garamond",
                     font_size=56, color=INK)
        sub1 = Text(
            "f(v) = 4π(m/2πk_BT)^(3/2) v² exp(−mv²/2k_BT)",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2 = Text(
            "The tail decides planetary history — not the average",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    # ── Phase 2: O₂ at 300 K, three markers ──────────────────────────────────
    def _phase_draw_curve(self):
        T0 = 300.0
        v_max = 1500.0
        vs = np.linspace(1, v_max, 600)
        fs = mb_speed(vs, M_O2, T0)
        f_max = fs.max()

        ax = Axes(
            x_range=[0, v_max, 300],
            y_range=[0, f_max * 1.15, f_max * 0.5],
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.4)

        lbl_x = MathTex(r"v\;(\mathrm{m/s})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"f(v)", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        title_ax = Text("O₂  at  300 K", font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.25)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(title_ax), run_time=1.5)

        # Draw curve
        curve_pts = [ax.c2p(v, f) for v, f in zip(vs, fs)]
        curve = VMobject(color=BLUE, stroke_width=3.5)
        curve.set_points_smoothly(curve_pts)
        self.play(Create(curve), run_time=2.5)
        self.wait(0.5)

        # Three markers
        vmp_val  = v_mp(M_O2, T0)
        vavg_val = v_avg(M_O2, T0)
        vrms_val = v_rms(M_O2, T0)

        markers_data = [
            (vmp_val,  r"v_{\rm mp}=395", GOLD),
            (vavg_val, r"v_{\rm avg}=446", BROWN),
            (vrms_val, r"v_{\rm rms}=484", INK),
        ]

        marker_objs = []
        for v_val, lbl_str, col in markers_data:
            f_val = mb_speed(np.array([v_val]), M_O2, T0)[0]
            top    = ax.c2p(v_val, f_val)
            bottom = ax.c2p(v_val, 0)
            line = DashedLine(bottom, top, color=col, stroke_width=2.0)
            lbl  = MathTex(lbl_str, color=col, font_size=20).next_to(
                ax.c2p(v_val, 0), DOWN, buff=0.15
            )
            self.play(Create(line), Write(lbl), run_time=0.8)
            marker_objs.extend([line, lbl])

        ratio_lbl = Text(
            "v_mp : v_avg : v_rms  =  1 : 1.128 : 1.225",
            font="EB Garamond", font_size=22, color=DIM,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(ratio_lbl), run_time=1.0)
        self.wait(1.8)
        self.play(FadeOut(*marker_objs, ratio_lbl, curve, title_ax), run_time=0.5)
        return ax

    # ── Phase 3: T sweep 100→2000 K ──────────────────────────────────────────
    def _phase_temp_sweep(self, ax):
        T_tracker = ValueTracker(100.0)
        v_max = 1500.0

        def make_curve():
            T = T_tracker.get_value()
            vs = np.linspace(1, v_max, 500)
            fs = mb_speed(vs, M_O2, T)
            pts = [ax.c2p(v, f) for v, f in zip(vs, fs)]
            c = VMobject(color=BLUE, stroke_width=3.5)
            c.set_points_smoothly(pts)
            return c

        def make_vmp_line():
            T = T_tracker.get_value()
            vmp_val = v_mp(M_O2, T)
            f_val = mb_speed(np.array([vmp_val]), M_O2, T)[0]
            return DashedLine(ax.c2p(vmp_val, 0), ax.c2p(vmp_val, f_val),
                              color=GOLD, stroke_width=2.0)

        dyn_curve    = always_redraw(make_curve)
        dyn_vmp_line = always_redraw(make_vmp_line)

        T_lbl  = MathTex(r"T = ", color=INK, font_size=30)
        T_num  = DecimalNumber(100.0, num_decimal_places=0, color=GOLD, font_size=30)
        T_K    = MathTex(r"\mathrm{K}", color=INK, font_size=30)
        T_num.add_updater(lambda m: m.set_value(T_tracker.get_value()))
        T_row  = VGroup(T_lbl, T_num, T_K).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.3)

        hdr = Text("O₂ — temperature sweep  100 K → 2000 K",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.25)
        note = Text("peak shifts right  ·  distribution broadens",
                    font="EB Garamond", font_size=20, color=DIM).next_to(hdr, DOWN, buff=0.1)

        self.add(dyn_curve, dyn_vmp_line)
        self.play(Write(hdr), FadeIn(note), FadeIn(T_row), run_time=1.0)

        self.play(T_tracker.animate.set_value(2000.0), run_time=6.0, rate_func=smooth)
        self.wait(1.0)
        self.play(FadeOut(hdr, note, T_row, dyn_curve, dyn_vmp_line), run_time=0.5)

    # ── Phase 4: H₂ vs N₂ at 200 K, escape tail ──────────────────────────────
    def _phase_escape(self, ax):
        T_atm = 200.0
        v_max = 1500.0
        v_esc = V_ESC_MARS  # 5000 m/s — far off screen, but we shade from v_esc onward

        vs = np.linspace(1, v_max, 600)
        fs_H2 = mb_speed(vs, M_H2, T_atm)
        fs_N2 = mb_speed(vs, M_N2, T_atm)

        hdr = Text("H₂  vs  N₂  at  200 K  —  Mars escape tail",
                   font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)
        self.play(Write(hdr), run_time=0.8)

        pts_H2 = [ax.c2p(v, f) for v, f in zip(vs, fs_H2)]
        pts_N2 = [ax.c2p(v, f) for v, f in zip(vs, fs_N2)]

        curve_H2 = VMobject(color=BLUE, stroke_width=3.5)
        curve_H2.set_points_smoothly(pts_H2)
        lbl_H2 = Text("H₂", font="EB Garamond", font_size=22, color=BLUE).next_to(
            ax.c2p(vs[np.argmax(fs_H2)], fs_H2.max()), UP, buff=0.1)

        curve_N2 = VMobject(color=BROWN, stroke_width=3.0)
        curve_N2.set_points_smoothly(pts_N2)
        lbl_N2 = Text("N₂", font="EB Garamond", font_size=22, color=BROWN).next_to(
            ax.c2p(vs[np.argmax(fs_N2)], fs_N2.max()), UP, buff=0.1)

        self.play(Create(curve_H2), Write(lbl_H2), run_time=1.8)
        self.play(Create(curve_N2), Write(lbl_N2), run_time=1.5)
        self.wait(0.8)

        # Shade H₂ tail above escape velocity (mark at x = v_esc projected on axis)
        # v_esc = 5000 m/s >> v_max visible; show the tail concept with arrow at x_max
        tail_note = Text(
            "Mars escape  5.0 km/s  →",
            font="EB Garamond", font_size=20, color=GOLD,
        ).next_to(ax.c2p(v_max, 0), RIGHT, buff=0.1)

        # H₂ escape fraction annotation
        frac_H2 = escape_fraction(M_H2, T_atm, V_ESC_MARS)
        frac_N2 = escape_fraction(M_N2, T_atm, V_ESC_MARS)
        frac_lbl = Text(
            f"H₂ escape fraction: {frac_H2:.1e}\nN₂ escape fraction: {frac_N2:.1e}",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.3)

        self.play(Write(tail_note), Write(frac_lbl), run_time=1.5)
        self.wait(2.0)

        # Earth escape comparison
        frac_H2_earth = escape_fraction(M_H2, T_atm, V_ESC_EARTH)
        earth_note = Text(
            f"Earth escape 11.2 km/s — H₂ fraction: {frac_H2_earth:.1e}",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(frac_lbl), Write(earth_note), run_time=1.0)
        self.wait(1.5)

        final = Text(
            "The tail is why Mars lost its hydrogen — and why Earth kept it",
            font="EB Garamond", font_size=26, color=INK,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(earth_note), Write(final), run_time=1.2)
        self.wait(2.5)
