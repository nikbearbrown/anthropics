from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B03_ClaudeLiamResearch(Scene):
    """B03 — scale: a tall 'a day' bar collapses to a short 'an hour' bar."""
    def construct(self):
        self.camera.background_color = BG
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 10, 5],
                  x_length=7, y_length=4.5,
                  axis_config={"color": INK, "stroke_width": 2},
                  y_axis_config={"include_numbers": False},
                  tips=False)
        ax.shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt_day  = ax.c2p(1, 9)
        pt_hour = ax.c2p(2, 1)
        bar_w = 0.7

        bar_day = Rectangle(
            width=bar_w,
            height=abs(pt_day[1] - origin[1]),
            color=INK, fill_color=INK, fill_opacity=0.85, stroke_width=0)
        bar_day.move_to([pt_day[0], (pt_day[1] + origin[1]) / 2, 0])

        lbl_day = Text("a day", font_size=28, color=INK, font=FONT)
        lbl_day.next_to(ax.c2p(1, 0), DOWN, buff=0.15)

        self.play(GrowFromEdge(bar_day, DOWN), Write(lbl_day), run_time=0.7)
        self.wait(0.3)

        bar_hour = Rectangle(
            width=bar_w,
            height=abs(pt_hour[1] - origin[1]),
            color=TERRA, fill_color=TERRA, fill_opacity=0.9, stroke_width=0)
        bar_hour.move_to([pt_hour[0], (pt_hour[1] + origin[1]) / 2, 0])

        lbl_hour = Text("an hour", font_size=28, color=TERRA, font=FONT)
        lbl_hour.next_to(ax.c2p(2, 0), DOWN, buff=0.15)

        caption = Text("The bottleneck was never your intelligence — it was your time.",
                       font_size=22, color=INK, font=FONT)
        caption.to_edge(UP, buff=0.35)

        self.play(GrowFromEdge(bar_hour, DOWN), Write(lbl_hour), run_time=0.7)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 13.8))


