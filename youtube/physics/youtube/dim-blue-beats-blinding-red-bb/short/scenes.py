import json
import numpy as np
from pathlib import Path
from manim import *

# ── palette (3b1b dark, Bear's palette-note: red literal for this video) ──────
CANVAS   = "#1C1C1C"   # 3b1b dark background
BLUE     = "#58C4DD"   # accent / high-frequency
BROWN    = "#CD853F"   # warm / red light (Bear's palette note: read as red)
RED_WARM = "#FC6255"   # the literal 3b1b-red used for red photons (palette note)
YELLOW   = "#F0E442"   # highlight
INK      = "#EEEEEE"   # text / labels (near-white on dark)
DIM      = "#888888"   # secondary / dimmed
FONT     = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs  = json.loads((HERE / "beat_sheet.json").read_text())
    DUR  = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 5)
            for b in _bs.get("beats", [])}
    TITLE = _bs["metadata"].get("title", "")
except Exception:
    DUR = {}; TITLE = ""

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CANVAS, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def blue_txt(t, size=36, color=BLUE, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def warm_txt(t, size=36, color=RED_WARM, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def dim_txt(t, size=28, color=DIM, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

# ── INTRO ─────────────────────────────────────────────────────────────────────
class INTRO(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("INTRO")

        series = ink_txt("Bear's Notes", size=28).move_to(UP * 2.8)
        rule   = Line(LEFT * 3.5, RIGHT * 3.5, stroke_width=1.2, color=BROWN).next_to(series, DOWN, buff=0.18)
        title  = ink_txt("Why a Dim Blue Lamp", size=46, weight=BOLD).next_to(rule, DOWN, buff=0.32)
        title2 = ink_txt("Beats a Blinding Red One", size=46, weight=BOLD).next_to(title, DOWN, buff=0.08)
        tick   = Dot(radius=0.08, color=BLUE).next_to(rule, RIGHT, buff=0.12).align_to(rule, DOWN)

        self.play(FadeIn(series, shift=UP * 0.2), run_time=0.5)
        self.play(Create(rule), FadeIn(tick), run_time=0.4)
        self.play(Write(title), Write(title2), run_time=0.9)
        self.wait(dur - 1.8)

# ── H01 — red lamp, nothing ───────────────────────────────────────────────────
class H01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H01")

        # metal plate
        plate = Rectangle(width=0.5, height=2.8, color=BROWN, fill_color=BROWN, fill_opacity=0.8)
        plate.move_to(RIGHT * 2)

        # electrons on plate
        e_positions = [plate.get_left() + LEFT * 0.25 + UP * v for v in np.linspace(-1.0, 1.0, 5)]
        electrons   = VGroup(*[Dot(radius=0.12, color=BLUE).move_to(p) for p in e_positions])

        # warm lamp shape (circle + glow)
        lamp_body = Circle(radius=0.35, color=RED_WARM, fill_color=RED_WARM, fill_opacity=0.9)
        lamp_body.move_to(LEFT * 4)
        lamp_glow = Circle(radius=0.55, color=RED_WARM, fill_opacity=0).set_stroke(RED_WARM, 1.5, opacity=0.35)
        lamp_glow.move_to(lamp_body.get_center())
        lamp_label = warm_txt("red", size=26).next_to(lamp_body, DOWN, buff=0.2)

        # long wavelength sinusoidal wave (animated)
        def make_long_wave():
            wave_pts = [lamp_body.get_right() + RIGHT * (0.1 + 0.15 * i) +
                        UP * 0.25 * np.sin(2 * PI / 1.4 * (0.15 * i))
                        for i in range(28)]
            return VMobject(color=RED_WARM, stroke_width=2, stroke_opacity=0.7).set_points_smoothly(wave_pts)

        wave = make_long_wave()

        # label: 0 escaping
        nothing_label = ink_txt("electrons: still", size=24).to_corner(DL, buff=0.4)

        self.play(FadeIn(plate), FadeIn(electrons), run_time=0.5)
        self.play(GrowFromCenter(lamp_body), FadeIn(lamp_glow), FadeIn(lamp_label), run_time=0.4)
        self.play(Create(wave), run_time=0.7)
        self.play(FadeIn(nothing_label), run_time=0.3)
        self.wait(dur - 1.9)

# ── H02 — dim blue, electrons fly ─────────────────────────────────────────────
class H02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H02")

        # rebuild plate + electrons
        plate = Rectangle(width=0.5, height=2.8, color=BROWN, fill_color=BROWN, fill_opacity=0.8).move_to(RIGHT * 2)
        electrons = VGroup(*[
            Dot(radius=0.12, color=BLUE).move_to(plate.get_left() + LEFT * 0.25 + UP * v)
            for v in np.linspace(-1.0, 1.0, 5)
        ])

        # small dim blue lamp (smaller than warm)
        lamp_body = Circle(radius=0.22, color=BLUE, fill_color=BLUE, fill_opacity=0.75)
        lamp_body.move_to(LEFT * 4)
        lamp_label = blue_txt("blue", size=26).next_to(lamp_body, DOWN, buff=0.18)

        # short-wavelength wave
        wave_pts = [lamp_body.get_right() + RIGHT * (0.1 + 0.12 * i) +
                    UP * 0.22 * np.sin(2 * PI / 0.6 * (0.12 * i))
                    for i in range(30)]
        wave = VMobject(color=BLUE, stroke_width=2).set_points_smoothly(wave_pts)

        self.add(plate, electrons)
        self.play(
            Transform(
                Circle(radius=0.35, color=RED_WARM, fill_color=RED_WARM, fill_opacity=0.9).move_to(LEFT * 4),
                lamp_body
            ),
            run_time=0.5
        )
        self.add(lamp_body, lamp_label)
        self.play(Create(wave), run_time=0.4)

        # two electrons fly off
        fly_targets = [
            plate.get_left() + LEFT * 2.5 + UP * 0.6,
            plate.get_left() + LEFT * 2.0 + DOWN * 0.5,
        ]
        fly_anims = []
        for i, target in enumerate(fly_targets):
            e = electrons[i + 1]
            arc = ArcBetweenPoints(e.get_center(), target, angle=PI / 4)
            fly_anims.append(MoveAlongPath(e, arc))

        self.play(*fly_anims, run_time=0.9)
        self.wait(dur - 1.8)

# ── H03 — blinding red, still nothing ─────────────────────────────────────────
class H03(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H03")

        plate = Rectangle(width=0.5, height=2.8, color=BROWN, fill_color=BROWN, fill_opacity=0.8).move_to(RIGHT * 2)
        electrons = VGroup(*[
            Dot(radius=0.12, color=BLUE).move_to(plate.get_left() + LEFT * 0.25 + UP * v)
            for v in np.linspace(-1.0, 1.0, 5)
        ])

        # huge warm lamp
        lamp_body = Circle(radius=0.72, color=RED_WARM, fill_color=RED_WARM, fill_opacity=0.95)
        lamp_body.move_to(LEFT * 3.8)
        lamp_glow = Circle(radius=1.1, color=RED_WARM, fill_opacity=0).set_stroke(RED_WARM, 1.5, opacity=0.3)
        lamp_glow.move_to(lamp_body.get_center())
        lamp_label = warm_txt("red  ×100", size=26).next_to(lamp_body, DOWN, buff=0.2)

        # many long waves
        waves = VGroup()
        for offset in np.linspace(-0.4, 0.4, 4):
            pts = [lamp_body.get_right() + RIGHT * (0.08 + 0.13 * i) +
                   UP * (offset + 0.2 * np.sin(2 * PI / 1.4 * (0.13 * i)))
                   for i in range(26)]
            w = VMobject(color=RED_WARM, stroke_width=1.8, stroke_opacity=0.6).set_points_smoothly(pts)
            waves.add(w)

        times_label = Text("×100", font=FONT, font_size=34, color=YELLOW, weight=BOLD)
        times_label.next_to(lamp_body, RIGHT, buff=0.15).shift(UP * 0.5)

        self.add(plate, electrons)
        self.play(
            GrowFromCenter(lamp_body), FadeIn(lamp_glow), FadeIn(lamp_label),
            run_time=0.5
        )
        self.play(Create(waves), run_time=0.6)
        self.play(FadeIn(times_label), run_time=0.3)
        # electrons don't move
        self.wait(dur - 1.4)

# ── K01 — wave → packets ──────────────────────────────────────────────────────
class K01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("K01")

        # smooth sine wave
        wave = FunctionGraph(
            lambda x: 0.55 * np.sin(2 * PI / 1.6 * x),
            x_range=[-5.5, 5.5], color=BLUE, stroke_width=3
        )

        # discrete packet dots
        packet_xs = np.linspace(-5.0, 5.0, 11)
        packets   = VGroup(*[Dot(radius=0.2, color=BLUE).move_to([x, 0, 0]) for x in packet_xs])

        label = ink_txt("light arrives as separate packets", size=30).to_edge(DOWN, buff=0.55)

        self.play(Create(wave), run_time=0.7)
        self.wait(0.3)
        self.play(FadeOut(wave), run_time=0.25)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in packets], lag_ratio=0.08), run_time=0.9)
        self.play(Write(label), run_time=0.5)
        self.wait(dur - 2.6)

# ── K02 — red weak, blue strong ──────────────────────────────────────────────
class K02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("K02")

        # two packets
        red_pkt  = Dot(radius=0.28, color=RED_WARM).move_to(LEFT * 2.5)
        blue_pkt = Dot(radius=0.28, color=BLUE).move_to(RIGHT * 2.5)

        # energy bars under each
        def energy_bar(height, color, anchor):
            bar = Rectangle(width=0.45, height=height, color=color, fill_color=color, fill_opacity=0.85)
            bar.align_to(anchor, DOWN).shift(DOWN * 0.65)
            return bar

        red_bar  = energy_bar(0.8, RED_WARM, red_pkt)
        blue_bar = energy_bar(2.1, BLUE,     blue_pkt)

        red_lbl  = warm_txt("red · weak",   size=25).next_to(red_bar,  DOWN, buff=0.18)
        blue_lbl = blue_txt("blue · strong", size=25).next_to(blue_bar, DOWN, buff=0.18)

        self.play(GrowFromCenter(red_pkt), GrowFromCenter(blue_pkt), run_time=0.5)
        self.play(
            GrowFromEdge(red_bar,  DOWN),
            GrowFromEdge(blue_bar, DOWN),
            run_time=0.7
        )
        self.play(Write(red_lbl), Write(blue_lbl), run_time=0.5)
        self.wait(dur - 1.7)

# ── K03 — brightness = more packets, same energy ──────────────────────────────
class K03(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("K03")

        # dense stream of red packets
        xs = np.linspace(-5.0, 5.0, 18)
        packets = VGroup(*[Dot(radius=0.18, color=RED_WARM).move_to([x, 0.5, 0]) for x in xs])

        # bar — stays same height, flashes
        bar = Rectangle(width=0.45, height=0.8, color=RED_WARM, fill_color=RED_WARM, fill_opacity=0.85)
        bar.move_to(RIGHT * 0.0 + DOWN * 1.2)
        bar_lbl = warm_txt("energy unchanged", size=25).next_to(bar, DOWN, buff=0.18)

        brace = Brace(packets, UP, color=INK, buff=0.1)
        brace_lbl = ink_txt("more packets / second", size=25).next_to(brace, UP, buff=0.1)

        self.play(LaggedStart(*[GrowFromCenter(p) for p in packets], lag_ratio=0.04), run_time=0.9)
        self.play(FadeIn(brace), Write(brace_lbl), run_time=0.4)
        self.play(GrowFromEdge(bar, DOWN), Write(bar_lbl), run_time=0.45)
        # flash bar highlight
        flash = bar.copy().set_color(YELLOW).set_stroke(YELLOW, 3)
        self.play(FadeIn(flash), run_time=0.2)
        self.play(FadeOut(flash), run_time=0.2)
        self.wait(dur - 2.15)

# ── C01 — U-well, escape cost ─────────────────────────────────────────────────
class C01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("C01")

        # U-shaped well
        well_pts = [
            LEFT * 1.5 + UP * 1.6,
            LEFT * 1.5 + DOWN * 1.2,
            RIGHT * 1.5 + DOWN * 1.2,
            RIGHT * 1.5 + UP * 1.6,
        ]
        well = VMobject(color=INK, stroke_width=2.5)
        well.set_points_as_corners(well_pts)

        # electron at bottom of well
        electron = Dot(radius=0.2, color=BLUE).move_to(DOWN * 1.0)

        # dashed rim hairline
        rim = DashedLine(LEFT * 1.5 + UP * 0.9, RIGHT * 1.5 + UP * 0.9,
                         color=YELLOW, stroke_width=1.8, dash_length=0.18)
        rim_lbl = ink_txt("escape cost  φ", size=24).next_to(rim, RIGHT, buff=0.18)

        title_lbl = ink_txt("one packet must pay the full cost", size=27).to_edge(DOWN, buff=0.5)

        self.play(Create(well), run_time=0.6)
        self.play(GrowFromCenter(electron), run_time=0.35)
        self.play(Create(rim), FadeIn(rim_lbl), run_time=0.5)
        self.play(Write(title_lbl), run_time=0.5)
        self.wait(dur - 1.95)

# ── X01 — red packets, near-misses ────────────────────────────────────────────
class X01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("X01")

        # well
        well_pts = [LEFT * 1.5 + UP * 1.6, LEFT * 1.5 + DOWN * 1.2,
                    RIGHT * 1.5 + DOWN * 1.2, RIGHT * 1.5 + UP * 1.6]
        well = VMobject(color=INK, stroke_width=2.5).set_points_as_corners(well_pts)
        rim  = DashedLine(LEFT * 1.5 + UP * 0.9, RIGHT * 1.5 + UP * 0.9,
                          color=YELLOW, stroke_width=1.8, dash_length=0.18)
        rim_lbl = ink_txt("escape cost  φ", size=22).next_to(rim, RIGHT, buff=0.15)
        electron = Dot(radius=0.18, color=BLUE).move_to(DOWN * 1.0)

        counter_lbl = ink_txt("freed: 0", size=28).to_corner(DR, buff=0.45)

        self.add(well, rim, rim_lbl, electron, counter_lbl)

        # animate 3 red packets bouncing electron sub-rim
        for _ in range(3):
            pkt = Dot(radius=0.18, color=RED_WARM).move_to(LEFT * 4.5 + DOWN * 0.0)
            self.play(pkt.animate.move_to(electron.get_center() + LEFT * 0.3), run_time=0.25)
            self.play(
                electron.animate.move_to(DOWN * 0.2),   # hop up but below rim
                pkt.animate(remover=True).move_to(LEFT * 5),
                run_time=0.3
            )
            self.play(electron.animate.move_to(DOWN * 1.0), run_time=0.25)  # fall back

        self.wait(dur - 3.0)

# ── X02 — one blue packet, electron escapes ───────────────────────────────────
class X02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("X02")

        well_pts = [LEFT * 1.5 + UP * 1.6, LEFT * 1.5 + DOWN * 1.2,
                    RIGHT * 1.5 + DOWN * 1.2, RIGHT * 1.5 + UP * 1.6]
        well     = VMobject(color=INK, stroke_width=2.5).set_points_as_corners(well_pts)
        rim      = DashedLine(LEFT * 1.5 + UP * 0.9, RIGHT * 1.5 + UP * 0.9,
                              color=YELLOW, stroke_width=1.8, dash_length=0.18)
        rim_lbl  = ink_txt("escape cost  φ", size=22).next_to(rim, RIGHT, buff=0.15)
        electron = Dot(radius=0.18, color=BLUE).move_to(DOWN * 1.0)

        counter_0 = ink_txt("freed: 0", size=28).to_corner(DR, buff=0.45)
        counter_1 = ink_txt("freed: 1", size=28, color=BLUE).to_corner(DR, buff=0.45)

        self.add(well, rim, rim_lbl, electron, counter_0)

        # single blue packet
        blue_pkt = Dot(radius=0.18, color=BLUE).move_to(LEFT * 4.5)
        self.play(GrowFromCenter(blue_pkt), run_time=0.2)
        self.play(blue_pkt.animate.move_to(electron.get_center() + LEFT * 0.3), run_time=0.35)

        # electron shoots over rim
        escape_path = ArcBetweenPoints(
            electron.get_center(), RIGHT * 3.5 + UP * 2.2, angle=-PI / 3
        )
        self.play(
            MoveAlongPath(electron, escape_path),
            FadeOut(blue_pkt),
            run_time=0.8
        )
        self.play(Transform(counter_0, counter_1), run_time=0.25)
        self.wait(dur - 1.6)

# ── A01 — E = hν ─────────────────────────────────────────────────────────────
class A01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("A01")

        eq     = MathTex(r"E = h\nu", color=BLUE, font_size=96).shift(UP * 0.5)
        photon = ink_txt("photon", size=38).next_to(eq, DOWN, buff=0.45)
        rule   = Line(LEFT * 1.2, RIGHT * 1.2, stroke_width=1.0, color=DIM).next_to(photon, UP, buff=0.22)

        color_note = ink_txt("color is energy", size=28, color=DIM).to_edge(DOWN, buff=0.6)

        self.play(Write(eq), run_time=0.8)
        self.play(Create(rule), FadeIn(photon, shift=DOWN * 0.15), run_time=0.55)
        self.play(FadeIn(color_note), run_time=0.35)
        self.wait(dur - 1.7)

# ── P01 — payoff: both lamps, well ───────────────────────────────────────────
class P01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("P01")

        # compact well
        scale = 0.72
        well_pts = [(-1.5 * scale) * RIGHT + (1.6 * scale) * UP,
                    (-1.5 * scale) * RIGHT + (-1.2 * scale) * UP,
                    ( 1.5 * scale) * RIGHT + (-1.2 * scale) * UP,
                    ( 1.5 * scale) * RIGHT + (1.6 * scale) * UP]
        well = VMobject(color=INK, stroke_width=2.2).set_points_as_corners(well_pts)
        rim  = DashedLine((-1.5 * scale) * RIGHT + (0.9 * scale) * UP,
                           (1.5 * scale) * RIGHT + (0.9 * scale) * UP,
                           color=YELLOW, stroke_width=1.5, dash_length=0.14)
        well_group = VGroup(well, rim).shift(DOWN * 0.2)

        electron = Dot(radius=0.14, color=BLUE).move_to(DOWN * 0.9)

        # lamps
        red_lamp  = Circle(radius=0.38, color=RED_WARM, fill_color=RED_WARM, fill_opacity=0.85).move_to(LEFT * 5.5 + UP * 1.5)
        blue_lamp = Circle(radius=0.2,  color=BLUE,     fill_color=BLUE,     fill_opacity=0.75).move_to(LEFT * 5.5 + DOWN * 1.5)
        red_lbl   = warm_txt("red · bright", size=22).next_to(red_lamp, RIGHT, buff=0.2)
        blue_lbl  = blue_txt("blue · dim",   size=22).next_to(blue_lamp, RIGHT, buff=0.2)

        self.add(well_group, rim, electron)
        self.play(
            FadeIn(red_lamp), FadeIn(red_lbl),
            FadeIn(blue_lamp), FadeIn(blue_lbl),
            run_time=0.5
        )

        # red torrent — electron bobs, never escapes
        for _ in range(2):
            rpkt = Dot(radius=0.14, color=RED_WARM).move_to(red_lamp.get_right() + RIGHT * 0.1)
            self.play(rpkt.animate.move_to(electron.get_center() + LEFT * 0.15), run_time=0.22)
            self.play(
                electron.animate.shift(UP * 0.5),
                FadeOut(rpkt),
                run_time=0.22
            )
            self.play(electron.animate.shift(DOWN * 0.5), run_time=0.18)

        # one blue packet — electron escapes
        bpkt = Dot(radius=0.14, color=BLUE).move_to(blue_lamp.get_right() + RIGHT * 0.1)
        self.play(bpkt.animate.move_to(electron.get_center() + LEFT * 0.15), run_time=0.3)
        arc  = ArcBetweenPoints(electron.get_center(), RIGHT * 3.5 + UP * 1.8, angle=-PI / 4)
        self.play(MoveAlongPath(electron, arc), FadeOut(bpkt), run_time=0.7)

        summary = ink_txt("brightness counts · color decides", size=25, color=DIM).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(summary), run_time=0.3)
        self.wait(dur - 2.6)

# ── OUTRO ─────────────────────────────────────────────────────────────────────
class OUTRO(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("OUTRO")

        # hold the final payoff feel — title parks top band
        title_card = ink_txt("Why a Dim Blue Lamp Beats a Blinding Red One", size=30)
        title_card.to_edge(UP, buff=0.45).set_opacity(0.70)
        subtitle   = dim_txt("The full story → long video on the channel", size=24).next_to(title_card, DOWN, buff=0.2)

        self.play(FadeIn(title_card), FadeIn(subtitle), run_time=0.6)
        self.wait(dur - 0.6)
