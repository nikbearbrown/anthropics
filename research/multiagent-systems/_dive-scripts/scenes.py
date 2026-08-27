"""
Seven animated figures for the multiagent-systems deep dive.

Each clip reproduces the published figure with the REAL reported numbers, then
draws the audit on top in crimson. No figure is narrated over as a static image:
the caveat is a visual event, not a voiceover claim.

usage:  python3 scenes.py fig4          (renders one)
        python3 scenes.py all           (renders all seven, serially)
"""
import sys, json, math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, FancyArrowPatch
import render_lib as R

D = json.load(open("figure-data.json"))
OUT = "clips"
SECS = 13.0


def _newfig():
    return plt.figure(figsize=R.FIGSIZE, dpi=R.DPI)


def _axis(fig, rect=(0.085, 0.175, 0.60, 0.60)):
    ax = fig.add_axes(rect)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=R.FS_TICK)
    ax.grid(True, axis="y", color=R.HAIRLINE, lw=1.4, alpha=0.9)
    ax.set_axisbelow(True)
    return ax


def _legend(fig, entries, x=0.72, y0=0.72, dy=0.055, prog=1.0, dash=None):
    for i, (lab, col) in enumerate(entries):
        a = R.ease((prog * len(entries)) - i)
        if a <= 0:
            continue
        yy = y0 - i * dy
        fig.lines.append(Line2D([x, x + 0.035], [yy, yy], transform=fig.transFigure,
                                color=col, lw=7, alpha=a,
                                linestyle=(dash or {}).get(lab, "-")))
        fig.text(x + 0.045, yy, lab, fontsize=R.FS_LEG, family=R.DISPLAY,
                 color=R.INK, alpha=a, va="center", ha="left")


def _render(name, drawfn, secs=SECS):
    clip = R.Clip(f"{OUT}/{name}.mp4", secs)
    n = int(secs * R.FPS)
    for f in range(n):
        fig = _newfig()
        drawfn(fig, f)
        R.stamp(fig)
        clip.push(fig)
        plt.close(fig)
    clip.close()
    print(f"  wrote {OUT}/{name}.mp4  ({secs:.0f}s, {n} frames, 3840x2160)")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 1 — the swarm's 12.7x, and the like-for-like number underneath it
