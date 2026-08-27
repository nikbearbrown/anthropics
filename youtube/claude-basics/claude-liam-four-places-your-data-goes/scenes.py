"""
scenes.py — claude-liam-four-places-your-data-goes
"Three You Can Take Back. One You Can't."

B17: B17_WordsBecomePattern
  The three detail tokens dissolve into a probability distribution over
  next-tokens. Words break to glyphs, glyphs settle into a bar distribution
  that nudges by a hair. Reveal lands on the spoken word "pattern".

PALETTE: cream stage, warm ink, ONE terracotta bar only (the one that moves).
No colour shift, no darkening — depth is layout and weight only per VISUAL-GRAMMAR.md.
The arch-oneway accent rule holds here too: terracotta on the moving bar only.
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"   # terracotta — ONE bar only
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"
STAGE  = "#F2F0E9"

config.background_color = STAGE


class B17_WordsBecomePattern(Scene):
    """
    Words → glyphs → probability distribution nudging by a hair.
    Duration: ~11 seconds at 30fps = 330 frames.
    Reveal ("pattern") lands at roughly the 85% mark.

    Spec from beat_sheet.json B17:
      "The three detail tokens dissolve into a probability distribution over
       next-tokens. Words break to glyphs, glyphs settle into a bar
       distribution that nudges by a hair. No colour shift, no darkening —
       cream stage, warm ink, terracotta only on the single bar that moves.
       Reveal lands on the spoken word 'pattern'."
    """

    def construct(self):
        dur = 9.15  # actual audio duration (Kokoro am_onyx measured 2026-08-13)

        # ── Phase 1 (0–2.5s): three word chips appear ─────────────────────────
        words = ["partner", "hiking", "near Denver"]
        chips = VGroup(*[
            RoundedRectangle(
                corner_radius=0.15, width=2.4, height=0.7, fill_color=PAGE,
                fill_opacity=1, stroke_color=BORDER, stroke_width=2,
            )
            for _ in words
        ]).arrange(RIGHT, buff=0.5).move_to(UP * 1.8)

        labels = VGroup(*[
            Text(w, font_size=28, color=INK, font='EB Garamond')
            for w in words
        ])
        for lbl, chip in zip(labels, chips):
            lbl.move_to(chip.get_center())

        self.play(FadeIn(chips, lag_ratio=0.25, run_time=1.0))
        self.play(FadeIn(labels, lag_ratio=0.25, run_time=0.8))
        self.wait(0.4)

        # ── Phase 2 (2.5–5s): words dissolve to letter glyphs ────────────────
        glyph_clouds = VGroup()
        for chip, word in zip(chips, words):
            for k in range(len(word)):
                dot = Dot(
                    point=chip.get_center() + RIGHT * (k - len(word) / 2) * 0.20,
                    radius=0.05, color=INK, fill_opacity=0.5,
                )
                glyph_clouds.add(dot)

        self.play(
            FadeOut(labels, run_time=0.6),
            FadeOut(chips, run_time=0.6),
        )
        self.play(
            FadeIn(glyph_clouds, lag_ratio=0.04, run_time=1.2),
        )
        self.wait(0.3)

        # ── Phase 3 (5–8.5s): glyphs settle into bar distribution ───────────
        # Seven token buckets. Heights represent next-token probabilities.
        # The one bar that nudges is shown in SPARK (terracotta).
        bucket_labels = ["the", "a", "her", "his", "this", "that", "an"]
        # Heights scaled to fill the frame: max bar reaches ~2/3 of frame height
        bar_heights_before = [5.2, 4.0, 2.9, 2.5, 2.0, 1.4, 1.1]
        # After training: "her" ticks up noticeably (the "pattern" being learned)
        bar_heights_after  = [5.2, 4.0, 3.35, 2.5, 2.0, 1.4, 1.1]

        bar_w = 1.0
        bar_gap = 0.28
        n = len(bucket_labels)
        total_w = n * bar_w + (n - 1) * bar_gap
        x0 = -total_w / 2 + bar_w / 2
        baseline = 2.4  # base of all bars — keeps token labels inside ±3.4 safe y

        bars_before = VGroup()
        for i, (h, lbl) in enumerate(zip(bar_heights_before, bucket_labels)):
            xi = x0 + i * (bar_w + bar_gap)
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=INK, fill_opacity=0.42,
                stroke_color=INK, stroke_width=2.0,
            ).move_to(RIGHT * xi + DOWN * (baseline - h / 2))
            tok = Text(lbl, font_size=28, color=SOFT, font='EB Garamond').next_to(bar, DOWN, buff=0.18)
            bars_before.add(bar, tok)

        self.play(
            FadeOut(glyph_clouds, run_time=0.5),
            FadeIn(bars_before, lag_ratio=0.06, run_time=1.4),
        )
        self.wait(1.2)  # extended: holds bars so reveal hits on "pattern" (8.00s in audio)

        # ── Phase 4 (~6.9s): one bar nudges; caption appears on "pattern" ─
        # The terracotta bar is bar index 2 ("her") — the one that moves.
        # Only this bar gets the SPARK color; all others stay INK.
        moving_bar_idx = 2
        h_before = bar_heights_before[moving_bar_idx]
        h_after  = bar_heights_after[moving_bar_idx]
        xi_moving = x0 + moving_bar_idx * (bar_w + bar_gap)

        bar_spark = Rectangle(
            width=bar_w, height=h_after,
            fill_color=SPARK, fill_opacity=0.55,
            stroke_color=SPARK, stroke_width=2.0,
        ).move_to(RIGHT * xi_moving + DOWN * (baseline - h_after / 2))

        caption = Text("a pattern, not a record", font_size=40, color=INK, font='EB Garamond')
        caption.move_to(UP * 3.1)

        # Replace the moving bar with the terracotta version
        old_bar = bars_before[moving_bar_idx * 2]  # bar objects are bar,tok pairs

        self.play(
            Transform(old_bar, bar_spark, run_time=0.9),
            FadeIn(caption, run_time=0.6),
        )
        self.wait(1.1)   # hold after reveal; "pattern" spoken ~0.2s after transform completes

        # ── Hold ──────────────────────────────────────────────────────────────
        self.wait(0.25)
