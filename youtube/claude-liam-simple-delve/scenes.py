"""scenes.py — Manim graphics for claude-liam-simple-delve
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
One terracotta accent per beat. No gradients, no glows, no shadows.
"delve" appears at S03, S08, S13 — identical face/weight/case every time.
THE ANCHOR (S03) returns identically at S13, with sentences added beneath.
THE REDRAW (S07) is reused in S08.

FILL LAW: every scene must fill ≥55% of the safe area with INK/TERRA marks.
Use poster-scale typography (font_size 64+ for headlines), full-width boxes.

Render all:
    python3 render_scenes.py

Render one:
    cd anthropics/youtube/claude-liam-simple-delve
    manim -qh --fps 24 -r 1920,1080 scenes.py S03Scene
"""
from manim import *
import numpy as np

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"

# Title-safe constants (Manim frame: 14.222 × 8.0 units)
SAFE_W  = 12.4   # usable width  (10% margins)
SAFE_H  = 6.6    # usable height (10% margins)
SAFE_X  = 0.0    # centred
SAFE_Y  = 0.0


# ── Shared helpers ────────────────────────────────────────────────────────────

def _delve(size=120):
    """'delve' in consistent typography — EB Garamond Bold lowercase INK.
    Size may vary by context but face/weight/case are always identical.
    """
    return Text("delve", font=SERIF, font_size=size, color=INK, weight=BOLD)


def _anchor_group():
    """THE ANCHOR composition. S03 and S13 call this identically.
    Returns (word, arrow, lbl_2022, lbl_2024).
    'delve' on upper-left; steep TERRA climbing arrow on right.
    """
    word = _delve(140)
    word.move_to(LEFT * 2.8 + UP * 1.2)

    p1 = np.array([ 0.5, -1.6, 0])
    p2 = np.array([ 5.5,  1.8, 0])
    arrow = Arrow(p1, p2, color=TERRA, stroke_width=7,
                  tip_length=0.28, buff=0)

    lbl_2022 = Text("2022", font=SANS, font_size=40, color=INK)
    lbl_2024 = Text("2024", font=SANS, font_size=40, color=INK)
    lbl_2022.move_to(p1 + DOWN * 0.55)
    lbl_2024.move_to(p2 + DOWN * 0.55 + RIGHT * 0.1)

    return word, arrow, lbl_2022, lbl_2024


def _popup(words, highlight_idx=None):
    """Candidate popup box. highlight_idx word in TERRA BOLD (matches anchor
    face/weight for 'delve' appearances per the reel's typography rule).
    """
    row_h = 0.70
    box_h = len(words) * row_h + 0.40
    bg = RoundedRectangle(corner_radius=0.18, width=3.4, height=box_h,
                           fill_color=GROUND, fill_opacity=1,
                           stroke_color=INK, stroke_width=2.5)
    items = VGroup()
    for i, w in enumerate(words):
        lbl = Text(w, font=SERIF, font_size=48,
                   color=TERRA if i == highlight_idx else INK,
                   weight=BOLD if i == highlight_idx else NORMAL)
        items.add(lbl)
    items.arrange(DOWN, buff=0.10)
    items.move_to(bg)
    return VGroup(bg, items)


# ── S01 — one word, two conclusions (5.03 s) ─────────────────────────────────
class S01Scene(Scene):
    def construct(self):
        # Generic "suspicious word" — delve introduced at S03.
        trigger = Text("a word", font=SERIF, font_size=96, color=INK)
        trigger.move_to(UP * 2.6)

        # Full-width conclusion cards
        c1_bg = RoundedRectangle(corner_radius=0.24, width=5.6, height=1.5,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3)
        c1_bg.move_to(LEFT * 3.1 + DOWN * 0.6)
        c1_lbl = Text("AI wrote this", font=SERIF, font_size=48, color=INK)
        c1_lbl.move_to(c1_bg)

        c2_bg = RoundedRectangle(corner_radius=0.24, width=5.6, height=1.5,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3)
        c2_bg.move_to(RIGHT * 3.1 + DOWN * 0.6)
        c2_lbl = Text("it's the watermark", font=SERIF, font_size=48, color=INK)
        c2_lbl.move_to(c2_bg)

        fork = trigger.get_bottom() + DOWN * 0.12
        a1 = Arrow(fork, c1_bg.get_top() + LEFT * 0.5,
                   color=INK, stroke_width=3.5, tip_length=0.22, buff=0.05)
        a2 = Arrow(fork, c2_bg.get_top() + RIGHT * 0.5,
                   color=TERRA, stroke_width=3.5, tip_length=0.22, buff=0.05)

        # Explanatory footer keeps bottom of safe area filled
        footer = Text("two conclusions, one word", font=SANS,
                       font_size=40, color=INK)
        footer.move_to(DOWN * 2.5)

        self.play(FadeIn(trigger), run_time=0.45)
        self.play(
            GrowArrow(a1), FadeIn(c1_bg), FadeIn(c1_lbl),
            GrowArrow(a2), FadeIn(c2_bg), FadeIn(c2_lbl),
            run_time=1.0,
        )
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(3.18)   # ≈ 5.03 s


