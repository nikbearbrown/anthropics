import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
RED_COL = "#C0392B"
BLUE_COL = "#2A6FB0"
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


class INTRO_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("INTRO", 3.93)
        series = ink_txt("Bear's Notes", size=40)
        title = ink_txt("Why a Dim Blue Lamp\nBeats a Blinding Red One", size=32)
        title.next_to(series, DOWN, buff=0.5)
        grp = VGroup(series, title).move_to(ORIGIN)
        self.play(FadeIn(series), run_time=dur * 0.4)
        self.play(FadeIn(title), run_time=dur * 0.4)
        self.wait(dur * 0.2)


class H01_BlindingRedLamp(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H01", 5.38)
        # A huge red lamp on the left, a metal plate on the right, nothing happens
        lamp_body = Circle(radius=0.7, color=RED_COL, fill_opacity=0.85)
        lamp_label = ink_txt("RED", size=22, color=RED_COL)
        lamp_label.next_to(lamp_body, DOWN, buff=0.15)
        lamp_grp = VGroup(lamp_body, lamp_label).shift(LEFT * 3.5)

        plate = Rectangle(width=0.6, height=2.5, color=INK, fill_opacity=0.6)
        plate.shift(RIGHT * 2.5)
        plate_label = ink_txt("metal plate", size=20)
        plate_label.next_to(plate, DOWN, buff=0.2)

        # Rays shooting right from lamp
        rays = VGroup(*[
            Line(lamp_body.get_right(), lamp_body.get_right() + RIGHT * 1.5 + UP * (i - 1) * 0.4,
                 color=RED_COL, stroke_width=3)
            for i in range(3)
        ])

        nothing = ink_txt("nothing happens", size=24)
        nothing.shift(DOWN * 2.5)
        cross = Line(nothing.get_left(), nothing.get_right(), color=RED_COL, stroke_width=4)

        self.play(Create(lamp_grp), run_time=dur * 0.25)
        self.play(Create(plate), Write(plate_label), run_time=dur * 0.25)
        self.play(Create(rays), run_time=dur * 0.2)
        self.play(Write(nothing), run_time=dur * 0.15)
        self.play(Create(cross), run_time=dur * 0.1)
        self.wait(dur * 0.05)


class H02_FaintBlueLamp(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("H02", 4.82)
        # Small blue light, electrons flying off
        lamp = Circle(radius=0.35, color=BLUE_COL, fill_opacity=0.8)
        lamp.shift(LEFT * 3.5)
        lamp_label = ink_txt("dim blue", size=20, color=BLUE_COL)
        lamp_label.next_to(lamp, DOWN, buff=0.15)

        plate = Rectangle(width=0.6, height=2.5, color=INK, fill_opacity=0.6)
        plate.shift(RIGHT * 1.0)

        electrons = VGroup(*[
            Dot(radius=0.12, color=TERRA).shift(plate.get_right() + RIGHT * (1.0 + i * 0.7) + UP * (i - 1) * 0.5)
            for i in range(3)
        ])
        e_label = ink_txt("electrons!", size=24, color=TERRA)
        e_label.next_to(electrons, RIGHT, buff=0.2)

        self.play(Create(lamp), Write(lamp_label), run_time=dur * 0.3)
        self.play(Create(plate), run_time=dur * 0.2)
        self.play(LaggedStart(*[FadeIn(e, shift=RIGHT * 0.5) for e in electrons], lag_ratio=0.2),
                  run_time=dur * 0.3)
        self.play(Write(e_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A01_LightPackets(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A01", 4.37)
        # Smooth beam resolving into discrete packets
        beam = Rectangle(width=5, height=0.6, color=BLUE_COL, fill_opacity=0.3, stroke_width=0)
        beam.shift(LEFT * 1.5)

        packets = VGroup(*[
            Circle(radius=0.28, color=BLUE_COL, fill_opacity=0.9).shift(LEFT * 3 + RIGHT * i * 0.9)
            for i in range(7)
        ])

        label = ink_txt("light arrives as packets", size=26)
        label.shift(DOWN * 2.5)

        self.play(FadeIn(beam), run_time=dur * 0.3)
        self.play(ReplacementTransform(beam, packets), run_time=dur * 0.4)
        self.play(Write(label), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A02_RedVsBluePackets(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A02", 5.23)
        # Existing flying packets (simplified), plus energy comparison
        red_pkt = Circle(radius=0.35, color=RED_COL, fill_opacity=0.9)
        red_pkt.shift(LEFT * 2.5 + UP * 0.3)
        red_e = ink_txt("low\nenergy", size=20, color=RED_COL)
        red_e.next_to(red_pkt, DOWN, buff=0.2)

        blue_pkt = Circle(radius=0.55, color=BLUE_COL, fill_opacity=0.9)
        blue_pkt.shift(RIGHT * 2.0 + UP * 0.3)
        blue_e = ink_txt("high\nenergy", size=20, color=BLUE_COL)
        blue_e.next_to(blue_pkt, DOWN, buff=0.2)

        # Energy bars
        bar_red = Rectangle(width=0.4, height=0.8, color=RED_COL, fill_opacity=0.8)
        bar_red.next_to(red_e, DOWN, buff=0.15)
        bar_blue = Rectangle(width=0.4, height=2.0, color=BLUE_COL, fill_opacity=0.8)
        bar_blue.next_to(blue_e, DOWN, buff=0.15)

        e_label = ink_txt("E = hν", size=30)
        e_label.shift(DOWN * 3.0)

        self.play(Create(red_pkt), Write(red_e), run_time=dur * 0.25)
        self.play(Create(blue_pkt), Write(blue_e), run_time=dur * 0.25)
        self.play(Create(bar_red), Create(bar_blue), run_time=dur * 0.25)
        self.play(Write(e_label), run_time=dur * 0.15)
        self.wait(dur * 0.1)


class A03_MetalPlateThreshold(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A03", 4.95)
        plate = Rectangle(width=1.2, height=3.0, color=INK, fill_opacity=0.55)
        plate.shift(RIGHT * 2.0)

        electrons = VGroup(*[
            Dot(radius=0.13, color=TERRA).shift(RIGHT * 2.0 + UP * (i * 0.5 - 0.5))
            for i in range(4)
        ])

        threshold = DashedLine(plate.get_top() + UP * 0.6 + LEFT * 1.5,
                               plate.get_top() + UP * 0.6 + RIGHT * 1.5,
                               color=TERRA, stroke_width=3)
        thresh_label = ink_txt("escape energy threshold", size=20, color=TERRA)
        thresh_label.next_to(threshold, RIGHT, buff=0.15)

        self.play(Create(plate), run_time=dur * 0.25)
        self.play(LaggedStart(*[FadeIn(e) for e in electrons], lag_ratio=0.15), run_time=dur * 0.3)
        self.play(Create(threshold), Write(thresh_label), run_time=dur * 0.3)
        self.wait(dur * 0.15)


class A04_RedPacketBounces(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A04", 4.91)
        plate = Rectangle(width=1.2, height=3.0, color=INK, fill_opacity=0.55).shift(RIGHT * 2.0)
        electrons = VGroup(*[
            Dot(radius=0.13, color=TERRA).shift(RIGHT * 2.0 + UP * (i * 0.5 - 0.5))
            for i in range(4)
        ])
        threshold = DashedLine(plate.get_top() + UP * 0.6 + LEFT * 1.5,
                               plate.get_top() + UP * 0.6 + RIGHT * 1.5,
                               color=TERRA, stroke_width=3)
        self.add(plate, electrons, threshold)

        red_pkt = Circle(radius=0.28, color=RED_COL, fill_opacity=0.9).shift(LEFT * 3.5 + UP * 0.2)
        arrow_in = Arrow(red_pkt.get_right(), plate.get_left() + UP * 0.2, color=RED_COL, buff=0.05)
        arrow_out = Arrow(plate.get_left() + UP * 0.2, red_pkt.get_center() + LEFT * 0.5 + DOWN * 0.8,
                          color=RED_COL, buff=0.05)
        no_label = ink_txt("falls short", size=22, color=RED_COL)
        no_label.shift(DOWN * 2.8)

        self.play(FadeIn(red_pkt), run_time=dur * 0.15)
        self.play(Create(arrow_in), run_time=dur * 0.25)
        self.play(Wiggle(electrons[1]), Create(arrow_out), run_time=dur * 0.3)
        self.play(Write(no_label), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A05_ManyRedPackets(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A05", 4.65)
        plate = Rectangle(width=1.2, height=3.0, color=INK, fill_opacity=0.55).shift(RIGHT * 2.0)
        electrons = VGroup(*[
            Dot(radius=0.13, color=TERRA).shift(RIGHT * 2.0 + UP * (i * 0.5 - 0.5))
            for i in range(4)
        ])
        threshold = DashedLine(plate.get_top() + UP * 0.6 + LEFT * 1.5,
                               plate.get_top() + UP * 0.6 + RIGHT * 1.5,
                               color=TERRA, stroke_width=3)
        self.add(plate, electrons, threshold)

        # Storm of red packets
        red_storm = VGroup(*[
            Circle(radius=0.18, color=RED_COL, fill_opacity=0.85).shift(
                LEFT * (2.5 + (i % 4) * 0.6) + UP * ((i // 4) * 0.7 - 1.5)
            )
            for i in range(12)
        ])
        result = ink_txt("0 electrons freed", size=28, color=RED_COL)
        result.shift(DOWN * 3.2)

        self.play(LaggedStart(*[FadeIn(p) for p in red_storm], lag_ratio=0.05),
                  run_time=dur * 0.4)
        self.play(Wiggle(electrons), run_time=dur * 0.3)
        self.play(Write(result), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A06_OneBluePacket(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A06", 5.03)
        plate = Rectangle(width=1.2, height=3.0, color=INK, fill_opacity=0.55).shift(RIGHT * 2.0)
        electrons = VGroup(*[
            Dot(radius=0.13, color=TERRA).shift(RIGHT * 2.0 + UP * (i * 0.5 - 0.5))
            for i in range(4)
        ])
        threshold = DashedLine(plate.get_top() + UP * 0.6 + LEFT * 1.5,
                               plate.get_top() + UP * 0.6 + RIGHT * 1.5,
                               color=TERRA, stroke_width=3)
        self.add(plate, electrons, threshold)

        blue_pkt = Circle(radius=0.35, color=BLUE_COL, fill_opacity=0.9).shift(LEFT * 3.5 + UP * 0.5)
        arrow_in = Arrow(blue_pkt.get_right(), plate.get_left() + UP * 0.5, color=BLUE_COL, buff=0.05)

        freed = Dot(radius=0.18, color=TERRA).shift(RIGHT * 3.5 + UP * 2.5)
        arrow_free = Arrow(plate.get_top() + LEFT * 0.1, freed.get_center(), color=INK, buff=0.05)
        freed_label = ink_txt("freed!", size=26)
        freed_label.next_to(freed, RIGHT, buff=0.15)

        self.play(FadeIn(blue_pkt), run_time=dur * 0.15)
        self.play(Create(arrow_in), run_time=dur * 0.25)
        self.play(Create(arrow_free), FadeIn(freed), run_time=dur * 0.3)
        self.play(Write(freed_label), run_time=dur * 0.2)
        self.wait(dur * 0.1)


class A07_BrightnessTally(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A07", 5.25)
        # Left: many red = 0 freed; Right: one blue = 1 freed
        red_crowd = VGroup(*[
            Circle(radius=0.16, color=RED_COL, fill_opacity=0.9).shift(
                LEFT * 3.5 + RIGHT * (i % 4) * 0.45 + UP * (i // 4) * 0.45 - UP * 0.4
            )
            for i in range(8)
        ])
        red_count = ink_txt("0 freed", size=28, color=RED_COL)
        red_count.shift(LEFT * 2.5 + DOWN * 1.5)

        blue_one = Circle(radius=0.35, color=BLUE_COL, fill_opacity=0.9).shift(RIGHT * 1.5 + UP * 0.2)
        blue_count = ink_txt("1 freed", size=28, color=BLUE_COL)
        blue_count.shift(RIGHT * 1.5 + DOWN * 1.5)

        vs = ink_txt("vs", size=32)
        vs.move_to(ORIGIN + DOWN * 0.5)

        label = ink_txt("colour decides, not brightness", size=24)
        label.shift(DOWN * 3.0)

        self.play(LaggedStart(*[FadeIn(p) for p in red_crowd], lag_ratio=0.06),
                  run_time=dur * 0.25)
        self.play(Write(red_count), run_time=dur * 0.15)
        self.play(Write(vs), run_time=dur * 0.1)
        self.play(FadeIn(blue_one), run_time=dur * 0.15)
        self.play(Write(blue_count), run_time=dur * 0.15)
        self.play(Write(label), run_time=dur * 0.15)
        self.wait(dur * 0.05)


class A08_PhotonHighlight(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        dur = d("A08", 4.69)
        # One blue photon highlighted; freed electron
        photon = Circle(radius=0.45, color=BLUE_COL, fill_opacity=0.9).shift(LEFT * 2.0 + UP * 0.5)
        photon_label = ink_txt("photon", size=24, color=BLUE_COL)
        photon_label.next_to(photon, DOWN, buff=0.2)
        e_eq = ink_txt("E = hν", size=28, color=BLUE_COL)
        e_eq.next_to(photon_label, DOWN, buff=0.2)

        arrow = Arrow(photon.get_right(), RIGHT * 0.5 + UP * 0.5, color=BLUE_COL, buff=0.05)

        freed = Dot(radius=0.22, color=TERRA).shift(RIGHT * 2.0 + UP * 1.5)
        freed_trail = Line(freed.get_center() + LEFT * 0.1 + DOWN * 0.1,
                           freed.get_center() + RIGHT * 0.8 + UP * 0.6,
                           color=TERRA, stroke_width=4)
        freed_label = ink_txt("electron free", size=24, color=TERRA)
        freed_label.next_to(freed, RIGHT, buff=0.2)

        self.play(FadeIn(photon), Write(photon_label), run_time=dur * 0.3)
        self.play(Write(e_eq), run_time=dur * 0.2)
        self.play(Create(arrow), FadeIn(freed), Create(freed_trail), run_time=dur * 0.3)
        self.play(Write(freed_label), run_time=dur * 0.15)
        self.wait(dur * 0.05)