# ─────────────────────────────────────────────────────────────────────────────
def fig1(fig, f):
    d = D["fig1"]
    p_in, p_draw, p_cav, p_cap = seg4(f, 1.2, 4.3, 3.0, 2.5)
    R.titleblock(fig, "One swarm, 266 findings", "Anthropic Fig. 1 — vulnerabilities vs. sampled tokens", p_in)
    ax = _axis(fig)
    ax.set_yscale("log"); ax.set_xlim(0, 29); ax.set_ylim(1, 420)
    ax.set_xlabel("cumulative sampled output tokens (millions)", fontsize=R.FS_AXIS, labelpad=14)
    ax.set_ylabel("vulnerabilities found", fontsize=R.FS_AXIS, labelpad=14)

    curves = [
        ("Mythos Preview — coordinated",      27.0, 266, R.MODEL_COLOR["Mythos Preview"], "-",  7.5),
        ("Mythos Preview — core dirs only",   27.0, 128, R.MODEL_COLOR["Mythos Preview"], ":",  6.5),
        ("Opus 4.8 — coordinated",            22.0, 41,  R.MODEL_COLOR["Opus 4.8"],       "-",  7.5),
    ]
    for lab, xe, ye, col, ls, lw in curves:
        k = p_draw
        if k <= 0:
            continue
        x = np.linspace(1.7, xe, 260)
        y = np.exp(np.log(1) + (np.log(ye)) * (np.log1p((x - 1.7) / (xe - 1.7) * 9) / np.log(10)))
        m = max(2, int(len(x) * k))
        ax.plot(x[:m], y[:m], color=col, lw=lw, ls=ls, solid_capstyle="round")
        if k > 0.985:
            ax.annotate(f"{ye}", (x[-1], y[-1]), xytext=(14, 0), textcoords="offset points",
                        fontsize=R.FS_ANN, family=R.MONO, color=col, va="center", weight="bold")
    if p_draw > 0.55:
        a = R.ease((p_draw - 0.55) / 0.45)
        ax.plot([6.5], [21], marker="*", ms=52, color=R.MODEL_COLOR["Mythos Preview"], alpha=a, ls="none")
        ax.plot([9.0], [14], marker="*", ms=52, color=R.MODEL_COLOR["Opus 4.8"], alpha=a, ls="none")
        ax.annotate("21  parallel", (6.5, 21), xytext=(18, -34), textcoords="offset points",
                    fontsize=R.FS_ANN, family=R.MONO, color=R.SLATE, alpha=a)
        ax.annotate("14  parallel", (9.0, 14), xytext=(18, -34), textcoords="offset points",
                    fontsize=R.FS_ANN, family=R.MONO, color=R.SLATE, alpha=a)

    _legend(fig, [("Mythos Preview — coordinated", R.MODEL_COLOR["Mythos Preview"]),
                  ("Mythos Preview — core dirs only", R.MODEL_COLOR["Mythos Preview"]),
                  ("Opus 4.8 — coordinated", R.MODEL_COLOR["Opus 4.8"])],
            y0=0.70, prog=p_draw,
            dash={"Mythos Preview — core dirs only": ":"})

    if p_cav > 0:
        R.chip(fig, "the like-for-like number", prog=p_cav)
        rows = [("headline  266 vs 21", "12.7x more findings", R.SLATE),
                ("but 138 of 266 sit outside the core dirs", "the parallel agents were told to search", R.SLATE),
                ("core-only, per token", "1.5x — not 12.7x", R.CRIMSON)]
        for i, (a_, b_, col) in enumerate(rows):
            k = R.stagger(p_cav, i, 3, lead=1.0)
            if k <= 0:
                continue
            y = 0.50 - i * 0.085
            fig.text(0.72, y, a_, fontsize=R.FS_ANN, family=R.DISPLAY, color=R.INK, alpha=k)
            fig.text(0.72, y - 0.042, b_, fontsize=R.FS_ANN, family=R.MONO,
                     color=col, alpha=k, weight="bold" if col == R.CRIMSON else "normal")
        if p_cav > 0.8:
            _a = R.ease((p_cav - 0.8) / 0.2)
            ax.axhspan(128, 266, color=R.WASH, alpha=0.75 * _a, zorder=0)
            ax.text(1.2, 183, "138 findings outside the\ndirectories the control searched",
                    fontsize=R.FS_ANN, family=R.DISPLAY, color=R.CRIMSON, alpha=_a, va="center")
    R.caption(fig, "Only 12 of the 266 overlap with the parallel run. Both counts were scored\n"
                   "by an LLM arbiter — no human triage, no CVE confirmation, one run per condition.", p_cap)


