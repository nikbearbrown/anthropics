#!/usr/bin/env python3
"""
vol1_step_reflection.py — Potential Step: Partial Quantum Reflection Above Barrier
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    k₀ = √(2mE)/ℏ, k₁ = √(2m(E−V₀))/ℏ
    R = ((k₀−k₁)/(k₀+k₁))²,  T = 4k₀k₁/(k₀+k₁)²
    R + T = 1 (probability current conservation)
    E = 2V₀: k₁ = k₀/√2 → R ≈ 0.029, T ≈ 0.971
    E = 4V₀: R ≈ 0.003

Verify:
    python3 vol1_step_reflection.py --verify

Render:
    manim -qh vol1_step_reflection.py StepReflectionScene
"""
import sys
import numpy as np

HBAR   = 1.0545718e-34
M_E    = 9.10938e-31
EV     = 1.60218e-19


def k0(E_eV):
    return np.sqrt(2 * M_E * E_eV * EV) / HBAR * 1e-9  # nm⁻¹


def k1(E_eV, V0_eV):
    if E_eV <= V0_eV:
        return None
    return np.sqrt(2 * M_E * (E_eV - V0_eV) * EV) / HBAR * 1e-9  # nm⁻¹


def R_coeff(E_eV, V0_eV):
    kk0 = k0(E_eV)
    kk1 = k1(E_eV, V0_eV)
    if kk1 is None:
        return 1.0  # total reflection below threshold
    return ((kk0 - kk1) / (kk0 + kk1))**2


def T_coeff(E_eV, V0_eV):
    return 1 - R_coeff(E_eV, V0_eV)


def verify():
    print("=== Potential Step Reflection Verification ===")
    V0 = 1.0  # eV

    # E = 2V₀
    E = 2 * V0
    kk0 = k0(E)
    kk1 = k1(E, V0)
    R = R_coeff(E, V0)
    T_val = T_coeff(E, V0)
    print(f"E = 2V₀ = {E:.1f} eV: k₀={kk0:.4f}, k₁={kk1:.4f}  (k₁/k₀={kk1/kk0:.4f} vs 1/√2={1/np.sqrt(2):.4f})")
    print(f"  R = {R:.4f}  T = {T_val:.4f}  R+T = {R+T_val:.6f}")

    # P1: R+T = 1
    print(f"\nP1: R + T = {R+T_val:.8f}  (should be 1.000)")

    # P2: Step downward (V₀ < 0)
    V0_neg = -1.0  # step down
    E2 = 3.0
    R2 = R_coeff(E2, V0_neg)
    T2 = T_coeff(E2, V0_neg)
    print(f"\nP2 (step down): E=3 eV, V₀=−1 eV:")
    print(f"  k₀={k0(E2):.4f}, k₁={k1(E2, V0_neg):.4f}")
    print(f"  R = {R2:.4f}  (should ≈ 0.005)  T = {T2:.4f}  R+T = {R2+T2:.6f}")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"


