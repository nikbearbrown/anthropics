"""scenes_std.py — GRAPHIC beats for claude-liam-vox-complexity-yield.

Newsprint palette (#F3EBDD ground / #2F2A26 ink / #1F6F5C teal / #BF3339 crimson / #F5D061 gold).
Scenes: B04_GateMultiply, B05_YieldCollapse, B06_MathCard,
        B07_OneVsSix, B09_ProgramAB, B10_DesignChoice

Render each scene:
  manim -qm --fps 24 scenes_std.py B04_GateMultiply
  mv media/videos/scenes_std/720p24/B04_GateMultiply.mp4 manim/B04.mp4
"""
import json
import pathlib

from manim import *

GROUND   = "#F3EBDD"
INK      = "#2F2A26"
TEAL     = "#1F6F5C"
CRIMSON  = "#BF3339"
GOLD     = "#F5D061"
SLATE    = "#3E5559"

DISPLAY = "Montserrat"
SERIF   = "EB Garamond"
MONO    = "PT Mono"

_SHEET = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
try:
    _data = json.load(open(_SHEET))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {}


def _bg(scene):
    scene.camera.background_color = GROUND


# ── B04  Six sequential gates, each at 90% ──────────────────────────────────
class B04_GateMultiply(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B04", 11.73)
        title = Text("Six gates. Every one must open.", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        gates = VGroup()
        labels = VGroup()
        pcts = VGroup()
        n = 6
        span = 10.0
        step = span / (n - 1)
        left = -span / 2
        for i in range(n):
            x = left + i * step
            bar = Rectangle(width=0.6, height=2.4)
            bar.set_fill(CRIMSON, 0.75).set_stroke(CRIMSON, 1.2)
            bar.move_to(RIGHT * x + DOWN * 0.2)
            # gate opening (narrow slit at center)
            slit = Rectangle(width=0.6, height=0.4).set_fill(GROUND, 1.0).set_stroke(width=0)
            slit.move_to(bar)
            gate = VGroup(bar, slit)
            lbl = Text(f"F{i+1}", font=MONO, font_size=16, color=INK)
            lbl.next_to(bar, DOWN, buff=0.2)
            pct = Text("90%", font=MONO, font_size=15, color=CRIMSON)
            pct.next_to(bar, UP, buff=0.15)
            gates.add(gate)
            labels.add(lbl)
            pcts.add(pct)
        pass_lbl = Text("PASS", font=DISPLAY, font_size=18, color=TEAL, weight=BOLD)
        pass_lbl.move_to(RIGHT * (left + span + 1.2) + DOWN * 0.2)
        self.play(Write(title), run_time=0.5)
        for i in range(n):
            self.play(FadeIn(gates[i]), FadeIn(labels[i]), FadeIn(pcts[i]),
                      run_time=0.35)
        self.play(FadeIn(pass_lbl), run_time=0.4)
        self.wait(max(0.3, total - 0.5 - n * 0.35 - 0.4))


# ── B05  Yield collapse bar chart — 90 81 73 66 59 53 ───────────────────────
class B05_YieldCollapse(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B05", 14.57)
        title = Text("Batch yield as functions stack", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        vals = [90, 81, 73, 66, 59, 53]
        labels_x = [f"F{i+1}" for i in range(6)]
        n = 6
        span = 10.0
        step = span / (n - 1)
        left = -span / 2
        max_h = 3.6
        # 90% reference line (teal)
        ref_y = (90 / 100.0) * max_h - 1.6
        ref = DashedLine(LEFT * (span / 2 + 0.6) + UP * ref_y,
                         RIGHT * (span / 2 + 0.6) + UP * ref_y,
                         color=TEAL, stroke_width=2.2, dash_length=0.15)
        ref_lbl = Text("90%", font=MONO, font_size=14, color=TEAL)
        ref_lbl.next_to(ref.get_end(), RIGHT, buff=0.2)
        bars = VGroup()
        pcts = VGroup()
        xlabs = VGroup()
        for i, v in enumerate(vals):
            x = left + i * step
            h = (v / 100.0) * max_h
            bar = Rectangle(width=0.8, height=h)
            bar.set_fill(CRIMSON, 0.85).set_stroke(CRIMSON, 1.2)
            bar.move_to(RIGHT * x + UP * (h / 2 - 1.6))
            pct = Text(f"{v}%", font=MONO, font_size=17, color=CRIMSON)
            pct.next_to(bar, UP, buff=0.15)
            xlab = Text(labels_x[i], font=MONO, font_size=15, color=INK)
            xlab.move_to(RIGHT * x + DOWN * 1.8)
            bars.add(bar)
            pcts.add(pct)
            xlabs.add(xlab)
        self.play(Write(title), run_time=0.5)
        self.play(Create(ref), FadeIn(ref_lbl), run_time=0.5)
        for i in range(n):
            self.play(FadeIn(bars[i]), FadeIn(pcts[i]), FadeIn(xlabs[i]),
                      run_time=0.5)
        self.wait(max(0.3, total - 1.0 - n * 0.5))


# ── B06  Math card 0.9^6 = 53% + 0.95^6 = 74% with gold highlight ───────────
class B06_MathCard(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B06", 13.87)
        eq1 = Text("0.9  ^  6  =  53%", font=MONO, font_size=64, color=INK)
        eq1.move_to(UP * 0.6)
        # Gold highlight bar under 53%
        gold = Rectangle(width=3.0, height=0.75).set_fill(GOLD, 0.6).set_stroke(width=0)
        # Roughly under the "53%" tail — right side of eq1
        gold.move_to(eq1.get_right() + LEFT * 1.35 + UP * 0.02)
        eq2 = Text("0.95  ^  6  =  74%", font=MONO, font_size=44, color=CRIMSON)
        eq2.move_to(DOWN * 1.5)
        note = Text("still one batch in four fails", font=SERIF, color=INK,
                    font_size=20, slant=ITALIC)
        note.move_to(DOWN * 2.7)
        title = Text("The arithmetic", font=DISPLAY, font_size=22, color=INK).move_to(UP * 3.0)
        self.play(Write(title), run_time=0.5)
        self.play(Write(eq1), run_time=1.2)
        self.play(FadeIn(gold), run_time=0.5)
        # bring gold behind eq1
        gold.set_z_index(-1)
        eq1.set_z_index(1)
        self.play(Write(eq2), run_time=1.0)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(max(0.3, total - 3.8))


# ── B07  One vs six — TEAL vs CRIMSON contrast ──────────────────────────────
class B07_OneVsSix(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B07", 13.95)
        title = Text("One function vs six — the translation contrast",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.0)
        # Left panel: single TEAL bar at 90%
        left_bar = Rectangle(width=1.0, height=3.24)
        left_bar.set_fill(TEAL, 0.85).set_stroke(TEAL, 1.2)
        left_bar.move_to(LEFT * 3.7 + UP * 0.0)
        left_pct = Text("90%", font=MONO, font_size=22, color=TEAL)
        left_pct.next_to(left_bar, UP, buff=0.15)
        left_lbl = Text("Doxil  |  1 function", font=DISPLAY, font_size=15,
                        color=TEAL, weight=BOLD)
        left_lbl.next_to(left_bar, DOWN, buff=0.35)
        left_note = Text("reached patients", font=SERIF, color=TEAL,
                         font_size=16, slant=ITALIC)
        left_note.next_to(left_lbl, DOWN, buff=0.15)
        # Right panel: six-bar collapse in crimson ending at 53%
        vals = [90, 81, 73, 66, 59, 53]
        bars = VGroup()
        max_h = 3.24
        n = 6
        rspan = 4.8
        rstep = rspan / (n - 1)
        rleft = 1.2
        for i, v in enumerate(vals):
            x = rleft + i * rstep
            h = (v / 100.0) * max_h
            bar = Rectangle(width=0.5, height=h)
            bar.set_fill(CRIMSON, 0.85).set_stroke(CRIMSON, 1.2)
            bar.move_to(RIGHT * x + UP * (h / 2 - 1.62))
            bars.add(bar)
        right_pct = Text("53%", font=MONO, font_size=22, color=CRIMSON)
        right_pct.next_to(bars[-1], UP, buff=0.15)
        right_lbl = Text("6-function theranostic", font=DISPLAY, font_size=15,
                         color=CRIMSON, weight=BOLD)
        right_lbl.move_to(RIGHT * (rleft + rspan / 2) + DOWN * 1.98)
        right_note = Text("did not translate", font=SERIF, color=CRIMSON,
                          font_size=16, slant=ITALIC)
        right_note.next_to(right_lbl, DOWN, buff=0.15)
        div = Line(UP * 2.6, DOWN * 2.6, color=INK, stroke_width=0.8)
        div.move_to(RIGHT * 0.4)
        self.play(Write(title), run_time=0.5)
        self.play(Create(div), run_time=0.3)
        self.play(FadeIn(left_bar), FadeIn(left_pct), run_time=0.5)
        self.play(FadeIn(left_lbl), FadeIn(left_note), run_time=0.4)
        for i in range(n):
            self.play(FadeIn(bars[i]), run_time=0.25)
        self.play(FadeIn(right_pct), FadeIn(right_lbl), FadeIn(right_note),
                  run_time=0.5)
        self.wait(max(0.3, total - 1.2 - 0.5 - 0.4 - n * 0.25 - 0.5))


# ── B09  Program A vs Program B batch grid ──────────────────────────────────
class B09_ProgramAB(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B09", 17.62)
        title = Text("Program A vs Program B — twelve batches each",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.0)
        # 4-column x 3-row grid of 12 batch squares per program
        def grid(center_x, pass_n, fail_n):
            g = VGroup()
            cell = 0.55
            gap = 0.11
            cols = 4
            rows = 3
            for i in range(12):
                r = i // cols
                c = i % cols
                x = center_x + (c - (cols - 1) / 2) * (cell + gap)
                y = 0.5 - (r - (rows - 1) / 2) * (cell + gap)
                sq = Square(cell)
                if i < pass_n:
                    sq.set_fill(TEAL, 0.85).set_stroke(TEAL, 1.0)
                else:
                    sq.set_fill(CRIMSON, 0.85).set_stroke(CRIMSON, 1.0)
                sq.move_to(RIGHT * x + UP * y)
                g.add(sq)
            return g
        A = grid(-3.5, pass_n=11, fail_n=1)
        B = grid(3.5, pass_n=7, fail_n=5)
        A_lbl = Text("Program A  |  1 function", font=DISPLAY, font_size=17,
                     color=INK, weight=BOLD)
        A_lbl.move_to(LEFT * 3.5 + UP * 2.1)
        A_sub = Text("11 pass  ·  1 fail", font=MONO, font_size=17, color=TEAL)
        A_sub.move_to(LEFT * 3.5 + DOWN * 1.9)
        B_lbl = Text("Program B  |  6 functions", font=DISPLAY, font_size=17,
                     color=INK, weight=BOLD)
        B_lbl.move_to(RIGHT * 3.5 + UP * 2.1)
        B_sub = Text("7 pass  ·  5 fail", font=MONO, font_size=17, color=CRIMSON)
        B_sub.move_to(RIGHT * 3.5 + DOWN * 1.9)
        div = Line(UP * 2.4, DOWN * 2.2, color=INK, stroke_width=0.8)
        self.play(Write(title), run_time=0.5)
        self.play(Create(div), run_time=0.3)
        self.play(FadeIn(A_lbl), FadeIn(B_lbl), run_time=0.4)
        self.play(AnimationGroup(*[GrowFromCenter(A[i]) for i in range(12)],
                                 lag_ratio=0.05), run_time=1.4)
        self.play(FadeIn(A_sub), run_time=0.4)
        self.play(AnimationGroup(*[GrowFromCenter(B[i]) for i in range(12)],
                                 lag_ratio=0.05), run_time=1.4)
        self.play(FadeIn(B_sub), run_time=0.4)
        self.wait(max(0.3, total - 4.8))


# ── B10  Design-choice annotation over the batch grid ───────────────────────
class B10_DesignChoice(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B10", 12.82)
        title = Text("Design choice, not manufacturing failure",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.0)
        def grid(center_x, pass_n, fail_n):
            g = VGroup()
            fails = VGroup()
            cell = 0.55
            gap = 0.11
            cols = 4
            rows = 3
            for i in range(12):
                r = i // cols
                c = i % cols
                x = center_x + (c - (cols - 1) / 2) * (cell + gap)
                y = 0.5 - (r - (rows - 1) / 2) * (cell + gap)
                sq = Square(cell)
                if i < pass_n:
                    sq.set_fill(TEAL, 0.85).set_stroke(TEAL, 1.0)
                else:
                    sq.set_fill(CRIMSON, 0.85).set_stroke(CRIMSON, 1.0)
                    fails.add(sq)
                sq.move_to(RIGHT * x + UP * y)
                g.add(sq)
            return g, fails
        A, _ = grid(-3.5, pass_n=11, fail_n=1)
        B, B_fails = grid(3.5, pass_n=7, fail_n=5)
        A_lbl = Text("Program A  |  1 function", font=DISPLAY, font_size=17,
                     color=INK, weight=BOLD)
        A_lbl.move_to(LEFT * 3.5 + UP * 2.1)
        B_lbl = Text("Program B  |  6 functions", font=DISPLAY, font_size=17,
                     color=INK, weight=BOLD)
        B_lbl.move_to(RIGHT * 3.5 + UP * 2.1)
        div = Line(UP * 2.4, DOWN * 2.2, color=INK, stroke_width=0.8)
        # HandRing: a hand-drawn-looking crimson ellipse around all 5 fail squares
        ring = Ellipse(width=2.1, height=1.35, color=CRIMSON, stroke_width=4)
        # Approximate center of the 5 crimson squares (positions 7-11)
        ring.move_to(RIGHT * 3.5 + DOWN * 0.35)
        annot = Text("design choice", font=SERIF, color=CRIMSON,
                     font_size=22, slant=ITALIC, weight=BOLD)
        annot.move_to(DOWN * 2.5)
        annot_arrow = Arrow(annot.get_top() + LEFT * 0.4,
                            ring.get_bottom() + LEFT * 0.2,
                            color=CRIMSON, stroke_width=1.5,
                            max_tip_length_to_length_ratio=0.06)
        self.play(Write(title), run_time=0.5)
        self.play(Create(div), FadeIn(A_lbl), FadeIn(B_lbl), run_time=0.5)
        self.play(FadeIn(A), FadeIn(B), run_time=0.8)
        self.play(Create(ring), run_time=0.9)
        self.play(FadeIn(annot), Create(annot_arrow), run_time=0.7)
        self.wait(max(0.3, total - 3.4))
