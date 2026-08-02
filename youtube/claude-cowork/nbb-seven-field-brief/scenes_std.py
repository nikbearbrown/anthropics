from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbSevenField(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: Marcus\'s brief said \'summarize Q3 reports into a board document.\' No year range."""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE-CRASH":
            act = Text("THE-CRASH", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Marcus\'s brief said \'summarize Q3 reports into a board docum":
            line1 = Text("Marcus\'s brief said \'summarize Q3 reports into a board docum", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "\' No year range":
            line2 = Text("\' No year range", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "No specification of which financial data was in scope":
            line3 = Text("No specification of which financial data was in scope", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Marcus\'s brief said \'summarize Q3 reports into a board docum":
            uline = Line(LEFT * min(4.0, len("Marcus\'s brief said \'summarize Q3 reports into a board docum") * 0.18), RIGHT * min(4.0, len("Marcus\'s brief said \'summarize Q3 reports into a board docum") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 12.00))


class Scene_B02_NbbSevenField(Scene):
    """Beat B02 — SHOW: pipeline / handoff flow. Narration: Field one: the objective. One sentence naming the outcome, not the process. Not """
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        # Act label at top
        if "FIELD-OBJECTIVE":
            act = Text("FIELD-OBJECTIVE", font_size=24, color="#2A1A0E", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Field one: the objective", "One sentence naming the outcome, not the process", "Not \'summarize the reports\' - that describes the process"] if t]
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

        self.wait(max(0.01, 11.00))


class Scene_B03_NbbSevenField(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: Field five is the one most people skip: decision rules. What does Cowork do when"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "DECISION-RULES":
            act = Text("DECISION-RULES", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Field five is the one most people skip: decision rules":
            line1 = Text("Field five is the one most people skip: decision rules", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "What does Cowork do when two sources contradict each other? ":
            line2 = Text("What does Cowork do when two sources contradict each other? ", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Field five is the one most people skip: decision rules":
            uline = Line(LEFT * min(4.0, len("Field five is the one most people skip: decision rules") * 0.18), RIGHT * min(4.0, len("Field five is the one most people skip: decision rules") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B04_NbbSevenField(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: Field seven: stop conditions. What should Cowork do when a source is missing, a """
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "STOP-CONDITIONS":
            act = Text("STOP-CONDITIONS", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Field seven: stop conditions":
            line1 = Text("Field seven: stop conditions", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "What should Cowork do when a source is missing, a file is in":
            line2 = Text("What should Cowork do when a source is missing, a file is in", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Stop conditions are the brief\'s safety valve - the instructi":
            line3 = Text("Stop conditions are the brief\'s safety valve - the instructi", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Field seven: stop conditions":
            uline = Line(LEFT * min(4.0, len("Field seven: stop conditions") * 0.18), RIGHT * min(4.0, len("Field seven: stop conditions") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))
