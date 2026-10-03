from dataclasses import dataclass, replace


@dataclass
class Todo:
    text: str
    done: bool


def remove_completed(todos, keep=None):
    if keep is None:
        keep = lambda t: not t.done
    return [t for t in todos if keep(t)]


def mark_all_done(todos):
    return [replace(t, done=True) for t in todos]
