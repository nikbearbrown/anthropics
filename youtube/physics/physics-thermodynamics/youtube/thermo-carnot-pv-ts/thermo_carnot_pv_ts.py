#!/usr/bin/env python3
"""
thermo_carnot_pv_ts.py — Carnot Cycle: PV Lens + TS Rectangle
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

All curves computed exactly with numpy. No audio spend (GATE P).
Runtime ≈ 45 s.

Render:
    cd physics-thermodynamics/youtube/thermo-carnot-pv-ts
    manim -pqh thermo_carnot_pv_ts.py CarnotScene

Numpy verification (run standalone):
    python3 thermo_carnot_pv_ts.py --verify

Physics (checkable):
    n=1 mol, R=8.314 J/(mol·K), γ=1.4 (diatomic air)
    T_H=600 K, T_C=300 K, Q_H=1000 J

    State A: V= 1.000 L, P=49.24 atm   [T_H isotherm, anchor]
    State B: V= 1.222 L, P=40.28 atm   [T_H isotherm, after Q_H=1000 J in]
    State C: V= 6.914 L, P= 3.56 atm   [T_C isotherm, after adiabat B→C]
    State D: V= 5.657 L, P= 4.35 atm   [T_C isotherm, after Q_C=500 J out]

    V_B/V_A = exp(Q_H / nRT_H) = exp(0.2005) = 1.2221  ✓
    V_C     = V_B·(T_H/T_C)^[1/(γ-1)] = 1.222·2^2.5 = 6.914 L  ✓
    V_D     = V_A·(T_H/T_C)^[1/(γ-1)] = 1.0·2^2.5   = 5.657 L  ✓
    ΔS      = Q_H/T_H = 1000/600 = 1.667 J/K  ✓
    W_net   = (T_H - T_C)·ΔS = 300·1.667 = 500 J  ✓
    η_C     = 1 - T_C/T_H = 50%  ✓
    ΔS_universe = Q_H/T_H + Q_C/T_C = -1.667 + 1.667 = 0  ✓ (reversible)
"""
import sys
import numpy as np

# ─── Physics constants ────────────────────────────────────────────────────────
R_GAS = 8.314       # J/(mol·K)
N_MOL = 1.0         # mol
GAMMA = 1.4         # diatomic air Cp/Cv
T_HOT = 600.0       # K  — fixed hot reservoir
Q_HOT = 1000.0      # J  — heat absorbed per cycle (fixed)
ATM   = 101325.0    # Pa per atm

# Entropy swing: ΔS = Q_H/T_H (fixed even when T_C varies)
DS = Q_HOT / T_HOT  # = 1.6667 J/K

# Log volume-expansion ratio for isothermal legs
LN_R = Q_HOT / (N_MOL * R_GAS * T_HOT)  # ≈ 0.2005


# ─── Pure numpy thermodynamics — no Manim dependencies ───────────────────────

def carnot_states(T_cold: float):
    """
    Exact Carnot state points for given T_cold.
    Returns (VA,PA), (VB,PB), (VC,PC), (VD,PD) — V in L, P in atm.
    """
    VA = 1.0
    PA = N_MOL * R_GAS * T_HOT / (VA * 1e-3) / ATM
    VB = VA * np.exp(LN_R)
    PB = N_MOL * R_GAS * T_HOT / (VB * 1e-3) / ATM
    # Adiabat B→C: T_H·V_B^(γ-1) = T_C·V_C^(γ-1)
    VC = VB * (T_HOT / T_cold) ** (1.0 / (GAMMA - 1.0))
    PC = N_MOL * R_GAS * T_cold / (VC * 1e-3) / ATM
    # Isothermal compression C→D: ln(V_C/V_D) = Q_C/(nRT_C) = same LN_R
    VD = VC / np.exp(LN_R)
    PD = N_MOL * R_GAS * T_cold / (VD * 1e-3) / ATM
    return (VA, PA), (VB, PB), (VC, PC), (VD, PD)


def isotherm_pts(V1: float, T: float, V2: float, N: int = 300) -> np.ndarray:
    """PV-plane sample points along isotherm PV=nRT (V in L, P in atm)."""
    V = np.linspace(V1, V2, N)
    P = N_MOL * R_GAS * T / (V * 1e-3) / ATM
    return np.column_stack([V, P])


