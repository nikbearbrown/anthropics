from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbCoworkTask(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: One wrong folder permission and a Cowork session reads three years of personnel """
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "PROBLEM":
            act = Text("PROBLEM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "One wrong folder permission and a Cowork session reads three":
            line1 = Text("One wrong folder permission and a Cowork session reads three", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The task packet audit catches it in sixty seconds":
            line2 = Text("The task packet audit catches it in sixty seconds", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Without it, you have handed a capable agent a vague mandate ":
            line3 = Text("Without it, you have handed a capable agent a vague mandate ", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "One wrong folder permission and a Cowork session reads three":
            uline = Line(LEFT * min(4.0, len("One wrong folder permission and a Cowork session reads three") * 0.18), RIGHT * min(4.0, len("One wrong folder permission and a Cowork session reads three") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B04_NbbCoworkTask(Scene):
    """Beat B04 — SHOW: pipeline / handoff flow. Narration: Run it on the book\'s bad task packet: full Documents folder, no forbidden action"""
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
        labels_text = [t for t in ["Run it on the book\'s bad task packet: full Documents folder,", "Six fails appear in sequence - inputs not named, forbidden n", ""] if t]
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


class Scene_B06_NbbCoworkTask(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: Bad packet: seven fails. Good packet: seven passes. The seventh dimension catche"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "OUTPUT — revised":
            act = Text("OUTPUT — revised", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Bad packet: seven fails":
            line1 = Text("Bad packet: seven fails", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Good packet: seven passes":
            line2 = Text("Good packet: seven passes", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The seventh dimension catches the opening-scene failure mode":
            line3 = Text("The seventh dimension catches the opening-scene failure mode", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Bad packet: seven fails":
            uline = Line(LEFT * min(4.0, len("Bad packet: seven fails") * 0.18), RIGHT * min(4.0, len("Bad packet: seven fails") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B07_NbbCoworkTask(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: The task packet is not bureaucracy — it is the specification that makes supervis"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "TEARDOWN":
            act = Text("TEARDOWN", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The task packet is not bureaucracy - it is the specification":
            line1 = Text("The task packet is not bureaucracy - it is the specification", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Without it, you have handed a capable agent a vague mandate ":
            line2 = Text("Without it, you have handed a capable agent a vague mandate ", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The audit makes that gap visible before the session begins":
            line3 = Text("The audit makes that gap visible before the session begins", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The task packet is not bureaucracy - it is the specification":
            uline = Line(LEFT * min(4.0, len("The task packet is not bureaucracy - it is the specification") * 0.18), RIGHT * min(4.0, len("The task packet is not bureaucracy - it is the specification") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B08_NbbCoworkTask(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: Your move: write your next Cowork task as a plain-text packet and run it through"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "NEXT STEPS":
            act = Text("NEXT STEPS", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Your move: write your next Cowork task as a plain-text packe":
            line1 = Text("Your move: write your next Cowork task as a plain-text packe", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Next reel: the risk-tiered verification checklist - reading ":
            line2 = Text("Next reel: the risk-tiered verification checklist - reading ", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Your move: write your next Cowork task as a plain-text packe":
            uline = Line(LEFT * min(4.0, len("Your move: write your next Cowork task as a plain-text packe") * 0.18), RIGHT * min(4.0, len("Your move: write your next Cowork task as a plain-text packe") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 4.00))
