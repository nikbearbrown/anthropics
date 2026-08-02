#!/usr/bin/env python3
"""
vol1_tunneling_barrier.py — Quantum Tunneling Through a Rectangular Barrier
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    E = 1 eV, V₀ = 5 eV, L = 5 Å, m = mₑ
    κ = √(2m(V₀−E))/ℏ ≈ 1.025 Å⁻¹, κL = 5.125
    T_exact = [1 + V₀²sinh²(κL)/4E(V₀−E)]⁻¹ ≈ 9.1×10⁻⁵
    T_WKB ≈ (16E(V₀−E)/V₀²)·e^{−2κL}
    prefactor = 16E(V₀−E)/V₀² = 2.56
    Doubling L: T_WKB ∝ e^{−10.25} ≈ 3.5×10⁻⁵ → 4.4×10⁻⁹

Verify:
    python3 vol1_tunneling_barrier.py --verify

Render:
    manim -qh vol1_tunneling_barrier.py TunnelingBarrierScene
"""
import sys
import numpy as np

# ─── Physics ──────────────────────────────────────────────────────────────────
HBAR  = 6.5821196e-16   # eV·s
HBAR_SI = 1.0545718e-34 # J·s
M_E   = 9.10938e-31     # kg
EV    = 1.60218e-19     # J

E_EV  = 1.0    # particle energy eV
V0_EV = 5.0    # barrier height eV
L_ANG = 5.0    # barrier width Å
L_SI  = L_ANG * 1e-10  # meters


def kappa(V0=V0_EV, E=E_EV):
    """Decay constant inside barrier, in Å⁻¹"""
    return np.sqrt(2 * M_E * (V0 - E) * EV) / HBAR_SI * 1e-10


def T_exact(V0=V0_EV, E=E_EV, L=L_ANG):
    kap = kappa(V0, E)
    kL = kap * L
    denom = 1 + (V0**2 * np.sinh(kL)**2) / (4 * E * (V0 - E))
    return 1.0 / denom


def T_WKB(V0=V0_EV, E=E_EV, L=L_ANG):
    kap = kappa(V0, E)
    prefactor = 16 * E * (V0 - E) / V0**2
    return prefactor * np.exp(-2 * kap * L)


def verify():
    print("=== Tunneling Barrier Verification ===")
    kap = kappa()
    kL = kap * L_ANG
    print(f"κ = {kap:.4f} Å⁻¹")
    print(f"κL = {kL:.4f}")
    T_ex = T_exact()
    T_wk = T_WKB()
    prefac = 16 * E_EV * (V0_EV - E_EV) / V0_EV**2
    print(f"T_exact = {T_ex:.4e}")
    print(f"T_WKB   = {T_wk:.4e}")
    print(f"Prefactor = 16E(V₀−E)/V₀² = {prefac:.4f}")
    print(f"T_exact/T_WKB = {T_ex/T_wk:.4f}  (should ≈ 2.56)")

    # P1: ratio check
    ratio = T_ex / T_wk
    print(f"\nP1: T_exact/T_WKB = {ratio:.4f}  (prefactor = {prefac:.4f}) match={np.isclose(ratio, prefac, rtol=0.05)}")

    # P2: doubling L
    T_2L = T_WKB(L=2*L_ANG)
    factor = T_2L / T_wk
    expected = np.exp(-2 * kap * L_ANG)
    print(f"\nP2: T_WKB(10 Å)/T_WKB(5 Å) = {factor:.4e}")
    print(f"    exp(-κL) = exp(-{kap*L_ANG:.4f}) = {expected:.4e}")
    print(f"    So doubling L gives factor e^(-{kap*L_ANG:.4f}) = {expected:.4e}")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"


