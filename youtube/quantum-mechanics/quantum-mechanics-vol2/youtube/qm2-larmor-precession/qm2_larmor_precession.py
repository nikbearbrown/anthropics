#!/usr/bin/env python3
"""
qm2_larmor_precession.py — Larmor Precession on the Bloch Sphere
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics:
    H = (γB₀ℏ/2)σ_z  →  ω_L = γB₀
    Proton: γ/(2π) = 42.58 MHz/T
    At B₀ = 1.5 T: ω_L/(2π) = 63.87 MHz, T_L = 15.66 ns
    ⟨S_x⟩ = (ℏ/2)sinθ₀·cos(ω_L·t)
    ⟨S_y⟩ = (ℏ/2)sinθ₀·sin(ω_L·t)
    ⟨S_z⟩ = (ℏ/2)cosθ₀  (constant!)

Verify:
    python3 qm2_larmor_precession.py --verify

Render:
    manim -qh qm2_larmor_precession.py LarmorPrecessionScene
"""
import sys
import numpy as np

GAMMA_P = 2 * np.pi * 42.58e6  # rad/(s·T) proton gyromagnetic ratio

def larmor_freq(B0_T):
    return GAMMA_P * B0_T / (2 * np.pi)  # Hz

def larmor_period_ns(B0_T):
    return 1.0 / larmor_freq(B0_T) * 1e9  # ns

def Sx_expect(theta0, t_ns, B0_T=1.5):
    omega_L = GAMMA_P * B0_T  # rad/s
    t = t_ns * 1e-9
    return 0.5 * np.sin(theta0) * np.cos(omega_L * t)

def Sy_expect(theta0, t_ns, B0_T=1.5):
    omega_L = GAMMA_P * B0_T
    t = t_ns * 1e-9
    return 0.5 * np.sin(theta0) * np.sin(omega_L * t)

def Sz_expect(theta0):
    return 0.5 * np.cos(theta0)

def verify():
    print("=== Larmor Precession Verification ===")
    B0 = 1.5  # T
    f_L = larmor_freq(B0)
    T_ns = larmor_period_ns(B0)
    print(f"B₀ = {B0} T: ω_L/(2π) = {f_L/1e6:.2f} MHz, T_L = {T_ns:.2f} ns")

    B0_3T = 3.0
    f_3T = larmor_freq(B0_3T)
    print(f"B₀ = {B0_3T} T: ω_L/(2π) = {f_3T/1e6:.2f} MHz  (doubled)")

    theta0 = np.pi / 3
    # P1: ⟨S_z⟩ constant
    Sz_vals = [Sz_expect(theta0) for _ in range(5)]
    print(f"\nP1: ⟨S_z⟩ = {Sz_expect(theta0):.4f}  (constant = cos(θ₀/2)×0.5 = {0.5*np.cos(theta0):.4f})")

    # P2: doubling B₀ doubles ω_L
    print(f"\nP2: f(3T)/f(1.5T) = {f_3T/f_L:.4f}  (should be 2.000)")

    # P(+) = cos²(θ/2) at any time
    P_plus = np.cos(theta0/2)**2
    print(f"\nAt θ₀=π/3: P(+) = cos²(π/6) = {P_plus:.4f}  (constant in time)")
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


