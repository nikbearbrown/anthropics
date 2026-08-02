from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbAiPolicy(Scene):
    """Beat B01 — SHOW: pipeline / handoff flow. Narration: Most AI use policies are written at the institution level but enforced at the as"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        # Act label at top
        if "PROBLEM":
            act = Text("PROBLEM", font_size=24, color="#2A1A0E", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Most AI use policies are written at the institution level bu", "A blanket \'no AI\' policy applied to an assignment that shoul", ""] if t]
        if not labels_text:
            labels_text = ["Input", "Process", "Output"]

        n = len(labels_text)
        spacing = 8.0 / n
        start_x = -(n - 1) * spacing / 2

        boxes = VGroup()
        arrows = VGroup()
        box_mobs = []
        for i, lbl in enumerate(labels_text):
            box = RoundedRectangle(width=spacing * 0.85, height=1.6,
                                   color="#2A1A0E", stroke_width=2,
                                   fill_color="#FFFFFF", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#2A1A0E", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#C8102E", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B04_NbbAiPolicy(Scene):
    """Beat B04 — SHOW: pipeline / handoff flow. Narration: The classification appears. A debugging assignment designed to build debugging s"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        # Act label at top
        if "OUTPUT":
            act = Text("OUTPUT", font_size=24, color="#2A1A0E", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["The classification appears", "A debugging assignment designed to build debugging skill: Pr", "A literature review with AI-sourced summaries: Permitted wit"] if t]
        if not labels_text:
            labels_text = ["Input", "Process", "Output"]

        n = len(labels_text)
        spacing = 8.0 / n
        start_x = -(n - 1) * spacing / 2

        boxes = VGroup()
        arrows = VGroup()
        box_mobs = []
        for i, lbl in enumerate(labels_text):
            box = RoundedRectangle(width=spacing * 0.85, height=1.6,
                                   color="#2A1A0E", stroke_width=2,
                                   fill_color="#FFFFFF", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#2A1A0E", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#C8102E", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 12.00))


class Scene_B06_NbbAiPolicy(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: The redesigned assignment is still about debugging — but now the student must us"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "OUTPUT":
            act = Text("OUTPUT", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The redesigned assignment is still about debugging - but now":
            line1 = Text("The redesigned assignment is still about debugging - but now", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The policy statement changes from \'AI use is prohibited\' to ":
            line2 = Text("The policy statement changes from \'AI use is prohibited\' to ", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "\' The same skill - debugging - now includes the meta-skill o":
            line3 = Text("\' The same skill - debugging - now includes the meta-skill o", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The redesigned assignment is still about debugging - but now":
            uline = Line(LEFT * min(4.0, len("The redesigned assignment is still about debugging - but now") * 0.18), RIGHT * min(4.0, len("The redesigned assignment is still about debugging - but now") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B07_NbbAiPolicy(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: Policy mode is a design choice, not just a rule. The same topic can legitimately"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "SUMMARY":
            act = Text("SUMMARY", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Policy mode is a design choice, not just a rule":
            line1 = Text("Policy mode is a design choice, not just a rule", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The same topic can legitimately sit in any of the four quadr":
            line2 = Text("The same topic can legitimately sit in any of the four quadr", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The classifier makes the design decision explicit - and give":
            line3 = Text("The classifier makes the design decision explicit - and give", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Policy mode is a design choice, not just a rule":
            uline = Line(LEFT * min(4.0, len("Policy mode is a design choice, not just a rule") * 0.18), RIGHT * min(4.0, len("Policy mode is a design choice, not just a rule") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B08_NbbAiPolicy(Scene):
    """Beat B08 — SHOW: two-column comparison. Narration: Next: Research What Makes AI Feedback Effective — an evidence review comparing A"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "NEXT STEPS":
            act = Text("NEXT STEPS", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Left column
        left_box = RoundedRectangle(width=5.5, height=3.5, color="#2A1A0E", stroke_width=2,
                                     fill_color="#FFFFFF", fill_opacity=1).shift(LEFT * 3.2)
        left_text = Text("Next: Research What Makes AI Feedback Effective - an evidenc"[:50], font_size=22, color="#2A1A0E", font=font)
        left_text.scale(min(1.0, 5.0 / max(0.1, left_text.width)))
        left_text.move_to(left_box)

        # Right column
        right_box = RoundedRectangle(width=5.5, height=3.5, color="#C8102E", stroke_width=2,
                                      fill_color="#FFFFFF", fill_opacity=1).shift(RIGHT * 3.2)
        right_text = Text("human feedback across writing, mathematics, and programming"[:50] if "human feedback across writing, mathematics, and programming" else "Result", font_size=22, color="#2A1A0E", font=font)
        right_text.scale(min(1.0, 5.0 / max(0.1, right_text.width)))
        right_text.move_to(right_box)

        # Divider
        divider = Line(UP * 2, DOWN * 2, color="#2A1A0E", stroke_width=1.5)

        self.play(FadeIn(left_box), FadeIn(right_box), Create(divider), run_time=0.5)
        self.play(Write(left_text), Write(right_text), run_time=0.8)

        if "":
            note = Text(""[:60], font_size=20, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.3)
            self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.01, 4.00))
