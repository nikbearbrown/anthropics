import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', '')
except Exception:
    DUR = {}; TITLE = ''

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


# Shared layout constants
WALL_X = 0.5
ALLOWED_COLOR = "#3D3929"  # INK
FORBIDDEN_COLOR = TERRA


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("The Wave Leaks\nInto the Forbidden Wall", size=50)
        title.move_to(ORIGIN)
        sub = terra_txt("ψ ∝ e^(−κx)  in classical forbidden zone", size=30)
        sub.next_to(title, DOWN, buff=0.7)
        bear = ink_txt("Bear's Notes · Quantum Mechanics", size=26)
        bear.next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(bear), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class H01_BallRollsBack(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H01", 5.0)
        lbl = ink_txt("Classical: ball rolls up,\nhits wall, rolls back.", size=52)
        lbl.to_edge(LEFT, buff=0.8)
        baseline_y = -1.5
        # hill / wall edge
        wall = Line([2.0, baseline_y, 0], [2.0, baseline_y + 3.0, 0], color=INK, stroke_width=4)
        base = Line([-5.0, baseline_y, 0], [2.0, baseline_y, 0], color=INK, stroke_width=3)
        ball = Dot([-2.5, baseline_y + 0.2, 0], radius=0.22, color=TERRA)
        self.add(wall, base)
        self.play(FadeIn(lbl), FadeIn(ball), run_time=0.5)
        # Roll toward wall and back
        self.play(ball.animate.move_to([1.7, baseline_y + 0.2, 0]), run_time=0.8)
        self.play(ball.animate.move_to([-2.5, baseline_y + 0.2, 0]), run_time=0.8)
        back_lbl = ink_txt("← bounces", size=42)
        back_lbl.move_to([-0.5, baseline_y + 1.0, 0])
        self.play(FadeIn(back_lbl), run_time=0.3)
        self.wait(max(0.1, dur - 2.4))


class H02_WaveGlows(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        lbl = ink_txt("Quantum wave glows\nright into the wall!", size=52)
        lbl.to_edge(LEFT, buff=0.8)
        baseline_y = -0.5
        # Wall
        wall = Line([WALL_X, baseline_y - 2.5, 0], [WALL_X, baseline_y + 2.5, 0],
                    color=INK, stroke_width=4)
        # Forbidden zone shading
        forbidden = Rectangle(width=5.0, height=5.0, color=TERRA, stroke_width=0)
        forbidden.set_fill(TERRA, opacity=0.15)
        forbidden.move_to([WALL_X + 2.5, baseline_y, 0])
        # Evanescent glow
        xs_right = np.linspace(WALL_X, WALL_X + 4.0, 100)
        ys_right = 0.9 * np.exp(-1.3 * (xs_right - WALL_X))
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        evanescent = VMobject(color=TERRA, stroke_width=2)
        evanescent.set_points_smoothly(pts)
        glows_lbl = ink_txt("glows in!", size=36)
        glows_lbl.move_to([WALL_X + 2.2, baseline_y + 1.5, 0])
        self.add(forbidden, wall)
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(Create(evanescent), FadeIn(glows_lbl), run_time=0.7)
        self.wait(max(0.1, dur - 1.2))


class A01_WallAndZone(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        baseline_y = 0.0
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        # Allowed (left)
        allowed_bg = Rectangle(width=7.5, height=7.0, color=INK, stroke_width=0)
        allowed_bg.set_fill(CREAM, opacity=1)
        allowed_bg.move_to([WALL_X - 3.75, baseline_y, 0])
        # Forbidden (right)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        allowed_lbl = ink_txt("allowed\n(E > V)", size=28)
        allowed_lbl.move_to([WALL_X - 3.0, baseline_y + 2.5, 0])
        forbidden_lbl = terra_txt("forbidden\n(E < V)", size=28)
        forbidden_lbl.move_to([WALL_X + 3.0, baseline_y + 2.5, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        x_lbl = ink_txt("x", size=26)
        x_lbl.move_to([7.2, baseline_y, 0])
        self.play(FadeIn(allowed_bg), FadeIn(forbidden_bg), run_time=0.3)
        self.play(Create(wall), Create(axis), FadeIn(x_lbl), run_time=0.5)
        self.play(FadeIn(allowed_lbl), FadeIn(forbidden_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.2))


class A02_BallBounces(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        baseline_y = 0.0
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        ball = Dot([-3.0, baseline_y + 0.2, 0], radius=0.22, color=INK)
        ball_lbl = ink_txt("classical ball", size=36)
        ball_lbl.next_to(ball, UP, buff=0.25)
        self.add(forbidden_bg, wall, axis)
        self.play(FadeIn(ball), FadeIn(ball_lbl), run_time=0.4)
        self.play(ball.animate.move_to([WALL_X - 0.3, baseline_y + 0.2, 0]),
                  ball_lbl.animate.next_to([WALL_X - 0.3, baseline_y + 0.4, 0], UP, buff=0.1),
                  run_time=0.7)
        bounce_lbl = ink_txt("← bounces", size=38)
        bounce_lbl.move_to([WALL_X - 1.5, baseline_y + 1.2, 0])
        self.play(ball.animate.move_to([-3.0, baseline_y + 0.2, 0]),
                  FadeIn(bounce_lbl), run_time=0.6)
        self.wait(max(0.1, dur - 1.7))


class A03_OscillatingWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        baseline_y = 0.0
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        # Wave on allowed side
        xs = np.linspace(-7.0, WALL_X, 300)
        ys = 0.9 * np.cos(2.5 * xs)
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        wave_lbl = ink_txt("ψ oscillates (E > V)", size=26)
        wave_lbl.move_to([-3.5, baseline_y + 1.8, 0])
        self.add(forbidden_bg, wall, axis)
        self.play(Create(wave), FadeIn(wave_lbl), run_time=0.8)
        self.wait(max(0.1, dur - 0.8))


class A04_BoundaryValue(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        baseline_y = 0.0
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        xs = np.linspace(-7.0, WALL_X, 300)
        amp_at_wall = 0.9 * np.cos(2.5 * WALL_X)
        ys = 0.9 * np.cos(2.5 * xs)
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        # Mark boundary value
        bv_dot = Dot([WALL_X, baseline_y + amp_at_wall, 0], radius=0.18, color=TERRA)
        bv_lbl = terra_txt("ψ(0) ≠ 0\n(non-zero, smooth)", size=28)
        bv_lbl.move_to([WALL_X + 2.5, baseline_y + 2.2, 0])
        arr = Arrow([WALL_X + 1.0, baseline_y + 1.6, 0],
                    [WALL_X + 0.2, baseline_y + amp_at_wall + 0.2, 0],
                    color=TERRA, buff=0.1, stroke_width=3)
        self.add(forbidden_bg, wall, axis, wave)
        self.play(FadeIn(bv_dot), Create(arr), FadeIn(bv_lbl), run_time=0.8)
        self.wait(max(0.1, dur - 0.8))


class A05_EvanescentTail(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        baseline_y = 0.0
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        xs_left = np.linspace(-7.0, WALL_X, 300)
        amp_at_wall = abs(0.9 * np.cos(2.5 * WALL_X))
        ys_left = 0.9 * np.cos(2.5 * xs_left)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        # Evanescent decay on right
        xs_right = np.linspace(WALL_X, WALL_X + 5.0, 200)
        ys_right = amp_at_wall * np.exp(-1.4 * (xs_right - WALL_X))
        pts_right = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        evanescent = VMobject(color=TERRA, stroke_width=2)
        evanescent.set_points_smoothly(pts_right)
        ev_lbl = ink_txt("ψ ~ e^(-κx)", size=42)
        ev_lbl.move_to([WALL_X + 2.5, baseline_y + 1.6, 0])
        self.add(forbidden_bg, wall, axis, wave_left)
        self.play(Create(evanescent), run_time=0.8)
        self.play(FadeIn(ev_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.2))


class A06_PenetrationDepth(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        baseline_y = 0.0
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        amp0 = 0.9
        xs_right = np.linspace(WALL_X, WALL_X + 5.0, 200)
        ys_right = amp0 * np.exp(-1.4 * (xs_right - WALL_X))
        pts_right = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        evanescent = VMobject(color=INK, stroke_width=2)
        evanescent.set_points_smoothly(pts_right)
        # Penetration depth 1/κ
        kappa = 1.4
        pen_x = WALL_X + 1.0 / kappa
        pen_y = amp0 * np.exp(-1.0)
        pen_line = DashedLine([pen_x, baseline_y, 0], [pen_x, baseline_y + pen_y, 0],
                              color=INK, stroke_width=2, dash_length=0.2)
        depth_brace = Brace(Line([WALL_X, baseline_y - 0.6, 0], [pen_x, baseline_y - 0.6, 0]),
                            direction=DOWN, color=INK)
        depth_lbl = ink_txt("δ = 1/κ", size=38)
        depth_lbl.next_to(depth_brace, DOWN, buff=0.15)
        self.add(forbidden_bg, wall, axis, evanescent)
        self.play(Create(pen_line), Create(depth_brace), FadeIn(depth_lbl), run_time=0.8)
        self.wait(max(0.1, dur - 0.8))


class A07_ReflectedArrow(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        baseline_y = 0.0
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        xs_right = np.linspace(WALL_X, WALL_X + 5.0, 200)
        ys_right = 0.9 * np.exp(-1.4 * (xs_right - WALL_X))
        pts_right = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        evanescent = VMobject(color=TERRA, stroke_width=2)
        evanescent.set_points_smoothly(pts_right)
        # Reflected wave on left (dashed, going back)
        xs_left = np.linspace(-7.0, WALL_X, 300)
        ys_reflected = 0.45 * np.cos(2.5 * xs_left + PI)  # phase-shifted
        pts_ref = [[x, baseline_y + y - 1.5, 0] for x, y in zip(xs_left, ys_reflected)]
        reflected = VMobject(color=INK, stroke_width=3, stroke_opacity=0.6)
        reflected.set_points_smoothly(pts_ref)
        ref_arrow = Arrow([WALL_X - 0.3, baseline_y - 1.5, 0],
                          [-4.0, baseline_y - 1.5, 0],
                          color=INK, buff=0, stroke_width=4)
        ref_lbl = ink_txt("reflected\n(most energy)", size=36)
        ref_lbl.move_to([-3.0, baseline_y - 2.5, 0])
        self.add(forbidden_bg, wall, axis, evanescent, reflected)
        self.play(Create(ref_arrow), FadeIn(ref_lbl), run_time=0.7)
        self.wait(max(0.1, dur - 0.7))


class A08_WaveLeaksLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        baseline_y = 0.5
        wall = Line([WALL_X, baseline_y - 3.5, 0], [WALL_X, baseline_y + 3.5, 0],
                    color=INK, stroke_width=5)
        forbidden_bg = Rectangle(width=8.0, height=7.0, color=TERRA, stroke_width=0)
        forbidden_bg.set_fill(TERRA, opacity=0.12)
        forbidden_bg.move_to([WALL_X + 4.0, baseline_y, 0])
        axis = Line([-7.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=2)
        xs_left = np.linspace(-7.0, WALL_X, 300)
        ys_left = 0.9 * np.cos(2.5 * xs_left)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        xs_right = np.linspace(WALL_X, WALL_X + 5.0, 200)
        ys_right = 0.9 * np.exp(-1.4 * (xs_right - WALL_X))
        pts_right = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        evanescent = VMobject(color=TERRA, stroke_width=2)
        evanescent.set_points_smoothly(pts_right)
        self.add(forbidden_bg, wall, axis, wave_left, evanescent)
        label = ink_txt("the wave leaks into\nthe forbidden wall", size=42)
        label.move_to([0, -2.4, 0])
        underline = Line(label.get_left() + DOWN * 0.08,
                         label.get_right() + DOWN * 0.08,
                         color=TERRA, stroke_width=3)
        self.play(Write(label), run_time=1.0)
        self.play(Create(underline), run_time=0.3)
        self.wait(max(0.1, dur - 1.3))
