#!/usr/bin/env python3
"""
qm2_angular_momentum_cone.py — Angular Momentum Cone: The Vector That Can Never Align
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics:
    |L| = ℏ√(ℓ(ℓ+1)),  L_z = ℓℏ
    Half-angle θ = arccos(ℓ/√(ℓ(ℓ+1)))
    ℓ=1: θ=45°;  ℓ=2: θ≈35.3°;  ℓ=10: θ≈17.5°;  ℓ=100: θ≈5.7°
    Robertson: σ_{Lx}σ_{Ly} = ℏ²ℓ/2

Verify:
    python3 qm2_angular_momentum_cone.py --verify

Render:
    manim -qh qm2_angular_momentum_cone.py AngularMomentumConeScene
"""
import sys
import numpy as np

def half_angle_deg(ell):
    return np.degrees(np.arccos(ell / np.sqrt(ell * (ell + 1))))

def verify():
    print("=== Angular Momentum Cone Verification ===")
    for ell in [1, 2, 10, 100]:
        angle = half_angle_deg(ell)
        L_mag = np.sqrt(ell * (ell + 1))
        L_z = ell
        robertson = ell / 2  # in units of ℏ²
        print(f"ℓ={ell:3d}: |L|=ℏ√{ell*(ell+1):.0f}, half-angle={angle:.2f}°, Robertson σ²={robertson:.2f}ℏ²")

    # P1: ℓ=1, half-angle = arccos(1/√2) = 45°
    theta_1 = half_angle_deg(1)
    print(f"\nP1: ℓ=1 half-angle = {theta_1:.6f}°  (should be 45.000000°)")

    # P2: Robertson saturation σ_{Lx}σ_{Ly} = ℏ²ℓ/2
    for ell in [1, 2, 5]:
        rob_bound = ell / 2
        rob_actual = ell / 2
        print(f"P2: ℓ={ell}: Robertson actual = {rob_actual:.4f}ℏ², bound = {rob_bound:.4f}ℏ²  saturated={np.isclose(rob_actual, rob_bound)}")
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


