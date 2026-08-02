from manim import *

config.background_color = "#FFFFFF"

class STD_B01_claude_roadmap(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-roadmap.
    Narration: 'Here is a practical reading order — seven guides, each with a time estimate so y'
    Duration: 27.9s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Reading order + time estimates"
        body_lines = ["#1 Claude For Dummies \u2014 5 min. Never tried", "Claude? Start here.", "#2 Claude basics \u2014 9-10 min. What Claude can", "actually do.", "#3 Claude Cowork \u2014 20 min. Multiagent work for", "non-coders.", "#4-7: Skills (15 min), Voice training, Free", "certification, Anti-AI writing."]
        spark_str = "Seven guides. One week."

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.39)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_roadmap(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-roadmap.
    Narration: 'Why are twenty-one guides outdated? Because Claude itself keeps shipping. A guid'
    Duration: 25.7s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "The update cycle problem"
        body_lines = ["Claude ships new models every few months. Guides", "written for 4.6 are wrong on 4.7.", "Cowork's interface changed \u2014 the folder setup", "that worked in January breaks in March.", "Even the most-shared procedural guides can become", "obsolete.", "The Claude 101 syllabus = the seven that are", "still accurate as of today."]
        spark_str = "Twenty million views. Now outdated."

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.12)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B04_claude_roadmap(Scene):
    """SHOW-DONT-TELL retrofit for B04 in claude-roadmap.
    Narration: 'The practical next step is simple. Save the guide. Block twenty minutes this wee'
    Duration: 25.5s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "What to do next"
        body_lines = ["Save the guide. Don't read all seven right now \u2014", "pick one this week.", "Block 20 minutes. Calendar it. Otherwise it", "doesn't happen.", "Start with #1 (Claude For Dummies) if you've", "never run a Claude session.", "Start with #3 (Cowork) if you already know the", "basics."]
        spark_str = "One guide. Twenty minutes."

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.08)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B05_claude_roadmap(Scene):
    """SHOW-DONT-TELL retrofit for B05 in claude-roadmap.
    Narration: "Here's the honest verdict on This seven-guide syllabus. It's genuinely useful — "
    Duration: 27.2s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "How to use this syllabus"
        body_lines = ["Ages well: Cowork concepts, Skills logic, voice", "training, anti-AI writing.", "Ages fast: anything with UI screenshots or model-", "selector steps.", "Rule: conceptual guides last. Setup guides go", "stale with every Claude release.", "Treat the list as orientation \u2014 not gospel.", "Update your mental model as Claude ships."]
        spark_str = "Concepts last. UI guides decay."

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.30)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
