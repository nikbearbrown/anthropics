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


def late_penalty(days_late, base_score):
    days = int(days_late)
    if days <= 0:
        percent_off = 0
    elif days == 1:
        percent_off = 10
    elif days == 2:
        percent_off = 20
    elif days <= 6:
        percent_off = 20 + 5 * (days - 2)
    else:
        percent_off = 50
    return base_score * (1 - percent_off / 100)


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
