"""audit — append-only log of every change to grades.json."""
from datetime import datetime
from pathlib import Path

LOG = Path("audit.log")


def audit(name, action):
    with LOG.open("a") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} {action} {name}\n")
