"""gradebook — add students, record scores, print averages."""
import json, sys
from pathlib import Path

DB = Path("grades.json")


def load():
    return json.loads(DB.read_text()) if DB.exists() else {}


def save(data):
    DB.write_text(json.dumps(data, indent=2))


def add(name):
    data = load()
    data.setdefault(name, [])
    save(data)
    print(f"added {name}")


def score(name, value):
    data = load()
    data.setdefault(name, []).append(float(value))
    save(data)
    print(f"{name}: {value}")


def remove(name):
    data = load()
    if data.pop(name, None) is None:
        print(f"no such student: {name}")
        return
    save(data)
    print(f"removed {name}")


def report():
    for name, scores in load().items():
        avg = sum(scores) / len(scores) if scores else 0.0
        print(f"{name:12s} {avg:6.1f}")


if __name__ == "__main__":
    cmd, *args = sys.argv[1:] or ["report"]
    {"add": add, "score": score, "remove": remove, "report": report}[cmd](*args)
