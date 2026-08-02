import json
from pathlib import Path
from manim import *

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 6.0
config.frame_height = 6.0 * 1920 / 1080  # ≈ 10.667

CREAM = "#FAF9F5"
DARK  = "#1a1a1a"
BLUE  = "#2A6FB0"
RED   = "#C0392B"
FONT  = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / "beat_sheet.json").read_text())
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 5)
           for b in _bs.get("beats", [])}
except Exception:
    DUR = {}

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=20, height=30).set_fill(CREAM, 1).set_stroke(width=0)

def ink(t, size=48, color=DARK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class A02(Scene):
    def construct(self):
        dur = d("A02", 4)
        self.camera.background_color = CREAM
        self.add(bg())

        label = ink("Red packets are weak;\nblue packets are strong.", 52, color=DARK).shift(UP * 3.5)

        r_bar = Rectangle(width=1.4, height=2.0, color=RED, stroke_width=3).set_fill(RED, 0.5).shift(LEFT * 1.0 + DOWN * 0.5)
        r_lbl = ink("red", 52, color=RED).next_to(r_bar, DOWN, buff=0.3)

        b_bar = Rectangle(width=1.4, height=4.2, color=BLUE, stroke_width=3).set_fill(BLUE, 0.5).shift(RIGHT * 1.0 + UP * 0.6)
        b_lbl = ink("blue", 52, color=BLUE).next_to(b_bar, DOWN, buff=0.3)

        y_lbl = ink("energy", 44, color=DARK).rotate(PI / 2).shift(LEFT * 2.6 + UP * 0.5)

        self.play(FadeIn(label), FadeIn(y_lbl), run_time=0.4)
        self.play(FadeIn(r_bar), FadeIn(r_lbl), run_time=0.5)
        self.play(FadeIn(b_bar), FadeIn(b_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.4))
