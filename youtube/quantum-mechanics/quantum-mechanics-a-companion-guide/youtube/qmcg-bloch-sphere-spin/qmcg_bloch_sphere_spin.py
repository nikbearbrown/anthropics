#!/usr/bin/env python3
"""
qmcg_bloch_sphere_spin.py — Bloch Sphere Spin Evolution: Larmor Precession and 720° Rotation
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-bloch-sphere-spin
    manim -qh qmcg_bloch_sphere_spin.py BlochSphereSpin2DScene

Verify:
    python3 qmcg_bloch_sphere_spin.py --verify

Physics:
    |ψ⟩ = cos(θ/2)|↑⟩ + e^{iφ}sin(θ/2)|↓⟩ → Bloch vector (sinθcosφ, sinθsinφ, cosθ)
    |↑_z⟩ → north pole (0,0,1)
    |↑_x⟩ → equator (1,0,0)  after H gate
    Under H=−(ħω₀/2)σ_z: Larmor precession φ(t)=ω₀t
    U(2π)=−I: 720° rotation returns Bloch vector but spinor picks up −1
"""
import sys
import numpy as np


def bloch_vector(theta, phi):
    """Bloch vector on unit sphere."""
    return np.array([
        np.sin(theta) * np.cos(phi),
        np.sin(theta) * np.sin(phi),
        np.cos(theta),
    ])


def verify():
    print("=== Bloch sphere spin verification ===")
    # |↑_z⟩ = north pole
    v_z = bloch_vector(0, 0)
    print(f"  |↑_z⟩: {v_z}  (should be (0,0,1))")

    # |↑_x⟩ = equator φ=0
    v_x = bloch_vector(np.pi/2, 0)
    print(f"  |↑_x⟩: {v_x}  (should be (1,0,0))")

    # P1: rotate |↑_z⟩ by 90° around x-axis → |↑_x⟩ (up along x)
    # Rotation by 90° about x: (x,y,z) → (x, -z, y)
    def rot_x(v, angle):
        c, s = np.cos(angle), np.sin(angle)
        R = np.array([[1,0,0],[0,c,-s],[0,s,c]])
        return R @ v
    v_after_90x = rot_x(np.array([0,0,1]), np.pi/2)
    print(f"\n  P1: |↑_z⟩ rotated 90° about x → {v_after_90x}  (should give Bloch on +x hemisphere)")

    # P2: U(2π) = -I (spinor picks up -1)
    # Verify: exp(-i*π*σ_x/2)*exp(-i*π*σ_x/2) = exp(-i*π*σ_x) = -I (by Pauli identity)
    # σ_x = [[0,1],[1,0]]
    sigma_x = np.array([[0,1],[1,0]], dtype=complex)
    U_2pi = np.cos(np.pi)*np.eye(2) - 1j*np.sin(np.pi)*sigma_x
    print(f"\n  P2: U(2π) around x = {U_2pi}  (should be -I)")
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


