import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

# Brown Blue palette
DARK_BG = "#1a1a1a"
BLUE = "#58C4DD"
BROWN = "#CD853F"
HIGHLIGHT = "#F0E442"
WARM = "#FC6255"   # red for this video (Bear's call: literal red for the low-frequency light)

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

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def blue_txt(t, size=36, color=BLUE, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def warm_txt(t, size=36, color=WARM, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def hl_txt(t, size=36, color=HIGHLIGHT, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def light_txt(t, size=36, **kw):
    return Text(t, font=FONT, font_size=size, color="#E0DDD5", **kw)


class INTRO_Title(Scene):
    def construct(self):
        self.add(bg())
        dur = d("INTRO", 3.93)
        series = Text("Bear's Notes", font=FONT, font_size=28, color=BROWN)
        series.move_to(UP * 1.2)
        title = Text("Why a Dim Blue Lamp Beats a Blinding Red One",
                     font=FONT, font_size=40, color="#E0DDD5")
        title.move_to(DOWN * 0.2)
        rule = Line(LEFT * 4, RIGHT * 4, color=BROWN, stroke_width=1.5)
        rule.move_to(DOWN * 0.9)
        tick = Dot(color=BLUE, radius=0.06).move_to(RIGHT * 4.2 + DOWN * 0.9)
        self.play(FadeIn(series), run_time=0.5)
        self.play(Write(title), run_time=1.5)
        self.play(Create(rule), FadeIn(tick), run_time=0.8)
        self.wait(dur - 2.8)


class H01_RedLampNoElectrons(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H01", 4.97)

        # Metal plate on the right
        plate = Rectangle(width=0.3, height=3, color="#888888", fill_opacity=1)
        plate.set_fill("#666666", 1).move_to(RIGHT * 3.5)

        # Electrons in plate
        electrons = VGroup(*[Dot(color=BLUE, radius=0.12).move_to(RIGHT * 3.2 + UP * (i - 1))
                              for i in range(3)])

        # Lamp on left
        lamp = Circle(radius=0.4, color=WARM, fill_opacity=0.8).move_to(LEFT * 4)
        lamp_label = Text("red", font=FONT, font_size=24, color=WARM).next_to(lamp, DOWN, buff=0.2)

        # Long-wavelength sine waves
        def make_wave(color=WARM, n_cycles=2, stretch=1.5):
            path = ParametricFunction(
                lambda t: np.array([t * stretch, 0.4 * np.sin(t * n_cycles * TAU / (stretch * 7.5)), 0]),
                t_range=[-5, 0], color=color, stroke_width=2)
            return path

        waves = VGroup(*[make_wave().shift(UP * (i - 1) * 0.3) for i in range(3)])
        waves.move_to(ORIGIN + LEFT * 0.5)

        self.play(GrowFromCenter(lamp), FadeIn(lamp_label), run_time=0.5)
        self.play(Create(plate), FadeIn(electrons), run_time=0.5)
        self.play(Create(waves), run_time=1.0)
        # electrons sit still
        self.wait(dur - 2.0)


class H02_BlueLampElectronsFly(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H02", 4.59)

        plate = Rectangle(width=0.3, height=3, color="#888888", fill_opacity=1)
        plate.set_fill("#666666", 1).move_to(RIGHT * 3.5)
        electrons = VGroup(*[Dot(color=BLUE, radius=0.12).move_to(RIGHT * 3.2 + UP * (i - 1))
                              for i in range(3)])
        self.add(plate, electrons)

        # Blue lamp (smaller)
        lamp = Circle(radius=0.28, color=BLUE, fill_opacity=0.7).move_to(LEFT * 4)
        lamp_label = Text("blue", font=FONT, font_size=24, color=BLUE).next_to(lamp, DOWN, buff=0.2)

        # Short-wavelength waves
        short_waves = VGroup(*[
            ParametricFunction(
                lambda t: np.array([t, 0.25 * np.sin(t * 5), 0]),
                t_range=[-5.5, -0.5], color=BLUE, stroke_width=2).shift(UP * (i - 1) * 0.3)
            for i in range(3)])
        short_waves.move_to(ORIGIN + LEFT * 0.5)

        self.play(GrowFromCenter(lamp), FadeIn(lamp_label), Create(short_waves), run_time=0.8)

        # Electrons fly off
        e1 = electrons[0].copy()
        e2 = electrons[1].copy()
        self.play(
            e1.animate.move_to(RIGHT * 5 + UP * 1.5),
            e2.animate.move_to(RIGHT * 5 + DOWN * 0.5),
            run_time=0.8)
        self.wait(dur - 1.6)


class H03_RedLampCrankedUp(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H03", 4.78)

        plate = Rectangle(width=0.3, height=3, color="#666666", fill_opacity=1).move_to(RIGHT * 3.5)
        electrons = VGroup(*[Dot(color=BLUE, radius=0.12).move_to(RIGHT * 3.2 + UP * (i - 1))
                              for i in range(3)])
        self.add(plate, electrons)

        # Large bright warm lamp
        lamp = Circle(radius=0.7, color=WARM, fill_opacity=0.9).move_to(LEFT * 4)
        lamp_label = Text("red", font=FONT, font_size=24, color=WARM).next_to(lamp, DOWN, buff=0.2)
        x100 = Text("×100", font="Courier New", font_size=32, color=INK).move_to(LEFT * 2 + UP * 2.5)

        many_waves = VGroup(*[
            ParametricFunction(
                lambda t: np.array([t * 1.5, 0.3 * np.sin(t * 1.5), 0]),
                t_range=[-5, 0], color=WARM, stroke_width=1.5).shift(UP * (i - 1.5) * 0.45)
            for i in range(6)])
        many_waves.move_to(ORIGIN + LEFT * 0.3)

        self.play(GrowFromCenter(lamp), FadeIn(lamp_label), run_time=0.5)
        self.play(Create(many_waves), run_time=0.8)
        self.play(FadeIn(x100), run_time=0.4)
        # electrons stay still
        self.wait(dur - 1.7)


class H04_BrightnessQuestion(Scene):
    def construct(self):
        self.add(bg())
        dur = d("H04", 4.82)

        plate = Rectangle(width=0.3, height=3, color="#666666", fill_opacity=1).move_to(RIGHT * 3.5)
        electrons = VGroup(*[Dot(color=BLUE, radius=0.12).move_to(RIGHT * 3.2 + UP * (i - 1))
                              for i in range(3)])
        lamp = Circle(radius=0.7, color=WARM, fill_opacity=0.9).move_to(LEFT * 4)
        x100 = Text("×100", font="Courier New", font_size=32, color=INK).move_to(LEFT * 2 + UP * 2.5)
        self.add(plate, electrons, lamp, x100)

        question = Text("?", font=FONT, font_size=72, color=HIGHLIGHT).move_to(RIGHT * 2 + UP * 0.5)
        self.play(FadeIn(question), run_time=0.4)
        self.play(Indicate(question, color=HIGHLIGHT, scale_factor=1.2), run_time=0.6)
        self.play(x100.animate.set_opacity(0.4), run_time=0.5)
        self.wait(dur - 1.5)


class W01_WavePicture(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W01", 7.08)

        plate = Rectangle(width=0.3, height=3, color="#666666", fill_opacity=1).move_to(RIGHT * 3.5)
        electrons = VGroup(*[Dot(color=BLUE, radius=0.12).move_to(RIGHT * 3.2 + UP * (i - 1))
                              for i in range(3)])
        self.add(plate, electrons)

        # Broad ripple arcs sweeping the plate
        ripples = VGroup(*[
            Arc(radius=1.5 + i * 0.4, angle=PI, start_angle=PI / 2,
                color=WARM, stroke_width=1.5, stroke_opacity=0.6)
            .move_to(LEFT * 1.5)
            for i in range(5)])

        # Energy bars under each electron
        bars = VGroup(*[
            Rectangle(width=0.15, height=0, color=BLUE, fill_opacity=1)
            .move_to(RIGHT * 3.2 + UP * (i - 1) + DOWN * 0.3)
            for i in range(3)])

        self.play(Create(ripples), run_time=1.0)
        self.play(*[bar.animate.stretch_to_fit_height(0.6).align_to(
            RIGHT * 3.2 + UP * (i - 1) + DOWN * 0.55, DOWN)
            for i, bar in enumerate(bars)], run_time=2.0)
        self.wait(dur - 3.0)


class W02_WaveModelFails(Scene):
    def construct(self):
        self.add(bg())
        dur = d("W02", 7.81)

        plate = Rectangle(width=0.3, height=3, color="#666666", fill_opacity=1).move_to(RIGHT * 3.5)
        electrons = VGroup(*[Dot(color=BLUE, radius=0.12).move_to(RIGHT * 3.2 + UP * (i - 1))
                              for i in range(3)])
        bars = VGroup(*[
            Rectangle(width=0.15, height=0.6, color=BLUE, fill_opacity=1)
            .move_to(RIGHT * 3.2 + UP * (i - 1) + DOWN * 0.55)
            for i in range(3)])
        ripples = VGroup(*[
            Arc(radius=1.5 + i * 0.4, angle=PI, start_angle=PI / 2,
                color=WARM, stroke_width=1.5, stroke_opacity=0.6).move_to(LEFT * 1.5)
            for i in range(5)])
        self.add(plate, electrons, bars, ripples)

        # Bars freeze; strike ripples; clock glyph
        strike = Line(ripples.get_left() + DOWN * 1.2, ripples.get_right() + UP * 1.2,
                      color=WARM, stroke_width=3)
        clock = Text("no patience", font=FONT, font_size=22, color="#888888").move_to(LEFT * 2 + DOWN * 2.5)

        self.play(Create(strike), run_time=0.6)
        self.play(FadeIn(clock), run_time=0.4)
        self.play(FadeOut(clock), run_time=0.5)
        self.wait(dur - 1.5)


class K01_LightAsPackets(Scene):
    def construct(self):
        self.add(bg())
        dur = d("K01", 5.01)

        # Start with smooth wave, then break into packets
        wave = ParametricFunction(
            lambda t: np.array([t, 0.5 * np.sin(t * 2), 0]),
            t_range=[-5, 5], color=WARM, stroke_width=3)
        wave.move_to(ORIGIN)

        # Discrete packets
        packets = VGroup(*[
            RoundedRectangle(width=0.5, height=0.5, corner_radius=0.1,
                             color=WARM, fill_opacity=0.8)
            .move_to(LEFT * 3 + RIGHT * i * 1.0)
            for i in range(7)])

        self.play(Create(wave), run_time=0.8)
        self.play(ReplacementTransform(wave, packets), run_time=1.2)
        # Packets drift rightward
        self.play(packets.animate.shift(RIGHT * 0.8), run_time=1.0)
        self.wait(dur - 3.0)


class K02_PacketEnergy(Scene):
    def construct(self):
        self.add(bg())
        dur = d("K02", 6.17)

        # Two packets center stage
        red_pkt = RoundedRectangle(width=0.6, height=0.6, corner_radius=0.1,
                                   color=WARM, fill_opacity=0.8).move_to(LEFT * 2.5)
        blue_pkt = RoundedRectangle(width=0.6, height=0.6, corner_radius=0.1,
                                    color=BLUE, fill_opacity=0.8).move_to(RIGHT * 2.5)

        # Energy bars beneath them
        red_bar = Rectangle(width=0.4, height=1.0, color=WARM, fill_opacity=0.9).next_to(red_pkt, DOWN, buff=0.3)
        blue_bar = Rectangle(width=0.4, height=2.5, color=BLUE, fill_opacity=0.9).next_to(blue_pkt, DOWN, buff=0.3)

        red_lbl = Text("red · weak", font=FONT, font_size=22, color=INK).next_to(red_bar, DOWN, buff=0.2)
        blue_lbl = Text("blue · strong", font=FONT, font_size=22, color=INK).next_to(blue_bar, DOWN, buff=0.2)

        self.play(GrowFromCenter(red_pkt), GrowFromCenter(blue_pkt), run_time=0.6)
        self.play(
            GrowFromEdge(red_bar, DOWN),
            GrowFromEdge(blue_bar, DOWN),
            run_time=1.0)
        self.play(Write(red_lbl), Write(blue_lbl), run_time=0.8)
        self.wait(dur - 2.4)


class K03_MorePacketsNotFatter(Scene):
    def construct(self):
        self.add(bg())
        dur = d("K03", 4.5)

        red_bar = Rectangle(width=0.4, height=1.0, color=WARM, fill_opacity=0.9).move_to(ORIGIN + DOWN * 0.5)
        red_lbl = Text("red · weak", font=FONT, font_size=22, color=INK).next_to(red_bar, DOWN, buff=0.2)
        self.add(red_bar, red_lbl)

        # Dense stream of warm packets
        stream = VGroup(*[
            RoundedRectangle(width=0.35, height=0.35, corner_radius=0.08, color=WARM, fill_opacity=0.7)
            .move_to(LEFT * 4 + RIGHT * i * 0.5 + UP * 1.5)
            for i in range(12)])
        self.play(LaggedStart(*[FadeIn(p) for p in stream], lag_ratio=0.08), run_time=1.2)

        # Bar unchanged — flash highlight
        self.play(Indicate(red_bar, color=HIGHLIGHT, scale_factor=1.1), run_time=0.8)
        self.wait(dur - 2.0)


class C01_EscapeCostWell(Scene):
    def construct(self):
        self.add(bg())
        dur = d("C01", 6.49)

        # U-shaped well
        well_l = Line(LEFT * 1.5 + DOWN * 2, LEFT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        well_b = Line(LEFT * 1.5 + DOWN * 2, RIGHT * 1.5 + DOWN * 2, color="#E0DDD5", stroke_width=3)
        well_r = Line(RIGHT * 1.5 + DOWN * 2, RIGHT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        well = VGroup(well_l, well_b, well_r)

        electron = Dot(color=BLUE, radius=0.2).move_to(DOWN * 1.6)

        rim_line = DashedLine(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5,
                              color=HIGHLIGHT, stroke_width=1.5)
        escape_lbl = Text("escape cost", font=FONT, font_size=22, color=HIGHLIGHT).next_to(rim_line, RIGHT, buff=0.3)

        self.play(Create(well), run_time=0.8)
        self.play(GrowFromCenter(electron), run_time=0.4)
        self.play(Create(rim_line), Write(escape_lbl), run_time=0.8)
        self.wait(dur - 2.0)


class C02_PacketAbsorbedWhole(Scene):
    def construct(self):
        self.add(bg())
        dur = d("C02", 5.14)

        well_l = Line(LEFT * 1.5 + DOWN * 2, LEFT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        well_b = Line(LEFT * 1.5 + DOWN * 2, RIGHT * 1.5 + DOWN * 2, color="#E0DDD5", stroke_width=3)
        well_r = Line(RIGHT * 1.5 + DOWN * 2, RIGHT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        electron = Dot(color=BLUE, radius=0.2).move_to(DOWN * 1.6)
        rim_line = DashedLine(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5,
                              color=HIGHLIGHT, stroke_width=1.5)
        self.add(well_l, well_b, well_r, electron, rim_line)

        packet = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.1, color=BLUE, fill_opacity=0.8)
        packet.move_to(LEFT * 3 + DOWN * 1.6)

        self.play(packet.animate.move_to(electron.get_center()), run_time=0.6)
        self.play(FadeOut(packet), electron.animate.scale(1.5).set_color(HIGHLIGHT), run_time=0.3)
        self.play(electron.animate.scale(1/1.5).set_color(BLUE), run_time=0.3)

        # Ghost of split-among-many
        ghost_text = Text("never split among many", font=FONT, font_size=20, color="#666666")
        ghost_text.move_to(RIGHT * 3 + UP * 1)
        ghost_line = Line(ghost_text.get_left(), ghost_text.get_right(), color="#888888", stroke_width=2)
        self.play(FadeIn(ghost_text), run_time=0.3)
        self.play(Create(ghost_line), run_time=0.3)
        self.play(FadeOut(ghost_text), FadeOut(ghost_line), run_time=0.5)
        self.wait(dur - 2.3)


class X01_RedFallsShort(Scene):
    def construct(self):
        self.add(bg())
        dur = d("X01", 5.95)

        well_l = Line(LEFT * 1.5 + DOWN * 2, LEFT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        well_b = Line(LEFT * 1.5 + DOWN * 2, RIGHT * 1.5 + DOWN * 2, color="#E0DDD5", stroke_width=3)
        well_r = Line(RIGHT * 1.5 + DOWN * 2, RIGHT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        electron = Dot(color=BLUE, radius=0.2).move_to(DOWN * 1.6)
        rim_line = DashedLine(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5,
                              color=HIGHLIGHT, stroke_width=1.5)
        self.add(well_l, well_b, well_r, electron, rim_line)

        # Red packet in, electron rises to ~60% of rim, falls back
        red_pkt = RoundedRectangle(width=0.4, height=0.4, corner_radius=0.1, color=WARM, fill_opacity=0.8)
        red_pkt.move_to(LEFT * 3 + DOWN * 1.6)

        self.play(red_pkt.animate.move_to(electron.get_center()), run_time=0.4)
        self.play(FadeOut(red_pkt), run_time=0.1)

        # Rise to ~60% of rim height (rim is at y=0.5, electron at y=-1.6, total=2.1, 60%=1.26)
        partial_pos = DOWN * 1.6 + UP * 1.26
        self.play(electron.animate.move_to(partial_pos), run_time=0.5)
        self.play(electron.animate.move_to(DOWN * 1.6), run_time=0.5)

        # Shimmer marks (heat)
        shimmers = VGroup(*[
            Dot(radius=0.05, color="#FF8866").move_to(partial_pos + RIGHT * (i - 1) * 0.3)
            for i in range(3)])
        self.play(LaggedStart(*[shimmers[i].animate.shift(UP * 0.6).set_opacity(0)
                                for i in range(3)], lag_ratio=0.1), run_time=0.8)
        self.wait(dur - 2.3)


class X02_FloodOfNearMisses(Scene):
    def construct(self):
        self.add(bg())
        dur = d("X02", 5.97)

        well_l = Line(LEFT * 1.5 + DOWN * 2, LEFT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        well_b = Line(LEFT * 1.5 + DOWN * 2, RIGHT * 1.5 + DOWN * 2, color="#E0DDD5", stroke_width=3)
        well_r = Line(RIGHT * 1.5 + DOWN * 2, RIGHT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        electron = Dot(color=BLUE, radius=0.2).move_to(DOWN * 1.6)
        rim_line = DashedLine(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5, color=HIGHLIGHT, stroke_width=1.5)
        counter = Text("freed: 0", font="Courier New", font_size=24, color=INK).move_to(RIGHT * 5 + DOWN * 2.5)
        self.add(well_l, well_b, well_r, electron, rim_line, counter)

        # Rain of red packets, each producing partial hop
        partial_pos = DOWN * 0.34  # -1.6 + 1.26
        for _ in range(4):
            pkt = RoundedRectangle(width=0.3, height=0.3, corner_radius=0.08, color=WARM, fill_opacity=0.8)
            pkt.move_to(LEFT * 3 + DOWN * 1.6)
            self.play(pkt.animate.move_to(electron.get_center()), FadeOut(pkt), run_time=0.15)
            self.play(electron.animate.move_to(partial_pos), run_time=0.15)
            self.play(electron.animate.move_to(DOWN * 1.6), run_time=0.15)

        # Counter never changes
        self.play(Indicate(counter, color=HIGHLIGHT), run_time=0.5)
        self.wait(dur - 2.0)


class X03_BlueClearsRim(Scene):
    def construct(self):
        self.add(bg())
        dur = d("X03", 6.49)

        well_l = Line(LEFT * 1.5 + DOWN * 2, LEFT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        well_b = Line(LEFT * 1.5 + DOWN * 2, RIGHT * 1.5 + DOWN * 2, color="#E0DDD5", stroke_width=3)
        well_r = Line(RIGHT * 1.5 + DOWN * 2, RIGHT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=3)
        electron = Dot(color=BLUE, radius=0.2).move_to(DOWN * 1.6)
        rim_line = DashedLine(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5, color=HIGHLIGHT, stroke_width=1.5)
        counter = Text("freed: 0", font="Courier New", font_size=24, color=INK).move_to(RIGHT * 5 + DOWN * 2.5)
        self.add(well_l, well_b, well_r, electron, rim_line, counter)

        blue_pkt = RoundedRectangle(width=0.4, height=0.4, corner_radius=0.1, color=BLUE, fill_opacity=0.8)
        blue_pkt.move_to(LEFT * 3 + DOWN * 1.6)
        counter2 = Text("freed: 1", font="Courier New", font_size=24, color=BLUE).move_to(RIGHT * 5 + DOWN * 2.5)

        self.play(blue_pkt.animate.move_to(electron.get_center()), run_time=0.4)
        self.play(FadeOut(blue_pkt), run_time=0.1)
        # Electron shoots over rim and arcs away
        self.play(electron.animate.move_to(UP * 0.5), run_time=0.4)
        self.play(electron.animate.move_to(RIGHT * 4 + UP * 1.5), run_time=0.6)
        self.play(ReplacementTransform(counter, counter2), run_time=0.4)
        self.wait(dur - 1.9)


class X04_LeftoverBecomesSpeed(Scene):
    def construct(self):
        self.add(bg())
        dur = d("X04", 4.78)

        # Blue packet energy bar split at rim
        total_h = 3.0
        cost_h = 2.0
        leftover_h = total_h - cost_h

        bar_bg = Rectangle(width=0.5, height=total_h, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2 + DOWN * 0.5)
        cost_part = Rectangle(width=0.5, height=cost_h, color="#888888", fill_opacity=0.7)
        cost_part.align_to(bar_bg, DOWN)
        leftover_part = Rectangle(width=0.5, height=leftover_h, color=BLUE, fill_opacity=0.9)
        leftover_part.align_to(bar_bg, UP)

        cost_line = DashedLine(LEFT * 2.5 + DOWN * 0.5, LEFT * 1.5 + DOWN * 0.5,
                               color=HIGHLIGHT, stroke_width=1.5)
        cost_lbl = Text("escape cost", font=FONT, font_size=20, color=HIGHLIGHT).next_to(cost_line, RIGHT, buff=0.2)

        # Free electron with speed arrow
        free_e = Dot(color=BLUE, radius=0.2).move_to(RIGHT * 2)
        speed_arrow = Arrow(RIGHT * 2, RIGHT * 4, color=HIGHLIGHT, buff=0)

        self.add(bar_bg, cost_part, leftover_part, cost_line, cost_lbl)
        self.play(GrowFromCenter(free_e), run_time=0.4)
        self.play(leftover_part.animate.set_color(HIGHLIGHT), run_time=0.5)
        self.play(ReplacementTransform(leftover_part.copy(), speed_arrow), run_time=0.8)
        self.wait(dur - 1.7)


class A01_EqualshNu(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A01", 8.06)

        # Keep well in bg
        well_l = Line(LEFT * 1.5 + DOWN * 2, LEFT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=2, stroke_opacity=0.4)
        well_b = Line(LEFT * 1.5 + DOWN * 2, RIGHT * 1.5 + DOWN * 2, color="#E0DDD5", stroke_width=2, stroke_opacity=0.4)
        well_r = Line(RIGHT * 1.5 + DOWN * 2, RIGHT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=2, stroke_opacity=0.4)
        self.add(well_l, well_b, well_r)

        # SIDE region: right side
        eq = MathTex(r"E = h\nu", color="#E0DDD5", font_size=56).move_to(RIGHT * 4.5 + UP * 1.5)
        photon_lbl = Text("photon", font=FONT, font_size=32, color=BLUE).next_to(eq, DOWN, buff=0.5)

        self.play(Write(eq), run_time=1.5)
        self.play(FadeIn(photon_lbl), run_time=0.6)
        self.wait(dur - 2.1)


class A02_KineticFormula(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A02", 8.55)

        eq1 = MathTex(r"E = h\nu", color="#E0DDD5", font_size=48).move_to(RIGHT * 4.5 + UP * 2.0)
        self.add(eq1)

        eq2 = MathTex(r"K = h\nu - \Phi", color="#E0DDD5", font_size=48).move_to(RIGHT * 4.5 + UP * 0.5)

        # Rim line in the well (background)
        rim_line = DashedLine(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5, color=HIGHLIGHT, stroke_width=1.5, stroke_opacity=0.5)
        self.add(rim_line)

        self.play(Write(eq2), run_time=1.5)
        self.play(Indicate(eq2, color=HIGHLIGHT), run_time=0.6)
        self.wait(dur - 2.1)


class A03_ThresholdFrequency(Scene):
    def construct(self):
        self.add(bg())
        dur = d("A03", 6.59)

        eq1 = MathTex(r"E = h\nu", color="#E0DDD5", font_size=40).move_to(RIGHT * 4.5 + UP * 2.5)
        eq2 = MathTex(r"K = h\nu - \Phi", color="#E0DDD5", font_size=40).move_to(RIGHT * 4.5 + UP * 1.5)
        self.add(eq1, eq2)

        # Frequency axis
        axis = NumberLine(x_range=[0, 6, 1], length=4, color="#E0DDD5",
                          include_ticks=False).move_to(RIGHT * 4.5 + DOWN * 0.5)

        warm_region = Rectangle(width=2, height=0.4, color=WARM, fill_opacity=0.3, stroke_width=0)
        warm_region.align_to(axis, LEFT).move_to(axis.get_left() + RIGHT * 1 + UP * 0.05)

        blue_region = Rectangle(width=2.5, height=0.4, color=BLUE, fill_opacity=0.3, stroke_width=0)
        blue_region.align_to(axis.n2p(2), LEFT).move_to(axis.n2p(3.25) + UP * 0.05)

        tick = DashedLine(axis.n2p(2) + UP * 0.3, axis.n2p(2) + DOWN * 0.3, color=HIGHLIGHT)
        nu0_lbl = MathTex(r"\nu_0", color=HIGHLIGHT, font_size=28).next_to(axis.n2p(2), DOWN, buff=0.15)

        self.play(Create(axis), run_time=0.5)
        self.play(FadeIn(warm_region), FadeIn(blue_region), run_time=0.5)
        self.play(Create(tick), Write(nu0_lbl), run_time=0.6)
        self.play(warm_region.animate.set_opacity(0.1), run_time=0.5)
        self.wait(dur - 2.1)


class P01_MysteryDissolves(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P01", 6.85)

        # Both lamps return above the well
        red_lamp = Circle(radius=0.5, color=WARM, fill_opacity=0.8).move_to(LEFT * 3 + UP * 2.5)
        red_lbl = Text("red", font=FONT, font_size=20, color=WARM).next_to(red_lamp, DOWN, buff=0.1)
        blue_lamp = Circle(radius=0.28, color=BLUE, fill_opacity=0.7).move_to(LEFT * 0.5 + UP * 2.5)
        blue_lbl = Text("blue", font=FONT, font_size=20, color=BLUE).next_to(blue_lamp, DOWN, buff=0.1)

        # Well
        well_l = Line(LEFT * 1.5 + DOWN * 2, LEFT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=2)
        well_b = Line(LEFT * 1.5 + DOWN * 2, RIGHT * 1.5 + DOWN * 2, color="#E0DDD5", stroke_width=2)
        well_r = Line(RIGHT * 1.5 + DOWN * 2, RIGHT * 1.5 + UP * 0.5, color="#E0DDD5", stroke_width=2)
        self.add(well_l, well_b, well_r)

        question = Text("?", font=FONT, font_size=60, color=HIGHLIGHT).move_to(RIGHT * 2.5 + UP * 0.5)

        self.play(FadeIn(red_lamp), FadeIn(red_lbl), FadeIn(blue_lamp), FadeIn(blue_lbl), run_time=0.6)

        # Red packets (many)
        red_pkts = VGroup(*[
            RoundedRectangle(width=0.3, height=0.3, corner_radius=0.07, color=WARM, fill_opacity=0.7)
            .move_to(red_lamp.get_center() + DOWN * (0.5 + i * 0.35))
            for i in range(4)])

        # Blue packet (one)
        blue_pkt = RoundedRectangle(width=0.35, height=0.35, corner_radius=0.07, color=BLUE, fill_opacity=0.8)
        blue_pkt.move_to(blue_lamp.get_center() + DOWN * 0.5)

        self.play(LaggedStart(*[FadeIn(p) for p in red_pkts], lag_ratio=0.15), FadeIn(blue_pkt), run_time=0.8)
        self.play(FadeIn(question), run_time=0.3)
        self.play(FadeOut(question), run_time=0.5)
        self.wait(dur - 2.2)


class P02_TorrentVsTrickle(Scene):
    def construct(self):
        self.add(bg())
        dur = d("P02", 6.87)

        # Well (small, left side)
        well_l = Line(LEFT * 5.5 + DOWN * 1.5, LEFT * 5.5 + UP * 0.3, color="#E0DDD5", stroke_width=2)
        well_b = Line(LEFT * 5.5 + DOWN * 1.5, LEFT * 3.5 + DOWN * 1.5, color="#E0DDD5", stroke_width=2)
        well_r = Line(LEFT * 3.5 + DOWN * 1.5, LEFT * 3.5 + UP * 0.3, color="#E0DDD5", stroke_width=2)
        e_red = Dot(color=BLUE, radius=0.15).move_to(LEFT * 4.5 + DOWN * 1.2)
        rim_red = DashedLine(LEFT * 5.5 + UP * 0.3, LEFT * 3.5 + UP * 0.3, color=HIGHLIGHT, stroke_width=1)
        self.add(well_l, well_b, well_r, e_red, rim_red)

        # Well (right side for blue)
        well2_l = Line(RIGHT * 3.5 + DOWN * 1.5, RIGHT * 3.5 + UP * 0.3, color="#E0DDD5", stroke_width=2)
        well2_b = Line(RIGHT * 3.5 + DOWN * 1.5, RIGHT * 5.5 + DOWN * 1.5, color="#E0DDD5", stroke_width=2)
        well2_r = Line(RIGHT * 5.5 + DOWN * 1.5, RIGHT * 5.5 + UP * 0.3, color="#E0DDD5", stroke_width=2)
        e_blue = Dot(color=BLUE, radius=0.15).move_to(RIGHT * 4.5 + DOWN * 1.2)
        rim_blue = DashedLine(RIGHT * 3.5 + UP * 0.3, RIGHT * 5.5 + UP * 0.3, color=HIGHLIGHT, stroke_width=1)
        self.add(well2_l, well2_b, well2_r, e_blue, rim_blue)

        # Red: many packets, all fail
        for _ in range(3):
            pkt = RoundedRectangle(width=0.25, height=0.25, corner_radius=0.06, color=WARM, fill_opacity=0.7)
            pkt.move_to(LEFT * 5 + UP * 1)
            self.play(pkt.animate.move_to(e_red.get_center()), run_time=0.2)
            partial = e_red.get_center() + UP * 0.8
            self.play(FadeOut(pkt), e_red.animate.move_to(partial), run_time=0.15)
            self.play(e_red.animate.move_to(LEFT * 4.5 + DOWN * 1.2), run_time=0.15)

        # Blue: one packet, electron frees
        blue_pkt = RoundedRectangle(width=0.3, height=0.3, corner_radius=0.07, color=BLUE, fill_opacity=0.8)
        blue_pkt.move_to(RIGHT * 4 + UP * 1)
        self.play(blue_pkt.animate.move_to(e_blue.get_center()), run_time=0.3)
        self.play(FadeOut(blue_pkt), e_blue.animate.move_to(RIGHT * 6 + UP * 0.5), run_time=0.4)
        self.wait(dur - 1.5 - 3 * 0.5)


class N01_SodiumNumbers(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N01", 9.75)

        # Sodium card
        title_card = Text("sodium · 300 nm", font=FONT, font_size=30, color="#E0DDD5").move_to(UP * 1.5)
        self.play(Write(title_card), run_time=0.5)

        # Bar: 4.13 eV vs cost at 2.28
        total_h = 3.0
        cost_frac = 2.28 / 4.13

        bar = Rectangle(width=0.8, height=total_h, color=BLUE, fill_opacity=0.8).move_to(DOWN * 0.5)
        cost_line = DashedLine(bar.get_left() + UP * (total_h * cost_frac - total_h / 2),
                               bar.get_right() + UP * (total_h * cost_frac - total_h / 2),
                               color=HIGHLIGHT, stroke_width=2)

        lbl_total = MathTex(r"4.13\,\text{eV}", color=BLUE, font_size=28).next_to(bar, RIGHT, buff=0.3).shift(UP * 0.8)
        lbl_cost = MathTex(r"\Phi = 2.28\,\text{eV}", color=HIGHLIGHT, font_size=28).next_to(cost_line, RIGHT, buff=0.3)

        surplus = Rectangle(width=0.8, height=total_h * (1 - cost_frac),
                            color=HIGHLIGHT, fill_opacity=0.5, stroke_width=0)
        surplus.align_to(bar, UP)

        self.play(GrowFromEdge(bar, DOWN), run_time=0.8)
        self.play(Create(cost_line), Write(lbl_cost), Write(lbl_total), run_time=0.8)
        self.play(FadeIn(surplus), run_time=0.3)
        self.play(surplus.animate.set_opacity(0.2), run_time=0.5)
        self.wait(dur - 2.4)


class N02_GreenFails(Scene):
    def construct(self):
        self.add(bg())
        dur = d("N02", 7.7)

        title_card = Text("546 nm", font=FONT, font_size=30, color="#E0DDD5").move_to(UP * 1.5)
        self.play(FadeIn(title_card), run_time=0.4)

        total_h = 3.0
        cost_frac_green = 2.27 / 4.13
        actual_frac_green = 2.27 / 4.13

        bar = Rectangle(width=0.8, height=total_h * actual_frac_green, color="#66CC66", fill_opacity=0.8)
        bar.move_to(DOWN * 1.0)

        # Cost hairline slightly above bar top
        cost_y = bar.get_top() + UP * 0.08
        cost_line = DashedLine(LEFT * 1 + cost_y[1] * UP,
                               RIGHT * 1 + cost_y[1] * UP,
                               color=HIGHLIGHT, stroke_width=2)

        lbl_total = MathTex(r"2.27\,\text{eV}", color="#66CC66", font_size=28).next_to(bar, RIGHT, buff=0.3)
        lbl_cost = MathTex(r"\Phi = 2.28\,\text{eV}", color=HIGHLIGHT, font_size=24).next_to(cost_line, RIGHT, buff=0.2)

        watts = Text("10,000 W", font="Courier New", font_size=28, color=INK).move_to(RIGHT * 4 + UP * 0.5)

        self.play(GrowFromEdge(bar, DOWN), run_time=0.6)
        self.play(Create(cost_line), Write(lbl_cost), Write(lbl_total), run_time=0.7)
        self.play(FadeIn(watts), run_time=0.4)
        # Nothing happens
        self.wait(dur - 1.7)


class B01_CloseCard(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B01", 7.15)

        eq1 = MathTex(r"E = h\nu", color="#E0DDD5", font_size=52).move_to(UP * 1.0)
        eq2 = MathTex(r"K = h\nu - \Phi", color="#E0DDD5", font_size=52).move_to(DOWN * 0.2)

        tag1 = Text("next · measuring h", font=FONT, font_size=24, color="#888888").move_to(DOWN * 1.5)
        tag2 = Text("next · the double slit", font=FONT, font_size=24, color="#888888").move_to(DOWN * 2.2)

        self.play(Write(eq1), Write(eq2), run_time=1.2)
        self.play(LaggedStart(FadeIn(tag1), FadeIn(tag2), lag_ratio=0.3), run_time=0.8)
        self.wait(dur - 2.0)


class B02_Exercise(Scene):
    def construct(self):
        self.add(bg())
        dur = d("B02", 6.93)

        eq1 = MathTex(r"E = h\nu", color="#E0DDD5", font_size=36).move_to(UP * 3 + LEFT * 2)
        eq2 = MathTex(r"K = h\nu - \Phi", color="#E0DDD5", font_size=36).move_to(UP * 3 + RIGHT * 2)
        self.add(eq1, eq2)

        exercise = Text(
            "Look up a metal's escape cost —\nfind the longest wavelength that can still free an electron.",
            font=FONT, font_size=28, color=HIGHLIGHT, line_spacing=1.4
        ).move_to(ORIGIN)

        self.play(Write(exercise), run_time=1.5)
        self.wait(dur - 1.5)


class OUTRO_Final(Scene):
    def construct(self):
        self.add(bg())
        dur = d("OUTRO", 7.21)

        # Final frame holds, title in upper band
        eq1 = MathTex(r"E = h\nu", color="#E0DDD5", font_size=36).move_to(UP * 2)
        eq2 = MathTex(r"K = h\nu - \Phi", color="#E0DDD5", font_size=36).move_to(UP * 1.0)
        self.add(eq1, eq2)

        title = Text("Why a Dim Blue Lamp Beats a Blinding Red One",
                     font=FONT, font_size=26, color="#E0DDD5", fill_opacity=0.7)
        title.move_to(UP * 3.5)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(dur - 0.5)
