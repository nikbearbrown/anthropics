import json
import numpy as np
from pathlib import Path
from manim import *

# ── palette (3b1b dark) ────────────────────────────────────────────────────────
CANVAS = "#1C1C1C"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
YELLOW = "#F0E442"
INK    = "#EEEEEE"
DIM    = "#888888"
FONT   = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs   = json.loads((HERE / "beat_sheet.json").read_text())
    DUR   = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 5)
             for b in _bs.get("beats", [])}
    TITLE = _bs["metadata"].get("title", "")
except Exception:
    DUR = {}; TITLE = ""

def d(bid, default=5.0):
    return DUR.get(bid, default)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def blue_txt(t, size=36, color=BLUE, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def brown_txt(t, size=36, color=BROWN, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def dim_txt(t, size=28, color=DIM, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

# ── compact two-slit lab (used in M01/M02/S01/S02/A01/A02/A03/P01) ───────────
def make_compact_lab(scale=0.70):
    """Return (gun, barrier, bar_x, slit_y_top, slit_y_bot, screen) scaled."""
    ox = -1.0   # shift left to leave right margin for top strip

    gun = Rectangle(width=0.5 * scale, height=0.7 * scale,
                    color=INK, fill_color=INK, fill_opacity=0.25)
    gun.move_to([-5.5 * scale + ox, 0, 0])

    # barrier pieces
    barrier_top = Rectangle(width=0.2, height=1.4 * scale, color=BROWN, fill_color=BROWN, fill_opacity=0.8)
    barrier_top.move_to([0.5 * scale + ox, 1.7 * scale, 0])
    barrier_mid = Rectangle(width=0.2, height=0.65 * scale, color=BROWN, fill_color=BROWN, fill_opacity=0.8)
    barrier_mid.next_to(barrier_top, DOWN, buff=0.45 * scale)
    barrier_bot = Rectangle(width=0.2, height=0.65 * scale, color=BROWN, fill_color=BROWN, fill_opacity=0.8)
    barrier_bot.next_to(barrier_mid, DOWN, buff=0.45 * scale)
    barrier_base = Rectangle(width=0.2, height=1.4 * scale, color=BROWN, fill_color=BROWN, fill_opacity=0.8)
    barrier_base.next_to(barrier_bot, DOWN, buff=0.0)
    barrier = VGroup(barrier_top, barrier_mid, barrier_bot, barrier_base)

    bar_x     = barrier_top.get_center()[0]
    slit_y_top = (barrier_top.get_bottom()[1] + barrier_mid.get_top()[1]) / 2
    slit_y_bot = (barrier_mid.get_bottom()[1] + barrier_bot.get_top()[1]) / 2

    screen = Line(UP * 2.8 * scale, DOWN * 2.8 * scale, color=INK, stroke_width=2)
    screen.move_to([4.5 * scale + ox, 0, 0])
    screen_x = screen.get_x()

    return gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x

# ── INTRO ─────────────────────────────────────────────────────────────────────
class INTRO(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("INTRO", 4.0)

        series = ink_txt("Bear's Notes", size=28).move_to(UP * 2.8)
        rule   = Line(LEFT * 3.8, RIGHT * 3.8, stroke_width=1.2, color=BROWN).next_to(series, DOWN, buff=0.18)
        title  = ink_txt("What Wave–Particle Duality", size=44, weight=BOLD).next_to(rule, DOWN, buff=0.32)
        title2 = ink_txt("Actually Means", size=44, weight=BOLD).next_to(title, DOWN, buff=0.08)
        tick   = Dot(radius=0.08, color=BLUE).next_to(rule, RIGHT, buff=0.12).align_to(rule, DOWN)

        self.play(FadeIn(series, shift=UP * 0.2), run_time=0.5)
        self.play(Create(rule), FadeIn(tick), run_time=0.4)
        self.play(Write(title), Write(title2), run_time=0.9)
        self.wait(dur - 1.8)

# ── H01 — brown ball with ripple circles ─────────────────────────────────────
class H01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H01", 5.0)

        ball    = Dot(radius=0.28, color=BROWN)
        ripples = VGroup(*[
            Circle(radius=r, color=BLUE, fill_opacity=0).set_stroke(BLUE, 1.5, opacity=0.6 - i * 0.1)
            for i, r in enumerate([0.7, 1.2, 1.8, 2.5])
        ])
        label = dim_txt("the popular cartoon", size=26).to_edge(DOWN, buff=0.55)

        self.play(GrowFromCenter(ball), run_time=0.45)
        self.play(LaggedStart(*[Create(r) for r in ripples], lag_ratio=0.2), run_time=0.8)
        self.play(FadeIn(label), run_time=0.35)
        self.wait(dur - 1.6)

# ── H02 — scale brace, cartoon dims ──────────────────────────────────────────
class H02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H02", 5.0)

        ball    = Dot(radius=0.28, color=BROWN)
        ripples = VGroup(*[
            Circle(radius=r, color=BLUE, fill_opacity=0).set_stroke(BLUE, 1.5, opacity=0.5 - i * 0.1)
            for i, r in enumerate([0.7, 1.2, 1.8, 2.5])
        ])
        cartoon = VGroup(ball, ripples)
        self.add(cartoon)

        # brace over ripples labeled wavelength
        outer_ripple = ripples[-1]
        brace = Brace(outer_ripple, UP, color=BLUE, buff=0.1)
        brace_lbl = blue_txt("0.167 nm", size=26).next_to(brace, UP, buff=0.1)

        # tick at ball labeled ÷60,000
        tick_lbl = ink_txt("÷ 60,000", size=24).next_to(ball, DR, buff=0.2)
        arrow    = Arrow(tick_lbl.get_left() + LEFT * 0.1, ball.get_right(), buff=0.05,
                         stroke_width=1.5, color=INK, max_tip_length_to_length_ratio=0.15)

        self.play(Create(brace), Write(brace_lbl), run_time=0.5)
        self.play(FadeIn(tick_lbl), Create(arrow), run_time=0.45)
        self.play(cartoon.animate.set_opacity(0.35), run_time=0.5)
        self.wait(dur - 1.45)

# ── M01 — compact lab, wave answer (stripes) ──────────────────────────────────
class M01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("M01", 5.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.play(FadeIn(gun), FadeIn(barrier), Create(screen), run_time=0.5)

        # faint streaks through slits
        for slit_y in [slit_y_top, slit_y_bot]:
            streak = Line(gun.get_right(), np.array([bar_x, slit_y, 0]),
                          color=BLUE, stroke_width=1, stroke_opacity=0.4)
            self.play(Create(streak), run_time=0.15)

        # striped curve
        def intensity(y):
            k, ds = 3.0, abs(slit_y_top - slit_y_bot) / 2
            return (np.cos(k * ds * y / (screen_x - bar_x))) ** 2

        ys  = np.linspace(-2.5, 2.5, 160)
        pts = [np.array([screen_x + 0.3 * intensity(y), y, 0]) for y in ys]
        stripe = VMobject(color=BLUE, stroke_width=2.2).set_points_smoothly(pts)

        q_label = ink_txt('"how do you travel?"', size=25, slant=ITALIC).to_edge(UP, buff=0.4)
        self.play(FadeIn(q_label), run_time=0.3)
        self.play(Create(stripe), run_time=0.7)
        self.wait(dur - 1.65)

# ── M02 — single whole dot on screen ──────────────────────────────────────────
class M02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("M02", 5.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        # striped curve faint
        def intensity(y):
            k, ds = 3.0, abs(slit_y_top - slit_y_bot) / 2
            return (np.cos(k * ds * y / (screen_x - bar_x))) ** 2
        ys     = np.linspace(-2.5, 2.5, 160)
        stripe = VMobject(color=BLUE, stroke_width=1.5, stroke_opacity=0.3).set_points_smoothly(
            [np.array([screen_x + 0.3 * intensity(y), y, 0]) for y in ys]
        )
        self.add(stripe)

        q_label = ink_txt('"where are you?"', size=25, slant=ITALIC).to_edge(UP, buff=0.4)

        # single electron flies, lands as whole dot with flash
        e     = Dot(radius=0.12, color=BLUE).move_to(gun.get_right())
        mid   = np.array([bar_x, slit_y_top, 0])
        land  = np.array([screen_x, slit_y_top * 0.5, 0])
        path  = VMobject().set_points_as_corners([e.get_center(), mid, land])
        path.make_smooth()
        dot   = Dot(radius=0.1, color=INK).move_to(land)
        flash = Flash(land, color=BLUE, flash_radius=0.25, line_stroke_width=2, num_lines=8)

        self.play(FadeIn(q_label), run_time=0.3)
        self.play(MoveAlongPath(e, path), run_time=0.6)
        self.play(FadeOut(e), GrowFromCenter(dot, scale_factor=0.5), run_time=0.2)
        self.play(flash, run_time=0.35)
        self.wait(dur - 1.45)

# ── S01 — "secret route" fails, heaps struck ──────────────────────────────────
class S01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("S01", 5.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        # striped curve (to contrast)
        def intensity(y):
            k, ds = 3.0, abs(slit_y_top - slit_y_bot) / 2
            return (np.cos(k * ds * y / (screen_x - bar_x))) ** 2
        ys     = np.linspace(-2.5, 2.5, 160)
        stripe = VMobject(color=BLUE, stroke_width=1.5, stroke_opacity=0.3).set_points_smoothly(
            [np.array([screen_x + 0.3 * intensity(y), y, 0]) for y in ys]
        )
        self.add(stripe)

        # dashed brown two-heap curve
        heap_ys = [slit_y_top, slit_y_bot]
        heap_pts = []
        for y in ys:
            val = sum(np.exp(-((y - cy) ** 2) / 0.2) for cy in heap_ys)
            heap_pts.append(np.array([screen_x + 0.28 * val, y, 0]))
        heap_curve = DashedVMobject(
            VMobject(color=BROWN, stroke_width=2.0).set_points_smoothly(heap_pts),
            num_dashes=20
        )
        label = brown_txt('"secret route"', size=25, slant=ITALIC).to_edge(UP, buff=0.4)

        self.play(FadeIn(label), Create(heap_curve), run_time=0.55)

        # strike through heap curve
        strike = Line(heap_curve.get_left() + LEFT * 0.1, heap_curve.get_right() + RIGHT * 0.1,
                      color=INK, stroke_width=2.5)
        self.play(Create(strike), run_time=0.35)
        self.play(
            heap_curve.animate.set_opacity(0.2),
            label.animate.set_opacity(0.2),
            strike.animate.set_opacity(0.2),
            run_time=0.4
        )
        self.wait(dur - 1.3)

# ── S02 — "smeared stuff" fails, half-dot struck ─────────────────────────────
class S02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("S02", 4.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        label = ink_txt('"smeared stuff"', size=25, slant=ITALIC).to_edge(UP, buff=0.4)

        # half-dot glyph near screen — a semicircle representing half an electron
        half_dot = Arc(radius=0.18, start_angle=PI / 2, angle=PI, color=BLUE,
                       fill_color=BLUE, fill_opacity=0.7, stroke_width=0)
        half_dot.move_to([screen_x, 0, 0])

        self.play(FadeIn(label), FadeIn(half_dot), run_time=0.4)

        # strike it
        strike = Line(half_dot.get_center() + LEFT * 0.35, half_dot.get_center() + RIGHT * 0.35,
                      color=INK, stroke_width=2.5)
        self.play(Create(strike), run_time=0.3)
        self.play(
            FadeOut(label), FadeOut(half_dot), FadeOut(strike),
            run_time=0.5
        )
        self.wait(dur - 1.2)

# ── A01 — wave packet glides through lab ──────────────────────────────────────
class A01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("A01", 5.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        label = ink_txt("one object — a wave of possibility", size=26).to_edge(DOWN, buff=0.5)

        # wave packet: gaussian envelope × cosine
        def make_packet(cx):
            pts = []
            for x in np.linspace(cx - 1.0, cx + 1.0, 80):
                envelope = np.exp(-((x - cx) ** 2) / 0.18)
                y = 0.4 * envelope * np.cos(7.0 * (x - cx))
                pts.append(np.array([x, y, 0]))
            vm = VMobject(color=BLUE, stroke_width=2.0)
            vm.set_points_smoothly(pts)
            return vm

        packet = make_packet(gun.get_right()[0] + 0.2)
        self.add(packet)
        self.play(Write(label), run_time=0.45)
        # glide toward slits
        self.play(packet.animate.shift(RIGHT * (bar_x - packet.get_center()[0] - 0.3)),
                  run_time=0.9)
        self.wait(dur - 1.35)

# ── A02 — |ψ|² top strip ──────────────────────────────────────────────────────
class A02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("A02", 5.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        # dot fringe pattern faint
        rng = np.random.default_rng(7)
        bright_ys = [0, 0.9, -0.9, 1.8, -1.8]
        dots = VGroup(*[
            Dot(radius=0.05, color=INK, fill_opacity=0.5).move_to(
                [screen_x + rng.normal(0, 0.05), rng.choice(bright_ys) + rng.normal(0, 0.18), 0]
            )
            for _ in range(55)
        ])
        self.add(dots)

        eq = MathTex(r"|\psi|^2", color=BLUE, font_size=72)
        eq.to_edge(UP, buff=0.35)
        brighter_note = ink_txt("brighter wave → likelier dot", size=25, color=DIM).next_to(eq, DOWN, buff=0.2)

        self.play(Write(eq), run_time=0.7)
        self.play(FadeIn(brighter_note, shift=DOWN * 0.1), run_time=0.4)
        self.wait(dur - 1.1)

# ── A03 — packet → dot, definition line ──────────────────────────────────────
class A03(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("A03", 5.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        eq = MathTex(r"|\psi|^2", color=BLUE, font_size=64).to_edge(UP, buff=0.35)
        self.add(eq)

        def make_packet(cx):
            pts = []
            for x in np.linspace(cx - 0.8, cx + 0.8, 70):
                envelope = np.exp(-((x - cx) ** 2) / 0.12)
                y = 0.35 * envelope * np.cos(7.0 * (x - cx))
                pts.append(np.array([x, y, 0]))
            vm = VMobject(color=BLUE, stroke_width=1.8)
            vm.set_points_smoothly(pts)
            return vm

        packet = make_packet(gun.get_right()[0] + 0.2)
        self.add(packet)

        landing = np.array([screen_x, 0, 0])

        # glide to screen
        self.play(packet.animate.shift(RIGHT * (screen_x - packet.get_center()[0] - 0.5)),
                  run_time=0.65)

        # packet → dot
        dot   = Dot(radius=0.12, color=INK).move_to(landing)
        flash = Flash(landing, color=BLUE, flash_radius=0.22, line_stroke_width=2, num_lines=8)
        self.play(FadeOut(packet), GrowFromCenter(dot, scale_factor=0.5), run_time=0.25)
        self.play(flash, run_time=0.3)

        # top strip: |ψ|² → definition line
        def_line = ink_txt("wave-shaped possibilities · particle-shaped results", size=22)
        def_line.to_edge(UP, buff=0.42)
        self.play(Transform(eq, def_line), run_time=0.55)
        self.wait(dur - 1.75)

# ── P01 — small replay + indicate definition ─────────────────────────────────
class P01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("P01", 5.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        def_line = ink_txt("wave-shaped possibilities · particle-shaped results", size=22)
        def_line.to_edge(UP, buff=0.42)
        self.add(def_line)

        def make_packet(cx, scale=0.7):
            pts = []
            for x in np.linspace(cx - 0.6 * scale, cx + 0.6 * scale, 60):
                envelope = np.exp(-((x - cx) ** 2) / (0.1 * scale))
                y = 0.28 * scale * envelope * np.cos(7.0 / scale * (x - cx))
                pts.append(np.array([x, y, 0]))
            vm = VMobject(color=BLUE, stroke_width=1.6)
            vm.set_points_smoothly(pts)
            return vm

        # small packet replay
        packet = make_packet(gun.get_right()[0] + 0.1, scale=0.65)
        self.add(packet)
        landing = np.array([screen_x, 0, 0])

        self.play(packet.animate.shift(RIGHT * (screen_x - packet.get_center()[0] - 0.35)),
                  run_time=0.65)
        dot   = Dot(radius=0.1, color=INK).move_to(landing)
        flash = Flash(landing, color=BLUE, flash_radius=0.18, line_stroke_width=1.8, num_lines=8)
        self.play(FadeOut(packet), GrowFromCenter(dot, scale_factor=0.5), run_time=0.2)
        self.play(flash, run_time=0.28)

        # indicate definition line
        rect = SurroundingRectangle(def_line, color=YELLOW, stroke_width=1.5, buff=0.08)
        self.play(Create(rect), run_time=0.4)
        self.play(FadeOut(rect), run_time=0.4)
        self.wait(dur - 1.93)

# ── OUTRO ─────────────────────────────────────────────────────────────────────
class OUTRO(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("OUTRO", 6.0)

        gun, barrier, bar_x, slit_y_top, slit_y_bot, screen, screen_x = make_compact_lab()
        self.add(gun, barrier, screen)

        # top strip clears → title parks
        title_card = ink_txt("What Wave–Particle Duality Actually Means", size=27)
        title_card.to_edge(UP, buff=0.38).set_opacity(0.70)
        self.play(FadeIn(title_card), run_time=0.5)
        self.wait(dur - 0.5)