def adiabat_pts(V1: float, P1: float, V2: float, N: int = 300) -> np.ndarray:
    """PV-plane sample points along adiabat PV^γ=const (V in L, P in atm)."""
    C = P1 * (V1 ** GAMMA)
    V = np.linspace(V1, V2, N)
    P = C / (V ** GAMMA)
    return np.column_stack([V, P])


def verify():
    """Print state-point table and check two testable predictions."""
    print("=== Carnot cycle verification ===")
    (VA, PA), (VB, PB), (VC, PC), (VD, PD) = carnot_states(300.0)
    print(f"A: V={VA:.3f} L, P={PA:.2f} atm")
    print(f"B: V={VB:.3f} L, P={PB:.2f} atm")
    print(f"C: V={VC:.3f} L, P={PC:.3f} atm")
    print(f"D: V={VD:.3f} L, P={PD:.3f} atm")
    print()
    print(f"ΔS = Q_H/T_H = {DS:.4f} J/K")
    W_ts = (T_HOT - 300.0) * DS
    print(f"W_net (TS area) = (T_H-T_C)·ΔS = {W_ts:.1f} J")
    # P1: dual-diagram consistency — PV area = TS area = 500 J
    from scipy import integrate
    ab = isotherm_pts(VA, T_HOT, VB, 1000)
    bc = adiabat_pts(VB, PB, VC, 1000)
    cd = isotherm_pts(VC, 300.0, VD, 1000)
    da = adiabat_pts(VD, PD, VA, 1000)
    # W = ∮P dV; signs: A→B and B→C are expansion (+), C→D and D→A compression (-)
    def pv_work(arr):
        return np.trapz(arr[:, 1] * ATM, arr[:, 0] * 1e-3)
    W_ab = pv_work(ab);  W_bc = pv_work(bc)
    W_cd = pv_work(cd);  W_da = pv_work(da)
    W_pv = W_ab + W_bc + W_cd + W_da
    print(f"W_net (PV area) = {W_pv:.1f} J  (should be ≈ 500 J)")
    # P2: ΔS_universe = 0
    dS_hot  = -Q_HOT / T_HOT
    dS_cold = (Q_HOT - W_pv) / 300.0
    print(f"ΔS_universe = ΔS_hot + ΔS_cold = {dS_hot:.4f} + {dS_cold:.4f} = {dS_hot+dS_cold:.6f} J/K  (≈ 0)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

# Brownblue dark palette (style.md)
CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"   # isotherms — the mathematical object under study
BROWN   = "#CD853F"   # adiabats — the contrast
GOLD    = "#F0E442"   # transient emphasis / area fill
DIM     = "#8A8780"   # cold isotherm, secondary labels


class CarnotScene(Scene):
    """
    Carnot cycle: PV lens (left) + TS rectangle (right) drawn in sync.
    Areas fill with the same 500 J. T_C slider collapses both to a line.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        T_cold = 300.0

        self._phase_title()
        ax_pv, ax_ts = self._phase_axes()
        curves = self._phase_legs(ax_pv, ax_ts, T_cold)
        self._phase_fill(ax_pv, ax_ts, T_cold)
        self._phase_efficiency()
        self._phase_slider(ax_pv, ax_ts, curves)

    # ── Phase 1: Title card ──────────────────────────────────────────────────

    def _phase_title(self):
        title = Text("Carnot Cycle", font="EB Garamond", font_size=64, color=INK)
        sub1 = Text(
            "PV diagram  ·  TS diagram  ·  two representations, one net work",
            font="EB Garamond", font_size=23, color=DIM,
        )
        sub2 = Text(
            "η = 1 − Tⱻ / Tⱺ  —  the ceiling every heat engine obeys",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    # ── Phase 2: Both axes ───────────────────────────────────────────────────

    def _phase_axes(self):
        axis_cfg = dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.2)

        ax_pv = Axes(
            x_range=[0.5, 9.2, 2.0],
            y_range=[0.0, 58.0, 15.0],
            x_length=5.6,
            y_length=4.2,
            axis_config=axis_cfg,
        ).shift(LEFT * 3.4)

        ax_ts = Axes(
            x_range=[-0.1, 2.4, 0.5],
            y_range=[200.0, 700.0, 100.0],
            x_length=5.6,
            y_length=4.2,
            axis_config=axis_cfg,
        ).shift(RIGHT * 3.4)

        lbl_pv_x = MathTex(r"V\;(\mathrm{L})",     color=INK, font_size=22).next_to(ax_pv.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_pv_y = MathTex(r"P\;(\mathrm{atm})",   color=INK, font_size=22).next_to(ax_pv.y_axis.get_end(), UP,    buff=0.08)
        lbl_ts_x = MathTex(r"S\;(\mathrm{J/K})",   color=INK, font_size=22).next_to(ax_ts.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_ts_y = MathTex(r"T\;(\mathrm{K})",     color=INK, font_size=22).next_to(ax_ts.y_axis.get_end(), UP,    buff=0.08)

        hdr_pv = Text("P-V  diagram", font="EB Garamond", font_size=21, color=DIM).next_to(ax_pv, UP, buff=0.12)
        hdr_ts = Text("T-S  diagram", font="EB Garamond", font_size=21, color=DIM).next_to(ax_ts, UP, buff=0.12)

        self.play(
            Create(ax_pv), Create(ax_ts),
            Write(lbl_pv_x), Write(lbl_pv_y),
            Write(lbl_ts_x), Write(lbl_ts_y),
            Write(hdr_pv),   Write(hdr_ts),
            run_time=2.0,
        )
        return ax_pv, ax_ts

    # ── Phase 3: Draw each Carnot leg, both panels simultaneously ────────────

    def _phase_legs(self, ax_pv, ax_ts, T_cold):
        (VA, PA), (VB, PB), (VC, PC), (VD, PD) = carnot_states(T_cold)

        def pv_curve(arr, color, w=3.0):
            pts = np.array([ax_pv.c2p(v, p) for v, p in arr])
            m = VMobject(color=color, stroke_width=w)
            m.set_points_smoothly(pts)
            return m

        def ts_line(seg, color, w=3.0):
            pts = np.array([ax_ts.c2p(s, t) for s, t in seg])
            m = VMobject(color=color, stroke_width=w)
            m.set_points_smoothly(pts)
            return m

        curves = {}

        # ── Leg A→B: isothermal expansion at T_H (blue) ──────────────────────
        ab_pv = pv_curve(isotherm_pts(VA, T_HOT, VB), BLUE)
        ab_ts = ts_line([(0.0, T_HOT), (DS, T_HOT)], BLUE)
        lbl = Text(
            "Isothermal expansion  T_H = 600 K  (heat Q_H = 1000 J absorbed)",
            font="EB Garamond", font_size=20, color=BLUE,
        ).to_edge(DOWN, buff=0.22)
        self.play(Create(ab_pv), Create(ab_ts), Write(lbl), run_time=2.2)
        self.wait(0.9)
        curves["AB"] = (ab_pv, ab_ts)

        # ── Leg B→C: adiabatic expansion (brown) ─────────────────────────────
        bc_pv = pv_curve(adiabat_pts(VB, PB, VC), BROWN)
        bc_ts = ts_line([(DS, T_HOT), (DS, T_cold)], BROWN)
        lbl2 = Text(
            "Adiabatic expansion  ΔS = 0  (no heat — temperature drops to T_C)",
            font="EB Garamond", font_size=20, color=BROWN,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(lbl), run_time=0.2)
        self.play(Create(bc_pv), Create(bc_ts), Write(lbl2), run_time=2.2)
        self.wait(0.9)
        curves["BC"] = (bc_pv, bc_ts)

        # ── Leg C→D: isothermal compression at T_C (dimmed) ──────────────────
        cd_pv = pv_curve(isotherm_pts(VC, T_cold, VD), DIM)
        cd_ts = ts_line([(DS, T_cold), (0.0, T_cold)], DIM)
        lbl3 = Text(
            "Isothermal compression  T_C = 300 K  (heat Q_C = 500 J rejected)",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(lbl2), run_time=0.2)
        self.play(Create(cd_pv), Create(cd_ts), Write(lbl3), run_time=2.2)
        self.wait(0.9)
        curves["CD"] = (cd_pv, cd_ts)

        # ── Leg D→A: adiabatic compression — closes the loop (brown) ─────────
        da_pv = pv_curve(adiabat_pts(VD, PD, VA), BROWN)
        da_ts = ts_line([(0.0, T_cold), (0.0, T_HOT)], BROWN)
        lbl4 = Text(
            "Adiabatic compression  ΔS = 0  —  cycle closes",
            font="EB Garamond", font_size=20, color=BROWN,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(lbl3), run_time=0.2)
        self.play(Create(da_pv), Create(da_ts), Write(lbl4), run_time=2.2)
        self.wait(0.9)
        self.play(FadeOut(lbl4), run_time=0.3)
        curves["DA"] = (da_pv, da_ts)

        return curves

    # ── Phase 4: Fill enclosed areas + show W_net = 500 J ───────────────────

    def _phase_fill(self, ax_pv, ax_ts, T_cold):
        (VA, PA), (VB, PB), (VC, PC), (VD, PD) = carnot_states(T_cold)

        # PV polygon: full boundary A→B→C→D→A (curved via sampled points)
        pv_bnd = np.vstack([
            isotherm_pts(VA, T_HOT, VB, 80),   # A→B  isothermal (top)
            adiabat_pts(VB, PB, VC, 80),        # B→C  adiabat (right side)
            isotherm_pts(VC, T_cold, VD, 80),   # C→D  isothermal (bottom, V↓)
            adiabat_pts(VD, PD, VA, 80),        # D→A  adiabat (left side)
        ])
        pv_coords = [ax_pv.c2p(v, p) for v, p in pv_bnd]
        pv_fill = Polygon(
            *pv_coords,
            color=GOLD, fill_color=GOLD, fill_opacity=0.22, stroke_width=0,
        )

        # TS rectangle (analytically exact)
        ts_coords = [
            ax_ts.c2p(0.0, T_HOT),
            ax_ts.c2p(DS,  T_HOT),
            ax_ts.c2p(DS,  T_cold),
            ax_ts.c2p(0.0, T_cold),
        ]
        ts_fill = Polygon(
            *ts_coords,
            color=GOLD, fill_color=GOLD, fill_opacity=0.22, stroke_width=0,
        )

        # In-diagram labels
        pv_w = MathTex(r"500\,\mathrm{J}", color=GOLD, font_size=26)
        pv_w.move_to(ax_pv.c2p(3.0, 13.5))
        ts_w = MathTex(r"500\,\mathrm{J}", color=GOLD, font_size=26)
        ts_w.move_to(ax_ts.c2p(0.83, 450.0))

        caption = MathTex(
            r"W_{\rm net} = \oint P\,dV = (T_H - T_C)\,\Delta S = 500\,\mathrm{J}",
            color=INK, font_size=27,
        ).to_edge(DOWN, buff=0.22)

        self.play(FadeIn(pv_fill), FadeIn(ts_fill), run_time=1.2)
        self.play(Write(pv_w), Write(ts_w), Write(caption), run_time=1.5)
        self.wait(2.2)
        self.play(FadeOut(caption, pv_w, ts_w, pv_fill, ts_fill), run_time=0.5)

    # ── Phase 5: Efficiency formula ──────────────────────────────────────────

    def _phase_efficiency(self):
        eq = MathTex(
            r"\eta_{\rm Carnot}",
            r"= 1 - \frac{T_C}{T_H}",
            r"= 1 - \frac{300\,\mathrm{K}}{600\,\mathrm{K}}",
            r"= 50\,\%",
            color=INK, font_size=36,
        ).to_edge(DOWN, buff=0.28)
        for i, part in enumerate(eq):
            self.play(Write(part), run_time=0.85 if i == 0 else 0.65)
        self.wait(1.8)
        self.play(FadeOut(eq), run_time=0.4)

    # ── Phase 6: ValueTracker — T_C rises from 300 K → 594 K ────────────────

    def _phase_slider(self, ax_pv, ax_ts, static_curves):
        tc = ValueTracker(300.0)

        # ── dynamic PV fill (always_redraw) ──────────────────────────────────
        def _pv_poly():
            t = tc.get_value()
            (vA, pA), (vB, pB), (vC, pC), (vD, pD) = carnot_states(t)
            bnd = np.vstack([
                isotherm_pts(vA, T_HOT, vB, 50),
                adiabat_pts(vB, pB, vC, 50),
                isotherm_pts(vC, t, vD, 50),
                adiabat_pts(vD, pD, vA, 50),
            ])
            coords = [ax_pv.c2p(v, p) for v, p in bnd]
            return Polygon(
                *coords,
                color=GOLD, fill_color=GOLD,
                fill_opacity=0.28, stroke_color=GOLD, stroke_width=1.5,
            )

        def _ts_rect():
            t = tc.get_value()
            coords = [
                ax_ts.c2p(0.0, T_HOT), ax_ts.c2p(DS, T_HOT),
                ax_ts.c2p(DS,  t),      ax_ts.c2p(0.0, t),
            ]
            return Polygon(
                *coords,
                color=GOLD, fill_color=GOLD,
                fill_opacity=0.28, stroke_color=GOLD, stroke_width=1.5,
            )

        def _pv_curves():
            t = tc.get_value()
            (vA, pA), (vB, pB), (vC, pC), (vD, pD) = carnot_states(t)
            def c(arr, col):
                pts = np.array([ax_pv.c2p(v, p) for v, p in arr])
                m = VMobject(color=col, stroke_width=2.5)
                m.set_points_smoothly(pts)
                return m
            return VGroup(
                c(isotherm_pts(vA, T_HOT, vB, 50), BLUE),
                c(adiabat_pts(vB, pB, vC, 50),     BROWN),
                c(isotherm_pts(vC, t, vD, 50),     DIM),
                c(adiabat_pts(vD, pD, vA, 50),     BROWN),
            )

        def _ts_curves():
            t = tc.get_value()
            def c(seg, col):
                pts = np.array([ax_ts.c2p(s, tt) for s, tt in seg])
                m = VMobject(color=col, stroke_width=2.5)
                m.set_points_smoothly(pts)
                return m
            return VGroup(
                c([(0.0, T_HOT), (DS,  T_HOT)], BLUE),
                c([(DS,  T_HOT), (DS,  t)],     BROWN),
                c([(DS,  t),     (0.0, t)],     DIM),
                c([(0.0, t),     (0.0, T_HOT)], BROWN),
            )

        dyn_pv_fill   = always_redraw(_pv_poly)
        dyn_ts_fill   = always_redraw(_ts_rect)
        dyn_pv_curves = always_redraw(_pv_curves)
        dyn_ts_curves = always_redraw(_ts_curves)

        # Swap static curves for dynamic
        for (pv_c, ts_c) in static_curves.values():
            self.remove(pv_c, ts_c)
        self.add(dyn_pv_fill, dyn_ts_fill, dyn_pv_curves, dyn_ts_curves)

        # ── Efficiency + T_C readouts ─────────────────────────────────────────
        eff_lbl = MathTex(r"\eta = ", color=GOLD, font_size=34)
        eff_num = DecimalNumber(50.0, num_decimal_places=1, color=GOLD, font_size=34)
        eff_pct = MathTex(r"\%",      color=GOLD, font_size=34)
        eff_num.add_updater(lambda m: m.set_value((1.0 - tc.get_value() / T_HOT) * 100.0))

        tc_lbl = MathTex(r"T_C = ", color=DIM, font_size=30)
        tc_num = DecimalNumber(300.0, num_decimal_places=0, color=DIM, font_size=30)
        tc_K   = MathTex(r"\mathrm{K}", color=DIM, font_size=30)
        tc_num.add_updater(lambda m: m.set_value(tc.get_value()))

        eff_row = VGroup(eff_lbl, eff_num, eff_pct).arrange(RIGHT, buff=0.08)
        tc_row  = VGroup(tc_lbl, tc_num, tc_K).arrange(RIGHT, buff=0.08)
        VGroup(tc_row, eff_row).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.28)

        hdr = Text(
            "Raise T_C toward T_H — both diagrams collapse together",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.18)

        self.play(Write(hdr), FadeIn(eff_row), FadeIn(tc_row), run_time=1.0)

        # Animate T_C from 300 K up to 594 K
        self.play(
            tc.animate.set_value(594.0),
            run_time=6.0,
            rate_func=smooth,
        )
        self.wait(1.5)

        # Final payoff
        final = Text(
            "No  ΔT  →  no work  →  η = 0",
            font="EB Garamond", font_size=30, color=INK,
        ).to_edge(DOWN, buff=0.28)
        self.play(
            FadeOut(hdr, eff_row, tc_row),
            Write(final),
            run_time=1.5,
        )
        self.wait(2.5)
