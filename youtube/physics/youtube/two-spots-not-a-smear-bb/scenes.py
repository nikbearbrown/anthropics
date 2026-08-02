import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

DARK_BG = "#1a1a1a"
BLUE = "#58C4DD"
BROWN = "#CD853F"
HIGHLIGHT = "#F0E442"

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
    return Rectangle(width=16, height=9).set_fill(DARK_BG, 1).set_stroke(width=0)

# Estimate durations for this previz-only beat sheet
_DEFAULT_DURS = {
    "INTRO": 3.5, "H01": 5.5, "H02": 5.0, "H03": 4.5, "H04": 3.5,
    "W01": 5.0, "W02": 5.0, "W03": 5.0, "W04": 5.0, "W05": 4.5,
    "S01": 4.0, "S02": 4.5, "S03": 4.0, "S04": 4.0, "S05": 4.5,
    "S06": 4.0, "S07": 3.5, "S08": 5.0, "S09": 4.0,
    "P01": 4.5, "P02": 5.0, "P03": 6.0, "OUTRO": 4.0
}

def dur(bid):
    v = DUR.get(bid)
    if v: return v
    return _DEFAULT_DURS.get(bid, 5.0)


def make_sg_apparatus():
    """Stern-Gerlach: oven, beam arrow, magnet wedge, plate."""
    oven = Rectangle(width=0.8, height=1.0, color="#888888", fill_opacity=0.8).move_to(LEFT * 5.5)
    oven_lbl = Text("oven", font=FONT, font_size=18, color="#888888").next_to(oven, DOWN, buff=0.15)

    # Asymmetric magnet: wedge pair
    mag_top = Polygon([-0.6, 0.4, 0], [-0.6, 2.0, 0], [0.6, 0.8, 0], [0.6, 0.4, 0],
                      color="#888888", fill_opacity=0.7).move_to(ORIGIN + UP * 0.9)
    mag_bot = Polygon([-0.6, -0.4, 0], [-0.6, -2.0, 0], [0.6, -0.8, 0], [0.6, -0.4, 0],
                      color="#888888", fill_opacity=0.7).move_to(ORIGIN + DOWN * 0.9)

    plate = Rectangle(width=0.15, height=4.5, color="#E0DDD5", fill_opacity=0.8).move_to(RIGHT * 4.5)

    return VGroup(oven, oven_lbl), VGroup(mag_top, mag_bot), plate


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("INTRO")
        series = Text("Bear's Notes", font=FONT, font_size=28, color=BROWN).move_to(UP * 1.2)
        title = Text("Two Spots, Not a Smear", font=FONT, font_size=52, color="#E0DDD5").move_to(DOWN * 0.2)
        rule = Line(LEFT * 4, RIGHT * 4, color=BROWN, stroke_width=1.5).move_to(DOWN * 0.9)
        tick = Dot(color=BLUE, radius=0.06).move_to(RIGHT * 4.2 + DOWN * 0.9)
        self.play(FadeIn(series), Write(title), run_time=1.0)
        self.play(Create(rule), FadeIn(tick), run_time=0.6)
        self.wait(d_dur - 1.6)


