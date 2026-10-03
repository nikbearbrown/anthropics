import unittest

from todos import Todo, filter_todos, mark_all_done


class FilterTodosTests(unittest.TestCase):
    def test_keeps_matching_items(self):
        todos = [
            Todo("buy milk", False),
            Todo("write report", True),
            Todo("call mom", False),
        ]
        result = filter_todos(todos, lambda t: not t.done)
        self.assertEqual(result, [Todo("buy milk", False), Todo("call mom", False)])

    def test_returns_empty_when_nothing_matches(self):
        todos = [Todo("a", True), Todo("b", True)]
        self.assertEqual(filter_todos(todos, lambda t: not t.done), [])

    def test_returns_all_when_predicate_always_true(self):
        todos = [Todo("a", False), Todo("b", True)]
        self.assertEqual(filter_todos(todos, lambda t: True), todos)

    def test_original_list_unchanged(self):
        todos = [Todo("a", False), Todo("b", True), Todo("c", False)]
        snapshot = [Todo(t.text, t.done) for t in todos]
        filter_todos(todos, lambda t: t.done)
        self.assertEqual(todos, snapshot)

    def test_returns_new_list_object(self):
        todos = [Todo("a", False)]
        result = filter_todos(todos, lambda t: True)
        self.assertIsNot(result, todos)


class MarkAllDoneTests(unittest.TestCase):
    def test_all_items_marked_done(self):
        todos = [Todo("a", False), Todo("b", True), Todo("c", False)]
        result = mark_all_done(todos)
        self.assertEqual(result, [Todo("a", True), Todo("b", True), Todo("c", True)])

    def test_empty_list(self):
        self.assertEqual(mark_all_done([]), [])

    def test_original_list_unchanged(self):
        todos = [Todo("a", False), Todo("b", False)]
        snapshot = [Todo(t.text, t.done) for t in todos]
        mark_all_done(todos)
        self.assertEqual(todos, snapshot)

    def test_original_items_unchanged(self):
        todos = [Todo("a", False), Todo("b", False)]
        mark_all_done(todos)
        for t in todos:
            self.assertFalse(t.done)

    def test_returns_new_list_object(self):
        todos = [Todo("a", False)]
        result = mark_all_done(todos)
        self.assertIsNot(result, todos)
        self.assertIsNot(result[0], todos[0])


if __name__ == "__main__":
    unittest.main()
