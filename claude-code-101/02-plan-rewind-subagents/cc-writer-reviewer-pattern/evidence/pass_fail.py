import csv

with open("grades.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"]
        if not name:
            continue
        scores = [int(row[q]) for q in ("q1", "q2", "q3") if row[q]]
        avg = sum(scores) / len(scores) if scores else 0
        print(f"{name}: {'PASS' if avg >= 70 else 'FAIL'}")
