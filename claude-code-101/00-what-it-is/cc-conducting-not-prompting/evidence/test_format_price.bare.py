import unittest

from format_price import format_price


class FormatPriceTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(format_price(0), "$0.00")

    def test_single_cent(self):
        self.assertEqual(format_price(1), "$0.01")

    def test_under_a_dollar(self):
        self.assertEqual(format_price(9), "$0.09")
        self.assertEqual(format_price(99), "$0.99")

    def test_whole_dollar(self):
        self.assertEqual(format_price(100), "$1.00")

    def test_dollars_and_cents(self):
        self.assertEqual(format_price(1234), "$12.34")

    def test_thousands_separator(self):
        self.assertEqual(format_price(123456), "$1,234.56")
        self.assertEqual(format_price(100000000), "$1,000,000.00")

    def test_negative_amount(self):
        self.assertEqual(format_price(-1), "-$0.01")
        self.assertEqual(format_price(-1234), "-$12.34")
        self.assertEqual(format_price(-123456), "-$1,234.56")

    def test_rejects_float(self):
        with self.assertRaises(TypeError):
            format_price(1.5)

    def test_rejects_string(self):
        with self.assertRaises(TypeError):
            format_price("100")

    def test_rejects_bool(self):
        with self.assertRaises(TypeError):
            format_price(True)


if __name__ == "__main__":
    unittest.main()
