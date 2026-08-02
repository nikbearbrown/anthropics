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

def gaussian_curve(x_arr, mu, sigma, amp=1.0):
    return amp * np.exp(-0.5 * ((x_arr - mu) / sigma) ** 2)


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("Position–Momentum\nUncertainty", size=54)
        title.move_to(ORIGIN)
        sub = terra_txt("Δx · Δp  ≥  ℏ/2", size=40)
        sub.next_to(title, DOWN, buff=0.7)
        bear = ink_txt("Bear's Notes · Quantum Mechanics", size=26)
        bear.next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(bear), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class H01_Pinning(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H01", 5.0)
        # Calipers / bracket trying to pin particle
        lbl = ink_txt("Trying to pin down\na tiny particle…", size=52)
        lbl.to_edge(LEFT, buff=1.0)
        # Draw bracket
        bracket_x = 2.0
        b_top = Line([bracket_x - 0.5, 1.5, 0], [bracket_x, 1.5, 0], color=INK, stroke_width=4)
        b_bot = Line([bracket_x - 0.5, -1.5, 0], [bracket_x, -1.5, 0], color=INK, stroke_width=4)
        b_vert = Line([bracket_x, 1.5, 0], [bracket_x, -1.5, 0], color=INK, stroke_width=4)
        b2_top = Line([bracket_x + 2.5, 1.5, 0], [bracket_x + 2.0, 1.5, 0], color=INK, stroke_width=4)
        b2_bot = Line([bracket_x + 2.5, -1.5, 0], [bracket_x + 2.0, -1.5, 0], color=INK, stroke_width=4)
        b2_vert = Line([bracket_x + 2.0, 1.5, 0], [bracket_x + 2.0, -1.5, 0], color=INK, stroke_width=4)
        # particle dot
        dot = Dot([bracket_x + 1.25, 0, 0], radius=0.18, color=TERRA)
        brackets = VGroup(b_top, b_bot, b_vert, b2_top, b2_bot, b2_vert)
        self.play(FadeIn(lbl), Create(brackets), run_time=0.8)
        self.play(FadeIn(dot), run_time=0.3)
        self.wait(max(0.1, dur - 1.1))


class H02_ShakingHead(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        lbl = ink_txt("The harder you squeeze x,\nthe more p escapes.", size=36)
        lbl.to_edge(LEFT, buff=1.0)
        # Arrow pointing away
        esc_arrow = Arrow([2.5, 0, 0], [5.5, 1.5, 0], color=INK, buff=0)
        esc_lbl = ink_txt("p?", size=36)
        esc_lbl.next_to(esc_arrow, RIGHT, buff=0.2)
        question = ink_txt("No! Δx·Δp ≥ h/2", size=42)
        question.move_to([0, -2.5, 0])
        self.play(FadeIn(lbl), run_time=0.6)
        self.play(Create(esc_arrow), FadeIn(esc_lbl), run_time=0.6)
        self.play(FadeIn(question), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class A01_TwoPanels(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        # Top panel: position
        top_panel = Rectangle(width=12, height=3.2, color=INK, stroke_width=2)
        top_panel.set_fill(CREAM, 1)
        top_panel.move_to([0, 1.8, 0])
        top_lbl = ink_txt("Position  Δx", size=28)
        top_lbl.move_to([-5.0, 1.8, 0])
        # Axis top
        ax_top = Arrow([-5.5, 1.8, 0], [5.5, 1.8, 0], color=INK, stroke_width=2, buff=0)
        x_lbl = ink_txt("x", size=26)
        x_lbl.next_to(ax_top, RIGHT, buff=0.15)
        # Bottom panel: momentum
        bot_panel = Rectangle(width=12, height=3.2, color=INK, stroke_width=2)
        bot_panel.set_fill(CREAM, 1)
        bot_panel.move_to([0, -1.8, 0])
        bot_lbl = ink_txt("Momentum  Δp", size=28)
        bot_lbl.move_to([-5.0, -1.8, 0])
        ax_bot = Arrow([-5.5, -1.8, 0], [5.5, -1.8, 0], color=INK, stroke_width=2, buff=0)
        p_lbl = ink_txt("p", size=26)
        p_lbl.next_to(ax_bot, RIGHT, buff=0.15)
        self.play(
            Create(top_panel), FadeIn(top_lbl),
            Create(bot_panel), FadeIn(bot_lbl),
            run_time=0.8
        )
        self.play(Create(ax_top), FadeIn(x_lbl), Create(ax_bot), FadeIn(p_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.3))


class A02_WideBumpNarrowPeak(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        xs = np.linspace(-5.5, 5.5, 300)
        # Top panel: wide position bump
        top_y = 1.8
        sig_x = 2.0
        ys_top = gaussian_curve(xs, 0, sig_x, amp=1.2)
        pts_top = [[x, top_y + y, 0] for x, y in zip(xs, ys_top)]
        curve_top = VMobject(color=TERRA, stroke_width=3)
        curve_top.set_points_smoothly(pts_top)
        axis_top = Line([-5.5, top_y, 0], [5.5, top_y, 0], color=INK, stroke_width=2)
        top_lbl = ink_txt("Δx  (wide)", size=26)
        top_lbl.move_to([-4.0, top_y + 1.4, 0])
        # Bottom panel: narrow momentum peak
        bot_y = -1.8
        sig_p = 0.4
        ys_bot = gaussian_curve(xs, 0, sig_p, amp=1.8)
        pts_bot = [[x, bot_y + y, 0] for x, y in zip(xs, ys_bot)]
        curve_bot = VMobject(color=INK, stroke_width=3)
        curve_bot.set_points_smoothly(pts_bot)
        axis_bot = Line([-5.5, bot_y, 0], [5.5, bot_y, 0], color=INK, stroke_width=2)
        bot_lbl = ink_txt("Δp  (sharp)", size=26)
        bot_lbl.move_to([-4.0, bot_y + 1.4, 0])
        sep = DashedLine([-5.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=1, dash_length=0.2)
        self.play(Create(axis_top), Create(axis_bot), Create(sep), run_time=0.4)
        self.play(Create(curve_top), FadeIn(top_lbl), run_time=0.6)
        self.play(Create(curve_bot), FadeIn(bot_lbl), run_time=0.6)
        self.wait(max(0.1, dur - 1.6))


class A03_PositionUncertain(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        xs = np.linspace(-5.5, 5.5, 300)
        top_y = 1.8
        sig_x = 2.0
        ys_top = gaussian_curve(xs, 0, sig_x, amp=1.2)
        pts_top = [[x, top_y + y, 0] for x, y in zip(xs, ys_top)]
        curve_top = VMobject(color=TERRA, stroke_width=4)
        curve_top.set_points_smoothly(pts_top)
        axis_top = Line([-5.5, top_y, 0], [5.5, top_y, 0], color=INK, stroke_width=2)
        # Bracket showing width
        brace_y = top_y - 0.2
        brace = Brace(Line([-sig_x * 2, brace_y, 0], [sig_x * 2, brace_y, 0]),
                      direction=DOWN, color=INK)
        dx_lbl = ink_txt("position uncertain", size=42)
        dx_lbl.next_to(brace, DOWN, buff=0.2)
        sep = DashedLine([-5.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=1, dash_length=0.2)
        bot_y = -1.8
        axis_bot = Line([-5.5, bot_y, 0], [5.5, bot_y, 0], color=INK, stroke_width=2)
        bot_lbl = ink_txt("Momentum →", size=38)
        bot_lbl.move_to([0, -2.3, 0])
        self.add(axis_top, axis_bot, sep, curve_top, bot_lbl)
        self.play(Create(brace), run_time=0.5)
        self.play(FadeIn(dx_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.9))


class A04_NarrowPosition(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        xs = np.linspace(-5.5, 5.5, 300)
        top_y = 1.8
        # Wide bump morphs to narrow spike
        sig_wide = 2.0
        sig_narrow = 0.25
        ys_wide = gaussian_curve(xs, 0, sig_wide, amp=1.2)
        ys_narrow = gaussian_curve(xs, 0, sig_narrow, amp=1.8)
        pts_wide = [[x, top_y + y, 0] for x, y in zip(xs, ys_wide)]
        pts_narrow = [[x, top_y + y, 0] for x, y in zip(xs, ys_narrow)]
        curve = VMobject(color=TERRA, stroke_width=4)
        curve.set_points_smoothly(pts_wide)
        axis_top = Line([-5.5, top_y, 0], [5.5, top_y, 0], color=INK, stroke_width=2)
        sep = DashedLine([-5.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=1, dash_length=0.2)
        lbl = terra_txt("squeeze position…", size=32)
        lbl.move_to([0, top_y + 2.3, 0])
        axis_bot = Line([-5.5, -1.8, 0], [5.5, -1.8, 0], color=INK, stroke_width=2)
        self.add(axis_top, axis_bot, sep, curve, lbl)
        target = VMobject(color=TERRA, stroke_width=4)
        target.set_points_smoothly(pts_narrow)
        self.play(Transform(curve, target), run_time=1.0)
        narrow_lbl = terra_txt("Δx small", size=28)
        narrow_lbl.move_to([1.5, top_y + 1.5, 0])
        self.play(FadeIn(narrow_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.4))


class A05_MomentumSpread(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        xs = np.linspace(-5.5, 5.5, 300)
        top_y = 1.8; bot_y = -1.8
        # Top: narrow position spike
        ys_top = gaussian_curve(xs, 0, 0.25, amp=1.8)
        pts_top = [[x, top_y + y, 0] for x, y in zip(xs, ys_top)]
        curve_top = VMobject(color=TERRA, stroke_width=3)
        curve_top.set_points_smoothly(pts_top)
        ax_top = Line([-5.5, top_y, 0], [5.5, top_y, 0], color=INK, stroke_width=2)
        # Bottom: wide momentum spread
        ys_bot_narrow = gaussian_curve(xs, 0, 0.5, amp=1.4)
        ys_bot_wide = gaussian_curve(xs, 0, 2.5, amp=0.55)
        pts_bot_n = [[x, bot_y + y, 0] for x, y in zip(xs, ys_bot_narrow)]
        pts_bot_w = [[x, bot_y + y, 0] for x, y in zip(xs, ys_bot_wide)]
        curve_bot = VMobject(color=INK, stroke_width=3)
        curve_bot.set_points_smoothly(pts_bot_n)
        ax_bot = Line([-5.5, bot_y, 0], [5.5, bot_y, 0], color=INK, stroke_width=2)
        sep = DashedLine([-5.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=1, dash_length=0.2)
        dx_lbl = ink_txt("Δx tiny", size=26)
        dx_lbl.move_to([-4.0, top_y + 1.5, 0])
        self.add(ax_top, ax_bot, sep, curve_top, dx_lbl, curve_bot)
        spread_lbl = terra_txt("Δp fans out!", size=32)
        spread_lbl.move_to([-3.5, bot_y + 1.0, 0])
        target_bot = VMobject(color=INK, stroke_width=3)
        target_bot.set_points_smoothly(pts_bot_w)
        self.play(Transform(curve_bot, target_bot), FadeIn(spread_lbl), run_time=1.2)
        self.wait(max(0.1, dur - 1.2))


class A06_InverseTrade(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        xs = np.linspace(-5.5, 5.5, 300)
        top_y = 1.8; bot_y = -1.8
        sig_x = 0.25; sig_p = 2.5
        ys_top = gaussian_curve(xs, 0, sig_x, amp=1.8)
        ys_bot = gaussian_curve(xs, 0, sig_p, amp=0.55)
        pts_top = [[x, top_y + y, 0] for x, y in zip(xs, ys_top)]
        pts_bot = [[x, bot_y + y, 0] for x, y in zip(xs, ys_bot)]
        curve_top = VMobject(color=TERRA, stroke_width=3)
        curve_top.set_points_smoothly(pts_top)
        curve_bot = VMobject(color=INK, stroke_width=3)
        curve_bot.set_points_smoothly(pts_bot)
        ax_top = Line([-5.5, top_y, 0], [5.5, top_y, 0], color=INK, stroke_width=2)
        ax_bot = Line([-5.5, bot_y, 0], [5.5, bot_y, 0], color=INK, stroke_width=2)
        sep = DashedLine([-5.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=1, dash_length=0.2)
        narrow_lbl = ink_txt("narrow Δx", size=26)
        narrow_lbl.move_to([-3.5, top_y + 1.3, 0])
        wide_lbl = ink_txt("wide Δp", size=26)
        wide_lbl.move_to([-3.5, bot_y + 0.8, 0])
        arrows = VGroup(
            Arrow([6.2, top_y + 0.5, 0], [6.2, bot_y + 0.5, 0], color=TERRA, buff=0)
        )
        trade_lbl = terra_txt("inverse\ntrade", size=26)
        trade_lbl.next_to(arrows, RIGHT, buff=0.2)
        self.add(ax_top, ax_bot, sep, curve_top, curve_bot, narrow_lbl, wide_lbl)
        self.play(Create(arrows), FadeIn(trade_lbl), run_time=0.7)
        self.wait(max(0.1, dur - 0.7))


class A07_Seesaw(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        # Seesaw visual
        pivot = Dot([0, -1.5, 0], radius=0.12, color=INK)
        beam = Line([-4.5, -1.0, 0], [4.5, -2.0, 0], color=INK, stroke_width=5)
        stand = Line([0, -1.5, 0], [0, -2.5, 0], color=INK, stroke_width=4)
        left_box = Rectangle(width=1.8, height=1.0, color=INK, stroke_width=3)
        left_box.set_fill(INK, 0.2)
        left_box.move_to([-4.0, -0.2, 0])
        left_lbl = ink_txt("Δx", size=44)
        left_lbl.move_to(left_box.get_center())
        right_box = Rectangle(width=1.8, height=1.0, color=INK, stroke_width=3)
        right_box.set_fill(INK, 0.2)
        right_box.move_to([4.0, -2.8, 0])
        right_lbl = ink_txt("Δp", size=44)
        right_lbl.move_to(right_box.get_center())
        label = ink_txt("Δx · Δp ≥ h/2\n(width × width is fixed)", size=42)
        label.move_to([0, 2.0, 0])
        self.play(Create(beam), Create(stand), FadeIn(pivot), run_time=0.5)
        self.play(FadeIn(left_box), FadeIn(left_lbl), FadeIn(right_box), FadeIn(right_lbl), run_time=0.5)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(max(0.1, dur - 1.5))


class A08_BakedIntoWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        xs = np.linspace(-6, 6, 400)
        # Wave packet
        envelope = np.exp(-0.5 * (xs / 1.5) ** 2)
        ripple = np.cos(3.5 * xs)
        ys = envelope * ripple * 1.5
        pts = [[x, y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        wave.move_to([0, 0.5, 0])
        self.add(wave)
        label = ink_txt("baked into the wave,\nbefore you look", size=42)
        label.move_to([0, -2.3, 0])
        underline = Line(label.get_left() + DOWN * 0.05,
                         label.get_right() + DOWN * 0.05,
                         color=TERRA, stroke_width=3)
        self.play(Write(label), run_time=0.9)
        self.play(Create(underline), run_time=0.3)
        self.wait(max(0.1, dur - 1.2))
