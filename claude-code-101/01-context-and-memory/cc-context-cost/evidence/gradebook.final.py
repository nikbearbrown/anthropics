"""gradebook — add students, record scores, print averages."""
import csv, json, sys
from contextlib import contextmanager
from pathlib import Path

DB = Path("grades.json")
CSV = Path("grades.csv")


def load():
    return json.loads(DB.read_text()) if DB.exists() else {}


def save(data):
    DB.write_text(json.dumps(data, indent=2))


@contextmanager
def session():
    data = load()
    before = json.dumps(data)
    yield data
    if json.dumps(data) != before:
        save(data)


def add(name):
    with session() as data:
        data.setdefault(name, [])
    print(f"added {name}")


def score(name, value):
    with session() as data:
        data.setdefault(name, []).append(float(value))
    print(f"{name}: {value}")


def remove(name):
    with session() as data:
        if data.pop(name, None) is None:
            print(f"no such student: {name}")
            return
    print(f"removed {name}")


def rename(old, new):
    with session() as data:
        if old not in data:
            print(f"no such student: {old}")
            return
        if new in data:
            print(f"already exists: {new}")
            return
        data[new] = data.pop(old)
    print(f"renamed {old} to {new}")


def report():
    for name, scores in load().items():
        avg = sum(scores) / len(scores) if scores else 0.0
        print(f"{name:12s} {avg:6.1f}")


def stats(name):
    data = load()
    if name not in data:
        print(f"no such student: {name}")
        return
    scores = data[name]
    if not scores:
        print(f"{name}: no scores")
        return
    print(f"{name} count={len(scores)} mean={sum(scores) / len(scores):.1f} min={min(scores):.1f} max={max(scores):.1f}")


def export():
    with CSV.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "average", "scores"])
        for name, scores in load().items():
            avg = sum(scores) / len(scores) if scores else 0.0
            writer.writerow([name, f"{avg:.1f}", " ".join(str(s) for s in scores)])
    print(f"wrote {CSV}")


def top(n):
    averages = [
        (name, sum(scores) / len(scores) if scores else 0.0)
        for name, scores in load().items()
    ]
    averages.sort(key=lambda item: item[1], reverse=True)
    for name, avg in averages[: int(n)]:
        print(f"{name:12s} {avg:6.1f}")


if __name__ == "__main__":
    cmd, *args = sys.argv[1:] or ["report"]
    {"add": add, "score": score, "remove": remove, "rename": rename, "report": report, "top": top, "stats": stats, "export": export}[cmd](*args)
