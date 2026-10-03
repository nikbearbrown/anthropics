# Fix `add` bug in tinycalc

## Context

`scratch/README.md` flags that `add` "doesn't handle negative numbers correctly." Reading `scratch/calc.py:1-4` confirms it — `add` has a guard clause that returns `0` when either argument is negative, instead of computing the sum. `add(-1, 2)` returns `0`; should return `1`. The existing tests in `scratch/test_calc.py` only cover the two-positive path, so they pass despite the bug.

## Change

**`scratch/calc.py`** — remove the negative-number guard so `add` just returns `a + b`:

```python
def add(a, b):
    return a + b
```

**`scratch/test_calc.py`** — add a test that exercises a negative operand (would have failed against the buggy version):

```python
def test_add_negative(self):
    self.assertEqual(add(-1, 2), 1)
```

Add it as another method on the existing `CalcTests` class.

## Verify

From `scratch/`:

```
python3 -m unittest test_calc.py
```

Expect 4 tests, all passing. Against the buggy `add`, `test_add_negative` would have asserted `0 == 1` and failed.