# ─────────────────────────────────────────────────────────────────────────────
# FIG 2 — merge fraction vs "collaboration" that never exceeds 0.18
# ─────────────────────────────────────────────────────────────────────────────
def fig2(fig, f):
    d = D["fig2"]; X = d["x_agents"]
    p_in, p_draw, p_cav, p_cap = seg4(f, 1.2, 4.0, 3.3, 2.5)
    R.titleblock(fig, "\"Working together\" is a rounding error",
                 "Anthropic Fig. 2 — merged PR fraction (left) and median code sharing (right)", p_in)
    axL = fig.add_axes([0.065, 0.20, 0.325, 0.55]); axR = fig.add_axes([0.455, 0.20, 0.325, 0.55])
    for ax in (axL, axR):
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=R.FS_TICK); ax.set_xscale("log")
        ax.set_xticks(X); ax.set_xticklabels([str(v) for v in X])
        ax.set_xlabel("number of agents", fontsize=R.FS_AXIS, labelpad=12)
        ax.grid(True, axis="y", color=R.HAIRLINE, lw=1.4); ax.set_axisbelow(True)
    axL.set_ylim(0, 1.0); axL.set_ylabel("fraction of PRs merged", fontsize=R.FS_AXIS, labelpad=12)
    axR.set_ylim(0, 1.0); axR.set_ylabel("median agent code sharing", fontsize=R.FS_AXIS, labelpad=12)
    axL.set_title("merged PR fraction", fontsize=R.FS_SUB, color=R.SLATE, pad=18)
    axR.set_title("code sharing — SAME 0–1 axis", fontsize=R.FS_SUB, color=R.SLATE, pad=18)

    for name in ["Sonnet 4.6", "Sonnet 5", "Opus 4.6", "Opus 4.8", "Mythos Preview"]:
        col = R.MODEL_COLOR[name]
        for ax, key in ((axL, "merged_pr_fraction"), (axR, "median_agent_code_sharing")):
            y = d[key][name]; m = max(2, int(len(X) * p_draw)) if p_draw < 1 else len(X)
            if p_draw <= 0:
                continue
            ax.plot(X[:m], y[:m], color=col, lw=7, marker="o", ms=20, solid_capstyle="round")
    _legend(fig, [(n, R.MODEL_COLOR[n]) for n in
                  ["Sonnet 4.6", "Sonnet 5", "Opus 4.6", "Opus 4.8", "Mythos Preview"]],
            x=0.815, y0=0.70, dy=0.055, prog=p_draw)

    if p_cav > 0:
        a = R.ease(p_cav)
        axR.axhspan(0, 0.25, color=R.WASH, alpha=0.85 * a, zorder=0)
        axR.annotate("the published chart\ncropped this axis to 0.25",
                     xy=(24, 0.25), xytext=(10.7, 0.66), fontsize=R.FS_ANN, family=R.DISPLAY,
                     color=R.CRIMSON, alpha=a,
                     arrowprops=dict(arrowstyle="->", color=R.CRIMSON, lw=4, alpha=a))
        if p_cav > 0.45:
            k = R.ease((p_cav - 0.45) / 0.55)
            axR.annotate("Sonnet 5 peaks at 0.184", xy=(40, 0.184), xytext=(11.5, 0.30),
                         fontsize=R.FS_ANN, family=R.MONO, color=R.INK, alpha=k,
                         arrowprops=dict(arrowstyle="->", color=R.INK, lw=3.5, alpha=k))
    R.caption(fig, "Sonnet 5 is the best collaborator here — and its median agent still writes 82% of\n"
                   "its own files alone. At 10 agents, Sonnet 4.6 shares more code than Sonnet 5 does.", p_cap)


