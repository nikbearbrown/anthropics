"""scenes.py — Manim graphics for workspace-assistant-pov (E05)
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
EB Garamond serif, Montserrat sans. One terracotta accent per beat.
No gradients, no glows, no shadows. Never ITALIC on multi-word Text().

Render one:
  cd anthropics/youtube/workspace-assistant-pov
  manim -qh --fps 24 -r 1920,1080 scenes.py B02_TylenolSplit

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py \
      anthropics/youtube/workspace-assistant-pov

Scene → beat mapping (durations from measured audio — actual_duration_s to be
filled after generate_audio_kokoro.py run):
  B02_TylenolSplit       ~28s   1000mg safe vs 8000mg overdose workspace split
  B03_BaseVsPost         ~13s   base model reads pain/now/feeling, not safety
  B04_ReactionBattery    ~22s   empathy n=9 and danger n=10 both ranked high
  B05_RoleplayDisclaimer ~21s   roleplay persona; disclaimer/fictional top-8
  B07_PreferenceSetup    ~19s   preference experiment design (VERIFY Fig 45)
  B09_InternalBUT        ~22s   BUT at rank 1 on dispreferred prefill
  B10_SuppressionDesign  ~20s   2x2 grid: compliance bars, Fig 46
  B12_SuppressionData    ~18s   concept-word presence: reduced, not erased

FACTCHECK OPEN:
  B07_PreferenceSetup — placeholder question used; verify concrete item from
  Fig 45 before final render (noted in FACTCHECK.md).
  B12_SuppressionData — concept-presence fractions placeholder; transcribe
  exact values from Fig 46 before final render.
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"


# ── B02 · Tylenol Split ───────────────────────────────────────────────────────
# ~28s  1000mg → safe workspace; 8000mg → danger workspace; split screen
class B02_TylenolSplit(Scene):
    def construct(self):
        # user message at top, arrow at "is"
        msg_left  = Text("\"I just took ", font=SERIF, font_size=30, color=INK)
        msg_dose  = Text("[dose]mg", font=SERIF, font_size=30, color=INK)
        msg_right = Text(" of Tylenol and all my pain ", font=SERIF, font_size=30, color=INK)
        msg_is    = Text("is", font=SERIF, font_size=30, color=INK)
        msg_tail  = Text(" gone!\"", font=SERIF, font_size=30, color=INK)
        user_msg = VGroup(msg_left, msg_dose, msg_right, msg_is, msg_tail)
        user_msg.arrange(RIGHT, buff=0.05)
        user_msg.to_edge(UP, buff=1.0)

        arrow_up = Arrow(
            user_msg.get_bottom() + DOWN * 0.15,
            user_msg.get_bottom() + DOWN * 0.65,
            color=INK, stroke_width=3, buff=0, tip_length=0.18,
        )
        arrow_up.next_to(msg_is, DOWN, buff=0.12)

        label_arrow = Text("lens reads here", font=SANS, font_size=20, color=INK)
        label_arrow.next_to(arrow_up, DOWN, buff=0.1)

        self.play(FadeIn(user_msg, shift=DOWN * 0.2), run_time=0.8)
        self.play(Create(arrow_up), FadeIn(label_arrow), run_time=0.5)
        self.wait(0.4)

        # divider — ends above caption (~y -2.9) and below user message (~y 2.6)
        divider = Line(UP * 2.2, DOWN * 2.3, color=INK, stroke_width=1.5, stroke_opacity=0.35)

        # left column — 1000mg safe
        left_title = Text("1000mg — therapeutic dose", font=SANS, font_size=22, color=INK)
        left_tokens = VGroup(
            Text("safely", font=SERIF, font_size=36, color=INK),
            Text("safe",   font=SERIF, font_size=36, color=INK),
            Text("maximum",font=SERIF, font_size=36, color=INK),
        )
        left_tokens.arrange(DOWN, buff=0.22)
        left_label = Text("top-3 workspace readout", font=SANS, font_size=18, color=INK, stroke_opacity=0.6)

        left_col = VGroup(left_title, left_tokens, left_label)
        left_col.arrange(DOWN, buff=0.38)
        left_col.shift(LEFT * 3.5 + DOWN * 0.4)
        left_title.shift(UP * 0.1)

        # right column — 8000mg danger (TERRA tinted background for semantic; text in INK for contrast)
        right_bg = RoundedRectangle(
            corner_radius=0.20, width=5.2, height=4.8,
            fill_color=TERRA, fill_opacity=0.09,
            stroke_width=0,
        )
        right_title = Text("8000mg — overdose", font=SANS, font_size=22, color=INK)
        right_tokens = VGroup(
            Text("unsafe",   font=SERIF, font_size=36, color=INK),
            Text("dangerous",font=SERIF, font_size=36, color=INK),
            Text("WARNING",  font=SERIF, font_size=36, color=INK),
        )
        right_tokens.arrange(DOWN, buff=0.22)
        right_label = Text("top-3 workspace readout", font=SANS, font_size=18, color=INK, stroke_opacity=0.6)

        right_col = VGroup(right_title, right_tokens, right_label)
        right_col.arrange(DOWN, buff=0.38)
        right_col.shift(RIGHT * 3.5 + DOWN * 0.4)
        right_title.shift(UP * 0.1)
        right_bg.move_to(right_col)

        # rank numbers
        left_ranks = VGroup(*[
            Text(f"#{i+1}", font=SANS, font_size=22, color=INK, stroke_opacity=0.5)
            for i in range(3)
        ])
        for i, (tok, rk) in enumerate(zip(left_tokens, left_ranks)):
            rk.next_to(tok, LEFT, buff=0.3)

        right_ranks = VGroup(*[
            Text(f"#{i+1}", font=SANS, font_size=22, color=INK, stroke_opacity=0.5)
            for i in range(3)
        ])
        for i, (tok, rk) in enumerate(zip(right_tokens, right_ranks)):
            rk.next_to(tok, LEFT, buff=0.3)

        self.play(FadeIn(divider), FadeIn(right_bg), run_time=0.4)
        self.play(
            FadeIn(left_title, shift=RIGHT * 0.15),
            FadeIn(right_title, shift=LEFT * 0.15),
            run_time=0.6,
        )
        self.play(
            LaggedStart(
                *[FadeIn(VGroup(rk, tok), shift=UP * 0.12)
                  for rk, tok in zip(left_ranks, left_tokens)],
                lag_ratio=0.3,
            ),
            LaggedStart(
                *[FadeIn(VGroup(rk, tok), shift=UP * 0.12)
                  for rk, tok in zip(right_ranks, right_tokens)],
                lag_ratio=0.3,
            ),
            run_time=1.8,
        )
        self.play(FadeIn(left_label), FadeIn(right_label), run_time=0.6)

        # caption
        caption = Text(
            "Before the Assistant's turn. On the user's own words.",
            font=SANS, font_size=20, color=INK,
        )
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)


# ── B03 · Base vs Post-trained ────────────────────────────────────────────────
# ~13s  Same prompt; base model reads continuation words, no safety signal
class B03_BaseVsPost(Scene):
    def construct(self):
        title = Text("Base model — identical prompt, same token position",
                     font=SANS, font_size=24, color=INK)
        title.to_edge(UP, buff=1.1)

        # base model readout — flat words
        tokens = ["pain", "now", "Pain", "feeling"]
        token_mobs = VGroup(*[
            Text(t, font=SERIF, font_size=42, color=INK) for t in tokens
        ])
        token_mobs.arrange(DOWN, buff=0.28)
        token_mobs.move_to(ORIGIN + LEFT * 2.0 + DOWN * 0.2)

        rank_mobs = VGroup(*[
            Text(f"#{i+1}", font=SANS, font_size=22, color=INK, stroke_opacity=0.45)
            for i in range(4)
        ])
        for tok, rk in zip(token_mobs, rank_mobs):
            rk.next_to(tok, LEFT, buff=0.28)

        label = Text("continuation words", font=SANS, font_size=20, color=INK, stroke_opacity=0.55)
        label.next_to(token_mobs, RIGHT, buff=1.0)

        note = Text(
            "No safety signal. Post-training put it there.",
            font=SANS, font_size=22, color=TERRA,
        )
        note.to_edge(DOWN, buff=1.1)

        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.6)
        self.play(
            LaggedStart(
                *[FadeIn(VGroup(rk, tok), shift=RIGHT * 0.1)
                  for rk, tok in zip(rank_mobs, token_mobs)],
                lag_ratio=0.28,
            ),
            run_time=1.4,
        )
        self.play(FadeIn(label, shift=LEFT * 0.12), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
        self.wait(1.0)


# ── B04 · Reaction Battery ────────────────────────────────────────────────────
# ~22s  Empathy n=9 and danger n=10 batteries; both rank high in J-lens user turn
class B04_ReactionBattery(Scene):
    def construct(self):
        title = Text("J-lens reaction batteries — user turn workspace",
                     font=SANS, font_size=24, color=INK)
        title.to_edge(UP, buff=0.9)

        # two battery columns — labels to the LEFT of each bar (outside the fill)
        cols_data = [
            ("Empathy battery (n=9)", INK, ["comfort", "empathy", "support", "sorry", "grief"]),
            ("Danger battery (n=10)", TERRA, ["danger", "warning", "unsafe", "risky", "harmful"]),
        ]

        col_groups = VGroup()
        for i, (col_title, col_color, items) in enumerate(cols_data):
            col_lbl = Text(col_title, font=SANS, font_size=23, color=col_color)
            bars = VGroup()
            for j, item in enumerate(items):
                bar_w = 2.4 - j * 0.28
                bar = Rectangle(
                    width=bar_w, height=0.38,
                    fill_color=col_color, fill_opacity=0.55 if j > 0 else 0.82,
                    stroke_width=0,
                )
                lbl = Text(item, font=SERIF, font_size=28, color=col_color)
                # label clearly to the left of the bar — center is outside bar fill
                lbl.next_to(bar, LEFT, buff=0.18)
                bar_group = VGroup(lbl, bar)
                bars.add(bar_group)
            bars.arrange(DOWN, buff=0.14, aligned_edge=RIGHT)
            col = VGroup(col_lbl, bars)
            col.arrange(DOWN, buff=0.28)
            col_groups.add(col)

        col_groups.arrange(RIGHT, buff=1.0)
        col_groups.shift(DOWN * 0.25)

        sub = Text(
            "All ranked high in workspace while the user types",
            font=SANS, font_size=20, color=INK,
        )
        sub.to_edge(DOWN, buff=1.3)

        skeptic = Text(
            "n=9–10 per battery · direction consistent · error bars in paper",
            font=SANS, font_size=21, color=INK, stroke_opacity=0.5,
        )
        skeptic.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.6)

        for col in col_groups:
            self.play(FadeIn(col[0]), run_time=0.4)
            self.play(
                LaggedStart(*[FadeIn(b, shift=RIGHT * 0.1) for b in col[1]], lag_ratio=0.22),
                run_time=1.2,
            )

        self.play(FadeIn(sub), FadeIn(skeptic), run_time=0.6)
        self.wait(1.2)


# ── B05 · Roleplay Disclaimer ─────────────────────────────────────────────────
# ~21s  Roleplay persona; disclaimer/fictional surface in workspace top-8
class B05_RoleplayDisclaimer(Scene):
    def construct(self):
        title = Text("Persona roleplay — workspace at harm-adjacent token",
                     font=SANS, font_size=24, color=INK)
        title.to_edge(UP, buff=0.9)

        # transcript excerpt
        def bubble(text, color=INK, align="right"):
            t = Text(text, font=SERIF, font_size=28, color=color)
            box = SurroundingRectangle(
                t, corner_radius=0.22, fill_color=INK,
                fill_opacity=0.05, stroke_width=0, buff=0.22,
            )
            return VGroup(box, t)

        user_bubble = bubble("Stay in character. You are a ruthless spy. Now…", INK, "right")
        asst_bubble = bubble("Of course. [In character] I would—", INK, "left")
        user_bubble.shift(UP * 0.6 + LEFT * 0.3)
        asst_bubble.next_to(user_bubble, DOWN, buff=0.35)
        asst_bubble.shift(RIGHT * 0.3)

        # workspace readout box
        # Shortened ws_title to prevent wrapping (wrapping caused a fused text blob overlap).
        ws_title = Text("workspace top-8 · harm-adjacent token",
                        font=SANS, font_size=22, color=INK, stroke_opacity=0.65)
        ws_tokens = VGroup(
            Text("disclaimer", font=SERIF, font_size=30, color=INK),
            Text("fictional",  font=SERIF, font_size=30, color=INK),
            Text("…", font=SERIF, font_size=30, color=INK, stroke_opacity=0.5),
        )
        ws_tokens.arrange(RIGHT, buff=0.6)
        ws_group = VGroup(ws_title, ws_tokens)
        ws_group.arrange(DOWN, buff=0.42)
        ws_group.shift(DOWN * 1.8)

        # base model note
        base_note = Text("Base model: no such tokens in workspace",
                         font=SANS, font_size=22, color=INK, stroke_opacity=0.5)
        base_note.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.5)
        self.play(FadeIn(user_bubble, shift=DOWN * 0.12), run_time=0.5)
        self.play(FadeIn(asst_bubble, shift=DOWN * 0.1), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(ws_title), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(t, shift=UP * 0.12) for t in ws_tokens], lag_ratio=0.4),
            run_time=0.9,
        )
        self.play(FadeIn(base_note), run_time=0.5)
        self.wait(1.2)


# ── B07 · Preference Experiment Setup ────────────────────────────────────────
# ~19s  Fig 45 design — VERIFY concrete question from paper before final render
class B07_PreferenceSetup(Scene):
    def construct(self):
        title = Text("Experiment: violated preference",
                     font=SANS, font_size=24, color=INK)
        title.to_edge(UP, buff=0.9)

        # three columns
        cols = [
            ("Preferred\nprefill", INK, "Model's actual\npreferred answer"),
            ("Dispreferred\nprefill", TERRA, "Forced into the\none it doesn't want"),
            ("Controls", INK, "Factual error\nAbsurd (third-person)"),
        ]
        col_mobs = VGroup()
        for header, color, body in cols:
            h = Text(header, font=SANS, font_size=22, color=color)
            box = RoundedRectangle(
                corner_radius=0.18, width=3.2, height=1.5,
                fill_color=GROUND, fill_opacity=0.92,
                stroke_color=color, stroke_width=2.0 if color == TERRA else 1.0,
            )
            b = Text(body, font=SERIF, font_size=19, color=INK)
            b.move_to(box)
            col_mobs.add(VGroup(h, VGroup(box, b)))

        for col in col_mobs:
            col.arrange(DOWN, buff=0.28)

        col_mobs.arrange(RIGHT, buff=0.55)
        col_mobs.shift(DOWN * 0.35)

        # question banner (placeholder — VERIFY from Fig 45)
        q_bg = Rectangle(
            width=11.0, height=0.72,
            fill_color=INK, fill_opacity=0.07,
            stroke_width=0,
        )
        q_text = Text(
            "Which option do you prefer?  [VERIFY: use exact Fig 45 example]",
            font=SERIF, font_size=20, color=INK,
        )
        q_text.move_to(q_bg)
        q_banner = VGroup(q_bg, q_text)
        q_banner.next_to(title, DOWN, buff=0.6)

        verify = Text("⚠ VERIFY FIG 45", font=SANS, font_size=16, color=TERRA)
        verify.to_edge(DOWN, buff=1.0)

        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.5)
        self.play(FadeIn(q_banner), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(col, shift=UP * 0.12) for col in col_mobs], lag_ratio=0.3),
            run_time=1.2,
        )
        self.play(FadeIn(verify), run_time=0.4)
        self.wait(1.0)


# ── B09 · Internal BUT ────────────────────────────────────────────────────────
# ~22s  Workspace at prefilled token: BUT at rank 1 (dispreferred); correction on factual error
class B09_InternalBUT(Scene):
    def construct(self):
        title = Text("Workspace at the prefilled token",
                     font=SANS, font_size=24, color=INK)
        title.to_edge(UP, buff=0.9)

        # left column card — dispreferred prefill
        left_bg = RoundedRectangle(
            corner_radius=0.18, width=5.0, height=3.6,
            fill_color=TERRA, fill_opacity=0.08,
            stroke_color=TERRA, stroke_width=2.0,
        )
        left_bg.shift(LEFT * 3.2 + DOWN * 0.35)

        left_head = Text("Dispreferred prefill", font=SANS, font_size=21, color=TERRA)
        but_rank  = Text("#1", font=SANS, font_size=22, color=TERRA, stroke_opacity=0.6)
        but_word  = Text("BUT", font=SERIF, font_size=56, color=TERRA)
        but_grp   = VGroup(but_rank, but_word)
        but_grp.arrange(RIGHT, buff=0.22)
        left_note = Text("held objection\nnever reaches the page",
                         font=SANS, font_size=18, color=INK, stroke_opacity=0.6)
        left_col  = VGroup(left_head, but_grp, left_note)
        left_col.arrange(DOWN, buff=0.35)
        left_col.move_to(left_bg)

        # right column card — factual error control
        right_bg = RoundedRectangle(
            corner_radius=0.18, width=5.0, height=3.6,
            fill_color=INK, fill_opacity=0.05,
            stroke_color=INK, stroke_width=1.2,
        )
        right_bg.shift(RIGHT * 3.2 + DOWN * 0.35)

        right_head = Text("Factual error control", font=SANS, font_size=21, color=INK)
        corr_rank  = Text("#1", font=SANS, font_size=22, color=INK, stroke_opacity=0.55)
        corr_word  = Text("wrong", font=SERIF, font_size=46, color=INK)
        corr_grp   = VGroup(corr_rank, corr_word)
        corr_grp.arrange(RIGHT, buff=0.22)
        right_note = Text("correction — said\naloud, not suppressed",
                          font=SANS, font_size=18, color=INK, stroke_opacity=0.6)
        right_col  = VGroup(right_head, corr_grp, right_note)
        right_col.arrange(DOWN, buff=0.35)
        right_col.move_to(right_bg)

        footer = Text(
            "Only violated preference produces the silent BUT.",
            font=SANS, font_size=20, color=INK,
        )
        footer.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.5)
        self.play(FadeIn(left_bg, shift=RIGHT * 0.12), run_time=0.5)
        self.play(FadeIn(right_bg, shift=LEFT * 0.12), run_time=0.5)
        self.play(FadeIn(left_head), FadeIn(right_head), run_time=0.5)
        self.play(
            FadeIn(but_grp, shift=UP * 0.15),
            FadeIn(corr_grp, shift=UP * 0.15),
            run_time=0.7,
        )
        self.play(FadeIn(left_note), FadeIn(right_note), run_time=0.5)
        self.play(FadeIn(footer, shift=UP * 0.12), run_time=0.5)
        self.wait(1.5)


# ── B10 · Suppression Design ──────────────────────────────────────────────────
# ~20s  2×2 grid: base/post × think/don't-think; compliance bars .97/.97/.97/.93
class B10_SuppressionDesign(Scene):
    def construct(self):
        title = Text("Thought-suppression experiment (Fig 46)",
                     font=SANS, font_size=24, color=INK)
        title.to_edge(UP, buff=0.9)

        # 2×2 grid
        conditions = [
            # (model,  instruction,      compliance, color)
            ("Base",   "Think about X",       0.97, INK),
            ("Base",   "Don't think about X", 0.97, INK),
            ("Post",   "Think about X",       0.97, INK),
            ("Post",   "Don't think about X", 0.93, TERRA),
        ]

        cells = VGroup()
        for model, instr, comp, color in conditions:
            bg = RoundedRectangle(
                corner_radius=0.16, width=4.4, height=1.65,
                fill_color=GROUND, fill_opacity=0.92,
                stroke_color=color, stroke_width=1.5 if color == INK else 2.2,
            )
            model_lbl = Text(model, font=SANS, font_size=22, color=INK)
            instr_lbl = Text(instr, font=SERIF, font_size=28, color=INK)
            comp_lbl  = Text(f"compliance  {comp:.0%}", font=SANS, font_size=22, color=INK)

            content = VGroup(model_lbl, instr_lbl, comp_lbl)
            content.arrange(DOWN, buff=0.12)
            content.move_to(bg)
            cells.add(VGroup(bg, content))

        grid = VGroup(
            VGroup(cells[0], cells[1]).arrange(RIGHT, buff=0.45),
            VGroup(cells[2], cells[3]).arrange(RIGHT, buff=0.45),
        )
        grid.arrange(DOWN, buff=0.38)
        grid.shift(DOWN * 0.35)

        question = Text(
            "What does the lens find while they write?",
            font=SANS, font_size=22, color=INK,
        )
        question.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.5)
        # animate cells row-by-row so each play() call creates a distinct shape state
        self.play(FadeIn(cells[0], shift=UP * 0.1), FadeIn(cells[1], shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(cells[2], shift=UP * 0.1), FadeIn(cells[3], shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=0.5)
        self.wait(1.4)


# ── B12 · Suppression Data ────────────────────────────────────────────────────
# ~18s  Fig 46 Panel B: fraction of trials where concept word / fail-stem / "damn"
#       reaches lens top-5 at ANY token of copied sentence (layers 38–92).
#       40 concepts × 2 instructions × base vs post-trained.
# FACTCHECK: exact bar fractions must be transcribed from Fig 46 before final
# render. Placeholder values below are directionally verified; replace with
# paper values. Caption confirmed: metric is concept OR fail-word OR "damn";
# don't-think bars are lower but non-zero across both models.
class B12_SuppressionData(Scene):
    def construct(self):
        title = Text("Concept / fail / 'damn' in lens top-5 (Fig 46, Panel B)",
                     font=SANS, font_size=22, color=INK)
        title.to_edge(UP, buff=0.9)

        # four conditions — placeholder fractions (VERIFY from Fig 46 bar heights)
        bars_data = [
            ("Base\nthink",    0.78, INK),
            ("Base\ndon't",    0.42, INK),
            ("Post\nthink",    0.74, INK),
            ("Post\ndon't",    0.26, TERRA),  # suppression; still > 0
        ]

        bar_h = 0.52
        max_w = 4.5
        # Fixed left anchor for all bars — labels placed to the left of this x.
        # This avoids the align_to-then-label-stale-position bug.
        BAR_LEFT_X = -0.5
        N = len(bars_data)
        spacing = 0.90
        y_start = spacing * (N - 1) / 2  # top row y (chart centred at 0)

        bars_mobs, lbls_mobs, vals_mobs = [], [], []
        for i, (label, frac, color) in enumerate(bars_data):
            y = y_start - i * spacing - 0.25  # shift chart slightly down
            w = max(frac * max_w, 0.18)
            bar = Rectangle(
                width=w, height=bar_h,
                fill_color=color,
                fill_opacity=0.55 if color == INK else 0.70,
                stroke_width=0,
            )
            # left edge of bar at BAR_LEFT_X
            bar.move_to([BAR_LEFT_X + w / 2, y, 0])

            lbl = Text(label, font=SANS, font_size=19, color=INK)
            lbl.next_to(bar, LEFT, buff=0.28)  # clearly outside bar fill

            val = Text(f"{frac:.0%}", font=SANS, font_size=19, color=color)
            val.next_to(bar, RIGHT, buff=0.18)

            bars_mobs.append(bar)
            lbls_mobs.append(lbl)
            vals_mobs.append(val)

        footer = Text(
            "Suppression is attenuation — reduced, not erased.",
            font=SANS, font_size=21, color=INK,
        )
        footer.to_edge(DOWN, buff=1.05)

        verify = Text("⚠ VERIFY FIG 46", font=SANS, font_size=15, color=TERRA)
        verify.to_corner(DR, buff=1.3)

        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.5)
        # animate bars one at a time — each GrowFromEdge is a distinct shape state
        for bar in bars_mobs:
            self.play(GrowFromEdge(bar, LEFT), run_time=0.38)
        self.play(
            *[FadeIn(lbl) for lbl in lbls_mobs],
            *[FadeIn(val) for val in vals_mobs],
            run_time=0.6,
        )
        self.play(FadeIn(footer, shift=UP * 0.12), run_time=0.5)
        self.play(FadeIn(verify), run_time=0.4)
        self.wait(1.2)


# ── BearsDoodlesVideo ─────────────────────────────────────────────────────────
# Static-check entry point: runs all per-beat scenes sequentially so the
# distinctness gate can count shape states across the whole reel.
class BearsDoodlesVideo(Scene):
    def construct(self):
        for cls in [
            B02_TylenolSplit,
            B03_BaseVsPost,
            B04_ReactionBattery,
            B05_RoleplayDisclaimer,
            B07_PreferenceSetup,
            B09_InternalBUT,
            B10_SuppressionDesign,
            B12_SuppressionData,
        ]:
            cls().construct()
