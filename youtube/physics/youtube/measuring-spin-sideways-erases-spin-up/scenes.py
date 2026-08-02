import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
SLATE = "#5A5653"
RED = "#C0392B"
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

def slate_txt(t, size=36, color=SLATE, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class INTRO_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("INTRO", 5.98)
        series = ink_txt("Bear's Notes", size=52).move_to([0, 1.8, 0])
        title = ink_txt("Why Measuring Spin Sideways\nErases What You Just Learned\nAbout Spin Up", size=34)
        title.next_to(series, DOWN, buff=0.5)
        accent = Line(LEFT * 5, RIGHT * 5, color=TERRA, stroke_width=3).next_to(series, DOWN, buff=0.15)
        self.play(FadeIn(series), run_time=1.0)
        self.play(Create(accent), FadeIn(title), run_time=2.0)
        self.wait(dur - 3.0)


class H01_JarOfUpAtoms(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H01", 3.89)
        jar = RoundedRectangle(width=2.0, height=2.8, corner_radius=0.3,
                               color=INK, stroke_width=3).set_fill(CREAM, 1)
        arrows = VGroup(*[
            Arrow(start=ORIGIN, end=UP * 0.45, color=SLATE, stroke_width=4, buff=0,
                  max_tip_length_to_length_ratio=0.4).shift(
                (j - 1) * RIGHT * 0.5 + (i - 1) * UP * 0.55)
            for i in range(3) for j in range(3)
        ])
        jar.move_to(ORIGIN + RIGHT * 1)
        arrows.move_to(jar.get_center())
        label = ink_txt("spin-up\nonly", size=26).next_to(jar, DOWN, buff=0.25)
        person = ink_txt("(you)", size=26, color=SLATE).next_to(jar, LEFT, buff=0.6)
        self.play(FadeIn(jar), FadeIn(person), run_time=0.8)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), run_time=1.2)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 2.5)


class H02_CoinFlipBaffled(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H02", 5.46)
        jar = RoundedRectangle(width=2.0, height=2.8, corner_radius=0.3,
                               color=INK, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 1.5)
        arrows_mixed = VGroup(
            Arrow(ORIGIN, UP * 0.45, color=SLATE, stroke_width=4, buff=0,
                  max_tip_length_to_length_ratio=0.4).shift(jar.get_center() + LEFT * 0.5 + UP * 0.3),
            Arrow(ORIGIN, DOWN * 0.45, color=RED, stroke_width=4, buff=0,
                  max_tip_length_to_length_ratio=0.4).shift(jar.get_center() + UP * 0.3),
            Arrow(ORIGIN, UP * 0.45, color=SLATE, stroke_width=4, buff=0,
                  max_tip_length_to_length_ratio=0.4).shift(jar.get_center() + RIGHT * 0.5 + UP * 0.3),
        )
        question = ink_txt("?", size=72, color=TERRA).shift(LEFT * 3)
        label = ink_txt("coin flip!", size=28, color=RED).shift(LEFT * 3 + DOWN * 1.2)
        self.play(FadeIn(jar), run_time=0.5)
        self.play(FadeIn(arrows_mixed), run_time=0.8)
        self.play(FadeIn(question), run_time=0.5)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(dur - 2.3)


class A01_BeamEntersZBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 3.84)
        beam = Arrow(LEFT * 5, LEFT * 1.8, color=SLATE, stroke_width=5, buff=0,
                     max_tip_length_to_length_ratio=0.2)
        box = Square(side_length=1.4, color=INK, stroke_width=3).set_fill(CREAM, 1).move_to(ORIGIN)
        label = ink_txt("Z", size=44).move_to(box)
        sublabel = ink_txt("up / down", size=26).next_to(box, DOWN, buff=0.2)
        self.play(GrowArrow(beam), run_time=0.8)
        self.play(FadeIn(box), FadeIn(label), run_time=0.6)
        self.play(FadeIn(sublabel), run_time=0.4)
        self.wait(dur - 1.8)


