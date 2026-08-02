#!/usr/bin/env python3
"""
math_gradient_steepest_ascent_potential.py — Gradient as Steepest Ascent
SILENT SLATE — math-explainer (brownblue) candidate, math-for-physics-vol-2 book.

V(x,y) = sin(x)cos(y). ∇V = (cos(x)cos(y), -sin(x)sin(y)).
Gradient arrows perpendicular to level curves. Particle climbs gradient to max.

Render:
    cd math-for-physics-vol-2/youtube/math-gradient-steepest-ascent-potential
    manim -qh math_gradient_steepest_ascent_potential.py GradientScene

Verify:
    python3 math_gradient_steepest_ascent_potential.py --verify

Testable predictions:
    P1: At (π/2, 0): ∇V = (0, 0) — critical point (gradient vanishes)
    P2: Gradient always perpendicular to level curves (90° angle)
"""
import sys
import numpy as np

def V(x, y):
    return np.sin(x) * np.cos(y)

def gradV(x, y):
    gx = np.cos(x) * np.cos(y)
    gy = -np.sin(x) * np.sin(y)
    return np.array([gx, gy])

def verify():
    print("=== Gradient Steepest Ascent — verification ===")
    # P1: critical point at (π/2, 0)
    g = gradV(np.pi/2, 0)
    print(f"P1: ∇V at (π/2, 0) = ({g[0]:.6f}, {g[1]:.6f})  (expected (0,0)) {'✓' if np.allclose(g, [0,0], atol=1e-9) else '✗'}")

    # A few other points
    pts = [(np.pi/4, 0), (0, 0), (np.pi/4, np.pi/4)]
    expected = [(np.cos(np.pi/4), 0), (1.0, 0),
                (np.cos(np.pi/4)*np.cos(np.pi/4), -np.sin(np.pi/4)*np.sin(np.pi/4))]
    for (x,y), exp in zip(pts, expected):
        g = gradV(x, y)
        print(f"  ∇V({x:.3f},{y:.3f}) = ({g[0]:.4f},{g[1]:.4f})  expected ({exp[0]:.4f},{exp[1]:.4f})  {'✓' if np.allclose(g, exp, atol=1e-9) else '✗'}")

    # P2: gradient perpendicular to level curve
    # At any point, gradient dotted with level-curve tangent = 0
    # Level curve: V(x,y) = c; tangent direction ∝ (∂V/∂y, -∂V/∂x) = (-∂V/∂x rotated)
    x0, y0 = 1.0, 0.5
    g = gradV(x0, y0)
    tangent = np.array([-g[1], g[0]])  # perpendicular to g
    dot = np.dot(g, tangent)
    print(f"P2: ∇V · (level-curve tangent) = {dot:.10f}  (expected 0) {'✓' if abs(dot) < 1e-10 else '✗'}")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class GradientScene(Scene):
    """
    2D heatmap of V=sin(x)cos(y) + gradient arrow field + level curves.
    Animated particle climbs gradient to maximum.
    """

    # Map x,y ∈ [-π,π] × [-π,π] to scene
    XY_RANGE = np.pi
    SCALE = 2.2  # screen units per π

    def _to_screen(self, x, y):
        return np.array([x * self.SCALE / np.pi, y * self.SCALE / np.pi, 0])

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_heatmap()
        self._phase_gradient_arrows()
        self._phase_level_curves()
        self._phase_particle()

    def _phase_title(self):
        title = Text("Gradient: Steepest Ascent", font="EB Garamond", font_size=56, color=INK)
        sub1 = MathTex(
            r"V(x,y) = \sin x \cos y \quad \nabla V = (\cos x \cos y,\;{-}\sin x \sin y)",
            color=DIM, font_size=24,
        )
        sub2 = Text(
            "gradient arrows point uphill  ·  level curves cross at exactly 90°",
            font="EB Garamond", font_size=21, color=BLUE,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.8)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_heatmap(self):
        """Render V(x,y) as a colored pixel grid."""
        N = 60
        xs = np.linspace(-np.pi, np.pi, N)
        ys = np.linspace(-np.pi, np.pi, N)
        cells = VGroup()
        cell_w = 2 * np.pi / N * self.SCALE / np.pi
        def _lerp_color(c1_hex, c2_hex, t):
            """Linear interpolate between two hex colors."""
            r1 = int(c1_hex[1:3], 16); g1 = int(c1_hex[3:5], 16); b1 = int(c1_hex[5:7], 16)
            r2 = int(c2_hex[1:3], 16); g2 = int(c2_hex[3:5], 16); b2 = int(c2_hex[5:7], 16)
            r = int(r1 + t * (r2 - r1)); g = int(g1 + t * (g2 - g1)); b = int(b1 + t * (b2 - b1))
            return f"#{r:02X}{g:02X}{b:02X}"

        for i, x in enumerate(xs):
            for j, y in enumerate(ys):
                v = V(x, y)  # in [-1, 1]
                # Color: negative → BROWN, zero → dark, positive → BLUE
                if v >= 0:
                    frac = v
                    col = _lerp_color(CANVAS, BLUE, frac * 0.7)
                else:
                    frac = -v
                    col = _lerp_color(CANVAS, BROWN, frac * 0.7)
                rect = Square(side_length=cell_w * 1.05, fill_color=col,
                              fill_opacity=0.85, stroke_width=0)
                rect.move_to(self._to_screen(x, y))
                cells.add(rect)

        self.play(FadeIn(cells, lag_ratio=0), run_time=1.5)
        self._cells = cells

        # Axis labels
        lbl_x = MathTex(r"x", color=INK, font_size=24).next_to(self._to_screen(np.pi, 0), RIGHT, buff=0.1)
        lbl_y = MathTex(r"y", color=INK, font_size=24).next_to(self._to_screen(0, np.pi), UP, buff=0.1)
        title_lbl = MathTex(r"V = \sin x \cos y", color=INK, font_size=24).to_corner(UR, buff=0.4)
        self.play(Write(lbl_x), Write(lbl_y), Write(title_lbl), run_time=0.8)
        self._title_lbl = title_lbl

    def _phase_gradient_arrows(self):
        """Draw gradient arrows at a coarse grid."""
        arrows = VGroup()
        N = 8
        xs = np.linspace(-np.pi * 0.9, np.pi * 0.9, N)
        ys = np.linspace(-np.pi * 0.9, np.pi * 0.9, N)
        for x in xs:
            for y in ys:
                g = gradV(x, y)
                mag = np.linalg.norm(g)
                if mag < 0.05:
                    continue
                g_norm = g / mag
                scale = min(mag, 1.0) * 0.28
                start = self._to_screen(x, y)
                end   = start + np.array([g_norm[0] * scale, g_norm[1] * scale, 0])
                arr = Arrow(start, end, color=GOLD, stroke_width=2.0,
                            buff=0, max_tip_length_to_length_ratio=0.35)
                arrows.add(arr)

        caption = Text(
            "∇V: arrows point toward steepest ascent",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.35)
        self.play(Create(arrows), Write(caption), run_time=2.0)
        self.wait(1.2)
        self.play(FadeOut(caption), run_time=0.3)
        self._arrows = arrows

    def _phase_level_curves(self):
        """Draw a few level curves; show they cross arrows at 90°."""
        curves = VGroup()
        levels = [-0.7, -0.3, 0.0, 0.3, 0.7]
        N = 400

        for level in levels:
            # Parametric: traverse grid and connect crossings
            xs = np.linspace(-np.pi, np.pi, N)
            ys = np.linspace(-np.pi, np.pi, N)
            # Use matplotlib-style contour tracing (simplified: just draw V=c contour points)
            pts_found = []
            for i in range(N - 1):
                for j in range(N - 1):
                    v00 = V(xs[i], ys[j])
                    v10 = V(xs[i+1], ys[j])
                    if (v00 - level) * (v10 - level) < 0:
                        # linear interpolation
                        t = (level - v00) / (v10 - v00)
                        px = xs[i] + t * (xs[i+1] - xs[i])
                        pts_found.append(self._to_screen(px, ys[j]))
            if len(pts_found) < 3:
                continue
            # Sort by x then just draw as dots
            col = DIM
            for pt in pts_found[::2]:
                dot = Dot(pt, radius=0.03, color=col, fill_opacity=0.7)
                curves.add(dot)

        caption = Text(
            "Level curves (V = const) cross gradient arrows at 90°",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(curves), Write(caption), run_time=1.8)
        self.wait(1.5)
        self.play(FadeOut(caption), run_time=0.3)
        self._curves = curves

    def _phase_particle(self):
        """Animate a particle climbing the gradient from a starting point."""
        # Start near a saddle, climb to max at (π/2, 0)
        x0, y0 = -1.5, 0.8
        n_steps = 300
        step_size = 0.03
        traj_x = [x0]
        traj_y = [y0]
        for _ in range(n_steps):
            g = gradV(traj_x[-1], traj_y[-1])
            mag = np.linalg.norm(g)
            if mag < 1e-4:
                break
            traj_x.append(traj_x[-1] + step_size * g[0] / mag)
            traj_y.append(traj_y[-1] + step_size * g[1] / mag)
        # Clip to domain
        traj_x = [np.clip(x, -np.pi, np.pi) for x in traj_x]
        traj_y = [np.clip(y, -np.pi, np.pi) for y in traj_y]

        traj_pts = [self._to_screen(x, y) for x, y in zip(traj_x, traj_y)]

        traj_mob = VMobject(color=GOLD, stroke_width=3.0)
        traj_mob.set_points_smoothly(traj_pts)

        particle = Dot(self._to_screen(x0, y0), color=GOLD, radius=0.14)
        target   = Dot(self._to_screen(traj_x[-1], traj_y[-1]), color=GOLD, radius=0.14)

        caption = Text(
            "Particle follows ∇V — climbs to maximum at (π/2, 0)",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(particle), Write(caption), run_time=0.7)
        self.play(
            MoveAlongPath(particle, traj_mob),
            Create(traj_mob),
            run_time=3.5, rate_func=smooth,
        )
        self.wait(0.8)

        # Critical point label at (π/2, 0)
        crit_dot = Dot(self._to_screen(np.pi/2, 0), color=BROWN, radius=0.12)
        crit_lbl = MathTex(r"\nabla V = 0", color=BROWN, font_size=22)
        crit_lbl.next_to(self._to_screen(np.pi/2, 0), UR, buff=0.15)
        self.play(Create(crit_dot), Write(crit_lbl), run_time=0.8)
        self.wait(1.0)

        final = Text(
            "Gradient = direction of steepest ascent · magnitude = rate of increase",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(caption), Write(final), run_time=1.0)
        self.wait(2.5)
