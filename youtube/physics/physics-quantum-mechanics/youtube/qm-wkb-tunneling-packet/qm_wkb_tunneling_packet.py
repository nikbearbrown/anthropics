#!/usr/bin/env python3
"""
qm_wkb_tunneling_packet.py — WKB Wave Packet Tunneling Through a Rectangular Barrier
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-wkb-tunneling-packet
    manim -qh qm_wkb_tunneling_packet.py WKBTunnelingScene

Verify:
    python3 qm_wkb_tunneling_packet.py

Physics:
    Electron, E=1 eV, V0=2 eV
    κ = sqrt(2m(V0-E))/ℏ
    T = exp(-2κL) for rectangular barrier
    L=0.5 nm: κ=5.13 nm⁻¹, T≈0.006 (0.6%)
    L=0.2 nm: κ=5.13 nm⁻¹, T=exp(-2.05)≈0.13 (13%)
    NOTE: κ does not depend on L; same barrier height difference
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
M_E  = 9.10938e-31
EV   = 1.60218e-19


def kappa(V0_eV: float, E_eV: float) -> float:
    """κ = sqrt(2m(V0-E))/ℏ in nm⁻¹."""
    if V0_eV <= E_eV:
        return 0.0
    return np.sqrt(2.0 * M_E * (V0_eV - E_eV) * EV) / HBAR * 1e-9


def T_wkb(V0_eV: float, E_eV: float, L_nm: float) -> float:
    """WKB transmission probability T = exp(-2κL)."""
    k = kappa(V0_eV, E_eV)
    return np.exp(-2.0 * k * L_nm)


def gaussian_packet(x: np.ndarray, x0: float, sigma: float, k0: float) -> np.ndarray:
    """Gaussian wave packet |ψ|² at t=0."""
    return (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - x0) / sigma)**2)


def verify():
    print("=== WKB tunneling verification ===")
    V0, E_ev = 2.0, 1.0
    k = kappa(V0, E_ev)
    print(f"κ = {k:.3f} nm⁻¹  (card says 5.13 nm⁻¹)")
    T05 = T_wkb(V0, E_ev, 0.5)
    T02 = T_wkb(V0, E_ev, 0.2)
    print(f"T (L=0.5 nm) = {T05:.4f}  (card says 0.006)")
    print(f"T (L=0.2 nm) = {T02:.4f}  (card says 0.13)")
    # P1: doubling width from 0.2→0.4 nm squares T
    T04 = T_wkb(V0, E_ev, 0.4)
    print(f"T (L=0.4 nm) = {T04:.4f}  (should be ≈ T02² = {T02**2:.4f})")
    ratio = T04 / T02**2
    print(f"Ratio T(0.4)/T(0.2)² = {ratio:.4f}  (should be ≈ 1.0)")
    print("=== PASSED ===" if abs(ratio - 1.0) < 0.01 else "=== CHECK ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class WKBTunnelingScene(Scene):
    """
    WKB tunneling: packet approaches barrier, splits into reflected + transmitted.
    Then: T vs L exponential curve. Then: barrier width slider.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_packet_split()
        self._phase_T_vs_L()
        self._phase_barrier_slider()

    def _phase_title(self):
        title = Text("Quantum Tunneling Through a Barrier", font="EB Garamond",
                     font_size=52, color=INK)
        sub1 = Text(
            "Classically impossible — quantum mechanically certain to happen.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"T = e^{-2\kappa L},\quad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}",
                       color=BLUE, font_size=28)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_packet_split(self):
        ax = Axes(
            x_range=[-4, 7, 2],
            y_range=[0, 0.55, 0.2],
            x_length=10.0,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.6)
        lbl_x = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"|\psi|^2", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("E=1 eV packet hits V₀=2 eV barrier of width L=0.5 nm",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)

        # Draw barrier
        barrier = Rectangle(
            width=ax.c2p(2.5, 0)[0] - ax.c2p(2.0, 0)[0],
            height=ax.c2p(0, 0.5)[1] - ax.c2p(0, 0)[1],
            color=BROWN, fill_color=BROWN, fill_opacity=0.35, stroke_width=2.0,
        )
        barrier.move_to(ax.c2p(2.25, 0.25))
        barrier_lbl = Text("V₀ = 2 eV", font="EB Garamond", font_size=17, color=BROWN
                           ).next_to(barrier, UP, buff=0.1)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr),
                  FadeIn(barrier), Write(barrier_lbl), run_time=1.5)

        # Stages: incoming, at barrier, split
        sigma = 0.6   # nm
        x_arr = np.linspace(-4, 7, 600)

        def packet(x0, amp, color, lw=3.5):
            y = amp * gaussian_packet(x_arr, x0, sigma, 0)
            pts = [ax.c2p(x, y_) for x, y_ in zip(x_arr, y)]
            m = VMobject(color=color, stroke_width=lw)
            m.set_points_smoothly(pts)
            return m

        T_val   = T_wkb(2.0, 1.0, 0.5)
        R_val   = 1.0 - T_val
        amp_inc = 1.0 / (sigma * np.sqrt(2 * np.pi))
        amp_ref = np.sqrt(R_val) * amp_inc
        amp_tr  = np.sqrt(T_val) * amp_inc

        c_inc  = packet(-2.0, amp_inc, BLUE)
        c_ref  = packet(-2.0, amp_ref, DIM)
        c_tr   = packet(5.0,  amp_tr,  GOLD)
        c_evan = packet(2.25, amp_inc * 0.08, BROWN)  # evanescent inside barrier

        cap_inc  = Text("Incoming packet — E=1 eV", font="EB Garamond", font_size=19, color=BLUE
                        ).to_edge(DOWN, buff=0.28)
        cap_ref  = Text("Reflected (R≈99.4%)", font="EB Garamond", font_size=19, color=DIM
                        ).to_edge(DOWN, buff=0.5)
        cap_tr   = Text("Transmitted (T≈0.6%) — arrives where classical particle cannot",
                        font="EB Garamond", font_size=19, color=GOLD).to_edge(DOWN, buff=0.28)

        self.play(Create(c_inc), Write(cap_inc), run_time=1.0)
        self.wait(0.5)
        self.play(FadeOut(cap_inc), Create(c_ref), Create(c_evan), run_time=0.8)
        self.play(Write(cap_ref), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(cap_ref), FadeOut(c_evan), Create(c_tr), Write(cap_tr), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, barrier, barrier_lbl,
                          c_inc, c_ref, c_tr, cap_tr), run_time=0.5)

    def _phase_T_vs_L(self):
        L_arr = np.linspace(0.05, 1.5, 300)
        T_arr = np.array([T_wkb(2.0, 1.0, L) for L in L_arr])

        ax = Axes(
            x_range=[0, 1.6, 0.4],
            y_range=[0, 0.65, 0.2],
            x_length=8.5,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.5)
        lbl_x = MathTex(r"L\;(\mathrm{nm})", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"T = e^{-2\kappa L}", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Transmission probability T vs barrier width L",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)

        c_T = VMobject(color=BLUE, stroke_width=3.5)
        c_T.set_points_smoothly([ax.c2p(L, T) for L, T in zip(L_arr, T_arr)])

        mk02 = Dot(ax.c2p(0.2, T_wkb(2.0, 1.0, 0.2)), radius=0.1, color=GOLD)
        mk05 = Dot(ax.c2p(0.5, T_wkb(2.0, 1.0, 0.5)), radius=0.1, color=GOLD)
        lbl02 = MathTex(r"T\!=\!13\%", color=GOLD, font_size=20).next_to(mk02, UR, buff=0.05)
        lbl05 = MathTex(r"T\!=\!0.6\%", color=GOLD, font_size=20).next_to(mk05, DR, buff=0.05)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)
        self.play(Create(c_T), run_time=1.5)
        self.play(FadeIn(mk02), Write(lbl02), FadeIn(mk05), Write(lbl05), run_time=1.0)

        cap = Text("Exponential sensitivity: 0.2→0.4 nm squares the transmission.",
                   font="EB Garamond", font_size=20, color=INK).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=0.9)
        self.wait(2.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, c_T, mk02, mk05, lbl02, lbl05, cap), run_time=0.5)

    def _phase_barrier_slider(self):
        """ValueTracker: E sweeps from 0.5 eV to V₀=2 eV, T rises."""
        V0 = 2.0
        E_tracker = ValueTracker(0.5)

        ax = Axes(
            x_range=[0, 1.6, 0.4],
            y_range=[0, 1.05, 0.2],
            x_length=8.5,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.5)
        lbl_x = MathTex(r"L\;(\mathrm{nm})", color=INK, font_size=21).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"T", color=INK, font_size=21).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Raise E toward V₀ — barrier becomes transparent",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.1)

        L_arr = np.linspace(0.01, 1.5, 200)

        def _curve():
            E = E_tracker.get_value()
            T_arr = np.array([T_wkb(V0, E, L) for L in L_arr])
            c = VMobject(color=BLUE, stroke_width=3.5)
            pts = [ax.c2p(L, T) for L, T in zip(L_arr, T_arr)]
            c.set_points_smoothly(pts)
            return c

        dyn = always_redraw(_curve)

        E_lbl = MathTex(r"E = ", color=GOLD, font_size=28)
        E_num = DecimalNumber(0.5, num_decimal_places=2, color=GOLD, font_size=28)
        E_num.add_updater(lambda m: m.set_value(E_tracker.get_value()))
        E_eV  = MathTex(r"\mathrm{eV}", color=GOLD, font_size=28)
        E_row = VGroup(E_lbl, E_num, E_eV).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.28)

        self.add(dyn)
        self.play(FadeIn(E_row), run_time=0.6)
        self.play(E_tracker.animate.set_value(1.95), run_time=5.0, rate_func=smooth)
        self.wait(0.5)

        final = MathTex(r"E \to V_0 \Rightarrow \kappa \to 0 \Rightarrow T \to 1",
                        color=INK, font_size=28).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(E_row), Write(final), run_time=1.0)
        self.wait(2.5)
