#!/usr/bin/env python3
"""
thermo_carnot_cycle.py — Carnot Cycle: PV Lens and η_C = 1 − T_C/T_H
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-thermodynamics book.

Render:
    cd physics-plus-one-thermodynamics/youtube/thermo-carnot-cycle
    manim -qh thermo_carnot_cycle.py CarnotCycleScene

Physics (n=1 mol, R=8.314, γ=1.4):
    Coal plant: T_H=823 K, T_C=298 K → η_C = 63.8%
    Nuclear PWR: T_H=600 K, T_C=298 K → η_C = 50.3%
    Human body: T_H=310 K, T_C=298 K → η_C = 3.9%
"""
import sys
import numpy as np

R_GAS = 8.314
N_MOL = 1.0
GAMMA = 1.4
ATM   = 101325.0


def carnot_states(T_H: float, T_C: float, Q_H: float = 1000.0):
    """State points for Carnot cycle. V in L, P in atm."""
    LN_R = Q_H / (N_MOL * R_GAS * T_H)
    VA = 1.0
    PA = N_MOL * R_GAS * T_H / (VA * 1e-3) / ATM
    VB = VA * np.exp(LN_R)
    PB = N_MOL * R_GAS * T_H / (VB * 1e-3) / ATM
    VC = VB * (T_H / T_C) ** (1.0 / (GAMMA - 1.0))
    PC = N_MOL * R_GAS * T_C / (VC * 1e-3) / ATM
    VD = VC / np.exp(LN_R)
    PD = N_MOL * R_GAS * T_C / (VD * 1e-3) / ATM
    return (VA, PA), (VB, PB), (VC, PC), (VD, PD)


def isotherm(V1, T, V2, N=200):
    V = np.linspace(V1, V2, N)
    P = N_MOL * R_GAS * T / (V * 1e-3) / ATM
    return np.column_stack([V, P])


def adiabat(V1, P1, V2, N=200):
    C = P1 * V1**GAMMA
    V = np.linspace(V1, V2, N)
    P = C / V**GAMMA
    return np.column_stack([V, P])


if __name__ == "__main__":
    print("=== Carnot Cycle Verification ===")
    for name, T_H, T_C in [("Coal", 823, 298), ("Nuclear", 600, 298), ("Body", 310, 298)]:
        eta = 1.0 - T_C / T_H
        print(f"  {name}: T_H={T_H}K T_C={T_C}K η_C={eta*100:.1f}%")
    # P1: coal plant
    assert abs((1 - 298/823) - 0.638) < 0.002, "P1 FAIL"
    # P2: T_H >> T_C → η → 1
    eta_high = 1 - 298/10000
    assert eta_high > 0.97, "P2 FAIL"
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

T_H_BASE = 823.0
T_C_BASE = 298.0
Q_H_VAL  = 1000.0


