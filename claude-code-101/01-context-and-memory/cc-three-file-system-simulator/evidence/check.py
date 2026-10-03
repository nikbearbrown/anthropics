"""check.py — the page's definition of done, as a script. Exit 0 = done."""
import re, sys
from pathlib import Path
p = Path("index.html")
if not p.exists(): sys.exit("FAIL: index.html missing")
h = p.read_text()
fails = []
if re.search(r'https?://', h): fails.append("external request (http/https URL)")
if re.search(r'<script\s+src|<link\s+[^>]*href', h): fails.append("external script/stylesheet")
if re.search(r'[\U0001F300-\U0001FAFF☀-➿]', h): fails.append("emoji")
if len(re.findall(r'font-family\s*:', h)) > 1: fails.append("more than one font-family")
if re.search(r'setInterval|setTimeout|requestAnimationFrame', h): fails.append("autoplay (setInterval/setTimeout/requestAnimationFrame)")
if re.search(r'type\s*=\s*"range"', h): fails.append("speed slider (input type=range)")
if len(re.findall(r'<button', h)) > 1: fails.append("more than one button")
allowed = {"#8B7355", "#6B8E6B", "#D97757", "#F6F1E6"}
hexes = {c.upper() for c in re.findall(r'#[0-9A-Fa-f]{6}', h)}
extra = {c for c in hexes if c not in {a.upper() for a in allowed} and c not in {"#000000", "#111111", "#222222"}}
if extra: fails.append("colours outside DESIGN.md: " + " ".join(sorted(extra)))
print("\n".join("FAIL: " + f for f in fails) if fails else "PASS: index.html meets PROJECT.md's definition of done")
sys.exit(1 if fails else 0)
