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


def oscillating_wave(x_arr, k=3.0, amp=0.8):
    return amp * np.cos(k * x_arr)

def exponential_decay(x_arr, x0, kappa=1.5, amp=0.8):
    return amp * np.exp(-kappa * (x_arr - x0))


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("Tunnel Through\na Thin Wall", size=54)
        title.move_to(ORIGIN)
        sub = terra_txt("T ≈ e^(−2κL)", size=38)
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
        lbl = ink_txt("Classically: not enough\nenergy → bounces back.", size=38)
        lbl.to_edge(LEFT, buff=0.8)
        # Hill
        xs = np.linspace(1.0, 6.0, 100)
        hill_ys = 2.0 * np.exp(-0.5 * ((xs - 3.5) / 0.6) ** 2)
        baseline_y = -1.5
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, hill_ys)]
        hill = VMobject(color=INK, stroke_width=4)
        hill.set_points_smoothly(pts)
        base = Line([0.0, baseline_y, 0], [7.0, baseline_y, 0], color=INK, stroke_width=3)
        # Ball
        ball = Dot([1.5, baseline_y + 0.2, 0], radius=0.22, color=TERRA)
        ball_lbl = terra_txt("ball", size=24)
        ball_lbl.next_to(ball, UP, buff=0.2)
        self.add(base, hill, ball, ball_lbl)
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(ball.animate.move_to([2.9, baseline_y + 1.4, 0]),
                  ball_lbl.animate.move_to([2.9, baseline_y + 1.9, 0]),
                  run_time=0.8)
        self.play(ball.animate.move_to([1.5, baseline_y + 0.2, 0]),
                  ball_lbl.animate.next_to(ball, UP, buff=0.2),
                  run_time=0.8, rate_func=there_and_back)
        back_lbl = terra_txt("← bounces back", size=28)
        back_lbl.move_to([2.0, baseline_y + 1.5, 0])
        self.play(FadeIn(back_lbl), run_time=0.3)
        self.wait(max(0.1, dur - 2.4))


