from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_ClaudeLiamAi(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: A six-column log turns \'Claude helped\' into auditable evidence — and takes forty"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "PROBLEM":
            act = Text("PROBLEM", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A six-column log turns \'Claude helped\' into auditable eviden":
            line1 = Text("A six-column log turns \'Claude helped\' into auditable eviden", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Disclosure norms are evolving, but the verification column i":
            line2 = Text("Disclosure norms are evolving, but the verification column i", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A six-column log turns \'Claude helped\' into auditable eviden":
            uline = Line(LEFT * min(4.0, len("A six-column log turns \'Claude helped\' into auditable eviden") * 0.18), RIGHT * min(4.0, len("A six-column log turns \'Claude helped\' into auditable eviden") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B04_ClaudeLiamAi(Scene):
    """Beat B04 — SHOW: pipeline / handoff flow. Narration: Run it three times with realistic research-workflow entries. Each row appends cl"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Act label at top
        if "OUTPUT":
            act = Text("OUTPUT", font_size=24, color="#3D3929", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Run it three times with realistic research-workflow entries", "Each row appends cleanly", "The report flag prints a markdown table: date, tool, purpose"] if t]
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
                                   color="#3D3929", stroke_width=2,
                                   fill_color="#F2F0E9", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#3D3929", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#D97757", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 12.00))


class Scene_B06_ClaudeLiamAi(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: Run the summary. Three tools, six sessions, usage counts sorted descending. The """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "OUTPUT — revised":
            act = Text("OUTPUT — revised", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Run the summary":
            line1 = Text("Run the summary", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Three tools, six sessions, usage counts sorted descending":
            line2 = Text("Three tools, six sessions, usage counts sorted descending", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The tool you are over-relying on appears at the top":
            line3 = Text("The tool you are over-relying on appears at the top", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Run the summary":
            uline = Line(LEFT * min(4.0, len("Run the summary") * 0.18), RIGHT * min(4.0, len("Run the summary") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B07_ClaudeLiamAi(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: Disclosure norms are evolving but the verification column is the constant — it i"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "TEARDOWN":
            act = Text("TEARDOWN", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Disclosure norms are evolving but the verification column is":
            line1 = Text("Disclosure norms are evolving but the verification column is", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "A log without verification is an alibi, not a record":
            line2 = Text("A log without verification is an alibi, not a record", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Disclosure norms are evolving but the verification column is":
            uline = Line(LEFT * min(4.0, len("Disclosure norms are evolving but the verification column is") * 0.18), RIGHT * min(4.0, len("Disclosure norms are evolving but the verification column is") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B08_ClaudeLiamAi(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: Your move: start logging every Claude session today. Next reel: the Cowork task """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "NEXT STEPS":
            act = Text("NEXT STEPS", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Your move: start logging every Claude session today":
            line1 = Text("Your move: start logging every Claude session today", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Next reel: the Cowork task packet audit - one wrong permissi":
            line2 = Text("Next reel: the Cowork task packet audit - one wrong permissi", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Your move: start logging every Claude session today":
            uline = Line(LEFT * min(4.0, len("Your move: start logging every Claude session today") * 0.18), RIGHT * min(4.0, len("Your move: start logging every Claude session today") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 4.00))