class H01_Apparatus(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("H01")
        oven_g, magnets, plate = make_sg_apparatus()
        self.play(Create(oven_g), run_time=0.5)
        # Beam of silver dots
        beam_dots = VGroup(*[
            Dot(color="#C0C0C0", radius=0.1).move_to(LEFT * 5.5 + RIGHT * i * 0.5)
            for i in range(1, 5)])
        self.play(Create(magnets), Create(plate), run_time=0.5)
        self.play(LaggedStart(*[dot.animate.move_to(dot.get_center() + RIGHT * 5) for dot in beam_dots],
                              lag_ratio=0.15), run_time=1.5)
        self.wait(d_dur - 2.5)


class H02_OrientationFan(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("H02")
        oven_g, magnets, plate = make_sg_apparatus()
        self.add(oven_g, magnets, plate)

        # Inset: atom dot with fan of compass needles
        atom = Dot(color="#C0C0C0", radius=0.25).move_to(LEFT * 3 + DOWN * 0.5)
        needles = VGroup(*[
            Arrow(atom.get_center(), atom.get_center() + 0.5 * np.array([np.cos(a), np.sin(a), 0]),
                  color=BLUE, buff=0, stroke_width=2, stroke_opacity=0.5, max_tip_length_to_length_ratio=0.3)
            for a in np.linspace(0, TAU, 12, endpoint=False)])

        self.play(GrowFromCenter(atom), run_time=0.4)
        self.play(Create(needles), run_time=0.8)
        self.wait(d_dur - 1.2)


class H03_ClassicalStreak(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("H03")
        oven_g, magnets, plate = make_sg_apparatus()
        self.add(oven_g, magnets, plate)

        # Ghost streak on plate
        streak = Rectangle(width=0.2, height=3.5, fill_opacity=0.3, stroke_width=0)
        streak.set_fill(color=["#C0C0C0", "#404040"], opacity=0.4)
        streak.move_to(RIGHT * 4.5)
        streak_lbl = Text("predicted", font=FONT, font_size=20, color="#888888").next_to(plate, RIGHT, buff=0.3)

        self.play(FadeIn(streak), Write(streak_lbl), run_time=0.8)

        # Fan of beam dots
        beam = VGroup(*[
            Arrow(LEFT * 5.5, RIGHT * 4.5 + UP * (y), color="#C0C0C0", buff=0,
                  stroke_width=1, stroke_opacity=0.3, max_tip_length_to_length_ratio=0.05)
            for y in np.linspace(-1.5, 1.5, 8)])
        self.play(Create(beam), run_time=0.8)
        self.wait(d_dur - 1.6)


class H04_TwoSpotsReveal(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("H04")
        oven_g, magnets, plate = make_sg_apparatus()
        self.add(oven_g, magnets, plate)

        # Ghost streak
        streak = Rectangle(width=0.2, height=3.5, fill_opacity=0.3, stroke_width=0)
        streak.move_to(RIGHT * 4.5)
        self.add(streak)

        # Reveal: streak dissolves, two sharp spots appear
        spot_up = Dot(color=BLUE, radius=0.18).move_to(RIGHT * 4.5 + UP * 1.2)
        spot_dn = Dot(color=BLUE, radius=0.18).move_to(RIGHT * 4.5 + DOWN * 1.2)

        self.play(FadeOut(streak), run_time=0.5)
        self.play(GrowFromCenter(spot_up), GrowFromCenter(spot_dn), run_time=0.8)
        self.wait(d_dur - 1.3)


class H05_TwoSpotsHold(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("H05")
        oven_g, magnets, plate = make_sg_apparatus()
        for obj in (oven_g, magnets, plate):
            obj.set_opacity(0.4)
        self.add(oven_g, magnets, plate)

        spot_up = Dot(color=BLUE, radius=0.2).move_to(RIGHT * 4.5 + UP * 1.2)
        spot_dn = Dot(color=BLUE, radius=0.2).move_to(RIGHT * 4.5 + DOWN * 1.2)
        self.add(spot_up, spot_dn)
        self.wait(d_dur)


class W01_TiltAndPush(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("W01")

        atom = Dot(color="#C0C0C0", radius=0.25).move_to(ORIGIN)
        t = ValueTracker(PI / 4)

        needle = always_redraw(lambda: Arrow(
            atom.get_center(),
            atom.get_center() + 0.8 * np.array([np.cos(t.get_value()), np.sin(t.get_value()), 0]),
            color=BLUE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25))

        push_arrow = always_redraw(lambda: Arrow(
            atom.get_center() + RIGHT * 0.5,
            atom.get_center() + RIGHT * 0.5 + UP * np.sin(t.get_value()) * 1.5,
            color=HIGHLIGHT, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.2))

        self.add(atom, needle, push_arrow)
        self.play(t.animate.set_value(PI / 6), run_time=0.8)
        self.play(t.animate.set_value(PI * 2 / 3), run_time=0.8)
        self.play(t.animate.set_value(PI / 4), run_time=0.5)
        self.wait(d_dur - 2.1)


class W02_ContinuousStreak(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("W02")

        atom = Dot(color="#C0C0C0", radius=0.25).move_to(LEFT * 2)
        self.add(atom)

        # Column of graded push arrows → streak
        push_arrows = VGroup(*[
            Arrow(LEFT * 1.3, LEFT * 1.3 + UP * y * 0.5,
                  color="#888888", buff=0, stroke_width=1.5, stroke_opacity=0.5,
                  max_tip_length_to_length_ratio=0.2)
            for y in np.linspace(-3, 3, 14)])

        streak = Rectangle(width=0.2, height=3.5, fill_opacity=0.25, stroke_width=0)
        streak.move_to(RIGHT * 4.5)

        self.play(LaggedStart(*[FadeIn(a) for a in push_arrows], lag_ratio=0.05), run_time=1.0)
        self.play(FadeIn(streak), run_time=0.6)
        self.wait(d_dur - 1.6)


class W03_TwoAllowedTilts(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("W03")

        atom = Dot(color="#C0C0C0", radius=0.25).move_to(LEFT * 2)
        self.add(atom)

        # Full fan collapses to up/down
        full_fan = VGroup(*[
            Arrow(atom.get_center(), atom.get_center() + 0.6 * np.array([np.cos(a), np.sin(a), 0]),
                  color="#888888", buff=0, stroke_width=1, stroke_opacity=0.3,
                  max_tip_length_to_length_ratio=0.2)
            for a in np.linspace(0, TAU, 12, endpoint=False)])

        up_arrow = Arrow(atom.get_center(), atom.get_center() + UP * 0.8,
                         color=BLUE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        dn_arrow = Arrow(atom.get_center(), atom.get_center() + DOWN * 0.8,
                         color=BLUE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.25)

        spot_up = Dot(color=BLUE, radius=0.18).move_to(RIGHT * 4.5 + UP * 1.2)
        spot_dn = Dot(color=BLUE, radius=0.18).move_to(RIGHT * 4.5 + DOWN * 1.2)
        self.add(spot_up, spot_dn)

        self.play(Create(full_fan), run_time=0.6)
        self.play(
            *[arrow.animate.set_opacity(0.05) for arrow in full_fan
              if abs(arrow.get_angle() - PI/2) > 0.3 and abs(arrow.get_angle() + PI/2) > 0.3],
            FadeIn(up_arrow), FadeIn(dn_arrow),
            run_time=1.0)
        self.wait(d_dur - 1.6)


class W04_TwoAnswerCard(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("W04")

        question = Text("spin along this axis?", font=FONT, font_size=28, color="#E0DDD5").move_to(UP * 1.5)
        box_up = Square(side_length=0.5, color=BLUE, fill_opacity=0.8).move_to(LEFT * 1 + DOWN * 0.2)
        box_dn = Square(side_length=0.5, color=BLUE, fill_opacity=0.8).move_to(RIGHT * 1 + DOWN * 0.2)
        lbl_up = Text("↑", font=FONT, font_size=28, color="#E0DDD5").move_to(box_up)
        lbl_dn = Text("↓", font=FONT, font_size=28, color="#E0DDD5").move_to(box_dn)
        ghost_box = Square(side_length=0.5, color="#888888", fill_opacity=0.2, stroke_opacity=0.4).move_to(RIGHT * 3 + DOWN * 0.2)
        ghost_x = Cross(ghost_box, color="#888888", stroke_width=2)

        self.play(Write(question), run_time=0.6)
        self.play(GrowFromCenter(box_up), GrowFromCenter(box_dn), FadeIn(lbl_up), FadeIn(lbl_dn), run_time=0.6)
        self.play(FadeIn(ghost_box), Create(ghost_x), run_time=0.5)
        self.wait(d_dur - 1.7)


class W05_BornRuleHold(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("W05")

        box_up = Square(side_length=0.8, color=BLUE, fill_opacity=0.6).move_to(LEFT * 1.2 + UP * 0.2)
        box_dn = Square(side_length=0.8, color=BLUE, fill_opacity=0.6).move_to(RIGHT * 1.2 + UP * 0.2)
        lbl_up = Text("↑", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box_up)
        lbl_dn = Text("↓", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box_dn)
        born_lbl = Text("Born rule", font=FONT, font_size=24, color=HIGHLIGHT).move_to(DOWN * 0.8)

        sweep = Line(LEFT * 2.2, RIGHT * 2.2, color=HIGHLIGHT, stroke_width=3)
        sweep.move_to(LEFT * 7 + UP * 0.2)  # start off-screen left

        self.add(box_up, box_dn, lbl_up, lbl_dn, born_lbl)
        self.play(sweep.animate.shift(RIGHT * 9.4), run_time=0.8)
        self.wait(d_dur - 0.8)


class S01_TwoBoxesInSeries(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S01")

        # Two Z boxes in series
        box1 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(LEFT * 2.5)
        lbl1 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box1)
        box2 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(RIGHT * 2.5)
        lbl2 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box2)
        beam_line = Arrow(LEFT * 5.5, RIGHT * 5.5, color="#C0C0C0", buff=0, stroke_width=2,
                          max_tip_length_to_length_ratio=0.05)

        self.play(Create(beam_line), run_time=0.4)
        self.play(GrowFromCenter(box1), FadeIn(lbl1), run_time=0.4)
        self.play(GrowFromCenter(box2), FadeIn(lbl2), run_time=0.4)
        self.wait(d_dur - 1.2)


class S02_SelectUpBeam(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S02")

        box1 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(LEFT * 2.5)
        lbl1 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box1)
        box2 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(RIGHT * 2.5)
        lbl2 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box2)
        self.add(box1, lbl1, box2, lbl2)

        # Beam exits box1: up and down beams; stopper blocks down
        up_beam = Arrow(LEFT * 1.9 + UP * 0.4, RIGHT * 1.9 + UP * 0.4,
                        color=BLUE, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.08)
        dn_beam = Arrow(LEFT * 1.9 + DOWN * 0.4, RIGHT * 0.5 + DOWN * 0.4,
                        color="#888888", buff=0, stroke_width=1.5, stroke_opacity=0.4,
                        max_tip_length_to_length_ratio=0.08)
        stopper = Rectangle(width=0.2, height=0.5, color="#C8102E", fill_opacity=0.9)
        stopper.move_to(RIGHT * 0.5 + DOWN * 0.4)

        self.play(Create(up_beam), Create(dn_beam), run_time=0.5)
        self.play(FadeIn(stopper), run_time=0.4)
        self.wait(d_dur - 0.9)


class S03_CertaintyUp(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S03")

        box1 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(LEFT * 2.5)
        lbl1 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box1)
        box2 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(RIGHT * 2.5)
        lbl2 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box2)
        up_beam = Arrow(LEFT * 1.9 + UP * 0.4, RIGHT * 1.9 + UP * 0.4,
                        color=BLUE, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.08)
        self.add(box1, lbl1, box2, lbl2, up_beam)

        # Box2 output: one full beam (up only), 100%
        out_beam = Arrow(RIGHT * 3.1 + UP * 0.4, RIGHT * 5 + UP * 0.4,
                         color=BLUE, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.08)
        pct_lbl = Text("100%", font=FONT, font_size=22, color=BLUE).move_to(RIGHT * 4 + UP * 0.9)

        self.play(Create(out_beam), Write(pct_lbl), run_time=0.6)
        self.wait(d_dur - 0.6)


class S04_SwitchToX(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S04")

        box1 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(LEFT * 2.5)
        lbl1 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box1)
        up_beam = Arrow(LEFT * 1.9 + UP * 0.4, RIGHT * 1.9 + UP * 0.4,
                        color=BLUE, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.08)
        self.add(box1, lbl1, up_beam)

        box2 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(RIGHT * 2.5)
        lbl2_z = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box2)
        lbl2_x = Text("X", font=FONT, font_size=36, color=BLUE).move_to(box2)
        self.add(box2, lbl2_z)

        self.play(Transform(lbl2_z, lbl2_x),
                  box2.animate.rotate(PI/2),
                  run_time=0.8)
        self.wait(d_dur - 0.8)


class S05_FiftyCoinFlip(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S05")

        box1 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(LEFT * 2.5)
        lbl1 = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box1)
        box2 = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(RIGHT * 2.5)
        lbl2 = Text("X", font=FONT, font_size=36, color=BLUE).move_to(box2)
        up_in = Arrow(LEFT * 1.9 + UP * 0.4, RIGHT * 1.9 + UP * 0.4,
                      color=BLUE, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.08)
        self.add(box1, lbl1, box2, lbl2, up_in)

        # Two equal output beams
        out_up = Arrow(RIGHT * 3.1 + UP * 0.5, RIGHT * 5 + UP * 1.0,
                       color=BLUE, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.08)
        out_dn = Arrow(RIGHT * 3.1 + UP * 0.4, RIGHT * 5 + DOWN * 0.2,
                       color=BLUE, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.08)
        pct_up = Text("50%", font=FONT, font_size=20, color=BLUE).move_to(RIGHT * 4.3 + UP * 1.2)
        pct_dn = Text("50%", font=FONT, font_size=20, color=BLUE).move_to(RIGHT * 4.3 + DOWN * 0.4)

        self.play(Create(out_up), Create(out_dn), run_time=0.5)
        self.play(Write(pct_up), Write(pct_dn), run_time=0.4)
        self.wait(d_dur - 0.9)


class S06_CertainUncertain(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S06")

        box_z = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(LEFT * 2.5)
        lbl_z = Text("Z", font=FONT, font_size=36, color=HIGHLIGHT).move_to(box_z)
        box_x = Square(side_length=1.2, color="#888888", fill_opacity=0.6).move_to(RIGHT * 2.5)
        lbl_x = Text("X", font=FONT, font_size=36, color=BLUE).move_to(box_x)

        arrow = Arrow(LEFT * 1.9, RIGHT * 1.9, color="#888888", buff=0, stroke_width=2,
                      max_tip_length_to_length_ratio=0.08)

        pct_z = Text("100%", font=FONT, font_size=24, color=HIGHLIGHT).move_to(LEFT * 2.5 + UP * 1.0)
        pct_x = Text("50 / 50", font=FONT, font_size=24, color=BLUE).move_to(RIGHT * 2.5 + UP * 1.0)

        self.add(box_z, lbl_z, box_x, lbl_x, arrow, pct_z, pct_x)

        self.play(Indicate(pct_z, scale_factor=1.3, color=HIGHLIGHT), run_time=0.5)
        self.play(Indicate(pct_x, scale_factor=1.3, color=BLUE), run_time=0.5)
        self.wait(d_dur - 1.0)


class S07_ChainExtendedZXZ(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S07")

        # Z → X → Z chain
        box1 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(LEFT * 3.5)
        lbl1 = Text("Z", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box1)
        box2 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(ORIGIN)
        lbl2 = Text("X", font=FONT, font_size=28, color=BLUE).move_to(box2)
        box3 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(RIGHT * 3.5)
        lbl3 = Text("Z", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box3)

        beam_line = Line(LEFT * 6 + UP * 0.3, RIGHT * 4 + UP * 0.3,
                         color="#C0C0C0", stroke_width=1.5, stroke_opacity=0.5)

        self.play(Create(beam_line), run_time=0.3)
        self.play(GrowFromCenter(box1), FadeIn(lbl1), run_time=0.3)
        self.play(GrowFromCenter(box2), FadeIn(lbl2), run_time=0.3)
        self.play(GrowFromCenter(box3), FadeIn(lbl3), run_time=0.3)
        self.wait(d_dur - 1.2)


class S08_XErasesZ(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S08")

        box1 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(LEFT * 3.5)
        lbl1 = Text("Z", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box1)
        box2 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(ORIGIN)
        lbl2 = Text("X", font=FONT, font_size=28, color=BLUE).move_to(box2)
        box3 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(RIGHT * 3.5)
        lbl3 = Text("Z", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box3)
        old_pct = Text("100%", font=FONT, font_size=20, color=BLUE).move_to(LEFT * 2.5 + UP * 0.8)
        self.add(box1, lbl1, box2, lbl2, box3, lbl3, old_pct)

        # Final Z splits 50/50; old 100% tag cracks
        out_up = Arrow(RIGHT * 4.0 + UP * 0.3, RIGHT * 5.5 + UP * 0.8,
                       color=BLUE, buff=0, stroke_width=1.8, max_tip_length_to_length_ratio=0.1)
        out_dn = Arrow(RIGHT * 4.0 + UP * 0.3, RIGHT * 5.5 + DOWN * 0.2,
                       color=BLUE, buff=0, stroke_width=1.8, max_tip_length_to_length_ratio=0.1)
        new_pct_up = Text("50%", font=FONT, font_size=18, color=BLUE).move_to(RIGHT * 5 + UP * 1.0)
        new_pct_dn = Text("50%", font=FONT, font_size=18, color=BLUE).move_to(RIGHT * 5 + DOWN * 0.4)

        self.play(Create(out_up), Create(out_dn), run_time=0.5)
        self.play(Write(new_pct_up), Write(new_pct_dn), run_time=0.4)
        self.play(old_pct.animate.set_opacity(0.15), run_time=0.6)
        self.wait(d_dur - 1.5)


class S09_MeasurementChain(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("S09")

        box_z1 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(LEFT * 3.5)
        lbl_z1 = Text("Z", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box_z1)
        box_x = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(ORIGIN)
        lbl_x = Text("X", font=FONT, font_size=28, color=BLUE).move_to(box_x)
        box_z2 = Square(side_length=0.9, color="#888888", fill_opacity=0.6).move_to(RIGHT * 3.5)
        lbl_z2 = Text("Z", font=FONT, font_size=28, color=HIGHLIGHT).move_to(box_z2)

        arr1 = Arrow(LEFT * 3.05, LEFT * 0.45, color="#888888", buff=0, stroke_width=1.5,
                     max_tip_length_to_length_ratio=0.08)
        arr2 = Arrow(RIGHT * 0.45, RIGHT * 3.05, color="#888888", buff=0, stroke_width=1.5,
                     max_tip_length_to_length_ratio=0.08)

        self.add(box_z1, lbl_z1, box_x, lbl_x, box_z2, lbl_z2, arr1, arr2)
        self.play(Indicate(box_x, scale_factor=1.4, color=BLUE), run_time=1.5)
        self.wait(d_dur - 1.5)


class P01_ClumsyAppStruckOut(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("P01")

        card = Text("the apparatus disturbed it", font=FONT, font_size=32, color="#E0DDD5").move_to(ORIGIN)
        self.play(Write(card), run_time=0.6)
        strike = Line(card.get_left() + LEFT * 0.3, card.get_right() + RIGHT * 0.3,
                      color="#C8102E", stroke_width=4)
        self.play(Create(strike), run_time=0.6)
        self.wait(d_dur - 1.2)


class P02_IncompatibilityCard(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("P02")

        card_struck = Text("the apparatus disturbed it", font=FONT, font_size=24, color="#E0DDD5",
                           fill_opacity=0.3).move_to(UP * 2)
        self.add(card_struck)

        def_card = Text("z-spin and x-spin: never both definite",
                        font=FONT, font_size=26, color="#E0DDD5").move_to(UP * 0.5)
        incompat = Text("incompatible", font=FONT, font_size=32, color=HIGHLIGHT).move_to(DOWN * 0.5)

        self.play(Write(def_card), run_time=0.8)
        self.play(Write(incompat), run_time=0.5)
        self.wait(d_dur - 1.3)


class P03_SpotsReturn(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("P03")

        def_card = Text("z-spin and x-spin: never both definite",
                        font=FONT, font_size=26, color="#E0DDD5").move_to(UP * 0.8)
        incompat = Text("incompatible", font=FONT, font_size=30, color=HIGHLIGHT).move_to(DOWN * 0.1)
        self.add(def_card, incompat)

        # Two spots return as evidence
        spot_up = Dot(color="#C0C0C0", radius=0.2).move_to(DOWN * 1.8 + LEFT * 0.5)
        spot_dn = Dot(color="#C0C0C0", radius=0.2).move_to(DOWN * 1.8 + RIGHT * 0.5)

        self.play(FadeIn(spot_up), FadeIn(spot_dn), run_time=0.5)
        sweep = Line(spot_up.get_center(), spot_dn.get_center(), color=HIGHLIGHT, stroke_width=2)
        self.play(Create(sweep), run_time=0.5)
        self.play(FadeOut(sweep), run_time=0.4)
        self.wait(d_dur - 1.4)


class OUTRO_Final(Scene):
    def construct(self):
        self.add(bg())
        d_dur = dur("OUTRO")

        series = Text("Bear's Notes", font=FONT, font_size=32, color=BROWN).move_to(UP * 1.0)
        rule = Line(LEFT * 3, RIGHT * 3, color=BROWN, stroke_width=1.5).move_to(UP * 0.2)
        tick = Dot(color=BLUE, radius=0.06).move_to(RIGHT * 3.2 + UP * 0.2)
        thanks = Text("thanks for watching", font=FONT, font_size=28, color="#E0DDD5").move_to(DOWN * 0.8)

        self.play(Write(series), Create(rule), FadeIn(tick), Write(thanks), run_time=1.0)
        self.wait(d_dur - 1.0)