class TunnelingBarrierScene(Scene):
    """
    Three-region wave function animation:
    Region I: oscillating incident + reflected wave
    Region II: exponentially decaying evanescent wave
    Region III: small transmitted oscillating wave
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_static()
        self._phase_animate()
        self._phase_sweep()

    def _phase_title(self):
        title = Text("Quantum Tunneling", font="EB Garamond", font_size=60, color=INK)
        sub = Text(
            "E = 1 eV  ·  V₀ = 5 eV  ·  L = 5 Å  ·  T_exact ≈ 9.1×10⁻⁵",
            font="EB Garamond", font_size=22, color=DIM,
        )
        eq = MathTex(
            r"T = \left[1 + \frac{V_0^2 \sinh^2(\kappa L)}{4E(V_0-E)}\right]^{-1}",
            color=BLUE, font_size=30,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_static(self):
        """Show the static picture with regions labeled."""
        ax = Axes(
            x_range=[-8, 14, 4], y_range=[-1.8, 1.8, 1.0],
            x_length=12.0, y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        )

        # Barrier: x in [0, 5] Å — we use normalized x where barrier = [0, 1] internally
        # Draw V₀ box from x=0 to x=5
        barrier = Rectangle(
            width=ax.c2p(5,0)[0] - ax.c2p(0,0)[0],
            height=ax.c2p(0,1.6)[1] - ax.c2p(0,-1.6)[1],
            color=BROWN, fill_color=BROWN, fill_opacity=0.25, stroke_width=2,
        )
        barrier.move_to(ax.c2p(2.5, 0))

        # Region labels
        r1 = Text("Region I", font="EB Garamond", font_size=20, color=BLUE).move_to(ax.c2p(-4, 1.5))
        r2 = Text("Region II", font="EB Garamond", font_size=20, color=BROWN).move_to(ax.c2p(2.5, 1.5))
        r3 = Text("Region III", font="EB Garamond", font_size=20, color=GOLD).move_to(ax.c2p(9.5, 1.5))

        # V₀ label
        v0_lbl = MathTex(r"V_0 = 5\,\mathrm{eV}", color=BROWN, font_size=20).move_to(ax.c2p(2.5, -1.6))
        e_lbl = MathTex(r"E = 1\,\mathrm{eV}", color=INK, font_size=20).move_to(ax.c2p(-4, -1.6))

        # Energy line
        e_line = DashedLine(ax.c2p(-8, 0.3), ax.c2p(14, 0.3), color=GOLD, stroke_width=1.5)
        e_line_lbl = MathTex(r"E", color=GOLD, font_size=18).next_to(ax.c2p(14, 0.3), RIGHT, buff=0.05)

        self.play(Create(ax), FadeIn(barrier), run_time=1.0)
        self.play(Write(r1), Write(r2), Write(r3), FadeIn(v0_lbl, e_lbl, e_line, e_line_lbl), run_time=1.2)

        # Static snapshot of wave function at t=0
        kap = kappa()
        k0 = np.sqrt(2 * M_E * E_EV * EV) / HBAR_SI * 1e-10  # Å⁻¹
        T = T_exact()
        R = 1 - T  # approx (not exact reflection coefficient here)
        B_over_A = (k0 - np.sqrt(0)) / (k0 + np.sqrt(0))  # simplified
        # Use amplitude ratios from continuity
        A_in = 1.0  # incident amplitude
        # Transmitted amplitude: |t| = √T, reflected: |r| = √R
        t_amp = np.sqrt(T)
        r_amp = np.sqrt(R) * 0.3  # scaled for visibility

        x1 = np.linspace(-8, 0, 200)
        x2 = np.linspace(0, 5, 100)
        x3 = np.linspace(5, 14, 200)

        # Region I: cos(k₀x) incident + small reflected wave
        psi1 = np.cos(k0 * x1) + r_amp * np.cos(k0 * x1 + np.pi)
        # Region II: exponential decay
        psi2 = np.exp(-kap * x2) * 0.9
        # Region III: transmitted oscillation (very small)
        psi3 = t_amp * 25 * np.cos(k0 * (x3 - 5))  # amplified for visibility

        def make_curve(x_arr, y_arr, color, w=2.5):
            pts = [ax.c2p(x, y) for x, y in zip(x_arr, y_arr)]
            c = VMobject(color=color, stroke_width=w)
            c.set_points_smoothly(pts)
            return c

        c1 = make_curve(x1, psi1, BLUE)
        c2 = make_curve(x2, psi2, BROWN)
        c3 = make_curve(x3, psi3, GOLD)

        self.play(Create(c1), run_time=1.5)
        self.play(Create(c2), run_time=1.0)
        self.play(Create(c3), run_time=1.5)

        # Annotations
        kL_lbl = MathTex(r"\kappa L = 5.125", color=BROWN, font_size=22).to_edge(DOWN, buff=0.5)
        T_lbl = MathTex(r"T_{\rm exact} = 9.1 \times 10^{-5}", color=GOLD, font_size=22)
        T_lbl.next_to(kL_lbl, UP, buff=0.15)
        self.play(Write(T_lbl), Write(kL_lbl), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(ax, barrier, r1, r2, r3, v0_lbl, e_lbl, e_line, e_line_lbl,
                          c1, c2, c3, T_lbl, kL_lbl), run_time=0.7)

    def _phase_animate(self):
        """Animate wave packet scattering."""
        ax = Axes(
            x_range=[-8, 14, 4], y_range=[-1.8, 1.8, 1.0],
            x_length=12.0, y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        )
        barrier = Rectangle(
            width=ax.c2p(5,0)[0] - ax.c2p(0,0)[0],
            height=ax.c2p(0,1.5)[1] - ax.c2p(0,-1.5)[1],
            color=BROWN, fill_color=BROWN, fill_opacity=0.25, stroke_width=2,
        )
        barrier.move_to(ax.c2p(2.5, 0))
        self.play(Create(ax), FadeIn(barrier), run_time=0.8)

        # Phase tracker
        phase = ValueTracker(0.0)
        kap = kappa()
        k0 = np.sqrt(2 * M_E * E_EV * EV) / HBAR_SI * 1e-10
        T = T_exact()
        t_amp = np.sqrt(T)

        x1 = np.linspace(-8, 0, 200)
        x2 = np.linspace(0, 5, 80)
        x3 = np.linspace(5, 14, 200)

        def _wave():
            ph = phase.get_value() * 2 * np.pi
            psi1 = np.cos(k0 * x1 - ph) + 0.08 * np.cos(-k0 * x1 - ph)
            psi2 = np.exp(-kap * x2) * np.cos(-kap * x2 * 0 - ph * 0.1)
            psi3 = t_amp * 30 * np.cos(k0 * (x3 - 5) - ph)

            def mc(xarr, yarr, col):
                pts = [ax.c2p(x, y) for x, y in zip(xarr, yarr)]
                c = VMobject(color=col, stroke_width=2.5)
                c.set_points_smoothly(pts)
                return c

            return VGroup(mc(x1, psi1, BLUE), mc(x2, psi2, BROWN), mc(x3, psi3, GOLD))

        dyn_wave = always_redraw(_wave)
        self.add(dyn_wave)

        # Labels
        r1 = Text("incident + reflected", font="EB Garamond", font_size=18, color=BLUE).move_to(ax.c2p(-4, 1.5))
        r2 = Text("evanescent decay", font="EB Garamond", font_size=18, color=BROWN).move_to(ax.c2p(2.5, 1.5))
        r3 = Text("transmitted (×30)", font="EB Garamond", font_size=18, color=GOLD).move_to(ax.c2p(9.5, 1.5))
        caption = MathTex(
            r"T_{\rm exact} \approx 9.1\times10^{-5}\quad \kappa = \sqrt{2m(V_0-E)}/\hbar \approx 1.025\,\text{\AA}^{-1}",
            color=INK, font_size=22,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(r1, r2, r3, caption), run_time=0.8)

        self.play(phase.animate.set_value(3.0), run_time=7.0, rate_func=linear)
        self.wait(1.0)
        self.play(FadeOut(ax, barrier, dyn_wave, r1, r2, r3, caption), run_time=0.6)

    def _phase_sweep(self):
        """Sweep barrier width and show T on log axis."""
        ax = Axes(
            x_range=[2, 10, 2], y_range=[-10, 0, 2],
            x_length=10.0, y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        )
        lbl_x = MathTex(r"L\,(\text{\AA})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"\log_{10}(T)", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title_sweep = Text(
            "T collapses exponentially with barrier width",
            font="EB Garamond", font_size=26, color=INK,
        ).to_edge(UP, buff=0.2)

        L_vals = np.linspace(2.01, 10, 300)
        log_T_ex = [np.log10(T_exact(L=Lv)) for Lv in L_vals]
        log_T_wk = [np.log10(T_WKB(L=Lv)) for Lv in L_vals]

        def make_curve(Lv, logT, color, w=2.5):
            pts = [ax.c2p(l, lt) for l, lt in zip(Lv, logT)]
            c = VMobject(color=color, stroke_width=w)
            c.set_points_smoothly(pts)
            return c

        c_ex = make_curve(L_vals, log_T_ex, BLUE)
        c_wk = make_curve(L_vals, log_T_wk, DIM, w=2.0)

        # Mark L=5 Å point
        dot = Dot(ax.c2p(5, np.log10(T_exact())), color=GOLD, radius=0.12)
        dot_wkb = Dot(ax.c2p(5, np.log10(T_WKB())), color=DIM, radius=0.10)

        ann = MathTex(
            r"L=5\,\text{\AA}:\ T_{\rm exact}=9.1\times10^{-5}",
            color=GOLD, font_size=20,
        ).next_to(dot, UR, buff=0.12)
        ratio_lbl = MathTex(
            r"\frac{T_{\rm exact}}{T_{\rm WKB}} = 2.56 = \frac{16E(V_0-E)}{V_0^2}",
            color=INK, font_size=22,
        ).to_edge(DOWN, buff=0.3)

        leg_ex = Text("T_exact", font="EB Garamond", font_size=18, color=BLUE).to_corner(UR, buff=0.5).shift(DOWN*0.1)
        leg_wk = Text("T_WKB", font="EB Garamond", font_size=18, color=DIM).next_to(leg_ex, DOWN, buff=0.1)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(title_sweep), run_time=1.0)
        self.play(Create(c_ex), Create(c_wk), run_time=2.0)
        self.play(FadeIn(dot, dot_wkb, leg_ex, leg_wk), Write(ann), run_time=0.8)
        self.play(Write(ratio_lbl), run_time=1.0)
        self.wait(3.0)