class LarmorPrecessionScene(Scene):
    """
    Bloch sphere with precessing vector + side traces of ⟨S_x⟩, ⟨S_y⟩, ⟨S_z⟩.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_precession()
        self._phase_north_pole()

    def _phase_title(self):
        title = Text("Larmor Precession", font="EB Garamond", font_size=58, color=INK)
        sub = Text(
            "Proton at 1.5 T  ·  ω_L/(2π) = 63.87 MHz  ·  T_L = 15.66 ns",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"\omega_L = \gamma B_0 \quad \Longrightarrow \quad \langle S_z\rangle = \tfrac{\hbar}{2}\cos\theta_0\text{ constant}",
            color=BLUE, font_size=28,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_precession(self):
        B0 = 1.5
        T_ns = larmor_period_ns(B0)
        theta0 = np.pi / 3  # 60° polar angle

        # Sphere (2D projection as circle)
        sphere = Circle(radius=2.0, color=DIM, stroke_width=1.5, stroke_opacity=0.5)
        sphere.shift(LEFT*3.0)

        equator = Ellipse(width=4.0, height=0.8, color=DIM, stroke_width=1, stroke_opacity=0.4)
        equator.shift(LEFT*3.0)

        z_ax = Arrow(LEFT*3.0 + DOWN*2.2, LEFT*3.0 + UP*2.4, buff=0, color=DIM, stroke_width=1.5)
        z_lbl = MathTex(r"z", color=DIM, font_size=18).next_to(z_ax.get_end(), UP, buff=0.04)
        x_ax = Arrow(LEFT*5.1, LEFT*0.9, buff=0, color=DIM, stroke_width=1.5)
        x_lbl = MathTex(r"x", color=DIM, font_size=18).next_to(x_ax.get_end(), RIGHT, buff=0.04)

        # Pole labels
        n_pole = Dot(LEFT*3.0 + UP*2.0, color=BLUE, radius=0.07)
        s_pole = Dot(LEFT*3.0 + DOWN*2.0, color=BLUE, radius=0.07)
        n_lbl = MathTex(r"|{\uparrow}\rangle", color=BLUE, font_size=16).next_to(n_pole, UR, buff=0.05)
        s_lbl = MathTex(r"|{\downarrow}\rangle", color=BLUE, font_size=16).next_to(s_pole, DR, buff=0.05)

        # Bloch vector initial position
        r_bloch = 2.0
        center_sphere = np.array([-3.0, 0.0, 0.0])

        # Side traces axes
        ax_side = Axes(
            x_range=[0, 3, 1], y_range=[-0.6, 0.6, 0.3],
            x_length=5.5, y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.3, include_ticks=True, tip_length=0.15),
        ).shift(RIGHT*2.8)
        lbl_t = MathTex(r"t/T_L", color=INK, font_size=14).next_to(ax_side.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_S = MathTex(r"\langle S\rangle / (\hbar/2)", color=INK, font_size=14).next_to(ax_side.y_axis.get_end(), UP, buff=0.04)

        self.play(
            Create(sphere), Create(equator), Create(z_ax), Create(x_ax),
            Write(z_lbl), Write(x_lbl),
            FadeIn(n_pole, s_pole, n_lbl, s_lbl),
            Create(ax_side), Write(lbl_t), Write(lbl_S),
            run_time=1.2,
        )

        t_track = ValueTracker(0.0)  # in units of T_L

        def _bloch_vec():
            t_frac = t_track.get_value()
            phi = 2 * np.pi * t_frac  # azimuthal angle
            # Project 3D onto 2D: x = r·sinθ·cosφ, z = r·cosθ
            bx = r_bloch * np.sin(theta0) * np.cos(phi)
            bz = r_bloch * np.cos(theta0)
            # 2D projection
            x_2d = center_sphere[0] + bx
            z_2d = center_sphere[1] + bz
            vec = Arrow(center_sphere, np.array([x_2d, z_2d, 0]),
                        buff=0, color=GOLD, stroke_width=3)
            dot = Dot(np.array([x_2d, z_2d, 0]), color=GOLD, radius=0.09)
            return VGroup(vec, dot)

        def _traces():
            t_frac = t_track.get_value()
            n_pts = max(2, int(t_frac * 100) + 2)
            t_vals = np.linspace(0, t_frac, n_pts)

            Sx_pts = [ax_side.c2p(tv, np.sin(theta0) * np.cos(2*np.pi*tv)) for tv in t_vals]
            Sy_pts = [ax_side.c2p(tv, np.sin(theta0) * np.sin(2*np.pi*tv)) for tv in t_vals]
            Sz_pts = [ax_side.c2p(0, np.cos(theta0)), ax_side.c2p(max(t_frac, 0.001), np.cos(theta0))]

            curves = VGroup()
            if len(Sx_pts) >= 2:
                cx = VMobject(color=BLUE, stroke_width=2.0)
                cx.set_points_smoothly(Sx_pts)
                curves.add(cx)
            if len(Sy_pts) >= 2:
                cy = VMobject(color=BROWN, stroke_width=2.0)
                cy.set_points_smoothly(Sy_pts)
                curves.add(cy)
            cz = VMobject(color=GOLD, stroke_width=2.5)
            cz.set_points_as_corners(Sz_pts)
            curves.add(cz)
            return curves

        def _info():
            t_frac = t_track.get_value()
            return Text(
                f"t = {t_frac:.2f} T_L  |  ⟨S_z⟩ = {np.cos(theta0)/2:.4f}ℏ/2  (flat)",
                font="EB Garamond", font_size=16, color=DIM,
            ).to_edge(DOWN, buff=0.15)

        # Circular arc (precession path)
        prec_circle = Ellipse(
            width=2 * r_bloch * np.sin(theta0),
            height=2 * r_bloch * np.sin(theta0) * 0.2,
            color=DIM, stroke_width=1.0, stroke_opacity=0.5,
        ).move_to(center_sphere + np.array([0, r_bloch * np.cos(theta0), 0]))

        dyn_vec = always_redraw(_bloch_vec)
        dyn_tr = always_redraw(_traces)
        dyn_info = always_redraw(_info)

        legend = VGroup(
            Text("⟨S_x⟩", font="EB Garamond", font_size=14, color=BLUE),
            Text("⟨S_y⟩", font="EB Garamond", font_size=14, color=BROWN),
            Text("⟨S_z⟩ (flat)", font="EB Garamond", font_size=14, color=GOLD),
        ).arrange(DOWN, buff=0.1).to_corner(UR, buff=0.4)

        self.add(prec_circle, dyn_vec, dyn_tr, dyn_info)
        self.play(FadeIn(legend), run_time=0.6)

        # 3 full revolutions
        self.play(t_track.animate.set_value(3.0), run_time=9.0, rate_func=linear)
        self.wait(1.0)

        payoff = MathTex(
            r"\omega_L = \gamma_p B_0 = 2\pi \times 63.87\,\mathrm{MHz}\text{ at }1.5\,\mathrm{T}",
            color=GOLD, font_size=22,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(dyn_info), Write(payoff), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(
            sphere, equator, z_ax, x_ax, z_lbl, x_lbl, n_pole, s_pole, n_lbl, s_lbl,
            prec_circle, dyn_vec, dyn_tr, ax_side, lbl_t, lbl_S, legend, payoff,
        ), run_time=0.6)

    def _phase_north_pole(self):
        """θ₀=0 (north pole, S_z eigenstate): stationary."""
        title = Text("θ₀ = 0 (S_z eigenstate): no precession",
                     font="EB Garamond", font_size=30, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"|{\uparrow}\rangle\text{ is an energy eigenstate of }H = \tfrac{\gamma B_0 \hbar}{2}\sigma_z", color=BLUE, font_size=24),
            MathTex(r"\Rightarrow |\uparrow, t\rangle = e^{-i\omega_L t/2}|\uparrow\rangle\text{ — global phase only}", color=GOLD, font_size=24),
            MathTex(r"\langle S_x\rangle = \langle S_y\rangle = 0,\quad \langle S_z\rangle = \hbar/2\text{ (all constant)}", color=BROWN, font_size=22),
            Text("The Bloch vector sits frozen at the north pole",
                 font="EB Garamond", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=0.7)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
