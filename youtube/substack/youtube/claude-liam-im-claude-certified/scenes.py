from manim import *

config.background_color = "#FFFFFF"

class STD_B01_claude_liam_im_claude_cer(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-im-claude-certified.
    Narration: 'Three certificates. All at anthropic.skilljar.com — sign up free, no Claude subs'
    Duration: 24.1s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "anthropic.skilljar.com"
        body_lines = ["Claude 101 \u2192 1 hour. Chat, Cowork, Code,", "Projects, Skills, Connectors.", "AI Fluency: Framework & Foundations \u2192 3 hours.", "Best of the three. Start here.", "Introduction to Claude Cowork \u2192 2 hours. The best", "Claude feature, end to end."]
        spark_str = "Three certs, six hours, free."

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
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.88)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B05_claude_liam_im_claude_cer(Scene):
    """SHOW-DONT-TELL retrofit for B05 in claude-liam-im-claude-certified.
    Narration: "Stanford's 2025 AI Index: seventy-eight percent of organizations used AI in 2024"
    Duration: 22.6s  Lines: 7  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "The numbers behind the signal"
        body_lines = ["78% of orgs used AI in 2024. Up from 55% a year", "earlier.", "AI-skilled workers earn 56% wage premium on", "average (PwC 2025).", "Less than 2% of the world has tried Claude Pro.", "Certificate = proof you started before most", "people did."]
        spark_str = "56% wage premium signal."

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
