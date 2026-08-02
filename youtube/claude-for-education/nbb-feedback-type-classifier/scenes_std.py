from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbFeedbackType(Scene):
    """Beat B01 — SHOW: cycle / feedback loop. Narration: Feedback from AI is abundant and fast — but most of it is the wrong type for lea"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "PROBLEM":
            act = Text("PROBLEM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        import numpy as np
        stages = [t for t in ["Feedback from AI is abundant and fast - but most of it is th", "The Hattie-Timperley model identifies three distinct compone", "Most AI feedback provides only one"] if t]
        if not stages:
            stages = ["Input", "Process", "Output"]
        n = len(stages)
        radius = 2.5
        colors = ["#2A1A0E", "#C8102E"] + ["#2A1A0E"] * 10

        nodes = []
        for i, lbl in enumerate(stages):
            angle = np.pi / 2 - 2 * np.pi * i / n
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            circle = Circle(radius=0.55, color=colors[i % 2], stroke_width=2.5,
                            fill_color="#FFFFFF", fill_opacity=1)
            circle.move_to(pos)
            txt = Text(lbl[:20], font_size=18, color="#2A1A0E", font=font)
            txt.scale(min(1.0, 0.9 / max(0.1, txt.width)))
            txt.move_to(circle)
            grp = VGroup(circle, txt)
            nodes.append((grp, pos))
            self.play(FadeIn(grp), run_time=0.4)

        # Draw curved arrows between nodes
        for i in range(n):
            start_pos = nodes[i][1]
            end_pos = nodes[(i + 1) % n][1]
            arr = CurvedArrow(start_pos, end_pos, color="#C8102E", stroke_width=2.5,
                              angle=-np.pi / 6)
            self.play(Create(arr), run_time=0.4)

        self.wait(max(0.01, 10.00))


class Scene_B04_NbbFeedbackType(Scene):
    """Beat B04 — SHOW: cycle / feedback loop. Narration: A feedback sample: \'Good work on your draft. Your argument is developing but nee"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "OUTPUT":
            act = Text("OUTPUT", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        import numpy as np
        stages = [t for t in ["A feedback sample: \'Good work on your draft", "Your argument is developing but needs more evidence", "\' Feed-up: zero - the goal is never stated"] if t]
        if not stages:
            stages = ["Input", "Process", "Output"]
        n = len(stages)
        radius = 2.5
        colors = ["#2A1A0E", "#C8102E"] + ["#2A1A0E"] * 10

        nodes = []
        for i, lbl in enumerate(stages):
            angle = np.pi / 2 - 2 * np.pi * i / n
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            circle = Circle(radius=0.55, color=colors[i % 2], stroke_width=2.5,
                            fill_color="#FFFFFF", fill_opacity=1)
            circle.move_to(pos)
            txt = Text(lbl[:20], font_size=18, color="#2A1A0E", font=font)
            txt.scale(min(1.0, 0.9 / max(0.1, txt.width)))
            txt.move_to(circle)
            grp = VGroup(circle, txt)
            nodes.append((grp, pos))
            self.play(FadeIn(grp), run_time=0.4)

        # Draw curved arrows between nodes
        for i in range(n):
            start_pos = nodes[i][1]
            end_pos = nodes[(i + 1) % n][1]
            arr = CurvedArrow(start_pos, end_pos, color="#C8102E", stroke_width=2.5,
                              angle=-np.pi / 6)
            self.play(Create(arr), run_time=0.4)

        self.wait(max(0.01, 12.00))


class Scene_B06_NbbFeedbackType(Scene):
    """Beat B06 — SHOW: cycle / feedback loop. Narration: Three feedback modes appear for the same student work. Diagnose-only fits expert"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "OUTPUT":
            act = Text("OUTPUT", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        import numpy as np
        stages = [t for t in ["Three feedback modes appear for the same student work", "Diagnose-only fits experts who can act on gap identification", "The coaching question fits intermediate students who need to"] if t]
        if not stages:
            stages = ["Input", "Process", "Output"]
        n = len(stages)
        radius = 2.5
        colors = ["#2A1A0E", "#C8102E"] + ["#2A1A0E"] * 10

        nodes = []
        for i, lbl in enumerate(stages):
            angle = np.pi / 2 - 2 * np.pi * i / n
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            circle = Circle(radius=0.55, color=colors[i % 2], stroke_width=2.5,
                            fill_color="#FFFFFF", fill_opacity=1)
            circle.move_to(pos)
            txt = Text(lbl[:20], font_size=18, color="#2A1A0E", font=font)
            txt.scale(min(1.0, 0.9 / max(0.1, txt.width)))
            txt.move_to(circle)
            grp = VGroup(circle, txt)
            nodes.append((grp, pos))
            self.play(FadeIn(grp), run_time=0.4)

        # Draw curved arrows between nodes
        for i in range(n):
            start_pos = nodes[i][1]
            end_pos = nodes[(i + 1) % n][1]
            arr = CurvedArrow(start_pos, end_pos, color="#C8102E", stroke_width=2.5,
                              angle=-np.pi / 6)
            self.play(Create(arr), run_time=0.4)

        self.wait(max(0.01, 8.00))


class Scene_B07_NbbFeedbackType(Scene):
    """Beat B07 — SHOW: bar/proportion chart. Narration: Feedback type mismatch is the most common reason AI feedback doesn\'t improve lea"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "SUMMARY":
            act = Text("SUMMARY", font_size=24, color="#2A1A0E", font=font)
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

        lbl1 = Text("Feedback type mismatch is the most common reason AI feedback"[:30], font_size=20, color="#2A1A0E", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("The classifier reveals which component is missing"[:30] if "The classifier reveals which component is missing" else "Comparison", font_size=20, color="#2A1A0E", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "The three-mode generation reveals how to fill it appropriate":
            note = Text("The three-mode generation reveals how to fill it appropriate"[:60], font_size=22, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.00))


class Scene_B08_NbbFeedbackType(Scene):
    """Beat B08 — SHOW: bar/proportion chart. Narration: Next: Build a Student AI Policy Classifier — map each assignment to a policy mod"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "NEXT STEPS":
            act = Text("NEXT STEPS", font_size=24, color="#2A1A0E", font=font)
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

        lbl1 = Text("Next: Build a Student AI Policy Classifier - map each assign"[:30], font_size=20, color="#2A1A0E", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text(""[:30] if "" else "Comparison", font_size=20, color="#2A1A0E", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "":
            note = Text(""[:60], font_size=22, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 4.00))