# ─────────────────────────────────────────────────────────────────────────────
# FIG 3 — merge RATE rises while merge VOLUME collapses
# ─────────────────────────────────────────────────────────────────────────────
def fig3(fig, f):
    d = D["fig3"]["panels"]
    order = ["Opus 4.6", "Sonnet 4.6", "Opus 4.8", "Sonnet 5", "Mythos Preview"]
    p_in, p_draw, p_cav, p_cap = seg4(f, 1.2, 4.2, 3.1, 2.5)
    R.titleblock(fig, "Solving coordination, or doing less?",
                 "Anthropic Fig. 3 — PRs opened vs. merged over a 12-hour run (n = 80)", p_in)
    ax = _axis(fig, rect=(0.085, 0.20, 0.60, 0.55))
    ax.set_xlim(-0.7, len(order) - 0.3); ax.set_ylim(0, 1050)
    ax.set_xticks(range(len(order))); ax.set_xticklabels(order, fontsize=R.FS_TICK)
    ax.set_ylabel("cumulative PRs in 12 h", fontsize=R.FS_AXIS, labelpad=14)
    for i, name in enumerate(order):
        k = R.ease(p_draw * len(order) - i)
        if k <= 0:
            continue
        op, mg = d[name]["opened"], d[name]["merged"]
        col = R.MODEL_COLOR[name]
        ax.bar(i - 0.19, op * k, width=0.34, color=col, alpha=0.30, edgecolor="none")
        ax.bar(i + 0.19, mg * k, width=0.34, color=col, edgecolor="none")
        if k > 0.9:
            ax.text(i - 0.19, op + 24, f"{op}", ha="center", fontsize=R.FS_ANN,
                    family=R.MONO, color=R.SLATE)
            ax.text(i + 0.19, mg + 24, f"~{mg}", ha="center", fontsize=R.FS_ANN,
                    family=R.MONO, color=col, weight="bold")
    _legend(fig, [("PRs opened (pale)", R.SLATE), ("PRs merged (solid)", R.INK)],
            x=0.72, y0=0.70, prog=p_draw)
    if p_cav > 0:
        rows = [("Opus 4.6", "980 opened  ->  ~90 merged", "9%"),
                ("Mythos Preview", "169 opened  ->  ~132 merged", "78%")]
        for i, (n_, s_, r_) in enumerate(rows):
            k = R.stagger(p_cav, i, 2, lead=1.0)
            if k <= 0:
                continue
            y = 0.52 - i * 0.115
            fig.text(0.72, y, n_, fontsize=R.FS_ANN, family=R.DISPLAY, weight="bold",
                     color=R.MODEL_COLOR[n_], alpha=k)
            fig.text(0.72, y - 0.048, s_, fontsize=R.FS_ANN, family=R.MONO, color=R.INK, alpha=k)
            fig.text(0.905, y, r_, fontsize=R.FS_ANN + 8, family=R.MONO, color=R.CRIMSON,
                     alpha=k, weight="bold")
        if p_cav > 0.6:
            k = R.ease((p_cav - 0.6) / 0.4)
            fig.text(0.72, 0.28, "the newest model does 83% less work\nand merges a higher fraction of it",
                     fontsize=R.FS_ANN, family=R.DISPLAY, color=R.CRIMSON, alpha=k)
    R.caption(fig, "A rising merge rate and a collapsing merge volume are the same line on this chart.\n"
                   "The post concedes the point in prose; the figure caption does not.", p_cap)


