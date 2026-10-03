inventory.py:6 — HIGH — Mutable default argument `seen=[]` persists across calls and accumulates state between invocations.
inventory.py:14 — HIGH — SQL injection via string concatenation of `sku` into the query; should use parameterized `?` placeholder.
inventory.py:30 — MEDIUM — Bare `except:` swallows all errors (including `KeyboardInterrupt`/`SystemExit`); should catch `OSError`.
inventory.py:35 — LOW — Off-by-one on slice upper bound; `items[-n:]` (or `items[len(items)-n:]`) is correct — `len(items)+1` is a misleading no-op that masks intent.
inventory.py:39 — HIGH — Shell injection via `os.system` with unsanitized `name`; use `subprocess.run([...], shell=False)` with a list.

5 issues found.