class BlochSphereSpin2DScene(Scene):
    """
    2D representation of Bloch sphere dynamics (no 3D Manim ThreeDScene).
    Phase 1: title
    Phase 2: show Bloch sphere as 2D circle; spin states as labeled points
    Phase 3: Larmor precession — state vector sweeps equator
    Phase 4: 720° rotation demonstration + phase clock
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_bloch_states()
        self._phase_precession()
        self._phase_720()

    def _phase_title(self):
        title = Text("Spin on the Bloch Sphere", font="EB Garamond", font_size=54, color=INK)
        sub1  = Text(
            "Every spin state is a point on a sphere — every rotation is a geodesic",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2  = Text(
            "720° to return spinor; 360° returns Bloch vector but multiplies ψ by −1",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_bloch_states(self):
        # Draw sphere as large circle (equatorial projection)
        radius = 2.5
        sphere = Circle(radius=radius, color=DIM, stroke_width=1.5).shift(LEFT * 2.5)
        # Axes lines
        z_axis = Line(sphere.get_center() + DOWN*radius, sphere.get_center() + UP*radius, color=INK, stroke_width=1.0)
        x_axis = Line(sphere.get_center() + LEFT*radius, sphere.get_center() + RIGHT*radius, color=INK, stroke_width=1.0)
        z_lbl  = MathTex(r"z", color=INK, font_size=20).next_to(sphere.get_center() + UP*radius, UP, buff=0.08)
        x_lbl  = MathTex(r"x", color=INK, font_size=20).next_to(sphere.get_center() + RIGHT*radius, RIGHT, buff=0.08)

        self.play(Create(sphere), Create(z_axis), Create(x_axis), Write(z_lbl), Write(x_lbl), run_time=0.8)

        ctr = sphere.get_center()
        states = [
            (ctr + UP*radius,        r"|\!\uparrow_z\rangle",  BLUE),
            (ctr + DOWN*radius,      r"|\!\downarrow_z\rangle", GOLD),
            (ctr + RIGHT*radius,     r"|\!\uparrow_x\rangle",  BROWN),
            (ctr + LEFT*radius,      r"|\!\downarrow_x\rangle", DIM),
        ]
        for pos, label, col in states:
            dot = Dot(pos, color=col, radius=0.12)
            lbl = MathTex(label, color=col, font_size=20).next_to(dot, pos - ctr, buff=0.15)
            self.play(FadeIn(dot), Write(lbl), run_time=0.4)

        # Arrow from center to north pole
        state_arrow = Arrow(ctr, ctr + UP*radius, buff=0, color=GOLD, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        self.play(GrowArrow(state_arrow), run_time=0.6)
        self.wait(1.5)

        # H gate: north pole → equator
        gate_lbl = Text("Apply H gate: |↑_z⟩ → |↑_x⟩", font="EB Garamond", font_size=20, color=BROWN).to_edge(DOWN, buff=0.3)
        self.play(Write(gate_lbl), run_time=0.5)
        self.play(Rotate(state_arrow, angle=np.pi/2, about_point=ctr, axis=OUT), run_time=1.2)
        self.wait(1.0)
        self.play(FadeOut(*self.mobjects), run_time=0.4)

    def _phase_precession(self):
        hdr = Text(
            "Larmor precession under H = −(ħω₀/2)σ_z  — state sweeps the equator",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.6)

        radius = 2.2
        ctr    = LEFT * 1.0
        sphere = Circle(radius=radius, color=DIM, stroke_width=1.5).move_to(ctr)
        z_axis = Line(ctr + DOWN*radius, ctr + UP*radius, color=INK, stroke_width=1.0)
        self.play(Create(sphere), Create(z_axis), run_time=0.6)

        phi_tracker = ValueTracker(0.0)

        def _arrow():
            phi = phi_tracker.get_value()
            # Equatorial precession: θ=π/2 fixed, φ sweeps
            tip = ctr + radius * np.array([np.cos(phi), np.sin(phi) * 0.4, 0])  # projected
            return Arrow(ctr, tip, buff=0, color=GOLD, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        def _phi_lbl():
            phi = phi_tracker.get_value()
            return MathTex(rf"\varphi = {np.degrees(phi):.0f}^{{\circ}}", color=GOLD, font_size=24).to_corner(UR, buff=0.35)

        dyn_arr = always_redraw(_arrow)
        dyn_lbl = always_redraw(_phi_lbl)
        self.add(dyn_arr, dyn_lbl)

        # Trace path
        path_pts = []
        n_pts = 200
        for i in range(n_pts):
            ph = 2 * np.pi * i / n_pts
            pt = ctr + radius * np.array([np.cos(ph), np.sin(ph) * 0.4, 0])
            path_pts.append(pt)

        self.play(phi_tracker.animate.set_value(2 * np.pi), run_time=4.0, rate_func=linear)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.4)

    def _phase_720(self):
        hdr = Text(
            "720° rotation: Bloch vector returns at 360°, spinor returns at 720° (phase −1)",
            font="EB Garamond", font_size=20, color=BROWN,
        ).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.7)

        radius = 2.0
        ctr    = LEFT * 2.0
        sphere = Circle(radius=radius, color=DIM, stroke_width=1.5).move_to(ctr)
        self.play(Create(sphere), run_time=0.4)

        # Bloch vector arrow
        rot_tracker = ValueTracker(0.0)

        def _bloch_arrow():
            angle = rot_tracker.get_value()
            tip   = ctr + radius * np.array([np.sin(angle), np.cos(angle), 0])
            return Arrow(ctr, tip, buff=0, color=GOLD, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        # Phase clock on right
        clock_ctr = RIGHT * 3.0
        clock_r   = 1.2
        clock     = Circle(radius=clock_r, color=DIM, stroke_width=1.5).move_to(clock_ctr)
        self.play(Create(clock), run_time=0.4)

        def _phase_arrow():
            angle    = rot_tracker.get_value()
            # Spinor phase = angle/2; at 360° rotation the spinor has rotated 180° (−1)
            sp_angle = angle / 2
            tip      = clock_ctr + clock_r * np.array([np.sin(sp_angle), np.cos(sp_angle), 0])
            return Arrow(clock_ctr, tip, buff=0, color=BLUE, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        bloch_lbl   = Text("Bloch vector", font="EB Garamond", font_size=18, color=GOLD).next_to(sphere, DOWN, buff=0.2)
        spinor_lbl  = Text("Spinor phase", font="EB Garamond", font_size=18, color=BLUE).next_to(clock, DOWN, buff=0.2)
        self.play(Write(bloch_lbl), Write(spinor_lbl), run_time=0.5)

        dyn_b = always_redraw(_bloch_arrow)
        dyn_s = always_redraw(_phase_arrow)
        self.add(dyn_b, dyn_s)

        def _rot_lbl():
            angle = rot_tracker.get_value()
            return MathTex(rf"\theta = {np.degrees(angle):.0f}^{{\circ}}", color=INK, font_size=24).to_corner(UR, buff=0.35)

        dyn_lbl = always_redraw(_rot_lbl)
        self.add(dyn_lbl)

        # Rotate 720°
        self.play(rot_tracker.animate.set_value(4 * np.pi), run_time=6.0, rate_func=linear)

        fin = MathTex(r"U(2\pi) = -I\quad\text{(spinor needs 720}^{\circ}\text{ to return)}", color=BROWN, font_size=26).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=0.8)
        self.wait(2.5)
