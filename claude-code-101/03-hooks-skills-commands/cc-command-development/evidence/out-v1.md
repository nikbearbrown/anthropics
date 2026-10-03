# Python Code Review — `inventory.py`

Found 6 issues across bugs and security concerns.

---

## 🔴 CRITICAL — Security

### 1. SQL injection (line 14)
```python
q = "SELECT name, price FROM items WHERE sku = '" + sku + "'"
```
String concatenation into SQL. An attacker who controls `sku` can read/modify anything.
**Fix:** use a parameterized query.
```python
cur.execute("SELECT name, price FROM items WHERE sku = ?", (sku,))
```

### 2. Shell injection via `os.system` (line 39)
```python
os.system("tar czf " + name + ".tgz data/")
```
A `name` like `"foo; rm -rf ~"` executes arbitrary commands.
**Fix:** use `subprocess.run` with a list (no shell).
```python
subprocess.run(["tar", "czf", f"{name}.tgz", "data/"], check=True)
```

---

## 🟠 HIGH — Correctness bugs

### 3. Mutable default argument (line 6)
```python
def load_items(rows, seen=[]):
```
The default list is shared across every call — items leak between invocations.
**Fix:**
```python
def load_items(rows, seen=None):
    if seen is None:
        seen = []
```

### 4. Off-by-one in `last_n` (line 35)
```python
return items[len(items) - n:len(items) + 1]
```
`len(items) + 1` is meaningless (slices tolerate out-of-range but the `+1` is wrong intent), and `n <= 0` gives surprising results. Idiomatic form:
```python
return items[-n:] if n > 0 else []
```

---

## 🟡 MEDIUM

### 5. Bare `except:` swallows everything (line 30)
```python
except:
    return None
```
Catches `KeyboardInterrupt` and `SystemExit` too, and hides real bugs (permission errors, disk errors).
**Fix:** narrow it.
```python
except (OSError, FileNotFoundError):
    return None
```

### 6. Float→int precision loss in `total_cents` (line 22)
```python
s = s + int(p * 100)
```
`int(0.29 * 100)` is `28`, not `29` — classic float truncation for money.
**Fix:** round, or better use `decimal.Decimal`.
```python
s += round(p * 100)
```

---

## Summary

| # | Severity | Line | Issue |
|---|---|---|---|
| 1 | Critical | 14 | SQL injection |
| 2 | Critical | 39 | Shell injection |
| 3 | High | 6 | Mutable default arg |
| 4 | High | 35 | Off-by-one slice |
| 5 | Medium | 30 | Bare `except` |
| 6 | Medium | 22 | Float money truncation |

Two critical injection vulns should be fixed before this touches any untrusted input. Want me to apply the fixes?