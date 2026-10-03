"""Draw honest slate PNGs for the three beats that have no manim scene:
   B02 STILL·ai (petri dishes photo slot)
   B11 OutroSeries
   B12 OutroCTA
The slate is the format for this review cut. Each card names what belongs
there. Cream ground, ink title, teal eyebrow, crimson callout, gold underline —
same house palette as the scenes so the sequence reads coherently.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1920, 1080
CREAM = (243, 235, 221)
INK   = (47, 42, 38)
TEAL  = (31, 111, 92)
CRIM  = (191, 51, 57)
GOLD  = (245, 208, 97)


def _font(size, family="EBGaramond"):
    # Try repo font first; fall back to any Garamond installed system-wide.
    candidates = [
        f"/Users/bear/Documents/CoWork/bear-textbooks/books/vox/fonts/{family}-Regular.ttf",
        f"/Users/bear/Documents/CoWork/bear-textbooks/books/vox/fonts/{family}-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for c in candidates:
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


def _draw_center(d, text, y, font, fill):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    d.text(((W - tw) // 2, y), text, font=font, fill=fill)
    return bbox


def make_b02():
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    d.rectangle([80, 80, W - 80, H - 80], outline=(212, 212, 212), width=2)
    _draw_center(d, "SLATE — STILL · ai", 120, _font(28), TEAL)
    _draw_center(d, "B02  ·  two petri dishes", 170, _font(24), INK)
    _draw_center(d, "Targeted vs Untargeted, culture", 210, _font(24), INK)

    # Body: what the still needs to show
    y = 320
    for line, color, size in [
        ("PROMPT", TEAL, 26),
        ("Two dishes seen from above on an aged newsprint surface.", INK, 32),
        ("Left dish labeled TARGETED — dense teal dots bound", INK, 32),
        ("to pink cancer cells. Right dish labeled UNTARGETED —", INK, 32),
        ("sparse teal dots. Editorial diagram, desaturated,", INK, 32),
        ("flat print reproduction.", INK, 32),
    ]:
        _draw_center(d, line, y, _font(size), color)
        y += size + 18

    # Bottom marker
    _draw_center(d, "the antibody works beautifully in the lab —", 900, _font(28), INK)
    _draw_center(d, "the tumor data tells a different story", 940, _font(28), CRIM)
    d.line([(W // 2 - 300, 985), (W // 2 + 300, 985)], fill=GOLD, width=3)
    im.save("media/B02.png")


def make_b11():
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    _draw_center(d, "CANCER NANOMEDICINE", 380, _font(28), TEAL)
    _draw_center(d, "Part of the series.", 460, _font(72), INK)
    d.line([(W // 2 - 260, 555), (W // 2 + 260, 555)], fill=GOLD, width=3)
    _draw_center(d, "github.com/NikBearBrown/cancer-nanomedicine", 640, _font(28), INK)
    im.save("media/B11.png")


def make_b12():
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    _draw_center(d, "@NikBearBrown", 380, _font(36), TEAL)
    _draw_center(d, "Like and subscribe for more.", 460, _font(60), INK)
    d.line([(W // 2 - 260, 545), (W // 2 + 260, 545)], fill=GOLD, width=3)
    _draw_center(d, "— Nik Bear Brown", 620, _font(28), INK)
    im.save("media/B12.png")


if __name__ == "__main__":
    import os
    os.chdir(Path(__file__).resolve().parent)
    Path("media").mkdir(exist_ok=True)
    make_b02()
    make_b11()
    make_b12()
    print("wrote media/B02.png, media/B11.png, media/B12.png")
