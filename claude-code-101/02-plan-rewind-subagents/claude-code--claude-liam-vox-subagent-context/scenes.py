from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class B01_ClaudeLiamVox(Scene):
    """Beat B01 — SHOW: bar/proportion chart. Narration: This is Liam, in for Bear. The grading-tool session has been running for an hour"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
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

        lbl1 = Text("This is Liam, in for Bear"[:30], font_size=40, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("The grading-tool session has been running for an hour"[:30] if "The grading-tool session has been running for an hour" else "Comparison", font_size=40, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Thirty percent context used":
            note = Text("Thirty percent context used"[:60], font_size=40, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 7.00))


class B02_ClaudeLiamVox(Scene):
    """Beat B02 — build 30% + research reads 48% = 78% used."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("Context window used", font_size=44, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.2)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 30)
        pt2 = ax.c2p(2, 78)
        bar_w = 0.6

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        val1 = Text("30%", font_size=32, color="#3D3929", font=font)
        val1.next_to(bar1, UP, buff=0.1)
        val2 = Text("78%", font_size=32, color="#3D3929", font=font)
        val2.next_to(bar2, UP, buff=0.1)

        lbl1 = Text("Build", font_size=32, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl2 = Text("+ Research", font_size=32, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), Write(val1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), Write(val2), run_time=0.6)

        note = Text("Only 22% remains — barely one student's feedback.",
                    font_size=30, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.00))


class B03_ClaudeLiamVox(Scene):
    """Beat B03 — SHOW: bar/proportion chart. Narration: Here is the question. Adding a research task to a productive session should exte"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
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

        lbl1 = Text("Here is the question"[:30], font_size=40, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Adding a research task to a productive session should extend"[:30] if "Adding a research task to a productive session should extend" else "Comparison", font_size=40, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Here is the session where a ten-minute research task left on":
            note = Text("Here is the session where a ten-minute research task left on"[:60], font_size=40, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 7.00))


class B04_ClaudeLiamVox(Scene):
    """Beat B04 — one shared window; research reads pile up alongside build."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("One window, no unread", font_size=44, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title), run_time=0.3)

        # Single stacked bar: build + accumulating research reads
        col_x = 0.0
        col_w = 1.6
        col_bottom = -2.4
        col_top = 2.4
        col_h = col_top - col_bottom

        frame = Rectangle(width=col_w, height=col_h,
                          color="#3D3929", fill_opacity=0, stroke_width=2)
        frame.move_to([col_x, (col_top + col_bottom) / 2, 0])
        self.play(Create(frame), run_time=0.3)

        # Build layer (30%)
        build_h = col_h * 0.30
        build_seg = Rectangle(width=col_w, height=build_h,
                              color="#3D3929", fill_color="#3D3929",
                              fill_opacity=0.85, stroke_width=0)
        build_seg.move_to([col_x, col_bottom + build_h / 2, 0])
        build_lbl = Text("Build 30%", font_size=28, color="#F2F0E9", font=font)
        build_lbl.move_to(build_seg.get_center())
        self.play(GrowFromEdge(build_seg, DOWN), FadeIn(build_lbl), run_time=0.5)

        # Research reads pile on
        reads = [
            ("Policy doc", 0.12),
            ("LMS export", 0.12),
            ("Meeting notes", 0.10),
            ("Syllabus", 0.14),
        ]
        y = col_bottom + build_h
        for name, frac in reads:
            h = col_h * frac
            seg = Rectangle(width=col_w, height=h,
                            color="#D97757", fill_color="#D97757",
                            fill_opacity=0.85, stroke_width=0)
            seg.move_to([col_x, y + h / 2, 0])
            tag = Text(name, font_size=22, color="#F2F0E9", font=font)
            tag.move_to(seg.get_center())
            self.play(GrowFromEdge(seg, DOWN), FadeIn(tag), run_time=0.35)
            y += h

        note = Text("The window does not grow — build and research share the same space.",
                    font_size=28, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.00))