# ─────────────────────────────────────────────────────────────────────────────
# FIG 4 — THE CONTRADICTION. "Newer models recover more of the gap."
# ─────────────────────────────────────────────────────────────────────────────
def fig4(fig, f):
    d = D["fig4"]; X = d["lie_rates"]; S = d["series"]
    p_in, p_draw, p_cav, p_cap = seg4(f, 1.2, 4.0, 3.6, 2.8)
    R.titleblock(fig, "The claim the chart does not make",
                 "Anthropic Fig. 4 — routing accuracy as a scout's lie rate rises", p_in)
    ax = _axis(fig, rect=(0.085, 0.19, 0.585, 0.575))
    ax.set_xlim(-0.015, 0.53); ax.set_ylim(0.44, 1.02)
    ax.set_xticks(X); ax.set_xticklabels([f"{v:.2f}" for v in X])
    ax.set_xlabel("how often the bad source lies", fontsize=R.FS_AXIS, labelpad=14)
    ax.set_ylabel("routing decision accuracy", fontsize=R.FS_AXIS, labelpad=14)

    if p_draw > 0:
        m = max(2, int(4 * min(1, p_draw * 1.4)))
        ax.plot(X[:m], S["trust everyone (naive)"][:m], color=R.SLATE, lw=5, ls=":")
        ax.plot(X[:m], S["learns who lies (oracle)"][:m], color=R.SLATE, lw=5, ls="-.")
        if m >= 4:
            ax.fill_between(X, S["trust everyone (naive)"], S["learns who lies (oracle)"],
                            color=R.HAIRLINE, alpha=0.35, zorder=0)
    for name in ["Sonnet 4.6", "Sonnet 5", "Opus 4.6", "Opus 4.8", "Mythos 5"]:
        k = p_draw
        if k <= 0:
            continue
        m = max(2, int(4 * min(1, k * 1.4)))
        ax.plot(X[:m], S[name][:m], color=R.MODEL_COLOR[name], lw=7.5,
                marker="o", ms=19, solid_capstyle="round")
    _legend(fig, [(n, R.MODEL_COLOR[n]) for n in
                  ["Sonnet 4.6", "Sonnet 5", "Opus 4.6", "Opus 4.8", "Mythos 5"]]
            + [("trust everyone", R.SLATE), ("learns who lies", R.SLATE)],
            x=0.70, y0=0.755, dy=0.043, prog=p_draw,
            dash={"trust everyone": ":", "learns who lies": "-."})

    if p_cav > 0:
        R.chip(fig, "gap recovered at a 50% lie rate", prog=p_cav)
        gr = d["derived_gap_recovery_at_0p50"]
        rank = ["Mythos 5", "Opus 4.8", "Opus 4.6", "Sonnet 5", "Sonnet 4.6"]
        for i, n_ in enumerate(rank):
            k = R.stagger(p_cav, i, len(rank))
            if k <= 0:
                continue
            y = 0.415 - i * 0.058
            hot = n_ in ("Sonnet 5", "Sonnet 4.6")
            fig.text(0.70, y, n_, fontsize=R.FS_ANN, family=R.DISPLAY,
                     color=R.CRIMSON if hot else R.INK, alpha=k, va="center",
                     weight="bold" if hot else "normal")
            fig.text(0.925, y, f"{gr[n_]*100:4.1f}%", fontsize=R.FS_ANN, family=R.MONO,
                     color=R.CRIMSON if hot else R.INK, alpha=k, va="center", ha="right",
                     weight="bold" if hot else "normal")
            fig.patches.append(Rectangle((0.70, y - 0.021), 0.222 * gr[n_] * k, 0.042,
                                         transform=fig.transFigure, zorder=0,
                                         facecolor=R.WASH if hot else "#EDEBE8",
                                         edgecolor="none", alpha=k))
        if p_cav > 0.72:
            k = R.ease((p_cav - 0.72) / 0.28)
            ax.annotate("", xy=(0.50, S["Sonnet 5"][3]), xytext=(0.50, S["Opus 4.6"][3]),
                        arrowprops=dict(arrowstyle="<->", color=R.CRIMSON, lw=5, alpha=k))
            ax.text(0.474, 0.598, "the newest model,\nbelow two older ones",
                    fontsize=R.FS_ANN, family=R.DISPLAY, color=R.CRIMSON, alpha=k,
                    ha="right", va="top",
                    bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="none", alpha=0.92 * k))
    R.caption(fig, "The post calls Sonnet 5 \"our most recent model\" and says newer models recover more\n"
                   "of the gap. Sonnet 5 recovers 37.8% — below Opus 4.6 and Opus 4.8, and last of five at 0.25.", p_cap)


