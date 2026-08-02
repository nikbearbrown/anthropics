from manim import *

config.background_color = "#FFFFFF"

class STD_B01_claude_liam_how_to_use_yo(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-how-to-use-your-personal-ai-at-work.
    Narration: "The Samsung case matters because it's public and it's damning. April 2023. Engin"
    Duration: 25.5s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "What happens when it goes wrong"
        body_lines = ["Engineers permitted to use ChatGPT \u2192 leaked", "source code 3 times in 20 days.", "Semiconductor code, defect code, internal meeting", "recording \u2014 all pasted in.", "Result: company-wide ChatGPT ban + disciplinary", "investigations.", "Personal AI = outside party. That's what the NDA", "you signed covers."]
        spark_str = "Samsung got burned fast."

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

class STD_B03_claude_liam_how_to_use_yo(Scene):
    """SHOW-DONT-TELL retrofit for B03 in claude-liam-how-to-use-your-personal-ai-at-work.
    Narration: 'For Claude: Settings → Privacy → turn off Help improve our AI models. For ChatGP'
    Duration: 29.6s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Where each toggle lives"
        body_lines = ["Claude: Settings \u2192 Privacy \u2192 'Help improve our AI", "models' \u2192 off.", "ChatGPT: Settings \u2192 Data controls \u2192 'Improve the", "model for everyone' \u2192 off.", "Grok: profile \u2192 settings \u2192 data controls \u2192 turn", "off everything.", "Gemini: myactivity.google.com \u2192 Gemini activity \u2192", "off (no shortcut)."]
        spark_str = "Four AIs, four toggles."

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

        reveal_t = max(0.30, 3.60)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B04_claude_liam_how_to_use_yo(Scene):
    """SHOW-DONT-TELL retrofit for B04 in claude-liam-how-to-use-your-personal-ai-at-work.
    Narration: "the not a lawyer — he's clear about that. But the cases are public. Pasting conf"
    Duration: 25.5s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Why it's a real risk"
        body_lines = ["NDA breach: AI company = outside party. Your", "contract likely covers this.", "Data protection violation: jurisdiction-", "dependent, but real exposure.", "IT security policy breach: even if no NDA clause,", "the policy likely does.", "None of these require malicious intent. A paste", "is enough."]
        spark_str = "Paste once, breach all three."

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

        reveal_t = max(0.30, 3.09)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
