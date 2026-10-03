"""Check any format_price.py against SPEC.md — the five cases the film cares about."""
import sys, importlib.util

def load(path):
    spec = importlib.util.spec_from_file_location("fp", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.format_price

def check(fp):
    cases = [(1299, "12.99 EUR"), (0, "0.00 EUR"), (10000, "100.00 EUR"), (12345, "123.45 EUR")]
    fails = []
    for cents, want in cases:
        try:
            got = fp(cents)
        except Exception as e:
            got = f"raised {type(e).__name__}"
        if got != want:
            fails.append(f"format_price({cents}) -> {got!r} (SPEC: {want!r})")
    try:
        got = fp(-50)
        fails.append(f"format_price(-50) -> {got!r} (SPEC: raises ValueError)")
    except ValueError:
        pass
    except Exception as e:
        fails.append(f"format_price(-50) -> raised {type(e).__name__} (SPEC: raises ValueError)")
    return fails

if __name__ == "__main__":
    fp = load(sys.argv[1])
    fails = check(fp)
    if not fails:
        print("PASS")
    else:
        for f in fails:
            print("FAIL:", f)
        sys.exit(1)