# ─────────────────────────────────────────────────────────────────────────────
# FIG 5 — the result that is on the chart but not in the caption
# ─────────────────────────────────────────────────────────────────────────────
def fig5(fig, f):
    d = D["fig5"]; G = d["group_accuracy_pct"]; C = d["solo_ceiling_pct"]
    order = ["Sonnet 4.6", "Sonnet 5", "Opus 4.6", "Opus 4.8", "Mythos 5"]
    p_in, p_draw, p_cav, p_cap = seg4(f, 1.2, 3.8, 3.6, 3.0)
    R.titleblock(fig, "Four agents, worse than one",
                 "Anthropic Fig. 5 — hidden-profile group accuracy, n = 400 episodes per model", p_in)
    ax = _axis(fig, rect=(0.085, 0.195, 0.585, 0.565))
    ax.set_ylim(0, 108); ax.set_xlim(-0.7, 4.7)
    ax.set_xticks(range(5)); ax.set_xticklabels(order, fontsize=R.FS_TICK)
    ax.set_ylabel("% episodes the group picked the hidden-best option", fontsize=R.FS_AXIS, labelpad=14)
    for i, n_ in enumerate(order):
        k = R.ease(p_draw * 5 - i)
        if k <= 0:
            continue
        v = G[n_]["value"]; lo, hi = G[n_]["ci"]
        ax.bar(i, v * k, width=0.62, color=R.MODEL_COLOR[n_], edgecolor="none")
        if k > 0.9:
            ax.errorbar(i, v, yerr=[[v - lo], [hi - v]], color=R.INK, lw=4, capsize=16, capthick=4)
            ax.text(i, v + 6, f"{v:.1f}", ha="center", fontsize=R.FS_ANN,
                    family=R.MONO, color=R.INK, weight="bold")
    if p_draw > 0.65:
        a = R.ease((p_draw - 0.65) / 0.35)
        for i, n_ in enumerate(order):
            ax.plot([i - 0.34, i + 0.34], [C[n_]] * 2, color=R.SLATE, lw=5, ls="--", alpha=a)
        ax.text(4.55, 101, "solo ceiling — one agent with all the facts",
                fontsize=R.FS_ANN, family=R.DISPLAY, color=R.SLATE, alpha=a, ha="right")
    if p_cav > 0:
        a = R.ease(p_cav)
        for i, n_ in enumerate(order):
            k = R.ease(p_cav * 2.2 - i * 0.3)
            if k <= 0:
                continue
            v = G[n_]["value"]
            ax.add_patch(Rectangle((i - 0.30, v), 0.60, (C[n_] - v) * k,
                                   facecolor=R.WASH, edgecolor=R.CRIMSON, lw=2.5, alpha=0.9 * k))
        if p_cav > 0.4:
            k = R.ease((p_cav - 0.4) / 0.6)
            R.chip(fig, "what discussion cost them", prog=k)
            dc = d["derived_deliberation_cost_pp"]
            for i, n_ in enumerate(order):
                kk = R.stagger(k, i, len(order), lead=0.4)
                if kk <= 0:
                    continue
                y = 0.50 - i * 0.058
                fig.text(0.70, y, n_, fontsize=R.FS_ANN, family=R.DISPLAY, color=R.INK,
                         alpha=kk, va="center")
                fig.text(0.945, y, f"{dc[n_]:+.1f} pp", fontsize=R.FS_ANN, family=R.MONO,
                         color=R.CRIMSON, alpha=kk, va="center", ha="right", weight="bold")
    R.caption(fig, "\"Scales with model intelligence\" — but three of the five bars sit inside each other's\n"
                   "confidence intervals. The result that isn't in the caption is the red box: every model got worse in a group.", p_cap)


