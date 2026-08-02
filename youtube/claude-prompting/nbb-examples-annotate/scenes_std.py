from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbExamplesAnnotate(Scene):
    """Beat B01 — SHOW: bar/proportion chart. Narration: When you provide an example, Claude observes the pattern and applies it to the n"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "WHAT-EXAMPLES-TEACH":
            act = Text("WHAT-EXAMPLES-TEACH", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#2A1A0E", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#2A1A0E", fill_color="#2A1A0E", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#C8102E", fill_color="#C8102E", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("When you provide an example, Claude observes the pattern and"[:30], font_size=20, color="#2A1A0E", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("An example teaches format, level, tone, reasoning pattern, l"[:30] if "An example teaches format, level, tone, reasoning pattern, l" else "Comparison", font_size=20, color="#2A1A0E", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "A research note teaches Claude to hedge like a researcher":
            note = Text("A research note teaches Claude to hedge like a researcher"[:60], font_size=22, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.00))


class Scene_B02_NbbExamplesAnnotate(Scene):
    """Beat B02 — SHOW: two-column comparison. Narration: An unannotated example is a complete specification. Claude cannot distinguish wh"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "UNANNOTATED-RISK":
            act = Text("UNANNOTATED-RISK", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Left column
        left_box = RoundedRectangle(width=5.5, height=3.5, color="#2A1A0E", stroke_width=2,
                                     fill_color="#FFFFFF", fill_opacity=1).shift(LEFT * 3.2)
        left_text = Text("An unannotated example is a complete specification"[:50], font_size=22, color="#2A1A0E", font=font)
        left_text.scale(min(1.0, 5.0 / max(0.1, left_text.width)))
        left_text.move_to(left_box)

        # Right column
        right_box = RoundedRectangle(width=5.5, height=3.5, color="#C8102E", stroke_width=2,
                                      fill_color="#FFFFFF", fill_opacity=1).shift(RIGHT * 3.2)
        right_text = Text("Claude cannot distinguish which features are intentional fro"[:50] if "Claude cannot distinguish which features are intentional fro" else "Result", font_size=22, color="#2A1A0E", font=font)
        right_text.scale(min(1.0, 5.0 / max(0.1, right_text.width)))
        right_text.move_to(right_box)

        # Divider
        divider = Line(UP * 2, DOWN * 2, color="#2A1A0E", stroke_width=1.5)

        self.play(FadeIn(left_box), FadeIn(right_box), Create(divider), run_time=0.5)
        self.play(Write(left_text), Write(right_text), run_time=0.8)

        if "If you paste a paragraph as an example of sentence rhythm an":
            note = Text("If you paste a paragraph as an example of sentence rhythm an"[:60], font_size=20, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.3)
            self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.01, 10.00))


class Scene_B03_NbbExamplesAnnotate(Scene):
    """Beat B03 — SHOW: bar/proportion chart. Narration: The annotation pattern names the features explicitly. \'The features to copy are:"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "ANNOTATION-PATTERN":
            act = Text("ANNOTATION-PATTERN", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#2A1A0E", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#2A1A0E", fill_color="#2A1A0E", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#C8102E", fill_color="#C8102E", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("The annotation pattern names the features explicitly"[:30], font_size=20, color="#2A1A0E", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("\'The features to copy are: short declarative sentences, past"[:30] if "\'The features to copy are: short declarative sentences, past" else "Comparison", font_size=20, color="#2A1A0E", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Do not copy the subject matter":
            note = Text("Do not copy the subject matter"[:60], font_size=22, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.00))
