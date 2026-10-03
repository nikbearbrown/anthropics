import unittest
from calc import add, sub, mul


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negatives(self):
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, -3), -5)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(mul(4, 3), 12)


if __name__ == "__main__":
    unittest.main()
