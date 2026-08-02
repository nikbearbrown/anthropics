from manim import *

config.background_color = "#FFFFFF"

class STD_B05_hai_who_was_albert_einste(Scene):
    """SHOW-DONT-TELL retrofit for B05 in hai-who-was-albert-einstein.
    Narration: 'The 1905 papers and 1915 general relativity are direct engineering dependencies '
    Duration: 29.2s  Lines: 10  font_sz: 20
    """
    def construct(self):
        config.background_color = "#F3EBDD"
        INK = "#2F2A26"
        ACC = "#E4572E"

        heading_str = "Direct engineering dependencies"
        body_lines = ["Photoelectric effect \u2192 photovoltaics, photodetectors,", "digital cameras", "Brownian motion \u2192 statistical mechanics tools, confirmation", "of atomic theory", "Special relativity \u2192 GPS timing corrections (38 \u03bcs/day", "without correction)", "E = mc\u00b2 \u2192 nuclear fission/fusion energy calculations", "General relativity (1915) \u2192 gravitational lensing, black", "holes, cosmology", "EPR (1935) \u2192 Bell tests \u2192 quantum cryptography protocols"]
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

        reveal_t = max(0.30, 2.84)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
