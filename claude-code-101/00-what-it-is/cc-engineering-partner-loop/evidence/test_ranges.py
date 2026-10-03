import unittest
from ranges import parse_range


class TestParseRange(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(parse_range("7"), (7, 7))

    def test_range(self):
        self.assertEqual(parse_range("1-5"), (1, 5))

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            parse_range("")

    def test_reversed_raises(self):
        with self.assertRaises(ValueError):
            parse_range("5-1")

    def test_extra_dash_raises(self):
        with self.assertRaises(ValueError):
            parse_range("1-2-3")


if __name__ == "__main__":
    unittest.main()