class B05_ClaudeLiamVox(Scene):
    """Beat B05 — subagent has its own window; main session receives only a summary."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("Subagent isolation", font_size=44, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.3)

        # Two boxes: subagent context (left), main session context (right)
        box_w, box_h = 3.4, 3.2
        sub_box = Rectangle(width=box_w, height=box_h,
                            color="#3D3929", fill_opacity=0, stroke_width=2)
        sub_box.move_to([-3.2, -0.1, 0])
        main_box = Rectangle(width=box_w, height=box_h,
                             color="#3D3929", fill_opacity=0, stroke_width=2)
        main_box.move_to([3.2, -0.1, 0])
        self.play(Create(sub_box), Create(main_box), run_time=0.4)

        sub_lbl = Text("Subagent context", font_size=26, color="#3D3929", font=font)
        sub_lbl.next_to(sub_box, UP, buff=0.15)
        main_lbl = Text("Main session", font_size=26, color="#3D3929", font=font)
        main_lbl.next_to(main_box, UP, buff=0.15)
        self.play(FadeIn(sub_lbl), FadeIn(main_lbl), run_time=0.3)

        # Subagent fills with crimson reads
        reads = ["Policy doc", "LMS export", "Meeting notes", "Syllabus"]
        y = -1.6
        for name in reads:
            fill = Rectangle(width=box_w - 0.2, height=0.55,
                             color="#D97757", fill_color="#D97757",
                             fill_opacity=0.85, stroke_width=0)
            fill.move_to([-3.2, y, 0])
            tag = Text(name, font_size=20, color="#F2F0E9", font=font)
            tag.move_to(fill.get_center())
            self.play(FadeIn(fill), FadeIn(tag), run_time=0.3)
            y += 0.6

        # Arrow: summary crosses to main session
        arrow = Arrow(start=[-1.4, -0.1, 0], end=[1.4, -0.1, 0],
                      color="#3D3929", buff=0.05, stroke_width=4)
        arr_lbl = Text("summary — ~300 words", font_size=22, color="#3D3929", font=font)
        arr_lbl.next_to(arrow, UP, buff=0.1)
        self.play(Create(arrow), FadeIn(arr_lbl), run_time=0.5)

        # Main session gets a small teal bar
        summary = Rectangle(width=box_w - 0.2, height=0.35,
                            color="#1F6F5C", fill_color="#1F6F5C",
                            fill_opacity=0.85, stroke_width=0)
        summary.move_to([3.2, -1.32, 0])
        stag = Text("summary", font_size=20, color="#F2F0E9", font=font)
        stag.move_to(summary.get_center())
        self.play(FadeIn(summary), FadeIn(stag), run_time=0.4)

        note = Text("Main session grows by the summary, not by every file the subagent read.",
                    font_size=26, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.35)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.00))


class B06_ClaudeLiamVox(Scene):
    """Beat B06 — the side-by-side: 78% used vs 32% used."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("Context used at the same point in the build",
                     font_size=40, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 78)
        pt2 = ax.c2p(2, 32)
        bar_w = 0.6

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        val1 = Text("78%", font_size=32, color="#3D3929", font=font)
        val1.next_to(bar1, UP, buff=0.1)
        val2 = Text("32%", font_size=32, color="#3D3929", font=font)
        val2.next_to(bar2, UP, buff=0.1)

        lbl1 = Text("Without", font_size=30, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl2 = Text("With subagent", font_size=30, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), Write(val1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), Write(val2), run_time=0.6)

        note = Text("Same build, same research — 46 points of context reclaimed.",
                    font_size=30, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.00))


class B08_ClaudeLiamVox(Scene):
    """Beat B08 — heuristic: task reads more than main session needs to see."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("The heuristic", font_size=44, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 80)
        pt2 = ax.c2p(2, 15)
        bar_w = 0.6

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        val1 = Text("many docs", font_size=28, color="#3D3929", font=font)
        val1.next_to(bar1, UP, buff=0.1)
        val2 = Text("one summary", font_size=28, color="#3D3929", font=font)
        val2.next_to(bar2, UP, buff=0.1)

        lbl1 = Text("Task reads", font_size=30, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl2 = Text("Session needs", font_size=30, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), Write(val1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), Write(val2), run_time=0.6)

        note = Text("Reads much more than the main session needs to see — subagent task.",
                    font_size=28, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.00))


class B09_ClaudeLiamVox(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: Research fills context. The subagent takes the fill. The main session keeps the """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Research fills context":
            line1 = Text("Research fills context", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The subagent takes the fill":
            line2 = Text("The subagent takes the fill", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The main session keeps the build":
            line3 = Text("The main session keeps the build", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Research fills context":
            uline = Line(LEFT * min(4.0, len("Research fills context") * 0.18), RIGHT * min(4.0, len("Research fills context") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))
