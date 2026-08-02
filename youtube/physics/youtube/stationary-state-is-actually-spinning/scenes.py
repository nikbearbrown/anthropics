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


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("A Stationary State\nIs Actually Spinning", size=54)
        title.move_to(ORIGIN)
        sub = terra_txt("ψ = e^(-iEt/ħ)|n⟩", size=36)
        sub.next_to(title, DOWN, buff=0.7)
        bear = ink_txt("Bear's Notes · Quantum Mechanics", size=26)
        bear.next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(bear), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class H01_FrozenObject(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H01", 5.0)
        lbl = ink_txt('"Stationary state" —\nnothing is moving.', size=38)
        lbl.to_edge(LEFT, buff=1.0)
        # Frozen clock
        circle = Circle(radius=1.5, color=INK, stroke_width=4)
        circle.move_to([3.5, 0, 0])
        hand = Line([3.5, 0, 0], [3.5, 1.4, 0], color=INK, stroke_width=5)
        frozen = ink_txt("FROZEN", size=32)
        frozen.move_to([3.5, -2.3, 0])
        self.play(FadeIn(lbl), Create(circle), Create(hand), run_time=0.7)
        self.play(FadeIn(frozen), run_time=0.4)
        self.wait(max(0.1, dur - 1.1))


class H02_SpinningRevealed(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        lbl = ink_txt("Lift the cover —\nit's spinning underneath!", size=38)
        lbl.to_edge(LEFT, buff=1.0)
        circle = Circle(radius=1.5, color=INK, stroke_width=4)
        circle.move_to([3.5, 0, 0])
        # Spinning hand
        angle_tracker = ValueTracker(PI / 2)
        hand = always_redraw(lambda: Line(
            [3.5, 0, 0],
            [3.5 + 1.4 * np.cos(angle_tracker.get_value()),
             1.4 * np.sin(angle_tracker.get_value()), 0],
            color=TERRA, stroke_width=6
        ))
        spinning = ink_txt("SPINNING!", size=32)
        spinning.move_to([3.5, -2.3, 0])
        self.add(circle, hand)
        self.play(FadeIn(lbl), FadeIn(spinning), run_time=0.5)
        self.play(angle_tracker.animate.set_value(PI / 2 + 2 * PI),
                  run_time=min(dur - 0.5, 3.5), rate_func=linear)
        self.wait(max(0.1, dur - 4.0))


class A01_ArgandPlane(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        cx, cy = 0.0, 0.3
        # Axes
        re_axis = Arrow([cx - 4.0, cy, 0], [cx + 4.0, cy, 0],
                        color=INK, stroke_width=3, buff=0)
        im_axis = Arrow([cx, cy - 3.5, 0], [cx, cy + 3.5, 0],
                        color=INK, stroke_width=3, buff=0)
        re_lbl = ink_txt("Re", size=28)
        re_lbl.next_to(re_axis, RIGHT, buff=0.15)
        im_lbl = ink_txt("Im", size=28)
        im_lbl.next_to(im_axis, UP, buff=0.15)
        origin_dot = Dot([cx, cy, 0], radius=0.08, color=INK)
        title_lbl = ink_txt("Complex (Argand) plane", size=30)
        title_lbl.to_edge(UP, buff=0.5)
        self.play(FadeIn(title_lbl), run_time=0.4)
        self.play(Create(re_axis), Create(im_axis),
                  FadeIn(re_lbl), FadeIn(im_lbl), FadeIn(origin_dot), run_time=0.8)
        self.wait(max(0.1, dur - 1.2))


class A02_ClockHand(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        cx, cy = -1.5, 0.3
        re_axis = Arrow([cx - 3.5, cy, 0], [cx + 3.5, cy, 0],
                        color=INK, stroke_width=3, buff=0)
        im_axis = Arrow([cx, cy - 3.0, 0], [cx, cy + 3.0, 0],
                        color=INK, stroke_width=3, buff=0)
        re_lbl = ink_txt("Re", size=26); re_lbl.next_to(re_axis, RIGHT, buff=0.1)
        im_lbl = ink_txt("Im", size=26); im_lbl.next_to(im_axis, UP, buff=0.1)
        # Fixed-length hand pointing at 45°
        r = 2.0
        angle = PI / 4
        tip = [cx + r * np.cos(angle), cy + r * np.sin(angle), 0]
        hand = Arrow([cx, cy, 0], tip, color=TERRA, buff=0, stroke_width=6)
        tip_dot = Dot(tip, radius=0.15, color=TERRA)
        # Radius label
        radius_lbl = ink_txt("|ψ| = 1", size=28)
        radius_lbl.move_to([cx + 1.0, cy + 1.6, 0])
        unit_circle = Circle(radius=r, color=INK, stroke_width=1, stroke_opacity=0.4)
        unit_circle.move_to([cx, cy, 0])
        self.add(re_axis, im_axis, re_lbl, im_lbl, unit_circle)
        self.play(Create(hand), FadeIn(tip_dot), run_time=0.6)
        self.play(FadeIn(radius_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.0))


class A03_HandRotates(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        cx, cy = -1.5, 0.3
        re_axis = Arrow([cx - 3.5, cy, 0], [cx + 3.5, cy, 0],
                        color=INK, stroke_width=3, buff=0)
        im_axis = Arrow([cx, cy - 3.0, 0], [cx, cy + 3.0, 0],
                        color=INK, stroke_width=3, buff=0)
        re_lbl = ink_txt("Re", size=26); re_lbl.next_to(re_axis, RIGHT, buff=0.1)
        im_lbl = ink_txt("Im", size=26); im_lbl.next_to(im_axis, UP, buff=0.1)
        r = 2.0
        unit_circle = Circle(radius=r, color=INK, stroke_width=1, stroke_opacity=0.4)
        unit_circle.move_to([cx, cy, 0])
        angle_tracker = ValueTracker(PI / 4)
        hand = always_redraw(lambda: Arrow(
            [cx, cy, 0],
            [cx + r * np.cos(angle_tracker.get_value()),
             cy + r * np.sin(angle_tracker.get_value()), 0],
            color=TERRA, buff=0, stroke_width=6
        ))
        omega_lbl = ink_txt("ω = E/ħ", size=28)
        omega_lbl.move_to([cx + 3.5, cy + 2.5, 0])
        self.add(re_axis, im_axis, re_lbl, im_lbl, unit_circle, hand)
        self.play(FadeIn(omega_lbl), run_time=0.3)
        self.play(angle_tracker.animate.set_value(PI / 4 + 2 * PI),
                  run_time=min(dur - 0.3, 3.0), rate_func=linear)
        self.wait(max(0.1, dur - 3.3))


class A04_Projections(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        cx, cy = -1.5, 0.0
        re_axis = Arrow([cx - 3.5, cy, 0], [cx + 3.5, cy, 0],
                        color=INK, stroke_width=3, buff=0)
        im_axis = Arrow([cx, cy - 3.0, 0], [cx, cy + 3.0, 0],
                        color=INK, stroke_width=3, buff=0)
        re_lbl = ink_txt("Re", size=24); re_lbl.next_to(re_axis, RIGHT, buff=0.1)
        im_lbl = ink_txt("Im", size=24); im_lbl.next_to(im_axis, UP, buff=0.1)
        r = 2.0
        unit_circle = Circle(radius=r, color=INK, stroke_width=1, stroke_opacity=0.35)
        unit_circle.move_to([cx, cy, 0])
        angle_tracker = ValueTracker(0)
        hand = always_redraw(lambda: Arrow(
            [cx, cy, 0],
            [cx + r * np.cos(angle_tracker.get_value()),
             cy + r * np.sin(angle_tracker.get_value()), 0],
            color=INK, buff=0, stroke_width=5
        ))
        re_proj = always_redraw(lambda: DashedLine(
            [cx + r * np.cos(angle_tracker.get_value()),
             cy + r * np.sin(angle_tracker.get_value()), 0],
            [cx + r * np.cos(angle_tracker.get_value()), cy, 0],
            color=INK, stroke_width=2, dash_length=0.15
        ))
        im_proj = always_redraw(lambda: DashedLine(
            [cx + r * np.cos(angle_tracker.get_value()),
             cy + r * np.sin(angle_tracker.get_value()), 0],
            [cx, cy + r * np.sin(angle_tracker.get_value()), 0],
            color=INK, stroke_width=2, dash_length=0.15
        ))
        self.add(re_axis, im_axis, re_lbl, im_lbl, unit_circle, hand, re_proj, im_proj)
        re_cos_lbl = ink_txt("cos(ωt)", size=24)
        re_cos_lbl.move_to([cx + 3.0, cy - 2.5, 0])
        im_sin_lbl = ink_txt("sin(ωt)", size=24)
        im_sin_lbl.move_to([cx - 3.5, cy + 1.5, 0])
        self.play(FadeIn(re_cos_lbl), FadeIn(im_sin_lbl), run_time=0.4)
        self.play(angle_tracker.animate.set_value(2 * PI),
                  run_time=min(dur - 0.4, 5.0), rate_func=linear)
        self.wait(max(0.1, dur - 5.4))


class A05_CircleTrace(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        cx, cy = -1.5, 0.0
        re_axis = Arrow([cx - 3.5, cy, 0], [cx + 3.5, cy, 0],
                        color=INK, stroke_width=3, buff=0)
        im_axis = Arrow([cx, cy - 3.0, 0], [cx, cy + 3.0, 0],
                        color=INK, stroke_width=3, buff=0)
        re_lbl = ink_txt("Re", size=24); re_lbl.next_to(re_axis, RIGHT, buff=0.1)
        im_lbl = ink_txt("Im", size=24); im_lbl.next_to(im_axis, UP, buff=0.1)
        r = 2.0
        unit_circle = Circle(radius=r, color=TERRA, stroke_width=4)
        unit_circle.move_to([cx, cy, 0])
        const_lbl = ink_txt("|ψ| = constant", size=30)
        const_lbl.move_to([cx + 3.5, cy + 1.5, 0])
        self.add(re_axis, im_axis, re_lbl, im_lbl)
        self.play(Create(unit_circle), run_time=0.8)
        self.play(FadeIn(const_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.2))


class A06_ProbabilityBar(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        cx, cy = -2.0, 0.0
        r = 2.0
        unit_circle = Circle(radius=r, color=TERRA, stroke_width=4)
        unit_circle.move_to([cx, cy, 0])
        re_axis = Arrow([cx - 3.0, cy, 0], [cx + 3.0, cy, 0],
                        color=INK, stroke_width=2, buff=0)
        im_axis = Arrow([cx, cy - 2.5, 0], [cx, cy + 2.5, 0],
                        color=INK, stroke_width=2, buff=0)
        hand = Line([cx, cy, 0], [cx + r, cy, 0], color=TERRA, stroke_width=5)
        self.add(unit_circle, re_axis, im_axis, hand)
        # Probability bar on right
        bar_x = 3.5
        bar = Rectangle(width=0.8, height=2.5, color=INK, stroke_width=3)
        bar.set_fill(INK, opacity=0.25)
        bar.move_to([bar_x, 0, 0])
        bar_lbl = ink_txt("|ψ|²", size=28)
        bar_lbl.move_to([bar_x, -2.0, 0])
        steady_lbl = ink_txt("steady!", size=26)
        steady_lbl.move_to([bar_x, 2.0, 0])
        self.play(Create(bar), FadeIn(bar_lbl), run_time=0.6)
        self.play(FadeIn(steady_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.0))


class A07_SpinningFrozenTags(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        cx, cy = -2.0, 0.0
        r = 2.0
        angle_tracker = ValueTracker(0)
        unit_circle = Circle(radius=r, color=INK, stroke_width=1, stroke_opacity=0.4)
        unit_circle.move_to([cx, cy, 0])
        re_axis = Arrow([cx - 3.0, cy, 0], [cx + 3.0, cy, 0],
                        color=INK, stroke_width=2, buff=0)
        im_axis = Arrow([cx, cy - 2.5, 0], [cx, cy + 2.5, 0],
                        color=INK, stroke_width=2, buff=0)
        hand = always_redraw(lambda: Arrow(
            [cx, cy, 0],
            [cx + r * np.cos(angle_tracker.get_value()),
             cy + r * np.sin(angle_tracker.get_value()), 0],
            color=INK, buff=0, stroke_width=5
        ))
        spinning_tag = ink_txt("spinning", size=26)
        spinning_tag.move_to([cx + 3.5, cy + 2.5, 0])
        bar_x = 3.8
        bar = Rectangle(width=0.8, height=2.5, color=INK, stroke_width=3)
        bar.set_fill(INK, opacity=0.25)
        bar.move_to([bar_x, 0, 0])
        bar_lbl = ink_txt("|ψ|²", size=28)
        bar_lbl.move_to([bar_x, -2.0, 0])
        frozen_tag = ink_txt("frozen", size=26)
        frozen_tag.move_to([bar_x, 2.0, 0])
        self.add(unit_circle, re_axis, im_axis, hand, bar, bar_lbl)
        self.play(FadeIn(spinning_tag), FadeIn(frozen_tag), run_time=0.5)
        self.play(angle_tracker.animate.set_value(2 * PI),
                  run_time=min(dur - 0.5, 4.5), rate_func=linear)
        self.wait(max(0.1, dur - 5.0))


class A08_StationaryOutsideSpinning(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        label = ink_txt("stationary outside,\nspinning underneath", size=46)
        label.move_to(ORIGIN)
        underline = Line(label.get_left() + DOWN * 0.08,
                         label.get_right() + DOWN * 0.08,
                         color=TERRA, stroke_width=3)
        sub = ink_txt("e^(-iEt/ħ) spins;\n|ψ|² stays put.", size=30)
        sub.next_to(label, DOWN, buff=0.7)
        self.play(Write(label), run_time=0.9)
        self.play(Create(underline), run_time=0.3)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))
