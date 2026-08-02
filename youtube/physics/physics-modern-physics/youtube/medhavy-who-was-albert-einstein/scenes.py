from manim import *

config.background_color = "#FFFFFF"

class STD_B06_medhavy_who_was_albert_ei(Scene):
    """SHOW-DONT-TELL retrofit for B06 in medhavy-who-was-albert-einstein.
    Narration: 'From five papers in one year, an entire century of physics unfolds. Atomic theor'
    Duration: 26.7s  Lines: 9  font_sz: 20
    """
    def construct(self):
        config.background_color = "#F0EAD6"
        INK = "#000000"
        ACC = "#009E73"

        heading_str = "What Einstein's papers made possible"
        body_lines = ["March 1905 \u2014 Photoelectric effect: light is quantized (Nobel", "Prize 1921)", "May 1905 \u2014 Brownian motion: atoms are real and measurable", "June 1905 \u2014 Special relativity: c is constant; space and", "time are relative", "September 1905 \u2014 E = mc\u00b2: mass-energy equivalence", "1915 \u2014 General relativity: gravity is curved spacetime", "1935 \u2014 EPR paradox: Einstein's challenge to quantum", "completeness"]
        spark_str = ""

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
            lobj = Text(txt, font="EB Garamond", color=col, font_size=20)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.88)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
