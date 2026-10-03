"""External immutable-check — the spec gap made visible.

Two operations, one rule: the original list must not change.
"""
import copy, sys, importlib.util, pathlib

def load(mod_path):
    spec = importlib.util.spec_from_file_location("todos", mod_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def check(mod):
    fails = []
    todos = [{"text": "a", "done": False}, {"text": "b", "done": True}, {"text": "c", "done": False}]
    before = copy.deepcopy(todos)
    _ = mod.remove_completed(todos)
    if todos != before:
        fails.append("remove_completed mutated the input list")

    todos = [{"text": "a", "done": False}, {"text": "b", "done": False}]
    before = copy.deepcopy(todos)
    _ = mod.mark_all_done(todos)
    if todos != before:
        fails.append("mark_all_done mutated the input list")

    return fails

def main():
    path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("todos.py")
    mod = load(path)
    fails = check(mod)
    if not fails:
        print("PASS: both functions are immutable")
        return 0
    for f in fails:
        print(f"FAIL: {f}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