class H02_ParticleOnOtherSide(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        lbl = ink_txt("Quantum: particle found\non the other side!", size=38)
        lbl.to_edge(LEFT, buff=0.8)
        # Wall block
        wall = Rectangle(width=0.6, height=3.0, color=TERRA, stroke_width=2)
        wall.set_fill(TERRA, opacity=0.3)
        wall.move_to([1.5, -0.2, 0])
        wall_lbl = terra_txt("wall", size=24)
        wall_lbl.next_to(wall, UP, buff=0.2)
        # Particle dot emerging on right
        particle = Dot([3.5, -0.2, 0], radius=0.22, color=INK)
        surprise = terra_txt("!", size=80)
        surprise.move_to([4.5, 0.5, 0])
        self.add(wall, wall_lbl)
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(FadeIn(particle), FadeIn(surprise), run_time=0.5)
        self.wait(max(0.1, dur - 1.0))


class A01_WaveAndBarrier(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        baseline_y = -0.5
        wall_x = 1.5; wall_w = 0.8
        # Incoming oscillating wave from left
        xs = np.linspace(-6.5, wall_x, 200)
        ys = oscillating_wave(xs, k=2.5, amp=0.9)
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        # Barrier block
        barrier = Rectangle(width=wall_w, height=3.5, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.35)
        barrier.move_to([wall_x + wall_w / 2, baseline_y + 0.25, 0])
        barrier_lbl = terra_txt("V > E", size=26)
        barrier_lbl.next_to(barrier, UP, buff=0.25)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        incident_lbl = ink_txt("incident wave →", size=26)
        incident_lbl.move_to([-4.0, baseline_y + 1.5, 0])
        self.play(Create(axis), Create(barrier), FadeIn(barrier_lbl), run_time=0.5)
        self.play(Create(wave), FadeIn(incident_lbl), run_time=0.7)
        self.wait(max(0.1, dur - 1.2))


class A02_StopSign(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        baseline_y = -0.5
        wall_x = 1.5; wall_w = 0.8
        xs = np.linspace(-6.5, wall_x, 200)
        ys = oscillating_wave(xs, k=2.5, amp=0.9)
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        barrier = Rectangle(width=wall_w, height=3.5, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.35)
        barrier.move_to([wall_x + wall_w / 2, baseline_y + 0.25, 0])
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        stop = Cross(color=TERRA, stroke_width=8)
        stop.scale(0.6)
        stop.move_to([wall_x, baseline_y + 0.8, 0])
        stop_lbl = terra_txt("STOP?", size=32)
        stop_lbl.next_to(stop, UP, buff=0.2)
        self.add(axis, wave, barrier)
        self.play(FadeIn(stop), FadeIn(stop_lbl), run_time=0.5)
        refuses_lbl = terra_txt("…wave refuses.", size=30)
        refuses_lbl.move_to([4.0, 1.5, 0])
        self.play(FadeIn(refuses_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.9))


class A03_ExponentialDecay(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        baseline_y = -0.5
        wall_x_left = 1.0; wall_w = 1.5; wall_x_right = wall_x_left + wall_w
        # Incident wave
        xs_left = np.linspace(-6.5, wall_x_left, 200)
        ys_left = oscillating_wave(xs_left, k=2.5, amp=0.9)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        # Inside barrier: exponential decay
        xs_inside = np.linspace(wall_x_left, wall_x_right, 100)
        ys_inside = exponential_decay(xs_inside, wall_x_left, kappa=1.5, amp=0.9)
        pts_inside = [[x, baseline_y + y, 0] for x, y in zip(xs_inside, ys_inside)]
        decay_curve = VMobject(color=TERRA, stroke_width=4)
        decay_curve.set_points_smoothly(pts_inside)
        barrier = Rectangle(width=wall_w, height=3.5, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.25)
        barrier.move_to([wall_x_left + wall_w / 2, baseline_y + 0.25, 0])
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        decay_lbl = terra_txt("e^(-κx) inside", size=28)
        decay_lbl.move_to([wall_x_left + wall_w / 2, baseline_y + 2.5, 0])
        kappa_lbl = ink_txt("κ = √(2m(V-E))/ħ", size=24)
        kappa_lbl.move_to([0.0, baseline_y - 1.5, 0])
        self.add(axis, barrier, wave_left)
        self.play(Create(decay_curve), FadeIn(decay_lbl), run_time=0.7)
        self.play(FadeIn(kappa_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.1))


class A04_ThickBarrier(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        baseline_y = -0.5
        wall_x_left = 0.0; wall_w = 4.0; wall_x_right = wall_x_left + wall_w
        xs_left = np.linspace(-6.5, wall_x_left, 200)
        ys_left = oscillating_wave(xs_left, k=2.5, amp=0.9)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        xs_inside = np.linspace(wall_x_left, wall_x_right, 200)
        ys_inside = exponential_decay(xs_inside, wall_x_left, kappa=1.2, amp=0.9)
        pts_inside = [[x, baseline_y + y, 0] for x, y in zip(xs_inside, ys_inside)]
        decay_curve = VMobject(color=TERRA, stroke_width=4)
        decay_curve.set_points_smoothly(pts_inside)
        barrier = Rectangle(width=wall_w, height=3.5, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.25)
        barrier.move_to([wall_x_left + wall_w / 2, baseline_y + 0.25, 0])
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        thick_lbl = ink_txt("thick barrier L", size=26)
        thick_lbl.move_to([wall_x_left + wall_w / 2, baseline_y + 2.5, 0])
        zero_lbl = terra_txt("≈ 0 at exit", size=26)
        zero_lbl.move_to([wall_x_right + 1.0, baseline_y + 0.5, 0])
        self.add(axis, barrier, wave_left, decay_curve, thick_lbl)
        self.play(FadeIn(zero_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.4))


class A05_ThinBarrier(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        baseline_y = -0.5
        wall_x_left = 0.0; wall_w = 1.2; wall_x_right = wall_x_left + wall_w
        xs_left = np.linspace(-6.5, wall_x_left, 200)
        ys_left = oscillating_wave(xs_left, k=2.5, amp=0.9)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        xs_inside = np.linspace(wall_x_left, wall_x_right, 100)
        ys_inside = exponential_decay(xs_inside, wall_x_left, kappa=1.2, amp=0.9)
        pts_inside = [[x, baseline_y + y, 0] for x, y in zip(xs_inside, ys_inside)]
        decay_curve = VMobject(color=TERRA, stroke_width=4)
        decay_curve.set_points_smoothly(pts_inside)
        barrier = Rectangle(width=wall_w, height=3.5, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.25)
        barrier.move_to([wall_x_left + wall_w / 2, baseline_y + 0.25, 0])
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        thin_lbl = ink_txt("thin barrier L", size=26)
        thin_lbl.move_to([wall_x_left + wall_w / 2, baseline_y + 2.8, 0])
        amp_at_exit = float(ys_inside[-1])
        survive_lbl = terra_txt(f"still has amplitude!", size=28)
        survive_lbl.move_to([wall_x_right + 2.0, baseline_y + 1.2, 0])
        dot_exit = Dot([wall_x_right, baseline_y + amp_at_exit, 0],
                       radius=0.2, color=TERRA)
        self.add(axis, barrier, wave_left, decay_curve, thin_lbl)
        self.play(FadeIn(dot_exit), FadeIn(survive_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.5))


class A06_TransmittedWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        baseline_y = -0.5
        wall_x_left = -0.5; wall_w = 1.2; wall_x_right = wall_x_left + wall_w
        xs_left = np.linspace(-6.5, wall_x_left, 200)
        ys_left = oscillating_wave(xs_left, k=2.5, amp=0.9)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        xs_inside = np.linspace(wall_x_left, wall_x_right, 80)
        ys_inside = exponential_decay(xs_inside, wall_x_left, kappa=1.2, amp=0.9)
        pts_inside = [[x, baseline_y + y, 0] for x, y in zip(xs_inside, ys_inside)]
        decay_curve = VMobject(color=TERRA, stroke_width=3)
        decay_curve.set_points_smoothly(pts_inside)
        barrier = Rectangle(width=wall_w, height=3.5, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.25)
        barrier.move_to([wall_x_left + wall_w / 2, baseline_y + 0.25, 0])
        # Transmitted wave: same frequency, smaller amplitude
        amp_exit = float(ys_inside[-1])
        xs_right = np.linspace(wall_x_right, 6.5, 200)
        ys_right = oscillating_wave(xs_right - wall_x_right, k=2.5, amp=amp_exit)
        pts_right = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        wave_right = VMobject(color=TERRA, stroke_width=3)
        wave_right.set_points_smoothly(pts_right)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        trans_lbl = terra_txt("transmitted wave", size=26)
        trans_lbl.move_to([4.0, baseline_y + 1.6, 0])
        self.add(axis, barrier, wave_left, decay_curve)
        self.play(Create(wave_right), FadeIn(trans_lbl), run_time=0.8)
        self.wait(max(0.1, dur - 0.8))


class A07_SmallButReal(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        baseline_y = -0.5
        wall_x_left = -0.5; wall_w = 1.2; wall_x_right = wall_x_left + wall_w
        xs_left = np.linspace(-6.5, wall_x_left, 200)
        ys_left = oscillating_wave(xs_left, k=2.5, amp=0.9)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        xs_inside = np.linspace(wall_x_left, wall_x_right, 80)
        ys_inside = exponential_decay(xs_inside, wall_x_left, kappa=1.2, amp=0.9)
        amp_exit = float(ys_inside[-1])
        pts_inside = [[x, baseline_y + y, 0] for x, y in zip(xs_inside, ys_inside)]
        decay_curve = VMobject(color=TERRA, stroke_width=3)
        decay_curve.set_points_smoothly(pts_inside)
        barrier = Rectangle(width=wall_w, height=3.5, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.25)
        barrier.move_to([wall_x_left + wall_w / 2, baseline_y + 0.25, 0])
        xs_right = np.linspace(wall_x_right, 6.5, 200)
        ys_right = oscillating_wave(xs_right - wall_x_right, k=2.5, amp=amp_exit)
        pts_right = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        wave_right = VMobject(color=TERRA, stroke_width=3)
        wave_right.set_points_smoothly(pts_right)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        self.add(axis, barrier, wave_left, decay_curve, wave_right)
        chance_lbl = terra_txt("small but real chance\nof tunneling", size=32)
        chance_lbl.move_to([3.5, 1.5, 0])
        t_formula = ink_txt("T ≈ e^(-2κL)", size=28)
        t_formula.move_to([3.5, -2.0, 0])
        self.play(FadeIn(chance_lbl), run_time=0.5)
        self.play(FadeIn(t_formula), run_time=0.4)
        self.wait(max(0.1, dur - 0.9))


class A08_TunneledNotOver(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        baseline_y = 0.3
        wall_x_left = -0.5; wall_w = 1.2; wall_x_right = wall_x_left + wall_w
        xs_left = np.linspace(-6.5, wall_x_left, 200)
        ys_left = oscillating_wave(xs_left, k=2.5, amp=0.7)
        pts_left = [[x, baseline_y + y, 0] for x, y in zip(xs_left, ys_left)]
        wave_left = VMobject(color=INK, stroke_width=3)
        wave_left.set_points_smoothly(pts_left)
        xs_inside = np.linspace(wall_x_left, wall_x_right, 80)
        ys_inside = exponential_decay(xs_inside, wall_x_left, kappa=1.2, amp=0.7)
        amp_exit = float(ys_inside[-1])
        pts_inside = [[x, baseline_y + y, 0] for x, y in zip(xs_inside, ys_inside)]
        decay_curve = VMobject(color=TERRA, stroke_width=3)
        decay_curve.set_points_smoothly(pts_inside)
        barrier = Rectangle(width=wall_w, height=3.0, color=TERRA, stroke_width=2)
        barrier.set_fill(TERRA, opacity=0.25)
        barrier.move_to([wall_x_left + wall_w / 2, baseline_y + 0.0, 0])
        xs_right = np.linspace(wall_x_right, 6.5, 200)
        ys_right = oscillating_wave(xs_right - wall_x_right, k=2.5, amp=amp_exit)
        pts_right = [[x, baseline_y + y, 0] for x, y in zip(xs_right, ys_right)]
        wave_right = VMobject(color=TERRA, stroke_width=3)
        wave_right.set_points_smoothly(pts_right)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        self.add(axis, barrier, wave_left, decay_curve, wave_right)
        label = terra_txt("tunneled through,\nnot over", size=44)
        label.move_to([0, -2.5, 0])
        underline = Line(label.get_left() + DOWN * 0.08,
                         label.get_right() + DOWN * 0.08,
                         color=TERRA, stroke_width=3)
        self.play(Write(label), run_time=0.9)
        self.play(Create(underline), run_time=0.3)
        self.wait(max(0.1, dur - 1.2))
