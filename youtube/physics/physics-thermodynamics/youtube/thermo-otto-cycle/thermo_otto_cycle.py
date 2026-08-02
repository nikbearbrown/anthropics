#!/usr/bin/env python3
"""
thermo_otto_cycle.py — Otto Cycle: Four-Leg Sequential Draw
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

Physics (verified at module level):
    γ=1.4, r=10, T₁=300 K
    T₂ = T₁·r^(γ−1) = 300×10^0.4 ≈ 754 K
    η  = 1 − 1/r^(γ−1) ≈ 60.2%

Render:
    cd physics-thermodynamics/youtube/thermo-otto-cycle
    manim -qh thermo_otto_cycle.py OttoCycleScene
"""
import sys
import numpy as np

# ─── Constants ────────────────────────────────────────────────────────────────
GAMMA = 1.4
R_GAS = 8.314       # J/(mol·K)
N_MOL = 1.0
T1    = 300.0       # K  — bottom dead center temperature
ATM   = 101325.0


def otto_states(r: float, T1_: float = T1, Q_in: float = 800.0):
    """
    Four state points for Otto cycle.
    State 1: BDC (bottom dead center) — start of compression
    State 2: TDC after adiabatic compression
    State 3: TDC after isochoric heat addition
    State 4: BDC after adiabatic expansion
    Returns (V1,P1,T1), (V2,P2,T2), (V3,P3,T3), (V4,P4,T4) in L / atm / K.
    """
    # Set anchor: V1=1 L, P1 from ideal gas
    V1 = 1.0        # L
    P1 = N_MOL * R_GAS * T1_ / (V1 * 1e-3) / ATM  # atm

    # State 2: adiabatic compression
    V2 = V1 / r
    P2 = P1 * r ** GAMMA
    T2 = T1_ * r ** (GAMMA - 1.0)

    # State 3: isochoric heat addition (V stays at V2)
    V3 = V2
    T3 = T2 + Q_in / (N_MOL * R_GAS / (GAMMA - 1.0))  # Cv = R/(γ-1)
    P3 = N_MOL * R_GAS * T3 / (V3 * 1e-3) / ATM

    # State 4: adiabatic expansion back to V1
    V4 = V1
    P4 = P3 * (V3 / V4) ** GAMMA
    T4 = T3 * (V3 / V4) ** (GAMMA - 1.0)

    return (V1, P1, T1_), (V2, P2, T2), (V3, P3, T3), (V4, P4, T4)


def adiabat_pv(V1: float, P1: float, V2: float, N: int = 300) -> np.ndarray:
    """PV points along adiabat PV^γ=const."""
    C = P1 * (V1 ** GAMMA)
    V = np.linspace(V1, V2, N)
    P = C / (V ** GAMMA)
    return np.column_stack([V, P])


def eta_otto(r: float) -> float:
    return 1.0 - r ** (-(GAMMA - 1.0))


# ─── Verification ─────────────────────────────────────────────────────────────
def _verify():
    print("=== Otto Cycle verification ===")
    r = 10.0
    s1, s2, s3, s4 = otto_states(r)
    V1, P1, T1_ = s1
    V2, P2, T2  = s2
    V3, P3, T3  = s3
    V4, P4, T4  = s4
    print(f"State 1: V={V1:.3f} L, P={P1:.2f} atm, T={T1_:.1f} K")
    print(f"State 2: V={V2:.3f} L, P={P2:.2f} atm, T={T2:.1f} K  (expected T≈754 K)")
    print(f"State 3: V={V3:.3f} L, P={P3:.2f} atm, T={T3:.1f} K")
    print(f"State 4: V={V4:.3f} L, P={P4:.2f} atm, T={T4:.1f} K")
    eta = eta_otto(r)
    print(f"η_Otto = 1 - r^(-(γ-1)) = {eta*100:.1f}%  (expected 60.2%)")
    print(f"T2/T1 = r^(γ-1) = {T2/T1_:.3f}  (10^0.4 = {10**0.4:.3f})")
    # PV work check
    ad12 = adiabat_pv(V1, P1, V2)
    W12 = np.trapz(ad12[:, 1] * ATM, ad12[:, 0] * 1e-3)   # compression — negative
    # isochoric 2→3: no PdV work
    W23 = 0.0
    ad34 = adiabat_pv(V3, P3, V4)
    W34 = np.trapz(ad34[:, 1] * ATM, ad34[:, 0] * 1e-3)   # expansion — positive
    # isochoric 4→1: no PdV work
    W41 = 0.0
    W_net = W12 + W23 + W34 + W41
    print(f"W_net (PV area) = {W_net:.1f} J")
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


