#!/usr/bin/env python3
"""csv_shape.py — print the shape of a CSV: rows, columns, dtypes."""
import csv, sys

def guess_dtype(v: str) -> str:
    v = v.strip()
    if v == "":
        return "empty"
    try:
        int(v); return "int"
    except ValueError:
        pass
    try:
        float(v); return "float"
    except ValueError:
        pass
    if v.lower() in ("true", "false", "yes", "no"):
        return "bool"
    return "str"

def main(path: str) -> int:
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        print("empty file"); return 1
    header, *body = rows
    dtypes = []
    for i, col in enumerate(header):
        sample = next((r[i] for r in body if i < len(r) and r[i].strip() != ""), "")
        dtypes.append(guess_dtype(sample))
    print(f"rows: {len(body)}")
    print(f"cols: {len(header)}")
    for name, dt in zip(header, dtypes):
        print(f"  {name}: {dt}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "sample.csv"))