class Scene_B05_ClaudeLiamResearch(Scene):
    """Beat B05 — SHOW: bar/proportion chart. Narration: The difference that matters: it doesn\'t tell you what each source says, one by o"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT II":
            act = Text("ACT II", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("The difference that matters: it doesn\'t tell you what each s"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("It tells you what they mean together"[:30] if "It tells you what they mean together" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "A pile of separate accounts becomes one picture - the throug":
            note = Text("A pile of separate accounts becomes one picture - the throug"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.80))


class Scene_B09_ClaudeLiamResearch(Scene):
    """B09 — positioning map: dots drop onto 2D axes, empty quadrant pulses terracotta."""
    def construct(self):
        self.camera.background_color = BG
        ax = Axes(x_range=[0, 10, 5], y_range=[0, 10, 5],
                  x_length=6, y_length=5,
                  axis_config={"color": INK, "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.2)

        x_lbl = Text("price", font_size=26, color=INK, font=FONT)
        x_lbl.next_to(ax.c2p(10, 0), RIGHT, buff=0.1)
        y_lbl = Text("focus", font_size=26, color=INK, font=FONT)
        y_lbl.next_to(ax.c2p(0, 10), UP, buff=0.1)

        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=0.5)

        dots_data = [(3, 3), (3.8, 3.5), (2.5, 4), (7, 7), (6.5, 6), (5, 5)]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), radius=0.15, color=INK, fill_opacity=0.85)
            for x, y in dots_data])

        self.play(AnimationGroup(*[FadeIn(d, shift=DOWN*0.3) for d in dots],
                                  lag_ratio=0.15), run_time=0.8)

        empty_corner = ax.c2p(7.5, 2.5)
        ring = Circle(radius=0.9, color=TERRA, stroke_width=4, fill_opacity=0).move_to(empty_corner)
        label = Text("gap", font_size=24, color=TERRA, font=FONT).move_to(empty_corner)

        self.play(Create(ring), Write(label), run_time=0.6)
        self.play(ring.animate.set_stroke(opacity=0.4), run_time=0.4)
        self.play(ring.animate.set_stroke(opacity=1.0), run_time=0.4)

        caption = Text("That empty quadrant is often the whole point.", font_size=24, color=INK, font=FONT)
        caption.to_edge(UP, buff=0.35)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 9.5))


class Scene_B11_ClaudeLiamResearch(Scene):
    """B11 — coverage grid: cells fill in, one region stays empty and gets ringed."""
    def construct(self):
        self.camera.background_color = BG
        rows, cols = 4, 5
        cell_w, cell_h = 1.2, 0.9
        grid = VGroup()
        cells = {}

        for r in range(rows):
            for c in range(cols):
                rect = Rectangle(width=cell_w - 0.05, height=cell_h - 0.05,
                                  color=INK, stroke_width=1.5,
                                  fill_color=BG, fill_opacity=1)
                rect.move_to([(c - cols/2 + 0.5) * cell_w,
                               (rows/2 - r - 0.5) * cell_h, 0])
                rect.shift(DOWN * 0.3)
                grid.add(rect)
                cells[(r, c)] = rect

        self.play(Create(grid), run_time=0.5)

        gap_cells = {(2, 3), (2, 4), (3, 3), (3, 4)}
        fill_order = [(r, c) for r in range(rows) for c in range(cols)
                      if (r, c) not in gap_cells]

        anims = [cells[(r, c)].animate.set_fill(color=INK, opacity=0.7)
                 for r, c in fill_order]
        self.play(AnimationGroup(*anims, lag_ratio=0.06), run_time=1.0)

        gap_center = cells[(2, 3)].get_center() / 2 + cells[(3, 4)].get_center() / 2 + DOWN * 0.15
        gap_rect = SurroundingRectangle(
            VGroup(*[cells[k] for k in gap_cells]),
            color=TERRA, stroke_width=4, buff=0.05)
        gap_lbl = Text("gap", font_size=26, color=TERRA, font=FONT)
        gap_lbl.next_to(gap_rect, RIGHT, buff=0.15)

        self.play(Create(gap_rect), Write(gap_lbl), run_time=0.6)
        caption = Text("You see the hole before it costs you.", font_size=24, color=INK, font=FONT)
        caption.to_edge(UP, buff=0.35)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 11.5))


class Scene_B15_ClaudeLiamResearch(Scene):
    """B15 — divergence: generic ask → fog vs purpose-tagged ask → sharp target."""
    def construct(self):
        self.camera.background_color = BG
        center = ORIGIN + DOWN * 0.2

        generic_lbl = Text("Generic ask", font_size=28, color=INK, font=FONT)
        generic_lbl.to_edge(LEFT, buff=1.2).shift(UP * 1.5)

        purpose_lbl = Text("Purpose-tagged ask", font_size=28, color=TERRA, font=FONT)
        purpose_lbl.to_edge(LEFT, buff=1.2).shift(DOWN * 1.5)

        self.play(Write(generic_lbl), Write(purpose_lbl), run_time=0.5)

        fog_lines = VGroup(*[
            Line(generic_lbl.get_right() + RIGHT * 0.15,
                 generic_lbl.get_right() + RIGHT * 0.15 + RIGHT * 2 + UP * (i - 1) * 0.4,
                 color=INK, stroke_width=2, stroke_opacity=0.35)
            for i in range(5)])
        fog_txt = Text("broad overview", font_size=24, color=INK, font=FONT)
        fog_txt.next_to(fog_lines, RIGHT, buff=0.2)

        self.play(Create(fog_lines), Write(fog_txt), run_time=0.6)

        arrow = Arrow(purpose_lbl.get_right() + RIGHT * 0.1,
                      purpose_lbl.get_right() + RIGHT * 2.5,
                      color=TERRA, stroke_width=4)
        target = Circle(radius=0.35, color=TERRA, stroke_width=3,
                        fill_color=TERRA, fill_opacity=0.3)
        target.next_to(arrow, RIGHT, buff=0.1)
        target_lbl = Text("usable\nintelligence", font_size=22, color=TERRA, font=FONT)
        target_lbl.next_to(target, RIGHT, buff=0.15)

        self.play(GrowArrow(arrow), Create(target), Write(target_lbl), run_time=0.6)
        caption = Text("The purpose shapes the answer.", font_size=24, color=INK, font=FONT)
        caption.to_edge(UP, buff=0.35)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 13.0))


class Scene_B17_ClaudeLiamResearch(Scene):
    """B17 — comparison: two option columns fill with pros/cons, balance beam settles."""
    def construct(self):
        self.camera.background_color = BG
        col_a_x = -3.2
        col_b_x = 3.2

        hdr_a = Text("Free trial", font_size=30, color=INK, font=FONT)
        hdr_a.move_to([col_a_x, 2.8, 0])
        hdr_b = Text("Freemium", font_size=30, color=TERRA, font=FONT)
        hdr_b.move_to([col_b_x, 2.8, 0])

        divider = Line(UP * 3, DOWN * 3, color=INK, stroke_width=1.5, stroke_opacity=0.3)

        self.play(Write(hdr_a), Write(hdr_b), Create(divider), run_time=0.5)

        pros_a = ["Higher intent conversion", "Clear upgrade moment", "Easier to explain"]
        cons_a = ["Short evaluation window", "Support cost upfront"]
        pros_b = ["Larger top of funnel", "Viral growth potential", "Always-on presence"]
        cons_b = ["Hard to convert free users", "Feature gating is costly"]

        y_start = 1.9
        step = 0.55
        for i, txt in enumerate(pros_a):
            t = Text("+ " + txt, font_size=20, color=INK, font=FONT)
            t.move_to([col_a_x, y_start - i * step, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.2)
        for i, txt in enumerate(cons_a):
            t = Text("- " + txt, font_size=20, color=INK, font=FONT, slant=ITALIC)
            t.move_to([col_a_x, y_start - (len(pros_a) + i) * step, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.2)

        for i, txt in enumerate(pros_b):
            t = Text("+ " + txt, font_size=20, color=TERRA, font=FONT)
            t.move_to([col_b_x, y_start - i * step, 0])
            self.play(FadeIn(t, shift=LEFT * 0.2), run_time=0.2)
        for i, txt in enumerate(cons_b):
            t = Text("- " + txt, font_size=20, color=TERRA, font=FONT, slant=ITALIC)
            t.move_to([col_b_x, y_start - (len(pros_b) + i) * step, 0])
            self.play(FadeIn(t, shift=LEFT * 0.2), run_time=0.2)

        beam = Line(LEFT * 2, RIGHT * 2, color=INK, stroke_width=3).shift(DOWN * 2.9)
        pivot = Dot(beam.get_center(), radius=0.1, color=INK)
        self.play(Create(beam), FadeIn(pivot), run_time=0.3)
        caption = Text("Deciding on a comparison, not a gut feeling.", font_size=22, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.15)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 10.0))


class Scene_B19_ClaudeLiamResearch(Scene):
    """B19 — contradiction-highlight: conflicting data points lit and ringed terracotta."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Sources", font_size=30, color=INK, font=FONT)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.4)

        claims = [
            ("Source A", "Market growing 18% YoY"),
            ("Source B", "Market growing 7% YoY"),
            ("Source C", "Market mature, consolidating"),
            ("Source D", "Three dominant players"),
            ("Source E", "No clear leader yet"),
        ]

        boxes = VGroup()
        for i, (src, claim) in enumerate(claims):
            src_t = Text(src + ":", font_size=22, color=INK, font=FONT, weight=BOLD)
            claim_t = Text(claim, font_size=22, color=INK, font=FONT)
            row = VGroup(src_t, claim_t).arrange(RIGHT, buff=0.25)
            row.move_to([0, 1.6 - i * 0.75, 0])
            boxes.add(row)

        self.play(AnimationGroup(*[FadeIn(b, shift=RIGHT * 0.15) for b in boxes],
                                  lag_ratio=0.1), run_time=0.8)

        conflict_idx = [0, 1, 3, 4]
        rings = VGroup()
        for idx in conflict_idx:
            r = SurroundingRectangle(boxes[idx], color=TERRA, stroke_width=3.5, buff=0.08)
            rings.add(r)

        self.play(AnimationGroup(*[Create(r) for r in rings], lag_ratio=0.12), run_time=0.6)
        caption = Text("Disagreement is a map of where the real uncertainty lives.",
                       font_size=22, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=0.4)
        self.wait(max(0.01, 11.5))