class A02_ZBoxSplits(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 4.41)
        box = Square(side_length=1.4, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2)
        zlabel = ink_txt("Z", size=44).move_to(box)
        up_beam = Arrow(LEFT * 0.3, RIGHT * 2.5 + UP * 1.2, color=SLATE, stroke_width=5,
                        buff=0, max_tip_length_to_length_ratio=0.15)
        dn_beam = Arrow(LEFT * 0.3, RIGHT * 2.5 + DOWN * 1.2, color=RED, stroke_width=5,
                        buff=0, max_tip_length_to_length_ratio=0.15)
        up_label = ink_txt("spin-up only", size=24, color=SLATE).next_to(up_beam.get_end(), RIGHT, buff=0.15)
        cross = Cross(color=RED, stroke_width=6).scale(0.4).move_to(dn_beam.get_end() + RIGHT * 0.4)
        dn_label = ink_txt("blocked", size=22, color=RED).next_to(cross, RIGHT, buff=0.1)
        self.add(box, zlabel)
        self.play(GrowArrow(up_beam), run_time=0.6)
        self.play(GrowArrow(dn_beam), run_time=0.6)
        self.play(FadeIn(up_label), run_time=0.4)
        self.play(FadeIn(cross), FadeIn(dn_label), run_time=0.5)
        self.wait(dur - 2.1)


class A03_SpinUpEntersXBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 5.46)
        beam_in = Arrow(LEFT * 5, LEFT * 1.8, color=SLATE, stroke_width=5, buff=0,
                        max_tip_length_to_length_ratio=0.15)
        beam_label = ink_txt("spin-up", size=24, color=SLATE).next_to(beam_in, UP, buff=0.1)
        box = Square(side_length=1.4, color=INK, stroke_width=3).set_fill(CREAM, 1).move_to(ORIGIN)
        xlabel = ink_txt("X", size=44).move_to(box)
        sublabel = ink_txt("left / right", size=22).next_to(box, DOWN, buff=0.2)
        self.play(GrowArrow(beam_in), FadeIn(beam_label), run_time=0.9)
        self.play(FadeIn(box), FadeIn(xlabel), run_time=0.6)
        self.play(FadeIn(sublabel), run_time=0.4)
        self.wait(dur - 1.9)


class A04_XBoxFiftyFifty(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 4.6)
        box = Square(side_length=1.4, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2)
        xlabel = ink_txt("X", size=44).move_to(box)
        left_beam = Arrow(LEFT * 0.3, RIGHT * 2.0 + UP * 1.1, color=SLATE, stroke_width=5,
                          buff=0, max_tip_length_to_length_ratio=0.15)
        right_beam = Arrow(LEFT * 0.3, RIGHT * 2.0 + DOWN * 1.1, color=SLATE, stroke_width=5,
                           buff=0, max_tip_length_to_length_ratio=0.15)
        left_label = ink_txt("left  50%", size=24, color=SLATE).next_to(left_beam.get_end(), RIGHT, buff=0.1)
        right_label = ink_txt("right 50%", size=24, color=INK).next_to(right_beam.get_end(), RIGHT, buff=0.1)
        self.add(box, xlabel)
        self.play(GrowArrow(left_beam), GrowArrow(right_beam),
                  FadeIn(left_label), FadeIn(right_label), run_time=0.9)
        self.wait(dur - 0.9)


class A05_KeepRight(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 4.0)
        box = Square(side_length=1.4, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2)
        xlabel = ink_txt("X", size=44).move_to(box)
        left_beam = Arrow(LEFT * 0.3, RIGHT * 2.0 + UP * 1.1, color=RED, stroke_width=5,
                          buff=0, max_tip_length_to_length_ratio=0.15)
        right_beam = Arrow(LEFT * 0.3, RIGHT * 2.0 + DOWN * 1.1, color=SLATE, stroke_width=5,
                           buff=0, max_tip_length_to_length_ratio=0.15)
        cross = Cross(color=RED, stroke_width=6).scale(0.4).move_to(left_beam.get_end() + RIGHT * 0.4)
        right_label = ink_txt("spin-right only", size=24, color=SLATE).next_to(right_beam.get_end(), RIGHT, buff=0.1)
        self.add(box, xlabel, left_beam, right_beam)
        self.play(FadeIn(cross), FadeIn(right_label), run_time=1.0)
        self.wait(dur - 1.0)


