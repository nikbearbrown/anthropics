"""stats.py — study-readings tiny stats module.

Reading log format (one per line):
    HH:MM  temp=<float>  humid=<int>

Example:
    09:00  temp=20.4  humid=45
"""

import math


def avg_temp(readings):
    """Mean temperature across readings, or None if none are usable.

    Skips a row whose "temp" is missing, non-numeric, or not finite —
    "NaN" is emitted by sensor dropouts and must not be averaged in.
    """
    temps = []
    for r in readings:
        v = r.get("temp")
        if v is None:
            continue
        try:
            t = float(v)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(t):
            continue
        temps.append(t)
    if not temps:
        return None
    return sum(temps) / len(temps)


def parse(line):
    """Parse one reading line into a dict, or None if malformed."""
    line = line.strip()
    if not line:
        return None
    parts = line.split()
    if len(parts) < 2:
        return None
    out = {"time": parts[0]}
    for kv in parts[1:]:
        if "=" not in kv:
            continue
        k, v = kv.split("=", 1)
        out[k] = v
    return out


def read_log(path):
    """Read a log file into a list of reading dicts."""
    with open(path) as f:
        return [r for r in (parse(line) for line in f) if r is not None]