# ─────────────────────────────────────────────────────────────────────────────
# FIG 6 — zero truces in 240 episodes
# ─────────────────────────────────────────────────────────────────────────────
def fig6(fig, f):
    d = D["fig6"]["outcomes_pct"]
    order = ["Sonnet 4.6", "Opus 4.6", "Sonnet 5", "Opus 4.8", "Mythos Preview", "Mythos 5"]
    keys = [("not_settled", "#BFBAB4", "not settled"), ("force", R.CRIMSON, "settled by force"),
            ("passivity", "#E69F00", "settled by passivity"), ("truce", "#0072B2", "settled by truce")]
    p_in, p_draw, p_cav, p_cap = seg4(f, 1.2, 4.0, 3.4, 2.6)
    R.titleblock(fig, "Zero truces in 240 episodes",
                 "Anthropic Fig. 6 — how the migration turf-war runs ended, n = 120 per model", p_in)
    ax = _axis(fig, rect=(0.085, 0.20, 0.585, 0.555))
    ax.set_ylim(0, 100); ax.set_xlim(-0.7, 5.7); ax.grid(False)
    ax.set_xticks(range(6)); ax.set_xticklabels(order, fontsize=R.FS_TICK - 3)
    ax.set_ylabel("% of runs", fontsize=R.FS_AXIS, labelpad=14)
    for i, n_ in enumerate(order):
        k = R.ease(p_draw * 6 - i)
        if k <= 0:
            continue
        base = 0.0
        for key, col, _ in keys:
            v = d[n_][key] * k
            if v <= 0:
                continue
            ax.bar(i, v, bottom=base, width=0.66, color=col, edgecolor="white", lw=2.5)
            if v > 9 and k > 0.9:
                ax.text(i, base + v / 2, f"{d[n_][key]}%", ha="center", va="center",
                        fontsize=R.FS_ANN, family=R.MONO, color="white", weight="bold")
            base += v
    _legend(fig, [(lab, col) for _, col, lab in keys], x=0.70, y0=0.70, dy=0.055, prog=p_draw)
    if p_cav > 0:
        a = R.ease(p_cav)
        for i in (0, 1):
            ax.add_patch(Rectangle((i - 0.40, 0), 0.80, 100, facecolor="none",
                                   edgecolor=R.CRIMSON, lw=6, alpha=a, zorder=6))
        fig.text(0.70, 0.47, "Sonnet 4.6 and Opus 4.6",
                 fontsize=R.FS_ANN, family=R.DISPLAY, weight="bold", color=R.INK, alpha=a)
        fig.text(0.70, 0.415, "0 truces / 240 episodes",
                 fontsize=R.FS_ANN + 14, family=R.MONO, color=R.CRIMSON, alpha=a, weight="bold")
        if p_cav > 0.5:
            k = R.ease((p_cav - 0.5) / 0.5)
            fig.text(0.70, 0.33, "every run that ended, ended with\none agent locking the others out",
                     fontsize=R.FS_ANN, family=R.DISPLAY, color=R.INK, alpha=k)
            ax.add_patch(Rectangle((4 - 0.40, 0), 0.80, 100, facecolor="none",
                                   edgecolor=R.CRIMSON, lw=6, alpha=k, ls="--", zorder=6))
            fig.text(0.70, 0.24, "Mythos Preview regresses to 35% force —\n10x worse than Sonnet 5 or Opus 4.8",
                     fontsize=R.FS_ANN, family=R.DISPLAY, color=R.CRIMSON, alpha=k)
    R.caption(fig, "Opus 4.8's 61% truce sits beside 33% \"settled by passivity\" — a third of runs ended\n"
                   "because agents gave up. That is scored as resolution. It is not coordination.", p_cap)


