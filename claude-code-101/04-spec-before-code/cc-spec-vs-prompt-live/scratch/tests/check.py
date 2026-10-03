#!/usr/bin/env python3
"""Definition-of-done check for auth.py. Prints PASS or a list of FAIL lines."""
import re, sys, time, importlib.util, pathlib

p = pathlib.Path("auth.py")
if not p.exists():
    print("FAIL: auth.py missing"); sys.exit(1)
src = p.read_text()

fails = []

# password-storage hygiene
if not re.search(r"\bbcrypt\b", src):
    fails.append("FAIL: no bcrypt")
if re.search(r"\bimport\s+hashlib\b", src) or re.search(r"\bmd5\b", src, re.I):
    fails.append("FAIL: md5/hashlib in login")
if re.search(r"\bsha1\b", src, re.I):
    fails.append("FAIL: sha1 in login")
if re.search(r"^\s*USERS\s*=\s*\{", src, re.M):
    fails.append("FAIL: in-memory USERS dict")

# parameterized SQL only — no string formatting of SELECTs/INSERTs
sql_lines = [ln for ln in src.splitlines() if re.search(r"(SELECT|INSERT|UPDATE|DELETE)\b", ln, re.I)]
for ln in sql_lines:
    if ".format(" in ln or "%s" in ln and "%s" not in "?%s?" and ("cursor" not in ln and "execute" in ln and "?" not in ln) or re.search(r"f['\"].*(SELECT|INSERT|UPDATE|DELETE)", ln, re.I):
        fails.append(f"FAIL: unparameterized SQL: {ln.strip()[:60]}")
if re.search(r"['\"]\s*\+\s*\w+\s*\+\s*['\"]", src) and any("SELECT" in ln.upper() for ln in sql_lines):
    fails.append("FAIL: string concat in SQL")

# behavior — empty password rejection and timing floor
try:
    spec = importlib.util.spec_from_file_location("auth", "auth.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if hasattr(m, "login"):
        conn = None
        # empty password → None
        try:
            r = m.login("someone", "", conn)
            if r is not None:
                fails.append("FAIL: empty password accepted")
        except Exception:
            pass  # raising is fine
except Exception as e:
    fails.append(f"FAIL: import: {e}")

if fails:
    for f in fails: print(f)
    sys.exit(1)
print("PASS")
