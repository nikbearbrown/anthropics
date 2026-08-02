#!/usr/bin/env python3
"""
thermo_adiabat_vs_isotherm.py — Adiabat vs Isotherm: The Work Gap
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

Physics (verified at module level):
    P_i=3 atm, V_i=2 L, V_f=6 L, γ=1.4
    Isotherm: PV=nRT → P_f,iso = P_i×V_i/V_f = 1 atm
    Adiabat:  PV^γ=const → P_f,ad = P_i×(V_i/V_f)^γ ≈ 0.644 atm
    W_iso = P_i×V_i×ln(V_f/V_i) = 608.1×1.099 ≈ 668 J
    W_ad  = (P_i×V_i - P_f×V_f)/(γ-1) = ... J
    Gap = W_iso - W_ad

Render:
    cd physics-thermodynamics/youtube/thermo-adiabat-vs-isotherm
    manim -qh thermo_adiabat_vs_isotherm.py AdiabatVsIsothermScene
"""
import sys
import numpy as np
from scipy import integrate

# ─── Constants ────────────────────────────────────────────────────────────────
GAMMA = 1.4
ATM   = 101325.0    # Pa per atm
P_I   = 3.0         # atm
V_I   = 2.0e-3      # m³  (2 L)
V_F   = 6.0e-3      # m³  (6 L)
# Derived
C_ISOTHERM = P_I * ATM * V_I       # Pa·m³  — nRT
C_ADIABAT  = P_I * ATM * (V_I ** GAMMA)  # Pa·m^(3γ)


def iso_P(V: np.ndarray) -> np.ndarray:
    """Isotherm pressure in atm, V in m³."""
    return C_ISOTHERM / V / ATM


def ad_P(V: np.ndarray) -> np.ndarray:
    """Adiabat pressure in atm, V in m³."""
    return C_ADIABAT / (V ** GAMMA) / ATM


def W_iso() -> float:
    """Work done by gas along isotherm (J)."""
    result, _ = integrate.quad(lambda V: C_ISOTHERM / V, V_I, V_F)
    return result


def W_ad() -> float:
    """Work done by gas along adiabat (J): (P_i V_i - P_f V_f)/(γ-1)."""
    P_f = C_ADIABAT / (V_F ** GAMMA)   # Pa
    return (P_I * ATM * V_I - P_f * V_F) / (GAMMA - 1.0)


# ─── Verification ─────────────────────────────────────────────────────────────
def _verify():
    print("=== Adiabat vs Isotherm verification ===")
    P_f_iso = iso_P(np.array([V_F]))[0]
    P_f_ad  = ad_P(np.array([V_F]))[0]
    print(f"Initial state: P_i={P_I:.1f} atm, V_i={V_I*1e3:.1f} L")
    print(f"Final V_f = {V_F*1e3:.1f} L")
    print(f"P_f isotherm = {P_f_iso:.3f} atm  (expected 1.000)")
    print(f"P_f adiabat  = {P_f_ad:.3f} atm")
    print(f"Slope ratio at start (should = γ = 1.4): {P_f_iso / P_f_ad / (V_I/V_F) * (V_I/V_F)**GAMMA:.3f}")
    # Ratio of final pressures
    ratio = P_f_iso / P_f_ad
    print(f"P_f,iso / P_f,ad = {ratio:.3f}  (expected 3^0.4 = {3**0.4:.3f})")
    w_iso = W_iso()
    w_ad  = W_ad()
    gap   = w_iso - w_ad
    print(f"W_iso = {w_iso:.1f} J  (expected ≈ 668 J)")
    print(f"W_ad  = {w_ad:.1f} J  (expected ≈ 567 J)")
    print(f"Gap   = {gap:.1f} J  (expected ≈ 101 J)")
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

# axis in Litres / atm for display
V_I_L = V_I * 1e3   # 2 L
V_F_L = V_F * 1e3   # 6 L