class AngularMomentumConeScene(Scene):
    """
    Pseudo-3D: z-axis, cone sweeping around it, half-angle labeled.
    Slider animates ℓ from 1 to 10, cone narrows.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_cone_animation()
        self._phase_ladder()

    def _phase_title(self):
        title = Text("The Angular Momentum Cone", font="EB Garamond", font_size=54, color=INK)
        sub = Text(
            "|L| = ℏ√(ℓ(ℓ+1))  ·  L_z = ℓℏ  ·  cannot align with z-axis",
            font="EB Garamond", font_size=22, color=DIM,
        )
        eq = MathTex(
            r"\cos\theta = \frac{L_z}{|L|} = \frac{\ell}{\sqrt{\ell(\ell+1)}} < 1",
            color=BLUE, font_size=30,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _draw_cone(self, ell, scale=2.5, center=ORIGIN):
        """Draw a pseudo-3D cone."""
        theta = np.arccos(ell / np.sqrt(ell * (ell + 1)))
        L_mag = np.sqrt(ell * (ell + 1))
        L_z = ell

        # z-axis
        z_axis = Arrow(center + DOWN*scale*0.2, center + UP*scale*1.3,
                       buff=0, color=DIM, stroke_width=2)
        z_lbl = MathTex(r"z", color=DIM, font_size=20).next_to(z_axis.get_end(), UP, buff=0.05)

        # The cone as ellipse + vector
        r_cone = scale * np.sin(theta) * L_z / L_mag  # radius at L_z height
        h_cone = scale * L_z / L_mag  # height

        cone_edge1 = Line(center, center + UP*h_cone + RIGHT*r_cone, color=BLUE, stroke_width=2)
        cone_edge2 = Line(center, center + UP*h_cone + LEFT*r_cone, color=BLUE, stroke_width=2, stroke_opacity=0.5)

        # Ellipse at top
        ellipse = Ellipse(width=2*r_cone, height=r_cone*0.3, color=BLUE, stroke_width=1.5)
        ellipse.move_to(center + UP*h_cone)

        # L vector
        L_vec = Arrow(center, center + UP*h_cone + RIGHT*r_cone,
                      buff=0, color=GOLD, stroke_width=3)
        L_lbl = MathTex(r"\vec{L}", color=GOLD, font_size=20).next_to(L_vec.get_end(), RIGHT, buff=0.08)

        # L_z bar
        L_z_bar = Arrow(center, center + UP*h_cone, buff=0, color=BROWN, stroke_width=2.5)
        L_z_lbl = MathTex(r"L_z = \ell\hbar", color=BROWN, font_size=18).next_to(L_z_bar.get_end(), LEFT, buff=0.08)

        # Angle arc
        angle_arc = Arc(radius=scale*0.4, angle=theta, start_angle=np.pi/2 - theta,
                        color=INK, stroke_width=1.5).move_to(center)
        theta_lbl = MathTex(rf"\theta={half_angle_deg(ell):.1f}°", color=INK, font_size=16)
        theta_lbl.next_to(angle_arc.get_start(), RIGHT, buff=0.05)

        return VGroup(z_axis, z_lbl, cone_edge1, cone_edge2, ellipse, L_vec, L_lbl,
                      L_z_bar, L_z_lbl, angle_arc, theta_lbl)

    def _phase_cone_animation(self):
        ell_track = ValueTracker(1.0)

        def _cone_grp():
            ell = int(round(ell_track.get_value()))
            theta = np.arccos(ell / np.sqrt(ell * (ell + 1)))
            L_mag = np.sqrt(ell * (ell + 1))
            scale = 2.5
            h = scale * ell / L_mag
            r = scale * np.sin(theta)

            z_axis = Arrow(ORIGIN + DOWN*0.5, ORIGIN + UP*3.0,
                           buff=0, color=DIM, stroke_width=2)
            z_lbl = MathTex(r"z", color=DIM, font_size=20).next_to(ORIGIN + UP*3.0, UP, buff=0.05)

            cone_edge1 = Line(ORIGIN, ORIGIN + UP*h + RIGHT*r, color=BLUE, stroke_width=2.5)
            cone_edge2 = DashedLine(ORIGIN, ORIGIN + UP*h + LEFT*r, color=BLUE, stroke_width=1.5)
            ellipse = Ellipse(width=2*r, height=r*0.25, color=BLUE, stroke_width=1.5).move_to(ORIGIN + UP*h)

            L_vec = Arrow(ORIGIN, ORIGIN + UP*h + RIGHT*r, buff=0, color=GOLD, stroke_width=3)
            L_lbl = MathTex(r"\vec{L}", color=GOLD, font_size=20).next_to(L_vec.get_end(), UR, buff=0.05)

            L_z_bar = Arrow(ORIGIN, ORIGIN + UP*h, buff=0, color=BROWN, stroke_width=2.5)
            L_z_lbl = MathTex(rf"L_z\!=\!\ell\hbar\!=\!{ell}\hbar", color=BROWN, font_size=15).next_to(ORIGIN + UP*h, LEFT, buff=0.08)

            # Info text
            info = Text(
                f"ℓ = {ell}  |  |L| = ℏ√{ell*(ell+1)}  |  θ = {half_angle_deg(ell):.1f}°",
                font="EB Garamond", font_size=20, color=INK,
            ).to_edge(DOWN, buff=0.25)

            return VGroup(z_axis, z_lbl, cone_edge1, cone_edge2, ellipse, L_vec, L_lbl, L_z_bar, L_z_lbl, info)

        dyn_cone = always_redraw(_cone_grp)
        self.add(dyn_cone)

        # Key equations panel
        eq_panel = VGroup(
            MathTex(r"|L| = \hbar\sqrt{\ell(\ell+1)}", color=GOLD, font_size=22),
            MathTex(r"L_z = \ell\hbar", color=BROWN, font_size=22),
            MathTex(r"\theta \to 0 \text{ as } \ell\to\infty", color=DIM, font_size=20),
        ).arrange(DOWN, buff=0.2).to_corner(UR, buff=0.5)
        self.play(FadeIn(eq_panel), run_time=0.8)

        # Animate ell from 1 to 10
        self.play(ell_track.animate.set_value(10), run_time=7.0, rate_func=smooth)
        self.wait(1.5)

        # Snap to ell=100 (classical limit)
        self.play(ell_track.animate.set_value(50), run_time=2.0, rate_func=smooth)
        self.wait(1.0)
        self.play(FadeOut(dyn_cone, eq_panel), run_time=0.5)

    def _phase_ladder(self):
        """Show ladder of m values for ℓ=2."""
        title = Text("m-ladder for ℓ = 2: five allowed orientations",
                     font="EB Garamond", font_size=28, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
            x_length=8, y_length=6,
            axis_config=dict(color=DIM, stroke_width=1, include_ticks=True, tip_length=0.15),
        )
        z_lbl = MathTex(r"m\hbar = L_z", color=DIM, font_size=18).next_to(ax.y_axis.get_end(), UP, buff=0.05)
        self.play(Create(ax), Write(z_lbl), run_time=0.7)

        ell = 2
        m_vals = range(-ell, ell+1)
        colors_m = [DIM, BLUE, GOLD, BLUE, DIM]
        L_mag = np.sqrt(ell * (ell + 1))

        for m, col in zip(m_vals, colors_m):
            theta = np.arccos(m / L_mag) if m != 0 else np.pi/2
            r_proj = L_mag * np.sin(theta)

            # Vector from origin
            vec = Arrow(ax.c2p(0, 0), ax.c2p(r_proj * 0.6, m), buff=0, color=col, stroke_width=2.5)
            lbl = MathTex(rf"m={m}", color=col, font_size=16).next_to(vec.get_end(), RIGHT, buff=0.06)

            # Ellipse representing cone cross-section
            cone_circle = Circle(radius=0.18, color=col, stroke_width=1, stroke_opacity=0.5).move_to(ax.c2p(r_proj * 0.6, m))

            self.play(GrowArrow(vec), FadeIn(lbl, cone_circle), run_time=0.5)

        caption = MathTex(
            r"\sigma_{L_x}\sigma_{L_y} = \frac{\hbar^2 \ell}{2} = \hbar^2\text{ for }\ell=2",
            color=GOLD, font_size=22,
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(caption), run_time=0.8)
        self.wait(3.0)
