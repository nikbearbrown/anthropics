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
if re.search(r'<h[1-3][^>]*>[^<]*!', h): fails.append("exclamation mark in a heading")
if re.search(r'type="email"|type="password"', h): fails.append("email/password field (sign-up wall)")
if len(re.findall(r'font-family\s*:', h)) > 1: fails.append("more than one font-family")
if re.search(r'welcome', h, re.I): fails.append("the word 'welcome'")
print("\n".join("FAIL: " + f for f in fails) if fails else "PASS: index.html meets PROJECT.md's definition of done")
sys.exit(1 if fails else 0)