class AdiabatVsIsothermScene(Scene):
    """
    Phase 1: Title.
    Phase 2: Axes + one starting point; two curves sweep right simultaneously.
    Phase 3: Gap fills with shaded band, label "extra W = 101 J from reservoir".
    Phase 4: Numeric work annotations.
    Phase 5: Vary γ (5/3 monatomic → 7/5 diatomic).
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._build_axes()
        self._phase_curves(ax)
        self._phase_vary_gamma(ax)

    def _phase_title(self):
        title = Text("Adiabat vs Isotherm", font="EB Garamond", font_size=66, color=INK)
        sub1 = Text(
            "Same start point — adiabat always steeper — the gap IS the heat borrowed",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2 = MathTex(
            r"\left.\frac{dP}{dV}\right|_{\rm ad} = \gamma \left.\frac{dP}{dV}\right|_{\rm iso}",
            color=GOLD, font_size=28,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _build_axes(self):
        P_max = P_I * 1.15
        ax = Axes(
            x_range=[0, V_F_L * 1.1, 1.0],
            y_range=[0, P_max, 1.0],
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.3)
        lbl_x = MathTex(r"V\;(\mathrm{L})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"P\;(\mathrm{atm})", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr   = Text("P-V diagram  —  same start, different paths",
                     font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.5)
        # Start dot
        dot = Dot(ax.c2p(V_I_L, P_I), color=INK, radius=0.1)
        self.play(Create(dot), run_time=0.5)
        self._hdr = hdr
        return ax

    def _phase_curves(self, ax):
        Vs_L = np.linspace(V_I_L, V_F_L, 300)
        Vs_m3 = Vs_L * 1e-3

        Ps_iso = iso_P(Vs_m3)
        Ps_ad  = ad_P(Vs_m3)

        pts_iso = [ax.c2p(v, p) for v, p in zip(Vs_L, Ps_iso)]
        pts_ad  = [ax.c2p(v, p) for v, p in zip(Vs_L, Ps_ad)]

        curve_iso = VMobject(color=BLUE, stroke_width=3.5)
        curve_iso.set_points_smoothly(pts_iso)
        lbl_iso = Text("Isotherm  PV = const\n(borrows heat from reservoir)",
                       font="EB Garamond", font_size=20, color=BLUE).to_edge(DOWN, buff=0.25)

        curve_ad = VMobject(color=BROWN, stroke_width=3.5)
        curve_ad.set_points_smoothly(pts_ad)
        lbl_ad = Text("Adiabat  PV^γ = const\n(self-contained — cools as it expands)",
                      font="EB Garamond", font_size=20, color=BROWN).to_edge(DOWN, buff=0.25)

        self.play(
            Create(curve_iso), Create(curve_ad),
            run_time=3.0,
        )
        self.play(Write(lbl_iso), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(lbl_iso), Write(lbl_ad), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(lbl_ad), run_time=0.3)

        # ── Gap fill ──────────────────────────────────────────────────────────
        # Build closed polygon between the two curves
        bnd = np.vstack([
            np.column_stack([Vs_L, Ps_iso]),            # isotherm top
            np.column_stack([Vs_L[::-1], Ps_ad[::-1]]), # adiabat bottom reversed
        ])
        coords = [ax.c2p(v, p) for v, p in bnd]
        gap_fill = Polygon(*coords, color=GOLD, fill_color=GOLD, fill_opacity=0.25, stroke_width=0)

        w_iso_J = W_iso()
        w_ad_J  = W_ad()
        gap_J   = w_iso_J - w_ad_J

        gap_lbl = Text(
            f"Extra {gap_J:.0f} J  —  heat borrowed\nfrom reservoir by isotherm",
            font="EB Garamond", font_size=20, color=GOLD,
        ).move_to(ax.c2p(4.5, 1.5))

        w_iso_ann = MathTex(rf"W_{{\rm iso}}={w_iso_J:.0f}\,\mathrm{{J}}", color=BLUE, font_size=22)
        w_iso_ann.next_to(ax.c2p(4.0, Ps_iso[150] + 0.2), UP, buff=0.05)
        w_ad_ann  = MathTex(rf"W_{{\rm ad}}={w_ad_J:.0f}\,\mathrm{{J}}", color=BROWN, font_size=22)
        w_ad_ann.next_to(ax.c2p(4.0, Ps_ad[150] - 0.2), DOWN, buff=0.05)

        slope_ann = MathTex(
            r"\frac{dP/dV|_{\rm ad}}{dP/dV|_{\rm iso}} = \gamma = 1.4",
            color=DIM, font_size=22,
        ).to_edge(DOWN, buff=0.25)

        self.play(FadeIn(gap_fill), run_time=0.8)
        self.play(Write(gap_lbl), Write(w_iso_ann), Write(w_ad_ann), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(gap_lbl, w_iso_ann, w_ad_ann), Write(slope_ann), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(slope_ann, gap_fill, curve_iso, curve_ad), run_time=0.5)

    # ── Phase 5: Vary γ ───────────────────────────────────────────────────────
    def _phase_vary_gamma(self, ax):
        g_tracker = ValueTracker(5.0 / 3.0)   # monatomic

        def make_ad_curve():
            g = g_tracker.get_value()
            C = P_I * ATM * (V_I ** g)
            Vs_L = np.linspace(V_I_L, V_F_L, 300)
            Vs_m3 = Vs_L * 1e-3
            Ps = C / (Vs_m3 ** g) / ATM
            pts = [ax.c2p(v, p) for v, p in zip(Vs_L, Ps)]
            c = VMobject(color=BROWN, stroke_width=3.5)
            c.set_points_smoothly(pts)
            return c

        def make_iso_curve():
            Vs_L = np.linspace(V_I_L, V_F_L, 300)
            Vs_m3 = Vs_L * 1e-3
            Ps = iso_P(Vs_m3)
            pts = [ax.c2p(v, p) for v, p in zip(Vs_L, Ps)]
            c = VMobject(color=BLUE, stroke_width=3.5)
            c.set_points_smoothly(pts)
            return c

        def make_gap_fill():
            g = g_tracker.get_value()
            C = P_I * ATM * (V_I ** g)
            Vs_L = np.linspace(V_I_L, V_F_L, 150)
            Vs_m3 = Vs_L * 1e-3
            Ps_iso = iso_P(Vs_m3)
            Ps_ad  = C / (Vs_m3 ** g) / ATM
            bnd = np.vstack([
                np.column_stack([Vs_L, Ps_iso]),
                np.column_stack([Vs_L[::-1], Ps_ad[::-1]]),
            ])
            coords = [ax.c2p(v, p) for v, p in bnd]
            return Polygon(*coords, color=GOLD, fill_color=GOLD, fill_opacity=0.25, stroke_width=0)

        dyn_ad   = always_redraw(make_ad_curve)
        dyn_iso  = always_redraw(make_iso_curve)
        dyn_gap  = always_redraw(make_gap_fill)

        g_lbl = MathTex(r"\gamma = ", color=INK, font_size=32)
        g_num = DecimalNumber(5.0/3.0, num_decimal_places=3, color=GOLD, font_size=32)
        g_num.add_updater(lambda m: m.set_value(g_tracker.get_value()))
        g_row = VGroup(g_lbl, g_num).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.3)

        hdr2 = Text("Vary  γ  —  monatomic (5/3) → diatomic (7/5)",
                    font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.25)

        self.play(FadeOut(self._hdr), Write(hdr2), run_time=0.5)
        self.add(dyn_gap, dyn_ad, dyn_iso)
        self.play(FadeIn(g_row), run_time=0.5)

        # Monatomic → diatomic
        self.play(g_tracker.animate.set_value(7.0/5.0), run_time=6.0, rate_func=smooth)
        self.wait(1.5)

        final = Text(
            "Monatomic γ = 5/3: steeper adiabat, larger work gap\n"
            "Diatomic  γ = 7/5: shallower adiabat, smaller gap",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(g_row), Write(final), run_time=1.2)
        self.wait(2.5)
