from dataclasses import dataclass, replace
from typing import Callable, List


@dataclass
class Todo:
    text: str
    done: bool


def filter_todos(todos: List[Todo], keep: Callable[[Todo], bool]) -> List[Todo]:
    return [t for t in todos if keep(t)]


def mark_all_done(todos: List[Todo]) -> List[Todo]:
    return [replace(t, done=True) for t in todos]