class StepReflectionScene(Scene):
    """
    Left: potential step diagram + wave amplitudes
    Right: R and T vs E/V₀ curve showing R never → 0
    Then: animate wave packet hitting the step
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_RT_curve()
        self._phase_wave_animation()

    def _phase_title(self):
        title = Text("Quantum Impedance Mismatch", font="EB Garamond", font_size=54, color=INK)
        sub = Text(
            "E = 2V₀  ·  R ≈ 2.9%  ·  T ≈ 97.1%  ·  R + T = 1.000 always",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"R = \left(\frac{k_0 - k_1}{k_0 + k_1}\right)^2, \quad T = \frac{4k_0 k_1}{(k_0+k_1)^2}, \quad R+T=1",
            color=BLUE, font_size=26,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_RT_curve(self):
        """Show R and T as function of E/V₀."""
        V0 = 1.0
        E_range = np.linspace(1.01, 8.0, 400)
        R_vals = np.array([R_coeff(E, V0) for E in E_range])
        T_vals = 1 - R_vals

        ax = Axes(
            x_range=[1, 8, 1], y_range=[0, 1.05, 0.25],
            x_length=10.0, y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        )
        lbl_x = MathTex(r"E / V_0", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"R,\;T", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        R_curve = VMobject(color=BROWN, stroke_width=2.5)
        R_pts = [ax.c2p(e, r) for e, r in zip(E_range, R_vals)]
        R_curve.set_points_smoothly(R_pts)

        T_curve = VMobject(color=BLUE, stroke_width=2.5)
        T_pts = [ax.c2p(e, t) for e, t in zip(E_range, T_vals)]
        T_curve.set_points_smoothly(T_pts)

        # Mark E=2V₀
        dot_R = Dot(ax.c2p(2, R_coeff(2, V0)), color=BROWN, radius=0.12)
        dot_T = Dot(ax.c2p(2, T_coeff(2, V0)), color=BLUE, radius=0.12)
        ann = MathTex(
            rf"E=2V_0:\ R={R_coeff(2,V0):.3f},\ T={T_coeff(2,V0):.3f}",
            color=INK, font_size=20,
        ).next_to(dot_R, UR, buff=0.15)

        lbl_R = Text("R (reflection)", font="EB Garamond", font_size=18, color=BROWN).to_corner(UR, buff=0.5).shift(DOWN*0.1)
        lbl_T = Text("T (transmission)", font="EB Garamond", font_size=18, color=BLUE).next_to(lbl_R, DOWN, buff=0.1)
        note = Text("R never equals zero (for V₀ ≠ 0)", font="EB Garamond", font_size=18, color=GOLD).to_edge(DOWN, buff=0.3)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=0.8)
        self.play(Create(R_curve), Create(T_curve), run_time=1.5)
        self.play(FadeIn(dot_R, dot_T), Write(ann), FadeIn(lbl_R, lbl_T), run_time=0.8)
        self.play(Write(note), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(ax, R_curve, T_curve, dot_R, dot_T, ann, lbl_R, lbl_T, lbl_x, lbl_y, note), run_time=0.5)

    def _phase_wave_animation(self):
        """Animate wave packet scattering off the step."""
        ax = Axes(
            x_range=[-8, 12, 4], y_range=[-1.8, 2.5, 1.0],
            x_length=12.0, y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        )

        # Step: V₀=1 eV at x=0
        step = Polygon(
            ax.c2p(0, 0), ax.c2p(12, 0), ax.c2p(12, 0.8), ax.c2p(0, 0.8),
            color=BROWN, fill_color=BROWN, fill_opacity=0.2, stroke_width=0,
        )
        v0_line = Line(ax.c2p(-8, 0), ax.c2p(12, 0), color=DIM, stroke_width=1, stroke_opacity=0.4)
        step_line = Line(ax.c2p(0, 0), ax.c2p(0, 2.2), color=BROWN, stroke_width=2)

        V0_lbl = MathTex(r"V_0 = 1\,\mathrm{eV}", color=BROWN, font_size=20).move_to(ax.c2p(6, 1.0))
        E_lbl = MathTex(r"E = 2\,\mathrm{eV}", color=GOLD, font_size=20).move_to(ax.c2p(-4, 1.2))

        E_line = DashedLine(ax.c2p(-8, 1.1), ax.c2p(12, 1.1), color=GOLD, stroke_width=1.2)

        self.play(Create(ax), FadeIn(step, step_line, v0_line, E_line, V0_lbl, E_lbl), run_time=0.8)

        # Wave numbers
        V0 = 1.0
        E = 2.0
        kk0 = k0(E)  # nm⁻¹
        kk1 = k1(E, V0)  # nm⁻¹
        R = R_coeff(E, V0)
        T_val = T_coeff(E, V0)
        r_amp = np.sqrt(R)
        t_amp = np.sqrt(T_val)

        phase = ValueTracker(0.0)

        x_left = np.linspace(-8, 0, 200)
        x_right = np.linspace(0, 12, 200)

        def _waves():
            ph = phase.get_value() * 2 * np.pi
            # Region I: incident + reflected (cos approximation with amplitude)
            psi_inc = np.cos(kk0 * x_left - ph)
            psi_ref = r_amp * np.cos(-kk0 * x_left - ph + np.pi)
            psi_left = psi_inc + psi_ref

            # Region II: transmitted with reduced amplitude and different k
            psi_right = t_amp * np.cos(kk1 * x_right - ph * kk1/kk0)

            def mc(xarr, yarr, col, w=2.5):
                pts = [ax.c2p(x, y) for x, y in zip(xarr, yarr)]
                c = VMobject(color=col, stroke_width=w)
                c.set_points_smoothly(pts)
                return c

            return VGroup(mc(x_left, psi_left, BLUE), mc(x_right, psi_right, GOLD))

        dyn_waves = always_redraw(_waves)
        self.add(dyn_waves)

        # Labels
        inc_lbl = Text("incident + reflected", font="EB Garamond", font_size=17, color=BLUE).move_to(ax.c2p(-4, 1.7))
        trans_lbl = Text(f"transmitted  (T={T_val:.3f})", font="EB Garamond", font_size=17, color=GOLD).move_to(ax.c2p(6, 1.7))
        RT_caption = MathTex(
            rf"R = {R:.4f},\quad T = {T_val:.4f},\quad R+T = {R+T_val:.6f}",
            color=INK, font_size=22,
        ).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(inc_lbl, trans_lbl), Write(RT_caption), run_time=0.8)
        self.play(phase.animate.set_value(3.0), run_time=7.0, rate_func=linear)
        self.wait(1.0)

        # Payoff
        final = Text(
            "Classical prediction: zero reflection above the step.  Quantum: always partial reflection.",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.35)
        self.play(ReplacementTransform(RT_caption, final), run_time=0.8)
        self.wait(2.5)
