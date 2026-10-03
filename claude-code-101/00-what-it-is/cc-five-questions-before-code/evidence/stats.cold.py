"""stats.py — study-readings tiny stats module.

Reading log format (one per line):
    HH:MM  temp=<float>  humid=<int>

Example:
    09:00  temp=20.4  humid=45
"""

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


def avg_temp(readings):
    """Return the average 'temp' across readings.

    Accepts the list-of-dicts shape produced by parse()/read_log().
    Readings missing a 'temp' key or with a non-float value are skipped.
    Raises ValueError if no readings contribute a valid temperature.
    """
    total = 0.0
    n = 0
    for r in readings:
        v = r.get("temp")
        if v is None:
            continue
        try:
            total += float(v)
        except (TypeError, ValueError):
            continue
        n += 1
    if n == 0:
        raise ValueError("no readings with a valid 'temp' field")
    return total / n
