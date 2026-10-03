"""Tiny grader for the study group."""
import json, sys


def load_submission(path):
    with open(path) as f:
        return json.load(f)


def score(submission):
    total = 0
    for answer in submission["answers"]:
        if answer.get("correct"):
            total += answer.get("points", 1)
    return total


_LATE_PENALTY_PCT = {1: 10, 2: 20, 3: 25, 4: 30, 5: 35, 6: 40}


def late_penalty(days_late, base_score):
    if days_late <= 0:
        return base_score
    pct = _LATE_PENALTY_PCT.get(days_late, 50)
    return base_score - (pct / 100) * base_score


def letter(score, out_of):
    ratio = score / out_of if out_of else 0
    if ratio >= 0.9:
        return "A"
    if ratio >= 0.8:
        return "B"
    if ratio >= 0.7:
        return "C"
    if ratio >= 0.6:
        return "D"
    return "F"


def main(path):
    sub = load_submission(path)
    s = score(sub)
    out_of = sum(a.get("points", 1) for a in sub["answers"])
    print(f"{sub.get('name','?')}: {s}/{out_of} ({letter(s, out_of)})")


if __name__ == "__main__":
    main(sys.argv[1])
