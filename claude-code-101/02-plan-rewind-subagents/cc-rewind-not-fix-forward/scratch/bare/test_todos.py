import copy
import unittest

from todos import Todo, mark_all_done, remove_completed


class RemoveCompletedTests(unittest.TestCase):
    def test_drops_done_items(self):
        todos = [
            Todo(text="a", done=False),
            Todo(text="b", done=True),
            Todo(text="c", done=False),
        ]
        self.assertEqual(
            remove_completed(todos),
            [Todo(text="a", done=False), Todo(text="c", done=False)],
        )

    def test_empty_list(self):
        self.assertEqual(remove_completed([]), [])

    def test_all_done(self):
        todos = [Todo(text="a", done=True), Todo(text="b", done=True)]
        self.assertEqual(remove_completed(todos), [])

    def test_none_done(self):
        todos = [Todo(text="a", done=False), Todo(text="b", done=False)]
        self.assertEqual(remove_completed(todos), todos)

    def test_does_not_mutate_input(self):
        todos = [Todo(text="a", done=False), Todo(text="b", done=True)]
        before = copy.deepcopy(todos)
        remove_completed(todos)
        self.assertEqual(todos, before)

    def test_custom_keep_predicate(self):
        todos = [
            Todo(text="a", done=False),
            Todo(text="bb", done=False),
            Todo(text="ccc", done=True),
        ]
        self.assertEqual(
            remove_completed(todos, keep=lambda t: len(t.text) > 1),
            [Todo(text="bb", done=False), Todo(text="ccc", done=True)],
        )


class MarkAllDoneTests(unittest.TestCase):
    def test_marks_every_item_done(self):
        todos = [Todo(text="a", done=False), Todo(text="b", done=True)]
        self.assertEqual(
            mark_all_done(todos),
            [Todo(text="a", done=True), Todo(text="b", done=True)],
        )

    def test_empty_list(self):
        self.assertEqual(mark_all_done([]), [])

    def test_does_not_mutate_input(self):
        todos = [Todo(text="a", done=False), Todo(text="b", done=False)]
        before = copy.deepcopy(todos)
        mark_all_done(todos)
        self.assertEqual(todos, before)


if __name__ == "__main__":
    unittest.main()
