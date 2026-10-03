from manim import *
import numpy as np

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B04_NbbPatternAnalysis(Scene):
    """B04 — pipeline: 3 submissions → isolated subagent → 3-field summary."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("OUTPUT", font_size=28, color=INK, font=FONT)
        act.to_edge(UP, buff=0.4)
        self.play(FadeIn(act), run_time=0.3)

        labels = ["3 submissions", "Read/Grep/Glob only", "3-field summary"]
        n = len(labels)
        spacing = 4.0
        start_x = -(n - 1) * spacing / 2

        boxes = []
        for i, lbl in enumerate(labels):
            box = RoundedRectangle(width=3.4, height=1.7,
                                   color=INK, stroke_width=3,
                                   fill_color=BG, fill_opacity=1,
                                   corner_radius=0.15)
            box.move_to(np.array([start_x + i * spacing, 0, 0]))
            txt = Text(lbl, font_size=32, color=INK, font=FONT)
            txt.move_to(box)
            grp = VGroup(box, txt)
            boxes.append(grp)

        for i, grp in enumerate(boxes):
            self.play(FadeIn(grp), run_time=0.5)
            if i < len(boxes) - 1:
                arr = Arrow(boxes[i].get_right(), boxes[i + 1].get_left(),
                            buff=0.15, color=TERRA, stroke_width=6,
                            max_tip_length_to_length_ratio=0.2)
                self.play(GrowArrow(arr), run_time=0.3)

        caption = Text("Main session context stays flat.",
                       font_size=28, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.01, 14.0))


class Scene_B06_NbbPatternAnalysis(Scene):
    """B06 — reviewer subagent: cycle with terracotta correction node."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("REVIEWER", font_size=28, color=INK, font=FONT)
        act.to_edge(UP, buff=0.4)
        self.play(FadeIn(act), run_time=0.3)

        labels = ["Analyzer", "Reviewer", "Correction"]
        colors = [INK, INK, TERRA]
        radius = 2.5
        nodes = []
        for i, lbl in enumerate(labels):
            angle = np.pi / 2 - 2 * np.pi * i / len(labels)
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            circle = Circle(radius=0.9, color=colors[i], stroke_width=3,
                            fill_color=BG, fill_opacity=1)
            circle.move_to(pos)
            txt = Text(lbl, font_size=26, color=INK, font=FONT)
            txt.move_to(circle)
            grp = VGroup(circle, txt)
            nodes.append((grp, pos))
            self.play(FadeIn(grp), run_time=0.4)

        for i in range(len(labels)):
            start = nodes[i][1]
            end = nodes[(i + 1) % len(labels)][1]
            arr = CurvedArrow(start, end, color=TERRA, stroke_width=3,
                              angle=-np.pi / 6)
            self.play(Create(arr), run_time=0.3)

        caption = Text("Fresh context, different reading.",
                       font_size=28, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.01, 12.0))


class Scene_B07_NbbPatternAnalysis(Scene):
    """B07 — three-part concept card: whitelist, output format, isolation."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("SUMMARY", font_size=28, color=INK, font=FONT)
        act.to_edge(UP, buff=0.4)
        self.play(FadeIn(act), run_time=0.3)

        title = Text("A subagent is three things", font_size=44, color=INK, font=FONT)
        title.next_to(act, DOWN, buff=0.7)
        self.play(Write(title), run_time=0.5)

        items = ["Tool whitelist", "Structured output", "Isolation contract"]
        y0 = -0.2
        rows = VGroup()
        for i, item in enumerate(items):
            dot = Dot(radius=0.12, color=TERRA)
            txt = Text(item, font_size=38, color=INK, font=FONT)
            txt.next_to(dot, RIGHT, buff=0.4)
            row = VGroup(dot, txt)
            row.move_to(np.array([-2.2, y0 - i * 1.1, 0]), aligned_edge=LEFT)
            rows.add(row)

        for row in rows:
            self.play(FadeIn(row), run_time=0.4)

        self.wait(max(0.01, 10.0))


class Scene_B08_NbbPatternAnalysis(Scene):
    """B08 — next-up: three-file simulation."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("NEXT", font_size=28, color=INK, font=FONT)
        act.to_edge(UP, buff=0.4)
        self.play(FadeIn(act), run_time=0.3)

        line1 = Text("Three-file simulation.", font_size=52, color=INK, font=FONT)
        line1.move_to(ORIGIN + UP * 0.3)
        self.play(Write(line1), run_time=0.5)

        underline = Line(LEFT * 2.5, RIGHT * 2.5,
                         color=TERRA, stroke_width=4)
        underline.next_to(line1, DOWN, buff=0.25)
        self.play(Create(underline), run_time=0.3)

        self.wait(max(0.01, 4.0))