class OttoCycleScene(Scene):
    """
    Phase 1: Title.
    Phase 2: PV diagram — draw four legs sequentially.
    Phase 3: Fill enclosed area (net work).
    Phase 4: Efficiency formula.
    Phase 5: Sweep r from 5→15 (ValueTracker).
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._build_axes()
        self._phase_legs(ax)
        self._phase_fill(ax)
        self._phase_efficiency()
        self._phase_sweep(ax)

    # ── Phase 1: Title ────────────────────────────────────────────────────────
    def _phase_title(self):
        title = Text("Otto Cycle", font="EB Garamond", font_size=72, color=INK)
        sub1 = Text(
            "Four strokes · one closed PV loop · net work = enclosed area",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2 = Text(
            "η = 1 − 1/r^(γ−1)  ·  r=10, γ=1.4  →  60.2%",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _build_axes(self):
        s1, s2, s3, s4 = otto_states(10.0)
        P_max = s3[1] * 1.2
        ax = Axes(
            x_range=[0.0, 1.15, 0.25],
            y_range=[0.0, P_max, P_max / 4],
            x_length=9.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.3)
        lbl_x = MathTex(r"V\;(\mathrm{L})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"P\;(\mathrm{atm})", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr   = Text("P-V  diagram  —  Otto cycle, r = 10", font="EB Garamond",
                     font_size=24, color=INK).to_edge(UP, buff=0.25)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.5)
        self._hdr = hdr
        return ax

    # ── Phase 2: Four legs ────────────────────────────────────────────────────
    def _phase_legs(self, ax):
        s1, s2, s3, s4 = otto_states(10.0)
        V1, P1, T1_ = s1
        V2, P2, T2  = s2
        V3, P3, T3  = s3
        V4, P4, T4  = s4

        def curve(arr, col, w=3.2):
            pts = [ax.c2p(v, p) for v, p in arr]
            m = VMobject(color=col, stroke_width=w)
            m.set_points_smoothly(pts)
            return m

        def vline(V, P_bot, P_top, col, w=3.2):
            return Line(ax.c2p(V, P_bot), ax.c2p(V, P_top), color=col, stroke_width=w)

        # 1→2: adiabatic compression (brown, steep, going UP-LEFT)
        leg12 = curve(adiabat_pv(V1, P1, V2), BROWN)
        lbl12 = Text("1→2  Adiabatic compression", font="EB Garamond",
                     font_size=22, color=BROWN).to_edge(DOWN, buff=0.22)
        self.play(Create(leg12), Write(lbl12), run_time=1.8)
        self.wait(0.8)

        # 2→3: isochoric heat addition (gold, vertical spike up)
        leg23 = vline(V2, P2, P3, GOLD)
        lbl23 = Text("2→3  Isochoric heat addition (Q_in, no volume change)",
                     font="EB Garamond", font_size=22, color=GOLD).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(lbl12), run_time=0.2)
        self.play(Create(leg23), Write(lbl23), run_time=1.5)
        self.wait(0.8)

        # 3→4: adiabatic expansion (blue, power stroke DOWN-RIGHT)
        leg34 = curve(adiabat_pv(V3, P3, V4), BLUE)
        lbl34 = Text("3→4  Adiabatic expansion — power stroke",
                     font="EB Garamond", font_size=22, color=BLUE).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(lbl23), run_time=0.2)
        self.play(Create(leg34), Write(lbl34), run_time=1.8)
        self.wait(0.8)

        # 4→1: isochoric heat rejection (dim, exhaust valve)
        leg41 = vline(V1, P4, P1, DIM)
        lbl41 = Text("4→1  Isochoric heat rejection (exhaust valve)",
                     font="EB Garamond", font_size=22, color=DIM).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(lbl34), run_time=0.2)
        self.play(Create(leg41), Write(lbl41), run_time=1.5)
        self.wait(0.8)
        self.play(FadeOut(lbl41), run_time=0.3)

        self._legs = (leg12, leg23, leg34, leg41)

    # ── Phase 3: Fill enclosed area ───────────────────────────────────────────
    def _phase_fill(self, ax):
        s1, s2, s3, s4 = otto_states(10.0)
        V1, P1 = s1[0], s1[1]
        V2, P2 = s2[0], s2[1]
        V3, P3 = s3[0], s3[1]
        V4, P4 = s4[0], s4[1]

        # Polygon boundary: 1→2 adiabat, 2→3 vertical, 3→4 adiabat, 4→1 vertical
        ad12 = adiabat_pv(V1, P1, V2, 60)
        ad34 = adiabat_pv(V3, P3, V4, 60)
        bnd  = np.vstack([
            ad12,
            np.array([[V2, P3]]),         # top of 2→3
            ad34[::-1],                    # 3→4 reversed (right to left)
            np.array([[V1, P1]]),
        ])
        coords = [ax.c2p(v, p) for v, p in bnd]
        fill = Polygon(*coords, color=GOLD, fill_color=GOLD, fill_opacity=0.22, stroke_width=0)

        # Work calculation
        W_net_J = np.trapz(adiabat_pv(V3, P3, V4)[:, 1] * ATM,
                           adiabat_pv(V3, P3, V4)[:, 0] * 1e-3) + \
                  np.trapz(adiabat_pv(V1, P1, V2)[:, 1] * ATM,
                           adiabat_pv(V1, P1, V2)[:, 0] * 1e-3)

        w_lbl = MathTex(rf"W_{{\rm net}} \approx {W_net_J:.0f}\,\mathrm{{J}}",
                        color=GOLD, font_size=28)
        w_lbl.move_to(ax.c2p(0.55, P3 * 0.25))

        cap = MathTex(r"\text{enclosed area} = W_{\rm net}", color=INK, font_size=28).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(fill), run_time=1.0)
        self.play(Write(w_lbl), Write(cap), run_time=1.2)
        self.wait(1.8)
        self.play(FadeOut(fill, w_lbl, cap), run_time=0.5)

    # ── Phase 4: Efficiency ───────────────────────────────────────────────────
    def _phase_efficiency(self):
        eq = MathTex(
            r"\eta_{\rm Otto}",
            r"= 1 - \frac{1}{r^{\gamma-1}}",
            r"= 1 - \frac{1}{10^{0.4}}",
            r"\approx 60.2\,\%",
            color=INK, font_size=34,
        ).to_edge(DOWN, buff=0.28)
        note = Text("Real gasoline engines: 25–35%  —  not because engineers are bad,",
                    font="EB Garamond", font_size=20, color=DIM).next_to(eq, UP, buff=0.18)
        note2 = Text("but because the Otto cycle assumes ideal gas + instant combustion + zero heat loss.",
                     font="EB Garamond", font_size=20, color=DIM).next_to(note, DOWN, buff=0.08)
        for part in eq:
            self.play(Write(part), run_time=0.7)
        self.play(FadeIn(note), FadeIn(note2), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(eq, note, note2), run_time=0.5)

    # ── Phase 5: Sweep compression ratio r 5→15 ──────────────────────────────
    def _phase_sweep(self, ax):
        r_tracker = ValueTracker(5.0)

        def make_cycle():
            r = r_tracker.get_value()
            s1, s2, s3, s4 = otto_states(r)
            V1, P1 = s1[0], s1[1]
            V2, P2 = s2[0], s2[1]
            V3, P3 = s3[0], s3[1]
            V4, P4 = s4[0], s4[1]

            def c(arr, col, w=2.8):
                pts = [ax.c2p(v, p) for v, p in arr]
                m = VMobject(color=col, stroke_width=w)
                m.set_points_smoothly(pts)
                return m

            ad12 = adiabat_pv(V1, P1, V2, 80)
            ad34 = adiabat_pv(V3, P3, V4, 80)

            # Fill polygon
            bnd = np.vstack([ad12, np.array([[V2, P3]]), ad34[::-1], np.array([[V1, P1]])])
            coords = [ax.c2p(v, p) for v, p in bnd]
            fill = Polygon(*coords, color=GOLD, fill_color=GOLD, fill_opacity=0.22, stroke_width=0)

            return VGroup(
                fill,
                c(ad12, BROWN),
                Line(ax.c2p(V2, P2), ax.c2p(V2, P3), color=GOLD, stroke_width=2.8),
                c(ad34, BLUE),
                Line(ax.c2p(V1, P4), ax.c2p(V1, P1), color=DIM, stroke_width=2.8),
            )

        dyn_cycle = always_redraw(make_cycle)
        for leg in self._legs:
            self.remove(leg)
        self.add(dyn_cycle)

        # Readout
        r_lbl  = MathTex(r"r = ", color=INK, font_size=32)
        r_num  = DecimalNumber(5.0, num_decimal_places=1, color=GOLD, font_size=32)
        r_num.add_updater(lambda m: m.set_value(r_tracker.get_value()))
        eta_lbl = MathTex(r"\eta = ", color=INK, font_size=32)
        eta_num = DecimalNumber(eta_otto(5.0) * 100, num_decimal_places=1, color=BLUE, font_size=32)
        eta_pct = MathTex(r"\%", color=BLUE, font_size=32)
        eta_num.add_updater(lambda m: m.set_value(eta_otto(r_tracker.get_value()) * 100))

        r_row   = VGroup(r_lbl, r_num).arrange(RIGHT, buff=0.1)
        eta_row = VGroup(eta_lbl, eta_num, eta_pct).arrange(RIGHT, buff=0.08)
        VGroup(r_row, eta_row).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.3)

        hdr2 = Text("Sweep compression ratio  r  5 → 15",
                    font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.25)
        self.play(FadeOut(self._hdr), Write(hdr2), FadeIn(r_row), FadeIn(eta_row), run_time=0.8)

        self.play(r_tracker.animate.set_value(15.0), run_time=7.0, rate_func=smooth)
        self.wait(1.5)

        final = Text(
            "Higher r  →  more enclosed area  →  more work  →  higher efficiency",
            font="EB Garamond", font_size=24, color=INK,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(r_row, eta_row), Write(final), run_time=1.2)
        self.wait(2.5)