# ── S02 — second conclusion inverted (5.53 s) ────────────────────────────────
class S02Scene(Scene):
    def construct(self):
        trigger = Text("a word", font=SERIF, font_size=96, color=INK)
        trigger.move_to(UP * 2.6)

        c1_bg = RoundedRectangle(corner_radius=0.24, width=5.6, height=1.5,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3)
        c1_bg.move_to(LEFT * 3.1 + DOWN * 0.6)
        c1_lbl = Text("AI wrote this", font=SERIF, font_size=48, color=INK)
        c1_lbl.move_to(c1_bg)

        c2_bg = RoundedRectangle(corner_radius=0.24, width=5.6, height=1.5,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3)
        c2_bg.move_to(RIGHT * 3.1 + DOWN * 0.6)
        c2_lbl = Text("it's the watermark", font=SERIF, font_size=48, color=INK)
        c2_lbl.move_to(c2_bg)

        fork = trigger.get_bottom() + DOWN * 0.12
        a1 = Arrow(fork, c1_bg.get_top() + LEFT * 0.5,
                   color=INK, stroke_width=3.5, tip_length=0.22, buff=0.05)
        a2 = Arrow(fork, c2_bg.get_top() + RIGHT * 0.5,
                   color=INK, stroke_width=3.5, tip_length=0.22, buff=0.05)

        card2 = VGroup(c2_bg, c2_lbl)
        self.add(trigger, a1, c1_bg, c1_lbl, a2, card2)
        self.wait(0.4)

        # TERRA underline marks the inverted card
        ul = Line(
            [c2_bg.get_left()[0],  c2_bg.get_bottom()[1] - 0.18, 0],
            [c2_bg.get_right()[0], c2_bg.get_bottom()[1] - 0.18, 0],
            color=TERRA, stroke_width=7,
        )
        self.play(Rotate(card2, angle=PI), run_time=1.0)
        self.play(Create(ul), run_time=0.45)

        # "backwards" label fills lower safe area
        label = Text("the second one is backwards", font=SANS,
                      font_size=38, color=INK)
        label.move_to(DOWN * 2.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(3.28)   # ≈ 5.53 s


# ── S03 — THE ANCHOR (6.27 s) ────────────────────────────────────────────────
class S03Scene(Scene):
    def construct(self):
        word, arrow, lbl_2022, lbl_2024 = _anchor_group()

        # "fifteen-fold" annotation fills upper safe area
        eyebrow = Text("something like fifteen-fold in two years",
                        font=SANS, font_size=38, color=INK)
        eyebrow.move_to(DOWN * 2.9)

        self.play(FadeIn(word), run_time=0.6)
        self.wait(0.2)
        self.play(
            GrowArrow(arrow),
            FadeIn(lbl_2022), FadeIn(lbl_2024),
            run_time=1.4,
        )
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.wait(3.57)   # ≈ 6.27 s


# ── S04 — watermark nudging toward one fixed word (7.36 s) ───────────────────
class S04Scene(Scene):
    def construct(self):
        wm_bg = RoundedRectangle(corner_radius=0.24, width=3.8, height=1.6,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3)
        wm_bg.move_to(LEFT * 4.0 + UP * 0.6)
        wm_lbl = Text("watermark", font=SANS, font_size=46, color=INK, weight=BOLD)
        wm_lbl.move_to(wm_bg)

        fixed_bg = RoundedRectangle(corner_radius=0.24, width=4.2, height=1.6,
                                     fill_color=GROUND, fill_opacity=1,
                                     stroke_color=INK, stroke_width=3)
        fixed_bg.move_to(RIGHT * 3.8 + UP * 0.6)
        fixed_lbl = Text("selected word", font=SERIF, font_size=52, color=INK)
        fixed_lbl.move_to(fixed_bg)

        # TERRA nudge arrow — one accent
        nudge = Arrow(
            wm_bg.get_right() + RIGHT * 0.05,
            fixed_bg.get_left() + LEFT * 0.05,
            color=TERRA, stroke_width=6, tip_length=0.26, buff=0.1,
        )

        caption = Text("always the same favourite", font=SERIF,
                        font_size=48, color=INK)
        caption.move_to(DOWN * 2.2)

        # "wrong read" label fills top
        read_lbl = Text("the natural read", font=SANS, font_size=40, color=INK)
        read_lbl.move_to(UP * 2.7)

        self.play(FadeIn(read_lbl), run_time=0.4)
        self.play(FadeIn(wm_bg), FadeIn(wm_lbl), run_time=0.45)
        self.play(FadeIn(fixed_bg), FadeIn(fixed_lbl), run_time=0.4)
        self.wait(0.2)
        self.play(GrowArrow(nudge), run_time=0.9)
        self.wait(0.3)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(4.22)   # ≈ 7.36 s


# ── S05 — find-and-replace kills it (5.25 s) ─────────────────────────────────
class S05Scene(Scene):
    def construct(self):
        # Hypothetical fixed-favourite words — generic, not AI tells
        favs = ["chosen", "selected", "marked"]
        chips = VGroup()
        for w in favs:
            bg = RoundedRectangle(corner_radius=0.2, width=4.0, height=1.2,
                                   fill_color=GROUND, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2.5)
            lbl = Text(w, font=SERIF, font_size=48, color=INK)
            lbl.move_to(bg)
            chips.add(VGroup(bg, lbl))
        chips.arrange(DOWN, buff=0.28).move_to(LEFT * 2.5)

        headline = Text("a fixed favourite list", font=SANS,
                         font_size=44, color=INK)
        headline.move_to(UP * 3.0)

        self.play(FadeIn(headline), FadeIn(chips), run_time=0.6)
        self.wait(0.2)

        # TERRA strikethrough each — the one accent for this beat
        strikes = VGroup()
        for chip in chips:
            lbl = chip[1]
            s = Line(
                [lbl.get_left()[0] - 0.12, lbl.get_center()[1], 0],
                [lbl.get_right()[0] + 0.12, lbl.get_center()[1], 0],
                color=TERRA, stroke_width=7,
            )
            strikes.add(s)

        self.play(
            LaggedStart(*[Create(s) for s in strikes], lag_ratio=0.28),
            run_time=1.1,
        )

        drain = Text("swap them out — signal gone", font=SANS,
                      font_size=42, color=INK)
        drain.move_to(DOWN * 2.5)
        self.play(FadeIn(drain), run_time=0.5)
        self.wait(2.84)   # ≈ 5.25 s


# ── S06 — no list to attack (3.95 s) ─────────────────────────────────────────
# FIX: large poster-scale content visible through both sample points.
class S06Scene(Scene):
    def construct(self):
        # Headline fills top
        headline = Text("its security depends on this", font=SANS,
                         font_size=48, color=INK)
        headline.move_to(UP * 2.9)

        # Full-width contrast row — persistent from ~1s onward
        # Left: "fixed list" struck; Right: "fresh draw" affirmed
        cross_bg = RoundedRectangle(corner_radius=0.2, width=5.0, height=1.5,
                                     fill_color=GROUND, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2.5)
        cross_bg.move_to(LEFT * 3.0 + UP * 0.6)
        cross_lbl = Text("fixed list", font=SERIF, font_size=52, color=INK)
        cross_lbl.move_to(cross_bg)
        cross_line = Line(
            [cross_bg.get_left()[0], cross_bg.get_center()[1], 0],
            [cross_bg.get_right()[0], cross_bg.get_center()[1], 0],
            color=TERRA, stroke_width=8,
        )

        fresh_bg = RoundedRectangle(corner_radius=0.2, width=5.0, height=1.5,
                                     fill_color=GROUND, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2.5)
        fresh_bg.move_to(RIGHT * 3.0 + UP * 0.6)
        fresh_lbl = Text("redrawn fresh", font=SERIF, font_size=52, color=INK)
        fresh_lbl.move_to(fresh_bg)

        caption = Text("no fixed favourite\n— nothing to find and replace",
                        font=SANS, font_size=44, color=INK, line_spacing=0.95)
        caption.move_to(DOWN * 1.5)

        sub = Text("so it doesn't", font=SERIF, font_size=56, color=INK)
        sub.move_to(DOWN * 2.5)

        self.play(FadeIn(headline), run_time=0.4)
        self.play(
            FadeIn(cross_bg), FadeIn(cross_lbl), Create(cross_line),
            FadeIn(fresh_bg), FadeIn(fresh_lbl),
            run_time=0.9,
        )
        self.play(FadeIn(caption), run_time=0.4)
        self.play(FadeIn(sub), run_time=0.35)
        self.wait(1.92)   # ≈ 3.95 s


# ── S07 — redrawn at every position (7.49 s) ─────────────────────────────────
# THE REDRAW MECHANISM — S08 reuses this visual vocabulary.
# FIX: key_label inside title-safe (x ≥ -5.5); all elements enlarged.
class S07Scene(Scene):
    def construct(self):
        headline = Text("at each word position:", font=SANS,
                         font_size=44, color=INK)
        headline.move_to(UP * 3.0)
        self.play(FadeIn(headline), run_time=0.4)

        # Stem sentence builds left to right
        stems = ["What", "it", "does"]
        cur_x = -5.5
        stem_mobs = []
        for w in stems:
            m = Text(w, font=SERIF, font_size=64, color=INK)
            m.move_to([cur_x + m.width / 2, 1.0, 0])
            cur_x += m.width + 0.18
            stem_mobs.append(m)
            self.play(FadeIn(m), run_time=0.28)
            self.wait(0.08)

        # TERRA border on each popup = THE MECHANISM accent for S07
        popup_data = [
            (["redraw", "refresh", "reset"], -1.5),
            (["at",    "each",   "every"],   1.1),
            (["word",  "place",  "slot"],    3.7),
        ]

        for words, px in popup_data:
            pop = _popup(words, highlight_idx=None)
            pop[0].set_stroke(color=TERRA, width=3)  # TERRA border
            pop.move_to([px, -0.6, 0])
            self.play(FadeIn(pop), run_time=0.32)
            self.wait(0.44)
            self.play(FadeOut(pop), run_time=0.28)

        payoff = Text("fresh preferences every time", font=SERIF,
                       font_size=52, color=INK)
        payoff.move_to(DOWN * 2.2)
        self.play(FadeIn(payoff), run_time=0.5)
        self.wait(2.53)   # ≈ 7.49 s


# ── S08 — favoured once, then not (5.38 s) ───────────────────────────────────
# Reuses S07's per-position popup mechanism — show all 3 draws simultaneously
# so there is no timing gap between sequential fades.
class S08Scene(Scene):
    def construct(self):
        headline = Text('three draws — where is "delve"?',
                         font=SANS, font_size=44, color=INK)
        headline.move_to(UP * 3.0)

        # All 3 popups shown at once: same mechanism as S07, three positions
        draw_configs = [
            (["delve", "explores", "notes"], 0,    "draw 1"),
            (["shows",  "finds",  "reveals"], None, "draw 2"),
            (["offers", "brings", "marks"],   None, "draw 3"),
        ]
        positions_x = [-3.8, 0.0, 3.8]

        pops = VGroup()
        pos_texts = VGroup()
        for (words, hi, plbl), px in zip(draw_configs, positions_x):
            pop = _popup(words, highlight_idx=hi)
            pop.move_to([px, 0.5, 0])
            pos_text = Text(plbl, font=SANS, font_size=40, color=INK)
            pos_text.move_to([px, pop.get_bottom()[1] - 0.42, 0])
            pops.add(pop)
            pos_texts.add(pos_text)

        absent = Text("favoured once — absent the next two", font=SERIF,
                       font_size=48, color=INK)
        absent.move_to(DOWN * 2.7)

        self.play(FadeIn(headline), run_time=0.35)
        self.play(
            LaggedStart(*[FadeIn(p) for p in pops], lag_ratio=0.25),
            LaggedStart(*[FadeIn(t) for t in pos_texts], lag_ratio=0.25),
            run_time=1.0,
        )
        self.wait(0.5)
        self.play(FadeIn(absent), run_time=0.45)
        self.wait(3.08)   # ≈ 5.38 s


# ── S09 — two different homes (5.18 s) ───────────────────────────────────────
class S09Scene(Scene):
    def construct(self):
        bw, bh = 5.0, 3.4

        w_bg = RoundedRectangle(corner_radius=0.24, width=bw, height=bh,
                                 fill_color=GROUND, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3)
        w_lbl = Text("model weights", font=SANS, font_size=42, color=INK, weight=BOLD)
        w_sub = Text("the habit", font=SERIF, font_size=52, color=INK)
        w_small = Text("lives in the weights", font=SERIF, font_size=48, color=INK)
        w_lbl.move_to(w_bg.get_top() + DOWN * 0.55)
        w_sub.move_to(w_bg.get_center() + DOWN * 0.05)
        w_small.move_to(w_bg.get_bottom() + UP * 0.55)
        weights = VGroup(w_bg, w_lbl, w_sub, w_small)

        # TERRA border on the watermark box — one accent
        c_bg = RoundedRectangle(corner_radius=0.24, width=bw, height=bh,
                                 fill_color=GROUND, fill_opacity=1,
                                 stroke_color=TERRA, stroke_width=3)
        c_lbl = Text("per-position draw", font=SANS, font_size=42, color=INK, weight=BOLD)
        c_sub = Text("the watermark", font=SERIF, font_size=52, color=INK)
        c_small = Text("lives in a coin flip", font=SERIF, font_size=48, color=INK)
        c_lbl.move_to(c_bg.get_top() + DOWN * 0.55)
        c_sub.move_to(c_bg.get_center() + DOWN * 0.05)
        c_small.move_to(c_bg.get_bottom() + UP * 0.55)
        coin = VGroup(c_bg, c_lbl, c_sub, c_small)

        weights.move_to(LEFT * 3.2)
        coin.move_to(RIGHT * 3.2)

        # Centre separator fills the gap between boxes
        sep = Line(np.array([0, -2.0, 0]), np.array([0, 2.0, 0]),
                    color=INK, stroke_width=2)
        headline = Text("two different homes", font=SANS, font_size=44, color=INK)
        headline.move_to(UP * 3.1)
        footer = Text("the habit and the mark\nlive in completely separate places",
                       font=SANS, font_size=40, color=INK, line_spacing=0.95)
        footer.move_to(DOWN * 2.8)

        self.play(FadeIn(headline), run_time=0.4)
        self.play(FadeIn(weights), FadeIn(coin), Create(sep), run_time=0.9)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(3.48)   # ≈ 5.18 s


# ── S10 — same word, unrelated documents (5.97 s) ────────────────────────────
# FIX: only 2 documents (wide) to avoid edge-bleed; single TERRA sweep.
class S10Scene(Scene):
    def construct(self):
        headline = Text("same word — no shared context", font=SANS,
                         font_size=48, color=INK)
        headline.move_to(UP * 3.1)
        self.play(FadeIn(headline), run_time=0.5)

        doc_data = [
            ("research paper",  "to delve into"),
            ("email",           "delve deeper"),
        ]
        docs = VGroup()
        for title, excerpt in doc_data:
            db = RoundedRectangle(corner_radius=0.24, width=5.3, height=3.2,
                                   fill_color=GROUND, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2.5)
            dt = Text(title, font=SANS, font_size=42, color=INK, weight=BOLD)
            dt.move_to(db.get_top() + DOWN * 0.65)
            de = Text(excerpt, font=SERIF, font_size=48, color=INK)
            de.move_to(db.get_center() + DOWN * 0.1)
            docs.add(VGroup(db, dt, de))
        docs.arrange(RIGHT, buff=0.9).move_to(UP * 0.5)

        self.play(FadeIn(docs), run_time=0.8)
        self.wait(0.2)

        # TERRA underline — single sweep, one accent
        uls = VGroup()
        for doc in docs:
            de = doc[2]
            ul = Line(
                [de.get_left()[0],  de.get_bottom()[1] - 0.1, 0],
                [de.get_right()[0], de.get_bottom()[1] - 0.1, 0],
                color=TERRA, stroke_width=6,
            )
            uls.add(ul)

        footer = Text("same habit — nothing watermarked", font=SERIF,
                       font_size=46, color=INK)
        footer.move_to(DOWN * 2.6)
        sub = Text("no nudge — it was already there",
                    font=SANS, font_size=40, color=INK)
        sub.move_to(DOWN * 3.1)

        self.play(
            LaggedStart(*[Create(ul) for ul in uls], lag_ratio=0.35),
            run_time=0.9,
        )
        self.play(FadeIn(footer), run_time=0.4)
        self.play(FadeIn(sub), run_time=0.35)
        self.wait(2.37)   # ≈ 5.97 s total


# ── S11 — traced back to the tuning step (6.25 s) ────────────────────────────
class S11Scene(Scene):
    def construct(self):
        stages = [
            ("pretraining\ncorpus", -4.4),
            ("base model",           0.0),
            ("alignment\ntuning",    4.4),
        ]

        headline = Text("where does the habit come from?", font=SANS,
                         font_size=44, color=INK)
        headline.move_to(UP * 3.0)
        self.play(FadeIn(headline), run_time=0.45)

        dots, lbls = [], []
        for label, x in stages:
            d = Dot(np.array([x, 0.2, 0]), radius=0.25, color=INK)
            l = Text(label, font=SANS, font_size=40, color=INK, line_spacing=0.88)
            l.move_to([x, -0.88, 0])
            dots.append(d)
            lbls.append(l)

        arrows_lr = []
        for i in range(len(stages) - 1):
            x0, x1 = stages[i][1] + 0.28, stages[i + 1][1] - 0.28
            arrows_lr.append(Arrow(
                np.array([x0, 0.2, 0]), np.array([x1, 0.2, 0]),
                color=INK, stroke_width=3, tip_length=0.22, buff=0,
            ))

        self.play(
            *[FadeIn(d) for d in dots],
            *[FadeIn(l) for l in lbls],
            *[GrowArrow(a) for a in arrows_lr],
            run_time=1.0,
        )
        self.wait(0.4)

        # TERRA ring + trail arrow — strengthens at tuning node
        ring = Circle(radius=0.46, color=TERRA, stroke_width=5, fill_opacity=0)
        ring.move_to(dots[2])

        trail_arrow = Arrow(
            np.array([2.6,  2.0, 0]),
            np.array([4.2,  0.7, 0]),
            color=TERRA, stroke_width=4, tip_length=0.22, buff=0,
        )
        trail_lbl = Text("trail strengthens here", font=SANS, font_size=40, color=INK)
        trail_lbl.move_to([2.2, 2.4, 0])

        self.play(Create(ring), GrowArrow(trail_arrow),
                  FadeIn(trail_lbl), run_time=0.9)
        self.wait(3.51)   # ≈ 6.25 s


# ── S12 — THE ONE FLAG (11.22 s) ─────────────────────────────────────────────
class S12Scene(Scene):
    def construct(self):
        # TERRA flag — required accent, reel's only hedge beat
        pole = Line(np.array([-5.8, -2.6, 0]), np.array([-5.8, 2.6, 0]),
                     color=TERRA, stroke_width=5)
        flag_rect = Rectangle(width=2.2, height=1.1,
                               fill_color=TERRA, fill_opacity=1, stroke_width=0)
        flag_rect.move_to(np.array([-4.7, 2.1, 0]))
        flag_text = Text("one flag", font=SANS, font_size=36,
                          color=GROUND, weight=BOLD)
        flag_text.move_to(flag_rect)

        fam_w, fam_h = 5.2, 5.0

        l_bg = RoundedRectangle(corner_radius=0.24, width=fam_w, height=fam_h,
                                 fill_color=GROUND, fill_opacity=1,
                                 stroke_color=INK, stroke_width=2.5)
        l_bg.move_to(LEFT * 2.1)
        l_title = Text("context-keyed\nwatermark", font=SANS, font_size=40, color=INK,
                        weight=BOLD, line_spacing=0.88)
        l_title.move_to(l_bg.get_top() + DOWN * 0.72)
        l_body = Text("redraws preferences\nat every position",
                       font=SERIF, font_size=46, color=INK, line_spacing=1.1)
        l_body.move_to(l_bg.get_center())
        l_foot = Text("clean split\nholds here", font=SERIF, font_size=46, color=INK,
                       line_spacing=1.1)
        l_foot.move_to(l_bg.get_bottom() + UP * 0.78)

        r_bg = RoundedRectangle(corner_radius=0.24, width=fam_w, height=fam_h,
                                 fill_color=GROUND, fill_opacity=1,
                                 stroke_color=INK, stroke_width=2.5)
        r_bg.move_to(RIGHT * 2.1)
        r_title = Text("fixed-list or\ntopic-steered", font=SANS, font_size=40, color=INK,
                        weight=BOLD, line_spacing=0.88)
        r_title.move_to(r_bg.get_top() + DOWN * 0.72)
        r_body = Text("holds a fixed list\nor steers a topic",
                       font=SERIF, font_size=46, color=INK, line_spacing=1.1)
        r_body.move_to(r_bg.get_center())
        r_foot = Text("line blurs here", font=SERIF, font_size=46, color=INK)
        r_foot.move_to(r_bg.get_bottom() + UP * 0.58)

        left_fam  = VGroup(l_bg, l_title, l_body, l_foot)
        right_fam = VGroup(r_bg, r_title, r_body, r_foot)

        self.play(Create(pole), FadeIn(flag_rect), FadeIn(flag_text), run_time=0.65)
        self.wait(0.25)
        self.play(FadeIn(left_fam), run_time=0.7)
        self.wait(0.35)
        self.play(FadeIn(right_fam), run_time=0.7)
        self.wait(8.57)   # ≈ 11.22 s


# ── S13 — THE ANCHOR RETURNS (9.66 s) ────────────────────────────────────────
class S13Scene(Scene):
    def construct(self):
        # IDENTICAL anchor composition to S03
        word, arrow, lbl_2022, lbl_2024 = _anchor_group()

        self.play(FadeIn(word), run_time=0.5)
        self.play(GrowArrow(arrow), FadeIn(lbl_2022), FadeIn(lbl_2024), run_time=0.85)
        self.wait(0.35)

        # Two sentences added beneath — "delve" in each, two different causes
        cause1 = Text("mark may have nudged it  →  delve",
                       font=SERIF, font_size=56, color=INK)
        cause1.move_to(DOWN * 1.2 + LEFT * 0.4)

        cause2 = Text("model reached for it  →  delve",
                       font=SERIF, font_size=56, color=INK)
        cause2.move_to(DOWN * 1.9 + LEFT * 0.4)

        divider = Text("same word · two reasons · indistinguishable",
                        font=SANS, font_size=40, color=INK)
        divider.move_to(DOWN * 2.7)

        self.play(FadeIn(cause1), run_time=0.5)
        self.play(FadeIn(cause2), run_time=0.5)
        self.play(FadeIn(divider), run_time=0.4)
        self.wait(5.66)   # ≈ 9.66 s


# ── S14 — two runs, one comparison (5.35 s) ──────────────────────────────────
class S14Scene(Scene):
    def construct(self):
        headline = Text("the only way to tell them apart", font=SANS,
                         font_size=44, color=INK)
        headline.move_to(UP * 3.0)
        self.play(FadeIn(headline), run_time=0.4)

        prompt_bg = RoundedRectangle(corner_radius=0.24, width=4.5, height=1.2,
                                      fill_color=GROUND, fill_opacity=1,
                                      stroke_color=INK, stroke_width=3)
        prompt_bg.move_to(UP * 1.6)
        prompt_lbl = Text("same prompt", font=SANS, font_size=40, color=INK, weight=BOLD)
        prompt_lbl.move_to(prompt_bg)
        prompt = VGroup(prompt_bg, prompt_lbl)

        mk_bg = RoundedRectangle(corner_radius=0.24, width=4.0, height=1.2,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2.5)
        mk_bg.move_to(LEFT * 2.8 + DOWN * 0.4)
        mk_lbl = Text("with mark", font=SANS, font_size=40, color=INK)
        mk_lbl.move_to(mk_bg)

        um_bg = RoundedRectangle(corner_radius=0.24, width=4.0, height=1.2,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2.5)
        um_bg.move_to(RIGHT * 2.8 + DOWN * 0.4)
        um_lbl = Text("without mark", font=SANS, font_size=40, color=INK)
        um_lbl.move_to(um_bg)

        # TERRA border on comparison box — the payoff
        co_bg = RoundedRectangle(corner_radius=0.24, width=5.5, height=1.3,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=TERRA, stroke_width=4)
        co_bg.move_to(DOWN * 2.3)
        co_lbl = Text("comparison", font=SANS, font_size=40, color=INK, weight=BOLD)
        co_lbl.move_to(co_bg)
        comp = VGroup(co_bg, co_lbl)

        a1 = Arrow(prompt_bg.get_left(),  mk_bg.get_top(),
                   color=INK, stroke_width=2.5, tip_length=0.2, buff=0.05)
        a2 = Arrow(prompt_bg.get_right(), um_bg.get_top(),
                   color=INK, stroke_width=2.5, tip_length=0.2, buff=0.05)
        a3 = Arrow(mk_bg.get_bottom(), co_bg.get_top() + LEFT * 1.0,
                   color=INK, stroke_width=2.5, tip_length=0.2, buff=0.05)
        a4 = Arrow(um_bg.get_bottom(), co_bg.get_top() + RIGHT * 1.0,
                   color=INK, stroke_width=2.5, tip_length=0.2, buff=0.05)

        self.play(FadeIn(prompt), run_time=0.4)
        self.play(GrowArrow(a1), GrowArrow(a2),
                  FadeIn(mk_bg), FadeIn(mk_lbl),
                  FadeIn(um_bg), FadeIn(um_lbl),
                  run_time=0.75)
        self.play(GrowArrow(a3), GrowArrow(a4), FadeIn(comp), run_time=0.7)
        self.wait(3.06)   # ≈ 5.35 s


# ── S15 — direction A: a tell doesn't prove it (6.74 s) ──────────────────────
class S15Scene(Scene):
    def construct(self):
        prem_bg = RoundedRectangle(corner_radius=0.24, width=9.0, height=1.8,
                                    fill_color=GROUND, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3)
        prem_bg.move_to(UP * 2.0)
        prem_lbl = Text("AI-SOUNDING WORD", font=SANS, font_size=54,
                         color=INK, weight=BOLD)
        prem_lbl.move_to(prem_bg)

        co_bg = RoundedRectangle(corner_radius=0.24, width=9.0, height=1.8,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3)
        co_bg.move_to(DOWN * 0.5)
        co_lbl = Text("THERE IS A WATERMARK", font=SERIF, font_size=54, color=INK)
        co_lbl.move_to(co_bg)

        arr = Arrow(prem_bg.get_bottom(), co_bg.get_top(),
                    color=INK, stroke_width=3.5, tip_length=0.24, buff=0.05)

        # TERRA strikethrough — the one accent
        strike = Line(
            [co_bg.get_left()[0]  - 0.2, co_bg.get_center()[1], 0],
            [co_bg.get_right()[0] + 0.2, co_bg.get_center()[1], 0],
            color=TERRA, stroke_width=10,
        )

        footer = Text("you would need a controlled comparison", font=SERIF,
                       font_size=48, color=INK)
        footer.move_to(DOWN * 2.5)

        self.play(FadeIn(prem_bg), FadeIn(prem_lbl), run_time=0.5)
        self.play(GrowArrow(arr), FadeIn(co_bg), FadeIn(co_lbl), run_time=0.7)
        self.wait(0.3)
        self.play(Create(strike), run_time=0.6)
        self.play(FadeIn(footer), run_time=0.5)
        self.wait(4.14)   # ≈ 6.74 s


# ── S16 — direction B: no tells don't prove absence (6.49 s) ─────────────────
# Mirror of S15 — same construction, opposite conclusion.
class S16Scene(Scene):
    def construct(self):
        prem_bg = RoundedRectangle(corner_radius=0.24, width=9.0, height=1.8,
                                    fill_color=GROUND, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3)
        prem_bg.move_to(UP * 2.0)
        prem_lbl = Text("NO TELLS AT ALL", font=SANS, font_size=54,
                         color=INK, weight=BOLD)
        prem_lbl.move_to(prem_bg)

        co_bg = RoundedRectangle(corner_radius=0.24, width=9.0, height=1.8,
                                  fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3)
        co_bg.move_to(DOWN * 0.5)
        co_lbl = Text("THERE IS NO WATERMARK", font=SERIF, font_size=54, color=INK)
        co_lbl.move_to(co_bg)

        arr = Arrow(prem_bg.get_bottom(), co_bg.get_top(),
                    color=INK, stroke_width=3.5, tip_length=0.24, buff=0.05)

        strike = Line(
            [co_bg.get_left()[0]  - 0.2, co_bg.get_center()[1], 0],
            [co_bg.get_right()[0] + 0.2, co_bg.get_center()[1], 0],
            color=TERRA, stroke_width=10,
        )

        # S16-specific: spread-thin label
        spread = Text("mark is spread thin — choices you'd never notice",
                       font=SERIF, font_size=48, color=INK)
        spread.move_to(DOWN * 2.5)

        self.play(FadeIn(prem_bg), FadeIn(prem_lbl), run_time=0.5)
        self.play(GrowArrow(arr), FadeIn(co_bg), FadeIn(co_lbl), run_time=0.7)
        self.wait(0.3)
        self.play(Create(strike), run_time=0.6)
        self.play(FadeIn(spread), run_time=0.5)
        self.wait(3.89)   # ≈ 6.49 s