class A06_SpinRightEntersZBox(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 4.41)
        beam_in = Arrow(LEFT * 5, LEFT * 1.8, color=SLATE, stroke_width=5, buff=0,
                        max_tip_length_to_length_ratio=0.15)
        beam_label = ink_txt("spin-right", size=24, color=SLATE).next_to(beam_in, UP, buff=0.1)
        box = Square(side_length=1.4, color=INK, stroke_width=3).set_fill(CREAM, 1).move_to(ORIGIN)
        zlabel = ink_txt("Z", size=44).move_to(box)
        sublabel = ink_txt("up / down\n(again)", size=26).next_to(box, DOWN, buff=0.2)
        self.play(GrowArrow(beam_in), FadeIn(beam_label), run_time=0.9)
        self.play(FadeIn(box), FadeIn(zlabel), run_time=0.6)
        self.play(FadeIn(sublabel), run_time=0.4)
        self.wait(dur - 1.9)


class A07_FiftyFiftyAgain(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 5.51)
        box = Square(side_length=1.4, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 2)
        zlabel = ink_txt("Z", size=44).move_to(box)
        up_beam = Arrow(LEFT * 0.3, RIGHT * 2.5 + UP * 1.2, color=SLATE, stroke_width=5,
                        buff=0, max_tip_length_to_length_ratio=0.15)
        dn_beam = Arrow(LEFT * 0.3, RIGHT * 2.5 + DOWN * 1.2, color=SLATE, stroke_width=5,
                        buff=0, max_tip_length_to_length_ratio=0.15)
        up_label = ink_txt("up   50%", size=24, color=SLATE).next_to(up_beam.get_end(), RIGHT, buff=0.1)
        dn_label = ink_txt("down 50%", size=24, color=INK).next_to(dn_beam.get_end(), RIGHT, buff=0.1)
        again = ink_txt("all over again", size=28, color=RED).shift(RIGHT * 3 + UP * 0.05)
        self.add(box, zlabel)
        self.play(GrowArrow(up_beam), GrowArrow(dn_beam),
                  FadeIn(up_label), FadeIn(dn_label), FadeIn(again), run_time=1.0)
        self.wait(dur - 1.0)


class A08_OverwriteLabel(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 6.11)
        # Final diagram: three boxes in sequence
        z1 = Square(side_length=1.0, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(LEFT * 4)
        x_box = Square(side_length=1.0, color=INK, stroke_width=3).set_fill(CREAM, 1).move_to(ORIGIN)
        z2 = Square(side_length=1.0, color=INK, stroke_width=3).set_fill(CREAM, 1).shift(RIGHT * 4)
        lz1 = ink_txt("Z", size=32).move_to(z1)
        lx = ink_txt("X", size=32).move_to(x_box)
        lz2 = ink_txt("Z", size=32).move_to(z2)
        arr1 = Arrow(LEFT * 3.5, LEFT * 0.5, color=SLATE, stroke_width=4, buff=0,
                     max_tip_length_to_length_ratio=0.2)
        arr2 = Arrow(RIGHT * 0.5, RIGHT * 3.5, color=SLATE, stroke_width=4, buff=0,
                     max_tip_length_to_length_ratio=0.2)
        overwrite = ink_txt("the middle measurement overwrote it", size=28, color=RED)
        overwrite.shift(DOWN * 1.8)
        self.play(FadeIn(VGroup(z1, x_box, z2, lz1, lx, lz2, arr1, arr2)),
                  FadeIn(overwrite), run_time=1.8)
        self.wait(dur - 1.8)
