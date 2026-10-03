import unittest
from dedupe import dedupe

class TestDedupe(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(dedupe([1, 2, 3, 2, 1]), [1, 2, 3])

    def test_preserve_order(self):
        self.assertEqual(dedupe([3, 1, 2, 1, 3]), [3, 1, 2])

    def test_unhashable(self):
        self.assertEqual(dedupe([[1], [2], [1]]), [[1], [2]])

if __name__ == "__main__":
    unittest.main()