class CarnotCycleScene(Scene):
    """Carnot PV cycle + efficiency formula + T_H slider."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_legs(ax)
        self._phase_benchmarks()
        self._phase_slider(ax)

    def _phase_title(self):
        title = Text("Carnot Cycle", font="EB Garamond", font_size=60, color=INK)
        sub = Text("The efficiency ceiling no heat engine can exceed",
                   font="EB Garamond", font_size=24, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[0.5, 16, 4],
            y_range=[0, 70, 20],
            x_length=9.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.1)
        x_lbl = MathTex(r"V\;(\mathrm{L})", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"P\;(\mathrm{atm})", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        self._ax = ax
        return ax

    def _phase_legs(self, ax):
        (VA, PA), (VB, PB), (VC, PC), (VD, PD) = carnot_states(T_H_BASE, T_C_BASE)

        def pv_vmob(arr, col, w=3.0):
            pts = [ax.c2p(v, p) for v, p in arr]
            m = VMobject(color=col, stroke_width=w)
            m.set_points_smoothly(pts)
            return m

        legs = [
            (isotherm(VA, T_H_BASE, VB), BLUE,
             "Isothermal expansion T_H = 823 K  (heat Q_H in)"),
            (adiabat(VB, PB, VC),       BROWN,
             "Adiabatic expansion  ΔS = 0  (temperature drops to T_C)"),
            (isotherm(VC, T_C_BASE, VD), DIM,
             "Isothermal compression T_C = 298 K  (heat Q_C rejected)"),
            (adiabat(VD, PD, VA),       BROWN,
             "Adiabatic compression  —  cycle closes"),
        ]

        curves = []
        for arr, col, caption in legs:
            c = pv_vmob(arr, col)
            lbl = Text(caption, font="EB Garamond", font_size=19, color=col
                       ).to_edge(DOWN, buff=0.25)
            self.play(Create(c), Write(lbl), run_time=1.8)
            self.wait(0.7)
            self.play(FadeOut(lbl), run_time=0.2)
            curves.append(c)

        # Fill enclosed area
        bnd = np.vstack([
            isotherm(VA, T_H_BASE, VB, 60),
            adiabat(VB, PB, VC, 60),
            isotherm(VC, T_C_BASE, VD, 60),
            adiabat(VD, PD, VA, 60),
        ])
        fill = Polygon(*[ax.c2p(v, p) for v, p in bnd],
                       color=GOLD, fill_color=GOLD, fill_opacity=0.25, stroke_width=0)
        area_lbl = MathTex(r"W_{\rm net}", color=GOLD, font_size=28).move_to(
            ax.c2p(4.0, 18.0))
        self.play(FadeIn(fill), Write(area_lbl), run_time=1.2)

        eta_eq = MathTex(
            r"\eta_C = 1-\frac{T_C}{T_H}=1-\frac{298}{823}=63.8\%",
            color=INK, font_size=30).to_edge(DOWN, buff=0.28)
        self.play(Write(eta_eq), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(fill, area_lbl, eta_eq, *curves), run_time=0.5)
        return curves

    def _phase_benchmarks(self):
        hdr = Text("Real engines vs Carnot ceiling", font="EB Garamond",
                   font_size=28, color=INK).to_edge(UP, buff=0.25)
        data = [
            ("Coal plant",    823, 298, 0.40),
            ("Natural gas",  1100, 310, 0.60),
            ("Nuclear PWR",   600, 310, 0.33),
            ("Car engine",    800, 310, 0.25),
            ("Human body",    310, 298, 0.08),
        ]
        rows = VGroup()
        for name, TH, TC, eta_real in data:
            eta_c = 1 - TC / TH
            row = Text(
                f"{name:20s}  η_C={eta_c*100:.0f}%   real≈{eta_real*100:.0f}%",
                font="EB Garamond", font_size=21, color=DIM)
            rows.add(row)
        rows.arrange(DOWN, buff=0.25).center()
        self.play(Write(hdr), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
        self.wait(2.5)
        self.play(FadeOut(hdr, rows), run_time=0.5)

    def _phase_slider(self, ax):
        th = ValueTracker(T_H_BASE)

        def _fill():
            TH = th.get_value()
            try:
                (VA, PA), (VB, PB), (VC, PC), (VD, PD) = carnot_states(TH, T_C_BASE)
                bnd = np.vstack([
                    isotherm(VA, TH, VB, 50),
                    adiabat(VB, PB, VC, 50),
                    isotherm(VC, T_C_BASE, VD, 50),
                    adiabat(VD, PD, VA, 50),
                ])
                return Polygon(*[ax.c2p(v, p) for v, p in bnd],
                               color=GOLD, fill_color=GOLD,
                               fill_opacity=0.28, stroke_color=GOLD, stroke_width=1.5)
            except Exception:
                return VMobject()

        dyn_fill = always_redraw(_fill)
        self.add(dyn_fill)

        eta_lbl = MathTex(r"\eta_C = ", color=GOLD, font_size=34)
        eta_num = DecimalNumber((1 - T_C_BASE / T_H_BASE) * 100, num_decimal_places=1,
                                color=GOLD, font_size=34)
        eta_pct = MathTex(r"\%", color=GOLD, font_size=34)
        eta_num.add_updater(lambda m: m.set_value((1 - T_C_BASE / th.get_value()) * 100))

        th_lbl = MathTex(r"T_H = ", color=DIM, font_size=30)
        th_num = DecimalNumber(T_H_BASE, num_decimal_places=0, color=DIM, font_size=30)
        th_K   = MathTex(r"\mathrm{K}", color=DIM, font_size=30)
        th_num.add_updater(lambda m: m.set_value(th.get_value()))

        eta_row = VGroup(eta_lbl, eta_num, eta_pct).arrange(RIGHT, buff=0.08)
        th_row  = VGroup(th_lbl, th_num, th_K).arrange(RIGHT, buff=0.08)
        VGroup(th_row, eta_row).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.25)

        hdr = Text("Raise T_H — the lens grows, efficiency rises",
                   font="EB Garamond", font_size=21, color=INK).to_edge(UP, buff=0.18)
        self.play(Write(hdr), FadeIn(eta_row), FadeIn(th_row), run_time=0.8)
        self.play(th.animate.set_value(2500.0), run_time=6.0, rate_func=smooth)
        self.wait(1.5)
        final = Text("T_H → ∞  means  η → 1 — but T_C → 0 K is harder",
                     font="EB Garamond", font_size=26, color=INK).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(hdr, eta_row, th_row), Write(final), run_time=1.2)
        self.wait(2.5)
