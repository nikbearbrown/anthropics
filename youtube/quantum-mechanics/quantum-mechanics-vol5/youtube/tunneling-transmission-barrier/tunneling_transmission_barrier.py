#!/usr/bin/env python3
"""
tunneling_transmission_barrier.py — Quantum Tunneling Transmission
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/tunneling-transmission-barrier
    manim -qh tunneling_transmission_barrier.py TunnelingScene

Verify:
    python3 tunneling_transmission_barrier.py --verify

Physics:
    T ≈ e^{−2κL};  κ = √(2m(V₀−E))/ℏ
    electron, V₀−E = 1 eV → κ = 5.12 nm⁻¹
    L=0.1 nm: T=0.36;  L=0.5 nm: T=0.006;  L=1 nm: T≈4×10⁻⁵
    ln(T) vs L is a straight line (slope = −2κ)
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
ME   = 9.10938e-31
EV   = 1.60218e-19


def kappa(V0_minus_E_eV):
    """Decay constant κ in nm⁻¹."""
    return np.sqrt(2 * ME * V0_minus_E_eV * EV) / HBAR * 1e-9


def transmission(L_nm, kappa_val):
    """T ≈ e^{-2κL}."""
    return np.exp(-2 * kappa_val * L_nm)


def verify():
    print("=== Tunneling transmission verification ===")
    k = kappa(1.0)
    print(f"  κ (1 eV barrier) = {k:.4f} nm⁻¹  (expected ~5.12)")
    for L in [0.1, 0.5, 1.0, 2.0]:
        T = transmission(L, k)
        print(f"  L={L:.1f} nm: T = {T:.3e}  (2κL = {2*k*L:.2f})")

    # P1: straight line on semi-log
    L_vals = [0.1, 0.5, 1.0]
    logT   = [-2 * k * L for L in L_vals]
    slope  = (logT[1] - logT[0]) / (L_vals[1] - L_vals[0])
    print(f"\n  Semi-log slope = {slope:.4f}  (should be {-2*k:.4f} = −2κ)")

    # P2: doubling V0-E → κ multiplies by √2 → T → T²
    k2 = kappa(4.0)  # quadruple barrier → √2 * k(1 eV)? No: κ(4eV) = 2κ(1eV)
    print(f"\n  κ at 4 eV = {k2:.4f}  (should be {2*k:.4f} = 2·κ(1eV))")
    T_05_1eV = transmission(0.5, k)
    T_05_4eV = transmission(0.5, k2)
    print(f"  T(L=0.5nm,1eV)={T_05_1eV:.4e}  T(L=0.5nm,4eV)={T_05_4eV:.4e}  ratio≈{T_05_4eV/T_05_1eV:.4f}  (≈T²/T={T_05_1eV:.4e})")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class TunnelingScene(Scene):
    """
    Phase 1: title
    Phase 2: wavefunction diagram — oscillating, decaying through barrier, oscillating
    Phase 3: semi-log plot T vs L (linear on log scale)
    Phase 4: L slider — both panels update simultaneously
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_wavefunction()
        self._phase_semilog()
        self._phase_slider()

    def _phase_title(self):
        title = Text("Quantum Tunneling", font="EB Garamond", font_size=60, color=INK)
        sub1  = Text(
            "T ≈ e^{−2κL}  ·  κ = √(2m(V₀−E))/ℏ  ·  exponential in barrier width",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2  = Text(
            "Double the barrier → T² (squaring the suppression)",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_wavefunction(self):
        k     = kappa(1.0)
        L_nm  = 0.5
        x_arr = np.linspace(-2.0, 2.0 + L_nm, 600)
        barrier_start = 0.0
        barrier_end   = L_nm

        def psi(x):
            """Schematic wavefunction: oscillating in, decaying in barrier, oscillating out."""
            if x < barrier_start:
                A = 1.0
                return A * np.sin(15 * x + 3)
            elif x < barrier_end:
                decay = np.exp(-k * (x - barrier_start))
                osc   = 0.3 * np.cos(5 * x)
                return decay + osc
            else:
                T_val = transmission(L_nm, k)
                return np.sqrt(T_val) * np.sin(15 * (x - barrier_end) + 3)

        ax = Axes(
            x_range=[-2.0, 2.5, 0.5], y_range=[-1.3, 1.3, 0.5],
            x_length=9.0, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": False},
        ).center().shift(UP * 0.3)

        # Barrier rectangle
        bx0 = ax.c2p(0.0, -1.3)
        bx1 = ax.c2p(L_nm, 1.3)
        barrier = Rectangle(
            width=bx1[0] - bx0[0], height=bx1[1] - bx0[1],
            color=BROWN, fill_color=BROWN, fill_opacity=0.25, stroke_width=0,
        ).move_to(np.array([(bx0[0]+bx1[0])/2, (bx0[1]+bx1[1])/2, 0]))

        pts = [ax.c2p(x, psi(x)) for x in x_arr]
        curve = VMobject(color=BLUE, stroke_width=2.5)
        curve.set_points_smoothly(pts)

        lbl_V = MathTex(r"V_0", color=BROWN, font_size=24).next_to(ax.c2p(L_nm/2, 1.2), UP, buff=0.1)
        lbl_T = MathTex(r"T\approx 0.006", color=GOLD, font_size=22).to_corner(UR, buff=0.35)

        self.play(Create(ax), FadeIn(barrier), run_time=0.8)
        self.play(Create(curve), Write(lbl_V), Write(lbl_T), run_time=1.5)

        note = Text(
            "Amplitude shrinks by √T inside barrier — wavefunction decays exponentially",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(note), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_semilog(self):
        k = kappa(1.0)
        L_max = 2.5

        ax = Axes(
            x_range=[0, L_max, 0.5], y_range=[-12, 1, 2],
            x_length=8.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(UP * 0.1)

        x_lbl = MathTex(r"L\;\mathrm{(nm)}", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = MathTex(r"\ln T", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.8)

        L_arr = np.linspace(0.01, L_max, 400)
        logT  = [-2 * k * L for L in L_arr]
        pts   = [ax.c2p(L, lt) for L, lt in zip(L_arr, logT)]
        line  = VMobject(color=GOLD, stroke_width=2.8)
        line.set_points_smoothly(pts)
        self.play(Create(line), run_time=1.5)

        slope_lbl = MathTex(r"\text{slope} = -2\kappa = -10.24\;\mathrm{nm}^{-1}", color=GOLD, font_size=22)
        slope_lbl.to_corner(UR, buff=0.35)
        self.play(Write(slope_lbl), run_time=0.7)

        # Mark specific points
        for L_mark, col in [(0.1, BLUE), (0.5, BROWN), (1.0, DIM)]:
            T_mark = transmission(L_mark, k)
            if np.log(T_mark) > -12:
                dot = Dot(ax.c2p(L_mark, np.log(T_mark)), color=col, radius=0.1)
                lbl = MathTex(rf"T={T_mark:.2e}", color=col, font_size=18).next_to(dot, RIGHT, buff=0.1)
                self.play(FadeIn(dot), Write(lbl), run_time=0.5)

        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_slider(self):
        k       = kappa(1.0)
        L_track = ValueTracker(0.1)

        ax = Axes(
            x_range=[0, 2.5, 0.5], y_range=[-12, 1, 2],
            x_length=7.5, y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.4, "include_ticks": True},
        ).center().shift(UP * 0.2)

        L_arr = np.linspace(0.01, 2.5, 300)
        logT  = [-2 * k * L for L in L_arr]
        pts   = [ax.c2p(L, lt) for L, lt in zip(L_arr, logT)]
        line  = VMobject(color=GOLD, stroke_width=2.5)
        line.set_points_smoothly(pts)
        self.play(Create(ax), Create(line), run_time=1.0)

        def _dot():
            L  = L_track.get_value()
            lt = -2 * k * L
            return Dot(ax.c2p(L, max(lt, -12)), color=BLUE, radius=0.12)

        def _lbl():
            L  = L_track.get_value()
            T  = transmission(L, k)
            return MathTex(
                rf"L={L:.2f}\;\mathrm{{nm}}\quad T={T:.2e}",
                color=BLUE, font_size=24,
            ).to_edge(DOWN, buff=0.28)

        dyn_dot = always_redraw(_dot)
        dyn_lbl = always_redraw(_lbl)
        self.add(dyn_dot, dyn_lbl)

        hdr = Text(
            "Each 0.1 nm of extra barrier → multiply T by e^{−1.02} ≈ 0.36",
            font="EB Garamond", font_size=19, color=INK,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.6)

        self.play(L_track.animate.set_value(2.5), run_time=5.0, rate_func=linear)
        self.wait(2.0)