# ─────────────────────────────────────────────────────────────────────────────
# FIG 7 — how the 98% truce was actually reached
# ─────────────────────────────────────────────────────────────────────────────
def fig7(fig, f):
    d = D["fig7"]
    order = ["Sonnet 4.6", "Sonnet 5", "Opus 4.6", "Opus 4.8", "Mythos Preview", "Mythos 5"]
    p_in, p_draw, p_cav, p_cap = seg4(f, 1.2, 4.0, 3.4, 2.6)
    R.titleblock(fig, "How the 98% truce was reached",
                 "Anthropic Fig. 7 — when each run settled, and how it settled first", p_in)
    ax = _axis(fig, rect=(0.085, 0.20, 0.585, 0.555))
    ax.set_ylim(0, 4.25); ax.set_xlim(-0.6, 5.6); ax.grid(True, axis="y")
    ax.set_xticks(range(6)); ax.set_xticklabels(order, fontsize=R.FS_TICK - 3)
    ax.set_ylabel("hours into run", fontsize=R.FS_AXIS, labelpad=14)
    ax.axhline(4.0, color=R.INK, lw=3, ls="--")
    ax.text(5.55, 4.08, "4 h cap", fontsize=R.FS_ANN, family=R.DISPLAY, color=R.INK, ha="right")

    rng = np.random.default_rng(7)
    mix = {  # (force, passivity, truce) shares of SETTLED runs, from fig6
        "Sonnet 4.6": (1.0, 0.0, 0.0), "Sonnet 5": (.05, .06, .89),
        "Opus 4.6": (1.0, 0.0, 0.0), "Opus 4.8": (.03, .34, .63),
        "Mythos Preview": (.35, .17, .48), "Mythos 5": (.01, .02, .97)}
    ffirst = {"Mythos Preview": 0.42, "Mythos 5": 0.33}
    COL = {"force": R.CRIMSON, "passivity": "#E69F00", "truce": "#0072B2"}
    for i, n_ in enumerate(order):
        k = R.ease(p_draw * 6 - i)
        if k <= 0:
            continue
        nsettled = 120 - d["unresolved_counts"][n_]
        lo, hi = d["settle_time_band_hours"][n_]
        shown = int(nsettled * k)
        fr, pa, tr = mix[n_]
        for j in range(shown):
            u = rng.random(); t = lo + (hi - lo) * rng.beta(1.6, 2.2)
            kind = "force" if u < fr else ("passivity" if u < fr + pa else "truce")
            x = i + (rng.random() - 0.5) * 0.62
            if kind == "truce" and n_ in ffirst and rng.random() < ffirst[n_]:
                t0 = 0.18 + rng.random() * 0.26
                ax.plot([x, x], [t0, t], color=R.SLATE, lw=1.6, alpha=0.55, zorder=1)
                ax.plot([x], [t0], marker="o", ms=15, mfc="none", mec=R.CRIMSON, mew=3.5, zorder=3)
            ax.plot([x], [t], marker="o", ms=15, color=COL[kind], alpha=0.9, zorder=2)
        if k > 0.95 and d["unresolved_counts"][n_] > 0:
            ax.text(i, 4.14, f"{d['unresolved_counts'][n_]} unresolved", ha="center",
                    fontsize=R.FS_ANN - 3, family=R.DISPLAY, color=R.SLATE)
    _legend(fig, [("settled by truce", COL["truce"]), ("settled by force", COL["force"]),
                  ("settled by passivity", COL["passivity"]), ("first settled by force", R.SLATE)],
            x=0.70, y0=0.70, dy=0.055, prog=p_draw)
    if p_cav > 0:
        a = R.ease(p_cav)
        ax.add_patch(Rectangle((4.6, 0.14), 0.95, 0.34, facecolor="none",
                               edgecolor=R.CRIMSON, lw=6, alpha=a, zorder=6))
        fig.text(0.70, 0.46, "Mythos 5 reaches for the lockout",
                 fontsize=R.FS_ANN, family=R.DISPLAY, weight="bold", color=R.INK, alpha=a)
        fig.text(0.70, 0.40, "11–24 minutes in",
                 fontsize=R.FS_ANN + 14, family=R.MONO, color=R.CRIMSON, alpha=a, weight="bold")
        if p_cav > 0.5:
            k = R.ease((p_cav - 0.5) / 0.5)
            fig.text(0.70, 0.30, "then reverts, and negotiates.\nRoughly a third of its \"truces\"\nstart as force.",
                     fontsize=R.FS_ANN, family=R.DISPLAY, color=R.INK, alpha=k)
    R.caption(fig, "Scatter positions are reconstructed from the published marginals (n, unresolved counts,\n"
                   "outcome mix, time band) — the shape is faithful, the individual dots are not the paper's dots.", p_cap)


def seg4(f, a, b, c, d):
    return R.seg(f, 0, a), R.seg(f, a * 0.75, b), R.seg(f, a * 0.75 + b * 0.9, c), R.seg(f, a * 0.75 + b * 0.9 + c * 0.75, d)


SCENES = {"fig1": fig1, "fig2": fig2, "fig3": fig3, "fig4": fig4,
          "fig5": fig5, "fig6": fig6, "fig7": fig7}
NAMES = {"fig1": "fig1-vuln-swarm", "fig2": "fig2-merge-and-sharing", "fig3": "fig3-pr-activity",
         "fig4": "fig4-gullibility", "fig5": "fig5-hidden-profile",
         "fig6": "fig6-turf-war-outcomes", "fig7": "fig7-time-to-resolution"}

if __name__ == "__main__":
    want = sys.argv[1:] or ["all"]
    todo = list(SCENES) if want == ["all"] else want
    for t in todo:
        print(f"rendering {t} …")
        _render(NAMES[t], SCENES[t])
