import unittest

from format_price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_1299(self):
        self.assertEqual(format_price(1299), "12.99 EUR")

    def test_zero(self):
        self.assertEqual(format_price(0), "0.00 EUR")

    def test_10000(self):
        self.assertEqual(format_price(10000), "100.00 EUR")

    def test_12345(self):
        self.assertEqual(format_price(12345), "123.45 EUR")

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            format_price(-50)


if __name__ == "__main__":
    unittest.main()
