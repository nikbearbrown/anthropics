from manim import *
import numpy as np

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "Helvetica"
config.background_color = BG


class Scene_B02_NbbWriterReviewer(Scene):
    """B02 — SUBAGENT-MECHANICS: main session -> isolated subagent -> summary."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("SUBAGENT-MECHANICS", font_size=36, color=INK, font=FONT)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        labels = ["Main session", "Subagent", "Summary"]
        n = len(labels)
        spacing = 3.9
        start_x = -(n - 1) * spacing / 2

        boxes = []
        for i, lbl in enumerate(labels):
            box = Rectangle(width=3.6, height=2.0,
                            color=INK, stroke_width=5,
                            fill_color=BG, fill_opacity=1)
            box.move_to(np.array([start_x + i * spacing, 0.4, 0]))
            txt = Text(lbl, font_size=40, color=INK, font=FONT)
            txt.move_to(box)
            grp = VGroup(box, txt)
            boxes.append(grp)

        for i, grp in enumerate(boxes):
            self.play(FadeIn(grp), run_time=0.5)
            if i < len(boxes) - 1:
                arr = Arrow(boxes[i].get_right(), boxes[i + 1].get_left(),
                            buff=0.2, color=TERRA, stroke_width=10,
                            max_tip_length_to_length_ratio=0.35,
                            max_stroke_width_to_length_ratio=8)
                self.play(GrowArrow(arr), run_time=0.3)

        caption = Text("OWN CONTEXT — MAIN SESSION STAYS CLEAN",
                       font_size=32, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=1.0)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 15.0))


class Scene_B03_NbbWriterReviewer(Scene):
    """B03 — WHAT-IT-CATCHES: three categories the cold reviewer surfaces."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("WHAT-IT-CATCHES", font_size=36, color=INK, font=FONT)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        labels = ["Assumptions", "Edge cases", "Off-by-one"]
        colors = [INK, INK, TERRA]

        n = len(labels)
        spacing = 4.0
        start_x = -(n - 1) * spacing / 2

        groups = []
        for i, (lbl, col) in enumerate(zip(labels, colors)):
            box = Rectangle(width=3.7, height=2.0,
                            color=col, stroke_width=5,
                            fill_color=BG, fill_opacity=1)
            box.move_to(np.array([start_x + i * spacing, 0.4, 0]))
            txt = Text(lbl, font_size=36, color=INK, font=FONT)
            txt.move_to(box)
            grp = VGroup(box, txt)
            groups.append(grp)
            self.play(FadeIn(grp), run_time=0.45)

        caption = Text("INVISIBLE TO THE WRITER — VISIBLE ON A COLD READ",
                       font_size=32, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=1.0)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 18.0))
